# V3-EXQ-179 -- H-A/H-B Goal Navigation Causal Diagnostic

**Status:** PASS
**Claims:** MECH-112, SD-012
**Seeds:** [42, 7]

## Diagnostic Design

Two competing hypotheses about why z_goal-guided navigation fails:

- **H-A (content problem):** z_goal seeded from z_world at resource contact, but z_world encodes the full scene. Resources respawn randomly -> z_goal is scene-specific noise.
  Measured by: Pearson r(goal_proximity(z_world_t), resource_proximity_t) = `goal_tracking_r`

- **H-B (utilisation problem):** z_goal is meaningful but E3 trajectory scoring doesn't use it effectively.
  Measured by: goal_score(selected_traj) - mean(goal_score(other_trajs)) = `selection_bias`

Conditions: GOAL_PRESENT (real E3.select() with goal_state) vs GOAL_ABSENT (random actions).

**alpha_world:** 0.9  (SD-008)
**drive_weight:** 2.0  (SD-012)
**Warmup:** 400 eps (curriculum=80 eps)
**Eval:** 60 eps per condition

## Key Diagnostic Results

| Metric | Value | Threshold | Interpretation |
|---|---|---|---|
| goal_tracking_r (H-A) | -0.056 | <0.05=confirmed, >0.20=disconfirmed | H-A CONFIRMED: goal_tracking_r=-0.056 < 0.05 -- z_goal does ... |
| selection_bias (H-B) | 0.00000 | <0.005=confirmed, >0.02=disconfirmed | H-B CONFIRMED: selection_bias=0.00000 < 0.005 -- E3 NOT usin... |
| goal_score_rank_pct | 0.504 | >0.5=E3 prefers high-goal | -- |

## H-A Conclusion

H-A CONFIRMED: goal_tracking_r=-0.056 < 0.05 -- z_goal does not track resource proximity (content noise hypothesis supported)

## H-B Conclusion

H-B CONFIRMED: selection_bias=0.00000 < 0.005 -- E3 NOT using goal score to select trajectories

## Navigation Results

| Condition | benefit/ep | z_goal_norm | cal_gap |
|---|---|---|---|
| GOAL_PRESENT | 0.200 | 0.450 | 0.0627 |
| GOAL_ABSENT  | 0.667 | -- | -- |

**Benefit ratio (goal/no-goal): 0.30x**

## PASS Criteria (diagnostic quality gates)

| Criterion | Result | Value |
|---|---|---|
| C1: z_goal_norm > 0.1 | PASS | 0.450 |
| C2: n_eval_goal_steps > 500 | PASS | 774 |
| C3: n_resource_seedings > 5 | PASS | 282.5 |
| C4: no fatal errors | PASS | -- |

Criteria met: 4/4 -> **PASS**

## MECH-124 Diagnostics

goal_vs_harm_ratio: 2.177 (< 0.3 = V4 salience risk)

## Interpretation Reference

```
goal_tracking_r < 0.05  -> H-A CONFIRMED  (z_goal is scene noise)
goal_tracking_r > 0.20  -> H-A DISCONFIRMED  (z_goal tracks resources)
selection_bias  < 0.005 -> H-B CONFIRMED  (E3 not using goal score)
selection_bias  > 0.02  -> H-B DISCONFIRMED  (E3 IS preferring high-goal trajs)
```

## Per-Seed

GOAL_PRESENT:
  seed=42: benefit/ep=0.167 z_goal_norm=0.404 goal_tracking_r=-0.007 selection_bias=0.00000 rank_pct=0.513 n_eval_steps=772
  seed=7: benefit/ep=0.233 z_goal_norm=0.497 goal_tracking_r=-0.104 selection_bias=-0.00000 rank_pct=0.494 n_eval_steps=776

GOAL_ABSENT:
  seed=42: benefit/ep=0.767
  seed=7: benefit/ep=0.567

