# V3-EXQ-033 — Training Depth vs. Gradient Detection Depth
            "Love Expands Under Intelligence" Computational Test

**Status:** FAIL
**Claims:** ARC-024, MECH-071, INV-029
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0

## Philosophical Basis

From Philosophy/notes/2026-03-18_love_once_means_love_all.md:
    "Love enters as a point commitment and expands, under intelligence and uncertainty,
    until it covers everything."

Computational prediction: with increasing training (capability), E3 detects harm
gradients further back along the causal chain. Approach detection (one step from contact)
should improve faster than contact detection (the endpoint), because the gradient
representation requires a richer causal model.

approach_slope > contact_slope → gradient extends backward with intelligence.

## Calibration Curve

| eps | none | approach | contact | gap_approach | gap_contact | n_approach |
|---|---|---|---|---|---|---|
|  100 | 0.489 | 0.494 | 0.494 | 0.0059 | 0.0053 | 499 |
|  250 | 0.430 | 0.558 | 0.542 | 0.1278 | 0.1139 | 501 |
|  500 | 0.347 | 0.632 | 0.634 | 0.2852 | 0.2756 | 532 |
| 1000 | 0.382 | 0.627 | 0.651 | 0.2448 | 0.2650 | 448 |

- **Approach slope**: 0.000265 per episode
- **Contact slope**:  0.000289 per episode
- **Slope ratio** (approach/contact): 0.920

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_approach[1000] > gap_approach[100] + 0.05 (grows with training) | PASS | 0.2448 vs 0.0059 |
| C2: gap_approach[500] > gap_approach[100] (monotonic in first half) | PASS | 0.2852 vs 0.0059 |
| C3: gap_approach[1000] > 0.10 (non-trivial at endpoint) | PASS | 0.2448 |
| C4: approach_slope > contact_slope (CORE — gradient deepens faster) | FAIL | 0.000265 vs 0.000289 |
| C5: n_approach_min >= 20 (sufficient events at each checkpoint) | PASS | 448 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C4 FAIL: approach_slope(0.000265/ep) <= contact_slope(0.000289/ep)
