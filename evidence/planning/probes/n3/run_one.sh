#!/bin/bash
# usage: run_one.sh <seed> <outname> [extra args...]   -- one seed per Mac probe-lock hold
S=$1; OUT=$2; shift 2
D=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924
L=$D/mac_probe.lock
cd $D/n3
LOG=results/decisions.log
while true; do
  if mkdir "$L" 2>/dev/null; then
    echo "bt0925-n3 $(date -u +%Y-%m-%dT%H:%M:%SZ) seed $S" > "$L/owner"; break
  fi
  OWN=$(cat "$L/owner" 2>/dev/null); AGE=$(( $(date +%s) - $(stat -f %m "$L" 2>/dev/null || date +%s) ))
  SLUG=$(echo "$OWN" | awk '{print $1}' | sed 's/^bt0925-//')
  LIVE=0; [ -n "$SLUG" ] && pgrep -f "breakthrough-20260924/$SLUG" >/dev/null 2>&1 && LIVE=1
  if [ "$AGE" -gt 2700 ] && [ "$LIVE" = "0" ]; then
    echo "$(date -u +%H:%M:%S) s$S breaking stale lock ($OWN age ${AGE}s no live proc)" >> $LOG
    rm -f "$L/owner"; rmdir "$L" 2>/dev/null; continue
  fi
  sleep 30
done
while true; do
  AV=$(vm_stat | awk '/Pages free|Pages inactive|Pages speculative/ {gsub(/\./,"",$NF); s+=$NF} END {print int(s*16384/1048576)}')
  [ "$AV" -ge 800 ] && break
  echo "$(date -u +%H:%M:%S) s$S waiting: avail ${AV}MB" >> $LOG; sleep 30
done
echo "$(date -u +%H:%M:%S) s$S start avail ${AV}MB args $*" >> $LOG
/opt/local/bin/python3 n3_probe.py --seed $S --out results/$OUT.json "$@" > results/$OUT.log 2>&1
RC=$?
echo "$(date -u +%H:%M:%S) s$S exit $RC" >> $LOG
rm -f "$L/owner"; rmdir "$L"
exit $RC
