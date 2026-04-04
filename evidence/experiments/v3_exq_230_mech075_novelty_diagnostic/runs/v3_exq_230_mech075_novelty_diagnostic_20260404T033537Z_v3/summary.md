# V3-EXQ-230 -- MECH-075 Novelty Loop Diagnostic

**Status:** FAIL  **Diagnostic finding:** substrate_limitation
**Claims:** MECH-075  **Purpose:** diagnostic

## Context

EXQ-192a FAIL (shape bug fixed, still FAIL). EXQ-209 weakens. This diagnostic tests whether the novelty signal is active and whether hippocampal gain variance differs between conditions.

## Conditions

- NOVELTY_GATED: novelty_ema from E1 MSE scales CEM noise (gain=2.0)
- NOVELTY_ABLATED: novelty_ema held at 0.0, fixed CEM noise

## Results by Seed

| Seed | Novelty mag | Explore gap | C1 | C2 |
|------|------------|------------|----|----|
| 42 | 0.00008 | +0.0000 | FAIL | FAIL |
| 7 | 0.00008 | +0.0000 | FAIL | FAIL |
| 123 | 0.00010 | +0.0300 | FAIL | FAIL |

## PASS Criteria

| Criterion | Threshold | Result |
|---|---|---|
| C1: novelty_signal_mag > 0.01 (>= 2/3 seeds) | 0.01 | FAIL |
| C2: exploration_gap >= 0.1 (>= 2/3 seeds) | 0.1 | FAIL |

## Diagnostic Finding

substrate_limitation

## Interpretation

Novelty signal magnitude < 0.01 in all seeds. E1 world-prediction error is not producing a detectable novelty signal. The LC-VTA novelty loop is structurally disconnected from hippocampal gain modulation in current V3 substrate. MECH-075 mechanism not measurable at current architectural stage.
