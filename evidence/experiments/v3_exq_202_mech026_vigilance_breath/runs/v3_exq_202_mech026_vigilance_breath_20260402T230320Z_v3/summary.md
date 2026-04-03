# V3-EXQ-202 -- MECH-026: Ready Vigilance via BreathOscillator

**Status:** FAIL
**Claim:** MECH-026 -- ready vigilance = heightened sensitivity without action commitment
**Supersedes:** V3-EXQ-067
**Design:** Single agent, within-eval spatial comparison (threat-proximate vs neutral uncommitted steps)
**BreathOscillator:** period=50, amplitude=0.3, duration=10
**Seeds:** [42, 123] | **Train:** 500 eps | **Eval:** 50 eps | **Steps:** 200

## Design Rationale

EXQ-067 compared two separate agents (one trained with hazards, one without). This confounded
environment exposure with vigilance state. EXQ-202 trains a SINGLE agent in a hazard environment
and uses the BreathOscillator to create periodic uncommitted windows. During eval, uncommitted
steps are classified by spatial proximity: threat-proximate (Manhattan distance <= 2
to nearest hazard) vs neutral (distance > 2). The readiness gap measures
whether harm_eval output is higher near threats even during uncommitted (non-doing) steps.

## Per-Seed Results

| Seed | Uncommitted | Threat | Neutral | Committed | harm_mean_threat | harm_mean_neutral | harm_std | Fatal |
|------|-------------|--------|---------|-----------|-----------------|------------------|----------|-------|
| 42 | 0 | 0 | 0 | 876 | 0.0000 | 0.0000 | 0.1366 | 0 |
| 123 | 0 | 0 | 0 | 1074 | 0.0000 | 0.0000 | 0.1465 | 0 |

## Aggregate

| Metric | Value |
|--------|-------|
| readiness_gap | +0.0000 |
| harm_eval_mean_threat | 0.0000 |
| harm_eval_mean_neutral | 0.0000 |
| total_uncommitted | 0 |
| total_uncommitted_threat | 0 |
| total_uncommitted_neutral | 0 |
| harm_pred_std (mean across seeds) | 0.1415 |

## PASS Criteria (need 4/5)

| Criterion | Result | Value |
|---|---|---|
| C1: uncommitted_step_count >= 50 per seed | FAIL | [0, 0] |
| C2: uncommitted_threat_steps >= 20 per seed | FAIL | [0, 0] |
| C3: readiness_gap > 0.01 | FAIL | +0.0000 |
| C4: harm_pred_std > 0.01 | PASS | 0.1415 |
| C5: no fatal errors | PASS | 0 |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C1 FAIL: per-seed uncommitted_steps=[0, 0] (need >= 50 each)
- C2 FAIL: per-seed uncommitted_threat_steps=[0, 0] (need >= 20 each)
- C3 FAIL: readiness_gap=+0.0000 <= 0.01
