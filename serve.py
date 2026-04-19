#!/usr/bin/env python3
"""
REE Claims Explorer Server

Replaces `python3 -m http.server` with a server that also manages the
experiment runner processes (V2 and V3) via a small HTTP API.

Usage:
    cd ~/REE_Working/REE_assembly
    caffeinate -i python3 serve.py    # http://localhost:8000/explorer
    python3 serve.py --port 9000

API (POST, called by the Experiments tab in the explorer):
    /api/runner/start             -- start V3 runner (default)
    /api/runner/stop              -- graceful drain: finish current experiment then stop
    /api/runner/force_stop        -- immediate SIGKILL (data loss acceptable)
    /api/runner/v3/start          -- start V3 runner
    /api/runner/v3/stop           -- graceful drain V3 runner
    /api/runner/v3/force_stop     -- force-kill V3 runner immediately
    /api/runner/v2/start          -- start V2 runner
    /api/runner/v2/stop           -- graceful drain V2 runner
    /api/runner/v2/force_stop     -- force-kill V2 runner immediately
    /api/runner/status            -- JSON status of both runners (includes draining flag)
    /api/review/tracker        -- GET: reviewed/discussed state from review_tracker.json
    /api/review/discuss        -- POST {dir_name, discussed}: toggle discussed_experiment_dirs

The runners write progress to evidence/experiments/runner_status.json,
which the explorer polls automatically when the Experiments tab is open.
Output from runners is appended to runner.log in this directory.

Stop the server: Ctrl+C  (also stops any runners started here)
"""

import argparse
import datetime
import http.server
import json
import os
import re
import signal
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml as _yaml
    _YAML_OK = True
except ImportError:
    _YAML_OK = False

# ── Paths ────────────────────────────────────────────────────────────────────

SERVE_DIR = Path(__file__).resolve().parent
STATUS_FILE = SERVE_DIR / "evidence" / "experiments" / "runner_status.json"  # legacy monolithic
STATUS_DIR = SERVE_DIR / "evidence" / "experiments" / "runner_status"       # per-machine split
RUNNER_LOG = SERVE_DIR / "runner.log"
REVIEW_TRACKER_FILE = SERVE_DIR / "evidence" / "experiments" / "review_tracker.json"
CONTRIBUTIONS_FILE  = SERVE_DIR / "contributors" / "contributions.json"

# Timeline data paths
_TL_CLAIMS_YAML     = SERVE_DIR / "docs" / "claims" / "claims.yaml"
_TL_CLAIM_EVIDENCE  = SERVE_DIR / "evidence" / "experiments" / "claim_evidence.v1.json"
_TL_EVIDENCE_DIR    = SERVE_DIR / "evidence" / "experiments"
_TL_LITERATURE_DIR  = SERVE_DIR / "evidence" / "literature"

_TL_MILESTONES = [
    {"date": "2026-02-13T00:00:00Z", "label": "Project start / first experiments",                   "kind": "start"},
    {"date": "2026-02-15T18:46:42Z", "label": "First governance batch (10 claims adjudicated)",       "kind": "governance"},
    {"date": "2026-02-25T16:56:00Z", "label": "Second governance batch",                              "kind": "governance"},
    {"date": "2026-02-26T00:00:00Z", "label": "ree-experiments-lab archived; V2 real substrate",      "kind": "architecture"},
    {"date": "2026-02-27T00:00:00Z", "label": "Epoch start: ree_hybrid_guardrails_v1",                "kind": "architecture"},
    {"date": "2026-03-06T00:00:00Z", "label": "SD-002 resolved: E1 prior wired into HippocampalModule","kind": "architecture"},
    {"date": "2026-03-14T00:00:00Z", "label": "SD-005: z_self/z_world split registered",              "kind": "architecture"},
    {"date": "2026-03-15T00:00:00Z", "label": "Control-plane heartbeat cluster registered",           "kind": "architecture"},
    {"date": "2026-03-16T00:00:00Z", "label": "Governance pipeline fixed; contamination corrected",   "kind": "governance"},
    {"date": "2026-03-18T00:00:00Z", "label": "V3 EXQ-013-019 root cause: SD-008/alpha_world",        "kind": "milestone"},
    {"date": "2026-03-19T00:00:00Z", "label": "V3 experiment series begins",                          "kind": "start"},
]

