# commit_dual_error_channels run summary

- condition: `pre_post_split_streams`
- seed: `53`
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
- cross_channel_leakage_rate: `0.031759445166`
- latent_prediction_error_mean: `0.183270275395`
- latent_prediction_error_p95: `0.449298781622`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.442944707381`
- pre_commit_error_signal_to_noise: `8.291579394323`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`

## Channel Provenance/Isolation
- corr_pre_post: `0.793986129147`
- corr_pre_realized: `0.87956008396`
- corr_post_realized: `0.98650479134`
- coupling_mean: `0.04`
- pre_noise_std: `0.038783190906`
