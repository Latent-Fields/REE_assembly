# V3-EXQ-085n -- SD-015 Multi-Step Greedy RFM Rollout

**Status:** FAIL
**Claims:** SD-015, SD-012, MECH-112
**Decision:** hybridize
**Seeds:** [42, 7, 13]
**Supersedes:** V3-EXQ-085l

## Architecture

ProximityEncoder (25->16, MSE regression) + ResourceForwardModel identical to 085l.
Action selection: multi-step greedy RFM rollout, depth=5.

**Rationale:** 085l confirmed prox_r2=0.91, goal_resource_r=0.87 -- representation is correct. benefit_ratio=0.42x because 1-step lookahead only informative when resource is in 5x5 FOV (~30%% of steps). Depth=5 rollout should extend horizon and allow action selection to see resources outside immediate FOV.

**Hypothesis (pre-registered as expected FAIL):** 5-step greedy rollout is sufficient to overcome 1-step horizon limitation. Predicted FAIL because: RFM compound error at depth=5 may wash out proximity gradient; greedy intermediate selections ignore hazard zones; resource still outside extended FOV in many steps. FAIL confirms SD-004 hippocampal navigation required.

**Rollout depth:** 5 steps
**Warmup:** 800 eps (curriculum=100 eps)
**Eval:** 100 eps
  (GOAL_PRESENT: depth=5 multistep RFM; GOAL_ABSENT: random)
**alpha_world:** 0.9  (SD-008)
**SD-012:** drive_weight=2.0, resource_respawn_on_consume=True
**lr_enc:** 0.001  **lr_rfm:** 0.0005
**enc_final_loss (avg):** 0.0011
**rfm_final_loss (avg):** 0.0076
**prox_r2 (avg):** 0.908

## Diagnostic Series Summary

| Variant | Action selection | goal_r | benefit_ratio | Note |
|---|---|---|---|---|
| 085l | 1-step RFM | 0.87 | 0.42x | horizon too short |
| 085m | depth=5 greedy RFM | 0.826 | 0.31x | this run |

## Navigation Results

| Condition | benefit/ep | z_goal_norm_enc | r_enc | prox_r2 |
|---|---|---|---|---|
| GOAL_PRESENT | 0.200 | 0.731 | 0.826 | 0.908 |
| GOAL_ABSENT  | 0.643 | -- | -- | -- |

**Benefit ratio (goal/no-goal): 0.31x**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm_enc > 0.1 | PASS | 0.731 |
| C2: benefit ratio >= 1.3x | FAIL | 0.31x |
| C3: goal_resource_r_enc > 0.2 | PASS | 0.826 |
| C4: prox_r2 > 0.3 | PASS | 0.908 |

Criteria met: 3/4 -> **FAIL**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 1.842 (< 0.3 = V4 risk)

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.060 z_goal_norm_enc=0.501 r_enc=0.786 prox_r2=0.892 rfm_loss=0.0075
  seed=7: benefit/ep=0.260 z_goal_norm_enc=0.921 r_enc=0.888 prox_r2=0.912 rfm_loss=0.0070
  seed=13: benefit/ep=0.280 z_goal_norm_enc=0.770 r_enc=0.805 prox_r2=0.919 rfm_loss=0.0083

GOAL_ABSENT:
  seed=42: benefit/ep=0.680
  seed=7: benefit/ep=0.730
  seed=13: benefit/ep=0.520

## Failure Notes

- C2 FAIL: benefit_ratio=0.31x < 1.3x BUT C3 PASS (r=0.826). Multi-step RFM rollout (depth=5) insufficient for grid-scale navigation. Conclusion: planning horizon not the bottleneck -- SD-004 hippocampal navigation required for goal-directed resource acquisition.
