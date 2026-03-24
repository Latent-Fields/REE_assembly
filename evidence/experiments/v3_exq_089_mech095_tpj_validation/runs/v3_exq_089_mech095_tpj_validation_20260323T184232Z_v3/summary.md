# V3-EXQ-089 -- MECH-095: TPJ Agency Comparator Validation

**Status:** FAIL
**Claims:** MECH-095
**World:** CausalGridWorldV2 (5 hazards, frequent env_drift for world-caused events)
**Protocol:** E2 training (300 eps) -> TPJ eval (200 eps, no TPJ training)

## TPJ Mechanism

agency_signal = 1 / (1 + ||E2.predict_next_self(z_self_t, a_t) - z_self_{t+1}||)

High agency_signal: action produced predicted z_self change -> self-caused.
Low agency_signal: z_self changed unexpectedly -> world-caused or action error.

Schizophrenia failure mode (Frith et al. 2000): if the comparator is absent/noisy,
self-generated actions appear world-caused (passivity experiences).

## Results

| Metric | Value |
|--------|-------|
| mean mismatch (self-caused) | 0.345029 |
| mean mismatch (world-caused) | 0.348826 |
| mismatch gap | 0.003798 |
| classification accuracy | 0.8547 |
| false attribution rate | 1.0000 |
| n_world_caused_eval | 42 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: mismatch_world > mismatch_self + 0.02 | FAIL | gap=0.003798 |
| C2: classification_acc > 0.70 | PASS | 0.8547 |
| C3: false_attribution < 0.15 | FAIL | 1.0000 |
| C4: n_world_caused >= 30 | PASS | 42 |
| C5: agency_signal not saturated | PASS | mean=0.744 std=0.007 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: mismatch gap=0.003798 <= 0.02. E2 predict_next_self does not differentiate self vs world-caused changes.
- C3 FAIL: false_attribution=1.0000 >= 0.15. World-caused events misattributed as self-caused (schizophrenic failure mode).