_TL_DATE_RE    = re.compile(r'\b(20\d{2}-\d{2}-\d{2})\b')
_TL_REG_RE     = re.compile(r'registered\s+(20\d{2}-\d{2}-\d{2})', re.IGNORECASE)
_TL_THOUGHT_RE = re.compile(r'docs/thoughts/(20\d{2}-\d{2}-\d{2})')

# Python executable -- prefer REE_PYTHON env var, then known torch-capable paths
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
        "evidence_dir": SERVE_DIR / "evidence" / "experiments",
        "python": V3_PYTHON,
        "label": "V3 (ree-v3)",
        "auto_sync": True,
    },
    "v2": {
        "script": SERVE_DIR.parent / "ree-v2" / "experiment_runner.py",
        "pid_file": SERVE_DIR.parent / "ree-v2" / "runner.pid",
        "queue_file": SERVE_DIR.parent / "ree-v2" / "experiment_queue.json",
        "evidence_dir": SERVE_DIR.parent / "ree-v2" / "evidence" / "experiments",
        "python": V2_PYTHON,
        "label": "V2 (ree-v2)",
        "auto_sync": True,
    },
}

DEFAULT_PORT = 8000

# ── GitHub fallback ───────────────────────────────────────────────────────────

ORG = "Latent-Fields"
ORG_MEMBERSHIP_URL = "https://github.com/orgs/Latent-Fields/teams"
REPO_NAMES: dict[str, str] = {
    "v3": "ree-v3",
    "v2": "ree-v2",
    "v1": "ree-v1-minimal",
}

_GIT_ACCESS_DENIED = re.compile(
    r"Repository not found|Permission denied|403|Authentication failed|could not read Username",
    re.IGNORECASE,
)


def _ensure_git_file(file_path: Path, repo_dir: Path, repo_name: str, clone_url: str) -> dict | None:
    """Ensure file_path exists, attempting git pull/clone if missing.
    Returns None on success, or an error dict on failure."""
    if file_path.exists():
        return None

    if (repo_dir / ".git").is_dir():
        cmd = ["git", "-C", str(repo_dir), "pull", "--ff-only"]
        action = "pull"
    else:
        cmd = ["git", "clone", clone_url, str(repo_dir)]
        action = "clone"

    print(f"[serve] {file_path.name} missing -- attempting git {action} from {clone_url}", flush=True)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return {"status": "error", "error": "timeout",
                "message": f"Git {action} timed out after 60s."}

    stderr_combined = result.stderr + result.stdout
    if result.returncode != 0 and _GIT_ACCESS_DENIED.search(stderr_combined):
        return {
            "status": "error",
            "error": "access_denied",
            "message": (
                f"Cannot access {ORG}/{repo_name} on GitHub. "
                "Request membership of the Latent-Fields organisation to gain access."
            ),
            "action_url": ORG_MEMBERSHIP_URL,
            "action_label": "Request Latent-Fields membership",
        }
    if result.returncode != 0:
        return {"status": "error", "error": "git_error",
                "message": f"Git {action} failed: {stderr_combined.strip()[:400]}"}
    if not file_path.exists():
        return {"status": "error", "error": "not_found",
                "message": f"{file_path.name} still missing after git {action}."}

    print(f"[serve] Git {action} succeeded -- {file_path.name} restored.", flush=True)
    return None


def _ensure_runner_script(ver: str) -> dict | None:
    cfg = RUNNERS[ver]
    script_path = cfg["script"]
    repo_name = REPO_NAMES[ver]
    clone_url = f"https://github.com/{ORG}/{repo_name}.git"
    return _ensure_git_file(script_path, script_path.parent, repo_name, clone_url)


def _ensure_explorer() -> dict | None:
    explorer_path = SERVE_DIR / "explorer.html"
    clone_url = f"https://github.com/{ORG}/REE_assembly.git"
    return _ensure_git_file(explorer_path, SERVE_DIR, "REE_assembly", clone_url)


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
        print(f"[serve] Ran {key} -> exit {result.returncode}", flush=True)
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


def load_review_tracker() -> dict:
    if REVIEW_TRACKER_FILE.exists():
        return json.loads(REVIEW_TRACKER_FILE.read_text())
    return {"schema_version": "review_tracker/v1", "reviewed_run_ids": [], "discussed_experiment_dirs": []}


def save_review_tracker(data: dict) -> None:
    REVIEW_TRACKER_FILE.write_text(json.dumps(data, indent=2) + "\n")


