# Promotion / Demotion Recommendations

Generated: `2026-02-13T08:31:03.449393Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.375, conflict_ratio=1, exp_entries=2, lit_entries=0; directions supports=1, weakens=1, mixed=0, unknown=0, conflict_ratio=1
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
