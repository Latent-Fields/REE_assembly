# V3-EXQ-043 — SD-003 Trajectory Attribution

**Status:** FAIL
**Claims:** SD-003, MECH-102
**World:** CausalGridWorldV2 (body=12, world=250)
**alpha_world:** 0.9 (SD-008)  |  **Seed:** 0
**Prerequisites:** EXQ-041 PASS, EXQ-042 PASS (full pipeline + terrain_prior trained)

## SD-003 Redesign: Trajectory Attribution

Prior SD-003 tests (EXQ-030b, 036) computed causal signatures as:
  `E3(E2(z_world, a_actual)) − E3(E2(z_world, a_cf))`
This produced weak signals (causal_sig ≈ 0.003) because:
  1. Single-step E2 predictions are nearly identical for all actions
  2. Training E3 on E2-predicted states (Fix2) causes sign inversion

This experiment implements SD-003 as terrain attribution:
  `causal_sig = mean(E3_score(cf_trajectories)) − E3_score(selected_trajectory)`

- N=16 hippocampal candidates generated from theta-averaged z_world
- E3 scores all N via J(ζ) = F(ζ) + λM(ζ) + ρΦ_R(ζ)
- Selected trajectory = lowest J(ζ) (agent's actual terrain path)
- Counterfactuals = all other terrain paths
- causal_sig > 0 means the agent's terrain navigation was meaningfully better

Near hazards, terrain paths diverge more (some paths enter residue-heavy regions,
others avoid them), so causal_sig should be elevated at approach and contact.

## Attribution Results by Transition Type

| Transition Type | causal_sig | n |
|---|---|---|
| none | 0.5257 | 5 |
| approach | 0.6184 | 5 |
| contact | 0.0000 | 0 |

approach − none gap: 0.0927
contact − approach gap: -0.6184

## E3 Calibration (required for meaningful scores)

| Type | mean harm_eval |
|---|---|
| none | 0.4794 |
| approach | 0.4793 |
calibration_gap_approach: -0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_approach > causal_sig_none | PASS | 0.6184 vs 0.5257 |
| C2: causal_sig_contact > causal_sig_approach (MECH-102) | FAIL | 0.0000 vs 0.6184 |
| C3: causal_sig_approach > 0.001 | PASS | 0.6184 |
| C4: cal_gap_approach > 0.03 (E3 calibrated) | FAIL | -0.0000 |
| C5: n_approach_eval >= 30 | FAIL | 5 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C2 FAIL: causal_sig_contact=0.0000 <= causal_sig_approach=0.6184. MECH-102 escalation ladder not present.
- C4 FAIL: cal_gap_approach=-0.0000 <= 0.03 (E3 not calibrated — trajectory scores not meaningful).
- C5 FAIL: n_approach_eval=5 < 30
