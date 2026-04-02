# Promotion / Demotion Recommendations

Generated: `2026-04-01T23:30:17.467339Z`
Decision scope: `current_epoch_applicable,epoch=ree_hybrid_guardrails_v1`

This file proposes decisions only. No claim status changes are applied automatically.
Use this as the human-in-the-loop review queue.

## Decision Queue

| claim_id | current_status | decision_needed | recommendation | decision_status |
|---|---|---|---|---|
| `ARC-026` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `ARC-030` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `ARC-032` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `ARC-033` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `ARC-038` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `ARC-041` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-025` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |
| `MECH-057a` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `applied` |
| `MECH-072` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-091` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-092` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-093` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-094` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-098` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-099` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-100` | `provisional` | Promotion review: provisional -> stable | `promote_to_stable` | `pending_user` |
| `MECH-111` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-112` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-116` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-118` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-135` | `candidate` | Hold — V3 substrate required before meaningful evidence can be collected | `hold_pending_v3_substrate` | `applied` |
| `MECH-150` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `MECH-152` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |
| `Q-019` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `Q-021` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `Q-022` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `Q-023` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `Q-024` | `open` | Question narrowing review | `narrow_open_question` | `applied` |
| `SD-009` | `candidate` | Promotion review: candidate -> provisional | `promote_to_provisional` | `pending_user` |
| `SD-011` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `SD-012` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `applied` |
| `SD-015` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` | `pending_user` |

## Decision Details

### ARC-026
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.539, conflict_ratio=1, exp_entries=2, lit_entries=2; directions supports=2, weakens=2, mixed=0, unknown=0, conflict_ratio=1
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.111675Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### ARC-030
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.682, conflict_ratio=0.667, exp_entries=7, lit_entries=3; directions supports=3, weakens=6, mixed=0, unknown=1, conflict_ratio=0.667
- Evidence quality note: Hold at candidate (2026-03-29): no new experiments this session. SD-010 dependency and approach-avoidance symmetry (Go sub-channel implementation) required before testing. No experimental evidence yet. EXQ-086 INCONCLUSIVE/bug (2026-03-30, re-run of 20260323): benefit_rate=0 despite 274 buffered benefit events -- measurement bug in benefit_rate computation from buffer. Go sub-channel logging works…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.149863Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### ARC-032
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.646, conflict_ratio=0.857, exp_entries=4, lit_entries=3; directions supports=3, weakens=4, mixed=0, unknown=0, conflict_ratio=0.857
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.185592Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### ARC-033
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.683, conflict_ratio=1, exp_entries=18, lit_entries=2; directions supports=4, weakens=4, mixed=2, unknown=0, conflict_ratio=1
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.222068Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### ARC-038
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.547, conflict_ratio=1, exp_entries=1, lit_entries=1; directions supports=1, weakens=1, mixed=0, unknown=0, conflict_ratio=1
- Evidence quality note: >
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
- Last logged decision: `applied` by `user` at `2026-03-31T20:20:00.000000Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: V3-gated claim, no V3 runs yet. Hold.

