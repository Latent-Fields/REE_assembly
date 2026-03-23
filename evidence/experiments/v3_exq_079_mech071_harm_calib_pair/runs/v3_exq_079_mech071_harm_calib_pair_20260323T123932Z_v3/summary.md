# V3-EXQ-079 -- MECH-071 Harm Calibration Discriminative Pair

**Status:** FAIL
**Claims:** MECH-071
**Decision:** retire_ree_claim
**Seeds:** [42]
**SHARP_WORLD alpha_world:** 0.9  (SD-008)
**SMOOTH_WORLD alpha_world:** 0.3  (baseline)
**Warmup:** 30 eps  **Eval:** 5 eps

## Pre-Registered Thresholds

C1: delta_calibration_gap        > 0.015
C2: calibration_gap_SHARP        > 0.025
C3: calibration_gap_SMOOTH       < 0.020
C4: per-seed SHARP > SMOOTH directionality

## Results

| Condition | calibration_gap | env_gap | approach_gap | mean_none | mean_agent |
|-----------|----------------|---------|--------------|-----------|------------|
| SHARP_WORLD  | -0.0007  | 0.0046 | 0.0029 | 0.5036 | 0.5029 |
| SMOOTH_WORLD | -0.0020 | 0.0021 | 0.0018 | 0.5043 | 0.5023 |

**delta_calibration_gap (SHARP - SMOOTH): +0.0013**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_calibration_gap > 0.015    | FAIL | 0.0013 |
| C2: calibration_gap_SHARP > 0.025    | FAIL | -0.0007 |
| C3: calibration_gap_SMOOTH < 0.020   | PASS | -0.0020 |
| C4: per-seed SHARP > SMOOTH           | PASS | [True] |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-071 NOT supported by this pair: SD-008 does not discriminate calibration gap (delta=0.0013 <= 0.015). Either z_world encodes hazard structure independently of EMA alpha, or E3 harm_eval cannot learn calibration asymmetry at all. Consider whether proxy gradient fields (ARC-024) are sufficient alone to explain EXQ-026 calibration_gap=0.037 without alpha sensitivity.

## Per-Seed

SHARP_WORLD:
  seed=42: calibration_gap=-0.0007 env_gap=0.0046 approach_gap=0.0029 n_agent=1 n_env=3

SMOOTH_WORLD:
  seed=42: calibration_gap=-0.0020 env_gap=0.0021 approach_gap=0.0018

## Failure Notes

- C1 FAIL: delta_calibration_gap=0.0013 <= 0.015 (SD-008 does not enable MECH-071 calibration asymmetry)
- C2 FAIL: calibration_gap_SHARP=-0.0007 <= 0.025 (no positive asymmetry even with alpha_world=0.9)
- WARNING: n_agent_hazard_eval_min=1 < 3 (insufficient agent-caused contacts for reliable mean)
