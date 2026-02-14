# Evidence Conflict Report

Generated: `2026-02-14T11:26:03.413442Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `MECH-056` | directional | 1 | 1 | 1 | `2026-02-13T070000Z_dummy-fail` |
| `MECH-058` | directional, source_disagreement | 4 | 7 | 0.727 | `mech_058_oscillatory_shift_anchor_decay_s58012_20260213t231415717627z` |
| `MECH-059` | directional, source_disagreement | 4 | 7 | 0.727 | `mech_059_ambiguity_fog_dispersion_s59012_20260213t231415719741z` |
| `MECH-060` | directional, mixed_evidence | 3 | 7 | 0.6 | `mech_060_memory_patch_cross_talk_s60012_20260213t231415722542z` |
| `Q-011` | directional | 1 | 1 | 1 | `2026-02-13T070000Z_dummy-fail` |

## Conflict Details

### MECH-056
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.372
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
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
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=4, weakens=7, conflict_ratio=0.727, overall_confidence=0.704
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-13T23:14:15.716219Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.716794Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.717321Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.717818Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech058:ema_drift_under_shift` (4)
  - `mech058:latent_cluster_collapse` (4)
  - `mech058:anchor_separation_collapse` (3)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=4, weakens=7, conflict_ratio=0.727, overall_confidence=0.701
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-13T23:14:15.718436Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.718916Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.719429Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.719958Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.75
- Recurring failure signatures:
  - `mech059:calibration_slope_break` (4)
  - `mech059:uncertainty_metric_gaming_detected` (4)
  - `mech059:abstention_reliability_collapse` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=7, conflict_ratio=0.6, overall_confidence=0.665
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.55
  - `2026-02-13T23:14:15.720486Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.721605Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.722141Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-13T23:14:15.722633Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
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
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.372
- Recent entries:
  - `2026-02-13T06:00:00Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
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
