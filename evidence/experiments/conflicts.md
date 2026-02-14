# Evidence Conflict Report

Generated: `2026-02-14T18:40:06.310940Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 2 | 1 | 0.667 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-033` | directional | 2 | 1 | 0.667 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-056` | directional | 6 | 3 | 0.667 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-058` | directional, source_disagreement, mixed_evidence | 9 | 11 | 0.9 | `2026-02-14_v3jepa_ijepa_control_plane_gap` |
| `MECH-059` | directional, source_disagreement, mixed_evidence | 9 | 11 | 0.9 | `2026-02-14_v3jepa_vjvcr_uncertainty_stream_limits` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 11 | 11 | 1 | `2026-02-14_v3jepa_vjvcr_uncertainty_stream_limits` |
| `Q-011` | directional | 1 | 2 | 0.667 | `2026-02-14_q011_prioritized_replay_vs_entropy_floor_natneuro2018` |

## Conflict Details

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.68
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=2, weakens=1, conflict_ratio=0.667, overall_confidence=0.68
- Recent entries:
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional
- Evidence breakdown: supports=6, weakens=3, conflict_ratio=0.667, overall_confidence=0.665
- Recent entries:
  - `2026-02-14T03:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T03:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-14T15:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Recurring failure signatures:
  - `stop:ledger_edit_detected_count>0` (3)
  - `stop:explanation_policy_divergence_rate>0.05` (3)
  - `stop:domination_lock_in_events>0` (3)
  - `threshold:ledger_edit_detected_count` (2)
  - `threshold:explanation_policy_divergence_rate` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=9, weakens=11, conflict_ratio=0.9, overall_confidence=0.665
- Recent entries:
  - `2026-02-14T13:43:14.580567Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-14T13:43:14.582817Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-14T13:43:14.583504Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-14T15:01:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
- Recurring failure signatures:
  - `mech058:ema_drift_under_shift` (6)
  - `mech058:latent_cluster_collapse` (6)
  - `mech058:anchor_separation_collapse` (5)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_prediction_error_p95` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=9, weakens=11, conflict_ratio=0.9, overall_confidence=0.702
- Recent entries:
  - `2026-02-14T13:43:14.578065Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T13:43:14.578626Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T15:02:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
- Recurring failure signatures:
  - `mech059:calibration_slope_break` (6)
  - `mech059:uncertainty_metric_gaming_detected` (6)
  - `mech059:abstention_reliability_collapse` (4)
  - `threshold:latent_prediction_error_mean` (2)
  - `threshold:latent_uncertainty_calibration_error` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=11, weakens=11, conflict_ratio=1, overall_confidence=0.724
- Recent entries:
  - `2026-02-14T15:03:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T20:40:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
  - `2026-02-14T20:55:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.74
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
- Recurring failure signatures:
  - `mech060:precommit_channel_contamination` (6)
  - `mech060:postcommit_channel_contamination` (6)
  - `mech060:attribution_reliability_break` (4)
  - `threshold:pre_commit_error_signal_to_noise` (2)
  - `threshold:post_commit_error_attribution_gain` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-011
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=2, conflict_ratio=0.667, overall_confidence=0.475
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
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
