#!/usr/bin/env python3
"""Coordinator /shadow/status client -- stdlib-only, never raises.

The git materialization of evidence/experiments/runner_heartbeats/*.json and
runner_status/*.json is retired (removed from master 2026-09-06). The live
authority for fleet telemetry is the coordinator on the hub
(http://10.8.0.1:8787 over WireGuard), whose GET /shadow/status returns:

    {"machines": [{"machine": ..., "last_seen": ..., "state": ...,
                   "current_exq": ..., "progress": {...},
                   "lifecycle_state": ..., ...}]}

Consumers in this directory call machine_rows() and PREFER its answer,
falling back to the frozen git files only when it returns None (or an empty
dict -- treat any falsy result as "coordinator unavailable" for fallback
purposes, so a degenerate empty answer can never silence the git path).

Failure contract (the whole point of this module):
  * fetch_shadow_status()/machine_rows() NEVER raise. Missing or unparseable
    ~/.ree_coordinator_client.json, unreachable hub, non-200 response, or a
    response that is not valid JSON all return None.
  * Config is read from ~/.ree_coordinator_client.json (keys "url"/"token").
    The path can be overridden with the REE_COORDINATOR_CLIENT_CONFIG env var
    (used by tests to point at a bogus path).
  * The first fetch outcome (success OR failure) is cached for the life of
    the process, so a script with several telemetry call sites pays the
    network timeout at most once. Pass refresh=True to bypass the cache.

Mirrors serve.py:_fetch_coordinator_machine_snapshots (the reference fetch
pattern) minus the TTL cache, which a long-lived server needs and these
one-shot generator scripts do not.

ASCII-only output per repo policy (this module prints nothing itself).
"""
import json
import os
import urllib.error
import urllib.request
from typing import Optional

DEFAULT_TIMEOUT = 6.0
CONFIG_ENV_VAR = "REE_COORDINATOR_CLIENT_CONFIG"
DEFAULT_CONFIG_PATH = os.path.join(
    os.path.expanduser("~"), ".ree_coordinator_client.json")

# Process-lifetime memo of the last fetch outcome (success or failure).
_UNSET = object()
_cached_status = _UNSET


def _config_path() -> str:
    return os.environ.get(CONFIG_ENV_VAR) or DEFAULT_CONFIG_PATH


def load_client_config() -> Optional[dict]:
    """Parsed coordinator client config, or None on any failure."""
    try:
        with open(_config_path(), "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
    except Exception:
        return None
    if not isinstance(cfg, dict):
        return None
    return cfg


def _fetch(timeout: float) -> Optional[dict]:
    cfg = load_client_config()
    if cfg is None:
        return None
    url = str(cfg.get("url") or "").rstrip("/")
    token = str(cfg.get("token") or "")
    if not url or not token:
        return None
    try:
        req = urllib.request.Request(
            url + "/shadow/status",
            headers={"Authorization": "Bearer " + token},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            # urlopen raises HTTPError (caught below) for non-2xx; the
            # explicit status check is belt-and-braces for exotic handlers.
            if getattr(resp, "status", 200) != 200:
                return None
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None
    if not isinstance(payload, dict):
        return None
    return payload


def fetch_shadow_status(timeout: float = DEFAULT_TIMEOUT,
                        refresh: bool = False) -> Optional[dict]:
    """Parsed /shadow/status payload, or None on ANY failure. Never raises."""
    global _cached_status
    if refresh or _cached_status is _UNSET:
        _cached_status = _fetch(timeout)
    return _cached_status


def machine_rows(timeout: float = DEFAULT_TIMEOUT,
                 refresh: bool = False) -> Optional[dict]:
    """{machine_name: row} from /shadow/status, or None when unavailable.

    Never raises. Rows are passed through unmodified (last_seen, state,
    current_exq, progress, lifecycle_state, ...). Callers should treat a
    falsy return (None OR {}) as "fall back to the git files".
    """
    status = fetch_shadow_status(timeout=timeout, refresh=refresh)
    if status is None:
        return None
    out: dict = {}
    for row in status.get("machines") or []:
        if not isinstance(row, dict):
            continue
        name = row.get("machine")
        if not name:
            continue
        out[str(name)] = row
    return out
