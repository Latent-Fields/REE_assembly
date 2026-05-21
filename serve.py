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
    /api/regression/preflight  -- GET: ree-v3 preflight suite result (cached 60s)

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
HEARTBEAT_DIR = SERVE_DIR / "evidence" / "experiments" / "runner_heartbeats"  # per-machine heartbeats
COMMANDS_DIR = SERVE_DIR / "evidence" / "experiments" / "runner_commands"     # per-machine command queues
RUNNER_LOG = SERVE_DIR / "runner.log"
PLANNING_DIR = SERVE_DIR / "evidence" / "planning"
WORKSET_JSON_FILE = PLANNING_DIR / "inter_governance_workset.v1.json"

# Command kinds the runner accepts (mirrors ree-v3/runner_remote_control.VALID_COMMAND_KINDS)
VALID_REMOTE_COMMAND_KINDS = (
    "stop", "force_stop", "pause", "resume", "kick", "release_claim",
)
MAX_REMOTE_COMMAND_HISTORY = 50
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
        "remote_control": True,
    },
    "v2": {
        "script": SERVE_DIR.parent / "ree-v2" / "experiment_runner.py",
        "pid_file": SERVE_DIR.parent / "ree-v2" / "runner.pid",
        "queue_file": SERVE_DIR.parent / "ree-v2" / "experiment_queue.json",
        "evidence_dir": SERVE_DIR.parent / "ree-v2" / "evidence" / "experiments",
        "python": V2_PYTHON,
        "label": "V2 (ree-v2)",
        "auto_sync": True,
        "remote_control": False,
    },
}

DEFAULT_PORT = 8000

# ── Preflight badge ──────────────────────────────────────────────────────────
# Memoised result of `pytest tests/preflight` for the regression-suite badge
# in the explorer. Cached for _PREFLIGHT_TTL seconds so a clicked refresh
# doesn't spawn pytest on every paint.
_PREFLIGHT_TTL = 60
_preflight_cache: dict | None = None
_preflight_cache_at: float = 0.0
_preflight_lock = threading.Lock()


def run_preflight_suite() -> dict:
    """Run ree-v3/tests/preflight and return a serialisable result dict.

    Fields: ok (bool), passed (int), failed (int), duration_s (float),
    cached_at (iso8601 Z), tail (last stdout lines, <=40), error (str|None).
    Memoised for _PREFLIGHT_TTL seconds.
    """
    global _preflight_cache, _preflight_cache_at
    with _preflight_lock:
        now = time.time()
        if _preflight_cache is not None and (now - _preflight_cache_at) < _PREFLIGHT_TTL:
            return _preflight_cache

        ree_v3 = SERVE_DIR.parent / "ree-v3"
        preflight_dir = ree_v3 / "tests" / "preflight"
        if not preflight_dir.exists():
            result = {
                "ok": False,
                "passed": 0,
                "failed": 0,
                "duration_s": 0.0,
                "cached_at": datetime.datetime.utcnow().isoformat() + "Z",
                "tail": [],
                "error": f"preflight directory missing: {preflight_dir}",
            }
            _preflight_cache = result
            _preflight_cache_at = now
            return result

        start = time.time()
        try:
            proc = subprocess.run(
                [V3_PYTHON, "-m", "pytest", "-q", "--tb=line", str(preflight_dir)],
                cwd=str(ree_v3),
                capture_output=True,
                text=True,
                timeout=120,
            )
            duration = time.time() - start
            out = (proc.stdout or "") + (proc.stderr or "")
            # Parse "N passed" / "N failed" from pytest summary.
            passed = 0
            failed = 0
            m_pass = re.search(r"(\d+)\s+passed", out)
            m_fail = re.search(r"(\d+)\s+failed", out)
            if m_pass:
                passed = int(m_pass.group(1))
            if m_fail:
                failed = int(m_fail.group(1))
            tail = out.splitlines()[-40:]
            result = {
                "ok": proc.returncode == 0,
                "passed": passed,
                "failed": failed,
                "duration_s": round(duration, 3),
                "cached_at": datetime.datetime.utcnow().isoformat() + "Z",
                "tail": tail,
                "error": None if proc.returncode == 0 else f"exit {proc.returncode}",
            }
        except subprocess.TimeoutExpired:
            result = {
                "ok": False,
                "passed": 0,
                "failed": 0,
                "duration_s": round(time.time() - start, 3),
                "cached_at": datetime.datetime.utcnow().isoformat() + "Z",
                "tail": [],
                "error": "timeout",
            }
        except Exception as exc:
            result = {
                "ok": False,
                "passed": 0,
                "failed": 0,
                "duration_s": round(time.time() - start, 3),
                "cached_at": datetime.datetime.utcnow().isoformat() + "Z",
                "tail": [],
                "error": f"{type(exc).__name__}: {exc}",
            }
        _preflight_cache = result
        _preflight_cache_at = now
        return result

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


_MANIFEST_INDEX_SKIP_FILES = {
    "claim_evidence.v1.json",
    "review_tracker.json",
    "runner_status.json",
    "substrate_status_snapshot.json",
}
_MANIFEST_INDEX_SKIP_DIRS = {
    "runner_status",
    "schemas",
    "scripts",
    "runner_commands",
    "runner_heartbeats",
    "runner_signals",
    "_runner_signals",
}


def _manifest_dir_name_from_stem(stem: str) -> str:
    """Collapse flat manifest filename to explorer dir_name (strip timestamp + .json)."""
    return re.sub(r"_(?:v\d+_)?\d{8}T\d{6}Z?(?:_v\d+)?$", "", stem)


