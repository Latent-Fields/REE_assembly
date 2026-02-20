# Human Decision Brief: MECH-058

Cycle: `2026-02-19`

## Mechanism / Claim Context

- Claim type: `mechanism hypothesis`
- Current claim status: `candidate`
- Subject: jepa substrate / ema target anchor timescale separation
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-058`
- Upstream dependencies: `ARC-001`, `ARC-002`, `ARC-004`, `ARC-015`, `MECH-057`
- Downstream dependents: `IMPL-023`

## How It Functions In The Architecture

- ## EMA target anchoring preserves E1/E2 substrate separation (MECH-058)
- When JEPA-like substrate training is used for REE E1/E2, a slow target-anchor pathway (for example, EMA-updated target
- encoder) should be treated as a stability requirement rather than an optimization trick.
- Proposed role in REE terms:
- - fast predictor updates support E2-like short-horizon adaptation,

## Decision Lanes

### Promotion / Conflict Lane

- Decision needed: Conflict resolution before promotion
- Recommendation: `hold_candidate_resolve_conflict`
- Decision status: `applied`
- Why this lane is open: overall_conf=0.716, conflict_ratio=0.87, exp_entries=124, lit_entries=9; directions supports=74, weakens=57, mixed=2, unknown=0, conflict_ratio=0.87
- Options:
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)

### Architecture Structure Lane

- Lane recommendation: `escalate_architecture_decision`
- Structure pressure recommendation: `escalate_architecture_decision`
- Conflict ratio: `0.87`; overall confidence: `0.716`
- Trigger signals: external_precedence_pressure, high_conflict_ratio, recurring_failure_signatures
- Recurring failure signatures:
  - `mech058:anchor_separation_collapse` (45)
  - `mech058:ema_drift_under_shift` (21)
  - `mech058:latent_cluster_collapse` (10)
  - `threshold:latent_prediction_error_mean` (5)
  - `threshold:latent_prediction_error_p95` (5)

## Evidence Snapshot

- Conflict report window: supports=40, weakens=26, conflict_ratio=0.788, entries_considered=67.
- Dossier direction mix: supports=74, weakens=57, mixed=2, unknown=0.
- Source counts: experimental=124, literature=9.
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
- Architecture anchor: `docs/architecture/agency_responsibility_flow.md#mech-058`
- Promotion queue: `evidence/experiments/promotion_demotion_recommendations.md`
- Conflict report: `evidence/experiments/conflicts.md`
- Structure dossier: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/structure_review/2026-02-19/MECH-058/DOSSIER.md`
- Structure dossier JSON: `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/structure_review/2026-02-19/MECH-058/dossier.v1.json`
- Decision state: `evidence/decisions/decision_state.v1.json`
- Decision log: `evidence/decisions/decision_log.v1.jsonl`
