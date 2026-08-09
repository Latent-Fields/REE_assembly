"""Contract tests for build_experiment_indexes.py adjudication logic.

Focus: the (3a) diagnostic-adjudication readiness recompute in
`_compute_adjudication` must respect each precondition's bound DIRECTION.

A FLOOR precondition (the default) is unmet when measured < threshold.
An UPPER-bound / CEILING precondition (e.g. rolled_out_zworld_*_bounded,
"stayed below the 643a explosion ceiling", threshold 1e6) is unmet only when
measured > threshold -- measured << threshold means the ceiling check PASSED.

Regression target: 2026-06-07 directionality bug where the recompute treated
EVERY numeric measured/threshold precondition as a floor (`m < t`), false-flagging
V3-EXQ-648a and V3-EXQ-649 `precondition_unmet`.

Run directly:  python test_build_experiment_indexes.py
Or via pytest:  pytest test_build_experiment_indexes.py
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


def _floor(measured, threshold, met=True):
    return {"name": "spread_supra_floor", "kind": "readiness",
            "measured": measured, "threshold": threshold, "met": met}


def _ceiling(measured, threshold, met=True, tag="direction"):
    p = {"name": "magnitude_bounded", "kind": "readiness",
         "measured": measured, "threshold": threshold, "met": met}
    if tag == "direction":
        p["direction"] = "upper"
    elif tag == "comparator":
        p["comparator"] = "<="
    return p


def _interp(preconditions, label="x", criteria=None):
    d = {"label": label, "preconditions": preconditions}
    if criteria is not None:
        d["criteria"] = criteria
    return d


# --- _precondition_direction ----------------------------------------------

def test_direction_defaults_to_lower():
    assert b._precondition_direction({"measured": 1, "threshold": 2}) == "lower"


def test_direction_explicit_upper():
    assert b._precondition_direction({"direction": "upper"}) == "upper"
    assert b._precondition_direction({"direction": "ceiling"}) == "upper"
    assert b._precondition_direction({"direction": "max"}) == "upper"


def test_direction_explicit_lower():
    assert b._precondition_direction({"direction": "lower"}) == "lower"
    assert b._precondition_direction({"direction": "floor"}) == "lower"


def test_comparator_resolves_direction():
    assert b._precondition_direction({"comparator": "<="}) == "upper"
    assert b._precondition_direction({"comparator": "<"}) == "upper"
    assert b._precondition_direction({"comparator": ">="}) == "lower"
    assert b._precondition_direction({"comparator": ">"}) == "lower"


def test_comparator_wins_over_unknown_direction():
    assert b._precondition_direction({"comparator": "<=", "direction": "??"}) == "upper"


# --- (3a) recompute: the load-bearing regression ---------------------------

def test_upper_bound_precondition_that_passes_is_not_flagged():
    """The core regression: a ceiling far below its threshold is VERIFIED, not
    precondition_unmet (V3-EXQ-648a / V3-EXQ-649 signature)."""
    interp = _interp([_ceiling(0.190288, 1_000_000.0)])
    label, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_upper_bound_via_comparator_tag_also_passes():
    interp = _interp([_ceiling(0.19, 1_000_000.0, tag="comparator")])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_upper_bound_genuinely_violated_is_flagged():
    """A ceiling ABOVE its threshold must still flag precondition_unmet."""
    interp = _interp([_ceiling(2_000_000.0, 1_000_000.0, met=True)])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_floor_below_threshold_still_flagged():
    """Default floor semantics preserved: measured < threshold -> unmet."""
    interp = _interp([_floor(0.02, 0.05, met=True)])
    _, flag = b._compute_adjudication(interp, "FAIL", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_floor_above_threshold_passes():
    interp = _interp([_floor(0.149, 0.05)])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_mixed_floors_and_ceiling_all_clear():
    """V3-EXQ-648a shape: two floors cleared + one upper-bound ceiling cleared."""
    interp = _interp([
        _floor(0.149011, 0.05),
        _floor(0.02061524, 0.0001),
        _ceiling(0.315368, 1_000_000.0),
    ], criteria=[{"name": "C2", "load_bearing": True, "passed": True}])
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_ceiling_clears_but_floor_fails_is_flagged():
    """Direction is per-entry: one floor failing still flags even if the
    ceiling is fine."""
    interp = _interp([
        _floor(0.01, 0.05, met=True),       # below floor -> unmet
        _ceiling(0.3, 1_000_000.0),         # fine
    ])
    _, flag = b._compute_adjudication(interp, "FAIL", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_non_diagnostic_is_na():
    interp = _interp([_floor(0.01, 0.05)])
    _, flag = b._compute_adjudication(interp, "FAIL", "evidence")
    assert flag == "n/a", flag


# --- two-sided INTERVAL preconditions (2026-07-19) -------------------------
# Motivating shape: V3-EXQ-779b `baseline_entropy_headroom`, whose backing check
# is `E_SAT_LOW < S < E_SAT_HIGH` (0.02 < S < 0.98). The single-bound
# direction/comparator vocabulary could declare only ONE leg, so the 0.02 floor
# was absent from the manifest entirely and the recompute adjudicated on the
# ceiling alone -- a saturated-to-zero baseline (S = 0.001, the exact condition
# the check exists to catch) recomputed as MET.

def _band(measured, lo=0.02, hi=0.98, strict=True, met=True):
    p = {"name": "baseline_entropy_headroom", "kind": "capability",
         "measured": measured, "threshold_low": lo, "threshold_high": hi,
         "direction": "interval", "met": met}
    if strict:
        p["comparator_low"] = ">"
        p["comparator_high"] = "<"
    return p


def test_interval_inside_band_is_met():
    assert b._precondition_unmet(_band(0.53)) is False


def test_interval_below_low_leg_is_unmet():
    """The leg the old vocabulary could not express: a floor violation."""
    assert b._precondition_unmet(_band(0.001)) is True


def test_interval_above_high_leg_is_unmet():
    assert b._precondition_unmet(_band(0.995)) is True


def test_interval_strict_legs_exclude_the_endpoints():
    """779b's check is STRICT on both legs, so measured == a bound is UNMET."""
    assert b._precondition_unmet(_band(0.02)) is True
    assert b._precondition_unmet(_band(0.98)) is True


def test_interval_non_strict_legs_include_the_endpoints():
    """Default (comparators absent) is inclusive on both legs."""
    assert b._precondition_unmet(_band(0.02, strict=False)) is False
    assert b._precondition_unmet(_band(0.98, strict=False)) is False


def test_interval_drives_adjudication_end_to_end():
    """A saturated baseline inside a PASS run is caught, not waved through."""
    _, flag = b._compute_adjudication(_interp([_band(0.001)]), "PASS", "diagnostic")
    assert flag == "precondition_unmet", flag
    _, flag = b._compute_adjudication(_interp([_band(0.53)]), "PASS", "diagnostic")
    assert flag == "verified", flag


