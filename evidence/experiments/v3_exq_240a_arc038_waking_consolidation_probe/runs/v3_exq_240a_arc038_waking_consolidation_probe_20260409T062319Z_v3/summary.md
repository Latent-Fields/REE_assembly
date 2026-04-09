# V3-EXQ-240a -- ARC-038 Waking Consolidation Mode Probe

**Status:** FAIL
**Claims:** ARC-038
**Decision:** inconclusive_diagnostic
**Purpose:** diagnostic
**Seeds:** [42, 7, 123, 0, 99]

## Design

CONSOLIDATE vs NO_CONSOLIDATE: after every K=10 episodes, CONSOLIDATE condition runs hippocampal.replay() (no z_goal) + residue_field.integrate() (offline map-geometry update). NO_CONSOLIDATE skips these calls entirely.

target_harm_rate=0.05 (reachable).
Majority rule: >= 3/5 seeds required per criterion.

## Results

| Condition | Final Harm Rate | Acq Speed | Benefit Ratio |
|---|---|---|---|
| CONSOLIDATE | 0.15411 | 97.4 | 2.047 |
| NO_CONSOLIDATE | 0.13514 | 93.4 | (baseline) |

## PASS Criteria

| Criterion | Result | Seeds Met | Detail |
|---|---|---|---|
| C1: CONSOLIDATE final_harm < NO_CONSOLIDATE | PASS | 3/5 | 0.15411 vs 0.13514 |
| C2: CONSOLIDATE acq_speed < NO_CONSOLIDATE | FAIL | 2/5 | 97.4 vs 93.4 |
| C3: benefit_ratio > 1.1 | FAIL | 2/5 | ratio=2.047 |

PASS = C1 AND (C2 OR C3). Status: **FAIL**

## Per-Seed

  seed=42 env=100: c_final=0.22913 nc_final=0.23717 ratio=1.035 c_acq=37 nc_acq=200 passes=20
  seed=7 env=200: c_final=0.01230 nc_final=0.08320 ratio=6.765 c_acq=21 nc_acq=26 passes=20
  seed=123 env=300: c_final=0.05285 nc_final=0.06421 ratio=1.215 c_acq=29 nc_acq=21 passes=20
  seed=0 env=400: c_final=0.23929 nc_final=0.22826 ratio=0.954 c_acq=200 nc_acq=200 passes=20
  seed=99 env=500: c_final=0.23698 nc_final=0.06284 ratio=0.265 c_acq=200 nc_acq=20 passes=20

## Diagnostic Notes

- C2 FAIL (2/5 seeds): acquisition speed CONSOLIDATE=97.4 not < NO_CONSOLIDATE=93.4.
- C3 FAIL (2/5 seeds): benefit_ratio=2.047 not > 1.1 threshold.
