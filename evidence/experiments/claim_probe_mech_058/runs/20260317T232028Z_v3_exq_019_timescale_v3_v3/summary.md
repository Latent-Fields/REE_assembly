# V3-EXQ-019 — MECH-058 V3 Timescale Separation

**Status:** FAIL
**Warmup:** 300 eps (RANDOM policy, 12×12, 15 hazards, drift_interval=3, drift_prob=0.5)
**Eval:** 60 eps
**Seed:** 0

## Motivation (MECH-058 — V2 FAIL EXQ-023)

V2 FAIL was because z_gamma conflated self and world channels. V3 has clean
z_self/z_world split (SD-005). MECH-058 predicts z_world has longer autocorrelation
than z_self (persistent world model vs fast motor-sensory). BUT: before reafference
correction (SD-007), perspective shift makes z_world look fast. This experiment
measures both before and after correction.

## Delta Statistics

| Channel | Mean Δ | Autocorr lag=1 | Autocorr lag=5 | Autocorr lag=10 |
|---|---|---|---|---|
| z_self | 0.0421 | 0.5235 | -0.0610 | -0.0192 |
| z_world raw | 0.0532 | 0.3942 | -0.0322 | 0.0400 |
| z_world corrected | 0.0554 | 0.4767 | -0.0379 | 0.0186 |

Autocorr(corrected, lag=5) - Autocorr(self, lag=5) = 0.0231

Event-type z_world_raw means: empty=0.0525  env_hazard=0.0672
n_steps = 969  |  ReafferencePredictor R²_test = -0.035

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: Δz_world_raw > Δz_self (perspective shift dominates) | PASS | 0.0532 vs 0.0421 |
| C2: autocorr_corr[5] > autocorr_self[5] (corrected world slower) | PASS | -0.0379 vs -0.0610 |
| C3: Δz_world_corr < Δz_world_raw (correction reduced churn) | FAIL | 0.0554 vs 0.0532 |
| C4: n_steps >= 3000 | FAIL | 969 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C3 FAIL: mean_dz_corr=0.0554 >= mean_dz_raw=0.0532
- C4 FAIL: n_steps=969 < 3000
