# V3-EXQ-086 -- ARC-030 Go/NoGo Symmetry (Approach-Avoidance)

**Status:** FAIL
**Claims:** ARC-030
**Decision:** retire_ree_claim
**Seeds:** [42, 7]
**Warmup:** 150 eps  **Eval:** 30 eps

## Pre-Registered Thresholds

C1: delta_benefit_rate          > 0.001
C2: harm_rate_GO                <= harm_rate_NOGO * 1.5
C3: benefit_rate_GO             > 0.001
C4: per-seed GO > NOGO direction

## Results

| Condition | benefit_rate | harm_rate | goal_proximity |
|-----------|-------------|-----------|----------------|
| GO_NOGO   | 0.00000  | 0.18597 | 0.8315 |
| NOGO_ONLY | 0.00000 | 0.18734 | N/A |

**delta_benefit_rate (GO - NOGO): +0.00000**

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: delta_benefit_rate > 0.001       | FAIL | +0.00000 |
| C2: harm_rate_GO <= NOGO*1.5         | PASS | 0.18597 vs 0.28102 |
| C3: benefit_rate_GO > 0.001          | FAIL | 0.00000 |
| C4: per-seed direction               | FAIL | [False, False] |

Criteria met: 1/4 -> **FAIL**

## Interpretation

ARC-030 NOT SUPPORTED: Go channel does not consistently improve resource collection. Either benefit_eval training is insufficient, z_goal attractor is not forming, or the environment benefit signal is too sparse. Diagnostic: check n_benefit_buf_pos in metrics.

## Per-Seed

GO_NOGO:
  seed=42: benefit_rate=0.00000 harm_rate=0.18440 goal_prox=0.8615 benefit_buf=119
  seed=7: benefit_rate=0.00000 harm_rate=0.18755 goal_prox=0.8015 benefit_buf=155

NOGO_ONLY:
  seed=42: benefit_rate=0.00000 harm_rate=0.19035
  seed=7: benefit_rate=0.00000 harm_rate=0.18434

## Failure Notes

- C1 FAIL: delta_benefit_rate=0.00000 <= 0.001 -- Go channel not producing measurable benefit advantage
- C3 FAIL: benefit_rate_GO=0.00000 <= 0.001 -- Go agent still behaviourally flat (training too short or goal_weight too low)
- C4 FAIL: inconsistent directionality across seeds -- [False, False]
