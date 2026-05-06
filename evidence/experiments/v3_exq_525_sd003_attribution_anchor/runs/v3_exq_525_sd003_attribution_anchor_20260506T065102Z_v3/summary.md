# V3-EXQ-525 -- SD-003 Harm Attribution Anchor

**Outcome:** PASS
**Claims:** SD-003, ARC-033
**Supersedes:** V3-EXQ-205
**Seeds:** [42, 7, 123, 13]  **P0:** 100 eps  **P1:** 200 eps  **Eval:** 50 eps

## Architecture

- P0: HarmEncoder warmup (autoencoder + center-cell regression)
- P1: Frozen encoder; ResidualHarmForward + E3.harm_eval_z_harm on .detach()ed z_harm_s
- Pipeline: causal_sig = eval(harm_fwd(z, a_actual)) - eval(harm_fwd(z, a_cf))
- attribution_gap = causal_sig(approach) - causal_sig(none)

## Results by Seed

| Seed | hf_r2 | gap | intact_approach | intact_none | intact_vs_ablated | null_cf_max | n_approach |
|------|-------|-----|-----------------|------------|------------------|------------|-----------|
| 42 | 0.9209 | 0.126225 | 0.006293 | -0.119932 | 0.002478 | 0.00e+00 | 845 |
| 7 | 0.9215 | 0.115477 | 0.013298 | -0.102179 | 0.010538 | 0.00e+00 | 876 |
| 123 | 0.9213 | 0.115882 | 0.012721 | -0.103161 | 0.016355 | 0.00e+00 | 848 |
| 13 | 0.9128 | 0.102392 | 0.008382 | -0.094011 | 0.015340 | 0.00e+00 | 783 |


## Aggregate

- hf_r2 mean: 0.9191 +/- 0.0037
- attribution_gap mean: 0.114994 +/- 0.008455
- intact_approach mean: 0.010173
- intact_vs_ablated mean: 0.011178

## PASS Criteria

| Criterion | Value | Required | Result |
|-----------|-------|---------|--------|
| C1 attribution_gap | 0.114994 | > 0.002 | PASS |
| C2 hf_r2 | 0.9191 | > 0.05 | PASS |
| C3 approach>0 | 4/4 seeds | >= 3 | PASS |
| C4 n_approach | 838 | >= 50 | PASS |
| C5 null_cf_max | 0.00e+00 | < 1e-05 | PASS |
| C6 intact>ablated | 4/4 seeds | >= 3 | PASS |

Criteria met: 6/6 -> **PASS**

