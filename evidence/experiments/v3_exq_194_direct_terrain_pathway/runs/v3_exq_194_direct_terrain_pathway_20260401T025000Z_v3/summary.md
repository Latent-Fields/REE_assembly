# V3-EXQ-194 -- Direct z_world Terrain Pathway (MECH-152 Isolation)

**Status:** MIXED
**Claims:** MECH-152
**Seeds:** [42, 7, 11]

## Context

EXQ-182 (sd016_terrain_calibration) FAIL: supervised terrain_loss through ContextMemory produced r_w_harm=0.01 because ContextMemory slots are non-differentiable EMA -- attention is uniform regardless of z_world. This experiment bypasses ContextMemory with a direct Linear(32,32)->ReLU->Linear(32,2)->Sigmoid pathway from z_world to terrain_weight, trained with the same terrain_loss.

## Design

**Phase 0 (warmup):** 200 episodes x 200 steps. E1 + E2 losses + terrain_loss (lambda=0.1). Adam lr=1e-3, alpha_world=0.9, num_hazards=1. TerrainHead is a standalone nn.Module.

**Phase 1 (collection):** 100 episodes x 200 steps. Random actions. Record terrain_weight and hazard_prox at each step.

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| r(w_harm, hazard_prox) | 0.6970 | > 0.5 |
| r(w_goal, hazard_prox) | -0.0067 | < -0.3 |
| final terrain_loss | 0.0183 | < 0.05 |
| n_context_A steps (total) | 2095 | -- |
| n_context_B steps (total) | 1360 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: r(w_harm, hazard_prox) > 0.5 | PASS | 3/3 |
| C2: r(w_goal, hazard_prox) < -0.3 | FAIL | 1/3 |
| C3: terrain_loss < 0.05 | PASS | 3/3 |

PASS rule: all three pass in >= 2/3 seeds -> **MIXED**

## Interpretation

C1 PASS: r_w_harm=0.6970 > 0.5 in 3/3 seeds. Direct pathway w_harm tracks hazard proximity.

C2 FAIL: r_w_goal=-0.0067 >= -0.3 (passed 1/3 seeds). Direct pathway w_goal does not inversely track hazard proximity.

C3 PASS: final_terrain_loss=0.0183 < 0.05 in 3/3 seeds. Terrain head converged.

## Per-Seed Results

  seed=42: n_A=719 n_B=378 r_w_harm=0.5775 r_w_goal=-0.5117 terrain_loss=0.0180 w_harm: A=0.844 B=0.687 w_goal: A=0.301 B=0.305 C1=PASS C2=PASS C3=PASS
  seed=7: n_A=739 n_B=490 r_w_harm=0.8301 r_w_goal=0.2611 terrain_loss=0.0054 w_harm: A=0.883 B=0.734 w_goal: A=0.304 B=0.304 C1=PASS C2=FAIL C3=PASS
  seed=11: n_A=637 n_B=492 r_w_harm=0.6833 r_w_goal=0.2305 terrain_loss=0.0315 w_harm: A=0.730 B=0.599 w_goal: A=0.307 B=0.304 C1=PASS C2=FAIL C3=PASS
