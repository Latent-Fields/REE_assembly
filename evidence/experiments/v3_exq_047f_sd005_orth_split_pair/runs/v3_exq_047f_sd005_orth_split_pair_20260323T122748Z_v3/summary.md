# V3-EXQ-047f -- SD-005: Orthogonality-Constrained Split vs Unified

**Status:** FAIL
**Claim:** SD-005 -- z_gamma split into z_self (motor-sensory) and z_world (environmental)
**Design:** 400-ep orth-constrained training + 100-ep linear probe eval; seeds [42]
**orth_weight:** 0.05  |  **alpha_world:** 0.9

## EXQ-047e Failure Analysis

EXQ-047e adversarial GRL ran post-hoc for only 80 eps, pushing action info out of
z_world but not pulling it into z_self. action_dissoc=0.055, contact_dissoc=0.051
(both below 0.10 threshold). contact_world_improvement=0.000.

EXQ-047f replaces GRL with persistent orthogonality loss L_orth=mean(|cos(z_self,z_world)|)
baked into all 400 training episodes. Bidirectional separation pressure applied throughout
learning. UNIFIED condition trains normally (no separation possible -- control).

## Probe Results (averaged over seeds [42])

| Probe | Split+Orth | Unified | delta |
|---|---|---|---|
| Action accuracy <- z_self  | 0.730 | 0.865 | -0.135 |
| Action accuracy <- z_world | 0.838 | 0.919 | -0.081 |
| Contact accuracy <- z_world | 0.000 | 0.000 | +0.000 |
| Contact accuracy <- z_self | 0.000 | 0.000 | +0.000 |

Action dissociation (split):   -0.108  (target: >0.10)
Contact dissociation (split):  +0.000  (target: >0.05)
Action improvement vs unified: -0.135  (target: >0.03)
Orth cosine (eval):            0.018    (target: <0.15)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: action dissoc > 0.10 | FAIL | -0.108 |
| C2: contact dissoc > 0.05 | FAIL | 0.000 |
| C3: action vs unified > 0.03 | FAIL | -0.135 |
| C4: orth_cos < 0.15 | PASS | 0.018 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 -> **FAIL**
Decision: **retire_ree_claim**

## Failure Notes

- C1 FAIL: action dissociation=-0.108 (need >0.10)  [self=0.730, world=0.838]
- C2 FAIL: contact dissociation=0.000 (need >0.05)  [world=0.000, self=0.000]
- C3 FAIL: action improvement over unified=-0.135 (need >0.03)
