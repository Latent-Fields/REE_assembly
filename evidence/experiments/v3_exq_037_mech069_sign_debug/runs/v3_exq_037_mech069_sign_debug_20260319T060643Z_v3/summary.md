# V3-EXQ-037 — MECH-069 Sign Investigation (EXQ-035 Follow-up)

**Status:** PASS
**Claims:** MECH-069, SD-003
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0
**Predecessor:** EXQ-035 (FAIL — calibration_gap_separated=-0.028 < 0)

## Problem Statement

EXQ-035 found negative calibration_gap for BOTH separated and merged conditions.
E3.harm_eval scores hazard_approach LOWER than none — backwards from expectation.
EXQ-026 (obs-only E3 training, simpler setup) got calibration_gap=+0.0375 (PASS).
Hypothesis: Fix 2 (E3 trained on E2-predicted states) causes sign inversion.

## SUB-A Results (Fix2 — E3 on observed + E2-predicted)

| Transition | mean harm_eval (raw) | mean harm_eval (sigmoid) |
|---|---|---|
| none         | 0.4047 | 0.5997 |
| hazard_approach | 0.5671 | 0.6377 |
| env_caused_hazard | 0.6022 | 0.6457 |
| agent_caused_hazard | 0.5267 | 0.6284 |

- **cal_gap_raw**: 0.1624
- **cal_gap_sig**: 0.0379
- **wf_r2**: 0.9460

## SUB-B Results (ObsOnly — E3 on observed states only, as in EXQ-026)

| Transition | mean harm_eval (raw) | mean harm_eval (sigmoid) |
|---|---|---|
| none         | 0.4361 | 0.6072 |
| hazard_approach | 0.5634 | 0.6369 |
| env_caused_hazard | 0.5537 | 0.6345 |
| agent_caused_hazard | 0.5442 | 0.6325 |

- **cal_gap_raw**: 0.1273
- **cal_gap_sig**: 0.0297
- **wf_r2**: 0.9473

## Diagnostic

**Sign inversion detected (Fix2<0 and ObsOnly>0):** NO
**cal_gap difference (ObsOnly − Fix2):** -0.0350

## PASS Criteria (SUB-B must show correct sign)

| Criterion | Result | Value |
|---|---|---|
| C1: SUB-B cal_gap_raw > 0 (correct sign) | PASS | 0.1273 |
| C2: SUB-B cal_gap_raw > 0.01 (above noise floor) | PASS | 0.1273 |
| C3: harm_approach > harm_none (correct ordering) | PASS | 0.5634 vs 0.4361 |
| C4: wf_r2_obsonly > 0.05 | PASS | 0.9473 |
| C5: n_approach_obsonly >= 30 | PASS | 775 |

Criteria met: 5/5 → **PASS**

