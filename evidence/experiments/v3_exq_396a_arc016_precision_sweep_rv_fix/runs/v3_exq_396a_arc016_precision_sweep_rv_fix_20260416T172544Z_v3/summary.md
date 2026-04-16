# V3-EXQ-396a -- ARC-016 Precision Threshold Sweep (rv-fix)

**Status:** FAIL
**Claims:** ARC-016, MECH-093
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Hazard harm levels:** [0.005, 0.01, 0.02, 0.05, 0.1]
**Seed:** 0
**Supersedes:** V3-EXQ-396 (which supersedes V3-EXQ-038)

## Root Cause Fixed

EXQ-038 and EXQ-396 had two bugs that together prevented commitment from firing:

1. Training loop: update_running_variance() was never called during training.
   Variance stayed at precision_init=0.5 for all 300 training episodes.
2. Eval loop: agent.e3._running_variance = precision_init reset to 0.5 at
   the start of every eval episode, discarding any accumulated signal.

EXQ-396a fix: (1) calls update_running_variance(pred_error) every training
step; (2) carries post-training variance into eval without resetting.

## Designed behavior

After 350 training episodes on stable env:
- E2 world_forward converges on predictable dynamics
- update_running_variance() accumulates low prediction errors
- variance drops to << commit_threshold=0.40 -> agent is committed

Stable eval (20 eps, no variance reset):
- E2 continues predicting accurately -> variance stays low -> committed

Perturbed eval (hazard drift every step):
- Hazard positions jump randomly -> E2 prediction errors spike
- variance rises toward threshold -> uncommitted fraction increases
- Higher hazard_harm: more harm-driven world changes -> larger gap

## Sweep Results

| hazard_harm | var_post_train | var_stable | var_perturbed | var_diff | commit_stable | commit_perturbed |
|---|---|---|---|---|---|---|
| 0.005 | 0.000034 | 0.001106 | 0.001077 | -0.000029 | 1.000 | 1.000 |
| 0.010 | 0.000026 | 0.001104 | 0.001124 | 0.000021 | 1.000 | 1.000 |
| 0.020 | 0.000035 | 0.001113 | 0.001088 | -0.000025 | 1.000 | 1.000 |
| 0.050 | 0.000032 | 0.001110 | 0.001094 | -0.000016 | 1.000 | 1.000 |
| 0.100 | 0.000034 | 0.001075 | 0.001092 | 0.000017 | 1.000 | 1.000 |

**Pearson r(hazard_harm, var_diff):** 0.442
**Monotone increases in var_diff:** 3/4

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff monotone increases (3+ consecutive) | PASS | 3/4 |
| C2: Pearson r(hazard_harm, var_diff) > 0.6 | FAIL | 0.442 |
| C3: >= 3 levels with var_diff > 0.001 | FAIL | 0/5 |
| C4: >= 3 levels with commit_stable > commit_perturbed | FAIL | 0/5 |
| C5: no fatal errors | PASS | 0 errors |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C2 FAIL: Pearson r(hazard_harm, var_diff) = 0.442 <= 0.6
- C3 FAIL: only 0/5 levels show var_diff > 0.001
- C4 FAIL: only 0/5 levels show commit_stable > commit_perturbed
