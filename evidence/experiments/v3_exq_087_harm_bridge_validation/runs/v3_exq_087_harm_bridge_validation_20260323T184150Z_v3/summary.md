# V3-EXQ-087 -- HarmBridge Counterfactual Validation

**Status:** FAIL
**Claims:** SD-010, SD-003
**World:** CausalGridWorldV2 (6 hazards, 3 resources, 12x12)
**Protocol:** Three-phase (terrain 300 -> calib 150 -> eval 100)

## HarmBridge Architecture

HarmBridge is a 2-layer MLP: z_world(32) -> z_harm(32).
Trained to approximate HarmEncoder(harm_obs) in latent space.

Counterfactual pipeline:
    z_harm_cf = harm_bridge(E2.world_forward(z_world, a_cf))

This eliminates the linear z_world -> harm_obs_approx intermediate step used in EXQ-058c,
working entirely in latent space.

## Results

| Metric | Value |
|--------|-------|
| HarmBridge alignment R2 | 0.0000 |
| causal_sig_none | -0.086085 |
| causal_sig_approach | 0.003054 |
| causal_sig_contact | 0.109451 |
| calibration_gap_approach | 0.0967 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: causal_approach > 0.001 | PASS | 0.003054 |
| C2: cal_gap > 0.05 | PASS | 0.0967 |
| C3: harm_none < harm_approach * 0.80 | FAIL | 0.5140 < 0.4886 |
| C4: causal_contact > causal_approach | PASS | 0.109451 vs 0.003054 |
| C5: bridge_r2 > 0.5 | FAIL | 0.0000 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C3 FAIL: harm_none=0.5140 not < harm_approach*0.80=0.4886
- C5 FAIL: bridge_r2=0.0000 <= 0.5
