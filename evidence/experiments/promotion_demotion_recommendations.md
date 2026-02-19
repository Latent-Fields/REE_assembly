# Promotion / Demotion Recommendations

Generated: `2026-02-19T17:53:23.758124Z`

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
| `MECH-062` | `provisional` | Promotion review: provisional -> stable | `promote_to_stable` | `approved` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.78, conflict_ratio=0.726, exp_entries=105, lit_entries=9; directions supports=41, weakens=72, mixed=1, unknown=0, conflict_ratio=0.726
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
- Why this decision is needed: overall_conf=0.707, conflict_ratio=0.769, exp_entries=9, lit_entries=7; directions supports=8, weakens=5, mixed=3, unknown=0, conflict_ratio=0.769
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
- Why this decision is needed: overall_conf=0.716, conflict_ratio=0.87, exp_entries=124, lit_entries=9; directions supports=74, weakens=57, mixed=2, unknown=0, conflict_ratio=0.87
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
- Why this decision is needed: overall_conf=0.761, conflict_ratio=0.605, exp_entries=132, lit_entries=6; directions supports=60, weakens=26, mixed=52, unknown=0, conflict_ratio=0.605
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
- Why this decision is needed: overall_conf=0.705, conflict_ratio=0.875, exp_entries=135, lit_entries=13; directions supports=81, weakens=63, mixed=4, unknown=0, conflict_ratio=0.875
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
- Why this decision is needed: overall_conf=0.61, conflict_ratio=0.8, exp_entries=8, lit_entries=2; directions supports=6, weakens=4, mixed=0, unknown=0, conflict_ratio=0.8
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

### MECH-062
- Current status: `provisional`
- Decision needed: Promotion review: provisional -> stable
- Why this decision is needed: overall_conf=0.899, conflict_ratio=0, exp_entries=24, lit_entries=2; directions supports=20, weakens=0, mixed=6, unknown=0, conflict_ratio=0
- Recommendation: `promote_to_stable`
- Options (pros/cons):
  - Promote now (clear canonical status, risk under-tested edge cases)
  - Hold pending stress-test replication (better stress confidence, slower closure)
  - Split claim scope before promotion (clearer boundaries, added doc work)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `approved`
- Last logged decision: `approved` by `user` at `2026-02-19T17:53:18.007513Z`
- Last selected option: Promote now (clear canonical status, risk under-tested edge cases)
- Last rationale: Approved promotion recommendation to stable based on high confidence and zero directional conflict.
