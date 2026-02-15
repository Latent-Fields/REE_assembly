# Evidence Conflict Report

Generated: `2026-02-15T17:50:04.047264Z`
Conflict scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |
|---|---|---|---|---|---|---|
| `MECH-056` | directional, source_disagreement | 6 | 22 | 0.429 | `2026-02-15T174850Z_claim-probe-mech-056_seed11_trajectory_first_enabled_toyenv_internal_minimal` | 28 |
| `MECH-058` | directional, source_disagreement | 14 | 14 | 1 | `2026-02-15T174851Z_claim-probe-mech-058_seed11_ema_anchor_on_toyenv_internal_minimal` | 28 |
| `MECH-059` | directional, mixed_evidence | 14 | 1 | 0.133 | `2026-02-15T174852Z_claim-probe-mech-059_seed11_explicit_uncertainty_head_toyenv_internal_minimal` | 27 |
| `MECH-060` | directional, source_disagreement | 14 | 14 | 1 | `2026-02-15T174853Z_claim-probe-mech-060_seed11_pre_post_split_streams_toyenv_internal_minimal` | 28 |
| `Q-017` | directional, source_disagreement | 14 | 15 | 0.966 | `2026-02-15T174855Z_claim-probe-q-017_seed11_full_axis_toyenv_internal_minimal` | 29 |

## Conflict Details

### MECH-056
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=6, weakens=22, conflict_ratio=0.429, overall_confidence=0.769
- Recent entries:
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:01Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:50Z` `experimental` `claim_probe_mech_056` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `ledger_editing` (20)
  - `stop:ledger_edit_detected_count>0` (20)
  - `domination_lock_in` (16)
  - `stop:domination_lock_in_events>0` (16)
  - `explanation_policy_divergence` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-058
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=14, weakens=14, conflict_ratio=1, overall_confidence=0.707
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T17:48:51Z` `experimental` `claim_probe_mech_058` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (12)
  - `mech058:ema_drift_under_shift` (4)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=14, weakens=1, conflict_ratio=0.133, overall_confidence=0.767
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T17:39:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `jepa_uncertainty_channels` direction=`mixed` confidence=0.5
  - `2026-02-15T17:39:01Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-15T17:48:52Z` `experimental` `claim_probe_mech_059` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech059:uncertainty_metric_gaming_detected` (8)
  - `mech059:abstention_reliability_collapse` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=14, weakens=14, conflict_ratio=1, overall_confidence=0.697
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:53Z` `experimental` `claim_probe_mech_060` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (12)
  - `mech060:attribution_reliability_break` (12)
  - `mech060:commitment_reversal_spike` (12)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-017
- Conflict types: directional, source_disagreement
- Evidence breakdown: supports=14, weakens=15, conflict_ratio=0.966, overall_confidence=0.724
- Recent entries:
  - `2026-02-15T17:39:00Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `control_axis_ablation` direction=`supports` confidence=0.75
  - `2026-02-15T17:39:00Z` `experimental` `control_axis_ablation` direction=`weakens` confidence=0.75
  - `2026-02-15T17:48:55Z` `experimental` `claim_probe_q_017` direction=`supports` confidence=0.75
- Recurring failure signatures:
  - `q017:control_axis_stability_drop` (12)
  - `q017:control_axis_entropy_collapse` (12)
  - `q017:control_axis_policy_loss_spike` (8)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.
