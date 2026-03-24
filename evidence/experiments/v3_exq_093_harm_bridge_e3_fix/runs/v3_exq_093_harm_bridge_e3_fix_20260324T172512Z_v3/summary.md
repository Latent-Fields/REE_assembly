# V3-EXQ-093 -- HarmBridge Counterfactual Validation (E3 Head Fix)

**Status:** FAIL
**Claims:** SD-010, SD-003
**Fixes:** EXQ-087 (E3 harm_eval head never trained)
**World:** CausalGridWorldV2 (6 hazards, 3 resources, 12x12)
**Protocol:** Three-phase (terrain 300 -> calib 150 -> eval 100)

## Root Cause Fixed (EXQ-087)

In EXQ-087, agent.e3.harm_eval_z_harm_head was excluded from opt_harm, so
loss_he = MSE(harm_eval_z_harm(z_harm), label) computed gradients through the head
but never applied them. Phase 2 then re-trained the head from scratch on top of a
HarmEncoder that had optimised toward a random head output.

Fix: opt_harm now includes both harm_enc.parameters() and
agent.e3.harm_eval_z_harm_head.parameters(). The head and encoder train jointly
from the start of Phase 1.

## Results

| Metric | Value |
|--------|-------|
| HarmBridge alignment R2 | 0.0000 |
| causal_sig_none | -0.016635 |
| causal_sig_approach | 0.064884 |
| causal_sig_contact | 0.116065 |
| calibration_gap_approach | 0.0836 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: causal_approach > 0.001 | PASS | 0.064884 |
| C2: cal_gap > 0.05 | PASS | 0.0836 |
| C3: harm_none < harm_approach * 0.80 | FAIL | 0.5650 < 0.5188 |
| C4: causal_contact > causal_approach | PASS | 0.116065 vs 0.064884 |
| C5: bridge_r2 > 0.5 | FAIL | 0.0000 |

Criteria met: 3/5 -> **FAIL**

## Failure Notes

- C3 FAIL: harm_none=0.5650 not < harm_approach*0.80=0.5188
- C5 FAIL: bridge_r2=0.0000 <= 0.5
