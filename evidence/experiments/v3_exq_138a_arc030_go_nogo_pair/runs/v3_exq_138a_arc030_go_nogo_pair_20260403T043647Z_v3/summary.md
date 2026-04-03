# V3-EXQ-138a -- ARC-030 Go/NoGo Symmetry Discriminative Pair

**Status:** FAIL
**Claims:** ARC-030
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Warmup:** 2 eps  **Eval:** 1 eps

## Pre-Registered Thresholds

C1: delta_benefit_rate           >= 0.002 (averaged seeds)
C2: benefit_rate_go per seed     >= 0.002 (both seeds)
C3: harm_rate_go                 <= harm_rate_nogo * 1.5
C4: per-seed direction           GO > NOGO (both seeds)
C5: n_benefit_buf_go per seed    >= 100 (manipulation check)

## Results

| Condition       | benefit_rate | harm_rate   | goal_proximity |
|-----------------|-------------|-------------|----------------|
| GO_NOGO_SUPPORT | 0.05452  | 0.08049 | 0.8593 |
| NOGO_ONLY_ABLATED | 0.05452 | 0.08049 | N/A |

**delta_benefit_rate (GO - NOGO): +0.00000**

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: delta >= 0.002 | FAIL | +0.00000 |
| C2: benefit_rate_go per seed >= 0.002 | FAIL | [False, True] |
| C3: harm_rate_go <= NOGO*1.5 | PASS | 0.08049 vs 0.12074 |
| C4: per-seed direction GO > NOGO | FAIL | [False, False] |
| C5: benefit_buf >= 100 per seed | FAIL | [0, 2] |

Criteria met: 1/5 -> **FAIL**

## Interpretation

ARC-030 NOT SUPPORTED: Go channel does not consistently outperform NOGO_ONLY on resource collection. Diagnostic: check n_benefit_buf_go_per_seed and goal_proximity_mean. If C5 fails, the environment benefit signal is insufficient.

## Prior Experiment

EXQ-086 (2026-03-23): FAIL (1/4), benefit_rate_go=0.0, warmup=150 -- training too short; benefit buffer barely populated (274 events).
EXQ-138 fixes: warmup 150->400, proximity_benefit_scale 0.05->0.10, num_resources 4->5, seeds [42,7]->[42,123].

## Per-Seed

GO_NOGO_SUPPORT:
  seed=42: benefit_rate=0.00000 harm_rate=0.12667 goal_prox=0.8651 benefit_buf=0
  seed=123: benefit_rate=0.10905 harm_rate=0.03432 goal_prox=0.8535 benefit_buf=2

NOGO_ONLY_ABLATED:
  seed=42: benefit_rate=0.00000 harm_rate=0.12667
  seed=123: benefit_rate=0.10905 harm_rate=0.03432

## Failure Notes

- C1 FAIL: delta_benefit_rate=0.00000 < 0.002 -- Go channel not producing reliable benefit advantage
- C2 FAIL: per-seed benefit_rate_go [False, True] -- some seeds flat (< 0.002)
- C4 FAIL: inconsistent directionality across seeds -- [False, False]
- C5 FAIL: benefit_buf_per_seed=[0, 2] -- some seeds below 100 -- Go channel saw insufficient positive events (experiment underspecified)
