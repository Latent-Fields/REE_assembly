#!/bin/bash
# N2 registered run: one seed, all 3 arms x {real, shuf}, post phase 600 steps (pre-registered).
S=$1
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n2
P=/opt/local/bin/python3; W=/Users/dgolden/REE_Working/.scratch/wt-n2
$P n2_probe.py --seed $S --wt $W --b0-only --out results/B0_s$S.json > results/B0_s$S.log 2>&1 || exit 1
for arm in frozen reencode stored; do
  for twin in real shuf; do
    $P n2_probe.py --seed $S --wt $W --arm $arm --twin $twin --post 600 --b0-cache results/B0_s$S.json \
      --out results/N2_${arm}_${twin}_s$S.json > results/N2_${arm}_${twin}_s$S.log 2>&1
  done
done
