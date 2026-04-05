# V3-EXQ-241 -- SD-011 Dual Nociceptive Stream POC

**Status:** FAIL  **Criteria met:** 2/3
**Claims:** SD-011  **Purpose:** diagnostic

## Design

Standalone dual-stream harm encoder validation (no ree_core changes required).
HarmEncoder(harm_obs [51]) -> z_harm_s [32] (sensory-discriminative, A-delta analog).
AffectiveHarmEncoder(harm_obs_a [50]) -> z_harm_a [16] (affective-motivational, C-fiber analog).
Forward probes: MLP(z_world, action) -> z_harm_s_next and -> z_harm_a_next.

## Results by Seed

| Seed | cos_sim | R2_s | R2_a | hr_single | hr_dual_s | D1 | D2 | D3 | D4 |
|------|---------|------|------|-----------|-----------|----|----|----|----|
| 42 | 0.2124 | 0.9136 | 0.9719 | 0.8640 | 0.8576 | PASS | PASS | FAIL | PASS |
| 7 | -0.2142 | 0.9427 | 0.9806 | 0.8683 | 0.7893 | PASS | PASS | FAIL | PASS |
| 13 | -0.1947 | 0.9199 | 0.9697 | 0.8531 | 0.8442 | PASS | PASS | FAIL | PASS |
| 99 | -0.1191 | 0.9168 | 0.9678 | 0.8665 | 0.7682 | PASS | PASS | FAIL | PASS |
| 17 | -0.0777 | 0.9410 | 0.9654 | 0.8101 | 0.7772 | PASS | PASS | FAIL | PASS |

## Interpretation

SD-011 PARTIAL: D1 (orthogonality) D2 (sensory predictability) met. Check failure criteria for diagnostic guidance.

## Failure Notes

- D3 FAIL: R2(z_harm_a) >= R2(z_harm_s) in 5 seeds: [(0.9136, 0.9719), (0.9427, 0.9806), (0.9199, 0.9697), (0.9168, 0.9678), (0.941, 0.9654)]. Affective stream should be less predictable than sensory stream.
