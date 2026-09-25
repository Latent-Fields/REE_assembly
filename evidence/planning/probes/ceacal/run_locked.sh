#!/bin/bash
# usage: run_locked.sh <cmd...>  -- acquires the Mac probe lock + memory floor, runs, releases.
LOCK=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
while true; do
  if mkdir "$LOCK" 2>/dev/null; then break; fi
  age=$(( $(date +%s) - $(stat -f %m "$LOCK") ))
  if [ $age -gt 2700 ]; then echo "stale lock ($age s), removing" >&2; rmdir "$LOCK" 2>/dev/null; continue; fi
  sleep 30
done
while true; do
  avail=$(vm_stat | awk '/Pages free/ {f=$3} /Pages inactive/ {i=$3} /Pages speculative/ {s=$3} END {gsub(/\./,"",f);gsub(/\./,"",i);gsub(/\./,"",s); print int((f+i+s)*16384/1048576)}')
  [ "$avail" -ge 800 ] && break
  echo "waiting for memory ($avail MB)" >&2; sleep 30
done
"$@"; rc=$?
rmdir "$LOCK"
exit $rc
