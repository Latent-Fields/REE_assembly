# tri_loop_arbitration_policy run summary

- condition: `weighted_merge`
- seed: `89`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `q016:tri_loop_conflict_spike, q016:tri_loop_alignment_break`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- latent_prediction_error_mean: `0.171668414753`
- latent_prediction_error_p95: `0.240136205021`
- latent_residual_coverage_rate: `1.0`
- precision_input_completeness_rate: `1.0`
- tri_loop_arbitration_override_rate: `0.15`
- tri_loop_gate_conflict_rate: `0.166666666667`
- tri_loop_policy_alignment_rate: `0.831237744351`
- tri_loop_trace_coverage_rate: `1.0`
