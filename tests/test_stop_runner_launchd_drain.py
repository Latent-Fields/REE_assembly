"""stop_runner() must DRAIN the launchd runner, never bootout out from under it.

WHY THIS FILE EXISTS
--------------------
Until 2026-09-22 `stop_runner()`'s launchd branch called `_launchd_bootout()`
and returned `{"status": "draining"}`. Its comment claimed "bootout sends
SIGTERM (drain) and unloads the plist. The runner finishes the current
experiment then exits, with no respawn."

The first sentence is right and the second does not follow. `launchctl bootout`
sends SIGTERM and then SIGKILLs the job once the exit timeout expires. The
runner's SIGTERM handler is graceful-only by design -- experiment_runner.main()
sets _drain_flag and keeps going until the current experiment finishes
("SIGTERM / remote stop only request drain") -- so it cannot possibly exit
inside that window while an experiment is running.

Measured on the Mac 2026-09-22 with a throwaway LaunchAgent whose program traps
SIGTERM and keeps running: bootout SIGKILLed it after 5.10s and 5.11s (two
runs), and `launchctl print gui/<uid>/com.ree.runner` independently reports
`exit timeout = 5` for the real job. The same probe under `launchctl kill TERM`
was still alive, job still loaded, 45s later. Experiments on this fleet run for
hours; V3-EXQ-1067 had ~99h left at the time. So pressing Stop destroyed the
in-flight experiment ~5s later while telling the operator "draining" -- a
silent multi-day data-loss path that nothing audited.

WHAT IS PINNED
--------------
`test_launchd_stop_does_not_bootout` is the point: it fails against the old
implementation. The rest are the negative controls that stop the two obvious
over-corrections -- ripping bootout out of force_stop_runner too (where it is
correct, because the caller has already accepted the loss and SIGKILL has
already been delivered), and letting an error from the signal call be reported
as a successful drain.

Time-independent and process-independent: no real runner, no launchctl, no
signals. Every launchd call is recorded by a stub.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
FAKE_PID = 424242


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


@pytest.fixture
def launchd(serve, monkeypatch):
    """Pretend a launchd-supervised v3 runner is up, and record every call."""
    calls: list[tuple[str, str]] = []

    monkeypatch.setattr(serve, "_launchd_supervises_v3", lambda: True)
    monkeypatch.setattr(serve, "_launchd_pid", lambda: FAKE_PID)

    def fake_bootout():
        calls.append(("bootout", ""))
        return True, "bootout"

    def fake_kill(sig):
        calls.append(("kill", sig))
        return True, f"signalled {sig}"

    monkeypatch.setattr(serve, "_launchd_bootout", fake_bootout)
    monkeypatch.setattr(serve, "_launchd_kill", fake_kill)
    serve._runner_drain_pids["v3"] = None
    yield calls
    serve._runner_drain_pids["v3"] = None


def test_launchd_stop_does_not_bootout(serve, launchd):
    """THE REGRESSION TEST: Stop must not unload the job under a live run.

    bootout is SIGTERM-then-SIGKILL (~5s). Calling it here is the data-loss
    path this file exists to prevent.
    """
    result = serve.stop_runner("v3")

    assert ("bootout", "") not in launchd, (
        "stop_runner() called launchctl bootout on a RUNNING launchd runner. "
        "bootout SIGKILLs the job ~5s after SIGTERM, which destroys the "
        "in-flight experiment -- use _launchd_kill('TERM') instead."
    )
    assert result["status"] == "draining"


def test_launchd_stop_sends_sigterm(serve, launchd):
    """The drain request itself must still be made -- and be SIGTERM."""
    serve.stop_runner("v3")
    assert launchd == [("kill", "TERM")], launchd


def test_launchd_stop_records_drain_pid(serve, launchd):
    """The draining flag must still light up, so the explorer swaps in Force Stop."""
    result = serve.stop_runner("v3")
    assert result["pid"] == FAKE_PID
    assert result["supervisor"] == "launchd"
    assert serve._runner_draining("v3", FAKE_PID) is True


def test_launchd_stop_reports_signal_failure(serve, monkeypatch, launchd):
    """A failed signal must surface as an error, never as a phantom drain.

    The whole defect class here is 'told the operator draining when it was
    not', so the failure path gets its own pin.
    """
    monkeypatch.setattr(serve, "_launchd_kill",
                        lambda sig: (False, "kill rc=3: no such process"))
    result = serve.stop_runner("v3")
    assert result["status"] == "error"
    assert serve._runner_draining("v3", FAKE_PID) is False


def test_launchd_force_stop_still_kills_then_boots_out(serve, launchd):
    """NEGATIVE CONTROL: bootout is CORRECT in force_stop_runner.

    force_stop semantics are 'no drain, no respawn, gone now' -- the caller
    has accepted losing the run. Do not let a fix for stop_runner() sweep
    bootout out of here too. Order matters: SIGKILL first, so bootout unloads
    an already-dead job instead of racing the exit timeout.
    """
    result = serve.force_stop_runner("v3")
    assert launchd == [("kill", "KILL"), ("bootout", "")], launchd
    assert result["status"] == "stopped"
    assert serve._runner_draining("v3", FAKE_PID) is False
