# V3-EXQ-189 -- MECH-112 Goal Present vs Absent

**Status:** FAIL
**Claims:** MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Dispatch mode:** discriminative_pair

## Design

Two-condition discriminative pair: GOAL_PRESENT (z_goal + benefit_eval active) vs GOAL_ABSENT (both ablated). Matched seeds, identical architecture otherwise.
GOAL_PRESENT eval: harm - benefit - goal_proximity scoring.
GOAL_ABSENT eval: harm-only scoring.
Warmup: 50% proximity-greedy navigation to ensure z_goal seeds.

## Results

| Metric | GOAL_PRESENT | GOAL_ABSENT |
|---|---|---|
| resource_collection_rate | 0.193 | 0.170 |
| mean_resources_per_ep | 0.24 | 0.21 |
| mean_benefit | 0.00353 | 0.00170 |
| harm_rate | 0.18624 | 0.12568 |

**benefit_eval_auc (GOAL_PRESENT):** 0.5387
**goal_norm_final (GOAL_PRESENT avg):** 0.2962

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: resource_lift >= 0.03 | FAIL | +0.023 |
| C2: benefit_ratio >= 1.15x | PASS | 2.07x |
| C3: harm_ratio <= 1.3x | FAIL | 1.48x |
| C4: goal_norm >= 0.05 | PASS | 0.2962 |

Criteria met: 2/4 -> **FAIL**

## Per-Seed

  seed=42: gp_res=0.130 ga_res=0.190 gp_ben=0.00492 ga_ben=0.00164 goal_norm=0.3530
  seed=7: gp_res=0.220 ga_res=0.180 gp_ben=0.00366 ga_ben=0.00255 goal_norm=0.2313
  seed=13: gp_res=0.230 ga_res=0.140 gp_ben=0.00201 ga_ben=0.00091 goal_norm=0.3042

## Failure Notes

- C1 FAIL: resource_lift=+0.023 < 0.03. GOAL_PRESENT does not collect more resources.
- C3 FAIL: harm_ratio=1.48x > 1.3x. Goal pursuit causes catastrophic harm regression.
