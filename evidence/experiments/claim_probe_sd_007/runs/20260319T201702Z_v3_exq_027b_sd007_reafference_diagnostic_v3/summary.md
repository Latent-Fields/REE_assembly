# V3-EXQ-027b — SD-007 Reafference Diagnostic

**Status:** PASS
**Claims:** SD-007, MECH-098, MECH-101
**SD-007 enabled (MECH-101 fix):** ReafferencePredictor(z_world_raw_prev + a → z_world)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 800 eps (random policy, 12×12, 15 hazards, drift)
**Eval:** 50 eps
**Seed:** 0

## Motivation

EXQ-027 paradox: reafference REDUCED calibration_gap from 0.0375 (EXQ-026, no reafference)
to 0.0244 (EXQ-027, with reafference). This experiment tests whether the harm_eval head
trained on z_world_raw vs z_world_corrected shows a systematic performance difference.

## Results

| Head | calibration_gap | harm_pred_std |
|------|----------------|--------------|
| raw z_world | 0.0491 | 0.1075 |
| corrected z_world (reafference) | 0.0041 | 0.0084 |

- **correction_delta** (corrected - raw): **-0.0450**  → SD-007 **hurts** E3 calibration
- reafference_r2: 0.3730  (predictor predictive quality)

## Interpretation

SD-007 hurts E3 calibration (correction_delta < 0). Over-correction hypothesis supported.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap_raw > 0.03 (E3 baseline functional) | PASS | 0.0491 |
| C2: reafference_r2 > 0.20 (predictor works) | PASS | 0.3730 |
| C3: harm_pred_std_raw > 0.01 (raw head not collapsed) | PASS | 0.1075 |
| C4: n_agent_hazard_steps >= 5 | PASS | 51 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 → **PASS**
