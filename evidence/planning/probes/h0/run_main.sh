#!/bin/bash
# Scored runs: seeds 31-33, 600 steps. Two runs per lock hold (<= 15 min), 45 s pause enforced by locked_run.sh.
H=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/h0
R=$H/results/main.jsonl
cd /Users/dgolden/REE_Working/.scratch/wt-h0
run() { /opt/local/bin/python3 $H/h0_reset_probe.py . "$1" "$2" 600 "${3:--}" $R > $H/results/main_$1_$2.out 2>&1 || echo "RUN_FAILED $1 $2"; echo "done $1 $2 $(date -u +%H:%M:%S)"; }
rate() { /opt/local/bin/python3 -c "import json,sys
for l in open('$R'):
  d=json.loads(l)
  if d['arm']=='A' and d['seed']==$1: print(d['boundary_rate'])" | tail -1; }
export -f run rate; export H R
$H/locked_run.sh bash -c 'run A 31; run A 32'
$H/locked_run.sh bash -c 'run A 33; run B 31'
$H/locked_run.sh bash -c 'run B 32; run B 33'
$H/locked_run.sh bash -c 'run C 31 $(rate 31); run C 32 $(rate 32)'
$H/locked_run.sh bash -c 'run C 33 $(rate 33)'
echo ALL_MAIN_DONE
