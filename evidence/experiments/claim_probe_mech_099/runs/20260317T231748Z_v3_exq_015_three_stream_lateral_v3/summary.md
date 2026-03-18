# V3-EXQ-015 — Three-Stream Lateral Head (MECH-099)

**Status:** FAIL
**Warmup:** 300 eps (RANDOM policy, 12×12, 15 hazards)
**Probe eval:** 10 grid resets
**harm_dim:** 16
**Seed:** 2

## Motivation (MECH-099 / SD-007 / SD-003)

EXQ-012 showed calibration_gap ≈ 0.0007 with z_world — E2 identity shortcut.
This experiment tests whether a dedicated lateral encoder head processing ONLY
hazard + contamination channels (lateral stream in MECH-099 biological grounding)
gives E3 a harm-salient z_harm embedding that bypasses the identity shortcut.

Attribution pipeline (lateral variant):
```
z_harm = SplitEncoder.lateral_head(hazard_channels + contamination_view)  # [16-dim]
net_eval: z_harm → scalar ∈ [-1, 1]  (trained on harm_signal values)
causal_signal = net_eval(z_harm_near_hazard) - net_eval(z_harm_safe)
calibration_gap = mean(causal_signal near-hazard) - mean(causal_signal safe)
```

## Probe Results

| Metric | Near-Hazard | Safe | Margin |
|---|---|---|---|
| net_eval (z_harm) | -0.2299 | -0.2178 | -0.0121 |
| \|\|z_harm\|\| norm | 0.5156 | 0.5050 | 0.0105 |
| \|\|z_world\|\| norm | 0.5299 | 0.5317 | — |

net_eval pred_std: 0.0153
Warmup: harm=755  benefit=113

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: calibration_gap > 0.05 | FAIL | -0.0121 |
| C2: z_harm selectivity margin > 0.01 | PASS | 0.0105 |
| C3: Warmup benefit events > 20 | PASS | 113 |
| C4: Probe coverage >= 10 each | PASS | near=482 safe=35 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: calibration_gap=-0.0121 <= 0.05
