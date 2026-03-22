# V3-EXQ-047d -- SD-005: Latent Information Separation Probe (Design Fix)

**Status:** FAIL
**Claim:** SD-005 -- z_gamma split into z_self (motor-sensory) and z_world (environmental)
**Design:** Linear probes on frozen representations -- round-robin action decodability + binary contact probe
**alpha_world:** 0.9  |  **Warmup:** 500 eps  |  **Eval:** 200 eps  |  **Probe steps:** 500  |  **Seed:** 0

## Design Rationale and Fixes

EXQ-047c used random actions (no decodable signal) and a 3-class event probe dominated
by 86% majority class (approach). Both split and unified conditions produced bit-for-bit
identical probe accuracies because both probes converged to majority-class prediction.

EXQ-047d fixes:
1. Round-robin action assignment (ep%n_actions = dominant action, 80% compliance)
   creates systematic action->body_state correlation that z_self should encode.
2. Binary contact probe (hazard_contact vs not) with balanced class sampling.
   Contact events are rare but represent salient environmental events requiring
   genuine proximity knowledge from z_world.
3. 500 probe steps for convergence beyond majority-class baseline.

## Probe Results

| Probe | Split | Unified | delta |
|---|---|---|---|
| Action accuracy <- z_self | 0.847 | 0.866 | -0.019 |
| Action accuracy <- z_world | 0.840 | 0.857 | -0.017 |
| Contact accuracy <- z_world | 0.667 | 0.650 | +0.016 |
| Contact accuracy <- z_self | 0.610 | 0.585 | +0.024 |

Action dissociation (split): +0.008
Contact dissociation (split): +0.057
Contacts collected (split): 307

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: action_self > action_world + 0.10 (z_self more action-selective, split) | FAIL | 0.847 vs 0.840 |
| C2: contact_world > contact_self + 0.10 (z_world more contact-selective, split) | FAIL | 0.667 vs 0.610 |
| C3: action_self_split > action_self_unified + 0.05 | FAIL | 0.847 vs 0.866 |
| C4: contact_world_split > contact_world_unified + 0.05 | FAIL | 0.667 vs 0.650 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: action_acc_self=0.847 not > action_acc_world=0.840 + 0.10 (z_self not more action-selective than z_world)
- C2 FAIL: contact_acc_world=0.667 not > contact_acc_self=0.610 + 0.10 (z_world not more contact-selective than z_self)
- C3 FAIL: action_acc_self_split=0.847 not > action_acc_self_unified=0.866 + 0.05
- C4 FAIL: contact_acc_world_split=0.667 not > contact_acc_world_unified=0.650 + 0.05
