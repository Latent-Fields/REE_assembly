# V3-EXQ-223a -- Toroidal Minimal Vertebrate Cognition Ablation

**Status:** FAIL
**Purpose:** Hypothesis generation -- does minimal mind survive without walls to exploit?
**Toroidal:** no walls; movement and hazard drift wrap at grid edges
**Ablation:** commitment_threshold=-1.0 (always uncommitted, no argmin, no BetaGate hold)
             z_goal_enabled=False, benefit_eval_enabled=False, goal_weight=0.0
**Warmup:** 100 eps | **Eval:** 50 eps | **Seeds:** [0]

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
| C1: ree_reward > rand_reward | > 0.0 | >= 2/1 seeds |
| C2: harm_ratio (ree/rand) | < 1.0 | >= 2/1 seeds |
| C3: n_cands per e3 tick (info) | >= 2 | informational |
| C4: warmup improvement delta | > 0.0 | >= 2/1 seeds |

## Results by Seed

| Seed | W-first25 | W-last25 | W-delta | REE reward | rand reward | REE harm | rand harm | harm ratio | n_cands |
|------|-----------|----------|---------|------------|------------|---------|----------|-----------|---------|
| 0 | -0.9756 | -0.9756 | 0.0000 | -0.9288 | -0.9662 | 1.0708 | 1.1018 | 0.9718 | 32.0 |

## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|--------------|---------|--------|
| C1 ree > rand reward | 1/1 | >=2 | FAIL |
| C2 harm ratio < 1.0 | 1/1 | >=2 | FAIL |
| C3 n_cands >= 2 (info) | 1/1 | informational | info |
| C4 warmup improvement > 0 | 0/1 | >=2 | FAIL |

Criteria met (C1+C2+C4): 0/3 -> **FAIL**

## Failure Notes

- C1 FAIL: ree>rand in 1/1 seeds (need 2); ree=['-0.9288'] rand=['-0.9662']
- C2 FAIL: harm_ratio < 1.0 in 1/1 seeds (need 2); ratios=['0.9718']
- C4 FAIL: warmup improvement > 0 in 0/1 seeds (need 2); deltas=['0.0000']
