# commit_dual_error_channels run summary

- condition: `pre_post_split_streams`
- seed: `47`
- status: `PASS`
- backend: `internal_minimal`
- failure_signatures: `none`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commitment_reversal_rate: `0.516666666667`
- cross_channel_leakage_rate: `0.107188669515`
- latent_prediction_error_mean: `0.190751653072`
- latent_prediction_error_p95: `0.458684603328`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.42627642074`
- pre_commit_error_signal_to_noise: `9.420406232295`
- precision_input_completeness_rate: `1.0`
