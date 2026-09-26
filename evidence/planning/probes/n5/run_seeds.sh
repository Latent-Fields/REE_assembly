#!/bin/bash
# N5 registered seeds, one seed per lock hold; 45 s pause between holds so 30 s pollers get a turn.
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n5
for s in "$@"; do
  ./with_lock.sh n5seed$s /opt/local/bin/python3 n5_probe.py --seed $s --wt /Users/dgolden/REE_Working/.scratch/wt-n5 \
     --out results/N5_s$s.json > results/N5_s$s.log 2>&1
  echo "seed $s rc=$? $(date -u +%H:%M:%S)" >> results/run_seeds.log
  sleep 45
done
echo ALLDONE >> results/run_seeds.log
