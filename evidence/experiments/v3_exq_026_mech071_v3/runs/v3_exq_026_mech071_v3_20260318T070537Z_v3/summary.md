# V3-EXQ-026 — MECH-071 V3: E3.harm_eval Calibration Gap

**Status:** FAIL
**Claim:** MECH-071 V3 redesign (harm_eval belongs on E3, not E2)
**alpha_world:** 0.9  (SD-008: must be >= 0.9 for event sensitivity)
**alpha_self:** 0.3
**Warmup:** 400 eps (random policy, 12×12, 15 hazards, drift)
**Eval:** 50 eps
**Seed:** 0

## Motivation

V3 redesign of MECH-071: harm evaluation lives on E3 (harm_eval_head), NOT on E2.
V2 approach (EXQ-027: E2.predict_harm calibration_gap ≈ 0.0007) failed because:
1. z_gamma (unified) dominated by perspective shift (SD-003 identity shortcut)
2. alpha=0.3 suppressed all event responses to ~30%

This test checks whether E3.harm_eval(z_world) can distinguish world states
corresponding to agent-caused hazard vs normal locomotion. Uses alpha_world=0.9
so z_world responds sharply to events (SD-008 prerequisite).

## E3 harm_eval Scores by Event Type

| Event Type | mean E3.harm_eval | n_steps |
|---|---|---|
| none (locomotion) | 0.1401 | 971 |
| env_caused_hazard | 0.1409 | 74 |
| agent_caused_hazard | 0.1403 | 53 |

- **calibration_gap** (agent - none): **0.0002**
- **env_gap** (env - none): **0.0008**
- harm_pred_std: 0.0037

## Training Summary

- warmup_harm: 1000
- agent_hazard events: 371
- env_hazard events: 629
- benefit: 173

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 (agent-caused > none) | FAIL | 0.0002 |
| C2: env_gap > 0.01 (env-caused > none) | FAIL | 0.0008 |
| C3: harm_pred_std > 0.01 (not collapsed) | FAIL | 0.0037 |
| C4: n_agent_hazard_steps >= 5 | PASS | 53 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0002 <= 0.05
- C2 FAIL: env_gap=0.0008 <= 0.01
- C3 FAIL: harm_pred_std=0.0037 <= 0.01 (collapsed)
