# Promotion / Demotion Recommendations

Generated: `2026-02-27T07:28:53.918141Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `MECH-040` | `provisional` | Demotion review: provisional -> candidate | `demote_to_candidate` | `pending_user` |
| `MECH-046` | `provisional` | Demotion review: provisional -> candidate | `demote_to_candidate` | `pending_user` |
| `MECH-057` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-058` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-060` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `Q-012` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `Q-015` | `active` | Demotion review: active -> candidate | `demote_to_candidate` | `pending_user` |

## Decision Details

### MECH-040
- Current status: `provisional`
- Decision needed: Demotion review: provisional -> candidate
- Why this decision is needed: overall_conf=0.55, conflict_ratio=0.889, exp_entries=9, lit_entries=0; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
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
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.607.

### MECH-046
- Current status: `provisional`
- Decision needed: Demotion review: provisional -> candidate
- Why this decision is needed: overall_conf=0.55, conflict_ratio=0.889, exp_entries=9, lit_entries=0; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
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
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.597.

### MECH-057
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.588, conflict_ratio=0.857, exp_entries=14, lit_entries=0; directions supports=6, weakens=8, mixed=0, unknown=0, conflict_ratio=0.857
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
- Why this decision is needed: overall_conf=0.732, conflict_ratio=0.808, exp_entries=96, lit_entries=5; directions supports=59, weakens=40, mixed=2, unknown=0, conflict_ratio=0.808
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

### MECH-060
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.732, conflict_ratio=0.8, exp_entries=96, lit_entries=5; directions supports=60, weakens=40, mixed=1, unknown=0, conflict_ratio=0.8
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

### Q-012
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.5, conflict_ratio=1, exp_entries=8, lit_entries=0; directions supports=4, weakens=4, mixed=0, unknown=0, conflict_ratio=1
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
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.634.

### Q-015
- Current status: `active`
- Decision needed: Demotion review: active -> candidate
- Why this decision is needed: overall_conf=0.55, conflict_ratio=0.889, exp_entries=9, lit_entries=0; directions supports=5, weakens=4, mixed=0, unknown=0, conflict_ratio=0.889
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
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.667; overall_confidence=0.586.
