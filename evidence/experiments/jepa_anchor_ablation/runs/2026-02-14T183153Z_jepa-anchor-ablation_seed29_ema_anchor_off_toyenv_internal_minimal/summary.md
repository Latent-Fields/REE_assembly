# jepa_anchor_ablation run summary

- condition: `ema_anchor_off`
- seed: `29`
- status: `PASS`
- backend: `internal_minimal`
- failure_signatures: `mech058:ema_drift_under_shift, mech058:anchor_separation_collapse`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- e1_e2_timescale_separation_ratio: `1.266066638779`
- latent_prediction_error_mean: `0.048863245646`
- latent_prediction_error_p95: `0.111849720352`
- latent_residual_coverage_rate: `1.0`
- latent_rollout_consistency_rate: `1.0`
- precision_input_completeness_rate: `1.0`
- representation_drift_rate: `0.141666666667`