def test_interval_needs_no_threshold_key():
    """An interval entry carries no single `threshold`, and must NOT therefore
    fall through to the legacy author-trusted `met is False` path."""
    p = _band(0.001, met=True)
    assert "threshold" not in p
    _, flag = b._compute_adjudication(_interp([p]), "PASS", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_inverted_interval_is_not_recomputable():
    """low > high is an authoring error; refuse to adjudicate rather than flag
    every such run unmet (the 2026-06-07 directionality bug's failure mode)."""
    assert b._precondition_unmet(_band(0.5, lo=0.98, hi=0.02)) is None


def test_declared_interval_missing_a_bound_is_not_recomputable():
    """A half-declared band must NOT silently degrade to a FLOOR read --
    _precondition_direction does not know "interval" and would default to
    "lower", adjudicating the band on one leg."""
    p = {"name": "n", "measured": 0.001, "threshold": 0.98, "direction": "interval"}
    assert b._precondition_unmet(p) is None
    p2 = {"name": "n", "measured": 0.001, "threshold_high": 0.98, "direction": "band"}
    assert b._precondition_unmet(p2) is None


def test_interval_ignores_a_stray_threshold_key():
    """Both bounds present wins over a legacy single `threshold`."""
    p = _band(0.001)
    p["threshold"] = 0.98  # legacy ceiling-only view
    assert b._precondition_unmet(p) is True


# --- single-bound comparator STRICTNESS (2026-07-19) ------------------------
# Previously ">" and ">=" were byte-identical in effect: _precondition_direction
# collapsed both to "lower" and the recompute hardcoded `m < t`. No manifest in
# the corpus declared a strict comparator when this landed (survey 2026-07-19:
# 1553 entries, comparator values {"<=": 4}), so this is a pure extension.

def test_strict_floor_excludes_the_endpoint():
    p = {"name": "n", "measured": 10, "threshold": 10, "comparator": ">"}
    assert b._precondition_unmet(p) is True


def test_non_strict_floor_includes_the_endpoint():
    p = {"name": "n", "measured": 10, "threshold": 10, "comparator": ">="}
    assert b._precondition_unmet(p) is False
    assert b._precondition_unmet({"name": "n", "measured": 10, "threshold": 10}) is False


def test_strict_ceiling_excludes_the_endpoint():
    p = {"name": "n", "measured": 10, "threshold": 10, "comparator": "<"}
    assert b._precondition_unmet(p) is True


def test_non_strict_ceiling_includes_the_endpoint():
    p = {"name": "n", "measured": 10, "threshold": 10, "comparator": "<="}
    assert b._precondition_unmet(p) is False


def test_non_numeric_entry_is_not_recomputable():
    assert b._precondition_unmet({"name": "n", "met": False}) is None
    assert b._precondition_unmet({"name": "n", "measured": "x", "threshold": 1}) is None
    assert b._precondition_unmet("not a dict") is None


# --- flat-manifest authoritative override (2026-06-14 regression) ----------
# Root cause: _scan_runs scores runs/<run_id>/manifest.json (the "pack" copy),
# but /failure-autopsy + governance corrections are written to the flat
# evidence/experiments/<run_id>.json. A flat-only correction was silently
# ignored, so a stale pack `does_not_support` (-> weakens) kept scoring against
# MECH-171 x3 / MECH-057b. _merge_flat_manifest_overrides makes the flat copy
# authoritative for governance/adjudication fields.

def test_annotated_flat_overrides_unannotated_pack():
    """The 2026-06-14 incident shape: flat carries the autopsy correction +
    note, pack is the stale auto-emit -> flat wins, applied=True."""
    pack = {"evidence_direction": "does_not_support",
            "evidence_direction_per_claim": {"MECH-171": "does_not_support"}}
    flat = {"evidence_direction": "non_contributory",
            "evidence_direction_per_claim": {"MECH-171": "non_contributory"},
            "evidence_direction_note": "autopsy: monomodal policy, untestable"}
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["evidence_direction"] == "non_contributory", merged
    assert merged["evidence_direction_per_claim"]["MECH-171"] == "non_contributory"
    fields = {d[0] for d in disagree}
    assert "evidence_direction" in fields
    assert "evidence_direction_per_claim" in fields


def test_unannotated_flat_does_not_override_annotated_pack():
    """The legacy v3_exq_150-series inverse: pack carries the supersession note,
    flat is a stale earlier emission -> pack MUST stay authoritative. This is
    the regression guard for the dozens of legacy runs the naive rule broke."""
    pack = {"evidence_direction": "superseded",
            "evidence_direction_note": "Implementation gap: policy entropy walk"}
    flat = {"evidence_direction": "weakens"}  # stale, no note
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is False
    assert merged["evidence_direction"] == "superseded"  # pack retained
    # disagreement is still reported (for diagnostics), but overlay suppressed
    assert ("evidence_direction", "superseded", "weakens") in disagree


def test_both_annotated_disagree_retains_pack():
    """When both copies are annotated but disagree, retain the pack (status quo
    scoring source) and surface the conflict via disagreements."""
    pack = {"evidence_direction": "weakens",
            "evidence_direction_note": "pack decision"}
    flat = {"evidence_direction": "supports",
            "evidence_direction_note": "flat decision"}
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is False
    assert merged["evidence_direction"] == "weakens"
    assert ("evidence_direction", "weakens", "supports") in disagree


def test_neither_annotated_retains_pack():
    """Two unannotated copies that differ (emission artifact): pack retained,
    no scoring change vs the historical pack-only behaviour."""
    pack = {"evidence_direction": "mixed"}
    flat = {"evidence_direction": "supports"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is False
    assert merged["evidence_direction"] == "mixed"


def test_flat_missing_sibling_is_noop():
    """No flat sibling (=> {}) must leave the pack manifest byte-identical --
    this is what preserves legacy/synthetic-run handling."""
    pack = {"evidence_direction": "supports", "run_id": "legacy_run"}
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, {})
    assert merged == pack
    assert disagree == []
    assert applied is False


def test_annotated_flat_absent_field_does_not_clobber_pack():
    """A field present on the pack but ABSENT from the annotated flat copy is
    left untouched (key presence, not truthiness, gates the overlay)."""
    pack = {"evidence_direction": "supports", "non_degenerate": True}
    flat = {"evidence_direction": "non_contributory",
            "evidence_direction_note": "x"}  # annotated; no non_degenerate key
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["non_degenerate"] is True
    assert merged["evidence_direction"] == "non_contributory"


def test_flat_explicit_false_non_degenerate_overrides():
    """An explicit non_degenerate: false on an ANNOTATED flat copy must override
    even though it is falsy (the key-presence rule, not truthiness). The
    degeneracy_reason both annotates the flat and propagates."""
    pack = {"non_degenerate": True}
    flat = {"non_degenerate": False, "degeneracy_reason": "constant metric"}
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["non_degenerate"] is False
    assert merged["degeneracy_reason"] == "constant metric"
    assert ("non_degenerate", True, False) in disagree


def test_flat_agreement_yields_no_disagreement():
    """Idempotent case: flat == pack (post manual 2026-06-14 fix). Both
    annotated and identical -> no disagreement, applied=False (nothing to do)."""
    shared = {"evidence_direction": "superseded",
              "evidence_direction_per_claim": {"MECH-057b": "superseded"},
              "non_degenerate": False,
              "evidence_direction_note": "superseded by 672a"}
    merged, disagree, applied = b._merge_flat_manifest_overrides(
        dict(shared), dict(shared))
    assert disagree == []
    assert applied is False
    assert merged["evidence_direction"] == "superseded"


def test_flat_superseded_by_substrate_propagates():
    pack = {}
    flat = {"superseded_by_substrate": "SD-046@2026-06-10"}  # self-annotating
    merged, disagree, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["superseded_by_substrate"] == "SD-046@2026-06-10"
    assert ("superseded_by_substrate", None, "SD-046@2026-06-10") in disagree


def test_metrics_and_status_not_overridden():
    """Only governance fields are overlaid; metrics/status/claim_ids come from
    the pack and must survive the merge untouched (annotated-flat path)."""
    pack = {"status": "PASS", "claim_ids_tested": ["MECH-171"],
            "evidence_direction": "does_not_support"}
    flat = {"status": "FAIL", "claim_ids_tested": ["WRONG"],
            "evidence_direction": "non_contributory",
            "evidence_direction_note": "autopsy"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["status"] == "PASS"           # pack wins (not authoritative)
    assert merged["claim_ids_tested"] == ["MECH-171"]
    assert merged["evidence_direction"] == "non_contributory"  # flat wins


# --- Unconditional provenance backfill (2026-07-16 thin-pack fix) -------------
# machine/machine_class/substrate_hash are pure provenance; a pre-2026-07-16 pack
# dropped them (build_runpack_docs did not map them) even when the flat sibling
# carried the always-core, so the index scored machine_class=null. The backfill
# fills them from the flat copy WITHOUT the annotation gate (they never change
# scoring direction), while never overwriting a non-empty pack value.

def test_provenance_backfill_unannotated_thin_pack():
    """The exact 2026-07-16 case: an unannotated thin pack whose flat sibling
    carries provenance is backfilled -- even though the direction-overlay gate
    does NOT fire (applied stays False)."""
    pack = {"run_id": "r1", "status": "PASS"}
    flat = {"machine": "ree-cloud-2",
            "machine_class": "linux-x86_64-py3.10",
            "substrate_hash": "f92a600cf17a"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is False  # provenance backfill must not set the overlay flag
    assert merged["machine"] == "ree-cloud-2"
    assert merged["machine_class"] == "linux-x86_64-py3.10"
    assert merged["substrate_hash"] == "f92a600cf17a"


def test_provenance_backfill_never_overwrites_nonempty_pack():
    """A pack that already carries provenance keeps ITS values (the pack ran on
    that class); the flat copy does not clobber a non-empty pack value."""
    pack = {"machine_class": "darwin-arm64-py3.13", "substrate_hash": "PACKHASH"}
    flat = {"machine_class": "linux-x86_64-py3.10", "substrate_hash": "FLATHASH"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert merged["machine_class"] == "darwin-arm64-py3.13"
    assert merged["substrate_hash"] == "PACKHASH"


def test_provenance_backfill_legacy_flat_without_provenance_is_noop():
    """A legacy flat that lacks provenance leaves a thin pack byte-identical."""
    pack = {"run_id": "legacy", "status": "PASS"}
    flat = {"evidence_direction": "supports"}  # no provenance keys
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert merged == pack
    assert applied is False


def test_provenance_backfill_composes_with_annotated_overlay():
    """Backfill and the annotated direction-overlay both apply: an annotated flat
    correction rides the overlay AND its provenance is backfilled onto the pack."""
    pack = {"evidence_direction": "supports"}
    flat = {"evidence_direction": "non_contributory",
            "evidence_direction_note": "autopsy: vacuous",
            "machine_class": "linux-x86_64-py3.10"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
    assert applied is True
    assert merged["evidence_direction"] == "non_contributory"
    assert merged["machine_class"] == "linux-x86_64-py3.10"


def test_is_annotated_signals():
    assert b._is_annotated({"evidence_direction_note": "x"}) is True
    assert b._is_annotated({"degeneracy_reason": "x"}) is True
    assert b._is_annotated({"superseded_by": "y"}) is True
    assert b._is_annotated({"superseded_by_substrate": "SD-1@d"}) is True
    assert b._is_annotated({"evidence_direction": "weakens"}) is False
    assert b._is_annotated({"evidence_direction_note": ""}) is False  # empty
    assert b._is_annotated({}) is False


# --- z_goal-stream liveness surfacing (2026-07-27) -------------------------
# The `z_goal_stream` block is carried through the indexer for QUERYABILITY
# ONLY. These pin the two ways the surface could be made worse than nothing:
# rendering an UNMEASURED run as a measured zero, and letting the block change
# how a run scores.

def test_prov_is_empty_is_type_aware():
    """The reason _prov_is_empty replaced `str(v).strip() == ""`: that test
    renders an empty dict as the non-empty literal "{}", which would backfill
    `z_goal_stream: {}` onto a pack and turn UNMEASURED into measured-zero."""
    assert b._prov_is_empty({}) is True
    assert b._prov_is_empty({"ticks_total": 0}) is False
    # String/None behaviour must be unchanged for machine / machine_class /
    # substrate_hash, which shared this loop before the dict field joined it.
    assert b._prov_is_empty(None) is True
    assert b._prov_is_empty("") is True
    assert b._prov_is_empty("   ") is True
    assert b._prov_is_empty("linux-x86_64-py3.10") is False


def test_z_goal_stream_backfilled_from_flat_onto_thin_pack():
    """A pack materialised by a sync_v3_results predating the run-pack mapping
    drops the block; the flat sibling still carries it, so backfill it. Same
    shape as the 2026-07-16 machine_class case, and NOT gated on annotation."""
    block = {"ticks_total": 12000, "ticks_active": 0, "writer_calls": 0,
             "active_frac": 0.0, "writer_defect": True,
             "goal_state_present": True, "n_agents": 6}
    pack = {"run_id": "r1", "status": "PASS"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, {"z_goal_stream": block})
    assert applied is False  # provenance backfill never sets the overlay flag
    assert merged["z_goal_stream"] == block


def test_empty_z_goal_stream_block_is_not_backfilled():
    """UNMEASURED must not be written into the shape of a measured run: an
    empty block on the flat copy leaves the pack byte-identical."""
    pack = {"run_id": "r1", "status": "PASS"}
    merged, _, applied = b._merge_flat_manifest_overrides(pack, {"z_goal_stream": {}})
    assert merged == pack
    assert applied is False


def test_z_goal_stream_never_overwrites_a_pack_block():
    """The pack is the scoring source; its own measurement wins."""
    pack_block = {"ticks_total": 10, "ticks_active": 4, "writer_calls": 10,
                  "active_frac": 0.4, "writer_defect": False}
    flat_block = {"ticks_total": 99, "ticks_active": 0, "writer_calls": 0,
                  "active_frac": 0.0, "writer_defect": True}
    merged, _, _ = b._merge_flat_manifest_overrides(
        {"z_goal_stream": pack_block}, {"z_goal_stream": flat_block})
    assert merged["z_goal_stream"] == pack_block


def test_z_goal_stream_is_not_a_direction_field():
    """Record-and-surface, never a gate. Membership in _FLAT_DIRECTION_FIELDS
    is what makes a flat/pack disagreement WARN as a governance conflict and is
    the marker of a scoring-relevant field -- z_goal_stream must stay out of it,
    and stay in the pure-provenance list that cannot change how a run scores."""
    assert "z_goal_stream" not in b._FLAT_DIRECTION_FIELDS
    assert "z_goal_stream" in b._FLAT_PROVENANCE_BACKFILL_FIELDS


# --- real-data smoke: the four incident run_ids ----------------------------

def _real_run_pairs():
    """Yield (run_id, flat_path, pack_path) for the 672/672a/673/677 cohort
    that exists in the repo. Skips any not present (keeps the test portable)."""
    import json
    from pathlib import Path
    base = Path(__file__).resolve().parents[1]  # evidence/experiments
    run_ids = [
        "v3_exq_672_mech057b_trajectory_promotion_gate_20260612T214458Z_v3",
        "v3_exq_672a_mech057b_trajectory_promotion_gate_20260613T180147Z_v3",
        "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260611T230231Z_v3",
        "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T032233Z_v3",
        "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T044809Z_v3",
        "v3_exq_677_mech180_novelty_sleep_upregulation_probe_20260613T161241Z_v3",
    ]
    for rid in run_ids:
        flat = base / f"{rid}.json"
        packs = list(base.glob(f"**/runs/{rid}/manifest.json"))
        if flat.exists() and packs:
            yield rid, flat, packs[0], json


def test_real_cohort_merge_makes_flat_authoritative():
    """For each incident run: the flat copy is annotated (autopsy note), so a
    STALE/UNANNOTATED pack (the pre-2026-06-14 state, reproduced by stripping
    the pack's annotation) is corrected back to the flat direction by the
    annotation-gated overlay."""
    seen = 0
    for rid, flat_path, pack_path, json in _real_run_pairs():
        seen += 1
        flat = json.loads(flat_path.read_text(encoding="utf-8"))
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        assert b._is_annotated(flat), f"{rid}: flat should carry autopsy note"
        # Reproduce the pre-fix incident: pack stale (does_not_support) AND
        # unannotated (no note/reason) -> flat overlay must fire and restore.
        corrupt = dict(pack)
        corrupt["evidence_direction"] = "does_not_support"
        corrupt["evidence_direction_per_claim"] = {
            k: "does_not_support" for k in (flat.get("evidence_direction_per_claim") or {})
        }
        for fld in b._ANNOTATION_MARKER_FIELDS:
            corrupt.pop(fld, None)
        m2, disagree, applied = b._merge_flat_manifest_overrides(corrupt, flat)
        assert applied is True, rid
        assert m2["evidence_direction"] == flat["evidence_direction"], rid
        if flat.get("evidence_direction") != "does_not_support":
            assert any(d[0] == "evidence_direction" for d in disagree), rid
    assert seen >= 4, f"expected >=4 incident runs present, found {seen}"


# --- legacy annotated-pack shape: SYNTHETIC contract + thin real-data smoke --
#
# 2026-08-09 BIT-ROT FIX. This contract used to be asserted directly against the
# live v3_exq_150/159 pairs, with `assert not b._is_annotated(flat)` as its data
# PREMISE. Governance has since annotated the 150-series flat (it now carries a
# `degeneracy_reason`), so that premise -- and only that premise -- went false and
# the test failed while the behaviour it guards was, and is, correct.
#
# The defect was the coupling, not the assertion: a contract test whose meaning
# silently changes when governance annotates a manifest cannot be trusted either
# way round. Had the flat instead been annotated to AGREE with the pack, the test
# would have kept PASSING while reaching `applied is False` through the
# both-annotated branch rather than the legacy branch it exists to pin -- a
# vacuous pass. So the contract is now built from synthetic fixtures in a tempdir
# and driven END-TO-END through `_scan_runs` (the real file-reading path), with a
# separate thin smoke over the real pairs asserting only what stays true as the
# live data evolves.


def _write_legacy_pair(base: Path, pack_extra: dict, flat_extra: dict) -> tuple[str, str]:
    """Materialise one `<experiment_type>/runs/<run_id>/manifest.json` pack plus
    its flat `<run_id>.json` sibling under `base`, in the on-disk shape
    `_scan_runs` globs for. Returns (experiment_type, run_id)."""
    run_id = "v3_exq_9150_legacy_annotated_pack_20260329T131504Z_v3"
    experiment_type = "v3_exq_9150_legacy_annotated_pack"
    run_dir = base / experiment_type / "runs" / run_id
    run_dir.mkdir(parents=True)
    pack = {"run_id": run_id, "timestamp_utc": "2026-03-29T13:15:04Z",
            "status": "PASS", "claim_ids_tested": ["MECH-9150"],
            "architecture_epoch": "ree_hybrid_guardrails_v1"}
    pack.update(pack_extra)
    (run_dir / "manifest.json").write_text(json.dumps(pack), encoding="utf-8")
    (run_dir / "metrics.json").write_text("{}", encoding="utf-8")
    (run_dir / "summary.md").write_text("synthetic\n", encoding="utf-8")
    flat = {"run_id": run_id, "timestamp_utc": "2026-03-29T13:15:04Z", "status": "PASS"}
    flat.update(flat_extra)
    (base / f"{run_id}.json").write_text(json.dumps(flat), encoding="utf-8")
    return experiment_type, run_id


def _scan_one_direction(pack_extra: dict, flat_extra: dict) -> str:
    """Run the real `_scan_runs` over a one-run synthetic tree and return the
    `evidence_direction` the indexer actually scored."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        experiment_type, run_id = _write_legacy_pair(base, pack_extra, flat_extra)
        by_experiment = b._scan_runs(base, {})
        records = by_experiment.get(experiment_type, [])
        assert len(records) == 1, f"expected 1 scanned run, got {len(records)}"
        assert records[0].run_id == run_id
        return records[0].evidence_direction


def test_legacy_annotated_pack_not_flipped_end_to_end():
    """The v3_exq_150-series SHAPE, synthetic: pack carries the supersession
    note, flat is a stale unannotated earlier emission. Driven through the real
    `_scan_runs` file-reading path, the scored direction must remain the pack's
    `superseded` -- the exclusion that keeps a superseded run out of scoring."""
    assert _scan_one_direction(
        {"evidence_direction": "superseded",
         "evidence_direction_note": "Sleep not implemented in V3. Superseded."},
        {"evidence_direction": "mixed"},
    ) == "superseded"


def test_legacy_annotated_pack_survives_a_later_flat_annotation():
    """The same pair AFTER governance annotates the flat copy too (the live
    2026-08-09 state of the 150-series). Both copies are now annotated and they
    disagree -> the pack is still retained. Pinned separately from the test above
    because these are DIFFERENT branches of the annotation gate that happen to
    share an outcome; conflating them is what made the old real-data test
    vacuous."""
    assert _scan_one_direction(
        {"evidence_direction": "superseded",
         "evidence_direction_note": "Sleep not implemented in V3. Superseded."},
        {"evidence_direction": "mixed",
         "degeneracy_reason": "All arms identical on the criterion-bearing metrics."},
    ) == "superseded"


def test_scan_does_read_the_flat_sibling():
    """Differential control for the two tests above: with the annotations the
    other way round (flat annotated, pack not) the scored direction DOES flip to
    the flat's. Without this, `superseded` above could be produced by a scan path
    that never opened the flat sibling at all, and both would pass vacuously."""
    assert _scan_one_direction(
        {"evidence_direction": "superseded"},
        {"evidence_direction": "mixed",
         "evidence_direction_note": "autopsy: correction lands on the flat copy"},
    ) == "mixed"


def test_real_legacy_150_series_pack_direction_survives_merge():
    """Thin real-data smoke over the actual 150/159 pairs. Asserts only the
    invariant that stays true as governance annotates these manifests: when the
    PACK is annotated, the merge never overwrites its `evidence_direction`,
    whatever the flat sibling's annotation state. Deliberately makes NO claim
    about whether the flat is annotated -- that premise is what rotted, and it is
    now pinned synthetically above instead."""
    import json
    from pathlib import Path
    base = Path(__file__).resolve().parents[1]
    checked = 0
    for rid in ("v3_exq_159_q020_arc007_valence_constraint_pair_20260329T193606Z_v3",
                "v3_exq_150_q005_sleep_anneal_20260329T131504Z_v3"):
        flat_p = base / f"{rid}.json"
        packs = list(base.glob(f"**/runs/{rid}/manifest.json"))
        if not (flat_p.exists() and packs):
            continue
        flat = json.loads(flat_p.read_text(encoding="utf-8"))
        pack = json.loads(packs[0].read_text(encoding="utf-8"))
        if not b._is_annotated(pack):
            continue  # no longer the annotated-pack shape; nothing to guard here
        checked += 1
        merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
        assert applied is False, rid
        assert merged.get("evidence_direction") == pack.get("evidence_direction"), rid
        assert merged.get("evidence_direction") == "superseded", rid
    assert checked >= 1, "expected at least one annotated-pack legacy pair present"


def test_does_not_support_still_maps_to_weakens():
    """Guardrail: the does_not_support -> weakens synonym is INTENTIONALLY
    preserved (171 manifests use it as a genuine 'evidence against' label).
    The 2026-06-14 fix is flat-authoritative merge, NOT re-mapping this token."""
    assert b._normalize_direction("does_not_support") == "weakens"


# ── inline-comment stripping on enum registry fields (2026-06-18) ────────────
# Regression target: _load_claim_registry captured a commented enum value
# (e.g. `epistemic_category: substrate_conditional  # note`) verbatim including
# the comment, so it fell out of the allowlist and mis-resolved to inference,
# silently un-suppressing promote/demote/narrow recommendations.

def test_strip_inline_comment_basic():
    assert b._strip_inline_yaml_comment(" substrate_conditional  # gov note") == "substrate_conditional"
    assert b._strip_inline_yaml_comment(" false  # cleared 2026-04-22: PASS") == "false"
    assert b._strip_inline_yaml_comment(" v3\t# tab-prefixed comment") == "v3"


def test_strip_inline_comment_no_comment_is_identity():
    assert b._strip_inline_yaml_comment(" substrate_ceiling") == "substrate_ceiling"
    assert b._strip_inline_yaml_comment("active") == "active"


def test_strip_inline_comment_hash_without_leading_space_kept():
    # A '#' not preceded by whitespace is not a YAML comment; leave it.
    assert b._strip_inline_yaml_comment("a#b") == "a#b"


def test_load_registry_strips_enum_field_comments():
    import tempfile
    import os
    yaml_text = (
        "- id: MECH-TEST-1\n"
        "  status: active\n"
        "  claim_type: mechanism_hypothesis\n"
        "  epistemic_category: substrate_conditional  # gov 2026-06-18: V5-bound owner MAE-4\n"
        "  v3_pending: true  # set by some session\n"
        "  implementation_phase: v3  # predicted\n"
        "- id: Q-TEST-2\n"
        "  status: open\n"
        "  claim_type: open_question\n"
        "  epistemic_category: derivational\n"  # no comment: must still work
    )
    fd, name = tempfile.mkstemp(suffix=".yaml")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(yaml_text)
        reg = b._load_claim_registry(b.Path(name))
    finally:
        os.unlink(name)
    assert reg["MECH-TEST-1"]["epistemic_category"] == "substrate_conditional", reg["MECH-TEST-1"]
    assert reg["MECH-TEST-1"]["v3_pending"] == "True", reg["MECH-TEST-1"]
    assert reg["MECH-TEST-1"]["implementation_phase"] == "v3", reg["MECH-TEST-1"]
    assert reg["Q-TEST-2"]["epistemic_category"] == "derivational", reg["Q-TEST-2"]
    # resolver honours the now-clean explicit value
    assert b._resolve_epistemic_category(
        "mechanism_hypothesis", "", reg["MECH-TEST-1"]["epistemic_category"]
    ) == "substrate_conditional"


# --- HEAD/worktree skew guard (2026-07-18 SD-068 incident) ------------------
# `git reset --mixed <remote-ref>` leaves files added by the adopted commits in
# HEAD and the index but NEVER writes them to disk. This script reads the
# working tree, so it would rebuild with those runs silently absent and drop
# real evidence from claim_evidence.v1.json / INDEX.md / pending_review.md.
# The guard must REFUSE TO WRITE, not warn and continue.
#
# These tests build a throwaway git repo in a tmpdir. They never touch the real
# evidence tree (the real-data tests above are read-only by design).

def _skew_fixture(tmp, materialise=True):
    """Create a tmp git repo shaped like evidence/experiments and commit a run.

    Returns the base_dir (the 'evidence/experiments' equivalent). When
    materialise is False, the committed files are removed from the working tree
    afterwards -- reproducing the post-reset skew exactly (tracked in HEAD and
    the index, absent on disk).
    """
    import subprocess
    from pathlib import Path

    base = Path(tmp) / "evidence" / "experiments"
    (base / "claim_probe_x" / "runs" / "run_a").mkdir(parents=True)
    (base / "run_a.json").write_text('{"run_id": "run_a"}\n', encoding="utf-8")
    pack = base / "claim_probe_x" / "runs" / "run_a" / "manifest.json"
    pack.write_text('{"run_id": "run_a"}\n', encoding="utf-8")

    def git(*a):
        subprocess.run(["git", "-C", str(tmp), *a], check=True,
                       capture_output=True)

    git("init", "-q")
    git("config", "user.email", "t@example.com")
    git("config", "user.name", "t")
    git("add", "-A")
    git("commit", "-q", "-m", "runs")

    if not materialise:
        # The skew: present in HEAD + index, absent on disk. `git status` shows
        # these as " D"; every working-tree reader sees a smaller repo.
        (base / "run_a.json").unlink()
        pack.unlink()

    return base


def test_is_indexer_read_path_shapes():
    assert b._is_indexer_read_path("run_a.json") is True
    assert b._is_indexer_read_path("claim_probe_x/runs/run_a/manifest.json") is True
    assert b._is_indexer_read_path("claim_probe_x/runs/run_a/metrics.json") is True
    assert b._is_indexer_read_path("claim_probe_x/runs/run_a/summary.md") is True
    # Not run evidence: derived artifacts, docs, scripts, profiles.
    assert b._is_indexer_read_path("INDEX.md") is False
    assert b._is_indexer_read_path("scripts/build_experiment_indexes.py") is False
    assert b._is_indexer_read_path("claim_probe_x/experiment.md") is False


def test_skew_guard_detects_unmaterialised_files():
    """The incident shape: tracked in HEAD, absent on disk -> both files flagged."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = _skew_fixture(tmp, materialise=False)
        missing = b._find_unmaterialised_evidence(base)
        assert missing == ["claim_probe_x/runs/run_a/manifest.json", "run_a.json"], missing


def test_skew_guard_clean_tree_is_silent():
    """A fully materialised tree reports nothing (no false positives)."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = _skew_fixture(tmp, materialise=True)
        assert b._find_unmaterialised_evidence(base) == []
        b._guard_worktree_materialised(base, allow_missing=False)  # must not exit


def test_skew_guard_exits_nonzero_without_writing():
    """The load-bearing behaviour: REFUSE, do not warn-and-continue."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = _skew_fixture(tmp, materialise=False)
        try:
            b._guard_worktree_materialised(base, allow_missing=False)
        except SystemExit as e:
            assert e.code == b.SKEW_GUARD_EXIT_CODE, e.code
        else:
            raise AssertionError("guard did not exit on a skewed tree")


def test_skew_guard_opt_out_proceeds():
    """--allow-missing-runs makes the absence a deliberate, explicit override."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = _skew_fixture(tmp, materialise=False)
        b._guard_worktree_materialised(base, allow_missing=True)  # must return


def test_skew_guard_non_git_tree_is_not_applicable():
    """Outside a git checkout there is no HEAD to skew from, so the guard is
    inapplicable rather than skipped -- and must not crash."""
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "evidence" / "experiments"
        base.mkdir(parents=True)
        assert b._git_tracked_paths(base) is None
        assert b._find_unmaterialised_evidence(base) == []


# --- recorded (NON-GATING) preconditions ----------------------------------
#
# `interpretation.recorded_preconditions[]` exists so a driver can record a real
# guard finding that does NOT invalidate its premise, WITHOUT the flat arm-blind
# preconditions[] path vacating the whole run (the V3-EXQ-785 defect). The tests
# below pin exactly that: the key is surfaced, and it is inert against
# adjudication. If a future change makes an unmet recorded_precondition block a
# run, these fail -- that is the point.
#
# Motivating drivers: v3_exq_737_ree_latent_policy_head_competence_probe.py and
# v3_exq_742_mech457_actor_critic_onoff.py (ree-v3 f2e8e2fcf8), both RECORD policy.
# See evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.

def _zworld_recorded(measured=0.0, arm="ac_cotrain", met=False):
    """A guard entry as experiments/_lib/zworld_encoder_guard.zworld_precondition()
    shapes it: a STRICT floor at 0.0 -- bit-identity is the failure signature, so
    measured == threshold == 0.0 is UNMET."""
    return {"name": "zworld_world_encoder_trained", "kind": "readiness",
            "measured": measured, "threshold": 0.0, "direction": "lower",
            "comparator": ">", "met": met, "arm": arm,
            "description": "P0 warmup moved a world_encoder tensor"}


def test_unmet_recorded_precondition_does_not_change_adjudication():
    """THE load-bearing invariant. An unmet recorded entry must NOT vacate the run."""
    interp = {"label": "x", "preconditions": [_floor(5.0, 1.0)],
              "recorded_preconditions": [_zworld_recorded()]}
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "verified", flag


def test_recorded_precondition_alone_does_not_make_a_run_adjudicable():
    """recorded_preconditions[] is not a substitute for the adjudicating list: a
    manifest declaring ONLY recorded entries is still `unverified` (surfaced, not
    blocked), never `precondition_unmet`."""
    interp = {"label": "x", "recorded_preconditions": [_zworld_recorded()]}
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "unverified", flag
    assert flag not in b.BLOCKING_ADJUDICATIONS


def test_recorded_precondition_never_appears_in_blocking_set():
    """Belt-and-braces: whatever the recorded entries say, the flag stays clear as
    long as the ADJUDICATING preconditions hold."""
    for measured in (0.0, -1.0, 1e-30):
        interp = {"label": "x", "preconditions": [_floor(5.0, 1.0)],
                  "recorded_preconditions": [_zworld_recorded(measured=measured)]}
        _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
        blocked, _reason = b.adjudication_blocks_governance_action(flag)
        assert not blocked, (measured, flag)


def test_an_unmet_gating_precondition_still_fires_alongside_a_recorded_one():
    """The non-gating list must not SUPPRESS the real gate either -- the exemption
    is scoped to recorded_preconditions[], not extended to preconditions[]."""
    interp = {"label": "x", "preconditions": [_floor(0.1, 1.0)],
              "recorded_preconditions": [_zworld_recorded()]}
    _, flag = b._compute_adjudication(interp, "FAIL", "diagnostic")
    assert flag == "precondition_unmet", flag


def test_recorded_findings_surface_unmet_entries():
    interp = {"label": "x",
              "recorded_preconditions": [_zworld_recorded(arm="ac_cotrain"),
                                         _zworld_recorded(arm="ac_frozen")]}
    found = b._recorded_precondition_findings(interp)
    assert len(found) == 2, found
    assert {f["arm"] for f in found} == {"ac_cotrain", "ac_frozen"}
    assert all(f["name"] == "zworld_world_encoder_trained" for f in found)


def test_recorded_findings_omit_met_entries():
    """A guard that PASSED is not a finding -- only unmet entries surface."""
    interp = {"label": "x",
              "recorded_preconditions": [_zworld_recorded(measured=0.004, met=True)]}
    assert b._recorded_precondition_findings(interp) == []


def test_recorded_findings_recompute_rather_than_trust_met():
    """Same recompute-is-authoritative rule as the adjudicating path: an author who
    writes met:True over a below-floor measurement is still surfaced."""
    interp = {"label": "x",
              "recorded_preconditions": [_zworld_recorded(measured=0.0, met=True)]}
    found = b._recorded_precondition_findings(interp)
    assert len(found) == 1, found


def test_recorded_findings_fall_back_to_met_when_not_recomputable():
    interp = {"label": "x",
              "recorded_preconditions": [{"name": "no_numbers", "met": False}]}
    assert [f["name"] for f in b._recorded_precondition_findings(interp)] == ["no_numbers"]


def test_recorded_findings_absent_key_is_empty():
    """Legacy manifests (the entire pre-2026-07-20 corpus) declare no
    recorded_preconditions -- output must be byte-identical, i.e. no findings."""
    assert b._recorded_precondition_findings({"label": "x"}) == []
    assert b._recorded_precondition_findings({}) == []
    assert b._recorded_precondition_findings(None) == []
    assert b._recorded_precondition_findings({"recorded_preconditions": "junk"}) == []
    assert b._recorded_precondition_findings({"recorded_preconditions": [None, 3]}) == []


def _conflicted_claim_meta():
    return {
        "direction_counts": {"supports": 1, "weakens": 1},  # conflict_ratio == 1.0
        "experimental_confidence": 0.0,
        "source_counts": {"experimental": 0, "literature": 2},
        "entries_total": 2,
    }


def test_hold_candidate_resolve_conflict_probe_gated_gets_acknowledge_option():
    """substrate_conditional/substrate_ceiling claims are explicitly parked
    pending an unbuilt upstream probe -- 'run conflict-resolution experiments'
    and 'promote despite conflict' don't name an action anyone can take."""
    criteria = {"thresholds": {"candidate_to_provisional": {"max_conflict_ratio": 0.35}}}
    registry_meta = {"epistemic_category": "substrate_conditional"}
    rec = b._recommendation_for_claim(
        "Q-TEST-PROBE-GATED", _conflicted_claim_meta(), "candidate", "open_question",
        criteria, registry_meta, matrix={"entries": []},
    )
    assert rec["recommendation"] == "hold_candidate_resolve_conflict"
    assert any("acknowledge conflict, no status change" in o.lower() for o in rec["options"])
    assert not any("run conflict-resolution experiments" in o.lower() for o in rec["options"])


def test_hold_candidate_resolve_conflict_substrate_ceiling_gets_acknowledge_option():
    criteria = {"thresholds": {"candidate_to_provisional": {"max_conflict_ratio": 0.35}}}
    registry_meta = {"epistemic_category": "substrate_ceiling"}
    rec = b._recommendation_for_claim(
        "Q-TEST-CEILING", _conflicted_claim_meta(), "candidate", "open_question",
        criteria, registry_meta, matrix={"entries": []},
    )
    assert rec["recommendation"] == "hold_candidate_resolve_conflict"
    assert any("acknowledge conflict, no status change" in o.lower() for o in rec["options"])


def test_hold_candidate_resolve_conflict_standard_category_options_unchanged():
    """A plain (non-gated) claim in conflict keeps the original balanced options
    -- the probe-gated variant must not leak into standard-category claims."""
    criteria = {"thresholds": {"candidate_to_provisional": {"max_conflict_ratio": 0.35}}}
    claim_meta = {
        "direction_counts": {"supports": 1, "weakens": 1},
        "experimental_confidence": 0.0,
        "genuine_exp_direction_counts": {"supports": 0},
        "source_counts": {"experimental": 2, "literature": 2},
        "entries_total": 4,
    }
    matrix = {"entries": [
        {"claim_id": "MECH-TEST-STANDARD", "source_type": "experimental", "run_id": "x_ree_v1_minimal"},
    ]}
    rec = b._recommendation_for_claim(
        "MECH-TEST-STANDARD", claim_meta, "candidate", "mechanism_hypothesis",
        criteria, registry_meta=None, matrix=matrix,
    )
    assert rec["recommendation"] == "hold_candidate_resolve_conflict"
    assert any("run conflict-resolution experiments" in o.lower() for o in rec["options"])


# --- EXP-* proposal-eligibility gate: substrate_conditional / v3_pending+v4 ---
#
# Regression target: 2026-08-02 (chip-20260802-backlog-dispatcher-gating-bug).
# _is_experiment_ineligible_claim previously checked only answered/closing
# status and out_of_domain/derivational/governance_rule epistemic_category --
# it did NOT recognize substrate_conditional/substrate_ceiling claims or
# claims deliberately deferred to a later architecture generation
# (v3_pending + implementation_phase>=v4), even though _recommendation_for_
# claim already had working logic for the second signal. Confirmed live: 56
# medium-priority EXP-* proposals had been minted for claims whose own
# claims.yaml notes said "DO NOT BUILD" / "DO NOT QUEUE AN EXPERIMENT AGAINST
# THIS" (Q-084, Q-082, Q-074, MECH-442 are the shapes fixtured below).

def test_ineligible_substrate_conditional_no_v3_pending():
    """Q-084/Q-082 shape: epistemic_category=substrate_conditional,
    implementation_phase=v4, but v3_pending is NOT set -- this must still be
    caught by the epistemic_category rule alone (the v3_pending+v4 rule is a
    distinct, independent signal, not a prerequisite)."""
    meta = {"status": "candidate", "epistemic_category": "substrate_conditional",
            "implementation_phase": "v4", "claim_type": "open_question"}
    assert b._is_experiment_ineligible_claim(meta) is True


def test_ineligible_substrate_ceiling():
    meta = {"status": "candidate", "epistemic_category": "substrate_ceiling",
            "implementation_phase": "v3", "claim_type": "mechanism_hypothesis"}
    assert b._is_experiment_ineligible_claim(meta) is True


def test_ineligible_v3_pending_deferred_to_later_generation():
    """Q-074/ARC-080/MECH-264/MECH-265 shape: v3_pending + implementation_phase
    >= v4, WITHOUT an explicit epistemic_category set -- must be caught by the
    _is_deferred_to_later_generation rule, mirroring _recommendation_for_
    claim's held_v4_by_architectural_commitment gate."""
    meta = {"status": "candidate", "v3_pending": "True", "implementation_phase": "v6",
            "claim_type": "open_question"}
    assert b._is_experiment_ineligible_claim(meta) is True
    # generation boundary: v4 is the lowest deferred generation
    assert b._is_experiment_ineligible_claim(
        {"status": "candidate", "v3_pending": "True", "implementation_phase": "v4"}
    ) is True


def test_ineligible_ceiling_decision_deferred_via_substrate_conditional():
    """MECH-442 shape: implementation_phase=v3 (NOT v4+), so the deferred-
    generation rule alone would miss it -- must be caught by
    epistemic_category=substrate_conditional independently."""
    meta = {"status": "candidate", "epistemic_category": "substrate_conditional",
            "implementation_phase": "v3", "claim_type": "mechanism_hypothesis"}
    assert b._is_experiment_ineligible_claim(meta) is True


def test_ineligible_unregistered_claim_id():
    """Dead/renamed claim_id (e.g. Q-046, MECH-900): claim_registry.get(claim_id,
    {}) falls through to an empty dict when the id has no claims.yaml entry at
    all. Must be ineligible -- there is no disposition to test."""
    assert b._is_experiment_ineligible_claim({}) is True


def test_eligible_v3_pending_still_v3_not_later_generation():
    """ARC-063 shape (the load-bearing negative control): v3_pending=true but
    implementation_phase=v3 (not >=v4) and no substrate_conditional/ceiling
    category -- this is hold_pending_v3_substrate territory (substrate already
    exists or is landing; genuinely testable), NOT an architectural deferral.
    Must stay eligible or the gate over-suppresses claims that need exactly
    the EXP-* proposal this pipeline would otherwise mint for them."""
    meta = {"status": "candidate", "v3_pending": "True", "implementation_phase": "v3",
            "claim_type": "architectural_commitment"}
    assert b._is_experiment_ineligible_claim(meta) is False


def test_eligible_plain_candidate_unaffected():
    """A standard registered claim with no gating fields at all must stay
    eligible -- the new rules must not over-suppress ordinary candidates."""
    meta = {"status": "candidate", "claim_type": "mechanism_hypothesis"}
    assert b._is_experiment_ineligible_claim(meta) is False


def test_recommendation_held_v4_still_fires_after_shared_helper_refactor():
    """_recommendation_for_claim's held_v4_by_architectural_commitment gate now
    delegates to the shared _is_deferred_to_later_generation helper -- pin that
    the refactor didn't change its own behavior."""
    criteria = {"thresholds": {}}
    registry_meta = {"v3_pending": "True", "implementation_phase": "v4"}
    rec = b._recommendation_for_claim(
        "ARC-TEST-V4", {"source_counts": {"experimental": 0}}, "candidate",
        "architectural_commitment", criteria, registry_meta, matrix={"entries": []},
    )
    assert rec["recommendation"] == "held_v4_by_architectural_commitment"


# --- decision_deadline_utc freeze-on-first-trigger -------------------------
#
# Regression target: 2026-08-01 (chip-20260801-decision-deadline-rolling-defect-
# review). decision_deadline_utc was recomputed as generated_at_dt + 72h on
# EVERY governance regeneration while the underlying mandatory_decision
# conflict stayed unresolved, instead of being frozen on the regen where the
# checkpoint first fired. That meant a "TIME-SENSITIVE, deadline approaching"
# citation was always ~3 days out and could never actually be missed.
# Confirmed concretely: 16 unrelated claims in the pre-fix
# evidence_backlog.v1.json all carried the IDENTICAL deadline timestamp
# (generated_at_utc of that one regen + 72h) -- only possible if every one was
# computed from "now" rather than from its own first-trigger time.

def _mandatory_decision_planning_criteria():
    # Loosen the mandatory-decision-checkpoint gate so two matched-seed
    # supports/weakens entries are sufficient to trigger it deterministically,
    # independent of the production defaults in planning_criteria.v1.json.
    return {
        "thresholds": {
            "mandatory_decision_conflict_ratio": 0.5,
            "mandatory_decision_min_fresh_batches": 1,
            "mandatory_decision_recent_window": 10,
            "mandatory_decision_deadline_hours": 72,
        },
    }


def _mandatory_decision_matrix(claim_id="MECH-TEST-DEADLINE"):
    # One genuine V3 "supports" + one genuine V3 "weakens" entry at distinct
    # minute-truncated timestamps -> conflict_ratio == 1.0 (>= 0.5 threshold)
    # and recent_targeted_batches == 2 (>= 1 threshold), with no recorded
    # decision -> decision_unresolved == True. Together these satisfy every
    # mandatory_decision_checkpoint precondition.
    entries = [
        {
            "claim_id": claim_id,
            "source_type": "experimental",
            "run_id": "run_a_v3",
            "run_id_full": "20260801T000000Z_run_a_v3",
            "evidence_direction": "supports",
            "timestamp_utc": "2026-08-01T00:00:00Z",
        },
        {
            "claim_id": claim_id,
            "source_type": "experimental",
            "run_id": "run_b_v3",
            "run_id_full": "20260801T010000Z_run_b_v3",
            "evidence_direction": "weakens",
            "timestamp_utc": "2026-08-01T01:00:00Z",
        },
    ]
    return {"claims": {claim_id: {}}, "entries": entries}


def test_mandatory_decision_checkpoint_deadline_frozen_across_regens():
    """Two consecutive regens of the same unresolved conflict must produce the
    SAME decision_deadline_utc -- not a fresh generated_at + 72h each time."""
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DEADLINE"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _mandatory_decision_matrix(claim_id)
    criteria = _mandatory_decision_planning_criteria()

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)

        backlog_1, _proposals_1, _arch_1 = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {}, criteria,
            "2026-08-01T00:00:00Z",
        )
        item_1 = next(i for i in backlog_1 if i["claim_id"] == claim_id)
        assert item_1["signals"]["mandatory_decision_checkpoint"] is True
        deadline_1 = item_1["signals"]["decision_deadline_utc"]
        assert deadline_1

        # A second regen, hours later, with the conflict still unresolved (no
        # decision entries were added). The buggy code computes
        # generated_at_dt + 72h off THIS call's generated_at and would
        # therefore differ from deadline_1 by exactly the 5h gap below.
        backlog_2, _proposals_2, _arch_2 = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {}, criteria,
            "2026-08-01T05:00:00Z",
        )
        item_2 = next(i for i in backlog_2 if i["claim_id"] == claim_id)
        assert item_2["signals"]["mandatory_decision_checkpoint"] is True
        deadline_2 = item_2["signals"]["decision_deadline_utc"]

        assert deadline_2 == deadline_1, (
            "decision_deadline_utc rolled forward on a second regen of the "
            f"same unresolved conflict: {deadline_1!r} -> {deadline_2!r}"
        )
        # Anchored to the FIRST regen's generated_at, not the second's.
        assert deadline_1 == "2026-08-04T00:00:00Z"


def test_mandatory_decision_checkpoint_deadline_remints_after_clearing():
    """If the checkpoint clears (claim drops out of the backlog) and later
    re-triggers, a fresh deadline is expected -- freezing must not persist
    across a genuine resolve-and-recur cycle."""
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DEADLINE-RETRIGGER"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _mandatory_decision_matrix(claim_id)
    criteria = _mandatory_decision_planning_criteria()

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)

        backlog_1, _p1, _a1 = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {}, criteria,
            "2026-08-01T00:00:00Z",
        )
        deadline_1 = next(
            i for i in backlog_1 if i["claim_id"] == claim_id
        )["signals"]["decision_deadline_utc"]
        assert deadline_1 == "2026-08-04T00:00:00Z"

        # Checkpoint clears: an approved decision with an allowed outcome
        # resolves the claim, so mandatory_decision_checkpoint no longer fires.
        latest_adjudication_decisions = {
            claim_id: b.DecisionLogEntry(
                claim_id=claim_id,
                decision_status="approved",
                recommendation="retain_ree",
                decision_needed="",
                timestamp_utc="2026-08-02T00:00:00Z",
            ),
        }
        backlog_cleared, _p2, _a2 = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, latest_adjudication_decisions,
            criteria, "2026-08-02T00:00:00Z",
        )
        cleared_items = [i for i in backlog_cleared if i["claim_id"] == claim_id]
        assert not any(i["signals"].get("mandatory_decision_checkpoint") for i in cleared_items)

        # Re-trigger with a fresh, still-unresolved conflict (revert to no
        # decision on record, simulating a new conflict cycle).
        backlog_3, _p3, _a3 = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {}, criteria,
            "2026-08-03T00:00:00Z",
        )
        deadline_3 = next(
            i for i in backlog_3 if i["claim_id"] == claim_id
        )["signals"]["decision_deadline_utc"]
        assert deadline_3 == "2026-08-06T00:00:00Z"
        assert deadline_3 != deadline_1


