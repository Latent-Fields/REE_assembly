#!/usr/bin/env python3
"""
REE Claims Explorer Server

Replaces `python3 -m http.server` with a server that also manages the
experiment runner processes (V2 and V3) via a small HTTP API.

Usage:
    cd ~/Documents/GitHub/REE_Working/REE_assembly
    caffeinate -i python3 serve.py    # http://localhost:8000/explorer
    python3 serve.py --port 9000

API (POST, called by the Experiments tab in the explorer):
    /api/runner/start          — start V3 runner (default)
    /api/runner/stop           — stop whichever runner is running
    /api/runner/v3/start       — start V3 runner
    /api/runner/v3/stop        — stop V3 runner
    /api/runner/v2/start       — start V2 runner
    /api/runner/v2/stop        — stop V2 runner
    /api/runner/status         — JSON status of both runners

The runners write progress to evidence/experiments/runner_status.json,
which the explorer polls automatically when the Experiments tab is open.
Output from runners is appended to runner.log in this directory.

Stop the server: Ctrl+C  (also stops any runners started here)
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
STATUS_FILE = SERVE_DIR / "evidence" / "experiments" / "runner_status.json"
RUNNER_LOG = SERVE_DIR / "runner.log"

# Python executable — prefer REE_PYTHON env var, then known torch-capable paths
def _default_python() -> str:
    if env := os.environ.get("REE_PYTHON"):
        return env
    for p in (
        "/opt/local/bin/python3",           # macOS MacPorts
        "/opt/homebrew/bin/python3",        # macOS Homebrew
        "/home/ree/.venv/ree/bin/python3",  # Linux venv (see remote_setup.sh)
    ):
        if os.path.exists(p):
            return p
    return sys.executable

_DEFAULT_PYTHON = _default_python()
V3_PYTHON = _DEFAULT_PYTHON
V2_PYTHON = _DEFAULT_PYTHON

# Runner configs keyed by substrate version
RUNNERS = {
    "v3": {
        "script": SERVE_DIR.parent / "ree-v3" / "experiment_runner.py",
        "pid_file": SERVE_DIR.parent / "ree-v3" / "runner.pid",
        "queue_file": SERVE_DIR.parent / "ree-v3" / "experiment_queue.json",
        "evidence_dir": SERVE_DIR.parent / "ree-v3" / "evidence" / "experiments",
        "python": V3_PYTHON,
        "label": "V3 (ree-v3)",
    },
    "v2": {
        "script": SERVE_DIR.parent / "ree-v2" / "experiment_runner.py",
        "pid_file": SERVE_DIR.parent / "ree-v2" / "runner.pid",
        "queue_file": SERVE_DIR.parent / "ree-v2" / "experiment_queue.json",
        "evidence_dir": SERVE_DIR.parent / "ree-v2" / "evidence" / "experiments",
        "python": V2_PYTHON,
        "label": "V2 (ree-v2)",
    },
}

DEFAULT_PORT = 8000

# ── Process state (module-level, single-threaded server) ─────────────────────

# Track launched processes per substrate: {"v3": Popen, "v2": Popen}
_runner_procs: dict[str, subprocess.Popen | None] = {"v3": None, "v2": None}
# Track externally-detected PIDs per substrate
_runner_ext_pids: dict[str, int | None] = {"v3": None, "v2": None}


def _proc_alive(pid: int) -> bool:
    """Return True if a process with this PID is currently running."""
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def _detect_existing_runners():
    """On startup, check for runners started in a previous server session."""
    for ver, cfg in RUNNERS.items():
        pid_file = cfg["pid_file"]
        if pid_file.exists():
            try:
                pid = int(pid_file.read_text().strip())
                if _proc_alive(pid):
                    _runner_ext_pids[ver] = pid
                    print(f"[serve] Detected existing {cfg['label']} runner PID {pid}", flush=True)
            except (ValueError, OSError):
                pass


def _runner_pid(ver: str) -> int | None:
    """Return the PID of the running runner for a given substrate, or None."""
    proc = _runner_procs.get(ver)
    if proc is not None and proc.poll() is None:
        return proc.pid
    ext = _runner_ext_pids.get(ver)
    if ext and _proc_alive(ext):
        return ext
    # Fallback: check PID file
    pid_file = RUNNERS[ver]["pid_file"]
    if pid_file.exists():
        try:
            pid = int(pid_file.read_text().strip())
            if _proc_alive(pid):
                return pid
        except (ValueError, OSError):
            pass
    return None


def _any_runner_pid() -> int | None:
    """Return PID of any running runner (for legacy /api/runner/stop)."""
    for ver in ["v3", "v2"]:
        pid = _runner_pid(ver)
        if pid:
            return pid
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


# ── Script allowlist ─────────────────────────────────────────────────────────

ALLOWED_SCRIPTS: dict[str, tuple[list[str], int]] = {
    'governance':        ([sys.executable, str(SERVE_DIR / 'evidence/planning/scripts/run_governance_cycle.py')], 120),
    'governance_strict': ([sys.executable, str(SERVE_DIR / 'evidence/planning/scripts/run_governance_cycle.py'), '--strict-thoughts'], 120),
    'build_indexes':     ([sys.executable, str(SERVE_DIR / 'evidence/experiments/scripts/build_experiment_indexes.py')], 60),
    'cutover_check':     ([sys.executable, str(SERVE_DIR / 'evidence/planning/scripts/check_ree_v2_cutover_readiness.py')], 30),
    'sync_task_inbox':   ([sys.executable, str(SERVE_DIR / 'evidence/planning/scripts/sync_task_inbox.py')], 30),
    'thought_sweep':     ([sys.executable, str(SERVE_DIR / 'docs/thoughts/scripts/thought_sweep.py')], 60),
}


def run_script(key: str) -> dict:
    if key not in ALLOWED_SCRIPTS:
        return {"status": "error", "message": f"Unknown script key: {key!r}"}
    cmd, timeout = ALLOWED_SCRIPTS[key]
    script_path = cmd[1]
    if not os.path.exists(script_path):
        return {"status": "error", "message": f"Script not found: {script_path}"}
    try:
        result = subprocess.run(
            cmd, cwd=str(SERVE_DIR),
            capture_output=True, text=True, timeout=timeout,
        )
        print(f"[serve] Ran {key} → exit {result.returncode}", flush=True)
        return {
            "status": "ok" if result.returncode == 0 else "error",
            "returncode": result.returncode,
            "stdout": result.stdout[-8000:],
            "stderr": result.stderr[-2000:],
        }
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": f"Timed out after {timeout}s"}
    except Exception as exc:
        return {"status": "error", "message": str(exc)}


def scan_evidence_runs() -> dict:
    """Scan evidence/experiments dirs for actual run counts on disk."""
    result = {}
    for ver, cfg in RUNNERS.items():
        ev_dir = cfg["evidence_dir"]
        if not ev_dir.exists():
            continue
        for exp_dir in sorted(ev_dir.iterdir()):
            if not exp_dir.is_dir():
                continue
            files = sorted(exp_dir.glob("*.json"))
            if not files:
                continue
            latest = {}
            try:
                latest = json.loads(files[-1].read_text())
            except Exception:
                pass
            result[exp_dir.name] = {
                "run_count": len(files),
                "latest_verdict": latest.get("verdict"),
                "latest_timestamp": latest.get("run_timestamp"),
                "claim_id": latest.get("claim"),
                "substrate": ver,
            }
    return result


def start_runner(ver: str = "v3") -> dict:
    if ver not in RUNNERS:
        return {"status": "error", "message": f"Unknown substrate: {ver}"}

    cfg = RUNNERS[ver]
    pid = _runner_pid(ver)
    if pid:
        return {"status": "already_running", "pid": pid, "substrate": ver}
    if not cfg["script"].exists():
        return {"status": "error", "message": f"Runner script not found: {cfg['script']}"}

    python_exe = cfg["python"]
    if not os.path.exists(python_exe):
        python_exe = sys.executable  # fallback

    log_fh = open(RUNNER_LOG, "a")
    proc = subprocess.Popen(
        [python_exe, str(cfg["script"]),
         "--status-file", str(STATUS_FILE)],
        stdout=log_fh,
        stderr=log_fh,
        cwd=str(cfg["script"].parent),
    )
    _runner_procs[ver] = proc
    print(f"[serve] {cfg['label']} runner started (PID {proc.pid})", flush=True)
    return {"status": "started", "pid": proc.pid, "substrate": ver}


def stop_runner(ver: str | None = None) -> dict:
    """Stop a specific runner (ver='v3'/'v2') or any running runner (ver=None)."""
    versions_to_try = [ver] if ver else ["v3", "v2"]

    for v in versions_to_try:
        if v not in RUNNERS:
            continue
        cfg = RUNNERS[v]

        # Try the subprocess we launched
        proc = _runner_procs.get(v)
        if proc is not None and proc.poll() is None:
            pid = proc.pid
            proc.terminate()
            try:
                proc.wait(timeout=6)
            except subprocess.TimeoutExpired:
                proc.kill()
            _runner_procs[v] = None
            print(f"[serve] {cfg['label']} runner stopped (PID {pid})", flush=True)
            return {"status": "stopped", "pid": pid, "substrate": v}

        # Try a runner started outside this server session
        target_pid = _runner_ext_pids.get(v) or _runner_pid(v)
        if target_pid:
            try:
                os.kill(target_pid, signal.SIGTERM)
                _runner_ext_pids[v] = None
                print(f"[serve] {cfg['label']} runner stopped via signal (PID {target_pid})", flush=True)
                return {"status": "stopped", "pid": target_pid, "substrate": v}
            except (ProcessLookupError, PermissionError) as e:
                return {"status": "error", "message": str(e)}

    return {"status": "not_running"}


def runner_status() -> dict:
    """Return status of all runners."""
    result = {}
    for ver in RUNNERS:
        pid = _runner_pid(ver)
        result[ver] = {
            "running": pid is not None,
            "pid": pid,
            "label": RUNNERS[ver]["label"],
        }
    return result


def read_queue(ver: str) -> dict:
    """Read experiment_queue.json for a substrate, cross-referencing completed items."""
    if ver not in RUNNERS:
        return {"error": f"Unknown substrate: {ver}"}
    qf = RUNNERS[ver]["queue_file"]
    if not qf.exists():
        return {"items": [], "ver": ver}
    try:
        data = json.loads(qf.read_text())
    except Exception:
        return {"items": [], "ver": ver}

    # Get completed queue_ids from runner_status.json
    completed_ids = set()
    if STATUS_FILE.exists():
        try:
            status = json.loads(STATUS_FILE.read_text())
            for c in status.get("completed", []):
                completed_ids.add(c.get("queue_id"))
        except Exception:
            pass

    # Annotate each item with whether it's already completed
    items = []
    for item in data.get("items", []):
        qid = item.get("queue_id", "")
        items.append({
            "queue_id": qid,
            "claim_id": item.get("claim_id", ""),
            "title": item.get("title", ""),
            "description": item.get("description", ""),
            "status": "completed" if qid in completed_ids else item.get("status", "pending"),
            "script": item.get("script", ""),
            "ree_version": ver,
        })
    return {"items": items, "ver": ver}


# ── HTTP handler ─────────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path
        # Short URL: /explorer → /explorer.html
        if path == "/explorer":
            self.send_response(302)
            self.send_header("Location", "/explorer.html")
            self.end_headers()
            return
        if path == "/api/evidence/runs":
            body = json.dumps(scan_evidence_runs()).encode()
            self._json_response(body)
            return
        if path == "/api/runner/status":
            body = json.dumps(runner_status()).encode()
            self._json_response(body)
            return
        if path == "/api/queue/v3":
            body = json.dumps(read_queue("v3")).encode()
            self._json_response(body)
            return
        if path == "/api/queue/v2":
            body = json.dumps(read_queue("v2")).encode()
            self._json_response(body)
            return
        super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path

        # Versioned runner endpoints
        if path == "/api/runner/v3/start":
            result = start_runner("v3")
        elif path == "/api/runner/v3/stop":
            result = stop_runner("v3")
        elif path == "/api/runner/v2/start":
            result = start_runner("v2")
        elif path == "/api/runner/v2/stop":
            result = stop_runner("v2")
        # Legacy endpoints (default to V3)
        elif path == "/api/runner/start":
            result = start_runner("v3")
        elif path == "/api/runner/stop":
            result = stop_runner()  # stop any
        elif path == "/api/run":
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length) or b'{}')
            result = run_script(body.get('script', ''))
        else:
            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps(result).encode()
        self._json_response(body)

    def end_headers(self):
        """Add no-cache headers to all responses so the browser always gets fresh content."""
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def _json_response(self, body: bytes, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def log_message(self, fmt, *args):
        if "/api/" in (self.path or ""):
            super().log_message(fmt, *args)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="REE Claims Explorer Server")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Port to listen on (default: {DEFAULT_PORT})")
    parser.add_argument("--python", type=str, default=None,
                        help="Python executable to use for runners "
                             "(default: auto-detect via REE_PYTHON env or known paths)")
    args = parser.parse_args()

    if args.python:
        for cfg in RUNNERS.values():
            cfg["python"] = args.python

    _detect_existing_runners()
    os.chdir(SERVE_DIR)

    server = http.server.HTTPServer(("0.0.0.0", args.port), Handler)

    def shutdown(sig, frame):
        print("\n[serve] Shutting down.", flush=True)
        for ver, proc in _runner_procs.items():
            if proc and proc.poll() is None:
                print(f"[serve] Stopping {RUNNERS[ver]['label']} runner.", flush=True)
                proc.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    url = f"http://localhost:{args.port}/explorer"
    print(f"[serve] REE Explorer → {url}", flush=True)
    print(f"[serve] Serving:       {SERVE_DIR}", flush=True)
    for ver, cfg in RUNNERS.items():
        exists = "✓" if cfg["script"].exists() else "✗"
        print(f"[serve] {cfg['label']} runner: {cfg['script']} [{exists}]", flush=True)
        print(f"[serve] {cfg['label']} python:  {cfg['python']}", flush=True)
    print(f"[serve] Runner log:    {RUNNER_LOG}", flush=True)
    print(f"[serve] Ctrl+C to stop", flush=True)
    print(flush=True)

    server.serve_forever()


if __name__ == "__main__":
    main()
