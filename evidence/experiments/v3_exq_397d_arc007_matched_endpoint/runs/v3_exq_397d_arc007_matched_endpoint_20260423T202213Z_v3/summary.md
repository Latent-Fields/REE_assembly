# V3-EXQ-397d -- ARC-007 Path Memory Ablation: Matched-Endpoint Metric

**Status:** FAIL
**Claims:** ARC-007, SD-004
**Supersedes:** V3-EXQ-397c (metric confound in resource-hazard-colocated env)
**alpha_world:** 0.9  (SD-008)
**Environment:** 16x16, 6 hazards, 3 resources (sparse)
**Warmup:** 800 eps  |  Eval: 50 intact/ablated + 30 restored
**Seed:** 0

## Metric Redesign (EXQ-397c supersession)

EXQ-397/397c used hippo_quality_gap = mean_random_residue - mean_hippo_residue
over unpaired trajectories. In resource-hazard-colocated envs this confounds
destination-choice with path-choice: the hippocampus correctly projects
toward goals, which are residue-dense (hazard-proximate) regions by env
design. Random E2 rollouts stay near the current (residue-sparse) z_world.
Result: persistent negative quality_gap (~-1.64) that reflects goal-seeking,
not harm-seeking.

Fix: matched-endpoint residue comparison. At each E3 tick, pair each hippo
candidate with the random candidate whose terminal z_world is closest
(L2). Compare mean per-step residue along paired paths. This isolates
path-choice from destination-choice.

## Navigation Quality: Intact vs Ablated vs Restored

| Phase | matched_gap | hippo_residue | random_residue | endpoint_L2 |
|-------|-------------|---------------|-----------------|-------------|
| Intact (trained) | -1.639377 | 2.033941 | 0.394563 | 0.3727 |
| Ablated (residue=0) | 0.000000 | 0.000000 | 0.000000 | 0.3713 |
| Restored | -1.639340 | 2.033917 | 0.394577 | 0.3739 |

- **ablation_degradation**: -1.639377
- world_forward_r2: 0.9740
- terrain_loss: 0.3426 -> 0.0000
- calibration_gap_approach: -0.0001

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: matched_gap_intact > 0 | FAIL | -1.639377 |
| C2: ablated <= intact x 0.5 (ablation degrades >=50%) | FAIL | 0.000000 vs -0.819689 |
| C3: restored >= ablated (no further degradation) | FAIL | -1.639340 vs 0.000000 |
| C4: calibration_gap_approach > 0.03 | FAIL | -0.0001 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: matched_gap_intact=-1.639377 <= 0
- C2 FAIL: matched_gap_ablated=0.000000 > -0.819689 (50% of intact)
- C3 FAIL: matched_gap_restored=-1.639340 < ablated=0.000000
- C4 FAIL: calibration_gap_approach=-0.0001 <= 0.03
