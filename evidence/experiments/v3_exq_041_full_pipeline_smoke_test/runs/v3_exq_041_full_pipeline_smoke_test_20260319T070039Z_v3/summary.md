# V3-EXQ-041 — Full Pipeline Smoke Test: ThetaBuffer E3 Calibration

**Status:** FAIL
**Claims:** MECH-089, ARC-016, MECH-071
**World:** CausalGridWorldV2 (body=12, world=250)
**alpha_world:** 0.9 (SD-008)  |  **Seed:** 0
**Predecessors:** EXQ-026 PASS (harm_eval on raw z_world), EXQ-037 PASS (sign inversion diagnosed)

## Motivation

First experiment to exercise the complete agent pipeline. All prior V3 experiments
called `agent.sense()` then `agent.e3.harm_eval(raw_z_world)` directly, bypassing:
- **ThetaBuffer** (MECH-089): E3 should receive theta-cycle averages, not raw z_world
- **HippocampalModule**: terrain-informed trajectory proposals (not random)
- **MultiRateClock**: E3 fires at its own rate, not every step

EXQ-037 showed sign inversion under Fix2 training. Hypothesis: the inversion was
a distributional artifact of raw z_world ≠ E2-predicted z_world. ThetaBuffer.summary()
averages z_world over the last 10 steps, smoothing
the distribution. E3 trained on theta-averaged z_world should be stable.

terrain_prior is FROZEN at random init — this experiment isolates the ThetaBuffer
effect. EXQ-042 adds terrain_prior training.

## Results

| Transition Type | mean harm_eval | n |
|---|---|---|
| none | 0.4825 | 5 |
| approach | 0.4811 | 5 |
| contact | 0.0000 | 0 |

**calibration_gap_approach:** -0.0014  (approach − none)
**calibration_gap_contact:**  -0.4825  (contact − none)

## Pipeline Verification

- E3 tick total: 1  (clock functional: True)
- world_forward R²: 0.0000
- final running_variance: 0.3185

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: cal_gap_approach > 0 (no sign inversion) | FAIL | -0.0014 |
| C2: cal_gap_approach > 0.03 (meaningful) | FAIL | -0.0014 |
| C3: n_approach_eval >= 30 | FAIL | 5 |
| C4: e3_tick_count > 0 | PASS | 1 |
| C5: world_forward R² > 0.05 | FAIL | 0.0000 |

Criteria met: 1/5 → **FAIL**

## Failure Notes

- C1 FAIL: cal_gap_approach=-0.0014 <= 0 (sign inversion PERSISTS even with ThetaBuffer — deeper problem, V4 signal)
- C2 FAIL: cal_gap_approach=-0.0014 <= 0.03
- C3 FAIL: n_approach_eval=5 < 30
- C5 FAIL: world_forward_r2=0.0000 <= 0.05
