# V3-EXQ-049b -- MECH-090: Beta-Gated Policy Propagation (Fixed)

**Status:** FAIL
**Claim:** MECH-090 -- beta gate holds E3 policy output during committed action
**Fix:** Routes through agent.select_action() instead of agent.e3.select() directly
**alpha_world:** 0.9
**Warmup:** 400 eps  |  Eval: 50 eps
**Seed:** 0

## Root Cause of EXQ-049 FAIL

Same bug as EXQ-048: `agent.e3.select()` called directly, bypassing
`agent.select_action()`. The `select_action()` method is the only code path that
calls `beta_gate.elevate()` and `beta_gate.propagate()`. Gate was never exercised.

## Motivation

MECH-090: When the agent is committed to a trajectory, BetaGate.is_elevated = True
and propagate() returns None (policy output held). When uncommitted, gate releases.
This measures the concordance between commitment state and gate state.

Committed state read from: agent.e3._committed_trajectory is not None
Gate state read from: agent.beta_gate.is_elevated, agent.beta_gate.get_state()

## Beta Gate Concordance

| State | Count | Rate |
|-------|-------|------|
| committed + gate elevated (correct hold) | 0 | 0.000 |
| committed + gate NOT elevated (unexpected) | 0 | 1.000 |
| uncommitted + NOT elevated (correct release) | 10000 | 1.000 |
| uncommitted + gate elevated (unexpected) | 0 | 0.000 |

- hold_count (total gate holds): 0
- propagation_count (total gate releases): 10350

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: committed_hold_concordance > 0.6 | FAIL | 0.000 |
| C2: uncommitted_release_concordance > 0.5 | PASS | 1.000 |
| C3: hold_count > 0 (gate holds) | FAIL | 0 |
| C4: propagation_count > 0 (gate releases) | PASS | 10350 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: committed_hold_concordance=0.000 <= 0.6
- C3 FAIL: hold_count=0 == 0
