#!/bin/bash
# two lanes, sequential within each
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/w3
( for s in 106 107 108 109 110; do /opt/local/bin/python3 w3_l2r_member_probe.py --seed $s --wt /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/w3/snap --arm real --out results/W3_real_s$s.json > results/W3_real_s$s.log 2>&1; done ) &
( for s in 106 107 108 109 110; do /opt/local/bin/python3 w3_l2r_member_probe.py --seed $s --wt /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/w3/snap --arm shuf --out results/W3_shuf_s$s.json > results/W3_shuf_s$s.log 2>&1; done ) &
wait
