# V3-EXQ-041 — Full Pipeline Smoke Test: ThetaBuffer E3 Calibration

**Status:** PASS
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
| none | 0.0090 | 9796 |
| approach | 0.9844 | 194 |
| contact | 0.9971 | 10 |

**calibration_gap_approach:** 0.9754  (approach − none)
**calibration_gap_contact:**  0.9881  (contact − none)

## Pipeline Verification

- E3 tick total: 8800  (clock functional: True)
- world_forward R²: 0.9309
- final running_variance: 0.0000

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: cal_gap_approach > 0 (no sign inversion) | PASS | 0.9754 |
| C2: cal_gap_approach > 0.03 (meaningful) | PASS | 0.9754 |
| C3: n_approach_eval >= 30 | PASS | 194 |
| C4: e3_tick_count > 0 | PASS | 8800 |
| C5: world_forward R² > 0.05 | PASS | 0.9309 |

Criteria met: 5/5 → **PASS**
