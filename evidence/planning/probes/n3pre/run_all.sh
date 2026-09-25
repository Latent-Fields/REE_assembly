#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n3pre
for S in 521 522 523 524 525; do
  while true; do
    AV=$(vm_stat | awk '/Pages free|Pages inactive|Pages speculative/ {gsub(/\./,"",$NF); s+=$NF} END {print int(s*16384/1048576)}')
    if [ "$AV" -ge 800 ]; then break; fi
    echo "$(date -u +%H:%M:%S) s$S waiting: avail ${AV}MB" >> results/decisions.log
    sleep 30
  done
  echo "$(date -u +%H:%M:%S) s$S start avail ${AV}MB" >> results/decisions.log
  /opt/local/bin/python3 n3pre_probe.py --seed $S --out results/N3_s$S.json > results/N3_s$S.log 2>&1
  echo "$(date -u +%H:%M:%S) s$S exit $?" >> results/decisions.log
done
