#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n3pre
for S in 521 522 523 524 525; do
  while true; do
    AV=$(vm_stat | awk '/Pages free|Pages inactive|Pages speculative/ {gsub(/\./,"",$NF); s+=$NF} END {print int(s*16384/1048576)}')
    [ "$AV" -ge 800 ] && break; echo "$(date -u +%H:%M:%S) PH s$S waiting ${AV}MB" >> results/decisions.log; sleep 30
  done
  echo "$(date -u +%H:%M:%S) POSTHOC s$S start avail ${AV}MB" >> results/decisions.log
  /opt/local/bin/python3 n3pre_posthoc.py --seed $S --out results/N3PH_s$S.json > results/N3PH_s$S.log 2>&1
  echo "$(date -u +%H:%M:%S) POSTHOC s$S exit $?" >> results/decisions.log
done
