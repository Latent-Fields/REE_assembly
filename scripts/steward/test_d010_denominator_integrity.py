#!/usr/bin/env python3
"""Contract tests for D-010's cycle-1 refinement (2026-08-18).

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_d010_denominator_integrity.py -q

WHAT IS BEING PINNED, AND WHY IT IS MOSTLY NEGATIVE CONTROLS
=====================================================================
The refinement makes two checks emit LESS than they used to: check 2 stops
firing when the exclusion is labelled, and check 5 stops escalating when the
mismatch is provable regen lag. Both are the direction that can go silently
wrong -- a labelling test with a bug, or a lag discriminator that says
"explained" too readily, turns the detector guarding the closure accounting into
one that reports nothing. So roughly half of these assert the checks STILL FIRE:
label absent, label present with a stale count, a new unlabelled status arriving
beside a labelled one, an unreadable snapshot, and a mismatch whose tally
matches. Those are the assertions that stop a later session widening the
narrowing until D-010 is inert.

Time-independent: no sleeps, no wall-clock dependence, no network, no git.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

_STEWARD = Path(__file__).resolve().parent
if str(_STEWARD) not in sys.path:
    sys.path.insert(0, str(_STEWARD))

from detectors import d010_denominator_integrity as d010  # noqa: E402
from detectors._common import load_context  # noqa: E402


# ---------------------------------------------------------------------------
# fixture helpers
# ---------------------------------------------------------------------------

def build(root: Path, nodes: list[tuple[str, str]], snapshot: str | None,
          generation: str | None = None) -> Path:
    """One v3 plan with the given (node_id, status) pairs, plus a snapshot."""
    (root / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims" / "claims.yaml").write_text("[]\n", encoding="utf-8")
    plan = {"id": "p", "title": "P", "last_updated": "2026-08-18",
            "nodes": [{"id": nid, "title": nid, "status": st}
                      for nid, st in nodes]}
    if generation:
        plan["generation"] = generation
    (root / "evidence" / "planning" / "p_plan.md").write_text(
        "---\n" + yaml.safe_dump({"closure_plan": plan}, sort_keys=False)
        + "\n---\n\n# P\n", encoding="utf-8")
    if snapshot is not None:
        (root / "evidence" / "planning" / "closure_status.md").write_text(
            snapshot, encoding="utf-8")
    return root


def snapshot(denominator: int, tally: dict[str, int] | None,
             frontier: int | None = None, frontier_label: str = "Assembly frontier",
             pct: float = 50.0) -> str:
    """A closure_status.md shaped exactly like generate_closure_snapshot.py's."""
    lines = ["# REE-v3 Closure Status (snapshot)", "", "## Overall", ""]
    lines.append("- Weighted progress: **%s%%** across %d non-deferred nodes "
                 "in 1 plan(s) with closure frontmatter." % (pct, denominator))
    if frontier is not None:
        lines.append("- %s (required, under construction -- a SEPARATE axis, not "
                     "counted in the %% above and not a stalled backlog): **%d** "
                     "nodes." % (frontier_label, frontier))
    if tally is not None:
        lines.append("- Status tally: %s"
                     % "  ".join("%s=%d" % kv for kv in sorted(tally.items())))
    lines += ["", "## Plans", "", "(none)", ""]
    return "\n".join(lines) + "\n"


def run(root: Path):
    findings, summary = d010.run(load_context(root))
    return {f["finding_id"]: f for f in findings}, summary


def silent_ids(found):
    return [k for k in found if k.startswith("D-010:silent_exclusion_surface")]


def mismatch_ids(found):
    return [k for k in found if k.startswith("D-010:snapshot_denominator_mismatch")]


# ---------------------------------------------------------------------------
# CHECK 2 -- the labelled/silent partition
# ---------------------------------------------------------------------------

def test_labelled_assembling_is_not_a_finding(tmp_path):
    """The live case. 2 assembling + 2 done, frontier line states 2 -> quiet."""
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("b", "assembling"),
                  ("c", "done"), ("d", "done")],
                 snapshot(2, {"assembling": 2, "done": 2}, frontier=2))
    found, summary = run(root)
    assert silent_ids(found) == []
    # ...and the exclusion is still AUDITABLE rather than vanishing with it.
    assert summary["labelled_exclusions"] == {"assembling": 2}
    assert summary["silent_exclusions"] == {}