### ARC-041
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.681, conflict_ratio=0.5, exp_entries=3, lit_entries=2; directions supports=3, weakens=1, mixed=0, unknown=0, conflict_ratio=0.5
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
- Last logged decision: `applied` by `user` at `2026-03-31T20:20:00.000000Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict_ratio=1.0 with only 2 experimental entries. Insufficient evidence to resolve.

### MECH-025
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.587, conflict_ratio=1, exp_entries=5, lit_entries=2; directions supports=2, weakens=2, mixed=3, unknown=0, conflict_ratio=1
- Evidence quality note: V3 gate cleared (2026-03-28): SD-004 (action objects), SD-005 (z_self/z_world split), and ARC-016 (dynamic precision) now implemented in ree-v3. V3 action-doing mode experiments can now proceed. V2 experiment EXQ-026 (action_doing_mode_probe, EVB-0025) FAIL -- 1 run (2026-03-08). Proximate failure: action_precision_lift = 0.0 across all seeds/conditions — E3 precision hardcoded, no dynamic channel…
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
- Last logged decision: `applied` by `user` at `2026-03-16T18:20:19.361130Z`
- Last selected option: Wait for V3 substrate implementation (correct path)
- Last rationale: User confirmed hold. Action-doing mode probe FAIL (EXQ-026): V2 substrate lacks the multi-rate loop and heartbeat architecture required to instantiate distinct action-doing mode.

### MECH-057a
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.786, conflict_ratio=0, exp_entries=2, lit_entries=2; directions supports=3, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Evidence quality note: Prior 10 synthetic runs (ree-v2/ree-experiments-lab, archived 2026-02-26) are invalid. Genuine ree-v1-minimal experiment completed 2026-02-26 (EVB-0042, control_completion_requirement): FAIL (informative baseline — effect direction correct, magnitude sub-threshold). FULL last-Q harm 0.879 | NO_ATTRIBUTION 0.896 (+1.9%) | NO_GATING 0.919 (+4.5%). Degradation threshold 1.1 (10%): neither ablation me…
- Recommendation: `promote_to_provisional`
- Options (pros/cons):
  - Promote now (faster convergence, risk premature lock-in)
  - Hold until one additional confirming run (better robustness, slower progress)
  - Hold and request targeted literature triangulation (better external grounding, extra delay)
- Discussion scope with Codex:
  - Which uncertainty source dominates: model variance, threshold choice, or claim scope?
  - What single additional experiment or literature extraction would most reduce uncertainty?
  - If this decision is wrong, what downstream architecture risk is largest?
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:15:31.848348Z`
- Last selected option: Hold at candidate -- investigate committed sequence generation first
- Last rationale: EXQ-139 FAIL: committed sequences never generated (mean_committed_seq_len_on=0.0) at current training budget. Substrate issue, not falsification. Hold until committed-sequence generation is verified before promotion.

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
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.501, conflict_ratio=1, exp_entries=1, lit_entries=1; directions supports=1, weakens=1, mixed=0, unknown=0, conflict_ratio=1
- Evidence quality note: Held (2026-03-28): specific blocker is SD-006 (async multi-rate loop execution). Phase-reset of E3 heartbeat requires SD-006 phase 2 async implementation first. EXQ-133 FAIL (2026-03-29): 5656 phase resets fired successfully but produced no discriminative behavioral signal (gap_on=0.014, criterion needs >=0.04). Resets execute but downstream async update consequences do not propagate. SD-006 phase…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.297665Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-092
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.543, conflict_ratio=1, exp_entries=1, lit_entries=1; directions supports=1, weakens=1, mixed=0, unknown=0, conflict_ratio=1
- Evidence quality note: Held (2026-03-28): specific blocker is SD-006 (async multi-rate loop execution). Quiescent heartbeat replay requires SD-006 phase 2 async loop before testing. EXQ-136 FAIL/weakens (2026-03-29): quiescent replay discriminative pair FAIL. SD-006 phase 2 async required for full offline consolidation. Confirms existing hold.
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.333183Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-093
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.686, conflict_ratio=0.889, exp_entries=10, lit_entries=1; directions supports=4, weakens=5, mixed=1, unknown=0, conflict_ratio=0.889
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

### MECH-094
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.627, conflict_ratio=0.5, exp_entries=2, lit_entries=3; directions supports=3, weakens=1, mixed=0, unknown=0, conflict_ratio=0.5
- Evidence quality note: EXQ-140 FAIL/weakens (2026-03-29): hypothesis tag gate discriminative pair FAIL. Consistent with prior finding that hypothesis tag gate as implemented is invalid as an approach. Weakening evidence accumulating.
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.368222Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-098
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.752, conflict_ratio=0.8, exp_entries=24, lit_entries=3; directions supports=8, weakens=12, mixed=7, unknown=0, conflict_ratio=0.8
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
- Why this decision is needed: overall_conf=0.689, conflict_ratio=0.857, exp_entries=6, lit_entries=3; directions supports=3, weakens=4, mixed=2, unknown=0, conflict_ratio=0.857
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

### MECH-100
- Current status: `provisional`
- Decision needed: Promotion review: provisional -> stable
- Why this decision is needed: overall_conf=0.817, conflict_ratio=0, exp_entries=4, lit_entries=3; directions supports=7, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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
- Status note: Prior decision exists but recommendation changed; needs fresh review.
- Last logged decision: `applied` by `user` at `2026-03-19T19:52:00Z`
- Last selected option: Promote to provisional
- Last rationale: User confirmed. V3 evidence crosses provisional threshold. Event-contrastive CE auxiliary loss required for z_world encoder discrimination. Promoted candidate → provisional.

