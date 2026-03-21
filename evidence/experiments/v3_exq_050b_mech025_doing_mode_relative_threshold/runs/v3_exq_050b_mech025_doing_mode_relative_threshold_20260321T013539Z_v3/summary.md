# V3-EXQ-050b -- MECH-025: Action-Doing Mode Probe (Relative Threshold)

**Status:** FAIL
**Claim:** MECH-025 -- action-doing mode produces distinct internal signature
**Prerequisite:** EXQ-030b PASS (SD-003 attribution pipeline functional), EXQ-018b (relative threshold)
**Key change:** commit_threshold = 2.0 x mean_training_variance (calibrated, not absolute)
**alpha_world:** 0.9
**Warmup:** 500 eps  |  Eval: 50 eps
**Seed:** 0

## Threshold Calibration

Training baseline variance samples were collected from the last 100 training episodes.
The calibrated threshold ensures the agent enters both committed and uncommitted modes.

| Parameter | Value |
|-----------|-------|
| mean_training_variance | 0.500000 |
| calibrated_threshold (2x) | 1.000000 |

## Motivation

MECH-025 (V2 FAIL): agent in doing mode should show a distinct internal signature.
V3 fix: SD-003 attribution now works (EXQ-030b PASS). During committed action
execution, the causal signature E3(E2(z,a_actual)) - E3(E2(z,a_cf)) should be
higher than during free exploration (uncommitted steps).

Committed state read from: agent.e3._committed_trajectory is not None

## Causal Signature by Mode

| Mode | mean causal_sig | n_steps |
|------|----------------|---------|
| Committed (doing) | -0.0045 | 7859 |
| Uncommitted (exploring) | 0.0052 | 8 |

- **doing_mode_delta**: -0.0097  (committed - uncommitted)
- world_forward_r2: 0.9373
- harm_pred_std: 0.1833

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: doing_mode_delta > 0.002 (committed has higher causal sig) | FAIL | -0.0097 |
| C2: uncommitted_step_count >= 10 (uncommitted mode entered) | FAIL | 8 |
| C3: world_forward_r2 > 0.05 (E2 functional) | PASS | 0.9373 |
| C4: harm_pred_std > 0.01 (E3 not collapsed) | PASS | 0.1833 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: doing_mode_delta=-0.0097 <= 0.002
- C2 FAIL: uncommitted_step_count=8 < 10
