# V3-EXQ-049d -- MECH-090: Beta-Gated Policy Propagation (chicken-and-egg fix)

**Status:** FAIL
**Claim:** MECH-090 -- beta gate holds E3 policy output during committed action
**Fix 1:** Direct update_running_variance(wf_err) after world_forward loss — breaks _committed_trajectory deadlock
**Fix 2:** is_committed = _running_variance < commit_threshold (not _committed_trajectory probe)
**Prior attempts:** EXQ-049/049b (gate not wired), EXQ-049c (post_action_update still stuck in deadlock)
**alpha_world:** 0.9
**Warmup:** 400 eps  |  Eval: 50 eps
**Seed:** 0

## Root Cause Chain

1. **EXQ-049**: `agent.e3.select()` bypassed → gate never wired
2. **EXQ-049b**: gate wired, `post_action_update` missing → variance frozen
3. **EXQ-049c**: `post_action_update` called, but its own `_committed_trajectory` guard
   re-creates the deadlock — variance still never moves
4. **EXQ-049d**: `update_running_variance(wf_err)` called directly → deadlock broken

## Training Diagnostics

| Metric | Value |
|--------|-------|
| final_running_variance (post-train) | 0.0000 |
| mean_committed_fraction (train) | 1.000 |
| commit_threshold | 0.400 |

## Beta Gate Concordance

| State | Count | Rate |
|-------|-------|------|
| committed + gate elevated (correct hold) | 10000 | 1.000 |
| committed + gate NOT elevated (unexpected) | 0 | 0.000 |
| uncommitted + NOT elevated (correct release) | 0 | 0.000 |
| uncommitted + gate elevated (unexpected) | 0 | 1.000 |

- hold_count (total gate holds): 10347
- propagation_count (total gate releases): 3
- mean_running_variance (eval): 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: committed_hold_concordance > 0.6 | PASS | 1.000 |
| C2: uncommitted_release_concordance > 0.5 | FAIL | 0.000 |
| C3: hold_count > 0 (gate holds) | PASS | 10347 |
| C4: propagation_count > 0 (gate releases) | PASS | 3 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 -> **FAIL**

## Failure Notes

- C2 FAIL: uncommitted_release_concordance=0.000 <= 0.5
