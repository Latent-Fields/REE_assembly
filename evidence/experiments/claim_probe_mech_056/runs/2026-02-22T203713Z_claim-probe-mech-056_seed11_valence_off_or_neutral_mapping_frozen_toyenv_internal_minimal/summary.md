# claim_probe_mech_056 run summary

- condition: `valence_off_or_neutral_mapping_frozen`
- seed: `11`
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
- commitment_reversal_rate: `0.033333333333`
- conflict_signature_rate: `0.041666666667`
- domination_lock_in_events: `1.0`
- explanation_policy_divergence_rate: `0.032928989479`
- hippocampal_path_selection_entropy: `0.433520037629`
- hippocampal_retrieval_valence_skew: `0.03573449465`
- latent_continuity: `0.913760994719`
- latent_knn_overlap: `0.913668129086`
- latent_prediction_error_mean: `0.026401736331`
- latent_prediction_error_p95: `0.064069256297`
- latent_procrustes_drift: `0.092575224555`
- latent_residual_coverage_rate: `1.0`
- latent_trustworthiness: `0.922289270021`
- latent_uncertainty_calibration_error: `0.007330341626`
- ledger_edit_detected_count: `2.0`
- policy_error_rate: `0.016666666667`
- precision_input_completeness_rate: `1.0`
- tri_loop_trace_coverage_rate: `1.0`
- valence_conditioned_recall_error: `0.068728267827`
