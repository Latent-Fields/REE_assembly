# Promotion / Demotion Recommendations

Generated: `2026-02-15T15:02:46.495933Z`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-056` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-059` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `approved` |
| `Q-011` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.721, conflict_ratio=1, exp_entries=43, lit_entries=5; directions supports=24, weakens=24, mixed=0, unknown=0, conflict_ratio=1
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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.827172Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.865603Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

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
- Last logged decision: `approved` by `dgolden` at `2026-02-14T13:22:46.902458Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Approved in review of v3 conflict decision packet; resolve directional conflict with targeted adjudication before any promotion.

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
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `approved` by `dgolden` at `2026-02-14T19:09:36.006388Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: After demotion to candidate, user approved the updated recommendation to hold at candidate pending conflict-resolution evidence.
