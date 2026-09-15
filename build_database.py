#!/usr/bin/env python3
"""Build ussc.duckdb from the U.S. Sentencing Commission's individual offender datafiles.

Source: https://www.ussc.gov/research/datafiles/commission-datafiles
    data/raw/opafyYYnid.zip  (FY2002-FY2025), each holding a fixed-width .dat plus the
    SAS (.sas) and SPSS (.sps) syntax that defines every column's position.

The public file has ~22,000 variables per year, almost all of them repeated
arrays (one slot per count of conviction, per guideline computation, per drug
type, ...). We keep the scalar variables as one wide table and unpivot each
array family into a long table keyed by (USSCIDN, fiscal_year, seq), dropping
empty slots:

    sentences              one row per sentenced defendant; all scalar variables (~500)
    counts                 one row per count of conviction: TTSC1-3 (statute title/section/sub), STA1-3, SMIN, SMAX
    guidelines             one row per guideline computation (ADJ_*, BASE, ..., 310 families)
    drugs                  one row per drug type on the case
    departure_reasons      REAS / RETEXT
    pleas                  INNOPL / INPLEA
    chapter_text           CHP2TXT/CHP3TXT/CHP4TXT + *CHG
    new_statutes           NWSTAT

Column names are the USSC's own (see docs/ codebook). Numeric variables are DOUBLE
(blank = NULL); character variables are VARCHAR (blank = NULL).

Usage:
    uv run python build_database.py [--years 2024 2025] [--output ussc.duckdb]
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import zipfile
from collections import defaultdict
from pathlib import Path

import duckdb

from datapond_build import Checker, build_columns_table, ensure_metadata, export_dictionary
from datapond_build.session import connect

RAW = Path("data/raw")
DEFAULT_OUTPUT = "ussc.duckdb"
YEARS = list(range(2002, 2026))

# Array families -> long table. Widths differ by year (counts of conviction have
# 266 slots in FY2002, 884 in FY2018, 111 in FY2025), so grouping is by name.
NAME_GROUPS = {
    "counts": {"TTSC1", "TTSC2", "TTSC3", "SMIN", "SMAX", "STA1", "STA2", "STA3"},
    "drugs": {"DAFROM", "DATO", "DESCRIP", "DRGAM", "DRUGTYP", "DUFROM", "DUTO", "MWGT", "UNIT", "WGT"},
    "departure_reasons": {"REAS", "RETEXT"},
    "pleas": {"INNOPL", "INPLEA"},
    "chapter_text": {"CHP2CHG", "CHP2TXT", "CHP3CHG", "CHP3TXT", "CHP4CHG", "CHP4TXT"},
    "new_statutes": {"NWSTAT"},
    "offense_dates": {"OFBEG", "OFEND"},
}
# Everything else (ABUS, ADJ_*, BASE, ... : one slot per guideline computation) -> guidelines.

TABLE_DESCRIPTIONS = {
    "sentences": "One row per federal defendant sentenced in the fiscal year: demographics, offense, guideline range, sentence imposed, departures (scalar variables of the USSC individual offender datafile)",
    "counts": "One row per count of conviction: statute (TTSC1/TTSC2/TTSC3 = title/section/subsection), statutory minimum/maximum (SMIN/SMAX) and STA1-3",
    "guidelines": "One row per guideline computation on the case: base offense level, specific offense characteristics and Chapter 3 adjustments (ADJ_*), per-guideline totals",
    "drugs": "One row per drug type involved: type, weight, units, equivalency (DRUGTYP, WGT, UNIT, MWGT, DRGAM, ...)",
    "departure_reasons": "One row per stated reason for departure/variance (REAS code, RETEXT text)",
    "pleas": "One row per plea/verdict slot (INPLEA, INNOPL)",
    "chapter_text": "Free-text chapter 2/3/4 guideline notes (CHP2TXT/CHP3TXT/CHP4TXT) and change flags",
    "new_statutes": "Statutes of conviction as recorded in NWSTAT slots",
    "offense_dates": "Offense begin/end dates per slot (OFBEG/OFEND; FY2002-era files only)",
}

JOIN_HINTS = {
    "USSCIDN": "USSC case identifier; joins every table",
    "fiscal_year": "Fiscal year of sentencing (from the datafile); joins every table",
    "seq": "Slot index within the array (1 = first count / guideline / drug ...)",
    "CIRCDIST": "Circuit-district code of the sentencing court (USSC coding; codebook table)",
    "DISTRICT": "District code",
    "MONCIRC": "Circuit",
}


def parse_layout(yy: int) -> list[tuple[str, bool, int, int]]:
    """(name, is_char, start, end) from the SAS INPUT statement (1-based inclusive positions)."""
    with zipfile.ZipFile(RAW / f"opafy{yy:02d}nid.zip") as z:
        sas = z.read(f"opafy{yy:02d}nid.sas").decode("latin-1")
    body = re.search(r"INPUT\s*(.*?);", sas, re.S).group(1)
    out = []
    for name, dollar, a, b in re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*(\$?)\s*(\d+)(?:-(\d+))?", body):
        out.append((name.upper(), dollar == "$", int(a), int(b) if b else int(a)))
    return out


ARRAY_FAMILIES: set[str] | None = None


def raw_families(layout) -> dict[str, dict[int, tuple]]:
    """family -> {index: (name, is_char, a, b)} for every numbered name (TTSC1_12 -> TTSC1; BASE7 -> BASE)."""
    fam: dict[str, dict[int, tuple]] = defaultdict(dict)
    for name, is_char, a, b in layout:
        m = re.match(r"^(.*?)_?(\d+)$", name)
        if m:
            fam[m.group(1)][int(m.group(2))] = (name, is_char, a, b)
    return fam


def array_families() -> set[str]:
    """Which numbered families are repeating arrays (reshaped long) rather than a handful of
    distinct numbered scalars (POINT1-3, MAND1-6, CAFROM1/2 ... stay wide in `sentences`).
    A family is an array if, in ANY available fiscal year's layout, it has >= 10 slots, uses the
    NAME_n underscore form (TTSC1_1, ADJ_B1), or is listed in NAME_GROUPS. Decided once over every
    zip in data/raw so the schema is the same whichever --years are built."""
    global ARRAY_FAMILIES
    if ARRAY_FAMILIES is None:
        named = {n for names in NAME_GROUPS.values() for n in names}
        arr: set[str] = set()
        for z in sorted(RAW.glob("opafy??nid.zip")):
            if not zipfile.is_zipfile(z):
                continue
            yy = int(z.name[5:7])
            for f, idx in raw_families(parse_layout(yy)).items():
                if len(idx) < 2:
                    continue
                if f in named or max(idx) >= 10 or any(v[0] != f"{f}{i}" for i, v in idx.items()):
                    arr.add(f)
        ARRAY_FAMILIES = arr
    return ARRAY_FAMILIES


def split_families(layout):
    """Return (scalars, families) where families maps array family -> {index: (name, is_char, a, b)}."""
    arr = array_families()
    families = {f: idx for f, idx in raw_families(layout).items() if f in arr and len(idx) > 1}
    array_names = {v[0] for idx in families.values() for v in idx.values()}
    scalars = [(n, c, a, b) for n, c, a, b in layout if n not in array_names]
    return scalars, families


def dat_member(yy: int) -> str:
    return f"opafy{yy:02d}nid.dat"


def ensure_extracted(yy: int) -> Path:
    dat = RAW / dat_member(yy)
    if not dat.exists():
        print(f"  extracting {dat.name}")
        with zipfile.ZipFile(RAW / f"opafy{yy:02d}nid.zip") as z:
            z.extract(dat_member(yy), RAW)
    return dat


def field_sql(name: str, is_char: bool, a: int, b: int) -> str:
    raw = f"substr(line, {a}, {b - a + 1})"
    if is_char:
        return f"NULLIF(TRIM({raw}), '') AS \"{name}\""
    return f"TRY_CAST(NULLIF(TRIM({raw}), '') AS DOUBLE) AS \"{name}\""


def fresh_stage(con, output: Path) -> Path:
    """(Re)create the scratch database that holds one fiscal year's staging tables. DuckDB
    never returns freed blocks, so staging inside the output file inflated it ~30x."""
    stage = output.with_suffix(".stage.duckdb")
    try:
        con.execute("DETACH stage")
    except Exception:
        pass
    for f in (stage, stage.with_suffix(".duckdb.wal")):
        if f.exists():
            f.unlink()
    con.execute(f"ATTACH '{stage}' AS stage")
    return stage


def load_year(con, yy: int, fiscal_year: int, output: Path) -> dict[str, int]:
    dat = ensure_extracted(yy)
    layout = parse_layout(yy)
    scalars, families = split_families(layout)
    lrecl = max(b for _, _, _, b in layout)
    fresh_stage(con, output)
    con.execute(f"""
        CREATE TABLE stage._lines AS
        SELECT line, row_number() OVER () AS _row
        FROM read_csv('{dat}', delim='\\x01', quote='', escape='', header=false, columns={{'line': 'VARCHAR'}},
                      new_line='\\n', max_line_size={lrecl + 100})
    """)
    n = con.execute("SELECT COUNT(*) FROM stage._lines").fetchone()[0]
    counts = {}
    # scalars -> sentences_<yy>
    sel = ", ".join(field_sql(*s) for s in scalars)
    con.execute(f"CREATE TABLE stage._y_sentences AS SELECT {fiscal_year} AS fiscal_year, {sel} FROM stage._lines")
    counts["sentences"] = n
    # arrays -> long tables by dimension
    groups: dict[str, dict[str, dict[int, tuple]]] = defaultdict(dict)
    for f, idx in families.items():
        tname = next((g for g, names in NAME_GROUPS.items() if f in names), "guidelines")
        groups[tname][f] = idx
    idn = next((s for s in scalars if s[0] == "USSCIDN"), None)
    if idn is None:
        raise RuntimeError(f"FY{fiscal_year}: no USSCIDN in layout")
    idn_sql = field_sql(*idn)
    for tname, fams in groups.items():
        dim = max(max(idx) for idx in fams.values())
        fam_names = sorted(fams)
        # One bounded query per slot index; a single UNION of all slots blew past the
        # memory cap (the planner materialises every branch at once).
        created = False
        for i in range(1, dim + 1):
            cols, present = [], []
            for f in fam_names:
                slot = fams[f].get(i)
                if slot:
                    cols.append(field_sql(f, slot[1], slot[2], slot[3])); present.append(f)
                else:
                    cols.append(f'NULL AS "{f}"')
            if not present:
                continue
            nonnull = " OR ".join(f'"{f}" IS NOT NULL' for f in present)
            sql = (f"SELECT * FROM (SELECT {fiscal_year} AS fiscal_year, {idn_sql}, {i} AS seq, {', '.join(cols)} "
                   f"FROM stage._lines) WHERE {nonnull}")
            if not created:
                con.execute(f"CREATE TABLE stage._y_{tname} AS {sql}")
                created = True
            else:
                con.execute(f"INSERT INTO stage._y_{tname} {sql}")
        if not created:
            print(f"    {tname}: no populated slots in FY{fiscal_year}")
            continue
        counts[tname] = con.execute(f"SELECT COUNT(*) FROM stage._y_{tname}").fetchone()[0]
    con.execute("DROP TABLE stage._lines")
    # append into the cumulative tables in the output database (union by name)
    for t in counts:
        exists = con.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_catalog = current_database() AND table_name = ?", [t]).fetchone()[0]
        if not exists:
            con.execute(f"CREATE TABLE {t} AS SELECT * FROM stage._y_{t}")
        else:
            have = {r[0] for r in con.execute(f"DESCRIBE {t}").fetchall()}
            for c, typ, *_ in con.execute(f"DESCRIBE stage._y_{t}").fetchall():
                if c not in have:
                    con.execute(f'ALTER TABLE {t} ADD COLUMN "{c}" {typ}')
            con.execute(f"INSERT INTO {t} BY NAME SELECT * FROM stage._y_{t}")
        con.execute(f"DROP TABLE stage._y_{t}")
    con.execute("CHECKPOINT")
    dat.unlink()  # 2-4 GB each; the zip stays cached
    return counts


def run_validation(con, n_years: int) -> int:
    ck = Checker("Validation")
    ck.query(con, "sentences per year >= 55k every year", "SELECT MIN(n) FROM (SELECT fiscal_year, COUNT(*) AS n FROM sentences GROUP BY 1)",
             lambda n: n >= 55000, lambda n: f"min {n:,}")
    ck.query(con, f"{n_years} fiscal years present", "SELECT COUNT(DISTINCT fiscal_year) FROM sentences", lambda n: n == n_years, str)
    ck.query(con, "USSCIDN unique within year", "SELECT COUNT(*) - COUNT(DISTINCT (fiscal_year, USSCIDN)) FROM sentences", lambda n: n == 0, str)
    ck.query(con, "SENTTOT populated (> 90%)", "SELECT COUNT(SENTTOT) * 1.0 / COUNT(*) FROM sentences", lambda v: v > 0.9, lambda v: f"{v:.1%}")
    ck.query(con, "counts rows >= sentences rows", "SELECT (SELECT COUNT(*) FROM counts) >= (SELECT COUNT(*) FROM sentences)", lambda v: v, str)
    ck.query(con, "guidelines rows >= sentences rows", "SELECT (SELECT COUNT(*) FROM guidelines) >= (SELECT COUNT(*) FROM sentences)", lambda v: v, str)
    ck.query(con, "every counts row joins to a sentence",
             "SELECT COUNT(*) FROM counts c LEFT JOIN sentences s USING (fiscal_year, USSCIDN) WHERE s.USSCIDN IS NULL", lambda n: n == 0, str)
    return ck.report()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    ap.add_argument("--years", nargs="+", type=int, default=YEARS)
    a = ap.parse_args()
    t0 = time.time()
    con = connect(a.output, fresh=True, memory_limit="3GB", threads=1)
    totals: dict[str, int] = defaultdict(int)
    for fy in a.years:
        t1 = time.time()
        c = load_year(con, fy % 100, fy, a.output)
        for k, v in c.items():
            totals[k] += v
        print(f"  FY{fy}: " + ", ".join(f"{k} {v:,}" for k, v in c.items()) + f"  ({time.time() - t1:.0f}s)")
    print("\nMetadata + dictionary")
    ensure_metadata(con, descriptions=TABLE_DESCRIPTIONS, tables=list(totals),
                    source_url="https://www.ussc.gov/research/datafiles/commission-datafiles", license="Public domain", replace=True)
    build_columns_table(con, join_hints=JOIN_HINTS, tables=list(totals))
    export_dictionary(con, Path("DICTIONARY.md"), title="ussc Data Dictionary",
                      intro=["Source: [U.S. Sentencing Commission individual offender datafiles](https://www.ussc.gov/research/datafiles/commission-datafiles), FY2002-FY2025.",
                             "Variable names are the Commission's; definitions and code values are in `docs/USSC_Public_Release_Codebook_FY99_FY25.pdf`.",
                             "Array variables (per count, per guideline, per drug ...) are unpivoted into the long tables keyed by (fiscal_year, USSCIDN, seq)."],
                      style="registry", tables=list(totals))
    con.execute("CHECKPOINT")
    stage = fresh_stage(con, a.output)
    con.execute("DETACH stage"); stage.unlink()
    failures = run_validation(con, len(a.years))
    con.close()
    print(f"\nBUILD DONE in {(time.time() - t0) / 60:.1f} min; " + ", ".join(f"{k} {v:,}" for k, v in totals.items())
          + f"; {a.output.stat().st_size / 1024**3:.2f} GB")
    if failures:
        print(f"BUILD FAILED: {failures} check(s) failed -- do not publish this file")
        sys.exit(1)


if __name__ == "__main__":
    main()
