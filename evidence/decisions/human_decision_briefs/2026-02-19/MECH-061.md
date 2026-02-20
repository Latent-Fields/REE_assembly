# Human Decision Brief: MECH-061

Cycle: `2026-02-19`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: commitment / boundary token error reclassification
- Architecture anchor: `docs/architecture/e3.md#mech-061`
- Upstream dependencies: `ARC-003`, `ARC-015`, `INV-012`, `MECH-060`
- Downstream dependents: `IMPL-023`, `IMPL-025`, `INV-021`, `MECH-062`, `MECH-066`, `MECH-067`, `Q-015`

## How It Functions In The Architecture

- ## Commit-Boundary Token and Error Reclassification (MECH-061)
- Claim Type: mechanism_hypothesis
- Scope: Explicit boundary token that separates pre-commit and post-commit error classes
- Depends On: ARC-003, MECH-060, INV-012, ARC-015
- Status: candidate

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Conflict resolution before promotion
- Recommendation: `hold_candidate_resolve_conflict`
- Decision status: `applied`
- Why this lane is open: overall_conf=0.61, conflict_ratio=0.8, exp_entries=8, lit_entries=2; directions supports=6, weakens=4, mixed=0, unknown=0, conflict_ratio=0.8
- Options:
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)

## Evidence Snapshot

- Conflict report window: supports=4, weakens=4, conflict_ratio=1, entries_considered=8.
- Latest decision state: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, timestamp=`2026-02-15T20:58:38.602475Z`.
- Recent decision history:
  - 2026-02-15T18:46:42.773429Z: status=`applied`, recommendation=`retain_ree`, decision_needed=Model adjudication outcome selection
  - 2026-02-15T20:49:23.356752Z: status=`approved`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion
  - 2026-02-15T20:58:38.602475Z: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion

## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Conflict resolution before promotion
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `docs/architecture/e3.md#mech-061`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Conflict report: `evidence/experiments/conflicts.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
