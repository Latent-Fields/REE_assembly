# V3-EXQ-223a -- Toroidal Minimal Vertebrate Cognition Ablation

**Status:** FAIL
**Purpose:** Hypothesis generation -- does minimal mind survive without walls to exploit?
**Toroidal:** no walls; movement and hazard drift wrap at grid edges
**Ablation:** commitment_threshold=-1.0 (always uncommitted, no argmin, no BetaGate hold)
             z_goal_enabled=False, benefit_eval_enabled=False, goal_weight=0.0
**Warmup:** 100 eps | **Eval:** 50 eps | **Seeds:** [0, 1, 2]

## Scientific Question

EXQ-223 passed via wall-hugging: agent moved in one direction to a wall
corner and stayed there. This provides free hazard avoidance because
jellyfish drift only within the interior. The minimal mind may have no
genuine gradient-following beyond exploiting this boundary effect.

With toroidal wrapping, walls are removed. If PASS: the minimal loop has
genuine spatial gradient-following beyond wall refuge. If FAIL: EXQ-223
result was entirely boundary-dependent.

Secondary question: does the agent develop a spatial preference (row/column
half of grid), indicating z_world encodes more than the immediate 5x5 view?

## Pre-registered Thresholds

| Criterion | Threshold | Seed requirement |
|-----------|-----------|-----------------|
| C1: ree_reward > rand_reward | > 0.0 | >= 2/3 seeds |
| C2: harm_ratio (ree/rand) | < 1.0 | >= 2/3 seeds |
| C3: n_cands per e3 tick (info) | >= 2 | informational |
| C4: warmup improvement delta | > 0.0 | >= 2/3 seeds |

## Results by Seed

| Seed | W-first25 | W-last25 | W-delta | REE reward | rand reward | REE harm | rand harm | harm ratio | n_cands |
|------|-----------|----------|---------|------------|------------|---------|----------|-----------|---------|
| 0 | -0.9414 | -0.9536 | -0.0122 | -0.9646 | -0.9976 | 1.0609 | 1.0773 | 0.9848 | 32.0 |
| 1 | -0.9222 | -0.9718 | -0.0496 | -0.8913 | -0.9438 | 1.1214 | 1.1052 | 1.0147 | 32.0 |
| 2 | -0.9427 | -0.9346 | 0.0081 | -0.9377 | -0.9753 | 1.0901 | 1.1042 | 0.9873 | 32.0 |

## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|--------------|---------|--------|
| C1 ree > rand reward | 3/3 | >=2 | PASS |
| C2 harm ratio < 1.0 | 2/3 | >=2 | PASS |
| C3 n_cands >= 2 (info) | 3/3 | informational | PASS |
| C4 warmup improvement > 0 | 1/3 | >=2 | FAIL |

Criteria met (C1+C2+C4): 2/3 -> **FAIL**

## Failure Notes

- C4 FAIL: warmup improvement > 0 in 1/3 seeds (need 2); deltas=['-0.0122', '-0.0496', '0.0081']
