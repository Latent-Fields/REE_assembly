#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n2
for s in 611 612 613 614 615; do
  echo "=== seed $s start $(date -u +%H:%M:%S)" >> results/run_all.log
  ./with_lock.sh seed$s ./run_seed.sh $s >> results/run_all.log 2>&1
  echo "=== seed $s end $(date -u +%H:%M:%S)" >> results/run_all.log
done
echo ALLDONE >> results/run_all.log
