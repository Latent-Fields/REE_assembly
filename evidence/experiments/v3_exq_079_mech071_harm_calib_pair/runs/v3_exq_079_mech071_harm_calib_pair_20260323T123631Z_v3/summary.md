# V3-EXQ-079 -- MECH-071 Harm Calibration Discriminative Pair

**Status:** FAIL
**Claims:** MECH-071
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**SHARP_WORLD alpha_world:** 0.9  (SD-008)
**SMOOTH_WORLD alpha_world:** 0.3  (baseline)
**Warmup:** 2 eps  **Eval:** 2 eps

## Pre-Registered Thresholds

C1: delta_calibration_gap        > 0.015
C2: calibration_gap_SHARP        > 0.025
C3: calibration_gap_SMOOTH       < 0.020
C4: per-seed SHARP > SMOOTH directionality

## Results

| Condition | calibration_gap | env_gap | approach_gap | mean_none | mean_agent |
|-----------|----------------|---------|--------------|-----------|------------|
| SHARP_WORLD  | -0.2653  | -0.2653 | 0.2670 | 0.2653 | 0.0000 |
| SMOOTH_WORLD | -0.2657 | -0.2657 | 0.2662 | 0.2657 | 0.0000 |

**delta_calibration_gap (SHARP - SMOOTH): +0.0004**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_calibration_gap > 0.015    | FAIL | 0.0004 |
| C2: calibration_gap_SHARP > 0.025    | FAIL | -0.2653 |
| C3: calibration_gap_SMOOTH < 0.020   | PASS | -0.2657 |
| C4: per-seed SHARP > SMOOTH           | FAIL | [True, False] |

Criteria met: 1/4 -> **FAIL**

## Interpretation

MECH-071 NOT supported by this pair: SD-008 does not discriminate calibration gap (delta=0.0004 <= 0.015). Either z_world encodes hazard structure independently of EMA alpha, or E3 harm_eval cannot learn calibration asymmetry at all. Consider whether proxy gradient fields (ARC-024) are sufficient alone to explain EXQ-026 calibration_gap=0.037 without alpha sensitivity.

## Per-Seed

SHARP_WORLD:
  seed=42: calibration_gap=-0.5306 env_gap=-0.5306 approach_gap=0.0001 n_agent=0 n_env=0
  seed=7: calibration_gap=0.0000 env_gap=0.0000 approach_gap=0.5339 n_agent=0 n_env=0

SMOOTH_WORLD:
  seed=42: calibration_gap=-0.5315 env_gap=-0.5315 approach_gap=-0.0004
  seed=7: calibration_gap=0.0000 env_gap=0.0000 approach_gap=0.5328

## Failure Notes

- C1 FAIL: delta_calibration_gap=0.0004 <= 0.015 (SD-008 does not enable MECH-071 calibration asymmetry)
- C2 FAIL: calibration_gap_SHARP=-0.2653 <= 0.025 (no positive asymmetry even with alpha_world=0.9)
- C4 FAIL: not all seeds show SHARP > SMOOTH directionality -- inconsistent
- WARNING: n_agent_hazard_eval_min=0 < 3 (insufficient agent-caused contacts for reliable mean)
