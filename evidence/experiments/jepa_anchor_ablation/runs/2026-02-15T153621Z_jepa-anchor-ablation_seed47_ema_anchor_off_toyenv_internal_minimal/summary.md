# jepa_anchor_ablation run summary

- condition: `ema_anchor_off`
- seed: `47`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `mech058:anchor_separation_collapse`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- e1_e2_timescale_separation_ratio: `1.260546531267`
- latent_prediction_error_mean: `0.043169989275`
- latent_prediction_error_p95: `0.116612959047`
- latent_residual_coverage_rate: `1.0`
- latent_rollout_consistency_rate: `1.0`
- precision_input_completeness_rate: `1.0`
- representation_drift_rate: `0.075`
- tri_loop_trace_coverage_rate: `1.0`
