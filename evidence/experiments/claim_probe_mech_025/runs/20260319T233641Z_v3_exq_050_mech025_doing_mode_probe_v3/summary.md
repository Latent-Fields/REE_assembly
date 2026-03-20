# V3-EXQ-050 — MECH-025: Action-Doing Mode Probe

**Status:** FAIL
**Claim:** MECH-025 — action-doing mode produces distinct internal signature
**Prerequisite:** EXQ-030b PASS (SD-003 attribution pipeline functional)
**alpha_world:** 0.9
**Warmup:** 500 eps  |  Eval: 50 eps
**Seed:** 0

## Motivation

MECH-025 (V2 FAIL): agent in doing mode should show a distinct internal signature.
V3 fix: SD-003 attribution now works (EXQ-030b PASS). During committed action
execution, the causal signature E3(E2(z,a_actual)) - E3(E2(z,a_cf)) should be
higher than during free exploration (uncommitted steps).

## Causal Signature by Mode

| Mode | mean causal_sig | n_steps |
|------|----------------|---------|
| Committed (doing) | -0.0059 | 7694 |
| Uncommitted (exploring) | 0.0000 | 0 |

- **doing_mode_delta**: -0.0059  (committed - uncommitted)
- world_forward_r2: 0.9152
- harm_pred_std: 0.2169

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: doing_mode_delta > 0.002 (committed has higher causal sig) | FAIL | -0.0059 |
| C2: committed_step_count >= 10 (doing mode entered) | PASS | 7694 |
| C3: world_forward_r2 > 0.05 (E2 functional) | PASS | 0.9152 |
| C4: harm_pred_std > 0.01 (E3 not collapsed) | PASS | 0.2169 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: doing_mode_delta=-0.0059 <= 0.002
