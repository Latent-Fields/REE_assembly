# V3-EXQ-010 — SD-003 Larger World + 3×3 Observation

**Status:** FAIL
**Environment:** 12×12 grid, 15 hazards, 3×3 local view
**world_obs_dim:** 72 (vs 200 in standard 5×5 view)
**Warmup:** 400 episodes, RANDOM policy + recon loss + 5-step E2 rollouts + target stopgrad
**Probe eval:** 10 grid resets x (near-hazard + safe positions)
**Seed:** 0

## Hypothesis

The E2 identity shortcut may be caused by insufficient per-step observation
change. In a 5×5 view, moving one cell changes ~20% of pixels. In a 3×3 view,
each step changes ~44%. Combined with a larger grid and more hazards, z_world
should encode genuinely different states each step.

A PASS here is a positive scalability signal: real-world observations change
substantially each timestep, matching this condition more than the 5×5 view.

Mean E2 world loss: 0.027756 (compare r6: 0.000311 on 5×5 view)
Mean reconstruction loss: 0.01827

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: TRAINED calibration_gap > 0.05 | FAIL | 0.0267 |
| C2: RANDOM abs(calibration_gap) < 0.10 | PASS | 0.0001 |
| C3: Warmup harm events > 100 | PASS | 1038 |
| C4: No fatal errors | PASS | 0 |
| C5: harm_eval non-degenerate | PASS | OK |
| C6: Probe coverage >= 10 each | PASS | near=421 safe=60 |

## Calibration Results (Probe-Based)

| Condition | mean_causal_sig(near_hazard) | mean_causal_sig(safe) | calibration_gap |
|---|---|---|---|
| TRAINED | -0.0393 | -0.0660 | 0.0267 |
| RANDOM  | -0.0001 | -0.0000 | -0.0001 |

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL: TRAINED calibration_gap 0.0267 <= 0.05
