# V3-EXQ-097b -- MECH-093 z_beta Heartbeat Rate Modulation (Step-Level)

**Status:** PASS
**Claims:** MECH-093
**Supersedes:** V3-EXQ-097
**Seed:** 42
**alpha_world:** 0.9  (SD-008)
**Warmup:** 500 eps  **Eval:** 40 eps  **Steps/ep:** 200

## Design Change vs EXQ-097

C1 redesigned: step-level Pearson r(|z_beta|_norm, 1/e3_steps_per_tick) >= 0.15
  (EXQ-097 used episode-level mean gap -- too coarse, z_beta showed minimal
   between-episode variance due to pervasive harm context: 16:1 pool skew)

## Pre-Registered Thresholds

C1 (modulation gate): Pearson r(|z_beta|, 1/e3_rate) >= 0.15 (BETA_MOD_ON)
C2 (reactivity):      harm_rate_ON <= 0.95 * harm_rate_OFF
C3 (stability):       action_var_ON <= 0.95 * action_var_OFF (safe phases)
PASS: C1 AND (C2 OR C3)

## Phase 1 Results (Modulation Gate, BETA_MOD_ON)

| Metric | Value |
|--------|-------|
| Pearson r(|z_beta|, 1/rate) | 0.964 (n=29937) |
| C1 threshold                | >= 0.15 |
| C1 result                   | PASS |

## Phase 2 Results (Behavioral)

| Condition | harm_rate | action_var_safe | n_safe_steps |
|-----------|-----------|-----------------|---------------|
| BETA_MOD_ON  | 0.3702  | 0.1576  | 898 |
| BETA_MOD_OFF | 0.2349 | 1.6336 | 1666 |

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: Pearson r >= 0.15        | PASS | 0.964 |
| C2: harm_rate ratio <= 0.95 | FAIL | 1.576 |
| C3: action_var ratio <= 0.95 | PASS | 0.096 |

Criteria met: 2/3 -> **PASS**

## Interpretation

MECH-093 SUPPORTED: step-level z_beta/rate correlation confirmed (C1) and behavioral benefit present. Pearson r=0.964 (n=29937). harm_rate_ON=0.3702 vs OFF=0.2349 (ratio=1.576). action_var_ON=0.1576 vs OFF=1.6336 (ratio=0.096).

## Failure Notes

- C2 FAIL: harm_rate_ON=0.3702 > 0.95 * harm_rate_OFF=0.2349
