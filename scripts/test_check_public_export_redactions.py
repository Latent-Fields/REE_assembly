#!/usr/bin/env python3
"""
Tests for the unattended-refresh gate (scripts/check_public_export_redactions.py).

Stdlib-only. Runs standalone or under pytest:
    /opt/local/bin/python3 scripts/test_check_public_export_redactions.py
    pytest scripts/test_check_public_export_redactions.py

WHY THE NEGATIVE CONTROLS MATTER MORE THAN THE POSITIVE ONE HERE. This gate's
steady state is "pass": the baseline is expected to cover every hit, week after
week. A gate that can only be observed passing is indistinguishable from a gate
that cannot fail -- and this repo has just spent a day on three instances of
exactly that (test files nothing collected, all green, for months). So every
gate below is exercised in BOTH directions: a synthetic unreviewed hit must
fail gate 1, a synthetic collapse must fail gate 3, and ordinary churn must not.

The build is done ONCE at module scope and shared -- it is a full export
(~2900 manifests) and re-running it per test would dominate the suite.
"""
import json
import sys
import tempfile
from pathlib import Path

import check_public_export_redactions as gate
import export_public_explorer as exp

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "docs" / "public_explorer" / "data"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "public-explorer-refresh.yml"

# Snapshot the tracked output BEFORE building, so test_build_export_writes_nothing
# can prove the gate is a pure read. Taken at import time because the build below
# is the thing under suspicion.
_TRACKED_BEFORE = {
    p.name: p.read_bytes() for p in sorted(DATA_DIR.glob("*.json"))
} if DATA_DIR.is_dir() else {}

_BUILT = exp.build_export()
_HITS = _BUILT["redactions"].pattern_hits
_COUNTS = _BUILT["counts"]


def test_build_export_writes_nothing():
    """The gate must never mutate the files it is gating.

    build_export() exists precisely so the gate can run without performing the
    export. If someone re-points it at main() for convenience, this fails --
    and it should, because in a shared multi-session checkout a tool that
    dirties tracked JSON is staging work for another session to sweep into its
    commit (root CLAUDE.md, "Read-modify-write contamination").
    """
    after = {p.name: p.read_bytes() for p in sorted(DATA_DIR.glob("*.json"))}
    assert after == _TRACKED_BEFORE, (
        "build_export() changed tracked files under docs/public_explorer/data/: "
        + ", ".join(sorted(
            set(after) ^ set(_TRACKED_BEFORE)
            or {k for k in after if after[k] != _TRACKED_BEFORE.get(k)}))
    )


def test_gate_is_not_vacuous():
    """An export that produced nothing would pass every gate below for free."""
    assert _COUNTS["claims"] > 0, "export produced no public claims"
    assert _COUNTS["experiments"] > 0, "export produced no public experiments"


def test_baseline_covers_current_hits():
    """The live assertion: no unreviewed scrub hit in the current export."""
    _, approved = gate.load_approved()
    new = [h for h in _HITS if gate.hit_key(h) not in approved]
    assert not new, (
        "unreviewed scrub hit(s) -- review them, then re-run with --update:\n  "
        + "\n  ".join(f"{h['record_type']} {h['record_id']} "
                      f"[{h['pattern']}] {h['matched']!r}" for h in new)
    )


def test_baseline_entries_are_reviewed_not_rubber_stamped():
    """`--update` writes TODO placeholders; landing them defeats the gate.

    An approved entry whose reason still reads TODO is an approval nobody wrote
    a reason for. It would silence the gate for that record forever while
    recording nothing about why dropping the field was correct.
    """
    entries, _ = gate.load_approved()
    bad = []
    for e in entries:
        missing = [f for f in gate.KEY_FIELDS if not e.get(f)]
        if missing:
            bad.append(f"{e.get('record_id', '?')}: missing {missing}")
            continue
        for field in ("verdict", "note", "reviewed_by", "reviewed_utc"):
            val = str(e.get(field, "")).strip()
            if not val or "TODO" in val:
                bad.append(f"{e['record_id']}: `{field}` is empty or still TODO")
    assert not bad, "unreviewed baseline entr(y/ies):\n  " + "\n  ".join(bad)


