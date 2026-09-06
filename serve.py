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
    /api/experiment/detail     -- GET ?script=&queue_id=: curated manifest detail for a Completed card
    /api/regression/preflight  -- GET: ree-v3 preflight suite result (cached 60s)
    /api/coordinator/phase3/preflight  -- GET: Phase 3 cutover pre-checks (cached 60s)
    /api/coordinator/phase3/writers    -- GET: Phase 3 sync_daemon writer health (cached 60s)
    /api/workspace/health       -- GET: stale TASK_CLAIMS + orphaned git stashes (cached 60s)
    /api/queue/live                -- GET: active queue (coordinator DB when reachable, else file)
    /api/queue/v3                  -- GET: experiment_queue.json mirror (file)

The runners write progress to evidence/experiments/runner_status.json,
which the explorer polls automatically when the Experiments tab is open.
Output from runners is appended to runner.log in this directory.

Stop the server: Ctrl+C  (also stops any runners started here)
"""

import argparse
import datetime
import http.server
import json
import contextlib
import fcntl
import os
import re
import shlex
import signal
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

# Make EVERY subprocess.run(timeout=) in this module SIGTERM its child before
# SIGKILLing it. serve.py runs `git pull` / `status` / `add` / `commit` against
# REE_assembly and ree-v3 unattended; the stdlib's SIGKILL-on-timeout bypasses
# git's cleanup handler and orphans `.git/index.lock`, which then blocks
# ree_commit.py's shared-index refresh and arms a staged revert for the next
# session. See graceful_timeout.py's module docstring for the measurement.
# Module-local rebinding: the stdlib module is not mutated.
import graceful_timeout
subprocess = graceful_timeout.wrap(subprocess)

# Every hostname this module keys coordination state on -- heartbeat/status
# FILENAMES, the /machines aggregation key, the runner_commands filename -- is
# resolved through here rather than compared raw. macOS re-suffixes this Mac's
# LocalHostName on a Bonjour collision, so one physical laptop reported
# `DLAPTOP-4.local` and `DLAPTOP-5.local` across Jul-Aug 2026; keyed raw, that
# splits one box into two dashboard cards, the older of which ages into looking
# like a dead machine. VENDORED byte-identical from ree-v3 (the canonical copy,
# which carries the contract test) -- a cross-repo sys.path hop works on this Mac
# and breaks on the hub and the cloud workers. Identity gate:
# scripts/audit_vendored_copies.py --set machine_identity.
import machine_identity

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
IGW_LEDGER_FILE = PLANNING_DIR / "igw_routine_ledger.json"
# Umbrella repo (SERVE_DIR.parent), same resolution used elsewhere in this file
# (see workdir = str(SERVE_DIR.parent) below) -- chip_ledger.py always writes
# TASK_CHIPS.json there, regardless of which repo a session's cwd is under.
TASK_CHIPS_FILE = SERVE_DIR.parent / "TASK_CHIPS.json"

# Command kinds the runner accepts (mirrors ree-v3/runner_remote_control.VALID_COMMAND_KINDS)
VALID_REMOTE_COMMAND_KINDS = (
    "stop", "force_stop", "pause", "resume", "suspend", "resume_run",
    "kick", "release_claim",
)
MAX_REMOTE_COMMAND_HISTORY = 50
REVIEW_TRACKER_FILE = SERVE_DIR / "evidence" / "experiments" / "review_tracker.json"
CONTRIBUTIONS_FILE  = SERVE_DIR / "contributors" / "contributions.json"

# Timeline data paths
_TL_CLAIMS_YAML     = SERVE_DIR / "docs" / "claims" / "claims.yaml"
_TL_CLAIM_EVIDENCE  = SERVE_DIR / "evidence" / "experiments" / "claim_evidence.v1.json"
_TL_EVIDENCE_DIR    = SERVE_DIR / "evidence" / "experiments"
_TL_LITERATURE_DIR  = SERVE_DIR / "evidence" / "literature"
_DERIVED_DB_PATH    = SERVE_DIR / "evidence" / "experiments" / ".derived" / "evidence.sqlite"

# --- claim_evidence.v1.json shared loader -------------------------------------
# The file is ~10 MB (486 claims / 4,983 entries). Two request paths used to
# json.loads() it independently on EVERY GET: _brain_load_claim_evidence()
# (/api/brain-map, which then reads 5 scalars per claim) and the confidence-series
# block in _build_timeline_events() (/api/timeline/events). Both want only the
# `claims` map; neither touches `entries`.
#
# Keyed on (mtime_ns, size) rather than a TTL on purpose: a governance rebuild is
# picked up on the very next request, so this cannot serve stale evidence. That
# matters here -- the no-cache posture for explorer data is deliberate (CLAUDE.md,
# "Explorer"), and a time-based cache would reintroduce exactly the staleness the
# no-cache headers exist to prevent.
#
# The returned dict is SHARED and must be treated as read-only by callers. It is
# not deep-copied -- copying 10 MB per request would defeat the purpose.
_CLAIM_EVIDENCE_CACHE: dict = {"key": None, "claims": {}}

# Same contract for the 3.7 MB docs/claims/claims.yaml parse; see _tl_load_claims().
_TL_CLAIMS_CACHE: dict = {"key": None, "claims": []}


# Derived read-model preference (derived_evidence_index:P2, plan section 7 rows
# 2-3). Both remaining in-process consumers of the 12 MB claim_evidence.v1.json
# -- /api/brain-map's 5 scalars per claim and /api/timeline/events' confidence
# series -- want only the `claims` map, never the 5,735-row `entries` list that
# is most of the file. When the derived DB is present they read a 574-row
# projection of it instead, so the big JSON is not parsed or held resident at
# all. When it is absent (fresh clone, deleted file, indexer never run) the JSON
# cache below is used exactly as before: the fallback is load-bearing, because
# the derived file is disposable BY CONTRACT and its absence is a normal state.
_ROLLUP_CACHE: dict = {"key": None, "claims": {}}


def _claim_rollup_for_serving() -> dict:
    """The `claims` map, from the derived DB when available. READ-ONLY; shared."""
    key = _derived_db_key()
    if key is None:
        return _load_claim_evidence_claims()
    if _ROLLUP_CACHE["key"] != key:
        rows = {}
        try:
            sys.path.insert(0, str(SERVE_DIR / "evidence" / "experiments" / "scripts"))
            import derived_evidence_db as _dedb  # noqa: WPS433
            conn = _dedb.open_readonly(SERVE_DIR / "evidence" / "experiments")
            if conn is not None:
                try:
                    rows = _dedb.claim_rollup_map(conn)
                finally:
                    conn.close()
        except Exception:
            rows = {}
        if not rows:
            # Any failure at all falls back to the authoritative JSON rather than
            # serving an empty evidence map, which would render as "no claim has
            # any evidence" -- a silently wrong page, not a degraded one.
            return _load_claim_evidence_claims()
        _ROLLUP_CACHE["claims"] = rows
        _ROLLUP_CACHE["key"] = key
    return _ROLLUP_CACHE["claims"]


def _load_claim_evidence_claims() -> dict:
    """Return the `claims` map from claim_evidence.v1.json. READ-ONLY; shared."""
    try:
        st = _TL_CLAIM_EVIDENCE.stat()
    except OSError:
        _CLAIM_EVIDENCE_CACHE["key"] = None
        _CLAIM_EVIDENCE_CACHE["claims"] = {}
        return {}
    key = (st.st_mtime_ns, st.st_size)
    if _CLAIM_EVIDENCE_CACHE["key"] != key:
        try:
            data = json.loads(_TL_CLAIM_EVIDENCE.read_text(encoding="utf-8"))
            claims = data.get("claims") or {}
        except Exception:
            claims = {}
        _CLAIM_EVIDENCE_CACHE["claims"] = claims if isinstance(claims, dict) else {}
        _CLAIM_EVIDENCE_CACHE["key"] = key
    return _CLAIM_EVIDENCE_CACHE["claims"]

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


def _utc_now_iso_z() -> str:
    """UTC ISO-8601 with Z suffix (microsecond precision)."""
    return (
        datetime.datetime.now(datetime.UTC)
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z")
    )


def _utc_now_compact() -> str:
    """UTC ISO-8601 second precision with Z suffix."""
    return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

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

_phase3_preflight_cache: dict | None = None
_phase3_preflight_cache_at: float = 0.0
_phase3_preflight_lock = threading.Lock()
_PHASE3_PREFLIGHT_TTL = 60.0

_phase3_writers_cache: dict | None = None
_phase3_writers_cache_at: float = 0.0
_phase3_writers_lock = threading.Lock()
_PHASE3_WRITERS_TTL = 60.0
_PHASE3_HUB_DEFAULT_HOST = ""
# WireGuard-tunnel address of the coordinator HTTP plane on the hub.
# /writer-health is the durable replacement for the SSH+journal probe; we
# try this first and fall back to SSH if the call fails (deploy windows,
# auth issues, endpoint not yet rolled out to the hub).
_PHASE3_COORDINATOR_WG_URL = ""
# sync_daemon's tick interval. Used to colour writer rows by tick-age:
# the SYNC_INTERVAL bump from 60s -> 300s landed on the hub 2026-05-31.
# Mirroring the default here lets the explorer judge "is the writer
# alive" without depending on commit cadence.
_PHASE3_SYNC_INTERVAL_S = 300.0


def run_phase3_preflight_summary() -> dict:
    """Run coordinator phase3_preflight (dry-run: no SSH). Cached 60s."""
    global _phase3_preflight_cache, _phase3_preflight_cache_at
    with _phase3_preflight_lock:
        now = time.time()
        if (_phase3_preflight_cache is not None
                and (now - _phase3_preflight_cache_at) < _PHASE3_PREFLIGHT_TTL):
            return _phase3_preflight_cache
        ree_v3 = SERVE_DIR.parent / "ree-v3"
        script = ree_v3 / "coordinator" / "phase3_preflight.py"
        env_file = SERVE_DIR / "coordinator.env"
        if not script.exists():
            result = {
                "ok": False,
                "error": "phase3_preflight.py missing",
                "cached_at": _utc_now_iso_z(),
            }
            _phase3_preflight_cache = result
            _phase3_preflight_cache_at = now
            return result
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "phase3_preflight", script)
            mod = importlib.util.module_from_spec(spec)
            assert spec.loader is not None
            spec.loader.exec_module(mod)
            summary = mod.run_preflight(
                env_file=env_file,
                dry_run=True,
                mock=False,
                quiet=True,
            )
            summary["cached_at"] = (
                _utc_now_iso_z())
            summary["dry_run"] = True
            summary["note"] = (
                "Explorer summary uses dry-run (no SSH). "
                "Run phase3_preflight.py on Mac for full fleet probes.")
        except Exception as exc:
            summary = {
                "ok": False,
                "error": "%s: %s" % (type(exc).__name__, exc),
                "cached_at": _utc_now_iso_z(),
            }
        _phase3_preflight_cache = summary
        _phase3_preflight_cache_at = now
        return summary


def _phase3_freshness_color(age_s: float | None,
                            writer: str = "default") -> str:
    """Map commit age to a UI colour, scaled per-writer.

    Per-writer thresholds (seconds):
      heartbeat_writer: green<10min  yellow<35min  red>=35min
        (SYNC_INTERVAL=300 + future change-triggered with 30-min liveness
        floor; old 5/15 thresholds false-alarmed during idle periods)
      git_writer:       green<60min  yellow<180min red>=180min
        (commits on experiment completion; quiet stretches 30-60min are
        routine on a 3-4 worker fleet running multi-hour experiments)
      queue_writer:     green<60min  yellow<180min red>=180min
        (commits on queue claim/release/add; can be silent for hours
        during long-running experiments)
      default:          green<5min   yellow<15min  red>=15min
        (legacy thresholds preserved for any unknown writer name)

    Note: these are 'last commit age' thresholds and still conflate
    'writer process alive' with 'something has changed lately'. The
    proper fix lives in chips: switch to journal-tick-age or a
    coordinator /writer-health endpoint. Until then, the thresholds
    above match each writer's realistic commit cadence so the explorer
    stops false-alarming on healthy quiet periods.
    """
    if age_s is None:
        return "red"
    thresholds = {
        "heartbeat_writer": (10 * 60, 35 * 60),
        "git_writer":       (60 * 60, 180 * 60),
        "queue_writer":     (60 * 60, 180 * 60),
        "default":          (5 * 60, 15 * 60),
    }
    green_max, yellow_max = thresholds.get(writer, thresholds["default"])
    if age_s < green_max:
        return "green"
    if age_s < yellow_max:
        return "yellow"
    return "red"


def _parse_phase3_log_line(line: str) -> dict:
    """One line of `git log --pretty='%H %at %s'`. Returns {sha10, ts, subject}
    or {} on empty/malformed."""
    line = (line or "").strip()
    if not line:
        return {}
    parts = line.split(" ", 2)
    if len(parts) < 2:
        return {}
    sha = parts[0]
    try:
        ts = int(parts[1])
    except ValueError:
        return {}
    subject = parts[2] if len(parts) >= 3 else ""
    return {"sha10": sha[:10], "committed_at": ts, "subject": subject}


def _phase3_writer_health_color(tick_age_s: float | None,
                                 last_error: dict | None) -> str:
    """Tick-age-based health colour for HTTP-mode writer rows.

    Healthy writer process iff it has ticked recently, regardless of
    commit cadence. This is the durable signal the chip introduced:
    "writer X last ticked at HH:MM" tells the explorer "the process is
    alive and running its loop", which is what the user actually wants
    to know. Commit age is kept on the row but is informational only.

    Thresholds: < 2 x SYNC_INTERVAL green, 2-5 x yellow, > 5x red.
    A non-None last_error always paints red regardless of tick age --
    the writer is alive but failing, which still warrants attention.
    last_error has already been aged out by the coordinator side
    (WRITER_HEALTH_ERROR_TTL_S), so a present error is recent enough
    to be load-bearing.
    """
    if last_error is not None:
        return "red"
    if tick_age_s is None:
        return "red"
    if tick_age_s < 2.0 * _PHASE3_SYNC_INTERVAL_S:
        return "green"
    if tick_age_s < 5.0 * _PHASE3_SYNC_INTERVAL_S:
        return "yellow"
    return "red"


def _parse_iso_utc_to_unix(iso_str: str | None) -> int | None:
    """Parse `YYYY-MM-DDTHH:MM:SSZ` to a unix int; None on malformed."""
    if not iso_str:
        return None
    try:
        # Tolerate `Z` or `+00:00` suffix.
        s = iso_str.rstrip("Z")
        dt = datetime.datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        return int(dt.timestamp())
    except (ValueError, TypeError):
        return None


def _fetch_phase3_writer_health_http(cfg: dict) -> dict | None:
    """Single HTTP GET to coordinator /writer-health over WireGuard.

    Returns the run_phase3_writers_summary-shaped result on success, or
    None on any failure (so the caller can fall back to the SSH path).
    Never raises. Token comes from coordinator.env COORDINATOR_LOCAL_TOKEN,
    same as the other coordinator probes in this file.
    """
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN")
    if not tok:
        return None
    base_url = (cfg.get("COORDINATOR_URL")
                or _PHASE3_COORDINATOR_WG_URL).strip()
    if not base_url:
        return None
    url = base_url.rstrip("/") + "/writer-health"
    import urllib.error
    import urllib.request
    try:
        req = urllib.request.Request(
            url, headers={"Authorization": "Bearer " + tok}, method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:
            doc = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError,
            OSError, ValueError, TimeoutError):
        return None
    writers_doc = doc.get("writers")
    if not isinstance(writers_doc, dict):
        return None

    now_unix = time.time()
    cached_at = _utc_now_iso_z()

    def _writer_row_from_health(rec: dict) -> dict:
        last_tick = _parse_iso_utc_to_unix(rec.get("last_tick_at"))
        last_commit = _parse_iso_utc_to_unix(rec.get("last_commit_at"))
        tick_age = (now_unix - last_tick) if last_tick is not None else None
        commit_age = (now_unix - last_commit) if last_commit is not None else None
        sha = rec.get("last_commit_sha") or None
        subject = rec.get("last_commit_subject")
        err = rec.get("last_error") if isinstance(rec.get("last_error"), dict) else None
        return {
            # Keep the legacy shape so the existing UI consumer is bit-
            # identical when reading committed_at / sha10 / subject.
            "sha10": (sha[:10] if isinstance(sha, str) else None),
            "committed_at": last_commit,
            "subject": subject,
            "age_s": int(commit_age) if commit_age is not None else None,
            # NEW: tick-age telemetry surfaced for the explorer to render.
            "last_tick_at": rec.get("last_tick_at"),
            "tick_age_s": int(tick_age) if tick_age is not None else None,
            "last_error": err,
            "color": _phase3_writer_health_color(tick_age, err),
        }

    writers = {
        "git_writer": _writer_row_from_health(
            writers_doc.get("git_writer") or {}),
        "queue_writer": _writer_row_from_health(
            writers_doc.get("queue_writer") or {}),
        "heartbeat_writer": _writer_row_from_health(
            writers_doc.get("heartbeat_writer") or {}),
    }
    # Status hint derived from per-writer error presence. Coarser than the
    # journal-line classifier, but the HTTP path is the durable fix and the
    # error message itself is on the row for the operator to read.
    any_error = any(w.get("last_error") is not None
                    for w in writers.values())
    writer_status = "errored" if any_error else "idle"
    for row in writers.values():
        row["status"] = writer_status

    spool_pending = None
    raw_spool = doc.get("spool_pending")
    if raw_spool is not None:
        try:
            spool_pending = int(raw_spool)
        except (TypeError, ValueError):
            spool_pending = None

    return {
        "hub_reachable": True,
        "hub_host": cfg.get("SHADOW_SSH_HOST_ree-cloud-1")
                    or cfg.get("PHASE3_HUB_SSH_HOST")
                    or _PHASE3_HUB_DEFAULT_HOST,
        "writers": writers,
        "spool_pending": spool_pending,
        # Journal tail still SSH-only; HTTP path leaves it empty.
        "journal_tail": [],
        "sync_daemon_pid": doc.get("sync_daemon_pid"),
        "probe": "http",
        "cached_at": cached_at,
    }


def run_phase3_writers_summary() -> dict:
    """Fetch phase3 writer health for the explorer panel.

    Primary path: HTTP GET coordinator:8787/writer-health (sync_daemon
    publishes a snapshot every tick; the coordinator serves it). Single
    auth'd call over WireGuard. Colours come from tick-age, not commit-age,
    so healthy writers stay green during quiet periods.

    Fallback: SSH to the hub, fetch the most recent commit per writer
    (phase3:/phase3-queue:/phase3-heartbeats:), spool depth, and the last
    few sync_daemon journal lines. Slower, conflates 'writer alive' with
    'something has changed lately', and depends on SSH access -- but
    survives any future deploy gap where the HTTP endpoint is unreachable.

    Returns {hub_reachable: bool, writers: {git_writer: {...}, queue_writer:
    {...}, heartbeat_writer: {...}} | None, spool_pending: int|null,
    journal_tail: [str], probe: 'http'|'ssh', cached_at: iso,
    fleet_drained: bool|null (optional)}.
    """
    global _phase3_writers_cache, _phase3_writers_cache_at
    with _phase3_writers_lock:
        now = time.time()
        if (_phase3_writers_cache is not None
                and (now - _phase3_writers_cache_at) < _PHASE3_WRITERS_TTL):
            return _phase3_writers_cache

        cfg = _load_coordinator_cfg()
        http_result = _fetch_phase3_writer_health_http(cfg)
        if http_result is not None:
            _phase3_writers_cache = http_result
            _phase3_writers_cache_at = now
            return http_result

        # Hub SSH target: local configuration only. Do not hard-code deployment
        # hostnames or public IPs in the public repo.
        hub_host = (cfg.get("SHADOW_SSH_HOST_ree-cloud-1")
                    or cfg.get("PHASE3_HUB_SSH_HOST")
                    or _PHASE3_HUB_DEFAULT_HOST)
        if not hub_host:
            result = {
                "hub_reachable": False,
                "hub_host": None,
                "writers": None,
                "spool_pending": None,
                "journal_tail": [],
                "error": "PHASE3 hub SSH host is not configured locally.",
                "probe": "ssh",
                "cached_at": _utc_now_iso_z(),
            }
            _phase3_writers_cache = result
            _phase3_writers_cache_at = now
            return result
        ssh_user = cfg.get("COORDINATOR_SSH_USER", "ree")
        sentinel_g = "===PHASE3_GIT==="
        sentinel_q = "===PHASE3_QUEUE==="
        sentinel_h = "===PHASE3_HB==="
        sentinel_s = "===PHASE3_SPOOL==="
        sentinel_j = "===PHASE3_JOURNAL==="
        # `--all` so we surface writer commits even if local HEAD is behind
        # origin/<default>. `git -C ~/REE_Working/REE_assembly` -- the hub
        # checkout path documented in CLAUDE.md Coordinator section.
        cmd = (
            "echo " + sentinel_g + " && "
            "git -C ~/REE_Working/REE_assembly log -1 --all "
            "--grep='^phase3:' --pretty='%H %at %s' 2>/dev/null && "
            "echo " + sentinel_q + " && "
            "git -C ~/REE_Working/ree-v3 log -1 --all "
            "--grep='^phase3-queue:' --pretty='%H %at %s' 2>/dev/null && "
            "echo " + sentinel_h + " && "
            "git -C ~/REE_Working/REE_assembly log -1 --all "
            "--grep='^phase3-heartbeats:' --pretty='%H %at %s' 2>/dev/null && "
            "echo " + sentinel_s + " && "
            "ls /home/ree/coordinator-spool/pending/ 2>/dev/null | wc -l && "
            "echo " + sentinel_j + " && "
            "(sudo -n journalctl -u ree-sync-daemon -n 3 --no-pager 2>&1 "
            "|| journalctl -u ree-sync-daemon -n 3 --no-pager --user 2>&1 "
            "|| echo 'journalctl unavailable')"
        )
        cached_at = _utc_now_iso_z()
        # _ssh() truncates stdout to 300 chars -- not enough for the journal
        # tail, so call subprocess directly. Same hardening as _ssh
        # (BatchMode, ConnectTimeout, accept-new).
        try:
            cp = subprocess.run(
                ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5",
                 "-o", "StrictHostKeyChecking=accept-new",
                 f"{ssh_user}@{hub_host}", cmd],
                capture_output=True, text=True, timeout=25)
        except Exception as exc:  # noqa: BLE001
            result = {
                "hub_reachable": False,
                "hub_host": hub_host,
                "writers": None,
                "spool_pending": None,
                "journal_tail": [],
                "error": repr(exc),
                "probe": "ssh",
                "cached_at": cached_at,
            }
            _phase3_writers_cache = result
            _phase3_writers_cache_at = now
            return result
        if cp.returncode != 0:
            detail = (cp.stderr or cp.stdout or "").strip()[:300]
            result = {
                "hub_reachable": False,
                "hub_host": hub_host,
                "writers": None,
                "spool_pending": None,
                "journal_tail": [],
                "error": detail or ("ssh rc=%d" % cp.returncode),
                "probe": "ssh",
                "cached_at": cached_at,
            }
            _phase3_writers_cache = result
            _phase3_writers_cache_at = now
            return result
        stdout = cp.stdout or ""

        def _block(text: str, start: str, end: str | None) -> str:
            i = text.find(start)
            if i < 0:
                return ""
            i += len(start)
            j = text.find(end, i) if end else len(text)
            if j < 0:
                j = len(text)
            return text[i:j].strip()

        g_block = _block(stdout, sentinel_g, sentinel_q)
        q_block = _block(stdout, sentinel_q, sentinel_h)
        h_block = _block(stdout, sentinel_h, sentinel_s)
        s_block = _block(stdout, sentinel_s, sentinel_j)
        j_block = _block(stdout, sentinel_j, None)

        now_unix = time.time()

        def _writer_row(block: str, writer: str = "default") -> dict:
            parsed = _parse_phase3_log_line(block)
            if not parsed:
                return {"sha10": None, "committed_at": None, "subject": None,
                        "age_s": None, "color": "red"}
            age = max(0.0, now_unix - parsed["committed_at"])
            return {
                "sha10": parsed["sha10"],
                "committed_at": parsed["committed_at"],
                "subject": parsed["subject"],
                "age_s": int(age),
                "color": _phase3_freshness_color(age, writer=writer),
            }

        writers = {
            "git_writer": _writer_row(g_block, writer="git_writer"),
            "queue_writer": _writer_row(q_block, writer="queue_writer"),
            "heartbeat_writer": _writer_row(h_block, writer="heartbeat_writer"),
        }
        # Journal-derived status hint for each writer. Cheap pattern match;
        # leaves "idle" as the default when the tail doesn't say otherwise.
        journal_lines = [ln for ln in j_block.splitlines() if ln.strip()]
        tail_blob = " ".join(journal_lines).lower()
        if "push rejected" in tail_blob or "non-fast-forward" in tail_blob:
            writer_status = "push-rejected"
        elif ("conflict" in tail_blob or "rebase aborted" in tail_blob
              or "needs operator" in tail_blob):
            writer_status = "rebase-conflict"
        elif "refusing" in tail_blob or "dirty tree" in tail_blob:
            writer_status = "refusing"
        elif ("committed" in tail_blob or "committing" in tail_blob
              or "wrote" in tail_blob or "tick:" in tail_blob):
            writer_status = "committing"
        else:
            writer_status = "idle"
        for row in writers.values():
            row["status"] = writer_status

        try:
            spool_pending = int(s_block.strip().splitlines()[-1])
        except (ValueError, IndexError):
            spool_pending = None

        result = {
            "hub_reachable": True,
            "hub_host": hub_host,
            "writers": writers,
            "spool_pending": spool_pending,
            "journal_tail": journal_lines[-3:],
            "probe": "ssh",
            "cached_at": cached_at,
        }
        _phase3_writers_cache = result
        _phase3_writers_cache_at = now
        return result


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
                "cached_at": _utc_now_iso_z(),
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
                "cached_at": _utc_now_iso_z(),
                "tail": tail,
                "error": None if proc.returncode == 0 else f"exit {proc.returncode}",
            }
        except subprocess.TimeoutExpired:
            result = {
                "ok": False,
                "passed": 0,
                "failed": 0,
                "duration_s": round(time.time() - start, 3),
                "cached_at": _utc_now_iso_z(),
                "tail": [],
                "error": "timeout",
            }
        except Exception as exc:
            result = {
                "ok": False,
                "passed": 0,
                "failed": 0,
                "duration_s": round(time.time() - start, 3),
                "cached_at": _utc_now_iso_z(),
                "tail": [],
                "error": f"{type(exc).__name__}: {exc}",
            }
        _preflight_cache = result
        _preflight_cache_at = now
        return result


# ── Workspace health (stale TASK_CLAIMS + orphaned git stashes) ─────────────
# Explorer UI improvement plan B2: neither signal was computed by serve.py at
# all -- both were standalone CLI scripts (scripts/audit_stale_claims.py,
# scripts/audit_stashes.py) with no HTTP surface. Shells out to each with
# --json on a cheap cache TTL, mirroring run_preflight_suite() above rather
# than porting the classification logic (lower risk -- the scripts stay the
# single source of truth for what counts as stale/orphaned).
_WORKSPACE_HEALTH_TTL = 60.0
_workspace_health_cache: dict | None = None
_workspace_health_cache_at: float = 0.0
_workspace_health_lock = threading.Lock()

UMBRELLA_DIR = SERVE_DIR.parent
_SCRIPTS_DIR = UMBRELLA_DIR / "scripts"


def _run_json_script(script: Path, args: list[str], timeout: float) -> dict:
    """Run `python3 script *args` and parse stdout as JSON. Raises on failure."""
    if not script.exists():
        raise FileNotFoundError(f"{script} missing")
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        cwd=str(UMBRELLA_DIR),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    try:
        return json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError) as exc:
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-5:]
        raise ValueError(
            f"exit {proc.returncode}, unparseable output: {'; '.join(tail)}"
        ) from exc


def _stale_claims_summary(timeout: float = 20.0) -> dict:
    try:
        data = _run_json_script(
            _SCRIPTS_DIR / "audit_stale_claims.py", ["--json"], timeout)
        buckets: dict[str, int] = {}
        for r in data.get("records") or []:
            b = r.get("bucket") or "?"
            buckets[b] = buckets.get(b, 0) + 1
        return {
            "ok": True,
            "count": data.get("stale_active", 0),
            "contentions": len(data.get("contentions") or []),
            "buckets": buckets,
            "error": None,
        }
    except Exception as exc:
        return {"ok": False, "count": 0, "contentions": 0, "buckets": {},
                "error": f"{type(exc).__name__}: {exc}"}


def _orphaned_stashes_summary(timeout: float = 20.0) -> dict:
    try:
        data = _run_json_script(
            _SCRIPTS_DIR / "audit_stashes.py", ["--json"], timeout)
        repos = []
        total = 0
        for r in data.get("repos") or []:
            n = len(r.get("entries") or [])
            n_rebase = len(r.get("rebase_findings") or [])
            total += n + n_rebase
            if n or n_rebase or r.get("error"):
                repos.append({
                    "repo": r.get("repo"),
                    "entries": n,
                    "rebase_findings": n_rebase,
                    "error": r.get("error"),
                })
        return {"ok": True, "count": total, "repos": repos, "error": None}
    except Exception as exc:
        return {"ok": False, "count": 0, "repos": [],
                "error": f"{type(exc).__name__}: {exc}"}


def run_workspace_health_summary() -> dict:
    """Combined stale-claim + orphaned-stash summary. Memoised for
    _WORKSPACE_HEALTH_TTL seconds -- each half is a git-touching CLI script,
    not free, and the corner-dock panel polls this on a fixed interval.
    """
    global _workspace_health_cache, _workspace_health_cache_at
    with _workspace_health_lock:
        now = time.time()
        if (_workspace_health_cache is not None
                and (now - _workspace_health_cache_at) < _WORKSPACE_HEALTH_TTL):
            return _workspace_health_cache
        stale_claims = _stale_claims_summary()
        stashes = _orphaned_stashes_summary()
        result = {
            "ok": stale_claims["ok"] and stashes["ok"],
            "cached_at": _utc_now_iso_z(),
            "stale_claims": stale_claims,
            "stashes": stashes,
        }
        _workspace_health_cache = result
        _workspace_health_cache_at = now
        return result


# ── Docs picker index ─────────────────────────────────────────────────────────

_DOCS_PICKER_CONFIG_PATH = SERVE_DIR / "docs_picker_config.json"
_DOCS_TITLE_ACRONYMS = {"REE", "E1", "E2", "E3", "JEPA", "V1", "V2", "V3", "V4"}


def _title_from_filename(path: Path) -> str:
    words = re.split(r"[_\-]+", path.stem)
    parts = [w.upper() if w.upper() in _DOCS_TITLE_ACRONYMS else w.capitalize()
             for w in words if w]
    return " ".join(parts) if parts else path.stem


def read_docs_index() -> dict:
    """Doc index for the Docs picker (GET /api/docs/index): curated groups
    from docs_picker_config.json, plus every *.md file in that config's
    low-noise 'auto_dirs' (titled from its filename). docs/architecture/ and
    evidence/planning/ are deliberately NOT auto-scanned -- both are mostly
    historical/working files rather than reference docs (247 vs ~48 curated,
    799 vs 11 curated as of 2026-08-02) -- see docs_picker_config.json's
    top-level comment and explorer_ui_improvement_plan.md C4.
    """
    try:
        config = json.loads(_DOCS_PICKER_CONFIG_PATH.read_text())
    except Exception as exc:
        return {"groups": [], "error": f"{type(exc).__name__}: {exc}"}

    serve_root = SERVE_DIR.resolve()
    groups = []
    seen_paths = set()

    for group in config.get("curated_groups", []):
        docs = []
        for doc in group.get("docs", []):
            rel_path = doc.get("path")
            if not rel_path:
                continue
            seen_paths.add(rel_path)
            docs.append({"title": doc.get("title") or rel_path, "path": rel_path})
        if docs:
            groups.append({"label": group.get("label") or "Docs", "docs": docs})

    for entry in config.get("auto_dirs", []):
        rel_dir = entry.get("dir")
        label = entry.get("group") or rel_dir
        if not rel_dir:
            continue
        abs_dir = (SERVE_DIR / rel_dir).resolve()
        if abs_dir != serve_root and serve_root not in abs_dir.parents:
            continue  # outside the repo root -- ignore rather than serve it
        if not abs_dir.is_dir():
            continue
        docs = []
        for f in sorted(abs_dir.glob("*.md")):
            rel_path = str(f.relative_to(serve_root))
            if rel_path in seen_paths:
                continue  # already reachable via a curated entry
            seen_paths.add(rel_path)
            docs.append({"title": _title_from_filename(f), "path": rel_path})
        if docs:
            groups.append({"label": label, "docs": docs})

    return {"groups": groups, "error": None}


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


# ── launchd supervision (Mac v3 runner) ──────────────────────────────────────
# When ~/Library/LaunchAgents/com.ree.runner.plist is installed, the v3
# runner is supervised by launchd (KeepAlive=true) instead of being
# spawned as a Popen child of this serve.py. This matches the cloud
# workers' systemd setup: crashes auto-respawn, the explorer's Stop
# button still maps to a genuine "really stop" (launchctl bootout). The
# plist runs ~/.local/bin/ree_runner_launchd.sh which loads the same env
# vars _default_runner_extra_env would have injected, so behaviour is
# bit-identical to the Popen path on a normal run.

_LAUNCHD_PLIST_PATH = Path.home() / "Library" / "LaunchAgents" / "com.ree.runner.plist"
_LAUNCHD_LABEL = "com.ree.runner"


def _launchd_supervises_v3() -> bool:
    """True iff the v3 runner should be driven via launchctl rather than Popen."""
    return _LAUNCHD_PLIST_PATH.is_file()


def _launchd_target() -> str:
    return f"gui/{os.getuid()}/{_LAUNCHD_LABEL}"


def _launchd_pid() -> int | None:
    """Return the PID of the running launchd-supervised runner, or None.

    Uses `launchctl print <target>` which prints a PID line when the
    service is loaded AND running, and exits non-zero (or shows
    'pid = -' style) when stopped.
    """
    try:
        r = subprocess.run(
            ["launchctl", "print", _launchd_target()],
            capture_output=True, text=True, timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if r.returncode != 0:
        return None
    for line in r.stdout.splitlines():
        s = line.strip()
        if s.startswith("pid ") or s.startswith("pid="):
            # Format: "pid = 12345" or similar
            parts = s.split("=", 1)
            if len(parts) == 2:
                try:
                    pid = int(parts[1].strip())
                    if pid > 0 and _proc_alive(pid):
                        return pid
                except ValueError:
                    pass
    return None


def _launchd_bootstrap_if_needed() -> tuple[bool, str]:
    """Ensure the plist is loaded into the user's gui session. Idempotent.

    Returns (ok, note). bootstrap returns 0 on success and 5 (or
    similar) on "already loaded" -- we treat both as ok.
    """
    try:
        r = subprocess.run(
            ["launchctl", "bootstrap", f"gui/{os.getuid()}",
             str(_LAUNCHD_PLIST_PATH)],
            capture_output=True, text=True, timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return False, f"bootstrap failed: {e}"
    if r.returncode == 0:
        return True, "bootstrapped"
    # 5 = service already loaded; benign for kickstart purposes
    stderr = (r.stderr or "").lower()
    if "already loaded" in stderr or "service already" in stderr or r.returncode == 5:
        return True, "already_loaded"
    return False, f"bootstrap rc={r.returncode}: {r.stderr.strip()}"


def _launchd_kickstart() -> tuple[bool, str]:
    """Tell launchd to start the service if it isn't already running."""
    try:
        r = subprocess.run(
            ["launchctl", "kickstart", _launchd_target()],
            capture_output=True, text=True, timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return False, f"kickstart failed: {e}"
    if r.returncode == 0:
        return True, "kickstarted"
    return False, f"kickstart rc={r.returncode}: {r.stderr.strip()}"


def _launchd_bootout() -> tuple[bool, str]:
    """Unload the plist entirely. KeepAlive does NOT respawn after bootout."""
    try:
        r = subprocess.run(
            ["launchctl", "bootout", _launchd_target()],
            capture_output=True, text=True, timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return False, f"bootout failed: {e}"
    if r.returncode == 0:
        return True, "bootout"
    stderr = (r.stderr or "").lower()
    if "could not find" in stderr or r.returncode == 113:
        return True, "not_loaded"
    return False, f"bootout rc={r.returncode}: {r.stderr.strip()}"


def _launchd_kill(sig: str) -> tuple[bool, str]:
    """Send a signal to the launchd-supervised runner. sig is 'TERM' or 'KILL'."""
    try:
        r = subprocess.run(
            ["launchctl", "kill", sig, _launchd_target()],
            capture_output=True, text=True, timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return False, f"kill failed: {e}"
    if r.returncode == 0:
        return True, f"signalled {sig}"
    return False, f"kill rc={r.returncode}: {r.stderr.strip()}"


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
    # When v3 is launchd-supervised, launchctl is the preferred source.
    # It catches PIDs that launchd respawned after a crash without our
    # knowledge. But fall through to the Popen / ext_pid / pid_file
    # paths when launchctl reports nothing -- the plist may be installed
    # while an old Popen-spawned runner from a previous serve.py session
    # is still alive (transition state), and the explorer needs to see
    # that PID so the Stop button works.
    if ver == "v3" and _launchd_supervises_v3():
        lpid = _launchd_pid()
        if lpid is not None:
            return lpid
        # fall through to legacy detection below
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


def _commit_and_push_assignments(message: str) -> dict:
    """Commit + push igw_assignments.json to origin/master immediately.

    Workaround for the heartbeat-reset race: ree-v3/runner_remote_control.py
    push_heartbeat()->_push_telemetry_file() runs
    `git checkout -f -B master origin/master` every ~6-13s. Uncommitted local
    mods to tracked files in evidence/planning/ are silently wiped (TOCTOU
    race with _hard_sync_is_safe). Pushing to origin immediately means the
    heartbeat's reset target ALREADY contains the assignment, so the reset
    preserves rather than wipes it.

    Returns {"status": "ok"|"skipped"|"error", "message": ..., "sha": ...}.
    Best-effort; never raises.
    """
    rel = "evidence/planning/igw_assignments.json"
    out = {"status": "error", "message": "?", "sha": None}
    try:
        # Stage only the assignments file. NEVER `git add -A` or `git add .`
        # -- the working tree may contain unrelated heartbeat-side files mid
        # commit, and we must not absorb them.
        add = subprocess.run(["git", "add", rel], cwd=str(SERVE_DIR),
                             capture_output=True, text=True, timeout=10)
        if add.returncode != 0:
            return {"status": "error", "message": f"git add: {add.stderr.strip()[:200]}", "sha": None}
        # Anything staged?
        diff = subprocess.run(["git", "diff", "--cached", "--quiet"],
                              cwd=str(SERVE_DIR), capture_output=True, text=True, timeout=10)
        if diff.returncode == 0:
            return {"status": "skipped", "message": "nothing staged", "sha": None}
        commit = subprocess.run(
            ["git", "commit", "-m", message, "--", rel],
            cwd=str(SERVE_DIR), capture_output=True, text=True, timeout=15,
        )
        if commit.returncode != 0:
            return {"status": "error", "message": f"git commit: {commit.stderr.strip()[:200]}", "sha": None}
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(SERVE_DIR),
                             capture_output=True, text=True, timeout=5).stdout.strip()[:12]
        push = subprocess.run(["git", "push", "origin", "HEAD:master"],
                              cwd=str(SERVE_DIR), capture_output=True, text=True, timeout=30)
        if push.returncode != 0:
            return {"status": "error", "message": f"git push: {push.stderr.strip()[:200]}", "sha": sha}
        return {"status": "ok", "message": "committed and pushed", "sha": sha}
    except subprocess.TimeoutExpired as exc:
        # MUST stay ahead of the bare `except Exception` below. A timeout here
        # is not just "the commit did not happen": until graceful_timeout was
        # wired in above, the SIGKILL left an orphan `.git/index.lock` in
        # REE_assembly, and this handler reported it as an ordinary error dict
        # that nobody reads -- a silent producer of the workspace's recurring
        # stale-lock incidents. The lock is fixed at the signal level now; this
        # branch exists so the TIMEOUT ITSELF is never again invisible.
        cmd = " ".join(exc.cmd) if isinstance(exc.cmd, (list, tuple)) else str(exc.cmd)
        print(f"[serve] TIMEOUT in _commit_and_push_assignments: repo=REE_assembly "
              f"cmd={cmd!r} after {exc.timeout}s -- SIGTERM sent first, so no "
              f"orphan .git/index.lock is expected; check if one appears.",
              flush=True)
        return {"status": "error",
                "message": f"timeout after {exc.timeout}s: {cmd}", "sha": None}
    except Exception as exc:
        return {"status": "error", "message": f"exception: {exc}", "sha": None}


def load_review_tracker() -> dict:
    if REVIEW_TRACKER_FILE.exists():
        return json.loads(REVIEW_TRACKER_FILE.read_text())
    return {"schema_version": "review_tracker/v1", "reviewed_run_ids": [], "discussed_experiment_dirs": []}


def save_review_tracker(data: dict) -> None:
    """Write review_tracker.json ATOMICALLY (tmp + os.replace).

    The previous implementation was a bare `write_text`, which truncates the file
    to zero and then refills it. A crash, a full disk, or a SIGKILL in that window
    leaves the 685 KB registry that CLAUDE.md calls "the sole source of truth for
    whether an experiment has been discussed" truncated or empty, with no copy
    anywhere -- it is hand-maintained state, derivable from nothing. os.replace is
    atomic on POSIX, so a reader either sees the whole old file or the whole new
    one and never a partial write.
    """
    REVIEW_TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = REVIEW_TRACKER_FILE.with_name(f"{REVIEW_TRACKER_FILE.name}.tmp-{os.getpid()}")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    os.replace(str(tmp), str(REVIEW_TRACKER_FILE))


# --- review_tracker.json lost-update fix (derived_evidence_index:P2, plan sec 3)
#
# THE BUG. `POST /api/review/discuss` did load -> mutate -> save with nothing in
# between. serve.py runs on a ThreadingHTTPServer, so two review actions arriving
# together both read the same 685 KB snapshot, each appends its own dir_name, and
# whichever saves LAST silently erases the other's append. No error, no log line,
# and the explorer shows the surviving one as if both had landed.
#
# WHY NOT THE PLAN'S FIX. Plan section 3 proposes moving this to
# `INSERT INTO discussed_dirs`. That would relocate CANONICAL, non-derivable state
# into the gitignored SQLite read-model, whose own contract says deleting it is
# always safe -- so the fix would trade a rare lost update for a routine total
# loss. review_tracker.json stays canonical and git-tracked; the DB carries a
# rebuilt-from-it mirror for querying only.
#
# WHY BOTH LOCKS. The threading.Lock serialises this process's own handler
# threads, which is the confirmed race. The flock covers the other writers of the
# same file that are not this process at all -- a second serve.py, a governance
# session running scripts/generate_pending_review.py's siblings, or a human
# editing via a helper -- and costs nothing when uncontended. Neither subsumes the
# other. The flock is best-effort by design: a filesystem without working flock
# (some network mounts) degrades to the in-process lock rather than refusing the
# write, because refusing to record a review is worse than the race it prevents.
_REVIEW_TRACKER_LOCK = threading.Lock()
_REVIEW_TRACKER_LOCKFILE = REVIEW_TRACKER_FILE.with_name(REVIEW_TRACKER_FILE.name + ".lock")


@contextlib.contextmanager
def _review_tracker_guard():
    with _REVIEW_TRACKER_LOCK:
        fh = None
        try:
            try:
                _REVIEW_TRACKER_LOCKFILE.parent.mkdir(parents=True, exist_ok=True)
                fh = open(_REVIEW_TRACKER_LOCKFILE, "a+")
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
            except Exception:
                if fh is not None:
                    try:
                        fh.close()
                    except Exception:
                        pass
                fh = None
            yield
        finally:
            if fh is not None:
                try:
                    fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
                finally:
                    fh.close()


def update_review_tracker(mutate) -> dict:
    """Serialised read-modify-write of review_tracker.json.

    `mutate(data)` is called with the file's CURRENT contents, re-read INSIDE the
    lock -- re-reading is the half that actually fixes the lost update; locking a
    stale snapshot would only make the overwrite orderly. Returns the saved dict.
    """
    with _review_tracker_guard():
        data = load_review_tracker()
        mutate(data)
        save_review_tracker(data)
        return data


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

    Two files can denote ONE physical box (`DLAPTOP-4.local.json` written
    before the identity fix, `DLAPTOP.json` after it), and the Phase-3 writer
    never deletes the superseded one. Keying on the raw filename stem therefore
    let a single box contribute two `current` entries -- the same in-flight
    experiment rendered twice under two `_machine` labels. `completed` and
    `queue` were always safe (both deduplicate by queue_id); `current` was not.

    So live state (`current`, `idle`, `runner_pid`) is taken per CANONICAL
    machine, freshest file winning, while `completed` and `queue` stay a UNION
    over every file -- a superseded twin still holds real run history that the
    box's fresh file does not carry, so dropping it outright would lose runs
    from the merged view. This is why the whole map is not simply passed
    through `_merge_by_canonical_machine`, as `/machines` does: that endpoint
    wants one ROW per box, this function returns a UNION.
    """
    raw_files = {}

    # Read per-machine files
    if STATUS_DIR.is_dir():
        for f in sorted(STATUS_DIR.glob("*.json")):
            try:
                raw_files[f.stem] = json.loads(f.read_text())
            except Exception:
                pass

    # Fallback: the pre-split monolithic runner_status.json.
    #
    # HISTORY ONLY -- the live fields are deliberately stripped (2026-09-01).
    # This branch used to `return json.loads(STATUS_FILE.read_text())` verbatim,
    # which handed the explorer's local runner card that file's `current` /
    # `idle` / `runner_pid` as CURRENT FLEET STATE. The file has been untracked
    # since 2026-03-22 (`19adc90be7`) and frozen on disk since 2026-07-20, so
    # what it would render is a months-old snapshot presented as live -- and
    # silently, because a stale-but-plausible runner card looks exactly like a
    # fresh one. `completed` and `queue` ARE still real history and are kept:
    # this is the same distinction generate_pending_review.py already draws when
    # it reads the same file for its completed-run corpus, and the reason
    # scripts/experiment_error_rate.py calls it the only record for its era.
    #
    # The branch is unreachable in practice (evidence/experiments/runner_status/
    # has existed since 2026-04-18 and the phase3 heartbeat writer keeps it
    # populated); it is corrected rather than deleted so that a box which somehow
    # loses the split directory degrades to "no live status" instead of to a
    # confidently wrong one.
    if not raw_files and STATUS_FILE.exists():
        try:
            legacy = json.loads(STATUS_FILE.read_text())
        except Exception:
            return {}
        if not isinstance(legacy, dict):
            return {}
        return {
            "completed": legacy.get("completed", []),
            "queue": legacy.get("queue", []),
            "current": [],
            "running": False,
            "idle": True,
            "last_updated": legacy.get("last_updated", ""),
            "_legacy_monolithic_fallback": True,
            "_legacy_live_fields_stripped": (
                "runner_status.json is frozen; current/running/runner_pid are not "
                "live state and have been withheld"
            ),
        }

    if not raw_files:
        return {}

    # Freshest file per canonical machine. The numbered cloud fleet does NOT
    # collapse -- `canonical_machine_name` is an allowlist, not a `-<digits>`
    # regex, so ree-cloud-1..5 and ree-worker-1..4 keep one entry each.
    machines = _merge_by_canonical_machine(raw_files, "last_updated")

    # Merge
    all_completed = []
    seen_queue_ids = set()
    current_list = []
    any_running = False
    latest_update = ""
    merged_queue = []
    queue_ids_seen = set()

    # History is a UNION over EVERY file, including a superseded identity twin:
    # both lists deduplicate by queue_id, and the stale twin still holds real
    # runs the box's current file no longer carries.
    for data in raw_files.values():
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

    # Live state is per CANONICAL machine, so one physical box contributes
    # exactly one `current` entry however many status files it owns.
    for machine_name, data in machines.items():
        # Current: collect all running experiments
        cur = data.get("current")
        if cur:
            cur["_machine"] = machine_name
            current_list.append(cur)

        # Running state
        if not data.get("idle", True) and data.get("runner_pid"):
            any_running = True

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
        # Clamp negative ages (a worker whose clock is slightly ahead of this
        # host) to 0: a just-arrived heartbeat with a future-skewed timestamp is
        # the freshest, not stale. Without this, the `0 <= age` freshness checks
        # downstream flip an actively-heartbeating machine to
        # fresh=False/display_fresh=False/state=stale on a few seconds of clock
        # skew (observed: ree-cloud-2 reporting age=-2 -> display_fresh=False).
        return max(0, int((now - t).total_seconds()))
    except Exception:
        return None


_COORD_SNAP_CACHE: dict = {
    "t": 0.0,
    "ok": False,
    "data": {},
    "last_good": {},
    "last_good_t": 0.0,
}
_COORD_SNAP_LOCK = threading.Lock()
_COORD_SNAP_TTL_SECONDS = 15.0
_COORD_SNAP_FAILURE_TTL_SECONDS = 3.0
_COORD_SNAP_LAST_GOOD_MAX_SECONDS = 120.0
_COORD_SNAP_TIMEOUT_SECONDS = 2.0


def _fetch_coordinator_machine_snapshots(cfg: dict) -> dict[str, dict]:
    """Live heartbeats from the Phase-1 coordinator (WireGuard).

    Returns {machine: snapshot} or {} when unconfigured/unreachable.
    Never raises -- /api/machines must stay available if the hub is down.

    Successful responses are cached for _COORD_SNAP_TTL_SECONDS. On fetch
    failure, returns the last successful snapshot for up to
    _COORD_SNAP_LAST_GOOD_MAX_SECONDS (does not cache empty failures for
    the full success TTL).
    """
    import urllib.error
    import urllib.request

    url = (cfg.get("COORDINATOR_URL") or "").rstrip("/")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN") or ""
    if not url or not tok:
        return {}

    now = time.monotonic()
    with _COORD_SNAP_LOCK:
        age = now - _COORD_SNAP_CACHE["t"]
        ttl = (_COORD_SNAP_TTL_SECONDS if _COORD_SNAP_CACHE.get("ok")
               else _COORD_SNAP_FAILURE_TTL_SECONDS)
        if age < ttl:
            if _COORD_SNAP_CACHE.get("ok"):
                return dict(_COORD_SNAP_CACHE["data"])
            lg = _COORD_SNAP_CACHE.get("last_good") or {}
            if lg and (now - _COORD_SNAP_CACHE.get("last_good_t", 0)
                       <= _COORD_SNAP_LAST_GOOD_MAX_SECONDS):
                return dict(lg)

    out: dict[str, dict] = {}
    fetch_ok = False
    try:
        req = urllib.request.Request(
            url + "/shadow/status",
            headers={"Authorization": "Bearer " + tok},
            method="GET",
        )
        with urllib.request.urlopen(
                req, timeout=_COORD_SNAP_TIMEOUT_SECONDS) as resp:
            st = json.loads(resp.read().decode("utf-8"))
        for m in st.get("machines") or []:
            name = m.get("machine")
            if not name:
                continue
            out[name] = {
                "last_tick_utc": m.get("last_seen") or "",
                "state": m.get("state") or "unknown",
                "current_exq": m.get("current_exq"),
                "progress": m.get("progress") or {},
                "seconds_elapsed": m.get("seconds_elapsed"),
                "seconds_remaining": m.get("seconds_remaining"),
            }
        # The DB carries rows under every hostname a box has ever reported, so
        # merge here rather than downstream -- this dict is CACHED, and caching
        # raw keys would re-split the laptop on every cache hit.
        out = _merge_by_canonical_machine(out, "last_tick_utc")
        fetch_ok = True
    except (urllib.error.URLError, OSError,
            json.JSONDecodeError, ValueError):
        out = {}

    with _COORD_SNAP_LOCK:
        _COORD_SNAP_CACHE["t"] = time.monotonic()
        if fetch_ok:
            _COORD_SNAP_CACHE["ok"] = True
            _COORD_SNAP_CACHE["data"] = out
            if out:
                _COORD_SNAP_CACHE["last_good"] = out
                _COORD_SNAP_CACHE["last_good_t"] = _COORD_SNAP_CACHE["t"]
            return dict(out)
        _COORD_SNAP_CACHE["ok"] = False
        _COORD_SNAP_CACHE["data"] = {}
        lg = _COORD_SNAP_CACHE.get("last_good") or {}
        if lg and (_COORD_SNAP_CACHE["t"] - _COORD_SNAP_CACHE.get(
                "last_good_t", 0) <= _COORD_SNAP_LAST_GOOD_MAX_SECONDS):
            return dict(lg)
    return {}


def _telemetry_tick(payload: dict, *keys: str) -> str:
    """First non-empty timestamp among `keys`, or "" when the payload has none.

    Fixed-width `%Y-%m-%dT%H:%M:%SZ`, so plain string ordering is chronological
    and "" sorts below every real timestamp -- which is the behaviour wanted:
    a telemetry file with no tick at all must never beat one that has ticked.
    """
    for key in keys:
        val = payload.get(key)
        if val:
            return str(val)
    return ""


def _merge_by_canonical_machine(raw_map: dict, *tick_keys: str) -> dict:
    """Re-key raw-hostname-keyed telemetry onto canonical machine identity.

    Two files can denote ONE physical machine (`DLAPTOP-4.local.json` written
    before the identity fix, `DLAPTOP.json` after it). They must MERGE to a
    single row rather than overwrite by iteration order -- `sorted()` is
    alphabetical, so a plain last-write-wins would hand the row to the stale
    `DLAPTOP-4.local` and show the live laptop as hours-old.

    Freshest tick wins. Ties go to the file whose own name is already canonical,
    i.e. the one the current writer produces, so the winner is deterministic
    rather than alphabetical.

    This PICKS A ROW, it does not combine fields -- despite the name, it returns
    exactly ONE payload per canonical machine and DISCARDS the losing file's
    payload wholesale. That is what `read_machines` wants (one row per box), but
    a caller needing the UNION of a list-valued field (`completed`, `queue`, or
    any future one) must union that field itself over the raw map; taking it from
    this return value silently drops every entry the loser held. Worked example:
    `read_merged_runner_status` uses this helper for LIVE STATE ONLY and unions
    `completed`/`queue` over the raw files separately.

    The numbered cloud fleet does NOT collapse: `canonical_machine_name` is an
    allowlist (see machine_identity.SUFFIX_BLIND_BASES), so `ree-cloud-1` .. `-5`
    and `ree-worker-1` .. `-4` pass through untouched and keep one row each.
    """
    merged: dict = {}
    rank: dict = {}
    for raw_key in sorted(raw_map):
        payload = raw_map[raw_key]
        key = machine_identity.canonical_machine_name(raw_key) or raw_key
        this = (_telemetry_tick(payload, *tick_keys), raw_key == key)
        if key not in merged or this > rank[key]:
            merged[key] = payload
            rank[key] = this
    return merged


def _hostname_fields(hb: dict) -> dict:
    """`hostname` resolved to canonical identity, raw preserved when it drifted.

    Canonicalised so no downstream consumer can re-split a machine on this field
    after /machines has already merged it. `hostname_reported` appears ONLY when
    the box reported a drifted spelling -- that disagreement is exactly the
    signal the Jul-Aug 2026 split was eventually noticed by, so it is surfaced
    rather than silently normalised away.
    """
    raw = hb.get("hostname")
    if not raw:
        return {}
    canon = machine_identity.canonical_machine_name(raw) or raw
    out = {"hostname": canon}
    if canon != raw:
        out["hostname_reported"] = raw
    return out


def _enrich_machine_from_git(entry: dict, hb: dict, st: dict) -> None:
    """Copy rich display fields from the git mirror only.

    Never changes last_tick_utc, age, fresh, state, or in-flight progress;
    those come from the coordinator when Phase 3 is live.
    """
    if hb:
        entry.update(_hostname_fields(hb))
        for key in (
            "current_exq_started_utc", "current_title", "current_claim_id",
            "current_description", "recent_lines", "queue_depth",
            "queue_id_at_head", "recent_completed", "runner_version",
        ):
            val = hb.get(key)
            if val is not None:
                entry[key] = val
        if hb.get("gpu"):
            entry["gpu"] = hb["gpu"]
        if hb.get("runner_pid") is not None:
            entry["runner_pid"] = hb["runner_pid"]
        entry["has_heartbeat"] = True
    if st:
        if st.get("runner_pid") is not None and entry.get("runner_pid") is None:
            entry["runner_pid"] = st.get("runner_pid")
        entry["status_idle"] = st.get("idle")
        entry["status_current"] = st.get("current")
        entry["status_last_updated"] = st.get("last_updated")
        entry["has_status"] = True



# See the ROLE-AWARE FRESHNESS note below: a metaworker box ticks every 5
# minutes and its heartbeat arrives here via git commit + push + pull, so the
# runner-sized 180s window would render a healthy orchestrator permanently
# STALE -- telemetry that reads as broken when the machine is fine.
ORCHESTRATOR_FRESH_WINDOW_SECONDS = 1200

def _machine_entry_from_git(name: str, hb: dict, st: dict, now,
                            fresh_window: int,
                            display_window: int) -> dict:
    """One machines-row built solely from git-synced heartbeat/status files.

    `name` is already a CANONICAL identity -- read_machines() merges the raw
    telemetry keys before calling here, so this never sees `DLAPTOP-5.local`.
    """
    last_tick = hb.get("last_tick_utc") or st.get("last_updated") or ""
    age_seconds = _utc_age_seconds(last_tick, now)

    # ROLE-AWARE FRESHNESS. The default windows are sized for a RUNNER, which
    # ticks every 60s (180s = 3 missed ticks). A metaworker box ticks every 5
    # MINUTES, and its heartbeat only reaches this checkout via a git commit +
    # push + pull -- so a perfectly healthy orchestrator is essentially never
    # under 180s old, and would render permanently STALE. That is the failure
    # mode this codebase already warns about elsewhere: telemetry that reads as
    # broken when the machine is fine trains people to ignore the panel.
    #
    # 20 min covers 3 missed 5-minute dispatch ticks plus git propagation; it is
    # deliberately far tighter than cloud-scaler.py's ORCHESTRATOR_FRESH_MIN
    # (50), because that number gates POWERING OFF A BOX and must tolerate the
    # writer's 30-minute liveness floor, whereas this one only colours a dot.
    if (hb.get("role") or "runner") == "orchestrator":
        fresh_window = max(fresh_window, ORCHESTRATOR_FRESH_WINDOW_SECONDS)
        display_window = max(display_window, ORCHESTRATOR_FRESH_WINDOW_SECONDS)

    fresh = (
        age_seconds is not None
        and 0 <= age_seconds <= fresh_window)
    display_fresh = (
        age_seconds is not None
        and 0 <= age_seconds <= display_window)
    entry = {
        "machine": name,
        # Overwritten by _hostname_fields below whenever the heartbeat carries a
        # hostname; the literal is what a status-only machine (no heartbeat)
        # keeps.
        "hostname": None,
        "last_tick_utc": last_tick,
        "age_seconds": age_seconds,
        "fresh": fresh,
        "display_fresh": display_fresh,
        "state": hb.get("state", "unknown" if not hb else "idle"),
        # "role" distinguishes a Phase H /loop metaworker-dispatch box (no
        # experiments, no coordinator client -- it will never appear in
        # coord_snaps, so this git-only path is the only one it ever takes)
        # from a normal experiment runner. Absent/omitted reads as "runner"
        # for every heartbeat written before this field existed.
        "role": hb.get("role", "runner"),
        "current_exq": hb.get("current_exq"),
        "current_exq_started_utc": hb.get("current_exq_started_utc"),
        "current_title": hb.get("current_title"),
        "current_claim_id": hb.get("current_claim_id"),
        "current_description": hb.get("current_description"),
        "progress": hb.get("progress"),
        "seconds_elapsed": hb.get("seconds_elapsed"),
        "seconds_remaining": hb.get("seconds_remaining"),
        "recent_lines": hb.get("recent_lines", []),
        "queue_depth": hb.get("queue_depth"),
        "queue_id_at_head": hb.get("queue_id_at_head"),
        "recent_completed": hb.get("recent_completed", []),
        "gpu": hb.get("gpu", {}),
        "runner_pid": hb.get("runner_pid") or st.get("runner_pid"),
        "runner_version": hb.get("runner_version"),
        "status_idle": st.get("idle"),
        "status_current": st.get("current"),
        "status_last_updated": st.get("last_updated"),
        "has_heartbeat": bool(hb),
        "has_status": bool(st),
        "telemetry_source": "git",
        # Orchestrator-role fields (role: "orchestrator"). None for a runner
        # heartbeat, since .get() has no default here -- machines.html only
        # reads these when it has already branched on role == "orchestrator".
        "cycles_completed": hb.get("cycles_completed"),
        "chips_dispatched_total": hb.get("chips_dispatched_total"),
        "chips_open_work": hb.get("chips_open_work"),
        "chips_open_decision": hb.get("chips_open_decision"),
        # `state` says what the dispatch wrapper DECIDED; `health` says what
        # came of it. Read health. `state` is written around the claude
        # invocation, so it attests only that the timer fired -- confirmed
        # 2026-08-19, ree-cloud-5 published state="dispatching" with a tick
        # fresh to the minute for ~12h while every cycle died on a usage limit.
        # See runner_heartbeats/README.md for the value table (note that
        # health=="idle" is HEALTHY and must not be rendered as an alarm).
        # Absent on a pre-2026-08-19 heartbeat, hence no default, same as the
        # rest of this block.
        "health": hb.get("health"),
        "health_reason": hb.get("health_reason"),
        "no_dispatch_streak": hb.get("no_dispatch_streak"),
        "session_outcome": hb.get("session_outcome"),
        "eligible_work": hb.get("eligible_work"),
        "dispatched_this_cycle": hb.get("dispatched_this_cycle"),
        "in_flight_dispatches": hb.get("in_flight_dispatches"),
        "last_dispatch_chip_ref": hb.get("last_dispatch_chip_ref"),
        "coordination_plane_paused": hb.get("coordination_plane_paused"),
        "last_cycle_note": hb.get("last_cycle_note"),
    }
    entry.update(_hostname_fields(hb))
    return entry


def _entry_from_coordinator_snapshot(name: str, snap: dict, now,
                                     fresh_window: int,
                                     display_window: int) -> dict:
    """Build a /api/machines row for a host only visible on the coordinator."""
    coord_age = _utc_age_seconds(snap.get("last_tick_utc") or "", now)
    coord_fresh = (
        coord_age is not None and 0 <= coord_age <= fresh_window)
    display_fresh = (
        coord_age is not None and 0 <= coord_age <= display_window)
    return {
        "machine": name,
        "hostname": None,
        "last_tick_utc": snap.get("last_tick_utc") or "",
        "age_seconds": coord_age,
        "fresh": coord_fresh,
        "display_fresh": display_fresh,
        "state": snap.get("state") or "unknown",
        "current_exq": snap.get("current_exq"),
        "current_exq_started_utc": None,
        "current_title": None,
        "current_claim_id": None,
        "current_description": None,
        "progress": snap.get("progress") or {},
        "seconds_elapsed": snap.get("seconds_elapsed"),
        "seconds_remaining": snap.get("seconds_remaining"),
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

    Rows are keyed by CANONICAL machine identity, never by the raw reported
    hostname: telemetry filenames outlive the name the box reports (the Phase-3
    writer materialises `runner_heartbeats/<machine>.json` from the coordinator
    DB and never deletes a superseded one), so a laptop whose LocalHostName was
    re-suffixed leaves a file behind under each spelling. Keyed raw, that is one
    physical machine rendered as two cards -- the stale one ageing into a card
    that reads as a dead box.
    """
    from datetime import datetime, timezone

    FRESH_WINDOW_SECONDS = 180
    # Explorer + Coordination panel: show live telemetry up to 10m.
    DISPLAY_FRESH_SECONDS = 600

    heartbeats: dict[str, dict] = {}
    if HEARTBEAT_DIR.is_dir():
        for f in sorted(HEARTBEAT_DIR.glob("*.json")):
            try:
                hb = json.loads(f.read_text())
                key = hb.get("machine") or f.stem
                heartbeats[key] = hb
            except Exception:
                pass
    heartbeats = _merge_by_canonical_machine(heartbeats, "last_tick_utc")

    statuses: dict[str, dict] = {}
    if STATUS_DIR.is_dir():
        for f in sorted(STATUS_DIR.glob("*.json")):
            try:
                statuses[f.stem] = json.loads(f.read_text())
            except Exception:
                pass
    statuses = _merge_by_canonical_machine(statuses, "last_updated")

    all_machines = set(heartbeats.keys()) | set(statuses.keys())
    now = datetime.now(timezone.utc)

    cfg = _load_coordinator_cfg()
    coord_url = (cfg.get("COORDINATOR_URL") or "").rstrip("/")
    coord_tok = cfg.get("COORDINATOR_LOCAL_TOKEN") or ""
    coordinator_configured = bool(coord_url and coord_tok)
    coord_snaps = (
        _fetch_coordinator_machine_snapshots(cfg)
        if coordinator_configured else {})

    # Phase 3: one timing authority. When the hub is configured, fleet rows
    # come from coordinator /shadow/status (same as the Coordination panel).
    # Git heartbeats only enrich recent_lines / titles / gpu -- never age.
    if coordinator_configured and coord_snaps:
        telemetry_mode = "coordinator"
        out_machines = []
        for name in sorted(coord_snaps.keys()):
            entry = _entry_from_coordinator_snapshot(
                name, coord_snaps[name], now,
                FRESH_WINDOW_SECONDS, DISPLAY_FRESH_SECONDS)
            _enrich_machine_from_git(
                entry, heartbeats.get(name, {}), statuses.get(name, {}))
            out_machines.append(entry)
        for name in sorted(all_machines - set(coord_snaps.keys())):
            out_machines.append(_machine_entry_from_git(
                name, heartbeats.get(name, {}), statuses.get(name, {}),
                now, FRESH_WINDOW_SECONDS, DISPLAY_FRESH_SECONDS))
    else:
        telemetry_mode = "git"
        out_machines = [
            _machine_entry_from_git(
                name, heartbeats.get(name, {}), statuses.get(name, {}),
                now, FRESH_WINDOW_SECONDS, DISPLAY_FRESH_SECONDS)
            for name in sorted(all_machines)
        ]

    # Exclude machines whose last heartbeat is older than the stale TTL.
    # Default 6h matches the claim stale-cutoff; override with
    # MACHINE_STALE_EXCLUDE_HOURS env var.  age_seconds=None (no timestamp
    # recorded) is kept so newly-provisioned machines are still visible.
    STALE_EXCLUDE_SECONDS = (
        float(os.environ.get("MACHINE_STALE_EXCLUDE_HOURS", "6")) * 3600
    )
    out_machines = [
        m for m in out_machines
        if m.get("age_seconds") is None
        or m["age_seconds"] <= STALE_EXCLUDE_SECONDS
    ]

    # Git-only rows (no hub row): mark display_stale when mirror is old.
    for m in out_machines:
        if m.get("telemetry_source") != "git":
            continue
        if m.get("display_fresh") is not False:
            continue
        if m.get("age_seconds") is None:
            continue
        if m.get("current_exq") or m.get("state") == "running":
            m["display_stale"] = True
            m["last_known_exq"] = m.get("current_exq")
        m["state"] = "stale"

    return {
        "schema_version": "v1",
        "now_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fresh_window_seconds": FRESH_WINDOW_SECONDS,
        "display_fresh_seconds": DISPLAY_FRESH_SECONDS,
        "stale_exclude_seconds": STALE_EXCLUDE_SECONDS,
        "telemetry_mode": telemetry_mode,
        "coordinator_overlay": telemetry_mode == "coordinator",
        "machines": out_machines,
    }


# ── Closure plan parsing ────────────────────────────────────────────────────

# Plans we know about; entries here without frontmatter still appear as
# placeholder cards in the Closure tab so the user knows they exist but
# haven't been retrofitted yet.
CLOSURE_KNOWN_PLANS = [
    "arc_062_rule_apprehension_plan.md",
    "commitment_closure_plan.md",
    "infant_substrate_plan.md",
    "goal_pipeline_plan.md",
    "self_attribution_plan.md",
    "sd033_governance_plan.md",
    "sleep_substrate_plan.md",
    "sd_037_axis_a_consumer_input_recalibration_plan.md",
    "sd_037_axis_b_sustained_threat_curriculum_plan.md",
    # --- V4/V5 forward-roadmap plans (generation: v4|v5; segmented out of the
    # V3 closure % by read_closure). See evidence/planning/*_v4_plan.md ---
    "object_representation_v4_plan.md",
    "self_model_v4_plan.md",
    "inference_belief_state_v4_plan.md",
    "object_reasoning_abstraction_v4_plan.md",
    "goal_deliberation_v4_plan.md",
    "hippocampal_planning_v4_plan.md",
    "affect_expression_v4_plan.md",
    "autobiographical_memory_v4_plan.md",
    "memory_lifecycle_v4_plan.md",
    "developmental_dmn_v4_plan.md",
    "drives_motivation_v4_plan.md",
    "perceptual_adaptors_v4_plan.md",
    "plasticity_neuromodulation_v4_plan.md",
    "biology_grounding_convergence_v4_plan.md",
    # V5 (social-mind) tier
    "multi_agent_ecology_v5_plan.md",
    "mirror_modelling_other_self_v5_plan.md",
    "fast_empathy_v5_plan.md",
    "relational_harm_moral_semantics_v5_plan.md",
    "ethics_as_coherence_v5_plan.md",
    "loveability_ethical_agency_v5_plan.md",
    # V6 (linguistic-mind) tier
    "language_emergence_bootstrap_v6_plan.md",
    "grammar_primitive_mining_v6_plan.md",
    "language_affect_adaptor_v6_plan.md",
    "abstract_relational_reasoning_v6_plan.md",
    "language_trust_deception_institutions_v6_plan.md",
    # Clinical lane (generation: clinical; excluded from the V3 closure % like
    # every other non-v3 lane). Psychiatric failure modes are CLINICAL objects,
    # not a version: a single syndrome's claims are spread across generations by
    # construction (catatonia subtype II = SD-036 v3 + MECH-214/215 v4), so
    # filing the programme by generation splits every syndrome in half. It is
    # also not `governance` (that is the SENT-*/GOV-* ethics perimeter), not
    # `process` (infrastructure owning no science), and not `deferred` (nothing
    # here is parked by commitment -- it is untested, which is the opposite).
    "psychiatric_failure_modes_plan.md",
    # Deferred-by-commitment parking lot (generation: deferred; excluded from
    # every generation %; nodes carry reversal triggers)
    "deferred_by_commitment_plan.md",
]

# Canonical closure-status weight map -- the SINGLE SOURCE OF TRUTH shared with
# scripts/generate_closure_snapshot.py (which imports this constant so the live
# map and the static snapshot can never report different %). None == excluded
# from the progress denominator (deferred work is not part of "what closes v3").
# upstream_blocked / blocked_pending_substrate are blocked variants (serve.py
# already colours them as blocked), so they carry the same 0.1 partial credit;
# pending_governance_stamp is work done-but-awaiting-a-stamp (0.4).
CLOSURE_STATUS_WEIGHTS = {
    "done": 1.0,
    "partial": 0.5,
    "in_progress": 0.4,
    "in-progress": 0.4,
    "blocked": 0.1,
    "upstream_blocked": 0.1,
    "blocked_pending_substrate": 0.1,
    "tracked": 0.2,
    "pending_governance_stamp": 0.4,
    "open": 0.0,
    # `pending`: not yet started (derived_evidence_index_plan.md's phase gates) --
    # same treatment as `open`.
    "pending": 0.0,
    # `assembling` / `open_by_design`: the node is REQUIRED for v3 and actively
    # (or intentionally) under construction -- substrate being built, not a
    # stalled gap. Weight None == excluded from the closure-% denominator so it
    # never PUNISHES the green-board for correct, unhurried assembly. Unlike
    # `deferred` (which is "not part of v3 closure"), an assembling node is part
    # of closure but is surfaced on a SEPARATE "assembly frontier" axis rather
    # than dragging the % toward red. See evidence/planning/assembly_vs_closure_plan.md.
    "assembling": None,
    "open_by_design": None,
    "deferred": None,   # excluded from progress denominator
    "deferred V4": None,
    "deferred_v4": None,
    "deferred_v5": None,
    # `parked` / `parked_indefinite` (pack_writer_single_writer_migration_plan.md
    # STEP-7.1/7.2): a considered decision to shelve, revisit only if a concrete
    # need appears -- same "not required right now" shape as `deferred`, so it
    # gets the same None (excluded, not scored as still-outstanding `open` work).
    "parked": None,
    "parked_indefinite": None,
    # `closed`: found without a weight entry 2026-08-13 -- was silently falling
    # through STATUS_WEIGHTS.get(st, 0.0) and being scored as `open` (unstarted),
    # the opposite of its meaning. Used across several V4/V5/process plans for a
    # terminal decision that is NOT a build outcome (see
    # substrate_stability_and_drift_detection_plan.md STEP P1f-more-gate-idioms'
    # own completion_note: "status=closed is this plan's closest existing enum
    # value to ... 'will not build' (a deliberate terminal decision, not a build
    # outcome, so 'done' would misrepresent it)"). None (excluded from the
    # denominator), matching `deferred`/`parked` rather than crediting it as
    # `done` -- the node authors explicitly avoided `done` on purpose.
    "closed": None,
}

# Default generation for a plan/node that HAS closure_plan frontmatter but does
# not declare a `generation`. The V3 closure map predates the `generation` field,
# so any such plan is V3 by definition -- this keeps the V3 closure % bit-identical
# after V4/V5 plans land. 16 plan docs relied on this as of 2026-09-02; do not
# change it without expecting the headline V3 closure % to move.
CLOSURE_DEFAULT_GENERATION = "v3"

# Generation for a plan doc with NO closure_plan frontmatter AT ALL (i.e.
# `_parse_plan_frontmatter` returned None). This is deliberately NOT
# CLOSURE_DEFAULT_GENERATION: the default above is backward compatibility with a
# filing decision made before the field existed, whereas a doc with no
# frontmatter has had NO filing decision made about it -- there is nothing to be
# backward-compatible with. Collapsing the two put
# `preservation_snapshot_plan.md` in the headline V3 closure map for 19 days
# (created 2026-08-14, found by the user 2026-09-02, one-off fix a5dd9112b6):
# the worst possible default, since the V3 view is the one everybody reads.
# These plans contribute zero nodes, so this only ever moves an empty
# placeholder card out of V3 and into a bucket that names the problem.
CLOSURE_UNFILED_GENERATION = "unfiled"

PENDING_REVIEW_FILE = SERVE_DIR / "evidence" / "experiments" / "pending_review.md"
REE_V3_QUEUE_FILE = SERVE_DIR.parent / "ree-v3" / "experiment_queue.json"
SUBSTRATE_QUEUE_FILE = PLANNING_DIR / "substrate_queue.json"
CLOSURE_DRIFT_JSON = PLANNING_DIR / "closure_drift.json"
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


_BRAIN_REGION_MAP_CACHE: dict = {"key": None, "doc": {}}


def _brain_load_region_map() -> dict:
    """Region map from BRAIN_REGION_MAP_FILE. READ-ONLY; shared.

    mtime-keyed like _tl_load_claims(); this parse is 0.056s and, once claims.yaml
    is cached, is the dominant remaining cost of /api/brain-map (78% of a warm
    request as profiled 2026-07-18).
    """
    if not _YAML_OK:
        return {}
    try:
        st = BRAIN_REGION_MAP_FILE.stat()
    except OSError:
        _BRAIN_REGION_MAP_CACHE["key"] = None
        _BRAIN_REGION_MAP_CACHE["doc"] = {}
        return {}
    key = (st.st_mtime_ns, st.st_size)
    if _BRAIN_REGION_MAP_CACHE["key"] != key:
        try:
            raw = _yaml.safe_load(BRAIN_REGION_MAP_FILE.read_text(encoding="utf-8"))
            doc = raw if isinstance(raw, dict) else {}
        except Exception:
            doc = {}
        _BRAIN_REGION_MAP_CACHE["doc"] = doc
        _BRAIN_REGION_MAP_CACHE["key"] = key
    return _BRAIN_REGION_MAP_CACHE["doc"]


def _brain_load_claim_evidence() -> dict:
    # Derived read-model when built, else the JSON cache; see
    # _claim_rollup_for_serving(). READ-ONLY, shared.
    return _claim_rollup_for_serving()


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


# ---------------------------------------------------------------------------
# Region <-> experiment join (read-side only)
# ---------------------------------------------------------------------------
# Two panels, one index, both directions of the same join:
#
#   (A) /brain-map sidebar -- "which experiments recently touched this region"
#   (B) /api/experiment/detail -- "which regions did this run exercise"
#
# Join path, entirely from data the governance pipeline already produces:
#   claim_evidence.v1.json `entries` carry (claim_id, run_id, status, timestamp)
#   -> claims.yaml gives each claim its `subject`, whose first dotted component
#      is a subject prefix
#   -> brain_region_map.yaml co-locates each region's `subject_prefixes` with
#      that region's identity.
#
# Nothing here mutates a manifest, the region map, claim_evidence.v1.json or
# claims.yaml, and nothing here is under sync_daemon's write ownership.

_REGION_EXPERIMENTS_CACHE: dict = {"key": None, "index": None}

# Rows kept per region in the /api/brain-map payload. ~40 nodes x this, so it is
# a payload-size knob as much as a UI one; the sidebar renders the first 8 and
# expands to the rest, and `recent_experiments_total` always reports the truth.
_REGION_EXPERIMENTS_MAX_PER_REGION = 20

_EMPTY_REGION_EXPERIMENT_INDEX: dict = {
    "by_region": {},
    "totals": {},
    "claim_to_regions": {},
    "region_labels": {},
}


def _region_experiment_readable_ts(compact: str) -> str:
    """20260722T041239Z -> 2026-07-22T04:12:39Z. Passes anything else through."""
    s = str(compact or "")
    if len(s) == 16 and s[8] == "T" and s.endswith("Z"):
        return f"{s[0:4]}-{s[4:6]}-{s[6:8]}T{s[9:11]}:{s[11:13]}:{s[13:15]}Z"
    return s


def _region_experiment_manifest_url(experiment_type: str, run_id: str) -> str:
    """Served URL for a run's evidence manifest, or "" when it is not on disk.

    The indexer's run-pack layout (evidence/experiments/<experiment_type>/runs/
    <run_id>/manifest.json) resolves 1565/1565 of the experimental runs in
    claim_evidence.v1.json as of 2026-08-16, so it is the only shape probed
    here; a miss just drops the link rather than the row.
    """
    if not experiment_type or not run_id:
        return ""
    rel = f"evidence/experiments/{experiment_type}/runs/{run_id}/manifest.json"
    try:
        if not (SERVE_DIR / rel).is_file():
            return ""
    except OSError:
        return ""
    return "/" + rel


def _region_experiment_index() -> dict:
    """Both directions of the region <-> experiment join. READ-ONLY; shared.

    Returns a dict with:
      by_region        {region_id: [run row, newest first]}, capped per region
      totals           {region_id: total runs before the cap}
      claim_to_regions {claim_id: [region_id, ...]}
      region_labels    {region_id: {"label": str, "bucket": str}}

    Keyed on (mtime_ns, size) of brain_region_map.yaml, claim_evidence.v1.json
    and claims.yaml -- not a TTL -- for the same reason as
    _load_claim_evidence_claims(): a governance rebuild must be visible on the
    very next request. The returned dict is SHARED; treat it as read-only.

    Never raises. A missing region map, a missing or malformed
    claim_evidence.v1.json, or an unavailable PyYAML all degrade to the empty
    index, i.e. every panel renders as absent rather than breaking the page.
    """
    def _stat_key(p):
        try:
            st = p.stat()
        except OSError:
            return None
        return (st.st_mtime_ns, st.st_size)

    try:
        key = (
            _stat_key(BRAIN_REGION_MAP_FILE),
            _stat_key(_TL_CLAIM_EVIDENCE),
            _stat_key(_TL_CLAIMS_YAML),
        )
        if _REGION_EXPERIMENTS_CACHE["key"] == key and _REGION_EXPERIMENTS_CACHE["index"]:
            return _REGION_EXPERIMENTS_CACHE["index"]

        map_doc = _brain_load_region_map()
        claims_list = _tl_load_claims()
        if not map_doc or not claims_list:
            return _EMPTY_REGION_EXPERIMENT_INDEX

        prefix_to_node = _brain_prefix_index(map_doc)
        region_labels: dict = {}
        for bucket in ("regions", "engineering_nodes"):
            for node in map_doc.get(bucket) or []:
                nid = str(node.get("id") or "")
                if nid:
                    region_labels[nid] = {
                        "label": str(node.get("label") or nid),
                        "bucket": "region" if bucket == "regions" else "engineering",
                    }

        claim_to_regions: dict = {}
        for c in claims_list:
            cid = str(c.get("id") or "")
            sub = str(c.get("subject") or "")
            if not cid or not sub:
                continue
            nid = prefix_to_node.get(sub.split(".")[0])
            if nid:
                claim_to_regions[cid] = [nid]

        # The `entries` list is not carried by the shared claim_evidence loader
        # (which keeps only `claims`), so parse it here -- once per mtime change,
        # and distilled straight into the index rather than retained.
        try:
            data = json.loads(_TL_CLAIM_EVIDENCE.read_text(encoding="utf-8"))
            entries = data.get("entries") or []
        except Exception:
            entries = []
        if not isinstance(entries, list):
            entries = []

        by_run: dict = {}
        for e in entries:
            if not isinstance(e, dict):
                continue
            if str(e.get("source_type") or "") != "experimental":
                continue
            run_id = str(e.get("run_id") or "")
            cid = str(e.get("claim_id") or "")
            if not run_id or not cid:
                continue
            rec = by_run.get(run_id)
            if rec is None:
                rec = by_run[run_id] = {
                    "run_id": run_id,
                    "experiment_type": str(e.get("experiment_type") or ""),
                    "timestamp_utc": str(e.get("timestamp_utc") or ""),
                    "outcome": str(e.get("status") or ""),
                    "summary": "",
                    "claim_ids": [],
                }
            if cid not in rec["claim_ids"]:
                rec["claim_ids"].append(cid)
            if not rec["outcome"]:
                rec["outcome"] = str(e.get("status") or "")
            if not rec["summary"]:
                rec["summary"] = str(
                    e.get("interpretation_label") or e.get("confidence_rationale") or ""
                )[:160]

        by_region: dict = {}
        for rec in by_run.values():
            per_region: dict = {}
            for cid in rec["claim_ids"]:
                for nid in claim_to_regions.get(cid) or ():
                    per_region.setdefault(nid, []).append(cid)
            for nid, cids in per_region.items():
                by_region.setdefault(nid, []).append({
                    "run_id": rec["run_id"],
                    "experiment_type": rec["experiment_type"],
                    "timestamp_utc": rec["timestamp_utc"],
                    "completed_at": _region_experiment_readable_ts(rec["timestamp_utc"]),
                    "outcome": rec["outcome"],
                    "summary": rec["summary"],
                    "claim_ids": sorted(cids),
                })

        totals: dict = {}
        for nid, rows in by_region.items():
            rows.sort(key=lambda r: (r.get("timestamp_utc") or "", r.get("run_id") or ""), reverse=True)
            totals[nid] = len(rows)
            del rows[_REGION_EXPERIMENTS_MAX_PER_REGION:]
            for r in rows:
                r["manifest_url"] = _region_experiment_manifest_url(
                    r.get("experiment_type") or "", r.get("run_id") or ""
                )

        index = {
            "by_region": by_region,
            "totals": totals,
            "claim_to_regions": claim_to_regions,
            "region_labels": region_labels,
        }
        _REGION_EXPERIMENTS_CACHE["index"] = index
        _REGION_EXPERIMENTS_CACHE["key"] = key
        return index
    except Exception:
        return _EMPTY_REGION_EXPERIMENT_INDEX


def _regions_for_claim_ids(claim_ids) -> list[dict]:
    """Inverse join for panel (B): a run's claims -> the regions they map into.

    Takes the claim ids straight off the run's own manifest (claim_ids_tested /
    claim_ids), so a run too fresh to be in claim_evidence.v1.json still
    resolves. Ordered by claim_count desc then region_id. Never raises."""
    try:
        idx = _region_experiment_index()
        claim_to_regions = idx.get("claim_to_regions") or {}
        region_labels = idx.get("region_labels") or {}
        if not claim_to_regions:
            return []
        grouped: dict = {}
        for cid in claim_ids or []:
            cid = str(cid or "")
            if not cid:
                continue
            for nid in claim_to_regions.get(cid) or ():
                bucket = grouped.setdefault(nid, [])
                if cid not in bucket:
                    bucket.append(cid)
        out = []
        for nid, cids in grouped.items():
            meta = region_labels.get(nid) or {}
            out.append({
                "region_id": nid,
                "label": str(meta.get("label") or nid),
                "bucket": str(meta.get("bucket") or ""),
                "claim_ids": sorted(cids),
                "claim_count": len(cids),
            })
        out.sort(key=lambda r: (-r["claim_count"], r["region_id"]))
        return out
    except Exception:
        return []


def read_brain_map() -> dict:
    """Aggregate brain-region stats for /api/brain-map."""
    generated_at = _utc_now_compact()
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
    region_exp = _region_experiment_index()
    region_exp_by_region = region_exp.get("by_region") or {}
    region_exp_totals = region_exp.get("totals") or {}

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
            "recent_experiments": list(region_exp_by_region.get(nid) or []),
            "recent_experiments_total": int(region_exp_totals.get(nid) or 0),
        }

    regions = [enrich_node(n, "region") for n in (map_doc.get("regions") or [])]
    engineering = [enrich_node(n, "engineering") for n in (map_doc.get("engineering_nodes") or [])]

    # Centroids for pathway overlay (rough layout matching SVG viewBox)
    _CENTROIDS = {
        "hippocampus": [210, 360],
        "amygdala": [210, 330],
        "pfc": [198, 100],
        "cingulate": [210, 162],
        "basal_ganglia": [210, 228],
        "default_mode": [210, 206],
        "sleep": [210, 300],
        "thalamus": [210, 264],
        "pag": [210, 372],
        "neuromodulation": [210, 345],
        "astrocyte": [210, 262],
        "harm_stream": [318, 258],
        "respiratory": [210, 430],
        "motor": [262, 98],
        "tpj": [314, 150],
        "peripersonal_space": [74, 252],
        "visual_streams": [66, 346],
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


# ---------------------------------------------------------------------------
# Code Atlas -- ree-v3 Understand-Anything knowledge-graph reader
# ---------------------------------------------------------------------------
# Reads the nightly-refreshed graph from ../ree-v3/.ua/knowledge-graph.json
# (committed weekly to ree-v3 main so a fresh clone can also serve it) and
# projects it for the code_atlas.html panels. Read-only; never mutates.

CODE_ATLAS_GRAPH_PATH = SERVE_DIR.parent / "ree-v3" / ".ua" / "knowledge-graph.json"
CODE_ATLAS_META_PATH  = SERVE_DIR.parent / "ree-v3" / ".ua" / "meta.json"
CODE_ATLAS_GITHUB_REPO = "https://github.com/Latent-Fields/ree-v3"
_code_atlas_cache: dict = {"mtime": None, "payload": None}


def _code_atlas_github_link(rel_path: str, commit: str | None) -> str:
    if not rel_path:
        return ""
    ref = commit if commit else "main"
    return f"{CODE_ATLAS_GITHUB_REPO}/blob/{ref}/{rel_path}"


def _code_atlas_related_claims_index(graph_nodes: list) -> dict:
    """Map each source filePath -> related claim chips {claim_id, title, status}.

    The claim<->file join is architectural: docs/architecture/brain_region_map.yaml
    co-locates each region's subject_prefixes (-> claims via claim.subject) with its
    ree_core_paths / functional_analogs (-> source files). A file inherits a region's
    claims when it is either

      (a) a *specific* owner match -- named in the region's functional_analogs, or under
          a sub-path (contains '/') ree_core_path -- in which case ALL that region's
          claims attach; or
      (b) a *broad* bare-directory ree_core_path match (e.g. control_plane owns the whole
          heartbeat/ package), in which case a claim attaches ONLY if its text names a
          symbol defined in the file (class/function) or the file's stem. The symbol gate
          keeps package-level directory ownership from flooding every file in a package
          with the region's entire claim set.

    claim_evidence.v1.json carries no file paths (it indexes claim -> runs/entries only),
    so it is not consulted here. Never raises: any failure -- missing brain_region_map.yaml,
    missing claims.yaml, unavailable PyYAML -- degrades to an empty index, i.e. every node
    gets related_claims: []."""
    try:
        if not _YAML_OK:
            return {}
        map_doc = _brain_load_region_map()
        claims_list = _tl_load_claims()
        if not map_doc or not claims_list:
            return {}

        _norm_re = re.compile(r"[^a-z0-9]+")
        _camel_re = re.compile(r"(?<!^)(?=[A-Z])")

        def _norm(s) -> str:
            return _norm_re.sub(" ", str(s).lower()).strip()

        status_rank = {"stable": 0, "provisional": 1, "candidate": 2}

        # subject-prefix -> claim chip records; and normalized claim text for the gate.
        by_pref: dict = {}
        claim_text: dict = {}
        for c in claims_list:
            cid = str(c.get("id") or "")
            if not cid:
                continue
            sub = str(c.get("subject") or "")
            pref = sub.split(".")[0] if sub else ""
            if pref:
                by_pref.setdefault(pref, []).append({
                    "claim_id": cid,
                    "title": str(c.get("title") or ""),
                    "status": str(c.get("status") or ""),
                })
            claim_text[cid] = _norm(" ".join(str(c.get(k) or "") for k in (
                "title", "functional_restatement", "subject", "evidence_quality_note")))

        # filePath -> symbol tokens (class / function / method names defined in that file).
        sym_by_file: dict = {}
        for n in graph_nodes or []:
            fp = str(n.get("filePath") or "")
            if fp and str(n.get("type") or "") in ("class", "function", "method"):
                nm = str(n.get("name") or "")
                if nm:
                    sym_by_file.setdefault(fp, set()).add(nm)

        regions = list(map_doc.get("regions") or []) + list(map_doc.get("engineering_nodes") or [])

        def _needles(fp: str) -> set:
            rel = fp[len("ree_core/"):] if fp.startswith("ree_core/") else fp
            stem = rel.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            out = {_norm(stem), _norm(stem.replace("_", " "))}
            for s in sym_by_file.get(fp, ()):
                out.add(_norm(s))
                out.add(_norm(_camel_re.sub(" ", s)))
            return {n for n in out if len(n) >= 4}

        def _match(rel: str, region: dict):
            specific = broad = False
            for p in (region.get("functional_analogs") or []):
                p = str(p)
                if rel == p or rel.startswith(p.rstrip("/") + "/"):
                    specific = True
            for p in (region.get("ree_core_paths") or []):
                p = str(p)
                if rel == p or rel.startswith(p.rstrip("/") + "/"):
                    if "/" in p:
                        specific = True
                    else:
                        broad = True
            return specific, broad

        index: dict = {}
        file_paths = {str(n.get("filePath") or "") for n in (graph_nodes or []) if n.get("filePath")}
        for fp in file_paths:
            rel = fp[len("ree_core/"):] if fp.startswith("ree_core/") else fp
            needles = None
            picked: dict = {}
            for region in regions:
                specific, broad = _match(rel, region)
                if not (specific or broad):
                    continue
                for pref in (region.get("subject_prefixes") or []):
                    for rec in by_pref.get(str(pref), ()):
                        cid = rec["claim_id"]
                        if specific:
                            picked[cid] = rec
                        elif cid not in picked:
                            if needles is None:
                                needles = _needles(fp)
                            txt = claim_text.get(cid, "")
                            if any(nd in txt for nd in needles):
                                picked[cid] = rec
            if picked:
                index[fp] = sorted(
                    picked.values(),
                    key=lambda r: (status_rank.get(r["status"], 3), r["claim_id"]),
                )
        return index
    except Exception:
        return {}


def read_code_atlas() -> dict:
    """Return the ree-v3 code atlas payload for /api/code_atlas.

    Caches on the graph file's mtime so a nightly refresh is picked up
    without a server restart. Never raises: on missing / unreadable graph
    the payload carries an `error` and an empty `nodes`/`layers`/`tour`."""
    try:
        stat = CODE_ATLAS_GRAPH_PATH.stat()
    except FileNotFoundError:
        return {
            "schema_version": 1,
            "generated_at": _utc_now_compact(),
            "error": "ree-v3 knowledge-graph not found (expected at "
                     f"{CODE_ATLAS_GRAPH_PATH}). Run /understand /path/to/ree-v3 "
                     "or wait for the nightly refresh.",
            "project": {}, "nodes": [], "edges": [], "layers": [], "tour": [],
        }
    except Exception as exc:
        return {
            "schema_version": 1,
            "generated_at": _utc_now_compact(),
            "error": f"cannot stat knowledge-graph: {exc}",
            "project": {}, "nodes": [], "edges": [], "layers": [], "tour": [],
        }

    if _code_atlas_cache["mtime"] == stat.st_mtime_ns and _code_atlas_cache["payload"]:
        return _code_atlas_cache["payload"]

    try:
        graph = json.loads(CODE_ATLAS_GRAPH_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "schema_version": 1,
            "generated_at": _utc_now_compact(),
            "error": f"cannot parse knowledge-graph: {exc}",
            "project": {}, "nodes": [], "edges": [], "layers": [], "tour": [],
        }

    # Prefer the meta.json's committed hash (matches what's on origin/main);
    # fall back to project.gitCommitHash on the graph itself.
    commit = None
    try:
        meta = json.loads(CODE_ATLAS_META_PATH.read_text(encoding="utf-8"))
        commit = str(meta.get("gitCommitHash") or "").strip() or None
    except Exception:
        commit = None
    project = dict(graph.get("project") or {})
    if not commit:
        commit = str(project.get("gitCommitHash") or "").strip() or None

    # Project nodes: preserve id + type + name + filePath + summary + tags,
    # add a GitHub source link, drop heavier fields the page doesn't render
    # (languageNotes, complexity). Tags default to [] so the page never NPEs.
    #
    # Layers list file-level nodes only; propagate the file's layer to its
    # class/function children so a search click always shows a layer.
    id_to_layer: dict[str, str] = {}
    for L in (graph.get("layers") or []):
        for nid in (L.get("nodeIds") or []):
            id_to_layer[str(nid)] = str(L.get("name") or L.get("id") or "")
    # Build a filePath -> layer index over the layered file nodes so class /
    # function nodes on the same file inherit their parent's layer.
    file_id_by_path: dict[str, str] = {}
    for n in (graph.get("nodes") or []):
        rel = str(n.get("filePath") or "")
        if rel and str(n.get("type") or "") in ("file", "config", "document",
                                                "service", "pipeline", "table",
                                                "schema", "resource", "endpoint"):
            file_id_by_path.setdefault(rel, str(n.get("id") or ""))
    # filePath -> related claim chips (architectural claim<->file join; see helper).
    # Built here so it caches on the graph mtime alongside the payload; degrades to an
    # empty index (related_claims: []) if the region map / claims registry is absent.
    related_index = _code_atlas_related_claims_index(graph.get("nodes") or [])
    nodes_out: list[dict] = []
    for n in (graph.get("nodes") or []):
        nid = str(n.get("id") or "")
        rel = str(n.get("filePath") or "")
        layer = id_to_layer.get(nid, "")
        if not layer and rel:
            layer = id_to_layer.get(file_id_by_path.get(rel, ""), "")
        nodes_out.append({
            "id": nid,
            "type": str(n.get("type") or ""),
            "name": str(n.get("name") or nid),
            "filePath": rel,
            "summary": str(n.get("summary") or ""),
            "tags": list(n.get("tags") or []),
            "layer": layer,
            "githubUrl": _code_atlas_github_link(rel, commit) if rel else "",
            "related_claims": related_index.get(rel, []) if rel else [],
        })

    # Edges: keep every one -- 628 * ~140 chars ~= 90 KB, well under any
    # response budget, and the module-lookup panel walks them for the
    # neighborhood chip strip.
    edges_out: list[dict] = []
    for e in (graph.get("edges") or []):
        edges_out.append({
            "source": str(e.get("source") or ""),
            "target": str(e.get("target") or ""),
            "type": str(e.get("type") or ""),
        })

    layers_out: list[dict] = []
    for L in (graph.get("layers") or []):
        layers_out.append({
            "id": str(L.get("id") or ""),
            "name": str(L.get("name") or ""),
            "description": str(L.get("description") or ""),
            "nodeIds": [str(x) for x in (L.get("nodeIds") or [])],
        })

    tour_out: list[dict] = []
    for step in (graph.get("tour") or []):
        tour_out.append({
            "order": int(step.get("order") or 0),
            "title": str(step.get("title") or ""),
            "description": str(step.get("description") or ""),
            "nodeIds": [str(x) for x in (step.get("nodeIds") or [])],
        })
    tour_out.sort(key=lambda s: s["order"])

    payload = {
        "schema_version": 1,
        "generated_at": _utc_now_compact(),
        "project": {
            "name": str(project.get("name") or "ree-v3"),
            "description": str(project.get("description") or ""),
            "languages": list(project.get("languages") or []),
            "frameworks": list(project.get("frameworks") or []),
            "analyzedAt": str(project.get("analyzedAt") or ""),
            "gitCommitHash": commit or "",
            "githubRepo": CODE_ATLAS_GITHUB_REPO,
        },
        "counts": {
            "nodes": len(nodes_out),
            "edges": len(edges_out),
            "layers": len(layers_out),
            "tour_steps": len(tour_out),
        },
        "nodes": nodes_out,
        "edges": edges_out,
        "layers": layers_out,
        "tour": tour_out,
    }
    _code_atlas_cache["mtime"] = stat.st_mtime_ns
    _code_atlas_cache["payload"] = payload
    return payload


# --- Code Atlas cross-reference linkifier ------------------------------------
# Auto-links bare mentions of source files, class/method names, EXQ ids and
# claim ids in served Markdown prose (docs/roadmap.md + the doc-viewer) to the
# exact Code Atlas node / GitHub blob / claim view. Purely additive and a strict
# no-op when the atlas payload is unavailable -- it returns the input verbatim.
#
# Design (see the "Recommended path" of the source chip):
#   * Build three lookup indexes off the atlas payload, cached on the payload
#     object identity (read_code_atlas already caches the payload on graph mtime,
#     so a nightly refresh rebuilds these for free).
#   * A single re.sub pass over the text with a master regex whose FIRST
#     alternative matches "protected" spans (fenced code, inline code, HTML
#     tags, existing <a>...</a>, markdown links, HTML comments); those are
#     emitted verbatim so we never linkify inside code or double-wrap an anchor
#     (idempotent). Remaining alternatives match linkifiable tokens.
#
# The emitted anchor carries class="atlas-xref" and RAW href/label characters
# (no server-side entity-escaping). The doc viewer's client renderer escapes the
# whole string and then restores atlas-xref anchors verbatim, so a raw '&' in a
# GitHub search href round-trips to a valid '&amp;' in the DOM. Labels/titles are
# constrained to a safe character set so the round-trip is unambiguous.

REE_ASSEMBLY_GITHUB_REPO = "https://github.com/Latent-Fields/REE_assembly"

_atlas_link_index_cache: dict = {"key": None, "indexes": None}


def _code_atlas_link_indexes() -> dict:
    """Return {by_path, by_class} lookup indexes derived from the atlas payload.

    by_path : filePath (exact, repo-relative) -> node id of the FILE node.
    by_class: class-node name -> node id (first definition wins).

    Cached on the payload object's identity: read_code_atlas returns the same
    cached dict until the graph mtime changes, so we rebuild only on refresh.
    On an unavailable / errored payload the indexes are empty (linkifier no-op)."""
    payload = read_code_atlas()
    key = id(payload)
    if _atlas_link_index_cache["key"] == key and _atlas_link_index_cache["indexes"] is not None:
        return _atlas_link_index_cache["indexes"]

    by_path: dict[str, str] = {}
    by_class: dict[str, str] = {}
    _file_like = ("file", "config", "document", "service", "pipeline",
                  "table", "schema", "resource", "endpoint")
    for n in (payload.get("nodes") or []):
        nid = str(n.get("id") or "")
        if not nid:
            continue
        ntype = str(n.get("type") or "")
        rel = str(n.get("filePath") or "")
        if rel and ntype in _file_like:
            by_path.setdefault(rel, nid)
        if ntype == "class":
            by_class.setdefault(str(n.get("name") or ""), nid)
    by_class.pop("", None)

    indexes = {"by_path": by_path, "by_class": by_class,
               "commit": str((payload.get("project") or {}).get("gitCommitHash") or "")}
    _atlas_link_index_cache["key"] = key
    _atlas_link_index_cache["indexes"] = indexes
    return indexes


# Master scanner. Protected spans FIRST (ordered alternation -> first wins at
# each position), then linkifiable token classes. NOTE: this is deliberately NOT
# re.DOTALL -- only fenced blocks and HTML comments are allowed to span newlines
# (via explicit [\s\S]); inline code, anchors and markdown links are line-bounded
# (matching Markdown semantics and the client renderer, which processes one line
# at a time). A whole-document `[^`]+` that crossed newlines would let a single
# stray backtick desync inline-code pairing for the rest of the document. Token
# order matters: file paths and EXQ/claim ids are tried before the generic
# ClassName.method / bare-identifier alternatives.
_ATLAS_LINK_RE = re.compile(
    r"(?P<prot>"
    r"```[\s\S]*?```"                 # fenced code block (multi-line)
    r"|<!--[\s\S]*?-->"               # HTML comment (multi-line)
    r"|<a\b[^>]*>.*?</a>"             # existing anchor (idempotency guard)
    r"|<[^>]+>"                       # any other HTML tag / attribute soup
    r"|`[^`\n]+`"                     # inline code span (line-bounded)
    r"|\[[^\]\n]*\]\([^)\n]*\)"       # markdown [label](url) (line-bounded)
    r")"
    r"|(?P<path>\b(?:ree_core|coordinator|experiments)/[A-Za-z0-9_./-]+\.py)"
    r"|(?P<exq>\bV3-EXQ-\d+[a-z]?(?:-[A-Za-z0-9]+)?)"
    r"|(?P<claim>\b(?:MECH|ARC|INV|IMPL|SD|Q)-\d+[a-z]?)"
    r"|(?P<dotted>\b[A-Z][A-Za-z0-9_]{2,}\.[a-z_][A-Za-z0-9_]{2,})"
    r"|(?P<ident>\b[A-Z][A-Za-z0-9_]{2,})",
)

_ATLAS_TITLE_SAFE_RE = re.compile(r"[^A-Za-z0-9 :._/#-]+")
# A "distinctive" CamelCase transition (lower/digit -> upper) -- gates bare
# identifier linking so plain capitalized words (Handler, Status, IMPORTANT)
# are not linked even when they collide with an atlas class name.
_ATLAS_CAMEL_RE = re.compile(r"[a-z0-9][A-Z]")


def _atlas_safe_title(text: str) -> str:
    return _ATLAS_TITLE_SAFE_RE.sub(" ", str(text)).strip()[:120]


def _atlas_anchor(href: str, label: str, title: str) -> str:
    """Build an atlas-xref anchor. href/label are emitted RAW (see module note);
    title is sanitised to a safe charset. Labels here are always code
    identifiers / paths / ids, so they carry no HTML-special characters."""
    return (f'<a class="atlas-xref" href="{href}" '
            f'title="{_atlas_safe_title(title)}">{label}</a>')


def _atlas_node_href(node_id: str) -> str:
    from urllib.parse import quote
    return "/code-atlas?node=" + quote(node_id, safe="")


def linkify_code_atlas(text: str) -> str:
    """Return `text` with bare code/experiment/claim references wrapped in
    Code Atlas cross-reference anchors. Strict no-op (returns input verbatim) if
    the text is empty or the atlas payload is unavailable. Idempotent: existing
    <a>...</a> spans are protected, so re-running produces identical output."""
    if not text:
        return text
    try:
        idx = _code_atlas_link_indexes()
    except Exception:
        return text
    by_path = idx.get("by_path") or {}
    by_class = idx.get("by_class") or {}
    commit = idx.get("commit") or None
    # No-op when the atlas is empty: nothing to link file paths / classes to.
    # EXQ + claim ids are atlas-independent, but without any atlas signal we keep
    # the whole pass off so an unavailable atlas is a true verbatim no-op.
    if not by_path and not by_class:
        return text

    def _link_path(tok: str) -> str:
        nid = by_path.get(tok)
        if nid:
            return _atlas_anchor(_atlas_node_href(nid), tok, f"Code Atlas: {tok}")
        # Not an atlas node (e.g. experiments/*.py live outside the graph) --
        # fall back to the GitHub blob on ree-v3.
        gh = _code_atlas_github_link(tok, commit)
        if gh:
            return _atlas_anchor(gh, tok, f"GitHub: {tok}")
        return tok

    def _link_exq(tok: str) -> str:
        from urllib.parse import quote
        # No standalone experiment_detail page exists; land the reader on the
        # manifest via a GitHub code search over REE_assembly for the run-id stem.
        stem = tok.lower().replace("v3-exq-", "v3_exq_").split("-")[0]
        q = quote(f"repo:Latent-Fields/REE_assembly {stem}", safe="")
        href = f"https://github.com/search?q={q}&type=code"
        return _atlas_anchor(href, tok, f"Find manifest for {tok}")

    def _link_claim(tok: str) -> str:
        from urllib.parse import quote
        href = "/code-atlas?claim=" + quote(tok, safe="")
        return _atlas_anchor(href, tok, f"Code Atlas claim view: {tok}")

    def _link_dotted(tok: str) -> str:
        cls = tok.split(".", 1)[0]
        nid = by_class.get(cls)
        if nid:
            return _atlas_anchor(_atlas_node_href(nid), tok, f"Code Atlas: {cls}")
        return tok

    def _link_ident(tok: str) -> str:
        nid = by_class.get(tok)
        if nid and _ATLAS_CAMEL_RE.search(tok):
            return _atlas_anchor(_atlas_node_href(nid), tok, f"Code Atlas: {tok}")
        return tok

    def _repl(m: "re.Match") -> str:
        if m.lastgroup == "prot" or m.group("prot") is not None:
            return m.group(0)
        tok = m.group(0)
        if m.group("path") is not None:
            return _link_path(tok)
        if m.group("exq") is not None:
            return _link_exq(tok)
        if m.group("claim") is not None:
            return _link_claim(tok)
        if m.group("dotted") is not None:
            return _link_dotted(tok)
        if m.group("ident") is not None:
            return _link_ident(tok)
        return tok

    try:
        return _ATLAS_LINK_RE.sub(_repl, text)
    except Exception:
        return text


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
    return linkify_code_atlas(snippet)


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


def _closure_drift_map() -> dict[str, dict]:
    """Read the closure_drift.json sidecar (written by check_closure_drift.py).

    Returns node_id -> {kind, owner_exq, detail} so the map can mark a status
    pill whose recorded status the drift checker considers stale relative to the
    owner experiment's actual terminal state. 'drifted' = status non-terminal
    but owner_exq terminal (manifest/autopsy landed); 'stale_since' = a later
    owner_exq sibling reached terminal state, or a confirmed autopsy touching
    this node's claims post-dates its last_updated. Suppressed nodes are
    intentionally absent (legitimately non-terminal)."""
    out: dict[str, dict] = {}
    try:
        doc = json.loads(CLOSURE_DRIFT_JSON.read_text(encoding="utf-8"))
    except Exception:
        return out
    for f in doc.get("drifted") or []:
        nid = f.get("node_id")
        if not nid:
            continue
        sig = f.get("manifest") or f.get("autopsy") or "terminal evidence"
        out[nid] = {
            "kind": "drifted",
            "owner_exq": f.get("owner_exq"),
            "detail": (
                "Status is '" + str(f.get("node_status")) + "' but owner "
                + str(f.get("owner_exq")) + " has finished (" + str(sig)
                + "). The plan-doc status may be out of date."
            ),
        }
    for s in doc.get("stale_since") or []:
        nid = s.get("node_id")
        if not nid or nid in out:
            continue
        reasons = "; ".join(s.get("reasons") or []) or "newer evidence landed"
        out[nid] = {
            "kind": "stale_since",
            "owner_exq": s.get("owner_exq"),
            "detail": (
                "Status '" + str(s.get("node_status")) + "' may be stale: "
                + reasons + ". Last updated " + str(s.get("node_last_updated"))
                + "."
            ),
        }
    return out


def _closure_claim_ids_by_flag(flag_substr: str) -> set[str]:
    """Scan claims.yaml list items for a boolean flag or note substring."""
    try:
        text = _TL_CLAIMS_YAML.read_text(encoding="utf-8")
    except Exception:
        return set()
    out: set[str] = set()
    current_id: str | None = None
    # A `key: value` flag (e.g. "epistemic_category: substrate_ceiling") is matched
    # as a substring -- the colon is in the query string. A BARE boolean flag
    # (e.g. "pending_retest_after_substrate") must match an actual `<flag>: true`
    # assignment; otherwise prose mentions -- including explicit `=false` / `: false`
    # -- would over-fire the flag (the RETEST lozenge in particular). The old
    # `... or flag_substr in line` defeated the `: true` guard, so any mention
    # counted; this restores the intended boolean semantics.
    has_value = ":" in flag_substr
    for line in text.splitlines():
        m = re.match(r"^- id:\s*(\S+)", line)
        if m:
            current_id = m.group(1)
            continue
        if not (current_id and flag_substr in line):
            continue
        if has_value:
            out.add(current_id)
        elif re.search(rf"{re.escape(flag_substr)}:\s*true", line):
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


def _closure_resume_prompt(
    node: dict,
    plan_file: str,
    nodes_by_id: dict[str, dict],
) -> str:
    """Build a paste-ready Claude Code resume prompt for a READY closure node.

    Caller-gated on `_closure_is_ready_gap`: the node is open, actionable
    severity, and every `depends_on` is satisfied -- so a fresh session can
    make real progress rather than re-deriving a vacuous FAIL on a still
    blocked / still assembling node. Built entirely from fields already on the
    node record; wired to the CLAUDE.md session-startup + skill conventions so
    the pasted session lands correctly. ASCII-only (renders in a terminal once
    pasted).
    """
    nid = str(node.get("id") or "")
    plan_id = str(node.get("plan_id") or "")
    title = str(node.get("title") or nid)
    severity = str(node.get("severity") or "medium")
    phase = node.get("phase")
    resume_condition = str(node.get("resume_condition") or "").strip()
    blocking_on = str(node.get("blocking_on") or "").strip()
    unblocks = [str(c) for c in (node.get("unblocks_claims") or [])]
    owner_exq = str(node.get("owner_exq") or "").strip()

    # depends_on are all satisfied (the ready-gate guarantees it); list them
    # with status so the resuming session sees the lineage it builds on.
    deps: list[str] = []
    for dep in node.get("depends_on") or []:
        dep_n = nodes_by_id.get(str(dep))
        st = dep_n.get("status") if dep_n else "unknown"
        deps.append(f"{dep} [{st}]")

    plan_ref = (
        f"REE_assembly/evidence/planning/{plan_file}"
        if plan_file else f"the {plan_id} plan-of-record doc"
    )

    # Some node ids already embed the plan prefix (e.g. "<plan>:OBJ-2"); only
    # add it when absent so the label never doubles up.
    node_label = nid if (":" in nid or not plan_id) else f"{plan_id}:{nid}"

    head = f"Node: {nid}  status: {node.get('status')}  severity: {severity}"
    if phase:
        head += f"  phase: {phase}"

    lines = [
        f"Resume work on closure node {node_label} ({title}).",
        "",
        "Repo: /Users/dgolden/REE_Working -- read CLAUDE.md first, then",
        f"{plan_ref} (this node's plan-of-record; its frontmatter status",
        "table is the cross-session resume primitive).",
        "",
        head,
    ]
    if resume_condition:
        lines.append(f"Resume condition: {resume_condition}")
    if blocking_on:
        lines.append(f"Was blocking on: {blocking_on}")
    if deps:
        lines.append("Depends on (all satisfied): " + ", ".join(deps))
    if unblocks:
        lines.append("Unblocks claims: " + ", ".join(unblocks))
    if owner_exq:
        lines.append(f"Owner EXQ: {owner_exq}")
    lines += [
        "",
        "Before editing any file, write a TASK_CLAIMS.json claim (umbrella",
        "REE_Working). If this node needs an experiment, go through the",
        "/queue-experiment skill -- never hand-edit experiment_queue.json or",
        "the experiments/ dir directly. Land via /session-land when done.",
    ]
    return "\n".join(lines)


def _closure_retest_prompt(
    claim_id: str,
    claim_meta: dict | None,
    substrate_nodes: list[dict],
) -> str:
    """Build a paste-ready Claude Code prompt to re-test a claim flagged
    `pending_retest_after_substrate: true`.

    A claim earns this flag when its verdict was parked pending substrate work.
    The retest is only genuinely DUE once that substrate work has landed, which
    on the closure map is the moment the unblocking node turns `done`. The prompt
    therefore reports each unblocking node's current status and tells the
    resuming session to confirm the substrate is in place BEFORE re-running --
    a retest on still-open substrate just re-derives the same parked result.
    ASCII-only (renders in a terminal once pasted).
    """
    title = str((claim_meta or {}).get("title") or "").strip()
    status = str((claim_meta or {}).get("status") or "").strip()
    epistemic = str((claim_meta or {}).get("epistemic_category") or "").strip()

    # Substrate readiness: the retest is DUE only when every unblocking node is
    # done. Partition so the prompt can say "ready now" vs "not landed yet".
    done_st = ("done", "deferred", "deferred_v4")
    node_lines: list[str] = []
    all_done = bool(substrate_nodes)
    for sn in substrate_nodes:
        st = str(sn.get("status") or "unknown")
        if st not in done_st:
            all_done = False
        plan = str(sn.get("plan_id") or "").strip()
        nid = str(sn.get("id") or "?")
        label = f"{plan}:{nid}" if (plan and ":" not in nid) else nid
        node_lines.append(f"  - {label} [{st}] ({sn.get('title') or ''})".rstrip())

    head = f"Re-test claim {claim_id}"
    if title:
        head += f" -- {title}"

    lines = [
        head,
        "",
        "Repo: /Users/dgolden/REE_Working -- read CLAUDE.md first.",
        "",
        f"Claim {claim_id} is flagged pending_retest_after_substrate: true in",
        "REE_assembly/docs/claims/claims.yaml -- its verdict was parked until the",
        "enabling substrate landed. It must be re-tested now that the substrate",
        "work is (or is becoming) available.",
        "",
        f"Claim status: {status or 'unknown'}"
        + (f"  epistemic_category: {epistemic}" if epistemic else ""),
    ]
    if node_lines:
        lines += ["", "Unblocking closure node(s) -- the substrate this retest waits on:"]
        lines += node_lines
    lines += [""]
    if all_done:
        lines += [
            "Substrate readiness: the unblocking node(s) above are DONE -- the",
            "retest is DUE. Proceed.",
        ]
    else:
        lines += [
            "Substrate readiness: at least one unblocking node above is NOT done.",
            "The substrate may not be fully landed yet -- VERIFY the enabling",
            "mechanism is actually wired in ree-v3 ree_core before re-running, or",
            "the retest will just re-derive the parked result.",
        ]
    lines += [
        "",
        "Steps:",
        "1. Read the claim entry + its gate/depends_on in claims.yaml.",
        "2. Confirm the enabling substrate is implemented in ree-v3/ree_core.",
        "3. Write a TASK_CLAIMS.json claim (umbrella REE_Working) before editing.",
        "4. Author the retest via the /queue-experiment skill (never hand-edit",
        "   experiment_queue.json or the experiments/ dir). Tag claim_ids exactly",
        f"   to what is tested -- include {claim_id} only if the run gives it",
        "   interpretable signal.",
        "5. After it runs, /governance to apply the verdict and clear the",
        "   pending_retest_after_substrate flag. Land via /session-land.",
    ]
    return "\n".join(lines)


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


# Statuses that read as "actively / intentionally under construction" -- the
# MOVE-1 keystone assembly states. Kept in sync with ASSEMBLING_STATUSES in
# scripts/check_closure_drift.py and the None entries in CLOSURE_STATUS_WEIGHTS.
_ASSEMBLING_STATUSES = {"assembling", "open_by_design"}
# Statuses serve.py / closure.html already colour as blocked.
_BLOCKED_STATUSES = {"blocked", "upstream_blocked", "blocked_pending_substrate"}


def _assembly_node_summary(n: dict, revisit_due: bool = False) -> dict:
    """Compact node record for the maturity portfolio buckets / frontier list."""
    return {
        "id": n.get("id"),
        "title": n.get("title") or n.get("id"),
        "plan_id": n.get("plan_id"),
        "status": n.get("status"),
        "severity": n.get("severity"),
        "owner_exq": n.get("owner_exq"),
        "awaiting": n.get("awaiting"),
        "assembly_status": n.get("assembly_status"),
        "revisit_after": n.get("revisit_after"),
        "revisit_due": revisit_due,
    }


def _closure_assembly_view(nodes: list[dict]) -> dict:
    """Bucket V3 nodes by maturity / assembly-state for the portfolio altitude.

    The companion to the closure %: where the % answers "how much of v3 is
    adjudicated done", this answers "what is the assembly made of right now" --
    mature vs actively-building vs awaiting-construction vs genuinely-blocked vs
    still-to-do. Deferred-family nodes (weight None, NOT assembling) are parked
    out of v3 and excluded entirely. The assembly frontier (status `assembling`
    / `open_by_design`, MOVE-1) is surfaced both as its own buckets and as a
    flat `frontier` list carrying each node's `revisit_due` resume flag.

    Headline = TWO numbers, not one burndown: the closure % (adjudication
    health, computed elsewhere) AND assembly-frontier health (how many nodes are
    on the frontier and how many are overdue for a revisit).
    """
    today = datetime.datetime.now(datetime.UTC).date()

    def _revisit_due(node: dict) -> bool:
        raw = node.get("revisit_after")
        if not raw:
            return False
        try:
            d = datetime.date.fromisoformat(str(raw).strip())
        except Exception:
            return False
        return d <= today

    buckets: dict[str, list[dict]] = {
        "mature": [],
        "mid_construction": [],
        "awaiting_construction": [],
        "genuinely_blocked": [],
        "remaining": [],
    }
    frontier: list[dict] = []

    for n in nodes:
        if (n.get("generation") or CLOSURE_DEFAULT_GENERATION) != CLOSURE_DEFAULT_GENERATION:
            continue
        status = n.get("status") or "open"
        if status in _ASSEMBLING_STATUSES:
            due = _revisit_due(n)
            summ = _assembly_node_summary(n, due)
            frontier.append(summ)
            astate = str(n.get("assembly_status") or "").strip().lower()
            if astate == "in_progress":
                buckets["mid_construction"].append(summ)
            else:
                # queued / built / unset -> awaiting active construction
                buckets["awaiting_construction"].append(summ)
            continue
        if status == "done":
            buckets["mature"].append(_assembly_node_summary(n))
            continue
        if status in _BLOCKED_STATUSES:
            buckets["genuinely_blocked"].append(_assembly_node_summary(n))
            continue
        # Deferred-family (weight None, not assembling) is parked out of v3 --
        # not part of the assembly portfolio at all.
        if CLOSURE_STATUS_WEIGHTS.get(status, 0.0) is None:
            continue
        buckets["remaining"].append(_assembly_node_summary(n))

    revisit_due_count = sum(1 for f in frontier if f.get("revisit_due"))
    counts = {k: len(v) for k, v in buckets.items()}
    counts["frontier"] = len(frontier)
    counts["revisit_due"] = revisit_due_count
    return {
        "buckets": buckets,
        "counts": counts,
        "frontier": frontier,
        # The second headline number (the first is overall_progress / closure %).
        "frontier_health": {
            "frontier_count": len(frontier),
            "revisit_due_count": revisit_due_count,
            "in_progress": counts["mid_construction"],
            "awaiting": counts["awaiting_construction"],
        },
    }


# ── Claims-layer assembly maturity (MOVE-4 follow-on, 2026-06-22) ────────────
# Draw the SAME maturity buckets MOVE-4 draws over closure-plan nodes over the
# whole claims registry, by consolidating the 6 scattered substrate-blocked
# conventions (epistemic_category substrate_conditional / substrate_ceiling,
# v3_pending, implementation_phase>=v4, implementation_phase=v3, the pending_*
# booleans) into ONE canonical `assembly_state`. CANONICAL DERIVATION kept in
# sync with scripts/build_claims_json.py:resolve_assembly_state (one logic, a
# synced sibling -- MOVE-1 precedent). This is READ-ONLY portfolio reporting; it
# changes no governance dispatch.
_ASSEMBLY_STATES = {
    "mature", "enriching", "awaiting_substrate", "gated_v3",
    "deferred_future", "remaining", "parked", "blocked",
}
_ASSEMBLY_STATUS_VALUES = {"queued", "in_progress", "built"}
_CLAIM_INACTIVE_STATUSES = {"legacy", "superseded", "retired", "applied", "deprecated"}
_CLAIM_MATURE_STATUSES = {"active", "stable", "provisional"}
_CLAIM_BLOCKED_STATUSES = {"blocked", "upstream_blocked", "blocked_pending_substrate"}
_CLAIM_FUTURE_PHASES = {"v4", "v5", "v6", "post_v5", "post_v4"}


def _norm_claim_assembly_status_token(raw) -> "str | None":
    """Map a (messy, free-text) substrate_queue status blob to one of
    {built, in_progress, queued}. Synced with build_claims_json."""
    s = str(raw or "").strip().lower()
    if not s:
        return None
    head = ""
    for ch in s:
        if ch.isalnum() or ch == "_":
            head += ch
        else:
            break
    if head.startswith(("implemented", "validated", "landed", "done")):
        return "built"
    if "ceiling_lifted" in s or head.startswith("ceiling"):
        return "built"
    if head.startswith(("phase", "amend", "substrate")) or "pending_validation" in s:
        return "in_progress"
    return "queued"


def _build_substrate_claim_index() -> dict:
    """Reverse map {claim_id: {awaiting, assembly_status}} from
    substrate_queue.json. Most-advanced build state wins. Synced with
    build_claims_json.build_substrate_claim_index."""
    order = {"queued": 0, "in_progress": 1, "built": 2}
    out: dict = {}
    try:
        data = json.loads(SUBSTRATE_QUEUE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return out
    queue = data.get("queue", []) if isinstance(data, dict) else []
    for it in queue:
        if not isinstance(it, dict):
            continue
        sd_id = it.get("sd_id")
        astatus = (_norm_claim_assembly_status_token(it.get("implementation_status"))
                   or _norm_claim_assembly_status_token(it.get("status"))
                   or ("built" if it.get("ready") is True else "queued"))
        for cid in (it.get("unblocks_claims") or []):
            prev = out.get(cid)
            if prev is None or order[astatus] > order[prev["assembly_status"]]:
                out[cid] = {"awaiting": sd_id, "assembly_status": astatus}
    return out


def _resolve_claim_assembly_state(claim: dict, substrate_index: dict) -> tuple:
    """Return (assembly_state, awaiting, assembly_status, is_explicit).
    CANONICAL -- keep in sync with build_claims_json.resolve_assembly_state."""
    cid = str(claim.get("id") or "")
    status = str(claim.get("status", "") or "").strip().lower()
    epi = str(claim.get("epistemic_category", "") or "").strip().lower()
    phase = str(claim.get("implementation_phase", "") or "").strip().lower()
    v3p = bool(claim.get("v3_pending"))

    join = substrate_index.get(cid, {})
    awaiting = str(claim.get("awaiting", "") or "").strip() or str(join.get("awaiting") or "")
    explicit_astatus = str(claim.get("assembly_status", "") or "").strip().lower()
    if explicit_astatus in _ASSEMBLY_STATUS_VALUES:
        assembly_status = explicit_astatus
    else:
        assembly_status = join.get("assembly_status") or ""

    explicit_state = str(claim.get("assembly_state", "") or "").strip().lower()
    if explicit_state in _ASSEMBLY_STATES:
        return explicit_state, awaiting, assembly_status, True

    if status in _CLAIM_INACTIVE_STATUSES:
        state = "parked"
    elif status in _CLAIM_BLOCKED_STATUSES:
        state = "blocked"
    elif epi == "substrate_conditional":
        state = "awaiting_substrate"
    elif epi == "substrate_ceiling":
        state = "enriching"
    elif v3p:
        state = "gated_v3"
    elif phase in _CLAIM_FUTURE_PHASES:
        state = "deferred_future"
    elif status in _CLAIM_MATURE_STATUSES:
        state = "mature"
    elif phase == "v3":
        state = "gated_v3"
    else:
        state = "remaining"
    return state, awaiting, assembly_status, False


# Claim assembly_state -> the same five maturity buckets _closure_assembly_view
# uses over nodes. deferred_future + parked are excluded from the portfolio
# (parked out of v3, exactly like deferred closure nodes).
_CLAIM_STATE_TO_BUCKET = {
    "mature": "mature",
    "blocked": "genuinely_blocked",
    "remaining": "remaining",
    # enriching / awaiting_substrate / gated_v3 split by assembly_status below.
}
# The waiting-on-assembly states form the claims "assembly frontier".
_CLAIM_WAITING_STATES = {"enriching", "awaiting_substrate", "gated_v3"}


def _claims_assembly_view(claims: list, substrate_index: dict) -> dict:
    """Bucket the whole claims registry by maturity / assembly-state -- the
    claims-layer companion to _closure_assembly_view (which buckets closure-plan
    nodes). Same bucket schema so closure.html's renderAssembly can switch data
    sources via the nodes<->claims toggle. READ-ONLY portfolio reporting.

    The "frontier" here = claims actively under construction (assembly_status
    in_progress) plus any with a past revisit_after -- a bounded, meaningful set
    (not all ~400 waiting claims). frontier_health.frontier_count reports the
    full assembly backlog (all waiting states) as the second headline number.
    """
    today = datetime.datetime.now(datetime.UTC).date()

    def _revisit_due(claim: dict) -> bool:
        raw = claim.get("revisit_after")
        if not raw:
            return False
        try:
            return datetime.date.fromisoformat(str(raw).strip()) <= today
        except Exception:
            return False

    buckets: dict = {
        "mature": [], "mid_construction": [], "awaiting_construction": [],
        "genuinely_blocked": [], "remaining": [],
    }
    frontier: list = []
    waiting_total = 0
    state_counts: dict = {}

    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        state, awaiting, astatus, explicit = _resolve_claim_assembly_state(c, substrate_index)
        state_counts[state] = state_counts.get(state, 0) + 1
        if state in ("deferred_future", "parked"):
            continue  # parked out of the v3 portfolio (like deferred nodes)
        due = _revisit_due(c)
        summ = {
            "id": cid,
            "title": c.get("title") or cid,
            "status": c.get("status"),
            "assembly_state": state,
            "awaiting": awaiting or None,
            "assembly_status": astatus or None,
            "revisit_after": c.get("revisit_after"),
            "revisit_due": due,
        }
        if state in _CLAIM_WAITING_STATES:
            waiting_total += 1
            if astatus == "in_progress":
                buckets["mid_construction"].append(summ)
            else:
                buckets["awaiting_construction"].append(summ)
            if astatus == "in_progress" or due:
                frontier.append(summ)
        else:
            buckets[_CLAIM_STATE_TO_BUCKET[state]].append(summ)

    revisit_due_count = sum(1 for f in frontier if f.get("revisit_due"))
    counts = {k: len(v) for k, v in buckets.items()}
    counts["frontier"] = waiting_total
    counts["revisit_due"] = revisit_due_count
    return {
        "buckets": buckets,
        "counts": counts,
        "frontier": frontier,
        "state_counts": state_counts,
        "total_in_scope": sum(len(v) for v in buckets.values()),
        "frontier_health": {
            "frontier_count": waiting_total,
            "revisit_due_count": revisit_due_count,
            "in_progress": counts["mid_construction"],
            "awaiting": counts["awaiting_construction"],
        },
    }


def _cusp_substrate_ready_items(sq: dict) -> list[dict]:
    """Build the cusp rail's "substrate_ready" items from a parsed
    substrate_queue.json dict.

    Suppresses already-built entries using the canonical classifiers from
    generate_inter_governance_workset.py's `_substrate_ready_items()` --
    this site used to read only `implementation_status` (blank on the
    majority of entries; the real state lives in the free-text `status`
    field), which advertised already-built substrate as buildable-now work
    on the dashboard (17x over-count vs. `_substrate_ready_items()`,
    confirmed 2026-08-19). Delegating avoids re-implementing (and silently
    drifting from) the MECH-302 / FM2 / FM3 / FM4 fixes those classifiers
    carry. Falls back to this file's own `_norm_claim_assembly_status_token`
    (suppressing "built"/"in_progress") if the import fails, so a broken
    import degrades rather than reverting to the old no-fallback behaviour.
    """
    try:
        sys.path.insert(0, str(SERVE_DIR / "scripts"))
        import generate_inter_governance_workset as _igw  # noqa: WPS433

        def _already_built(item):
            return _igw._substrate_resolved(item) or _igw._substrate_implementation_complete(item)
    except Exception:
        def _already_built(item):
            token = (_norm_claim_assembly_status_token(item.get("implementation_status"))
                     or _norm_claim_assembly_status_token(item.get("status")))
            return token in ("built", "in_progress")
    out: list[dict] = []
    for item in sq.get("queue") or []:
        if not isinstance(item, dict) or not item.get("ready"):
            continue
        if _already_built(item):
            continue
        out.append({
            "kind": "substrate_ready",
            "label": item.get("sd_id") or item.get("title") or "?",
            "sd_id": item.get("sd_id"),
        })
    return out


def _enrich_closure_v2(data: dict) -> dict:
    """Add closure/v2 orientation, live EXQ, cusp rail, per-node flags."""
    nodes = data.get("nodes") or []
    nodes_by_id = {n["id"]: n for n in nodes if n.get("id")}
    live_exq_ids: set[str] = set()

    machines_view = read_machines()
    running_rows: list[dict] = []
    fresh_machines: set[str] = set()
    for m in machines_view.get("machines") or []:
        if m.get("fresh") and m.get("machine"):
            fresh_machines.add(str(m.get("machine")))
        exq = m.get("current_exq")
        if exq and m.get("fresh"):
            live_exq_ids.add(str(exq))
            running_rows.append({
                "queue_id": exq,
                "machine": m.get("machine"),
                "progress": m.get("progress") or {},
                "state": m.get("state"),
            })

    # A queue claim only counts as "live" when the claiming machine still has a
    # fresh heartbeat. Without this gate an orphaned claim -- runner crashed or
    # was shut down mid-run without releasing it, or a stale >6h claim the
    # coordinator never reaped -- keeps marking its node [LIVE] long after the
    # experiment has actually finished. That is the staleness the operator hit
    # (e.g. cloud-4 / V3-EXQ-591b: heartbeat dead, claim still on the queue item).
    queue_claimed = _closure_queue_claimed()
    for row in queue_claimed:
        qid = row.get("queue_id")
        mach = row.get("machine")
        if qid and mach and str(mach) in fresh_machines:
            live_exq_ids.add(str(qid))

    retest_ids = _closure_claim_ids_by_flag("pending_retest_after_substrate")
    # Claim metadata (title/status/category) + the node(s) that unblock each
    # retest claim, so the RETEST lozenge -- on a node card or a cusp chip -- can
    # carry a paste-ready Claude Code retest prompt. node_map is filled in the
    # badge loop below; retest_meta is read once here.
    retest_meta = {
        str(c.get("id")): c
        for c in _tl_load_claims()
        if str(c.get("id")) in retest_ids
    }
    retest_node_map: dict[str, list[dict]] = {}
    node_retest_cids: dict[str, list[str]] = {}
    ceil_ids = _closure_claim_ids_by_flag("epistemic_category: substrate_ceiling")
    # Governance epistemic facet: SENT-*/GOV-* ethics-perimeter claims carry
    # epistemic_category: governance_rule; a node that unblocks one is an ethics
    # gate. substrate_conditional rounds out the per-node epistemic_category
    # dominance order (governance_rule > substrate_ceiling > substrate_conditional).
    gov_ids = _closure_claim_ids_by_flag("epistemic_category: governance_rule")
    cond_ids = _closure_claim_ids_by_flag("epistemic_category: substrate_conditional")
    drift_map = _closure_drift_map()

    cusp_items: list[dict] = []
    for n in nodes:
        # Cusp rail is a V3-closure surface; do not surface V4/V5 roadmap nodes
        # as "ready gaps" on it (they would otherwise pollute the V3 view).
        if (n.get("generation") or CLOSURE_DEFAULT_GENERATION) != CLOSURE_DEFAULT_GENERATION:
            continue
        if _closure_is_ready_gap(n, nodes_by_id):
            cusp_items.append({
                "kind": "ready_gap",
                "label": n["id"],
                "gap_id": n["id"],
                "plan_id": n.get("plan_id"),
            })
    try:
        sq = json.loads(SUBSTRATE_QUEUE_FILE.read_text(encoding="utf-8"))
        cusp_items.extend(_cusp_substrate_ready_items(sq))
    except Exception:
        pass
    for cid in sorted(retest_ids)[:12]:
        cusp_items.append({
            "kind": "pending_retest",
            "label": cid,
            "claim_id": cid,
        })

    # plan_id -> source filename, for the per-node resume prompt's plan ref.
    plan_file_by_id = {
        p.get("id"): p.get("file") for p in (data.get("plans") or [])
    }

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
        unblocks = n.get("unblocks_claims") or []
        unblocks_gov = False
        for cid in unblocks:
            if cid in retest_ids:
                flags.append("pending_retest")
                if "RETEST" not in badges:
                    badges.append("RETEST")
                node_retest_cids.setdefault(str(n.get("id")), []).append(cid)
                retest_node_map.setdefault(cid, []).append({
                    "id": n.get("id"),
                    "plan_id": n.get("plan_id"),
                    "title": n.get("title"),
                    "status": n.get("status"),
                })
            if cid in ceil_ids:
                if "CEIL" not in badges:
                    badges.append("CEIL")
            if cid in gov_ids:
                unblocks_gov = True
        n["claim_flags"] = flags
        n["badges"] = badges

        # Governance / welfare epistemic facet (read by closure.html chips).
        #   epistemic_category: dominant flagged category of the claims this node
        #     unblocks, emitted only when derivable so an absent value reads as
        #     "standard" (the common case).
        #   is_governance: the node advances governance work -- it sits in a
        #     governance plan (substrate governance, e.g. sd033_governance) OR it
        #     unblocks a governance_rule ethics-perimeter claim.
        #   welfare_*: surfaced from the node's GOV-PROC-1 s2 ethical_metadata.
        if unblocks_gov:
            n["epistemic_category"] = "governance_rule"
            if "GOV" not in badges:
                badges.append("GOV")
        elif any(cid in ceil_ids for cid in unblocks):
            n["epistemic_category"] = "substrate_ceiling"
        elif any(cid in cond_ids for cid in unblocks):
            n["epistemic_category"] = "substrate_conditional"
        em = n.get("ethical_metadata") if isinstance(
            n.get("ethical_metadata"), dict) else {}
        welfare_relevance = str(em.get("welfare_relevance") or "none").strip().lower()
        requires_welfare_review = bool(em.get("requires_welfare_review"))
        n["welfare_relevance"] = welfare_relevance
        n["requires_welfare_review"] = requires_welfare_review
        n["applicable_ethics_gates"] = list(em.get("applicable_ethics_gates") or [])
        n["welfare_relevant"] = (
            requires_welfare_review
            or welfare_relevance in ("moderate", "high", "hard_review")
        )
        n["is_governance"] = (
            unblocks_gov
            or "governance" in str(n.get("plan_id") or "").lower()
            # the whole generation: governance tab IS the ethics-perimeter
            # governance layer, so every node in it is governance.
            or (n.get("generation") or CLOSURE_DEFAULT_GENERATION) == "governance"
        )
        n["drift"] = drift_map.get(n.get("id"))
        n["active_blocker_short"] = _closure_active_blocker_short(
            n, nodes_by_id)

        # resume_prompt: paste-ready Claude Code bootstrap, emitted ONLY for
        # ready gaps (open + actionable severity + all depends_on satisfied).
        # Its absence is the signal closure.html uses to NOT offer a copy
        # button on blocked / assembling / done nodes -- a resume prompt there
        # would invite a session that just re-derives a vacuous FAIL.
        if _closure_is_ready_gap(n, nodes_by_id):
            n["resume_prompt"] = _closure_resume_prompt(
                n, plan_file_by_id.get(n.get("plan_id")) or "", nodes_by_id)

    # retest_prompt: paste-ready Claude Code prompt to re-test a parked claim.
    # Built now that retest_node_map is complete (so each prompt can list ALL
    # nodes unblocking the claim, not just one). Attached to (a) every node
    # carrying a RETEST badge -- one prompt covering each retest claim it
    # unblocks -- and (b) every pending_retest cusp chip. Per-claim cache so a
    # claim unblocked by several nodes builds its prompt once.
    retest_prompt_by_claim: dict[str, str] = {}
    for cid in retest_ids:
        retest_prompt_by_claim[cid] = _closure_retest_prompt(
            cid, retest_meta.get(cid), retest_node_map.get(cid) or [])
    for n in nodes:
        cids = node_retest_cids.get(str(n.get("id")))
        if cids:
            n["retest_prompt"] = "\n\n----\n\n".join(
                retest_prompt_by_claim[c] for c in cids)
    for it in cusp_items:
        if it.get("kind") == "pending_retest":
            cid = it.get("claim_id")
            if cid in retest_prompt_by_claim:
                it["retest_prompt"] = retest_prompt_by_claim[cid]

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
    # Dual-progress (implementation vs evidence) is a V3-closure orientation bar;
    # compute it over V3 nodes only so V4/V5 roadmap nodes do not skew it.
    data["progress"] = _closure_dual_progress(
        [n for n in nodes
         if (n.get("generation") or CLOSURE_DEFAULT_GENERATION) == CLOSURE_DEFAULT_GENERATION]
    )
    # Assembly/maturity portfolio view (MOVE-4): the broad-overview altitude
    # parallel to the closure %. Computed over V3 nodes only (same scope as the
    # dual-progress bar) so V4/V5 roadmap nodes do not skew the buckets.
    data["assembly"] = _closure_assembly_view(
        [n for n in nodes
         if (n.get("generation") or CLOSURE_DEFAULT_GENERATION) == CLOSURE_DEFAULT_GENERATION]
    )
    # Claims-layer companion (MOVE-4 follow-on): the SAME maturity buckets over
    # the whole claims registry, consolidating the 6 substrate-blocked
    # conventions into one canonical assembly_state. Surfaced via the
    # nodes<->claims toggle on closure.html's Assembly maturity strip.
    data["claims_assembly"] = _claims_assembly_view(
        _tl_load_claims(), _build_substrate_claim_index())
    data["exq_live"] = {
        "running": running_rows,
        "queue_claimed": queue_claimed,
    }
    data["cusp_items"] = cusp_items[:30]
    data["contributory_exq_ids"] = sorted(contributory)
    return data



def _closure_shp_head(n: dict, cp_index: dict | None = None) -> dict:
    """status_history_plane (SHP-2) head projection for a closure node, flattened
    for the map overlay. Pulls the two-plane `live:` / `join:` blocks straight from
    the node frontmatter (same source read_status_history serves) and derives the
    convenience channels the closure map renders: needs_review (ambiguity ring),
    live_as_of (currency fade), brake (substrate-blocked badge), live_next (tooltip).
    `collapsed` is False for any node predating the SHP-2 collapse (no `live:`).

    `cp_index` (optional, from `_status_changepoints_index()`, built ONCE by the
    caller) supplies the compact `history_changepoints` channel the map draws as a
    per-node sparkline: {count, last_utc, points:[{utc,status,verdict}]}. CHANGE-ONLY
    log => 0-1 points is a STABLE node (flat baseline), never a broken/blank one."""
    live = n.get("live") if isinstance(n.get("live"), dict) else None
    join = n.get("join") if isinstance(n.get("join"), dict) else None
    # needs_review has two reason kinds (project_status_head.project_live +
    # _umbrella_children_disagree_pass): "umbrella_children_disagree:<verdicts>" is
    # a GENUINE head ambiguity (the map's prominent flag), while
    # "newest_forward_predates_later_<kinds>_event(s)" is collinear with the brake
    # (substrate_ceiling) + verdict channels the map already renders. Surface the
    # raw reasons AND a derived `needs_review_ambiguous` gate so the map can promote
    # only genuine ambiguity and soften the brake-collinear case.
    review_reasons = list(live.get("needs_review_reasons") or []) if live else []
    review_ambiguous = any(
        str(r).startswith("umbrella_children_disagree") for r in review_reasons)
    # Sparkline channel: the node's change-only status_projection timeline. Cap the
    # embedded point list (the tail, still oldest-first) so the payload stays small;
    # `count` keeps the honest total. Empty/short list == stable, not missing.
    nid = str(n.get("id") or "")
    cp_points = list(cp_index.get(nid, [])) if cp_index else []
    history_changepoints = {
        "count": len(cp_points),
        "last_utc": (cp_points[-1].get("utc") if cp_points else None),
        "points": cp_points[-12:],
    }
    out = {
        "collapsed": live is not None,
        "live": live,
        "join": join,
        "needs_review": bool(live.get("needs_review")) if live else False,
        "needs_review_reasons": review_reasons,
        "needs_review_ambiguous": review_ambiguous,
        "live_as_of": (live.get("as_of") if live else None),
        "live_from": (live.get("from") if live else None),
        "live_verdict": (live.get("verdict") if live else None),
        "live_next": (live.get("next") if live else None),
        "brake": (str(live.get("brake")) if live and live.get("brake") is not None else None),
        # bears_on / scope_claims surfaced for the node<->claim / node<->event edges
        "bears_on": list(join.get("bears_on") or []) if join else [],
        "join_scope_claims": list(join.get("scope_claims") or []) if join else [],
        "history_changepoints": history_changepoints,
    }
    return out


def read_closure() -> dict:
    """Aggregate closure_plan frontmatter across planning/*_plan.md docs."""
    plans: list[dict] = []
    nodes_by_id: dict[str, dict] = {}
    edges: list[dict] = []
    cross_links: list[dict] = []

    seen_files: set[str] = set()

    # Build the per-node change-point index ONCE (reads the append-only status log a
    # single time) so _closure_shp_head can attach each node's sparkline timeline
    # without re-scanning the log per node.
    cp_index = _status_changepoints_index()

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
            # No closure_plan frontmatter at all -> UNFILED, not V3. See the
            # CLOSURE_UNFILED_GENERATION comment: an explicit generation here is
            # what stops an unfiled plan from silently defaulting into the
            # headline V3 closure map via the `or CLOSURE_DEFAULT_GENERATION`
            # fallbacks in the rollup below and in closure.html.
            plans.append({
                "id": fname.replace("_plan.md", ""),
                "title": fname.replace("_plan.md", "").replace("_", " ").title(),
                "file": fname,
                "generation": CLOSURE_UNFILED_GENERATION,
                "frontmatter_pending": True,
                "node_count": 0,
                "progress": 0.0,
            })
            continue

        plan_id = str(plan.get("id") or fname.replace("_plan.md", ""))
        generation = str(plan.get("generation") or CLOSURE_DEFAULT_GENERATION).strip().lower()
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
                "generation": generation,
                "title": n.get("title") or nid,
                "phase": n.get("phase"),
                "status": status,
                "severity": n.get("severity") or "medium",
                "owner_exq": n.get("owner_exq"),
                "unblocks_claims": list(n.get("unblocks_claims") or []),
                "depends_on": list(n.get("depends_on") or []),
                "cross_plan_link": list(n.get("cross_plan_link") or []),
                "blocking_external": list(n.get("blocking_external") or []),
                # readiness_gate: forward-roadmap (V4/V5) field listing the V3-era
                # prerequisites (claims/tracks) that gate this node. V3 closure
                # nodes leave it empty; passed through for the roadmap view.
                "readiness_gate": list(n.get("readiness_gate") or []),
                "last_updated": n.get("last_updated"),
                # resume_condition / blocking_on: free-text + structured fields
                # for distinguishing a node's CURRENT active blocker from its
                # static depends_on lineage. depends_on records phase order
                # (e.g. Phase 2 follows Phase 1) and does not flip back to
                # incomplete once a downstream node hits a new blocker.
                "resume_condition": n.get("resume_condition"),
                "blocking_on": n.get("blocking_on"),
                # ethical_metadata: the GOV-PROC-1 s2 carry-forward of the
                # deferred SENT-*/GOV-* ethics gates onto the roadmap node they
                # bite on (welfare_relevance / requires_welfare_review /
                # applicable_ethics_gates / forbidden_combinations). Passed
                # through verbatim so the governance/welfare epistemic facet can
                # surface it; absence == welfare_relevance: none (Class 0/1).
                "ethical_metadata": (
                    n.get("ethical_metadata")
                    if isinstance(n.get("ethical_metadata"), dict) else None
                ),
                # Assembly-frontier fields (MOVE-1 keystone). Passed through so
                # the maturity portfolio view (MOVE-4) can bucket a `status:
                # assembling` node by its build state and surface its resume
                # trigger. Absent on the vast majority of (non-assembling) nodes.
                "awaiting": n.get("awaiting"),
                "assembly_status": n.get("assembly_status"),
                "revisit_after": n.get("revisit_after"),
            }
            # status_history_plane (SHP-2) head overlay: live:/join: + derived
            # needs_review / currency / brake / next channels for the map.
            node_record.update(_closure_shp_head(n, cp_index))
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
            "generation": generation,
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

    # Per-generation weighted progress across non-deferred nodes. The top-level
    # overall_* fields report the V3 (CLOSURE_DEFAULT_GENERATION) generation ONLY,
    # so that V4/V5 forward-roadmap plans never dilute the V3 closure %. The
    # `generations` dict carries every generation's rollup for the segmented view.
    gen_acc: dict[str, dict] = {}
    for n in nodes_by_id.values():
        gen = n.get("generation") or CLOSURE_DEFAULT_GENERATION
        acc = gen_acc.setdefault(gen, {"done": 0.0, "total": 0.0, "plan_ids": set()})
        acc["plan_ids"].add(n.get("plan_id"))
        w = CLOSURE_STATUS_WEIGHTS.get(n["status"], 0.0)
        if w is not None:
            acc["total"] += 1.0
            acc["done"] += w
    # Ensure plans with zero non-deferred nodes (or zero nodes) still register
    # their generation bucket so the UI can offer an (empty) view.
    for p in plans:
        gen_acc.setdefault(
            p.get("generation") or CLOSURE_DEFAULT_GENERATION,
            {"done": 0.0, "total": 0.0, "plan_ids": set()},
        )["plan_ids"].add(p.get("id"))

    generations = {}
    for gen, acc in gen_acc.items():
        total = acc["total"]
        generations[gen] = {
            "progress": round((acc["done"] / total) if total > 0 else 0.0, 4),
            "node_done_weighted": round(acc["done"], 4),
            "node_total": int(total),
            "plan_count": len([pid for pid in acc["plan_ids"] if pid]),
        }

    v3 = generations.get(CLOSURE_DEFAULT_GENERATION, {
        "progress": 0.0, "node_done_weighted": 0.0, "node_total": 0,
    })

    return _enrich_closure_v2({
        "schema_version": "closure/v1",
        "generated_at": _utc_now_iso_z(),
        "plans": plans,
        "nodes": list(nodes_by_id.values()),
        "edges": edges,
        "cross_links": cross_links,
        # V3-only (preserves the historical closure % semantics)
        "overall_progress": v3["progress"],
        "node_total": v3["node_total"],
        "node_done_weighted": v3["node_done_weighted"],
        # per-generation rollups for the segmented roadmap view
        "generations": generations,
    })


# Scientific Progress Dashboard (Build/Prove/Narrow/Decide + momentum). The
# payload is DERIVED offline by scripts/build_hypothesis_space.py (derive-only,
# exits 0, runs in governance.sh); serve.py only reads the committed snapshot.
# This never re-weights closure -- Dimension 2 embeds read_closure() read-only.
PROGRESS_JSON_FILE = PLANNING_DIR / "hypothesis_space.v1.json"


def read_progress() -> dict:
    """Load the committed hypothesis_space.v1.json snapshot for /progress.

    Derive-only consumer: if the snapshot is missing/unreadable, return a
    friendly empty state pointing at the build script rather than erroring."""
    empty = {
        "schema_version": "hypothesis_space/v1",
        "generated_at": None,
        "empty": True,
        "empty_note": (
            "No hypothesis_space.v1.json yet. Run "
            "python scripts/build_hypothesis_space.py (or bash scripts/governance.sh)."
        ),
        "references": {"closure_map": "/closure"},
    }
    if not PROGRESS_JSON_FILE.exists():
        return empty
    try:
        data = json.loads(PROGRESS_JSON_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    empty["empty_note"] = "hypothesis_space.v1.json unreadable."
    return empty


def read_workset() -> dict:
    """Load inter-governance workset from generate_inter_governance_workset.py.

    A PARSE FAILURE IS REPORTED, NOT SWALLOWED. This used to return the empty
    stub for any exception, so an unreadable workset rendered as a page with
    zero packages and no error anywhere -- indistinguishable from "the
    generator has never run" and from "your filters match nothing". The
    realistic cause is a TORN READ: the generator rewrites this ~465 KB file
    while /workset polls this endpoint every 20s. That window is now closed at
    the source (generate_inter_governance_workset._atomic_write_text), so a
    parse failure here means either genuine corruption or a writer that has
    regressed to a non-atomic write -- both worth seeing.

    `unreadable: true` is the machine-readable signal; workset.html renders it
    as a banner instead of a muted empty-state. Deliberately NOT a 500 and
    deliberately NOT a cached last-good payload in this process: the page stays
    up, this read path stays stateless, and the client decides what to keep
    showing.

    One retry after a short delay, because a torn read is transient by nature
    and the retry costs ~50ms against a failure that would otherwise blank an
    open page for a whole refresh cycle.
    """
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
    last_err = None
    for attempt in range(2):
        if attempt:
            time.sleep(0.05)  # let a torn write land; see the docstring
        try:
            data = json.loads(WORKSET_JSON_FILE.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 -- reported below, never raised
            last_err = exc
            continue
        if not (isinstance(data, dict) and isinstance(data.get("items"), list)):
            last_err = ValueError(
                "parsed, but not an object with an 'items' list"
            )
            continue
        # Re-merge live agent assignments at read time. The generator bakes
        # `assignments` into the workset JSON, but assign/release POSTs only
        # write to evidence/planning/igw_assignments.json -- without this
        # merge, the UI shows stale assignments until the next generator run.
        try:
            sys.path.insert(0, str(SERVE_DIR / "scripts"))
            from igw_assignments_lib import (  # noqa: WPS433
                assignments_by_hash,
                stable_hash_item,
            )
            by_hash = assignments_by_hash()
            for it in data["items"]:
                sh = it.get("stable_hash") or stable_hash_item(it)
                it["stable_hash"] = sh
                it["assignments"] = by_hash.get(sh) or []
        except Exception:
            pass
        return data
    empty["unreadable"] = True
    empty["unreadable_detail"] = "%s: %s" % (type(last_err).__name__, last_err)
    empty["empty_note"] = (
        "Workset file unreadable -- %s could not be parsed (%s). "
        "The page is showing nothing because the READ failed, not because "
        "there is no work. Re-run scripts/generate_inter_governance_workset.py."
        % (WORKSET_JSON_FILE.name, empty["unreadable_detail"])
    )
    print("read_workset: %s unreadable: %s"
          % (WORKSET_JSON_FILE, empty["unreadable_detail"]), file=sys.stderr)
    return empty


def read_chips() -> dict:
    """Load the durable spawn_task/dismiss_task chip ledger (TASK_CHIPS.json).

    Read fresh on every call -- unlike the workset JSON, this file is not
    regenerated by a skill, it is appended to live by chip_ledger.py, so there
    is no staleness to guard against here.

    Status here reflects only what chip_ledger.py has been told: "open"
    (recorded, not withdrawn/done) or "withdrawn"/"done". It cannot see a
    human clicking the live chip in the UI -- that event never reaches any
    session's tool calls -- so "open" means "not known to be stale", not
    "definitely still unclicked". A chip's `claimed_by`/`claimed_at`/
    `claim_note` fields (added 2026-08-02, see chip_ledger.py's "CLAIMING"
    docstring section), when present on an `open` chip, mean a worker or
    session has already started it via `chip_ledger.py claim` -- distinct
    from status, which only ever reflects resolution, not in-progress work.
    """
    empty = {"schema_version": "task_chips/v1", "chips": [],
             "empty_note": "No TASK_CHIPS.json yet, or it is unreadable. "
                           "See scripts/chip_ledger.py."}
    if not TASK_CHIPS_FILE.exists():
        return empty
    try:
        data = json.loads(TASK_CHIPS_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("chips"), list):
            return data
    except Exception:
        pass
    return empty


# --- Chip ledger projection ---------------------------------------------------
#
# TASK_CHIPS.json is ~7 MB (1160+ chips) and its ONE consumer is the collapsed
# "Pending chips" panel in workset.html. Measured 2026-08-19, three fields are
# 87.6% of those bytes and the panel renders NONE of them:
#
#     prompt           3.98 MB  61.3%   needed only on CLICK (copy to clipboard)
#     resolution_note  1.45 MB  22.3%   never rendered
#     prompt_history   0.26 MB   4.0%   never rendered
#
# So `/api/chips` projects to the columns the panel actually draws and carries a
# `has_prompt` boolean in place of the prompt text; `/api/chips/prompt` serves
# one chip's prompt when a row is clicked. The panel also re-polls every 20 s per
# open tab, so the parse is cached on (mtime_ns, size) and an unchanged ledger
# answers the poll with a 304 via ETag.
#
# Deliberately NOT a schema or storage change: TASK_CHIPS.json is a git-tracked
# coordination file written concurrently from this Mac and ree-cloud-5, merged by
# chip_ledger.py's merge_origin_into_local(), committed through ree_commit.py's
# compare-and-swap, and audited by its per-item delta summary and plain git diff.
# A binary or columnar store would break every one of those. The columns are free
# at the serving layer instead.

# Fields workset.html's renderChips()/copyChipPrompt() read. Keep in sync with
# that function -- a field dropped here silently renders blank there.
CHIP_PANEL_FIELDS = (
    "chip_ref",
    "status",
    "title",
    "tldr",
    "session_id",
    "cwd",
    "spawned_at",
    "claimed_by",
    "claimed_at",
    "claim_note",
    # Filter columns for the panel's filter bar (added 2026-08-20). Measured cost
    # at the 1273 chips in the ledger that day: 943.9 KB -> 1055.5 KB, +11.8% --
    # paid once per ledger change, since the 20 s poll still answers 304 off the
    # (mtime_ns, size) ETag. Worth it because without them the client can filter
    # only on status, and the 52 open chips stay buried among 1144 done ones.
    # `resolved_at` is what an age filter reads for a RESOLVED chip (spawned_at
    # is the wrong clock there).
    "origin",
    "kind",
    "urgency",
    "resolved_at",
)

_CHIPS_CACHE = {"key": None, "projected": None, "prompts": None,
                "archived": None, "etag": None}
_CHIPS_CACHE_LOCK = threading.Lock()


def _chips_cache_key():
    """(mtime_ns, size) of the ledger, or None if it is not there."""
    try:
        st = TASK_CHIPS_FILE.stat()
        return (st.st_mtime_ns, st.st_size)
    except OSError:
        return None


def read_chips_projected() -> tuple:
    """Return (payload, etag) for the panel: chips reduced to CHIP_PANEL_FIELDS.

    `prompt` is replaced by a `has_prompt` boolean -- the panel only needs to
    know whether there is something to copy; the text itself comes from
    /api/chips/prompt on click. Parse is memoised on (mtime_ns, size), so the
    20 s poll from every open tab costs a stat() rather than a 7 MB parse.
    """
    key = _chips_cache_key()
    with _CHIPS_CACHE_LOCK:
        if key is not None and _CHIPS_CACHE["key"] == key:
            return _CHIPS_CACHE["projected"], _CHIPS_CACHE["etag"]

    data = read_chips()
    rows = []
    prompts = {}
    archived = {}
    for ch in data.get("chips", []):
        if not isinstance(ch, dict):
            continue
        row = {k: ch[k] for k in CHIP_PANEL_FIELDS if k in ch}
        # Same fallback chain copyChipPrompt() uses, so has_prompt is true
        # exactly when a click would produce something to paste.
        marker = ch.get("archived")
        has_archived_prompt = (isinstance(marker, dict)
                               and "prompt" in (marker.get("fields") or []))
        body = ch.get("prompt") or ch.get("tldr") or ch.get("title")
        row["has_prompt"] = bool(body) or has_archived_prompt
        rows.append(row)
        ref = ch.get("chip_ref")
        if ref and ch.get("prompt"):
            prompts[ref] = ch["prompt"]
        elif ref and isinstance(ch.get("archived"), dict):
            # Keep the stub (chip_ref + archived marker) so read_chip_prompt()
            # can resolve it out of chip_archive/ on click.
            archived[ref] = {"chip_ref": ref, "archived": ch["archived"],
                             "resolved_at": ch.get("resolved_at"),
                             "spawned_at": ch.get("spawned_at")}

    payload = {
        "schema_version": data.get("schema_version", "task_chips/v1"),
        "projection": "panel/v1",
        "prompt_endpoint": "/api/chips/prompt?chip_ref=",
        "chips": rows,
    }
    if data.get("empty_note"):
        payload["empty_note"] = data["empty_note"]
    etag = '"chips-%s-%s"' % (key[0], key[1]) if key else '"chips-none"'

    with _CHIPS_CACHE_LOCK:
        _CHIPS_CACHE.update(
            {"key": key, "projected": payload, "prompts": prompts,
             "archived": archived, "etag": etag}
        )
    return payload, etag


def read_chip_prompt(chip_ref: str):
    """One chip's recorded spawn_task prompt, or None. Served on row click.

    Falls back to the fat-field archive (chip_archive/<YYYY-MM>.json, written by
    chip_ledger.py's `archive` subcommand) when the chip is past the retention
    window and its prompt is no longer inline in TASK_CHIPS.json. Without this
    the panel's copy-to-clipboard would degrade to tldr/title for every chip
    older than the window -- silently, since has_prompt is computed from the
    same fallback chain and would still say true.
    """
    read_chips_projected()  # refreshes the cache if the ledger moved
    with _CHIPS_CACHE_LOCK:
        prompts = _CHIPS_CACHE["prompts"] or {}
        archived = _CHIPS_CACHE["archived"] or {}
    if chip_ref in prompts:
        return prompts[chip_ref]
    chip = archived.get(chip_ref)
    if chip is None:
        return None
    try:
        sys.path.insert(0, str(SERVE_DIR.parent / "scripts"))
        import chip_ledger  # noqa: WPS433
        return chip_ledger.archived_field(chip, "prompt")
    except Exception:
        return None


# --- Status/history plane query (status_history_plane:SHP-3, Q2=both) ---------

STATUS_HISTORY_LOG = PLANNING_DIR / "status_history" / "status_snapshot.v1.jsonl"


def _iter_status_history_records():
    """Yield each JSON record from the append-only status-plane log, skipping
    blank/malformed lines. The log holds two kinds: `shp2_backfill_lift` (SHP-2
    non-destructive archive) and `status_projection` (SHP-3 derived-live timeline)."""
    if not STATUS_HISTORY_LOG.exists():
        return
    try:
        with open(STATUS_HISTORY_LOG, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except ValueError:
                    continue
    except OSError:
        return


def _status_changepoints_index() -> dict:
    """Compact per-node change-point index for the closure-map sparkline. Reads the
    append-only status log ONCE (avoids the O(nodes x file) blow-up of calling
    read_status_history_for_node per node) and returns
    {node_id: [{"utc","status","verdict"}, ...]} in append order (oldest first).

    Only `status_projection` records count as change-points. The log is
    CHANGE-ONLY: a gap between two points is a STABLE span, never missing data, so
    a node with 0-1 points reads as "stable" (flat baseline), never "unknown"."""
    idx: dict[str, list] = {}
    for d in _iter_status_history_records():
        if d.get("kind") != "status_projection":
            continue
        nid = d.get("node_id")
        if not nid:
            continue
        live = d.get("live") if isinstance(d.get("live"), dict) else {}
        idx.setdefault(str(nid), []).append({
            "utc": d.get("projected_utc"),
            "status": d.get("status"),
            "verdict": (str(live.get("verdict"))
                        if live.get("verdict") is not None else None),
        })
    return idx


def read_status_history_for_node(node_id: str) -> dict:
    """History-plane slice for one node from the append-only log: the
    `status_projection` timeline (append order = oldest first) plus the SHP-2
    backfill-lift archive record (if the node was collapsed via the razor)."""
    projections: list[dict] = []
    backfill = None
    for d in _iter_status_history_records():
        if d.get("node_id") != node_id:
            continue
        kind = d.get("kind")
        if kind == "status_projection":
            projections.append({
                "projected_utc": d.get("projected_utc"),
                "projected_by": d.get("projected_by"),
                "status": d.get("status"),
                "severity": d.get("severity"),
                "live": d.get("live"),
            })
        elif kind == "shp2_backfill_lift":
            backfill = {
                "lifted_utc": d.get("lifted_utc"),
                "lifted_by": d.get("lifted_by"),
                "reason": d.get("reason"),
                "at_risk_history_bits": d.get("at_risk_history_bits") or [],
            }
    return {
        "projection_count": len(projections),
        "projections": projections,
        "backfill_lift": backfill,
    }


def _node_head_view(plan: dict, fname: str, node: dict) -> dict:
    """The status-plane head view for one collapsed-plan node (the `live:` block
    plus its `join:` and plan provenance). `collapsed` is False for any node that
    predates the SHP-2 two-plane collapse (no `live:` block)."""
    live = node.get("live")
    join = node.get("join")
    plan_id = str(plan.get("id") or fname.replace("_plan.md", ""))
    return {
        "node_id": node.get("id"),
        "plan_id": plan_id,
        "plan_file": f"evidence/planning/{fname}",
        "status": node.get("status"),
        "severity": node.get("severity"),
        "collapsed": isinstance(live, dict),
        "live": live if isinstance(live, dict) else None,
        "join": join if isinstance(join, dict) else None,
    }


def query_status_history(node_id: str | None = None,
                         claim_id: str | None = None) -> dict:
    """Q2=BOTH query (design sec 3): for a node id OR a claim id, return the
    collapsed-plan `live:` head (status plane) AND the appended
    `status_snapshot/v1` history slice (history plane) from the append-only log.

    - `?node=<id>`  -> {found, node:{...live..., history:{...}}}
    - `?claim=<id>` -> {found, match_count, nodes:[{...}]} for every node whose
      node-level (or plan-level) scope_claims contains the claim."""
    if node_id:
        found = None
        if PLANNING_DIR.exists():
            for path in sorted(PLANNING_DIR.glob("*_plan.md")):
                plan = _parse_plan_frontmatter(path)
                if not plan:
                    continue
                for node in plan.get("nodes") or []:
                    if isinstance(node, dict) and node.get("id") == node_id:
                        found = _node_head_view(plan, path.name, node)
                        break
                if found:
                    break
        if found is None:
            return {"query": {"node": node_id}, "found": False,
                    "message": "No closure-plan node with this id."}
        found["history"] = read_status_history_for_node(node_id)
        return {"query": {"node": node_id}, "found": True, "node": found}

    if claim_id:
        matches: list[dict] = []
        if PLANNING_DIR.exists():
            for path in sorted(PLANNING_DIR.glob("*_plan.md")):
                plan = _parse_plan_frontmatter(path)
                if not plan:
                    continue
                plan_scope = plan.get("scope_claims") or []
                for node in plan.get("nodes") or []:
                    if not isinstance(node, dict) or not node.get("id"):
                        continue
                    join = node.get("join") if isinstance(node.get("join"), dict) else {}
                    scope = (node.get("scope_claims")
                             or join.get("scope_claims") or plan_scope or [])
                    if claim_id in scope:
                        view = _node_head_view(plan, path.name, node)
                        view["history"] = read_status_history_for_node(node["id"])
                        matches.append(view)
        return {"query": {"claim": claim_id}, "found": bool(matches),
                "match_count": len(matches), "nodes": matches}

    return {"error": "provide ?node=<node_id> or ?claim=<claim_id>",
            "example": "/api/status_history?node=goal_pipeline:GAP-1"}


def read_igw_ledger() -> dict:
    """Load the IGW auto-spawn routine ledger for the explorer panel.

    The ledger (evidence/planning/igw_routine_ledger.json) is written by
    scripts/igw_routine_tick.py -- one entry per spawned/staged IGW item.
    This reader is READ-ONLY (the tick is the sole writer); it returns the
    entries newest-first plus a status/outcome summary. Never raises.
    """
    empty = {
        "schema": "igw_routine_ledger/view",
        "count": 0,
        "summary": {"by_status": {}, "by_outcome": {}, "staged_waiting": 0},
        "entries": [],
        "references": {"workset_page": "/workset", "explorer": "/explorer.html"},
        "empty_note": (
            "No IGW routine ledger yet. The hourly routine "
            "(scripts/igw_routine_tick.py) writes it on first spawn/stage."
        ),
    }
    if not IGW_LEDGER_FILE.exists():
        return empty
    try:
        data = json.loads(IGW_LEDGER_FILE.read_text(encoding="utf-8"))
    except Exception:
        empty["empty_note"] = "IGW ledger file unreadable."
        return empty
    if isinstance(data, dict):
        entries = data.get("entries") or data.get("ledger") or []
    elif isinstance(data, list):
        entries = data
    else:
        entries = []
    if not isinstance(entries, list):
        entries = []

    # Join the cross-agent assignment ledger (igw_assignments.json) by
    # stable_hash so the panel shows the SAME "assigned" label the workset
    # uses (agent chip: claude_local / cursor / codex / other). This is the
    # one shared source of truth for "who holds this IGW"; the routine ledger
    # only carries process state. Keyed by stable_hash; read-only.
    by_hash: dict = {}
    try:
        sys.path.insert(0, str(SERVE_DIR / "scripts"))
        import igw_assignments_lib as _ial  # noqa: WPS433
        by_hash = _ial.assignments_by_hash()
    except Exception:
        by_hash = {}
    for e in entries:
        if isinstance(e, dict):
            e["active_assignments"] = by_hash.get(e.get("stable_hash") or "", [])

    def _sort_key(e):
        return e.get("reaped_at") or e.get("assigned_at") or e.get("staged_at") or ""

    entries = sorted(entries, key=_sort_key, reverse=True)
    by_status: dict = {}
    by_outcome: dict = {}
    by_assigned_agent: dict = {}
    staged_waiting = 0
    assigned_active = 0
    for e in entries:
        st = e.get("status") or "unknown"
        by_status[st] = by_status.get(st, 0) + 1
        if st == "staged":
            staged_waiting += 1
        oc = e.get("outcome")
        if oc:
            by_outcome[oc] = by_outcome.get(oc, 0) + 1
        asn = e.get("active_assignments") or []
        if asn:
            assigned_active += 1
            for a in asn:
                ag = a.get("agent") or "unknown"
                by_assigned_agent[ag] = by_assigned_agent.get(ag, 0) + 1
    return {
        "schema": "igw_routine_ledger/view",
        "count": len(entries),
        "summary": {
            "by_status": by_status,
            "by_outcome": by_outcome,
            "by_assigned_agent": by_assigned_agent,
            "assigned_active": assigned_active,
            "staged_waiting": staged_waiting,
        },
        "entries": entries,
        "references": {"workset_page": "/workset", "explorer": "/explorer.html"},
    }


def _machine_safe_filename(machine: str) -> str:
    keep = "-_."
    return "".join(c if (c.isalnum() or c in keep) else "_" for c in machine)


def _commands_file(machine: str) -> Path:
    # Canonicalised so a command issued against a drifted spelling still lands in
    # the file the runner actually polls: runner_remote_control.get_machine_id()
    # resolves the same way, so it reads `DLAPTOP.json` and would never see a
    # command parked in `DLAPTOP-5.local.json`. Reads and writes both route
    # through here, so the two stay consistent.
    canon = machine_identity.canonical_machine_name(machine) or machine
    return COMMANDS_DIR / f"{_machine_safe_filename(canon)}.json"


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


def _coordinator_issue_command(
    machine: str,
    kind: str,
    args: dict | None,
    issued_by: str,
) -> tuple[bool, bool, object]:
    """Best-effort issue of a remote-control command via the coordinator's
    POST /commands/issue. Returns (attempted, ok, detail).

      attempted == False -> coordinator not configured (coordinator.env
                            missing COORDINATOR_URL / COORDINATOR_LOCAL_TOKEN);
                            caller treats as git-only.
      attempted == True, ok == True  -> detail is the created command dict.
      attempted == True, ok == False -> detail is an error string.

    Never raises. Mirrors the urllib pattern of _fetch_coordinator_snapshot /
    _shadow_status proxy."""
    cfg = _load_coordinator_cfg()
    url = (cfg.get("COORDINATOR_URL") or "").rstrip("/")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN") or ""
    if not url or not tok:
        return (False, False, "coordinator not configured")
    import urllib.error
    import urllib.request
    # Resolve before posting, matching what the git fallback already does via
    # _commands_file(). Without it the PRIMARY channel was the unresolved one
    # and the deprecated fallback the resolved one -- the asymmetry the wrong
    # way round. The runner polls GET /commands under its CANONICAL name
    # (experiment_runner._get_machine_name canonicalises), so a command issued
    # from a machine card still labelled `DLAPTOP-4.local` would sit pending
    # forever with no error anywhere. The coordinator canonicalises this same
    # value at ingest too (coordinator/app.py `_canon`); resolving here as
    # well keeps the explorer's own echo/logging honest about where the
    # command actually went. `ree-cloud-N` names pass through untouched --
    # canonical_machine_name is an allowlist, not a `-<digits>` strip.
    machine = machine_identity.canonical_machine_name(machine) or machine
    body = json.dumps({
        "machine": machine, "kind": kind,
        "args": args or {}, "issued_by": issued_by,
    }).encode("utf-8")
    try:
        req = urllib.request.Request(
            url + "/commands/issue", data=body,
            headers={"Authorization": "Bearer " + tok,
                     "Content-Type": "application/json"},
            method="POST")
        with urllib.request.urlopen(req, timeout=8) as r:
            resp = json.loads(r.read().decode("utf-8"))
        return (True, bool(resp.get("ok")), resp.get("command"))
    except (urllib.error.URLError, urllib.error.HTTPError, OSError,
            ValueError, json.JSONDecodeError) as exc:
        return (True, False, f"coordinator issue failed: {exc}")


def _utc_now_iso() -> str:
    return _utc_now_compact()


def _normalize_manifest_fields(m: dict) -> tuple:
    """Pull (verdict, timestamp, claim_id) out of any of the three manifest
    schemas we currently emit: legacy flat (verdict/run_timestamp/claim),
    indexer-built flat sibling (outcome|result/timestamp_utc/claim_ids), and
    runs/<id>/manifest.json (status/timestamp_utc/claim_ids_tested).
    """
    verdict = m.get("verdict") or m.get("outcome") or m.get("result") or m.get("status")
    timestamp = m.get("run_timestamp") or m.get("timestamp_utc")
    claim_id = m.get("claim")
    if not claim_id:
        for key in ("claim_ids", "claim_ids_tested"):
            v = m.get(key)
            if isinstance(v, list) and v:
                claim_id = v[0]
                break
    return verdict, timestamp, claim_id


# --- Claude Code local usage (ccusage-style) -------------------------------
# Per-1M-token pricing (input, output). cache-write 5m = 1.25x input,
# cache-write 1h = 2x input, cache-read = 0.1x input. Source: claude-api skill;
# verify if stale. Unknown models default to opus-tier (5 / 25).
_CLAUDE_PRICING = {
    "claude-opus-4-8": (5.0, 25.0),
    "claude-opus-4-7": (5.0, 25.0),
    "claude-opus-4-6": (5.0, 25.0),
    "claude-opus-4-5": (5.0, 25.0),
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-sonnet-4-5": (3.0, 15.0),
    "claude-fable-5": (10.0, 50.0),
    "claude-haiku-4-5": (1.0, 5.0),
}
_CLAUDE_PRICING_DEFAULT = (5.0, 25.0)
_CLAUDE_BLOCK_SECONDS = 5 * 3600
_CLAUDE_USAGE_MTIME_CUTOFF_DAYS = 8

# Subscription context. The local transcript scrape only sees THIS device, so
# any usage reading here is a lower bound on the account total (claude.ai, the
# desktop app, and Claude Code on other machines are not visible). Anthropic
# does not publish exact token caps for Max plans (limits are message/hour-based
# and have shifted over time), and the token totals below are inflated by
# cache-reads -- so we deliberately do NOT show a fabricated "% of plan limit".
# Instead the 5h gauge self-calibrates against the user's own busiest recent
# block, and the weekly section reports a real fixed-anchor window.
_CLAUDE_PLAN_LABEL = "Max 20x"
_CLAUDE_DEVICE_SCOPE = "this device only"
# Weekly-window reset anchor (UTC). Matches how the Max plan weekly limit
# resets on a fixed 7-day cycle. Calibrated 2026-06-23 to the Claude app's
# Usage screen, which showed the weekly limit "Resets Fri 18:59" in local
# (Ireland = IST = UTC+1 in summer), i.e. Friday 17:59 UTC. Re-check against
# the app's Usage screen if the displayed countdown drifts.
_CLAUDE_WEEKLY_RESET_WEEKDAY = 4  # 0=Monday .. 6=Sunday; 4=Friday
_CLAUDE_WEEKLY_RESET_HOUR = 17
_CLAUDE_WEEKLY_RESET_MINUTE = 59


def _claude_price_for(model):
    """(input, output) per-1M price for a model id.

    Transcripts carry dated ids (e.g. claude-haiku-4-5-20251001) that do not
    exact-match the undated pricing keys, so fall back to a prefix match before
    the opus-tier default; otherwise a dated haiku/sonnet is priced as opus.
    """
    if model in _CLAUDE_PRICING:
        return _CLAUDE_PRICING[model]
    for key, price in _CLAUDE_PRICING.items():
        if model.startswith(key):
            return price
    return _CLAUDE_PRICING_DEFAULT


def _claude_parse_ts(raw):
    """Parse an ISO-8601 timestamp (trailing 'Z') into an aware UTC datetime."""
    from datetime import datetime, timezone
    if not raw or not isinstance(raw, str):
        return None
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _claude_zero_tokens():
    return {"input": 0, "output": 0, "cache_write": 0, "cache_read": 0, "total": 0}


def _claude_accumulate(bucket, entry):
    """Add one parsed entry's cost/tokens/message into a running bucket dict."""
    bucket["cost_usd"] += entry["cost"]
    bucket["messages"] += 1
    tk = bucket["tokens"]
    tk["input"] += entry["input"]
    tk["output"] += entry["output"]
    tk["cache_write"] += entry["cache_write"]
    tk["cache_read"] += entry["cache_read"]
    tk["total"] += entry["total"]


def compute_claude_usage() -> dict:
    """Compute Claude Code token+cost usage from local transcript JSONL.

    ccusage-style: walks ~/.claude/projects/**/*.jsonl, prices each assistant
    line per-model, and reports the active 5h block, rolling 7d, today, and a
    per-model breakdown. Percentages elsewhere are vs an estimated cap and
    'weekly' is a rolling 7-day sum -- accepted by design.
    """
    from datetime import datetime, timezone, timedelta
    import json as _json
    try:
        now = datetime.now(timezone.utc)
        base = Path.home() / ".claude" / "projects"
        mtime_cutoff = now.timestamp() - _CLAUDE_USAGE_MTIME_CUTOFF_DAYS * 86400
        seen = set()
        entries = []
        if base.exists():
            for fp in base.glob("**/*.jsonl"):
                try:
                    if fp.stat().st_mtime < mtime_cutoff:
                        continue
                except OSError:
                    continue
                try:
                    with open(fp, "r", errors="replace") as fh:
                        for line in fh:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                obj = _json.loads(line)
                            except Exception:
                                continue
                            if obj.get("type") != "assistant":
                                continue
                            msg = obj.get("message") or {}
                            usage = msg.get("usage")
                            if not isinstance(usage, dict):
                                continue
                            model = msg.get("model") or ""
                            if model == "<synthetic>":
                                continue
                            dedup_key = (msg.get("id"), obj.get("requestId"))
                            if dedup_key in seen:
                                continue
                            seen.add(dedup_key)
                            ts = _claude_parse_ts(obj.get("timestamp"))
                            if ts is None:
                                continue
                            inp = int(usage.get("input_tokens") or 0)
                            out = int(usage.get("output_tokens") or 0)
                            cw_total = int(usage.get("cache_creation_input_tokens") or 0)
                            cr = int(usage.get("cache_read_input_tokens") or 0)
                            cc = usage.get("cache_creation")
                            if isinstance(cc, dict):
                                cw5m = int(cc.get("ephemeral_5m_input_tokens") or 0)
                                cw1h = int(cc.get("ephemeral_1h_input_tokens") or 0)
                            else:
                                cw5m, cw1h = cw_total, 0
                            in_price, out_price = _claude_price_for(model)
                            cost = (
                                inp * in_price
                                + out * out_price
                                + cw5m * in_price * 1.25
                                + cw1h * in_price * 2.0
                                + cr * in_price * 0.1
                            ) / 1e6
                            entries.append({
                                "ts": ts,
                                "model": model,
                                "cost": cost,
                                "input": inp,
                                "output": out,
                                "cache_write": cw_total,
                                "cache_read": cr,
                                "total": inp + out + cw_total + cr,
                            })
                except OSError:
                    continue

        entries.sort(key=lambda e: e["ts"])
        block_secs = timedelta(seconds=_CLAUDE_BLOCK_SECONDS)
        cutoff_7d = now - timedelta(days=7)

        # Fixed weekly window anchor (matches the Max plan weekly reset cycle).
        def _week_start(dt):
            days_back = (dt.weekday() - _CLAUDE_WEEKLY_RESET_WEEKDAY) % 7
            anchor = dt.replace(hour=_CLAUDE_WEEKLY_RESET_HOUR,
                                minute=_CLAUDE_WEEKLY_RESET_MINUTE,
                                second=0, microsecond=0) - timedelta(days=days_back)
            if anchor > dt:
                anchor -= timedelta(days=7)
            return anchor
        week_start = _week_start(now)
        week_reset = week_start + timedelta(days=7)

        # --- 5h block (ccusage-style) ---
        block_5h = {
            "active": False,
            "start": None,
            "reset_at": None,
            "seconds_to_reset": 0,
            "elapsed_frac": 0.0,
            "cost_usd": 0.0,
            "messages": 0,
            "tokens": _claude_zero_tokens(),
            "peak_total_tokens": 0,
            "peak_cost_usd": 0.0,
        }
        if entries:
            blocks = []  # list of dicts: {start, entries}
            block_start = None
            prev_ts = None
            cur = None
            for e in entries:
                ts = e["ts"]
                new_block = (
                    cur is None
                    or (ts - block_start) >= block_secs
                    or (ts - prev_ts) >= block_secs
                )
                if new_block:
                    block_start = ts.replace(minute=0, second=0, microsecond=0)
                    cur = {"start": block_start, "entries": []}
                    blocks.append(cur)
                cur["entries"].append(e)
                prev_ts = ts
            last = blocks[-1]
            start = last["start"]
            last_ts = last["entries"][-1]["ts"]
            reset_at = start + block_secs
            active = (now - last_ts) < block_secs
            elapsed = (now - start).total_seconds() / _CLAUDE_BLOCK_SECONDS
            elapsed_frac = max(0.0, min(1.0, elapsed))
            secs_to_reset = max(0, int((reset_at - now).total_seconds()))
            block_5h["active"] = bool(active)
            block_5h["start"] = start.strftime("%Y-%m-%dT%H:%M:%SZ")
            block_5h["reset_at"] = reset_at.strftime("%Y-%m-%dT%H:%M:%SZ")
            block_5h["seconds_to_reset"] = secs_to_reset
            block_5h["elapsed_frac"] = round(elapsed_frac, 4)
            for e in last["entries"]:
                _claude_accumulate(block_5h, e)
            # Self-calibrating reference: heaviest 5h block in the trailing 7d,
            # so the panel reads "this block vs your busiest recent block"
            # without needing Anthropic's (unpublished, shifting) plan caps.
            peak_total = 0
            peak_cost = 0.0
            for blk in blocks:
                if blk["start"] < cutoff_7d:
                    continue
                bt = sum(e["total"] for e in blk["entries"])
                bc = sum(e["cost"] for e in blk["entries"])
                peak_total = max(peak_total, bt)
                peak_cost = max(peak_cost, bc)
            block_5h["peak_total_tokens"] = peak_total
            block_5h["peak_cost_usd"] = round(peak_cost, 4)

        # --- rolling 7d ---
        rolling_7d = {
            "cost_usd": 0.0,
            "messages": 0,
            "start": cutoff_7d.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "tokens": _claude_zero_tokens(),
        }
        # --- today (UTC date) ---
        today_date = now.date()
        today = {
            "cost_usd": 0.0,
            "messages": 0,
            "tokens": _claude_zero_tokens(),
        }
        # --- weekly window (fixed anchor; matches the Max plan weekly reset) ---
        week_span = (now - week_start).total_seconds() / (7 * 86400)
        weekly_window = {
            "cost_usd": 0.0,
            "messages": 0,
            "tokens": _claude_zero_tokens(),
            "start": week_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "reset_at": week_reset.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "seconds_to_reset": max(0, int((week_reset - now).total_seconds())),
            "elapsed_frac": round(max(0.0, min(1.0, week_span)), 4),
        }
        by_model = {}
        for e in entries:
            if e["ts"] >= cutoff_7d:
                _claude_accumulate(rolling_7d, e)
                bm = by_model.get(e["model"])
                if bm is None:
                    bm = {"model": e["model"], "cost_usd": 0.0,
                          "total_tokens": 0, "messages": 0}
                    by_model[e["model"]] = bm
                bm["cost_usd"] += e["cost"]
                bm["total_tokens"] += e["total"]
                bm["messages"] += 1
            if e["ts"] >= week_start:
                _claude_accumulate(weekly_window, e)
            if e["ts"].date() == today_date:
                _claude_accumulate(today, e)

        for bucket in (block_5h, rolling_7d, weekly_window, today):
            bucket["cost_usd"] = round(bucket["cost_usd"], 4)
        by_model_list = sorted(
            by_model.values(), key=lambda r: r["cost_usd"], reverse=True)
        for r in by_model_list:
            r["cost_usd"] = round(r["cost_usd"], 4)

        return {
            "ok": True,
            "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "plan": _CLAUDE_PLAN_LABEL,
            "device_scope": _CLAUDE_DEVICE_SCOPE,
            "block_5h": block_5h,
            "weekly_window": weekly_window,
            "rolling_7d": rolling_7d,
            "today": today,
            "by_model": by_model_list,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


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
            latest_file = None
            run_count = 0
            if files:
                latest_file = files[-1]
                run_count = len(files)
            else:
                # Indexer-built run-pack: manifests live under runs/<run_id>/manifest.json
                # only (no flat top-level copy). Pick the lexicographically latest run dir
                # (run_ids are timestamped, so name order == time order).
                runs_dir = exp_dir / "runs"
                if runs_dir.is_dir():
                    run_manifests = sorted(runs_dir.glob("*/manifest.json"))
                    if run_manifests:
                        latest_file = run_manifests[-1]
                        run_count = len(run_manifests)
                if latest_file is None:
                    # Last-ditch fallback: indexer's flat input manifest may sit as a
                    # sibling at the top of evidence/experiments/ (not inside the dir).
                    sibling_matches = sorted(
                        f for f in ev_dir.glob(f"{exp_dir.name}_*.json")
                        if f.is_file() and not f.name.endswith("_episode_log.json")
                    )
                    if sibling_matches:
                        latest_file = sibling_matches[-1]
                        run_count = 1
            if latest_file is None:
                continue
            latest = {}
            try:
                latest = json.loads(latest_file.read_text())
            except Exception:
                pass
            # Check for companion episode log alongside the latest result.
            # For runs/<id>/manifest.json, the episode log (if any) sits next
            # to the manifest in the same run dir.
            episode_log_url = None
            if latest_file.name == "manifest.json":
                ep_candidates = list(latest_file.parent.glob("*_episode_log.json"))
                if ep_candidates:
                    try:
                        episode_log_url = str(ep_candidates[0].relative_to(SERVE_DIR))
                    except ValueError:
                        pass
            else:
                episode_log_file = latest_file.parent / f"{latest_file.stem}_episode_log.json"
                if episode_log_file.exists():
                    try:
                        episode_log_url = str(episode_log_file.relative_to(SERVE_DIR))
                    except ValueError:
                        pass
            verdict, timestamp, claim_id = _normalize_manifest_fields(latest)
            result[exp_dir.name] = {
                "run_count": run_count,
                "latest_verdict": verdict,
                "latest_timestamp": timestamp,
                "claim_id": claim_id,
                "substrate": ver,
                "episode_log_url": episode_log_url,
            }
    return result


def _find_manifest_file(script_name: str = "", queue_id: str = ""):
    """Locate the best (most-recent) manifest on local disk for a completed
    experiment card.

    Completed cards carry script_name (the evidence dir / flat-manifest stem)
    and queue_id. The card's output_file is an absolute path from whatever
    machine ran the experiment (Windows C:\\..., a different Mac root, etc.)
    and is NOT usable on this filesystem -- so we resolve against the local
    evidence/experiments tree by script_name, then fall back to queue_id.

    Returns a Path or None. Covers all three layouts the runner/indexer emit:
      * flat top-level:   evidence/experiments/<script>_<ts>.json  (V3 default)
      * exact flat:       evidence/experiments/<script>.json
      * per-dir flat:     evidence/experiments/<script>/*.json
      * indexer run-pack: evidence/experiments/<script>/runs/*/manifest.json
    """
    def _is_manifest(p) -> bool:
        return p.is_file() and not p.name.endswith("_episode_log.json")

    if script_name:
        # Prefer rich "flat" manifests (the runner's own output, with
        # metrics/criteria/summary) over the indexer-built run-pack
        # manifest.json (a lean schema that drops those bulky fields).
        flat = []
        runpack = []
        for cfg in RUNNERS.values():
            ev_dir = cfg["evidence_dir"]
            if not ev_dir.exists():
                continue
            flat += [f for f in ev_dir.glob(f"{script_name}_*.json") if _is_manifest(f)]
            exact = ev_dir / f"{script_name}.json"
            if _is_manifest(exact):
                flat.append(exact)
            sub = ev_dir / script_name
            if sub.is_dir():
                sub_flat = [f for f in sub.glob("*.json") if _is_manifest(f)]
                if sub_flat:
                    flat += sub_flat
                else:
                    runpack += list((sub / "runs").glob("*/manifest.json"))
        if flat:
            # Filenames carry a sortable timestamp -> latest last.
            return sorted(flat, key=lambda p: p.name)[-1]
        if runpack:
            # All named manifest.json -> order by the timestamped parent run-dir.
            return sorted(runpack, key=lambda p: p.parent.name)[-1]

    if queue_id:
        # Derive a filename hint from the queue_id so we only parse a handful
        # of files (e.g. "V3-EXQ-624b" -> "exq_624b") instead of every manifest.
        hint = queue_id.lower()
        for pfx in ("v3-", "v2-", "v1-"):
            if hint.startswith(pfx):
                hint = hint[len(pfx):]
                break
        hint = hint.replace("-", "_")
        for cfg in RUNNERS.values():
            ev_dir = cfg["evidence_dir"]
            if not ev_dir.exists():
                continue
            matches = []
            for f in ev_dir.glob(f"*{hint}*.json"):
                if not _is_manifest(f):
                    continue
                try:
                    m = json.loads(f.read_text())
                except Exception:
                    continue
                if m.get("queue_id") == queue_id:
                    matches.append(f)
            if matches:
                return sorted(matches, key=lambda p: p.name)[-1]
    return None


def _truncate_for_detail(obj, max_list: int = 8, max_str: int = 800, _depth: int = 0):
    """Return a JSON-serialisable copy of obj with long lists/strings clipped,
    so a manifest's bulky metric arrays don't blow up the detail payload."""
    if _depth > 6:
        return "..."
    if isinstance(obj, str):
        return obj if len(obj) <= max_str else obj[:max_str] + f"... (+{len(obj) - max_str} chars)"
    if isinstance(obj, list):
        out = [_truncate_for_detail(x, max_list, max_str, _depth + 1) for x in obj[:max_list]]
        if len(obj) > max_list:
            out.append(f"... (+{len(obj) - max_list} more items)")
        return out
    if isinstance(obj, dict):
        return {k: _truncate_for_detail(v, max_list, max_str, _depth + 1) for k, v in obj.items()}
    return obj


# Keys rendered in the detail header (or pure plumbing) -- not shown as sections.
_DETAIL_HEADER_KEYS = {
    "run_id", "queue_id", "timestamp_utc", "run_timestamp", "outcome", "verdict",
    "result_verdict", "status", "claim_ids", "claim_ids_tested", "claim",
    "evidence_direction", "evidence_direction_per_claim", "architecture_epoch",
    "experiment_type", "schema_version", "machine", "runner", "source_repo",
    "producer_capabilities", "stop_criteria_version", "evidence_class", "dry_run",
    "supersedes", "proposal_id", "backlog_id", "pending_failure_autopsy",
    "elapsed_seconds",
}
# Content keys rendered first, in this order, when present. `result` covers the
# newer schema's nested results dict; summary/metrics/criteria/notes cover the
# older inline schema. Any remaining content key is appended generically.
_DETAIL_SECTION_ORDER = [
    ("PURPOSE", "experiment_purpose"),
    ("EVIDENCE DIRECTION NOTE", "evidence_direction_note"),
    ("SUMMARY", "summary"),
    ("RESULT", "result"),
    ("CRITERIA", "criteria"),
    ("METRICS", "metrics"),
    ("NOTES", "notes"),
    ("FAILURE SIGNATURES", "failure_signatures"),
    ("REGISTERED THRESHOLDS", "registered_thresholds"),
    ("CONFIG", "config"),
    ("CONFIG SUMMARY", "config_summary"),
    ("ENV KWARGS", "env_kwargs"),
    ("ENVIRONMENT", "environment"),
    ("ARTIFACTS", "artifacts"),
]


def build_manifest_detail(m: dict) -> str:
    """Human-readable, size-bounded rendering of a completed experiment's
    manifest for the explorer Completed-card detail panel. Mirrors the
    information density of the running card's scrollable stdout readout, but
    drawn from the persistent manifest instead of ephemeral recent_lines.

    Schema-agnostic: handles both the inline-metrics manifest family
    (summary/metrics/criteria/notes) and the nested-result family
    (result/config_summary/env_kwargs/evidence_direction_note), and appends a
    generic catch-all for any other content key so no schema drops detail."""
    verdict, timestamp, _ = _normalize_manifest_fields(m)
    lines = []
    head = f"OUTCOME: {verdict or '?'}"
    ed = m.get("evidence_direction")
    if ed:
        head += f"    evidence_direction: {ed}"
    lines.append(head)
    if m.get("run_id"):
        lines.append(f"run_id: {m['run_id']}")
    if timestamp:
        lines.append(f"timestamp: {timestamp}")
    claims = m.get("claim_ids_tested") or m.get("claim_ids")
    if claims:
        lines.append("claims: " + ", ".join(str(c) for c in claims))
    edpc = m.get("evidence_direction_per_claim")
    if isinstance(edpc, dict) and edpc:
        lines.append("per-claim direction: " + ", ".join(f"{k}={v}" for k, v in edpc.items()))

    rendered = set()

    def section(title: str, key: str):
        if key in rendered:
            return
        val = m.get(key)
        if val in (None, "", [], {}):
            return
        rendered.add(key)
        lines.append("")
        lines.append(f"== {title} ==")
        if isinstance(val, str):
            lines.append(val if len(val) <= 4000 else val[:4000] + f"... (+{len(val) - 4000} chars)")
        else:
            lines.append(json.dumps(_truncate_for_detail(val), indent=2, default=str))

    for title, key in _DETAIL_SECTION_ORDER:
        section(title, key)
    # Catch-all: any content key not already shown and not pure header/plumbing.
    for key in m:
        if key in rendered or key in _DETAIL_HEADER_KEYS:
            continue
        section(key.replace("_", " ").upper(), key)

    text = "\n".join(lines)
    cap = 24000
    if len(text) > cap:
        text = text[:cap] + "\n... (detail truncated)"
    return text


def _default_runner_extra_env() -> dict | None:
    """Shadow env to inject when start_runner is called without explicit
    extra_env (i.e. the everyday /api/runner/v3/start path). Reads
    coordinator.env via _load_coordinator_cfg; returns None when the file
    is missing or COORDINATOR_URL / COORDINATOR_LOCAL_TOKEN is unset, so
    behaviour stays bit-identical to the pre-default-injection path on a
    Mac that has not configured the coordinator.

    Without this default, the explorer "Start" button produced a runner
    with COORDINATION_MODE unset -> coordinator_client._ENABLED=False ->
    every report_claim / report_result / heartbeat POST became a no-op.
    The Shadow Coordination panel's start path passes its own explicit
    dict; this function consolidates the lookup for the everyday
    /api/runner/v3/start path.

    Phase 3 (live 2026-05-29): COORDINATION_MODE=coordinator so claim
    arbitration goes through the writer-authoritative /claim endpoint
    instead of the legacy git-mutex path. Shadow on a worker under
    Phase 3 is unsafe: the legacy stale-recovery check reads local
    heartbeat files materialised by the hub's sync_daemon, which can
    lag the DB by minutes; a worker can then "stale-recover" a claim
    the DB still considers active and run a duplicate. Hit on
    2026-05-29 when DLAPTOP-4 took V3-EXQ-610a away from ree-cloud-3
    via that exact path. The three PHASE3_DISABLE_RUNNER_*_PUSH gates
    keep the Mac from double-writing telemetry the sync_daemon already
    publishes. Cloud workers get the same env via
    /etc/systemd/system/ree-runner.service.d/shadow.conf.
    """
    cfg = _load_coordinator_cfg()
    url = cfg.get("COORDINATOR_URL")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN")
    if not url or not tok:
        return None
    return {
        "COORDINATION_MODE": "coordinator",
        "COORDINATOR_URL": url,
        "COORDINATOR_TOKEN": tok,
        "COORDINATOR_LOG": str(SERVE_DIR / "coordinator_shadow.log"),
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_RESULT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_QUEUE_PUSH": "1",
        # Claim-push gate (2026-06-03): retire the last git-as-IPC coordination
        # path. The coordinator /claim endpoint (db.try_claim, atomic
        # BEGIN IMMEDIATE) is the authoritative claim mutex under
        # COORDINATION_MODE=coordinator (set above), so the legacy
        # attempt_claim / release_claim `claim:` commits to ree-v3/main are
        # pure noise. The claimed_by write still lands in the LOCAL queue file
        # (read next tick); only the commit/push is skipped. Mirrors the cloud
        # workers' shadow.conf + ree_runner_launchd.sh. Default OFF would run
        # the git-mode mutex (bit-identical pre-Phase-3 behaviour).
        "PHASE3_DISABLE_RUNNER_CLAIM_PUSH": "1",
        # Suppress the LOCAL heartbeat + commands file writes too. The
        # writer publishes the canonical runner_heartbeats/<host>.json
        # from the coordinator DB; without this flag, the runner's local
        # write conflicts with the writer-pulled version on every
        # auto-sync `git pull REE_assembly` and leaves UU markers that
        # block subsequent pulls until a human clears them. The flag's
        # docstring frames it as hub-only, but the same UU happens on any
        # worker's local checkout -- the "hub-only" guidance was scoped
        # to *writer-side* corruption, not worker-local conflicts.
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_WRITE": "1",
        # Command-channel migration (2026-06-03): fetch + ack remote-control
        # commands via the coordinator too (dual-read; the local git command-
        # file is the fallback). Mirrors the cloud workers' shadow.conf +
        # ~/.local/bin/ree_runner_launchd.sh. Default-safe: the runner's
        # gate is a no-op unless COORDINATION_MODE=coordinator (set above).
        "PHASE3_COMMANDS_VIA_COORDINATOR": "1",
        # OFF_GIT (2026-06-03): coordinator is the SOLE command channel; the
        # runner neither reads nor writes the local git command-file. Self-
        # guards back to git if the coordinator is unavailable, so the runner
        # is never left uncontrollable. Mirrors the fleet shadow.conf +
        # ree_runner_launchd.sh. Commands now reach off-git runners via the
        # serve.py dual-write path (PHASE3_COMMANDS_DUAL_WRITE in coordinator.env).
        "PHASE3_COMMANDS_OFF_GIT": "1",
    }


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

    # Launchd-supervised path for the v3 Mac runner. Bootstrap the plist
    # (idempotent), then kickstart it. launchd then owns the lifecycle:
    # KeepAlive=true means crashes auto-respawn without a new Start
    # click. The plist runs ree_runner_launchd.sh which loads the same
    # env vars _default_runner_extra_env would inject for the Popen path
    # -- behaviour is bit-identical on a normal run. extra_env is
    # ignored on this path (the wrapper script owns env) -- callers
    # that need a custom env should temporarily uninstall the plist.
    if ver == "v3" and _launchd_supervises_v3() and extra_env is None:
        boot_ok, boot_note = _launchd_bootstrap_if_needed()
        if not boot_ok:
            return {"status": "error", "message": boot_note}
        kick_ok, kick_note = _launchd_kickstart()
        if not kick_ok:
            return {"status": "error", "message": kick_note}
        # Brief wait so the wrapper script has a chance to exec python.
        time.sleep(1.0)
        new_pid = _launchd_pid()
        print(f"[serve] {cfg['label']} runner started via launchd "
              f"(PID {new_pid}; {boot_note}; {kick_note})", flush=True)
        return {"status": "started", "pid": new_pid, "substrate": ver,
                "supervisor": "launchd"}

    python_exe = cfg["python"]
    if not os.path.exists(python_exe):
        python_exe = sys.executable  # fallback

    log_fh = open(RUNNER_LOG, "a")
    # Canonicalised because this value becomes BOTH the --status-file NAME and
    # the runner's --machine. runner_remote_control.get_machine_id() already
    # canonicalises the --machine it is handed, so a raw name here would write
    # the heartbeat under the canonical identity and the status file under the
    # drifted one -- half a split, created by this launcher rather than by the OS.
    _raw_machine_name = os.environ.get("REE_MACHINE_NAME") or socket.gethostname()
    machine_name = (machine_identity.canonical_machine_name(_raw_machine_name)
                    or _raw_machine_name)
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
    if extra_env is None:
        extra_env = _default_runner_extra_env()
    if extra_env:
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
                "On Mac: curl -s <COORDINATOR_URL>/health (expect ok:true).",
                "If it times out, the Mac WireGuard tunnel is down -- bounce it: "
                "sudo wg-quick down wg0 && sudo wg-quick up wg0.",
                "On ree-cloud-1: systemctl status ree-coordinator wg-quick@wg0.",
                "Coordinator + worker health are independent of this Mac's tunnel; "
                "the fleet may still be running fine -- this only blocks this "
                "panel's view.",
            ],
        }
    if verdict == "DIVERGENCE":
        if mode == "coordinator":
            return {
                "phase": 3,
                "phase_label": "Phase 3 -- writers live (DIVERGENCE)",
                "parallel": "Coordinator owns claims; sync_daemon is sole "
                            "git writer (Phase 3 live as of 2026-05-29). "
                            "Writer-rows below show per-writer health.",
                "assess": ("FAIL -- unexplained claim divergence under "
                           "Phase 3 (blocking=%d, raw audit=%d). The "
                           "coordinator's claim verdict disagreed with "
                           "the git mirror; same Phase-2 root-cause "
                           "checks still apply." % (div, raw_div)),
                "retire": "Phase 3 writers are live but divergence blocks "
                          "Phase 4 cleanup (deleting dead git-claim code). "
                          "Resolve the divergence first.",
                "next": [
                    "Read recent_divergences in this panel; classify per "
                    "ree-v3/coordinator/SOAK_LOG.md.",
                    "If a worker is still in git/shadow mode, drain it "
                    "(do not run a mixed-authority fleet).",
                    "Fix root cause before resuming workers.",
                ],
            }
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
        if mode == "coordinator":
            return {
                "phase": 3,
                "phase_label": "Phase 3 -- writers live (no fresh heartbeats)",
                "parallel": "Coordinator owns claims; sync_daemon is sole "
                            "git writer (Phase 3 live as of 2026-05-29). "
                            "No worker has heartbeated inside the "
                            "freshness window.",
                "assess": ("Phase-3 mutex + writers healthy (div=%d) but "
                           "workers are not reporting -- runners may be "
                           "down, paused, or wedged." % div),
                "retire": "Writer rows below should still be ticking "
                          "(phase3_heartbeat_writer runs on a clock, not "
                          "on worker traffic). If they ARE ticking, the "
                          "issue is worker-side; if NOT, the writer is "
                          "wedged too -- check journal_tail in the panel.",
                "next": [
                    "Check each runner: systemctl status ree-runner on "
                    "clouds; ps/launchctl on the laptop.",
                    "Clear stale stop commands and restart drained runners.",
                    "Confirm COORDINATION_MODE=coordinator on every "
                    "active worker (no mixed-authority fleet).",
                ],
            }
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
        # Steady-state Phase 3: HEALTHY verdict + writer rows below are the
        # whole panel. Operators only need a pointer to the troubleshooting
        # guide if a row goes red. Reference unused locals to satisfy linters.
        _ = div
        return {
            "phase": 3,
            "phase_label": "",
            "parallel": "",
            "assess": "",
            "next": [
                "If a writer row goes red, see OPERATOR_GUIDE.md "
                "'What to do when a row goes red'.",
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
                          "COORDINATOR_LOCAL_TOKEN",
                "guide": _shadow_operator_guide("NOT_CONFIGURED")}
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
                "detail": f"HTTP {exc.code} from coordinator",
                "guide": _shadow_operator_guide("UNREACHABLE")}
    except Exception as exc:  # noqa: BLE001 -- must not crash the request
        return {"verdict": "UNREACHABLE", "color": "red",
                "detail": repr(exc),
                "guide": _shadow_operator_guide("UNREACHABLE")}
    # Filter stale machines from the coordinator response before returning.
    # Uses the same TTL as read_machines() so both views are consistent.
    from datetime import datetime as _dt, timezone as _tz
    _stale_exclude_s = (
        float(os.environ.get("MACHINE_STALE_EXCLUDE_HOURS", "6")) * 3600
    )
    _now_utc = _dt.now(_tz.utc)

    def _shadow_machine_fresh(m: dict) -> bool:
        ls = m.get("last_seen") or ""
        if not ls:
            return True  # no timestamp -> keep (may be newly provisioned)
        try:
            dt = _dt.fromisoformat(ls.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=_tz.utc)
            return (_now_utc - dt).total_seconds() <= _stale_exclude_s
        except ValueError:
            return True

    fresh_machines = [m for m in st.get("machines", [])
                      if _shadow_machine_fresh(m)]

    # Recompute verdict on the filtered machines list so the status card
    # reflects the same set the caller will see.
    st_filtered = dict(st)
    st_filtered["machines"] = fresh_machines
    verdict, color = _shadow_verdict(st_filtered)
    guide = _shadow_operator_guide(verdict, st_filtered)
    return {"verdict": verdict, "color": color,
            "mode": st.get("mode"),
            "total_claims": st.get("total_claims", 0),
            "divergences": st.get("divergences", 0),
            "adjusted_divergences": st.get(
                "adjusted_divergences",
                st.get("divergences_blocking", st.get("divergences", 0))),
            "divergences_explained": st.get("divergences_explained", 0),
            "experiments_in_mirror": st.get("experiments_in_mirror", 0),
            "machines": fresh_machines,
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
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_RESULT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_QUEUE_PUSH": "1",
        # Suppress the LOCAL heartbeat + commands file writes too. The
        # writer publishes the canonical runner_heartbeats/<host>.json
        # from the coordinator DB; without this flag, the runner's local
        # write conflicts with the writer-pulled version on every
        # auto-sync `git pull REE_assembly` and leaves UU markers that
        # block subsequent pulls until a human clears them. The flag's
        # docstring frames it as hub-only, but the same UU happens on any
        # worker's local checkout -- the "hub-only" guidance was scoped
        # to *writer-side* corruption, not worker-local conflicts.
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_WRITE": "1",
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
    coord_health_url = url.rstrip("/") + "/health"

    hub_flip = (
        "sudo sed -i 's/^COORDINATOR_MODE=.*/COORDINATOR_MODE=coordinator/' "
        "/etc/ree-coordinator.env && "
        "sudo sed -i 's/^SYNC_MODE=.*/SYNC_MODE=coordinator/' "
        "/etc/ree-coordinator.env && "
        "sudo systemctl restart ree-coordinator ree-sync-daemon && "
        "sleep 2 && curl -sf " + shlex.quote(coord_health_url)
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
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_RESULT_PUSH": "1",
        "PHASE3_DISABLE_RUNNER_QUEUE_PUSH": "1",
        # Claim-push gate (2026-06-03): coordinator /claim (db.try_claim,
        # atomic BEGIN IMMEDIATE) is the authoritative claim mutex in
        # coordinator mode, so the legacy attempt_claim / release_claim
        # `claim:` commits to ree-v3/main are noise. Local queue claimed_by
        # write is preserved; only the commit/push is skipped.
        "PHASE3_DISABLE_RUNNER_CLAIM_PUSH": "1",
        # Suppress the LOCAL heartbeat + commands file writes too. The
        # writer publishes the canonical runner_heartbeats/<host>.json
        # from the coordinator DB; without this flag, the runner's local
        # write conflicts with the writer-pulled version on every
        # auto-sync `git pull REE_assembly` and leaves UU markers that
        # block subsequent pulls until a human clears them. The flag's
        # docstring frames it as hub-only, but the same UU happens on any
        # worker's local checkout -- the "hub-only" guidance was scoped
        # to *writer-side* corruption, not worker-local conflicts.
        "PHASE3_DISABLE_RUNNER_HEARTBEAT_WRITE": "1",
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

        # Launchd-supervised v3: unload the plist entirely so KeepAlive
        # does NOT respawn the runner after this clean exit. The Stop
        # button keeps its expected "really stop" meaning. To run the
        # runner again the user clicks Start, which re-bootstraps the
        # plist + kickstarts. If launchctl reports no PID (transition
        # state: plist installed but the running runner is an orphan
        # Popen child of a previous serve.py session), fall through to
        # the legacy Popen / ext_pid detection below so the Stop button
        # can still SIGTERM the orphan.
        if v == "v3" and _launchd_supervises_v3():
            target_pid = _launchd_pid()
            if target_pid is not None:
                # bootout sends SIGTERM (drain) and unloads the plist.
                # The runner finishes the current experiment then exits,
                # with no respawn. Return immediately -- drain may take
                # minutes.
                ok, note = _launchd_bootout()
                if not ok:
                    return {"status": "error", "message": note}
                print(f"[serve] {cfg['label']} drain requested via "
                      f"launchd bootout (PID {target_pid}; {note})",
                      flush=True)
                return {"status": "draining", "pid": target_pid,
                        "substrate": v, "supervisor": "launchd"}
            # No launchd-managed runner -- fall through to legacy paths.

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

        # Launchd-supervised v3: SIGKILL via launchctl, then bootout to
        # prevent KeepAlive respawn. force_stop semantics are "no drain,
        # no respawn, gone now". If launchctl reports no PID, fall
        # through to legacy Popen / ext_pid detection so we can still
        # kill an orphan from a previous serve.py session.
        if v == "v3" and _launchd_supervises_v3():
            target_pid = _launchd_pid()
            if target_pid is not None:
                _launchd_kill("KILL")
                ok, note = _launchd_bootout()
                print(f"[serve] {cfg['label']} force-killed via launchd "
                      f"(PID {target_pid}; {note})", flush=True)
                return {"status": "stopped", "pid": target_pid,
                        "substrate": v, "supervisor": "launchd"}
            # No launchd-managed runner -- fall through to legacy paths.

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


def _queue_items_from_raw(data: dict, ver: str) -> list[dict]:
    """Normalize queue JSON items for explorer APIs."""
    items = []
    for item in data.get("items", []):
        qid = item.get("queue_id", "")
        claim_ids = item.get("claim_ids")
        claim_id = item.get("claim_id", "")
        if not claim_id and isinstance(claim_ids, list) and claim_ids:
            claim_id = claim_ids[0]
        items.append({
            "queue_id": qid,
            "claim_id": claim_id,
            "title": item.get("title", ""),
            "description": item.get("description", item.get("note", "")),
            "status": item.get("status", "pending"),
            "script": item.get("script", ""),
            "estimated_minutes": item.get("estimated_minutes"),
            "machine_affinity": item.get("machine_affinity", ""),
            "priority": item.get("priority"),
            "claimed_by": item.get("claimed_by"),
            "ree_version": ver,
        })
    return items


def read_queue(ver: str) -> dict:
    """Read experiment_queue.json for a substrate. Queue file is authoritative for status."""
    if ver not in RUNNERS:
        return {"error": f"Unknown substrate: {ver}"}
    qf = RUNNERS[ver]["queue_file"]
    if not qf.exists():
        return {"items": [], "ver": ver, "source": "file"}
    try:
        data = json.loads(qf.read_text())
    except Exception:
        return {"items": [], "ver": ver, "source": "file"}

    return {
        "items": _queue_items_from_raw(data, ver),
        "ver": ver,
        "source": "file",
    }


_COORD_QUEUE_CACHE: dict = {
    "t": 0.0,
    "ok": False,
    "payload": {},
    "last_good": {},
}
_COORD_QUEUE_LOCK = threading.Lock()
_COORD_QUEUE_TTL_SECONDS = 15.0
_COORD_QUEUE_FAILURE_TTL_SECONDS = 3.0


def read_queue_live(ver: str = "v3") -> dict:
    """Active queue from coordinator DB when reachable; else local file mirror."""
    file_payload = read_queue(ver)
    if ver != "v3":
        return file_payload

    cfg = _load_coordinator_cfg()
    url = (cfg.get("COORDINATOR_URL") or "").rstrip("/")
    tok = cfg.get("COORDINATOR_LOCAL_TOKEN") or ""
    if not url or not tok:
        return file_payload

    import urllib.error
    import urllib.request

    now = time.monotonic()
    with _COORD_QUEUE_LOCK:
        age = now - _COORD_QUEUE_CACHE["t"]
        ttl = (_COORD_QUEUE_TTL_SECONDS if _COORD_QUEUE_CACHE.get("ok")
               else _COORD_QUEUE_FAILURE_TTL_SECONDS)
        if age < ttl and _COORD_QUEUE_CACHE.get("ok"):
            return dict(_COORD_QUEUE_CACHE["payload"])

    payload = dict(file_payload)
    fetch_ok = False
    try:
        req = urllib.request.Request(
            url + "/queue/active",
            headers={"Authorization": "Bearer " + tok},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=4) as resp:
            live = json.loads(resp.read().decode("utf-8"))
        raw_items = live.get("items") or []
        items = _queue_items_from_raw({"items": raw_items}, ver)
        payload = {
            "items": items,
            "ver": ver,
            "source": live.get("source") or "coordinator",
            "now_utc": live.get("now_utc"),
        }
        fetch_ok = True
    except (urllib.error.URLError, OSError,
            json.JSONDecodeError, ValueError):
        fetch_ok = False

    with _COORD_QUEUE_LOCK:
        _COORD_QUEUE_CACHE["t"] = time.monotonic()
        if fetch_ok:
            _COORD_QUEUE_CACHE["ok"] = True
            _COORD_QUEUE_CACHE["payload"] = payload
            _COORD_QUEUE_CACHE["last_good"] = payload
            return dict(payload)
        _COORD_QUEUE_CACHE["ok"] = False
        lg = _COORD_QUEUE_CACHE.get("last_good") or {}
        if lg:
            return dict(lg)
    return file_payload


# ── Timeline builder ─────────────────────────────────────────────────────────

def _tl_utc_now() -> str:
    return _utc_now_compact()


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
    """Load claims list from claims.yaml. Returns [] on failure.

    Cached on (mtime_ns, size) of claims.yaml -- NOT a TTL -- for the same reason
    as _load_claim_evidence_claims() above: a governance run or a manual
    claims.yaml edit must be visible on the very next request, and a time-based
    cache would reintroduce the staleness the explorer's no-cache posture exists
    to prevent. The returned list is SHARED and must be treated as READ-ONLY;
    it is not deep-copied (the parse it avoids is ~2.0s per call).
    """
    try:
        st = _TL_CLAIMS_YAML.stat()
    except OSError:
        _TL_CLAIMS_CACHE["key"] = None
        _TL_CLAIMS_CACHE["claims"] = []
        return []
    key = (st.st_mtime_ns, st.st_size)
    if _TL_CLAIMS_CACHE["key"] != key:
        try:
            if _YAML_OK:
                raw = _yaml.safe_load(_TL_CLAIMS_YAML.read_text())
                claims_list = raw.get("claims", []) if isinstance(raw, dict) else (raw or [])
            else:
                # Minimal regex fallback if PyYAML unavailable
                claims_list = []
        except Exception:
            claims_list = []
        _TL_CLAIMS_CACHE["claims"] = claims_list or []
        _TL_CLAIMS_CACHE["key"] = key
    return _TL_CLAIMS_CACHE["claims"]


# --- /api/claims/summary ------------------------------------------------------
# derived_evidence_index:P2, plan section 7 row 1 -- plus the claims.yaml half the
# plan did not anticipate.
#
# WHAT THE EXPLORER DID BEFORE THIS ENDPOINT EXISTED. Every page load of the
# Claims Explorer fetched TWO large canonical files straight into the browser:
#   docs/claims/claims.yaml            6.44 MB, parsed with a hand-rolled regex
#   claim_evidence.v1.json            12.37 MB, for FOUR scalars per claim
# ~18.8 MB over the wire and both retained in JS memory, to end up with about a
# dozen small fields per claim. This endpoint serves exactly those fields.
#
# IT ALSO FIXES A CORRECTNESS BUG, and that is not a side benefit to gloss over.
# explorer.html's parseClaimsYaml() is a line-oriented regex scanner: it starts a
# NEW claim at any line whose first 10 characters contain `id: <ID>`, which also
# matches `id:` lines nested inside a claim's own prose/source blocks. Measured
# 2026-09-01 against a PyYAML parse of the same file: the browser parser yields
# 1025 "claims" of which ~31 are spurious mid-claim splits, MISSES 83 genuine
# registry entries whose id does not match its `[A-Z]{1,6}-\d{3}` shape
# (every GOV-*, SENT-*, SOC-HUM-*, and every lettered claim -- MECH-057a,
# SD-032b, ...), and MISATTRIBUTES fields across the bogus boundaries: 248 claims
# lost `v3_pending` entirely, 43 got the wrong `depends_on`, and 19/29/15 got the
# wrong claim_type/subject/status. Serving the real 1077 entries from a real YAML
# parse is therefore a VISIBLE change to the graph, deliberately made, not a
# transparent optimisation -- see the completion note on derived_evidence_index:P2.
#
# Cached on BOTH source keys (claims.yaml mtime/size AND the evidence source's),
# never a TTL -- same contract and same reason as _tl_load_claims() above.
_CLAIMS_SUMMARY_CACHE: dict = {"key": None, "payload": None}

# Mirrors explorer.html's normalizeDep(): strip a trailing comment and any
# trailing ',' / ']', then reduce to the first bare claim reference if one is
# present, else keep the stripped text. Replicated rather than simplified so a
# dependency edge drawn today keeps being drawn after the cutover.
_DEP_REF_RE = re.compile(r"\b(INV|ARC|MECH|IMPL|Q)-\d{3}\b")


def _summary_normalize_dep(item) -> str:
    text = re.sub(r"#.*", "", str(item))
    text = re.sub(r"[,\]]+$", "", text).strip()
    m = _DEP_REF_RE.search(text)
    return m.group(0) if m else text


def _derived_db_key():
    """(mtime_ns, size) of the derived read-model, or None when it is absent.

    Absent is a NORMAL state, never an error: the DB is disposable by contract
    (see derived_evidence_db.py). Callers fall back to claim_evidence.v1.json.
    """
    try:
        st = _DERIVED_DB_PATH.stat()
    except OSError:
        return None
    return (st.st_mtime_ns, st.st_size)


def _claim_evidence_fields() -> tuple:
    """({claim_id: {4 evidence fields}}, source_label).

    Prefers the derived SQLite read-model (a 5-column scan over 574 rows) and
    falls back to the shared 12 MB claim_evidence.v1.json cache. The fallback is
    load-bearing, not decorative: a checkout that has never run the indexer, or
    one where the derived file was deleted, must still render the explorer.
    """
    if _derived_db_key() is not None:
        try:
            sys.path.insert(0, str(SERVE_DIR / "evidence" / "experiments" / "scripts"))
            import derived_evidence_db as _dedb  # noqa: WPS433
            conn = _dedb.open_readonly(SERVE_DIR / "evidence" / "experiments")
            if conn is not None:
                try:
                    rows = _dedb.claim_summary_rows(conn)
                finally:
                    conn.close()
                if rows:
                    return rows, "derived_sqlite"
        except Exception:
            pass
    out = {}
    for cid, ev in (_load_claim_evidence_claims() or {}).items():
        if not isinstance(ev, dict):
            continue
        out[cid] = {
            "genuine_exp_count": ev.get("genuine_exp_count") or 0,
            "evidence_quadrant": ev.get("evidence_quadrant") or None,
            "experimental_confidence_decoupled": (
                ev.get("experimental_confidence_decoupled")
                if isinstance(ev.get("experimental_confidence_decoupled"), (int, float)) else None
            ),
            "literature_confidence_parallel": (
                ev.get("literature_confidence_parallel")
                if isinstance(ev.get("literature_confidence_parallel"), (int, float)) else None
            ),
        }
    return out, "claim_evidence_json"


def build_claims_summary() -> dict:
    """Compact per-claim summary for the Claims Explorer graph. Cached; read-only."""
    try:
        st = _TL_CLAIMS_YAML.stat()
        yaml_key = (st.st_mtime_ns, st.st_size)
    except OSError:
        yaml_key = None
    key = (yaml_key, _derived_db_key())
    if _CLAIMS_SUMMARY_CACHE["key"] == key and _CLAIMS_SUMMARY_CACHE["payload"] is not None:
        return _CLAIMS_SUMMARY_CACHE["payload"]

    evidence, evidence_source = _claim_evidence_fields()
    claims = []
    for c in _tl_load_claims():
        if not isinstance(c, dict):
            continue
        cid = str(c.get("id") or "").strip()
        if not cid:
            continue
        ev = evidence.get(cid) or {}
        claims.append({
            "id": cid,
            "claim_type": str(c.get("claim_type") or "").strip(),
            "subject": str(c.get("subject") or "").strip(),
            "polarity": str(c.get("polarity") or "").strip(),
            "status": str(c.get("status") or "").strip(),
            "location": str(c.get("location") or "").strip(),
            "implementation_phase": str(c.get("implementation_phase") or "").strip(),
            "v3_pending": bool(c.get("v3_pending")),
            "depends_on": [
                d for d in (_summary_normalize_dep(x) for x in (c.get("depends_on") or [])) if d
            ],
            # GOV-EDGE-1 (2026-09-04): the UNDIRECTED reciprocal-coupling layer,
            # split out of depends_on (which is now a prerequisite DAG). Written
            # on both endpoints in claims.yaml; the explorer draws it without an
            # arrowhead and never treats it as a dependency.
            "coupled_with": [
                d for d in (_summary_normalize_dep(x) for x in (c.get("coupled_with") or [])) if d
            ],
            "genuine_exp_count": ev.get("genuine_exp_count") or 0,
            "evidence_quadrant": ev.get("evidence_quadrant"),
            "experimental_confidence_decoupled": ev.get("experimental_confidence_decoupled"),
            "literature_confidence_parallel": ev.get("literature_confidence_parallel"),
        })
    claims.sort(key=lambda c: c["id"])
    payload = {
        "schema_version": "claims_summary/v1",
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_claims": len(claims),
        "evidence_source": evidence_source,
        "claims": claims,
    }
    _CLAIMS_SUMMARY_CACHE["key"] = key
    _CLAIMS_SUMMARY_CACHE["payload"] = payload
    return payload


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
        # Derived read-model when built, else the JSON cache. `recent_entries`
        # is stored VERBATIM in claim_rollup, so this series is byte-identical
        # either way -- see the column comment in derived_evidence_db.py.
        for cid, cdata in _claim_rollup_for_serving().items():
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

    # BaseHTTPRequestHandler only sets self.path inside parse_request(). A malformed
    # request line makes parse_request() bail BEFORE that assignment and go straight to
    # send_error() -> log_error() -> log_message(), so any self.path read on that path
    # raised AttributeError and killed the connection's handler thread. Port 8000 is
    # bound on 0.0.0.0 on the hub, so internet scanners tripped this routinely.
    # A class-level default fixes every reader at once, pre-parse.
    path = ""

    def do_GET(self):
        path = urlparse(self.path).path
        # /mobile.css -- the one shared stylesheet. Every dashboard page keeps its
        # own inline <style> (the house convention); this carries ONLY the
        # narrow-viewport hardening, which is identical for all of them and would
        # otherwise be 16 copies to keep in sync. Same no-cache headers as the HTML
        # pages so a phone reload always gets the current file.
        # Served before any other route so a stylesheet request never falls through
        # to the SimpleHTTPRequestHandler default handler.
        if path == "/mobile.css":
            css_file = SERVE_DIR / "mobile.css"
            if css_file.exists():
                content = css_file.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/css; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.end_headers()
                self.wfile.write(content)
            else:
                # A missing stylesheet must not blank a page: the pages degrade to
                # their own inline CSS (i.e. to the pre-2026-08-20 desktop-only
                # rendering), which is why 404 here is safe rather than fatal.
                self.send_response(404)
                self.end_headers()
            return
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
        if path == "/api/coordinator/phase3/preflight":
            body = json.dumps(run_phase3_preflight_summary()).encode()
            self._json_response(body)
            return
        if path == "/api/coordinator/phase3/writers":
            body = json.dumps(run_phase3_writers_summary()).encode()
            self._json_response(body)
            return
        if path == "/api/workspace/health":
            body = json.dumps(run_workspace_health_summary()).encode()
            self._json_response(body)
            return
        if path == "/api/docs/index":
            body = json.dumps(read_docs_index()).encode()
            self._json_response(body)
            return
        if path == "/api/usage":
            body = json.dumps(compute_claude_usage()).encode()
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
        if path == "/api/code_atlas":
            body = json.dumps(read_code_atlas(), default=str).encode()
            self._json_response(body)
            return
        if path in ("/code-atlas", "/code_atlas", "/code_atlas.html"):
            atlas_page = SERVE_DIR / "code_atlas.html"
            if atlas_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(atlas_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
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
        if path == "/api/fleet/summary":
            # Compact workload readout for the corner dock: what is queued, and
            # what durable work is outstanding. Replaces the Claude-usage panel,
            # which was a documented dead end -- the real plan-limit % is only
            # in API response headers at request time and is not exposed to any
            # local API or file, so that panel could never show the number
            # anyone actually wanted.
            #
            # Reads the three files directly rather than shelling out to the
            # audit scripts (/api/workspace/health does that, with a 20s
            # subprocess and a 60s cache). This is a 60s-poll dock panel; it
            # must be cheap and must never block on a slow audit.
            summary = {"ok": True}
            try:
                q = read_queue("v3") or {}
                items = q.get("items") or []
                by_status = {}
                for it in items:
                    st = it.get("status") or "?"
                    by_status[st] = by_status.get(st, 0) + 1
                summary["queue"] = {
                    "total": len(items),
                    "pending": by_status.get("pending", 0),
                    "claimed": by_status.get("claimed", 0),
                }
            except Exception as exc:  # noqa: BLE001
                summary["queue"] = {"error": str(exc)}
            try:
                chips = (read_chips() or {}).get("chips") or []
                open_chips = [c for c in chips if c.get("status") == "open"]
                summary["chips"] = {
                    "open": len(open_chips),
                    "open_work": sum(1 for c in open_chips
                                     if c.get("kind") == "work"),
                    "open_decision": sum(1 for c in open_chips
                                         if c.get("kind") == "decision"),
                    # A claimed-but-open chip is being worked right now; that is
                    # distinct from status, which only records resolution.
                    "claimed": sum(1 for c in open_chips if c.get("claimed_by")),
                }
            except Exception as exc:  # noqa: BLE001
                summary["chips"] = {"error": str(exc)}
            try:
                cf = UMBRELLA_DIR / "TASK_CLAIMS.json"
                cdata = json.loads(cf.read_text(encoding="utf-8"))
                claims = cdata.get("claims") or cdata.get("items") or []
                summary["claims"] = {
                    "active": sum(1 for c in claims
                                  if c.get("status") == "active"),
                    "total": len(claims),
                }
            except Exception as exc:  # noqa: BLE001
                summary["claims"] = {"error": str(exc)}
            body = json.dumps(summary, indent=2, default=str).encode()
            self._json_response(body)
            return
        if path in ("/api/chips", "/api/chips/prompt"):
            from urllib.parse import parse_qs  # noqa: WPS433
            qs = parse_qs(urlparse(self.path).query)
        if path == "/api/chips":
            # Projected to the panel's columns -- see read_chips_projected().
            # ?full=1 returns the raw ledger for anything that needs every field.
            if qs.get("full", ["0"])[0] in ("1", "true", "yes"):
                body = json.dumps(read_chips(), indent=2, default=str).encode()
                self._json_response(body)
                return
            payload, etag = read_chips_projected()
            if self.headers.get("If-None-Match") == etag:
                self.send_response(304)
                self.send_header("ETag", etag)
                self.end_headers()
                return
            body = json.dumps(payload, default=str).encode()
            self._json_response(body, extra_headers={"ETag": etag})
            return
        if path == "/api/chips/prompt":
            ref = (qs.get("chip_ref", [""])[0] or "").strip()
            prompt = read_chip_prompt(ref) if ref else None
            body = json.dumps(
                {"chip_ref": ref, "prompt": prompt}, default=str
            ).encode()
            self._json_response(body, status=200 if prompt else 404)
            return
        if path == "/api/workset/assignments":
            try:
                sys.path.insert(0, str(SERVE_DIR / "scripts"))
                import igw_assignments_lib as _ial  # noqa: WPS433
                payload = {
                    "active": _ial.active_entries(),
                    "agent_kinds": sorted(_ial.VALID_AGENTS),
                }
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "error", "message": str(exc)}
            body = json.dumps(payload, indent=2, default=str).encode()
            self._json_response(body)
            return
        if path == "/api/workset/recent_activity":
            # Released-assignment events within the last `hours` (default 24).
            # Used by the workset "Recent activity" panel.
            from urllib.parse import parse_qs
            qs = parse_qs(urlparse(self.path).query)
            try:
                hours = float(qs.get("hours", ["24"])[0])
            except (TypeError, ValueError):
                hours = 24.0
            hours = max(0.5, min(hours, 24 * 30))  # clamp 0.5h .. 30d
            try:
                sys.path.insert(0, str(SERVE_DIR / "scripts"))
                import igw_assignments_lib as _ial  # noqa: WPS433
                releases = _ial.recent_releases(hours=hours)
                payload = {
                    "hours": hours,
                    "count": len(releases),
                    "releases": releases,
                }
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "error", "message": str(exc)}
            body = json.dumps(payload, indent=2, default=str).encode()
            self._json_response(body)
            return
        if path == "/api/closure":
            body = json.dumps(read_closure(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path == "/api/progress":
            body = json.dumps(read_progress(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path in ("/progress", "/progress.html"):
            progress_page = SERVE_DIR / "progress.html"
            if progress_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(progress_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        # /insights-report and /dual-insights-report -- static snapshots regenerated by
        # the /dual-insights skill each run (REE_assembly/{insights,dual_insights}_report.html).
        # Same static-file-with-no-cache pattern as /progress, /machines, /igw above --
        # these are periodic snapshots, not live dashboards, so no matching /api/* endpoint.
        if path in ("/insights-report", "/insights-report.html"):
            insights_page = SERVE_DIR / "insights_report.html"
            if insights_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(insights_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path in ("/dual-insights-report", "/dual-insights-report.html"):
            dual_insights_page = SERVE_DIR / "dual_insights_report.html"
            if dual_insights_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(dual_insights_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
            return
        if path == "/api/igw/ledger":
            body = json.dumps(read_igw_ledger(), indent=2, default=str).encode()
            self._json_response(body)
            return
        if path == "/api/status_history":
            # status_history_plane:SHP-3 (Q2=both): collapsed-plan live: head +
            # appended status_snapshot/v1 history slice for a node or claim.
            from urllib.parse import parse_qs
            qs = parse_qs(urlparse(self.path).query)
            node_id = (qs.get("node", [""])[0] or "").strip()
            claim_id = (qs.get("claim", [""])[0] or "").strip()
            body = json.dumps(
                query_status_history(node_id or None, claim_id or None),
                indent=2, default=str,
            ).encode()
            self._json_response(body)
            return
        if path in ("/igw", "/igw.html"):
            igw_page = SERVE_DIR / "igw.html"
            if igw_page.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(igw_page.read_bytes())
            else:
                self.send_response(404)
                self.end_headers()
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
        if path == "/api/queue/live":
            body = json.dumps(read_queue_live("v3")).encode()
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
        if path == "/api/claims/summary":
            self._json_response(json.dumps(build_claims_summary()).encode())
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
                "pending_review_count": _closure_pending_review_count(),
            }).encode()
            self._json_response(body)
            return
        if path == "/api/experiment/detail":
            # Curated, size-bounded manifest detail for a Completed experiment
            # card's expand panel. Resolves the on-disk manifest by script_name
            # (preferred) or queue_id; output_file from the card is a foreign
            # absolute path and is not consulted here.
            from urllib.parse import parse_qs
            qs = parse_qs(urlparse(self.path).query)
            script_name = (qs.get("script", [""])[0] or "").strip()
            queue_id = (qs.get("queue_id", [""])[0] or "").strip()
            mf = _find_manifest_file(script_name, queue_id)
            if mf is None:
                body = json.dumps({
                    "found": False,
                    "message": "No manifest found on disk for this experiment.",
                }).encode()
                self._json_response(body)
                return
            try:
                m = json.loads(mf.read_text())
            except Exception as exc:  # noqa: BLE001
                body = json.dumps({
                    "found": False,
                    "message": f"Manifest unreadable: {exc}",
                }).encode()
                self._json_response(body)
                return
            verdict, timestamp, _ = _normalize_manifest_fields(m)
            try:
                rel = str(mf.relative_to(SERVE_DIR))
            except ValueError:
                rel = mf.name
            # Inverse region join: this run's claims -> the brain-map regions they
            # exercise. Read off the manifest itself (not claim_evidence.v1.json)
            # so a run too fresh to be indexed still resolves. Empty on any failure.
            m_claim_ids = [
                str(x) for x in (m.get("claim_ids_tested") or m.get("claim_ids") or []) if x
            ]
            body = json.dumps({
                "found": True,
                "queue_id": m.get("queue_id", queue_id),
                "run_id": m.get("run_id", ""),
                "outcome": verdict,
                "timestamp": timestamp,
                "evidence_direction": m.get("evidence_direction"),
                "manifest_path": rel,
                "claim_ids": m_claim_ids,
                "regions": _regions_for_claim_ids(m_claim_ids),
                "detail": build_manifest_detail(m),
            }, default=str).encode()
            self._json_response(body)
            return
        # Auto-linkify Code Atlas references in served Markdown prose. The doc
        # viewer fetches these .md files raw and renders them client-side; we
        # rewrite bare file / class / EXQ / claim mentions into atlas anchors on
        # the way out. Strictly additive: any failure (or an unavailable atlas)
        # falls straight through to the normal static handler.
        if path.endswith(".md"):
            try:
                fs = Path(self.translate_path(self.path)).resolve()
                serve_root = SERVE_DIR.resolve()
                if fs.is_file() and (serve_root == fs or serve_root in fs.parents):
                    linked = linkify_code_atlas(fs.read_text(encoding="utf-8"))
                    body = linked.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/markdown; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                    self.end_headers()
                    if self.command != "HEAD":
                        self.wfile.write(body)
                    return
            except Exception:
                pass  # fall through to the default static handler
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
                def _toggle(data):
                    dirs = data.setdefault("discussed_experiment_dirs", [])
                    if discussed and dir_name not in dirs:
                        dirs.append(dir_name)
                    elif not discussed and dir_name in dirs:
                        dirs.remove(dir_name)
                data = update_review_tracker(_toggle)
                result = {
                    "status": "ok",
                    "discussed_experiment_dirs": data.get("discussed_experiment_dirs", []),
                }
            else:
                result = {"status": "error", "message": "missing dir_name"}
        elif path in ("/api/workset/assign", "/api/workset/release"):
            length = int(self.headers.get("Content-Length", 0))
            try:
                payload = json.loads(self.rfile.read(length) or b"{}")
            except Exception as exc:
                body = json.dumps({"status": "error", "message": f"bad json: {exc}"}).encode()
                self._json_response(body, status=400)
                return
            try:
                sys.path.insert(0, str(SERVE_DIR / "scripts"))
                import igw_assignments_lib as _ial  # noqa: WPS433
            except Exception as exc:
                body = json.dumps({"status": "error", "message": f"lib import failed: {exc}"}).encode()
                self._json_response(body, status=500)
                return
            ws = read_workset()
            items_by_id = {it.get("id"): it for it in ws.get("items", [])}
            items_by_hash = {it.get("stable_hash"): it for it in ws.get("items", []) if it.get("stable_hash")}
            agent = (payload.get("agent") or "").strip()
            agent_label = payload.get("agent_label")
            if path == "/api/workset/assign":
                igw_id = (payload.get("igw_id") or "").strip()
                item = items_by_id.get(igw_id)
                if not item:
                    body = json.dumps({"status": "error", "message": f"unknown igw_id {igw_id!r}"}).encode()
                    self._json_response(body, status=404)
                    return
                # Guard: if this (item, agent, label) already has an active
                # assignment, treat as idempotent no-op rather than double-write.
                sh = _ial.stable_hash_item(item)
                already = [
                    e for e in _ial.active_entries()
                    if e["stable_hash"] == sh
                    and e["agent"] == agent
                    and (e.get("agent_label") or "") == (agent_label or "")
                ]
                if already:
                    result = {"status": "noop", "message": "already assigned", "entry": already[0]}
                else:
                    try:
                        entry = _ial.assign(
                            item,
                            agent=agent,
                            agent_label=agent_label,
                            source=payload.get("source") or "manual_ui",
                            note=payload.get("note"),
                        )
                        # Commit + push immediately so the heartbeat's hourly
                        # `git checkout -f -B master origin/master` resets the
                        # working tree onto a copy of master that ALREADY
                        # contains this assignment. Without this push the
                        # in-flight uncommitted assign is wiped on the next
                        # heartbeat tick.
                        push_result = _commit_and_push_assignments(
                            f"workset: assign IGW {igw_id} -> {agent}"
                        )
                        result = {"status": "ok", "entry": entry, "git": push_result}
                    except ValueError as exc:
                        body = json.dumps({"status": "error", "message": str(exc)}).encode()
                        self._json_response(body, status=400)
                        return
            else:  # /api/workset/release
                stable_hash_val = (payload.get("stable_hash") or "").strip()
                if not stable_hash_val and payload.get("igw_id"):
                    item = items_by_id.get(payload["igw_id"])
                    if item:
                        stable_hash_val = _ial.stable_hash_item(item)
                if not stable_hash_val:
                    body = json.dumps({"status": "error", "message": "need stable_hash or igw_id"}).encode()
                    self._json_response(body, status=400)
                    return
                try:
                    entry = _ial.release(
                        stable_hash_val,
                        agent=agent,
                        agent_label=agent_label,
                        released_by=payload.get("released_by") or "manual_ui",
                        reason=payload.get("reason"),
                    )
                except ValueError as exc:
                    body = json.dumps({"status": "error", "message": str(exc)}).encode()
                    self._json_response(body, status=400)
                    return
                if entry is None:
                    result = {"status": "noop", "message": "no active assignment to release"}
                else:
                    # See assign-side comment: commit+push immediately so the
                    # heartbeat reset can't wipe the release event.
                    push_result = _commit_and_push_assignments(
                        f"workset: release IGW assignment {stable_hash_val[:8]} -> {agent}"
                    )
                    result = {"status": "ok", "entry": entry, "git": push_result}
            body = json.dumps(result).encode()
            self._json_response(body, status=200)
            return
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
            # Phase 3 (OFF_GIT complete, 2026-06-03): the coordinator is THE
            # remote-control command channel. Issue via the coordinator when it
            # is configured; the legacy git command-file is written ONLY as a
            # fallback when the coordinator is NOT configured (a no-coordinator
            # / pre-Phase-3 setup). A configured-but-unreachable coordinator
            # fails loudly so the operator retries -- we do NOT silently write a
            # git command-file that OFF_GIT workers (the whole fleet) would
            # ignore, which would make a dropped command look issued.
            c_attempted, c_ok, c_detail = _coordinator_issue_command(
                host, kind, args, issued_by)
            if c_attempted:
                ok = c_ok
                cmd = c_detail if c_ok else None
                if c_ok and isinstance(c_detail, dict):
                    msg = f"issued via coordinator (id={c_detail.get('id')})"
                else:
                    msg = f"coordinator issue failed: {c_detail}"
                channel = "coordinator"
            else:
                # Coordinator not configured -> legacy git command-file.
                ok, msg, cmd = append_machine_command(host, kind, args, issued_by)
                channel = "git_command_file"
            result = {
                "status": "ok" if ok else "error",
                "message": msg,
                "command": cmd,
                "machine": host,
                "channel": channel,
                "coordinator": {"attempted": c_attempted, "ok": c_ok},
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

    def _json_response(self, body: bytes, status: int = 200,
                       extra_headers: dict = None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        for name, value in (extra_headers or {}).items():
            self.send_header(name, value)
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
        # getattr guard is belt-and-braces alongside the Handler.path class default:
        # log_message is reachable before parse_request() has set self.path.
        if "/api/" in (getattr(self, "path", "") or ""):
            super().log_message(fmt, *args)


# ── Main ─────────────────────────────────────────────────────────────────────

def ensure_mobile_tmux_session():
    """Best-effort: make sure a detached tmux session named 'ree' exists so the
    user can attach Claude Code from the phone (Blink -> ssh/mosh -> tmux attach
    -t ree) without re-running scripts/claude_mobile.sh by hand after a reboot.

    Idempotent and never fatal: no-op if tmux is not installed or the session
    already exists. Opt out with REE_MOBILE_SESSION=0. See docs/mobile_access.md.
    """
    if os.environ.get("REE_MOBILE_SESSION", "1") == "0":
        return
    session = "ree"
    workdir = str(SERVE_DIR.parent)  # REE_Working (umbrella)
    try:
        has = subprocess.run(["tmux", "has-session", "-t", session],
                             capture_output=True, timeout=5)
        if has.returncode == 0:
            return  # already running -- leave it (and any work inside) alone
        subprocess.run(["tmux", "new-session", "-d", "-s", session, "-c", workdir],
                       capture_output=True, timeout=5)
        print(f"[serve] mobile: ensured tmux session '{session}' "
              f"(attach from phone: tmux attach -t {session})", flush=True)
    except FileNotFoundError:
        pass  # tmux not installed -- mobile Claude Code path just unavailable
    except Exception as e:
        print(f"[serve] mobile: tmux ensure skipped ({e})", flush=True)


def main():
    parser = argparse.ArgumentParser(description="REE Claims Explorer Server")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Port to listen on (default: {DEFAULT_PORT})")
    parser.add_argument("--python", type=str, default=None,
                        help="Python executable to use for runners "
                             "(default: auto-detect via REE_PYTHON env or known paths)")
    parser.add_argument("--bind", action="append", default=None, metavar="ADDR",
                        help="Address to listen on (repeatable). Default: 0.0.0.0 "
                             "(all interfaces, unchanged). For WireGuard + localhost "
                             "only, pass --bind <MAC_WG_IP> --bind 127.0.0.1 "
                             "(see docs/mobile_access.md).")
    args = parser.parse_args()

    if args.python:
        for cfg in RUNNERS.values():
            cfg["python"] = args.python

    _detect_existing_runners()
    os.chdir(SERVE_DIR)
    ensure_mobile_tmux_session()  # phone Claude Code session always ready

    # Bind addresses: default 0.0.0.0 (all interfaces, backward-compatible).
    # Pass --bind one or more times to restrict (e.g. WireGuard IP + localhost).
    bind_addrs = args.bind if args.bind else ["0.0.0.0"]

    class _QuietThreadingHTTPServer(http.server.ThreadingHTTPServer):
        """ThreadingHTTPServer that swallows benign client-disconnect errors.

        A browser tab polling an endpoint (e.g. /api/usage) that is closed,
        navigated away, or refreshed mid-response drops the socket, so the
        handler's wfile.write() raises BrokenPipeError / ConnectionResetError
        deep in http.server. Those are harmless -- the client simply left --
        but the base handler prints a full multi-line traceback per hit, which
        floods the runner log. Suppress just those two; re-raise everything else.
        """
        def handle_error(self, request, client_address):
            exc = sys.exc_info()[1]
            if isinstance(exc, (BrokenPipeError, ConnectionResetError)):
                return
            super().handle_error(request, client_address)

    servers = []
    for addr in bind_addrs:
        servers.append(_QuietThreadingHTTPServer((addr, args.port), Handler))
    server = servers[0]  # primary (foreground); extras serve in daemon threads

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
    print(f"[serve] Listening on:  {', '.join(a + ':' + str(args.port) for a in bind_addrs)}", flush=True)
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
        # repo name -> monotonic timestamp of the first consecutive skipped pull.
        # Cleared on any successful pull. Lets the log report how long the
        # explorer has been serving stale evidence, which a per-cycle message
        # cannot: an 8-hour stall and a one-cycle blip looked identical before.
        stuck_since = {}

        def _pull_repo(repo):
            """One repo's pull cycle. A bare `return` means: on to the next repo.

            Extracted from the loop body so the caller can fault-isolate each
            repo individually -- see the try/except in the while loop below.
            """
            if not (repo / ".git").is_dir():
                return
            result = subprocess.run(
                ["git", "-C", str(repo), "pull", "--ff-only"],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode == 0:
                stuck_since.pop(repo.name, None)
                if "Already up to date" not in result.stdout:
                    print(f"[serve] git pull {repo.name}: {result.stdout.strip()}", flush=True)
                return
            # --ff-only failed. TWO distinct causes, which need different
            # remedies and used to print the same (often wrong) message:
            #
            #   A. NOT diverged (0 ahead), but a dirty working-tree file
            #      overlaps an incoming change, so the merge would clobber
            #      it. Retrying can NEVER clear this -- the dirty tree also
            #      skips the rebase below. It clears only when a session
            #      commits those paths. This is the common case here: the
            #      evidence/ derived artifacts are rewritten on origin by
            #      the phase3 writers AND held dirty by governance sessions.
            #   B. Genuinely diverged -- local un-pushed commits (e.g.
            #      igw-ledger automation on this Mac). Auto-heal by rebasing
            #      onto origin, but ONLY when the tree is clean. Never
            #      autostash: an autostash cycle here can transiently revert
            #      another session's uncommitted evidence/ or claims edits
            #      (see CLAUDE.md High-Contention Files).
            #
            # A dirty tree alone never blocks a fast-forward -- only a dirty
            # tree whose paths COLLIDE with the incoming diff does.
            branch = subprocess.run(
                ["git", "-C", str(repo), "symbolic-ref", "--short", "HEAD"],
                capture_output=True, text=True, timeout=30,
            ).stdout.strip() or "HEAD"
            counts = subprocess.run(
                ["git", "-C", str(repo), "rev-list", "--left-right", "--count",
                 f"origin/{branch}...HEAD"],
                capture_output=True, text=True, timeout=30,
            ).stdout.split()
            behind, ahead = (counts + ["?", "?"])[:2]
            dirty = subprocess.run(
                ["git", "-C", str(repo), "status", "--porcelain"],
                capture_output=True, text=True, timeout=30,
            ).stdout.strip()

            first = stuck_since.setdefault(repo.name, time.monotonic())
            mins = int((time.monotonic() - first) / 60)
            stale = f"; stale {mins}m" if mins >= 10 else ""

            if dirty:
                # git's own stderr names the exact blocking paths -- the one
                # piece of information that makes this actionable. It was
                # captured and discarded before.
                blockers = [ln.strip() for ln in result.stderr.splitlines()
                            if ln.startswith("\t")]
                detail = (f" blocked by: {', '.join(blockers[:6])}"
                          + (f" (+{len(blockers) - 6} more)" if len(blockers) > 6 else "")
                          ) if blockers else ""
                kind = ("diverged + local changes"
                        if ahead not in ("0", "?")
                        else f"behind {behind}, NOT diverged -- uncommitted paths block ff")
                print(f"[serve] git pull {repo.name}: {kind}; skipping{stale}.{detail}",
                      flush=True)
                return
            rebase = subprocess.run(
                ["git", "-C", str(repo), "pull", "--rebase"],
                capture_output=True, text=True, timeout=60,
            )
            if rebase.returncode == 0:
                stuck_since.pop(repo.name, None)
                print(f"[serve] git pull {repo.name}: rebased local commits onto origin", flush=True)
            else:
                subprocess.run(["git", "-C", str(repo), "rebase", "--abort"],
                               capture_output=True, text=True, timeout=30)
                print(f"[serve] git pull {repo.name}: diverged ({ahead} ahead/{behind} behind), "
                      f"rebase conflict -- manual merge needed{stale}", flush=True)

        # EVERY cycle is fault-isolated, per repo. This loop previously had NO
        # exception handling at all, so a single TimeoutExpired from any of the
        # git calls above -- unattended, every 5 minutes, against the two repos
        # that actually accumulate stale locks -- killed this thread
        # PERMANENTLY, after which the explorer served stale evidence forever
        # with nothing printed anywhere. One bad cycle must cost one cycle.
        while True:
            time.sleep(300)
            try:
                ensure_mobile_tmux_session()  # recreate the phone session if it died
            except Exception as exc:
                print(f"[serve] auto-pull: ensure_mobile_tmux_session failed: "
                      f"{type(exc).__name__}: {exc} -- continuing.", flush=True)
            for repo in repos:
                try:
                    _pull_repo(repo)
                except subprocess.TimeoutExpired as exc:
                    # Kept AHEAD of the generic handler because this is the one
                    # failure that used to damage the repo rather than just the
                    # thread: before graceful_timeout was wired in above, the
                    # stdlib SIGKILLed the git child and orphaned
                    # .git/index.lock. Name the repo and the command -- a silent
                    # producer is what made this take three sessions to narrow.
                    cmd = (" ".join(exc.cmd) if isinstance(exc.cmd, (list, tuple))
                           else str(exc.cmd))
                    print(f"[serve] auto-pull TIMEOUT: repo={repo.name} cmd={cmd!r} "
                          f"after {exc.timeout}s -- SIGTERM was sent first, so git "
                          f"should have unlinked .git/index.lock itself; thread "
                          f"CONTINUES to the next cycle.", flush=True)
                except Exception as exc:
                    import traceback
                    print(f"[serve] auto-pull ERROR: repo={repo.name} "
                          f"{type(exc).__name__}: {exc} -- thread CONTINUES to the "
                          f"next cycle.", flush=True)
                    traceback.print_exc()

    threading.Thread(target=_auto_pull, daemon=True, name="auto-pull").start()
    print("[serve] Auto-pull: every 5 min (REE_assembly + ree-v3)", flush=True)

    # Extra bind addresses serve in daemon threads; the primary runs in the
    # foreground so Ctrl+C / SIGTERM still reaches shutdown() above.
    for srv in servers[1:]:
        threading.Thread(target=srv.serve_forever, daemon=True,
                         name=f"serve-{srv.server_address[0]}").start()
    server.serve_forever()


if __name__ == "__main__":
    main()
