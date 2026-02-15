# Evidence Conflict Report

Generated: `2026-02-15T15:02:46.495933Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 5 | 1 | 0.333 | `2026-02-15_arc018_lit-0005_completion` |
| `MECH-033` | directional | 5 | 1 | 0.333 | `2026-02-15_mech033_lit-0008_completion` |
| `MECH-056` | directional, source_disagreement | 24 | 24 | 1 | `2026-02-15_mech056_lit-0014_completion` |
| `MECH-058` | directional, mixed_evidence | 35 | 31 | 0.939 | `2026-02-15_mech058_lit-0017_completion` |
| `MECH-059` | directional, mixed_evidence | 35 | 19 | 0.704 | `2026-02-15_mech059_lit-0019_completion` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 42 | 37 | 0.937 | `2026-02-15_mech060_lit-0021_completion` |
| `Q-011` | directional | 1 | 5 | 0.333 | `2026-02-15_q011_lit-0026_completion` |
| `Q-017` | directional, source_disagreement | 16 | 13 | 0.897 | `2026-02-15_q017_lit-0032_completion` |

## Conflict Details

### ARC-018
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=1, conflict_ratio=0.333, overall_confidence=0.804
- Recent entries:
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:30:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.75
  - `2026-02-15T15:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-15T16:00:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-033
- Conflict types: directional
- Evidence breakdown: supports=5, weakens=1, conflict_ratio=0.333, overall_confidence=0.799
- Recent entries:
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T22:35:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.74
  - `2026-02-15T15:11:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.74
  - `2026-02-15T16:01:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=24, weakens=24, conflict_ratio=1, overall_confidence=0.721
- Recent entries:
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:38Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:13:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-15T16:02:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
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
- Evidence breakdown: supports=35, weakens=31, conflict_ratio=0.939, overall_confidence=0.704
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:14:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
  - `2026-02-15T16:03:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
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
- Evidence breakdown: supports=35, weakens=19, conflict_ratio=0.704, overall_confidence=0.737
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T14:56:37Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:15:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
  - `2026-02-15T16:04:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
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
- Evidence breakdown: supports=42, weakens=37, conflict_ratio=0.937, overall_confidence=0.695
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T15:16:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
  - `2026-02-15T16:05:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
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
- Evidence breakdown: supports=1, weakens=5, conflict_ratio=0.333, overall_confidence=0.659
- Recent entries:
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T14:10:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.66
  - `2026-02-14T23:00:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
  - `2026-02-15T15:17:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
  - `2026-02-15T16:06:00Z` `literature` `targeted_review_q_011` direction=`weakens` confidence=0.72
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
- Evidence breakdown: supports=16, weakens=13, conflict_ratio=0.897, overall_confidence=0.721
- Recent entries:
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T14:56:37Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:18:00Z` `literature` `targeted_review_mech_063` direction=`supports` confidence=0.79
  - `2026-02-15T16:07:00Z` `literature` `targeted_review_mech_063` direction=`supports` confidence=0.79
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
