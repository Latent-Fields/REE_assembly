# Evidence Conflict Report

Generated: `2026-02-15T15:52:12.882031Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `MECH-056` | directional, source_disagreement | 2 | 6 | 0.5 | `2026-02-15_mech056_lit-0014_completion` | 8 |
| `MECH-058` | directional, source_disagreement | 4 | 4 | 1 | `2026-02-15_mech058_lit-0017_completion` | 8 |
| `MECH-059` | directional, mixed_evidence | 4 | 1 | 0.4 | `2026-02-15_mech059_lit-0019_completion` | 8 |
| `MECH-060` | directional, source_disagreement | 4 | 4 | 1 | `2026-02-15_mech060_lit-0021_completion` | 8 |
| `Q-017` | directional, source_disagreement | 4 | 4 | 1 | `2026-02-15_q017_lit-0032_completion` | 8 |

## Conflict Details

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=2, weakens=6, conflict_ratio=0.5, overall_confidence=0.744
- Recent entries:
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T16:02:00Z` `literature` `targeted_review_v3_hippocampal_rollout` direction=`supports` confidence=0.73
- Recurring failure signatures:
  - `ledger_editing` (5)
  - `stop:ledger_edit_detected_count>0` (5)
  - `domination_lock_in` (4)
  - `stop:domination_lock_in_events>0` (4)
  - `explanation_policy_divergence` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.707
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T16:03:00Z` `literature` `targeted_review_mech_058` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (3)
  - `mech058:ema_drift_under_shift` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=4, weakens=1, conflict_ratio=0.4, overall_confidence=0.741
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T15:36:21Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T15:36:22Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:22Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T16:04:00Z` `literature` `targeted_review_v3_jepa_mapping_limits` direction=`supports` confidence=0.67
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (2)
  - `mech059:abstention_reliability_collapse` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.698
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T16:05:00Z` `literature` `targeted_review_v3_prefrontal_control` direction=`supports` confidence=0.78
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (3)
  - `mech060:attribution_reliability_break` (3)
  - `mech060:commitment_reversal_spike` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-017
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=4, weakens=4, conflict_ratio=1, overall_confidence=0.725
- Recent entries:
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T15:36:21Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T16:07:00Z` `literature` `targeted_review_mech_063` direction=`supports` confidence=0.79
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (3)
  - `q017:control_axis_entropy_collapse` (3)
  - `q017:control_axis_policy_loss_spike` (2)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
