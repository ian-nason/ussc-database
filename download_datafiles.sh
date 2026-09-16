#!/usr/bin/env bash
# USSC individual offender datafiles (no identifiers), FY2002-FY2025.
# https://www.ussc.gov/research/datafiles/commission-datafiles
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p data/raw
failed=0
for yy in $(seq -w 2 25); do
  f="data/raw/opafy${yy}nid.zip"
  # FY2016 and FY2017 are published with a hyphen in the file name
  case $yy in 16|17) url="https://www.ussc.gov/sites/default/files/zip/opafy${yy}-nid.zip" ;; *) url="https://www.ussc.gov/sites/default/files/zip/opafy${yy}nid.zip" ;; esac
  [[ -s "$f" ]] && continue
  curl --fail -L --retry 5 --retry-delay 10 -sS -A "Mozilla/5.0 (datapond-maintenance)" -o "$f.part" "$url" && mv "$f.part" "$f" && echo "ok $f $(stat -c %s "$f")" || { rm -f "$f.part"; echo "FAIL $f" >&2; failed=$((failed + 1)); }
done
curl -sS -A "Mozilla/5.0" -o data/raw/USSC_Public_Release_Codebook_FY99_FY25.pdf "https://www.ussc.gov/sites/default/files/pdf/research-and-publications/datafiles/USSC_Public_Release_Codebook_FY99_FY25.pdf" && echo "codebook ok"
echo "USSC DOWNLOADS DONE"
if [[ $failed -gt 0 ]]; then echo "$failed download(s) failed" >&2; exit 1; fi
