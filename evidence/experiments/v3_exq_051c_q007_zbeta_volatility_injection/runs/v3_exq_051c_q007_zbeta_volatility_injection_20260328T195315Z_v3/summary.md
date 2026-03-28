# V3-EXQ-051c -- Q-007 z_beta Volatility Injection

**Status:** FAIL
**Claims:** Q-007

## Results

| Condition | mean_rv | mean_z_beta |
|---|---|---|
| Stable   | 0.5000 | 0.6592 |
| Volatile | 0.5000 | 0.7751 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: volatile z_beta > stable + 0.05 (delta=+0.1159) | PASS |
| C2: Pearson r(rv, z_beta) > 0.3 (r=0.0000) | FAIL |
| C3: transfer rise > 0.02 (delta=+0.0001) | FAIL |

Criteria met: 1/3 -> **FAIL**