# --- mandatory_decision_checkpoint: since-decision freshness ---------------
#
# Regression target: a claim that already received a deliberate governance
# decision -- including a hold_* deferral, which is NOT a terminal outcome --
# re-tripped mandatory_decision_checkpoint on every subsequent regen purely
# because recent_targeted_batches counts a flat trailing window with no
# regard for when the decision was made. Only batches that land AFTER the
# decision should count as "fresh" once a decision is on record.

def _v3_entries(claim_id, specs):
    """specs: list of (direction, timestamp_utc, run_suffix) tuples."""
    return {
        "claims": {claim_id: {}},
        "entries": [
            {
                "claim_id": claim_id,
                "source_type": "experimental",
                "run_id": f"run_{suffix}_v3",
                "evidence_direction": direction,
                "timestamp_utc": ts,
            }
            for direction, ts, suffix in specs
        ],
    }


def test_mandatory_decision_checkpoint_suppressed_after_hold_with_no_new_evidence():
    """A claim already carrying an applied hold_* decision, with no evidence
    landed since, must NOT re-trigger the checkpoint -- even though a hold is
    not a terminal outcome and conflict_ratio/batches still meet the raw
    thresholds on their own."""
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-HOLD-NO-NEW-EVIDENCE"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
        ("weakens", "2026-07-01T01:00:00Z", "b"),
    ])
    criteria = {
        "thresholds": {
            "mandatory_decision_conflict_ratio": 0.5,
            "mandatory_decision_min_fresh_batches": 1,
            "mandatory_decision_recent_window": 10,
            "mandatory_decision_deadline_hours": 72,
        },
    }
    latest_adjudication_decisions = {
        claim_id: b.DecisionLogEntry(
            claim_id=claim_id,
            decision_status="applied",
            recommendation="hold_candidate_resolve_conflict",
            decision_needed="",
            timestamp_utc="2026-07-02T00:00:00Z",  # after both entries
        ),
    }

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        backlog, _p, _a = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, latest_adjudication_decisions,
            criteria, "2026-07-05T00:00:00Z",
        )
        items = [i for i in backlog if i["claim_id"] == claim_id]
        assert not any(i["signals"].get("mandatory_decision_checkpoint") for i in items), (
            "checkpoint re-fired on a claim with an applied hold and no new "
            "evidence since"
        )


