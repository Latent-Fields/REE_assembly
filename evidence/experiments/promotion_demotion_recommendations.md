# Promotion / Demotion Recommendations

Generated: `2026-02-16T15:09:35.081467Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-057` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-059` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-061` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.749, conflict_ratio=0.892, exp_entries=75, lit_entries=9; directions supports=37, weakens=46, mixed=1, unknown=0, conflict_ratio=0.892
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.

### MECH-057
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.711, conflict_ratio=0.769, exp_entries=9, lit_entries=7; directions supports=8, weakens=5, mixed=3, unknown=0, conflict_ratio=0.769
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.709, conflict_ratio=0.891, exp_entries=94, lit_entries=9; directions supports=56, weakens=45, mixed=2, unknown=0, conflict_ratio=0.891
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.

### MECH-059
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.765, conflict_ratio=0.588, exp_entries=102, lit_entries=6; directions supports=48, weakens=20, mixed=40, unknown=0, conflict_ratio=0.588
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.

### MECH-060
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.698, conflict_ratio=0.895, exp_entries=105, lit_entries=13; directions supports=63, weakens=51, mixed=4, unknown=0, conflict_ratio=0.895
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.

### MECH-061
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.615, conflict_ratio=0.8, exp_entries=8, lit_entries=2; directions supports=6, weakens=4, mixed=0, unknown=0, conflict_ratio=0.8
- Recommendation: `hold_candidate_resolve_conflict`
- Options (pros/cons):
  - Keep candidate and run conflict-resolution experiments (most balanced)
  - Promote despite conflict (speed, high lock-in risk)
  - Demote to legacy (conservative, may discard useful partial mechanism)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-02-15T20:58:38.602475Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied approved conflict-hold decision to keep queue actionable without pending manual status.
