# V3-EXQ-047i -- MECH-095 Supervised TPJ Routing PoC

**Status:** FAIL
**Claims:** MECH-095, SD-005
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**lambda_route:** 0.1
**Warmup:** 400 eps  **Probe:** 20 eps
**Design note:** Supervised routing via transition_type labels. EXQ-089 showed unsupervised E2 mismatch insufficient at 300 eps (gap=0.004, false_attribution=1.0). This PoC tests the routing PRINCIPLE using ground-truth labels.

## Pre-Registered Thresholds

C1: contact_dissociation_routed > 0.05
C2: routing improvement (routed - baseline) > 0.04
C3: action_dissociation_routed > 0.05
C4: n_contact_probe >= 20
C5: no fatal errors

## Results

| Condition | contact_dissoc | action_dissoc |
|-----------|---------------|---------------|
| ROUTED    | +0.000          | -0.084         |
| BASELINE  | +0.000          | +0.085         |

**Routing improvement: +0.000**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contact_dissoc_routed > 0.05 | FAIL | +0.000 |
| C2: improvement > 0.04 | FAIL | +0.000 |
| C3: action_dissoc_routed > 0.05 | FAIL | -0.084 |
| C4: n_contact_min >= 20 | PASS | 164 |
| C5: no fatal errors | PASS | -- |

Criteria met: 2/5 -> **FAIL**

## Per-Seed

ROUTED:
  seed=42: contact_world=0.911 contact_self=0.911 contact_dissoc=+0.000 action_dissoc=-0.100 route_loss=0.0000
  seed=7: contact_world=0.902 contact_self=0.902 contact_dissoc=+0.000 action_dissoc=-0.067 route_loss=0.0000

BASELINE:
  seed=42: contact_world=0.911 contact_self=0.911 contact_dissoc=+0.000 action_dissoc=+0.083
  seed=7: contact_world=0.902 contact_self=0.902 contact_dissoc=+0.000 action_dissoc=+0.088

## Failure Notes

- C1 FAIL: contact_dissoc_routed=+0.000 <= 0.05
- C2 FAIL: routing improvement=+0.000 <= 0.04 (routed=+0.000 vs baseline=+0.000)
- C3 FAIL: action_dissoc_routed=-0.084 <= 0.05
