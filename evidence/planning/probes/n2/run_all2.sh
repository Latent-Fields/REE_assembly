#!/bin/bash
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n2
echo "=== phaseA start $(date -u +%H:%M:%S)" >> results/run_all.log
./with_lock.sh phaseA ./run_phaseA.sh >> results/run_all.log 2>&1
for s in 612 613 614 615; do
  echo "=== seed $s phaseB start $(date -u +%H:%M:%S)" >> results/run_all.log
  ./with_lock.sh seed${s}B ./run_phaseB_seed.sh $s >> results/run_all.log 2>&1
done
echo ALLDONE >> results/run_all.log
