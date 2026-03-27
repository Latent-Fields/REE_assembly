# V3-EXQ-076d -- MECH-116 / ARC-032 E1 Goal Conditioning

**Status:** FAIL
**Claims:** MECH-116, ARC-032
**Seed:** 42  **Steps:** 2000  **Resource removal:** step 1000
**Fix from 076c:** CausalGridWorldV2 size=6, resource_respawn, 50% proximity-following navigation (z_goal seeding fix).

## Conditions

- wanting_noe1: z_goal_enabled=True, e1_goal_conditioned=False
- wanting_withe1: z_goal_enabled=True, e1_goal_conditioned=True

## Results

| Metric | noe1 | withe1 |
|---|---|---|
| resource_visit_rate | 0.2750 | 0.2750 |
| goal_halflife (steps) | 2000 | 2000 |
| peak_goal_norm | 0.3569 | 0.3569 |
| goal_norm_at_1200 | 0.1310 | 0.1310 |
| harm_rate | 0.6985 | 0.6985 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: halflife ratio >= 1.5x | FAIL |
| C2: resource gap >= 0.03 | FAIL |
| C3: noe1 goal decays to <50% peak by t1200 | PASS |
| C4: withe1 goal_norm_t1200 >= noe1 + 0.02 | FAIL |

Criteria met: 1/4 -> **FAIL**

## Interpretation

MECH-116 / ARC-032 NOT SUPPORTED: E1 conditioning does not demonstrably extend goal persistence. z_goal decay_goal may dominate over E1 recurrent maintenance, or benefit signal is insufficient to establish a strong z_goal prior to removal.

## Failure Notes

- C1 FAIL: halflife ratio=1.00 < 1.5 (noe1=2000 withe1=2000)
- C2 FAIL: resource_rate gap=0.0000 < 0.03
- C4 FAIL: goal_norm_t1200 diff=0.0000 < 0.02
