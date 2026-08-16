#!/usr/bin/env python3
"""Contract tests for D-007 -- stale gate reference.

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_d007_stale_gate_reference.py -q

THE PRIMARY TEST IS THE HISTORICAL REPLAY. D-007's whole risk is a framing risk,
not a parsing risk: the naive reading of a cleared gate is "the node should
open", and that reading would have been WRONG on all three recorded instances in
this repo. So the load-bearing assertion is not "the parser finds the gate" but
"the finding says the TEXT is stale and offers a consumer no way to read a status
transition out of it". `test_no_replay_finding_proposes_a_status_change` is the
constraint made executable; the rest support it.

The replay runs against REAL git history in this checkout -- REE_assembly's
history reaches back to 2026-02, so unlike the stage-3 git-lane replay (which
needed a range that lived only in the Mac's reflog) the actual historical trees
are reachable here. Each revision's evidence/planning/ is materialised into a
tmpdir and run through the ordinary load_context path, so the detector sees the
real frontmatter with the real prose, not a paraphrase of it.

Those tests SKIP if the history is not reachable (a shallow clone, or a copy of
this file run outside the repo). To stop that degrading into a vacuous pass, the
same three incidents are ALSO pinned as synthetic fixtures that always run --
`test_incident_*_synthetic` -- carrying the same statuses and the same real gate
strings lifted verbatim from the plan frontmatter.

Time-independent: no sleeps, no wall-clock dependence, no network. The replay
tests shell out to git in read-only mode (`ls-tree`, `show`) and never mutate
the checkout.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

_STEWARD = Path(__file__).resolve().parent
sys.path.insert(0, str(_STEWARD))

from detectors import DETECTORS, FIXABLE  # noqa: E402
from detectors import d007_stale_gate_reference as d007  # noqa: E402
from detectors._common import load_context  # noqa: E402


def _load_runner():
    spec = importlib.util.spec_from_file_location(
        "steward_run_detectors_d007", _STEWARD / "run_detectors.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["steward_run_detectors_d007"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


runner = _load_runner()

# The three recorded instances, as (revision, label, what the record says).
#
# 43ba39ca9e is the 2026-06-09 re-adjudication commit ("self_attribution
# GAP-1/2: re-adjudicate stale 2026-05-16 monostrategy gate vs landed GAP-A
# substrate"); its PARENT is the tree that carried the stale text.
# fb11650188 is the 2026-06-23 closure-map enhancement.
# 7e60b8a675 is the 2026-07-29 plan-doc reconcile.
REV_2026_06_09 = "43ba39ca9e^"
REV_2026_06_23 = "fb11650188"
REV_2026_07_29 = "7e60b8a675"

_REPO = _STEWARD.parents[1]          # REE_assembly/


def _git(args: list[str]):
    return subprocess.run(["git", "-C", str(_REPO)] + args,
                          capture_output=True, text=True)


def _history_available() -> bool:
    if not (_REPO / ".git").exists():
        return False
    for rev in (REV_2026_06_09, REV_2026_06_23, REV_2026_07_29):
        if _git(["rev-parse", "--verify", "--quiet", rev + "^{commit}"]).returncode:
            return False
    return True


_HAVE_HISTORY = _history_available()
_skip_no_history = pytest.mark.skipif(
    not _HAVE_HISTORY,
    reason="REE_assembly history for the 2026-06/07 incidents is not reachable "
           "in this checkout (shallow clone?); the synthetic incident fixtures "
           "below still run")


def materialise(rev: str, dest: Path) -> int:
    """Write evidence/planning/*_plan.md at `rev` into `dest`. Read-only."""
    (dest / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (dest / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    # D-007 reads no claims, but load_context records a parse error without it
    # and a noisy context makes a failure harder to read.
    (dest / "docs" / "claims" / "claims.yaml").write_text("[]\n", encoding="utf-8")
    listing = _git(["ls-tree", "--name-only", rev, "evidence/planning/"])
    assert listing.returncode == 0, listing.stderr
    n = 0
    for rel in listing.stdout.split():
        if not rel.endswith("_plan.md"):
            continue
        blob = subprocess.run(["git", "-C", str(_REPO), "show", "%s:%s" % (rev, rel)],
                              capture_output=True)
        assert blob.returncode == 0, rel
        (dest / rel).write_bytes(blob.stdout)
        n += 1
    return n


def run_at(rev: str, tmp_path: Path):
    dest = tmp_path / rev.replace("^", "_parent")
    n = materialise(rev, dest)
    assert n > 0, "no plans materialised at %s -- the replay would pass vacuously" % rev
    ctx = load_context(dest)
    return d007.run(ctx)


def by_node(findings: list[dict], node_id: str) -> dict | None:
    for f in findings:
        if f["evidence"]["node_id"] == node_id:
            return f
    return None


# ---------------------------------------------------------------------------
# synthetic fixture helpers (mirrors test_run_detectors.py's shape)
# ---------------------------------------------------------------------------

def make_repo(root: Path, plans: dict[str, dict]) -> Path:
    (root / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims" / "claims.yaml").write_text("[]\n", encoding="utf-8")
    for name, p in plans.items():
        body = ("---\n" + yaml.safe_dump({"closure_plan": p}, sort_keys=False)
                + "\n---\n\n# %s\n" % name)
        (root / "evidence" / "planning" / ("%s_plan.md" % name)).write_text(
            body, encoding="utf-8")
    return root


def plan(pid, nodes):
    return {"id": pid, "title": pid, "nodes": nodes}


def node(nid, status, blocking_external=None, resume_condition=None,
         depends_on=None):
    n = {"id": nid, "status": status, "title": nid}
    if blocking_external is not None:
        n["blocking_external"] = blocking_external
    if resume_condition is not None:
        n["resume_condition"] = resume_condition
    if depends_on is not None:
        n["depends_on"] = depends_on
    return n


def run_synthetic(tmp_path: Path, plans: dict[str, dict]):
    root = make_repo(tmp_path / "repo", plans)
    return d007.run(load_context(root))


# ===========================================================================
# THE PRIMARY TEST -- the framing constraint, made executable
# ===========================================================================

@_skip_no_history
@pytest.mark.parametrize("rev", [REV_2026_06_09, REV_2026_06_23, REV_2026_07_29])
def test_no_replay_finding_proposes_a_status_change(rev, tmp_path):
    """THE load-bearing assertion. Every recorded instance ended with the node
    correctly STILL BLOCKED on a re-pointed gate, so a finding that structurally
    offers "the node should open" would have been wrong all three times."""
    findings, _ = run_at(rev, tmp_path)
    assert findings, "replay at %s produced nothing -- it cannot be checking the framing" % rev
    for f in findings:
        assert f["tier"] == "T1"
        assert f["autofix"] is False
        # Structural, not prose: no field anywhere a consumer could read a
        # transition or a repair out of.
        d007.assert_no_status_proposal([f])
        # And the finding says what it IS about.
        assert "documentation-accuracy" in f["evidence"]["framing"]
        assert "NOT AN UNBLOCK SIGNAL" in f["detail"]


@_skip_no_history
def test_replay_2026_06_09_reports_stale_gate_text(tmp_path):
    """2026-06-09: self_attribution:GAP-1's blocking_external named
    sleep_substrate:GAP-1, which was already `done`. The governance note that
    day recorded exactly this ("Two of GAP-1's three blocking_external
    prerequisites are DONE") and left the node BLOCKED on a re-pointed gate."""
    findings, summary = run_at(REV_2026_06_09, tmp_path)
    f = by_node(findings, "self_attribution:GAP-1")
    assert f is not None, "the 2026-06-09 stale gate text was not detected"
    assert f["evidence"]["gates_cleared"] == ["sleep_substrate:GAP-1"]
    assert f["evidence"]["gate_fields"] == ["blocking_external"]
    assert f["severity"] == "P1"          # the one resolvable gate had cleared
    assert summary["detector"] == "D-007"


@_skip_no_history
def test_replay_2026_06_23_is_p2_partial_clearance(tmp_path):
    """2026-06-23: behavioral_diversity_isolation:GAP-A went `done`, and
    self_attribution:GAP-2's gate names "GAP-A/GAP-B". GAP-B had NOT cleared, so
    this is the partial tier. The node record names the naive reading by name as
    "the same env-conditional trap the axis_b autopsy caught"."""
    findings, _ = run_at(REV_2026_06_23, tmp_path)
    f = by_node(findings, "self_attribution:GAP-2")
    assert f is not None
    assert f["severity"] == "P2", "partial clearance must rank below total"
    assert f["evidence"]["gates_cleared"] == ["behavioral_diversity_isolation:GAP-A"]
    assert f["evidence"]["gates_outstanding"] == ["behavioral_diversity_isolation:GAP-B"]
    # The compound "GAP-A/GAP-B" token really did expand into two gates.
    assert len(f["evidence"]["gates_named"]) == 2


@_skip_no_history
def test_replay_2026_07_29_is_p1_all_named_gates_cleared(tmp_path):
    """2026-07-29 status-table reconcile: sleep_substrate:GAP-1 and
    goal_pipeline:GAP-1 both `done`. Every gate node GAP-1's text names had
    cleared, so the stated rationale was entirely vacuous -- P1. The node still
    correctly stayed blocked, on a re-pointed third gate."""
    findings, _ = run_at(REV_2026_07_29, tmp_path)
    f = by_node(findings, "self_attribution:GAP-1")
    assert f is not None
    assert f["severity"] == "P1"
    assert f["evidence"]["gates_outstanding"] == []
    assert "entirely vacuous" in f["detail"]


@_skip_no_history
def test_replays_are_not_vacuous(tmp_path):
    """Guard on the replay harness itself: a materialisation that silently
    produced an empty or tiny tree would make every replay above pass by
    finding nothing to contradict."""
    for rev, min_nodes in ((REV_2026_06_09, 50), (REV_2026_06_23, 200),
                           (REV_2026_07_29, 200)):
        dest = tmp_path / ("probe_" + rev.replace("^", "_p"))
        assert materialise(rev, dest) >= 10
        ctx = load_context(dest)
        assert len(ctx.nodes) >= min_nodes


# ===========================================================================
# The same three incidents as synthetic fixtures -- these ALWAYS run, so a
# skipped replay never leaves the framing unpinned.
# ===========================================================================

def test_incident_2026_06_09_synthetic_is_p1(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "self_attribution": plan("self_attribution", [
            node("self_attribution:GAP-1", "blocked",
                 blocking_external=[
                     "sleep_substrate:GAP-1 Phase 1 PASS",
                     "MECH-269 V_s monostrategy landing",
                     "MECH-307 conjunction architecture"]),
        ]),
        "sleep_substrate": plan("sleep_substrate", [
            node("sleep_substrate:GAP-1", "done"),
        ]),
    })
    assert len(findings) == 1
    assert findings[0]["severity"] == "P1"
    assert findings[0]["evidence"]["gates_cleared"] == ["sleep_substrate:GAP-1"]
    # The two claim-shaped prerequisites (MECH-269, MECH-307) are deliberately
    # NOT resolved -- D-007 keys on plan:NODE gates only.
    assert findings[0]["evidence"]["gates_named"] == ["sleep_substrate:GAP-1"]


def test_incident_2026_06_23_synthetic_is_p2(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "self_attribution": plan("self_attribution", [
            node("self_attribution:GAP-2", "blocked",
                 blocking_external=[
                     "behavioral_diversity_isolation:GAP-A/GAP-B "
                     "behaviourally-validated non-monostrategy policy in the "
                     "main agent path (the re-pointed gate; supersedes the "
                     "stale 2026-05-16 'SP-CEM in main path' satisfier)"]),
        ]),
        "behavioral_diversity_isolation": plan("behavioral_diversity_isolation", [
            node("behavioral_diversity_isolation:GAP-A", "done"),
            node("behavioral_diversity_isolation:GAP-B", "partial"),
        ]),
    })
    assert len(findings) == 1
    assert findings[0]["severity"] == "P2"
    assert findings[0]["evidence"]["gates_cleared"] == \
        ["behavioral_diversity_isolation:GAP-A"]
    assert findings[0]["evidence"]["gates_outstanding"] == \
        ["behavioral_diversity_isolation:GAP-B"]


def test_incident_2026_07_29_synthetic_reports_text_not_status(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "self_attribution": plan("self_attribution", [
            node("self_attribution:GAP-1", "blocked",
                 blocking_external=["sleep_substrate:GAP-1 Phase 1 PASS",
                                    "goal_pipeline:GAP-1 conjunction architecture"]),
        ]),
        "sleep_substrate": plan("sleep_substrate", [node("sleep_substrate:GAP-1", "done")]),
        "goal_pipeline": plan("goal_pipeline", [node("goal_pipeline:GAP-1", "done")]),
    })
    assert len(findings) == 1
    f = findings[0]
    assert f["severity"] == "P1"
    assert sorted(f["evidence"]["gates_cleared"]) == \
        ["goal_pipeline:GAP-1", "sleep_substrate:GAP-1"]
    # The node is STILL blocked and the finding must not suggest otherwise.
    assert f["evidence"]["node_status"] == "blocked"
    d007.assert_no_status_proposal([f])


# ===========================================================================
# Schema contract -- "no autofix payload, no suggested status transition"
# ===========================================================================

def test_d007_is_permanently_t1(tmp_path):
    assert d007.TIER == "T1"
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert summary["tier"] == "T1"
    assert all(f["tier"] == "T1" and f["autofix"] is False for f in findings)


def test_d007_offers_no_fix_entry_point():
    """A T0 detector exposes fix(); D-007 must not, and must not be registered
    as fixable. Re-pointing a gate IS the judgement."""
    assert not hasattr(d007, "fix")
    assert d007 not in FIXABLE
    assert d007 in DETECTORS


@pytest.mark.parametrize("bad_key", sorted(d007.FORBIDDEN_KEYS))
def test_forbidden_key_anywhere_raises(bad_key):
    f = {"finding_id": "D-007:x", "tier": "T1", "autofix": False,
         "evidence": {"nested": {bad_key: "anything"}}}
    with pytest.raises(d007.StatusProposalForbidden):
        d007.assert_no_status_proposal([f])


def test_forbidden_key_in_a_list_raises():
    f = {"finding_id": "D-007:x", "tier": "T1", "autofix": False,
         "evidence": {"items": [{"ok": 1}, {"proposed_status": "open"}]}}
    with pytest.raises(d007.StatusProposalForbidden):
        d007.assert_no_status_proposal([f])


def test_autofix_true_raises():
    f = {"finding_id": "D-007:x", "tier": "T1", "autofix": True, "evidence": {}}
    with pytest.raises(d007.StatusProposalForbidden):
        d007.assert_no_status_proposal([f])


@pytest.mark.parametrize("tier", ["T0", "T2"])
def test_non_t1_tier_raises(tier):
    f = {"finding_id": "D-007:x", "tier": tier, "autofix": False, "evidence": {}}
    with pytest.raises(d007.StatusProposalForbidden):
        d007.assert_no_status_proposal([f])


def test_clean_finding_passes_the_guard(tmp_path):
    """Negative control: the guard must not fire on the detector's own output,
    or it would be a guard nobody can ship behind."""
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    d007.assert_no_status_proposal(findings)     # must not raise


# ===========================================================================
# Suppression key -- (node, gate-set)
# ===========================================================================

_SETTLED = {
    "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:DONE1", "beta_gate:OPEN1"])]),
    "beta_gate": plan("beta_gate", [node("beta_gate:DONE1", "done"), node("beta_gate:OPEN1", "open")]),
}


def _fid(tmp_path, plans, sub="repo"):
    root = make_repo(tmp_path / sub, plans)
    findings, _ = d007.run(load_context(root))
    assert len(findings) == 1
    return findings[0]["finding_id"]


def test_finding_id_is_stable_across_identical_runs(tmp_path):
    """A settled adjudication ("still blocked, gate re-pointed") must not
    re-escalate every cycle."""
    assert _fid(tmp_path, _SETTLED, "r1") == _fid(tmp_path, _SETTLED, "r2")


def test_repointing_the_gate_changes_the_finding_id(tmp_path):
    repointed = {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             blocking_external=["beta_gate:DONE1", "beta_gate:OPEN2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:DONE1", "done"), node("beta_gate:OPEN1", "open"),
                        node("beta_gate:OPEN2", "open")]),
    }
    assert _fid(tmp_path, _SETTLED, "r1") != _fid(tmp_path, repointed, "r2")


def test_a_second_gate_clearing_changes_the_finding_id(tmp_path):
    """P2 -> P1 is news: the node's stated rationale has gone from partly stale
    to entirely vacuous, and that is precisely what the severity tier ranks."""
    now_all_done = {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             blocking_external=["beta_gate:DONE1", "beta_gate:OPEN1"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:DONE1", "done"), node("beta_gate:OPEN1", "done")]),
    }
    root = make_repo(tmp_path / "r2", now_all_done)
    findings, _ = d007.run(load_context(root))
    assert findings[0]["severity"] == "P1"
    assert _fid(tmp_path, _SETTLED, "r1") != findings[0]["finding_id"]


def test_status_churn_among_outstanding_gates_does_not_change_the_id(tmp_path):
    """Only the cleared/outstanding PARTITION is folded into the id, never a raw
    status -- a gate moving `open` -> `in_progress` (outstanding either way)
    must not churn the key and re-escalate a settled finding."""
    churned = {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             blocking_external=["beta_gate:DONE1", "beta_gate:OPEN1"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:DONE1", "done"),
                        node("beta_gate:OPEN1", "in_progress")]),
    }
    assert _fid(tmp_path, _SETTLED, "r1") == _fid(tmp_path, churned, "r2")


def test_settled_finding_does_not_re_escalate_through_the_runner(tmp_path):
    """End-to-end through the runner's NEW/RECURRING classification: loud once,
    quiet after."""
    root = make_repo(tmp_path / "repo", _SETTLED)
    state = tmp_path / "state"
    state.mkdir()
    ctx = load_context(root)
    r1 = runner.build_report(ctx, state, "2026-08-16T00:00:00Z", 0.0)
    d7 = [f for f in r1["findings"] if f["detector"] == "D-007"]
    assert len(d7) == 1 and d7[0]["classification"] == "NEW"
    assert d7[0]["finding_id"] in r1["escalated"]

    runner.write_state(state, r1, "2026-08-16T00:00:00Z")
    r2 = runner.build_report(load_context(root), state, "2026-08-16T01:00:00Z", 0.0)
    d7b = [f for f in r2["findings"] if f["detector"] == "D-007"]
    assert len(d7b) == 1 and d7b[0]["classification"] == "RECURRING"
    assert d7b[0]["finding_id"] not in r2["escalated"]


# ===========================================================================
# Framing negative controls -- the ways this detector must NOT fire
# ===========================================================================

def test_no_finding_when_nothing_has_cleared(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "in_progress")]),
    })
    assert findings == []


def test_depends_on_is_never_read(tmp_path):
    """THE TRAP GUARD. `depends_on` is the structured, map-rendered dependency
    edge, and "every depends_on is done therefore the node should open" is
    exactly the inference D-007 is forbidden from making. Reading it here would
    import that trap through the back door, so the field is out of scope even
    though it is the most gate-shaped field on the node."""
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", depends_on=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []
    assert summary["gate_bearing_nodes_scanned"] == 0

    # NON-VACUITY: the identical fixture with the identical gate moved into
    # blocking_external DOES fire, so the silence above is the field being out
    # of scope and not the fixture failing to reach the detector at all.
    positive, _ = run_synthetic(tmp_path / "positive", {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                                               blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert len(positive) == 1


@pytest.mark.parametrize("gate_status", ["deferred", "parked", "closed",
                                         "open_by_design", "assembling"])
def test_a_set_down_gate_is_not_a_cleared_gate(tmp_path, gate_status):
    """CLEARED means `done` alone -- deliberately NOT the wider "excluded from
    the closure denominator" set. A `deferred` or `parked` gate has not been
    satisfied, it has been set down, and reading that as cleared inverts the
    meaning."""
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", gate_status)]),
    })
    assert findings == []


@pytest.mark.parametrize("node_status", ["done", "closed", "partial",
                                         "in_progress", "in-progress"])
def test_terminal_or_moving_nodes_are_not_reported(tmp_path, node_status):
    """A node that is finished or demonstrably moving is not asserting that it
    is waiting, so its gate text is history rather than a stale claim."""
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", node_status, blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []


def test_self_reference_is_skipped(tmp_path):
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["alpha_work:N1 itself"])]),
    })
    assert findings == []
    assert summary["self_references_skipped"] == 1


# ===========================================================================
# Prose conservatism -- prefer a miss over a false positive
# ===========================================================================

def test_gate_clause_in_resume_condition_is_read(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             resume_condition="RE-POINTED GATE: resume once "
                                              "beta_gate:N2 lands behaviourally.")]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert len(findings) == 1
    assert findings[0]["evidence"]["gate_fields"] == ["resume_condition"]


def test_citation_clause_is_vetoed(tmp_path):
    """Real clauses from self_attribution:GAP-2's resume_condition. Both name a
    plan:NODE and both carry a gate cue ("after", "gate"), but both are
    cross-references to evidence rather than gate declarations -- which is why
    the citation veto has to beat the gate cue rather than the other way round."""
    prose = (
        "Empirical proof of insufficiency: beta_gate:N2 records 'V3-EXQ-543l ran "
        "2026-05-26 with SP-CEM live and still collapsed'; the V3-EXQ-614e "
        "autopsy located the real bottleneck after one E2 world-forward step. "
        "See the 2026-06-09 re-adjudication note + beta_gate:N2 (identical gate)."
    )
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", resume_condition=prose)]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []
    assert summary["prose_tokens_vetoed"] >= 2


def test_narrative_clause_without_a_gate_cue_is_vetoed(tmp_path):
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             resume_condition="The substrate landed in "
                                              "beta_gate:N2 and the smoke was clean.")]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []
    assert summary["prose_tokens_vetoed"] == 1


def test_a_reference_cannot_satisfy_its_own_gate_cue(tmp_path):
    """A node or plan id containing a cue word must not make every passing
    mention of it read as a gate. The live corpus really does contain
    `global_workspace_jlens:GATE-B`, and the fixture plan id `beta_gate` above
    carries the same hazard -- both would qualify every clause they appear in
    if cues were tested against the raw text.

    Non-vacuity: the SAME reference in a clause that really does declare a gate
    still fires (second half), so this pins the discrimination, not silence."""
    narrative = {
        "alpha_work": plan("alpha_work", [
            node("alpha_work:N1", "blocked",
                 resume_condition="Superseded by workspace_gate:GATE-B in the "
                                  "2026-06 redesign, which shipped.")]),
        "workspace_gate": plan("workspace_gate", [node("workspace_gate:GATE-B", "done")]),
    }
    findings, summary = run_synthetic(tmp_path, narrative)
    assert findings == [], "a cue word inside the reference must not count"
    assert summary["prose_tokens_vetoed"] == 1

    declaring = {
        "alpha_work": plan("alpha_work", [
            node("alpha_work:N1", "blocked",
                 resume_condition="Resume only once workspace_gate:GATE-B has "
                                  "built and smoke-tested the access gate.")]),
        "workspace_gate": plan("workspace_gate", [node("workspace_gate:GATE-B", "done")]),
    }
    findings2, _ = run_synthetic(tmp_path / "second", declaring)
    assert len(findings2) == 1
    assert findings2[0]["evidence"]["gates_cleared"] == ["workspace_gate:GATE-B"]


def test_blocking_external_needs_no_cue(tmp_path):
    """blocking_external is a DECLARED gate list, so every plan:NODE token in it
    is a gate -- the cue machinery applies to free text only."""
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert len(findings) == 1


def test_bare_node_id_without_a_plan_prefix_is_ignored(tmp_path):
    """The corpus writes bare "GAP-B" and "arc_062 GAP-B" constantly. Resolving
    those needs a guess about which plan is meant, which is the false positive
    the conservatism rule forbids."""
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             resume_condition="Blocked until GAP-B lands.")]),
        "beta_gate": plan("beta_gate", [node("beta_gate:GAP-B", "done")]),
    })
    assert findings == []


def test_unknown_plan_prefix_is_ignored_and_counted(tmp_path):
    """`generation:v4` / `status:deferred` really do occur in the corpus and
    match the token shape. They are dropped, not resolved."""
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             blocking_external=["generation:v4 is required",
                                                "status:deferred upstream"])]),
    })
    assert findings == []
    assert summary["non_plan_tokens_ignored"] == 2


def test_dangling_gate_ref_is_counted_not_guessed(tmp_path):
    """A REAL plan naming a node that does not exist in it is a different
    defect (a dangling closure link) and is counted rather than repaired."""
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:GONE"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []
    assert summary["dangling_gate_refs"] == 1


def test_compound_slash_token_expands_to_every_named_node(tmp_path):
    findings, _ = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked",
                             blocking_external=["beta_gate:GAP-A/GAP-B/GAP-C now"])]),
        "beta_gate": plan("beta_gate", [node("beta_gate:GAP-A", "done"), node("beta_gate:GAP-B", "done"),
                        node("beta_gate:GAP-C", "open")]),
    })
    assert len(findings) == 1
    ev = findings[0]["evidence"]
    assert ev["gates_named"] == ["beta_gate:GAP-A", "beta_gate:GAP-B", "beta_gate:GAP-C"]
    assert ev["gates_cleared"] == ["beta_gate:GAP-A", "beta_gate:GAP-B"]
    assert findings[0]["severity"] == "P2"


# ===========================================================================
# The precision floor
# ===========================================================================

_FLOOR_FIXTURE = {
    "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked", blocking_external=["beta_gate:N2"])]),
    "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
}


def test_above_the_floor_the_detector_escalates(tmp_path, monkeypatch):
    monkeypatch.setattr(d007, "MEASURED_PRECISION", 0.9)
    findings, summary = run_synthetic(tmp_path, _FLOOR_FIXTURE)
    assert summary["escalating"] is True
    assert findings[0]["escalate"] is True


def test_below_the_floor_is_list_only_but_still_reported(tmp_path, monkeypatch):
    """A floor gates ESCALATION only. Withholding the finding from the report
    would be the failure D-002's docstring refutes -- severity and confidence
    RANK findings, they never remove one."""
    monkeypatch.setattr(d007, "MEASURED_PRECISION", 0.4)
    findings, summary = run_synthetic(tmp_path, _FLOOR_FIXTURE)
    assert summary["escalating"] is False
    assert len(findings) == 1                  # still reported
    assert findings[0]["escalate"] is False    # just not escalated


def test_unmeasured_precision_is_list_only(tmp_path, monkeypatch):
    """An unvalidated detector carrying a precision floor has not earned the
    right to wake a model."""
    monkeypatch.setattr(d007, "MEASURED_PRECISION", None)
    findings, summary = run_synthetic(tmp_path, _FLOOR_FIXTURE)
    assert summary["escalating"] is False
    assert findings[0]["escalate"] is False


def test_the_shipped_measurement_is_recorded_and_above_the_floor():
    """The shipped constants are evidence, not a target -- pin that they are
    actually filled in, so a later edit cannot quietly blank them."""
    assert d007.PRECISION_FLOOR == 0.6
    assert d007.MEASURED_PRECISION is not None
    assert d007.MEASURED_PRECISION >= d007.PRECISION_FLOOR
    assert "n=3" in d007.MEASURED_AT and "REE_assembly" in d007.MEASURED_AT
    assert d007.escalates() is True


# ===========================================================================
# Runner integration
# ===========================================================================

def test_detector_is_registered_and_reports_through_the_runner(tmp_path):
    root = make_repo(tmp_path / "repo", _FLOOR_FIXTURE)
    state = tmp_path / "state"
    state.mkdir()
    report = runner.build_report(load_context(root), state,
                                 "2026-08-16T00:00:00Z", 0.0)
    ids = [s["detector"] for s in report["detectors"]]
    assert "D-007" in ids
    s = next(s for s in report["detectors"] if s["detector"] == "D-007")
    assert not s.get("error"), s.get("error")
    assert s["n_findings"] == 1


def test_a_clean_tree_produces_no_d007_finding(tmp_path):
    """The quiet case: nothing named, nothing cleared, no finding, no escalation."""
    findings, summary = run_synthetic(tmp_path, {
        "alpha_work": plan("alpha_work", [node("alpha_work:N1", "blocked")]),
        "beta_gate": plan("beta_gate", [node("beta_gate:N2", "done")]),
    })
    assert findings == []
    assert summary["n_findings"] == 0
    assert summary["gate_bearing_nodes_scanned"] == 0
