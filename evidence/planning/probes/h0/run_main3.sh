#!/bin/bash
# Scored runs, one run per job. Each lock hold is capped at 14 min: if the run is still going, the
# python process is SIGSTOPped (no CPU while stopped), the lock is released, >=45 s pause, the lock is
# re-taken (waiting if another worker holds it), and the process is SIGCONTed. Pre-registered 600 steps kept.
H=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/h0
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
R=$H/results/main.jsonl
cd /Users/dgolden/REE_Working/.scratch/wt-h0
take() {
  if [ -f "$H/.last_release" ]; then
    while [ $(( $(date +%s) - $(cat "$H/.last_release") )) -lt 45 ]; do sleep 2; done
  fi
  until mkdir "$L" 2>/dev/null; do sleep 2; done
  echo "bt0926-h0 $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$L/owner"
  echo "lock taken $(date -u +%H:%M:%S)"
}
give() {
  rm -f "$L/owner"; rmdir "$L"; date +%s > "$H/.last_release"
  if [ -d "$L" ]; then echo "LOCK_RELEASE_FAILED"; else echo "lock released $(date -u +%H:%M:%S)"; fi
}
rate() { /opt/local/bin/python3 -c "import json
for l in open('$R'):
  d=json.loads(l)
  if d['arm']=='A' and d['seed']==$1: print(d['boundary_rate'])" | tail -1; }
HELD=0
cleanup() { [ $HELD = 1 ] && give; }
trap cleanup EXIT
for job in "$@"; do
  a=${job%_*}; s=${job#*_}; r=-
  [ "$a" = C ] && r=$(rate $s)
  take; HELD=1
  /opt/local/bin/python3 $H/h0_reset_probe.py . $a $s 600 $r $R > $H/results/main_${a}_${s}.out 2>&1 &
  pid=$!
  t0=$(date +%s)
  while kill -0 $pid 2>/dev/null; do
    if [ $(( $(date +%s) - t0 )) -ge 840 ]; then
      kill -STOP $pid; echo "paused $a $s $(date -u +%H:%M:%S)"; give; HELD=0
      take; HELD=1; kill -CONT $pid; echo "resumed $a $s"; t0=$(date +%s)
    fi
    sleep 5
  done
  wait $pid && echo "done $a $s $(date -u +%H:%M:%S)" || echo "RUN_FAILED $a $s"
  give; HELD=0
done
echo ALL_JOBS_DONE "$@"