# Cache of experiment dir_name -> set(run_id). Rebuilt every _DIR_RUN_TTL seconds
# so the explorer can resolve `reviewed_run_ids` back to dir_names for the
# "discussed" badge without a startup migration. Scanning ~430 dirs takes ~2s.
_DIR_RUN_CACHE: dict = {"built_at": 0.0, "map": {}}
_DIR_RUN_TTL = 60.0


def _build_dir_to_runs() -> dict:
    """Scan evidence/experiments/ and build {dir_name: {run_id, ...}}.

    Reads manifest.json under each experiment dir (and any flat *.json files
    with a run_id field) so that runs marked in reviewed_run_ids can be matched
    back to their parent directory.
    """
    exp_root = SERVE_DIR / "evidence" / "experiments"
    result: dict = {}
    if not exp_root.is_dir():
        return result
    for d in exp_root.iterdir():
        if not d.is_dir():
            continue
        if d.name in ("runner_status", "schemas", "scripts"):
            continue
        runs: set = set()
        for m in d.glob("**/manifest.json"):
            try:
                data = json.loads(m.read_text())
                rid = data.get("run_id")
                if rid:
                    runs.add(rid)
            except Exception:
                pass
        for j in d.glob("*.json"):
            try:
                data = json.loads(j.read_text())
                if isinstance(data, dict):
                    rid = data.get("run_id")
                    if rid:
                        runs.add(rid)
            except Exception:
                pass
        if runs:
            result[d.name] = runs
    return result


def get_dir_to_runs() -> dict:
    now = time.time()
    if now - _DIR_RUN_CACHE["built_at"] > _DIR_RUN_TTL:
        _DIR_RUN_CACHE["map"] = _build_dir_to_runs()
        _DIR_RUN_CACHE["built_at"] = now
    return _DIR_RUN_CACHE["map"]


def read_merged_runner_status() -> dict:
    """Read and merge per-machine runner_status files into a single view.

    Falls back to the old monolithic runner_status.json if the per-machine
    directory doesn't exist yet (migration period).
    """
    machines = {}

    # Read per-machine files
    if STATUS_DIR.is_dir():
        for f in sorted(STATUS_DIR.glob("*.json")):
            try:
                machines[f.stem] = json.loads(f.read_text())
            except Exception:
                pass

    # Fallback: read old monolithic file if no per-machine files found
    if not machines and STATUS_FILE.exists():
        try:
            return json.loads(STATUS_FILE.read_text())
        except Exception:
            return {}

    if not machines:
        return {}

    # Merge
    all_completed = []
    seen_queue_ids = set()
    current_list = []
    any_running = False
    latest_update = ""
    merged_queue = []
    queue_ids_seen = set()

    for machine_name, data in machines.items():
        # Completed: deduplicate by queue_id, prefer non-ERROR
        for c in data.get("completed", []):
            qid = c.get("queue_id", "")
            if qid not in seen_queue_ids:
                seen_queue_ids.add(qid)
                all_completed.append(c)
            else:
                # Replace ERROR with non-ERROR if we have both
                if c.get("result") != "ERROR":
                    all_completed = [
                        (c if x.get("queue_id") == qid else x)
                        for x in all_completed
                    ]

        # Current: collect all running experiments
        cur = data.get("current")
        if cur:
            cur["_machine"] = machine_name
            current_list.append(cur)

        # Running state
        if not data.get("idle", True) and data.get("runner_pid"):
            any_running = True

        # Queue: merge, deduplicate
        for qi in data.get("queue", []):
            qid = qi.get("queue_id", "")
            if qid not in queue_ids_seen:
                queue_ids_seen.add(qid)
                merged_queue.append(qi)

        # Track latest update
        lu = data.get("last_updated", "")
        if lu > latest_update:
            latest_update = lu

    # Build merged result — same schema as old monolithic file
    merged = {
        "schema_version": "v1",
        "runner_pid": None,  # not meaningful for merged view
        "last_updated": latest_update,
        "idle": not any_running,
        "current": current_list[0] if current_list else None,
        "current_all": current_list if len(current_list) > 1 else None,
        "queue": merged_queue,
        "completed": all_completed,
        "machines": {
            name: {
                "runner_pid": d.get("runner_pid"),
                "idle": d.get("idle", True),
                "last_updated": d.get("last_updated", ""),
                "current": d.get("current"),
            }
            for name, d in machines.items()
        },
    }

    # If exactly one machine is running, use its PID for backward compat
    running_machines = [d for d in machines.values() if not d.get("idle", True) and d.get("runner_pid")]
    if len(running_machines) == 1:
        merged["runner_pid"] = running_machines[0]["runner_pid"]

    return merged


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
            # Exclude companion episode log files from run count
            files = sorted(
                f for f in exp_dir.glob("*.json")
                if not f.name.endswith("_episode_log.json")
            )
            if not files:
                continue
            latest = {}
            try:
                latest = json.loads(files[-1].read_text())
            except Exception:
                pass
            # Check for companion episode log alongside the latest result
            episode_log_url = None
            episode_log_file = exp_dir / f"{files[-1].stem}_episode_log.json"
            if episode_log_file.exists():
                try:
                    episode_log_url = str(episode_log_file.relative_to(SERVE_DIR))
                except ValueError:
                    pass
            result[exp_dir.name] = {
                "run_count": len(files),
                "latest_verdict": latest.get("verdict"),
                "latest_timestamp": latest.get("run_timestamp"),
                "claim_id": latest.get("claim"),
                "substrate": ver,
                "episode_log_url": episode_log_url,
            }
    return result


