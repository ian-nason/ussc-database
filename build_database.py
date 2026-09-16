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
    "drugs": {"DAFROM", "DATO", "DESCRIP", "CDESCRIP", "DRGAM", "DRUGTYP", "DUFROM", "DUTO", "MWGT", "UNIT", "WGT"},
    # FY2002-03 (pre-Booker) departure reasons are REASON/REASTXT; FY2004+ are REAS/RETEXT.
    # Both live in departure_reasons under the Commission's own names (the other pair is NULL).
    "departure_reasons": {"REAS", "RETEXT", "REASON", "REASTXT"},
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
    "departure_reasons": "One row per stated reason for departure/variance: REAS code + RETEXT text (FY2004+, post-Booker coding) or REASON + REASTXT (FY2002-03, pre-Booker coding)",
    "pleas": "One row per plea/verdict slot (INPLEA, INNOPL)",
    "chapter_text": "Free-text chapter 2/3/4 guideline notes (CHP2TXT/CHP3TXT/CHP4TXT) and change flags",
    "new_statutes": "Statutes of conviction as recorded in NWSTAT slots",
    "offense_dates": "Offense begin/end dates per slot (OFBEG/OFEND; FY2002-era files only)",
    "v_sentence_terms": "View over sentences: prison_months (TOTPRISN with the special codes >= 9990 removed) and term_type (months / no prison / life / death / prison with no term stated / under one day / missing)",
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
    """Extract the .dat and make it pure ASCII without moving any column. Positions in the SAS
    layout are byte offsets, and some years (FY2006, FY2017) carry stray cp1252 bytes (curly
    quotes) in free text. Each such byte becomes one '?', so character positions still equal
    the layout's byte positions -- and DuckDB's substr() stays O(1) per call, which it is
    only for ASCII strings (measured 300x slower on lines with a multibyte character)."""
    dat = RAW / dat_member(yy)
    if not dat.exists():
        print(f"  extracting {dat.name}")
        with zipfile.ZipFile(RAW / f"opafy{yy:02d}nid.zip") as z:
            z.extract(dat_member(yy), RAW)
    marker = dat.with_suffix(".dat.transcoded")
    if marker.exists():  # already rewritten by an earlier run; scanning again would double-encode
        return dat
    non_ascii = False
    with open(dat, "rb") as src:
        while chunk := src.read(1 << 24):
            if not chunk.isascii():
                non_ascii = True
                break
    if non_ascii:
        print(f"  {dat.name}: non-ASCII bytes present, replacing each with '?' (one byte per character)")
        tmp = dat.with_suffix(".dat.ascii")
        table = bytes(b if b < 128 else ord("?") for b in range(256))
        with open(dat, "rb") as src, open(tmp, "wb") as out:
            while chunk := src.read(1 << 24):
                out.write(chunk.translate(table))
        tmp.replace(dat)
        marker.touch()
    return dat


SLOT_BATCH = 8  # slots unpivoted per query; the full UNION of ~130 slots blew past the memory cap


def cell_sql(raw: str, is_char: bool, name: str) -> str:
    """Blank and SAS's missing marker '.' are both NULL. Character fields carry '.' too (e.g.
    FY2004 BASECL in every unused guideline slot), so it is stripped before the empty-slot test."""
    expr = f"NULLIF(NULLIF(TRIM({raw}), ''), '.')"
    if not is_char:
        expr = f"TRY_CAST({expr} AS DOUBLE)"
    return f'{expr} AS "{name}"'


def field_sql(name: str, is_char: bool, a: int, b: int) -> str:
    return cell_sql(f"substr(line, {a}, {b - a + 1})", is_char, name)


