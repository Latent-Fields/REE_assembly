#!/usr/bin/env python3
"""Contract tests for the Steward stage 1 detector runner.

Run from REE_assembly/ root:
    /opt/local/bin/python3 -m pytest scripts/steward/test_run_detectors.py -q

Every test builds a SYNTHETIC repo in a tmpdir rather than asserting against the
live tree. That is deliberate: the live findings are expected to change (the
2026-08-15 adjudication PROPOSED un-deferring three owning nodes to governance,
and when governance acts those D-002 findings correctly disappear). A test
pinned to the live count would then fail on a CORRECT fix and teach the next
session to weaken the detector. So the classification logic is pinned here and
the live numbers are recorded in README.md as a baseline to re-measure, not as
an assertion.

Time-independent: no sleeps, no wall-clock dependence, no network, no git.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

_STEWARD = Path(__file__).resolve().parent


def _load_runner():
    spec = importlib.util.spec_from_file_location(
        "steward_run_detectors", _STEWARD / "run_detectors.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["steward_run_detectors"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


runner = _load_runner()


# ---------------------------------------------------------------------------
# fixture helpers
# ---------------------------------------------------------------------------

def make_repo(root: Path, claims: list[dict], plans: dict[str, dict]) -> Path:
    """Build a minimal REE_assembly-shaped tree."""
    (root / "docs" / "claims").mkdir(parents=True, exist_ok=True)
    (root / "evidence" / "planning").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "claims" / "claims.yaml").write_text(
        yaml.safe_dump(claims, sort_keys=False), encoding="utf-8")
    for name, plan in plans.items():
        body = "---\n" + yaml.safe_dump({"closure_plan": plan}, sort_keys=False) \
               + "\n---\n\n# %s\n" % name
        (root / "evidence" / "planning" / ("%s_plan.md" % name)).write_text(
            body, encoding="utf-8")
    return root


def claim(cid, phase="v3", v3_pending=None, status="candidate"):
    c = {"id": cid, "status": status, "implementation_phase": phase}
    if v3_pending is not None:
        c["v3_pending"] = v3_pending
    return c


def plan(pid, nodes, generation=None):
    p = {"id": pid, "title": pid, "nodes": nodes}
    if generation:
        p["generation"] = generation
    return p


def node(nid, status, unblocks=()):
    return {"id": nid, "status": status, "title": nid,
            "unblocks_claims": list(unblocks)}


def run_once(repo: Path, state_dir: Path) -> dict:
    """Run the full pipeline once, writing state (so the next call diffs)."""
    state_dir.mkdir(parents=True, exist_ok=True)
    from detectors._common import load_context  # noqa: WPS433
    ctx = load_context(repo)
    now = "2026-01-01T00:00:0%dZ" % (runner.load_state(
        state_dir / runner.STATE_FILE).get("runs", 0) % 10)
    report = runner.build_report(ctx, state_dir, now, 0.0)
    runner.write_state(state_dir, report, now)
    return report


def ids(report, detector=None):
    return sorted(f["finding_id"] for f in report["findings"]
                  if detector is None or f["detector"] == detector)


# A repo with one genuine D-002 orphan: claim is live v3, its only owning node
# is deferred.
ORPHAN_CLAIMS = [claim("MECH-001", phase="v3", v3_pending=True)]
ORPHAN_PLANS = {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                             ["MECH-001"])])}


# ---------------------------------------------------------------------------
# classification: NEW / RECURRING / RESOLVED
# ---------------------------------------------------------------------------

def test_first_run_is_new_and_escalates(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    r = run_once(repo, tmp_path / "state")
    assert "D-002:MECH-001" in ids(r)
    f = next(x for x in r["findings"] if x["finding_id"] == "D-002:MECH-001")
    assert f["classification"] == "NEW"
    assert r["escalate"] is True
    assert "D-002:MECH-001" in r["escalated"]


def test_second_identical_run_is_recurring_and_does_not_escalate(tmp_path):
    """The budget mechanism. An unfixed defect is real but it is not NEWS."""
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    first = run_once(repo, state)
    assert first["escalate"] is True

    second = run_once(repo, state)
    f = next(x for x in second["findings"] if x["finding_id"] == "D-002:MECH-001")
    assert f["classification"] == "RECURRING"
    assert f["times_seen"] == 2
    assert second["escalate"] is False, "a repeat run must not re-escalate"
    assert second["escalated"] == []


def test_first_seen_is_preserved_across_runs(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    first = run_once(repo, state)
    seen = next(x for x in first["findings"]
                if x["finding_id"] == "D-002:MECH-001")["first_seen"]
    second = run_once(repo, state)
    again = next(x for x in second["findings"]
                 if x["finding_id"] == "D-002:MECH-001")
    assert again["first_seen"] == seen


def test_fixing_the_defect_reports_it_resolved(tmp_path):
    """SD-031 vanishing from D-002 is the ratchet working -- pin that path."""
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    run_once(repo, state)

    # Governance un-defers the owning node: the orphan is discharged.
    make_repo(repo, ORPHAN_CLAIMS,
              {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked",
                                            ["MECH-001"])])})
    r = run_once(repo, state)
    assert "D-002:MECH-001" not in ids(r)
    assert [x["finding_id"] for x in r["resolved"]] == ["D-002:MECH-001"]
    assert r["counts"]["resolved"] == 1
    assert r["escalate"] is False, "a resolution is reported, never escalated"


def test_resolved_finding_does_not_linger_into_the_next_run(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    run_once(repo, state)
    make_repo(repo, ORPHAN_CLAIMS,
              {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked",
                                            ["MECH-001"])])})
    run_once(repo, state)
    r = run_once(repo, state)
    assert r["resolved"] == []


def test_reappearing_defect_is_new_again(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    run_once(repo, state)
    make_repo(repo, ORPHAN_CLAIMS,
              {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked",
                                            ["MECH-001"])])})
    run_once(repo, state)
    make_repo(repo, ORPHAN_CLAIMS, ORPHAN_PLANS)  # regressed
    r = run_once(repo, state)
    f = next(x for x in r["findings"] if x["finding_id"] == "D-002:MECH-001")
    assert f["classification"] == "NEW"
    assert r["escalate"] is True


def test_clean_repo_does_not_escalate(tmp_path):
    """The whole cost model: no findings -> the Steward skill never loads."""
    repo = make_repo(tmp_path / "repo",
                     [claim("MECH-001", phase="v3", v3_pending=True)],
                     {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked",
                                                   ["MECH-001"])])})
    r = run_once(repo, tmp_path / "state")
    assert r["escalate"] is False
    assert ids(r, "D-002") == []
    assert ids(r, "D-001") == []


# ---------------------------------------------------------------------------
# suppression filtering
# ---------------------------------------------------------------------------

def write_suppressions(state_dir: Path, entries: list[dict]) -> None:
    state_dir.mkdir(parents=True, exist_ok=True)
    (state_dir / runner.SUPPRESSIONS_FILE).write_text(
        yaml.safe_dump({"suppressions": entries}, sort_keys=False),
        encoding="utf-8")


def test_exact_suppression_blocks_escalation_but_keeps_the_finding(tmp_path):
    """A suppression de-prioritises; it must never hide."""
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    write_suppressions(state, [{"finding_id": "D-002:MECH-001",
                                "reason": "adjudicated, not a defect"}])
    r = run_once(repo, state)
    assert "D-002:MECH-001" in ids(r), "suppressed findings stay in the report"
    f = next(x for x in r["findings"] if x["finding_id"] == "D-002:MECH-001")
    assert f["suppressed"] is True
    assert f["suppression_reason"] == "adjudicated, not a defect"
    assert f["classification"] == "NEW"
    assert r["escalate"] is False
    assert r["counts"]["suppressed"] == 1


def test_glob_suppression_covers_a_class(tmp_path):
    repo = make_repo(
        tmp_path / "repo",
        [claim("MECH-001", "v3", True), claim("MECH-002", "v3", True)],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                      ["MECH-001", "MECH-002"])])})
    state = tmp_path / "state"
    write_suppressions(state, [{"finding_id": "D-002:*", "reason": "whole class"}])
    r = run_once(repo, state)
    assert len(ids(r, "D-002")) == 2
    assert all(f["suppressed"] for f in r["findings"] if f["detector"] == "D-002")
    assert r["escalate"] is False


def test_unrelated_suppression_does_not_match(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    write_suppressions(state, [{"finding_id": "D-002:SOMETHING-ELSE",
                                "reason": "x"}])
    r = run_once(repo, state)
    f = next(x for x in r["findings"] if x["finding_id"] == "D-002:MECH-001")
    assert f["suppressed"] is False
    assert r["escalate"] is True


def test_missing_suppressions_file_is_not_an_error(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    r = run_once(repo, tmp_path / "state")
    assert r["escalate"] is True


def test_shipped_suppressions_file_parses(tmp_path):
    """The seeded file must actually load -- a malformed one silently disarms."""
    entries = runner.load_suppressions(
        _STEWARD / "state" / runner.SUPPRESSIONS_FILE)
    assert len(entries) >= 3
    assert all(e.get("reason") for e in entries), \
        "every suppression must state a reason"
    assert any(e["finding_id"] == "D-001:MECH-099" for e in entries)


# ---------------------------------------------------------------------------
# D-002 predicate -- the regressions that actually bit during the build
# ---------------------------------------------------------------------------

def test_d002_does_not_fire_on_assembling_owners(tmp_path):
    """`assembling` is excluded from the denominator but is NOT a defect.

    It means "required for v3, under construction, leave it alone" -- the
    anti-forcing status. Widening the predicate from DEFERRED_STATUSES to the
    full weight-None set added three pure false positives on the live tree.
    """
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS,
                     {"alpha": plan("alpha", [node("alpha:GAP-1", "assembling",
                                                   ["MECH-001"])])})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-002") == []


def test_d002_fires_when_every_owner_is_deferred_not_when_one_is_live(tmp_path):
    repo = make_repo(
        tmp_path / "repo", ORPHAN_CLAIMS,
        {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred", ["MECH-001"]),
                                 node("alpha:GAP-2", "blocked", ["MECH-001"])])})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-002") == [], "one live owner makes the claim visible"


def test_d002_uses_unblocks_claims_not_scope_claims(tmp_path):
    """Ownership is `unblocks_claims`. `join.scope_claims` is a broad 'bears on'
    association -- one live node lists 2 of the former and 29 of the latter, so
    using it would make nearly every claim look owned by nearly every node."""
    n = node("alpha:GAP-1", "deferred", [])
    n["join"] = {"scope_claims": ["MECH-001"]}
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS,
                     {"alpha": plan("alpha", [n])})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-002") == []


def test_d002_escalates_weak_signal_too(tmp_path):
    """The refuted gate. v3_pending absent must NOT downgrade to list-only:
    MECH-314a was a real stale node an earlier signal gate would have withheld
    indefinitely. Ranking may reorder these; nothing may withhold one."""
    repo = make_repo(
        tmp_path / "repo",
        [claim("MECH-001", "v3", True), claim("MECH-002", "v3", None),
         claim("MECH-003", "v3", False)],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                      ["MECH-001", "MECH-002", "MECH-003"])])})
    r = run_once(repo, tmp_path / "state")
    d2 = [f for f in r["findings"] if f["detector"] == "D-002"]
    assert len(d2) == 3
    assert all(f["escalate"] for f in d2), \
        "every D-002 finding escalates regardless of signal strength"
    strong = [f for f in d2 if f["subject"] == "MECH-001"][0]
    weak = [f for f in d2 if f["subject"] == "MECH-002"][0]
    assert strong["signal"] == "strong" and weak["signal"] == "weak"
    assert runner.rank_score(strong) > runner.rank_score(weak), \
        "signal ranks, it does not gate"


def test_d002_ignores_claims_with_no_v3_owner(tmp_path):
    """That is the generation axis -- D-001's finding, not D-002's. Reporting it
    in both would double-count one claim and make both look noisier."""
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS,
                     {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                                   ["MECH-001"])], "v4")})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-002") == []
    assert ids(r, "D-001") == ["D-001:MECH-001"]


def test_d002_ignores_non_v3_claims(tmp_path):
    repo = make_repo(tmp_path / "repo", [claim("MECH-001", phase="v4")],
                     ORPHAN_PLANS)
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-002") == []


# ---------------------------------------------------------------------------
# D-001 predicate
# ---------------------------------------------------------------------------

def test_d001_ignores_benign_forward_backpointer(tmp_path):
    """A v4 roadmap plan back-pointing at a v3 claim that ALSO has a v3 owner is
    a forward reference, not a defect. The any-owner reading fires 63 times on
    the live tree; requiring no-v3-owner cuts it to 27."""
    repo = make_repo(
        tmp_path / "repo", [claim("MECH-001", "v3")],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked", ["MECH-001"])]),
         "beta": plan("beta", [node("beta:B-1", "open", ["MECH-001"])], "v4")})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-001") == []


def test_d001_fires_when_no_owner_shares_the_declared_phase(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [claim("MECH-001", "v3", True)],
        {"beta": plan("beta", [node("beta:B-1", "open", ["MECH-001"])], "v5")})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-001") == ["D-001:MECH-001"]
    f = r["findings"][0]
    assert f["evidence"]["owner_generations"] == ["v5"]
    assert f["severity"] == "P1" and f["signal"] == "strong"


def test_d001_ignores_consequence_free_cross_generation_drift(tmp_path):
    """A v4 claim owned only by a v5 plan is outside V3 accounting under BOTH
    readings, so neither side's staleness changes what closure reports."""
    repo = make_repo(
        tmp_path / "repo", [claim("MECH-001", "v4")],
        {"beta": plan("beta", [node("beta:B-1", "open", ["MECH-001"])], "v5")})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-001") == []


