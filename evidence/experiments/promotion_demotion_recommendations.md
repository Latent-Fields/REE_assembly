# Promotion / Demotion Recommendations

Generated: `2026-03-20T22:40:34.047938Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-023` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-024` | `provisional` | Demotion review: provisional -> candidate | `demote_to_candidate` | `applied` |
| `ARC-027` | `provisional` | Promotion review: provisional -> stable | `promote_to_stable` | `pending_user` |
| `MECH-025` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-057b` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |
| `MECH-072` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |
| `MECH-090` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `MECH-091` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-092` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-093` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-096` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-097` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-098` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-099` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-101` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |
| `Q-007` | `active` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `Q-019` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `SD-008` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `SD-010` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |

## Decision Details

### ARC-007
- Current status: `active`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=3, weakens=3, mixed=0, unknown=0, conflict_ratio=1
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

### ARC-023
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### ARC-024
- Current status: `provisional`
- Decision needed: Demotion review: provisional -> candidate
- Why this decision is needed: overall_conf=0.545, conflict_ratio=0.923, exp_entries=25, lit_entries=0; directions supports=6, weakens=7, mixed=12, unknown=0, conflict_ratio=0.923
- Evidence quality note: EXQ-028 PASS (2026-03-18): Gradient dominance confirmed with random policy on CausalGridWorldV2. mean_dz_world_hazard_approach >> mean_dz_world_none. World generates observable signals before contact events. Direct confirmation that the simulated world must and does produce proxy-gradient fields. EXQ-029 PASS (2026-03-18): E3.harm_eval learned graded danger model on gradient world. none=0.373, app…
- Recommendation: `demote_to_candidate`
- Options (pros/cons):
  - Demote now (reduces false certainty, destabilizes current roadmap references)
  - Hold and run conflict-resolution suite first (more data, temporary ambiguity)
  - Split into subclaims (isolates conflict, increases registry complexity)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-19T20:35:00Z`
- Last selected option: Hold at provisional — split resolved conflict scope
- Last rationale: Governance 2026-03-19: ARC-024 split. Claim was spanning two layers — philosophical/foundational (death/love as asymptotic limits, derived from INV-025-029) and behavioral/capability-expansion prediction (love expands under intelligence). The demotion trigger was correct insofar as the behavioral layer needs more work, but the philosophical layer is architecturally well-supported by EXQ-028/029. Resolved by: splitting behavioral prediction to ARC-026 (candidate, v3); retaining ARC-024 at provisional (not demoting to candidate). Conflict experiment pool reflects ARC-026 scope. No demotion applied.

