# V3-EXQ-119 -- MECH-090: Beta Gate Committed Dynamics (Multi-Seed Pair)

**Status:** FAIL
**Claims:** MECH-090
**Proposal:** EXP-0016 / EVB-0013
**Decision:** hold
**Seeds:** [42, 123]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 50 eps  **Steps/ep:** 200

## Context

EXQ-049e (seed=0) two-condition design showed committed_hold_conc=1.0 (C1) and uncommitted_release_conc consistent with claim. This is the matched-seed discriminative replication with a full GATE_OFF ablation arm.

## Pre-Registered Thresholds

C1 (hold concordance, GATE_ON): committed_hold_conc >= 0.6 for BOTH seeds
C2 (release concordance, GATE_ON): uncommitted_release_conc >= 0.5 for >= 1 seed
C3 (ablation, GATE_OFF): committed_hold_conc < 0.4 for BOTH seeds
C4 (data quality): n_committed >= 50 per seed (GATE_ON)
C5 (no crashes): zero fatal errors
PASS: C1_both AND C2_at_least_one AND C3_both AND C4_both AND C5

## Per-Seed Results -- BETA_GATE_ON

| Seed | hold_conc | release_conc | n_committed | n_uncommitted | C1 | C2 |
|------|-----------|--------------|-------------|---------------|----|----|  
| 42 | 1.000 | 0.000 | 790 | 0 | PASS | FAIL |
| 123 | 1.000 | 0.000 | 760 | 0 | PASS | FAIL |

## Per-Seed Results -- BETA_GATE_OFF (Ablation)

| Seed | hold_conc | n_committed | C3 |
|------|-----------|-------------|----|
| 42 | 0.000 | 790 | PASS |
| 123 | 0.000 | 760 | PASS |

## Aggregate

| Criterion | Result | Detail |
|-----------|--------|--------|
| C1: hold_conc>=0.6 both (GATE_ON) | PASS | 2/2 seeds |
| C2: release_conc>=0.5 >=1 (GATE_ON) | FAIL | 0/2 seeds |
| C3: hold_conc<0.4 both (GATE_OFF) | PASS | 2/2 seeds |
| C4: n_committed>=50 both (GATE_ON) | PASS | 2/2 seeds |
| C5: no fatal errors | PASS | fatal=0 |

Criteria met: 4/5 -> **FAIL**

## Interpretation

MECH-090 INCONCLUSIVE: criteria_met=4/5. See failure notes for details.

## Failure Notes

- C2 seed=42 (GATE_ON): uncommitted_release_conc=0.000 < 0.5
- C2 seed=123 (GATE_ON): uncommitted_release_conc=0.000 < 0.5
