# V3-EXQ-194a -- Direct Terrain Pathway, Phased Training (MECH-152)

**Status:** MIXED
**Claims:** MECH-152
**Supersedes:** V3-EXQ-194
**Seeds:** [42, 7, 11]

## Context

EXQ-194 MIXED: C1 PASS (r_w_harm=0.70) but C2 FAIL (r_w_goal=-0.007). Two fixes: (1) phased training (P0 E1+E2 warmup, P1 frozen-encoder TerrainHead) per 166e lesson; (2) corrected w_goal threshold (< 0.33 not < 0.1) to produce non-trivial goal-high label distribution.

## Design

**Phase 0 (E1+E2 warmup):** 200 episodes x 200 steps. E1 + E2 losses only. No terrain_loss. z_world converges.

**Phase 1 (TerrainHead training):** 100 episodes x 200 steps. E1+E2 frozen. TerrainHead trained on z_world.detach() with terrain_loss. Labels: w_harm=0.8 if haz>0.3 else 0.2; w_goal=0.8 if haz<0.33 else 0.2.

**Phase 2 (collection):** 100 episodes x 200 steps. Random actions. Record terrain_weight and hazard_prox.

## Key Results

| Metric | Value | Threshold |
|---|---|---|
| r(w_harm, hazard_prox) | 0.4128 | > 0.5 |
| r(w_goal, hazard_prox) | -0.4130 | < -0.3 |
| final terrain_loss | 0.0335 | < 0.05 |
| n_context_A (total) | 2349 | -- |
| n_context_B (total) | 1303 | -- |

## Pass Criteria

| Criterion | Result | Seeds passing |
|---|---|---|
| C1: r(w_harm, hazard_prox) > 0.5 | FAIL | 0/3 |
| C2: r(w_goal, hazard_prox) < -0.3 | PASS | 3/3 |
| C3: terrain_loss < 0.05 | PASS | 2/3 |

PASS rule: all three pass in >= 2/3 seeds -> **MIXED**

## Interpretation

C1 FAIL: r_w_harm=0.4128 <= 0.5 (passed 0/3 seeds). Direct pathway w_harm does not track hazard proximity even on stable z_world.

C2 PASS: r_w_goal=-0.4130 < -0.3 in 3/3 seeds. Direct pathway w_goal inversely tracks hazard -- goal upweighted when safe. Corrected threshold (< 0.33) provides sufficient goal-high label coverage.

C3 PASS: final_terrain_loss=0.0335 < 0.05 in 2/3 seeds. Terrain head converged on stable z_world.

## Per-Seed Results

  seed=42: n_A=774 n_B=329 r_w_harm=0.4682 r_w_goal=-0.4683 terrain_loss=0.0082 w_harm: A=0.719 B=0.711 w_goal: A=0.280 B=0.288 C1=FAIL C2=PASS C3=PASS
  seed=7: n_A=812 n_B=449 r_w_harm=0.3850 r_w_goal=-0.3862 terrain_loss=0.0688 w_harm: A=0.740 B=0.731 w_goal: A=0.259 B=0.270 C1=FAIL C2=PASS C3=FAIL
  seed=11: n_A=763 n_B=525 r_w_harm=0.3854 r_w_goal=-0.3845 terrain_loss=0.0234 w_harm: A=0.701 B=0.694 w_goal: A=0.300 B=0.307 C1=FAIL C2=PASS C3=PASS
