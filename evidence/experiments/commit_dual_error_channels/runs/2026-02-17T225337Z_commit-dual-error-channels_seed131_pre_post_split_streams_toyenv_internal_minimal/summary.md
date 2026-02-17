# commit_dual_error_channels run summary

- condition: `pre_post_split_streams`
- seed: `131`
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
- commitment_reversal_rate: `0.008333333333`
- cross_channel_leakage_rate: `0.024603659003`
- latent_prediction_error_mean: `0.187353770154`
- latent_prediction_error_p95: `0.434403137986`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.54091321872`
- pre_commit_error_signal_to_noise: `5.552521189694`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`

## Channel Provenance/Isolation
- corr_pre_post: `0.615091475067`
- corr_pre_realized: `0.770237337833`
- corr_post_realized: `0.975150556552`
- coupling_mean: `0.04`
- pre_noise_std: `0.043549773638`
