#!/bin/bash
# ── REE Claims Explorer Launcher ──────────────────────────────────────────
# Double-click this file in Finder to start the explorer server and open it.
# Close this Terminal window (or Ctrl+C) to stop the server.
# ───────────────────────────────────────────────────────────────────────────

cd "$(dirname "$0")"
PORT=8000

# ── Pull latest code before starting ─────────────────────────────────────────
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

echo "┌─────────────────────────────────────────────┐"
echo "│  REE Claims Explorer                        │"
echo "│  Starting server on http://localhost:$PORT   │"
echo "│  Ctrl+C to stop                             │"
echo "└─────────────────────────────────────────────┘"
echo ""

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

# Open explorer in default browser
open "http://localhost:$PORT/explorer"

echo ""
echo "Explorer opened in browser."
echo "Start experiment runners from the Experiments tab (V3/V2 Start buttons)."
echo ""
echo "── Server log below (Ctrl+C to stop) ──"
echo ""

# Bring server back to foreground so Ctrl+C stops it
wait $SERVER_PID