def start_runner(ver: str = "v3") -> dict:
    if ver not in RUNNERS:
        return {"status": "error", "message": f"Unknown substrate: {ver}"}

    cfg = RUNNERS[ver]
    pid = _runner_pid(ver)
    if pid:
        return {"status": "already_running", "pid": pid, "substrate": ver}
    err = _ensure_runner_script(ver)
    if err:
        return err

    python_exe = cfg["python"]
    if not os.path.exists(python_exe):
        python_exe = sys.executable  # fallback

    log_fh = open(RUNNER_LOG, "a")
    machine_name = os.environ.get("REE_MACHINE_NAME") or socket.gethostname()
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [python_exe, str(cfg["script"]),
           "--status-file", str(STATUS_DIR / f"{machine_name}.json"),
           "--machine", machine_name,
           "--loop"]  # Keep polling for new experiments after queue exhaustion
    if cfg.get("auto_sync"):
        cmd.append("--auto-sync")
    # STUB: future config could set per-runner flags from a machines.json config file
    proc = subprocess.Popen(
        cmd,
        stdout=log_fh,
        stderr=log_fh,
        cwd=str(cfg["script"].parent),
    )
    _runner_procs[ver] = proc
    print(f"[serve] {cfg['label']} runner started (PID {proc.pid})", flush=True)
    return {"status": "started", "pid": proc.pid, "substrate": ver}


def stop_runner(ver: str | None = None) -> dict:
    """Request graceful drain of a runner (ver='v3'/'v2') or any running runner.

    Sends SIGTERM which triggers the runner's drain mode: it finishes the current
    experiment then exits cleanly.  Returns immediately with status='draining' --
    the runner continues running until the experiment completes.

    Use force_stop_runner() for an immediate SIGKILL when data loss is acceptable.
    """
    versions_to_try = [ver] if ver else ["v3", "v2"]

    for v in versions_to_try:
        if v not in RUNNERS:
            continue
        cfg = RUNNERS[v]

        # Try the subprocess we launched
        proc = _runner_procs.get(v)
        if proc is not None and proc.poll() is None:
            pid = proc.pid
            proc.terminate()  # SIGTERM -> runner sets drain flag, finishes current experiment
            # Do NOT wait -- experiment may take minutes.  Runner will exit on its own.
            print(f"[serve] {cfg['label']} drain requested (PID {pid})", flush=True)
            return {"status": "draining", "pid": pid, "substrate": v}

        # Try a runner started outside this server session
        target_pid = _runner_ext_pids.get(v) or _runner_pid(v)
        if target_pid:
            try:
                os.kill(target_pid, signal.SIGTERM)
                _runner_ext_pids[v] = None
                print(f"[serve] {cfg['label']} drain requested via signal (PID {target_pid})",
                      flush=True)
                return {"status": "draining", "pid": target_pid, "substrate": v}
            except (ProcessLookupError, PermissionError) as e:
                return {"status": "error", "message": str(e)}

    return {"status": "not_running"}


