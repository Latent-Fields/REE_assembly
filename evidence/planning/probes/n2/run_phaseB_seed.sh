#!/bin/bash
# Phase B: the two W6a arms x {real, shuf} for one seed.
S=$1
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n2
P=/opt/local/bin/python3; W=/Users/dgolden/REE_Working/.scratch/wt-n2
for arm in reencode stored; do
  for twin in real shuf; do
    $P n2_probe.py --seed $S --wt $W --arm $arm --twin $twin --post 600 --b0-cache results/B0_s$S.json \
      --out results/N2_${arm}_${twin}_s$S.json > results/N2_${arm}_${twin}_s$S.log 2>&1
  done
done