### MECH-111
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.564, conflict_ratio=0.667, exp_entries=2, lit_entries=2; directions supports=2, weakens=1, mixed=1, unknown=0, conflict_ratio=0.667
- Evidence quality note: EXQ-141 FAIL/weakens (2026-03-29): novelty drive discriminative pair FAIL. First experimental entry.
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.399734Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-112
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.752, conflict_ratio=1, exp_entries=22, lit_entries=3; directions supports=6, weakens=6, mixed=8, unknown=0, conflict_ratio=1
- Evidence quality note: EXQ-074c superseded (2026-03-27): resource_respawn bug -- zero resource visits in all conditions. Superseded by EXQ-074d. EXQ-074d FAIL 3/4, EXQ-074e FAIL 3/4 (2026-03-27): C1 FAIL in both (resource_rate_gap=0). C1 confound: greedy navigation applied uniformly to all conditions -- wanting cannot show a behavioural lift above nogo even when z_goal is active (goal_active=True, goal_norm=0.28 in 074d…
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
- Last logged decision: `applied` by `user` at `2026-03-31T20:20:00.000000Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict_ratio=0.889 with greedy navigation confound identified. Resolution experiments needed to isolate z_goal behavioral signal.

### MECH-116
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.64, conflict_ratio=0.857, exp_entries=4, lit_entries=3; directions supports=3, weakens=4, mixed=0, unknown=0, conflict_ratio=0.857
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.432666Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-118
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.724, conflict_ratio=0.4, exp_entries=3, lit_entries=3; directions supports=4, weakens=1, mixed=1, unknown=0, conflict_ratio=0.4
- Evidence quality note: EXQ-143 FAIL/mixed (2026-03-29): Hopfield familiarity discriminative pair FAIL. First experimental entry. EXQ-084d SUPPORTS (per-claim override, 2026-03-30): stability dissociation confirmed -- stab collapses with both noise (0.063 vs 0.950) and novelty (0.026 vs 0.950) perturbation. Stability signal responds to perturbation as distinct signal from D_eff (D_eff remains flat ~20.6-20.8 across R1/R2…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.465228Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### MECH-135
- Current status: `candidate`
- Decision needed: Hold — V3 substrate required before meaningful evidence can be collected
- Why this decision is needed: Claim is flagged v3_pending (explicit manual gate). No promotion or demotion should be applied until this flag is cleared.; directions supports=8, weakens=2, mixed=1, unknown=0, conflict_ratio=0.4
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

### MECH-150
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.685, conflict_ratio=0.5, exp_entries=3, lit_entries=2; directions supports=3, weakens=1, mixed=0, unknown=0, conflict_ratio=0.5
- Evidence quality note: >
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
- Last logged decision: `applied` by `user` at `2026-03-31T20:20:00.000000Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict_ratio=1.0, only 2 experimental entries, empty evidence quality note. Needs dedicated experiments.

### MECH-152
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.775, conflict_ratio=0, exp_entries=2, lit_entries=2; directions supports=4, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Evidence quality note: >
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

### Q-019
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.866, conflict_ratio=0, exp_entries=0, lit_entries=6; directions supports=5, weakens=0, mixed=1, unknown=0, conflict_ratio=0
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
- Why this decision is needed: overall_conf=0.723, conflict_ratio=0, exp_entries=1, lit_entries=3; directions supports=3, weakens=0, mixed=1, unknown=0, conflict_ratio=0
- Evidence quality note: narrow_open_question (2026-03-29): two independent pathways to behavioral flatness already identified in notes. Pathway A (drive absence, ARC-030) tested by EXQ-072; Pathway B (self-incoherence-gated commit suppression, MECH-113/114) untested. Definitive test requires both pathways. No experimental evidence yet -- question narrowing applied to focus on discriminating between the two pathways.
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:15:46.773489Z`
- Last selected option: Narrow the question into testable sub-questions (higher tractability)
- Last rationale: Two independent pathways to behavioral flatness identified (Pathway A: drive absence, ARC-030; Pathway B: self-incoherence-gated commit suppression, MECH-113/114). Discriminative experiment design specified in evidence_quality_note.

### Q-022
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.643, conflict_ratio=0, exp_entries=2, lit_entries=2; directions supports=2, weakens=0, mixed=2, unknown=0, conflict_ratio=0
- Evidence quality note: narrow_open_question (2026-03-29): three-regime dissociation experiment design specified in notes: (1) Normal training: low D_eff + high stability; (2) Noise perturbation: high D_eff + low stability; (3) Structured novel perturbation: low D_eff + low stability (targeted basis rotation). Experiment to test whether Regime 3 is empirically distinguishable from Regime 2. No experimental evidence yet -…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:15:46.805989Z`
- Last selected option: Narrow the question into testable sub-questions (higher tractability)
- Last rationale: Three-regime dissociation experiment design specified: Normal training (low D_eff + high stability), Noise perturbation (high D_eff + low stability), Structured novel perturbation (low D_eff + low stability). Target: distinguish Regime 3 from Regime 2 empirically.

### Q-023
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.728, conflict_ratio=0, exp_entries=1, lit_entries=3; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Evidence quality note: narrow_open_question (2026-03-29): three-step focused programme identified -- (1) prove base REE (symmetric coupling, separable harm/benefit) is an ordinal potential game; (2) show MECH-127 (counterfactual utility) breaks the standard framework; (3) characterize the extended framework (pseudo-potential or interdependent-types). No experimental evidence yet. EXQ-160 SUPERSEDED (2026-03-29): impleme…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:15:46.837005Z`
- Last selected option: Narrow the question into testable sub-questions (higher tractability)
- Last rationale: Three-step programme: (1) prove base REE is ordinal potential game; (2) show MECH-127 counterfactual utility breaks standard framework; (3) characterize extended framework. EXQ-160 superseded -- implementation gap.

### Q-024
- Current status: `open`
- Decision needed: Question narrowing review
- Why this decision is needed: overall_conf=0.691, conflict_ratio=0, exp_entries=2, lit_entries=3; directions supports=3, weakens=0, mixed=0, unknown=0, conflict_ratio=0
- Evidence quality note: EXQ-161 T104847Z SUPERSEDED (2026-03-29): dry_run=true -- no training occurred; all harm events=0; result invalid. Manifest marked superseded. EXQ-161 T200440Z SUPERSEDED (2026-03-29): implementation gap -- policy trained only with entropy bonus, z_world/z_self detached from policy forward pass; maximum-entropy random walk (action_entropy=ln(5)=1.6094). No harm events; trajectory representation qu…
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
- Last logged decision: `applied` by `user` at `2026-03-29T21:15:46.867662Z`
- Last selected option: Narrow the question into testable sub-questions (higher tractability)
- Last rationale: EXQ-161 superseded (dry-run artifact; implementation gap -- policy trained with entropy bonus only, z_world/z_self detached). Question narrowing applied to focus on discriminating DESCRIPTIVE vs PRESCRIPTIVE vs DIAGNOSTIC trajectory representations. Fresh experiment required.

### SD-009
- Current status: `candidate`
- Decision needed: Promotion review: candidate -> provisional
- Why this decision is needed: overall_conf=0.768, conflict_ratio=0, exp_entries=2, lit_entries=2; directions supports=4, weakens=0, mixed=0, unknown=0, conflict_ratio=0
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

### SD-011
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.818, conflict_ratio=0.667, exp_entries=24, lit_entries=5; directions supports=8, weakens=4, mixed=3, unknown=0, conflict_ratio=0.667
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
- Decision status: `applied`
- Last logged decision: `applied` by `user` at `2026-03-29T21:16:41.260169Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: conflict ratio requires resolution before promotion. Dedicated experiments queued.

### SD-012
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.729, conflict_ratio=0.857, exp_entries=12, lit_entries=3; directions supports=4, weakens=3, mixed=3, unknown=0, conflict_ratio=0.857
- Evidence quality note: EXQ-085f FAIL 3/4 (2026-03-27): drive_weight=2.0, resource_respawn_on_consume=True, curriculum=100 eps. C1 PASS: z_goal_norm=0.228 > 0.1 -- SD-012 drive modulation successfully seeds z_goal (this IS the SD-012 core claim: drive-scaled benefit enables seeding). C2 FAIL: benefit_ratio=0.28x -- goal-guided performance worse than random. C3 PASS (cal_gap=0.030). SD-012 seeding mechanism works; downstr…
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
- Last logged decision: `applied` by `user` at `2026-03-31T20:20:00.000000Z`
- Last selected option: Keep candidate and run conflict-resolution experiments (most balanced)
- Last rationale: Hold at candidate: seeding mechanism works (C1 PASS) but downstream utilization fails (C2 FAIL). SD-012 core claim partially validated; resolution experiments needed for goal-to-behavior pathway.

### SD-015
- Current status: `candidate`
- Decision needed: Conflict resolution before promotion
- Why this decision is needed: overall_conf=0.665, conflict_ratio=0.75, exp_entries=10, lit_entries=3; directions supports=3, weakens=5, mixed=1, unknown=0, conflict_ratio=0.75
- Evidence quality note: Registered 2026-03-29 from EXQ-085g FAIL analysis (goal_resource_r=0.066 across all 085x iterations despite contact-gated seeding). EXP-0091 will first test a handcrafted resource_indicator to confirm the diagnosis before implementing the full encoder. EXQ-085h through 085l (2026-03-30, 085l final, supersedes prior): ResourceEncoder tested across 5 iterations. 085l (proximity regression encoder): …
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
