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
import os
import sys

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


def test_real_legacy_150_series_not_flipped():
    """Regression guard: the v3_exq_150-series has an ANNOTATED pack
    (supersession note) and a STALE unannotated flat. The overlay must NOT
    fire, so the pack's `superseded`/`inconclusive` exclusion is preserved."""
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
        checked += 1
        flat = json.loads(flat_p.read_text(encoding="utf-8"))
        pack = json.loads(packs[0].read_text(encoding="utf-8"))
        assert b._is_annotated(pack), rid          # pack has the note
        assert not b._is_annotated(flat), rid       # flat is stale
        merged, _, applied = b._merge_flat_manifest_overrides(pack, flat)
        assert applied is False, rid
        assert merged.get("evidence_direction") == pack.get("evidence_direction"), rid
    assert checked >= 1, "expected at least one legacy 150-series pair present"


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
