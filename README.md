# U.S. Sentencing Commission individual offender datafiles as a DuckDB database

Every federal defendant sentenced from FY2002 through FY2025, from the
[U.S. Sentencing Commission's public datafiles](https://www.ussc.gov/research/datafiles/commission-datafiles)
(the "individual offender" files without identifiers), reshaped into a queryable DuckDB file.

## Why the reshaping

The Commission publishes one fixed-width file per fiscal year with ~22,000 variables,
because every repeating item is stored as a numbered slot: `TTSC1_1 ... TTSC1_111` for the
statute of each count of conviction, `ADJ_B1 ... ADJ_B66` for each guideline computation,
and so on. Loading that as one wide table would give a 22,000-column table that is
mostly empty. Instead:

| Table | One row per | Contents |
|-------|-------------|----------|
| `sentences` | sentenced defendant | every scalar variable (demographics, offense, guideline range, sentence, departures) |
| `counts` | count of conviction | statute title/section/subsection (`TTSC1`-`TTSC3`), statutory min/max (`SMIN`/`SMAX`), `STA1`-`STA3` |
| `guidelines` | guideline computation | base offense level, specific offense characteristics, Chapter 3 adjustments (`ADJ_*`, `BASE`, `ADJOFL`, ...) |
| `drugs` | drug type on the case | `DRUGTYP`, `WGT`, `UNIT`, `MWGT`, `DRGAM`, dates |
| `departure_reasons` | stated departure reason | `REAS` code, `RETEXT` text |
| `pleas` | plea/verdict slot | `INPLEA`, `INNOPL` |
| `chapter_text` | free-text guideline note | `CHP2TXT`/`CHP3TXT`/`CHP4TXT` and change flags |
| `new_statutes` | `NWSTAT` slot | statutes of conviction |
| `offense_dates` | slot | `OFBEG`/`OFEND` (FY2002-era files only) |

Every long table is keyed by (`fiscal_year`, `USSCIDN`, `seq`); empty slots are not stored.
Variable names are the Commission's; definitions and code values are in
`docs/USSC_Public_Release_Codebook_FY99_FY25.pdf`. Numeric variables are `DOUBLE`
(the Commission's blank = missing), character variables are `VARCHAR`.

## Quick start

```python
import datapond
con = datapond.connect("ussc")
con.sql("""
    SELECT fiscal_year, COUNT(*) AS defendants, ROUND(AVG(SENTTOT), 1) AS avg_months
    FROM sentences GROUP BY 1 ORDER BY 1
""").show()
```

## Researcher caveats

- **Variables come and go across fiscal years.** The Commission adds, renames and retires
  variables; a column that is NULL for a whole fiscal year was not collected that year.
  `_columns.null_pct` and the codebook's "AMENDYR"/"applies only to" notes explain most gaps.
- **`SENTTOT` is total prison months** with the Commission's conventions (e.g. 9996 = life,
  probation-only = 0); see the codebook before averaging.
- Slot arrays widen over time (counts of conviction: 266 slots in FY2002, 884 in FY2018,
  111 in FY2025); `seq` is the slot index and is not meaningful across years beyond ordering.
- The files exclude identifiers; `USSCIDN` is unique within a fiscal year only.
- FY1999-FY2001 files exist only at ICPSR under terms that do not allow redistribution.

## Build

```bash
uv sync
./download_datafiles.sh          # 24 zips, ~700 MB
uv run python build_database.py  # one fiscal year at a time; DuckDB capped at 4 GB
uv run python publish_to_hf.py --token hf_xxx --verify
```

## License

Code: MIT. Data: public domain (U.S. federal government).
