# V3-EXQ-132 -- MECH-070 E2 Motor-Model Discriminative Pair

**Status:** FAIL
**Claims:** MECH-070
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** E2_MOTOR_ON vs E2_MOTOR_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.4

## Design

MECH-070 asserts E2 is a conceptual-sensorium motor model (cerebellar analog)
with planning horizon exceeding E1 (cortical, prediction_horizon=20).

E2_MOTOR_ON: E2 trains on z_self motor-sensory transitions (1-step MSE on z_self). E1 and E3 harm_eval also train normally.

E2_MOTOR_ABLATED: E2 frozen at random init. E1 and E3 harm_eval train normally.
Motor model contribution removed; E3 must rely on z_world alone.

Key metric: harm_eval_gap = mean_harm_score - mean_safe_score at eval.
Secondary: e2_r2 (R^2 of E2.world_forward on z_self norm; confirms manipulation).

## Pre-Registered Thresholds

C1: gap_motor_on >= 0.04 in all seeds  (E2_MOTOR_ON harm eval above floor)
C2: per-seed delta (ON - ABLATED) >= 0.02 in all seeds  (motor model adds >=2pp)
C3: gap_ablated >= 0.0  (ablation learns from z_world; data quality)
C4: n_harm_eval_min >= 20  (sufficient harm events)
C5: e2_r2_on >= 0.05  (E2 learned a useful z_self forward model)

## Results

| Condition | gap (avg) | mean_harm | mean_safe | e2_r2 |
|-----------|-----------|-----------|-----------|-------|
| E2_MOTOR_ON      | 0.0153 | 0.5218 | 0.5065 | 0.9961 |
| E2_MOTOR_ABLATED | 0.0153 | 0.5218 | 0.5065 | -- |

**delta_gap (ON - ABLATED): +0.0000**

Diagnostic: e2_r2_on=0.9961 (manipulation check -- confirms E2 learned a useful z_self forward model in E2_MOTOR_ON).

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_on >= 0.04 (all seeds) | FAIL | 0.0153 |
| C2: per-seed delta >= 0.02 (all seeds) | FAIL | [0.0, 0.0] |
| C3: gap_ablated >= 0.0 | PASS | 0.0153 |
| C4: n_harm_min >= 20 | PASS | 533 |
| C5: e2_r2_on >= 0.05 | PASS | 0.9961 |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-070 NOT supported at V3 proxy level: gap_on=0.0153 (C1 FAIL), delta=+0.0000 (C2 FAIL), e2_r2=0.9961 (C5 PASS). Trained E2 motor model does not produce a detectable improvement in harm_eval quality over the frozen-E2 ablation at this scale. Possible reasons: (a) at world_dim=32 the z_self forward model is too simple to add discriminative value; (b) E3 learns from z_world alone, making E2 contributions marginal; (c) the V3 proxy does not exercise the rollout horizon advantage claimed by MECH-070 (which requires active trajectory evaluation, not just R^2 of next-step z_self prediction).

## Per-Seed

E2_MOTOR_ON:
  seed=42: gap=0.0138 n_harm=580 e2_r2=0.9950
  seed=123: gap=0.0168 n_harm=533 e2_r2=0.9972

E2_MOTOR_ABLATED:
  seed=42: gap=0.0138 n_harm=580 e2_r2=0.0000
  seed=123: gap=0.0168 n_harm=533 e2_r2=0.0000

## Failure Notes

- C1 FAIL: E2_MOTOR_ON gap below 0.04 in seeds [42, 123] -- E2 motor model does not produce discriminative harm eval signal
- C2 FAIL: per-seed deltas [0.0, 0.0] < 0.02 -- E2 motor model does not add >=2pp harm eval advantage over ablation