def force_stop_runner(ver: str | None = None) -> dict:
    """Immediately kill a runner (SIGKILL).  Use when stopping cannot wait for experiment end.

    Data from any in-progress experiment will be lost.
    """
    versions_to_try = [ver] if ver else ["v3", "v2"]

    for v in versions_to_try:
        if v not in RUNNERS:
            continue
        cfg = RUNNERS[v]

        proc = _runner_procs.get(v)
        if proc is not None and proc.poll() is None:
            pid = proc.pid
            proc.kill()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
            _runner_procs[v] = None
            print(f"[serve] {cfg['label']} force-killed (PID {pid})", flush=True)
            return {"status": "stopped", "pid": pid, "substrate": v}

        target_pid = _runner_ext_pids.get(v) or _runner_pid(v)
        if target_pid:
            try:
                os.kill(target_pid, signal.SIGKILL)
                _runner_ext_pids[v] = None
                print(f"[serve] {cfg['label']} force-killed via signal (PID {target_pid})",
                      flush=True)
                return {"status": "stopped", "pid": target_pid, "substrate": v}
            except (ProcessLookupError, PermissionError) as e:
                return {"status": "error", "message": str(e)}

    return {"status": "not_running"}


def runner_status() -> dict:
    """Return status of all runners, including draining flag."""
    # Read per-machine status files once to check for draining state.
    draining_any = False
    try:
        if STATUS_DIR.is_dir():
            for f in STATUS_DIR.glob("*.json"):
                try:
                    d = json.loads(f.read_text())
                    if d.get("draining") and not d.get("idle", True):
                        draining_any = True
                        break
                except Exception:
                    pass
    except Exception:
        pass

    result = {}
    for ver in RUNNERS:
        pid = _runner_pid(ver)
        result[ver] = {
            "running": pid is not None,
            "pid": pid,
            "label": RUNNERS[ver]["label"],
            # draining: runner is alive but finishing current experiment before stopping.
            # Only meaningful for V3 (V2 is archived); attached to the ver that is actually running.
            "draining": draining_any and pid is not None,
        }
    return result


def read_queue(ver: str) -> dict:
    """Read experiment_queue.json for a substrate. Queue file is authoritative for status."""
    if ver not in RUNNERS:
        return {"error": f"Unknown substrate: {ver}"}
    qf = RUNNERS[ver]["queue_file"]
    if not qf.exists():
        return {"items": [], "ver": ver}
    try:
        data = json.loads(qf.read_text())
    except Exception:
        return {"items": [], "ver": ver}

    items = []
    for item in data.get("items", []):
        qid = item.get("queue_id", "")
        items.append({
            "queue_id": qid,
            "claim_id": item.get("claim_id", ""),
            "title": item.get("title", ""),
            "description": item.get("description", ""),
            "status": item.get("status", "pending"),
            "script": item.get("script", ""),
            "estimated_minutes": item.get("estimated_minutes"),
            "machine_affinity": item.get("machine_affinity", ""),
            "ree_version": ver,
        })
    return {"items": items, "ver": ver}


# ── Timeline builder ─────────────────────────────────────────────────────────

def _tl_utc_now() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def _tl_claim_date(claim: dict) -> tuple:
    """Return (iso_date_str_or_None, confidence_str) for a claim dict.
    Confidence: 'adjudicated' | 'inferred' | 'thought_file' | 'unknown'
    """
    adj = claim.get("adjudicated_at_utc")
    if adj:
        return str(adj), "adjudicated"
    # Search note fields for explicit "registered YYYY-MM-DD" pattern first
    for field in ("evidence_quality_note", "reframe_note", "notes"):
        txt = str(claim.get(field) or "")
        m = _TL_REG_RE.search(txt)
        if m:
            return m.group(1) + "T00:00:00Z", "inferred"
    # Fallback: earliest date found in any note field
    all_dates = []
    for field in ("evidence_quality_note", "reframe_note", "notes"):
        all_dates += _TL_DATE_RE.findall(str(claim.get(field) or ""))
    if all_dates:
        return min(all_dates) + "T00:00:00Z", "inferred"
    # Fallback: date from thought-file in source list
    for src in (claim.get("source") or []):
        m = _TL_THOUGHT_RE.search(str(src))
        if m:
            return m.group(1) + "T00:00:00Z", "thought_file"
    return None, "unknown"


def _tl_load_claims() -> list:
    """Load claims list from claims.yaml. Returns [] on failure."""
    if not _TL_CLAIMS_YAML.exists():
        return []
    try:
        if _YAML_OK:
            raw = _yaml.safe_load(_TL_CLAIMS_YAML.read_text())
            claims_list = raw.get("claims", []) if isinstance(raw, dict) else (raw or [])
        else:
            # Minimal regex fallback if PyYAML unavailable
            claims_list = []
    except Exception:
        claims_list = []
    return claims_list or []