def test_missing_label_still_fires(tmp_path):
    """NEGATIVE CONTROL: drop the frontier line and the finding must come back."""
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("b", "assembling"),
                  ("c", "done"), ("d", "done")],
                 snapshot(2, {"assembling": 2, "done": 2}, frontier=None))
    found, summary = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=assembling"]
    assert summary["labelled_exclusions"] == {}


def test_stale_label_count_still_fires(tmp_path):
    """A frontier line saying 7 while 2 are excluded is a second wrong number."""
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("b", "assembling"),
                  ("c", "done"), ("d", "done")],
                 snapshot(2, {"assembling": 2, "done": 2}, frontier=7))
    found, _ = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=assembling"]


def test_renamed_label_still_fires(tmp_path):
    """EXCLUSION_LABELS is a wording contract; a rename must escalate, not pass."""
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("c", "done")],
                 snapshot(1, {"assembling": 1, "done": 1}, frontier=1,
                          frontier_label="Under construction"))
    found, _ = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=assembling"]


def test_new_unlabelled_status_fires_beside_a_labelled_one(tmp_path):
    """THE POINT OF THE SUBJECT REFINE.

    `parked` has no label. It must fire on its own merits, with its own
    finding_id, while `assembling` stays quiet -- which is exactly what a
    constant-subject suppression of the old finding could never have expressed.
    """
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("p", "parked"), ("c", "done")],
                 snapshot(1, {"assembling": 1, "parked": 1, "done": 1}, frontier=1))
    found, summary = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=parked"]
    assert summary["labelled_exclusions"] == {"assembling": 1}
    assert summary["silent_exclusions"] == {"parked": 1}


def test_subject_carries_the_whole_status_set(tmp_path):
    """Two unlabelled statuses -> one finding, one id, both named and sorted."""
    root = build(tmp_path / "r",
                 [("p", "parked"), ("z", "closed"), ("c", "done")],
                 snapshot(1, {"parked": 1, "closed": 1, "done": 1}))
    found, _ = run(root)
    assert silent_ids(found) == \
        ["D-010:silent_exclusion_surface@statuses=closed,parked"]


def test_shared_marker_is_checked_against_the_sum(tmp_path):
    """assembling + open_by_design are ONE number in the snapshot.

    generate_closure_snapshot.ASSEMBLING_STATUSES reports them together, so
    checking either count alone would fire spuriously the first time an
    open_by_design node appeared.
    """
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("b", "assembling"),
                  ("o", "open_by_design"), ("c", "done")],
                 snapshot(1, {"assembling": 2, "open_by_design": 1, "done": 1},
                          frontier=3))
    found, summary = run(root)
    assert silent_ids(found) == []
    assert summary["labelled_exclusions"] == {"assembling": 2, "open_by_design": 1}


def test_absent_snapshot_reads_as_unlabelled(tmp_path):
    """Fail LOUD: no snapshot means the label cannot be verified, not that it is fine."""
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("c", "done")], None)
    found, _ = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=assembling"]


def test_label_outside_the_overall_block_does_not_count(tmp_path):
    """A label further down the file does not stop the percentage being misread."""
    snap = snapshot(1, {"assembling": 1, "done": 1}, frontier=None)
    snap += "\n## Assembly frontier -- required, under construction (1)\n"
    root = build(tmp_path / "r", [("a", "assembling"), ("c", "done")], snap)
    found, _ = run(root)
    assert silent_ids(found) == ["D-010:silent_exclusion_surface@statuses=assembling"]


def test_deferred_is_never_part_of_this_surface(tmp_path):
    """`deferred` IS what the snapshot says it excludes -- never a silent one."""
    root = build(tmp_path / "r",
                 [("x", "deferred"), ("y", "deferred_v4"), ("c", "done")],
                 snapshot(1, {"deferred": 1, "deferred_v4": 1, "done": 1}))
    found, summary = run(root)
    assert silent_ids(found) == []
    assert summary["silent_exclusions"] == {}


# ---------------------------------------------------------------------------
# CHECK 5 -- the lag discriminator
# ---------------------------------------------------------------------------

