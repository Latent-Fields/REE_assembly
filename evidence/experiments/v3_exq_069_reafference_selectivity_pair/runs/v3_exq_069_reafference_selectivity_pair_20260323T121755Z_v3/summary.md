# V3-EXQ-069 -- MECH-098 Reafference Event Selectivity Pair

**Status:** FAIL
**Claims:** MECH-098
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 30 eps

## Pre-Registered Threshold

C1: event_selectivity_delta >= 0.01

## Results

| Condition | margin | mean_dz_loco | mean_dz_event | cal_gap (info) |
|-----------|--------|-------------|---------------|----------------|
| REAFFERENCE_ON  | 0.0035 | 0.0459 | 0.0494 | -0.0001 |
| REAFFERENCE_OFF | 0.0056 | 0.0422 | 0.0478 | -0.0000 |

**event_selectivity_delta (ON - OFF): -0.0021**
reafference_r2 (ON, predictor quality): 0.3389

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: selectivity_delta >= 0.01 (core claim) | FAIL | -0.0021 |
| C2: reafference_r2 > 0.20 (predictor works) | PASS | 0.3389 |
| C3: margin_OFF > 0 (baseline non-trivial) | PASS | 0.0056 |
| C4: min event steps >= 10 | PASS | 45 |

Criteria met: 3/4 -> **FAIL**

## Interpretation

MECH-098 NOT SUPPORTED: reafference correction does not improve z_world event selectivity. EXQ-027b over-correction hypothesis extends to selectivity domain. SD-010 (harm stream separation) may be required before MECH-098 can show net benefit.

## Per-Seed

REAFFERENCE_ON:
  seed=42: margin=0.0033 r2=0.3232 n_event=45
  seed=7: margin=0.0037 r2=0.3547 n_event=47
REAFFERENCE_OFF:
  seed=42: margin=0.0041 n_event=45
  seed=7: margin=0.0071 n_event=47

## Failure Notes

- C1 FAIL: event_selectivity_delta=-0.0021 < 0.01
