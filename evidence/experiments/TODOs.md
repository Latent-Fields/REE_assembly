# Experiment-Driven TODO Queue

Generated: `2026-02-14T20:53:08.829966Z`

Auto-generated from FAIL signatures in Experiment Pack runs.

## commit_dual_error_channels

- [ ] Investigate signature `mech060:precommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:postcommit_channel_contamination` (10 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `mech060:attribution_reliability_break` (8 FAIL run(s), latest `bridge_v2_mech_060_cross_channel_contamination_stress_s60022_20260214t185325220849z`).
- [ ] Investigate signature `threshold:pre_commit_error_signal_to_noise` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).
- [ ] Investigate signature `threshold:post_commit_error_attribution_gain` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).
- [ ] Investigate signature `threshold:cross_channel_leakage_rate` (2 FAIL run(s), latest `2026-02-14T030000Z_commit-dual-error-channels_seed29_single_error_stream`).

## jepa_anchor_ablation

- [ ] Investigate signature `mech058:ema_drift_under_shift` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:latent_cluster_collapse` (10 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `mech058:anchor_separation_collapse` (9 FAIL run(s), latest `bridge_v2_mech_058_anchor_drift_extreme_shift_s58022_20260214t185325228646z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-anchor-ablation_seed29_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_prediction_error_p95` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-anchor-ablation_seed29_ema_anchor_off`).
- [ ] Investigate signature `threshold:latent_rollout_consistency_rate` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-anchor-ablation_seed29_ema_anchor_off`).

## jepa_uncertainty_channels

- [ ] Investigate signature `mech059:calibration_slope_break` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:uncertainty_metric_gaming_detected` (10 FAIL run(s), latest `bridge_v2_mech_059_adversarial_uncertainty_gaming_s59022_20260214t185325225490z`).
- [ ] Investigate signature `mech059:abstention_reliability_collapse` (4 FAIL run(s), latest `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z`).
- [ ] Investigate signature `threshold:latent_prediction_error_mean` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:latent_uncertainty_calibration_error` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).
- [ ] Investigate signature `threshold:precision_input_completeness_rate` (2 FAIL run(s), latest `2026-02-14T030000Z_jepa-uncertainty-channels_seed29_deterministic_plus_dispersion`).

## trajectory_integrity

- [ ] Investigate signature `stop:ledger_edit_detected_count>0` (8 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `stop:domination_lock_in_events>0` (7 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
- [ ] Investigate signature `ledger_editing` (6 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_enabled_toyenv_internal_minimal`).
- [ ] Investigate signature `stop:explanation_policy_divergence_rate>0.05` (6 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
- [ ] Investigate signature `explanation_policy_divergence` (4 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
- [ ] Investigate signature `domination_lock_in` (4 FAIL run(s), latest `2026-02-14T183154Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal`).
