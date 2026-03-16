# Promotion / Demotion Recommendations

Generated: `2026-03-16T06:29:04.910148Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `ARC-016` | `provisional` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `ARC-018` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `MECH-025` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `MECH-033` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `Q-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `Q-019` | `open` | Question narrowing review | `narrow_open_question` | `pending_user` |

## Decision Details

### ARC-007
- Current status: `active`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: hybridize
- Last rationale: Applied anti-lock-in dispatch recommendation: hybridize; basis=high_conflict; conflict_ratio=0.857; overall_confidence=0.58.

### ARC-016
- Current status: `provisional`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### ARC-018
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.6; overall_confidence=0.639.

### MECH-025
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### MECH-033
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-02-15T18:46:42.773429Z`
- Last selected option: retain_ree
- Last rationale: Applied anti-lock-in dispatch recommendation: retain_ree; basis=conflict_below_hybrid_threshold; conflict_ratio=0.6; overall_confidence=0.637.

### Q-007
- Current status: `active`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### Q-019
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.87, conflict_ratio=0, exp_entries=0, lit_entries=6; directions supports=5, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Evidence quality note: Open architectural question arising 2026-02-27. Two competing models: (A) Single-gate: BG gate one action endpoint, evaluating three criteria simultaneously (sensorium readiness, thought/trajectory readiness, motor commitment). (B) Three-gate: BG implement three anatomically distinct gating loops — (1) Sensorium loop: limbic/beta-associated, gates what the system attends to — selecting not only fr…
- Recommendation: `narrow_open_question`
- Options (pros/cons):
  - Narrow the question into testable sub-questions (higher tractability)
  - Keep broad question (flexibility, weaker experiment planning)
  - Convert one branch into candidate mechanism (progress, possible overcommitment)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`
