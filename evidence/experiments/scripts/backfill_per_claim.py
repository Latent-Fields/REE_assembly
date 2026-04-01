#!/usr/bin/env python3
"""Backfill evidence_direction_per_claim for 3+ claim experiments.

One-shot script. Reads each manifest, applies per-claim directions based on
analysis of criteria pass/fail mapping, writes updated manifest back.

Only touches manifests that:
  - Have 3+ claim_ids_tested
  - Have experiment_purpose == "evidence" (or missing = default evidence)
  - Do NOT already have evidence_direction_per_claim populated
"""
import json
import glob
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # evidence/experiments/

# ---- Per-claim direction rules ----
# Key = experiment_type prefix (matched with startswith)
# Value = dict of claim_id -> direction
# Special value "__default__" used for claims not explicitly listed

# PASS experiments: all criteria pass -> confirm supports for all claims
ALL_SUPPORTS = {"__default__": "supports"}

# Catastrophic FAIL: all criteria fail -> confirm weakens for all claims
ALL_WEAKENS = {"__default__": "weakens"}

# Mixed: confirm mixed for all (honest about uncertainty)
ALL_MIXED = {"__default__": "mixed"}

RULES = {
    # === PASS experiments where all criteria genuinely support all claims ===
    # EXQ-029: proxy gradient world (PASS) - all 4 criteria map to all claims
    "v3_exq_029_sd003_proxy_gradient_world": {
        "__status_filter__": "PASS",
        "SD-003": "supports", "SD-007": "supports",
        "ARC-024": "supports", "MECH-071": "supports",
    },
    # EXQ-034: engine ablation (PASS) - E3+E2 both load-bearing
    "v3_exq_034_arc025_engine_ablation": {
        "__status_filter__": "PASS",
        "ARC-025": "supports", "SD-003": "supports", "MECH-071": "supports",
    },
    # EXQ-042: hippocampal terrain (PASS) - terrain_prior, hippo quality, E3 cal all pass
    "v3_exq_042_hippocampal_terrain_training": {
        # PASS runs get supports; FAIL runs get weakens (catastrophic 0/5)
        "__status_filter__": "PASS",
        "SD-004": "supports", "ARC-007": "supports", "MECH-089": "supports",
    },
    # EXQ-057: reafference isolation (PASS)
    "v3_exq_057_sd010_reafference_isolation": {
        "__status_filter__": "PASS",
        "SD-010": "supports", "SD-007": "supports", "MECH-101": "supports",
    },
    # EXQ-058_arc027: harm stream calibration (PASS)
    "v3_exq_058_arc027_harm_stream_calibration": {
        "__status_filter__": "PASS",
        "ARC-027": "supports", "SD-010": "supports", "MECH-071": "supports",
    },
    # EXQ-032b: ttype escalation (PASS) - all escalation criteria pass
    "v3_exq_032b_mech102_ttype_escalation": {
        "__status_filter__": "PASS",
        "MECH-102": "supports", "ARC-024": "supports", "SD-003": "supports",
    },
    # EXQ-041: full pipeline smoke test (PASS)
    "v3_exq_041_full_pipeline_smoke_test": {
        "__status_filter__": "PASS",
        "ARC-016": "supports", "MECH-071": "supports", "MECH-089": "supports",
    },
    # EXQ-096a: full integration benchmark (PASS) - each criterion maps to specific claim
    "v3_exq_096a_full_integration_benchmark": {
        "__status_filter__": "PASS",
        "SD-005": "supports", "ARC-016": "supports", "MECH-090": "supports",
        "SD-006": "supports", "ARC-007": "supports", "MECH-089": "supports",
        "MECH-093": "supports",
    },
    # EXQ-026 (PASS runs): harm eval works
    "v3_exq_026_mech071_v3": {
        "__status_filter__": "PASS",
        "MECH-071": "supports", "SD-003": "supports", "SD-005": "supports",
    },

    # === Claim probe PASS experiments ===
    "claim_probe_arc_025": {
        "__status_filter__": "PASS",
        "ARC-025": "supports", "SD-003": "supports", "MECH-071": "supports",
    },
    "claim_probe_mech_089": {
        "__status_filter__": "PASS",
        "MECH-089": "supports", "ARC-016": "supports", "MECH-071": "supports",
    },
    "claim_probe_sd_004": {
        "__status_filter__": "PASS",
        "__default__": "supports",
    },

    # === DIFFERENTIATED: some claims pass, others fail ===
    # EXQ-023: SD-008 event selectivity passes, all others fail
    "claim_probe_sd_008": {
        "SD-008": "supports", "SD-003": "weakens",
        "MECH-098": "weakens", "ARC-016": "weakens",
    },

    # EXQ-027: SD-007 reafference R2 passes, MECH-071 harm_pred_std passes,
    # SD-003 calibration_gap fails
    "v3_exq_027_sd003_v3_reafference": {
        "SD-003": "weakens", "SD-007": "supports",
        "MECH-071": "supports", "MECH-098": "mixed",
    },

    # SD-003 attribution family (FAIL): SD-003 criteria fail,
    # ARC-024/MECH-071 are secondary tags not directly tested
    "v3_exq_030_sd003_full_attribution": {
        "__status_filter__": "FAIL",
        "SD-003": "weakens", "ARC-024": "mixed", "MECH-071": "mixed",
    },
    "v3_exq_030b_sd003_full_attribution_v2": {
        "__status_filter__": "FAIL",
        "SD-003": "weakens", "ARC-024": "mixed", "MECH-071": "mixed",
    },
    "v3_exq_030c_sd003_attribution_largescale": {
        "__status_filter__": "FAIL",
        "SD-003": "weakens", "ARC-024": "mixed", "MECH-071": "mixed",
    },
    "v3_exq_036_sd003_multistep_attribution": {
        "__status_filter__": "FAIL",
        "SD-003": "weakens", "ARC-024": "mixed", "MECH-071": "mixed",
    },
    "v3_exq_071_rollout_batched_attribution": {
        "__status_filter__": "FAIL",
        "SD-003": "weakens", "ARC-024": "mixed", "MECH-071": "mixed",
    },

    # EXQ-032/032c: MECH-102 energy escalation fails (design issue: policy too effective)
    "v3_exq_032_mech102_energy_escalation": {
        "__status_filter__": "FAIL",
        "MECH-102": "weakens", "ARC-024": "mixed", "SD-003": "mixed",
    },
    "v3_exq_032c_mech102_dense_grid": {
        "__status_filter__": "FAIL",
        "MECH-102": "weakens", "ARC-024": "mixed", "SD-003": "mixed",
    },

    # EXQ-017: combined lateral+reafference - all criteria failed
    "claim_probe_mech_099": {
        "__status_filter__": "FAIL",
        "MECH-099": "weakens", "MECH-098": "weakens",
        "SD-007": "weakens", "SD-003": "weakens",
    },

    # EXQ-100/claim_probe_mech_100: event contrastive - selectivity PASS but calibration FAIL
    "claim_probe_mech_100": {
        "__status_filter__": "FAIL",
        "MECH-100": "supports", "SD-009": "supports", "SD-003": "weakens",
    },

    # EXQ-095: harm forward model - all relevant criteria failed
    "v3_exq_095_harm_forward_model_sd003": {
        "__status_filter__": "FAIL",
        "ARC-033": "weakens", "SD-011": "weakens", "SD-003": "weakens",
    },

    # EXQ-145 second run (inconclusive): phase 1 gate failure, no criteria ran
    "v3_exq_145_sd008_sd007_sd003_integration": {
        "SD-008": "unknown", "SD-007": "unknown", "SD-003": "unknown",
    },

    # claim_probe_arc_024: 4/5 pass but core C4 failed
    "claim_probe_arc_024": {
        "__status_filter__": "FAIL",
        "ARC-024": "mixed", "MECH-071": "mixed", "INV-029": "mixed",
    },

    # claim_probe_sd_007 (FAIL): all criteria failed
    "claim_probe_sd_007": {
        "__status_filter__": "FAIL",
        "__default__": "weakens",
    },

    # claim_probe_sd_003 (FAIL): attribution collapsed
    "claim_probe_sd_003": {
        "__status_filter__": "FAIL",
        "__default__": "weakens",
    },

    # claim_probe_mech_102 (PASS): all pass
    "claim_probe_mech_102": {
        "__status_filter__": "PASS",
        "MECH-102": "supports", "ARC-024": "supports", "SD-003": "supports",
    },

    # claim_probe_mech_071 3-claim (PASS)
    "claim_probe_mech_071": {
        "__status_filter__": "PASS",
        "MECH-071": "supports", "SD-003": "supports", "SD-005": "supports",
    },

    # runtime_authority_commit_boundary (PASS): all 7 claims
    "runtime_authority_commit_boundary": {
        "__status_filter__": "PASS",
        "__default__": "supports",
    },
}

