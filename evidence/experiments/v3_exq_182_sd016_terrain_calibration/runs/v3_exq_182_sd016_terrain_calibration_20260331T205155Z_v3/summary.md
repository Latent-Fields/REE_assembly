# V3-EXQ-182 -- Supervised Terrain Calibration (MECH-150 / ARC-041)

**Status:** FAIL
**Claims:** MECH-150, ARC-041
**Seeds:** [42, 7, 11]

## Context

EXQ-181/181b showed that ContextMemory does not spontaneously produce differentiated cue content (cosine_sim=0.9999 without supervised training). This experiment adds a supervised terrain_loss (lambda=0.1) using hazard_field_view.max() as proxy label, training the full extract_cue_context() projection pathway end-to-end.

## Design

**Phase 0 (warmup):** 200 episodes x 200 steps. E1 + E2 losses + terrain_loss (lambda=0.1). Adam lr=1e-3, alpha_world=0.9, sd016_enabled=True, num_hazards=1.

**Phase 1 (collection):** 100 episodes x 200 steps. Random actions. At each step: extract_cue_context(z_world) -> record cue_context, terrain_weight. Context A: hazard_max > 0.7. Context B: hazard_max < 0.33.

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| cosine_sim(mean_A, mean_B) | 1.0000 | < 0.85 |
| r(w_harm, hazard_prox) | 0.0101 | > 0.5 |
| r(w_goal, hazard_prox) | 0.1159 | < -0.3 |
| n_context_A steps (total) | 2095 | -- |
| n_context_B steps (total) | 1360 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: cosine_sim < 0.85 | FAIL | 0/3 |
| C2: r(w_harm, hazard_prox) > 0.5 | FAIL | 0/3 |
| C3: r(w_goal, hazard_prox) < -0.3 | FAIL | 0/3 |

PASS rule: all three criteria pass in >= 2/3 seeds -> **FAIL**

## Interpretation

C1 FAIL: cosine_sim=1.0000 >= 0.85 (passed 0/3 seeds). Cue context does NOT differentiate despite supervised training. Possible causes: lambda_terrain too low, insufficient warmup, or ContextMemory EMA slots lack sufficient diversity.

C2 FAIL: r_w_harm=0.0101 <= 0.5 (passed 0/3 seeds). w_harm does not reliably track hazard proximity.

C3 FAIL: r_w_goal=0.1159 >= -0.3 (passed 0/3 seeds). w_goal does not inversely track hazard proximity.

## Per-Seed Results

  seed=42: n_A=719 n_B=378 cos_sim=1.0 r_w_harm=0.0000 r_w_goal=0.1239 terrain_loss=0.0254 C1=FAIL C2=FAIL C3=FAIL
  seed=7: n_A=739 n_B=490 cos_sim=1.0 r_w_harm=0.0303 r_w_goal=-0.0316 terrain_loss=0.0054 C1=FAIL C2=FAIL C3=FAIL
  seed=11: n_A=637 n_B=492 cos_sim=0.9999999403953552 r_w_harm=0.0000 r_w_goal=0.2553 terrain_loss=0.0297 C1=FAIL C2=FAIL C3=FAIL
