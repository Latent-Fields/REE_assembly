"""The /api/runner/status `draining` flag must be able to be BOTH true and false.

WHY THIS FILE EXISTS
--------------------
Until 2026-09-09 `runner_status()` derived the flag by globbing
`evidence/experiments/runner_status/*.json`. That per-machine git-telemetry
render was retired 2026-09-06 (CLAUDE.md archaeology note A-93): the directory
is gone from master, and the Mac runner runs under
PHASE3_RUNNER_TELEMETRY_OFF_GIT=1, whose gate returns from
`experiment_runner.write_status()` before it touches disk. So the glob matched
nothing, forever, and the flag reported "not draining" with no error -- a field
that could not be true, which is worse than an absent one because callers
cannot tell.

The trap was latent rather than live (explorer.html only uses the flag to swap
Stop for Force Stop), but an idle/safety gate built on it would have silently
always passed.

WHAT IS PINNED
--------------
The positive case is the point: `test_stop_then_status_reports_draining` fails
against the old implementation. The negative controls stop the obvious
over-corrections -- a flag that latches on forever, one that survives a
restart, and one that leaks onto a substrate that was never asked to drain.

Time-independent and process-independent: no real runner is spawned, no
signals are sent, and PIDs are stubbed.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_serve():
    """Import REE_assembly/serve.py under its own name (see sibling tests)."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("serve", ROOT / "serve.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def serve():
    return load_serve()


@pytest.fixture(autouse=True)
def clean_drain_state(serve):
    """Module-level dicts persist across tests -- reset them either side."""
    for d in (serve._runner_drain_pids, serve._runner_ext_pids):
        for k in d:
            d[k] = None
    yield
    for d in (serve._runner_drain_pids, serve._runner_ext_pids):
        for k in d:
            d[k] = None


def _pin_pids(serve, monkeypatch, mapping):
    """Make _runner_pid() report `mapping` without touching launchd or /proc."""
    monkeypatch.setattr(serve, "_runner_pid", lambda ver: mapping.get(ver))


def test_draining_is_false_when_no_drain_requested(serve, monkeypatch):
    _pin_pids(serve, monkeypatch, {"v3": 4242, "v2": None})
    st = serve.runner_status()
    assert st["v3"]["running"] is True
    assert st["v3"]["draining"] is False


def test_stop_then_status_reports_draining(serve, monkeypatch):
    """THE REGRESSION TEST: this is the case the retired-telemetry read could
    never produce. A drain request recorded against the live PID must surface."""
    _pin_pids(serve, monkeypatch, {"v3": 4242, "v2": None})
    serve._runner_drain_pids["v3"] = 4242

    st = serve.runner_status()
    assert st["v3"]["draining"] is True, (
        "draining must be reachable -- if this fails the flag is dead again")
    assert st["v3"]["pid"] == 4242


def test_drain_does_not_leak_to_the_other_substrate(serve, monkeypatch):
    _pin_pids(serve, monkeypatch, {"v3": 4242, "v2": 777})
    serve._runner_drain_pids["v3"] = 4242

    st = serve.runner_status()
    assert st["v3"]["draining"] is True
    assert st["v2"]["draining"] is False


def test_draining_is_false_once_the_runner_is_gone(serve, monkeypatch):
    """Drain finished: the process exited, so nothing is draining."""
    _pin_pids(serve, monkeypatch, {"v3": None, "v2": None})
    serve._runner_drain_pids["v3"] = 4242

    st = serve.runner_status()
    assert st["v3"]["running"] is False
    assert st["v3"]["draining"] is False


def test_a_restarted_runner_is_not_draining_and_clears_the_record(
        serve, monkeypatch):
    """A stale request must not attach itself to a NEW pid -- including a
    recycled one. This is why the check is pid equality, not a bare bool."""
    _pin_pids(serve, monkeypatch, {"v3": 9999, "v2": None})
    serve._runner_drain_pids["v3"] = 4242

    st = serve.runner_status()
    assert st["v3"]["draining"] is False
    assert serve._runner_drain_pids["v3"] is None, (
        "the superseded request should be cleared, not left to re-fire")


def test_stop_runner_records_the_drain_for_a_popen_child(serve, monkeypatch):
    """Wire-up check on the real stop path: stop_runner() must populate the
    record the flag reads, or the flag is dead however correct its logic is."""

    class _FakeProc:
        pid = 5150

        def __init__(self):
            self.terminated = False

        def poll(self):
            return None

        def terminate(self):
            self.terminated = True

    proc = _FakeProc()
    monkeypatch.setattr(serve, "_launchd_supervises_v3", lambda: False)
    monkeypatch.setitem(serve._runner_procs, "v3", proc)

    res = serve.stop_runner("v3")
    assert res["status"] == "draining" and res["pid"] == 5150
    assert proc.terminated is True
    assert serve._runner_drain_pids["v3"] == 5150

    _pin_pids(serve, monkeypatch, {"v3": 5150, "v2": None})
    assert serve.runner_status()["v3"]["draining"] is True

    monkeypatch.setitem(serve._runner_procs, "v3", None)


def test_force_stop_clears_the_drain_record(serve, monkeypatch):
    """Force Stop is terminal -- nothing is 'finishing its experiment' after."""

    class _FakeProc:
        pid = 5151

        def poll(self):
            return None

        def kill(self):
            pass

        def wait(self, timeout=None):
            return 0

    monkeypatch.setattr(serve, "_launchd_supervises_v3", lambda: False)
    monkeypatch.setitem(serve._runner_procs, "v3", _FakeProc())
    serve._runner_drain_pids["v3"] = 5151

    res = serve.force_stop_runner("v3")
    assert res["status"] == "stopped"
    assert serve._runner_drain_pids["v3"] is None
