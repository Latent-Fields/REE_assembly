#!/bin/bash
# Phase A (reordering only, rule unchanged): B0 + control arm (frozen real/shuf) for 612-615.
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n2
P=/opt/local/bin/python3; W=/Users/dgolden/REE_Working/.scratch/wt-n2
for S in 612 613 614 615; do
  $P n2_probe.py --seed $S --wt $W --b0-only --out results/B0_s$S.json > results/B0_s$S.log 2>&1 || continue
  for twin in real shuf; do
    $P n2_probe.py --seed $S --wt $W --arm frozen --twin $twin --post 600 --b0-cache results/B0_s$S.json \
      --out results/N2_frozen_${twin}_s$S.json > results/N2_frozen_${twin}_s$S.log 2>&1
  done
done
