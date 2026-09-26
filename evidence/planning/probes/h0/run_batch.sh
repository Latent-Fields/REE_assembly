#!/bin/bash
# Several jobs per lock hold; the hold is capped at 14 min (running process SIGSTOPped, lock released,
# >=45 s pause, re-take, SIGCONT). TICKS env (default 600, the pre-registered value).
H=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/h0
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
R=${R:-$H/results/main.jsonl}; TICKS=${TICKS:-600}
cd /Users/dgolden/REE_Working/.scratch/wt-h0
take() {
  if [ -f "$H/.last_release" ]; then
    while [ $(( $(date +%s) - $(cat "$H/.last_release") )) -lt 45 ]; do sleep 2; done
  fi
  until mkdir "$L" 2>/dev/null; do sleep 2; done
  echo "bt0926-h0 $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$L/owner"
  echo "lock taken $(date -u +%H:%M:%S)"; HOLD0=$(date +%s); HELD=1
}
give() {
  rm -f "$L/owner"; rmdir "$L"; date +%s > "$H/.last_release"; HELD=0
  if [ -d "$L" ]; then echo "LOCK_RELEASE_FAILED"; else echo "lock released $(date -u +%H:%M:%S)"; fi
}
rate() { /opt/local/bin/python3 -c "import json
for l in open('$R'):
  d=json.loads(l)
  if d['arm']=='A' and d['seed']==$1 and d['ticks']==$TICKS: print(d['boundary_rate'])" | tail -1; }
HELD=0
cleanup() { [ $HELD = 1 ] && give; }
trap cleanup EXIT
take
for job in "$@"; do
  a=${job%_*}; s=${job#*_}; r=-
  [ "$a" = C ] && r=$(rate $s)
  if [ $(( $(date +%s) - HOLD0 )) -ge 780 ]; then give; take; fi
  /opt/local/bin/python3 $H/h0_reset_probe.py . "$a" $s $TICKS $r $R > "$H/results/main_${a}_${s}_${TICKS}.out" 2>&1 &
  pid=$!
  while kill -0 $pid 2>/dev/null; do
    if [ $(( $(date +%s) - HOLD0 )) -ge 840 ]; then
      kill -STOP $pid; echo "paused $a $s"; give; take; kill -CONT $pid; echo "resumed $a $s"
    fi
    sleep 3
  done
  wait $pid && echo "done $a $s $(date -u +%H:%M:%S)" || echo "RUN_FAILED $a $s"
done
give
echo ALL_JOBS_DONE "$@"