def test_d001_fires_on_non_v3_claim_inside_the_v3_denominator(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [claim("MECH-001", "v4")],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked", ["MECH-001"])])})
    r = run_once(repo, tmp_path / "state")
    assert ids(r, "D-001") == ["D-001:MECH-001"]


def test_d001_narrowing_is_counted_not_silent(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [claim("MECH-001", "v3")],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "blocked", ["MECH-001"])]),
         "beta": plan("beta", [node("beta:B-1", "open", ["MECH-001"])], "v4")})
    r = run_once(repo, tmp_path / "state")
    s = next(x for x in r["detectors"] if x["detector"] == "D-001")
    assert s["raw_owner_pairs_mismatched"] == 1
    assert s["benign_forward_backpointers_filtered"] == 1


# ---------------------------------------------------------------------------
# D-010 denominator integrity
# ---------------------------------------------------------------------------

def test_d010_denominator_excludes_every_weight_none_status(tmp_path):
    """The correction the brief's one-line spec gets wrong: the exclusion set is
    weight-is-None, which is a strict SUPERSET of DEFERRED_STATUSES."""
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done"),
                                 node("alpha:2", "blocked"),
                                 node("alpha:3", "deferred"),
                                 node("alpha:4", "assembling"),
                                 node("alpha:5", "parked")])})
    r = run_once(repo, tmp_path / "state")
    s = next(x for x in r["detectors"] if x["detector"] == "D-010")
    assert s["v3_nodes"] == 5
    assert s["denominator"] == 2, "deferred + assembling + parked all excluded"
    assert s["excluded"] == 3


