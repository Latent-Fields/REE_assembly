# V3-EXQ-397c -- ARC-007 Path Memory Ablation: Harder Env + Terrain Fix

**Status:** FAIL
**Claims:** ARC-007, SD-004
**Supersedes:** V3-EXQ-397 (inverted quality_gap from terrain-training on E3-selected trajectories)
**alpha_world:** 0.9  (SD-008)
**Environment:** 16x16, 6 hazards, 3 resources (sparse)
**Warmup:** 800 eps  |  Eval: 50 intact/ablated + 30 restored
**Seed:** 0

## Root Cause Fix (EXQ-397 inversion)

EXQ-397 trained terrain_prior on E3-selected trajectories. E3 selects toward
hazard-proximate resources (high reward, high residue), teaching hippocampus to
navigate TOWARD harm, inverting the quality_gap sign.

Fix: terrain_prior trained on minimum-residue candidate at each E3 tick.
This teaches hippocampus to propose paths that avoid accumulated harm residue.

## Navigation Quality: Intact vs Ablated vs Restored

| Phase | hippo_quality_gap | calibration_gap_approach |
|-------|------------------|--------------------------|
| Intact (trained) | -1.638433 | -0.0001 |
| Ablated (residue=0) | 0.000000 | -0.0001 |
| Restored | -1.638396 | -0.0002 |

- **ablation_degradation**: -1.638433
- world_forward_r2: 0.9740
- terrain_loss: 0.3426 -> 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: hippo_quality_gap_intact > 0 | FAIL | -1.638433 |
| C2: ablated <= intact x 0.5 (ablation degrades >=50%) | FAIL | 0.000000 vs -0.819216 |
| C3: restored >= ablated (no further degradation) | FAIL | -1.638396 vs 0.000000 |
| C4: calibration_gap_approach > 0.03 | FAIL | -0.0001 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 -> **FAIL**

## Failure Notes

- C1 FAIL: hippo_quality_gap_intact=-1.638433 <= 0
- C2 FAIL: hippo_quality_gap_ablated=0.000000 > -0.819216 (50% of intact)
- C3 FAIL: quality_restored=-1.638396 < ablated=0.000000
- C4 FAIL: calibration_gap_approach=-0.0001 <= 0.03
