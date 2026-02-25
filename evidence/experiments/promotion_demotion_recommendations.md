# Promotion / Demotion Recommendations

Generated: `2026-02-25T20:08:01.120819Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

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
| `Q-012` | `active` | Demotion review: active -> candidate | `demote_to_candidate` | `pending_user` |

## Decision Details

### MECH-056
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.766, conflict_ratio=0.435, exp_entries=120, lit_entries=1; directions supports=25, weakens=90, mixed=6, unknown=0, conflict_ratio=0.435
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
- Why this decision is needed: overall_conf=0.525, conflict_ratio=1, exp_entries=12, lit_entries=0; directions supports=6, weakens=6, mixed=0, unknown=0, conflict_ratio=1
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
- Last logged decision: `applied` by `user` at `2026-02-25T16:39:07.535473Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied conflict-lane hold after architecture adjudication (hybridize); keep candidate while reducing uncertainty with targeted probes.

### MECH-058
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.725, conflict_ratio=0.816, exp_entries=94, lit_entries=5; directions supports=58, weakens=40, mixed=1, unknown=0, conflict_ratio=0.816
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
- Last logged decision: `applied` by `user` at `2026-02-25T16:39:07.573674Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied conflict-lane hold after architecture adjudication (hybridize); maintain candidate status while anchor-separation conflict signatures are worked down.

### MECH-059
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.743, conflict_ratio=0.415, exp_entries=102, lit_entries=1; directions supports=42, weakens=11, mixed=50, unknown=0, conflict_ratio=0.415
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
- Why this decision is needed: overall_conf=0.733, conflict_ratio=0.8, exp_entries=96, lit_entries=5; directions supports=60, weakens=40, mixed=1, unknown=0, conflict_ratio=0.8
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
- Last logged decision: `applied` by `user` at `2026-02-25T16:35:40.759224Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Applied conflict-lane hold after architecture adjudication reaffirmation; maintain candidate status while continuing targeted boundary-condition probes.

### MECH-061
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.615, conflict_ratio=0.8, exp_entries=10, lit_entries=0; directions supports=6, weakens=4, mixed=0, unknown=0, conflict_ratio=0.8
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
- Last logged decision: `applied` by `user` at `2026-02-25T16:56:17.938917Z`
- Last selected option: hold_candidate_resolve_conflict
- Last rationale: Refreshed after corrected thought-date intake; keep MECH-061 candidate and continue targeted conflict-resolution probes while preserving commit-token boundary semantics.

### Q-012
- Current status: `active`
- Decision needed: Demotion review: active -> candidate
- Why this decision is needed: overall_conf=0.503, conflict_ratio=1, exp_entries=8, lit_entries=0; directions supports=4, weakens=4, mixed=0, unknown=0, conflict_ratio=1
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
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.634.
