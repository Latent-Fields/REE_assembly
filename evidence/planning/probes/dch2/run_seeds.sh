#!/bin/bash
# DCH2 registered seeds: first 5 of 841..852 passing P-a. One process per seed; the process takes,
# rotates (<= 12 min per hold, 45 s gap) and releases the Mac probe lock itself.
cd /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/dch2
WT=/Users/dgolden/REE_Working/.scratch/wt-dch2
npass=0
for s in 841 842 843 844 845 846 847 848 849 850 851 852; do
  [ $npass -ge 5 ] && break
  [ -f STOP ] && { echo "STOP file before seed $s $(date -u +%H:%M:%S)" >> results/run_seeds.log; break; }
  /opt/local/bin/python3 dch2_probe.py --seed $s --wt $WT --out results/DCH2_s$s.json > results/DCH2_s$s.log 2>&1
  rc=$?
  if grep -q '"pa_pass": true' results/DCH2_s$s.json; then npass=$((npass+1)); fi
  echo "seed $s rc=$rc pass_total=$npass $(date -u +%H:%M:%S)" >> results/run_seeds.log
  sleep 45
done
echo "ALLDONE npass=$npass" >> results/run_seeds.log
