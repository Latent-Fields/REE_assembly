# V3-EXQ-016 — SD-007 Reafference Correction

**Status:** FAIL
**Warmup:** 600 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Probe eval:** 20 grid resets
**Seed:** 0

## Motivation (SD-007 / MECH-098)

EXQ-012 revealed calibration_gap ≈ 0.0007 — E2 identity shortcut from perspective shift.
EXQ-014 (expected) confirmed locomotion explains > 30% of z_world variance.
This experiment applies reafference correction (SD-007) at z-space level:
  `z_world_corrected = z_world_raw - ReafferencePredictor(z_self_prev, a_prev)`
Then re-runs the SD-003 attribution probe using corrected z_world.

## ReafferencePredictor

- Architecture: Linear(37, 64) → ReLU → Linear(64, 32)
- Trained on empty-space steps (transition_type == "none")
- R² train: 0.181 | R² test: 0.118
- Empty-step data collected: 9700

## Δz_world Before/After Correction

| Event Type | Raw Δz_world | Corrected Δz_world | Reduction |
|---|---|---|---|
| empty_move (locomotion) | 0.0621 | 0.0621 | -0.0000 |
| env_caused_hazard | 0.0606 | 0.0606 | 0.0000 |

## SD-003 Attribution (Corrected z_world)

| Position | mean(causal_sig) |
|---|---|
| Near-hazard | -0.0010 |
| Safe | -0.0013 |
| **calibration_gap** | **0.0003** |

net_eval pred_std: 0.0298
n_near=906  n_safe=82
Warmup: harm=1507  benefit=235

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 (corrected) | FAIL | 0.0003 |
| C2: reafference R²_test > 0.2 | FAIL | 0.118 |
| C3: Δz_corrected(empty) < Δz_raw(empty) | FAIL | 0.0621 vs 0.0621 |
| C4: Warmup harm events > 100 | PASS | 1507 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: corrected calibration_gap=0.0003 <= 0.05
- C2 FAIL: reafference R²_test=0.118 <= 0.2
- C3 FAIL: Δz_corrected(empty)=0.0621 >= Δz_raw(empty)=0.0621
