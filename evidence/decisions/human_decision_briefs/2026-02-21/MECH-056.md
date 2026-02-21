# Human Decision Brief: MECH-056

Cycle: `2026-02-21`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: residue / trajectory first placement
- Architecture anchor: `docs/architecture/residue_geometry.md#mech-056`
- Upstream dependencies: `ARC-013`, `ARC-018`, `ARC-003`, `ARC-004`, `MECH-034`, `MECH-060`, `MECH-062`

## How It Functions In The Architecture

- ## Trajectory-First Residue Placement (MECH-056)
- Claim Type: mechanism_hypothesis
- Scope: Prefer trajectory-space gating before representational distortion
- Depends On: ARC-013, ARC-018, ARC-003, ARC-004, MECH-034
- Status: candidate

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Conflict resolution before promotion
- Recommendation: `hold_candidate_resolve_conflict`
- Decision status: `applied`
- Why this lane is open: overall_conf=0.788, conflict_ratio=0.688, exp_entries=117, lit_entries=9; directions supports=43, weakens=82, mixed=1, unknown=0, conflict_ratio=0.688
- Options:
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)

## Evidence Snapshot

- Conflict report window: supports=17, weakens=58, conflict_ratio=0.453, entries_considered=75.
- Latest decision state: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, timestamp=`2026-02-15T20:58:38.602475Z`.
- Recent decision history:
  - 2026-02-15T18:46:42.773429Z: status=`applied`, recommendation=`hybridize`, decision_needed=Model adjudication outcome selection
  - 2026-02-15T20:49:23.356752Z: status=`approved`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion
  - 2026-02-15T20:58:38.602475Z: status=`applied`, recommendation=`hold_candidate_resolve_conflict`, decision_needed=Conflict resolution before promotion

## Human Decision Prompt

- Promotion/conflict lane decision to resolve now: Conflict resolution before promotion
- Interpret metric semantics using: `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`.

## Source Paths

- Claim registry: `docs/claims/claims.yaml`
- Architecture anchor: `docs/architecture/residue_geometry.md#mech-056`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Conflict report: `evidence/experiments/conflicts.md`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
