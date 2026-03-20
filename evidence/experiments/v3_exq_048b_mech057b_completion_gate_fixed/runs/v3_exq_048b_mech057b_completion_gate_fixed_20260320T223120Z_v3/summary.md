# V3-EXQ-048b -- MECH-057b: Trajectory Completion Gate (Fixed)

**Status:** FAIL
**Claims:** MECH-057b, MECH-090
**Fix:** Routes through agent.select_action() instead of agent.e3.select() directly
**Prerequisite:** EXQ-042 PASS (HippocampalModule terrain prior functional)
**alpha_world:** 0.9
**Warmup:** 400 eps  |  Eval: 50 eps
**Seed:** 0

## Root Cause of EXQ-048 FAIL

EXQ-048 called `agent.e3.select()` directly and set `agent._last_action` manually,
bypassing `agent.select_action()`. The `select_action()` method is the only code
path that calls `beta_gate.elevate()` and `beta_gate.propagate()`. As a result,
`gate.is_elevated` was always False and `hold_count=0` in EXQ-048, regardless of
commitment state. This was an experiment instrumentation error, not a mechanism failure.

## Motivation

MECH-057b: BetaGate should hold policy output during committed action execution,
and release at completion (E3 tick boundary where a new trajectory is selected).
This tests whether the gate behaves correctly: elevated during sequences, released
when sequences complete.

Committed state read from: agent.e3._committed_trajectory is not None
Gate state read from: agent.beta_gate.is_elevated, agent.beta_gate.get_state()

## Beta Gate State During Eval

| Metric | Value |
|--------|-------|
| committed_step_count | 0 |
| uncommitted_step_count | 10000 |
| hold_rate_during_committed | 0.000 |
| gate_release_events | 0 |
| hold_count_total (all steps) | 0 |
| propagation_count_total | 10350 |
| calibration_gap_approach | 0.9647 |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: committed_step_count >= 10 (agent commits) | FAIL | 0 |
| C2: hold_rate_during_committed > 0.5 (gate holds) | FAIL | 0.000 |
| C3: propagation_count > 0 (gate releases) | PASS | 10350 |
| C4: calibration_gap_approach > 0 (E3 functional) | PASS | 0.9647 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: committed_step_count=0 < 10
- C2 FAIL: hold_rate_during_committed=0.000 <= 0.5
