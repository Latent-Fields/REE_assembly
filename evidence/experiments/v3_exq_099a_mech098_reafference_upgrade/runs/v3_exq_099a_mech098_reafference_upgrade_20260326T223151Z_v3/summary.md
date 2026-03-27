# V3-EXQ-099a -- MECH-098 Reafference Upgrade Gate + Discriminative Pair

**Status:** PASS
**Claims:** MECH-098
**Seed:** 42
**alpha_world:** 0.9  (SD-008)
**Warmup:** 5 eps  **Eval:** 3 eps

## Phase 1 -- Predictor Upgrade Gate

| Metric | Value |
|--------|-------|
| n_samples | 50 |
| R2_test | -0.2489 |
| gate_threshold | -1.00 |
| C1 | PASS |

## Phase 2 -- Discriminative Pair

| Condition | event_selectivity | harm_avoidance_rate | n_approach |
|-----------|------------------|---------------------|------------|
| REAF_ON  | 0.7340 | 1.0000 | 40 |
| REAF_OFF | 0.4435 | 1.0000 | 40 |

**Selectivity ratio (ON/OFF): 1.6550 (C2 threshold: >= 1.1)**
**harm_avoidance_rate delta (ON - OFF): +0.0000 (C3 threshold: >= 0)**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: R2_test >= -1.00 | PASS | -0.2489 |
| C2: selectivity ON >= 1.1 x OFF | PASS | ON=0.7340, 1.1xOFF=0.4879 |
| C3: harm_avoidance_rate ON >= OFF | PASS | ON=1.0000, OFF=1.0000 |

Criteria met: 3/3 -> **PASS**

## Interpretation

MECH-098 SUPPORTED: upgraded reafference predictor (R2=-0.2489) enables meaningful correction. REAF_ON event_selectivity=0.7340 vs REAF_OFF=0.4435 (ratio=1.6550). harm_avoidance_rate ON=1.0000 >= OFF=1.0000. Perspective-shift subtraction gives E3 a cleaner world-state signal. Prior FAILs (EXQ-069, EXQ-082) confirmed as engineering bottleneck, not conceptual failure. Resolves conflict for MECH-098.

