# V3-EXQ-080 -- MECH-102 Terminal Error-Correction Discriminative Pair

**Status:** FAIL
**Claims:** MECH-102
**Decision:** hybridize
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Eval policy:** E3-guided greedy (argmin E3.harm_eval(E2.world_fwd(z, a)))
**Warmup:** 2 eps  **Eval:** 2 eps

## Pre-Registered Thresholds

C1: delta_contact_rate           > 0.03
C2: delta_avoidance (enabled-blocked) > 0.05
C3: world_forward_r2_ENABLED     > 0.10
C4: per-seed BLOCKED > ENABLED contact_rate

## Results

| Condition | contact_rate | avoidance_rate | wf_r2 |
|-----------|-------------|----------------|-------|
| COORDINATION_ENABLED  | 2.7500 | 1.0000 | 0.0000 |
| COORDINATION_BLOCKED  | 3.0000 | 1.0000 | 0.0000 |

**delta_contact_rate (BLOCKED - ENABLED): +0.2500**
**delta_avoidance (ENABLED - BLOCKED): +0.0000**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_contact_rate > 0.03              | PASS | 0.2500 |
| C2: delta_avoidance > 0.05                 | FAIL | 0.0000 |
| C3: world_forward_r2_ENABLED > 0.10        | FAIL | 0.0000 |
| C4: per-seed BLOCKED > ENABLED contact_rate | FAIL | [True, False] |

Criteria met: 1/4 -> **FAIL**

## Interpretation

Weak positive: COORDINATION_BLOCKED shows higher contact rate but discriminative margin is below threshold. Early correction advantage is marginal. May indicate E2.world_forward noise limits greedy policy effectiveness, or approach gradient signal is insufficient for clear harm avoidance.

## Per-Seed

COORDINATION_ENABLED:
  seed=42: contact_rate=2.5000 avoidance=1.0000 wf_r2=0.0000 n_approach=8
  seed=7: contact_rate=3.0000 avoidance=1.0000 wf_r2=0.0000 n_approach=8

COORDINATION_BLOCKED:
  seed=42: contact_rate=3.0000 avoidance=1.0000 wf_r2=0.0000
  seed=7: contact_rate=3.0000 avoidance=1.0000 wf_r2=0.0000

## Failure Notes

- C2 FAIL: delta_avoidance=0.0000 <= 0.05 (gradient did not enable measurable early correction)
- C3 FAIL: world_forward_r2=0.0000 <= 0.10 (E2.world_forward insufficiently trained -- greedy policy unreliable)
- C4 FAIL: not all seeds show BLOCKED > ENABLED contact_rate -- inconsistent
