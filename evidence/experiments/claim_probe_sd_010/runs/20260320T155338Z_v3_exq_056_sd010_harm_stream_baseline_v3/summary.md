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
| HarmEncoder → z_harm (SD-010) | 0.7084 |
| z_world encoder (baseline)    | 0.3175 |
| Difference (SD-010 advantage) | 0.3908 |

**z_harm variance across event types:** 0.002322
**n_contact_steps:** 57

## harm_eval_z_harm by transition type

| Type | Mean harm_eval_z_harm |
|---|---|
| agent_caused_hazard | 0.6164 |
| env_caused_hazard | 0.6934 |
| hazard_approach | 0.6221 |
| none | 0.5575 |
| resource | 0.5966 |


## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_eval_pearson_r_z_harm > 0.30 | PASS | 0.7084 |
| C2: R_z_harm > R_z_world + 0.10 (SD-010 adds value) | PASS | 0.7084 vs 0.3175+0.10 |
| C3: z_harm_variance_across_event_types > 0.01 | FAIL | 0.002322 |
| C4: n_contact_steps >= 30 (sufficient eval data) | PASS | 57 |

Criteria met: 3/4 → **FAIL**

## Failure Notes

- C3 FAIL: z_harm_var_across_event_types=0.002322 <= 0.01. z_harm does not vary across event types — signal collapsed.
