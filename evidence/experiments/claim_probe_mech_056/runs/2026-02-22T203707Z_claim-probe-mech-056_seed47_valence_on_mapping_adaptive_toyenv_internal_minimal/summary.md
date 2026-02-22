# claim_probe_mech_056 run summary

- condition: `valence_on_mapping_adaptive`
- seed: `47`
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
- commitment_reversal_rate: `0.1`
- conflict_signature_rate: `0.258333333333`
- domination_lock_in_events: `1.0`
- explanation_policy_divergence_rate: `0.075505788521`
- hippocampal_path_selection_entropy: `0.698011669791`
- hippocampal_retrieval_valence_skew: `0.342116521508`
- latent_continuity: `0.854334139756`
- latent_knn_overlap: `0.852115936753`
- latent_prediction_error_mean: `0.046254614161`
- latent_prediction_error_p95: `0.118815519814`
- latent_procrustes_drift: `0.132183663377`
- latent_residual_coverage_rate: `1.0`
- latent_trustworthiness: `0.866429844807`
- latent_uncertainty_calibration_error: `0.008848378885`
- ledger_edit_detected_count: `3.0`
- policy_error_rate: `0.033333333333`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
- valence_conditioned_recall_error: `0.167123987172`
