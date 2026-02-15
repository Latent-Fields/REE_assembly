# Evidence Conflict Report

Generated: `2026-02-14T20:59:13.206518Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 3 | 1 | 0.5 | `2026-02-14_v3hippo_bidirectional_replay_sequences_natneuro2007` |
| `MECH-033` | directional | 3 | 1 | 0.5 | `2026-02-14_v3hippo_preplay_future_sequences_nature2011` |
| `MECH-056` | directional | 16 | 6 | 0.545 | `2026-02-14_v3hippo_reward_sequences_unexplored_space_elife2015` |
| `MECH-058` | directional, mixed_evidence | 21 | 18 | 0.923 | `2026-02-14_mech058_byol_ema_target_predictor_separation` |
| `MECH-059` | directional, mixed_evidence | 21 | 15 | 0.833 | `2026-02-14_v3jepa_uncertainty_decomposition_kendall_gal2017` |
| `MECH-060` | directional, mixed_evidence | 22 | 18 | 0.9 | `2026-02-14_v3pfc_modelbased_prediction_error_integration_neuron2011` |
| `Q-011` | directional | 1 | 3 | 0.5 | `2026-02-14_q011_reverse_replay_reward_modulation_neuron2016` |

## Conflict Details

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.766
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:30:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.765
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:35:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.74
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional
- Evidence breakdown: supports=16, weakens=6, conflict_ratio=0.545, overall_confidence=0.752
- Recent entries:
  - `2026-02-14T18:31:54Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T18:31:54Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.45
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:40:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.69
- Recurring failure signatures:
  - `stop:ledger_edit_detected_count>0` (8)
  - `stop:domination_lock_in_events>0` (7)
  - `ledger_editing` (6)
  - `stop:explanation_policy_divergence_rate>0.05` (6)
  - `explanation_policy_divergence` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=21, weakens=18, conflict_ratio=0.923, overall_confidence=0.682
- Recent entries:
  - `2026-02-14T18:53:25.227124Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-14T18:53:25.228121Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-14T18:53:25.228898Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
  - `2026-02-14T22:45:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (12)
  - `mech058:ema_drift_under_shift` (12)
  - `mech058:latent_cluster_collapse` (10)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_prediction_error_p95` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=21, weakens=15, conflict_ratio=0.833, overall_confidence=0.715
- Recent entries:
  - `2026-02-14T18:53:25.224836Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T18:53:25.225836Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
  - `2026-02-14T22:50:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (14)
  - `mech059:calibration_slope_break` (10)
  - `mech059:abstention_reliability_collapse` (6)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_uncertainty_calibration_error` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=22, weakens=18, conflict_ratio=0.9, overall_confidence=0.693
- Recent entries:
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T20:40:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
  - `2026-02-14T20:55:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.74
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
  - `2026-02-14T22:55:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`mixed` confidence=0.66
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (14)
  - `mech060:attribution_reliability_break` (12)
  - `mech060:precommit_channel_contamination` (10)
  - `threshold:pre_commit_error_signal_to_noise` (2)
  - `threshold:post_commit_error_attribution_gain` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-011
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=3, conflict_ratio=0.5, overall_confidence=0.558
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T23:00:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
- Recurring failure signatures:
  - `ledger_editing` (1)
  - `explanation_policy_divergence` (1)
  - `stop:ledger_edit_detected_count>0` (1)
  - `stop:explanation_policy_divergence_rate>0.05` (1)
  - `stop:domination_lock_in_events>0` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
