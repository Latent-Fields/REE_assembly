#!/bin/bash
# Usage: with_lock.sh <cmd...>  -- acquire the Mac CPU lock (mkdir), require >=800MB avail, run, release.
L=/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock
while true; do
  if mkdir "$L" 2>/dev/null; then
    echo "bt0925-rt5 pid $$ $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$L/owner"; break
  fi
  age=$(( $(date +%s) - $(stat -f %m "$L") ))
  if [ "$age" -gt 2700 ] && ! grep -q "bt0925-rt5" "$L/owner" 2>/dev/null; then
    echo "stale lock age ${age}s (owner: $(cat $L/owner 2>/dev/null)); removing"; rm -rf "$L"; continue
  fi
  sleep 30
done
trap 'rm -rf "$L"' EXIT
while true; do
  avail=$(vm_stat | awk '/Pages free/{f=$3}/Pages inactive/{i=$3}/Pages speculative/{s=$3}END{gsub(/\./,"",f);gsub(/\./,"",i);gsub(/\./,"",s);print int((f+i+s)*16384/1048576)}')
  [ "$avail" -ge 800 ] && break
  echo "avail ${avail}MB < 800MB; waiting"; sleep 30
done
echo "LOCK acquired $(date -u +%H:%M:%SZ) avail=${avail}MB"
"$@"
rc=$?
echo "LOCK released $(date -u +%H:%M:%SZ) rc=$rc"
exit $rc
