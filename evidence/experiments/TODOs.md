# Experiment-Driven TODO Queue

Generated: `2026-02-15T11:20:45.619956Z`

Auto-generated from FAIL signatures in Experiment Pack runs.

## commit_dual_error_channels

- [ ] Investigate signature `mech060:precommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (8 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `threshold:pre_commit_error_signal_to_noise` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).
- [ ] Investigate signature `threshold:post_commit_error_attribution_gain` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).
- [ ] Investigate signature `threshold:cross_channel_leakage_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_commit-dual-error-channels_seed47_single_error_stream`).

## jepa_anchor_ablation

- [ ] Investigate signature `mech058:ema_drift_under_shift` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:latent_cluster_collapse` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:anchor_separation_collapse` (9 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_prediction_error_p95` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_rollout_consistency_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-anchor-ablation_seed47_ema_anchor_off`).

## jepa_uncertainty_channels

- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:uncertainty_coverage_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_jepa-uncertainty-channels_seed47_deterministic_plus_dispersion`).

## trajectory_integrity

- [ ] Investigate signature `stop:ledger_edit_detected_count>0` (11 FAIL run(s), latest `2026-02-14T200000Z_trajectory-integrity_seed47_trajectory_first_ablated`).
- [ ] Investigate signature `stop:domination_lock_in_events>0` (10 FAIL run(s), latest `2026-02-14T200000Z_trajectory-integrity_seed47_trajectory_first_ablated`).
- [ ] Investigate signature `stop:explanation_policy_divergence_rate>0.05` (9 FAIL run(s), latest `2026-02-14T200000Z_trajectory-integrity_seed47_trajectory_first_ablated`).
- [ ] Investigate signature `ledger_editing` (6 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `threshold:ledger_edit_detected_count` (5 FAIL run(s), latest `2026-02-14T200000Z_trajectory-integrity_seed47_trajectory_first_ablated`).
- [ ] Investigate signature `threshold:explanation_policy_divergence_rate` (5 FAIL run(s), latest `2026-02-14T200000Z_trajectory-integrity_seed47_trajectory_first_ablated`).
