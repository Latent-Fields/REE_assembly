# claim_probe_mech_056 run summary

- condition: `trajectory_first_enabled`
- seed: `131`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `ledger_editing`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-004, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.1`
- domination_lock_in_events: `0.0`
- explanation_policy_divergence_rate: `0.031547113166`
- latent_prediction_error_mean: `0.027842429346`
- latent_prediction_error_p95: `0.06297453047`
- latent_residual_coverage_rate: `1.0`
- latent_uncertainty_calibration_error: `0.007200702342`
- ledger_edit_detected_count: `1.0`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
