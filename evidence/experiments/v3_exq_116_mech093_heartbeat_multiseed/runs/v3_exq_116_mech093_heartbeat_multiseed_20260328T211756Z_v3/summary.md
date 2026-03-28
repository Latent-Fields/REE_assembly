# V3-EXQ-116 -- MECH-093 z_beta Heartbeat Rate Modulation (Multi-Seed)

**Status:** PASS
**Claims:** MECH-093
**Proposal:** EXP-0011 / EVB-0009
**Decision:** retain_ree
**Seeds:** [42, 123]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 500 eps  **Eval:** 40 eps  **Steps/ep:** 200

## Context

EXQ-097b (seed=42 only) PASS 2/3: C1 r=0.964, C3 var_ratio=0.096. MECH-093 promoted to provisional pending multi-seed replication. This experiment provides that replication.

## Pre-Registered Thresholds

C1 (modulation gate): Pearson r(|z_beta|_norm, 1/e3_rate) >= 0.15 for BOTH seeds (BETA_MOD_ON)
C2 (safe-phase stability): action_var_ratio (ON/OFF) <= 0.9 for >= 1 seed
C3 (direction consistency): r >= 0 for BOTH seeds (no inversion)
C4 (data quality): n_steps >= 1000 per seed
PASS: C1_both AND C3 AND C4

## Per-Seed Results (BETA_MOD_ON)

| Seed | Pearson r | n_steps | C1 | C3 | C2 |
|------|-----------|---------|----|----|----|
| 42 | 0.965 | 26716 | PASS | PASS | PASS |
| 123 | 0.975 | 25586 | PASS | PASS | PASS |

## Aggregate

| Criterion | Result | Detail |
|-----------|--------|--------|
| C1: r>=0.15 both seeds | PASS | 2/2 seeds |
| C2: var_ratio<=0.9 >=1 seed | PASS | 2/2 seeds |
| C3: direction consistent | PASS | 2/2 seeds |
| C4: data quality | PASS | 2/2 seeds |

Criteria met: 4/4 -> **PASS**

## Interpretation

MECH-093 SUPPORTED by multi-seed replication (2 seeds). Step-level z_beta/rate correlation confirmed for all seeds (C1 r>=0.15), direction consistent (C3), data sufficient (C4). z_beta encodes arousal state and modulates E3 heartbeat frequency at the step level. This is distinct from precision-weighting (MECH-059): rate modulation controls update frequency, not update magnitude.
