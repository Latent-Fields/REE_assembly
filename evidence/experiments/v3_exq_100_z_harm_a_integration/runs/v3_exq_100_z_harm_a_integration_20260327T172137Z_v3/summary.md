# V3-EXQ-100 -- SD-011 / ARC-016 Affective Harm Stream First Integration

**Status:** FAIL
**Claims:** SD-011, ARC-016
**Design:** HIGH_HAZARD (6) vs LOW_HAZARD (2) -- does z_harm_a respond and stabilise?
**First test:** AffectiveHarmEncoder wired into active experiment loop (never done before)

## Biological Grounding

z_harm_s (A-delta analog): immediate, high-frequency proximity. Step-to-step variation.
z_harm_a (C-fiber/paleospinothalamic analog): integrated, homeostatic accumulation.
  harm_obs_a is an EMA (tau~20 steps) of harm_obs_s proximity fields.
  AffectiveHarmEncoder maps this to z_harm_a [16 dims].
  ARC-016 reframe: z_harm_a.norm as urgency for dynamic commit threshold.

## Results

| Metric | HIGH (6 hazards) | LOW (2 hazards) |
|--------|-----------------|-----------------|
| z_harm_a mean norm | 0.3923 | 0.4249 |
| z_harm_a / z_harm_a ratio | 0.92x | -- |
| autocorr_lag10 z_harm_a | -0.017 | -- |
| autocorr_lag10 z_harm_s | 0.061 | -- |
| step-std z_harm_a | 0.0257 | -- |
| step-std z_harm_s | 0.3686 | -- |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: z_harm_a responds to hazard density | FAIL | 0.3923 vs 0.4249 * 1.2 |
| C2: z_harm_a more autocorrelated than z_harm_s | FAIL | -0.017 > 0.061 |
| C3: z_harm_a step-variance < z_harm_s | PASS | 0.0257 < 0.3686 |
| C4: no fatal errors | PASS | -- |

Criteria met: 2/4 -> **FAIL**

## Failure Notes

- C1 FAIL: z_harm_a_high=0.3923 vs low=0.4249 -- affective stream does not respond to hazard density
- C2 FAIL: autocorr_a=-0.017 not > autocorr_s=0.061 -- EMA not adding temporal stability