# For experiments with FAIL runs that match a PASS-only rule, apply these FAIL defaults
FAIL_DEFAULTS = {
    "v3_exq_042_hippocampal_terrain_training": {"__default__": "weakens"},
    "v3_exq_026_mech071_v3": {"__default__": "weakens"},
    "v3_exq_029_sd003_proxy_gradient_world": {"__default__": "weakens"},
    "claim_probe_mech_102": {"__default__": "weakens"},
    "claim_probe_mech_071": {"__default__": "weakens"},
    "runtime_authority_commit_boundary": {"__default__": "weakens"},
    "claim_probe_sd_004": {"__default__": "weakens"},
}


def get_per_claim(rule, claim_ids):
    """Build per-claim dict from rule + claim list."""
    result = {}
    default = rule.get("__default__")
    for cid in claim_ids:
        if cid in rule:
            result[cid] = rule[cid]
        elif default:
            result[cid] = default
    return result


def main():
    manifests = sorted(glob.glob(str(BASE / "*/runs/*/manifest.json")))
    updated = 0
    skipped_has_perclaim = 0
    skipped_few_claims = 0
    skipped_not_evidence = 0
    skipped_no_rule = 0

    no_rule_types = set()

    for mp in manifests:
        with open(mp) as f:
            m = json.load(f)

        cids = m.get("claim_ids_tested", [])
        if len(cids) < 3:
            skipped_few_claims += 1
            continue

        purpose = m.get("experiment_purpose", "evidence")
        if purpose != "evidence":
            skipped_not_evidence += 1
            continue

        existing = m.get("evidence_direction_per_claim", {})
        if existing:
            skipped_has_perclaim += 1
            continue

        etype = m.get("experiment_type", "")
        status = m.get("status", "UNKNOWN").upper()

        # Find matching rule
        rule = None
        for prefix, r in RULES.items():
            if etype.startswith(prefix) or etype == prefix:
                status_filter = r.get("__status_filter__")
                if status_filter and status != status_filter:
                    # Check FAIL defaults
                    if status == "FAIL" and prefix in FAIL_DEFAULTS:
                        rule = FAIL_DEFAULTS[prefix]
                    elif status == "PASS" and not status_filter:
                        rule = r
                    continue
                rule = r
                break

        if rule is None:
            # Try FAIL defaults
            for prefix, r in FAIL_DEFAULTS.items():
                if etype.startswith(prefix) or etype == prefix:
                    if status == "FAIL":
                        rule = r
                        break

        if rule is None:
            no_rule_types.add(f"{etype} ({status})")
            skipped_no_rule += 1
            continue

        per_claim = get_per_claim(rule, cids)
        if not per_claim:
            skipped_no_rule += 1
            continue

        m["evidence_direction_per_claim"] = per_claim
        with open(mp, "w") as f:
            json.dump(m, f, indent=2)
            f.write("\n")

        run_id = m.get("run_id", "?")
        print(f"  Updated {run_id}: {per_claim}")
        updated += 1

    print(f"\n=== Summary ===")
    print(f"Updated: {updated}")
    print(f"Skipped (already has per-claim): {skipped_has_perclaim}")
    print(f"Skipped (<3 claims): {skipped_few_claims}")
    print(f"Skipped (not evidence): {skipped_not_evidence}")
    print(f"Skipped (no rule): {skipped_no_rule}")
    if no_rule_types:
        print(f"\nNo rule for:")
        for t in sorted(no_rule_types):
            print(f"  {t}")


if __name__ == "__main__":
    main()
