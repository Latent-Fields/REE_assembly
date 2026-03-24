# V3-EXQ-094 -- ARC-016: Harm Variance Commit (Rollout E3 Fix)

**Status:** FAIL
**Claims:** ARC-016
**Fixes:** EXQ-088 (E3 harm_eval head not trained on rollout distribution)

## Root Cause Fixed (EXQ-088)

In EXQ-088, agent.e3.harm_eval_z_harm_head was never trained during warmup.
std_params included it, but compute_prediction_loss() + compute_e2_loss() produce
no gradients through the harm_eval pathway, so the head stayed at random init.

Additionally: E3 at eval time receives z_harm from harm_bridge(E2.world_forward(z_world, a)),
but warmup only had the head see z_harm from HarmEncoder(harm_obs) -- a different
distribution. Even if the head had been trained, distribution mismatch would suppress
the variance signal.

Fix: explicit E3 training step in warmup loop using z_harm_bridge = harm_bridge(z_world).detach()
as input and the actual harm label as target. E3 now trains on exactly the
distribution it encounters at eval time.

## Sweep Results

| hazard_harm | harm_var_mean | commit_rate |
|-------------|---------------|-------------|
| 0.005 | 0.000001 | 1.000 |
| 0.01 | 0.000001 | 1.000 |
| 0.02 | 0.000001 | 1.000 |
| 0.05 | 0.000001 | 1.000 |
| 0.1 | 0.000001 | 1.000 |

- Pearson r(hazard_harm, harm_var_mean): -0.3287
- harm_var CV at mid level: 0.7897

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: harm_var increases at >= 3 transitions | FAIL | 1/4 |
| C2: Pearson r > 0.6 | FAIL | -0.3287 |
| C3: harm_var CV > 0.10 | PASS | 0.7897 |
| C4: commit_rate[low] > commit_rate[high] | FAIL | 1.000 vs 1.000 |
| C5: no fatal errors | PASS | - |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C1 FAIL: harm_var increases at only 1/4 transitions. harm_var_means: ['0.000001', '0.000001', '0.000001', '0.000001', '0.000001']
- C2 FAIL: Pearson r=-0.329 <= 0.6. Harm variance not scaling with danger.
- C4 FAIL: commit_rate[low=0.005]=1.000 <= commit_rate[high=0.1]=1.000
