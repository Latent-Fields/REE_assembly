# Promotion / Demotion Recommendations

Generated: `2026-03-29T15:41:02.734729Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-023` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `ARC-026` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `ARC-030` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `ARC-032` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `ARC-033` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `ARC-036` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `pending_user` |
| `MECH-072` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-091` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-092` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-093` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-098` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-099` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-116` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `MECH-118` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `MECH-135` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `Q-019` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `Q-021` | `open` | Question narrowing review | `narrow_open_question` | `pending_user` |
| `Q-022` | `open` | Question narrowing review | `narrow_open_question` | `pending_user` |
| `Q-023` | `open` | Question narrowing review | `narrow_open_question` | `pending_user` |
| `Q-024` | `open` | Question narrowing review | `narrow_open_question` | `pending_user` |
| `SD-011` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |

## Decision Details

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

### ARC-026
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.543, conflict_ratio=1, exp_entries=2, lit_entries=2; directions supports=2, weakens=2, mixed=0, unknown=0, conflict_ratio=1
- Evidence quality note: EXQ-033 FAIL (2026-03-18): Tested C4 — whether approach_slope > contact_slope across training depths (ep 200–1000) on CausalGridWorldV2 (alpha_world=0.9, proximity_scale=0.05). Result: approach_slope=0.000265, contact_slope=0.000289, ratio=0.920. FAIL attributed to training instability: both signals peaked at ep500 (gap_approach=0.285, gap_contact=0.276) then degraded by ep1000 (0.245, 0.265). The…
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

### ARC-030
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.71, conflict_ratio=0.5, exp_entries=1, lit_entries=3; directions supports=3, weakens=1, mixed=0, unknown=0, conflict_ratio=0.5
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

### ARC-032
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.65, conflict_ratio=0.857, exp_entries=4, lit_entries=3; directions supports=3, weakens=4, mixed=0, unknown=0, conflict_ratio=0.857
- Evidence quality note: EXQ-076d FAIL 1/4 (tested jointly with MECH-116, 2026-03-27): same null result as MECH-116 at 2000 steps. ARC-032's specific prediction (theta-bypass degrades goal maintenance) has not been tested -- EXQ-076 only tests joint goal conditioning; no theta-bypass ablation condition was included. ARC-032 remains untested as a standalone architectural claim. Design a separate ablation experiment isolati…
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

