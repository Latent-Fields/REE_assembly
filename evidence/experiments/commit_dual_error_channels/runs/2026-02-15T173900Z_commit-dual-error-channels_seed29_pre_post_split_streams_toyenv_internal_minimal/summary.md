# commit_dual_error_channels run summary

- condition: `pre_post_split_streams`
- seed: `29`
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
- commitment_reversal_rate: `0.0`
- cross_channel_leakage_rate: `0.02881857174`
- latent_prediction_error_mean: `0.168337620546`
- latent_prediction_error_p95: `0.373024878614`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.469246636745`
- pre_commit_error_signal_to_noise: `14.370068730283`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`

## Channel Provenance/Isolation
- corr_pre_post: `0.720464293495`
- corr_pre_realized: `0.844834063422`
- corr_post_realized: `0.978080700167`
- coupling_mean: `0.04`
- pre_noise_std: `0.039349686204`
