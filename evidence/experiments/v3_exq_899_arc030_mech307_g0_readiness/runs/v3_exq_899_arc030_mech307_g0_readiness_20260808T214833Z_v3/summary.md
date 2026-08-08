# V3-EXQ-899 -- ARC-030 / MECH-307 G0-readiness diagnostic

**Status:** FAIL  **Label:** readiness_fail_curriculum_gate_blocks_retest
**Purpose:** diagnostic (claim_ids=[]; gates ARC-030/Q-021/INV-034)
**Readiness check of:** V3-EXQ-866a

## Readiness gate

| Item | Frac seeds | Pass |
|---|---|---|
| P1 curriculum_reached_p2 | 1.00 | True |
| P2 p2_window_admits_contact | 0.67 | True |
| **G0_ON (load-bearing)** | 0.00 | False |
| G0_OFF (reproduction, non-gating) | 0.00 | False |

## MECH-307 A/B (non-gating diagnostics)

| Metric | FULL_M307_ON | FULL_M307_OFF | RANDOM |
|---|---|---|---|
| resource_visit_rate (mean) | 0.0040 | 0.0039 | 0.0116 |
| zgoal_norm (mean; C6 floor 0.4) | 0.1645 | 0.1597 | -- |

d_resource_visit_rate (ON-OFF) = 0.0001; d_zgoal (ON-OFF) = 0.0049; mech307_perturbs_baseline = False

## Interpretation

READINESS FAIL (informative, NOT a claim verdict): with MECH-307 genuinely ON, the FULL arm still does not clear the RANDOM baseline by >= 0.05 on >= 2/3 seeds (G0_ON), on a live/discriminating P2 window. MECH-307 reachability alone does not restore the G0 gate -- consistent with the still-open curriculum gap (z_goal starved before P2). Route to the substrate_queue stub `scaffolded-curriculum-hazard-rebalance` FIRST, then re-run this readiness gate; do NOT force through to the discriminative retest. mech307_perturbs_baseline=FALSE: the OFF arm also fails G0, so this is the pre-existing curriculum gap (866a reproduced), not a MECH-307 regression.
