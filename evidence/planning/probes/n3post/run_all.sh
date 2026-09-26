#!/bin/bash
# Runs all 10 registered (seed, arm) jobs sequentially under the Mac probe lock.
set -u
D=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924
L=$D/mac_probe.lock
cd $D/n3post
mkdir -p results
LOG=results/run_all.log
: > "$LOG"

SEEDS="531 532 533 534 535"

run_one () {
  S=$1; ARM=$2
  if [ "$ARM" = "off" ]; then
    WT=/Users/dgolden/REE_Working/.scratch/wt-n3post; FIXON=0
  else
    WT=/Users/dgolden/REE_Working/.scratch/wt-n3post-on; FIXON=1
  fi
  OUT=results/N3POST_${ARM}_s${S}.json
  # acquire lock
  while true; do
    if mkdir "$L" 2>/dev/null; then
      echo "bt0926-n3post $(date -u +%Y-%m-%dT%H:%M:%SZ) seed $S arm $ARM" > "$L/owner"
      break
    fi
    OWN=$(cat "$L/owner" 2>/dev/null)
    AGE=$(( $(date +%s) - $(stat -f %m "$L" 2>/dev/null || date +%s) ))
    SLUG=$(echo "$OWN" | awk '{print $1}' | sed 's/^bt09[0-9][0-9]-//')
    LIVE=0; [ -n "$SLUG" ] && pgrep -f "breakthrough-20260924/$SLUG" >/dev/null 2>&1 && LIVE=1
    if [ "$AGE" -gt 2700 ] && [ "$LIVE" = "0" ]; then
      echo "$(date -u +%H:%M:%S) s$S/$ARM breaking stale lock ($OWN age ${AGE}s no live proc)" >> "$LOG"
      rm -f "$L/owner"; rmdir "$L" 2>/dev/null; continue
    fi
    sleep 30
  done
  # memory gate
  while true; do
    AV=$(vm_stat | awk '/Pages free|Pages inactive|Pages speculative/ {gsub(/\./,"",$NF); s+=$NF} END {print int(s*16384/1048576)}')
    [ "$AV" -ge 800 ] && break
    echo "$(date -u +%H:%M:%S) s$S/$ARM waiting: avail ${AV}MB" >> "$LOG"; sleep 30
  done
  echo "$(date -u +%H:%M:%S) s$S/$ARM start avail ${AV}MB" >> "$LOG"
  N3POST_WT=$WT N3POST_FIXON=$FIXON /opt/local/bin/python3 n3post_probe.py --seed $S --out $OUT > results/N3POST_${ARM}_s${S}.log 2>&1
  RC=$?
  echo "$(date -u +%H:%M:%S) s$S/$ARM exit $RC" >> "$LOG"
  rm -f "$L/owner"; rmdir "$L" 2>/dev/null
  sleep 45
}

for S in $SEEDS; do
  run_one $S off
  run_one $S on
done
echo "$(date -u +%H:%M:%S) ALL DONE" >> "$LOG"
