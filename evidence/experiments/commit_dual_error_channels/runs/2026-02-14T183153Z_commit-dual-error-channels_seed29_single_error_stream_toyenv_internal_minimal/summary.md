# commit_dual_error_channels run summary

- condition: `single_error_stream`
- seed: `29`
- status: `PASS`
- backend: `internal_minimal`
- failure_signatures: `mech060:postcommit_channel_contamination, mech060:attribution_reliability_break`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commitment_reversal_rate: `0.008333333333`
- cross_channel_leakage_rate: `0.850833961284`
- latent_prediction_error_mean: `0.185030895868`
- latent_prediction_error_p95: `0.43271608408`
- latent_residual_coverage_rate: `1.0`
- post_commit_error_attribution_gain: `0.033604431738`
- pre_commit_error_signal_to_noise: `4.184498611488`
- precision_input_completeness_rate: `1.0`
