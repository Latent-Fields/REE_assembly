# Promotion / Demotion Recommendations

Generated: `2026-03-18T19:52:25.887781Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-016` | `provisional` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-018` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-023` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-025` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-033` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-071` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-072` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-089` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-090` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-091` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-092` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-093` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-095` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-096` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-097` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-098` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-099` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-100` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `Q-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `Q-019` | `open` | Question narrowing review | `narrow_open_question` | `applied` |

## Decision Details

### ARC-007
- Current status: `active`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=1, mixed=0, unknown=0, conflict_ratio=1
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.360735Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Path memory ablation PASS (EXQ-024) is real but v3_pending gate applies; ARC-007 requires proper HippocampalModule (SD-004) before conclusive V3 testing.

### ARC-016
- Current status: `provisional`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=4, mixed=0, unknown=0, conflict_ratio=0.4
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361120Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Precision regime probe FAIL (EXQ-025) is substrate-limited: V3 needs E3-derived dynamic precision and end-to-end commitment→behavior wiring.

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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361124Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Rollout viability mapping FAIL (EXQ-021) is substrate-limited: requires SD-004 HippocampalModule for proper map backbone.

### ARC-023
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361127Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Heartbeat architecture claim, V3-scoped by design. No V2 experiment can test multi-rate loop execution.

### MECH-025
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=2, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361130Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Action-doing mode probe FAIL (EXQ-026): V2 substrate lacks the multi-rate loop and heartbeat architecture required to instantiate distinct action-doing mode.

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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361133Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Kernel chaining FAIL (EXQ-023): V2 E2 is a transition model only; proper kernel chaining requires SD-004 action objects as hippocampal map backbone.

### MECH-071
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361137Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. E2 attribution calibration FAIL (EXQ-027): E2 cannot discriminate agent vs env harm in z_gamma. Requires SD-005 z_self/z_world latent split in V3.

### MECH-072
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361139Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Selective residue attribution FAIL (EXQ-028): directly depends on MECH-071 which failed; both require V3 z_self/z_world split (SD-005).

### MECH-089
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361142Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Theta-gamma nesting for E1→E3 packaging. V3-scoped heartbeat cluster claim; no V2 oscillatory substrate.

### MECH-090
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361144Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Beta gating of E3→action_selection propagation. V3-scoped heartbeat cluster claim.

### MECH-091
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361147Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Salient event phase-reset of E3 heartbeat clock. V3-scoped heartbeat cluster claim.

### MECH-092
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361150Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Quiescent heartbeat → hippocampal SWR-equivalent replay (micro-DMN). V3-scoped heartbeat cluster claim.

### MECH-093
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361152Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. z_beta modulates E3 heartbeat frequency. V3-scoped heartbeat cluster claim.

### MECH-095
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=4, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-17T22:29:07.342936Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: Confirmed hold. New MECH registered 2026-03-17 as part of three-stream reafference architecture (SD-007). V3 substrate (reafference predictor, lateral encoder head) required before experimental evidence can be collected. EXQ-013 through EXQ-016 will provide this substrate.

### MECH-096
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-17T22:29:07.389682Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: Confirmed hold. New MECH registered 2026-03-17 as part of three-stream reafference architecture (SD-007). V3 substrate (reafference predictor, lateral encoder head) required before experimental evidence can be collected. EXQ-013 through EXQ-016 will provide this substrate.

### MECH-097
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-17T22:29:07.427773Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: Confirmed hold. New MECH registered 2026-03-17 as part of three-stream reafference architecture (SD-007). V3 substrate (reafference predictor, lateral encoder head) required before experimental evidence can be collected. EXQ-013 through EXQ-016 will provide this substrate.

### MECH-098
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=4, weakens=4, mixed=1, unknown=0, conflict_ratio=1
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-17T22:29:07.468717Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: Confirmed hold. New MECH registered 2026-03-17 as part of three-stream reafference architecture (SD-007). V3 substrate (reafference predictor, lateral encoder head) required before experimental evidence can be collected. EXQ-013 through EXQ-016 will provide this substrate.

### MECH-099
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=3, weakens=1, mixed=1, unknown=0, conflict_ratio=0.5
- Recommendation: `hold_pending_v3_substrate`
- Options (pros/cons):
  - Wait for V3 substrate implementation (correct path).
  - Mark as legacy/deferred if claim is being superseded.
  - Demote to candidate to acknowledge insufficient evidence.
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-17T22:29:07.504152Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: Confirmed hold. New MECH registered 2026-03-17 as part of three-stream reafference architecture (SD-007). V3 substrate (reafference predictor, lateral encoder head) required before experimental evidence can be collected. EXQ-013 through EXQ-016 will provide this substrate.

### MECH-100
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending or implementation_phase=v3. Current V2 substrate cannot produce valid evidence for this claim. No promotion or demotion should be applied until V3 experiments complete.; directions supports=0, weakens=1, mixed=1, unknown=0, conflict_ratio=0
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361155Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Valence-regime correlation FAIL (EXQ-022): V2 lacks proper affective z_beta channel tied to resource valence. V3 universal expression channel test required.

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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361158Z`
- Last selected option: Narrow the question into testable sub-questions (higher tractability)
- Last rationale: User confirmed: narrow Q-019 into testable V3 sub-questions targeting the BG three-gate vs single-gate distinction. ARC-021 direction (three distinct loops with incommensurable errors) is the working hypothesis; V3 experiment design should isolate each loop independently before testing full three-gate interaction.