def _build_dir_to_runs() -> dict:
    """Scan evidence/experiments/ and build {dir_name: {run_id, ...}}.

    Reads manifest.json under each experiment dir, per-dir *.json, and flat
    top-level *.json manifests so reviewed_run_ids map to explorer dir_names.
    """
    exp_root = SERVE_DIR / "evidence" / "experiments"
    result: dict = {}
    if not exp_root.is_dir():
        return result

    def _add_runs(dir_name: str, run_ids: set) -> None:
        if not dir_name or not run_ids:
            return
        result.setdefault(dir_name, set()).update(run_ids)

    # Flat manifests at evidence/experiments/*.json (V3 runner default layout).
    for j in exp_root.glob("*.json"):
        if j.name in _MANIFEST_INDEX_SKIP_FILES:
            continue
        try:
            data = json.loads(j.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        rid = data.get("run_id")
        if rid:
            _add_runs(_manifest_dir_name_from_stem(j.stem), {rid})

    for d in exp_root.iterdir():
        if not d.is_dir():
            continue
        if d.name in _MANIFEST_INDEX_SKIP_DIRS:
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
            _add_runs(d.name, runs)
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


def _utc_age_seconds(iso: str, now) -> int | None:
    """Seconds since an ISO-8601 UTC timestamp, or None if unparsable."""
    from datetime import datetime, timezone
    if not iso:
        return None
    try:
        t = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        return int((now - t).total_seconds())
    except Exception:
        return None


def _fetch_coordinator_machine_snapshots(cfg: dict) -> dict[str, dict]:
    """Live heartbeats from the Phase-1 coordinator (WireGuard).

    Returns {machine: snapshot} or {} when unconfigured/unreachable.
    Never raises -- /api/machines must stay available if the hub is down.
    """
    import urllib.error
    import urllib.request

    url = (cfg.get("COORDINATOR_URL") or "").rstrip("/")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN") or ""
    if not url or not tok:
        return {}
    try:
        req = urllib.request.Request(
            url + "/shadow/status",
            headers={"Authorization": "Bearer " + tok},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            st = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, OSError, json.JSONDecodeError, ValueError):
        return {}
    out: dict[str, dict] = {}
    for m in st.get("machines") or []:
        name = m.get("machine")
        if not name:
            continue
        out[name] = {
            "last_tick_utc": m.get("last_seen") or "",
            "state": m.get("state") or "unknown",
            "current_exq": m.get("current_exq"),
            "progress": m.get("progress") or {},
        }
    return out


def _coordinator_preferred(git_fresh: bool, git_age: int | None,
                          coord_age: int | None,
                          fresh_window: int) -> bool:
    """True when coordinator telemetry should override stale git heartbeats."""
    if coord_age is None or coord_age < 0 or coord_age > fresh_window:
        return False
    if not git_fresh:
        return True
    if git_age is None:
        return True
    return coord_age < git_age


def _overlay_coordinator_heartbeat(entry: dict, snap: dict, now,
                                   fresh_window: int) -> None:
    """Mutate a /api/machines row with fresher coordinator fields."""
    coord_age = _utc_age_seconds(snap.get("last_tick_utc") or "", now)
    coord_fresh = (
        coord_age is not None and 0 <= coord_age <= fresh_window)
    if not _coordinator_preferred(
            entry.get("fresh"), entry.get("age_seconds"),
            coord_age, fresh_window):
        return
    entry["last_tick_utc"] = snap.get("last_tick_utc") or entry["last_tick_utc"]
    entry["age_seconds"] = coord_age
    entry["fresh"] = coord_fresh
    entry["state"] = snap.get("state") or entry["state"]
    entry["current_exq"] = snap.get("current_exq")
    if snap.get("progress"):
        entry["progress"] = snap["progress"]
    entry["telemetry_source"] = "coordinator"


def _entry_from_coordinator_snapshot(name: str, snap: dict, now,
                                     fresh_window: int) -> dict:
    """Build a /api/machines row for a host only visible on the coordinator."""
    coord_age = _utc_age_seconds(snap.get("last_tick_utc") or "", now)
    coord_fresh = (
        coord_age is not None and 0 <= coord_age <= fresh_window)
    return {
        "machine": name,
        "hostname": None,
        "last_tick_utc": snap.get("last_tick_utc") or "",
        "age_seconds": coord_age,
        "fresh": coord_fresh,
        "state": snap.get("state") or "unknown",
        "current_exq": snap.get("current_exq"),
        "current_exq_started_utc": None,
        "current_title": None,
        "current_claim_id": None,
        "current_description": None,
        "progress": snap.get("progress") or {},
        "seconds_elapsed": None,
        "seconds_remaining": None,
        "recent_lines": [],
        "queue_depth": None,
        "queue_id_at_head": None,
        "recent_completed": [],
        "gpu": {},
        "runner_pid": None,
        "runner_version": None,
        "status_idle": None,
        "status_current": None,
        "status_last_updated": None,
        "has_heartbeat": False,
        "has_status": False,
        "telemetry_source": "coordinator",
    }


def read_machines() -> dict:
    """Aggregate per-machine heartbeats + status into a single view.

    Returns:
        {
          "schema_version": "v1",
          "now_utc": "<iso>",
          "machines": [
             {
               machine, hostname, last_tick_utc, age_seconds, fresh,
               state, current_exq, queue_depth, recent_completed,
               gpu, runner_pid, runner_version,
               status_idle, status_current, status_last_updated,
             }, ...
          ],
        }

    `fresh` is True when last_tick_utc is within FRESH_WINDOW_SECONDS (default
    180s -- 3x the default --loop-interval=60s, so a missed tick is OK).
    `state` falls back to "unknown" when no heartbeat exists for a machine
    that does have a status file.
    """
    from datetime import datetime, timezone

    FRESH_WINDOW_SECONDS = 180

    heartbeats: dict[str, dict] = {}
    if HEARTBEAT_DIR.is_dir():
        for f in sorted(HEARTBEAT_DIR.glob("*.json")):
            try:
                hb = json.loads(f.read_text())
                key = hb.get("machine") or f.stem
                heartbeats[key] = hb
            except Exception:
                pass

    statuses: dict[str, dict] = {}
    if STATUS_DIR.is_dir():
        for f in sorted(STATUS_DIR.glob("*.json")):
            try:
                statuses[f.stem] = json.loads(f.read_text())
            except Exception:
                pass

    all_machines = set(heartbeats.keys()) | set(statuses.keys())
    now = datetime.now(timezone.utc)

    out_machines = []
    for name in sorted(all_machines):
        hb = heartbeats.get(name, {})
        st = statuses.get(name, {})

        last_tick = hb.get("last_tick_utc") or st.get("last_updated") or ""
        age_seconds = _utc_age_seconds(last_tick, now)
        fresh = (
            age_seconds is not None
            and 0 <= age_seconds <= FRESH_WINDOW_SECONDS)

        entry = {
            "machine": name,
            "hostname": hb.get("hostname"),
            "last_tick_utc": last_tick,
            "age_seconds": age_seconds,
            "fresh": fresh,
            "state": hb.get("state", "unknown" if not hb else "idle"),
            "current_exq": hb.get("current_exq"),
            "current_exq_started_utc": hb.get("current_exq_started_utc"),
            "current_title": hb.get("current_title"),
            "current_claim_id": hb.get("current_claim_id"),
            "current_description": hb.get("current_description"),
            "progress": hb.get("progress"),
            "seconds_elapsed": hb.get("seconds_elapsed"),
            "seconds_remaining": hb.get("seconds_remaining"),
            "recent_lines": hb.get("recent_lines"),
            "queue_depth": hb.get("queue_depth"),
            "queue_id_at_head": hb.get("queue_id_at_head"),
            "recent_completed": hb.get("recent_completed", []),
            "gpu": hb.get("gpu", {}),
            "runner_pid": hb.get("runner_pid") or st.get("runner_pid"),
            "runner_version": hb.get("runner_version"),
            "status_idle": st.get("idle"),
            "status_current": st.get("current"),
            "status_last_updated": st.get("last_updated"),
            "has_heartbeat": name in heartbeats,
            "has_status": name in statuses,
            "telemetry_source": "git",
        }
        out_machines.append(entry)

    # Phase-1 bridge: coordinator heartbeats are live over WireGuard while
    # git-synced runner_heartbeats/*.json on this Mac may lag (branch drift,
    # pull interval, push races). Prefer coordinator when fresher.
    coord_snaps = _fetch_coordinator_machine_snapshots(_load_coordinator_cfg())
    if coord_snaps:
        by_name = {e["machine"]: e for e in out_machines}
        for entry in out_machines:
            snap = coord_snaps.get(entry["machine"])
            if snap:
                _overlay_coordinator_heartbeat(
                    entry, snap, now, FRESH_WINDOW_SECONDS)
        for name, snap in coord_snaps.items():
            if name not in by_name:
                out_machines.append(_entry_from_coordinator_snapshot(
                    name, snap, now, FRESH_WINDOW_SECONDS))
        out_machines.sort(key=lambda e: e["machine"])

    return {
        "schema_version": "v1",
        "now_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fresh_window_seconds": FRESH_WINDOW_SECONDS,
        "coordinator_overlay": bool(coord_snaps),
        "machines": out_machines,
    }


# ── Closure plan parsing ────────────────────────────────────────────────────

# Plans we know about; entries here without frontmatter still appear as
# placeholder cards in the Closure tab so the user knows they exist but
# haven't been retrofitted yet.
CLOSURE_KNOWN_PLANS = [
    "commitment_closure_plan.md",
    "goal_pipeline_plan.md",
    "self_attribution_plan.md",
    "sd033_governance_plan.md",
    "sleep_substrate_plan.md",
]

CLOSURE_STATUS_WEIGHTS = {
    "done": 1.0,
    "partial": 0.5,
    "in_progress": 0.4,
    "in-progress": 0.4,
    "blocked": 0.1,
    "tracked": 0.2,
    "open": 0.0,
    "deferred": None,   # excluded from progress denominator
    "deferred V4": None,
}

PENDING_REVIEW_FILE = SERVE_DIR / "evidence" / "experiments" / "pending_review.md"
REE_V3_QUEUE_FILE = SERVE_DIR.parent / "ree-v3" / "experiment_queue.json"
SUBSTRATE_QUEUE_FILE = PLANNING_DIR / "substrate_queue.json"
_EXQ_ID_RE = re.compile(r"V3-EXQ-\d+[a-z]?", re.IGNORECASE)


def _parse_plan_frontmatter(path: Path) -> dict | None:
    """Return the closure_plan dict from a plan doc's YAML frontmatter, or None."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    if not _YAML_OK:
        return None
    fm_text = text[4:end]
    try:
        fm = _yaml.safe_load(fm_text)
    except Exception:
        return None
    if not isinstance(fm, dict):
        return None
    plan = fm.get("closure_plan")
    if not isinstance(plan, dict):
        return None
    return plan


def _normalize_status(s: str | None) -> str:
    if not s:
        return "open"
    s = str(s).strip().lower().replace(" ", "_")
    return s.replace("-", "_")


BRAIN_REGION_MAP_FILE = SERVE_DIR / "docs" / "architecture" / "brain_region_map.yaml"
BRAIN_MAP_SVG_FILE = SERVE_DIR / "docs" / "architecture" / "brain_map_sagittal.svg"
REE_V3_CORE_DIR = SERVE_DIR.parent / "ree-v3" / "ree_core"
CONFLICTS_DIR = SERVE_DIR / "docs" / "conflicts"


def _brain_path_exists(rel_path: str) -> bool:
    """True if rel_path exists under ree-v3/ree_core (file or directory)."""
    if not rel_path:
        return False
    p = REE_V3_CORE_DIR / rel_path.replace("\\", "/")
    return p.exists()


def _brain_implementation_tier(
    ree_core_paths: list,
    functional_analogs: list,
) -> str:
    core_hits = sum(1 for p in (ree_core_paths or []) if _brain_path_exists(p))
    analog_hits = sum(1 for p in (functional_analogs or []) if _brain_path_exists(p))
    n_core = len(ree_core_paths or [])
    n_analog = len(functional_analogs or [])
    if n_core > 0 and core_hits == n_core:
        return "full"
    if core_hits > 0 or analog_hits > 0:
        return "partial"
    return "claim_only"


def _brain_prefix_index(map_doc: dict) -> dict[str, str]:
    """Map subject prefix -> region or engineering node id."""
    out: dict[str, str] = {}
    for bucket in ("regions", "engineering_nodes"):
        for node in map_doc.get(bucket) or []:
            nid = str(node.get("id") or "")
            if not nid:
                continue
            for pref in node.get("subject_prefixes") or []:
                out[str(pref)] = nid
    return out


def _brain_load_region_map() -> dict:
    if not _YAML_OK or not BRAIN_REGION_MAP_FILE.exists():
        return {}
    try:
        raw = _yaml.safe_load(BRAIN_REGION_MAP_FILE.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else {}
    except Exception:
        return {}


def _brain_load_claim_evidence() -> dict:
    if not _TL_CLAIM_EVIDENCE.exists():
        return {}
    try:
        data = json.loads(_TL_CLAIM_EVIDENCE.read_text(encoding="utf-8"))
        return data.get("claims") or {}
    except Exception:
        return {}


def _brain_queued_exqs() -> list[dict]:
    qf = RUNNERS["v3"]["queue_file"]
    if not qf.exists():
        return []
    try:
        data = json.loads(qf.read_text(encoding="utf-8"))
    except Exception:
        return []
    out = []
    for item in data.get("items") or []:
        if not isinstance(item, dict):
            continue
        status = str(item.get("status") or "pending").lower()
        if status in ("done", "completed", "removed"):
            continue
        cids = []
        if item.get("claim_id"):
            cids.append(str(item["claim_id"]))
        for c in item.get("claim_ids") or []:
            if c:
                cids.append(str(c))
        out.append({
            "queue_id": str(item.get("queue_id") or ""),
            "title": str(item.get("title") or ""),
            "status": status,
            "claim_ids": cids,
        })
    return out


def _brain_conflict_snippets(region_docs: list[str]) -> list[str]:
    snippets: list[str] = []
    if not CONFLICTS_DIR.exists():
        return snippets
    needles = [d.replace("\\", "/").lower() for d in (region_docs or []) if d]
    if not needles:
        return snippets
    for md in CONFLICTS_DIR.glob("*.md"):
        if md.name.upper() == "README.MD":
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace").lower()
        except Exception:
            continue
        if any(n in text for n in needles):
            snippets.append(md.stem)
    return snippets[:8]


def read_brain_map() -> dict:
    """Aggregate brain-region stats for /api/brain-map."""
    generated_at = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    map_doc = _brain_load_region_map()
    if not map_doc:
        return {
            "schema_version": 1,
            "generated_at": generated_at,
            "error": "brain_region_map.yaml missing or unreadable",
            "regions": [],
            "engineering_nodes": [],
            "pathways": [],
        }

    prefix_to_node = _brain_prefix_index(map_doc)
    claims_list = _tl_load_claims()
    evidence_by_id = _brain_load_claim_evidence()
    queued = _brain_queued_exqs()
    queued_claim_ids = {cid for q in queued for cid in q.get("claim_ids") or []}

    claims_by_prefix: dict[str, list[dict]] = {}
    for c in claims_list:
        cid = str(c.get("id") or "")
        sub = str(c.get("subject") or "")
        pref = sub.split(".")[0] if sub else ""
        if not pref:
            continue
        ev = evidence_by_id.get(cid) or {}
        rec = {
            "id": cid,
            "title": str(c.get("title") or ""),
            "subject": sub,
            "status": str(c.get("status") or ""),
            "v3_pending": bool(c.get("v3_pending")),
            "genuine_exp_count": int(ev.get("genuine_exp_count") or 0),
            "pass_runs": int(ev.get("pass_runs") or 0),
            "fail_runs": int(ev.get("fail_runs") or 0),
            "evidence_quadrant": str(ev.get("evidence_quadrant") or ""),
            "overall_confidence": ev.get("overall_confidence"),
        }
        claims_by_prefix.setdefault(pref, []).append(rec)

    def enrich_node(node: dict, bucket: str) -> dict:
        nid = str(node.get("id") or "")
        prefixes = [str(p) for p in (node.get("subject_prefixes") or [])]
        matched: list[dict] = []
        for pref in prefixes:
            matched.extend(claims_by_prefix.get(pref) or [])
        claim_ids = [m["id"] for m in matched]
        v3_pending = [m["id"] for m in matched if m.get("v3_pending")]
        exp_support = sum(m.get("genuine_exp_count") or 0 for m in matched)
        pass_runs = sum(m.get("pass_runs") or 0 for m in matched)
        fail_runs = sum(m.get("fail_runs") or 0 for m in matched)
        queued_here = [q for q in queued if any(cid in claim_ids for cid in q.get("claim_ids") or [])]
        conflict_hits = _brain_conflict_snippets(node.get("primary_docs") or [])
        implementation = _brain_implementation_tier(
            list(node.get("ree_core_paths") or []),
            list(node.get("functional_analogs") or []),
        )
        leading_edge = bool(
            v3_pending
            or queued_here
            or conflict_hits
        )
        scope = str(node.get("scope") or "in_scope")
        if scope == "out_of_scope":
            coverage_tier = "absent"
        elif leading_edge and exp_support == 0 and scope != "engineering":
            coverage_tier = "frontier"
        elif implementation in ("full", "partial") and pass_runs > 0:
            coverage_tier = "expressed"
        elif matched:
            coverage_tier = "claimed"
        else:
            coverage_tier = "absent" if scope == "out_of_scope" else "claimed"

        quadrants: dict[str, int] = {}
        for m in matched:
            q = m.get("evidence_quadrant") or "unknown"
            quadrants[q] = quadrants.get(q, 0) + 1

        return {
            "id": nid,
            "label": str(node.get("label") or nid),
            "bucket": bucket,
            "scope": scope,
            "subject_prefixes": prefixes,
            "svg_path_ids": list(node.get("svg_path_ids") or []),
            "ree_core_paths": list(node.get("ree_core_paths") or []),
            "functional_analogs": list(node.get("functional_analogs") or []),
            "primary_docs": list(node.get("primary_docs") or []),
            "notes": str(node.get("notes") or ""),
            "claim_count": len(matched),
            "claim_ids": claim_ids,
            "claims_sample": sorted(matched, key=lambda x: x["id"])[:12],
            "implementation": implementation,
            "evidence": {
                "genuine_exp_count": exp_support,
                "pass_runs": pass_runs,
                "fail_runs": fail_runs,
                "quadrant_counts": quadrants,
            },
            "v3_pending_count": len(v3_pending),
            "v3_pending_ids": v3_pending[:20],
            "leading_edge": leading_edge,
            "queued_exqs": queued_here[:10],
            "conflict_refs": conflict_hits,
            "coverage_tier": coverage_tier,
        }

    regions = [enrich_node(n, "region") for n in (map_doc.get("regions") or [])]
    engineering = [enrich_node(n, "engineering") for n in (map_doc.get("engineering_nodes") or [])]

    # Centroids for pathway overlay (rough layout matching SVG viewBox)
    _CENTROIDS = {
        "hippocampus": [210, 305],
        "amygdala": [170, 288],
        "pfc": [190, 130],
        "cingulate": [210, 200],
        "basal_ganglia": [210, 245],
        "default_mode": [210, 215],
        "sleep": [210, 205],
        "thalamus": [220, 250],
        "pag": [220, 415],
        "neuromodulation": [210, 218],
        "astrocyte": [210, 268],
        "harm_stream": [315, 225],
        "respiratory": [220, 388],
        "e1": [366, 58],
        "e2": [366, 106],
        "e3": [366, 154],
        "control_plane": [366, 202],
        "latent_stack": [366, 250],
        "policy_engineering": [366, 298],
        "architecture_meta": [366, 346],
    }
    all_nodes = {n["id"]: n for n in regions + engineering}

    pathways_out = []
    for pw in map_doc.get("pathways") or []:
        pid = str(pw.get("id") or "")
        edges = []
        for edge in pw.get("edges") or []:
            if not isinstance(edge, (list, tuple)) or len(edge) < 2:
                continue
            a, b = str(edge[0]), str(edge[1])
            ca = _CENTROIDS.get(a)
            cb = _CENTROIDS.get(b)
            edges.append({
                "from": a,
                "to": b,
                "from_xy": ca,
                "to_xy": cb,
            })
        pathways_out.append({
            "id": pid,
            "label": str(pw.get("label") or pid),
            "edges": edges,
            "claim_subjects": list(pw.get("claim_subjects") or []),
        })

    unmapped_prefixes = []
    known = set(map_doc.get("known_anatomy_prefixes") or [])
    for pref in sorted(claims_by_prefix.keys()):
        if pref in known and pref not in prefix_to_node:
            unmapped_prefixes.append(pref)

    return {
        "schema_version": map_doc.get("schema_version", 1),
        "generated_at": generated_at,
        "disclaimer": str(map_doc.get("disclaimer") or ""),
        "svg_url": "/docs/architecture/brain_map_sagittal.svg",
        "regions": regions,
        "engineering_nodes": engineering,
        "pathways": pathways_out,
        "unmapped_prefixes": unmapped_prefixes,
        "prefix_to_node": prefix_to_node,
    }


def _closure_pending_review_count() -> int:
    try:
        text = PENDING_REVIEW_FILE.read_text(encoding="utf-8")
    except Exception:
        return 0
    m = re.search(r"Pending:\s*\*\*(\d+)\*\*", text)
    return int(m.group(1)) if m else 0


def _closure_roadmap_snippet(max_len: int = 900) -> str:
    path = SERVE_DIR / "docs" / "roadmap.md"
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return ""
    m = re.search(
        r"(### Immediate Work Queue.*?\n(?:\d+\.\s+.*\n)+)",
        text,
        re.DOTALL,
    )
    snippet = (m.group(1) if m else text[:max_len]).strip()
    if len(snippet) > max_len:
        snippet = snippet[: max_len - 3] + "..."
    return snippet


def _closure_queue_claimed() -> list[dict]:
    try:
        data = json.loads(REE_V3_QUEUE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[dict] = []
    for item in data.get("items") or []:
        if not isinstance(item, dict):
            continue
        cb = item.get("claimed_by")
        if not isinstance(cb, dict) or not cb.get("machine"):
            continue
        out.append({
            "queue_id": item.get("queue_id"),
            "machine": cb.get("machine"),
            "claimed_at": cb.get("claimed_at"),
            "title": item.get("title") or "",
            "priority": item.get("priority"),
        })
    return out


def _closure_claim_ids_by_flag(flag_substr: str) -> set[str]:
    """Scan claims.yaml list items for a boolean flag or note substring."""
    try:
        text = _TL_CLAIMS_YAML.read_text(encoding="utf-8")
    except Exception:
        return set()
    out: set[str] = set()
    current_id: str | None = None
    for line in text.splitlines():
        m = re.match(r"^- id:\s*(\S+)", line)
        if m:
            current_id = m.group(1)
            continue
        if current_id and flag_substr in line:
            if re.search(
                rf"{re.escape(flag_substr)}:\s*true",
                line,
            ) or flag_substr in line:
                out.add(current_id)
    return out


def _closure_is_ready_gap(node: dict, nodes_by_id: dict[str, dict]) -> bool:
    if node.get("status") != "open":
        return False
    if node.get("severity") not in ("load-bearing", "high", "medium"):
        return False
    for dep in node.get("depends_on") or []:
        dep_n = nodes_by_id.get(str(dep))
        if not dep_n or dep_n.get("status") not in (
            "done", "deferred", "deferred_v4",
        ):
            return False
    return True


def _closure_active_blocker_short(
    node: dict,
    nodes_by_id: dict[str, dict],
) -> str:
    for dep in node.get("depends_on") or []:
        dep_n = nodes_by_id.get(str(dep))
        if dep_n and dep_n.get("status") not in (
            "done", "deferred", "deferred_v4",
        ):
            return f"{dep} [{dep_n.get('status')}]"
    ext = node.get("blocking_external") or []
    if ext:
        return str(ext[0])[:96]
    if node.get("status") == "blocked" and node.get("owner_exq"):
        return f"awaiting {node.get('owner_exq')}"
    return ""


def _closure_dual_progress(nodes: list[dict]) -> dict:
    impl_done = impl_total = 0.0
    ev_done = ev_total = 0.0
    for n in nodes:
        sev = n.get("severity") or ""
        if sev in ("load-bearing", "high"):
            w = CLOSURE_STATUS_WEIGHTS.get(n.get("status") or "open", 0.0)
            if w is not None:
                impl_total += 1.0
                impl_done += w
        owner = n.get("owner_exq")
        if owner and str(owner).strip().lower() not in ("null", "tbd", ""):
            ev_total += 1.0
            w = CLOSURE_STATUS_WEIGHTS.get(n.get("status") or "open", 0.0)
            if w is not None:
                ev_done += w
    def _pct(done: float, total: float) -> float:
        return round(done / total, 4) if total > 0 else 0.0
    return {
        "implementation": {
            "done_weighted": round(impl_done, 4),
            "node_total": int(impl_total),
            "progress": _pct(impl_done, impl_total),
        },
        "evidence": {
            "done_weighted": round(ev_done, 4),
            "node_total": int(ev_total),
            "progress": _pct(ev_done, ev_total),
        },
    }


def _enrich_closure_v2(data: dict) -> dict:
    """Add closure/v2 orientation, live EXQ, cusp rail, per-node flags."""
    nodes = data.get("nodes") or []
    nodes_by_id = {n["id"]: n for n in nodes if n.get("id")}
    live_exq_ids: set[str] = set()

    machines_view = read_machines()
    running_rows: list[dict] = []
    for m in machines_view.get("machines") or []:
        exq = m.get("current_exq")
        if exq and m.get("fresh"):
            live_exq_ids.add(str(exq))
            running_rows.append({
                "queue_id": exq,
                "machine": m.get("machine"),
                "progress": m.get("progress") or {},
                "state": m.get("state"),
            })

    queue_claimed = _closure_queue_claimed()
    for row in queue_claimed:
        qid = row.get("queue_id")
        if qid:
            live_exq_ids.add(str(qid))

    retest_ids = _closure_claim_ids_by_flag("pending_retest_after_substrate")
    ceil_ids = _closure_claim_ids_by_flag("epistemic_category: substrate_ceiling")

    cusp_items: list[dict] = []
    for n in nodes:
        if _closure_is_ready_gap(n, nodes_by_id):
            cusp_items.append({
                "kind": "ready_gap",
                "label": n["id"],
                "gap_id": n["id"],
                "plan_id": n.get("plan_id"),
            })
    try:
        sq = json.loads(SUBSTRATE_QUEUE_FILE.read_text(encoding="utf-8"))
        for item in sq.get("queue") or []:
            if not isinstance(item, dict) or not item.get("ready"):
                continue
            impl = (item.get("implementation_status") or "").lower()
            if impl in ("implemented", "done", "complete"):
                continue
            cusp_items.append({
                "kind": "substrate_ready",
                "label": item.get("sd_id") or item.get("title") or "?",
                "sd_id": item.get("sd_id"),
            })
    except Exception:
        pass
    for cid in sorted(retest_ids)[:12]:
        cusp_items.append({
            "kind": "pending_retest",
            "label": cid,
            "claim_id": cid,
        })

    contributory: set[str] = set()
    for n in nodes:
        for m in _EXQ_ID_RE.finditer(str(n.get("owner_exq") or "")):
            contributory.add(m.group(0).upper().replace("v3-exq", "V3-EXQ"))

    for n in nodes:
        badges: list[str] = []
        flags: list[str] = []
        owner = str(n.get("owner_exq") or "")
        exq_m = _EXQ_ID_RE.search(owner)
        if exq_m:
            badges.append("EXQ")
            qid = exq_m.group(0).upper().replace("v3-exq", "V3-EXQ")
            n["exq_live"] = qid in live_exq_ids
        for cid in n.get("unblocks_claims") or []:
            if cid in retest_ids:
                flags.append("pending_retest")
                if "RETEST" not in badges:
                    badges.append("RETEST")
            if cid in ceil_ids:
                if "CEIL" not in badges:
                    badges.append("CEIL")
        n["claim_flags"] = flags
        n["badges"] = badges
        n["active_blocker_short"] = _closure_active_blocker_short(
            n, nodes_by_id)

    for p in data.get("plans") or []:
        plan_nodes = [n for n in nodes if n.get("plan_id") == p.get("id")]
        p["blocked_load_bearing"] = sum(
            1 for n in plan_nodes
            if n.get("status") == "blocked"
            and n.get("severity") == "load-bearing"
        )
        run_exqs: set[str] = set()
        for n in plan_nodes:
            for m in _EXQ_ID_RE.finditer(str(n.get("owner_exq") or "")):
                qid = m.group(0).upper().replace("v3-exq", "V3-EXQ")
                if qid in live_exq_ids:
                    run_exqs.add(qid)
        p["running_exqs"] = sorted(run_exqs)

    n_fresh = sum(
        1 for m in machines_view.get("machines") or [] if m.get("fresh"))
    runner_bits: list[str] = []
    if running_rows:
        runner_bits.append(
            ", ".join(
                f"{r['machine']}:{r['queue_id']}"
                for r in running_rows[:5]
            )
        )
    runner_summary = (
        f"{len(running_rows)} running / {n_fresh} fresh machines"
        + (": " + "; ".join(runner_bits) if runner_bits else "")
    )

    data["schema_version"] = "closure/v2"
    data["orientation"] = {
        "roadmap_snippet": _closure_roadmap_snippet(),
        "pending_review_count": _closure_pending_review_count(),
        "runner_summary": runner_summary,
        "any_runner_active": bool(running_rows),
    }
    data["progress"] = _closure_dual_progress(nodes)
    data["exq_live"] = {
        "running": running_rows,
        "queue_claimed": queue_claimed,
    }
    data["cusp_items"] = cusp_items[:30]
    data["contributory_exq_ids"] = sorted(contributory)
    return data



def read_closure() -> dict:
    """Aggregate closure_plan frontmatter across planning/*_plan.md docs."""
    plans: list[dict] = []
    nodes_by_id: dict[str, dict] = {}
    edges: list[dict] = []
    cross_links: list[dict] = []

    seen_files: set[str] = set()

    # Load known plans first (preserves order in UI), then any other *_plan.md.
    candidates = list(CLOSURE_KNOWN_PLANS)
    if PLANNING_DIR.exists():
        for p in sorted(PLANNING_DIR.glob("*_plan.md")):
            if p.name not in candidates:
                candidates.append(p.name)

    for fname in candidates:
        path = PLANNING_DIR / fname
        if not path.exists():
            continue
        seen_files.add(fname)
        plan = _parse_plan_frontmatter(path)
        if plan is None:
            plans.append({
                "id": fname.replace("_plan.md", ""),
                "title": fname.replace("_plan.md", "").replace("_", " ").title(),
                "file": fname,
                "frontmatter_pending": True,
                "node_count": 0,
                "progress": 0.0,
            })
            continue

        plan_id = str(plan.get("id") or fname.replace("_plan.md", ""))
        plan_nodes = plan.get("nodes") or []
        weighted_done = 0.0
        weighted_total = 0.0
        status_counts: dict[str, int] = {}

        for n in plan_nodes:
            if not isinstance(n, dict):
                continue
            nid = str(n.get("id") or "")
            if not nid:
                continue
            status = _normalize_status(n.get("status"))
            status_counts[status] = status_counts.get(status, 0) + 1
            weight = CLOSURE_STATUS_WEIGHTS.get(status, 0.0)
            if weight is not None:
                weighted_total += 1.0
                weighted_done += weight

            node_record = {
                "id": nid,
                "plan_id": plan_id,
                "title": n.get("title") or nid,
                "phase": n.get("phase"),
                "status": status,
                "severity": n.get("severity") or "medium",
                "owner_exq": n.get("owner_exq"),
                "unblocks_claims": list(n.get("unblocks_claims") or []),
                "depends_on": list(n.get("depends_on") or []),
                "cross_plan_link": list(n.get("cross_plan_link") or []),
                "blocking_external": list(n.get("blocking_external") or []),
                "last_updated": n.get("last_updated"),
                # resume_condition / blocking_on: free-text + structured fields
                # for distinguishing a node's CURRENT active blocker from its
                # static depends_on lineage. depends_on records phase order
                # (e.g. Phase 2 follows Phase 1) and does not flip back to
                # incomplete once a downstream node hits a new blocker.
                "resume_condition": n.get("resume_condition"),
                "blocking_on": n.get("blocking_on"),
            }
            # If a node id appears in multiple plans, keep first and record alias.
            if nid in nodes_by_id:
                nodes_by_id[nid].setdefault("aliases", []).append(plan_id)
            else:
                nodes_by_id[nid] = node_record

            for dep in node_record["depends_on"]:
                edges.append({"from": str(dep), "to": nid, "kind": "depends_on"})
            for link in node_record["cross_plan_link"]:
                cross_links.append({"from": nid, "to": str(link), "kind": "cross_plan_link"})

        progress = (weighted_done / weighted_total) if weighted_total > 0 else 0.0

        plans.append({
            "id": plan_id,
            "title": plan.get("title") or plan_id,
            "file": fname,
            "registered": str(plan.get("registered") or ""),
            "scope_claims": list(plan.get("scope_claims") or []),
            "parent_plan": plan.get("parent_plan"),
            "sibling_plans": list(plan.get("sibling_plans") or []),
            "node_count": len(plan_nodes),
            "status_counts": status_counts,
            "progress": round(progress, 4),
            "frontmatter_pending": False,
        })

    # Overall progress: weighted across all non-deferred nodes, all plans.
    overall_done = 0.0
    overall_total = 0.0
    for n in nodes_by_id.values():
        w = CLOSURE_STATUS_WEIGHTS.get(n["status"], 0.0)
        if w is not None:
            overall_total += 1.0
            overall_done += w
    overall_progress = (overall_done / overall_total) if overall_total > 0 else 0.0

    return _enrich_closure_v2({
        "schema_version": "closure/v1",
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "plans": plans,
        "nodes": list(nodes_by_id.values()),
        "edges": edges,
        "cross_links": cross_links,
        "overall_progress": round(overall_progress, 4),
        "node_total": int(overall_total),
        "node_done_weighted": round(overall_done, 4),
    })


def read_workset() -> dict:
    """Load inter-governance workset from generate_inter_governance_workset.py."""
    empty = {
        "schema_version": "inter_governance_workset/v1.1",
        "generated_at": None,
        "generator": "scripts/generate_inter_governance_workset.py",
        "summary": {
            "total": 0,
            "ready": 0,
            "in_flight": 0,
            "blocked": 0,
            "pending_review_count": 0,
            "queue_pending": 0,
            "live_exqs": [],
        },
        "lenses": {},
        "indexes": {"by_plan": {}},
        "plans": {},
        "items": [],
        "references": {
            "closure_v3": "/closure",
            "workset_page": "/workset",
            "machines": "/machines",
            "explorer": "/explorer.html",
        },
        "empty_note": (
            "No workset yet. Run /inter-governance-brief or "
            "python scripts/generate_inter_governance_workset.py"
        ),
    }
    if not WORKSET_JSON_FILE.exists():
        return empty
    try:
        data = json.loads(WORKSET_JSON_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("items"), list):
            return data
    except Exception:
        pass
    empty["empty_note"] = "Workset file unreadable."
    return empty


def _machine_safe_filename(machine: str) -> str:
    keep = "-_."
    return "".join(c if (c.isalnum() or c in keep) else "_" for c in machine)


def _commands_file(machine: str) -> Path:
    return COMMANDS_DIR / f"{_machine_safe_filename(machine)}.json"


def read_machine_commands(machine: str) -> dict:
    path = _commands_file(machine)
    if not path.exists():
        return {"schema_version": "v1", "machine": machine, "commands": []}
    try:
        data = json.loads(path.read_text())
        if not isinstance(data, dict) or "commands" not in data:
            return {"schema_version": "v1", "machine": machine, "commands": []}
        if not isinstance(data["commands"], list):
            data["commands"] = []
        return data
    except Exception:
        return {"schema_version": "v1", "machine": machine, "commands": []}


def append_machine_command(
    machine: str,
    kind: str,
    args: dict | None,
    issued_by: str,
) -> tuple[bool, str, dict | None]:
    """Append a pending command to runner_commands/<machine>.json.

    Returns (ok, message, command_dict).
    Mirrors ree-v3/runner_remote_control.append_command schema.
    """
    if kind not in VALID_REMOTE_COMMAND_KINDS:
        return False, f"unknown command kind: {kind!r}", None
    if kind in ("kick", "release_claim"):
        if not (args and args.get("queue_id")):
            return False, f"{kind} requires args.queue_id", None
    try:
        COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        return False, f"mkdir failed: {exc}", None

    data = read_machine_commands(machine)
    now = _utc_now_iso()
    cmd = {
        "id": f"cmd-{now}-{os.urandom(3).hex()}",
        "kind": kind,
        "args": args or {},
        "issued_at_utc": now,
        "issued_by": issued_by or "unknown",
        "status": "pending",
        "ack_at_utc": None,
        "completed_at_utc": None,
        "error": None,
        "result_note": None,
    }
    cmds = data.setdefault("commands", [])
    cmds.append(cmd)

    pending = [c for c in cmds if c.get("status") in ("pending", "ack")]
    history = [c for c in cmds if c.get("status") in ("done", "failed")]
    if len(history) > MAX_REMOTE_COMMAND_HISTORY:
        history = history[-MAX_REMOTE_COMMAND_HISTORY:]
    data["commands"] = pending + history
    data["machine"] = machine
    data["schema_version"] = "v1"

    path = _commands_file(machine)
    try:
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, indent=2) + "\n")
        os.replace(tmp, path)
    except Exception as exc:
        return False, f"write failed: {exc}", None

    return True, f"command {cmd['id']} queued for {machine}", cmd


def _utc_now_iso() -> str:
    from datetime import datetime
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


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


def start_runner(ver: str = "v3", extra_env: dict | None = None) -> dict:
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
    if cfg.get("remote_control"):
        cmd.append("--remote-control")  # heartbeat + command channel for /machines dashboard
    # STUB: future config could set per-runner flags from a machines.json config file
    popen_kwargs = {"stdout": log_fh, "stderr": log_fh,
                    "cwd": str(cfg["script"].parent)}
    if extra_env:
        # Only diverge from inherited environment when explicitly asked
        # (shadow start). Default callers pass nothing -> behaviour is
        # byte-identical to before.
        _env = os.environ.copy()
        _env.update({k: str(v) for k, v in extra_env.items()})
        popen_kwargs["env"] = _env
    proc = subprocess.Popen(cmd, **popen_kwargs)
    _runner_procs[ver] = proc
    print(f"[serve] {cfg['label']} runner started (PID {proc.pid})", flush=True)
    return {"status": "started", "pid": proc.pid, "substrate": ver}


# -- Shadow Coordination -----------------------------------------------------
# Backs the explorer "Shadow Coordination" panel. All shadow-only: this never
# triggers a Phase-2 cutover. The local runner start reuses the proven
# start_runner() path (only adding env); remote actions are bounded,
# best-effort SSH that can never hang or crash the request.

_COORDINATOR_ENV_FILE = SERVE_DIR / "coordinator.env"
_SHADOW_CLOUD_HOSTS = ["ree-cloud-1", "ree-cloud-2", "ree-cloud-3",
                       "ree-cloud-4"]
_SHADOW_MANUAL_HOSTS = ["Daniel-PC", "EWIN-PC"]


def _load_coordinator_cfg() -> dict:
    """KEY=VALUE from coordinator.env (gitignored), overlaid by any matching
    process env var. Keys: COORDINATOR_URL, COORDINATOR_LOCAL_TOKEN,
    COORDINATOR_SSH_USER (default 'ree')."""
    cfg = {"COORDINATOR_SSH_USER": "ree"}
    try:
        if _COORDINATOR_ENV_FILE.exists():
            for line in _COORDINATOR_ENV_FILE.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                cfg[k.strip()] = v.strip()
    except OSError:
        pass
    for k in ("COORDINATOR_URL", "COORDINATOR_LOCAL_TOKEN",
              "COORDINATOR_SSH_USER"):
        if os.environ.get(k):
            cfg[k] = os.environ[k]
    return cfg


def _shadow_operator_guide(verdict: str, st: dict | None = None) -> dict:
    """Plain-language phase + next actions for the explorer panel."""
    st = st or {}
    mode = st.get("mode") or "?"
    div = st.get("adjusted_divergences",
                 st.get("divergences_blocking", st.get("divergences", 0)))
    raw_div = st.get("divergences", 0)
    if verdict == "NOT_CONFIGURED":
        return {
            "phase": 0,
            "phase_label": "Phase 0 -- setup",
            "parallel": "Coordinator not wired on this Mac yet.",
            "assess": "n/a",
            "retire": "Do not change git claiming or heartbeats.",
            "next": [
                "Copy REE_assembly/coordinator.env.example to coordinator.env.",
                "Set COORDINATOR_URL and COORDINATOR_LOCAL_TOKEN; use public "
                "SSH IPs for cloud-2/3/4 (see coordinator/OPERATOR_GUIDE.md).",
                "Restart serve.py, then open this panel again.",
            ],
        }
    if verdict == "UNREACHABLE":
        return {
            "phase": 0,
            "phase_label": "Phase 0 -- hub unreachable",
            "parallel": "Cannot reach coordinator (WireGuard or ree-coordinator).",
            "assess": "n/a",
            "retire": "Do not change git claiming or heartbeats.",
            "next": [
                "On Mac: curl -s http://10.8.0.1:8787/health (expect ok:true).",
                "On ree-cloud-1: systemctl status ree-coordinator wg-quick@wg0.",
                "Fix network before starting a soak.",
            ],
        }
    if verdict == "DIVERGENCE":
        return {
            "phase": 1,
            "phase_label": "Phase 1 -- shadow soak (BLOCKED)",
            "parallel": "Git claiming ON + coordinator watching (both active).",
            "assess": ("FAIL -- unexplained divergence (blocking=%d, "
                       "raw audit=%d)." % (div, raw_div)),
            "retire": "Do NOT shut down git. Do NOT advance to Phase 2.",
            "next": [
                "Read recent_divergences in this panel or check_shadow.py output.",
                "Classify each row (see ree-v3/coordinator/SOAK_LOG.md).",
                "Fix harness/setup; wait for HEALTHY + div 0 before cutover.",
            ],
        }
    if verdict == "NO_SIGNAL":
        return {
            "phase": 1,
            "phase_label": "Phase 1 -- shadow soak (no traffic)",
            "parallel": "Git claiming ON; coordinator sees no fresh shadow traffic.",
            "assess": "Not running -- soak is not exercising anything.",
            "retire": "Do not shut down git.",
            "next": [
                "Confirm each cloud has shadow.conf and ree-runner is active.",
                "Click Start shadow soak (or restart runners) after clearing "
                "stale stop commands on clouds.",
                "Need FRESH heartbeats from Mac + all clouds in shadow mode.",
            ],
        }
    # HEALTHY
    if mode == "coordinator":
        return {
            "phase": 2,
            "phase_label": "Phase 2 -- claim cutover (live)",
            "parallel": "Coordinator owns claims; git still carries results, "
                        "status, and queue commits.",
            "assess": "Phase-2 active -- claims via POST /claim (div 0).",
            "retire": "Git claim pushes are retired for mutex. Heartbeats and "
                      "result git pushes remain until Phase 3.",
            "next": [
                "Watch /api/machines and coordinator logs for claim errors.",
                "Do not flip any host back to git/shadow without draining.",
                "Phase 3 (sync_daemon sole git writer) is a separate step.",
            ],
        }
    return {
        "phase": 1,
        "phase_label": "Phase 1 -- shadow soak (assessing)",
        "parallel": "TWO systems: git owns claims/results NOW; coordinator "
                    "compares (mode=%s)." % mode,
        "assess": "PASS so far -- claims seen, 0 unexplained divergence.",
        "retire": "Do NOT shut down git claiming or heartbeat pushes yet. "
                  "Retire git-MUTEX after multi-day HEALTHY, then Phase 2 "
                  "drain + cutover (see OPERATOR_GUIDE.md).",
        "next": [
            "Keep runners in COORDINATION_MODE=shadow on all experiment hosts.",
            "Run check_shadow.py daily; need days of HEALTHY at div 0.",
            "When ready for Phase 2: drain fleet, flip to coordinator mode "
            "everywhere at once (no mixed fleet).",
        ],
    }


def _shadow_verdict(st: dict, stale_mins: float = 10.0) -> tuple:
    """Same logic as ree-v3/coordinator/check_shadow.py (kept in sync by
    hand -- the two live in different repos so duplication is deliberate)."""
    from datetime import datetime, timezone
    ndiv = st.get("adjusted_divergences",
                  st.get("divergences_blocking", st.get("divergences", 0)))
    total = st.get("total_claims", 0)
    fresh = 0
    for m in st.get("machines", []):
        ls = m.get("last_seen")
        if not ls:
            continue
        try:
            dt = datetime.fromisoformat(ls.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        age = (datetime.now(timezone.utc) - dt).total_seconds()
        if age <= stale_mins * 60.0:
            fresh += 1
    if ndiv > 0:
        return ("DIVERGENCE", "red")
    if total == 0 or fresh == 0:
        return ("NO_SIGNAL", "amber")
    return ("HEALTHY", "green")


def read_shadow_status() -> dict:
    """Proxy the coordinator's /shadow/status and fold in the verdict.
    Never raises; degrades to a NOT_CONFIGURED / UNREACHABLE verdict."""
    cfg = _load_coordinator_cfg()
    url = cfg.get("COORDINATOR_URL")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN")
    if not url or not tok:
        return {"verdict": "NOT_CONFIGURED", "color": "grey",
                "detail": "coordinator.env missing COORDINATOR_URL / "
                          "COORDINATOR_LOCAL_TOKEN"}
    import urllib.request
    import urllib.error
    try:
        req = urllib.request.Request(
            url.rstrip("/") + "/shadow/status",
            headers={"Authorization": "Bearer " + tok}, method="GET")
        with urllib.request.urlopen(req, timeout=8) as r:
            st = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return {"verdict": "UNREACHABLE", "color": "red",
                "detail": f"HTTP {exc.code} from coordinator"}
    except Exception as exc:  # noqa: BLE001 -- must not crash the request
        return {"verdict": "UNREACHABLE", "color": "red",
                "detail": repr(exc)}
    verdict, color = _shadow_verdict(st)
    guide = _shadow_operator_guide(verdict, st)
    return {"verdict": verdict, "color": color,
            "mode": st.get("mode"),
            "total_claims": st.get("total_claims", 0),
            "divergences": st.get("divergences", 0),
            "adjusted_divergences": st.get(
                "adjusted_divergences",
                st.get("divergences_blocking", st.get("divergences", 0))),
            "divergences_explained": st.get("divergences_explained", 0),
            "experiments_in_mirror": st.get("experiments_in_mirror", 0),
            "machines": st.get("machines", []),
            "recent_divergences": st.get("recent_divergences", []),
            "guide": guide}


def _ssh(host: str, user: str, remote_cmd: str,
         timeout: int = 20) -> dict:
    """Bounded, password-less SSH. BatchMode + ConnectTimeout guarantee it
    fails fast instead of hanging the HTTP request. Never raises."""
    try:
        cp = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5",
             "-o", "StrictHostKeyChecking=accept-new",
             f"{user}@{host}", remote_cmd],
            capture_output=True, text=True, timeout=timeout)
        ok = cp.returncode == 0
        detail = (cp.stdout or cp.stderr or "").strip()[-300:]
        return {"ok": ok, "detail": detail or ("rc=%d" % cp.returncode)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "detail": "ssh timed out (host unreachable?)"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "detail": repr(exc)}


def start_shadow() -> dict:
    """Start the shadow soak: local Mac runner in shadow mode + bounded
    best-effort SSH to bring the coordinator (ree-cloud-1) and cloud
    runners up in shadow. Daniel-PC / EWIN-PC are reported as manual."""
    cfg = _load_coordinator_cfg()
    url = cfg.get("COORDINATOR_URL")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN")
    if not url or not tok:
        return {"status": "error",
                "message": "coordinator.env not configured "
                           "(COORDINATOR_URL / COORDINATOR_LOCAL_TOKEN). "
                           "See coordinator.env.example."}
    ssh_user = cfg.get("COORDINATOR_SSH_USER", "ree")

    local = start_runner("v3", extra_env={
        "COORDINATION_MODE": "shadow",
        "COORDINATOR_URL": url,
        "COORDINATOR_TOKEN": tok,
        "COORDINATOR_LOG": str(SERVE_DIR / "coordinator_shadow.log"),
    })

    hosts = {}
    for h in _SHADOW_CLOUD_HOSTS:
        if h == "ree-cloud-1":
            rc = ("sudo systemctl start ree-coordinator ree-sync-daemon "
                  "&& sudo systemctl restart ree-runner")
        else:
            rc = "sudo systemctl restart ree-runner"
        # Bare names like 'ree-cloud-1' do not resolve on the Mac. Let
        # coordinator.env map each to a reachable target (WireGuard tunnel
        # IP, ssh-config alias, ...). Default = the name (unchanged).
        target = cfg.get("SHADOW_SSH_HOST_" + h, h)
        hosts[h] = _ssh(target, ssh_user, rc)

    manual = {h: {"status": "manual",
                  "note": "start manually with COORDINATION_MODE=shadow"}
              for h in _SHADOW_MANUAL_HOSTS}

    return {"status": "ok", "coordinator_url": url,
            "local_mac_runner": local, "cloud_hosts": hosts,
            "manual_hosts": manual}


def start_coordinator() -> dict:
    """Phase-2 claim cutover: hub coordinator+sync modes, workers in
    coordinator mode, Mac runner via start_runner(extra_env). Caller must
    have drained the fleet first (no mixed git/shadow/coordinator claims)."""
    cfg = _load_coordinator_cfg()
    url = cfg.get("COORDINATOR_URL")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN")
    if not url or not tok:
        return {"status": "error",
                "message": "coordinator.env not configured "
                           "(COORDINATOR_URL / COORDINATOR_LOCAL_TOKEN). "
                           "See coordinator.env.example."}
    ssh_user = cfg.get("COORDINATOR_SSH_USER", "ree")

    hub_flip = (
        "sudo sed -i 's/^COORDINATOR_MODE=.*/COORDINATOR_MODE=coordinator/' "
        "/etc/ree-coordinator.env && "
        "sudo sed -i 's/^SYNC_MODE=.*/SYNC_MODE=coordinator/' "
        "/etc/ree-coordinator.env && "
        "sudo systemctl restart ree-coordinator ree-sync-daemon && "
        "sleep 2 && curl -sf http://10.8.0.1:8787/health"
    )
    worker_flip = (
        "sudo sed -i 's/COORDINATION_MODE=shadow/COORDINATION_MODE=coordinator/' "
        "/etc/systemd/system/ree-runner.service.d/shadow.conf && "
        "sudo systemctl daemon-reload && sudo systemctl restart ree-runner"
    )

    local = start_runner("v3", extra_env={
        "COORDINATION_MODE": "coordinator",
        "COORDINATOR_URL": url,
        "COORDINATOR_TOKEN": tok,
        "COORDINATOR_LOG": str(SERVE_DIR / "coordinator_shadow.log"),
    })

    hosts = {}
    for h in _SHADOW_CLOUD_HOSTS:
        target = cfg.get("SHADOW_SSH_HOST_" + h, h)
        if h == "ree-cloud-1":
            hosts[h] = _ssh(target, ssh_user, hub_flip + " && " + worker_flip)
        else:
            hosts[h] = _ssh(target, ssh_user, worker_flip)

    manual = {h: {"status": "manual",
                  "note": "flip shadow.conf to COORDINATION_MODE=coordinator "
                           "and restart runner"}
              for h in _SHADOW_MANUAL_HOSTS}

    health = None
    try:
        with urllib.request.urlopen(url.rstrip("/") + "/health", timeout=8) as resp:
            health = json.loads(resp.read().decode())
    except Exception:
        pass

    return {"status": "ok", "phase": 2, "coordinator_url": url,
            "hub_health": health, "local_mac_runner": local,
            "cloud_hosts": hosts, "manual_hosts": manual}


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
        if path == "/api/shadow/status":
            body = json.dumps(read_shadow_status()).encode()
            self._json_response(body)
            return
        if path == "/api/regression/preflight":
            body = json.dumps(run_preflight_suite()).encode()
            self._json_response(body)
            return
        if path == "/api/machines":
            body = json.dumps(read_machines(), indent=2).encode()
            self._json_response(body)
            return
        # /api/machines/<host>/commands -- list pending + recent for one machine
        m = re.match(r"^/api/machines/([^/]+)/commands$", path or "")
        if m:
            from urllib.parse import unquote
            host = unquote(m.group(1))
            body = json.dumps(read_machine_commands(host), indent=2).encode()
            self._json_response(body)
            return
        if path in ("/machines", "/machines.html"):
            machines_page = SERVE_DIR / "machines.html"
            if machines_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(machines_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path == "/api/brain-map":
            body = json.dumps(read_brain_map(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path in ("/brain-map", "/brain-map.html"):
            brain_page = SERVE_DIR / "brain_map.html"
            if brain_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(brain_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path == "/api/workset":
            body = json.dumps(read_workset(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path == "/api/closure":
            body = json.dumps(read_closure(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path in ("/workset", "/workset.html"):
            workset_page = SERVE_DIR / "workset.html"
            if workset_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(workset_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path in ("/closure", "/closure.html"):
            closure_page = SERVE_DIR / "closure.html"
            if closure_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(closure_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
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
        elif path == "/api/shadow/start":
            result = start_shadow()
        elif path == "/api/coordinator/start":
            result = start_coordinator()
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
        elif (m := re.match(r"^/api/machines/([^/]+)/command$", path or "")):
            from urllib.parse import unquote
            host = unquote(m.group(1))
            length = int(self.headers.get("Content-Length", 0))
            try:
                payload = json.loads(self.rfile.read(length) or b"{}")
            except Exception as exc:
                result = {"status": "error", "message": f"bad json: {exc}"}
                body = json.dumps(result).encode()
                self._json_response(body, status=400)
                return
            kind = (payload.get("kind") or "").strip()
            args = payload.get("args") or {}
            issued_by = payload.get("issued_by") or "explorer"
            ok, msg, cmd = append_machine_command(host, kind, args, issued_by)
            result = {
                "status": "ok" if ok else "error",
                "message": msg,
                "command": cmd,
                "machine": host,
                "valid_kinds": list(VALID_REMOTE_COMMAND_KINDS),
            }
            body = json.dumps(result).encode()
            self._json_response(body, status=200 if ok else 400)
            return
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
