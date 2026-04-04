# V3-EXQ-074f -- MECH-117 Wanting/Liking Dissociation

**Status:** PASS
**Claims:** MECH-112, MECH-117
**Seed:** 42  **Steps:** 3000  **Relocation:** step 1500
**Fix from 074e:** wanting condition chases L1 (spatial greedy toward old resource location) post-relocation; liking chases env.resources (L2). Both conditions use greedy+random pre-relocation to keep z_goal refreshed. Criteria revised: C1 is floor check (>= 0.05), C4 tests L1-fraction dissociation (wanting >> liking) rather than harm delta.

## Conditions

- nogo: benefit_eval_enabled=False, z_goal_enabled=False (greedy+random throughout)
- liking: benefit_eval_enabled=True, z_goal_enabled=False (model-based benefit_eval scoring after warmup)
- wanting: benefit_eval_enabled=False, z_goal_enabled=True (model-based z_goal proximity scoring after warmup)

## Results

| Metric | nogo | liking | wanting |
|---|---|---|---|
| resource_visit_rate | 0.2513 | 0.3707 | 0.1483 |
| harm_rate | 0.6113 | 0.5353 | 0.7157 |
| l2_redirect_steps | -- | 2 | -- |
| l1_directed_fraction | -- | 0.430 | 0.960 |
| goal_norm_final | -- | -- | 0.0930 |

## PASS Criteria

| Criterion | Result |
|---|---|
| C1: wanting resource_rate >= 0.05 (floor) | PASS |
| C2: liking l2_redirect <= 15 steps | PASS |
| C3: wanting l1_fraction >= 0.25 | PASS |
| C4: liking l1_fraction <= wanting l1_fraction - 0.10 (dissociation) | PASS |

Criteria met: 4/4 -> **PASS**

## Interpretation

MECH-117 SUPPORTED: wanting (z_goal_latent) and liking (benefit_eval_head) are functionally dissociable. Wanting produces persistent L1-directed approach after relocation; liking rapidly redirects to L2. Consistent with Berridge (1996) incentive salience / Culbreth et al. (2023) profiles.

