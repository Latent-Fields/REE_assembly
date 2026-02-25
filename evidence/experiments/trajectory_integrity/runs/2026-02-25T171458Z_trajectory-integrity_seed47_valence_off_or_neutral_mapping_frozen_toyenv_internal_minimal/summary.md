# trajectory_integrity run summary

- condition: `valence_off_or_neutral_mapping_frozen`
- seed: `47`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `ledger_editing, domination_lock_in`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-004, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.008333333333`
- conflict_signature_rate: `0.033333333333`
- domination_lock_in_events: `1.0`
- explanation_policy_divergence_rate: `0.032969222647`
- hippocampal_path_selection_entropy: `0.431824364365`
- hippocampal_retrieval_valence_skew: `0.034619135204`
- latent_continuity: `0.913740445686`
- latent_knn_overlap: `0.911997797782`
- latent_prediction_error_mean: `0.027432129524`
- latent_prediction_error_p95: `0.074253417938`
- latent_procrustes_drift: `0.093416087074`
- latent_residual_coverage_rate: `1.0`
- latent_trustworthiness: `0.921794042166`
- latent_uncertainty_calibration_error: `0.007719831736`
- ledger_edit_detected_count: `3.0`
- policy_error_rate: `0.0`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
- valence_conditioned_recall_error: `0.068897454733`