def test_mandatory_decision_checkpoint_refires_after_new_evidence_since_decision():
    """The SAME hold as above, but a new conflicting entry lands after the
    decision timestamp -- the checkpoint must fire again."""
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-HOLD-NEW-EVIDENCE"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
        ("weakens", "2026-07-01T01:00:00Z", "b"),
        ("weakens", "2026-07-03T00:00:00Z", "c"),  # after the decision below
    ])
    criteria = {
        "thresholds": {
            "mandatory_decision_conflict_ratio": 0.6,
            "mandatory_decision_min_fresh_batches": 1,
            "mandatory_decision_recent_window": 10,
            "mandatory_decision_deadline_hours": 72,
        },
    }
    latest_adjudication_decisions = {
        claim_id: b.DecisionLogEntry(
            claim_id=claim_id,
            decision_status="applied",
            recommendation="hold_candidate_resolve_conflict",
            decision_needed="",
            timestamp_utc="2026-07-02T00:00:00Z",  # before entry c only
        ),
    }

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        backlog, _p, _a = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, latest_adjudication_decisions,
            criteria, "2026-07-05T00:00:00Z",
        )
        item = next(i for i in backlog if i["claim_id"] == claim_id)
        assert item["signals"]["mandatory_decision_checkpoint"] is True
        assert item["signals"]["fresh_batches_since_decision"] == 1


