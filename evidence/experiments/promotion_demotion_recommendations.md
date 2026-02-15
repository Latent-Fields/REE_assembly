# Promotion / Demotion Recommendations

Generated: `2026-02-15T15:37:22.224857Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-059` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `Q-011` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `approved` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.744, conflict_ratio=0.966, exp_entries=50, lit_entries=9; directions supports=28, weakens=30, mixed=1, unknown=0, conflict_ratio=0.966
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
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `codex` at `2026-02-15T15:31:31.190642Z`
- Last selected option: hybridize
- Last rationale: Keep trajectory-first core but add explicit pre-commit rehearsal guardrails and commit-boundary mutation constraints.

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.707, conflict_ratio=0.959, exp_entries=69, lit_entries=5; directions supports=38, weakens=35, mixed=1, unknown=0, conflict_ratio=0.959
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
- Why this decision is needed: overall_conf=0.741, conflict_ratio=0.69, exp_entries=69, lit_entries=6; directions supports=38, weakens=20, mixed=17, unknown=0, conflict_ratio=0.69
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
- Why this decision is needed: overall_conf=0.698, conflict_ratio=0.953, exp_entries=80, lit_entries=9; directions supports=45, weakens=41, mixed=3, unknown=0, conflict_ratio=0.953
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
