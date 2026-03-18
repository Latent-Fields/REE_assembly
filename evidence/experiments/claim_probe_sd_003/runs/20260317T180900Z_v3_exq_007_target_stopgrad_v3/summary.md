# V3-EXQ-007 — SD-003 Target Stopgrad Diagnostic

**Status:** FAIL
**Warmup:** 300 episodes, RANDOM policy + recon loss + 5-step E2 rollouts
**Design change:** z_target detached in multi-step E2 loss (prevents encoder co-adaptation)
**Probe eval:** 10 grid resets x (near-hazard + safe positions)
**Seed:** 0

## Hypothesis

r6 E2 identity shortcut may be caused by encoder co-adaptation: both
z_start and z_target come from the same encoder trained in the same
backward pass. The encoder could learn representations where consecutive
observations map to nearly identical latents, making delta≈0 correct.

Detaching z_target prevents this — E2 must predict where the *frozen*
target lands. If this fixes the gap, encoder collapse is the bottleneck.
If not, the grid environment itself lacks sufficient per-step variation.

Mean E2 world loss: 0.009722 | Mean reconstruction loss: 0.03960

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: TRAINED calibration_gap > 0.05 | FAIL | -0.0151 |
| C2: RANDOM abs(calibration_gap) < 0.10 | PASS | 0.0002 |
| C3: Warmup harm events > 100 | PASS | 819 |
| C4: No fatal errors | PASS | 0 |
| C5: harm_eval non-degenerate | PASS | OK |
| C6: Probe coverage >= 10 each | PASS | near=231 safe=66 |

## Calibration Results (Probe-Based)

| Condition | mean_causal_sig(near_hazard) | mean_causal_sig(safe) | calibration_gap |
|---|---|---|---|
| TRAINED | -0.0408 | -0.0257 | -0.0151 |
| RANDOM  | 0.0000 | -0.0002 | 0.0002 |

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL: TRAINED calibration_gap -0.0151 <= 0.05