# --- dormant_high_conflict watchlist -----------------------------------------
#
# Two claim shapes are contentious (high conflict_ratio) but invisible to
# mandatory_decision_checkpoint: claims worked so rarely they never meet the
# fresh-batch floor ("dormant_low_activity"), and claims worked heavily whose
# conflict never quite crosses the mandatory bar ("chronic_under_threshold").
# Both should surface in the no-deadline evidence_backlog.v1.json watchlist.

def _dormant_criteria(**overrides):
    thresholds = {
        "mandatory_decision_conflict_ratio": 0.8,
        "mandatory_decision_min_fresh_batches": 2,
        "mandatory_decision_recent_window": 10,
        "mandatory_decision_deadline_hours": 72,
        "dormant_high_conflict_ratio": 0.55,
        "dormant_high_conflict_min_entries": 2,
    }
    thresholds.update(overrides)
    return {"thresholds": thresholds}


def _dormant_items_for(planning_root, matrix, claim_registry, criteria, generated_at,
                        latest_adjudication_decisions=None):
    b._write_planning_outputs(
        planning_root, matrix, claim_registry, [], {},
        latest_adjudication_decisions or {}, criteria, generated_at,
    )
    doc = json.loads((planning_root / "evidence_backlog.v1.json").read_text(encoding="utf-8"))
    return doc["dormant_high_conflict"]


def test_dormant_high_conflict_watchlist_flags_low_activity_claim():
    """Two batches total, but mandatory_decision_min_fresh_batches is 5 -- the
    claim never meets the mandatory floor despite conflict_ratio 1.0."""
    import json
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DORMANT-LOW-ACTIVITY"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
        ("weakens", "2026-07-01T01:00:00Z", "b"),
    ])
    criteria = _dormant_criteria(mandatory_decision_min_fresh_batches=5)

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        items = _dormant_items_for(planning_root, matrix, claim_registry, criteria,
                                    "2026-07-05T00:00:00Z")
        entry = next((i for i in items if i["claim_id"] == claim_id), None)
        assert entry is not None, "dormant, high-conflict claim never surfaced"
        assert entry["pattern"] == "dormant_low_activity"
        assert entry["conflict_ratio"] == 1.0


def test_dormant_high_conflict_watchlist_flags_chronic_under_threshold_claim():
    """Three batches (>= the mandatory batch floor) but conflict_ratio 0.667
    stays under the 0.8 mandatory bar -- heavy work, never forced to decide."""
    import json
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-CHRONIC-UNDER-THRESHOLD"
    claim_registry = {claim_id: {"status": "active", "claim_type": "mechanism_hypothesis"}}
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
        ("supports", "2026-07-01T01:00:00Z", "b"),
        ("weakens", "2026-07-01T02:00:00Z", "c"),
    ])
    criteria = _dormant_criteria()

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        items = _dormant_items_for(planning_root, matrix, claim_registry, criteria,
                                    "2026-07-05T00:00:00Z")
        entry = next((i for i in items if i["claim_id"] == claim_id), None)
        assert entry is not None, "chronic under-threshold claim never surfaced"
        assert entry["pattern"] == "chronic_under_threshold"
        assert entry["conflict_ratio"] == 0.667
        assert entry["current_status"] == "active"


