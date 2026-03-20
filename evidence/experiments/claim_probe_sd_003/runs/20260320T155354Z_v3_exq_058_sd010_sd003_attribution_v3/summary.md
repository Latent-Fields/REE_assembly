# V3-EXQ-058 — SD-010: SD-003 Attribution Recovery

**Status:** FAIL
**Claims:** SD-003, SD-010
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Retests:** EXQ-043/044 (causal_sig threshold 0.001)
**Protocol:** Three-phase (terrain 400 → calibration 200 → eval 100)
**alpha_world:** 0.9  |  **Seed:** 0

## Context

EXQ-043/044 FAILED: causal_sig ≈ 0.0004 (threshold 0.001). Root cause: harm_eval(z_world)
collapsed as terrain training matured — approach states dominated harm_buf, E3 predicted
harm≈1 for all states, causal_sig → 0.

SD-010 fix: z_harm from HarmEncoder(harm_obs) is isolated from terrain-correlated z_world
features. CF pipeline: z_harm_cf = harm_enc(harm_bridge(E2.world_forward(z_world, a_cf))).

## Results — SD-003 Attribution

| Transition type | causal_sig |
|---|---|
| none (safe locomotion) | -0.161504 |
| hazard_approach        | -0.004514 |
| contact (combined)     | 0.059833 |

- **world_forward R²**: 0.9504
- **calibration_gap_approach**: 0.1736
- **mean_harm_eval_none**: 0.3651  (collapse guard: < 0.2 required)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: causal_sig_approach > 0.001 | FAIL | -0.004514 |
| C2: calibration_gap_approach > 0.05 | PASS | 0.1736 |
| C3: mean_harm_eval_none < 0.2 (no collapse) | FAIL | 0.3651 |
| C4: causal_sig_contact > causal_sig_approach (MECH-102) | PASS | 0.059833 vs -0.004514 |
| C5: n_approach_eval >= 30 | PASS | 1193 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: causal_sig_approach=-0.004514 <= 0.001. SD-003 attribution still collapsed with z_harm. harm_enc may not be learning proximity signal or harm_bridge misaligned.
- C3 FAIL: mean_harm_eval_none=0.3651 >= 0.2. E3 predicting harm everywhere — collapse still occurring.
