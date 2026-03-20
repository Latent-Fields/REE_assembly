# V3-EXQ-027 — SD-003 V3: Full Reafference Pipeline

**Status:** FAIL
**Claims:** SD-003, SD-007, MECH-071, MECH-098
**SD-007 enabled (MECH-101 fix):** ReafferencePredictor(z_world_raw_prev[32] + a[5] → 32)
**alpha_world:** 0.9  (SD-008)
**alpha_self:** 0.3
**Warmup:** 500 eps (random policy, 12×12, 15 hazards, drift)
**Eval:** 50 eps
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

- n_empty_steps collected: 7969
- R² (held-out): **0.3619**  (PASS threshold: 0.20)

## E3 harm_eval Scores (z_world_corrected)

| Event Type | mean E3.harm_eval | n_steps |
|---|---|---|
| none (locomotion) | 0.4678 | 906 |
| env_caused_hazard | 0.4890 | 80 |
| agent_caused_hazard | 0.4921 | 49 |

- **calibration_gap** (agent - none): **0.0244**  (PASS threshold: 0.15)
- env_gap (env - none): 0.0213
- harm_pred_std: 0.0657

## Training Summary

- warmup_harm: 1250
- agent_hazard events: 460
- env_hazard events: 790
- benefit: 201

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.15 (SD-003 threshold) | FAIL | 0.0244 |
| C2: reafference_r2 > 0.20 (SD-007 predictive) | PASS | 0.3619 |
| C3: harm_pred_std > 0.01 (E3 not collapsed) | PASS | 0.0657 |
| C4: n_agent_hazard_steps >= 5 | PASS | 49 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0244 <= 0.15