def test_dormant_high_conflict_watchlist_excludes_mandatory_checkpoint_claims():
    """A claim that DOES trigger mandatory_decision_checkpoint must not also
    appear in the watchlist -- the two are mutually exclusive."""
    import json
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DEADLINE"  # reuses the module-level mandatory-decision fixture
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _mandatory_decision_matrix(claim_id)
    criteria = _mandatory_decision_planning_criteria()
    criteria["thresholds"]["dormant_high_conflict_ratio"] = 0.1
    criteria["thresholds"]["dormant_high_conflict_min_entries"] = 1

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        items = _dormant_items_for(planning_root, matrix, claim_registry, criteria,
                                    "2026-08-01T00:00:00Z")
        assert not any(i["claim_id"] == claim_id for i in items), (
            "claim under an active mandatory_decision_checkpoint also leaked "
            "into the no-deadline watchlist"
        )


def test_dormant_high_conflict_watchlist_excludes_resolved_claims():
    """A high-conflict claim with an already-resolved (terminal) decision is
    not neglected -- it must not appear in the watchlist."""
    import json
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DORMANT-RESOLVED"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
        ("weakens", "2026-07-01T01:00:00Z", "b"),
    ])
    criteria = _dormant_criteria(mandatory_decision_min_fresh_batches=5)
    latest_adjudication_decisions = {
        claim_id: b.DecisionLogEntry(
            claim_id=claim_id,
            decision_status="applied",
            recommendation="retain_ree",  # terminal, allowed outcome
            decision_needed="",
            timestamp_utc="2026-07-02T00:00:00Z",
        ),
    }

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        items = _dormant_items_for(planning_root, matrix, claim_registry, criteria,
                                    "2026-07-05T00:00:00Z", latest_adjudication_decisions)
        assert not any(i["claim_id"] == claim_id for i in items), (
            "resolved claim still showed up on the neglect watchlist"
        )


def test_dormant_high_conflict_watchlist_markdown_surfaces_worst_first():
    """The dormant_high_conflict list is machine-readable JSON only -- nothing
    previously surfaced it to a human. DORMANT_HIGH_CONFLICT_WATCHLIST.md must
    list both dormant patterns, worst-conflict-first, and INDEX.md must count
    them."""
    import json
    import tempfile
    from pathlib import Path

    low_activity_id = "MECH-TEST-DORMANT-MD-LOW"
    chronic_id = "MECH-TEST-DORMANT-MD-CHRONIC"
    claim_registry = {
        low_activity_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"},
        chronic_id: {"status": "active", "claim_type": "mechanism_hypothesis"},
    }
    matrix = {
        "claims": {low_activity_id: {}, chronic_id: {}},
        "entries": (
            _v3_entries(low_activity_id, [
                ("supports", "2026-07-01T00:00:00Z", "a"),
                ("weakens", "2026-07-01T01:00:00Z", "b"),
            ])["entries"]
            + _v3_entries(chronic_id, [
                ("supports", "2026-07-01T00:00:00Z", "c"),
                ("supports", "2026-07-01T01:00:00Z", "d"),
                ("weakens", "2026-07-01T02:00:00Z", "e"),
            ])["entries"]
        ),
    }
    criteria = _dormant_criteria(mandatory_decision_min_fresh_batches=5)

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        backlog, _p, _a = b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {},
            criteria, "2026-07-05T00:00:00Z",
        )
        watchlist_path = planning_root / "DORMANT_HIGH_CONFLICT_WATCHLIST.md"
        assert watchlist_path.exists(), "watchlist markdown was not written"
        text = watchlist_path.read_text(encoding="utf-8")

        # conflict_ratio 1.0 (low_activity) must precede 0.667 (chronic) -- worst-first.
        low_pos = text.index(low_activity_id)
        chronic_pos = text.index(chronic_id)
        assert low_pos < chronic_pos, (
            "watchlist is not sorted worst-conflict-first"
        )
        assert "dormant_low_activity" in text
        assert "chronic_under_threshold" in text

        doc = json.loads((planning_root / "evidence_backlog.v1.json").read_text(encoding="utf-8"))
        n_dormant = len(doc["dormant_high_conflict"])
        assert n_dormant == 2

        index_text = (planning_root / "INDEX.md").read_text(encoding="utf-8")
        assert f"({n_dormant} item(s))" in index_text and "Dormant high-conflict watchlist" in index_text, (
            "INDEX.md does not reference the dormant high-conflict watchlist count"
        )


def test_dormant_high_conflict_watchlist_markdown_reports_none_when_empty():
    """An empty dormant_high_conflict list must still render a valid (empty)
    watchlist file rather than a stale one from a prior run."""
    import tempfile
    from pathlib import Path

    claim_id = "MECH-TEST-DORMANT-MD-EMPTY"
    claim_registry = {claim_id: {"status": "candidate", "claim_type": "mechanism_hypothesis"}}
    # Only one entry -- fails dormant_high_conflict_min_entries (2), so the
    # watchlist stays empty for this claim.
    matrix = _v3_entries(claim_id, [
        ("supports", "2026-07-01T00:00:00Z", "a"),
    ])
    criteria = _dormant_criteria()

    with tempfile.TemporaryDirectory() as tmp:
        planning_root = Path(tmp)
        b._write_planning_outputs(
            planning_root, matrix, claim_registry, [], {}, {},
            criteria, "2026-07-05T00:00:00Z",
        )
        text = (planning_root / "DORMANT_HIGH_CONFLICT_WATCHLIST.md").read_text(encoding="utf-8")
        assert "_none_" in text
        assert claim_id not in text


# --- _suggest_experiment_type / _suggest_literature_type: literal-duplicate
# reuse bug ---
#
# Regression target: 2026-08-02 (chip-20260802-suggest-exp-type-reuse-bug).
# Both functions fell back to the MOST COMMON historical experiment_type/
# literature_type already tagged to a claim. In this corpus that value is a
# one-off identifier naming a SPECIFIC, ALREADY-EXECUTED
# ree-v3/experiments/<type>.py script (or an already-written
# evidence/literature/<type>/ review) -- never a reusable category -- so the
# "suggestion" was always literally the name of completed work. Confirmed
# live against the real committed matrix (claim_evidence.v1.json) and
# proposals file (experiment_proposals.v1.json) as of 2026-08-02: 35/35
# medium-priority EXP-* proposals matching the v3_exq_* convention (already
# hand-patched in REE_assembly e7be2c32d4), plus one residual case the
# convention-specific grep missed -- EXP-0407/Q-017, suggesting
# `control_axis_ablation`, an experiment_type with 70+ completed runs on
# disk under a pre-v3_exq naming era. Fix: never surface a historical type
# verbatim; always hand back the generic claim_probe_/targeted_review_
# placeholder.

def test_suggest_experiment_type_ignores_prior_history():
    """A claim with prior experimental entries must NOT get one of those
    entries' experiment_type back -- that would be an already-run script
    (MECH-124 shape: v3_exq_224_mech124_zgoal_salience_diag /
    v3_exq_298_mech124_zgoal_salience_discriminative, both real completed
    runs)."""
    matrix = {
        "entries": [
            {
                "claim_id": "MECH-124",
                "source_type": "experimental",
                "experiment_type": "v3_exq_224_mech124_zgoal_salience_diag",
                "run_id": "v3_exq_224_mech124_zgoal_salience_diag_20260101T000000Z_v3",
            },
            {
                "claim_id": "MECH-124",
                "source_type": "experimental",
                "experiment_type": "v3_exq_224_mech124_zgoal_salience_diag",
                "run_id": "v3_exq_224_mech124_zgoal_salience_diag_20260102T000000Z_v3",
            },
            {
                "claim_id": "MECH-124",
                "source_type": "experimental",
                "experiment_type": "v3_exq_298_mech124_zgoal_salience_discriminative",
                "run_id": "v3_exq_298_mech124_zgoal_salience_discriminative_20260103T000000Z_v3",
            },
        ],
    }
    result = b._suggest_experiment_type("MECH-124", matrix)
    assert result not in {
        "v3_exq_224_mech124_zgoal_salience_diag",
        "v3_exq_298_mech124_zgoal_salience_discriminative",
    }
    assert result == "claim_probe_mech_124"


def test_suggest_experiment_type_no_history_matches_prior_behavior():
    """No-history case is unchanged: the generic placeholder, same as before
    this fix (this branch was never the buggy one)."""
    matrix = {"entries": []}
    assert b._suggest_experiment_type("Q-999", matrix) == "claim_probe_q_999"


def test_suggest_literature_type_ignores_prior_history():
    """ARC-062 shape (real corpus data): a claim with prior literature entries
    tagged with a topic-specific literature_type must not get that value back
    -- `targeted_review_arc_062_rule_apprehension` already has a populated
    evidence/literature/ dir with real entries. The claim-generic placeholder
    (`targeted_review_arc_062`) is a distinct, safe, never-yet-used name."""
    matrix = {
        "entries": [
            {
                "claim_id": "ARC-062",
                "source_type": "literature",
                "experiment_type": "targeted_review_arc_062_rule_apprehension",
                "run_id": "lit_targeted_review_arc_062_rule_apprehension_0001",
            },
            {
                "claim_id": "ARC-062",
                "source_type": "literature",
                "experiment_type": "targeted_review_arc_062_rule_apprehension",
                "run_id": "lit_targeted_review_arc_062_rule_apprehension_0002",
            },
            {
                "claim_id": "ARC-062",
                "source_type": "literature",
                "experiment_type": "targeted_review_arc_062_refuge_forage_ecology",
                "run_id": "lit_targeted_review_arc_062_refuge_forage_ecology_0001",
            },
        ],
    }
    result = b._suggest_literature_type("ARC-062", matrix)
    assert result not in {
        "targeted_review_arc_062_rule_apprehension",
        "targeted_review_arc_062_refuge_forage_ecology",
    }
    assert result == "targeted_review_arc_062"


def test_suggest_literature_type_no_history_matches_prior_behavior():
    """No-history case is unchanged: the generic placeholder, same as before
    this fix (this branch was never the buggy one)."""
    matrix = {"entries": []}
    assert b._suggest_literature_type("Q-999", matrix) == "targeted_review_q_999"


# --- backlog_id-null proposal carry-forward instability --------------------
#
# Regression target: 2026-08-02 (chip-20260802-backlog-null-carryforward).
# Proposals with backlog_id null/absent (manual_proposals.v1.json historically
# had NO backlog_id on any of its 81 items) relied on falling back to
# proposal_id for carry-forward identity. That fallback is not code-enforced
# stable the way backlog_id is (every auto-generated proposal gets one,
# minted once and carried forward by claim_id) -- a manual item's status
# survived a regen only because nothing rewrote its proposal_id, an
# unenforced invariant. Confirmed incident shape: MECH-426/EXP-0384,
# MECH-427/EXP-0385, INV-087/EXP-0386 were hand-patched to
# blocked_substrate/blocked_substrate/executed and observed reverted to
# "proposed" in a shared working tree the same day. Fix: mint a stable
# EVB-NNNN for every manual proposal on first regen
# (_mint_missing_manual_backlog_ids), persisted back to manual_proposals.v1.json
# so it is never re-minted, with the numeric id space shared/reserved against
# evidence_backlog.v1.json via _reserve_manual_proposal_backlog_ids so the two
# minting loops can never collide.
#
# A second, more subtle bug was found empirically running this fix's FIRST
# regen against the real (not-yet-regenerated) live experiment_proposals.v1.json
# in an isolated scratch copy: the OLD on-disk record for a manual proposal
# is keyed only by proposal_id (it predates minting), but the FRESH item now
# carries a backlog_id and a single-preferred-key lookup keys on THAT instead
# -- missing the old record entirely. The "preserve historical resolution
# records" safety net then re-appends the old record verbatim (so nothing is
# silently lost), but the result is a DUPLICATE: one fresh "proposed" row plus
# one stale-but-correct row. _proposal_identity_keys returns every identifier
# a proposal carries (backlog_id AND proposal_id) so a lookup can match either
# way, in either direction, at any point in the transition.

def test_proposal_identity_keys_backlog_id_first():
    assert b._proposal_identity_keys(
        {"backlog_id": "EVB-0500", "proposal_id": "EXP-0384"}
    ) == ["EVB-0500", "EXP-0384"]


def test_proposal_identity_keys_proposal_id_only():
    assert b._proposal_identity_keys(
        {"backlog_id": None, "proposal_id": "EXP-0384"}
    ) == ["EXP-0384"]
    assert b._proposal_identity_keys({"proposal_id": "EXP-0384"}) == ["EXP-0384"]


def test_proposal_identity_keys_empty_when_neither_present():
    assert b._proposal_identity_keys({}) == []


def test_proposal_identity_keys_dedupes_when_equal():
    # Pathological but should not produce a 2-element list of the same string.
    assert b._proposal_identity_keys(
        {"backlog_id": "EXP-0384", "proposal_id": "EXP-0384"}
    ) == ["EXP-0384"]