def _build_timeline_events() -> dict:
    """Build the timeline events payload from all available data sources."""
    events = []
    claims_map = {}

    # --- Claims ---
    for c in _tl_load_claims():
        cid = str(c.get("id") or "")
        if not cid:
            continue
        dt, conf = _tl_claim_date(c)
        claims_map[cid] = {
            "id": cid,
            "title": str(c.get("title") or ""),
            "claim_type": str(c.get("claim_type") or ""),
            "status": str(c.get("status") or ""),
            "lifecycle_stage": str(c.get("lifecycle_stage") or ""),
            "confidence": c.get("confidence"),
            "depends_on": list(c.get("depends_on") or []),
            "v3_pending": bool(c.get("v3_pending")),
            "estimated_at": dt,
            "date_confidence": conf,
        }
        events.append({
            "type": "claim",
            "date": dt or "2026-02-13T00:00:00Z",
            "date_confidence": conf,
            "claim_id": cid,
            "claim_type": str(c.get("claim_type") or ""),
            "status": str(c.get("status") or ""),
            "title": str(c.get("title") or ""),
        })
        if c.get("adjudicated_at_utc"):
            events.append({
                "type": "governance",
                "date": str(c["adjudicated_at_utc"]),
                "date_confidence": "exact",
                "claim_id": cid,
                "outcome": str(c.get("adjudication_outcome") or ""),
            })

    # --- Experiment manifests ---
    if _TL_EVIDENCE_DIR.exists():
        for mf in sorted(_TL_EVIDENCE_DIR.glob("**/runs/**/manifest.json")):
            try:
                m = json.loads(mf.read_text())
            except Exception:
                continue
            ts = str(m.get("timestamp_utc") or "").strip()
            if not ts:
                continue
            events.append({
                "type": "experiment",
                "date": ts,
                "date_confidence": "exact",
                "run_id": str(m.get("run_id") or ""),
                "experiment_type": str(m.get("experiment_type") or ""),
                "status": str(m.get("status") or "UNKNOWN").upper(),
                "claim_ids": [str(x) for x in (
                    m.get("claim_ids_tested") or m.get("claim_ids") or []
                ) if x],
                "evidence_direction": str(m.get("evidence_direction") or "unknown"),
                "architecture_epoch": str(m.get("architecture_epoch") or ""),
            })

    # --- Literature records ---
    if _TL_LITERATURE_DIR.exists():
        for rf in sorted(_TL_LITERATURE_DIR.glob("**/record.json")):
            try:
                r = json.loads(rf.read_text())
            except Exception:
                continue
            ts = str(r.get("timestamp_utc") or "").strip()
            if not ts:
                continue
            events.append({
                "type": "literature",
                "date": ts,
                "date_confidence": "exact",
                "entry_id": str(r.get("entry_id") or ""),
                "claim_ids": [str(x) for x in (r.get("claim_ids") or []) if x],
                "evidence_direction": str(r.get("evidence_direction") or "unknown"),
                "title": str((r.get("source") or {}).get("title") or ""),
            })

    # --- Milestones ---
    for ms in _TL_MILESTONES:
        events.append({**ms, "type": "milestone", "date_confidence": "exact"})

    events.sort(key=lambda e: str(e.get("date") or ""))

    # --- Confidence series ---
    confidence_series = {}
    try:
        cev = json.loads(_TL_CLAIM_EVIDENCE.read_text())
        for cid, cdata in (cev.get("claims") or {}).items():
            entries = sorted(
                [e for e in (cdata.get("recent_entries") or []) if e.get("timestamp_utc")],
                key=lambda e: str(e["timestamp_utc"]),
            )
            pts = [
                {
                    "date": str(e["timestamp_utc"]),
                    "confidence": e.get("confidence"),
                    "source_type": e.get("source_type", "experimental"),
                    "status": e.get("status", ""),
                }
                for e in entries if e.get("confidence") is not None
            ]
            if pts:
                confidence_series[cid] = pts
    except Exception:
        pass

    date_vals = [e["date"] for e in events if e.get("date")]
    return {
        "schema_version": "timeline/v1",
        "generated_at": _tl_utc_now(),
        "date_range": {
            "start": min(date_vals) if date_vals else "2026-02-13T00:00:00Z",
            "end":   max(date_vals) if date_vals else "2026-03-25T00:00:00Z",
        },
        "events": events,
        "claims": claims_map,
        "milestones": _TL_MILESTONES,
        "confidence_series": confidence_series,
    }