def test_matching_denominator_is_no_finding(tmp_path):
    root = build(tmp_path / "r", [("c", "done"), ("o", "open")],
                 snapshot(2, {"done": 1, "open": 1}))
    found, _ = run(root)
    assert mismatch_ids(found) == []


def test_differing_tally_is_regen_lag_and_does_not_escalate(tmp_path):
    """The live case: the snapshot was built from different plan content."""
    root = build(tmp_path / "r", [("c", "done"), ("o", "open"), ("b", "blocked")],
                 snapshot(2, {"done": 1, "open": 1}))          # stale: no `blocked`
    found, summary = run(root)
    assert mismatch_ids(found) == \
        ["D-010:snapshot_denominator_mismatch@lag=explained"]
    f = found["D-010:snapshot_denominator_mismatch@lag=explained"]
    assert f["severity"] == "P2"
    assert f["escalate"] is False
    assert f["evidence"]["lag"] == "explained"
    # the specific statuses that moved are named, not just "they differ"
    assert set(summary["tally_delta"]) == {"blocked"}


def test_identical_tally_is_a_rule_divergence_and_escalates(tmp_path):
    """NEGATIVE CONTROL, and the whole reason for the split.

    Same inputs, different answer. Regenerating will NOT fix this, so it must
    NOT be reported as lag -- it is the accounting breaking, which is what D-010
    exists for.
    """
    root = build(tmp_path / "r", [("c", "done"), ("o", "open")],
                 snapshot(7, {"done": 1, "open": 1}))          # tally agrees, N does not
    found, _ = run(root)
    assert mismatch_ids(found) == \
        ["D-010:snapshot_denominator_mismatch@lag=unexplained"]
    f = found["D-010:snapshot_denominator_mismatch@lag=unexplained"]
    assert f["severity"] == "P1"
    assert f["escalate"] is True


def test_unparseable_tally_escalates_rather_than_assuming_lag(tmp_path):
    """No tally line -> lag is undecidable -> take the loud branch."""
    root = build(tmp_path / "r", [("c", "done"), ("o", "open")],
                 snapshot(7, None))
    found, _ = run(root)
    assert mismatch_ids(found) == \
        ["D-010:snapshot_denominator_mismatch@lag=unknown"]
    assert found["D-010:snapshot_denominator_mismatch@lag=unknown"]["escalate"] is True


def test_lag_verdicts_have_distinct_finding_ids(tmp_path):
    """A lag mismatch resolving must not carry a rule divergence's history."""
    lag = build(tmp_path / "a", [("c", "done"), ("o", "open"), ("b", "blocked")],
                snapshot(2, {"done": 1, "open": 1}))
    rule = build(tmp_path / "b", [("c", "done"), ("o", "open")],
                 snapshot(7, {"done": 1, "open": 1}))
    assert mismatch_ids(run(lag)[0]) != mismatch_ids(run(rule)[0])


# ---------------------------------------------------------------------------
# guards against reverting the refinement
# ---------------------------------------------------------------------------

def test_constant_subjects_are_gone(tmp_path):
    """Both old finding_ids were constants; a suppression on either was a blanket.

    If this fails, someone has restored a subject that cannot express "this
    status is dispositioned but a new one is not".
    """
    root = build(tmp_path / "r",
                 [("a", "assembling"), ("c", "done"), ("b", "blocked")],
                 snapshot(1, {"assembling": 1, "done": 1}))
    found, _ = run(root)
    assert "D-010:silent_exclusion_surface" not in found
    assert "D-010:snapshot_denominator_mismatch" not in found


def test_structural_invariant_check_is_untouched(tmp_path):
    """The P0 check that the recomputation and the producer share a rule."""
    root = build(tmp_path / "r", [("c", "done")], snapshot(1, {"done": 1}))
    found, summary = run(root)
    assert "D-010:denominator_invariant" not in found
    assert summary["denominator"] == 1


def test_non_v3_plans_stay_out_of_the_surface(tmp_path):
    """A v4 plan's assembling nodes are not v3 denominator business."""
    root = build(tmp_path / "r", [("a", "assembling"), ("c", "done")],
                 snapshot(0, {}), generation="v4")
    found, summary = run(root)
    assert silent_ids(found) == []
    assert summary["v3_nodes"] == 0
