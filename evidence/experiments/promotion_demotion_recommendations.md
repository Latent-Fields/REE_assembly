# Promotion / Demotion Recommendations

Generated: `2026-02-15T15:19:20.479566Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-059` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `Q-011` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `approved` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.724, conflict_ratio=0.941, exp_entries=43, lit_entries=9; directions supports=27, weakens=24, mixed=1, unknown=0, conflict_ratio=0.941
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
- Last logged decision: `approved` by `codex` at `2026-02-15T15:10:33.718527Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Conflict remains high; maintain candidate status while conflict-adjudication experiments continue.

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.704, conflict_ratio=0.939, exp_entries=62, lit_entries=5; directions supports=35, weakens=31, mixed=1, unknown=0, conflict_ratio=0.939
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
- Last logged decision: `approved` by `codex` at `2026-02-15T15:10:33.757919Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Directional conflict remains material; keep candidate and continue adjudication protocol.

### MECH-059
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.737, conflict_ratio=0.704, exp_entries=62, lit_entries=6; directions supports=35, weakens=19, mixed=14, unknown=0, conflict_ratio=0.704
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
- Last logged decision: `approved` by `codex` at `2026-02-15T15:10:33.793159Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Mixed evidence remains unresolved; retain candidate status and continue conflict resolution.

### MECH-060
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.695, conflict_ratio=0.937, exp_entries=73, lit_entries=9; directions supports=42, weakens=37, mixed=3, unknown=0, conflict_ratio=0.937
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
- Last logged decision: `approved` by `codex` at `2026-02-15T15:10:33.830375Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: High conflict ratio persists; hold promotion and continue paired adjudication runs.

### Q-011
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.659, conflict_ratio=0.333, exp_entries=2, lit_entries=4; directions supports=1, weakens=5, mixed=0, unknown=0, conflict_ratio=0.333
- Recommendation: `promote_to_provisional`
- Options (pros/cons):
  - Promote now (faster convergence, risk premature lock-in)
  - Hold until one additional confirming run (better robustness, slower progress)
  - Hold and request targeted literature triangulation (better external grounding, extra delay)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `approved`
- Last logged decision: `approved` by `codex` at `2026-02-15T15:10:33.865089Z`
- Last selected option: Promote now (faster convergence, risk premature lock-in)
- Last rationale: Current evidence meets provisional promotion recommendation; proceed while monitoring conflict drift.
