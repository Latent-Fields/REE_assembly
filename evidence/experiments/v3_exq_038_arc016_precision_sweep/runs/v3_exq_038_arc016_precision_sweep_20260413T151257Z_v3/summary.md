# V3-EXQ-038 — ARC-016 Precision Threshold Sweep

**Status:** FAIL
**Claims:** ARC-016, MECH-093
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Hazard harm levels:** [0.005, 0.01, 0.02, 0.05, 0.1]
**Seed:** 0
**Predecessors:** EXQ-018 (PASS), EXQ-031 (PASS) — ARC-016 mechanism confirmed

## Motivation

EXQ-018 and EXQ-031 confirm that dynamic precision responds to environment stability.
This experiment characterizes the quantitative relationship: does precision/commitment
behavior scale predictably with hazard_harm (environment danger level)?

MECH-093 (z_beta modulates E3 heartbeat frequency) predicts the precision boundary is
not fixed but scales with environment danger. A systematic sweep tests this prediction.

## Sweep Results

| hazard_harm | var_stable | var_perturbed | var_diff | commit_stable | commit_perturbed |
|---|---|---|---|---|---|
| 0.005 | 0.402576 | 0.402551 | -0.000025 | 0.000 | 0.000 |
| 0.010 | 0.402576 | 0.402551 | -0.000025 | 0.000 | 0.000 |
| 0.020 | 0.402576 | 0.402551 | -0.000025 | 0.000 | 0.000 |
| 0.050 | 0.402576 | 0.402551 | -0.000025 | 0.000 | 0.000 |
| 0.100 | 0.402576 | 0.402551 | -0.000025 | 0.000 | 0.000 |

**Pearson r(hazard_harm, var_diff):** -1.000
**Monotone increases in var_diff:** 0/4

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff monotone increases (3+ consecutive) | FAIL | 0/4 |
| C2: Pearson r(hazard_harm, var_diff) > 0.6 | FAIL | -1.000 |
| C3: >= 3 levels with var_diff > 0.001 | FAIL | 0/5 |
| C4: >= 3 levels with commit_stable > commit_perturbed | FAIL | 0/5 |
| C5: no fatal errors | PASS | 0 errors |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: only 0/4 consecutive monotone increases in var_diff
- C2 FAIL: Pearson r(hazard_harm, var_diff) = -1.000 <= 0.6
- C3 FAIL: only 0/5 levels show var_diff > 0.001
- C4 FAIL: only 0/5 levels show commit_stable > commit_perturbed
