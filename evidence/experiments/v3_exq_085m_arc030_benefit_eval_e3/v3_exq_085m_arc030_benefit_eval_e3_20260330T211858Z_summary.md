# V3-EXQ-085m -- ARC-030 benefit_eval_head + E3 Selection

**Status:** FAIL
**Claims:** ARC-030, MECH-112, SD-015
**Seeds:** [42, 7]

## Experimental Design

First experiment to train `benefit_eval_head` on resource proximity regression
and test whether E3's native benefit pathway drives goal-directed navigation.

Training target: `max(resource_field_view)` per step (MSE regression).
Evaluation: BENEFIT_ENABLED (E3 uses benefit) vs BENEFIT_DISABLED (E3 harm+residue only).

No goal_state / z_goal attractor. Pure ARC-030 Go-channel test.

**benefit_weight:** 2.0  **alpha_world:** 0.9
**Warmup:** 400 eps (curriculum=80 eps)
**Eval:** 60 eps per condition

## Key Results

| Metric | Value | Criterion | Status |
|---|---|---|---|
| benefit_eval_r2_train | -0.005 | > 0.3 | FAIL |
| benefit_ratio | 1.00x | >= 1.3x | FAIL |
| selection_bias_benefit | -0.00000 | > 0.005 | FAIL |
| calibration_gap_benefit | 0.0000 | > 0.0 | FAIL |

## Navigation Results

| Condition | benefit/ep |
|---|---|
| BENEFIT_ENABLED | 0.200 |
| BENEFIT_DISABLED | 0.200 |

**Benefit ratio: 1.00x**

## H-B Analysis

H-B CONFIRMED independently: selection_bias=-0.00000 < 0.005. E3 does not preferentially select higher-benefit trajectories. Benefit scoring in score_trajectory() not effective.

benefit_eval_r2_train=-0.005  benefit_eval_r2_eval=-0.010  calibration_gap=0.0000  harm_calibration_gap=0.0627

benefit_vs_harm_ratio=2.149

## Per-Seed

BENEFIT_ENABLED:
  seed=42: benefit/ep=0.167 r2_train=0.004 r2_eval=-0.021 sel_bias=-0.00001 rank_pct=0.496
  seed=7: benefit/ep=0.233 r2_train=-0.014 r2_eval=0.002 sel_bias=0.00000 rank_pct=0.523

BENEFIT_DISABLED:
  seed=42: benefit/ep=0.167
  seed=7: benefit/ep=0.233

## Failure Notes

- C1 FAIL: benefit_r2_train=-0.005 <= 0.3. benefit_eval_head cannot learn resource proximity from z_world. Check if z_world encodes resource_field_view (world_dim, alpha_world).
- C2 FAIL: benefit_ratio=1.00x < 1.3x. Benefit-guided E3 not improving navigation vs harm-only E3.
- C3 FAIL: selection_bias=-0.00000 <= 0.005. E3 not preferentially selecting higher-benefit trajectories. H-B CONFIRMED independently of H-A.
- C4 FAIL: calibration_gap=0.0000 <= 0.0. benefit_eval_head not assigning higher scores near resources.
