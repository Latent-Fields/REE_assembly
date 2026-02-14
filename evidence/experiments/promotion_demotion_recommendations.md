# Promotion / Demotion Recommendations

Generated: `2026-02-14T16:17:14.812568Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-059` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `Q-011` | `active` | Demotion review: active -> candidate | `demote_to_candidate` | `pending_user` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.665, conflict_ratio=0.667, exp_entries=7, lit_entries=2; directions supports=6, weakens=3, mixed=0, unknown=0, conflict_ratio=0.667
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

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.666, conflict_ratio=0.9, exp_entries=19, lit_entries=2; directions supports=9, weakens=11, mixed=1, unknown=0, conflict_ratio=0.9
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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.827172Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

### MECH-059
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.703, conflict_ratio=0.9, exp_entries=19, lit_entries=3; directions supports=9, weakens=11, mixed=2, unknown=0, conflict_ratio=0.9
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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.865603Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

### MECH-060
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.725, conflict_ratio=1, exp_entries=19, lit_entries=5; directions supports=11, weakens=11, mixed=2, unknown=0, conflict_ratio=1
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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.902458Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

### Q-011
- Current status: `active`
- Decision needed: Demotion review: active -> candidate
- Why this decision is needed: overall_conf=0.475, conflict_ratio=0.667, exp_entries=2, lit_entries=1; directions supports=1, weakens=2, mixed=0, unknown=0, conflict_ratio=0.667
- Recommendation: `demote_to_candidate`
- Options (pros/cons):
  - Demote now (reduces false certainty, destabilizes current roadmap references)
  - Hold and run conflict-resolution suite first (more data, temporary ambiguity)
  - Split into subclaims (isolates conflict, increases registry complexity)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `approved` by `dgolden` at `2026-02-13T08:45:40.164281Z`
- Last selected option: Keep open and run conflict-resolution experiments plus literature triangulation
- Last rationale: Directional conflict ratio remains 1.0 with balanced support/weakening evidence; resolve with adjudication runs and targeted literature before narrowing the question.
