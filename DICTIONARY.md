# ussc Data Dictionary

Source: [U.S. Sentencing Commission individual offender datafiles](https://www.ussc.gov/research/datafiles/commission-datafiles), FY2002-FY2025.
Variable names are the Commission's; definitions and code values are in `docs/USSC_Public_Release_Codebook_FY99_FY25.pdf`.
Array variables (per count, per guideline, per drug ...) are unpivoted into the long tables keyed by (fiscal_year, USSCIDN, seq).

## chapter_text

Free-text chapter 2/3/4 guideline notes (CHP2TXT/CHP3TXT/CHP4TXT) and change flags

Rows: 215,883

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2006 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000020.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| CHP2CHG | DOUBLE | 41.6% | 1.0 |  |
| CHP2TXT | VARCHAR | 63.3% | +2 enhancement doesnt apply |  |
| CHP3CHG | DOUBLE | 50.9% | 1.0 |  |
| CHP3TXT | VARCHAR | 78.0% | +2 for a total of +3 levels for 3E1.1? |  |
| CHP4CHG | DOUBLE | 89.8% | 1.0 |  |
| CHP4TXT | VARCHAR | 94.3% | +3 to para 26 |  |

## counts

One row per count of conviction: statute (TTSC1/TTSC2/TTSC3 = title/section/subsection), statutory minimum/maximum (SMIN/SMAX) and STA1-3

Rows: 2,412,926

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| SMAX | DOUBLE | 2.7% | 0.0 |  |
| SMIN | DOUBLE | 2.5% | 0.0 |  |
| STA1 | VARCHAR | 0.0% | 018137 |  |
| STA2 | VARCHAR | 49.8% | 052 |  |
| STA3 | VARCHAR | 87.8% | 1021028A2 |  |
| TTSC1 | VARCHAR | 85.2% | 121715Z |  |
| TTSC2 | VARCHAR | 92.0% | 121956 |  |
| TTSC3 | VARCHAR | 98.0% | 13305 |  |

## departure_reasons

One row per stated reason for departure/variance: REAS code + RETEXT text (FY2004+, post-Booker coding) or REASON + REASTXT (FY2002-03, pre-Booker coding)

Rows: 2,637,999

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000002.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| REASON | DOUBLE | 98.3% | 0.0 |  |
| REASTXT | VARCHAR | 92.6% | " " |  |
| REAS | DOUBLE | 8.2% | 1.0 |  |
| RETEXT | VARCHAR | 99.2% | ""log jam"" |  |

## drugs

One row per drug type involved: type, weight, units, equivalency (DRUGTYP, WGT, UNIT, MWGT, DRGAM, ...)

Rows: 749,098

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| CDESCRIP | VARCHAR | 100.0% |  |  |
| DAFROM | DOUBLE | 85.3% | 0.0 |  |
| DATO | DOUBLE | 86.7% | 0.0 |  |
| DESCRIP | VARCHAR | 99.0% | .40gr of Diazepam |  |
| DRGAM | DOUBLE | 19.3% | 0.0 |  |
| DRUGTYP | DOUBLE | 0.0% | 1.0 |  |
| DUFROM | DOUBLE | 75.4% | 1.0 |  |
| DUTO | DOUBLE | 76.5% | 1.0 |  |
| MWGT | DOUBLE | 19.6% | 0.0 |  |
| UNIT | DOUBLE | 0.0% | 1.0 |  |
| WGT | DOUBLE | 19.1% | 0.0 |  |

## guidelines

One row per guideline computation on the case: base offense level, specific offense characteristics and Chapter 3 adjustments (ADJ_*), per-guideline totals

Rows: 1,706,580

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| ABUS | DOUBLE | 0.0% | -2.0 |  |
| ABUSR | DOUBLE | 91.5% | -2.0 |  |
| ADJOFL | DOUBLE | 0.0% | -2.0 |  |
| ADJOFR | DOUBLE | 39.8% | -2.0 |  |
| ADJR_B | DOUBLE | 92.2% | -2.0 |  |
| ADJR_C | DOUBLE | 92.6% | -10.0 |  |
| ADJR_D | DOUBLE | 93.2% | -10.0 |  |
| ADJR_E | DOUBLE | 93.7% | -1.0 |  |
| ADJR_F | DOUBLE | 93.9% | -2.0 |  |
| ADJR_G | DOUBLE | 94.2% | -2.0 |  |
| ADJR_H | DOUBLE | 94.9% | -2.0 |  |
| ADJR_I | DOUBLE | 95.7% | 0.0 |  |
| ADJR_J | DOUBLE | 95.8% | -2.0 |  |
| ADJR_K | DOUBLE | 96.1% | 0.0 |  |
| ADJR_L | DOUBLE | 96.1% | -2.0 |  |
| ADJR_M | DOUBLE | 96.4% | 0.0 |  |
| ADJR_N | DOUBLE | 96.5% | 0.0 |  |
| ADJR_O | DOUBLE | 96.5% | 0.0 |  |
| ADJR_P | DOUBLE | 96.6% | -2.0 |  |
| ADJ_B | DOUBLE | 3.4% | -2.0 |  |
| ADJ_C | DOUBLE | 17.8% | -10.0 |  |
| ADJ_D | DOUBLE | 20.7% | -1.0 |  |
| ADJ_E | DOUBLE | 32.0% | -1.0 |  |
| ADJ_F | DOUBLE | 33.8% | -1.0 |  |
| ADJ_G | DOUBLE | 35.9% | -1.0 |  |
| ADJ_H | DOUBLE | 45.5% | -1.0 |  |
| ADJ_I | DOUBLE | 61.7% | 0.0 |  |
| ADJ_J | DOUBLE | 62.2% | -2.0 |  |
| ADJ_K | DOUBLE | 69.0% | 0.0 |  |
| ADJ_L | DOUBLE | 69.0% | -2.0 |  |
| ADJ_M | DOUBLE | 73.3% | 0.0 |  |
| ADJ_N | DOUBLE | 74.3% | 0.0 |  |
| ADJ_O | DOUBLE | 74.3% | 0.0 |  |
| ADJ_P | DOUBLE | 74.7% | -2.0 |  |
| AGGRLR | DOUBLE | 91.5% | 0.0 |  |
| AGGROL | DOUBLE | 0.0% | -2.0 |  |
| BASADJ | DOUBLE | 3.8% | -1.0 |  |
| BASADR | DOUBLE | 40.5% | -12.0 |  |
| BASE | DOUBLE | 0.0% | -3.0 |  |
| BASER | DOUBLE | 40.0% | -9.0 |  |
| FLGHTR | DOUBLE | 91.5% | 0.0 |  |
| FLIGHT | DOUBLE | 0.0% | 0.0 |  |
| GDLINE | VARCHAR | 0.0% | 2A1.1 |  |
| GDREF | VARCHAR | 91.6% | 2A1.1 |  |
| GDSTAT | VARCHAR | 0.0% | 2A1.1 |  |
| LOSS | DOUBLE | 45.6% | 0.0 |  |
| LOSSR | DOUBLE | 94.8% | 0.0 |  |
| MITRLR | DOUBLE | 91.5% | -1.0 |  |
| MITROL | DOUBLE | 0.0% | -1.0 |  |
| OBSTRC | DOUBLE | 0.0% | -1.0 |  |
| OBSTRR | DOUBLE | 91.5% | 0.0 |  |
| OFFVCR | DOUBLE | 91.5% | 0.0 |  |
| OFFVCT | DOUBLE | 0.0% | 0.0 |  |
| RLADJR | DOUBLE | 97.8% | 0.0 |  |
| ROLADJ | DOUBLE | 66.7% | 0.0 |  |
| RSTRVC | DOUBLE | 0.0% | 0.0 |  |
| RSTRVR | DOUBLE | 91.5% | 0.0 |  |
| TEROR | DOUBLE | 0.0% | 0.0 |  |
| TERORR | DOUBLE | 91.6% | 0.0 |  |
| USKID | DOUBLE | 0.0% | -4.0 |  |
| USKIDR | DOUBLE | 91.6% | 0.0 |  |
| VCADJR | DOUBLE | 97.8% | 0.0 |  |
| VCTADJ | DOUBLE | 66.7% | 0.0 |  |
| VULVCR | DOUBLE | 91.5% | 0.0 |  |
| VULVCT | DOUBLE | 0.0% | 0.0 |  |
| ABUSC | DOUBLE | 99.5% | 0.0 |  |
| ABUSS | DOUBLE | 7.8% | 0.0 |  |
| ADCL_B | VARCHAR | 99.5% | A |  |
| ADCL_C | VARCHAR | 99.6% | A |  |
| ADCL_D | VARCHAR | 99.7% | A |  |
| ADCL_E | VARCHAR | 99.7% | A |  |
| ADCL_F | VARCHAR | 99.7% | A |  |
| ADCL_G | VARCHAR | 99.7% | A |  |
| ADCL_H | VARCHAR | 99.8% | A |  |
| ADCL_I | VARCHAR | 99.8% | A |  |
| ADCL_J | VARCHAR | 99.8% | A |  |
| ADCL_K | VARCHAR | 99.9% | A |  |
| ADCL_L | VARCHAR | 99.9% | A |  |
| ADCL_M | VARCHAR | 99.9% | A |  |
| ADCL_N | VARCHAR | 99.9% | A |  |
| ADCL_O | VARCHAR | 99.9% | A |  |
| ADCL_P | VARCHAR | 99.9% | A |  |
| ADJC_B | DOUBLE | 99.5% | -2.0 |  |
| ADJC_C | DOUBLE | 99.6% | -3.0 |  |
| ADJC_D | DOUBLE | 99.7% | -18.0 |  |
| ADJC_E | DOUBLE | 99.7% | -1.0 |  |
| ADJC_F | DOUBLE | 99.7% | 0.0 |  |
| ADJC_G | DOUBLE | 99.7% | -2.0 |  |
| ADJC_H | DOUBLE | 99.8% | -2.0 |  |
| ADJC_I | DOUBLE | 99.8% | 0.0 |  |
| ADJC_J | DOUBLE | 99.8% | -2.0 |  |
| ADJC_K | DOUBLE | 99.9% | 0.0 |  |
| ADJC_L | DOUBLE | 99.9% | -2.0 |  |
| ADJC_M | DOUBLE | 99.9% | 0.0 |  |
| ADJC_N | DOUBLE | 99.9% | 0.0 |  |
| ADJC_O | DOUBLE | 99.9% | 0.0 |  |
| ADJC_P | DOUBLE | 99.9% | -2.0 |  |
| ADJL_B | VARCHAR | 10.9% | A |  |
| ADJL_C | VARCHAR | 24.2% | A |  |
| ADJL_D | VARCHAR | 26.7% | A |  |
| ADJL_E | VARCHAR | 37.9% | A |  |
| ADJL_F | VARCHAR | 39.5% | A |  |
| ADJL_G | VARCHAR | 41.4% | A |  |
| ADJL_H | VARCHAR | 47.2% | A |  |
| ADJL_I | VARCHAR | 62.8% | A |  |
| ADJL_J | VARCHAR | 62.9% | A |  |
| ADJL_K | VARCHAR | 69.7% | A |  |
| ADJL_L | VARCHAR | 69.7% | A |  |
| ADJL_M | VARCHAR | 74.0% | A |  |
| ADJL_N | VARCHAR | 74.3% | A |  |
| ADJL_O | VARCHAR | 74.3% | A |  |
| ADJL_P | VARCHAR | 74.7% | A |  |
| ADJOFC | DOUBLE | 42.6% | 0.0 |  |
| ADJOFS | DOUBLE | 7.8% | -2.0 |  |
| ADJS_B | DOUBLE | 12.4% | -2.0 |  |
| ADJS_C | DOUBLE | 25.6% | -10.0 |  |
| ADJS_D | DOUBLE | 27.6% | -1.0 |  |
| ADJS_E | DOUBLE | 41.4% | -1.0 |  |
| ADJS_F | DOUBLE | 42.9% | -1.0 |  |
| ADJS_G | DOUBLE | 44.6% | -2.0 |  |
| ADJS_H | DOUBLE | 50.1% | -1.0 |  |
| ADJS_I | DOUBLE | 65.3% | 0.0 |  |
| ADJS_J | DOUBLE | 65.5% | -2.0 |  |
| ADJS_K | DOUBLE | 72.1% | 0.0 |  |
| ADJS_L | DOUBLE | 72.1% | -2.0 |  |
| ADJS_M | DOUBLE | 76.3% | 0.0 |  |
| ADJS_N | DOUBLE | 76.6% | 0.0 |  |
| ADJS_O | DOUBLE | 76.6% | 0.0 |  |
| ADJS_P | DOUBLE | 76.9% | -2.0 |  |
| ADRL_B | VARCHAR | 92.7% | A |  |
| ADRL_C | VARCHAR | 93.1% | A |  |
| ADRL_D | VARCHAR | 93.6% | A |  |
| ADRL_E | VARCHAR | 94.1% | A |  |
| ADRL_F | VARCHAR | 94.3% | A |  |
| ADRL_G | VARCHAR | 94.6% | A |  |
| ADRL_H | VARCHAR | 95.0% | A |  |
| ADRL_I | VARCHAR | 95.8% | A |  |
| ADRL_J | VARCHAR | 95.8% | A |  |
| ADRL_K | VARCHAR | 96.1% | A |  |
| ADRL_L | VARCHAR | 96.1% | A |  |
| ADRL_M | VARCHAR | 96.5% | A |  |
| ADRL_N | VARCHAR | 96.5% | A |  |
| ADRL_O | VARCHAR | 96.5% | A |  |
| ADRL_P | VARCHAR | 96.6% | A |  |
| ADSL_B | VARCHAR | 12.2% | A |  |
| ADSL_C | VARCHAR | 25.4% | A |  |
| ADSL_D | VARCHAR | 27.4% | A |  |
| ADSL_E | VARCHAR | 41.4% | A |  |
| ADSL_F | VARCHAR | 42.9% | A |  |
| ADSL_G | VARCHAR | 44.6% | A |  |
| ADSL_H | VARCHAR | 50.1% | A |  |
| ADSL_I | VARCHAR | 65.3% | A |  |
| ADSL_J | VARCHAR | 65.5% | A |  |
| ADSL_K | VARCHAR | 72.1% | A |  |
| ADSL_L | VARCHAR | 72.1% | A |  |
| ADSL_M | VARCHAR | 76.2% | A |  |
| ADSL_N | VARCHAR | 76.6% | A |  |
| ADSL_O | VARCHAR | 76.6% | A |  |
| ADSL_P | VARCHAR | 76.9% | A |  |
| AGGRLC | DOUBLE | 99.5% | 0.0 |  |
| AGGRLS | DOUBLE | 7.8% | -3.0 |  |
| BASADC | DOUBLE | 42.6% | -13.0 |  |
| BASADS | DOUBLE | 7.9% | -1.0 |  |
| BASEC | DOUBLE | 42.6% | 0.0 |  |
| BASECL | VARCHAR | 99.5% | A |  |
| BASEL | VARCHAR | 7.8% | A |  |
| BASERL | VARCHAR | 92.6% | A |  |
| BASES | DOUBLE | 7.8% | -3.0 |  |
| BASESL | VARCHAR | 13.5% | A |  |
| FLGHTC | DOUBLE | 99.5% | 0.0 |  |
| FLGHTS | DOUBLE | 7.8% | 0.0 |  |
| GDCROS | VARCHAR | 99.5% | 2A1.1 |  |
| INDEXC | DOUBLE | 99.9% | 0.0 |  |
| INDEXR | DOUBLE | 98.6% | 0.0 |  |
| INDEXS | DOUBLE | 66.6% | 0.0 |  |
| LOSSC | DOUBLE | 99.8% | 0.0 |  |
| LOSSS | DOUBLE | 55.3% | 0.0 |  |
| MITRLC | DOUBLE | 99.5% | -2.0 |  |
| MITRLS | DOUBLE | 7.8% | -1.0 |  |
| OBSTCC | DOUBLE | 99.5% | 0.0 |  |
| OBSTRS | DOUBLE | 7.8% | -1.0 |  |
| OFFVCC | DOUBLE | 99.5% | 0.0 |  |
| OFFVCS | DOUBLE | 7.8% | 0.0 |  |
| RLADJC | DOUBLE | 99.9% | 0.0 |  |
| RLADJS | DOUBLE | 74.6% | 0.0 |  |
| RSTRCC | DOUBLE | 99.5% | 0.0 |  |
| RSTRVS | DOUBLE | 7.8% | 0.0 |  |
| TERORC | DOUBLE | 99.5% | 0.0 |  |
| TERORS | DOUBLE | 7.9% | 0.0 |  |
| USARM | DOUBLE | 10.4% | 0.0 |  |
| USARMC | DOUBLE | 99.5% | 0.0 |  |
| USARMR | DOUBLE | 92.4% | 0.0 |  |
| USARMS | DOUBLE | 10.4% | 0.0 |  |
| USKIDC | DOUBLE | 99.5% | 0.0 |  |
| USKIDS | DOUBLE | 7.9% | -4.0 |  |
| VCADJC | DOUBLE | 99.9% | 0.0 |  |
| VCADJS | DOUBLE | 74.6% | 0.0 |  |
| VULVCC | DOUBLE | 99.5% | 0.0 |  |
| VULVCS | DOUBLE | 7.8% | 0.0 |  |
| FALDM | DOUBLE | 22.0% | 0.0 |  |
| FALDMC | DOUBLE | 99.5% | 0.0 |  |
| FALDMR | DOUBLE | 93.0% | 0.0 |  |
| FALDMS | DOUBLE | 22.0% | 0.0 |  |
| MCCDA | DOUBLE | 99.6% | 1.0 |  |
| MCCDB | DOUBLE | 100.0% | 1.0 |  |
| MCCDC | DOUBLE | 100.0% | 1.0 |  |
| MCCDCA | DOUBLE | 100.0% | 1.0 |  |
| MCCDCB | DOUBLE | 100.0% | 2.0 |  |
| MCCDCC | DOUBLE | 100.0% | 3.0 |  |
| MCCDCD | DOUBLE | 100.0% |  |  |
| MCCDD | DOUBLE | 100.0% | 1.0 |  |
| MCCDRA | DOUBLE | 100.0% | 1.0 |  |
| MCCDRB | DOUBLE | 100.0% | 2.0 |  |
| MCCDRC | DOUBLE | 100.0% | 3.0 |  |
| MCCDRD | DOUBLE | 100.0% |  |  |
| MCCDSA | DOUBLE | 99.6% | 1.0 |  |
| MCCDSB | DOUBLE | 100.0% | 1.0 |  |
| MCCDSC | DOUBLE | 100.0% | 1.0 |  |
| MCCDSD | DOUBLE | 100.0% | 1.0 |  |
| MCCNT | DOUBLE | 95.8% | 0.0 |  |
| MCCNTC | DOUBLE | 100.0% | 0.0 |  |
| MCCNTR | DOUBLE | 99.7% | 0.0 |  |
| MCCNTS | DOUBLE | 95.8% | 0.0 |  |
| MCUNT | DOUBLE | 95.8% | 0.0 |  |
| MCUNTC | DOUBLE | 100.0% | 0.0 |  |
| MCUNTR | DOUBLE | 99.7% | 0.0 |  |
| MCUNTS | DOUBLE | 95.8% | 0.0 |  |
| RLEAS | DOUBLE | 22.0% | 0.0 |  |
| RLEASC | DOUBLE | 99.5% | 0.0 |  |
| RLEASR | DOUBLE | 93.0% | 0.0 |  |
| RLEASS | DOUBLE | 22.0% | 0.0 |  |
| ADCL_Q | VARCHAR | 99.9% | A |  |
| ADJC_Q | DOUBLE | 99.9% | -2.0 |  |
| ADJL_Q | VARCHAR | 76.4% | A |  |
| ADJR_Q | DOUBLE | 96.8% | -2.0 |  |
| ADJS_Q | DOUBLE | 78.4% | -2.0 |  |
| ADJ_Q | DOUBLE | 76.4% | -2.0 |  |
| ADRL_Q | VARCHAR | 96.8% | A |  |
| ADSL_Q | VARCHAR | 78.4% | A |  |
| ADCL_R | VARCHAR | 99.9% | A |  |
| ADJC_R | DOUBLE | 99.9% | -2.0 |  |
| ADJL_R | VARCHAR | 82.2% | A |  |
| ADJR_R | DOUBLE | 97.4% | -2.0 |  |
| ADJS_R | DOUBLE | 84.0% | -2.0 |  |
| ADJ_R | DOUBLE | 82.2% | -2.0 |  |
| ADRL_R | VARCHAR | 97.4% | A |  |
| ADSL_R | VARCHAR | 84.0% | A |  |
| ABUSU | DOUBLE | 100.0% | 0.0 |  |
| ADCL_S | VARCHAR | 99.9% | A |  |
| ADJC_S | DOUBLE | 99.9% | -2.0 |  |
| ADJL_S | VARCHAR | 87.9% | A |  |
| ADJOFU | DOUBLE | 42.7% | 0.0 |  |
| ADJR_S | DOUBLE | 98.0% | -2.0 |  |
| ADJS_S | DOUBLE | 89.4% | -2.0 |  |
| ADJU_B | DOUBLE | 100.0% | 0.0 |  |
| ADJU_C | DOUBLE | 100.0% | 0.0 |  |
| ADJU_D | DOUBLE | 100.0% | 0.0 |  |
| ADJU_E | DOUBLE | 100.0% | 0.0 |  |
| ADJU_F | DOUBLE | 100.0% | 0.0 |  |
| ADJU_G | DOUBLE | 100.0% | 0.0 |  |
| ADJU_H | DOUBLE | 100.0% | 0.0 |  |
| ADJU_I | DOUBLE | 100.0% | 0.0 |  |
| ADJU_J | DOUBLE | 100.0% | 0.0 |  |
| ADJU_K | DOUBLE | 100.0% | 0.0 |  |
| ADJU_L | DOUBLE | 100.0% | 0.0 |  |
| ADJU_M | DOUBLE | 100.0% | 0.0 |  |
| ADJU_N | DOUBLE | 100.0% | 0.0 |  |
| ADJU_O | DOUBLE | 100.0% | 0.0 |  |
| ADJU_P | DOUBLE | 100.0% | 0.0 |  |
| ADJU_Q | DOUBLE | 100.0% | 0.0 |  |
| ADJU_R | DOUBLE | 100.0% | -2.0 |  |
| ADJU_S | DOUBLE | 100.0% | 0.0 |  |
| ADJ_S | DOUBLE | 87.9% | -2.0 |  |
| ADRL_S | VARCHAR | 98.0% | A |  |
| ADSL_S | VARCHAR | 89.4% | A |  |
| ADUL_B | VARCHAR | 100.0% | A |  |
| ADUL_C | VARCHAR | 100.0% | A |  |
| ADUL_D | VARCHAR | 100.0% | A |  |
| ADUL_E | VARCHAR | 100.0% | A |  |
| ADUL_F | VARCHAR | 100.0% | A |  |
| ADUL_G | VARCHAR | 100.0% | A |  |
| ADUL_H | VARCHAR | 100.0% | A |  |
| ADUL_I | VARCHAR | 100.0% | A |  |
| ADUL_J | VARCHAR | 100.0% | A |  |
| ADUL_K | VARCHAR | 100.0% | A |  |
| ADUL_L | VARCHAR | 100.0% | A |  |
| ADUL_M | VARCHAR | 100.0% | A |  |
| ADUL_N | VARCHAR | 100.0% | A |  |
| ADUL_O | VARCHAR | 100.0% | A |  |
| ADUL_P | VARCHAR | 100.0% | A |  |
| ADUL_Q | VARCHAR | 100.0% | A |  |
| ADUL_R | VARCHAR | 100.0% | A |  |
| ADUL_S | VARCHAR | 100.0% | A |  |
| AGGRLU | DOUBLE | 100.0% | 0.0 |  |
| BASADU | DOUBLE | 42.7% | -6.0 |  |
| BASEU | DOUBLE | 42.7% | 0.0 |  |
| BASEUL | VARCHAR | 100.0% | A |  |
| BASLN | DOUBLE | 42.7% | 1.0 |  |
| BASLNC | DOUBLE | 99.6% | 1.0 |  |
| BASLNR | DOUBLE | 94.8% | 1.0 |  |
| BASLNS | DOUBLE | 47.0% | 1.0 |  |
| BASLNU | DOUBLE | 100.0% | 1.0 |  |
| FALDMU | DOUBLE | 100.0% | 0.0 |  |
| FLGHTU | DOUBLE | 100.0% | 0.0 |  |
| GDUNDR | VARCHAR | 100.0% | 2A1.1 |  |
| LOSSU | DOUBLE | 100.0% | 0.0 |  |
| MITRLU | DOUBLE | 100.0% | -2.0 |  |
| OBSTCU | DOUBLE | 100.0% | 0.0 |  |
| OFFVCU | DOUBLE | 100.0% | 0.0 |  |
| RLEASU | DOUBLE | 100.0% | 0.0 |  |
| RSTRVU | DOUBLE | 100.0% | 0.0 |  |
| TERORU | DOUBLE | 100.0% | 0.0 |  |
| USARMU | DOUBLE | 100.0% | 0.0 |  |
| USKIDU | DOUBLE | 100.0% | 0.0 |  |
| VULVCU | DOUBLE | 100.0% | 0.0 |  |
| HUMAN | DOUBLE | 48.9% | 0.0 |  |
| HUMANC | DOUBLE | 99.7% | 0.0 |  |
| HUMANR | DOUBLE | 95.1% | 0.0 |  |
| HUMANS | DOUBLE | 48.9% | 0.0 |  |
| HUMANU | DOUBLE | 100.0% | 0.0 |  |
| HUMLB | VARCHAR | 48.9% | A |  |
| HUMLBC | VARCHAR | 99.7% | A |  |
| HUMLBR | VARCHAR | 95.1% | A |  |
| HUMLBS | VARCHAR | 48.9% | A |  |
| HUMLBU | VARCHAR | 100.0% | A |  |
| ADCL_T | VARCHAR | 100.0% | A |  |
| ADJC_T | DOUBLE | 100.0% | 0.0 |  |
| ADJL_T | VARCHAR | 96.0% | A |  |
| ADJR_T | DOUBLE | 98.7% | 0.0 |  |
| ADJS_T | DOUBLE | 97.0% | 0.0 |  |
| ADJU_T | DOUBLE | 100.0% | 0.0 |  |
| ADJ_T | DOUBLE | 96.0% | 0.0 |  |
| ADRL_T | VARCHAR | 98.7% | A |  |
| ADSL_T | VARCHAR | 97.0% | A |  |
| ADUL_T | VARCHAR | 100.0% | A |  |
| ADCL_U | VARCHAR | 100.0% | A |  |
| ADJC_U | DOUBLE | 100.0% | 0.0 |  |
| ADJL_U | VARCHAR | 98.0% | A |  |
| ADJR_U | DOUBLE | 99.3% | 0.0 |  |
| ADJS_U | DOUBLE | 98.6% | 0.0 |  |
| ADJU_U | DOUBLE | 100.0% | 0.0 |  |
| ADJ_U | DOUBLE | 98.0% | 0.0 |  |
| ADRL_U | VARCHAR | 99.3% | A |  |
| ADSL_U | VARCHAR | 98.6% | A |  |
| ADUL_U | VARCHAR | 100.0% | A |  |

## new_statutes

Statutes of conviction as recorded in NWSTAT slots

Rows: 3,279,305

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| NWSTAT | VARCHAR | 0.0% | 018137 |  |

## offense_dates

Offense begin/end dates per slot (OFBEG/OFEND; FY2002-era files only)

Rows: 501,590

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 534273.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| OFBEG | DOUBLE | 0.0% | 0.0 |  |
| OFEND | DOUBLE | 0.0% | 0.0 |  |

## pleas

One row per plea/verdict slot (INPLEA, INNOPL)

Rows: 738,024

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2005 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000002.0 | USSC case identifier; joins every table |
| seq | INTEGER | 0.0% | 1 | Slot index within the array (1 = first count / guideline / drug ...) |
| INNOPL | DOUBLE | 40.6% | 1.0 |  |
| INPLEA | DOUBLE | 52.8% | 1.0 |  |

## sentences

One row per federal defendant sentenced in the fiscal year: demographics, offense, guideline range, sentence imposed, departures (scalar variables of the USSC individual offender datafile)

Rows: 1,720,684

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| SAFETY | VARCHAR | 66.0% | 0.0 |  |
| ZONE | VARCHAR | 2.6% | A |  |
| AMTFINEC | DOUBLE | 0.1% | 0.0 |  |
| AMTREST | DOUBLE | 1.0% | 0.0 |  |
| AMTTOTAL | DOUBLE | 0.4% | 0.0 |  |
| COSTSUP | DOUBLE | 0.1% | 0.0 |  |
| FINE | DOUBLE | 0.1% | 0.0 |  |
| TOTREST | DOUBLE | 0.3% | 0.0 |  |
| SENTTOT | DOUBLE | 12.4% | 0.03 |  |
| SENTTOT0 | DOUBLE | 31.2% | 0.0 |  |
| SENSPLT | DOUBLE | 38.0% | 0.03 |  |
| SENSPLT0 | DOUBLE | 0.1% | 0.0 |  |
| TIMESERV | DOUBLE | 31.2% | 0.0 |  |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| ACCAP | DOUBLE | 7.0% | 0.0 |  |
| ACCCAT | DOUBLE | 96.4% | 1.0 |  |
| ACCGDLN | DOUBLE | 2.0% | 0.0 |  |
| ACCOFFLV | DOUBLE | 63.5% | 0.0 |  |
| ACCTRESP | DOUBLE | 7.9% | -1.0 |  |
| CAROFFAP | DOUBLE | 7.0% | 0.0 |  |
| AGE | DOUBLE | 0.8% | 102.0 |  |
| ALTDUM | DOUBLE | 0.1% | 0.0 |  |
| ALTMO | DOUBLE | 0.0% | 0.0 |  |
| AMENDYR | DOUBLE | 6.9% | 1986.0 |  |
| CAROFFLV | DOUBLE | 62.2% | 0.0 |  |
| CHAP2 | DOUBLE | 8.0% | -2.0 |  |
| CIRCDIST | DOUBLE | 0.0% | 1.0 | Circuit-district code of the sentencing court (USSC coding; codebook table) |
| CITIZEN | DOUBLE | 2.4% | 1.0 |  |
| CITWHERE | DOUBLE | 3.8% | 100.0 |  |
| COADJLEV | DOUBLE | 21.9% | -4.0 |  |
| COMBDRG2 | DOUBLE | 66.6% | 1.0 |  |
| COMDUM | DOUBLE | 0.1% | 0.0 |  |
| COSTSDUM | DOUBLE | 0.1% | 0.0 |  |
| CRIMHIST | DOUBLE | 4.9% | 0.0 |  |
| CRIMLIV | DOUBLE | 31.5% | 0.0 |  |
| CRIMPTS | DOUBLE | 7.7% | 0.0 |  |
| DAYSDUM | DOUBLE | 0.1% | 0.0 |  |
| DEFCONSL | DOUBLE | 95.9% | 1.0 |  |
| DEPART | DOUBLE | 92.8% | 0.0 |  |
| DISPOSIT | DOUBLE | 0.1% | 0.0 |  |
| DISTRICT | DOUBLE | 0.0% | 0.0 | District code |
| DSIND | DOUBLE | 0.0% | 0.0 |  |
| DSJANDC | DOUBLE | 0.0% | 0.0 |  |
| DSPLEA | DOUBLE | 0.0% | 0.0 |  |
| DSPSR | DOUBLE | 0.0% | 0.0 |  |
| DSSOR | DOUBLE | 0.0% | 0.0 |  |
| ECONDUM | DOUBLE | 0.4% | 0.0 |  |
| EDUCATN | DOUBLE | 10.1% | 0.0 |  |
| ENCRYPT1 | DOUBLE | 2.1% | 0.0 |  |
| ENCRYPT2 | DOUBLE | 25.6% | 0.0 |  |
| FINECDUM | DOUBLE | 0.2% | 0.0 |  |
| FINEWAIV | DOUBLE | 29.5% | 0.0 |  |
| HISPORIG | DOUBLE | 0.7% | 0.0 |  |
| HOMDUM | DOUBLE | 0.1% | 0.0 |  |
| HRCOMSRV | DOUBLE | 0.1% | 0.0 |  |
| INOUT | DOUBLE | 78.1% | 0.0 |  |
| INTDUM | DOUBLE | 0.1% | 0.0 |  |
| IS924C | DOUBLE | 0.1% | 0.0 |  |
| MARRIED | DOUBLE | 92.9% | 1.0 |  |
| MOCOMCON | DOUBLE | 0.1% | 0.0 |  |
| MOHOMDET | DOUBLE | 0.1% | 0.0 |  |
| MOINTCON | DOUBLE | 0.1% | 0.0 |  |
| MONCIRC | DOUBLE | 0.0% | 0.0 | Circuit |
| MONRACE | DOUBLE | 1.6% | 1.0 |  |
| MONSEX | DOUBLE | 1.6% | 0.0 |  |
| NEWCIT | DOUBLE | 2.4% | 0.0 |  |
| NEWCNVTN | DOUBLE | 0.1% | 0.0 |  |
| NEWEDUC | DOUBLE | 10.1% | 1.0 |  |
| NEWRACE | DOUBLE | 4.6% | 1.0 |  |
| NOCOMP | DOUBLE | 8.0% | 1.0 |  |
| NOCOUNTS | DOUBLE | 0.1% | 0.0 |  |
| NOUSTAT | DOUBLE | 0.1% | 1.0 |  |
| NUMDEPEN | DOUBLE | 11.0% | 0.0 |  |
| OFFTYPE2 | DOUBLE | 30.6% | 1.0 |  |
| POINT1 | DOUBLE | 5.3% | 0.0 |  |
| POINT2 | DOUBLE | 7.7% | 0.0 |  |
| POINT3 | DOUBLE | 7.7% | 0.0 |  |
| PRESENT | DOUBLE | 6.8% | 1.0 |  |
| PRISDUM | DOUBLE | 0.1% | 0.0 |  |
| PROBATN | DOUBLE | 0.1% | 0.0 |  |
| PROBDUM | DOUBLE | 0.1% | 0.0 |  |
| RANGEPT | DOUBLE | 50.6% | 1.0 |  |
| REL2PTS | DOUBLE | 44.2% | 0.0 |  |
| RESNTDOC | DOUBLE | 92.2% | 0.0 |  |
| RESTDUM | DOUBLE | 0.3% | 0.0 |  |
| SAFE | DOUBLE | 68.6% | 0.0 |  |
| SENTIMP | DOUBLE | 0.1% | 0.0 |  |
| SENTPTS | DOUBLE | 7.7% | 0.0 |  |
| SEXOFFNA | DOUBLE | 33.5% | 0.0 |  |
| SEXOFFNB | DOUBLE | 34.7% | 0.0 |  |
| SOURCES | DOUBLE | 0.1% | 1.0 |  |
| SUPRDUM | DOUBLE | 0.2% | 0.0 |  |
| SUPREL | DOUBLE | 0.2% | -36.0 |  |
| TOTCHPTS | DOUBLE | 7.0% | 0.0 |  |
| TOTDAYS | DOUBLE | 0.1% | 0.0 |  |
| TOTUNIT | DOUBLE | 4.0% | 0.0 |  |
| TYPEMONY | DOUBLE | 0.4% | 1.0 |  |
| TYPEOTHS | DOUBLE | 0.1% | 0.0 |  |
| VIOL1PTS | DOUBLE | 7.7% | 0.0 |  |
| WEAPON | DOUBLE | 0.1% | 0.0 |  |
| WEAPSOC | DOUBLE | 8.0% | 0.0 |  |
| XCRHISSR | DOUBLE | 2.3% | 1.0 |  |
| XFOLSOR | DOUBLE | 2.9% | 1.0 |  |
| YEARS | DOUBLE | 0.8% | 1.0 |  |
| DRUGMIN | DOUBLE | 0.1% | 0.0 |  |
| GLMIN | DOUBLE | 2.8% | 0.0 |  |
| GLMAX | DOUBLE | 2.8% | 0.0 |  |
| GUNMIN1 | DOUBLE | 0.1% | 0.0 |  |
| GUNMIN2 | DOUBLE | 0.1% | 0.0 |  |
| STATMAX | DOUBLE | 3.7% | 0.0 |  |
| STATMIN | DOUBLE | 3.7% | 0.0 |  |
| TOTPRISN | DOUBLE | 0.1% | 0.0 |  |
| XMAXSOR | DOUBLE | 2.9% | 10.0 |  |
| XMINSOR | DOUBLE | 2.9% | 0.0 |  |
| ABERTXT | VARCHAR | 99.7% | $100 assessment for all 4 counts |  |
| POOFFICE | VARCHAR | 2.1% | 0 |  |
| TIMSERVD | DOUBLE | 0.2% | 0.0 |  |
| TIMSERVM | DOUBLE | 0.2% | 0.0 |  |
| SPECASSM | DOUBLE | 5.4% | 0.0 |  |
| ABERCASE | VARCHAR | 99.8% | 0 |  |
| CHMAM1 | DOUBLE | 99.9% | 0.2 |  |
| CHMAM2 | DOUBLE | 100.0% | 0.13 |  |
| CHMAM3 | DOUBLE | 100.0% | 10.0 |  |
| CHMAM4 | DOUBLE | 100.0% | 200.0 |  |
| CHMAM5 | DOUBLE | 100.0% | 200.0 |  |
| CUNIT1 | DOUBLE | 99.8% | -1.0 |  |
| CUNIT2 | DOUBLE | 100.0% | -1.0 |  |
| CUNIT3 | DOUBLE | 100.0% | 1.0 |  |
| CUNIT4 | DOUBLE | 100.0% | -1.0 |  |
| CUNIT5 | DOUBLE | 100.0% | 1.0 |  |
| CHEMTYP1 | DOUBLE | 99.8% | 1.0 |  |
| CHEMTYP2 | DOUBLE | 100.0% | 11.0 |  |
| CHEMTYP3 | DOUBLE | 100.0% | 26.0 |  |
| CHEMTYP4 | DOUBLE | 100.0% | 27.0 |  |
| CHEMTYP5 | DOUBLE | 100.0% | 33.0 |  |
| CAFROM1 | DOUBLE | 100.0% | 0.0 |  |
| CAFROM2 | DOUBLE | 100.0% | 100.0 |  |
| CAFROM3 | DOUBLE | 100.0% |  |  |
| CAFROM4 | DOUBLE | 100.0% | 9.0 |  |
| CAFROM5 | DOUBLE | 100.0% |  |  |
| CATO1 | DOUBLE | 100.0% | 1.0 |  |
| CATO2 | DOUBLE | 100.0% | 1552.0 |  |
| CATO3 | DOUBLE | 100.0% |  |  |
| CATO4 | DOUBLE | 100.0% | 1559.0 |  |
| CATO5 | DOUBLE | 100.0% |  |  |
| DATE1 | DOUBLE | 100.0% |  |  |
| DATE1_1 | DOUBLE | 100.0% |  |  |
| ABUSHI | DOUBLE | 8.0% | -2.0 |  |
| ABUSRHI | DOUBLE | 93.0% | -2.0 |  |
| ADJOFLHI | DOUBLE | 8.0% | -2.0 |  |
| ADJOFRHI | DOUBLE | 45.1% | -2.0 |  |
| ADJR_BHI | DOUBLE | 93.5% | -2.0 |  |
| ADJR_CHI | DOUBLE | 93.6% | -10.0 |  |
| ADJR_DHI | DOUBLE | 94.0% | -10.0 |  |
| ADJR_EHI | DOUBLE | 94.4% | -1.0 |  |
| ADJR_FHI | DOUBLE | 94.6% | -2.0 |  |
| ADJR_GHI | DOUBLE | 94.8% | -2.0 |  |
| ADJR_HHI | DOUBLE | 95.3% | -2.0 |  |
| ADJR_IHI | DOUBLE | 95.8% | 0.0 |  |
| ADJR_JHI | DOUBLE | 95.9% | -2.0 |  |
| ADJR_KHI | DOUBLE | 96.2% | 0.0 |  |
| ADJR_LHI | DOUBLE | 96.2% | -2.0 |  |
| ADJR_MHI | DOUBLE | 96.5% | 0.0 |  |
| ADJR_NHI | DOUBLE | 96.7% | 0.0 |  |
| ADJR_OHI | DOUBLE | 96.7% | 0.0 |  |
| ADJR_PHI | DOUBLE | 96.7% | -2.0 |  |
| ADJ_BHI | DOUBLE | 10.9% | -2.0 |  |
| ADJ_CHI | DOUBLE | 24.6% | -10.0 |  |
| ADJ_DHI | DOUBLE | 26.9% | -1.0 |  |
| ADJ_EHI | DOUBLE | 37.8% | -1.0 |  |
| ADJ_FHI | DOUBLE | 39.4% | -1.0 |  |
| ADJ_GHI | DOUBLE | 41.0% | -1.0 |  |
| ADJ_HHI | DOUBLE | 49.7% | -1.0 |  |
| ADJ_IHI | DOUBLE | 62.6% | 0.0 |  |
| ADJ_JHI | DOUBLE | 63.1% | -2.0 |  |
| ADJ_KHI | DOUBLE | 69.8% | 0.0 |  |
| ADJ_LHI | DOUBLE | 69.8% | -2.0 |  |
| ADJ_MHI | DOUBLE | 74.0% | 0.0 |  |
| ADJ_NHI | DOUBLE | 75.0% | 0.0 |  |
| ADJ_OHI | DOUBLE | 75.0% | 0.0 |  |
| ADJ_PHI | DOUBLE | 75.3% | -2.0 |  |
| AGGRLRHI | DOUBLE | 93.0% | 0.0 |  |
| AGGROLHI | DOUBLE | 8.0% | -2.0 |  |
| BASADJHI | DOUBLE | 11.4% | -1.0 |  |
| BASADRHI | DOUBLE | 45.6% | -12.0 |  |
| BASEHI | DOUBLE | 8.0% | -3.0 |  |
| BASERHI | DOUBLE | 45.2% | -9.0 |  |
| FLGHTRHI | DOUBLE | 93.0% | 0.0 |  |
| FLIGHTHI | DOUBLE | 8.0% | 0.0 |  |
| MITRLRHI | DOUBLE | 93.0% | -1.0 |  |
| MITROLHI | DOUBLE | 8.0% | -1.0 |  |
| OBSTRCHI | DOUBLE | 8.0% | -1.0 |  |
| OBSTRRHI | DOUBLE | 93.0% | 0.0 |  |
| OFFVCRHI | DOUBLE | 93.0% | 0.0 |  |
| OFFVCTHI | DOUBLE | 8.0% | 0.0 |  |
| RLADJRHI | DOUBLE | 98.1% | 0.0 |  |
| ROLADJHI | DOUBLE | 69.2% | 0.0 |  |
| RSTRVCHI | DOUBLE | 8.0% | 0.0 |  |
| RSTRVRHI | DOUBLE | 93.0% | 0.0 |  |
| TERORHI | DOUBLE | 8.0% | 0.0 |  |
| TERORRHI | DOUBLE | 93.0% | 0.0 |  |
| USKIDHI | DOUBLE | 8.0% | -4.0 |  |
| USKIDRHI | DOUBLE | 93.0% | 0.0 |  |
| VCADJRHI | DOUBLE | 98.1% | 0.0 |  |
| VCTADJHI | DOUBLE | 69.2% | 0.0 |  |
| VULVCRHI | DOUBLE | 93.0% | 0.0 |  |
| VULVCTHI | DOUBLE | 8.0% | 0.0 |  |
| GDLINEHI | VARCHAR | 8.0% | 2A1.1 |  |
| GDSTATHI | VARCHAR | 8.0% | 2A1.1 |  |
| LOSSHI | DOUBLE | 50.7% | 0.0 |  |
| GDREFHI | VARCHAR | 93.0% | 2A1.1 |  |
| LOSSRHI | DOUBLE | 95.4% | 0.0 |  |
| OFBEG | DOUBLE | 100.0% |  |  |
| DATE1_2 | DOUBLE | 100.0% |  |  |
| OFBEG_1 | DOUBLE | 100.0% |  |  |
| DATE1_3 | DOUBLE | 100.0% |  |  |
| OFBEG_2 | DOUBLE | 100.0% |  |  |
| DATE1_4 | DOUBLE | 100.0% |  |  |
| OFBEG_3 | DOUBLE | 100.0% |  |  |
| DATE1_5 | DOUBLE | 100.0% |  |  |
| OFBEG_4 | DOUBLE | 100.0% | 1.0 |  |
| DATE1_6 | DOUBLE | 100.0% |  |  |
| OFBEG_5 | DOUBLE | 100.0% | 0.0 |  |
| DATE1_7 | DOUBLE | 100.0% |  |  |
| OFBEG_6 | DOUBLE | 99.9% | 0.0 |  |
| DATE1_8 | DOUBLE | 100.0% |  |  |
| OFBEG_7 | DOUBLE | 99.6% | 0.0 |  |
| DATE1_9 | DOUBLE | 100.0% |  |  |
| OFBEG_8 | DOUBLE | 99.2% | 0.0 |  |
| DATE1_10 | DOUBLE | 100.0% |  |  |
| DATE1_11 | DOUBLE | 100.0% |  |  |
| DATE1_12 | DOUBLE | 100.0% |  |  |
| DATE1_13 | DOUBLE | 100.0% |  |  |
| DATE1_14 | DOUBLE | 100.0% |  |  |
| DATE1_15 | DOUBLE | 100.0% |  |  |
| DATE1_16 | DOUBLE | 100.0% |  |  |
| DATE1_17 | DOUBLE | 100.0% |  |  |
| DATE1_18 | DOUBLE | 100.0% |  |  |
| DATE1_19 | DOUBLE | 100.0% |  |  |
| DATE1_20 | DOUBLE | 100.0% |  |  |
| DATE1_21 | DOUBLE | 100.0% |  |  |
| DATE1_22 | DOUBLE | 100.0% |  |  |
| DATE1_23 | DOUBLE | 100.0% |  |  |
| DATE1_24 | DOUBLE | 100.0% |  |  |
| DATE1_25 | DOUBLE | 100.0% |  |  |
| DATE1_26 | DOUBLE | 100.0% |  |  |
| DATE1_27 | DOUBLE | 100.0% |  |  |
| DATE1_28 | DOUBLE | 100.0% |  |  |
| DATE1_29 | DOUBLE | 100.0% |  |  |
| DATE1_30 | DOUBLE | 100.0% |  |  |
| DATE1_31 | DOUBLE | 100.0% |  |  |
| DATE1_32 | DOUBLE | 100.0% |  |  |
| DATE1_33 | DOUBLE | 100.0% |  |  |
| DATE1_34 | DOUBLE | 100.0% |  |  |
| DATE1_35 | DOUBLE | 100.0% |  |  |
| DATE1_36 | DOUBLE | 100.0% |  |  |
| DATE1_37 | DOUBLE | 100.0% |  |  |
| DATE1_38 | DOUBLE | 100.0% |  |  |
| DATE1_39 | DOUBLE | 100.0% |  |  |
| DATE1_40 | DOUBLE | 100.0% |  |  |
| DATE1_41 | DOUBLE | 100.0% |  |  |
| DATE1_42 | DOUBLE | 100.0% |  |  |
| DATE1_43 | DOUBLE | 100.0% |  |  |
| DATE1_44 | DOUBLE | 100.0% |  |  |
| DATE1_45 | DOUBLE | 100.0% |  |  |
| DATE1_46 | DOUBLE | 100.0% |  |  |
| DATE1_47 | DOUBLE | 100.0% |  |  |
| DATE1_48 | DOUBLE | 100.0% |  |  |
| DATE1_49 | DOUBLE | 100.0% |  |  |
| DATE1_50 | DOUBLE | 100.0% |  |  |
| DATE1_51 | DOUBLE | 100.0% |  |  |
| DATE1_52 | DOUBLE | 100.0% |  |  |
| DATE1_53 | DOUBLE | 100.0% |  |  |
| DATE1_54 | DOUBLE | 100.0% |  |  |
| DATE1_55 | DOUBLE | 100.0% |  |  |
| DATE1_56 | DOUBLE | 100.0% |  |  |
| DATE1_57 | DOUBLE | 100.0% |  |  |
| DATE1_58 | DOUBLE | 100.0% |  |  |
| DATE1_59 | DOUBLE | 100.0% |  |  |
| DATE1_60 | DOUBLE | 100.0% |  |  |
| DATE1_61 | DOUBLE | 100.0% |  |  |
| DATE1_62 | DOUBLE | 100.0% |  |  |
| DATE1_63 | DOUBLE | 100.0% |  |  |
| DATE1_64 | DOUBLE | 100.0% |  |  |
| DATE1_65 | DOUBLE | 100.0% |  |  |
| DATE1_66 | DOUBLE | 100.0% |  |  |
| DATE1_67 | DOUBLE | 100.0% |  |  |
| DATE1_68 | DOUBLE | 100.0% |  |  |
| DATE1_69 | DOUBLE | 100.0% |  |  |
| DATE1_70 | DOUBLE | 100.0% |  |  |
| DATE1_71 | DOUBLE | 100.0% |  |  |
| DATE1_72 | DOUBLE | 100.0% |  |  |
| DATE1_73 | DOUBLE | 100.0% |  |  |
| DATE1_74 | DOUBLE | 100.0% |  |  |
| DATE1_75 | DOUBLE | 100.0% |  |  |
| DATE1_76 | DOUBLE | 100.0% |  |  |
| DATE1_77 | DOUBLE | 100.0% |  |  |
| DATE1_78 | DOUBLE | 100.0% |  |  |
| DATE1_79 | DOUBLE | 100.0% |  |  |
| DATE1_80 | DOUBLE | 100.0% |  |  |
| DATE1_81 | DOUBLE | 100.0% |  |  |
| DATE1_82 | DOUBLE | 100.0% |  |  |
| DATE1_83 | DOUBLE | 100.0% |  |  |
| DATE1_84 | DOUBLE | 100.0% |  |  |
| DATE1_85 | DOUBLE | 100.0% |  |  |
| DATE1_86 | DOUBLE | 100.0% |  |  |
| DATE1_87 | DOUBLE | 100.0% |  |  |
| DATE1_88 | DOUBLE | 100.0% |  |  |
| DATE1_89 | DOUBLE | 100.0% |  |  |
| DATE1_90 | DOUBLE | 100.0% |  |  |
| DATE1_91 | DOUBLE | 100.0% |  |  |
| DATE1_92 | DOUBLE | 100.0% |  |  |
| DATE1_93 | DOUBLE | 100.0% |  |  |
| DATE1_94 | DOUBLE | 100.0% |  |  |
| DATE1_95 | DOUBLE | 100.0% |  |  |
| DATE1_96 | DOUBLE | 100.0% |  |  |
| DATE1_97 | DOUBLE | 100.0% |  |  |
| DATE1_98 | DOUBLE | 100.0% |  |  |
| DATE1_99 | DOUBLE | 100.0% |  |  |
| DATE1_100 | DOUBLE | 100.0% |  |  |
| DATE1_101 | DOUBLE | 100.0% |  |  |
| DATE1_102 | DOUBLE | 100.0% |  |  |
| DATE1_103 | DOUBLE | 100.0% |  |  |
| DATE1_104 | DOUBLE | 100.0% |  |  |
| DATE1_105 | DOUBLE | 100.0% |  |  |
| DATE1_106 | DOUBLE | 100.0% |  |  |
| DATE1_107 | DOUBLE | 100.0% |  |  |
| DATE1_108 | DOUBLE | 100.0% |  |  |
| DATE1_109 | DOUBLE | 100.0% |  |  |
| DATE1_110 | DOUBLE | 100.0% |  |  |
| DATE1_111 | DOUBLE | 100.0% |  |  |
| DATE1_112 | DOUBLE | 100.0% |  |  |
| DATE1_113 | DOUBLE | 100.0% |  |  |
| DATE1_114 | DOUBLE | 100.0% |  |  |
| DATE1_115 | DOUBLE | 100.0% |  |  |
| DATE1_116 | DOUBLE | 100.0% |  |  |
| DATE1_117 | DOUBLE | 100.0% |  |  |
| DATE1_118 | DOUBLE | 100.0% |  |  |
| DATE1_119 | DOUBLE | 100.0% |  |  |
| DATE1_120 | DOUBLE | 100.0% |  |  |
| DATE1_121 | DOUBLE | 100.0% |  |  |
| DATE1_122 | DOUBLE | 100.0% |  |  |
| DATE1_123 | DOUBLE | 100.0% |  |  |
| DATE1_124 | DOUBLE | 100.0% |  |  |
| DATE1_125 | DOUBLE | 100.0% |  |  |
| DATE1_126 | DOUBLE | 100.0% |  |  |
| DATE1_127 | DOUBLE | 100.0% |  |  |
| DATE1_128 | DOUBLE | 100.0% |  |  |
| DATE1_129 | DOUBLE | 100.0% |  |  |
| DATE1_130 | DOUBLE | 100.0% |  |  |
| DATE1_131 | DOUBLE | 100.0% |  |  |
| DATE1_132 | DOUBLE | 100.0% |  |  |
| DATE1_133 | DOUBLE | 100.0% |  |  |
| DATE1_134 | DOUBLE | 100.0% |  |  |
| DATE1_135 | DOUBLE | 100.0% |  |  |
| DATE1_136 | DOUBLE | 100.0% |  |  |
| DATE1_137 | DOUBLE | 100.0% |  |  |
| DATE1_138 | DOUBLE | 100.0% |  |  |
| DATE1_139 | DOUBLE | 100.0% |  |  |
| DATE1_140 | DOUBLE | 100.0% |  |  |
| DATE1_141 | DOUBLE | 100.0% |  |  |
| DATE1_142 | DOUBLE | 100.0% |  |  |
| DATE1_143 | DOUBLE | 100.0% |  |  |
| DATE1_144 | DOUBLE | 100.0% |  |  |
| DATE1_145 | DOUBLE | 100.0% |  |  |
| DATE1_146 | DOUBLE | 100.0% |  |  |
| DATE1_147 | DOUBLE | 100.0% |  |  |
| DATE1_148 | DOUBLE | 100.0% |  |  |
| DATE1_149 | DOUBLE | 100.0% |  |  |
| DATE1_150 | DOUBLE | 100.0% |  |  |
| DATE1_151 | DOUBLE | 100.0% |  |  |
| DATE1_152 | DOUBLE | 100.0% |  |  |
| DATE1_153 | DOUBLE | 100.0% |  |  |
| DATE1_154 | DOUBLE | 100.0% |  |  |
| DATE1_155 | DOUBLE | 100.0% |  |  |
| DATE1_156 | DOUBLE | 100.0% |  |  |
| DATE1_157 | DOUBLE | 100.0% |  |  |
| DATE1_158 | DOUBLE | 100.0% |  |  |
| DATE1_159 | DOUBLE | 100.0% |  |  |
| DATE1_160 | DOUBLE | 100.0% |  |  |
| DATE1_161 | DOUBLE | 100.0% |  |  |
| DATE1_162 | DOUBLE | 100.0% |  |  |
| DATE1_163 | DOUBLE | 100.0% |  |  |
| DATE1_164 | DOUBLE | 100.0% |  |  |
| DATE1_165 | DOUBLE | 100.0% |  |  |
| DATE1_166 | DOUBLE | 100.0% |  |  |
| DATE1_167 | DOUBLE | 100.0% |  |  |
| DATE1_168 | DOUBLE | 100.0% |  |  |
| DATE1_169 | DOUBLE | 100.0% |  |  |
| DATE1_170 | DOUBLE | 100.0% |  |  |
| DATE1_171 | DOUBLE | 100.0% |  |  |
| DATE1_172 | DOUBLE | 100.0% |  |  |
| DATE1_173 | DOUBLE | 100.0% |  |  |
| DATE1_174 | DOUBLE | 100.0% |  |  |
| DATE1_175 | DOUBLE | 100.0% |  |  |
| DATE1_176 | DOUBLE | 100.0% |  |  |
| DATE1_177 | DOUBLE | 100.0% |  |  |
| DATE1_178 | DOUBLE | 100.0% |  |  |
| DATE1_179 | DOUBLE | 100.0% |  |  |
| DATE1_180 | DOUBLE | 100.0% |  |  |
| DATE1_181 | DOUBLE | 100.0% |  |  |
| DATE1_182 | DOUBLE | 100.0% |  |  |
| DATE1_183 | DOUBLE | 100.0% |  |  |
| DATE1_184 | DOUBLE | 100.0% |  |  |
| DATE1_185 | DOUBLE | 100.0% |  |  |
| DATE1_186 | DOUBLE | 100.0% |  |  |
| DATE1_187 | DOUBLE | 100.0% |  |  |
| DATE1_188 | DOUBLE | 100.0% |  |  |
| DATE1_189 | DOUBLE | 100.0% |  |  |
| DATE1_190 | DOUBLE | 100.0% |  |  |
| DATE1_191 | DOUBLE | 100.0% |  |  |
| DATE1_192 | DOUBLE | 100.0% |  |  |
| DATE1_193 | DOUBLE | 100.0% |  |  |
| DATE1_194 | DOUBLE | 100.0% |  |  |
| DATE1_195 | DOUBLE | 100.0% |  |  |
| DATE1_196 | DOUBLE | 100.0% |  |  |
| DATE1_197 | DOUBLE | 100.0% |  |  |
| DATE1_198 | DOUBLE | 100.0% |  |  |
| DATE1_199 | DOUBLE | 100.0% |  |  |
| DATE1_200 | DOUBLE | 100.0% |  |  |
| DATE1_201 | DOUBLE | 100.0% |  |  |
| DATE1_202 | DOUBLE | 100.0% |  |  |
| DATE1_203 | DOUBLE | 100.0% |  |  |
| DATE1_204 | DOUBLE | 100.0% |  |  |
| DATE1_205 | DOUBLE | 100.0% |  |  |
| DATE1_206 | DOUBLE | 100.0% |  |  |
| DATE1_207 | DOUBLE | 100.0% |  |  |
| DATE1_208 | DOUBLE | 100.0% |  |  |
| DATE1_209 | DOUBLE | 100.0% |  |  |
| DATE1_210 | DOUBLE | 100.0% |  |  |
| DATE1_211 | DOUBLE | 100.0% |  |  |
| DATE1_212 | DOUBLE | 100.0% |  |  |
| DATE1_213 | DOUBLE | 100.0% |  |  |
| DATE1_214 | DOUBLE | 100.0% |  |  |
| DATE1_215 | DOUBLE | 100.0% |  |  |
| DATE1_216 | DOUBLE | 100.0% |  |  |
| DATE1_217 | DOUBLE | 100.0% |  |  |
| DATE1_218 | DOUBLE | 100.0% |  |  |
| DATE1_219 | DOUBLE | 100.0% |  |  |
| DATE1_220 | DOUBLE | 100.0% |  |  |
| DATE1_221 | DOUBLE | 100.0% |  |  |
| DATE1_222 | DOUBLE | 100.0% |  |  |
| DATE1_223 | DOUBLE | 100.0% |  |  |
| DATE1_224 | DOUBLE | 100.0% |  |  |
| DATE1_225 | DOUBLE | 100.0% |  |  |
| DATE1_226 | DOUBLE | 100.0% |  |  |
| DATE1_227 | DOUBLE | 100.0% |  |  |
| DATE1_228 | DOUBLE | 100.0% |  |  |
| DATE1_229 | DOUBLE | 100.0% |  |  |
| DATE1_230 | DOUBLE | 100.0% |  |  |
| DATE1_231 | DOUBLE | 100.0% |  |  |
| DATE1_232 | DOUBLE | 100.0% |  |  |
| DATE1_233 | DOUBLE | 100.0% |  |  |
| DATE1_234 | DOUBLE | 100.0% |  |  |
| DATE1_235 | DOUBLE | 100.0% |  |  |
| DATE1_236 | DOUBLE | 100.0% |  |  |
| DATE1_237 | DOUBLE | 100.0% |  |  |
| DATE1_238 | DOUBLE | 100.0% |  |  |
| DATE1_239 | DOUBLE | 100.0% |  |  |
| DATE1_240 | DOUBLE | 100.0% |  |  |
| DATE1_241 | DOUBLE | 100.0% |  |  |
| DATE1_242 | DOUBLE | 100.0% |  |  |
| DATE1_243 | DOUBLE | 100.0% |  |  |
| DATE1_244 | DOUBLE | 100.0% |  |  |
| DATE1_245 | DOUBLE | 100.0% |  |  |
| DATE1_246 | DOUBLE | 100.0% |  |  |
| DATE1_247 | DOUBLE | 100.0% |  |  |
| DATE1_248 | DOUBLE | 100.0% |  |  |
| DATE1_249 | DOUBLE | 100.0% |  |  |
| DATE1_250 | DOUBLE | 100.0% |  |  |
| DATE1_251 | DOUBLE | 100.0% |  |  |
| DATE1_252 | DOUBLE | 100.0% |  |  |
| DATE1_253 | DOUBLE | 100.0% |  |  |
| DATE1_254 | DOUBLE | 100.0% |  |  |
| DATE1_255 | DOUBLE | 100.0% |  |  |
| DATE1_256 | DOUBLE | 100.0% |  |  |
| DATE1_257 | DOUBLE | 100.0% |  |  |
| DATE1_258 | DOUBLE | 100.0% |  |  |
| DATE1_259 | DOUBLE | 100.0% |  |  |
| DATE1_260 | DOUBLE | 100.0% |  |  |
| DATE1_261 | DOUBLE | 100.0% |  |  |
| DATE1_262 | DOUBLE | 100.0% |  |  |
| DATE1_263 | DOUBLE | 100.0% |  |  |
| DATE1_264 | DOUBLE | 100.0% |  |  |
| DATE1_265 | DOUBLE | 100.0% |  |  |
| DATE1_266 | DOUBLE | 100.0% |  |  |
| DATE1_267 | DOUBLE | 100.0% |  |  |
| OFEND | DOUBLE | 100.0% |  |  |
| DATE1_268 | DOUBLE | 100.0% |  |  |
| OFEND_1 | DOUBLE | 100.0% |  |  |
| DATE1_269 | DOUBLE | 100.0% |  |  |
| OFEND_2 | DOUBLE | 100.0% |  |  |
| DATE1_270 | DOUBLE | 100.0% |  |  |
| OFEND_3 | DOUBLE | 100.0% |  |  |
| DATE1_271 | DOUBLE | 100.0% |  |  |
| OFEND_4 | DOUBLE | 100.0% | 1.0 |  |
| DATE1_272 | DOUBLE | 100.0% |  |  |
| OFEND_5 | DOUBLE | 100.0% | 0.0 |  |
| DATE1_273 | DOUBLE | 100.0% |  |  |
| OFEND_6 | DOUBLE | 99.9% | 0.0 |  |
| DATE1_274 | DOUBLE | 100.0% |  |  |
| OFEND_7 | DOUBLE | 99.6% | 0.0 |  |
| DATE1_275 | DOUBLE | 100.0% |  |  |
| OFEND_8 | DOUBLE | 99.2% | 0.0 |  |
| DATE1_276 | DOUBLE | 100.0% |  |  |
| DATE1_277 | DOUBLE | 100.0% |  |  |
| DATE1_278 | DOUBLE | 100.0% |  |  |
| DATE1_279 | DOUBLE | 100.0% |  |  |
| DATE1_280 | DOUBLE | 100.0% |  |  |
| DATE1_281 | DOUBLE | 100.0% |  |  |
| DATE1_282 | DOUBLE | 100.0% |  |  |
| DATE1_283 | DOUBLE | 100.0% |  |  |
| DATE1_284 | DOUBLE | 100.0% |  |  |
| DATE1_285 | DOUBLE | 100.0% |  |  |
| DATE1_286 | DOUBLE | 100.0% |  |  |
| DATE1_287 | DOUBLE | 100.0% |  |  |
| DATE1_288 | DOUBLE | 100.0% |  |  |
| DATE1_289 | DOUBLE | 100.0% |  |  |
| DATE1_290 | DOUBLE | 100.0% |  |  |
| DATE1_291 | DOUBLE | 100.0% |  |  |
| DATE1_292 | DOUBLE | 100.0% |  |  |
| DATE1_293 | DOUBLE | 100.0% |  |  |
| DATE1_294 | DOUBLE | 100.0% |  |  |
| DATE1_295 | DOUBLE | 100.0% |  |  |
| DATE1_296 | DOUBLE | 100.0% |  |  |
| DATE1_297 | DOUBLE | 100.0% |  |  |
| DATE1_298 | DOUBLE | 100.0% |  |  |
| DATE1_299 | DOUBLE | 100.0% |  |  |
| DATE1_300 | DOUBLE | 100.0% |  |  |
| DATE1_301 | DOUBLE | 100.0% |  |  |
| DATE1_302 | DOUBLE | 100.0% |  |  |
| DATE1_303 | DOUBLE | 100.0% |  |  |
| DATE1_304 | DOUBLE | 100.0% |  |  |
| DATE1_305 | DOUBLE | 100.0% |  |  |
| DATE1_306 | DOUBLE | 100.0% |  |  |
| DATE1_307 | DOUBLE | 100.0% |  |  |
| DATE1_308 | DOUBLE | 100.0% |  |  |
| DATE1_309 | DOUBLE | 100.0% |  |  |
| DATE1_310 | DOUBLE | 100.0% |  |  |
| DATE1_311 | DOUBLE | 100.0% |  |  |
| DATE1_312 | DOUBLE | 100.0% |  |  |
| DATE1_313 | DOUBLE | 100.0% |  |  |
| DATE1_314 | DOUBLE | 100.0% |  |  |
| DATE1_315 | DOUBLE | 100.0% |  |  |
| DATE1_316 | DOUBLE | 100.0% |  |  |
| DATE1_317 | DOUBLE | 100.0% |  |  |
| DATE1_318 | DOUBLE | 100.0% |  |  |
| DATE1_319 | DOUBLE | 100.0% |  |  |
| DATE1_320 | DOUBLE | 100.0% |  |  |
| DATE1_321 | DOUBLE | 100.0% |  |  |
| DATE1_322 | DOUBLE | 100.0% |  |  |
| DATE1_323 | DOUBLE | 100.0% |  |  |
| DATE1_324 | DOUBLE | 100.0% |  |  |
| DATE1_325 | DOUBLE | 100.0% |  |  |
| DATE1_326 | DOUBLE | 100.0% |  |  |
| DATE1_327 | DOUBLE | 100.0% |  |  |
| DATE1_328 | DOUBLE | 100.0% |  |  |
| DATE1_329 | DOUBLE | 100.0% |  |  |
| DATE1_330 | DOUBLE | 100.0% |  |  |
| DATE1_331 | DOUBLE | 100.0% |  |  |
| DATE1_332 | DOUBLE | 100.0% |  |  |
| DATE1_333 | DOUBLE | 100.0% |  |  |
| DATE1_334 | DOUBLE | 100.0% |  |  |
| DATE1_335 | DOUBLE | 100.0% |  |  |
| DATE1_336 | DOUBLE | 100.0% |  |  |
| DATE1_337 | DOUBLE | 100.0% |  |  |
| DATE1_338 | DOUBLE | 100.0% |  |  |
| DATE1_339 | DOUBLE | 100.0% |  |  |
| DATE1_340 | DOUBLE | 100.0% |  |  |
| DATE1_341 | DOUBLE | 100.0% |  |  |
| DATE1_342 | DOUBLE | 100.0% |  |  |
| DATE1_343 | DOUBLE | 100.0% |  |  |
| DATE1_344 | DOUBLE | 100.0% |  |  |
| DATE1_345 | DOUBLE | 100.0% |  |  |
| DATE1_346 | DOUBLE | 100.0% |  |  |
| DATE1_347 | DOUBLE | 100.0% |  |  |
| DATE1_348 | DOUBLE | 100.0% |  |  |
| DATE1_349 | DOUBLE | 100.0% |  |  |
| DATE1_350 | DOUBLE | 100.0% |  |  |
| DATE1_351 | DOUBLE | 100.0% |  |  |
| DATE1_352 | DOUBLE | 100.0% |  |  |
| DATE1_353 | DOUBLE | 100.0% |  |  |
| DATE1_354 | DOUBLE | 100.0% |  |  |
| DATE1_355 | DOUBLE | 100.0% |  |  |
| DATE1_356 | DOUBLE | 100.0% |  |  |
| DATE1_357 | DOUBLE | 100.0% |  |  |
| DATE1_358 | DOUBLE | 100.0% |  |  |
| DATE1_359 | DOUBLE | 100.0% |  |  |
| DATE1_360 | DOUBLE | 100.0% |  |  |
| DATE1_361 | DOUBLE | 100.0% |  |  |
| DATE1_362 | DOUBLE | 100.0% |  |  |
| DATE1_363 | DOUBLE | 100.0% |  |  |
| DATE1_364 | DOUBLE | 100.0% |  |  |
| DATE1_365 | DOUBLE | 100.0% |  |  |
| DATE1_366 | DOUBLE | 100.0% |  |  |
| DATE1_367 | DOUBLE | 100.0% |  |  |
| DATE1_368 | DOUBLE | 100.0% |  |  |
| DATE1_369 | DOUBLE | 100.0% |  |  |
| DATE1_370 | DOUBLE | 100.0% |  |  |
| DATE1_371 | DOUBLE | 100.0% |  |  |
| DATE1_372 | DOUBLE | 100.0% |  |  |
| DATE1_373 | DOUBLE | 100.0% |  |  |
| DATE1_374 | DOUBLE | 100.0% |  |  |
| DATE1_375 | DOUBLE | 100.0% |  |  |
| DATE1_376 | DOUBLE | 100.0% |  |  |
| DATE1_377 | DOUBLE | 100.0% |  |  |
| DATE1_378 | DOUBLE | 100.0% |  |  |
| DATE1_379 | DOUBLE | 100.0% |  |  |
| DATE1_380 | DOUBLE | 100.0% |  |  |
| DATE1_381 | DOUBLE | 100.0% |  |  |
| DATE1_382 | DOUBLE | 100.0% |  |  |
| DATE1_383 | DOUBLE | 100.0% |  |  |
| DATE1_384 | DOUBLE | 100.0% |  |  |
| DATE1_385 | DOUBLE | 100.0% |  |  |
| DATE1_386 | DOUBLE | 100.0% |  |  |
| DATE1_387 | DOUBLE | 100.0% |  |  |
| DATE1_388 | DOUBLE | 100.0% |  |  |
| DATE1_389 | DOUBLE | 100.0% |  |  |
| DATE1_390 | DOUBLE | 100.0% |  |  |
| DATE1_391 | DOUBLE | 100.0% |  |  |
| DATE1_392 | DOUBLE | 100.0% |  |  |
| DATE1_393 | DOUBLE | 100.0% |  |  |
| DATE1_394 | DOUBLE | 100.0% |  |  |
| DATE1_395 | DOUBLE | 100.0% |  |  |
| DATE1_396 | DOUBLE | 100.0% |  |  |
| DATE1_397 | DOUBLE | 100.0% |  |  |
| DATE1_398 | DOUBLE | 100.0% |  |  |
| DATE1_399 | DOUBLE | 100.0% |  |  |
| DATE1_400 | DOUBLE | 100.0% |  |  |
| DATE1_401 | DOUBLE | 100.0% |  |  |
| DATE1_402 | DOUBLE | 100.0% |  |  |
| DATE1_403 | DOUBLE | 100.0% |  |  |
| DATE1_404 | DOUBLE | 100.0% |  |  |
| DATE1_405 | DOUBLE | 100.0% |  |  |
| DATE1_406 | DOUBLE | 100.0% |  |  |
| DATE1_407 | DOUBLE | 100.0% |  |  |
| DATE1_408 | DOUBLE | 100.0% |  |  |
| DATE1_409 | DOUBLE | 100.0% |  |  |
| DATE1_410 | DOUBLE | 100.0% |  |  |
| DATE1_411 | DOUBLE | 100.0% |  |  |
| DATE1_412 | DOUBLE | 100.0% |  |  |
| DATE1_413 | DOUBLE | 100.0% |  |  |
| DATE1_414 | DOUBLE | 100.0% |  |  |
| DATE1_415 | DOUBLE | 100.0% |  |  |
| DATE1_416 | DOUBLE | 100.0% |  |  |
| DATE1_417 | DOUBLE | 100.0% |  |  |
| DATE1_418 | DOUBLE | 100.0% |  |  |
| DATE1_419 | DOUBLE | 100.0% |  |  |
| DATE1_420 | DOUBLE | 100.0% |  |  |
| DATE1_421 | DOUBLE | 100.0% |  |  |
| DATE1_422 | DOUBLE | 100.0% |  |  |
| DATE1_423 | DOUBLE | 100.0% |  |  |
| DATE1_424 | DOUBLE | 100.0% |  |  |
| DATE1_425 | DOUBLE | 100.0% |  |  |
| DATE1_426 | DOUBLE | 100.0% |  |  |
| DATE1_427 | DOUBLE | 100.0% |  |  |
| DATE1_428 | DOUBLE | 100.0% |  |  |
| DATE1_429 | DOUBLE | 100.0% |  |  |
| DATE1_430 | DOUBLE | 100.0% |  |  |
| DATE1_431 | DOUBLE | 100.0% |  |  |
| DATE1_432 | DOUBLE | 100.0% |  |  |
| DATE1_433 | DOUBLE | 100.0% |  |  |
| DATE1_434 | DOUBLE | 100.0% |  |  |
| DATE1_435 | DOUBLE | 100.0% |  |  |
| DATE1_436 | DOUBLE | 100.0% |  |  |
| DATE1_437 | DOUBLE | 100.0% |  |  |
| DATE1_438 | DOUBLE | 100.0% |  |  |
| DATE1_439 | DOUBLE | 100.0% |  |  |
| DATE1_440 | DOUBLE | 100.0% |  |  |
| DATE1_441 | DOUBLE | 100.0% |  |  |
| DATE1_442 | DOUBLE | 100.0% |  |  |
| DATE1_443 | DOUBLE | 100.0% |  |  |
| DATE1_444 | DOUBLE | 100.0% |  |  |
| DATE1_445 | DOUBLE | 100.0% |  |  |
| DATE1_446 | DOUBLE | 100.0% |  |  |
| DATE1_447 | DOUBLE | 100.0% |  |  |
| DATE1_448 | DOUBLE | 100.0% |  |  |
| DATE1_449 | DOUBLE | 100.0% |  |  |
| DATE1_450 | DOUBLE | 100.0% |  |  |
| DATE1_451 | DOUBLE | 100.0% |  |  |
| DATE1_452 | DOUBLE | 100.0% |  |  |
| DATE1_453 | DOUBLE | 100.0% |  |  |
| DATE1_454 | DOUBLE | 100.0% |  |  |
| DATE1_455 | DOUBLE | 100.0% |  |  |
| DATE1_456 | DOUBLE | 100.0% |  |  |
| DATE1_457 | DOUBLE | 100.0% |  |  |
| DATE1_458 | DOUBLE | 100.0% |  |  |
| DATE1_459 | DOUBLE | 100.0% |  |  |
| DATE1_460 | DOUBLE | 100.0% |  |  |
| DATE1_461 | DOUBLE | 100.0% |  |  |
| DATE1_462 | DOUBLE | 100.0% |  |  |
| DATE1_463 | DOUBLE | 100.0% |  |  |
| DATE1_464 | DOUBLE | 100.0% |  |  |
| DATE1_465 | DOUBLE | 100.0% |  |  |
| DATE1_466 | DOUBLE | 100.0% |  |  |
| DATE1_467 | DOUBLE | 100.0% |  |  |
| DATE1_468 | DOUBLE | 100.0% |  |  |
| DATE1_469 | DOUBLE | 100.0% |  |  |
| DATE1_470 | DOUBLE | 100.0% |  |  |
| DATE1_471 | DOUBLE | 100.0% |  |  |
| DATE1_472 | DOUBLE | 100.0% |  |  |
| DATE1_473 | DOUBLE | 100.0% |  |  |
| DATE1_474 | DOUBLE | 100.0% |  |  |
| DATE1_475 | DOUBLE | 100.0% |  |  |
| DATE1_476 | DOUBLE | 100.0% |  |  |
| DATE1_477 | DOUBLE | 100.0% |  |  |
| DATE1_478 | DOUBLE | 100.0% |  |  |
| DATE1_479 | DOUBLE | 100.0% |  |  |
| DATE1_480 | DOUBLE | 100.0% |  |  |
| DATE1_481 | DOUBLE | 100.0% |  |  |
| DATE1_482 | DOUBLE | 100.0% |  |  |
| DATE1_483 | DOUBLE | 100.0% |  |  |
| DATE1_484 | DOUBLE | 100.0% |  |  |
| DATE1_485 | DOUBLE | 100.0% |  |  |
| DATE1_486 | DOUBLE | 100.0% |  |  |
| DATE1_487 | DOUBLE | 100.0% |  |  |
| DATE1_488 | DOUBLE | 100.0% |  |  |
| DATE1_489 | DOUBLE | 100.0% |  |  |
| DATE1_490 | DOUBLE | 100.0% |  |  |
| DATE1_491 | DOUBLE | 100.0% |  |  |
| DATE1_492 | DOUBLE | 100.0% |  |  |
| DATE1_493 | DOUBLE | 100.0% |  |  |
| DATE1_494 | DOUBLE | 100.0% |  |  |
| DATE1_495 | DOUBLE | 100.0% |  |  |
| DATE1_496 | DOUBLE | 100.0% |  |  |
| DATE1_497 | DOUBLE | 100.0% |  |  |
| DATE1_498 | DOUBLE | 100.0% |  |  |
| DATE1_499 | DOUBLE | 100.0% |  |  |
| DATE1_500 | DOUBLE | 100.0% |  |  |
| DATE1_501 | DOUBLE | 100.0% |  |  |
| DATE1_502 | DOUBLE | 100.0% |  |  |
| DATE1_503 | DOUBLE | 100.0% |  |  |
| DATE1_504 | DOUBLE | 100.0% |  |  |
| DATE1_505 | DOUBLE | 100.0% |  |  |
| DATE1_506 | DOUBLE | 100.0% |  |  |
| DATE1_507 | DOUBLE | 100.0% |  |  |
| DATE1_508 | DOUBLE | 100.0% |  |  |
| DATE1_509 | DOUBLE | 100.0% |  |  |
| DATE1_510 | DOUBLE | 100.0% |  |  |
| DATE1_511 | DOUBLE | 100.0% |  |  |
| DATE1_512 | DOUBLE | 100.0% |  |  |
| DATE1_513 | DOUBLE | 100.0% |  |  |
| DATE1_514 | DOUBLE | 100.0% |  |  |
| DATE1_515 | DOUBLE | 100.0% |  |  |
| DATE1_516 | DOUBLE | 100.0% |  |  |
| DATE1_517 | DOUBLE | 100.0% |  |  |
| DATE1_518 | DOUBLE | 100.0% |  |  |
| DATE1_519 | DOUBLE | 100.0% |  |  |
| DATE1_520 | DOUBLE | 100.0% |  |  |
| DATE1_521 | DOUBLE | 100.0% |  |  |
| DATE1_522 | DOUBLE | 100.0% |  |  |
| DATE1_523 | DOUBLE | 100.0% |  |  |
| DATE1_524 | DOUBLE | 100.0% |  |  |
| DATE1_525 | DOUBLE | 100.0% |  |  |
| DATE1_526 | DOUBLE | 100.0% |  |  |
| DATE1_527 | DOUBLE | 100.0% |  |  |
| DATE1_528 | DOUBLE | 100.0% |  |  |
| DATE1_529 | DOUBLE | 100.0% |  |  |
| DATE1_530 | DOUBLE | 100.0% |  |  |
| DATE1_531 | DOUBLE | 100.0% |  |  |
| DATE1_532 | DOUBLE | 100.0% |  |  |
| DATE1_533 | DOUBLE | 100.0% |  |  |
| CRPTS | DOUBLE | 7.0% | 0.0 |  |
| MWEIGHT | DOUBLE | 73.7% | 0.0075 |  |
| ARMCRIM | DOUBLE | 42.5% | -2.0 |  |
| CAROFFEN | DOUBLE | 42.0% | -1.0 |  |
| MONACCEP | DOUBLE | 18.8% | -1.0 |  |
| SEXACCA | DOUBLE | 42.9% | -2.0 |  |
| SEXACCB | DOUBLE | 42.9% | -2.0 |  |
| DEFCONTX | VARCHAR | 100.0% | Attorney at law |  |
| CHEMDES1 | VARCHAR | 100.0% | 1BOC4AP |  |
| CHEMDES2 | VARCHAR | 100.0% | Alprazolam |  |
| CHEMDES3 | VARCHAR | 100.0% | NAPTHA |  |
| CHEMDES4 | VARCHAR | 100.0% | NAPTHA |  |
| CHEMDES5 | VARCHAR | 100.0% |  |  |
| TYPEOTTX | VARCHAR | 99.9% | $10965 |  |
| CH5G13ST | DOUBLE | 43.5% | -5.0 |  |
| DATE1_534 | DOUBLE | 100.0% |  |  |
| DATE1_535 | DOUBLE | 100.0% |  |  |
| DATE1_536 | DOUBLE | 100.0% |  |  |
| DATE1_537 | DOUBLE | 100.0% |  |  |
| DATE1_538 | DOUBLE | 100.0% |  |  |
| DATE1_539 | DOUBLE | 100.0% |  |  |
| DATE1_540 | DOUBLE | 100.0% |  |  |
| DATE1_541 | DOUBLE | 100.0% |  |  |
| DATE1_542 | DOUBLE | 100.0% |  |  |
| DATE1_543 | DOUBLE | 100.0% |  |  |
| DATE1_544 | DOUBLE | 100.0% |  |  |
| DATE1_545 | DOUBLE | 100.0% |  |  |
| DATE1_546 | DOUBLE | 100.0% |  |  |
| DATE1_547 | DOUBLE | 100.0% |  |  |
| DATE1_548 | DOUBLE | 100.0% |  |  |
| DATE1_549 | DOUBLE | 100.0% |  |  |
| DATE1_550 | DOUBLE | 100.0% |  |  |
| DATE1_551 | DOUBLE | 100.0% |  |  |
| DATE1_552 | DOUBLE | 100.0% |  |  |
| DATE1_553 | DOUBLE | 100.0% |  |  |
| DATE1_554 | DOUBLE | 100.0% |  |  |
| DATE1_555 | DOUBLE | 100.0% |  |  |
| DATE1_556 | DOUBLE | 100.0% |  |  |
| DATE1_557 | DOUBLE | 100.0% |  |  |
| DATE1_558 | DOUBLE | 100.0% |  |  |
| DATE1_559 | DOUBLE | 100.0% |  |  |
| DATE1_560 | DOUBLE | 100.0% |  |  |
| DATE1_561 | DOUBLE | 100.0% |  |  |
| DATE1_562 | DOUBLE | 100.0% |  |  |
| DATE1_563 | DOUBLE | 100.0% |  |  |
| DATE1_564 | DOUBLE | 100.0% |  |  |
| DATE1_565 | DOUBLE | 100.0% |  |  |
| DATE1_566 | DOUBLE | 100.0% |  |  |
| DATE1_567 | DOUBLE | 100.0% |  |  |
| DATE1_568 | DOUBLE | 100.0% |  |  |
| DATE1_569 | DOUBLE | 100.0% |  |  |
| DATE1_570 | DOUBLE | 100.0% |  |  |
| DATE1_571 | DOUBLE | 100.0% |  |  |
| DATE1_572 | DOUBLE | 100.0% |  |  |
| DATE1_573 | DOUBLE | 100.0% |  |  |
| DATE1_574 | DOUBLE | 100.0% |  |  |
| DATE1_575 | DOUBLE | 100.0% |  |  |
| DATE1_576 | DOUBLE | 100.0% |  |  |
| DATE1_577 | DOUBLE | 100.0% |  |  |
| DATE1_578 | DOUBLE | 100.0% |  |  |
| DATE1_579 | DOUBLE | 100.0% |  |  |
| DATE1_580 | DOUBLE | 100.0% |  |  |
| DATE1_581 | DOUBLE | 100.0% |  |  |
| DATE1_582 | DOUBLE | 100.0% |  |  |
| DATE1_583 | DOUBLE | 100.0% |  |  |
| DATE1_584 | DOUBLE | 100.0% |  |  |
| DATE1_585 | DOUBLE | 100.0% |  |  |
| DATE1_586 | DOUBLE | 100.0% |  |  |
| DATE1_587 | DOUBLE | 100.0% |  |  |
| DATE1_588 | DOUBLE | 100.0% |  |  |
| DATE1_589 | DOUBLE | 100.0% |  |  |
| DATE1_590 | DOUBLE | 100.0% |  |  |
| DATE1_591 | DOUBLE | 100.0% |  |  |
| DATE1_592 | DOUBLE | 100.0% |  |  |
| DATE1_593 | DOUBLE | 100.0% |  |  |
| DATE1_594 | DOUBLE | 100.0% |  |  |
| DATE1_595 | DOUBLE | 100.0% |  |  |
| DATE1_596 | DOUBLE | 100.0% |  |  |
| DATE1_597 | DOUBLE | 100.0% |  |  |
| DATE1_598 | DOUBLE | 100.0% |  |  |
| DATE1_599 | DOUBLE | 100.0% |  |  |
| DATE1_600 | DOUBLE | 100.0% |  |  |
| DATE1_601 | DOUBLE | 100.0% |  |  |
| DATE1_602 | DOUBLE | 100.0% |  |  |
| DATE1_603 | DOUBLE | 100.0% |  |  |
| DATE1_604 | DOUBLE | 100.0% |  |  |
| DATE1_605 | DOUBLE | 100.0% |  |  |
| DATE1_606 | DOUBLE | 100.0% |  |  |
| DATE1_607 | DOUBLE | 100.0% |  |  |
| DATE1_608 | DOUBLE | 100.0% |  |  |
| DATE1_609 | DOUBLE | 100.0% |  |  |
| DATE1_610 | DOUBLE | 100.0% |  |  |
| DATE1_611 | DOUBLE | 100.0% |  |  |
| DATE1_612 | DOUBLE | 100.0% |  |  |
| DATE1_613 | DOUBLE | 100.0% |  |  |
| DATE1_614 | DOUBLE | 100.0% |  |  |
| DATE1_615 | DOUBLE | 100.0% |  |  |
| DATE1_616 | DOUBLE | 100.0% |  |  |
| DATE1_617 | DOUBLE | 100.0% |  |  |
| DATE1_618 | DOUBLE | 100.0% |  |  |
| DATE1_619 | DOUBLE | 100.0% |  |  |
| DATE1_620 | DOUBLE | 100.0% |  |  |
| DATE1_621 | DOUBLE | 100.0% |  |  |
| DATE1_622 | DOUBLE | 100.0% |  |  |
| DATE1_623 | DOUBLE | 100.0% |  |  |
| DATE1_624 | DOUBLE | 100.0% |  |  |
| DATE1_625 | DOUBLE | 100.0% |  |  |
| DATE1_626 | DOUBLE | 100.0% |  |  |
| DATE1_627 | DOUBLE | 100.0% |  |  |
| DATE1_628 | DOUBLE | 100.0% |  |  |
| DATE1_629 | DOUBLE | 100.0% |  |  |
| DATE1_630 | DOUBLE | 100.0% |  |  |
| DATE1_631 | DOUBLE | 100.0% |  |  |
| DATE1_632 | DOUBLE | 100.0% |  |  |
| DATE1_633 | DOUBLE | 100.0% |  |  |
| DATE1_634 | DOUBLE | 100.0% |  |  |
| DATE1_635 | DOUBLE | 100.0% |  |  |
| DATE1_636 | DOUBLE | 100.0% |  |  |
| DATE1_637 | DOUBLE | 100.0% |  |  |
| DATE1_638 | DOUBLE | 100.0% |  |  |
| DATE1_639 | DOUBLE | 100.0% |  |  |
| DATE1_640 | DOUBLE | 100.0% |  |  |
| DATE1_641 | DOUBLE | 100.0% |  |  |
| DATE1_642 | DOUBLE | 100.0% |  |  |
| DATE1_643 | DOUBLE | 100.0% |  |  |
| DATE1_644 | DOUBLE | 100.0% |  |  |
| DATE1_645 | DOUBLE | 100.0% |  |  |
| DATE1_646 | DOUBLE | 100.0% |  |  |
| DATE1_647 | DOUBLE | 100.0% |  |  |
| DATE1_648 | DOUBLE | 100.0% |  |  |
| DATE1_649 | DOUBLE | 100.0% |  |  |
| DATE1_650 | DOUBLE | 100.0% |  |  |
| DATE1_651 | DOUBLE | 100.0% |  |  |
| DATE1_652 | DOUBLE | 100.0% |  |  |
| DATE1_653 | DOUBLE | 100.0% |  |  |
| DATE1_654 | DOUBLE | 100.0% |  |  |
| DATE1_655 | DOUBLE | 100.0% |  |  |
| DATE1_656 | DOUBLE | 100.0% |  |  |
| DATE1_657 | DOUBLE | 100.0% |  |  |
| DATE1_658 | DOUBLE | 100.0% |  |  |
| DATE1_659 | DOUBLE | 100.0% |  |  |
| DATE1_660 | DOUBLE | 100.0% |  |  |
| DATE1_661 | DOUBLE | 100.0% |  |  |
| DATE1_662 | DOUBLE | 100.0% |  |  |
| DATE1_663 | DOUBLE | 100.0% |  |  |
| DATE1_664 | DOUBLE | 100.0% |  |  |
| DATE1_665 | DOUBLE | 100.0% |  |  |
| DATE1_666 | DOUBLE | 100.0% |  |  |
| DATE1_667 | DOUBLE | 100.0% |  |  |
| DATE1_668 | DOUBLE | 100.0% |  |  |
| DATE1_669 | DOUBLE | 100.0% |  |  |
| DATE1_670 | DOUBLE | 100.0% |  |  |
| DATE1_671 | DOUBLE | 100.0% |  |  |
| DATE1_672 | DOUBLE | 100.0% |  |  |
| DATE1_673 | DOUBLE | 100.0% |  |  |
| DATE1_674 | DOUBLE | 100.0% |  |  |
| DATE1_675 | DOUBLE | 100.0% |  |  |
| DATE1_676 | DOUBLE | 100.0% |  |  |
| DATE1_677 | DOUBLE | 100.0% |  |  |
| DATE1_678 | DOUBLE | 100.0% |  |  |
| DATE1_679 | DOUBLE | 100.0% |  |  |
| DATE1_680 | DOUBLE | 100.0% |  |  |
| DATE1_681 | DOUBLE | 100.0% |  |  |
| DATE1_682 | DOUBLE | 100.0% |  |  |
| DATE1_683 | DOUBLE | 100.0% |  |  |
| DATE1_684 | DOUBLE | 100.0% |  |  |
| DATE1_685 | DOUBLE | 100.0% |  |  |
| DATE1_686 | DOUBLE | 100.0% |  |  |
| DATE1_687 | DOUBLE | 100.0% |  |  |
| DATE1_688 | DOUBLE | 100.0% |  |  |
| DATE1_689 | DOUBLE | 100.0% |  |  |
| DATE1_690 | DOUBLE | 100.0% |  |  |
| DATE1_691 | DOUBLE | 100.0% |  |  |
| DATE1_692 | DOUBLE | 100.0% |  |  |
| DATE1_693 | DOUBLE | 100.0% |  |  |
| DATE1_694 | DOUBLE | 100.0% |  |  |
| DATE1_695 | DOUBLE | 100.0% |  |  |
| DATE1_696 | DOUBLE | 100.0% |  |  |
| DATE1_697 | DOUBLE | 100.0% |  |  |
| DATE1_698 | DOUBLE | 100.0% |  |  |
| DATE1_699 | DOUBLE | 100.0% |  |  |
| DATE1_700 | DOUBLE | 100.0% |  |  |
| DATE1_701 | DOUBLE | 100.0% |  |  |
| DATE1_702 | DOUBLE | 100.0% |  |  |
| DATE1_703 | DOUBLE | 100.0% |  |  |
| DATE1_704 | DOUBLE | 100.0% |  |  |
| DATE1_705 | DOUBLE | 100.0% |  |  |
| DATE1_706 | DOUBLE | 100.0% |  |  |
| DATE1_707 | DOUBLE | 100.0% |  |  |
| DATE1_708 | DOUBLE | 100.0% |  |  |
| DATE1_709 | DOUBLE | 100.0% |  |  |
| DATE1_710 | DOUBLE | 100.0% |  |  |
| DATE1_711 | DOUBLE | 100.0% |  |  |
| DATE1_712 | DOUBLE | 100.0% |  |  |
| DATE1_713 | DOUBLE | 100.0% |  |  |
| DATE1_714 | DOUBLE | 100.0% |  |  |
| DATE1_715 | DOUBLE | 100.0% |  |  |
| DATE1_716 | DOUBLE | 100.0% |  |  |
| DATE1_717 | DOUBLE | 100.0% |  |  |
| DATE1_718 | DOUBLE | 100.0% |  |  |
| DATE1_719 | DOUBLE | 100.0% |  |  |
| DATE1_720 | DOUBLE | 100.0% |  |  |
| DATE1_721 | DOUBLE | 100.0% |  |  |
| DATE1_722 | DOUBLE | 100.0% |  |  |
| DATE1_723 | DOUBLE | 100.0% |  |  |
| DATE1_724 | DOUBLE | 100.0% |  |  |
| DATE1_725 | DOUBLE | 100.0% |  |  |
| DATE1_726 | DOUBLE | 100.0% |  |  |
| DATE1_727 | DOUBLE | 100.0% |  |  |
| DATE1_728 | DOUBLE | 100.0% |  |  |
| DATE1_729 | DOUBLE | 100.0% |  |  |
| DATE1_730 | DOUBLE | 100.0% |  |  |
| DATE1_731 | DOUBLE | 100.0% |  |  |
| DATE1_732 | DOUBLE | 100.0% |  |  |
| DATE1_733 | DOUBLE | 100.0% |  |  |
| DATE1_734 | DOUBLE | 100.0% |  |  |
| DATE1_735 | DOUBLE | 100.0% |  |  |
| DATE1_736 | DOUBLE | 100.0% |  |  |
| DATE1_737 | DOUBLE | 100.0% |  |  |
| DATE1_738 | DOUBLE | 100.0% |  |  |
| DATE1_739 | DOUBLE | 100.0% |  |  |
| DATE1_740 | DOUBLE | 100.0% |  |  |
| DATE1_741 | DOUBLE | 100.0% |  |  |
| DATE1_742 | DOUBLE | 100.0% |  |  |
| DATE1_743 | DOUBLE | 100.0% |  |  |
| DATE1_744 | DOUBLE | 100.0% |  |  |
| DATE1_745 | DOUBLE | 100.0% |  |  |
| DATE1_746 | DOUBLE | 100.0% |  |  |
| DATE1_747 | DOUBLE | 100.0% |  |  |
| DATE1_748 | DOUBLE | 100.0% |  |  |
| DATE1_749 | DOUBLE | 100.0% |  |  |
| DATE1_750 | DOUBLE | 100.0% |  |  |
| DATE1_751 | DOUBLE | 100.0% |  |  |
| DATE1_752 | DOUBLE | 100.0% |  |  |
| DATE1_753 | DOUBLE | 100.0% |  |  |
| DATE1_754 | DOUBLE | 100.0% |  |  |
| DATE1_755 | DOUBLE | 100.0% |  |  |
| DATE1_756 | DOUBLE | 100.0% |  |  |
| DATE1_757 | DOUBLE | 100.0% |  |  |
| DATE1_758 | DOUBLE | 100.0% |  |  |
| DATE1_759 | DOUBLE | 100.0% |  |  |
| DATE1_760 | DOUBLE | 100.0% |  |  |
| DATE1_761 | DOUBLE | 100.0% |  |  |
| DATE1_762 | DOUBLE | 100.0% |  |  |
| DATE1_763 | DOUBLE | 100.0% |  |  |
| DATE1_764 | DOUBLE | 100.0% |  |  |
| DATE1_765 | DOUBLE | 100.0% |  |  |
| DATE1_766 | DOUBLE | 100.0% |  |  |
| DATE1_767 | DOUBLE | 100.0% |  |  |
| DATE1_768 | DOUBLE | 100.0% |  |  |
| DATE1_769 | DOUBLE | 100.0% |  |  |
| DATE1_770 | DOUBLE | 100.0% |  |  |
| DATE1_771 | DOUBLE | 100.0% |  |  |
| DATE1_772 | DOUBLE | 100.0% |  |  |
| DATE1_773 | DOUBLE | 100.0% |  |  |
| DATE1_774 | DOUBLE | 100.0% |  |  |
| DATE1_775 | DOUBLE | 100.0% |  |  |
| DATE1_776 | DOUBLE | 100.0% |  |  |
| DATE1_777 | DOUBLE | 100.0% |  |  |
| DATE1_778 | DOUBLE | 100.0% |  |  |
| DATE1_779 | DOUBLE | 100.0% |  |  |
| DATE1_780 | DOUBLE | 100.0% |  |  |
| DATE1_781 | DOUBLE | 100.0% |  |  |
| DATE1_782 | DOUBLE | 100.0% |  |  |
| DATE1_783 | DOUBLE | 100.0% |  |  |
| DATE1_784 | DOUBLE | 100.0% |  |  |
| DATE1_785 | DOUBLE | 100.0% |  |  |
| DATE1_786 | DOUBLE | 100.0% |  |  |
| DATE1_787 | DOUBLE | 100.0% |  |  |
| DATE1_788 | DOUBLE | 100.0% |  |  |
| DATE1_789 | DOUBLE | 100.0% |  |  |
| DATE1_790 | DOUBLE | 100.0% |  |  |
| DATE1_791 | DOUBLE | 100.0% |  |  |
| DATE1_792 | DOUBLE | 100.0% |  |  |
| DATE1_793 | DOUBLE | 100.0% |  |  |
| DATE1_794 | DOUBLE | 100.0% |  |  |
| DATE1_795 | DOUBLE | 100.0% |  |  |
| DATE1_796 | DOUBLE | 100.0% |  |  |
| DATE1_797 | DOUBLE | 100.0% |  |  |
| DATE1_798 | DOUBLE | 100.0% |  |  |
| DATE1_799 | DOUBLE | 100.0% |  |  |
| DATE1_800 | DOUBLE | 100.0% |  |  |
| DATE1_801 | DOUBLE | 100.0% |  |  |
| DATE1_802 | DOUBLE | 100.0% |  |  |
| DATE1_803 | DOUBLE | 100.0% |  |  |
| DATE1_804 | DOUBLE | 100.0% |  |  |
| DATE1_805 | DOUBLE | 100.0% |  |  |
| DATE1_806 | DOUBLE | 100.0% |  |  |
| DATE1_807 | DOUBLE | 100.0% |  |  |
| DATE1_808 | DOUBLE | 100.0% |  |  |
| DATE1_809 | DOUBLE | 100.0% |  |  |
| DATE1_810 | DOUBLE | 100.0% |  |  |
| DATE1_811 | DOUBLE | 100.0% |  |  |
| DATE1_812 | DOUBLE | 100.0% |  |  |
| DATE1_813 | DOUBLE | 100.0% |  |  |
| DATE1_814 | DOUBLE | 100.0% |  |  |
| DATE1_815 | DOUBLE | 100.0% |  |  |
| DATE1_816 | DOUBLE | 100.0% |  |  |
| DATE1_817 | DOUBLE | 100.0% |  |  |
| DATE1_818 | DOUBLE | 100.0% |  |  |
| DATE1_819 | DOUBLE | 100.0% |  |  |
| DATE1_820 | DOUBLE | 100.0% |  |  |
| DATE1_821 | DOUBLE | 100.0% |  |  |
| DATE1_822 | DOUBLE | 100.0% |  |  |
| DATE1_823 | DOUBLE | 100.0% |  |  |
| DATE1_824 | DOUBLE | 100.0% |  |  |
| DATE1_825 | DOUBLE | 100.0% |  |  |
| DATE1_826 | DOUBLE | 100.0% |  |  |
| DATE1_827 | DOUBLE | 100.0% |  |  |
| DATE1_828 | DOUBLE | 100.0% |  |  |
| DATE1_829 | DOUBLE | 100.0% |  |  |
| DATE1_830 | DOUBLE | 100.0% |  |  |
| DATE1_831 | DOUBLE | 100.0% |  |  |
| DATE1_832 | DOUBLE | 100.0% |  |  |
| DATE1_833 | DOUBLE | 100.0% |  |  |
| DATE1_834 | DOUBLE | 100.0% |  |  |
| DATE1_835 | DOUBLE | 100.0% |  |  |
| DATE1_836 | DOUBLE | 100.0% |  |  |
| DATE1_837 | DOUBLE | 100.0% |  |  |
| DATE1_838 | DOUBLE | 100.0% |  |  |
| DATE1_839 | DOUBLE | 100.0% |  |  |
| DATE1_840 | DOUBLE | 100.0% |  |  |
| DATE1_841 | DOUBLE | 100.0% |  |  |
| DATE1_842 | DOUBLE | 100.0% |  |  |
| DATE1_843 | DOUBLE | 100.0% |  |  |
| DATE1_844 | DOUBLE | 100.0% |  |  |
| DATE1_845 | DOUBLE | 100.0% |  |  |
| DATE1_846 | DOUBLE | 100.0% |  |  |
| DATE1_847 | DOUBLE | 100.0% |  |  |
| DATE1_848 | DOUBLE | 100.0% |  |  |
| DATE1_849 | DOUBLE | 100.0% |  |  |
| DATE1_850 | DOUBLE | 100.0% |  |  |
| DATE1_851 | DOUBLE | 100.0% |  |  |
| DATE1_852 | DOUBLE | 100.0% |  |  |
| DATE1_853 | DOUBLE | 100.0% |  |  |
| DATE1_854 | DOUBLE | 100.0% |  |  |
| DATE1_855 | DOUBLE | 100.0% |  |  |
| DATE1_856 | DOUBLE | 100.0% |  |  |
| DATE1_857 | DOUBLE | 100.0% |  |  |
| DATE1_858 | DOUBLE | 100.0% |  |  |
| DATE1_859 | DOUBLE | 100.0% |  |  |
| DATE1_860 | DOUBLE | 100.0% |  |  |
| DATE1_861 | DOUBLE | 100.0% |  |  |
| DATE1_862 | DOUBLE | 100.0% |  |  |
| DATE1_863 | DOUBLE | 100.0% |  |  |
| DATE1_864 | DOUBLE | 100.0% |  |  |
| DATE1_865 | DOUBLE | 100.0% |  |  |
| DATE1_866 | DOUBLE | 100.0% |  |  |
| DATE1_867 | DOUBLE | 100.0% |  |  |
| DATE1_868 | DOUBLE | 100.0% |  |  |
| DATE1_869 | DOUBLE | 100.0% |  |  |
| DATE1_870 | DOUBLE | 100.0% |  |  |
| DATE1_871 | DOUBLE | 100.0% |  |  |
| DATE1_872 | DOUBLE | 100.0% |  |  |
| DATE1_873 | DOUBLE | 100.0% |  |  |
| DATE1_874 | DOUBLE | 100.0% |  |  |
| DATE1_875 | DOUBLE | 100.0% |  |  |
| DATE1_876 | DOUBLE | 100.0% |  |  |
| DATE1_877 | DOUBLE | 100.0% |  |  |
| DATE1_878 | DOUBLE | 100.0% |  |  |
| DATE1_879 | DOUBLE | 100.0% |  |  |
| DATE1_880 | DOUBLE | 100.0% |  |  |
| DATE1_881 | DOUBLE | 100.0% |  |  |
| DATE1_882 | DOUBLE | 100.0% |  |  |
| DATE1_883 | DOUBLE | 100.0% |  |  |
| DATE1_884 | DOUBLE | 100.0% |  |  |
| DATE1_885 | DOUBLE | 100.0% |  |  |
| DATE1_886 | DOUBLE | 100.0% |  |  |
| DATE1_887 | DOUBLE | 100.0% |  |  |
| DATE1_888 | DOUBLE | 100.0% |  |  |
| DATE1_889 | DOUBLE | 100.0% |  |  |
| DATE1_890 | DOUBLE | 100.0% |  |  |
| DATE1_891 | DOUBLE | 100.0% |  |  |
| DATE1_892 | DOUBLE | 100.0% |  |  |
| DATE1_893 | DOUBLE | 100.0% |  |  |
| DATE1_894 | DOUBLE | 100.0% |  |  |
| DATE1_895 | DOUBLE | 100.0% |  |  |
| DATE1_896 | DOUBLE | 100.0% |  |  |
| DATE1_897 | DOUBLE | 100.0% |  |  |
| DATE1_898 | DOUBLE | 100.0% |  |  |
| DATE1_899 | DOUBLE | 100.0% |  |  |
| DATE1_900 | DOUBLE | 100.0% |  |  |
| DATE1_901 | DOUBLE | 100.0% |  |  |
| DATE1_902 | DOUBLE | 100.0% |  |  |
| DATE1_903 | DOUBLE | 100.0% |  |  |
| DATE1_904 | DOUBLE | 100.0% |  |  |
| DATE1_905 | DOUBLE | 100.0% |  |  |
| DATE1_906 | DOUBLE | 100.0% |  |  |
| DATE1_907 | DOUBLE | 100.0% |  |  |
| DATE1_908 | DOUBLE | 100.0% |  |  |
| DATE1_909 | DOUBLE | 100.0% |  |  |
| DATE1_910 | DOUBLE | 100.0% |  |  |
| DATE1_911 | DOUBLE | 100.0% |  |  |
| DATE1_912 | DOUBLE | 100.0% |  |  |
| DATE1_913 | DOUBLE | 100.0% |  |  |
| DATE1_914 | DOUBLE | 100.0% |  |  |
| DATE1_915 | DOUBLE | 100.0% |  |  |
| DATE1_916 | DOUBLE | 100.0% |  |  |
| DATE1_917 | DOUBLE | 100.0% |  |  |
| DATE1_918 | DOUBLE | 100.0% |  |  |
| DATE1_919 | DOUBLE | 100.0% |  |  |
| DATE1_920 | DOUBLE | 100.0% |  |  |
| DATE1_921 | DOUBLE | 100.0% |  |  |
| DATE1_922 | DOUBLE | 100.0% |  |  |
| DATE1_923 | DOUBLE | 100.0% |  |  |
| DATE1_924 | DOUBLE | 100.0% |  |  |
| DATE1_925 | DOUBLE | 100.0% |  |  |
| DATE1_926 | DOUBLE | 100.0% |  |  |
| DATE1_927 | DOUBLE | 100.0% |  |  |
| DATE1_928 | DOUBLE | 100.0% |  |  |
| DATE1_929 | DOUBLE | 100.0% |  |  |
| DATE1_930 | DOUBLE | 100.0% |  |  |
| DATE1_931 | DOUBLE | 100.0% |  |  |
| DATE1_932 | DOUBLE | 100.0% |  |  |
| DATE1_933 | DOUBLE | 100.0% |  |  |
| DATE1_934 | DOUBLE | 100.0% |  |  |
| DATE1_935 | DOUBLE | 100.0% |  |  |
| DATE1_936 | DOUBLE | 100.0% |  |  |
| DATE1_937 | DOUBLE | 100.0% |  |  |
| DATE1_938 | DOUBLE | 100.0% |  |  |
| DATE1_939 | DOUBLE | 100.0% |  |  |
| DATE1_940 | DOUBLE | 100.0% |  |  |
| DATE1_941 | DOUBLE | 100.0% |  |  |
| DATE1_942 | DOUBLE | 100.0% |  |  |
| DATE1_943 | DOUBLE | 100.0% |  |  |
| DATE1_944 | DOUBLE | 100.0% |  |  |
| DATE1_945 | DOUBLE | 100.0% |  |  |
| DATE1_946 | DOUBLE | 100.0% |  |  |
| DATE1_947 | DOUBLE | 100.0% |  |  |
| DATE1_948 | DOUBLE | 100.0% |  |  |
| DATE1_949 | DOUBLE | 100.0% |  |  |
| DATE1_950 | DOUBLE | 100.0% |  |  |
| DATE1_951 | DOUBLE | 100.0% |  |  |
| DATE1_952 | DOUBLE | 100.0% |  |  |
| DATE1_953 | DOUBLE | 100.0% |  |  |
| DATE1_954 | DOUBLE | 100.0% |  |  |
| DATE1_955 | DOUBLE | 100.0% |  |  |
| DATE1_956 | DOUBLE | 100.0% |  |  |
| DATE1_957 | DOUBLE | 100.0% |  |  |
| DATE1_958 | DOUBLE | 100.0% |  |  |
| DATE1_959 | DOUBLE | 100.0% |  |  |
| DATE1_960 | DOUBLE | 100.0% |  |  |
| DATE1_961 | DOUBLE | 100.0% |  |  |
| DATE1_962 | DOUBLE | 100.0% |  |  |
| DATE1_963 | DOUBLE | 100.0% |  |  |
| DATE1_964 | DOUBLE | 100.0% |  |  |
| DATE1_965 | DOUBLE | 100.0% |  |  |
| DATE1_966 | DOUBLE | 100.0% |  |  |
| DATE1_967 | DOUBLE | 100.0% |  |  |
| DATE1_968 | DOUBLE | 100.0% |  |  |
| DATE1_969 | DOUBLE | 100.0% |  |  |
| DATE1_970 | DOUBLE | 100.0% |  |  |
| DATE1_971 | DOUBLE | 100.0% |  |  |
| DATE1_972 | DOUBLE | 100.0% |  |  |
| DATE1_973 | DOUBLE | 100.0% |  |  |
| DATE1_974 | DOUBLE | 100.0% |  |  |
| DATE1_975 | DOUBLE | 100.0% |  |  |
| DATE1_976 | DOUBLE | 100.0% |  |  |
| DATE1_977 | DOUBLE | 100.0% |  |  |
| DATE1_978 | DOUBLE | 100.0% |  |  |
| DATE1_979 | DOUBLE | 100.0% |  |  |
| DATE1_980 | DOUBLE | 100.0% |  |  |
| DATE1_981 | DOUBLE | 100.0% |  |  |
| DATE1_982 | DOUBLE | 100.0% |  |  |
| DATE1_983 | DOUBLE | 100.0% |  |  |
| DATE1_984 | DOUBLE | 100.0% |  |  |
| DATE1_985 | DOUBLE | 100.0% |  |  |
| DATE1_986 | DOUBLE | 100.0% |  |  |
| DATE1_987 | DOUBLE | 100.0% |  |  |
| DATE1_988 | DOUBLE | 100.0% |  |  |
| DATE1_989 | DOUBLE | 100.0% |  |  |
| DATE1_990 | DOUBLE | 100.0% |  |  |
| DATE1_991 | DOUBLE | 100.0% |  |  |
| CH5G13YN | DOUBLE | 60.2% | 0.0 |  |
| DEPART_S | DOUBLE | 96.2% | 0.0 |  |
| DEPART_D | DOUBLE | 98.9% | 0.0 |  |
| FINEDUM | DOUBLE | 7.9% | 0.0 |  |
| SEXCAP | DOUBLE | 14.4% | 0.0 |  |
| MANDTXT1 | VARCHAR | 100.0% | 11c1c agreement |  |
| MANDTXT2 | VARCHAR | 100.0% | 1 |  |
| MANDTXT3 | VARCHAR | 100.0% | 1 |  |
| MANDTXT4 | VARCHAR | 100.0% |  |  |
| MANDTXT5 | VARCHAR | 100.0% |  |  |
| MANDTXT6 | VARCHAR | 100.0% |  |  |
| CO924TAB | DOUBLE | 98.8% | 0.0 |  |
| SORFORM | DOUBLE | 12.6% | 1.0 |  |
| MAND1 | DOUBLE | 21.3% | 1.0 |  |
| MAND2 | DOUBLE | 92.8% | 2.0 |  |
| MAND3 | DOUBLE | 99.2% | 3.0 |  |
| MAND4 | DOUBLE | 100.0% | 4.0 |  |
| MAND5 | DOUBLE | 100.0% | 6.0 |  |
| MAND6 | DOUBLE | 100.0% |  |  |
| USARMHI | DOUBLE | 17.4% | 0.0 |  |
| USARMRHI | DOUBLE | 93.7% | 0.0 |  |
| ABUSSHI | DOUBLE | 15.1% | 0.0 |  |
| ADJOFSHI | DOUBLE | 15.1% | -2.0 |  |
| ADJS_BHI | DOUBLE | 18.7% | -2.0 |  |
| ADJS_CHI | DOUBLE | 31.3% | -10.0 |  |
| ADJS_DHI | DOUBLE | 33.0% | -1.0 |  |
| ADJS_EHI | DOUBLE | 46.2% | -1.0 |  |
| ADJS_FHI | DOUBLE | 47.6% | -1.0 |  |
| ADJS_GHI | DOUBLE | 48.9% | -2.0 |  |
| ADJS_HHI | DOUBLE | 53.6% | -1.0 |  |
| ADJS_IHI | DOUBLE | 66.1% | 0.0 |  |
| ADJS_JHI | DOUBLE | 66.2% | -2.0 |  |
| ADJS_KHI | DOUBLE | 72.7% | 0.0 |  |
| ADJS_LHI | DOUBLE | 72.7% | -2.0 |  |
| ADJS_MHI | DOUBLE | 76.8% | 0.0 |  |
| ADJS_NHI | DOUBLE | 77.1% | 0.0 |  |
| ADJS_OHI | DOUBLE | 77.1% | 0.0 |  |
| ADJS_PHI | DOUBLE | 77.4% | -2.0 |  |
| AGGRLSHI | DOUBLE | 15.1% | -3.0 |  |
| BASADSHI | DOUBLE | 15.1% | -1.0 |  |
| BASESHI | DOUBLE | 15.1% | -3.0 |  |
| FLGHTSHI | DOUBLE | 15.1% | 0.0 |  |
| MITRLSHI | DOUBLE | 15.1% | -1.0 |  |
| OBSTRSHI | DOUBLE | 15.1% | -1.0 |  |
| OFFVCSHI | DOUBLE | 15.1% | 0.0 |  |
| RLADJSHI | DOUBLE | 76.4% | 0.0 |  |
| RSTRVSHI | DOUBLE | 15.1% | 0.0 |  |
| TERORSHI | DOUBLE | 15.1% | 0.0 |  |
| USKIDSHI | DOUBLE | 15.1% | -4.0 |  |
| VCADJSHI | DOUBLE | 76.4% | 0.0 |  |
| VULVCSHI | DOUBLE | 15.1% | 0.0 |  |
| USARMSHI | DOUBLE | 17.4% | 0.0 |  |
| ABUSCHI | DOUBLE | 99.6% | 0.0 |  |
| ADJOFCHI | DOUBLE | 47.5% | 0.0 |  |
| ADJC_BHI | DOUBLE | 99.6% | -2.0 |  |
| ADJC_CHI | DOUBLE | 99.7% | -3.0 |  |
| ADJC_DHI | DOUBLE | 99.7% | -18.0 |  |
| ADJC_EHI | DOUBLE | 99.7% | -1.0 |  |
| ADJC_FHI | DOUBLE | 99.7% | 0.0 |  |
| ADJC_GHI | DOUBLE | 99.8% | -2.0 |  |
| ADJC_HHI | DOUBLE | 99.8% | -2.0 |  |
| ADJC_IHI | DOUBLE | 99.8% | 0.0 |  |
| ADJC_JHI | DOUBLE | 99.8% | -2.0 |  |
| ADJC_KHI | DOUBLE | 99.9% | 0.0 |  |
| ADJC_LHI | DOUBLE | 99.9% | -2.0 |  |
| ADJC_MHI | DOUBLE | 99.9% | 0.0 |  |
| ADJC_NHI | DOUBLE | 99.9% | 0.0 |  |
| ADJC_OHI | DOUBLE | 99.9% | 0.0 |  |
| ADJC_PHI | DOUBLE | 99.9% | -2.0 |  |
| AGGRLCHI | DOUBLE | 99.6% | 0.0 |  |
| BASADCHI | DOUBLE | 47.5% | -3.0 |  |
| BASECHI | DOUBLE | 47.5% | 0.0 |  |
| FLGHTCHI | DOUBLE | 99.6% | 0.0 |  |
| MITRLCHI | DOUBLE | 99.6% | -2.0 |  |
| OBSTCCHI | DOUBLE | 99.6% | 0.0 |  |
| OFFVCCHI | DOUBLE | 99.6% | 0.0 |  |
| RLADJCHI | DOUBLE | 99.9% | 0.0 |  |
| RSTRCCHI | DOUBLE | 99.6% | 0.0 |  |
| TERORCHI | DOUBLE | 99.6% | 0.0 |  |
| USKIDCHI | DOUBLE | 99.6% | 0.0 |  |
| VCADJCHI | DOUBLE | 99.9% | 0.0 |  |
| VULVCCHI | DOUBLE | 99.6% | 0.0 |  |
| USARMCHI | DOUBLE | 99.6% | 0.0 |  |
| ADJL_BHI | VARCHAR | 17.8% | A |  |
| ADJL_CHI | VARCHAR | 30.4% | A |  |
| ADJL_DHI | VARCHAR | 32.4% | A |  |
| ADJL_EHI | VARCHAR | 43.2% | A |  |
| ADJL_FHI | VARCHAR | 44.7% | A |  |
| ADJL_GHI | VARCHAR | 46.1% | A |  |
| ADJL_HHI | VARCHAR | 51.1% | A |  |
| ADJL_IHI | VARCHAR | 63.6% | A |  |
| ADJL_JHI | VARCHAR | 63.8% | A |  |
| ADJL_KHI | VARCHAR | 70.4% | A |  |
| ADJL_LHI | VARCHAR | 70.4% | A |  |
| ADJL_MHI | VARCHAR | 74.7% | A |  |
| ADJL_NHI | VARCHAR | 75.0% | A |  |
| ADJL_OHI | VARCHAR | 75.0% | A |  |
| ADJL_PHI | VARCHAR | 75.3% | A |  |
| BASELHI | VARCHAR | 15.1% | A |  |
| ADRL_BHI | VARCHAR | 93.9% | A |  |
| ADRL_CHI | VARCHAR | 94.0% | A |  |
| ADRL_DHI | VARCHAR | 94.4% | A |  |
| ADRL_EHI | VARCHAR | 94.8% | A |  |
| ADRL_FHI | VARCHAR | 94.9% | A |  |
| ADRL_GHI | VARCHAR | 95.1% | A |  |
| ADRL_HHI | VARCHAR | 95.5% | A |  |
| ADRL_IHI | VARCHAR | 96.0% | A |  |
| ADRL_JHI | VARCHAR | 96.0% | A |  |
| ADRL_KHI | VARCHAR | 96.3% | A |  |
| ADRL_LHI | VARCHAR | 96.3% | A |  |
| ADRL_MHI | VARCHAR | 96.6% | A |  |
| ADRL_NHI | VARCHAR | 96.7% | A |  |
| ADRL_OHI | VARCHAR | 96.7% | A |  |
| ADRL_PHI | VARCHAR | 96.7% | A |  |
| BASERLHI | VARCHAR | 93.8% | A |  |
| ADSL_BHI | VARCHAR | 18.5% | A |  |
| ADSL_CHI | VARCHAR | 31.1% | A |  |
| ADSL_DHI | VARCHAR | 32.8% | A |  |
| ADSL_EHI | VARCHAR | 46.2% | A |  |
| ADSL_FHI | VARCHAR | 47.5% | A |  |
| ADSL_GHI | VARCHAR | 48.9% | A |  |
| ADSL_HHI | VARCHAR | 53.6% | A |  |
| ADSL_IHI | VARCHAR | 66.1% | A |  |
| ADSL_JHI | VARCHAR | 66.2% | A |  |
| ADSL_KHI | VARCHAR | 72.7% | A |  |
| ADSL_LHI | VARCHAR | 72.7% | A |  |
| ADSL_MHI | VARCHAR | 76.8% | A |  |
| ADSL_NHI | VARCHAR | 77.1% | A |  |
| ADSL_OHI | VARCHAR | 77.1% | A |  |
| ADSL_PHI | VARCHAR | 77.4% | A |  |
| BASESLHI | VARCHAR | 19.6% | A |  |
| ADCL_BHI | VARCHAR | 99.6% | A |  |
| ADCL_CHI | VARCHAR | 99.7% | A |  |
| ADCL_DHI | VARCHAR | 99.7% | A |  |
| ADCL_EHI | VARCHAR | 99.7% | A |  |
| ADCL_FHI | VARCHAR | 99.7% | A |  |
| ADCL_GHI | VARCHAR | 99.8% | A |  |
| ADCL_HHI | VARCHAR | 99.8% | A |  |
| ADCL_IHI | VARCHAR | 99.8% | A |  |
| ADCL_JHI | VARCHAR | 99.8% | A |  |
| ADCL_KHI | VARCHAR | 99.9% | A |  |
| ADCL_LHI | VARCHAR | 99.9% | A |  |
| ADCL_MHI | VARCHAR | 99.9% | A |  |
| ADCL_NHI | VARCHAR | 99.9% | A |  |
| ADCL_OHI | VARCHAR | 99.9% | A |  |
| ADCL_PHI | VARCHAR | 99.9% | A |  |
| BASECLHI | VARCHAR | 99.6% | A |  |
| LOSSSHI | DOUBLE | 59.5% | 0.0 |  |
| GDCROSHI | VARCHAR | 99.6% | 2A1.1 |  |
| LOSSCHI | DOUBLE | 99.8% | 0.0 |  |
| DRUGPROB | DOUBLE | 71.0% | 0.0 |  |
| LOSSPROB | DOUBLE | 7.8% | 0.0 |  |
| BLAKPOST | DOUBLE | 95.9% | 0.0 |  |
| DEPART_A | DOUBLE | 95.2% | 0.0 |  |
| SENTMON | DOUBLE | 15.3% | 1.0 |  |
| SENTYR | DOUBLE | 15.3% | 2003.0 |  |
| DOBMON | DOUBLE | 15.9% | 1.0 |  |
| DOBYR | DOUBLE | 15.9% | 1901.0 |  |
| BOOKPOST | DOUBLE | 95.8% | 0.0 |  |
| BOOKERCD | DOUBLE | 44.9% | 0.0 |  |
| GUNMIN3 | DOUBLE | 16.1% | 0.0 |  |
| FIREMIN1 | DOUBLE | 16.1% | 0.0 |  |
| FIREMIN2 | DOUBLE | 16.1% | 0.0 |  |
| PORNMIN | DOUBLE | 16.1% | 0.0 |  |
| IDMIN | DOUBLE | 16.1% | 0.0 |  |
| IMMIMIN | DOUBLE | 16.1% | 0.0 |  |
| SEXMIN | DOUBLE | 16.1% | 0.0 |  |
| OTHRMIN | DOUBLE | 16.1% | 0.0 |  |
| MITCAP | DOUBLE | 16.1% | 0.0 |  |
| QUARTER | DOUBLE | 16.1% | 1.0 |  |
| CRCKBOL1 | DOUBLE | 99.7% | 12.0 |  |
| CRCKBOL2 | DOUBLE | 100.0% | 12.0 |  |
| CRCKBOL3 | DOUBLE | 100.0% | 14.0 |  |
| CRCKBOL4 | DOUBLE | 100.0% | 14.0 |  |
| CRCKBOL5 | DOUBLE | 100.0% | 16.0 |  |
| REPSXMIN | DOUBLE | 20.3% | 0.0 |  |
| RESTTXT1 | VARCHAR | 99.7% | 100 dollars ordered minus any credits for monies already repaid due within 60... |  |
| RESTTXT2 | VARCHAR | 100.0% | 7201 and restitution is not applicable. |  |
| RESTTXT3 | VARCHAR | 100.0% | The ct agreed to revisit the issue of restitution if it is subsequently deter... |  |
| RESTTXT4 | VARCHAR | 100.0% |  |  |
| RESTTXT5 | VARCHAR | 100.0% |  |  |
| RESTTXT6 | VARCHAR | 100.0% |  |  |
| RESTDET1 | DOUBLE | 34.2% | 0.0 |  |
| RESTDET2 | DOUBLE | 99.9% | 1.0 |  |
| RESTDET3 | DOUBLE | 100.0% | 2.0 |  |
| RESTDET4 | DOUBLE | 100.0% | 3.0 |  |
| RESTDET5 | DOUBLE | 100.0% | 5.0 |  |
| RESTDET6 | DOUBLE | 100.0% | 7.0 |  |
| ACPTCOMM | DOUBLE | 99.3% | 1.0 |  |
| RANGECD | DOUBLE | 95.3% | 1.0 |  |
| RLEASHI | DOUBLE | 28.2% | 0.0 |  |
| FALDMHI | DOUBLE | 28.2% | 0.0 |  |
| MCCNTHI | DOUBLE | 96.1% | 0.0 |  |
| MCUNTHI | DOUBLE | 96.1% | 0.0 |  |
| MCCDAHI | DOUBLE | 99.6% | 1.0 |  |
| MCCDBHI | DOUBLE | 100.0% | 1.0 |  |
| MCCDCHI | DOUBLE | 100.0% | 2.0 |  |
| MCCDDHI | DOUBLE | 100.0% | 3.0 |  |
| RLEASRHI | DOUBLE | 94.2% | 0.0 |  |
| FALDMRHI | DOUBLE | 94.2% | 0.0 |  |
| MCCNTRHI | DOUBLE | 99.8% | 0.0 |  |
| MCUNTRHI | DOUBLE | 99.8% | 0.0 |  |
| MCCDRAHI | DOUBLE | 100.0% | 1.0 |  |
| MCCDRBHI | DOUBLE | 100.0% | 2.0 |  |
| MCCDRCHI | DOUBLE | 100.0% | 3.0 |  |
| MCCDRDHI | DOUBLE | 100.0% |  |  |
| RLEASSHI | DOUBLE | 28.2% | 0.0 |  |
| FALDMSHI | DOUBLE | 28.2% | 0.0 |  |
| MCCNTSHI | DOUBLE | 96.1% | 0.0 |  |
| MCUNTSHI | DOUBLE | 96.1% | 0.0 |  |
| MCCDSAHI | DOUBLE | 99.7% | 1.0 |  |
| MCCDSBHI | DOUBLE | 100.0% | 1.0 |  |
| MCCDSCHI | DOUBLE | 100.0% | 2.0 |  |
| MCCDSDHI | DOUBLE | 100.0% | 3.0 |  |
| RLEASCHI | DOUBLE | 99.6% | 0.0 |  |
| FALDMCHI | DOUBLE | 99.6% | 0.0 |  |
| MCCNTCHI | DOUBLE | 100.0% | 0.0 |  |
| MCUNTCHI | DOUBLE | 100.0% | 0.0 |  |
| MCCDCAHI | DOUBLE | 100.0% | 1.0 |  |
| MCCDCBHI | DOUBLE | 100.0% | 2.0 |  |
| MCCDCCHI | DOUBLE | 100.0% | 3.0 |  |
| MCCDCDHI | DOUBLE | 100.0% |  |  |
| RELMIN | DOUBLE | 24.6% | 0.0 |  |
| KIMBPOST | DOUBLE | 95.6% | 0.0 |  |
| BOOKER2 | DOUBLE | 56.0% | 0.0 |  |
| BOOKER3 | DOUBLE | 56.0% | 0.0 |  |
| IS1028A | DOUBLE | 29.0% | 0.0 |  |
| FAILMIN | DOUBLE | 29.0% | 0.0 |  |
| ADJ_QHI | DOUBLE | 76.9% | -2.0 |  |
| ADJR_QHI | DOUBLE | 96.9% | -2.0 |  |
| ADJS_QHI | DOUBLE | 78.9% | -2.0 |  |
| ADJC_QHI | DOUBLE | 99.9% | -2.0 |  |
| ADJL_QHI | VARCHAR | 76.9% | A |  |
| ADRL_QHI | VARCHAR | 96.9% | A |  |
| ADSL_QHI | VARCHAR | 78.9% | A |  |
| ADCL_QHI | VARCHAR | 99.9% | A |  |
| COUNT18924C | DOUBLE | 95.3% | 0.0 |  |
| ONLY924C | DOUBLE | 33.7% | 0.0 |  |
| ONLY1028A | DOUBLE | 33.7% | 0.0 |  |
| ADJ_RHI | DOUBLE | 82.7% | -2.0 |  |
| ADJR_RHI | DOUBLE | 97.5% | -2.0 |  |
| ADJS_RHI | DOUBLE | 84.4% | -2.0 |  |
| ADJC_RHI | DOUBLE | 99.9% | -2.0 |  |
| ADJL_RHI | VARCHAR | 82.7% | A |  |
| ADRL_RHI | VARCHAR | 97.5% | A |  |
| ADSL_RHI | VARCHAR | 84.4% | A |  |
| ADCL_RHI | VARCHAR | 99.9% | A |  |
| OFFTYPSB | DOUBLE | 64.2% | 1.0 |  |
| TIMSERVC | DOUBLE | 38.6% | 0.0 |  |
| ISMETHMIN | DOUBLE | 38.6% | 0.0 |  |
| METHMIN | DOUBLE | 38.6% | 0.0 |  |
| CRMLIVAP | DOUBLE | 71.1% | -2.0 |  |
| MONSXOFB | DOUBLE | 74.8% | 0.0 |  |
| NODRUG | DOUBLE | 82.0% | 1.0 |  |
| NOCHEM | DOUBLE | 99.9% | 1.0 |  |
| SEXADJB | DOUBLE | 71.1% | 0.0 |  |
| REGSXMIN | DOUBLE | 43.6% | 0.0 |  |
| ADJ_SHI | DOUBLE | 88.3% | -2.0 |  |
| BASLNHI | DOUBLE | 47.6% | 1.0 |  |
| ADJR_SHI | DOUBLE | 98.1% | -2.0 |  |
| BASLNRHI | DOUBLE | 95.7% | 1.0 |  |
| ADJS_SHI | DOUBLE | 89.6% | -2.0 |  |
| BASLNSHI | DOUBLE | 50.9% | 1.0 |  |
| ADJC_SHI | DOUBLE | 99.9% | -2.0 |  |
| BASLNCHI | DOUBLE | 99.7% | 1.0 |  |
| ABUSUHI | DOUBLE | 100.0% | 0.0 |  |
| ADJOFUHI | DOUBLE | 47.6% | 0.0 |  |
| ADJU_BHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_CHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_DHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_EHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_FHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_GHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_HHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_IHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_JHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_KHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_LHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_MHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_NHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_OHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_PHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_QHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_RHI | DOUBLE | 100.0% | -2.0 |  |
| ADJU_SHI | DOUBLE | 100.0% | 0.0 |  |
| AGGRLUHI | DOUBLE | 100.0% | 0.0 |  |
| BASADUHI | DOUBLE | 47.6% | 0.0 |  |
| BASEUHI | DOUBLE | 47.6% | 0.0 |  |
| FLGHTUHI | DOUBLE | 100.0% | 0.0 |  |
| MITRLUHI | DOUBLE | 100.0% | -2.0 |  |
| OBSTCUHI | DOUBLE | 100.0% | 0.0 |  |
| OFFVCUHI | DOUBLE | 100.0% | 0.0 |  |
| RSTRVUHI | DOUBLE | 100.0% | 0.0 |  |
| TERORUHI | DOUBLE | 100.0% | 0.0 |  |
| USKIDUHI | DOUBLE | 100.0% | 0.0 |  |
| VULVCUHI | DOUBLE | 100.0% | 0.0 |  |
| USARMUHI | DOUBLE | 100.0% | 0.0 |  |
| RLEASUHI | DOUBLE | 100.0% | 0.0 |  |
| FALDMUHI | DOUBLE | 100.0% | 0.0 |  |
| BASLNUHI | DOUBLE | 100.0% | 1.0 |  |
| ADJL_SHI | VARCHAR | 88.3% | A |  |
| ADRL_SHI | VARCHAR | 98.1% | A |  |
| ADSL_SHI | VARCHAR | 89.6% | A |  |
| ADCL_SHI | VARCHAR | 99.9% | A |  |
| ADUL_BHI | VARCHAR | 100.0% | A |  |
| ADUL_CHI | VARCHAR | 100.0% | A |  |
| ADUL_DHI | VARCHAR | 100.0% | A |  |
| ADUL_EHI | VARCHAR | 100.0% | A |  |
| ADUL_FHI | VARCHAR | 100.0% | A |  |
| ADUL_GHI | VARCHAR | 100.0% | A |  |
| ADUL_HHI | VARCHAR | 100.0% | A |  |
| ADUL_IHI | VARCHAR | 100.0% | A |  |
| ADUL_JHI | VARCHAR | 100.0% | A |  |
| ADUL_KHI | VARCHAR | 100.0% | A |  |
| ADUL_LHI | VARCHAR | 100.0% | A |  |
| ADUL_MHI | VARCHAR | 100.0% | A |  |
| ADUL_NHI | VARCHAR | 100.0% | A |  |
| ADUL_OHI | VARCHAR | 100.0% | A |  |
| ADUL_PHI | VARCHAR | 100.0% | A |  |
| ADUL_QHI | VARCHAR | 100.0% | A |  |
| ADUL_RHI | VARCHAR | 100.0% | A |  |
| ADUL_SHI | VARCHAR | 100.0% | A |  |
| BASEULHI | VARCHAR | 100.0% | A |  |
| GDUNDRHI | VARCHAR | 100.0% | 2A1.1 |  |
| LOSSUHI | DOUBLE | 100.0% | 0.0 |  |
| HUMANHI | DOUBLE | 53.3% | 0.0 |  |
| HUMANSHI | DOUBLE | 53.3% | 0.0 |  |
| HUMANRHI | DOUBLE | 96.0% | 0.0 |  |
| HUMANCHI | DOUBLE | 99.7% | 0.0 |  |
| HUMANUHI | DOUBLE | 100.0% | 0.0 |  |
| HUMLBHI | VARCHAR | 53.3% | A |  |
| HUMLBSHI | VARCHAR | 53.3% | A |  |
| HUMLBRHI | VARCHAR | 96.0% | A |  |
| HUMLBCHI | VARCHAR | 99.7% | A |  |
| HUMLBUHI | VARCHAR | 100.0% | A |  |
| NOREAVAR | DOUBLE | 74.4% | 1.0 |  |
| ADJ_THI | DOUBLE | 96.1% | 0.0 |  |
| ADJS_THI | DOUBLE | 97.1% | 0.0 |  |
| ADJR_THI | DOUBLE | 98.8% | 0.0 |  |
| ADJC_THI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_THI | DOUBLE | 100.0% | 0.0 |  |
| ADJL_THI | VARCHAR | 96.1% | A |  |
| ADSL_THI | VARCHAR | 97.1% | A |  |
| ADRL_THI | VARCHAR | 98.8% | A |  |
| ADCL_THI | VARCHAR | 100.0% | A |  |
| ADUL_THI | VARCHAR | 100.0% | A |  |
| SORGDL | VARCHAR | 99.7% | 0-6 |  |
| FINEMIN | DOUBLE | 63.8% | 0.0 |  |
| FINEMAX | DOUBLE | 63.7% | 0.0 |  |
| BOOKER4 | DOUBLE | 92.3% | 0.0 |  |
| SUPERMIN | DOUBLE | 68.2% | 0.0 |  |
| SUPERMAX | DOUBLE | 63.7% | 0.0 |  |
| SENTTCAP | DOUBLE | 72.0% | 0.03 |  |
| SENSPCAP | DOUBLE | 69.5% | 0.0 |  |
| CASETYPE | DOUBLE | 69.9% | 1.0 |  |
| DTGDL | DOUBLE | 71.3% | 0.0 |  |
| OFFGUIDE | DOUBLE | 69.5% | 1.0 |  |
| SENTRNGE | DOUBLE | 69.7% | 0.0 |  |
| WEAPSCHI | DOUBLE | 71.3% | 0.0 |  |
| PCNTDEPT | DOUBLE | 84.4% | 0.25 |  |
| MNTHDEPT | DOUBLE | 84.4% | 0.03 |  |
| AGECAT | DOUBLE | 73.6% | 1.0 |  |
| FSASV | DOUBLE | 73.6% | 0.0 |  |
| ADJ_UHI | DOUBLE | 98.1% | 0.0 |  |
| ADJS_UHI | DOUBLE | 98.7% | 0.0 |  |
| ADJR_UHI | DOUBLE | 99.3% | 0.0 |  |
| ADJC_UHI | DOUBLE | 100.0% | 0.0 |  |
| ADJU_UHI | DOUBLE | 100.0% | 0.0 |  |
| ADJL_UHI | VARCHAR | 98.1% | A |  |
| ADSL_UHI | VARCHAR | 98.7% | A |  |
| ADRL_UHI | VARCHAR | 99.3% | A |  |
| ADCL_UHI | VARCHAR | 100.0% | A |  |
| ADUL_UHI | VARCHAR | 100.0% | A |  |
| ZEROPNT | DOUBLE | 93.8% | -1.0 |  |

## v_sentence_terms


| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| fiscal_year | INTEGER | 0.0% | 2002 | Fiscal year of sentencing (from the datafile); joins every table |
| USSCIDN | DOUBLE | 0.0% | 1000001.0 | USSC case identifier; joins every table |
| prison_months | DOUBLE | 0.4% | 0.0 |  |
| term_type | VARCHAR | 0.0% | death |  |
| prison_imposed | BOOLEAN | 0.1% | false |  |
| TOTPRISN | DOUBLE | 0.1% | 0.0 |  |
| SENTTOT | DOUBLE | 12.4% | 0.03 |  |
| SENTIMP | DOUBLE | 0.1% | 0.0 |  |
| PRISDUM | DOUBLE | 0.1% | 0.0 |  |
