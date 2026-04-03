# V3-EXQ-200 -- Q-007 z_beta Volatility Pathway

**Status:** FAIL
**Claims:** Q-007
**Supersedes:** V3-EXQ-051c

## Key Config

- volatility_signal_dim=1 (rv -> z_beta encoder pathway)
- alpha_world=0.9 (SD-008)
- use_event_classifier=True (SD-009)
- CausalGridWorldV2 size=6, hazards=4, nav_bias=0.45
- Seeds: [42, 123]

## Aggregate Results (2 seeds)

| Condition | mean_rv | mean_z_beta |
|---|---|---|
| Stable (drift=0.05) | 0.0055 | 0.5430 |
| Volatile (drift=0.3) | 0.0052 | 0.6715 |

## PASS Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: volatile z_beta > stable + 0.05 (delta=+0.1285) | FAIL | 1/2 |
| C2: Pearson r(rv, z_beta) > 0.3 (r=0.0888) | FAIL | 0/2 |
| C3: transfer rise > 0.02 (delta=+0.0193) | FAIL | 1/2 |

Criteria met: 0/3 -> **FAIL**