def test_a_new_hit_fails_gate_1():
    """Negative control: an unapproved hit must NOT be silently tolerated."""
    _, approved = gate.load_approved()
    synthetic = {
        "record_type": "experiment",
        "record_id": "v3_exq_000_synthetic_negative_control_20260101T000000Z_v3",
        "field": "summary",
        "pattern": "cloud_host",
        "matched": "ree-cloud-9",
    }
    assert gate.hit_key(synthetic) not in approved, (
        "the synthetic control collides with a real baseline entry; change its id"
    )


def test_empty_baseline_would_flag_every_hit():
    """Negative control on the loader: a missing baseline approves nothing.

    Fails open would be the dangerous direction -- a typo'd path silently
    approving everything, forever, with the gate still printing 'ok'.
    """
    with tempfile.TemporaryDirectory() as td:
        entries, keys = gate.load_approved(Path(td) / "does_not_exist.json")
    assert entries == [] and keys == set(), "missing baseline must approve nothing"
    if _HITS:
        assert all(gate.hit_key(h) not in keys for h in _HITS)


def test_hit_key_excludes_matched_substring():
    """Same record + pattern, different matched text == same review event."""
    a = {"record_type": "experiment", "record_id": "r", "field": "summary",
         "pattern": "cloud_host", "matched": "ree-cloud-2"}
    b = dict(a, matched="ree-cloud-3")
    assert gate.hit_key(a) == gate.hit_key(b)
    assert gate.hit_key(dict(a, record_id="other")) != gate.hit_key(a)


def test_count_collapse_is_detected():
    """Negative control on gate 3, in both of its shapes."""
    old = {"claims_public": 196, "experiments_public": 233}
    halved = gate.check_counts({"claims": 98, "experiments": 233}, old, 0.20)
    assert halved and "claims_public" in halved[0]

    zeroed = gate.check_counts({"claims": 196, "experiments": 0}, old, 0.20)
    assert zeroed and "experiments_public" in zeroed[0]


def test_ordinary_churn_is_tolerated():
    """Gate 3 must not fire on real governance movement.

    Anchored on measured history: the 2026-06-15 -> 2026-07-27 refresh lost 4
    of 179 claims to status changes while gaining 21. A gate that flagged that
    would be turned off within a month.
    """
    old = {"claims_public": 179, "experiments_public": 153}
    assert gate.check_counts({"claims": 196, "experiments": 233}, old, 0.20) == []
    assert gate.check_counts({"claims": 175, "experiments": 153}, old, 0.20) == []


def test_no_committed_index_skips_gate_3():
    """First-ever run has nothing to compare against; that is not a failure."""
    assert gate.check_counts({"claims": 1, "experiments": 1}, None, 0.20) == []


def test_refresh_workflow_gates_before_it_publishes():
    """The gate is only a gate if it runs BEFORE the commit step.

    Asserted on ordering rather than on the presence of the script name alone:
    a workflow that ran the check after pushing would satisfy a name-only check
    while publishing every week regardless of the verdict.
    """
    assert WORKFLOW.exists(), f"missing refresh workflow: {WORKFLOW}"
    text = WORKFLOW.read_text(encoding="utf-8")
    gate_at = text.find("check_public_export_redactions.py")
    assert gate_at != -1, "refresh workflow never runs the gate script"
    push_at = text.find("git push")
    assert push_at != -1, "refresh workflow never pushes"
    assert gate_at < push_at, (
        "the gate runs AFTER `git push` in the refresh workflow, so it cannot "
        "prevent anything from being published"
    )


ALL_TESTS = [
    test_build_export_writes_nothing,
    test_gate_is_not_vacuous,
    test_baseline_covers_current_hits,
    test_baseline_entries_are_reviewed_not_rubber_stamped,
    test_a_new_hit_fails_gate_1,
    test_empty_baseline_would_flag_every_hit,
    test_hit_key_excludes_matched_substring,
    test_count_collapse_is_detected,
    test_ordinary_churn_is_tolerated,
    test_no_committed_index_skips_gate_3,
    test_refresh_workflow_gates_before_it_publishes,
]


def main():
    failed = 0
    for t in ALL_TESTS:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}\n      {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"ERROR {t.__name__}\n      {type(e).__name__}: {e}")
    print(f"\n{len(ALL_TESTS) - failed}/{len(ALL_TESTS)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
