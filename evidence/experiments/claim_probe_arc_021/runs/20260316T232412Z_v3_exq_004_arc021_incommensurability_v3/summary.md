# V3-EXQ-004 -- ARC-021 Three-Loop Incommensurability

**Status:** FAIL
**Warmup:** 300 episodes, RANDOM policy
**Probe eval:** 10 grid resets x (near-hazard + safe positions)
**Seed:** 0

## ARC-021 Prediction

Collapsing E1/E2/E3 gradients into a single optimizer forces E3.harm_eval to
compete with much larger E1/E2 prediction gradients. On steps with no harm events
(~88% of steps), E3 parameters receive only E1/E2 gradient signal, corrupting
the harm_eval function. Separate optimizers isolate the E3 learning channel.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: SEPARATE calibration_gap > 0.05 | FAIL | 0.0001 |
| C2: SEPARATE gap > COLLAPSED gap | PASS | 0.0001 vs -0.0004 |
| C3: COLLAPSED gap < SEPARATE * 0.7 or degenerate | PASS | -0.0004  |
| C4: Warmup harm events > 100 | PASS | 819 |
| C5: No fatal errors | PASS | 0 |
| C6: Probe coverage >= 10 each | PASS | near=231 safe=66 |

## Calibration Results

| Condition | Optimizer | mean_near | mean_safe | calibration_gap |
|---|---|---|---|---|
| SEPARATE  | E12 (lr=1e-3) + E3 (lr=1e-4) | -0.0011 | -0.0012 | 0.0001 |
| COLLAPSED | All params (lr=1e-3, lambda_e3=0.1) | -0.0020 | -0.0016 | -0.0004 |

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL: SEPARATE gap 0.0001 <= 0.05
