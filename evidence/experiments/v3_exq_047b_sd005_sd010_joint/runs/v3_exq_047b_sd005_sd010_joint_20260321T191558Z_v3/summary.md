# V3-EXQ-047b — SD-005 + SD-010 Joint Validation

**Status:** FAIL
**Claims:** SD-005, MECH-069
**Design:** split (z_self ≠ z_world) vs unified (z_self = z_world = avg). SD-010 active in BOTH conditions.
**alpha_world:** 0.9  |  **Warmup:** 500 eps  |  **Eval:** 50 eps  |  **Seed:** 0

## Context

EXQ-047 (SD-005) FAIL: calibration improvement only 3.4pp vs 5pp threshold.
Diagnosis: nociceptive content in z_world contaminated both conditions equally.
EXQ-047b retest: SD-010 now confirmed (EXQ-056c/059c PASS). HarmEncoder routes
harm_obs → z_harm independently, removing nociception from z_world gradient path.

## Results

| Metric | Split | Unified | Delta |
|---|---|---|---|
| world_forward_r2 | 0.9480 | 0.9648 | -0.0168 |
| attribution_gap | -0.001496 | -0.000684 | -0.000811 |
| harm_eval_pearson_r (SD-010) | 0.9999 | 0.9999 | — |
| n_approach | 801 | 801 | — |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: wf_r2_split > wf_r2_unified + 0.05 (split improves E2 prediction) | FAIL | 0.9480 vs 0.9648 |
| C2: attr_gap_split > attr_gap_unified + 0.01 (split improves attribution) | FAIL | -0.001496 vs -0.000684 |
| C3: harm_eval_pearson_r > 0.50 (SD-010 HarmEncoder functional) | PASS | 0.9999 |
| C4: wf_r2_split > 0.30 (E2 model is learning) | PASS | 0.9480 |
| C5: n_approach >= 50 (sufficient attribution data) | PASS | 801 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: wf_r2_split=0.9480 <= wf_r2_unified=0.9648 + 0.05
- C2 FAIL: attr_gap_split=-0.001496 <= attr_gap_unified=-0.000684 + 0.01
