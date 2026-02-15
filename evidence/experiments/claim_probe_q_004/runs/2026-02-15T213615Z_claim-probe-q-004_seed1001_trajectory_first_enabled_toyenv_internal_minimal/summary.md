# claim_probe_q_004 run summary

- condition: `trajectory_first_enabled`
- seed: `1001`
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
- commitment_reversal_rate: `0.016666666667`
- domination_lock_in_events: `0.0`
- explanation_policy_divergence_rate: `0.030875802209`
- latent_prediction_error_mean: `0.027502345444`
- latent_prediction_error_p95: `0.070864935193`
- latent_residual_coverage_rate: `1.0`
- latent_uncertainty_calibration_error: `0.00754603004`
- ledger_edit_detected_count: `1.0`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
