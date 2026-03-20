# V3-EXQ-051 — Q-007: Valence-Precision Correlation (V3)

**Status:** FAIL
**Claim:** Q-007 — z_beta (valence) correlates with E3-derived precision
**alpha_world:** 0.9  (SD-008)
**Training:** 400 eps per condition (stable drift=0.02, volatile drift=0.5)
**Seed:** 0

## Motivation

Q-007 V2 FAIL: z_beta mixed into z_gamma (no SD-005 split) + hardcoded precision.
V3: z_beta is isolated in shared stack; E3 precision derives from prediction error variance.

## Valence-Precision Correlation

| Condition | pearson_r | mean z_beta norm | mean running_var | n_pairs |
|-----------|-----------|-----------------|-----------------|---------|
| Stable (drift=0.02) | -0.0285 | 0.7193 | 0.00139 | 6875 |
| Volatile (drift=0.5) | -0.0329 | 0.7195 | 0.00137 | 6959 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: pearson_r_volatile > 0.05 (positive correlation) | FAIL | -0.0329 |
| C2: z_beta_volatile > z_beta_stable (arousal up) | PASS | 0.7195 vs 0.7193 |
| C3: running_var_volatile > running_var_stable (less certain) | FAIL | 0.00137 vs 0.00139 |
| C4: n_pairs >= 50 per condition | PASS | stable=6875  volatile=6959 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: pearson_r_volatile=-0.0329 <= 0.05
- C3 FAIL: mean_running_var_volatile=0.00137 <= stable=0.00139
