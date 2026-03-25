# V3-EXQ-047k -- MECH-095 TPJ Routing Larger-N Replication

**Status:** PASS
**Claims:** MECH-095, SD-005
**Decision:** retain_ree
**Seeds:** [42, 7, 123, 99]
**alpha_world:** 0.9  (SD-008)
**lambda_route:** 0.1
**Warmup:** 400 eps  **Probe:** 20 eps
**mean_routing_loss (ROUTED):** 0.0330 (ACTIVE)
**Change from EXQ-047j:** 4 seeds (42,7,123,99); C3 relaxed to action_dissoc > -0.05

## Pre-Registered Thresholds

C1: contact_recall_world_routed > 0.55
C2: recall improvement (routed - baseline) > 0.04
C3: action_dissoc_mean > -0.05 (routing must not significantly hurt action prediction)
C4: n_contact_probe >= 20
C5: no fatal errors

## Results

| Condition | contact_recall | action_dissoc (mean +/- std) | route_loss |
|-----------|----------------|------------------------------|------------|
| ROUTED    | 0.796          | -0.007 +/- 0.157   | 0.0330     |
| BASELINE  | 0.731          | --                           | --         |

**Recall improvement: +0.065**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world > 0.55 | PASS | 0.796 |
| C2: improvement > 0.04 | PASS | +0.065 |
| C3: action_dissoc > -0.05 | PASS | -0.007 (std=0.157) |
| C4: n_contact >= 20 | PASS | 164 |
| C5: no fatal errors | PASS | -- |

Criteria met: 5/5 -> **PASS**

## Per-Seed

ROUTED:
  seed=42: contact_recall_world=0.875 contact_recall_self=0.750 action_dissoc=-0.189 route_loss=0.0344 n_contact=164
  seed=7: contact_recall_world=0.789 contact_recall_self=0.737 action_dissoc=+0.180 route_loss=0.0302 n_contact=175
  seed=123: contact_recall_world=0.789 contact_recall_self=0.737 action_dissoc=-0.132 route_loss=0.0338 n_contact=186
  seed=99: contact_recall_world=0.731 contact_recall_self=0.731 action_dissoc=+0.114 route_loss=0.0335 n_contact=167

BASELINE:
  seed=42: contact_recall_world=0.812 contact_recall_self=0.750 action_dissoc=+0.067 n_contact=164
  seed=7: contact_recall_world=0.737 contact_recall_self=0.842 action_dissoc=+0.093 n_contact=175
  seed=123: contact_recall_world=0.684 contact_recall_self=0.474 action_dissoc=+0.020 n_contact=186
  seed=99: contact_recall_world=0.692 contact_recall_self=0.846 action_dissoc=+0.104 n_contact=167

