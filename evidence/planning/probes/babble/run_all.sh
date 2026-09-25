#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/babble
for s in 106 107 108 109 110; do
  SK=$(cat skip.txt)
  echo "=== seed $s skip=$SK start $(date -u +%H:%M:%S)" >> results/run_all.log
  /opt/local/bin/python3 -u babble_probe.py --seed $s --n-eps 12 --skip "$SK" --out results/BAB_s$s.json > results/BAB_s$s.log 2>&1
  echo "=== seed $s exit $? end $(date -u +%H:%M:%S)" >> results/run_all.log
done
echo ALLDONE >> results/run_all.log
