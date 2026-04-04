# V3-EXQ-074f -- MECH-117 Wanting/Liking Dissociation

**Status:** FAIL
**Claims:** MECH-112, MECH-117
**Seed:** 42  **Steps:** 3000  **Relocation:** step 1500
**Fix from 074e:** wanting/liking conditions now use model-based action selection (z_goal proximity / benefit_eval via E2.world_forward) after warmup step 300.

## Conditions

- nogo: benefit_eval_enabled=False, z_goal_enabled=False (greedy+random throughout)
- liking: benefit_eval_enabled=True, z_goal_enabled=False (model-based benefit_eval scoring after warmup)
- wanting: benefit_eval_enabled=False, z_goal_enabled=True (model-based z_goal proximity scoring after warmup)

## Results

| Metric | nogo | liking | wanting |
|---|---|---|---|
| resource_visit_rate | 0.2513 | 0.0427 | 0.0287 |
| harm_rate | 0.6113 | 0.5173 | 0.0643 |
| l2_redirect_steps | -- | 3 | -- |
| l1_directed_fraction | -- | -- | 0.000 |
| goal_norm_final | -- | -- | 0.0067 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: wanting resource >= nogo + 0.04 | FAIL |
| C2: liking l2_redirect <= 15 steps | PASS |
| C3: wanting l1_fraction >= 0.25 | FAIL |
| C4: wanting harm delta <= 0.03 | PASS |

Criteria met: 2/4 -> **FAIL**

## Interpretation

MECH-117 PARTIAL: Some dissociation signal present but below full threshold. Consider longer training or adjusted goal_weight/decay_goal.

## Failure Notes

- C1 FAIL: resource_rate gap=-0.2227 < 0.04
- C3 FAIL: wanting l1_fraction=0.000 < 0.25
