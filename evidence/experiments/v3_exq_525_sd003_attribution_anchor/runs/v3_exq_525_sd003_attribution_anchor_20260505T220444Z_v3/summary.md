# V3-EXQ-525 -- SD-003 Harm Attribution Anchor

**Outcome:** FAIL
**Claims:** SD-003, ARC-033
**Supersedes:** V3-EXQ-205
**Seeds:** [42]  **P0:** 5 eps  **P1:** 5 eps  **Eval:** 5 eps

## Architecture

- P0: HarmEncoder warmup (autoencoder + center-cell regression)
- P1: Frozen encoder; ResidualHarmForward + E3.harm_eval_z_harm on .detach()ed z_harm_s
- Pipeline: causal_sig = eval(harm_fwd(z, a_actual)) - eval(harm_fwd(z, a_cf))
- attribution_gap = causal_sig(approach) - causal_sig(none)

## Results by Seed

| Seed | hf_r2 | gap | intact_approach | intact_none | intact_vs_ablated | null_cf_max | n_approach |
|------|-------|-----|-----------------|------------|------------------|------------|-----------|
| 42 | 0.3363 | -0.001559 | -0.001559 | 0.000000 | -0.000631 | 0.00e+00 | 48 |


## Aggregate

- hf_r2 mean: 0.3363 +/- 0.0000
- attribution_gap mean: -0.001559 +/- 0.000000
- intact_approach mean: -0.001559
- intact_vs_ablated mean: -0.000631

## PASS Criteria

| Criterion | Value | Required | Result |
|-----------|-------|---------|--------|
| C1 attribution_gap | -0.001559 | > 0.002 | FAIL |
| C2 hf_r2 | 0.3363 | > 0.05 | PASS |
| C3 approach>0 | 0/1 seeds | >= 3 | FAIL |
| C4 n_approach | 48 | >= 50 | FAIL |
| C5 null_cf_max | 0.00e+00 | < 1e-05 | PASS |
| C6 intact>ablated | 0/1 seeds | >= 3 | FAIL |

Criteria met: 2/6 -> **FAIL**

## Failure Notes

- C1 FAIL: attribution_gap_mean=-0.001559 <= 0.002
- C3 FAIL: causal_sig_approach > 0 in 0/1 seeds (need 3)
- C4 FAIL: n_approach_mean=48 < 50
- C6 FAIL: intact > ablated in 0/1 seeds (need 3)
