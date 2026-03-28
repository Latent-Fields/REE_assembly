# V3-EXQ-113 -- SD-005 Double Dissociation

**Status:** FAIL
**Claims:** SD-005
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 300 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, use_proxy_fields=True, nav_bias=0.4

## Pre-Registered Thresholds

C1: delta_approach_gap_world (SPLIT-UNIFIED) >= 0.02  (world improves in SPLIT)
C2: gap_approach_split_world >= 0.06  (SPLIT world absolutely detects approach)
C3: gap_approach_unified_world >= 0.0  (UNIFIED learns something)
C4: delta_approach_gap_self (SPLIT-UNIFIED) <= -0.02  (z_self loses world content in SPLIT = purification)
C5: n_approach_eval >= 30  (data quality)

## Results

| Condition | gap_world | gap_self | mean_world_none | mean_world_appr |
|-----------|----------|---------|-----------------|------------------|
| SPLIT   | 0.0095 | 0.0011 | 0.5065 | 0.5160 |
| UNIFIED | 0.0062 | 0.0017 | 0.5066 | 0.5128 |

**delta_world (SPLIT-UNIFIED): +0.0033**  **delta_self (SPLIT-UNIFIED): -0.0006**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: delta_world >= 0.02 | FAIL | 0.0033 |
| C2: gap_world_split >= 0.06 | FAIL | 0.0095 |
| C3: gap_world_unified >= 0.0 | PASS | 0.0062 |
| C4: delta_self <= -0.02 | FAIL | -0.0006 |
| C5: n_approach_min >= 30 | PASS | 446 |

Criteria met: 2/5 -> **FAIL**

## Interpretation

SD-005 z_world advantage not replicated at this environment scale (gap_world_split=0.0095, delta=+0.0033). Suggests EXQ-078 result may not generalise to 6x6 environment or warmup reduction from 350->300 episodes was insufficient.

## Per-Seed

SPLIT:
  seed=42: gap_world=0.0130 gap_self=0.0016 n_approach=447
  seed=123: gap_world=0.0059 gap_self=0.0006 n_approach=446

UNIFIED:
  seed=42: gap_world=0.0085 gap_self=0.0014 n_approach=447
  seed=123: gap_world=0.0039 gap_self=0.0021 n_approach=446

## Failure Notes

- C1 FAIL: delta_world=0.0033 < 0.02 (split does not improve world approach detection by >=2pp)
- C2 FAIL: gap_world_split=0.0095 < 0.06 (split z_world cannot detect hazard approach at all)
- C4 FAIL: delta_self=-0.0006 > -0.02 (split z_self does NOT lose world content vs unified z_self) -- purification not demonstrated at current scale