def test_d010_reports_the_silent_exclusion_surface(tmp_path):
    """These fixtures write no closure_status.md, so nothing is labelled.

    The subject carries the status set as of the 2026-08-18 refinement -- see
    test_d010_denominator_integrity.py for the labelled/silent partition itself.
    """
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done"),
                                 node("alpha:2", "assembling"),
                                 node("alpha:3", "deferred")])})
    r = run_once(repo, tmp_path / "state")
    f = next(x for x in r["findings"]
             if x["finding_id"]
             == "D-010:silent_exclusion_surface@statuses=assembling")
    assert f["evidence"]["by_status"] == {"assembling": ["alpha:2"]}, \
        "deferred is labelled; assembling is the unlabelled exclusion"


def test_d010_quiet_when_every_exclusion_is_labelled_deferred(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done"),
                                 node("alpha:2", "deferred")])})
    r = run_once(repo, tmp_path / "state")
    assert "D-010:silent_exclusion_surface" not in ids(r)


def test_d010_flags_an_unknown_status(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done"),
                                 node("alpha:2", "brand_new_status")])})
    r = run_once(repo, tmp_path / "state")
    f = next(x for x in r["findings"] if x["finding_id"] == "D-010:unknown_status")
    assert "brand_new_status" in f["evidence"]["by_status"]
    assert f["severity"] == "P1"


