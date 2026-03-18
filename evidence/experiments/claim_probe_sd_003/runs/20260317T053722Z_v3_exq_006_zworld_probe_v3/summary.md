# V3-EXQ-006 — Diagnostic: What Does z_world Encode?

**Status:** FAIL
**Agent training:** 300 episodes, RANDOM policy
**Probe data:** 30 grid resets, 1680 total samples
**Seed:** 0

## Motivation

EXQ-002r4 and EXQ-004r2 produce calibration_gap ≈ 0 despite correct probe design.
EXQ-005 shows E2.world_forward loss = 0.00002 (delta ≈ 0 is trivially good) and
E3 harm loss ≈ log(2) (random chance). This diagnostic checks whether z_world
encodes the information needed for SD-003 attribution.

## Linear Probe Results

| Probe | Target | TRAINED test | UNTRAINED test | Criterion |
|---|---|---|---|---|
| Hazard adjacency | binary (dist <= 1) | 0.693 | 0.720 | > 0.70 |
| Position X | regression (0-1) | R2=0.800 | R2=0.819 | R2 > 0.50 |
| Position Y | regression (0-1) | R2=0.557 | R2=0.576 | R2 > 0.50 |

Hazard-adjacent positive rate: 0.366 (baseline accuracy for majority-class classifier)

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: hazard_adj test_acc > 0.70 | FAIL | 0.693 |
| C2: position_x test_R2 > 0.50 | PASS | 0.800 |
| C3: position_y test_R2 > 0.50 | PASS | 0.557 |
| C4: No fatal errors | PASS | 0 |
| C5: n_samples >= 1000 | PASS | 1680 |

## Interpretation

C1 FAIL: z_world does NOT encode hazard proximity. The world encoder (trained by E1 prediction loss alone) discards hazard-relevant features. Fix: add reconstruction loss to world encoder so z_world preserves full observation content.

C2+C3: z_world encodes spatial position — the encoder is learning meaningful representations.

Criteria met: 4/5 -> **FAIL**

## Failure Notes

- C1 FAIL: hazard_adj test_acc 0.693 <= 0.70 — z_world does NOT encode hazard proximity
