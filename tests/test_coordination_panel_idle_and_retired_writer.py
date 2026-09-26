"""Explorer Coordination panel: an idle fleet and a retired writer are not faults.

WHAT THIS PINS (2026-09-26)
---------------------------
1. `_shadow_verdict` returns IDLE (green) when no machine is fresh AND the
   coordinator reports zero active queue items. Before, an empty queue with the
   scaler correctly powering workers down painted the panel amber forever.
2. The negative controls are the point: IDLE must NOT fire when the queue still
   has work (that is the real "workers silent while work waits" alarm), when
   the queue count could not be fetched (`None` is unknown, never zero), or
   when there is divergence.
3. `_mark_heartbeat_writer_retired` greys the retired phase3 heartbeat writer
   row (A-93) instead of letting its ever-ageing commit paint red -- but a
   present `last_error` keeps it red.

Time-independent: the one "fresh" timestamp is computed from now.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def serve():
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("serve", ROOT / "serve.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BASE = {"total_claims": 10, "adjusted_divergences": 0}


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.parametrize("st, queue_active, expected", [
    (dict(BASE, machines=[]), 0, ("IDLE", "green")),
    (dict(BASE, machines=[]), 3, ("NO_SIGNAL", "amber")),
    (dict(BASE, machines=[]), None, ("NO_SIGNAL", "amber")),
    (dict(BASE, adjusted_divergences=1, machines=[]), 0, ("DIVERGENCE", "red")),
    (dict(BASE, total_claims=0, machines=[]), 0, ("NO_SIGNAL", "amber")),
])
def test_idle_only_when_queue_known_empty(serve, st, queue_active, expected):
    assert serve._shadow_verdict(st, queue_active=queue_active) == expected


def test_fresh_machine_is_still_healthy(serve):
    st = dict(BASE, machines=[{"last_seen": _now()}])
    assert serve._shadow_verdict(st, queue_active=0) == ("HEALTHY", "green")


def test_default_call_never_reports_idle(serve):
    """Callers that do not pass a queue count keep the old behaviour."""
    assert serve._shadow_verdict(dict(BASE, machines=[]))[0] == "NO_SIGNAL"


def test_idle_has_an_operator_guide(serve):
    assert "idle" in serve._shadow_operator_guide("IDLE", {})["phase_label"]


def test_retired_heartbeat_writer_is_grey(serve):
    writers = {
        "heartbeat_writer": {"color": "red", "status": "idle", "last_error": None},
        "git_writer": {"color": "green", "status": "idle", "last_error": None},
    }
    serve._mark_heartbeat_writer_retired(writers)
    assert writers["heartbeat_writer"]["color"] == "grey"
    assert writers["heartbeat_writer"]["status"] == "retired"
    assert writers["git_writer"] == {"color": "green", "status": "idle",
                                     "last_error": None}


def test_erroring_retired_writer_stays_red(serve):
    writers = {"heartbeat_writer": {"color": "red", "status": "idle",
                                    "last_error": {"message": "boom"}}}
    serve._mark_heartbeat_writer_retired(writers)
    assert writers["heartbeat_writer"]["color"] == "red"
