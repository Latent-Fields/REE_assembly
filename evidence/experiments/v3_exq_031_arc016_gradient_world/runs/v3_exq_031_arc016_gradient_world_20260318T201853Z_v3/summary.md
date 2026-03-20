# V3-EXQ-031 — ARC-016 Dynamic Precision Test on CausalGridWorldV2 (Gradient World)

**Status:** PASS
**World type:** CausalGridWorldV2 (use_proxy_fields=True) — body_obs_dim=12, world_obs_dim=250
**Training:** 1000 eps (stable: num_hazards=3, drift_interval=100, drift_prob=0.0)
**Eval stable:** 50 eps | **Eval perturbed:** 50 eps (num_hazards=20, drift_interval=1, drift_prob=1.0)
**Recovery:** 30 eps
**Seed:** 0 | **alpha_world:** 0.9 (SD-008) | **proximity_scale:** 0.05

## Motivation (ARC-016 on Gradient World)

EXQ-018 validated ARC-016 on the original CausalGridWorld (sparse occupancy, body_obs=10,
world_obs=200). EXQ-031 re-tests on CausalGridWorldV2, which adds proxy-gradient fields:
- hazard_field_view (25ch, decay=0.5): continuous proximity gradient toward hazards
- resource_field_view (25ch): continuous gradient toward resources
- harm_exposure, benefit_exposure: EMA interoceptive channels in body_state

These gradient channels provide richer signal for E2.world_forward: when hazards drift
(perturbed env), field values shift smoothly over many timesteps, producing larger and
more structured prediction errors compared to sparse occupancy changes. The ARC-016
variance signal should be amplified.

**Separate world_forward optimizer (MECH-069):** E2.world_transition and
E2.world_action_encoder use a dedicated Adam(lr=1e-3) optimizer, isolated from main
agent updates. This keeps world-model training from interfering with the E1/E2-self
training signal — an architectural requirement given incommensurable error channels.

**Architecture:** precision = 1 / (running_variance + ε); committed = running_variance < commit_threshold

## Phase Results

| Phase | mean_var | mean_precision | commit_rate | n_decisions | mean_pred_err |
|---|---|---|---|---|---|
| Training (stable) | 0.0005 | 12926.039 | 0.995 | 2309 | 0.00010 |
| Eval stable | 0.0090 | 10365.021 | 0.905 | 116 | 0.00009 |
| Eval perturbed | 0.0490 | 1544.934 | 0.500 | 26 | 0.00016 |
| Recovery | 0.0144 | 7827.790 | 0.849 | 73 | 0.00009 |

**Key differences:**
- running_variance: perturbed - stable = 0.0400
- precision: stable - perturbed = 8820.0870
- commit_rate: stable - perturbed = 0.4052

## Comparison to EXQ-018 (original CausalGridWorld)

Gradient world amplified variance gap: 0.0400 vs EXQ-018 baseline ~0.0011 (+0.0389). Prediction confirmed: continuous field channels drive larger E2 prediction errors.

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: var_diff > 0.001 (calibrated from EXQ-018: stable≈0.0027, perturbed≈0.0038) | PASS | 0.0400 |
| C2: precision_stable > precision_perturbed | PASS | 8820.0870 |
| C3: commit_rate_stable > commit_rate_perturbed | PASS | 0.4052 |
| C4: n_stable_decisions >= 20 | PASS | 116 |
| C5: No fatal errors | PASS | 0 |

Criteria met: 5/5 → **PASS**

