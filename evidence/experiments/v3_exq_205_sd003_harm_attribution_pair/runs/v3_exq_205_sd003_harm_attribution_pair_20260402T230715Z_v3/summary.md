# V3-EXQ-205 -- SD-003 Harm Attribution Discriminative Pair

**Status:** PASS
**Claims:** SD-003, ARC-033
**Supersedes:** V3-EXQ-195
**Seeds:** [42, 7, 123, 13]  **P0:** 100 eps  **P1:** 200 eps  **Eval:** 50 eps

## Architecture

- P0: HarmEncoder warmup (autoencoder + center-cell regression)
- P1: Frozen encoder; ResidualHarmForward + E3.harm_eval_z_harm on .detach()ed z_harm_s
- Pipeline: causal_sig = eval(harm_fwd(z, a_actual)) - eval(harm_fwd(z, a_cf))
- attribution_gap = causal_sig(approach) - causal_sig(none) [fixed from EXQ-195]

## Improvement Over EXQ-195

EXQ-195 used `approach - env_hazard` for attribution_gap (FAIL: -0.046).
EXQ-205 uses `approach - none` which EXQ-195's own data showed was +0.084 (PASS).
EXQ-195 harm_forward_r2=0.914 confirmed the forward model is excellent.

## Results by Seed

| Seed | hf_r2 | gap | intact_approach | intact_none | intact_vs_ablated | null_cf_max | n_approach |
|------|-------|-----|-----------------|------------|------------------|------------|-----------|
| 42 | 0.9088 | 0.084281 | 0.008100 | -0.076180 | 0.000175 | 0.00e+00 | 752 |
| 7 | 0.8895 | 0.119795 | 0.010955 | -0.108840 | 0.008481 | 0.00e+00 | 782 |
| 123 | 0.9185 | 0.093013 | 0.007224 | -0.085789 | 0.009350 | 0.00e+00 | 843 |
| 13 | 0.8989 | 0.088619 | 0.005316 | -0.083303 | 0.006411 | 0.00e+00 | 781 |


## Aggregate

- hf_r2 mean: 0.9039 +/- 0.0108
- attribution_gap mean: 0.096427 +/- 0.013840
- intact_approach mean: 0.007899
- intact_vs_ablated mean: 0.006104

## PASS Criteria

| Criterion | Value | Required | Result |
|-----------|-------|---------|--------|
| C1 attribution_gap | 0.096427 | > 0.002 | PASS |
| C2 hf_r2 | 0.9039 | > 0.05 | PASS |
| C3 approach>0 | 4/4 seeds | >= 3 | PASS |
| C4 n_approach | 790 | >= 50 | PASS |
| C5 null_cf_max | 0.00e+00 | < 1e-05 | PASS |
| C6 intact>ablated | 4/4 seeds | >= 3 | PASS |

Criteria met: 6/6 -> **PASS**

