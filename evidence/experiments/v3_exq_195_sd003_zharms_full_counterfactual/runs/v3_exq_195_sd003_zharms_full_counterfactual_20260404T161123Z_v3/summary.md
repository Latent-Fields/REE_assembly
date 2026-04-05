# V3-EXQ-195 -- SD-003 Full Latent Counterfactual on z_harm_s (Post-SD-011)

**Status:** FAIL
**Claims:** SD-003, ARC-033
**Decision:** hybridize
**Seeds:** [42, 7, 123, 13] (0/4 PASS)
**Proposal:** EXP-0094

## Architecture

- HarmEncoder (SD-010): harm_obs (51-dim) -> z_harm_s (32-dim)
- ResidualHarmForward: z_harm_s + delta(z_harm_s, action) -> z_harm_s_next
  (identity-collapse fix: residual architecture, cf. E2.world_forward)
- E3.harm_eval_z_harm: z_harm_s -> harm score
- Fix #2: E3 trained on observed + forward-predicted z_harm_s states

## Attribution Results (seed means)

| Transition | harm_delta | causal_sig | n |
|---|---|---|---|
| none (locomotion)   | 0.3472 | -0.078252 | 74 |
| hazard_approach     | 0.3252 | 0.005512 | 821 |
| env_caused_hazard   | 0.4096 | 0.050113 | 14 |
| agent_caused_hazard | 0.3302 | 0.008602 | 32 |

- **harm_forward R2**: 0.9138
- **attribution_gap** (approach - env): -0.044601

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: attribution_gap > 0 | FAIL | -0.044601 |
| C2: causal_sig_approach > causal_sig_none | PASS | 0.005512 vs -0.078252 |
| C3: causal_sig_approach > 0.005 | PASS | 0.005512 |
| C4: harm_forward_r2 > 0.05 | PASS | 0.9138 |
| C5: n_approach >= 50 | PASS | 821 |
| C6: >= 3/4 seeds causal_sig > 0 | PASS | 0/4 |

Criteria met: 5/6 -> **FAIL**

## Failure Notes

- C1 FAIL: attribution_gap_mean=-0.044601 <= 0
