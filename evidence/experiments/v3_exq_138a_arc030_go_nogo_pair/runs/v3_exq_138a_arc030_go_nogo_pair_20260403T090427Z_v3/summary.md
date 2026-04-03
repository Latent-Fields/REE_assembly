# V3-EXQ-138a -- ARC-030 Go/NoGo Symmetry Discriminative Pair

**Status:** FAIL
**Claims:** ARC-030
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Warmup:** 400 eps  **Eval:** 50 eps

## Pre-Registered Thresholds

C1: delta_benefit_rate           >= 0.002 (averaged seeds)
C2: benefit_rate_go per seed     >= 0.002 (both seeds)
C3: harm_rate_go                 <= harm_rate_nogo * 1.5
C4: per-seed direction           GO > NOGO (both seeds)
C5: n_benefit_buf_go per seed    >= 100 (manipulation check)

## Results

| Condition       | benefit_rate | harm_rate   | goal_proximity |
|-----------------|-------------|-------------|----------------|
| GO_NOGO_SUPPORT | 0.00039  | 0.09371 | 0.9498 |
| NOGO_ONLY_ABLATED | 0.00037 | 0.09374 | N/A |

**delta_benefit_rate (GO - NOGO): +0.00002**

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: delta >= 0.002 | FAIL | +0.00002 |
| C2: benefit_rate_go per seed >= 0.002 | FAIL | [False, False] |
| C3: harm_rate_go <= NOGO*1.5 | PASS | 0.09371 vs 0.14060 |
| C4: per-seed direction GO > NOGO | FAIL | [False, True] |
| C5: benefit_buf >= 100 per seed | PASS | [759, 738] |

Criteria met: 2/5 -> **FAIL**

## Interpretation

ARC-030 NOT SUPPORTED: Go channel does not consistently outperform NOGO_ONLY on resource collection. Diagnostic: check n_benefit_buf_go_per_seed and goal_proximity_mean. If C5 fails, the environment benefit signal is insufficient.

## Prior Experiment

EXQ-086 (2026-03-23): FAIL (1/4), benefit_rate_go=0.0, warmup=150 -- training too short; benefit buffer barely populated (274 events).
EXQ-138 fixes: warmup 150->400, proximity_benefit_scale 0.05->0.10, num_resources 4->5, seeds [42,7]->[42,123].

## Per-Seed

GO_NOGO_SUPPORT:
  seed=42: benefit_rate=0.00000 harm_rate=0.18646 goal_prox=0.9477 benefit_buf=759
  seed=123: benefit_rate=0.00078 harm_rate=0.00096 goal_prox=0.9519 benefit_buf=738

NOGO_ONLY_ABLATED:
  seed=42: benefit_rate=0.00000 harm_rate=0.18676
  seed=123: benefit_rate=0.00073 harm_rate=0.00071

## Failure Notes

- C1 FAIL: delta_benefit_rate=0.00002 < 0.002 -- Go channel not producing reliable benefit advantage
- C2 FAIL: per-seed benefit_rate_go [False, False] -- some seeds flat (< 0.002)
- C4 FAIL: inconsistent directionality across seeds -- [False, True]
