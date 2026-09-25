#!/bin/bash
# usage: with_lock.sh <label> <cmd...>   -- acquire the Mac probe lock (mkdir), run, release.
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
LABEL="$1"; shift
while ! mkdir "$L" 2>/dev/null; do sleep 30; done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) bt0925-n2 $LABEL pid $$" > "$L/owner"
echo "LOCK ACQUIRED $(date -u +%Y-%m-%dT%H:%M:%SZ) $LABEL"
"$@"
rc=$?
rm -f "$L/owner"; rmdir "$L"
echo "LOCK RELEASED $(date -u +%Y-%m-%dT%H:%M:%SZ) rc=$rc"
exit $rc