### ARC-033
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.595, conflict_ratio=0.8, exp_entries=5, lit_entries=2; directions supports=2, weakens=3, mixed=2, unknown=0, conflict_ratio=0.8
- Evidence quality note: EXQ-030b PASS (2026-03-18): SD-003 counterfactual pipeline validated with z_world and E2.world_forward. This confirms the E2-forward-model-as-counterfactual architecture is sound; the same pattern now applies to z_harm_s. EXQ-093 FAIL (bridge_r2=0) and EXQ-094 FAIL (100x regression) confirm that z_world -> z_harm bridge is not the path forward. EXQ-095a FAIL/SLOW_LEARNING (2026-03-27, 900 phase1 e…
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

### ARC-036
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim has implementation_phase=v3 but no V3 experimental runs yet. No promotion or demotion should be applied until V3 experiments complete.; directions supports=4, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### MECH-072
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=2, weakens=1, mixed=4, unknown=0, conflict_ratio=0.667
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
- Why this decision is needed: overall_conf=0.692, conflict_ratio=0.889, exp_entries=10, lit_entries=1; directions supports=4, weakens=5, mixed=1, unknown=0, conflict_ratio=0.889
- Evidence quality note: EXQ-097 FAIL 2/3 (2026-03-26): C1 FAIL -- p1_rate_gap=-0.74 (threshold >= 2.0). E3 heartbeat rate did NOT differentiate high-harm from low-harm episodes; gap is negative (higher harm -> slightly lower rate) -- opposite of prediction. DIAGNOSTIC (2026-03-27): z_beta IS wired to clock rate. update_e3_rate_from_beta() is called every step in agent._e1_step() (agent.py:272). Implementation gap does NO…
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

### MECH-098
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.764, conflict_ratio=0.857, exp_entries=24, lit_entries=3; directions supports=9, weakens=12, mixed=6, unknown=0, conflict_ratio=0.857
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
- Why this decision is needed: overall_conf=0.692, conflict_ratio=0.857, exp_entries=6, lit_entries=3; directions supports=3, weakens=4, mixed=2, unknown=0, conflict_ratio=0.857
- Evidence quality note: EXQ-098 (2026-03-26): Two independent FAILs. Run 1 (seeds=42, 5 eps warmup): auc_delta=0.0000 (threshold >= 0.05). Run 2 (seeds=42+7, 400 eps warmup): auc_delta=-0.0384 -- lateral head UNDERPERFORMS baseline with more training. Adverse direction in run 2 suggests lateral head may actively interfere with the existing two-stream harm signal. Hold at candidate. EXQ-098b redesign needed before closing…
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

### MECH-116
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.644, conflict_ratio=0.857, exp_entries=4, lit_entries=3; directions supports=3, weakens=4, mixed=0, unknown=0, conflict_ratio=0.857
- Evidence quality note: EXQ-076d FAIL 1/4 (2026-03-27, 2 runs identical): halflife_ratio=1.0, resource_rate_gap=0, goal_norm_t1200_diff=0. Only C3 PASS (goal_norm > 0 in wanting condition). Root cause: halflife threshold (30% of peak goal_norm) never reached in either condition. At 2000 total steps with 1000-step post-removal window, goal persists robustly in both conditions -- insufficient time to observe meaningful dec…
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

### MECH-118
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.697, conflict_ratio=0.5, exp_entries=1, lit_entries=3; directions supports=3, weakens=1, mixed=0, unknown=0, conflict_ratio=0.5
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

### MECH-135
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=7, weakens=2, mixed=1, unknown=0, conflict_ratio=0.444
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
- Last logged decision: `applied` by `user` at `2026-03-28T17:30:00Z`
- Last selected option: Hold at candidate -- EXQ-104b diagnostic required before evidence update
- Last rationale: EXQ-103 PASS x2 confirms E2 multi-step training substrate is functional. EXQ-104/105 FAIL 0/3 is an implementation artifact (untrained agent -- E2.world_forward maps to near-zero, FROZEN appears high from random cosine similarity). EXQ-104b queued with training phase. Do not count EXQ-104/105 as weakening MECH-135 until trained-agent retest. v3_pending retained pending diagnostic.

### Q-019
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.867, conflict_ratio=0, exp_entries=0, lit_entries=6; directions supports=5, weakens=0, mixed=1, unknown=0, conflict_ratio=0
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

### Q-021
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.726, conflict_ratio=0, exp_entries=1, lit_entries=3; directions supports=3, weakens=0, mixed=1, unknown=0, conflict_ratio=0
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

### Q-022
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.669, conflict_ratio=0, exp_entries=1, lit_entries=2; directions supports=2, weakens=0, mixed=1, unknown=0, conflict_ratio=0
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

### Q-023
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.812, conflict_ratio=0, exp_entries=0, lit_entries=3; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### Q-024
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.8, conflict_ratio=0, exp_entries=0, lit_entries=3; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### SD-011
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.777, conflict_ratio=0.667, exp_entries=12, lit_entries=5; directions supports=6, weakens=3, mixed=4, unknown=0, conflict_ratio=0.667
- Evidence quality note: EXQ-093 FAIL + EXQ-094 FAIL (2026-03-24): Both confirmed bridge_r2=0 -- SD-010 makes z_world perp z_harm by architectural design, so HarmBridge(z_world -> z_harm) is infeasible (nothing to learn). EXQ-094 confirmed training E3 on bridge noise produced 100x regression in harm_var vs EXQ-088. These experiments collectively demonstrate that the current single-stream z_harm cannot simultaneously serve…
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
