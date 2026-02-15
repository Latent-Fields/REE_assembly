# Evidence Conflict Report

Generated: `2026-02-15T14:54:27.997179Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 3 | 1 | 0.5 | `2026-02-14_v3hippo_bidirectional_replay_sequences_natneuro2007` |
| `MECH-033` | directional | 3 | 1 | 0.5 | `2026-02-14_v3hippo_preplay_future_sequences_nature2011` |
| `MECH-056` | directional | 20 | 14 | 0.824 | `2026-02-15T144904Z_trajectory-integrity_seed47_trajectory_first_ablated_toyenv_internal_minimal` |
| `MECH-058` | directional, mixed_evidence | 27 | 25 | 0.962 | `2026-02-15T144903Z_jepa-anchor-ablation_seed47_ema_anchor_on_toyenv_internal_minimal` |
| `MECH-059` | directional, mixed_evidence | 27 | 19 | 0.826 | `2026-02-15T144903Z_jepa-uncertainty-channels_seed47_explicit_uncertainty_head_toyenv_internal_minimal` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 34 | 31 | 0.954 | `exp_0021_20260215T144911050815Z` |
| `Q-011` | directional | 1 | 3 | 0.5 | `2026-02-14_q011_reverse_replay_reward_modulation_neuron2016` |
| `Q-017` | directional, source_disagreement | 8 | 7 | 0.933 | `exp_0032_20260215T144911111065Z` |

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
- Evidence breakdown: supports=20, weakens=14, conflict_ratio=0.824, overall_confidence=0.692
- Recent entries:
  - `2026-02-15T14:49:03Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:04Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:04Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:04Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `stop:ledger_edit_detected_count>0` (16)
  - `stop:domination_lock_in_events>0` (14)
  - `stop:explanation_policy_divergence_rate>0.05` (12)
  - `ledger_editing` (11)
  - `domination_lock_in` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=27, weakens=25, conflict_ratio=0.962, overall_confidence=0.676
- Recent entries:
  - `2026-02-15T14:49:03Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (15)
  - `mech058:ema_drift_under_shift` (13)
  - `mech058:latent_cluster_collapse` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_prediction_error_p95` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=27, weakens=19, conflict_ratio=0.826, overall_confidence=0.719
- Recent entries:
  - `2026-02-15T14:49:03Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T14:49:03Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T14:49:03Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (16)
  - `mech059:calibration_slope_break` (10)
  - `mech059:abstention_reliability_collapse` (8)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_uncertainty_calibration_error` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=34, weakens=31, conflict_ratio=0.954, overall_confidence=0.691
- Recent entries:
  - `2026-02-15T14:49:03Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:11.050815Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (22)
  - `mech060:attribution_reliability_break` (20)
  - `mech060:precommit_channel_contamination` (10)
  - `mech060:commitment_reversal_spike` (8)
  - `threshold:pre_commit_error_signal_to_noise` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-011
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=3, conflict_ratio=0.5, overall_confidence=0.557
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

### Q-017
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=8, weakens=7, conflict_ratio=0.933, overall_confidence=0.656
- Recent entries:
  - `2026-02-15T14:49:03Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:49:03Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:49:11.111065Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (6)
  - `q017:control_axis_entropy_collapse` (6)
  - `q017:control_axis_policy_loss_spike` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
