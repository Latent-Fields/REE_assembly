# V3-EXQ-017 — Combined Lateral + Reafference (MECH-099 + MECH-098)

**Status:** FAIL
**Warmup:** 300 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Probe eval:** 10 grid resets
**harm_dim:** 16  **world_dim:** 32  **Seed:** 1

## Motivation (MECH-099 + MECH-098 / SD-007 / SD-003)

EXQ-015 (lateral head alone) and EXQ-016 (reafference alone) tested individual fixes
for the E2 identity shortcut (EXQ-012 calibration_gap ≈ 0.0007). This experiment
combines both: reafference correction removes perspective shift from z_world, while
the lateral head provides harm-salient z_harm context. The combined attribution:
  combined_act = combined_head([z_harm; E2.world_forward(z_w_corr_act, a_act)])
  combined_cf  = combined_head([z_harm; E2.world_forward(z_w_corr_cf, a_cf)])
  causal_sig   = combined_act - combined_cf

## ReafferencePredictor

- R² train: 0.060 | R² test: 0.037
- Empty-step data: 4977

## Probe Results

| Metric | Near-Hazard | Safe | Margin |
|---|---|---|---|
| Combined causal_sig | 0.0002 | 0.0001 | 0.0001 |
| \|\|z_harm\|\| norm | 0.4299 | 0.4312 | -0.0013 |

pred_std: 0.0026
Warmup: harm=771  benefit=111

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 | FAIL | 0.0001 |
| C2: z_harm selectivity > 0.01 | FAIL | -0.0013 |
| C3: reafference R²_test > 0.2 | FAIL | 0.037 |
| C4: Warmup harm events > 100 | PASS | 771 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 2/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=0.0001 <= 0.05
- C2 FAIL: z_harm selectivity=-0.0013 <= 0.01
- C3 FAIL: reafference R²_test=0.037 <= 0.2
