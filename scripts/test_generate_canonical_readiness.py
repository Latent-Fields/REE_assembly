"""Tests for generate_canonical_readiness.py (GOV-UMPIRE-1 detector v1).

Time-independent: every fixture is a synthetic manifest corpus built in a
tempdir, never the real evidence/experiments/ corpus. Run with pytest, e.g.:

    /opt/local/bin/python3 -m pytest REE_assembly/scripts/test_generate_canonical_readiness.py -q

This file lives in REE_assembly/scripts/ (not REE_Working/scripts/), so it is
NOT part of the REE_Working/scripts/ corpus run_scripts_tests.sh drives; run it
directly with pytest per the module docstring above.
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_canonical_readiness as gcr  # noqa: E402


# --------------------------------------------------------------------------
# Fixture helpers
# --------------------------------------------------------------------------


def _write_flat(evidence_dir: Path, run_id: str, **fields) -> Path:
    rec = {"run_id": run_id, "experiment_type": fields.pop("experiment_type", run_id)}
    rec.update(fields)
    path = evidence_dir / f"{run_id}.json"
    path.write_text(json.dumps(rec))
    return path


def _write_nested(evidence_dir: Path, run_id: str, **fields) -> Path:
    rec = {"run_id": run_id, "experiment_type": fields.pop("experiment_type", run_id)}
    rec.update(fields)
    d = evidence_dir / run_id / "runs" / f"{run_id}_20260101T000000Z_v3"
    d.mkdir(parents=True, exist_ok=True)
    path = d / "manifest.json"
    path.write_text(json.dumps(rec))
    return path


@pytest.fixture
def evidence_dir():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "evidence" / "experiments"
        d.mkdir(parents=True)
        yield d


# --------------------------------------------------------------------------
# load_manifest_corpus
# --------------------------------------------------------------------------


def test_load_skips_non_manifest_top_level_files(evidence_dir):
    for name in gcr.NON_MANIFEST_TOP_LEVEL:
        (evidence_dir / name).write_text(json.dumps({"run_id": "should_not_load", "not_a_manifest": True}))
    _write_flat(evidence_dir, "real_run")
    merged, counts = gcr.load_manifest_corpus(evidence_dir)
    assert list(merged.keys()) == ["real_run"]
    assert counts["flat_candidates"] == 1  # only the real one is even attempted


def test_load_skips_unparseable_and_no_run_id(evidence_dir):
    (evidence_dir / "garbage.json").write_text("{not json")
    (evidence_dir / "no_id.json").write_text(json.dumps({"foo": "bar"}))
    _write_flat(evidence_dir, "real_run")
    merged, _ = gcr.load_manifest_corpus(evidence_dir)
    assert list(merged.keys()) == ["real_run"]


def test_load_merges_flat_and_nested_field_level_not_whole_record(evidence_dir):
    """The critical bug this detector must not reproduce: a naive whole-record
    'prefer nested' merge silently drops enabled_default_off_flags for any
    run_id that also has a nested pack (the newer schema omits that field)."""
    _write_flat(
        evidence_dir,
        "run_a",
        enabled_default_off_flags={"use_thing": True},
        claim_ids=["MECH-001"],
    )
    _write_nested(
        evidence_dir,
        "run_a",
        outcome="PASS",  # a field only nested carries
        claim_ids_tested=["MECH-001"],
    )
    merged, _ = gcr.load_manifest_corpus(evidence_dir)
    rec = merged["run_a"]
    assert rec["enabled_default_off_flags"] == {"use_thing": True}, (
        "field-level merge must preserve flat-only fields when nested omits them"
    )
    assert rec["outcome"] == "PASS", "nested-only fields must still come through"
    assert rec["claim_ids"] == ["MECH-001"], "nested must win per-key when both have the key... "


def test_load_nested_wins_per_key_when_both_present(evidence_dir):
    _write_flat(evidence_dir, "run_b", outcome="FAIL")
    _write_nested(evidence_dir, "run_b", outcome="PASS")
    merged, _ = gcr.load_manifest_corpus(evidence_dir)
    assert merged["run_b"]["outcome"] == "PASS"


def test_load_dedupes_by_run_id_across_shapes(evidence_dir):
    _write_flat(evidence_dir, "solo_flat")
    _write_nested(evidence_dir, "solo_nested")
    _write_flat(evidence_dir, "both")
    _write_nested(evidence_dir, "both")
    merged, counts = gcr.load_manifest_corpus(evidence_dir)
    assert set(merged.keys()) == {"solo_flat", "solo_nested", "both"}
    assert counts["merged_total"] == 3


# --------------------------------------------------------------------------
# filter_scorable
# --------------------------------------------------------------------------


def test_filter_scorable_excludes_superseded_and_scoring_excluded():
    manifests = {
        "a": {"run_id": "a"},
        "b": {"run_id": "b", "evidence_direction": "superseded"},
        "c": {"run_id": "c", "scoring_excluded": "degenerate"},
        "d": {"run_id": "d", "scoring_excluded": False},  # falsy -> kept
    }
    kept, diag = gcr.filter_scorable(manifests)
    assert set(kept.keys()) == {"a", "d"}
    assert diag["excluded_superseded"] == 1
    assert diag["excluded_scoring_excluded"] == 1
    assert diag["kept_total"] == 2


# --------------------------------------------------------------------------
# Gate A
# --------------------------------------------------------------------------


def _manifest(run_id, experiment_type=None, commit=None, flags=None, sub_hash=None):
    rec = {"run_id": run_id, "experiment_type": experiment_type or run_id}
    if commit is not None:
        rec["substrate_commit"] = {"commit": commit, "dirty": False}
    if flags is not None:
        rec["enabled_default_off_flags"] = flags
    if sub_hash is not None:
        rec["substrate_hash"] = sub_hash
    return rec


def test_gate_a_no_warrant_on_empty_corpus():
    ga = gcr.compute_gate_a({})
    assert ga["satisfied"] is False
    assert "NO_IDENTIFIABLE_ORGANISM" in ga["reason_codes"]
    assert ga["diagnostics"]["total_scorable_manifests"] == 0


def test_gate_a_no_warrant_when_no_manifest_has_substrate_commit():
    manifests = {f"r{i}": _manifest(f"r{i}") for i in range(5)}
    ga = gcr.compute_gate_a(manifests)
    assert ga["satisfied"] is False
    assert ga["diagnostics"]["manifests_with_substrate_commit"] == 0


def test_gate_a_same_experiment_seeds_do_not_count_as_recurrence():
    """Mechanism A succeeded in one animal is fine as long as it's re-run --
    but N seeds of the SAME experiment_type must not satisfy the gate; the
    thought document's example is DIFFERENT experiments/mechanisms recurring
    against the same identifiable configuration, not one experiment's own
    internal seed replication."""
    manifests = {
        f"seed{i}": _manifest(
            f"seed{i}", experiment_type="v3_exq_100_same_thing", commit="deadbeef", flags={"use_x": True}
        )
        for i in range(5)
    }
    ga = gcr.compute_gate_a(manifests)
    assert ga["satisfied"] is False, "single experiment_type recurrence must not satisfy Gate A"


def test_gate_a_satisfied_when_distinct_experiments_share_exact_configuration():
    manifests = {}
    for i, etype in enumerate(["v3_exq_1_a", "v3_exq_2_b", "v3_exq_3_c"]):
        manifests[f"r{i}"] = _manifest(f"r{i}", experiment_type=etype, commit="c0ffee", flags={"use_x": True})
    ga = gcr.compute_gate_a(manifests)
    assert ga["satisfied"] is True
    assert ga["tier"] == "exact_recurring_configuration"
    g = ga["diagnostics"]["exact_recurring_best_group"]
    assert g["group_size"] == 3
    assert len(g["distinct_experiment_types"]) == 3


def test_gate_a_below_threshold_group_does_not_satisfy():
    # Only 2 distinct experiments -- below EXACT_RECURRENCE_MIN group size of 3
    manifests = {}
    for i, etype in enumerate(["v3_exq_1_a", "v3_exq_2_b"]):
        manifests[f"r{i}"] = _manifest(f"r{i}", experiment_type=etype, commit="c0ffee", flags={"use_x": True})
    ga = gcr.compute_gate_a(manifests)
    assert ga["satisfied"] is False


def test_gate_a_hash_recurrence_alone_is_informational_not_sufficient():
    manifests = {}
    for i, etype in enumerate(["v3_exq_1_a", "v3_exq_2_b", "v3_exq_3_c"]):
        # same substrate_hash, but NO substrate_commit/flags recorded at all
        manifests[f"r{i}"] = _manifest(f"r{i}", experiment_type=etype, sub_hash="hash123")
    ga = gcr.compute_gate_a(manifests)
    assert ga["satisfied"] is False
    assert ga["diagnostics"]["fingerprint_recurring_best_group"] is not None
    assert ga["diagnostics"]["fingerprint_recurring_best_group"]["group_size"] == 3
    assert any("informational" in r for r in ga["reason_codes"])


def test_gate_a_different_flag_values_do_not_falsely_merge():
    manifests = {
        "a": _manifest("a", experiment_type="e1", commit="c1", flags={"use_x": True}),
        "b": _manifest("b", experiment_type="e2", commit="c1", flags={"use_x": False}),
        "c": _manifest("c", experiment_type="e3", commit="c1", flags={"use_x": True}),
    }
    ga = gcr.compute_gate_a(manifests)
    # only 2 manifests share the exact (commit, flags) signature -- below min group size 3
    assert ga["satisfied"] is False


# --------------------------------------------------------------------------
# Gate C
# --------------------------------------------------------------------------


def test_gate_c_empty_corpus():
    gc = gcr.compute_gate_c({})
    d = gc["diagnostics"]
    assert d["manifests_with_any_flag"] == 0
    assert d["distinct_flags_observed"] == 0
    assert d["pairs_observed_at_least_once"] == 0


def test_gate_c_single_flag_manifests_contribute_no_pairs():
    manifests = {
        "a": _manifest("a", flags={"use_x": True}),
        "b": _manifest("b", flags={"use_y": True}),
    }
    gc = gcr.compute_gate_c(manifests)
    d = gc["diagnostics"]
    assert d["distinct_flags_observed"] == 2
    assert d["pairs_observed_at_least_once"] == 0
    assert set(d["flags_observed_only_alone_never_paired"]) == {"use_x", "use_y"}


def test_gate_c_counts_coexisting_pairs_correctly():
    manifests = {
        "a": _manifest("a", flags={"use_x": True, "use_y": True}),
        "b": _manifest("b", flags={"use_x": True, "use_y": True, "use_z": False}),
        "c": _manifest("c", flags={"use_x": True}),
    }
    gc = gcr.compute_gate_c(manifests)
    d = gc["diagnostics"]
    assert d["manifests_with_any_flag"] == 3
    assert d["manifests_with_multi_flag_combination"] == 2
    assert d["distinct_flags_observed"] == 3
    pairs = {(p["a"], p["b"]): p["count"] for p in d["top_coexisting_pairs"]}
    assert pairs[("use_x", "use_y")] == 2
    assert pairs[("use_y", "use_z")] == 1
    assert pairs[("use_x", "use_z")] == 1
    assert d["pairs_observed_at_least_once"] == 3
    assert d["total_possible_pairs_among_observed_flags"] == 3  # C(3,2)
    assert d["pairs_never_combined_among_observed"] == 0
    assert d["flags_observed_only_alone_never_paired"] == []


def test_gate_c_ignores_manifests_with_non_dict_or_empty_flags():
    manifests = {
        "a": _manifest("a", flags=None),
        "b": {"run_id": "b", "enabled_default_off_flags": {}},
        "c": {"run_id": "c", "enabled_default_off_flags": "not_a_dict"},
    }
    gc = gcr.compute_gate_c(manifests)
    assert gc["diagnostics"]["manifests_with_any_flag"] == 0


# --------------------------------------------------------------------------
# Gates B/D/E/F -- unmeasured stubs
# --------------------------------------------------------------------------


@pytest.mark.parametrize("fn", [gcr.compute_gate_b, gcr.compute_gate_d, gcr.compute_gate_e, gcr.compute_gate_f])
def test_stub_gates_are_unmeasured_never_satisfied(fn):
    g = fn()
    assert g["status"] == "unmeasured"
    assert g["satisfied"] is False
    assert "reason" in g and g["reason"]


def test_stub_gates_distinct_reasons():
    reasons = {fn()["reason"] for fn in (gcr.compute_gate_b, gcr.compute_gate_d, gcr.compute_gate_e, gcr.compute_gate_f)}
    assert len(reasons) == 4, "each stub gate must carry its own distinct reason, not a shared placeholder"


# --------------------------------------------------------------------------
# State machine
# --------------------------------------------------------------------------


def test_resolve_state_no_warrant_when_gate_a_fails():
    ga = {"satisfied": False, "reason_codes": ["NO_IDENTIFIABLE_ORGANISM"]}
    resolved = gcr.resolve_state(ga, gcr.compute_gate_b(), gcr.compute_gate_d(), gcr.compute_gate_e(), gcr.compute_gate_f())
    assert resolved["state"] == "NO_WARRANT"
    assert any("Gate A" in r for r in resolved["reasons"])
    # every unmeasured gate must ALSO be named, since it too fails the conjunction
    assert any("Gate B" in r for r in resolved["reasons"])
    assert any("Gate D" in r for r in resolved["reasons"])
    assert any("Gate E" in r for r in resolved["reasons"])
    assert any("Gate F" in r for r in resolved["reasons"])


def test_resolve_state_admission_pass_when_all_gates_satisfied():
    ga = {"satisfied": True, "tier": "exact_recurring_configuration", "reason_codes": []}
    all_satisfied = {"satisfied": True, "status": "satisfied"}
    resolved = gcr.resolve_state(ga, all_satisfied, all_satisfied, all_satisfied, all_satisfied)
    assert resolved["state"] == "ADMISSION_PASS_WARRANTED"
    assert resolved["reasons"] == []


def test_resolve_state_never_produces_a_state_outside_the_five():
    ga = {"satisfied": False, "reason_codes": []}
    resolved = gcr.resolve_state(ga, gcr.compute_gate_b(), gcr.compute_gate_d(), gcr.compute_gate_e(), gcr.compute_gate_f())
    assert resolved["state"] in gcr.STATES


# --------------------------------------------------------------------------
# Transition detection
# --------------------------------------------------------------------------


def _fake_result(state, gate_a_satisfied=False, b="unmeasured", d="unmeasured", e="unmeasured", f="unmeasured"):
    return {
        "state": state,
        "gates": {
            "A": {"satisfied": gate_a_satisfied},
            "B": {"status": b},
            "D": {"status": d},
            "E": {"status": e},
            "F": {"status": f},
        },
    }


def test_transition_initial_when_no_prior():
    current = _fake_result("NO_WARRANT")
    t = gcr.diff_against_prior(current, None)
    assert t["has_prior"] is False
    assert t["state_transition"] == "initial"
    assert t["escalate"] is True
    assert all(v == "initial" for v in t["predicate_transitions"].values())


def test_transition_unchanged_when_identical():
    current = _fake_result("NO_WARRANT")
    prior = _fake_result("NO_WARRANT")
    t = gcr.diff_against_prior(current, prior)
    assert t["state_transition"] == "unchanged"
    assert t["escalate"] is False
    assert all(v == "unchanged" for v in t["predicate_transitions"].values())


def test_transition_newly_satisfied_and_newly_blocked():
    prior = _fake_result("NO_WARRANT", gate_a_satisfied=False)
    current = _fake_result("NO_WARRANT", gate_a_satisfied=True)
    t = gcr.diff_against_prior(current, prior)
    assert t["predicate_transitions"]["gate_a_satisfied"] == "newly_satisfied"
    assert t["escalate"] is True

    prior2 = _fake_result("ADMISSION_PASS_WARRANTED", gate_a_satisfied=True)
    current2 = _fake_result("NO_WARRANT", gate_a_satisfied=False)
    t2 = gcr.diff_against_prior(current2, prior2)
    assert t2["predicate_transitions"]["gate_a_satisfied"] == "newly_blocked"
    assert t2["state_transition"] == "ADMISSION_PASS_WARRANTED -> NO_WARRANT"
    assert t2["escalate"] is True


def test_transition_gate_status_string_change_reports_from_to():
    prior = _fake_result("NO_WARRANT", b="unmeasured")
    current = _fake_result("NO_WARRANT", b="satisfied")
    t = gcr.diff_against_prior(current, prior)
    assert "unmeasured" in t["predicate_transitions"]["gate_b_status"]
    assert "satisfied" in t["predicate_transitions"]["gate_b_status"]
    assert t["escalate"] is True


def test_transition_persistent_no_warrant_across_multiple_reasons_stays_non_escalating():
    """The Steward principle this detector borrows: fifty cycles of the same
    NO_WARRANT state, for the same reasons, should not re-escalate."""
    prior = _fake_result("NO_WARRANT")
    current = _fake_result("NO_WARRANT")
    t = gcr.diff_against_prior(current, prior)
    assert t["escalate"] is False


# --------------------------------------------------------------------------
# Full assembly: build_readiness_report against a synthetic corpus
# --------------------------------------------------------------------------


def test_build_readiness_report_expected_first_verdict_is_no_warrant(evidence_dir):
    """Per the source thought and the governing claim's own notes, the
    expected v1 verdict on a realistic corpus (thin substrate_commit
    coverage, no dominant recurring configuration) is NO_WARRANT. This test
    pins that on a small synthetic corpus shaped like the real one:
    experiment-specific configs, no true recurrence."""
    for i in range(10):
        _write_flat(
            evidence_dir,
            f"v3_exq_{i}_unique_experiment",
            experiment_type=f"v3_exq_{i}_unique_experiment",
        )
    report = gcr.build_readiness_report(evidence_dir, "2026-09-01T00:00:00Z")
    assert report["state"] == "NO_WARRANT"
    assert any("NO_IDENTIFIABLE_ORGANISM" in r for r in report["reasons"])


def test_build_readiness_report_excludes_superseded_from_gate_a(evidence_dir):
    # Three superseded manifests share an exact configuration; they must not
    # count toward Gate A recurrence.
    for i, etype in enumerate(["a", "b", "c"]):
        _write_flat(
            evidence_dir,
            f"sup{i}",
            experiment_type=etype,
            substrate_commit={"commit": "dead", "dirty": False},
            enabled_default_off_flags={"use_x": True},
            evidence_direction="superseded",
        )
    report = gcr.build_readiness_report(evidence_dir, "2026-09-01T00:00:00Z")
    assert report["state"] == "NO_WARRANT"
    assert report["corpus"]["filter"]["excluded_superseded"] == 3
    assert report["gates"]["A"]["satisfied"] is False


def test_build_readiness_report_is_deterministic(evidence_dir):
    _write_flat(evidence_dir, "r1", experiment_type="e1")
    _write_nested(evidence_dir, "r2", experiment_type="e2")
    r1 = gcr.build_readiness_report(evidence_dir, "2026-09-01T00:00:00Z")
    r2 = gcr.build_readiness_report(evidence_dir, "2026-09-01T00:00:00Z")
    assert r1 == r2


# --------------------------------------------------------------------------
# CLI / main() -- structural prohibition + write-scope tests
# --------------------------------------------------------------------------


def test_main_writes_only_its_two_declared_artifacts(tmp_path):
    evidence_dir = tmp_path / "evidence" / "experiments"
    evidence_dir.mkdir(parents=True)
    _write_flat(evidence_dir, "r1", experiment_type="e1")

    planning_dir = tmp_path / "evidence" / "planning"
    out_json = planning_dir / "canonical_readiness.v1.json"
    out_md = planning_dir / "canonical_readiness.md"

    # Snapshot every file under tmp_path before running.
    before = set(tmp_path.rglob("*"))

    rc = gcr.main(
        [
            "--evidence-dir",
            str(evidence_dir),
            "--out-json",
            str(out_json),
            "--out-md",
            str(out_md),
        ]
    )
    assert rc == 0
    after = set(tmp_path.rglob("*"))
    new_paths = after - before
    # Only the json/md files (and their newly-created parent dir) may appear.
    allowed = {out_json, out_md, planning_dir}
    unexpected = {p for p in new_paths if p not in allowed}
    assert unexpected == set(), f"main() wrote unexpected paths: {unexpected}"
    assert out_json.exists()
    assert out_md.exists()


def test_main_check_flag_exit_code_reflects_escalation(tmp_path):
    evidence_dir = tmp_path / "evidence" / "experiments"
    evidence_dir.mkdir(parents=True)
    _write_flat(evidence_dir, "r1", experiment_type="e1")
    out_json = tmp_path / "canonical_readiness.v1.json"
    out_md = tmp_path / "canonical_readiness.md"

    # First run: no prior artifact -> initial -> escalates -> exit 1 under --check.
    rc1 = gcr.main(
        ["--check", "--evidence-dir", str(evidence_dir), "--out-json", str(out_json), "--out-md", str(out_md)]
    )
    assert rc1 == 1

    # Second run against the now-written prior: unchanged -> exit 0 under --check.
    rc2 = gcr.main(
        ["--check", "--evidence-dir", str(evidence_dir), "--out-json", str(out_json), "--out-md", str(out_md)]
    )
    assert rc2 == 0


def test_main_missing_evidence_dir_errors_cleanly(tmp_path):
    rc = gcr.main(
        [
            "--evidence-dir",
            str(tmp_path / "does_not_exist"),
            "--out-json",
            str(tmp_path / "out.json"),
            "--out-md",
            str(tmp_path / "out.md"),
        ]
    )
    assert rc == 2


def test_render_markdown_is_ascii_only():
    result = {
        "schema": gcr.SCHEMA,
        "generated_at_utc": "2026-09-01T00:00:00Z",
        "state": "NO_WARRANT",
        "reasons": ["Gate A: NO_IDENTIFIABLE_ORGANISM"],
        "gates": {
            "A": gcr.compute_gate_a({}),
            "B": gcr.compute_gate_b(),
            "C": gcr.compute_gate_c({}),
            "D": gcr.compute_gate_d(),
            "E": gcr.compute_gate_e(),
            "F": gcr.compute_gate_f(),
        },
    }
    transition = {"has_prior": False, "predicate_transitions": {"x": "initial"}, "escalate": True}
    md = gcr.render_markdown(result, transition)
    md.encode("ascii")  # raises UnicodeEncodeError if any non-ASCII character present