### ARC-027
- Current status: `provisional`
- Decision needed: Promotion review: provisional -> stable
- Why this decision is needed: overall_conf=0.91, conflict_ratio=0, exp_entries=5, lit_entries=3; directions supports=4, weakens=0, mixed=4, unknown=0, conflict_ratio=0
- Evidence quality note: EXQ-027b PASS (2026-03-19): Reafference diagnostic confirms SD-007 hurts E3 calibration when applied to z_world (correction_delta=-0.045, harm_pred_std drops from 0.108 to 0.008). Over-correction explained by applying reafference to a fused stream that includes the nociceptive signal. If z_harm were separate, reafference correction to z_world would not strip the harm signal. EXQ-044 FAIL (2026-03-…
- Recommendation: `promote_to_stable`
- Options (pros/cons):
  - Promote now (clear canonical status, risk under-tested edge cases)
  - Hold pending stress-test replication (better stress confidence, slower closure)
  - Split claim scope before promotion (clearer boundaries, added doc work)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `pending_user`

### MECH-025
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=0, weakens=2, mixed=2, unknown=0, conflict_ratio=0
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

### MECH-057b
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.906, conflict_ratio=0, exp_entries=4, lit_entries=0; directions supports=0, weakens=1, mixed=3, unknown=0, conflict_ratio=0
- Evidence quality note: No genuine experiments. This claim is explicitly V3-scoped. The thought-loop trajectory promotion gate requires HippocampalModule to implement a feedback path that suppresses trajectory candidates from being promoted to E3 consideration before hippocampal sequence completion is verified. This path is not present in V1 or V2. V3 primary scope: full HippocampalModule trajectory promotion policy and …
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

### MECH-072
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.955, conflict_ratio=0, exp_entries=5, lit_entries=0; directions supports=0, weakens=1, mixed=4, unknown=0, conflict_ratio=0
- Evidence quality note: EXQ-028 FAIL (V2): Same root cause as EXQ-027. Foreseeable-harm gating depends on E2 discriminating agent-caused from env-caused harm — impossible without z_self/z_world split (SD-005) and joint SD-003 pipeline. V3 EXQ-054 FAIL (2026-03-20): world_delta_agent=0.01776 ≈ world_delta_env=0.01806 (1.7% difference, below C3 threshold). C4 FAIL: calibration_gap_approach=0. E2 cannot discriminate agent v…
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
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361139Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Selective residue attribution FAIL (EXQ-028): directly depends on MECH-071 which failed; both require V3 z_self/z_world split (SD-005).

### MECH-090
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.874, conflict_ratio=0.5, exp_entries=4, lit_entries=1; directions supports=1, weakens=3, mixed=1, unknown=0, conflict_ratio=0.5
- Evidence quality note: EXQ-049 FAIL (2026-03-20): Same bug as EXQ-048 — agent.select_action() bypassed, gate never exercised. EXQ-049b fixes this. EXQ-059b FAIL (2026-03-20, 2/5 criteria): Same finding as MECH-057b — routing through select_action() restored but mean_running_variance=0.000. BetaGate elevation requires _running_variance to be populated, which only happens in the E3 training-loop path, not the inference pa…
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
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361144Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Beta gating of E3→action_selection propagation. V3-scoped heartbeat cluster claim.

### MECH-091
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.831, conflict_ratio=0.5, exp_entries=3, lit_entries=1; directions supports=1, weakens=3, mixed=0, unknown=0, conflict_ratio=0.5
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
- Last logged decision: `applied` by `user` at `2026-03-19T19:52:00Z`
- Last selected option: Hold at candidate — resolve conflict first
- Last rationale: User confirmed hold for conflict resolution. z_beta modulates E3 heartbeat frequency — conflicting V3 evidence. Hold at candidate until targeted experiment resolves.

### MECH-096
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=1, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.794, conflict_ratio=0.857, exp_entries=15, lit_entries=3; directions supports=6, weakens=8, mixed=4, unknown=0, conflict_ratio=0.857
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
- Last logged decision: `applied` by `user` at `2026-03-19T19:52:00Z`
- Last selected option: Hold at candidate — resolve conflict first
- Last rationale: User confirmed hold for conflict resolution. Reafference cancellation lstsq vs EMA — 4:4 evidence tie. Hold at candidate until SD-008/009 experiments clarify.

### MECH-099
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.848, conflict_ratio=0.5, exp_entries=2, lit_entries=3; directions supports=3, weakens=1, mixed=1, unknown=0, conflict_ratio=0.5
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
- Last logged decision: `applied` by `user` at `2026-03-19T19:52:00Z`
- Last selected option: Hold at candidate — resolve conflict first
- Last rationale: User confirmed hold for conflict resolution. Three-pathway visual stream — conflicting V3 reafference evidence. Hold at candidate pending resolution.

### MECH-101
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.823, conflict_ratio=0, exp_entries=2, lit_entries=0; directions supports=2, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### Q-007
- Current status: `active`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=0, weakens=1, mixed=2, unknown=0, conflict_ratio=0
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
- Why this decision is needed: overall_conf=0.869, conflict_ratio=0, exp_entries=0, lit_entries=6; directions supports=5, weakens=0, mixed=1, unknown=0, conflict_ratio=0
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

### SD-008
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.696, conflict_ratio=0.5, exp_entries=4, lit_entries=0; directions supports=1, weakens=3, mixed=0, unknown=0, conflict_ratio=0.5
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

### SD-010
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.951, conflict_ratio=0, exp_entries=17, lit_entries=0; directions supports=1, weakens=0, mixed=16, unknown=0, conflict_ratio=0
- Evidence quality note: EXQ-058b ARC-027 PASS (2026-03-20, 5/5 criteria): Foundational validation of the separate harm pathway. HarmEncoder trained with direct MSE supervision on hazard/ resource proximity labels achieves Pearson_r=0.973, calibration_gap=0.712, harm_pred_std=0.417. mean_harm_none=0.014 vs mean_harm_contact=0.987 — clean rank ordering across all event types. First V3 experiment showing z_harm can be learn…
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
