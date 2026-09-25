#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/babble
until grep -q ALLDONE results/run_all.log; do sleep 20; done
for s in 108 109 110; do
  echo "=== L2R trailing seed $s start $(date -u +%H:%M:%S)" >> results/run_all.log
  /opt/local/bin/python3 -u babble_l2r_trailing.py --seed $s > results/BAB_L2R_s$s.log 2>&1
  echo "=== L2R trailing seed $s exit $? end $(date -u +%H:%M:%S)" >> results/run_all.log
done
echo L2RDONE >> results/run_all.log
