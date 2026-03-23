# V3-EXQ-065 -- MECH-029: Default Mode Probe

**Status:** FAIL
**Claim:** MECH-029 -- default mode (uncommitted/idle) shows higher z_world variance and E3 uncertainty than committed execution
**Design:** Single-condition; label each eval step as committed or uncommitted; compare latent variance distributions
**alpha_world:** 0.9  |  **Train:** 500 eps  |  **Eval:** 100 eps  |  **Seed:** 0

## Design Rationale

Committed execution is a convergent, low-variance state: E3 has selected a trajectory,
the world model is relatively stable, and E3 precision is high (running_variance low).
Uncommitted / default mode is divergent: E3 is exploring, z_world is varying across
candidate world models, and E3 remains uncertain. The ratio of uncommitted/committed
variance is the key readout.

Commitment criterion: running_variance < commit_threshold (ARC-016).

## z_world Variance by Mode

| Mode | z_world_var | E3 running_var_mean | step_count |
|------|------------|---------------------|------------|
| Committed | 0.000076 | 0.000001 | 20000 |
| Uncommitted (default) | 0.000000 | 0.000000 | 0 |

**z_world_var_ratio** (uncommitted/committed) = 0.0000
**e3_var_ratio** (uncommitted/committed) = 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: uncommitted_z_world_var > committed * 1.1 | FAIL | 0.000000 vs 0.000083 |
| C2: uncommitted_e3_var > committed * 1.05 | FAIL | 0.000000 vs 0.000001 |
| C3: both modes >= 20 steps | FAIL | committed=20000 uncommitted=0 |
| C4: harm_pred_std > 0.01 (E3 not collapsed) | PASS | 0.1063 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C1 FAIL: uncommitted_z_world_var=0.000000 <= committed_z_world_var*1.1=0.000083
- C2 FAIL: uncommitted_e3_var_mean=0.000000 <= committed_e3_var_mean*1.05=0.000001
- C3 FAIL: committed_steps=20000  uncommitted_steps=0  (both need >= 20)
