# claim_probe_mech_061 run summary

- condition: `pre_post_split_streams`
- seed: `11`
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
- cross_channel_leakage_rate: `0.024126362797`
- latent_prediction_error_mean: `0.162885969918`
- latent_prediction_error_p95: `0.412779882704`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.517204923973`
- pre_commit_error_signal_to_noise: `6.987054196711`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
