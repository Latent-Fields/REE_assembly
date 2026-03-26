# V3-EXQ-097 -- MECH-093 z_beta Heartbeat Rate Modulation

**Status:** FAIL
**Claims:** MECH-093
**Seed:** 42
**alpha_world:** 0.9  (SD-008)
**Warmup:** 200 eps  **Eval:** 40 eps  **Steps/ep:** 200

## Pre-Registered Thresholds

C1 (modulation gate): p1_rate_gap (low_harm_mean - high_harm_mean) >= 2.0 steps
C2 (reactivity):      harm_rate_ON <= 0.95 * harm_rate_OFF
C3 (stability):       action_var_ON <= 0.95 * action_var_OFF (safe phases)
PASS: C1 AND (C2 OR C3)

## Phase 1 Results (Modulation Gate, BETA_MOD_ON)

| Metric | Value |
|--------|-------|
| mean e3_steps_per_tick (high-harm eps) | 9.10 (n=1600) |
| mean e3_steps_per_tick (low-harm eps)  | 8.36 (n=100) |
| rate_gap (low - high)                  | -0.74 |
| C1 result | FAIL |

## Phase 2 Results (Behavioral)

| Condition | harm_rate | action_var_safe | n_safe_steps |
|-----------|-----------|-----------------|---------------|
| BETA_MOD_ON  | 0.2615  | 0.2221  | 1574 |
| BETA_MOD_OFF | 0.3049 | 1.3083 | 1227 |

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: rate_gap >= 2.0               | FAIL | -0.74 |
| C2: harm_rate ratio <= 0.95       | PASS | 0.858 |
| C3: action_var ratio <= 0.95      | PASS | 0.170 |

Criteria met: 2/3 -> **FAIL**

## Interpretation

MECH-093 NOT SUPPORTED: modulation not instantiated. E3 rate did not differ between high-harm and low-harm episodes (p1_rate_gap=-0.74, need >=2). z_beta may not encode harm salience after current training budget. Options: more warmup episodes, explicit z_beta harm supervision, or larger harm_scale to increase z_beta excursion. [modulation not instantiated (C1 gate failed)]

## Failure Notes

- C1 FAIL: p1_rate_gap=-0.74 < 2.0 (n_high_ticks=1600, n_low_ticks=100)
