#!/usr/bin/env python3
"""Contract tests for the Steward -> governance.sh wiring (Step 3m).

WHY THIS FILE EXISTS. The detectors have 170 tests; none of them assert that
anything ever RUNS them. Stage 1 shipped deliberately unwired ("runnable by hand
first"), so the wiring is the newest and least-defended part of the arrangement,
and every property it depends on is invisible from inside run_detectors.py:

  - that governance.sh invokes it at all
  - that it does NOT pass --exit-nonzero-on-escalate (which would turn a detector
    finding into a failed regen, inverting the "detection is free" design)
  - that it does NOT pass --fix (19 real repairs queued against shared plan
    frontmatter -- a governance-visible action, not a per-regen one)
  - that it runs AFTER generate_closure_snapshot.py, which D-010 reads
  - that the `escalate` boolean is SURFACED, including on an abort path
  - that a crash in a detector cannot abort a governance regen

MOST OF THESE ARE EXECUTED, NOT GREPPED. A wiring test built only from string
matching passes forever while the thing it describes rots -- the same reason
scripts/test_audit_worktree_skills_hook.py runs the command the live settings
file holds rather than asserting it is present. The bash here is extracted from
the LIVE governance.sh and really run, against a stubbed run_detectors.py in a
tmpdir, so it is fast, hermetic, and time-independent.

The static assertions that remain are the ones with no runtime signature: an
absent flag cannot be observed by running the thing that does not pass it.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
GOVERNANCE_SH = REPO_ROOT / "scripts" / "governance.sh"

TRAP_MARKER = "trap 'gov_on_signal TERM 15' TERM"
STEP_MARKER = "--- Step 3m: Steward"
NEXT_STEP_MARKER = "--- Step 4/7:"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def governance_lines() -> list[str]:
    return GOVERNANCE_SH.read_text(encoding="utf-8").splitlines(True)


def _index_of(lines: list[str], marker: str) -> int:
    for i, line in enumerate(lines):
        if marker in line:
            return i
    raise AssertionError(
        "governance.sh no longer contains %r -- the Steward wiring test cannot "
        "locate the step. If the step was renamed, update the marker; if it was "
        "REMOVED, that is the regression this file exists to catch." % marker)


def step_3m_source() -> str:
    lines = governance_lines()
    return "".join(lines[_index_of(lines, STEP_MARKER):
                         _index_of(lines, NEXT_STEP_MARKER)])


def step_3m_code() -> str:
    """Step 3m with comment lines removed.

    The step's own comment block EXPLAINS why --fix and
    --exit-nonzero-on-escalate are not passed, and therefore names both. A flag
    test run over the raw source matches the explanation and fails on a correct
    file -- so the flag checks read the code, and assert the stripping did not
    gut what they are checking.
    """
    code = "".join(line for line in step_3m_source().splitlines(True)
                   if not line.lstrip().startswith("#"))
    assert "run_detectors.py" in code, (
        "comment-stripping removed the invocation itself -- this helper is "
        "broken, not the wiring")
    return code


def build_harness(tmp_path: Path, trailer: str = "") -> Path:
    """Extract the live declarations + traps + Step 3m into a runnable script.

    The harness keeps governance.sh's own `cd "$(dirname "$0")/.."`, so writing
    it to <tmp>/scripts/ makes <tmp> the repo root -- the extracted block runs
    verbatim, against the stub tree, with no path rewriting.

    The TASK_CLAIMS lock helpers are overridden to no-ops AFTER their real
    definitions: they are a different concern with their own trap wiring, and a
    wiring test must not touch the real TASK_CLAIMS.json.
    """
    lines = governance_lines()
    head = "".join(lines[:_index_of(lines, TRAP_MARKER) + 1])
    body = step_3m_source()
    script = (
        head
        + "\n# test harness: neuter the TASK_CLAIMS lock; everything else verbatim\n"
        + "gov_claim_open() { :; }\ngov_claim_close() { :; }\n\n"
        + body
        + trailer
    )
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    path = scripts_dir / "harness.sh"
    path.write_text(script, encoding="utf-8")
    return path


CANNED_ESCALATING = {
    "schema": "steward_report.v1",
    "escalate": True,
    "escalated": ["D-002:MECH-999", "D-007:someplan:GAP-9"],
    "escalation_budget": 5,
    "escalation_candidates": 9,
    "escalation_truncated": 7,
    "counts": {"total": 12, "new": 9, "recurring": 3, "resolved": 1,
               "suppressed": 2},
    "detectors": [{"detector": "D-002", "n_findings": 1}],
    "findings": [
        {"finding_id": "D-002:MECH-999", "severity": "P0", "signal": "strong",
         "confidence": 0.95, "title": "MECH-999 is an orphan V3 claim"},
        {"finding_id": "D-007:someplan:GAP-9", "severity": "P1",
         "signal": "strong", "confidence": 0.85,
         "title": "someplan:GAP-9 names a gate that is now done"},
    ],
    "resolved": [],
}

CANNED_QUIET = {
    "schema": "steward_report.v1",
    "escalate": False,
    "escalated": [],
    "escalation_budget": 5,
    "escalation_candidates": 0,
    "escalation_truncated": 0,
    "counts": {"total": 54, "new": 0, "recurring": 54, "resolved": 1,
               "suppressed": 1},
    "detectors": [{"detector": "D-002", "n_findings": 4}],
    "findings": [],
    "resolved": [],
}


def write_stub_runner(tmp_path: Path, report: dict | None,
                      exit_code: int = 0) -> None:
    """A stand-in run_detectors.py that writes `report` where the real one does.

    Deriving the report path from the REAL run_detectors.py rather than
    hardcoding it is deliberate: it makes this a test of the AGREEMENT between
    the two files. If someone moves the real default, the stub follows and
    governance.sh's own STEWARD_REPORT is left behind -- which is the failure.
    """
    sys.path.insert(0, str(HERE))
    import run_detectors  # noqa: E402  (path-dependent by design)

    rel = Path(run_detectors.REPORT_DIRNAME) / run_detectors.REPORT_FILE
    target = tmp_path / "scripts" / "steward" / rel
    stub = tmp_path / "scripts" / "steward" / "run_detectors.py"
    stub.parent.mkdir(parents=True, exist_ok=True)
    payload = "None" if report is None else repr(json.dumps(report))
    stub.write_text(
        "import json, sys\n"
        "from pathlib import Path\n"
        "print('stub run_detectors banner')\n"
        "payload = %s\n"
        "if payload is not None:\n"
        "    p = Path(%r)\n"
        "    p.parent.mkdir(parents=True, exist_ok=True)\n"
        "    p.write_text(payload)\n"
        "raise SystemExit(%d)\n" % (payload, str(target), exit_code),
        encoding="utf-8")


def run_harness(harness: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["PYTHON"] = sys.executable          # the default is a MacPorts path
    return subprocess.run(["bash", str(harness)], capture_output=True,
                          text=True, env=env)


# ---------------------------------------------------------------------------
# static assertions -- properties with no runtime signature
# ---------------------------------------------------------------------------

def test_governance_invokes_the_detector_runner():
    """An actual invocation line, not a mention.

    Checked against the code rather than the file text on purpose: the step's
    comment block and its own "re-run by hand" error message both name the
    script, so a whole-file substring test passes even after the invocation has
    been deleted (verified by mutation).
    """
    invocations = [line for line in step_3m_code().splitlines()
                   if line.strip().startswith(
                       '"$PYTHON" scripts/steward/run_detectors.py')]
    assert invocations, (
        "governance.sh no longer RUNS the Steward detectors (it may still "
        "mention them in a comment)")


def test_no_exit_nonzero_on_escalate():
    """A detector finding must never fail a governance regen.

    The whole cost argument is that detection is free, so it can run on every
    cycle. Gating the regen on it makes detection expensive and the next session
    to be blocked by it will (correctly) remove the step.
    """
    assert "--exit-nonzero-on-escalate" not in step_3m_code()


def test_no_fix_flag():
    """--fix edits shared plan frontmatter; it is a deliberate governance act.

    RESOLVED 2026-08-18, and this test is now pinning a DECISION rather than a
    deferral: the deliberate act has an owner -- the daily launchd sweep
    `steward_sweep.py` / `com.ree.steward` (user decision 2026-08-17, option
    (ii)). Governance stays read-only. Adding --fix here would ALSO break this
    step's own placement: Step 3m sits after Step 3c-bis because D-010 must
    audit the closure snapshot 3c-bis writes, so fixing plan frontmatter here
    leaves that snapshot stale. See README.md "The daily T0 sweep".
    """
    src = step_3m_code()
    for tok in (" --fix", "\t--fix", "--fix "):
        assert tok not in src, (
            "Step 3m passes --fix. The T0 lane is opt-in by design: it has real "
            "repairs queued against evidence/planning/ frontmatter, and applying "
            "them changes what the morning digest reports. The daily sweep "
            "(scripts/steward/steward_sweep.py) is where --fix belongs.")


def test_runs_after_the_closure_snapshot():
    """D-010 reads evidence/planning/closure_status.md, written by Step 3c-bis.

    Ordered the other way it audits a stale snapshot and reports the staleness
    as a defect -- a false positive manufactured purely by step order.
    """
    lines = governance_lines()
    assert _index_of(lines, "generate_closure_snapshot.py") < \
        _index_of(lines, STEP_MARKER)


def test_runs_before_the_derived_artifact_steps():
    """Placed with the warn-only scan family, not after the site builders."""
    lines = governance_lines()
    assert _index_of(lines, STEP_MARKER) < _index_of(lines, NEXT_STEP_MARKER)


def test_verdict_is_printed_from_the_exit_trap():
    """Surfacing has to survive an abort at Step 4b / Step 9c.

    Both are blocking gates that exit before the end of the pipeline, so a
    verdict printed only at the end of a successful run is a verdict that
    vanishes exactly when the cycle went wrong.
    """
    src = GOVERNANCE_SH.read_text(encoding="utf-8")
    trap_body = src.split("gov_on_exit() {", 1)[1].split("\n}", 1)[0]
    assert "steward_print_summary" in trap_body


def test_report_path_agrees_with_run_detectors():
    sys.path.insert(0, str(HERE))
    import run_detectors

    expected = "scripts/steward/%s/%s" % (run_detectors.REPORT_DIRNAME,
                                          run_detectors.REPORT_FILE)
    assert expected in GOVERNANCE_SH.read_text(encoding="utf-8"), (
        "governance.sh reads a different report path than run_detectors.py "
        "writes -- the verdict would be read from a stale or absent file")


# ---------------------------------------------------------------------------
# the gitignore decision (2026-08-16) -- see README "Wiring"
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("relpath", [
    "scripts/steward/reports/steward_report.json",
    "scripts/steward/state/steward_state.json",
    "scripts/steward/state/steward_ref_pins.json",
])
def test_per_machine_artifacts_are_ignored(relpath):
    """All three carry machine-local absolute paths and/or suppress escalations.

    ref_pins in particular was neither tracked nor ignored until the wiring
    landed, so a governance regen left it as `??` for a human to sweep into a
    landing commit.
    """
    proc = subprocess.run(["git", "-C", str(REPO_ROOT), "check-ignore", "-q",
                           relpath], capture_output=True)
    if proc.returncode == 128:
        pytest.skip("not a git checkout")
    assert proc.returncode == 0, "%s is NOT gitignored" % relpath


def test_the_ledger_is_not_ignored():
    """The append-only audit series is the deliberate exception, both ways.

    It merges and it suppresses nothing, so it is tracked. Ignoring it would
    silently discard the time series the escalation ranking is calibrated on.
    """
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "check-ignore", "-q",
         "scripts/steward/state/steward_ledger.jsonl"], capture_output=True)
    if proc.returncode == 128:
        pytest.skip("not a git checkout")
    assert proc.returncode == 1, (
        "steward_ledger.jsonl is gitignored -- the run time series would be "
        "lost. Only the report and the ratchet state are per-machine.")


# ---------------------------------------------------------------------------
# executed behaviour -- the live bash, really run
# ---------------------------------------------------------------------------

def test_escalation_is_surfaced_loudly(tmp_path):
    write_stub_runner(tmp_path, CANNED_ESCALATING)
    proc = run_harness(build_harness(tmp_path))
    assert proc.returncode == 0, proc.stderr
    assert "ESCALATE = YES -- 2 NEW finding(s)" in proc.stdout
    assert "MECH-999 is an orphan V3 claim" in proc.stdout
    assert "[P0 strong conf=0.95]" in proc.stdout
    assert "Load the Steward skill" in proc.stdout


def test_the_escalation_budget_is_reported_as_a_budget(tmp_path):
    """Five must never read as "all of them" -- the report says so, so must this."""
    write_stub_runner(tmp_path, CANNED_ESCALATING)
    proc = run_harness(build_harness(tmp_path))
    assert "+7 more candidate(s) over the escalation budget of 5" in proc.stdout
    assert "five is NOT all of them" in proc.stdout


def test_no_truncation_note_when_nothing_is_truncated(tmp_path):
    report = dict(CANNED_ESCALATING, escalation_truncated=0,
                  escalation_candidates=2)
    write_stub_runner(tmp_path, report)
    proc = run_harness(build_harness(tmp_path))
    assert "over the escalation budget" not in proc.stdout


def test_quiet_run_says_the_skill_should_not_load(tmp_path):
    write_stub_runner(tmp_path, CANNED_QUIET)
    proc = run_harness(build_harness(tmp_path))
    assert proc.returncode == 0, proc.stderr
    assert "ESCALATE = no" in proc.stdout
    assert "should NOT load" in proc.stdout
    assert "ESCALATE = YES" not in proc.stdout


def test_the_verdict_is_printed_twice(tmp_path):
    """Once at the step, once from the exit trap.

    Several hundred lines of regen output follow Step 3m, so a single in-place
    line is a line nobody reads -- and the boolean is the entire point.
    """
    write_stub_runner(tmp_path, CANNED_ESCALATING)
    proc = run_harness(build_harness(tmp_path))
    assert proc.stdout.count("ESCALATE = YES") == 2, proc.stdout


def test_a_detector_crash_does_not_abort_the_regen(tmp_path):
    """A hint, never a gate -- including when the hint itself is broken."""
    write_stub_runner(tmp_path, None, exit_code=3)
    proc = run_harness(build_harness(
        tmp_path, trailer='\necho "REACHED THE NEXT STEP"\n'))
    assert proc.returncode == 0, proc.stderr
    assert "REACHED THE NEXT STEP" in proc.stdout
    assert "escalation state UNKNOWN" in proc.stdout
    assert "exited 3" in proc.stdout


def test_an_unreadable_report_is_unknown_not_quiet(tmp_path):
    """Exit 0 with no report must never be reported as "nothing to escalate".

    That is the failure that reads as reassurance: a silent detector and a clean
    one look identical to a human scanning the log.
    """
    write_stub_runner(tmp_path, None, exit_code=0)
    proc = run_harness(build_harness(tmp_path))
    assert proc.returncode == 0, proc.stderr
    assert "escalation state UNKNOWN" in proc.stdout
    assert "ESCALATE = no" not in proc.stdout


def test_a_later_blocking_gate_still_shows_the_verdict(tmp_path):
    """Step 4b / Step 9c shape: abort after 3m, exit status preserved."""
    write_stub_runner(tmp_path, CANNED_ESCALATING)
    proc = run_harness(build_harness(
        tmp_path, trailer='\necho "--- Step 9c: simulated gate ---"\nexit 1\n'))
    assert proc.returncode == 1
    assert proc.stdout.count("ESCALATE = YES") == 2
    # ...and it is the LAST thing on the screen, after the gate's own output.
    assert proc.stdout.rindex("ESCALATE = YES") > \
        proc.stdout.rindex("simulated gate")


def test_nothing_is_printed_when_the_step_never_ran(tmp_path):
    """An abort before Step 3m must not print a stale or empty verdict."""
    lines = governance_lines()
    head = "".join(lines[:_index_of(lines, TRAP_MARKER) + 1])
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    path = scripts_dir / "harness.sh"
    path.write_text(
        head + "\ngov_claim_open() { :; }\ngov_claim_close() { :; }\n"
        + '\necho "--- Step 0: simulated early gate ---"\nexit 1\n',
        encoding="utf-8")
    proc = run_harness(path)
    assert proc.returncode == 1
    assert "STEWARD" not in proc.stdout
    assert "ESCALATE" not in proc.stdout


def test_detector_errors_mark_the_totals_incomplete(tmp_path):
    """A partial run must not present its counts as a complete picture."""
    report = dict(CANNED_QUIET, detectors=[
        {"detector": "D-002", "n_findings": 4},
        {"detector": "D-010", "error": "ValueError: boom", "n_findings": 0},
    ])
    write_stub_runner(tmp_path, report)
    proc = run_harness(build_harness(tmp_path))
    assert "DETECTOR ERROR(S): D-010" in proc.stdout
    assert "INCOMPLETE" in proc.stdout


def test_output_is_ascii(tmp_path):
    """CLAUDE.md: anything reaching a terminal must survive cp1252."""
    write_stub_runner(tmp_path, CANNED_ESCALATING)
    proc = run_harness(build_harness(tmp_path))
    proc.stdout.encode("ascii")
    step_3m_source().encode("ascii")


def test_the_real_runner_produces_a_report_the_wiring_can_read(tmp_path):
    """One end-to-end pass with the REAL detectors, not the stub.

    The stub tests pin the wiring's behaviour; this pins that the real runner
    still emits the keys the wiring reads. Writes to a tmpdir, so the live
    ratchet state is untouched.
    """
    report_path = tmp_path / "report.json"
    proc = subprocess.run(
        [sys.executable, str(HERE / "run_detectors.py"),
         "--repo-root", str(REPO_ROOT),
         "--state-dir", str(tmp_path / "state"),
         "--report", str(report_path)],
        capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    report = json.loads(report_path.read_text(encoding="utf-8"))
    for key in ("escalate", "escalated", "escalation_budget",
                "escalation_truncated", "counts", "detectors", "findings"):
        assert key in report, "run_detectors.py no longer emits %r" % key
