# V3-EXQ-014 — Perspective Shift Calibration

**Status:** PASS
**Training:** 300 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Eval:** 100 eps
**Seed:** 0

## Motivation (SD-007 / MECH-098)

EXQ-012 revealed true calibration_gap ≈ 0.0007 — near-zero. Root cause: E2_world
takes an identity shortcut because the egocentric world_obs changes on every body
movement (perspective shift), not genuine world change. This experiment quantifies
that problem before implementing the reafference correction (SD-007).

## Mean ||Δz_world|| by Event Type

| Event Type | n | Mean Δz_world |
|---|---|---|
| empty_move (locomotion only) | 1341 | 0.0546 |
| env_caused_hazard (genuine world event) | 149 | 0.0569 |
| agent_caused_hazard | 91 | 0.0457 |

**Perspective shift dominance ratio:** 0.960
(ratio > 1.0 = locomotion induces more z_world change than genuine world events — the problem)

## Reafference Predictor (linear fit)

Linear predictor `Δz_world = W @ [z_self; action] + b` trained on empty-space steps:
- R² (train): 0.378
- R² (test, held-out empty steps): 0.333
- **Locomotion explained variance: 0.333**

High R² on held-out empty steps confirms that z_self + action can predict the
z_world change caused by locomotion — i.e., that z_world encodes perspective shift.
This is the perspective shift that SD-007 must subtract.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: locomotion_explained_variance > 0.3 | PASS | 0.333 |
| C2: mean_dz_world_env_hazard > mean_dz_world_empty | PASS | 0.0569 vs 0.0546 |
| C3: n_empty >= 200 | PASS | 1341 |
| C4: No fatal errors | PASS | 0 |

Criteria met: 4/4 → **PASS**
