#!/bin/bash
# usage: locked_run.sh <cmd...>
# Enforces the 45 s pause after this worker's last release, waits (<= 40 min) for a busy lock,
# takes the Mac probe lock (owner file only after mkdir succeeds), runs cmd, ALWAYS releases, verifies.
H=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/h0
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
if [ -f "$H/.last_release" ]; then
  while [ $(( $(date +%s) - $(cat "$H/.last_release") )) -lt 45 ]; do sleep 2; done
fi
n=0
until mkdir "$L" 2>/dev/null; do
  n=$((n+1)); [ $n -gt 1200 ] && { echo "LOCK_BUSY_TIMEOUT $(cat $L/owner 2>/dev/null)"; exit 75; }
  sleep 2
done
echo "bt0926-h0 $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$L/owner"
echo "lock taken $(date -u +%H:%M:%S)"
release() { rm -f "$L/owner"; rmdir "$L"; date +%s > "$H/.last_release"; if [ -d "$L" ]; then echo "LOCK_RELEASE_FAILED"; else echo "lock released $(date -u +%H:%M:%S)"; fi; }
trap release EXIT
"$@"
