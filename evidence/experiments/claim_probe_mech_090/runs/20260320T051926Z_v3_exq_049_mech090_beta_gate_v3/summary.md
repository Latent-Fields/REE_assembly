# V3-EXQ-049 — MECH-090: Beta-Gated Policy Propagation

**Status:** FAIL
**Claim:** MECH-090 — beta gate holds E3 policy output during committed action
**alpha_world:** 0.9
**Warmup:** 400 eps  |  Eval: 50 eps
**Seed:** 0

## Motivation

MECH-090: When the agent is committed to a trajectory, BetaGate.is_elevated = True
and propagate() returns None (policy output held). When uncommitted, gate releases.
This measures the concordance between commitment state and gate state.

## Beta Gate Concordance

| State | Count | Rate |
|-------|-------|------|
| committed + gate elevated (correct hold) | 0 | 0.000 |
| committed + gate NOT elevated (unexpected) | 7687 | 1.000 |
| uncommitted + NOT elevated (correct release) | 0 | 0.000 |
| uncommitted + gate elevated (unexpected) | 0 | 1.000 |

- hold_count (total gate holds): 0
- propagation_count (total gate releases): 0

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: committed_hold_concordance > 0.6 | FAIL | 0.000 |
| C2: uncommitted_release_concordance > 0.5 | FAIL | 0.000 |
| C3: hold_count > 0 (gate holds) | FAIL | 0 |
| C4: propagation_count > 0 (gate releases) | FAIL | 0 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: committed_hold_concordance=0.000 <= 0.6
- C2 FAIL: uncommitted_release_concordance=0.000 <= 0.5
- C3 FAIL: hold_count=0 == 0
- C4 FAIL: propagation_count=0 == 0
