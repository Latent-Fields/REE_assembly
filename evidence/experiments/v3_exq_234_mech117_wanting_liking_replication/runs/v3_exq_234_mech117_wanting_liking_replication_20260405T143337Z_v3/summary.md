# V3-EXQ-234 -- MECH-117 Wanting/Liking Dissociation Replication

**Status:** PASS  **Criteria met:** 4/4
**Claims:** MECH-112, MECH-117  **Purpose:** evidence
**Replication of:** V3-EXQ-074f (seeds [42,7,13])
**Seeds:** [1, 2, 3] (independent)

## Design

Identical to EXQ-074f: 3000 steps, 6x6 grid, L1->L2 relocation at step 1500. Wanting chases L1 post-relocation; liking chases L2 (env.resources). Only seeds differ.

## Results by Seed

| Seed | want_res_rate | l2_redirect | want_l1_frac | like_l1_frac | C1 | C2 | C3 | C4 |
|------|--------------|------------|-------------|-------------|----|----|----|----|
| 1 | 0.1453 | 4 | 0.990 | 0.615 | PASS | PASS | PASS | PASS |
| 2 | 0.1360 | 6 | 0.980 | 0.720 | PASS | PASS | PASS | PASS |
| 3 | 0.1380 | 3 | 0.920 | 0.290 | PASS | PASS | PASS | PASS |

## Interpretation

MECH-117 REPLICATED: Independent seeds [1,2,3] confirm wanting/liking dissociation. z_goal-driven wanting produces persistent L1-directed approach after relocation; benefit_eval-driven liking rapidly redirects to L2. Consistent with EXQ-074f [42,7,13]. Supports stable MECH-117 promotion.
