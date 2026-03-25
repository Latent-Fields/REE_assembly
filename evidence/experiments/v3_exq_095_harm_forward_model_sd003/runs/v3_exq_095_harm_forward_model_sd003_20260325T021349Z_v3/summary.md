# V3-EXQ-095 -- SD-003 Redesign: HarmForwardModel Counterfactual

**Status:** FAIL
**Claims:** ARC-033, SD-011, SD-003
**Supersedes:** EXQ-093/094 (both confirmed bridge_r2=0; bridge approach infeasible)
**World:** CausalGridWorldV2 (6 hazards, 3 resources, 12x12)
**Protocol:** Three-phase (terrain 300 -> calib 150 -> eval 100)

## Redesign: HarmForwardModel replaces HarmBridge

HarmBridge (z_world -> z_harm) has bridge_r2=0 by design: SD-010 makes z_world
perp z_harm. HarmForwardModel operates entirely within the harm stream:
    z_harm_s_cf = HarmForwardModel(z_harm_s_actual, a_cf)
    causal_sig = E3(z_harm_s_actual) - E3(z_harm_s_cf)

This is tractable: z_harm_s (sensory-discriminative, Adelta-pathway analog) encodes
proximity that changes predictably with movement. ARC-033 validates this approach.

## Results

| Metric | Value | Baseline (EXQ-093/094) |
|--------|-------|------------------------|
| HarmForwardModel R2 | 0.0000 | bridge_r2=0.0 (infeasible) |
| causal_sig_none | -0.015784 | -- |
| causal_sig_approach | -0.014481 | 0.065 |
| causal_sig_contact | -0.011877 | 0.116 |
| calibration_gap_approach | 0.0780 | 0.084 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: harm_fwd_r2 > 0.2 (forward model learns) | FAIL | 0.0000 |
| C2: causal_approach > 0.001 | FAIL | -0.014481 |
| C3: causal_contact > causal_approach (MECH-102) | PASS | -0.011877 vs -0.014481 |
| C4: cal_gap > 0.05 | PASS | 0.0780 |
| C5: harm_none < harm_approach * 0.90 | PASS | 0.5691 < 0.5824 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C1 FAIL: harm_fwd_r2=0.0000 <= 0.2 (forward model not learning harm dynamics)
- C2 FAIL: causal_approach=-0.014481 <= 0.001
