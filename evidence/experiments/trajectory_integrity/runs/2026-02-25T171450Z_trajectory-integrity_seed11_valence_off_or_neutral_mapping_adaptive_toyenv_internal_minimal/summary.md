# trajectory_integrity run summary

- condition: `valence_off_or_neutral_mapping_adaptive`
- seed: `11`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `domination_lock_in`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-004, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.058333333333`
- conflict_signature_rate: `0.075`
- domination_lock_in_events: `4.0`
- explanation_policy_divergence_rate: `0.037258460734`
- hippocampal_path_selection_entropy: `0.497196386214`
- hippocampal_retrieval_valence_skew: `0.100823682919`
- latent_continuity: `0.893318685229`
- latent_knn_overlap: `0.891305546634`
- latent_prediction_error_mean: `0.029251761682`
- latent_prediction_error_p95: `0.070791148958`
- latent_procrustes_drift: `0.103506553967`
- latent_residual_coverage_rate: `1.0`
- latent_trustworthiness: `0.904600007275`
- latent_uncertainty_calibration_error: `0.006657190416`
- ledger_edit_detected_count: `0.0`
- policy_error_rate: `0.041666666667`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
- valence_conditioned_recall_error: `0.077332883189`