def block_plan(fams: dict[str, dict[int, tuple]]):
    """Lay a group's cells (family-major, slot ascending) end to end in a compact block string.
    Returns (concat SQL over the line, {(family, slot): (offset, width, is_char)}, dim, families).
    Adjacent cells are merged into one substr() run; a family is normally one run."""
    cells, runs, off = {}, [], 1
    run_a = run_b = None
    for f in sorted(fams):
        for i in sorted(fams[f]):
            _, is_char, a, b = fams[f][i]
            cells[(f, i)] = (off, b - a + 1, is_char)
            off += b - a + 1
            if run_b is not None and a == run_b + 1:
                run_b = b
            else:
                if run_a is not None:
                    runs.append((run_a, run_b))
                run_a, run_b = a, b
    runs.append((run_a, run_b))
    concat = "concat(" + ", ".join(f"substr(line, {a}, {b - a + 1})" for a, b in runs) + ")"
    return concat, cells, max(max(idx) for idx in fams.values()), sorted(fams)


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
    # Line endings differ by year (CRLF in FY2002-03 and FY2016, LF elsewhere); the sniffer
    # cannot cope with an 18-100k character single-column line, so everything is explicit
    with open(dat, "rb") as fh:
        nl = "\\r\\n" if b"\r\n" in fh.read(65536) else "\\n"
    con.execute(f"""
        CREATE TABLE stage._lines AS
        SELECT line
        FROM read_csv('{dat}', delim='\\x01', quote='', escape='', header=false, columns={{'line': 'VARCHAR'}},
                      auto_detect=false, new_line='{nl}', max_line_size={lrecl + 100})
    """)
    n, short = con.execute(f"SELECT COUNT(*), COUNT(*) FILTER (WHERE length(line) < {lrecl}) FROM stage._lines").fetchone()
    if short:
        print(f"    WARNING FY{fiscal_year}: {short:,} of {n:,} lines shorter than the layout ({lrecl} chars); trailing fields read as NULL")
        if short > n * 0.001:
            raise RuntimeError(f"FY{fiscal_year}: {short:,} short lines -- layout/file mismatch")
    counts = {}
    # scalars -> sentences
    sel = ", ".join(field_sql(*s) for s in scalars)
    con.execute(f"CREATE TABLE stage._y_sentences AS SELECT {fiscal_year} AS fiscal_year, {sel} FROM stage._lines")
    counts["sentences"] = n
    # arrays -> long tables by group. One pass cuts every group's cells out of the 20-100k
    # character line into its own compact block column; the per-slot unpivot then scans only
    # that block instead of re-reading the whole line for each of ~130 slots.
    groups: dict[str, dict[str, dict[int, tuple]]] = defaultdict(dict)
    for f, idx in families.items():
        tname = next((g for g, names in NAME_GROUPS.items() if f in names), "guidelines")
        groups[tname][f] = idx
    idn = next((s for s in scalars if s[0] == "USSCIDN"), None)
    if idn is None:
        raise RuntimeError(f"FY{fiscal_year}: no USSCIDN in layout")
    plans = {t: block_plan(fams) for t, fams in groups.items()}
    con.execute(f"CREATE TABLE stage._blocks AS SELECT {field_sql(*idn)}, "
                + ", ".join(f'{concat} AS "{t}"' for t, (concat, *_rest) in plans.items())
                + " FROM stage._lines")
    con.execute("DROP TABLE stage._lines")
    for tname, (_concat, cells, dim, fam_names) in plans.items():
        selects = []
        for i in range(1, dim + 1):
            cols, present = [], []
            for f in fam_names:
                c = cells.get((f, i))
                if c:
                    off, w, is_char = c
                    cols.append(cell_sql(f'substr("{tname}", {off}, {w})', is_char, f)); present.append(f)
                else:
                    cols.append(f'NULL AS "{f}"')
            if not present:
                continue
            nonnull = " OR ".join(f'"{f}" IS NOT NULL' for f in present)
            selects.append(f"SELECT * FROM (SELECT {fiscal_year} AS fiscal_year, USSCIDN, {i} AS seq, {', '.join(cols)} "
                           f"FROM stage._blocks) WHERE {nonnull}")
        if not selects:
            print(f"    {tname}: no populated slots in FY{fiscal_year}")
            continue
        for k in range(0, len(selects), SLOT_BATCH):
            sql = " UNION ALL ".join(selects[k:k + SLOT_BATCH])
            if k == 0:
                con.execute(f"CREATE TABLE stage._y_{tname} AS {sql}")
            else:
                con.execute(f"INSERT INTO stage._y_{tname} {sql}")
        counts[tname] = con.execute(f"SELECT COUNT(*) FROM stage._y_{tname}").fetchone()[0]
    con.execute("DROP TABLE stage._blocks")
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
    dat.with_suffix(".dat.transcoded").unlink(missing_ok=True)
    return counts


