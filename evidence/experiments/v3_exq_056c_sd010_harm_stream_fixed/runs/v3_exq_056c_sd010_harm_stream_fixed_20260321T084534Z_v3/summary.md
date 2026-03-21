# V3-EXQ-056c — SD-010 Harm Stream Fixed

**Status:** PASS
**Claims:** SD-010, ARC-027
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Training:** 500 eps random  |  **Eval:** 100 eps random
**Metric:** Pearson R (harm_eval vs harm_obs[12] normalized label)
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0

## Fixes vs EXQ-056

1. **Label normalization**: harm_obs[12] (normalized center of hazard_field_view, ∈ [0,1])
   used for both training and eval. Raw hazard_field_at_agent was unbounded (>1), saturating
   the Sigmoid head to 1.0 for all inputs.
2. **Sigmoid removed**: harm_eval_z_harm_head is now a linear regression head. MSE with
   [0,1] labels constrains outputs naturally.
3. **Event-stratified replay buffer**: Separate circular buffers for none/approach/contact.
   Each training batch samples equally from all non-empty buckets — prevents 85%
   approach-dominated batches from collapsing the gradient.

## Question

Does HarmEncoder(harm_obs → z_harm) produce a harm estimate that correlates
with actual hazard proximity better than the fused z_world encoder?

## Results — Pearson R

| Source | Pearson R (vs harm_obs[12]) |
|---|---|
| HarmEncoder → z_harm (SD-010) | 0.9137 |
| z_world encoder (baseline)    | 0.4169 |
| Difference (SD-010 advantage) | 0.4967 |

**z_harm variance across event types:** 0.008051
**n_contact_steps:** 66

## harm_eval_z_harm by transition type

| Type | Mean harm_eval_z_harm |
|---|---|
| agent_caused_hazard | 0.5419 |
| env_caused_hazard | 0.7643 |
| hazard_approach | 0.6179 |
| none | 0.5472 |
| resource | 0.6272 |


## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_eval_pearson_r_z_harm > 0.30 | PASS | 0.9137 |
| C2: R_z_harm > R_z_world + 0.10 (SD-010 adds value) | PASS | 0.9137 vs 0.4169+0.10 |
| C3: mean_zh_contact > mean_zh_none + 0.05 (ordinal sep.) | PASS | 0.6699 vs 0.5472+0.05 (gap=0.1227) |
| C4: n_contact_steps >= 30 (sufficient eval data) | PASS | 66 |

Criteria met: 4/4 → **PASS**

