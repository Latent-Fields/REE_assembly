# V3-EXQ-058c — SD-010: SD-003 Attribution Fixed

**Status:** FAIL
**Claims:** SD-003, SD-010
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Retests:** EXQ-058a (same three-phase protocol, three fixes applied)
**Protocol:** Three-phase (terrain 400 → calibration 200 → eval 100)
**alpha_world:** 0.9  |  **Seed:** 0

## Fixes vs EXQ-058a

1. **Label normalization**: harm_obs[12] (normalized, ∈ [0,1]) for both harm_enc training and harm_eval head.
2. **Sigmoid removed**: harm_eval_z_harm_head is now a linear regression head.
3. **Stratified Phase 2**: Separate buffers for none/approach/contact. Equal sampling per bucket.
   Also includes E2 counterfactual z_harm in each training batch.

## Results — SD-003 Attribution

| Transition type | causal_sig |
|---|---|
| none (safe locomotion) | 0.012706 |
| hazard_approach        | 0.035183 |
| contact (combined)     | 0.103775 |

- **world_forward R²**: 0.9504
- **calibration_gap_approach**: 0.0396
- **mean_harm_eval_none**: 0.6305  (collapse guard: < 0.2 required)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_approach > 0.001 | PASS | 0.035183 |
| C2: calibration_gap_approach > 0.05 | FAIL | 0.0396 |
| C3: mean_harm_eval_none < 0.2 (no collapse) | FAIL | 0.6305 |
| C4: causal_sig_contact > causal_sig_approach (MECH-102) | PASS | 0.103775 vs 0.035183 |
| C5: n_approach_eval >= 30 | PASS | 1133 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C2 FAIL: calibration_gap_approach=0.0396 <= 0.05. E3.harm_eval_z_harm not calibrated for approach states.
- C3 FAIL: mean_harm_eval_none=0.6305 >= 0.2. E3 predicting harm everywhere — collapse still occurring.
