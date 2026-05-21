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
echo "Pulling latest code..."
git pull --ff-only origin master 2>&1 | tail -1 || echo "  (REE_assembly pull skipped -- local changes present or offline)"
if [ -d "../ree-v3/.git" ]; then
    git -C ../ree-v3 pull --ff-only origin main 2>&1 | tail -1 || echo "  (ree-v3 pull skipped -- local changes present or offline)"
fi
echo ""
echo "NOTE: If experiment_runner.py was updated, stop and restart the runner"
echo "      from the Explorer UI (Experiments tab) to pick up the new code."
echo ""

# Kill any existing serve.py on this port
existing_pid=$(lsof -ti :$PORT 2>/dev/null)
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
caffeinate -i python3 serve.py --port $PORT &
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
