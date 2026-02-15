# Evidence Conflict Report

Generated: `2026-02-15T15:37:22.224857Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 5 | 1 | 0.333 | `2026-02-15_arc018_lit-0005_completion` |
| `MECH-033` | directional | 5 | 1 | 0.333 | `2026-02-15_mech033_lit-0008_completion` |
| `MECH-056` | directional, source_disagreement, mixed_evidence | 28 | 30 | 0.966 | `2026-02-15_mech056_lit-0014_completion` |
| `MECH-058` | directional, source_disagreement, mixed_evidence | 38 | 35 | 0.959 | `2026-02-15_mech058_lit-0017_completion` |
| `MECH-059` | directional, mixed_evidence | 38 | 20 | 0.69 | `2026-02-15_mech059_lit-0019_completion` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 45 | 41 | 0.953 | `2026-02-15_mech060_lit-0021_completion` |
| `Q-011` | directional | 1 | 5 | 0.333 | `2026-02-15_q011_lit-0026_completion` |
| `Q-017` | directional, source_disagreement | 19 | 17 | 0.944 | `2026-02-15_q017_lit-0032_completion` |

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
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=28, weakens=30, conflict_ratio=0.966, overall_confidence=0.744
- Recent entries:
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T16:02:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Recurring failure signatures:
  - `stop:ledger_edit_detected_count>0` (31)
  - `ledger_editing` (26)
  - `stop:domination_lock_in_events>0` (26)
  - `stop:explanation_policy_divergence_rate>0.05` (21)
  - `domination_lock_in` (20)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=38, weakens=35, conflict_ratio=0.959, overall_confidence=0.707
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T16:03:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (24)
  - `mech058:ema_drift_under_shift` (16)
  - `mech058:latent_cluster_collapse` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_prediction_error_p95` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=38, weakens=20, conflict_ratio=0.69, overall_confidence=0.741
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T15:36:21Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T15:36:22Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T16:04:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (22)
  - `mech059:abstention_reliability_collapse` (14)
  - `mech059:calibration_slope_break` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_uncertainty_calibration_error` (5)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=45, weakens=41, conflict_ratio=0.953, overall_confidence=0.698
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T16:05:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (31)
  - `mech060:attribution_reliability_break` (29)
  - `mech060:commitment_reversal_spike` (17)
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
- Evidence breakdown: supports=19, weakens=17, conflict_ratio=0.944, overall_confidence=0.725
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T16:07:00Z` `literature` `targeted_review_mech_063` direction=`supports` confidence=0.79
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (15)
  - `q017:control_axis_entropy_collapse` (15)
  - `q017:control_axis_policy_loss_spike` (10)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
