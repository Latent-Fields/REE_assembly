# claim_probe_mech_059 run summary

- condition: `explicit_uncertainty_head`
- seed: `101`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `mech059:uncertainty_metric_gaming_detected`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-004, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- latent_prediction_error_mean: `0.151410496037`
- latent_prediction_error_p95: `0.21772308668`
- latent_residual_coverage_rate: `1.0`
- latent_uncertainty_calibration_error: `0.06600954335`
- precision_input_completeness_rate: `0.975`
- tri_loop_trace_coverage_rate: `1.0`
- uncertainty_coverage_rate: `0.75`
