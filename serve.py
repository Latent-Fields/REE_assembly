#!/usr/bin/env python3
"""
REE Claims Explorer Server

Replaces `python3 -m http.server` with a server that also manages the
experiment runner process via a small HTTP API.

Usage:
    cd ~/Documents/GitHub/REE_assembly
    python3 serve.py                  # http://localhost:8000
    python3 serve.py --port 9000

API (POST, called by the Experiments tab in the explorer):
    /api/runner/start  — launch experiment_runner.py in background
    /api/runner/stop   — send SIGTERM to the runner process

The runner writes progress to evidence/experiments/runner_status.json,
which the explorer polls automatically when the Experiments tab is open.
Output from the runner is appended to runner.log in this directory.

Stop the server: Ctrl+C  (also stops the runner if it was started here)
"""

import argparse
import http.server
import json
import os
import signal
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

# ── Paths ────────────────────────────────────────────────────────────────────

SERVE_DIR = Path(__file__).resolve().parent
RUNNER_SCRIPT = SERVE_DIR.parent / "ree-v1-minimal" / "experiment_runner.py"
STATUS_FILE = SERVE_DIR / "evidence" / "experiments" / "runner_status.json"
RUNNER_LOG = SERVE_DIR / "runner.log"
RUNNER_PID_FILE = SERVE_DIR.parent / "ree-v1-minimal" / "runner.pid"

DEFAULT_PORT = 8000

# ── Process state (module-level, single-threaded server) ─────────────────────

_runner_proc = None   # subprocess.Popen, set when we launched it
_runner_ext_pid = None  # int PID of a runner we didn't launch (detected at startup)


def _proc_alive(pid: int) -> bool:
    """Return True if a process with this PID is currently running."""
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def _detect_existing_runner():
    """On startup, check for a runner started in a previous server session."""
    global _runner_ext_pid
    if RUNNER_PID_FILE.exists():
        try:
            pid = int(RUNNER_PID_FILE.read_text().strip())
            if _proc_alive(pid):
                _runner_ext_pid = pid
                print(f"[serve] Detected existing runner PID {pid}", flush=True)
        except (ValueError, OSError):
            pass


def _runner_pid() -> int | None:
    """Return the PID of the running runner, or None."""
    if _runner_proc is not None and _runner_proc.poll() is None:
        return _runner_proc.pid
    if _runner_ext_pid and _proc_alive(_runner_ext_pid):
        return _runner_ext_pid
    # Final fallback: status file
    if STATUS_FILE.exists():
        try:
            s = json.loads(STATUS_FILE.read_text())
            pid = s.get("runner_pid")
            if pid and _proc_alive(int(pid)):
                return int(pid)
        except Exception:
            pass
    return None


def start_runner() -> dict:
    global _runner_proc
    pid = _runner_pid()
    if pid:
        return {"status": "already_running", "pid": pid}
    if not RUNNER_SCRIPT.exists():
        return {"status": "error", "message": f"Runner script not found: {RUNNER_SCRIPT}"}

    log_fh = open(RUNNER_LOG, "a")
    _runner_proc = subprocess.Popen(
        [sys.executable, str(RUNNER_SCRIPT),
         "--status-file", str(STATUS_FILE),
         "--loop", "--loop-interval", "60"],
        stdout=log_fh,
        stderr=log_fh,
        cwd=str(RUNNER_SCRIPT.parent),
    )
    print(f"[serve] Runner started (PID {_runner_proc.pid})", flush=True)
    return {"status": "started", "pid": _runner_proc.pid}


def stop_runner() -> dict:
    global _runner_proc, _runner_ext_pid

    # Try the subprocess we launched
    if _runner_proc is not None and _runner_proc.poll() is None:
        pid = _runner_proc.pid
        _runner_proc.terminate()
        try:
            _runner_proc.wait(timeout=6)
        except subprocess.TimeoutExpired:
            _runner_proc.kill()
        _runner_proc = None
        print(f"[serve] Runner stopped (PID {pid})", flush=True)
        return {"status": "stopped", "pid": pid}

    # Try a runner started outside this server session
    target_pid = _runner_ext_pid or _runner_pid()
    if target_pid:
        try:
            os.kill(target_pid, signal.SIGTERM)
            _runner_ext_pid = None
            print(f"[serve] Runner stopped via signal (PID {target_pid})", flush=True)
            return {"status": "stopped", "pid": target_pid}
        except (ProcessLookupError, PermissionError) as e:
            return {"status": "error", "message": str(e)}

    return {"status": "not_running"}


# ── HTTP handler ─────────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/runner/start":
            result = start_runner()
        elif path == "/api/runner/stop":
            result = stop_runner()
        else:
            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps(result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        # Handle CORS preflight (not normally needed on localhost)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def log_message(self, fmt, *args):
        # Only log API requests; suppress noisy static-file entries
        if "/api/" in (self.path or ""):
            super().log_message(fmt, *args)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="REE Claims Explorer Server")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Port to listen on (default: {DEFAULT_PORT})")
    args = parser.parse_args()

    _detect_existing_runner()
    os.chdir(SERVE_DIR)

    server = http.server.HTTPServer(("127.0.0.1", args.port), Handler)

    def shutdown(sig, frame):
        print("\n[serve] Shutting down.", flush=True)
        if _runner_proc and _runner_proc.poll() is None:
            print("[serve] Stopping runner process.", flush=True)
            _runner_proc.terminate()
        # server.shutdown() deadlocks when called from the main thread's signal
        # handler while serve_forever() is also on the main thread — use sys.exit.
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    url = f"http://localhost:{args.port}/docs/claims/explorer.html"
    print(f"[serve] REE Explorer → {url}", flush=True)
    print(f"[serve] Serving:       {SERVE_DIR}", flush=True)
    print(f"[serve] Runner script: {RUNNER_SCRIPT}", flush=True)
    print(f"[serve] Runner log:    {RUNNER_LOG}", flush=True)
    print(f"[serve] Ctrl+C to stop", flush=True)
    print(flush=True)

    server.serve_forever()


if __name__ == "__main__":
    main()
