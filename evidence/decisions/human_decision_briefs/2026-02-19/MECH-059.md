# Human Decision Brief: MECH-059

Cycle: `2026-02-19`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: precision / confidence channel separate from prediction error
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-059`
- Upstream dependencies: `ARC-005`, `ARC-004`, `ARC-015`, `MECH-054`, `MECH-057`
- Downstream dependents: `IMPL-023`, `Q-013`, `Q-014`

## How It Functions In The Architecture

- ## Confidence channel must remain distinct from residual error (MECH-059)
- Latent prediction residual and the confidence channel (uncertainty-derived precision) should remain distinct streams.
- - residual answers: *how wrong was the prediction*,
- - confidence channel answers: *how strongly should this error be trusted for control and learning*.
- - uncertainty/dispersion remains an explicit input to confidence-channel computation.

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Conflict resolution before promotion
- Recommendation: `hold_candidate_resolve_conflict`
- Decision status: `applied`
- Why this lane is open: overall_conf=0.761, conflict_ratio=0.605, exp_entries=132, lit_entries=6; directions supports=60, weakens=26, mixed=52, unknown=0, conflict_ratio=0.605
- Options:
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)

## Evidence Snapshot

- Conflict report window: supports=26, weakens=7, conflict_ratio=0.424, entries_considered=71.
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
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-059`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Conflict report: `evidence/experiments/conflicts.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
