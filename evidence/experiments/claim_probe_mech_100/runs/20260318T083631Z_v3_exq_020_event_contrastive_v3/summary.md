# V3-EXQ-020 — Event-Auxiliary Contrastive Encoder Loss

**Status:** FAIL
**Warmup:** 1000 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**λ_event:** 2.0
**Probe eval:** 10 grid resets
**Seed:** 0

## Motivation (MECH-100 / SD-009)

EXQ-013 showed z_world has near-zero event selectivity — Δz_world barely differs
between empty_move and env_caused_hazard. Root cause: encoder training losses are
event-invariant (E1 reconstruction, E2 self-prediction reward all z_world equally).
Fix: add cross-entropy event classifier (Linear(world_dim, 3)) to total_loss,
backpropagating through z_world encoder. This forces z_world to carry event-type
discriminative information.

## Event Selectivity

| Event Type | mean Δz_world |
|---|---|
| none (locomotion) | 0.7803 |
| env_caused_hazard | 1.8372 |
| agent_caused_hazard | 1.9066 |
| **selectivity margin** (env - none) | **1.0569** |

Event classifier accuracy: 0.692
Training CE loss mean: 1.0864

## SD-003 Attribution (Standard, No Reafference Correction)

| Position | mean(causal_sig) |
|---|---|
| Near-hazard | 0.0015 |
| Safe | 0.0010 |
| **calibration_gap** | **0.0004** |

net_eval pred_std: 0.0023
n_near=440  n_safe=33
Warmup: harm=55227  benefit=2114

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 | FAIL | 0.0004 |
| C2: event_classification_acc > 0.5 | PASS | 0.692 |
| C3: selectivity_margin > 0.005 | PASS | 1.0569 |
| C4: Warmup harm events > 100 | PASS | 55227 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0004 <= 0.05