def test_mint_missing_manual_backlog_ids_assigns_only_missing():
    manual_doc = {
        "items": [
            {"proposal_id": "EXP-0384", "claim_id": "MECH-426"},  # missing
            {"proposal_id": "EXP-0129", "claim_id": "MECH-104", "backlog_id": "EVB-0062"},  # has one
        ]
    }
    changed, next_idx = b._mint_missing_manual_backlog_ids(manual_doc, 490)
    assert changed is True
    assert manual_doc["items"][0]["backlog_id"] == "EVB-0490"
    assert manual_doc["items"][1]["backlog_id"] == "EVB-0062"  # untouched
    assert next_idx == 491


def test_mint_missing_manual_backlog_ids_is_idempotent():
    """Second call on an already-minted doc is a no-op: same ids, changed=False.
    This is what makes the carry-forward SAFE across repeated regens -- a
    manual item's backlog_id, once minted, never moves again."""
    manual_doc = {"items": [{"proposal_id": "EXP-0384", "claim_id": "MECH-426"}]}
    changed1, next_idx1 = b._mint_missing_manual_backlog_ids(manual_doc, 490)
    assert changed1 is True
    minted_id = manual_doc["items"][0]["backlog_id"]

    changed2, next_idx2 = b._mint_missing_manual_backlog_ids(manual_doc, next_idx1)
    assert changed2 is False
    assert manual_doc["items"][0]["backlog_id"] == minted_id
    assert next_idx2 == next_idx1  # counter did not advance on the no-op pass


def test_reserve_manual_proposal_backlog_ids_prevents_future_collision():
    """The auto-backlog minting loop only scans evidence_backlog.v1.json;
    without folding manual_proposals.v1.json's own ids into the same
    reservation set, a freshly-minted auto EVB-NNNN could collide with one
    already owned by a manual proposal."""
    manual_doc = {
        "items": [
            {"proposal_id": "EXP-0384", "backlog_id": "EVB-0490"},
            {"proposal_id": "EXP-0385", "backlog_id": "EVB-0491"},
            {"proposal_id": "EXP-0129", "backlog_id": "EVB-PINNED-Q019"},  # non-numeric, ignored
            {"proposal_id": "EXP-0999"},  # missing backlog_id, ignored
        ]
    }
    used = {489}
    b._reserve_manual_proposal_backlog_ids(manual_doc, used)
    assert used == {489, 490, 491}


def _carry_forward(fresh_item, existing_status_by_key):
    """Mirrors main()'s real merge loop exactly (site 3):
    `for _key in _proposal_identity_keys(_p): if _key in status: update; break`.
    Not a reimplementation of new logic -- the same try-each-key-in-order
    shape now used at every carry-forward site in main()."""
    for _key in b._proposal_identity_keys(fresh_item):
        if _key in existing_status_by_key:
            fresh_item.update(existing_status_by_key[_key])
            return True
    return False


def _index_by_all_keys(item, status_fields):
    """Mirrors main()'s _existing_proposal_status population (site 1):
    register the SAME status dict under every identity key the old record
    carries, not just its preferred one."""
    status = {k: item[k] for k in status_fields if k in item}
    return {key: status for key in b._proposal_identity_keys(item)}


def test_manual_proposal_status_survives_transition_onto_a_freshly_minted_backlog_id():
    """The actual bug found empirically 2026-08-02: the OLD on-disk record
    (written before this fix existed) is keyed ONLY by proposal_id -- it has
    no backlog_id at all, exactly like every real entry in
    experiment_proposals.v1.json today. The FRESH item, from a
    manual_proposals.v1.json that has since been backfilled with a minted
    backlog_id, now prefers a DIFFERENT key. A lookup that only tries the
    fresh item's preferred key misses the old record. This is the case a
    single-key `_proposal_carry_forward_key` lookup got wrong; asserting it
    here is what pins the fix rather than just the steady-state case."""
    # Old record: pre-fix shape, backlog_id was never minted at all.
    old_record = {"proposal_id": "EXP-0384", "status": "blocked_substrate",
                  "blocked_note": "velocity readout not built"}
    existing_status_by_key = _index_by_all_keys(
        old_record, ("status", "blocked_note")
    )
    assert set(existing_status_by_key) == {"EXP-0384"}  # no backlog_id key yet

    # Fresh item: same proposal, but manual_proposals.v1.json has since been
    # backfilled -- it now carries a minted backlog_id the old record never had.
    fresh_item = {"proposal_id": "EXP-0384", "backlog_id": "EVB-0490", "status": "proposed"}

    matched = _carry_forward(fresh_item, existing_status_by_key)
    assert matched is True
    assert fresh_item["status"] == "blocked_substrate"
    assert fresh_item["blocked_note"] == "velocity readout not built"


def test_manual_proposal_status_survives_two_regen_cycles_via_backlog_id():
    """Steady-state shape (after the transition above has already happened
    once): a manual proposal is hand-gated between two regens where BOTH the
    old record and the fresh item already carry the same minted backlog_id.
    Exercises _mint_missing_manual_backlog_ids' idempotency (cycle 2's mint
    call is a no-op) together with the carry-forward merge."""
    # Cycle 1: manual_proposals.v1.json has no backlog_id yet.
    manual_doc = {
        "items": [{"proposal_id": "EXP-0384", "claim_id": "MECH-426", "status": "proposed"}]
    }
    changed, next_idx = b._mint_missing_manual_backlog_ids(manual_doc, 490)
    assert changed is True
    assert manual_doc["items"][0]["backlog_id"] == "EVB-0490"

    # Regen 1's output (experiment_proposals.v1.json) carries the minted id.
    regen1_proposal = dict(manual_doc["items"][0])
    assert regen1_proposal["status"] == "proposed"

    # A session hand-patches the DERIVED file's status (as the real MECH-426
    # incident did), independent of the regen.
    regen1_proposal["status"] = "blocked_substrate"
    regen1_proposal["blocked_note"] = "velocity readout not built"

    # Cycle 2: a fresh regen reloads manual_proposals.v1.json (backlog_id
    # already minted and persisted from cycle 1 -- mint is a no-op) and
    # rebuilds proposals from source (status resets to "proposed" in the
    # freshly-loaded copy, exactly as main() does every cycle).
    changed2, _ = b._mint_missing_manual_backlog_ids(manual_doc, next_idx)
    assert changed2 is False  # already minted -- no re-mint, no drift
    fresh_proposal = dict(manual_doc["items"][0])
    assert fresh_proposal["status"] == "proposed"  # source is always "proposed"

    existing_status_by_key = _index_by_all_keys(
        regen1_proposal, ("status", "blocked_note")
    )
    matched = _carry_forward(fresh_proposal, existing_status_by_key)
    assert matched is True
    assert fresh_proposal["status"] == "blocked_substrate"
    assert fresh_proposal["blocked_note"] == "velocity readout not built"


def test_manual_proposal_without_backlog_id_still_survives_single_cycle_fallback():
    """Defense-in-depth: even if a manual item somehow skips minting (a
    malformed entry, or a doc that bypassed _mint_missing_manual_backlog_ids),
    the proposal_id-only fallback still works for a SINGLE regen cycle in
    isolation -- this was never actually broken (proposal_id is stable for a
    manual item that nothing rewrites). The exposure the fix closes is the
    missing code-enforced guarantee AND the transition case above, not a
    demonstrated single-cycle failure; this test pins that the fallback path
    itself keeps working when neither side ever gets a backlog_id."""
    old_proposal = {
        "proposal_id": "EXP-0384", "status": "executed", "executed_by": "V3-EXQ-872",
    }
    fresh_proposal = {"proposal_id": "EXP-0384", "status": "proposed"}

    existing_status_by_key = _index_by_all_keys(
        old_proposal, ("status", "executed_by")
    )
    matched = _carry_forward(fresh_proposal, existing_status_by_key)
    assert matched is True
    assert fresh_proposal["status"] == "executed"


def test_old_record_not_duplicated_when_fresh_item_matches_via_either_key():
    """Regression for the exact duplicate-row shape observed empirically: the
    "preserve historical resolution records" re-append must recognise a fresh
    item as already covering an old record when EITHER key matches, not just
    the fresh item's preferred one -- otherwise the old (correctly-resolved)
    record gets re-appended as a second, redundant row alongside the fresh
    (freshly-reset-to-"proposed") one. Mirrors main()'s _regenerated_bids
    membership check (site 3.5)."""
    old_record = {"proposal_id": "EXP-0384", "status": "executed"}
    fresh_item = {"proposal_id": "EXP-0384", "backlog_id": "EVB-0490", "status": "proposed"}

    regenerated_keys = set(b._proposal_identity_keys(fresh_item))
    old_keys = b._proposal_identity_keys(old_record)
    already_covered = any(k in regenerated_keys for k in old_keys)

    assert already_covered is True  # matched via the shared "EXP-0384" key


# --- ERROR-as-PASS miscategorization (2026-08-02) --------------------------
#
# Regression cover for the confirmed V3-EXQ-870 defect: a crash-before-manifest
# / synthetic runner ERROR record (manifest_status="ERROR", claim_ids=[]) was
# indexed into claim_evidence.v1.json's unlinked_runs with status="PASS" --
# RunRecord.final_status defaults to "PASS" and _evaluate_runs only ever set it
# to "FAIL", never propagating ERROR/UNKNOWN through. generate_pending_review.py
# then listed the crash under "PASS (verify & close)" instead of routing it to
# /diagnose-errors. The fix has two parts, tested separately below: (1)
# _evaluate_runs must set final_status to the manifest's own ERROR/UNKNOWN
# value rather than defaulting past it, and (2) an ERROR/UNKNOWN-status
# unlinked run must not be written into claim_evidence at all, matching
# generate_pending_review.load_error_manifests()'s documented assumption that
# such records are "never indexed" (which is what lets it read them straight
# off the raw on-disk manifest and route them to /diagnose-errors).

def _run_record(run_id="run1", manifest_status="PASS", claim_ids_tested=None,
                 experiment_type="exp_type_1"):
    return b.RunRecord(
        experiment_type=experiment_type,
        run_id=run_id,
        timestamp_raw="2026-08-02T10:50:35Z",
        timestamp=datetime(2026, 8, 2, 10, 50, 35, tzinfo=timezone.utc),
        manifest_path=Path(f"/tmp/{run_id}/manifest.json"),
        metrics_path=Path(f"/tmp/{run_id}/metrics.json"),
        summary_path=Path(f"/tmp/{run_id}/summary.md"),
        manifest_status=manifest_status,
        claim_ids_tested=claim_ids_tested or [],
    )


def test_evaluate_runs_error_status_propagates_not_defaulted_to_pass():
    """The core defect: manifest_status=ERROR must not collapse to final_status
    PASS just because it isn't literally FAIL."""
    run = _run_record(manifest_status="ERROR")
    b._evaluate_runs([run], {})
    assert run.final_status == "ERROR"


def test_evaluate_runs_unknown_status_propagates_not_defaulted_to_pass():
    run = _run_record(manifest_status="UNKNOWN")
    b._evaluate_runs([run], {})
    assert run.final_status == "UNKNOWN"


def test_evaluate_runs_fail_still_wins_over_manifest_status():
    """Sanity: ordinary FAIL behavior is unchanged by the ERROR/UNKNOWN branch."""
    run = _run_record(manifest_status="FAIL")
    b._evaluate_runs([run], {})
    assert run.final_status == "FAIL"


def test_evaluate_runs_criteria_fail_wins_over_error_manifest_status():
    """Defensive: if a run somehow carries both fail_if-triggering metrics AND
    manifest_status=ERROR, FAIL must still take precedence (this should not
    happen in practice -- a crash produces no metrics -- but final_status must
    never silently prefer ERROR over a genuine criteria failure)."""
    run = _run_record(manifest_status="ERROR")
    run.metrics = {"some_metric": 10.0}
    b._evaluate_runs([run], {"fail_if": [{"metric": "some_metric", "op": ">", "threshold": 5.0}]})
    assert run.final_status == "FAIL"


def test_write_claim_evidence_matrix_excludes_error_class_unlinked_run():
    """An ERROR-class run tagging no claims must not appear anywhere in
    claim_evidence.v1.json -- indexing it (even with the correct "ERROR" status)
    makes load_error_manifests() skip the run_id as already-indexed, so the
    crash vanishes from pending_review.md entirely instead of routing to
    /diagnose-errors."""
    run = _run_record(run_id="crash_run", manifest_status="ERROR")
    b._evaluate_runs([run], {})
    assert run.final_status == "ERROR"

    with tempfile.TemporaryDirectory() as td:
        matrix = b._write_claim_evidence_matrix(
            Path(td), {"exp_type_1": [run]}, {}, "2026-08-02T00:00:00Z")

    unlinked_ids = {e["run_id"] for e in matrix["unlinked_runs"]}
    entry_ids = {e["run_id"] for e in matrix["entries"]}
    assert "crash_run" not in unlinked_ids
    assert "crash_run" not in entry_ids


