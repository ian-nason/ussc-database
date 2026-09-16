# U.S. Sentencing Commission individual offender datafiles as a DuckDB database

Every federal defendant sentenced from FY2002 through FY2025 (1,720,684 defendants, 14.0M rows), from the
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
| `drugs` | drug type on the case | `DRUGTYP`, `WGT`, `UNIT`, `MWGT`, `DRGAM`, `DESCRIP`, dates |
| `departure_reasons` | stated departure reason | `REAS` code + `RETEXT` text (FY2004+, post-Booker coding) or `REASON` + `REASTXT` (FY2002-03, pre-Booker coding) |
| `pleas` | plea/verdict slot | `INPLEA`, `INNOPL` |
| `chapter_text` | free-text guideline note | `CHP2TXT`/`CHP3TXT`/`CHP4TXT` and change flags |
| `new_statutes` | `NWSTAT` slot | statutes of conviction |
| `offense_dates` | slot | `OFBEG`/`OFEND` (FY2002-era files only) |
| `v_sentence_terms` (view) | sentenced defendant | `prison_months` and `term_type` derived from `TOTPRISN` (special codes separated) |

Every long table is keyed by (`fiscal_year`, `USSCIDN`, `seq`); empty slots are not stored.
Variable names are the Commission's; definitions and code values are in
`docs/USSC_Public_Release_Codebook_FY99_FY25.pdf`. Numeric variables are `DOUBLE`
(the Commission's blank = missing), character variables are `VARCHAR`.

What counts as an array is decided once over all 24 layouts: a numbered family is
unpivoted if it ever has 10 or more slots, uses the `NAME_n` form (`TTSC1_1`, `ADJ_B1`)
or is one of the named groups above. Small numbered sets that are really distinct
variables (`MAND1`-`MAND6`, `POINT1`-`POINT3`, `GUNMIN1`-`GUNMIN3`, `CAFROM1`/`CATO1`,
`CHEMTYP1`/`CHEMTYP2`, `RESTDET1`-`RESTDET6`, `BOOKER1`-`BOOKER4`, ...) stay as columns of
`sentences`, so the schema is the same whichever fiscal years are loaded.

## Quick start

```python
import datapond
con = datapond.connect("ussc")
con.sql("""
    -- defendants per year, share sentenced to prison, and the mean term among
    -- ordinary month-denominated prison terms (life, death and "no term stated" are
    -- categories in the source, reported separately below, not months)
    SELECT fiscal_year, COUNT(*) AS defendants,
           ROUND(100.0 * COUNT(*) FILTER (WHERE term_type IN ('months', 'life', 'death', 'prison, no term stated')) / COUNT(*), 1) AS pct_prison,
           ROUND(AVG(prison_months) FILTER (WHERE term_type = 'months'), 1) AS mean_months_when_term_stated,
           COUNT(*) FILTER (WHERE term_type = 'life') AS life,
           COUNT(*) FILTER (WHERE term_type = 'prison, no term stated') AS no_term_stated
    FROM v_sentence_terms GROUP BY 1 ORDER BY 1
""").show()
```

`v_sentence_terms` is `sentences` with `TOTPRISN` split into `prison_months` (real month
counts) and `term_type`. `TOTPRISN` alone is not averageable: the Commission codes
9992 = under one day, 9996 = life, 9997 = prison with no term stated and 9998 = death
(4,990 rows; nine more rows carry 9990 or an implausible total above 9990 and are labelled `other special code`), and it excludes imposed days, time served and section 5G1.3 credit.
`SENTTOT` is the Commission's capped composite (life = 470 in early years, 9996/9997
later) and is NULL for probation-only sentences; read the codebook's Appendix B before
choosing a sentencing measure and always state the denominator.

## Researcher caveats

- **Variables come and go across fiscal years.** `sentences` has 1,610 columns, the union of
  every year's scalar variables; 216 are populated in most rows and 1,215 are at least 99%
  NULL (year-specific or rarely-coded items). A column that is NULL for a whole fiscal year
  was not collected that year. `_columns.null_pct` and the codebook's "available FY..."
  notes explain most gaps.
- **No raw sentencing variable is a plain month count.** `TOTPRISN` (0 for no prison)
  carries the special codes 9992/9996/9997/9998 described above; `SENTTOT` is NULL for
  probation-only and zero-month sentences and caps life at 470 in early years. Use
  `v_sentence_terms.prison_months` with `term_type = 'months'` for averages and report
  life / death / no-term-stated counts alongside.
- The FY2010 file contains one record twice (`USSCIDN` 1325685, byte-identical). It is kept as
  published; `(fiscal_year, USSCIDN)` is otherwise unique.
- Slot arrays widen over time (counts of conviction: 266 slots in FY2002, 884 in FY2018,
  111 in FY2025); `seq` is the slot index and is not meaningful across years beyond ordering.
- The files exclude identifiers; `USSCIDN` is unique within a fiscal year only.
- **FY2002 codes `REASON = 0` ("no reason given") explicitly in every departure slot**, so
  `departure_reasons` has three rows per FY2002 defendant; filter `REASON > 0` (later years
  leave unused slots blank, and blank / SAS `.` slots are never stored).
- Positions in the Commission's SAS layout are byte offsets. Files are read one byte per
  character; the stray Windows-1252 punctuation some years carry in free-text fields
  (FY2006, FY2017) is replaced by `?` rather than dropped, so no column shifts. Every line is
  checked against the layout length before loading.
- FY1999-FY2001 files exist only at ICPSR under terms that do not allow redistribution.

## Build

```bash
uv sync
./download_datafiles.sh          # 24 zips, ~700 MB
uv run python build_database.py  # one fiscal year at a time (~4 min each); DuckDB capped at 3 GB, 1 thread, ~3 GB peak RSS
uv run python publish_to_hf.py --token hf_xxx --verify
```

## License

Code: MIT. Data: public domain (U.S. federal government).
