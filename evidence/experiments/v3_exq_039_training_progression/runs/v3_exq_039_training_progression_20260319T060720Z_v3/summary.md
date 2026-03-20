# V3-EXQ-039 — Training Progression Analysis

**Status:** FAIL
**Claims:** MECH-071, ARC-024
**World:** CausalGridWorldV2 (proximity_scale=0.05)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0
**Predecessor:** EXQ-033 (FAIL — C4: approach_slope ≤ contact_slope with 4 checkpoints)

## Motivation

EXQ-033 used 4 checkpoints (100, 250, 500, 1000 episodes) and found approach_slope=0.000265
vs contact_slope=0.000289. The hierarchical prediction is that approach detection should
emerge faster (gradient signal is observable before contact). EXQ-039 tests with 16
checkpoints (every 50 episodes over 800 total) for much more reliable slope estimation.

## Checkpoint Progression

| Episode | gap_approach | gap_contact | n_approach | n_contact |
|---|---|---|---|---|
|   50 | -0.0008 | -0.0016 |  320 |   14 |
|  100 | 0.0038 | 0.0039 |  340 |   19 |
|  150 | 0.0140 | 0.0277 |  316 |   19 |
|  200 | 0.0514 | 0.0354 |  305 |   17 |
|  250 | 0.0602 | 0.0629 |  324 |   21 |
|  300 | 0.1074 | 0.0960 |  339 |   16 |
|  350 | 0.1110 | 0.0908 |  316 |   16 |
|  400 | 0.1352 | 0.1245 |  335 |   21 |
|  450 | 0.1646 | 0.0933 |  356 |   20 |
|  500 | 0.1690 | 0.0733 |  317 |   22 |
|  550 | 0.1631 | 0.1446 |  303 |   20 |
|  600 | 0.2085 | 0.1984 |  332 |   17 |
|  650 | 0.2130 | 0.2268 |  307 |   23 |
|  700 | 0.1768 | 0.2129 |  332 |   18 |
|  750 | 0.1955 | 0.1976 |  325 |   18 |
|  800 | 0.2278 | 0.2453 |  300 |   19 |

**approach_slope:** 0.000314  **contact_slope:** 0.000326
**slope_diff (approach − contact):** -0.000012

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: final_gap_approach > 0.03 | PASS | 0.2278 |
| C2: early monotone improvement (ep50 → ep100) | PASS | yes |
| C3: approach_slope > 0 | PASS | 0.000314 |
| C4: approach_slope > contact_slope | FAIL | 0.000314 vs 0.000326 |
| C5: n_approach_min >= 20 | PASS | 300 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C4 FAIL: approach_slope(0.000314) <= contact_slope(0.000326)
