# V3-EXQ-027 — SD-003 V3: Full Reafference Pipeline

**Status:** FAIL
**Claims:** SD-003, SD-007, MECH-071, MECH-098
**SD-007 enabled:** ReafferencePredictor(32 + 5 → 32)
**alpha_world:** 0.9  (SD-008)
**alpha_self:** 0.3
**Warmup:** 3 eps (random policy, 12×12, 15 hazards, drift)
**Eval:** 1 eps
**Seed:** 0

## Motivation

V3 SD-003 pipeline with full reafference correction (SD-007):
1. ReafferencePredictor trained on empty steps to predict perspective-shift Δz_world
2. z_world_corrected = z_world_raw - predicted_shift (applied in LatentStack.encode)
3. E3.harm_eval(z_world_corrected) trained and evaluated by event type
4. calibration_gap = mean(agent_hazard) - mean(none) → PASS > 0.15

V2 EXQ-027 FAIL root causes:
- alpha=0.3: event responses suppressed to 30% → identity shortcut trivially wins
- E2.predict_harm on z_gamma: wrong module + wrong latent

This experiment tests whether the corrected pipeline achieves genuine causal attribution.
Compare with EXQ-026 (same design but no reafference): gap between them isolates SD-007 effect.

## ReafferencePredictor Diagnostic

- n_empty_steps collected: 19
- R² (held-out): **0.0000**  (PASS threshold: 0.20)

## E3 harm_eval Scores (z_world_corrected)

| Event Type | mean E3.harm_eval | n_steps |
|---|---|---|
| none (locomotion) | 0.5211 | 8 |
| env_caused_hazard | 0.0000 | 0 |
| agent_caused_hazard | 0.0000 | 0 |

- **calibration_gap** (agent - none): **-0.5211**  (PASS threshold: 0.15)
- env_gap (env - none): -0.5211
- harm_pred_std: 0.0025

## Training Summary

- warmup_harm: 2
- agent_hazard events: 0
- env_hazard events: 2
- benefit: 0

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.15 (SD-003 threshold) | FAIL | -0.5211 |
| C2: reafference_r2 > 0.20 (SD-007 predictive) | FAIL | 0.0000 |
| C3: harm_pred_std > 0.01 (E3 not collapsed) | FAIL | 0.0025 |
| C4: n_agent_hazard_steps >= 5 | FAIL | 0 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=-0.5211 <= 0.15
- C2 FAIL: reafference_r2=0.0000 <= 0.20
- C3 FAIL: harm_pred_std=0.0025 <= 0.01 (collapsed)
- C4 FAIL: n_agent_hazard_steps=0 < 5
