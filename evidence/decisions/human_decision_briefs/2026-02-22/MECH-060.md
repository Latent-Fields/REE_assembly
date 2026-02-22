# Human Decision Brief: MECH-060

Cycle: `2026-02-22`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: commitment / dual error channels pre post commit
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`
- Upstream dependencies: `ARC-003`, `ARC-005`, `ARC-015`, `INV-012`, `MECH-057`
- Downstream dependents: `IMPL-023`, `INV-019`, `MECH-056`, `MECH-061`, `MECH-066`, `MECH-067`

## How It Functions In The Architecture

- ## Dual error channels map to pre-commit and post-commit learning (MECH-060)
- REE should maintain two explicit error channels around E3 commitment:
- - pre-commit simulation error: from uncommitted rollouts/counterfactuals, used for gating/search,
- - post-commit realized error: from executed committed trajectories, used for responsibility attribution and durable
- model update.

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Conflict resolution before promotion
- Recommendation: `hold_candidate_resolve_conflict`
- Decision status: `applied`
- Why this lane is open: overall_conf=0.709, conflict_ratio=0.875, exp_entries=167, lit_entries=13; directions supports=99, weakens=77, mixed=4, unknown=0, conflict_ratio=0.875
- Options:
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)

### Architecture Structure Lane

- Lane recommendation: `mandatory_decision_checkpoint`
- Structure pressure recommendation: `mandatory_decision_checkpoint`
- Conflict ratio: `0.875`; overall confidence: `0.709`
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Recurring failure signatures:
  - `mech060:postcommit_channel_contamination` (64)
  - `mech060:attribution_reliability_break` (62)
  - `mech060:commitment_reversal_spike` (50)
  - `mech060:precommit_channel_contamination` (10)
  - `threshold:pre_commit_error_signal_to_noise` (7)

## Evidence Snapshot

- Conflict report window: supports=58, weakens=40, conflict_ratio=0.816, entries_considered=99.
- Dossier direction mix: supports=99, weakens=77, mixed=4, unknown=0.
- Source counts: experimental=167, literature=13.
- Latest decision state: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, timestamp=`2026-02-15T20:58:38.602475Z`.
- Recent decision history:
  - 2026-02-15T18:46:42.773429Z: status=`applied`, recommendation=`hybridize`, decision_needed=Model adjudication outcome selection
  - 2026-02-15T20:49:23.356752Z: status=`approved`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion
  - 2026-02-15T20:58:38.602475Z: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion

## Human Decision Prompt

- Architecture adjudication outcome to select now: `retain_ree`, `hybridize`, `adopt_jepa_structure`, `retire_ree_claim`
- Promotion/conflict lane decision to resolve now: Conflict resolution before promotion
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-060`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Conflict report: `evidence/experiments/conflicts.md`
- Structure dossier: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/structure_review/2026-02-22/MECH-060/DOSSIER.md`
- Structure dossier JSON: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/structure_review/2026-02-22/MECH-060/dossier.v1.json`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
