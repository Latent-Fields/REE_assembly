# V3-EXQ-231 -- MECH-106 BG Hysteresis

**Status:** FAIL  **Criteria met:** 2/4
**Claims:** MECH-106  **Purpose:** evidence

First experiment for MECH-106. Tests whether committed mode persists beyond the initial triggering condition (variance < threshold).

## Conditions

- PERSISTENT: commitment held for >= 20 steps after trigger; releases only when variance > threshold + 0.05
- REACTIVE: commitment = instantaneous (variance < threshold each step)

## Results

| Seed | Persist ratio | Reactive ratio | Commit eps | C1 | C2 | C3 | C4 |
|------|--------------|----------------|------------|----|----|----|----|
| 42 | 1.000 | 1.000 | 400 | FAIL | PASS | FAIL | PASS |
| 7 | 1.000 | 1.000 | 400 | FAIL | PASS | FAIL | PASS |
| 13 | 1.000 | 1.000 | 400 | FAIL | PASS | FAIL | PASS |

## Interpretation

MECH-106 PARTIAL: Some hysteresis signal present but below full threshold. Consider longer training or wider margin.

## Failure Notes

- C1 FAIL: persist_ratios=[1.0, 1.0, 1.0] (need > 2.0 in >= 2/3)
- C3 FAIL: PERSISTENT not committing more steps than REACTIVE
