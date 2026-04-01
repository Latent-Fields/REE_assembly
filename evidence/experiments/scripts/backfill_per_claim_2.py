#!/usr/bin/env python3
"""Backfill evidence_direction_per_claim for 2-claim experiments.

One-shot script. For most 2-claim experiments, both claims are co-tested
by the same criteria so the blanket evidence_direction applies to both.
Five experiments have asymmetric per-claim directions (confirmed by
reading summaries).

Only touches manifests that:
  - Have exactly 2 claim_ids_tested
  - Have experiment_purpose == "evidence" (or missing = default evidence)
  - Do NOT already have evidence_direction_per_claim populated
"""
import json
import glob
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # evidence/experiments/

# ---- Asymmetric overrides ----
# Keyed on (experiment_type, frozenset(claims)) -> per-claim dict
# These 5 experiments have different directions per claim (all confirmed
# by reading summary.md criteria pass/fail breakdowns).
ASYMMETRIC = {
    # EXQ-087: SD-003 causal signal detected (C1/C2 PASS) but HarmBridge
    # alignment R^2=0.0 (C3/C5 FAIL) -> SD-010 architecture fails
    ("v3_exq_087_harm_bridge_validation", frozenset(["SD-003", "SD-010"])):
        {"SD-003": "supports", "SD-010": "weakens"},

    # EXQ-183: benefit_ratio=1.21x passes (MECH-112) but benefit_eval_auc=0.54
    # fails (ARC-030 shared selector can't discriminate)
    ("v3_exq_183_arc030_shared_selector_payoff", frozenset(["ARC-030", "MECH-112"])):
        {"MECH-112": "supports", "ARC-030": "weakens"},

    # EXQ-185: proximity repr is solid (r^2=0.921, MECH-112) but proximity
    # gradient does not drive navigation (benefit_ratio=0.21x, SD-015 fails)
    ("v3_exq_185_direct_prox_argmax", frozenset(["MECH-112", "SD-015"])):
        {"MECH-112": "supports", "SD-015": "weakens"},

    # EXQ-006: z_world encodes spatial position (R^2=0.800, SD-003 C2/C3 PASS)
    # but drops hazard proximity (test_acc=0.693 < 0.70, SD-005 C1 FAIL)
    ("claim_probe_sd_003", frozenset(["SD-003", "SD-005"])):
        {"SD-003": "supports", "SD-005": "weakens"},

    # EXQ-011: z_self/z_world separation intact (agent_env_gap=0.00035, SD-005
    # C2 PASS) but TPJ mismatch signal too weak (harm_safe_gap=0.0047, MECH-095
    # C1 FAIL)
    ("claim_probe_mech_095", frozenset(["MECH-095", "SD-005"])):
        {"MECH-095": "weakens", "SD-005": "supports"},
}


def main():
    manifests = sorted(glob.glob(str(BASE / "*/runs/*/manifest.json")))
    updated = 0
    skipped_has_perclaim = 0
    skipped_wrong_count = 0
    skipped_not_evidence = 0
    asymmetric_applied = 0

    for mp in manifests:
        with open(mp) as f:
            m = json.load(f)

        cids = m.get("claim_ids_tested", [])
        if len(cids) != 2:
            skipped_wrong_count += 1
            continue

        purpose = m.get("experiment_purpose", "evidence")
        if purpose != "evidence":
            skipped_not_evidence += 1
            continue

        if m.get("evidence_direction_per_claim"):
            skipped_has_perclaim += 1
            continue

        etype = m.get("experiment_type", "")
        direction = m.get("evidence_direction", "")
        claim_set = frozenset(cids)

        # Check for asymmetric override
        key = (etype, claim_set)
        if key in ASYMMETRIC:
            per_claim = ASYMMETRIC[key]
            asymmetric_applied += 1
        else:
            # Default: blanket direction applies to both claims
            per_claim = {cid: direction for cid in cids}

        m["evidence_direction_per_claim"] = per_claim
        with open(mp, "w") as f:
            json.dump(m, f, indent=2)
            f.write("\n")

        run_id = m.get("run_id", "?")
        marker = " [ASYMMETRIC]" if key in ASYMMETRIC else ""
        print(f"  Updated {run_id}: {per_claim}{marker}")
        updated += 1

    print(f"\n=== Summary ===")
    print(f"Updated: {updated} ({asymmetric_applied} asymmetric)")
    print(f"Skipped (already has per-claim): {skipped_has_perclaim}")
    print(f"Skipped (not 2 claims): {skipped_wrong_count}")
    print(f"Skipped (not evidence): {skipped_not_evidence}")


if __name__ == "__main__":
    main()
