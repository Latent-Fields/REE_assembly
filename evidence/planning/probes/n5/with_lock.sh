#!/bin/bash
# usage: with_lock.sh <label> <cmd...> -- acquire the Mac probe lock (lock_acquire.py), run, release.
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
LABEL="$1"; shift
/opt/local/bin/python3 /Users/dgolden/REE_Working/.scratch/breakthrough-20260924/n5/lock_acquire.py "$LABEL" || exit 9
"$@"
rc=$?
rm -f "$L/owner"; rmdir "$L"
echo "LOCK RELEASED $(date -u +%Y-%m-%dT%H:%M:%SZ) rc=$rc"
exit $rc
