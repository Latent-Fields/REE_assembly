# V3-EXQ-047l -- MECH-095 TPJ Agency-Routing Retest on SD-047 Env

**Status:** FAIL
**Claims:** MECH-095
**Decision:** ceiling_confirmed_route_autopsy
**Seeds:** [42, 7, 123, 99]
**Substrate:** SD-047 multi-source dynamics (intensity_scale=1.0)
**alpha_world:** 0.9  (SD-008)
**lambda_route:** 0.1
**Warmup:** 400 eps  **Probe:** 20 eps
**mean_routing_loss (ROUTED):** 0.0046 (ACTIVE)
**Operationalisation:** EXQ-047k routing comparator, world/contact labels
fold multi_source_n_env_events>0 additively. See also V3-EXQ-510
(counterfactual-gap comparator on SD-047 -> WOO_SPELKE flat-FAIL).

## Pre-Registered Thresholds (identical to EXQ-047k)

C1: contact_recall_world_routed > 0.55
C2: recall improvement (routed - baseline) > 0.04
C3: action_dissoc_mean > -0.05
C4: n_contact_probe >= 20
C5: no fatal errors

## Results

| Condition | contact_recall | action_dissoc (mean +/- std) | route_loss |
|-----------|----------------|------------------------------|------------|
| ROUTED    | 0.000          | -0.004 +/- 0.020   | 0.0046     |
| BASELINE  | 0.000          | --                           | --         |

**Recall improvement: +0.000**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world > 0.55 | FAIL | 0.000 |
| C2: improvement > 0.04 | FAIL | +0.000 |
| C3: action_dissoc > -0.05 | PASS | -0.004 (std=0.020) |
| C4: n_contact >= 20 | PASS | 105 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Per-Seed

ROUTED:
  seed=42: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=-0.016 route_loss=0.0053 n_contact=126 env_ev_ticks=4405
  seed=7: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=-0.025 route_loss=0.0042 n_contact=119 env_ev_ticks=4484
  seed=123: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.027 route_loss=0.0041 n_contact=113 env_ev_ticks=4477
  seed=99: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.000 route_loss=0.0048 n_contact=105 env_ev_ticks=4471

BASELINE:
  seed=42: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.230 n_contact=126 env_ev_ticks=4405
  seed=7: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.101 n_contact=119 env_ev_ticks=4484
  seed=123: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.115 n_contact=113 env_ev_ticks=4477
  seed=99: contact_recall_world=0.000 contact_recall_self=0.000 action_dissoc=+0.114 n_contact=105 env_ev_ticks=4471

## Failure Notes

- C1 FAIL: contact_recall_world_routed=0.000 <= 0.55
- C2 FAIL: recall improvement=+0.000 <= 0.04 (routed=0.000 vs baseline=0.000)