def run_validation(con, n_years: int) -> int:
    ck = Checker("Validation")
    ck.query(con, "sentences per year >= 55k every year", "SELECT MIN(n) FROM (SELECT fiscal_year, COUNT(*) AS n FROM sentences GROUP BY 1)",
             lambda n: n >= 55000, lambda n: f"min {n:,}")
    ck.query(con, f"{n_years} fiscal years present", "SELECT COUNT(DISTINCT fiscal_year) FROM sentences", lambda n: n == n_years, str)
    # The FY2010 file carries one record twice (USSCIDN 1325685, byte-identical); it is kept as
    # published. Any other duplicate id is a build error.
    ck.query(con, "USSCIDN unique within year (except the known FY2010 duplicate)",
             "SELECT COUNT(*) FROM (SELECT fiscal_year, USSCIDN FROM sentences GROUP BY 1, 2 HAVING COUNT(*) > 1) "
             "WHERE NOT (fiscal_year = 2010 AND USSCIDN = 1325685)", lambda n: n == 0, str)
    # SENTTOT is NULL by design for probation-only and zero-month sentences (codebook); TOTPRISN
    # carries 0 for those, so it is the coverage check.
    ck.query(con, "TOTPRISN populated (> 98%)", "SELECT COUNT(TOTPRISN) * 1.0 / COUNT(*) FROM sentences", lambda v: v > 0.98, lambda v: f"{v:.1%}")
    # 9 rows carry 9990 (FY2002-07) or an out-of-range total (11520, 19080); they surface as
    # term_type = 'other special code' rather than being averaged as months
    ck.query(con, "TOTPRISN values >= 9990 outside the codebook's 9992/9996/9997/9998 stay a handful (<= 20)",
             "SELECT COUNT(*) FROM sentences WHERE TOTPRISN >= 9990 AND TOTPRISN NOT IN (9992, 9996, 9997, 9998)", lambda n: n <= 20, str)
    ck.query(con, "v_sentence_terms: prison_months never carries a special code", "SELECT COALESCE(MAX(prison_months), 0) FROM v_sentence_terms", lambda v: v < 9990, str)
    ck.query(con, "v_sentence_terms: 'other special code' rows stay a handful (<= 20)", "SELECT COUNT(*) FROM v_sentence_terms WHERE term_type = 'other special code'", lambda n: n <= 20, str)
    ck.query(con, "SENTTOT populated (> 80%; NULL = probation/zero months)", "SELECT COUNT(SENTTOT) * 1.0 / COUNT(*) FROM sentences", lambda v: v > 0.8, lambda v: f"{v:.1%}")
    ck.query(con, "counts rows >= sentences rows", "SELECT (SELECT COUNT(*) FROM counts) >= (SELECT COUNT(*) FROM sentences)", lambda v: v, str)
    ck.query(con, "defendants with a guideline computation >= 80% every year",
             "SELECT MIN(share) FROM (SELECT s.fiscal_year, COUNT(DISTINCT g.USSCIDN) * 1.0 / COUNT(DISTINCT s.USSCIDN) AS share "
             "FROM sentences s LEFT JOIN guidelines g USING (fiscal_year, USSCIDN) GROUP BY 1)", lambda v: v >= 0.8, lambda v: f"min {v:.1%}")
    ck.query(con, "every long table joins to a sentence",
             "SELECT " + " + ".join(f"(SELECT COUNT(*) FROM {t} x LEFT JOIN sentences s USING (fiscal_year, USSCIDN) WHERE s.USSCIDN IS NULL)"
                                    for t in ("guidelines", "drugs", "departure_reasons", "pleas", "chapter_text", "new_statutes", "offense_dates")),
             lambda n: n == 0, str)
    ck.query(con, "every counts row joins to a sentence",
             "SELECT COUNT(*) FROM counts c LEFT JOIN sentences s USING (fiscal_year, USSCIDN) WHERE s.USSCIDN IS NULL", lambda n: n == 0, str)
    return ck.report()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    ap.add_argument("--years", nargs="+", type=int, default=YEARS)
    ap.add_argument("--finalize-only", action="store_true",
                    help="skip loading; rebuild _metadata/_columns/DICTIONARY.md and validate an existing output file")
    a = ap.parse_args()
    t0 = time.time()
    con = connect(a.output, fresh=not a.finalize_only, memory_limit="3GB", threads=1)
    totals: dict[str, int] = defaultdict(int)
    if a.finalize_only:
        base_tables = [r[0] for r in con.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'main' AND table_type = 'BASE TABLE' ORDER BY 1").fetchall()]
        for t in base_tables:
            if not t.startswith("_"):
                totals[t] = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        a.years = [r[0] for r in con.execute("SELECT DISTINCT fiscal_year FROM sentences ORDER BY 1").fetchall()]
    for fy in ([] if a.finalize_only else a.years):
        t1 = time.time()
        c = load_year(con, fy % 100, fy, a.output)
        for k, v in c.items():
            totals[k] += v
        print(f"  FY{fy}: " + ", ".join(f"{k} {v:,}" for k, v in c.items()) + f"  ({time.time() - t1:.0f}s)")
    # TOTPRISN carries the Commission's special codes above 9990 (see the codebook): 9992
    # under one day, 9996 life, 9997 prison with no term stated, 9998 death. They are
    # categories, not months; the view separates them so averages use real month counts.
    con.execute("""
        CREATE OR REPLACE VIEW v_sentence_terms AS
        SELECT fiscal_year, USSCIDN,
               CASE WHEN TOTPRISN IS NULL THEN NULL WHEN TOTPRISN < 9990 THEN TOTPRISN END AS prison_months,
               CASE WHEN TOTPRISN IS NULL THEN 'missing'
                    WHEN TOTPRISN = 0 THEN 'no prison'
                    WHEN TOTPRISN < 9990 THEN 'months'
                    WHEN TOTPRISN = 9992 THEN 'less than one day'
                    WHEN TOTPRISN = 9996 THEN 'life'
                    WHEN TOTPRISN = 9997 THEN 'prison, no term stated'
                    WHEN TOTPRISN = 9998 THEN 'death'
                    ELSE 'other special code' END AS term_type,
               TOTPRISN, SENTTOT, SENTIMP, PRISDUM
        FROM sentences""")
    documented = list(totals) + ["v_sentence_terms"]  # the view is in the dictionary, not in the row totals
    print("\nMetadata + dictionary")
    ensure_metadata(con, descriptions=TABLE_DESCRIPTIONS, tables=list(totals),
                    source_url="https://www.ussc.gov/research/datafiles/commission-datafiles", license="Public domain", replace=True)
    build_columns_table(con, join_hints=JOIN_HINTS, tables=documented)
    export_dictionary(con, Path("DICTIONARY.md"), title="ussc Data Dictionary",
                      intro=["Source: [U.S. Sentencing Commission individual offender datafiles](https://www.ussc.gov/research/datafiles/commission-datafiles), FY2002-FY2025.",
                             "Variable names are the Commission's; definitions and code values are in `docs/USSC_Public_Release_Codebook_FY99_FY25.pdf`.",
                             "Array variables (per count, per guideline, per drug ...) are unpivoted into the long tables keyed by (fiscal_year, USSCIDN, seq)."],
                      style="registry", tables=documented)
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