def test_write_claim_evidence_matrix_still_includes_pass_class_unlinked_run():
    """Regression guard against over-correcting: a legitimate PASS/FAIL run
    that tags no claims (e.g. a substrate-readiness diagnostic) must still be
    indexed in unlinked_runs -- only ERROR/UNKNOWN-status runs are excluded."""
    run = _run_record(run_id="readiness_probe", manifest_status="PASS")
    b._evaluate_runs([run], {})
    assert run.final_status == "PASS"

    with tempfile.TemporaryDirectory() as td:
        matrix = b._write_claim_evidence_matrix(
            Path(td), {"exp_type_1": [run]}, {}, "2026-08-02T00:00:00Z")

    unlinked = {e["run_id"]: e for e in matrix["unlinked_runs"]}
    assert "readiness_probe" in unlinked
    assert unlinked["readiness_probe"]["status"] == "PASS"


# --- non-standard status rendered as PASS in INDEX.md (2026-08-08) ---------
#
# Sibling defect to the ERROR-as-PASS block above, one status class further out.
# _evaluate_runs branches on FAIL and on ERROR/UNKNOWN, so every OTHER manifest
# status string lands in its terminal `else` and becomes final_status="PASS".
# The INDEX.md tables printed final_status directly, so a run whose manifest
# says PARTIAL_NO_CANCEL / INCONCLUSIVE / MIXED / SUPERSEDED rendered as a clean
# pass. Confirmed 2026-08-08 on
# v3_exq_162_mech137_commit_token_structure_9e3b4eaa_v3 (PARTIAL_NO_CANCEL shown
# as PASS); 34 of the corpus's 37 non-standard-status runs were affected.
#
# The fix is display-only: _display_status() falls back to the manifest's own
# status string when final_status is a fallthrough "PASS". final_status itself is
# deliberately NOT widened -- it feeds scoring / evidence-direction inference /
# claim_evidence.v1.json, where reclassifying those runs is a governance change.
# The tests below pin both halves: the string is shown, AND final_status stays
# "PASS" so nothing downstream moves.

def test_display_status_shows_partial_status_not_pass():
    run = _run_record(manifest_status="PARTIAL_NO_CANCEL")
    b._evaluate_runs([run], {})
    assert run.final_status == "PASS", "final_status semantics must be unchanged"
    assert b._display_status(run) == "PARTIAL_NO_CANCEL"


def test_display_status_shows_other_non_standard_statuses():
    for status in ("INCONCLUSIVE", "INCONCLUSIVE_UNDERTRAINED", "MIXED",
                   "SUPERSEDED", "DIAGNOSTIC_COMPLETE", "N/A",
                   "PARTIAL_COLLAPSE_ADEQUATE"):
        run = _run_record(manifest_status=status)
        b._evaluate_runs([run], {})
        assert b._display_status(run) == status, status


def test_display_status_leaves_standard_statuses_exactly_as_before():
    """Negative control: PASS/ERROR/UNKNOWN render unchanged, FAIL stays bold."""
    for status, expected in (("PASS", "PASS"), ("ERROR", "ERROR"),
                             ("UNKNOWN", "UNKNOWN"), ("FAIL", "**FAIL**")):
        run = _run_record(manifest_status=status)
        b._evaluate_runs([run], {})
        assert b._display_status(run) == expected, status


def test_display_status_derived_fail_wins_over_non_standard_manifest_status():
    """A stop-criteria hit still renders **FAIL** even when the manifest carries
    a non-standard status -- the derived verdict is not discarded in favour of
    the raw string."""
    run = _run_record(manifest_status="INCONCLUSIVE")
    run.metrics = {"some_metric": 10.0}
    b._evaluate_runs([run], {"fail_if": [{"metric": "some_metric", "op": ">",
                                          "threshold": 5.0}]})
    assert run.final_status == "FAIL"
    assert b._display_status(run) == "**FAIL**"


def _index_status_cell(index_md, key, col):
    """The status cell of the INDEX.md row matching `key`.

    `col` is 1-based over the table's own columns -- the per-experiment table is
    `| run_id | timestamp | status | ...` (col 3) and the top-level one is
    `| experiment_type | latest status | ...` (col 2).
    """
    for line in index_md.splitlines():
        if line.startswith("|") and key in line:
            cells = [c.strip() for c in line.split("|")]
            return cells[col] if len(cells) > col else None
    return None


def test_experiment_index_table_renders_partial_status_end_to_end():
    """End-to-end through the real INDEX.md writer, not just the helper."""
    with tempfile.TemporaryDirectory() as td:
        exp_dir = Path(td) / "v3_exq_000_partial"
        run_dir = exp_dir / "runs" / "run_partial_v3"
        run_dir.mkdir(parents=True)
        for name in ("manifest.json", "metrics.json", "summary.md"):
            (run_dir / name).write_text("{}", encoding="utf-8")

        run = b.RunRecord(
            experiment_type="v3_exq_000_partial",
            run_id="run_partial_v3",
            timestamp_raw="2026-08-08T10:00:00Z",
            timestamp=datetime(2026, 8, 8, 10, 0, 0, tzinfo=timezone.utc),
            manifest_path=run_dir / "manifest.json",
            metrics_path=run_dir / "metrics.json",
            summary_path=run_dir / "summary.md",
            manifest_status="PARTIAL_NO_CANCEL",
        )
        b._evaluate_runs([run], {})
        b._write_experiment_index(exp_dir, "v3_exq_000_partial", [run], [],
                                  "2026-08-08T10:00:00Z")

        text = (exp_dir / "INDEX.md").read_text(encoding="utf-8")

    cell = _index_status_cell(text, "run_partial_v3", 3)
    assert cell == "PARTIAL_NO_CANCEL", f"INDEX.md status cell was {cell!r}"
    assert "PASS" not in text, "the collapsed PASS must not appear anywhere"


def test_top_level_index_latest_status_renders_partial_status():
    with tempfile.TemporaryDirectory() as td:
        run = _run_record(run_id="run_partial_v3",
                          manifest_status="PARTIAL_NO_CANCEL",
                          experiment_type="v3_exq_000_partial")
        b._evaluate_runs([run], {})
        b._write_top_level_index(Path(td), {"v3_exq_000_partial": [run]}, {},
                                 0, 0, 0, 0, "2026-08-08T10:00:00Z")
        text = (Path(td) / "INDEX.md").read_text(encoding="utf-8")

    cell = _index_status_cell(text, "v3_exq_000_partial", 2)
    assert cell == "PARTIAL_NO_CANCEL", f"top-level status cell was {cell!r}"


# ---------------------------------------------------------------------------
# criteria_non_degenerate{} <-> criteria[] join, THIRD sub-case (V3-EXQ-906).
#
# A broad-report/narrow-gate driver reports every monitored channel's
# non-degeneracy in criteria_non_degenerate{} but gates PASS on a SUBSET via one
# AGGREGATE criterion, so the excess keys have no criteria[] entry at all -- by
# design, not by the spelling slip of 783 or the direction reversal of 830. The
# unmatched False values used to trip a spurious vacuous_pass.
# Regression target: failure_autopsy_V3-EXQ-906_2026-08-09.md.
# ---------------------------------------------------------------------------

def _fishtank(core_passed=True, load_bearing=True, vigor=False):
    """The real V3-EXQ-906 declaration shape, reduced to what the join reads."""
    return {
        "label": "full_stack_observational_showcase_live",
        "preconditions": [{"name": "harm_pathway_trained", "kind": "readiness",
                           "measured": 3794.0, "threshold": 1.0, "met": True}],
        "criteria_non_degenerate": {
            "channel_z_harm_a": True, "channel_drive": True,
            "channel_z_goal": True, "channel_vigor": vigor,
            "channel_z_block": False, "harm_pathway_trained": True,
        },
        "criteria": [
            {"name": "core_channels_non_degenerate",
             "load_bearing": load_bearing, "passed": core_passed},
            {"name": "harm_pathway_trained", "load_bearing": True, "passed": True},
        ],
    }


def test_unmatched_key_outside_a_cleared_aggregate_is_not_vacuous():
    """THE FIX. channel_vigor/channel_z_block have zero criteria[] candidates,
    but a load-bearing `core_channels_non_degenerate` aggregate cleared."""
    _, flag = b._compute_adjudication(_fishtank(), "PASS", "diagnostic")
    assert flag == "verified", flag


def test_degenerate_gated_subset_still_flags_via_the_aggregate():
    """SAFETY. If the AGGREGATE's own scope goes degenerate the author reports
    passed:false on it, and (3b) fires before the legacy join is reached."""
    _, flag = b._compute_adjudication(_fishtank(core_passed=False),
                                      "PASS", "diagnostic")
    assert flag == "vacuous_pass", flag


def test_aggregate_must_be_load_bearing_to_licence_the_exclusion():
    """A non-load-bearing aggregate is not a gate declaration, so unmatched
    keys keep the conservative resolve-toward-flagging default."""
    _, flag = b._compute_adjudication(_fishtank(load_bearing=False),
                                      "PASS", "diagnostic")
    assert flag == "vacuous_pass", flag


def test_no_aggregate_means_unmatched_keys_still_flag():
    """NEGATIVE CONTROL -- the V3-EXQ-859/863 shape: unmatched False keys and a
    lone non-aggregate criterion. The blanket 'criteria[] present => unmatched
    is informational' rule cleared these; this one must not."""
    interp = {"label": "abl",
              "criteria_non_degenerate": {"mech448_ablation_discriminates": False,
                                          "mech449_ablation_discriminates": False},
              "criteria": [{"name": "sample_adequate",
                            "load_bearing": True, "passed": True}]}
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "vacuous_pass", flag


def test_matched_load_bearing_key_still_flags_even_beside_an_aggregate():
    """The exclusion is scoped to UNMATCHED keys. A key that DOES join to a
    load-bearing criterion is unaffected by a sibling aggregate."""
    interp = _fishtank()
    interp["criteria_non_degenerate"]["harm_pathway_trained"] = False
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "vacuous_pass", flag


def test_783_and_830_exclusions_are_unchanged_without_an_aggregate():
    """The two prior fixes keep working: exact-name load_bearing:false (783)
    and the prefix-tolerant short-key/long-name join (830)."""
    i783 = {"label": "x",
            "criteria_non_degenerate": {"C1_cr_crossing": True,
                                        "C2_event_selectivity": False},
            "criteria": [{"name": "C1_cr_crossing", "load_bearing": True,
                          "passed": True},
                         {"name": "C2_event_selectivity", "load_bearing": False,
                          "passed": False}]}
    assert b._compute_adjudication(i783, "PASS", "diagnostic")[1] == "verified"
    i830 = {"label": "x",
            "criteria_non_degenerate": {"C_DECIDABLE": True, "C_DISSOCIABLE": False},
            "criteria": [{"name": "C_DECIDABLE_instrument_returned_a_reading",
                          "load_bearing": True, "passed": True},
                         {"name": "C_DISSOCIABLE_low_cofire_distinct_positions",
                          "load_bearing": False, "passed": False}]}
    assert b._compute_adjudication(i830, "PASS", "diagnostic")[1] == "verified"


def test_aggregate_does_not_rescue_a_declaration_that_declares_nothing():
    """An empty criteria_non_degenerate{} with no preconditions is still
    `unverified` -- the exclusion filters the vacuity check, it does not
    fabricate a declaration."""
    interp = {"label": "x", "criteria_non_degenerate": {},
              "criteria": [{"name": "core_channels_non_degenerate",
                            "load_bearing": True, "passed": True}]}
    _, flag = b._compute_adjudication(interp, "PASS", "diagnostic")
    assert flag == "unverified", flag


def test_branch_selector_exclusion_survives_the_aggregate_path():
    """NEGATIVE CONTROL for the 648a/649 class: a `_branch` selector False is
    still excluded, with or without an aggregate in play."""
    interp = _fishtank()
    interp["criteria_non_degenerate"]["diffuse_branch"] = False
    assert b._compute_adjudication(interp, "PASS", "diagnostic")[1] == "verified"


def test_aggregate_exclusion_does_not_apply_to_a_non_pass():
    """A FAIL was never vacuous_pass; the exclusion must not change that."""
    _, flag = b._compute_adjudication(_fishtank(), "FAIL", "diagnostic")
    assert flag == "verified", flag


def _run_all():
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {fn.__name__}: {e}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
