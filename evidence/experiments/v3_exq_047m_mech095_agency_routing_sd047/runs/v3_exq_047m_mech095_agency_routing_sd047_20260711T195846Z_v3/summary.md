# V3-EXQ-047m -- MECH-095 TPJ Agency-Routing CORRECTED Retest on SD-047

**Status:** FAIL
**Claims:** MECH-095
**Supersedes:** V3-EXQ-047l
**Decision:** ceiling_confirmed_route_autopsy
**Seeds:** [42, 7, 123, 99]
**Substrate:** SD-047 multi-source dynamics (intensity_scale=1.0)
**alpha_world:** 0.9  (SD-008)
**lambda_route:** 0.1
**Warmup:** 400 eps  **Probe:** 20 eps
**mean_routing_loss (ROUTED):** 0.0046 (ACTIVE)
**Probe partition:** n_contact_min=97 n_no_contact_min=8 (floor=5 OK; balanced_target=20 IMBALANCED-warn)
**047m fix vs 047l:** training is_world label KEEPS the env_events fold;
probe is_contact REVERTS to 047k's non-folded CONTACT_SET; added a probe-
partition non-degeneracy guard (blocking floor n_no_contact >= 5/arm
= non_contributory; advisory balanced target 20 = WARN only).

## Pre-Registered Thresholds (identical to EXQ-047k / 047l)

C1: contact_recall_world_routed > 0.55
C2: recall improvement (routed - baseline) > 0.04
C3: action_dissoc_mean > -0.05
C4: n_contact_probe >= 20
C5: no fatal errors

## Results

| Condition | contact_recall | action_dissoc (mean +/- std) | route_loss |
|-----------|----------------|------------------------------|------------|
| ROUTED    | 0.492          | -0.002 +/- 0.032   | 0.0046     |
| BASELINE  | 0.795          | +0.140 +/- 0.052   | --         |

**Recall improvement: -0.302**

**Secondary (claim-orthogonal) action-dissociation collapse: BASELINE +0.140 -> ROUTED -0.002**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world > 0.55 | FAIL | 0.492 |
| C2: improvement > 0.04 | FAIL | -0.302 |
| C3: action_dissoc > -0.05 | PASS | -0.002 (std=0.032) |
| C4: n_contact >= 20 | PASS | 97 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Per-Seed

ROUTED:
  seed=42: contact_recall_world=0.562 contact_recall_self=0.625 action_dissoc=-0.016 route_loss=0.0053 n_contact=110 n_no_contact=16 env_ev_ticks=4405
  seed=7: contact_recall_world=0.545 contact_recall_self=0.636 action_dissoc=-0.025 route_loss=0.0042 n_contact=108 n_no_contact=11 env_ev_ticks=4484
  seed=123: contact_recall_world=0.111 contact_recall_self=1.000 action_dissoc=+0.053 route_loss=0.0041 n_contact=104 n_no_contact=9 env_ev_ticks=4477
  seed=99: contact_recall_world=0.750 contact_recall_self=0.625 action_dissoc=-0.019 route_loss=0.0048 n_contact=97 n_no_contact=8 env_ev_ticks=4471

BASELINE:
  seed=42: contact_recall_world=0.688 contact_recall_self=0.812 action_dissoc=+0.230 n_contact=110 n_no_contact=16 env_ev_ticks=4405
  seed=7: contact_recall_world=0.727 contact_recall_self=0.818 action_dissoc=+0.101 n_contact=108 n_no_contact=11 env_ev_ticks=4484
  seed=123: contact_recall_world=0.889 contact_recall_self=0.556 action_dissoc=+0.115 n_contact=104 n_no_contact=9 env_ev_ticks=4477
  seed=99: contact_recall_world=0.875 contact_recall_self=0.625 action_dissoc=+0.114 n_contact=97 n_no_contact=8 env_ev_ticks=4471

## Failure Notes

- WARN (non-blocking): n_no_contact_min=8 < balanced-probe target 20 -- probe ran but is imbalanced / underpowered on this grid (hazard_approach saturates ~91% of steps; 047k PASSed at ~6). Result stands; read the recall with caution.
- C1 FAIL: contact_recall_world_routed=0.492 <= 0.55
- C2 FAIL: recall improvement=-0.302 <= 0.04 (routed=0.492 vs baseline=0.795)
