# V3-EXQ-056 — SD-010 Harm Stream Baseline

**Status:** FAIL
**Claims:** SD-010, ARC-027
**World:** CausalGridWorldV2 (6 hazards, 3 resources)
**Training:** 400 eps random  |  **Eval:** 100 eps random
**Metric:** Pearson R (harm_eval vs hazard_field_at_agent proximity label)
**alpha_world:** 0.9  (SD-008)  |  **Seed:** 0

## Question

Does HarmEncoder(harm_obs → z_harm) produce a harm estimate that correlates
with actual hazard proximity better than the fused z_world encoder?

SD-010 hypothesis: separating nociceptive signals (hazard proximity) from the
exteroceptive world model (layout, content, perspective) enables the harm stream
to carry a cleaner hazard-proximity signal, uncontaminated by reafference correction
and world-model identity shortcuts.

## Results — Pearson R

| Source | Pearson R (vs hazard_label) |
|---|---|
| HarmEncoder → z_harm (SD-010) | 0.1483 |
| z_world encoder (baseline)    | 0.0472 |
| Difference (SD-010 advantage) | 0.1011 |

**z_harm variance across event types:** 0.000000
**n_contact_steps:** 57

## harm_eval_z_harm by transition type

| Type | Mean harm_eval_z_harm |
|---|---|
| agent_caused_hazard | 1.0000 |
| env_caused_hazard | 1.0000 |
| hazard_approach | 1.0000 |
| none | 1.0000 |
| resource | 1.0000 |


## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_eval_pearson_r_z_harm > 0.30 | FAIL | 0.1483 |
| C2: R_z_harm > R_z_world + 0.10 (SD-010 adds value) | PASS | 0.1483 vs 0.0472+0.10 |
| C3: z_harm_variance_across_event_types > 0.01 | FAIL | 0.000000 |
| C4: n_contact_steps >= 30 (sufficient eval data) | PASS | 57 |

Criteria met: 2/4 → **FAIL**

## Failure Notes

- C1 FAIL: harm_eval_pearson_r_z_harm=0.1483 <= 0.30. HarmEncoder cannot discriminate hazard proximity.
- C3 FAIL: z_harm_var_across_event_types=0.000000 <= 0.01. z_harm does not vary across event types — signal collapsed.
