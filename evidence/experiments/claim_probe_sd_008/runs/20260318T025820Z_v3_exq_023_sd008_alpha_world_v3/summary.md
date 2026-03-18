# V3-EXQ-023 — SD-008 alpha_world Fix Test

**Status:** FAIL
**alpha_world:** 1.0  (baseline was 0.3 — root cause of EXQ-013–019 FAIL cluster)
**alpha_self:** 0.3
**Warmup:** 300 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Probe eval:** 10 grid resets
**Seed:** 0

## Motivation (SD-008)

LatentStack.encode() used alpha=0.3 for z_world → ~3-step EMA → event responses
suppressed to 30% per step. Root cause of all EXQ-013–019 FAILs:
- EXQ-013: Δz_world barely differs by event type (selectivity ≈ 0)
- EXQ-014/016/021: reafference R²=0.118 (SGD) instead of 0.333 (lstsq)
- EXQ-018: ARC-016 precision ≈ 188 always (E2 trivially accurate)
- EXQ-019: z_self more autocorrelated than z_world (backwards from MECH-058)

This test uses alpha_world=1.0: z_world tracks current observation much more
directly. MECH-089 theta buffer handles temporal integration; encoder EMA was redundant.

## Event Selectivity (SD-008 diagnostic)

| Event Type | mean Δz_world |
|---|---|
| none (locomotion) | 0.0813 |
| env_caused_hazard | 0.1657 |
| agent_caused_hazard | 0.1068 |
| **selectivity margin** (env - none) | **0.0843** |

## lstsq Reafference (MECH-098)

| Metric | Value |
|---|---|
| n_empty_steps | 4916 |
| R²_train | -0.065 |
| R²_test | 0.021 |

## ARC-016 Precision Dynamics

| Condition | mean_pred_err | variance | precision |
|---|---|---|---|
| stable (drift_prob=0.1) | 0.00084 | 0.00000 | 725015.24 |
| perturbed (drift_prob=0.9) | 0.00092 | 0.00000 | 707763.34 |
| **var_diff** | — | **0.00000** | — |

## SD-003 Attribution

| Position | mean(causal_sig) |
|---|---|
| Near-hazard | 0.0013 |
| Safe | 0.0018 |
| **calibration_gap** | **-0.0005** |

Warmup: harm=753  benefit=131

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: event_selectivity_margin > 0.005 | PASS | 0.0843 |
| C2: R²_test > 0.25 (lstsq reafference) | FAIL | 0.021 |
| C3: var_diff > 0.001 (ARC-016 fires) | FAIL | 0.00000 |
| C4: calibration_gap > 0.05 (SD-003) | FAIL | -0.0005 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C2 FAIL: reafference_r2=0.021 <= 0.25 (EXQ-014 lstsq benchmark = 0.333)
- C3 FAIL: var_diff=0.00000 <= 0.001 (stable=0.00000  perturbed=0.00000)
- C4 FAIL: calibration_gap=-0.0005 <= 0.05
