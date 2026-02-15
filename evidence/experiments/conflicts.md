# Evidence Conflict Report

Generated: `2026-02-15T14:59:53.493960Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 4 | 1 | 0.4 | `2026-02-15_arc018_future_path_replay_followup` |
| `MECH-033` | directional | 4 | 1 | 0.4 | `2026-02-15_mech033_preplay_sequences_followup` |
| `MECH-056` | directional, source_disagreement | 23 | 24 | 0.979 | `2026-02-15_mech056_prioritized_replay_followup` |
| `MECH-058` | directional, mixed_evidence | 34 | 31 | 0.954 | `2026-02-15_mech058_byol_target_anchor_followup` |
| `MECH-059` | directional, mixed_evidence | 34 | 19 | 0.717 | `2026-02-15_mech059_uncertainty_decomposition_followup` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 41 | 37 | 0.949 | `2026-02-15_mech060_conflict_control_followup` |
| `Q-011` | directional | 1 | 4 | 0.4 | `2026-02-15_q011_reverse_replay_reward_followup` |
| `Q-017` | directional, source_disagreement | 15 | 13 | 0.929 | `2026-02-15_q017_uncertainty_neuromod_followup` |

## Conflict Details

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.792
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:30:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.75
  - `2026-02-15T15:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.786
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:35:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.74
  - `2026-02-15T15:11:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.74
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=23, weakens=24, conflict_ratio=0.979, overall_confidence=0.722
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:13:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Recurring failure signatures:
  - `stop:ledger_edit_detected_count>0` (26)
  - `stop:domination_lock_in_events>0` (22)
  - `ledger_editing` (21)
  - `stop:explanation_policy_divergence_rate>0.05` (18)
  - `domination_lock_in` (16)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=34, weakens=31, conflict_ratio=0.954, overall_confidence=0.703
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:14:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (21)
  - `mech058:ema_drift_under_shift` (15)
  - `mech058:latent_cluster_collapse` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_prediction_error_p95` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=34, weakens=19, conflict_ratio=0.717, overall_confidence=0.739
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:15:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (20)
  - `mech059:abstention_reliability_collapse` (12)
  - `mech059:calibration_slope_break` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_uncertainty_calibration_error` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=41, weakens=37, conflict_ratio=0.949, overall_confidence=0.693
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T15:16:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (28)
  - `mech060:attribution_reliability_break` (26)
  - `mech060:commitment_reversal_spike` (14)
  - `mech060:precommit_channel_contamination` (10)
  - `threshold:pre_commit_error_signal_to_noise` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-011
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=4, conflict_ratio=0.4, overall_confidence=0.628
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T23:00:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
  - `2026-02-15T15:17:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
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

### Q-017
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=15, weakens=13, conflict_ratio=0.929, overall_confidence=0.696
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:18:00Z` `literature` `targeted_review_mech_063` direction=`supports` confidence=0.79
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
