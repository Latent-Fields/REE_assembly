# Evidence Conflict Report

Generated: `2026-02-13T22:02:12.974027Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `MECH-056` | directional | 1 | 1 | 1 | `2026-02-13T070000Z_dummy-fail` |
| `MECH-058` | directional | 4 | 3 | 0.857 | `2026-02-13T224000Z_jepa-anchor-ablation_seed47_ema_anchor_on` |
| `MECH-059` | directional | 4 | 3 | 0.857 | `2026-02-13T224000Z_jepa-uncertainty-channels_seed47_explicit_uncertainty_head` |
| `MECH-060` | directional, mixed_evidence | 3 | 3 | 1 | `2026-02-13T224000Z_commit-dual-error-channels_seed47_single_error_stream` |
| `Q-011` | directional | 1 | 1 | 1 | `2026-02-13T070000Z_dummy-fail` |

## Conflict Details

### MECH-056
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.374
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
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=3, conflict_ratio=0.857, overall_confidence=0.566
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `jepa_anchor_ablation` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-059
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=3, conflict_ratio=0.857, overall_confidence=0.564
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `jepa_uncertainty_channels` direction=`supports` confidence=0.75
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### MECH-060
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=3, conflict_ratio=1, overall_confidence=0.527
- Recent entries:
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.55
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`supports` confidence=0.75
  - `2026-02-13T22:40:00Z` `experimental` `commit_dual_error_channels` direction=`weakens` confidence=0.55
- Recurring failure signatures:
  - `lit_gap:commitment_semantics_not_explicit` (1)
- Suggested resolution actions:
  - Run one targeted adjudication experiment with narrower stop criteria.
  - Add one replication run with seed sweep to reduce variance ambiguity.
  - If disagreement persists, split claim scope into separable subclaims.

### Q-011
- Conflict types: directional
- Evidence breakdown: supports=1, weakens=1, conflict_ratio=1, overall_confidence=0.374
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
