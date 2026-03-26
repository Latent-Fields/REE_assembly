# V3-EXQ-098 -- MECH-099 Three-Stream vs Two-Stream Harm Channel

**Status:** FAIL
**Claims:** MECH-099
**Seeds:** [42]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 5 eps  **Eval:** 3 eps

## Pre-Registered Thresholds

C1: auc_THREE - auc_TWO >= 0.05  (harm_event_AUC improvement)
C2: r2_world_THREE / r2_world_TWO <= 0.80  (z_world purity, MECH-069)
C3: avoidance_THREE >= avoidance_TWO  (behavioral, flee policy)

## Aggregate Results

| Metric | THREE_STREAM | TWO_STREAM | Delta/Ratio | Pass |
|--------|-------------|-----------|-------------|------|
| harm_event_AUC | 0.5000 | 0.5000 | +0.0000 | NO |
| z_world_harm_R2 | 0.0000 | 0.0000 | 0.0000 | YES |
| harm_avoidance | 0.0000 | 0.0000 | +0.0000 | YES |

## Interpretation

MECH-099 NOT SUPPORTED at this training budget/scale. AUC delta=+0.0000 (C1 needs 0.05). Lateral head did not produce a cleaner harm signal than z_world. Possible causes: lateral_head input (HAZARD_INDICES + contamination_view) insufficient for 400-episode training; world_obs_encoder shared weights create interference; or both conditions reach similar representation quality.

## Per-Seed (THREE_STREAM)

  seed=42: auc=0.5000 r2_world=0.0000 avoidance=0.0000 harm_events_train=95

## Per-Seed (TWO_STREAM)

  seed=42: auc=0.5000 r2_world=0.0000 avoidance=0.0000 harm_events_train=95

## Failure Notes

- C1 FAIL: auc_THREE=0.5000 vs auc_TWO=0.5000 (delta=+0.0000, needs >=0.05). Lateral head did not improve harm event AUC by 5pp.
