# V3-EXQ-024 — E2_world 1-Step Loss + Fixed SD-003 Probe

**Status:** FAIL
**alpha_world:** 0.9  (SD-008 fix, same as EXQ-023)
**E2W_1STEP_WEIGHT:** 1.0  (KEY FIX: direct 1-step loss added)
**E2W_ROLLOUT_WEIGHT:** 0.5  (5-step rollout kept as auxiliary)
**Probe env:** 6 hazards, min_dist > 2  (FIX: was 15 hazards, min_dist > 3)
**Seed:** 1

## Motivation (from EXQ-023 diagnosis)

Two problems diagnosed from EXQ-023:

1. **E2_world worse than identity baseline**: With 5-step rollout on random policy,
   ~50% wall collisions produce unpredictable 5-step outcomes.
   EXQ-023 identity_MSE = 0.000162; reported E2_world MSE = 0.0006–0.0008 (4–7× worse).
   Fix: add 1-step direct loss `MSE(E2.world_forward(z_world_t, a_t), z_world_t+1)`.

2. **Probe geometry broken at 15 hazards**: 15 × ~25 cells exclusion = ~375 on 144 grid.
   Only 27–59 safe cells — measuring near-hazard vs near-hazard.
   Fix: probe_env with 6 hazards + min_dist > 2.

## E2_world Quality

| Metric | Value |
|---|---|
| 1-step MSE | 0.00021 |
| Identity baseline MSE | 0.00020 |
| Improvement ratio | 0.94× |

## Event Selectivity

| Event Type | mean Δz_world |
|---|---|
| none (locomotion) | 0.0632 |
| env_caused_hazard | 0.1196 |
| agent_caused_hazard | 0.0724 |
| **selectivity margin** | **0.0564** |

## ARC-016 Precision Dynamics

| Condition | mean_pred_err | variance | precision |
|---|---|---|---|
| stable (drift=0.1) | 0.00045 | 0.00000 | 915139.58 |
| perturbed (drift=0.9) | 0.00048 | 0.00000 | 905453.74 |
| **var_diff** | — | **0.00000** | — |

## SD-003 Attribution

| Position | mean(causal_sig) |
|---|---|
| Near-hazard | -0.0025 |
| Safe (min_dist > 2) | -0.0109 |
| **calibration_gap** | **0.0083** |

n_near=207  n_safe=487

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: event_selectivity_margin > 0.005 | PASS | 0.0564 |
| C2: e2w_improvement_ratio > 2.0× | FAIL | 0.94× |
| C3: var_diff > 0.001 (ARC-016) | FAIL | 0.00000 |
| C4: calibration_gap > 0.05 (SD-003) | FAIL | 0.0083 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C2 FAIL: e2w_improvement_ratio=0.94x <= 2.0 (1-step MSE=0.00021, identity=0.00020)
- C3 FAIL: var_diff=0.00000 <= 0.001
- C4 FAIL: calibration_gap=0.0083 <= 0.05
