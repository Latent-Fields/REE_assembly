# V3-EXQ-029 — SD-003 on CausalGridWorldV2: Proxy-Gradient World

**Status:** PASS
**Claims:** SD-003, SD-007, ARC-024, MECH-071
**World:** CausalGridWorldV2 (use_proxy_fields=True, proximity_scale=0.05)
**SD-007 (MECH-101):** ReafferencePredictor(z_world_raw_prev[32] + a[5] → 32)
**alpha_world:** 0.9  (SD-008)
**Seed:** 1

## Motivation (ARC-024)

Harm/benefit signals are proxies along gradients toward asymptotic limits. A world
generating harm only at contact models the endpoint, not the gradient. CausalGridWorldV2
generates observable gradient fields preceding contact events:
- hazard_field_view (25 channels) in world_obs: visible proximity to hazards
- harm_exposure (EMA) in body_obs: accumulated nociceptive history
- harm_signal at approach steps: continuous gradient signal before contact

HYPOTHESIS: E3.harm_eval trained on gradient-world data fires at approach, not just contact.

## Key Metrics

| Transition Type | mean E3.harm_eval | n |
|---|---|---|
| none (locomotion)        | 0.3908 | 70 |
| hazard_approach (NEW)    | 0.5992 | 817 |
| env_caused_hazard        | 0.5906 | 20 |
| agent_caused_hazard      | 0.6116 | 32 |

- **gap_approach** (approach - none): **0.2084**  (PASS > 0.08)
- **gap_contact** (contact - none):   **0.2103**  (PASS > 0.05)
- reafference_r2: **0.4048**  (PASS > 0.10)
- harm_pred_std: 0.1827

## Training Counts

- approach events: 8118
- contact events:  449

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: gap_approach > 0.08 (E3 detects approach) | PASS | 0.2084 |
| C2: gap_contact > 0.05 (E3 still detects contact) | PASS | 0.2103 |
| C3: reafference_r2 > 0.10 | PASS | 0.4048 |
| C4: harm_pred_std > 0.01 | PASS | 0.1827 |
| C5: n_hazard_approach >= 30 | PASS | 817 |

Criteria met: 5/5 → **PASS**
