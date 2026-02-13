# Evidence Conflict Report

Generated: `2026-02-13T15:36:32.913046Z`

## Conflict Queue

| claim_id | conflict_types | supports | weakens | conflict_ratio | latest |
|---|---|---|---|---|---|
| `MECH-056` | directional | 4 | 2 | 0.667 | `2026-02-13_mech056_extinction_gating` |
| `Q-011` | directional, mixed_evidence | 3 | 2 | 0.8 | `2026-02-13_q011_controllability_passivity` |

## Conflict Details

### MECH-056
- Conflict types: directional
- Evidence breakdown: supports=4, weakens=2, conflict_ratio=0.667, overall_confidence=0.572
- Recent entries:
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-13T09:06:39.857099Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T09:06:39.905363Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-13T10:00:00Z` `literature` `targeted_review_mech_056` direction=`supports` confidence=0.62
  - `2026-02-13T12:20:00Z` `literature` `targeted_review_mech_056` direction=`supports` confidence=0.66
- Recurring failure signatures:
  - `ledger_editing` (1)
  - `explanation_policy_divergence` (1)
  - `stop:ledger_edit_detected_count>0` (1)
  - `stop:explanation_policy_divergence_rate>0.05` (1)
  - `stop:domination_lock_in_events>0` (1)
- Claim-specific framing: Trajectory/commit pressure is primary; perceptual sampling bias is secondary; structural representational bias is tertiary and bounded.
- Suggested resolution actions:
  - Run ablation comparison across channel placements: trajectory-only vs trajectory+perceptual vs trajectory+structural.
  - Run seed sweeps focused on high-uncertainty boundary cases where trajectory constraints alone may be insufficient.
  - If evidence remains split, split MECH-056 into separable subclaims (placement order vs bounded structural channel).
- Adjudication criteria:
  - Primary-channel integrity: successful safety behavior should be explainable mainly by rollout weighting, E3 thresholds, and veto channels.
  - Perceptual-channel constraint: pre-commit sampling bias may alter what is sampled, but must not semantically overwrite sensory latent content.
  - Structural-channel cap: representational drift must be slower and smaller than trajectory/commit effects and reserved for repeated post-commit mismatch.
  - Escalation-order validity: trajectory/commit constraints are attempted first; secondary channels activate only under explicit uncertainty triggers.
- Evidence targets:
  - Emit per-run channel usage counts for trajectory_commit, perceptual_sampling, and structural_consolidation.
  - Emit precommit_semantic_overwrite_events and require zero for adjudication PASS.
  - Emit structural_bias_magnitude and structural_bias_rate with explicit cap checks.
  - Include summary rationale describing which escalation trigger activated each non-primary channel.

### Q-011
- Conflict types: directional, mixed_evidence
- Evidence breakdown: supports=3, weakens=2, conflict_ratio=0.8, overall_confidence=0.564
- Recent entries:
  - `2026-02-13T07:00:00Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-13T09:06:39.951474Z` `experimental` `trajectory_integrity` direction=`supports` confidence=0.75
  - `2026-02-13T09:06:39.999186Z` `experimental` `trajectory_integrity` direction=`weakens` confidence=0.75
  - `2026-02-13T10:05:00Z` `literature` `targeted_review_q_011` direction=`supports` confidence=0.61
  - `2026-02-13T12:21:00Z` `literature` `targeted_review_q_011` direction=`mixed` confidence=0.58
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
