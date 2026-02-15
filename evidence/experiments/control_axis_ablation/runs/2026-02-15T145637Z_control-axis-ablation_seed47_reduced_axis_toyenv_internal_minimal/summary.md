# control_axis_ablation run summary

- condition: `reduced_axis`
- seed: `47`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `q017:control_axis_stability_drop, q017:control_axis_entropy_collapse`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-006, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- control_axis_policy_loss_rate: `0.116666666667`
- control_axis_readout_entropy: `0.631218610304`
- control_axis_stability_index: `0.704089052409`
- latent_prediction_error_mean: `0.197804597479`
- latent_prediction_error_p95: `0.26298579175`
- latent_residual_coverage_rate: `1.0`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
