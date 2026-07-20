#!/bin/bash
# -- REE Claims Explorer Launcher ------------------------------------------
# Double-click this file in Finder to start the explorer server and open it.
# Close this Terminal window (or Ctrl+C) to stop the server.
#
# Canonical tree ONLY (not iCloud Documents/GitHub). Desktop shortcut should
# exec this path: /Users/dgolden/REE_Working/REE_assembly/Start Explorer.command
# ---------------------------------------------------------------------------

CANONICAL_ASSEMBLY="/Users/dgolden/REE_Working/REE_assembly"
PORT=8000

# Silence the libmalloc teardown warning that every spawned python subprocess
# prints ("MallocStackLogging: can't turn off malloc stack logging because it
# was not enabled"). It fires when MallocStackLogging is present-but-falsy in
# the environment -- inherited from whatever exported it upstream (Xcode /
# Instruments), never set by this tree. Unsetting is the fix; setting it to 0
# is what TRIGGERS the message. Purely cosmetic: it only declutters the log.
unset MallocStackLogging
unset MallocStackLoggingNoCompact

# Where serve.py listens. Default 0.0.0.0 = all interfaces (unchanged behaviour).
# For WireGuard + localhost only (recommended once the iPhone peer is set up --
# see docs/mobile_access.md), run the launcher with:
#   REE_BIND="<MAC_WG_IP> 127.0.0.1" "/Users/dgolden/REE_Working/REE_assembly/Start Explorer.command"
# Each space-separated address becomes a --bind flag.
REE_BIND="${REE_BIND:-}"
BIND_ARGS=""
for _addr in $REE_BIND; do
    BIND_ARGS="$BIND_ARGS --bind $_addr"
done

cd "$CANONICAL_ASSEMBLY" || {
    echo "ERROR: cannot cd to canonical REE_assembly:"
    echo "  $CANONICAL_ASSEMBLY"
    exit 1
}

ROOT="$(pwd -P)"
if [ "$ROOT" != "$CANONICAL_ASSEMBLY" ]; then
    echo "ERROR: resolved path is not the canonical REE tree."
    echo "  expected: $CANONICAL_ASSEMBLY"
    echo "  got:      $ROOT"
    exit 1
fi

if [ ! -d "$ROOT/.git" ]; then
    echo "ERROR: $ROOT is not a git checkout (missing .git)."
    exit 1
fi

echo "REE Explorer launcher"
echo "  assembly: $ROOT"
echo ""

# coordinator.env powers Shadow Coordination panel (gitignored; not on GitHub)
COORD_ENV="$ROOT/coordinator.env"
COORD_OK=1
if [ ! -f "$COORD_ENV" ]; then
    echo "WARN: coordinator.env missing -- Shadow Coordination panel will show NOT_CONFIGURED."
    echo "  cp coordinator.env.example coordinator.env"
    echo "  set COORDINATOR_URL and COORDINATOR_LOCAL_TOKEN (gen_token.py on hub)"
    COORD_OK=0
else
    coord_url="$(grep '^COORDINATOR_URL=' "$COORD_ENV" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '[:space:]')"
    coord_tok="$(grep '^COORDINATOR_LOCAL_TOKEN=' "$COORD_ENV" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '[:space:]')"
    if [ -z "$coord_url" ] || [ -z "$coord_tok" ]; then
        echo "WARN: coordinator.env needs non-empty COORDINATOR_URL and COORDINATOR_LOCAL_TOKEN."
        echo "  Shadow / coordinator start buttons will fail until fixed."
        COORD_OK=0
    else
        echo "coordinator.env: OK (WireGuard hub + token set)"
    fi
fi
echo ""

# -- Pull latest code before starting ----------------------------------------
# Hardening: GIT_HTTP_LOW_SPEED_* abort the fetch if transfer stalls below
# 1000 B/s for 30 seconds. Without these git can hang forever when network
# briefly drops, leaving a chain of orphan git-remote-https processes the
# user can't see. Incident 2026-05-26 ~7:17AM: bare git fetch hung for
# 9 minutes before being killed manually. The 2>&1 | tail -1 trims the
# usual line spam but loses the original exit status, so we test the
# pipeline status with PIPESTATUS instead of relying on the implicit $?.
echo "Pulling latest code..."
GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=30 \
    git pull --ff-only origin master 2>&1 | tail -1
if [ "${PIPESTATUS[0]}" -ne 0 ]; then
    echo "  (REE_assembly pull skipped -- local changes present, offline, or stalled)"
fi
if [ -d "../ree-v3/.git" ]; then
    GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=30 \
        git -C ../ree-v3 pull --ff-only origin main 2>&1 | tail -1
    if [ "${PIPESTATUS[0]}" -ne 0 ]; then
        echo "  (ree-v3 pull skipped -- local changes present, offline, or stalled)"
    fi
fi
echo ""
echo "NOTE: If experiment_runner.py was updated, stop and restart the runner"
echo "      from the Explorer UI (Experiments tab) to pick up the new code."
echo ""

# Kill any existing serve.py on this port.
#
# NOTE: we used to run `lsof -ti :$PORT` here, but lsof probes every mount at
# startup, and a dead Time Machine SMB mount under /Volumes/.timemachine/ can
# put lsof into uninterruptible kernel IO wait (state U+ on macOS) that even
# `kill -9` can't release. Once that happens the launcher wedges until reboot.
# pgrep reads /proc-equivalent process tables only -- never touches mounts --
# so it's immune to that failure mode. (Incident: 2026-05-26 ~7:17AM, ttys267.)
existing_pid=$(pgrep -f "serve\.py.*--port $PORT" 2>/dev/null | head -1)
if [ -n "$existing_pid" ]; then
    echo "Port $PORT in use (PID $existing_pid) -- stopping it first..."
    kill "$existing_pid" 2>/dev/null
    sleep 1
fi

echo "+---------------------------------------------+"
echo "|  REE Claims Explorer                        |"
echo "|  Starting server on http://localhost:$PORT   |"
echo "|  Ctrl+C to stop                             |"
echo "+---------------------------------------------+"
echo ""

# Ensure correct machine identity for runner affinity matching
export REE_MACHINE_NAME=DLAPTOP-4.local

# Start server in background, capture PID
caffeinate -i python3 serve.py --port $PORT $BIND_ARGS &
SERVER_PID=$!

# Ensure server is killed cleanly when terminal closes or Ctrl+C is pressed
trap 'echo ""; echo "Stopping server..."; kill $SERVER_PID 2>/dev/null; wait $SERVER_PID 2>/dev/null; exit' INT TERM HUP

# Wait for server to be ready (up to 10 seconds)
echo -n "Waiting for server"
for i in {1..20}; do
    if curl -s -o /dev/null -w "" "http://localhost:$PORT/explorer.html" 2>/dev/null; then
        echo " ready!"
        break
    fi
    echo -n "."
    sleep 0.5
done
echo ""

if [ "$COORD_OK" -eq 1 ]; then
    verdict="$(curl -s "http://localhost:$PORT/api/shadow/status" 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('verdict','?'))" 2>/dev/null || echo "?")"
    echo "Shadow Coordination panel: $verdict"
    echo ""
fi

# Open explorer in default browser
open "http://localhost:$PORT/explorer"

echo ""
echo "Explorer opened in browser."
echo "Start experiment runners from the Experiments tab (V3/V2 Start buttons)."
echo ""
echo "-- Server log below (Ctrl+C to stop) --"
echo ""

# Bring server back to foreground so Ctrl+C stops it
wait $SERVER_PID
