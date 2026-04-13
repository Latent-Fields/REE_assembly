# V3-EXQ-046 — ARC-007 Path Memory Ablation (Proper)

**Status:** FAIL
**Claims:** ARC-007, SD-004
**Prerequisite:** EXQ-042 PASS (terrain prior training validates hippo_quality_gap > 0)
**alpha_world:** 0.9  (SD-008)
**Warmup:** 2 eps  |  Eval: 2 eps intact/ablated + 2 restored
**Seed:** 0

## Motivation

V2 ARC-007 FAIL used z_gamma proxy; EXQ-042 validated terrain prior on V3 substrate.
This experiment ablates the residue field (path memory) to test whether hippocampal
navigation quality degrades without terrain geometry. ARC-007 STRICT (Q-020): if
ablation causes quality collapse, hippocampal module has no independent value head.

## Navigation Quality: Intact vs Ablated vs Restored

| Phase | hippo_quality_gap | calibration_gap_approach |
|-------|------------------|--------------------------|
| Intact (trained) | 0.000000 | -0.0011 |
| Ablated (residue=0) | 0.000000 | -0.0009 |
| Restored | 0.000000 | 0.4819 |

- **ablation_degradation**: 0.000000
- world_forward_r2: 0.0000
- terrain_loss: 0.0000 → 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: hippo_quality_gap_intact > 0 | FAIL | 0.000000 |
| C2: ablated <= intact x 0.5 (ablation degrades ≥50%) | PASS | 0.000000 vs 0.000000 |
| C3: restored >= ablated (no further degradation) | PASS | 0.000000 vs 0.000000 |
| C4: calibration_gap_approach > 0.03 | FAIL | -0.0011 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 3/5 → **FAIL**

## Failure Notes

- C1 FAIL: hippo_quality_gap_intact=0.000000 <= 0
- C4 FAIL: calibration_gap_approach=-0.0011 <= 0.03
