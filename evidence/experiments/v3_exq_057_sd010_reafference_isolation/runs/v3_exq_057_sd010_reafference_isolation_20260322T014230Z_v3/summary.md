# V3-EXQ-057 — SD-010: Reafference Isolation

**Status:** PASS
**Claims:** SD-010, SD-007, MECH-101
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Retests:** EXQ-027b (calibration_gap threshold 0.03)
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0

## Context

EXQ-027b FAILED: calibration_gap_raw=0.024 (threshold 0.03). Root cause:
hazard proximity signals fused into z_world → ReafferencePredictor cancelled
legitimate harm signal as "reafference" from locomotion.

SD-010 fix: z_harm from HarmEncoder(harm_obs) is architecturally separate from
z_world and never enters the reafference correction pipeline.

## Results

| Metric | Value | Threshold |
|---|---|---|
| calibration_gap_z_harm (approach-none) | 0.0793 | > 0.03 |
| harm_pred_std_z_harm (at approach)     | 0.1219 | > 0.01 |
| reafference_r2_z_world (locomotion)    | 0.3895 | > 0.10 |
| n_agent_hazard_steps                   | 31 | >= 5 |
| identity_test_pass                     | 1.0 | == 1.0 |

## harm_eval_z_harm by ttype

| Transition | Mean | n |
|---|---|---|
| none (safe locomotion) | 0.5445 | 113 |
| hazard_approach        | 0.6238 | 1136 |
| contact (combined)     | 0.6744 | 71 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap_z_harm > 0.03 | PASS | 0.0793 |
| C2: harm_pred_std_z_harm > 0.01   | PASS | 0.1219 |
| C3: reafference_r2_z_world > 0.10 | PASS | 0.3895 |
| C4: n_agent_hazard_steps >= 5     | PASS | 31 |
| C5: identity_test_pass == 1.0     | PASS | 1.0 |

Criteria met: 5/5 → **PASS**

