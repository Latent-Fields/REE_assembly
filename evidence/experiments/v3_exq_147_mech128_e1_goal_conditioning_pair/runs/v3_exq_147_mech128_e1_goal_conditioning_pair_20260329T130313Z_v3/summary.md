# V3-EXQ-147 -- MECH-128 / Q-002: E1 Goal-Conditioning Discriminative Pair

**Status:** FAIL
**Claims:** MECH-128, Q-002
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** GOAL_CONDITIONED vs GOAL_ABLATED at world_dim=32 (primary) and world_dim=16 (Q-002 resolution probe)
**Warmup:** 400 eps x 200 steps  **Eval:** 120 eps x 200 steps
**Env:** CausalGridWorldV2 size=10, 2 hazards, 3 resources

## Design

MECH-128 asserts E1's LSTM must be conditioned on z_goal_latent so that E1's predictive distribution is shaped by goal context rather than being goal-agnostic. GOAL_CONDITIONED: config.e1.goal_dim=world_dim (goal_input_proj active). GOAL_ABLATED: config.e1.goal_dim=0 (goal_input_proj disabled; z_goal withheld from E1 input).

Key metric: interaction = (err_neutral_ablated - err_neutral_conditioned) - (err_goal_ablated - err_goal_conditioned). Positive = goal context selectively reduces goal-relevant prediction error (MECH-128 signature).

Q-002 probe: compare err_all at world_dim=32 vs world_dim=16. If world_dim=32 is no worse (ratio <= 1.1x), finer resolution is at least neutral and likely beneficial.

## Pre-Registered Thresholds

C1: interaction_32 >= 0.005 (both seeds)
C2: err_goal_conditioned < err_goal_ablated at dim=32 (both seeds)
C3: |neutral_diff_32| < 0.03 (both seeds)
C4 (Q-002): err_all(dim=32) <= err_all(dim=16) * 1.1 (both seeds)
C5: interaction_16 >= 0.003 (both seeds)

## Results

### Primary (world_dim=32)

| Condition | err_goal | err_neutral | err_all |
|-----------|----------|-------------|----------|
| GOAL_CONDITIONED | 0.00026 | 0.00026 | 0.00026 |
| GOAL_ABLATED     | 0.00023 | 0.00023 | 0.00023 |

**interaction_32 per seed: [-1e-05, -0.0]**
**goal_diff (ablated-cond) per seed: [-3e-05, -2e-05]**
**neutral_diff (ablated-cond) per seed: [-4e-05, -2e-05]**

### Q-002 Resolution Probe (dim=16 vs dim=32)

| Condition | err_all (dim=32) | err_all (dim=16) |
|-----------|-----------------|------------------|
| GOAL_CONDITIONED | 0.00026 | 0.00030 |
| GOAL_ABLATED     | 0.00023 | 0.00025 |

**interaction_16 per seed: [-1e-05, 0.0]**

### GOAL_CONDITIONED per seed (dim=32)
  seed=42 dim=32: err_goal=0.00032 err_neutral=0.00032 err_all=0.00032 goal_norm=0.3636 n_goal=1609 n_neutral=430
  seed=123 dim=32: err_goal=0.00019 err_neutral=0.00019 err_all=0.00019 goal_norm=0.4251 n_goal=1572 n_neutral=405

### GOAL_ABLATED per seed (dim=32)
  seed=42 dim=32: err_goal=0.00029 err_neutral=0.00029 err_all=0.00029 goal_norm=0.3619 n_goal=1609 n_neutral=430
  seed=123 dim=32: err_goal=0.00018 err_neutral=0.00017 err_all=0.00018 goal_norm=0.4221 n_goal=1572 n_neutral=405

## PASS Criteria

| Criterion | Result |
|-----------|--------|
| C1: interaction_32 >= 0.005 (both seeds) | FAIL |
| C2: err_goal_cond < err_goal_abla at dim=32 (both seeds) | FAIL |
| C3: |neutral_diff_32| < 0.03 (both seeds) | PASS |
| C4 (Q-002): err_all(32) <= err_all(16)*1.1 (both seeds) | PASS |
| C5: interaction_16 >= 0.003 (both seeds) | FAIL |

Criteria met: 2/5 -> **FAIL**

## Interpretation

MECH-128 NOT CONFIRMED: goal conditioning does not produce differential E1 prediction error on goal-relevant transitions. interaction_32=-0.00000 (target >= 0.005). err_goal: COND=0.00026 vs ABLA=0.00023. err_neutral: COND=0.00026 vs ABLA=0.00023. Only 2/5 criteria met. Possible interpretation: E1 LSTM captures goal-relevant dynamics from sequential observations alone; explicit z_goal injection (MECH-128) adds no additional predictive signal at current world scale.

## Failure Notes

- C1 FAIL: interaction_32 [-1e-05, -0.0] < 0.005. Goal conditioning does not produce a differential reduction in goal-zone prediction error vs neutral. Possible causes: (1) goal_input_proj wiring is correct but z_goal is not seeded from benefit (benefit_eval_enabled may not fire); check goal_norm > 0 at eval. (2) The LSTM hidden state already captures goal context from sequential observations without explicit z_goal injection; MECH-128 redundant. (3) world_dim=32 representation too compact for E1 to distinguish goal-relevant vs neutral world transitions.
- C2 FAIL: err_goal_conditioned NOT < err_goal_ablated for [0.00032, 0.00019] vs [0.00029, 0.00018]. E1 prediction error is not lower when goal context is provided. This may indicate goal_input_proj is not receiving useful z_goal signal, or benefit events are too rare for z_goal to stabilise.
- C5 FAIL: interaction_16 [-1e-05, 0.0] < 0.003. Goal conditioning interaction does not replicate at world_dim=16. MECH-128 effect may be resolution-dependent.