def test_d010_excludes_non_v3_generations_from_the_denominator(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done")]),
         "beta": plan("beta", [node("beta:1", "done"),
                               node("beta:2", "open")], "v4")})
    r = run_once(repo, tmp_path / "state")
    s = next(x for x in r["detectors"] if x["detector"] == "D-010")
    assert s["v3_nodes"] == 1 and s["denominator"] == 1


def test_d010_flags_a_snapshot_denominator_mismatch(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done")])})
    (repo / "evidence" / "planning" / "closure_status.md").write_text(
        "- Weighted progress: **50.0%** across 99 non-deferred nodes in 1 plan(s).\n",
        encoding="utf-8")
    r = run_once(repo, tmp_path / "state")
    # No `Status tally:` line in this fixture, so lag is undecidable and the
    # 2026-08-18 refinement takes the loud branch rather than assuming lag.
    f = next(x for x in r["findings"]
             if x["finding_id"]
             == "D-010:snapshot_denominator_mismatch@lag=unknown")
    assert f["evidence"]["committed_denominator"] == 99
    assert f["evidence"]["recomputed_denominator"] == 1
    assert f["escalate"] is True


def test_d010_quiet_when_snapshot_agrees(tmp_path):
    repo = make_repo(
        tmp_path / "repo", [],
        {"alpha": plan("alpha", [node("alpha:1", "done")])})
    (repo / "evidence" / "planning" / "closure_status.md").write_text(
        "- Weighted progress: **100.0%** across 1 non-deferred nodes in 1 plan(s).\n",
        encoding="utf-8")
    r = run_once(repo, tmp_path / "state")
    assert not [i for i in ids(r)
                if i.startswith("D-010:snapshot_denominator_mismatch")]


# ---------------------------------------------------------------------------
# escalation budget
# ---------------------------------------------------------------------------

def test_escalation_is_capped_and_reports_the_truncation(tmp_path):
    """The cap is a BUDGET, not a filter -- everything stays in `findings` and
    the overflow is stated, so five never read as 'all of them'."""
    n = runner.MAX_ESCALATE + 3
    claims = [claim("MECH-%03d" % i, "v3", True) for i in range(n)]
    repo = make_repo(
        tmp_path / "repo", claims,
        {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                      [c["id"] for c in claims])])})
    r = run_once(repo, tmp_path / "state")
    assert len(ids(r, "D-002")) == n
    assert len(r["escalated"]) == runner.MAX_ESCALATE
    assert r["escalation_candidates"] == n
    assert r["escalation_truncated"] == 3


