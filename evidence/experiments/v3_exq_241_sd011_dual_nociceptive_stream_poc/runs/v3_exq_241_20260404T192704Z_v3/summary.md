# V3-EXQ-241 -- SD-011 Dual Nociceptive Stream POC

**Status:** FAIL  **Criteria met:** 1/3
**Claims:** SD-011  **Purpose:** diagnostic

## Design

Standalone dual-stream harm encoder validation (no ree_core changes required).
HarmEncoder(harm_obs [51]) -> z_harm_s [32] (sensory-discriminative, A-delta analog).
AffectiveHarmEncoder(harm_obs_a [50]) -> z_harm_a [16] (affective-motivational, C-fiber analog).
Forward probes: MLP(z_world, action) -> z_harm_s_next and -> z_harm_a_next.

## Results by Seed

| Seed | cos_sim | R2_s | R2_a | hr_single | hr_dual_s | D1 | D2 | D3 | D4 |
|------|---------|------|------|-----------|-----------|----|----|----|----|
| 42 | 0.2360 | -0.3197 | -0.0964 | 0.8750 | 1.0000 | PASS | FAIL | FAIL | FAIL |

## Interpretation

SD-011 NOT CONFIRMED: Dual-stream separation not observed. Possible causes: encoders not diverging (same input structure), insufficient training steps, or env too uniform for stream separation.

## Failure Notes

- D2 FAIL: R2(z_harm_s forward) < 0.3 in 1 seeds: [-0.3197]. Sensory stream not forward-predictable from (z_world, action).
- D3 FAIL: R2(z_harm_a) >= R2(z_harm_s) in 1 seeds: [(-0.3197, -0.0964)]. Affective stream should be less predictable than sensory stream.
