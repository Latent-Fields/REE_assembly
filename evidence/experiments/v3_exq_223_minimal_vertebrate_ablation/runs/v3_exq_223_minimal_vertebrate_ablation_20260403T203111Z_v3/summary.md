# V3-EXQ-223 -- Minimal Vertebrate Cognition Ablation

**Status:** FAIL
**Purpose:** Milestone validation -- core E1/E2/hippocampus loop as gradient-follower
**Ablation:** commitment_threshold=-1.0 (always uncommitted, no argmin, no BetaGate hold)
             z_goal_enabled=False, benefit_eval_enabled=False, goal_weight=0.0
**Warmup:** 100 eps | **Eval:** 50 eps | **Seeds:** [0, 1, 2]

## Evolutionary Hypothesis

If REE correctly decomposes vertebrate cognition, the minimal loop
(E1 associations + E2 transitions + hippocampal sequences + multinomial
go/no-go + raw harm/goal signals) should produce gradient-following
behavior without the commitment architecture.

Sidesteps SD-011 (z_world perp z_harm) and SD-012 (z_goal seeding failures)
by using raw environmental signals, not latent harm/goal substrates.

## Ablation Config

- commitment_threshold = -1.0  (committed = rv < -1.0 = always False)
- z_goal_enabled = False
- benefit_eval_enabled = False
- goal_weight = 0.0

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
| 0 | -0.3981 | -0.3981 | 0.0000 | -0.3104 | -0.9606 | 0.4499 | 1.2352 | 0.3642 | 32.0 |
| 1 | -0.3124 | -0.3124 | 0.0000 | 0.1195 | -0.8908 | 0.4308 | 1.1582 | 0.3719 | 32.0 |
| 2 | -0.0750 | -0.0750 | 0.0000 | -0.7063 | -0.8252 | 0.7063 | 1.1044 | 0.6395 | 32.0 |

## PASS Criteria

| Criterion | Seeds passing | Required | Result |
|-----------|--------------|---------|--------|
| C1 ree > rand reward | 3/3 | >=2 | PASS |
| C2 harm ratio < 1.0 | 3/3 | >=2 | PASS |
| C3 n_cands >= 2 (info) | 3/3 | informational | PASS |
| C4 warmup improvement > 0 | 0/3 | >=2 | FAIL |

Criteria met (C1+C2+C4): 2/3 -> **FAIL**

## Failure Notes

- C4 FAIL: warmup improvement > 0 in 0/3 seeds (need 2); deltas=['0.0000', '0.0000', '0.0000']
