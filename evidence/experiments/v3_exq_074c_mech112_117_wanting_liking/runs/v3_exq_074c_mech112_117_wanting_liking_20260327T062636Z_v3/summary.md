# V3-EXQ-074c -- MECH-117 Wanting/Liking Dissociation

**Status:** FAIL
**Claims:** MECH-112, MECH-117
**Seed:** 42  **Steps:** 3000  **Relocation:** step 1500

## Conditions

- nogo: benefit_eval_enabled=False, z_goal_enabled=False
- liking: benefit_eval_enabled=True, z_goal_enabled=False
- wanting: benefit_eval_enabled=False, z_goal_enabled=True

## Results

| Metric | nogo | liking | wanting |
|---|---|---|---|
| resource_visit_rate | 0.0000 | 0.0000 | 0.0000 |
| harm_rate | 0.0037 | 0.0037 | 0.0037 |
| l2_redirect_steps | -- | 200 | -- |
| l1_directed_fraction | -- | -- | 1.000 |
| goal_norm_final | -- | -- | 0.0000 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: wanting resource >= nogo + 0.04 | FAIL |
| C2: liking l2_redirect <= 15 steps | FAIL |
| C3: wanting l1_fraction >= 0.25 | PASS |
| C4: wanting harm delta <= 0.03 | PASS |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-117 PARTIAL: Some dissociation signal present but below full threshold. Consider longer training or adjusted goal_weight/decay_goal.

## Failure Notes

- C1 FAIL: resource_rate gap=0.0000 < 0.04
- C2 FAIL: liking l2_redirect=200 steps > 15
