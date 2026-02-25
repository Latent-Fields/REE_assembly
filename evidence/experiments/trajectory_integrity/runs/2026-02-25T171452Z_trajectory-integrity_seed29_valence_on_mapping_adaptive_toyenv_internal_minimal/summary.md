# trajectory_integrity run summary

- condition: `valence_on_mapping_adaptive`
- seed: `29`
- status: `FAIL`
- backend: `internal_minimal`
- failure_signatures: `ledger_editing, explanation_policy_divergence, domination_lock_in, mech056:valence_mapping_competition`
- emitted_hooks: `HK-001, HK-002, HK-003, HK-004, HK-005, HK-007, HK-008, HK-009, HK-101, HK-102, HK-103, HK-104`
- model_source: `ree_v2_internal_minimal`
- synthetic_frame_fallback: `False`
- checkpoint_verified: `False`
- checkpoint_verify_reason: `not_jepa_inference_backend`

## Metrics
- commit_boundary_join_coverage_rate: `1.0`
- commitment_reversal_rate: `0.133333333333`
- conflict_signature_rate: `0.341666666667`
- domination_lock_in_events: `4.0`
- explanation_policy_divergence_rate: `0.07573451489`
- hippocampal_path_selection_entropy: `0.700763294111`
- hippocampal_retrieval_valence_skew: `0.342358687946`
- latent_continuity: `0.853958441484`
- latent_knn_overlap: `0.850779896301`
- latent_prediction_error_mean: `0.044573714626`
- latent_prediction_error_p95: `0.11063243668`
- latent_procrustes_drift: `0.132226540025`
- latent_residual_coverage_rate: `1.0`
- latent_trustworthiness: `0.866842932557`
- latent_uncertainty_calibration_error: `0.00819544968`
- ledger_edit_detected_count: `3.0`
- policy_error_rate: `0.091666666667`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
- valence_conditioned_recall_error: `0.167455252276`
