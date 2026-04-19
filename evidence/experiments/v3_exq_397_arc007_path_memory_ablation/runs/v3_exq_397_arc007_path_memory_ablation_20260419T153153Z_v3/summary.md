# V3-EXQ-397 — ARC-007 Path Memory Ablation (Proper)

**Status:** FAIL
**Claims:** ARC-007, SD-004
**Prerequisite:** EXQ-042 PASS (terrain prior training validates hippo_quality_gap > 0)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 600 eps  |  Eval: 50 eps intact/ablated + 30 restored
**Seed:** 0

## Motivation

V2 ARC-007 FAIL used z_gamma proxy; EXQ-042 validated terrain prior on V3 substrate.
This experiment ablates the residue field (path memory) to test whether hippocampal
navigation quality degrades without terrain geometry. ARC-007 STRICT (Q-020): if
ablation causes quality collapse, hippocampal module has no independent value head.

## Navigation Quality: Intact vs Ablated vs Restored

| Phase | hippo_quality_gap | calibration_gap_approach |
|-------|------------------|--------------------------|
| Intact (trained) | -1.640248 | -0.0001 |
| Ablated (residue=0) | 0.000000 | -0.0001 |
| Restored | -1.640152 | 0.0000 |

- **ablation_degradation**: -1.640248
- world_forward_r2: 0.9658
- terrain_loss: 0.2914 → 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: hippo_quality_gap_intact > 0 | FAIL | -1.640248 |
| C2: ablated <= intact x 0.5 (ablation degrades ≥50%) | FAIL | 0.000000 vs -0.820124 |
| C3: restored >= ablated (no further degradation) | FAIL | -1.640152 vs 0.000000 |
| C4: calibration_gap_approach > 0.03 | FAIL | -0.0001 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: hippo_quality_gap_intact=-1.640248 <= 0
- C2 FAIL: hippo_quality_gap_ablated=0.000000 > -0.820124 (50% of intact)
- C3 FAIL: quality_restored=-1.640152 < ablated=0.000000
- C4 FAIL: calibration_gap_approach=-0.0001 <= 0.03
