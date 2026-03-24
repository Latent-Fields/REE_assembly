# V3-EXQ-047g -- SD-005 Functional Separation Probe

**Status:** FAIL
**Claims:** SD-005
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Probe:** 20 eps
**Design note:** Functional cross-decoding probes. No orthogonality constraint.

## Pre-Registered Thresholds

C1: action_dissociation_split (self - world) > 0.10
C2: contact_dissociation_split (world - self) > 0.05
C3: action_acc_self_split - unified > 0.03
C4: contact_acc_world_split - unified > 0.03
C5: n_contact_probe >= 20

## Results

| Condition | action_self | action_world | contact_world | contact_self |
|-----------|------------|--------------|---------------|-------------|
| SPLIT     | 0.471       | 0.385         | 0.907          | 0.907        |
| UNIFIED   | 0.500       | n/a          | 0.907          | n/a         |

**action_dissociation_split (self - world): +0.085**
**contact_dissociation_split (world - self): +0.000**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: action dissociation > 0.10 | FAIL | +0.085 |
| C2: contact dissociation > 0.05 | FAIL | +0.000 |
| C3: split vs unified action (+0.03) | FAIL | -0.030 |
| C4: split vs unified contact (+0.03) | FAIL | +0.000 |
| C5: n_contact_min >= 20 | PASS | 164 |

Criteria met: 1/5 -> **FAIL**

## Per-Seed

SPLIT:
  seed=42: action_self=0.478 action_world=0.394 contact_world=0.911 contact_self=0.911 n_contact=164
  seed=7: action_self=0.464 action_world=0.376 contact_world=0.902 contact_self=0.902 n_contact=175

UNIFIED:
  seed=42: action_self=0.511 action_world=0.533 contact_world=0.911 contact_self=0.911
  seed=7: action_self=0.490 action_world=0.490 contact_world=0.902 contact_self=0.902

## Failure Notes

- C1 FAIL: action_dissociation_split=+0.085 <= 0.10 (z_self not better motor probe than z_world in split condition)
- C2 FAIL: contact_dissociation_split=+0.000 <= 0.05 (z_world not better world probe than z_self in split condition)
- C3 FAIL: split z_self action advantage over unified = -0.030 <= 0.03
- C4 FAIL: split z_world contact advantage over unified = +0.000 <= 0.03
