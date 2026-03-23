# V3-EXQ-083 -- MECH-102 Terminal Error-Correction Discriminative Pair

**Status:** FAIL
**Claims:** MECH-102
**Decision:** hybridize
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Eval policy:** E3-guided greedy (argmin E3.harm_eval(E2.world_fwd(z, a)))
**Warmup:** 400 eps  **Eval:** 80 eps

## Pre-Registered Thresholds

C1: delta_contact_rate           > 0.03
C2: delta_avoidance (enabled-blocked) > 0.05
C3: world_forward_r2_ENABLED     > 0.10
C4: per-seed BLOCKED > ENABLED contact_rate

## Results

| Condition | contact_rate | avoidance_rate | wf_r2 |
|-----------|-------------|----------------|-------|
| COORDINATION_ENABLED  | 1.3000 | 1.0000 | 0.5468 |
| COORDINATION_BLOCKED  | 1.7500 | 1.0000 | 0.4748 |

**delta_contact_rate (BLOCKED - ENABLED): +0.4500**
**delta_avoidance (ENABLED - BLOCKED): +0.0000**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_contact_rate > 0.03              | PASS | 0.4500 |
| C2: delta_avoidance > 0.05                 | FAIL | 0.0000 |
| C3: world_forward_r2_ENABLED > 0.10        | PASS | 0.5468 |
| C4: per-seed BLOCKED > ENABLED contact_rate | FAIL | [True, False] |

Criteria met: 2/4 -> **FAIL**

## Interpretation

Weak positive: COORDINATION_BLOCKED shows higher contact rate but discriminative margin is below threshold. Early correction advantage is marginal. May indicate E2.world_forward noise limits greedy policy effectiveness, or approach gradient signal is insufficient for clear harm avoidance.

## Per-Seed

COORDINATION_ENABLED:
  seed=42: contact_rate=1.2125 avoidance=1.0000 wf_r2=0.5528 n_approach=701
  seed=7: contact_rate=1.3875 avoidance=1.0000 wf_r2=0.5408 n_approach=691

COORDINATION_BLOCKED:
  seed=42: contact_rate=3.0875 avoidance=1.0000 wf_r2=0.4863
  seed=7: contact_rate=0.4125 avoidance=1.0000 wf_r2=0.4633

## Failure Notes

- C2 FAIL: delta_avoidance=0.0000 <= 0.05 (gradient did not enable measurable early correction)
- C4 FAIL: not all seeds show BLOCKED > ENABLED contact_rate -- inconsistent
