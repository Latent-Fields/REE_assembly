# V3-EXQ-047j -- MECH-095 TPJ Routing via CE Head

**Status:** FAIL
**Claims:** MECH-095, SD-005
**Decision:** hybridize
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**lambda_route:** 0.1
**Warmup:** 400 eps  **Probe:** 20 eps
**mean_routing_loss (ROUTED):** 0.0323 (ACTIVE)
**Bug fixes vs EXQ-047i:**
  (1) CE routing head replaces MSE-stability loss (was near-zero due to alpha=0.9 EMA).
  (2) Balanced contact probe (undersampled) replaces majority-class-collapse probe.

## Pre-Registered Thresholds

C1: contact_recall_world_routed > 0.55
C2: recall improvement (routed - baseline) > 0.04
C3: action_dissoc_routed > 0 (z_self better than z_world for actions)
C4: n_contact_probe >= 20
C5: no fatal errors

## Results

| Condition | contact_recall | action_dissoc | route_loss |
|-----------|----------------|---------------|------------|
| ROUTED    | 0.832          | -0.004        | 0.0323     |
| BASELINE  | 0.775          | --            | --         |

**Recall improvement: +0.058**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world > 0.55 | PASS | 0.832 |
| C2: improvement > 0.04 | PASS | +0.058 |
| C3: action_dissoc > 0 | FAIL | -0.004 |
| C4: n_contact >= 20 | PASS | 164 |
| C5: no fatal errors | PASS | -- |

Criteria met: 4/5 -> **FAIL**

## Per-Seed

ROUTED:
  seed=42: contact_recall_world=0.875 contact_recall_self=0.750 action_dissoc=-0.189 route_loss=0.0344 n_contact=164
  seed=7: contact_recall_world=0.789 contact_recall_self=0.737 action_dissoc=+0.180 route_loss=0.0302 n_contact=175

BASELINE:
  seed=42: contact_recall_world=0.812 contact_recall_self=0.750 action_dissoc=+0.067 n_contact=164
  seed=7: contact_recall_world=0.737 contact_recall_self=0.842 action_dissoc=+0.093 n_contact=175

## Failure Notes

- C3 FAIL: action_dissoc_routed=-0.004 <= 0