def test_escalation_is_ranked_by_severity_times_confidence(tmp_path):
    repo = make_repo(
        tmp_path / "repo",
        [claim("MECH-001", "v3", None), claim("MECH-002", "v3", True)],
        {"alpha": plan("alpha", [node("alpha:GAP-1", "deferred",
                                      ["MECH-001", "MECH-002"])])})
    r = run_once(repo, tmp_path / "state")
    assert r["escalated"][0] == "D-002:MECH-002", "P0 strong outranks P1 weak"


def test_report_is_json_serialisable_and_has_the_gate_key(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    r = run_once(repo, tmp_path / "state")
    round_tripped = json.loads(json.dumps(r, sort_keys=True))
    assert round_tripped["schema"] == "steward_report.v1"
    assert isinstance(round_tripped["escalate"], bool)


def test_a_broken_detector_does_not_kill_the_run(tmp_path, monkeypatch):
    """One detector raising must not take the other two down with it."""
    class Boom:
        DETECTOR_ID = "D-999"

        @staticmethod
        def run(ctx):
            raise RuntimeError("boom")

    from detectors import DETECTORS
    monkeypatch.setattr(runner, "DETECTORS", list(DETECTORS) + [Boom])
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    r = run_once(repo, tmp_path / "state")
    assert "D-002:MECH-001" in ids(r)
    broken = next(x for x in r["detectors"] if x["detector"] == "D-999")
    assert "boom" in broken["error"]


def test_ledger_appends_one_line_per_run(tmp_path):
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    state = tmp_path / "state"
    state.mkdir(parents=True, exist_ok=True)
    from detectors._common import load_context
    for _ in range(3):
        ctx = load_context(repo)
        rep = runner.build_report(ctx, state, "2026-01-01T00:00:00Z", 0.0)
        runner.append_ledger(state, rep, "2026-01-01T00:00:00Z")
        runner.write_state(state, rep, "2026-01-01T00:00:00Z")
    lines = (state / runner.LEDGER_FILE).read_text().strip().splitlines()
    assert len(lines) == 3
    entry = json.loads(lines[0])
    assert entry["by_detector"]["D-002"] == 1


def test_detectors_never_write_to_the_repo(tmp_path):
    """Stage 1 is READ ONLY -- no auto-fix, no queueing, no registry edit."""
    repo = make_repo(tmp_path / "repo", ORPHAN_CLAIMS, ORPHAN_PLANS)
    before = {p: p.read_bytes() for p in sorted(repo.rglob("*")) if p.is_file()}
    run_once(repo, tmp_path / "state")
    after = {p: p.read_bytes() for p in sorted(repo.rglob("*")) if p.is_file()}
    assert before == after


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
