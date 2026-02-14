# Evidence Conflict Report

Generated: `2026-02-14T13:28:15.471144Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `ARC-018` | directional | 2 | 1 | 0.667 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-033` | directional | 2 | 1 | 0.667 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-056` | directional | 3 | 1 | 0.5 | `2026-02-14_v3hippo_prioritized_replay_planning_natneuro2018` |
| `MECH-058` | directional, source_disagreement, mixed_evidence | 4 | 7 | 0.727 | `2026-02-14_v3jepa_ijepa_control_plane_gap` |
| `MECH-059` | directional, source_disagreement, mixed_evidence | 4 | 7 | 0.727 | `2026-02-14_v3jepa_vjvcr_uncertainty_stream_limits` |
| `MECH-060` | directional, source_disagreement, mixed_evidence | 6 | 7 | 0.923 | `2026-02-14_v3jepa_vjvcr_uncertainty_stream_limits` |
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
- Evidence breakdown: supports=3, weakens=1, conflict_ratio=0.5, overall_confidence=0.576
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-14T20:10:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.79
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
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

### MECH-058
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=4, weakens=7, conflict_ratio=0.727, overall_confidence=0.729
- Recent entries:
  - `2026-02-13T23:14:15.716219Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.716794Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.717321Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.717818Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
- Recurring failure signatures:
  - `mech058:ema_drift_under_shift` (4)
  - `mech058:latent_cluster_collapse` (4)
  - `mech058:anchor_separation_collapse` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=4, weakens=7, conflict_ratio=0.727, overall_confidence=0.755
- Recent entries:
  - `2026-02-13T23:14:15.718916Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.719429Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.719958Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T21:10:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.76
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
- Recurring failure signatures:
  - `mech059:calibration_slope_break` (4)
  - `mech059:uncertainty_metric_gaming_detected` (4)
  - `mech059:abstention_reliability_collapse` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement, mixed_evidence
- Evidence breakdown: supports=6, weakens=7, conflict_ratio=0.923, overall_confidence=0.777
- Recent entries:
  - `2026-02-13T23:14:15.722633Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-14T20:25:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
  - `2026-02-14T20:40:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
  - `2026-02-14T20:55:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.74
  - `2026-02-14T21:25:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`mixed` confidence=0.69
- Recurring failure signatures:
  - `mech060:precommit_channel_contamination` (4)
  - `mech060:postcommit_channel_contamination` (4)
  - `mech060:attribution_reliability_break` (2)
  - `lit_gap:commitment_semantics_not_explicit` (1)
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
