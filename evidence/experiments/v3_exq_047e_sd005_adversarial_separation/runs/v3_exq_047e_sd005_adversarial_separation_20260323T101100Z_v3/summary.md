# V3-EXQ-047e -- SD-005: Latent Information Separation (Adversarial Training)

**Status:** FAIL
**Claim:** SD-005 -- z_gamma split into z_self (motor-sensory) and z_world (environmental)
**Design:** Phase 1 warmup + Phase 2 adversarial GRL fine-tuning + Phase 3 linear probe eval
**adv_lambda:** 0.1  |  **adv_weight:** 0.5  |  **Seed:** 0
**Warmup:** 300 eps  |  **Adv:** 80 eps  |  **Eval:** 150 eps

## EXQ-047d Failure Analysis

EXQ-047d probed frozen representations with no separation training objective.
Both z_self and z_world carried equal action information (dissociation=0.008).
Two "runs" were byte-identical (same seed, deterministic frozen probe).
Root cause: without adversarial pressure, the encoder has no incentive to
concentrate action information in z_self and expel it from z_world.

EXQ-047e adds gradient reversal on z_world during adversarial Phase 2:
the probe learns to predict action from z_world; the reversed gradient forces
the encoder to push action information out of z_world. In the unified condition,
z_self = z_world, so adversarial suppression affects both -- the split is required.

## Probe Results

| Probe | Split | Unified | delta |
|---|---|---|---|
| Action accuracy <- z_self | 0.899 | 0.862 | +0.038 |
| Action accuracy <- z_world | 0.844 | 0.858 | -0.014 |
| Contact accuracy <- z_world | 0.643 | 0.643 | +0.000 |
| Contact accuracy <- z_self | 0.592 | 0.643 | -0.051 |

Action dissociation (split):   +0.055  (target: > 0.10)
Contact dissociation (split):  +0.051  (target: > 0.10)
Contacts collected (split): 243

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: action_self > action_world + 0.10 (split z_self action-selective) | FAIL | 0.899 vs 0.844 |
| C2: contact_world > contact_self + 0.10 (split z_world contact-selective) | FAIL | 0.643 vs 0.592 |
| C3: action_self_split > action_self_unified + 0.05 | FAIL | 0.899 vs 0.862 |
| C4: contact_world_split > contact_world_unified + 0.05 | FAIL | 0.643 vs 0.643 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: action_acc_self=0.899 not > action_acc_world=0.844 + 0.10
- C2 FAIL: contact_acc_world=0.643 not > contact_acc_self=0.592 + 0.10
- C3 FAIL: action_acc_self_split=0.899 not > action_acc_self_unified=0.862 + 0.05
- C4 FAIL: contact_acc_world_split=0.643 not > contact_acc_world_unified=0.643 + 0.05
