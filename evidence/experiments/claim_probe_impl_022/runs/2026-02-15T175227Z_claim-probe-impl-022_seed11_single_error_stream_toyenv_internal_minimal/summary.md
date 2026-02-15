# claim_probe_impl_022 run summary

- condition: `single_error_stream`
- seed: `11`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `mech060:postcommit_channel_contamination, mech060:attribution_reliability_break, mech060:commitment_reversal_spike`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.45`
- cross_channel_leakage_rate: `0.866327364023`
- latent_prediction_error_mean: `0.233875957342`
- latent_prediction_error_p95: `0.540989640019`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.02284925893`
- pre_commit_error_signal_to_noise: `3.573350200463`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
