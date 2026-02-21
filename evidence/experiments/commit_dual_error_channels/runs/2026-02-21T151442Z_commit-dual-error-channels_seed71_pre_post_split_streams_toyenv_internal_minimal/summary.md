# commit_dual_error_channels run summary

- condition: `pre_post_split_streams`
- seed: `71`
- status: `PASS`
- backend: `internal_minimal`
- failure_signatures: `none`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.016666666667`
- cross_channel_leakage_rate: `0.026368492609`
- latent_prediction_error_mean: `0.180832264412`
- latent_prediction_error_p95: `0.412178413674`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.486818698916`
- pre_commit_error_signal_to_noise: `9.11452448095`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`

## Channel Provenance/Isolation
- corr_pre_post: `0.659212315222`
- corr_pre_realized: `0.819114287693`
- corr_post_realized: `0.969932986609`
- coupling_mean: `0.04`
- pre_noise_std: `0.042841572511`