# ── HTTP handler ─────────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path
        # Ensure explorer.html is present; attempt GitHub pull/clone if missing
        if path in ("/explorer", "/explorer.html"):
            if not (SERVE_DIR / "explorer.html").exists():
                err = _ensure_explorer()
                if err:
                    self._html_error_page(err)
                    return
        # Short URL: /explorer -> /explorer.html
        if path == "/explorer":
            self.send_response(302)
            self.send_header("Location", "/explorer.html")
            self.end_headers()
            return
        # Serve explorer.html with no-cache headers so browser always gets the latest version
        if path == "/explorer.html":
            content = (SERVE_DIR / "explorer.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
            self.wfile.write(content)
            return
        if path == "/api/evidence/runs":
            body = json.dumps(scan_evidence_runs()).encode()
            self._json_response(body)
            return
        # Intercept runner_status.json requests -- return merged per-machine view
        if path == "/evidence/experiments/runner_status.json":
            body = json.dumps(read_merged_runner_status(), indent=2).encode()
            self._json_response(body)
            return
        if path == "/api/runner/status":
            body = json.dumps(runner_status()).encode()
            self._json_response(body)
            return
        # STUB /api/machines -- future endpoint returning status of all known machines
        # (hostnames, last-seen, queue assignments, GPU info from machines.json config)
        if path == "/api/queue/v3":
            body = json.dumps(read_queue("v3")).encode()
            self._json_response(body)
            return
        if path == "/api/queue/v2":
            body = json.dumps(read_queue("v2")).encode()
            self._json_response(body)
            return
        if path == "/api/contributions":
            if CONTRIBUTIONS_FILE.exists():
                body = CONTRIBUTIONS_FILE.read_bytes()
            else:
                body = json.dumps({"error": "contributions.json not yet generated -- run contributors/build_contributions.py"}).encode()
            self._json_response(body)
            return
        if path in ("/setup", "/contributors/setup.html"):
            setup_page = SERVE_DIR / "contributors" / "setup.html"
            if setup_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(setup_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path in ("/contribute", "/contribute.html"):
            contribute_page = SERVE_DIR / "docs" / "contribute.html"
            if contribute_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(contribute_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path == "/api/timeline/events":
            body = json.dumps(_build_timeline_events()).encode()
            self._json_response(body)
            return
        if path == "/api/fishtank/logs":
            logs = []
            exp_root = SERVE_DIR / "evidence" / "experiments"
            if exp_root.exists():
                for log_file in sorted(exp_root.glob("**/*_episode_log.json"), reverse=True):
                    rel = log_file.relative_to(SERVE_DIR)
                    parts = rel.parts  # ('evidence', 'experiments', '<exp_dir>', '<filename>')
                    exp_name = parts[2] if len(parts) >= 3 else str(rel.parent)
                    stem = log_file.stem.replace("_episode_log", "")
                    logs.append({
                        "experiment": exp_name,
                        "run": stem,
                        "path": str(rel).replace("\\", "/"),
                    })
            body = json.dumps({"logs": logs}).encode()
            self._json_response(body)
            return
        if path == "/api/review/tracker":
            data = load_review_tracker()
            # Map reviewed_run_ids back to experiment dir_names via manifests on
            # disk so previously-reviewed runs show as "discussed" in the explorer
            # (explorer.html matches by dir_name only). Ad-hoc regex derivation
            # misses claim_probe_* dirs whose manifest run_ids don't match the
            # dir name (e.g. claim_probe_arc_016 contains precision_regime_probe).
            reviewed_set = set(data.get("reviewed_run_ids", []))
            reviewed_dirs = {
                dir_name for dir_name, runs in get_dir_to_runs().items()
                if runs & reviewed_set
            }
            # Also emit queue_id aliases (e.g. "V3-EXQ-028") so explorer cards
            # whose output_file is missing (falls back to queue_id for dir_name)
            # still resolve as discussed.
            queue_aliases = set()
            for dir_name in reviewed_dirs:
                m = re.match(r'v([123])_exq_(\w+?)(?:_|$)', dir_name)
                if m:
                    queue_aliases.add(f"V{m.group(1)}-EXQ-{m.group(2)}")
            discussed = list(
                set(data.get("discussed_experiment_dirs", []))
                | reviewed_dirs
                | queue_aliases
            )
            body = json.dumps({
                "discussed_experiment_dirs": discussed,
                "reviewed_run_ids": data.get("reviewed_run_ids", []),
                "last_review_utc": data.get("last_review_utc", ""),
            }).encode()
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
        elif path == "/api/runner/v3/force_stop":
            result = force_stop_runner("v3")
        elif path == "/api/runner/v2/start":
            result = start_runner("v2")
        elif path == "/api/runner/v2/stop":
            result = stop_runner("v2")
        elif path == "/api/runner/v2/force_stop":
            result = force_stop_runner("v2")
        # Legacy endpoints (default to V3)
        elif path == "/api/runner/start":
            result = start_runner("v3")
        elif path == "/api/runner/stop":
            result = stop_runner()  # stop any
        elif path == "/api/runner/force_stop":
            result = force_stop_runner()  # force-stop any
        elif path == "/api/run":
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length) or b'{}')
            result = run_script(body.get('script', ''))
        elif path == "/api/review/discuss":
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length) or b"{}")
            dir_name = payload.get("dir_name", "").strip()
            discussed = bool(payload.get("discussed", True))
            if dir_name:
                data = load_review_tracker()
                dirs = data.setdefault("discussed_experiment_dirs", [])
                if discussed and dir_name not in dirs:
                    dirs.append(dir_name)
                elif not discussed and dir_name in dirs:
                    dirs.remove(dir_name)
                save_review_tracker(data)
                result = {"status": "ok", "discussed_experiment_dirs": dirs}
            else:
                result = {"status": "error", "message": "missing dir_name"}
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

    def _html_error_page(self, err: dict):
        message = err.get("message", "An error occurred.")
        action_url = err.get("action_url", "")
        action_label = err.get("action_label", "Learn more")
        link_html = (
            f'<p><a href="{action_url}" target="_blank">{action_label} &rarr;</a></p>'
            if action_url else ""
        )
        body = f"""<!DOCTYPE html>
<html><head><title>REE Explorer -- Access Error</title>
<style>body{{font-family:system-ui,sans-serif;max-width:600px;margin:80px auto;padding:0 20px;color:#333}}
h1{{color:#c00}}a{{color:#0070f3}}</style></head>
<body><h1>Cannot load REE Explorer</h1><p>{message}</p>{link_html}</body></html>""".encode()
        self.send_response(503)
        self.send_header("Content-Type", "text/html; charset=utf-8")
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

    server = http.server.ThreadingHTTPServer(("0.0.0.0", args.port), Handler)

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
    print(f"[serve] REE Explorer -> {url}", flush=True)
    print(f"[serve] Serving:       {SERVE_DIR}", flush=True)
    for ver, cfg in RUNNERS.items():
        exists = "✓" if cfg["script"].exists() else "✗"
        print(f"[serve] {cfg['label']} runner: {cfg['script']} [{exists}]", flush=True)
        print(f"[serve] {cfg['label']} python:  {cfg['python']}", flush=True)
    print(f"[serve] Runner log:    {RUNNER_LOG}", flush=True)
    print(f"[serve] Ctrl+C to stop", flush=True)
    print(flush=True)

    def _auto_pull():
        """Background thread: pull REE_assembly and ree-v3 every 5 minutes."""
        repos = [SERVE_DIR, SERVE_DIR.parent / "ree-v3"]
        while True:
            time.sleep(300)
            for repo in repos:
                if not (repo / ".git").is_dir():
                    continue
                result = subprocess.run(
                    ["git", "-C", str(repo), "pull", "--ff-only"],
                    capture_output=True, text=True, timeout=30,
                )
                if result.returncode == 0 and "Already up to date" not in result.stdout:
                    print(f"[serve] git pull {repo.name}: {result.stdout.strip()}", flush=True)
                elif result.returncode != 0:
                    print(f"[serve] git pull {repo.name} failed: {result.stderr.strip()}", flush=True)

    threading.Thread(target=_auto_pull, daemon=True, name="auto-pull").start()
    print("[serve] Auto-pull: every 5 min (REE_assembly + ree-v3)", flush=True)

    server.serve_forever()


if __name__ == "__main__":
    main()
