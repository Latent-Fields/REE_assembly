# Promotion / Demotion Recommendations

Generated: `2026-02-13T14:45:02.477288Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `Q-011` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.572, conflict_ratio=0.667, exp_entries=4, lit_entries=2; directions supports=4, weakens=2, mixed=0, unknown=0, conflict_ratio=0.667
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `approved`
- Last logged decision: `approved` by `dgolden` at `2026-02-13T08:43:59.847373Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Directional conflict ratio remains 1.0 with symmetric support/weakening evidence; run adjudication experiments and literature triangulation before promotion.

### Q-011
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.564, conflict_ratio=0.8, exp_entries=4, lit_entries=2; directions supports=3, weakens=2, mixed=1, unknown=0, conflict_ratio=0.8
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `approved`
- Last logged decision: `approved` by `dgolden` at `2026-02-13T12:15:33.457161Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: After demotion to candidate, evidence remains directionally split (supports=2, weakens=2); approve hold-and-resolve before any promotion review.
