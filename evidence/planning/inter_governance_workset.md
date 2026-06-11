# Inter-Governance Workset

Generated: `2026-06-11T07:14:40Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **208** (ready 28, in_flight 0, blocked 161)
- Pending review: **1**
- Queue pending (unclaimed): **0**

- Live EXQs: V3-EXQ-514m, V3-EXQ-603o, V3-EXQ-655, V3-EXQ-660b, V3-EXQ-667

- Auto-absorbed retests (queued, suppressed from workset): INV-074 -> V3-EXQ-655, MECH-229 -> V3-EXQ-514m, MECH-341 -> V3-EXQ-660b, Q-043 -> V3-EXQ-667, SD-059 -> V3-EXQ-603o

## Work packages

### IGW-20260611-001 -- Complete governance review (1 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 1 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-001
Title: Complete governance review (1 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 1 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-183 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-183
Title: Implement substrate: ARC-046 (unblocks ARC-046)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-046, DEV-NEED-008
Blocked by: ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
Why now: substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-185 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-185
Title: Implement substrate: escape-affordance-bridge (unblocks ARC-060)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-058, MECH-357, ARC-060, MECH-320, ARC-068, SD-054-readiness
Blocked by: ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
Why now: substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-187 -- Implement substrate: ARC-062 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-187
Title: Implement substrate: ARC-062 (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-309, ARC-062, SD-033a, MECH-262, SD-029
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-188 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-188
Title: Implement substrate: SD-054 (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-054, MECH-309, ARC-062
Blocked by: ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
Why now: substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-189 -- Implement substrate: crf-availability-maintenance (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: PRIMARY blocking dep: targeted_review_arc_063_crf_rule_cell_persistence lit-pull (persistent-firing vs activity-silent fork) -- if activity-silent, crf_frac_active is itself the wrong readout and must; free-text: targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented]
- **Why now:** substrate_queue entry status=pending_implementation with 3 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-189
Title: Implement substrate: crf-availability-maintenance (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-309, ARC-062, ARC-063
Blocked by: ready_blocked_by: PRIMARY blocking dep: targeted_review_arc_063_crf_rule_cell_persistence lit-pull (persistent-firing vs activity-silent fork) -- if activity-silent, crf_frac_active is itself the wrong readout and must; free-text: targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented]
Why now: substrate_queue entry status=pending_implementation with 3 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-192 -- Implement substrate: ARC-065 (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Q-044 three-arm ablation + Q-045 4-arm ablation pending substrate-landing of all four child substrates (MECH-313/314/318/319).; Q-043 [no-substrate-entry]: Q-043 weight calibration; Q-044 [no-substrate-entry]: Q-044 three-arm ablation; Q-045 [no-substrate-entry]: Q-045 4-arm ablation
- **Why now:** substrate_queue entry status=phase_1_implemented with 4 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-192
Title: Implement substrate: ARC-065 (unblocks ARC-065)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-065, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c
Blocked by: ready_blocked_by: Q-044 three-arm ablation + Q-045 4-arm ablation pending substrate-landing of all four child substrates (MECH-313/314/318/319).; Q-043 [no-substrate-entry]: Q-043 weight calibration; Q-044 [no-substrate-entry]: Q-044 three-arm ablation; Q-045 [no-substrate-entry]: Q-045 4-arm ablation
Why now: substrate_queue entry status=phase_1_implemented with 4 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-193 -- Implement substrate: MECH-314a-Phase-2-impl (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Amend implemented 2026-06-07 (e2.world_forward novelty source); validation pending V3-EXQ-648a substrate-readiness PASS (curiosity_candidate_source='e2_world_forward' + readiness precondition re-targe
- **Why now:** substrate_queue entry status=amend_implemented_pending_validation with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-193
Title: Implement substrate: MECH-314a-Phase-2-impl (unblocks ARC-065)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-314a, MECH-314, ARC-065
Blocked by: ready_blocked_by: Amend implemented 2026-06-07 (e2.world_forward novelty source); validation pending V3-EXQ-648a substrate-readiness PASS (curiosity_candidate_source='e2_world_forward' + readiness precondition re-targe
Why now: substrate_queue entry status=amend_implemented_pending_validation with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-194 -- Implement substrate: SD-056 (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-194
Title: Implement substrate: SD-056 (unblocks ARC-065)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-065, MECH-341, MECH-309
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-197 -- Implement substrate: SD-049 (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
- **Why now:** substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-197
Title: Implement substrate: SD-049 (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
Why now: substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-198 -- Implement substrate: SD-049-PHASE-2 (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3
- **Why now:** substrate_queue entry status=phase_2_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-198
Title: Implement substrate: SD-049-PHASE-2 (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3
Why now: substrate_queue entry status=phase_2_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-199 -- Implement substrate: MECH-307 (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-199
Title: Implement substrate: MECH-307 (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: Q-040, SD-049, SD-015, MECH-111, SD-032b, ARC-030
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-203 -- Implement substrate: SD-033 (unblocks MECH-266)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
- **Why now:** substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-266. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-203
Title: Implement substrate: SD-033 (unblocks MECH-266)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-033a, SD-033b, SD-033c, SD-033d, SD-033e, SD-034
Blocked by: ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
Why now: substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-266. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-002 -- Two-levels-of-abstraction distinction (the load-bearing scoping claim)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** abstract_relational_reasoning_v6:ARR-1
- **Why now:** Plan gap open on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-002
Title: Two-levels-of-abstraction distinction (the load-bearing scoping claim)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): abstract_relational_reasoning_v6:ARR-1
Claims: ARC-102
Why now: Plan gap open on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-021 -- Memory-type taxonomy decision (Q-060): distinct autobiographical-event type, or a tag on episodic content?

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** autobiographical_memory_v4:ABM-1
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-021
Title: Memory-type taxonomy decision (Q-060): distinct autobiographical-event type, or a tag on episodic content?
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): autobiographical_memory_v4:ABM-1
Claims: Q-060, ARC-085
Why now: Plan gap open on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-040 -- Non-terminal drive register (drives beyond hunger/thirst as first-class axes)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** drives_motivation_v4:DRV-1
- **Why now:** Plan gap open on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-040
Title: Non-terminal drive register (drives beyond hunger/thirst as first-class axes)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): drives_motivation_v4:DRV-1
Claims: SD-060, MECH-111
Why now: Plan gap open on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-051 -- No-empathy-scalar architectural prohibition (the load-bearing prohibition)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** fast_empathy_v5:EMP-1
- **Why now:** Plan gap open on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-051
Title: No-empathy-scalar architectural prohibition (the load-bearing prohibition)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): fast_empathy_v5:EMP-1
Claims: ARC-094
Why now: Plan gap open on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-057 -- Single-slot vs multi-slot fork (the first design decision: does V4 widen GoalState to N>=2?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** goal_deliberation_v4:GDL-1
- **Why now:** Plan gap open on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-057
Title: Single-slot vs multi-slot fork (the first design decision: does V4 widen GoalState to N>=2?)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): goal_deliberation_v4:GDL-1
Claims: SD-046
Why now: Plan gap open on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-065 -- Mine-not-import discipline: grammar/LLMs are a primitive MINE, never an architecture to transfer (load-bearing prohibiti

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** grammar_primitive_mining_v6:GRAM-1
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-065
Title: Mine-not-import discipline: grammar/LLMs are a primitive MINE, never an architecture to transfer (load-bearing prohibiti
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): grammar_primitive_mining_v6:GRAM-1
Claims: ARC-100, INV-003, INV-007
Why now: Plan gap open on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-080 -- Name + route the inference layer (V3 architecture note, no substrate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** inference_belief_state_v4:INF-1
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-080
Title: Name + route the inference layer (V3 architecture note, no substrate)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): inference_belief_state_v4:INF-1
Claims: ARC-091
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-092 -- Bootstrap-not-bolt-on architectural commitment (the load-bearing spine: language emerges from social ecology, is never i

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** language_emergence_bootstrap_v6:LANG-1
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-092
Title: Bootstrap-not-bolt-on architectural commitment (the load-bearing spine: language emerges from social ecology, is never i
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): language_emergence_bootstrap_v6:LANG-1
Claims: INV-003, ARC-009
Why now: Plan gap open on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-099 -- Language-cannot-override-harm as an explicit GUARD mechanism (operationalise INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** language_trust_deception_institutions_v6:LTI-1
- **Why now:** Plan gap open on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-099
Title: Language-cannot-override-harm as an explicit GUARD mechanism (operationalise INV-007)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): language_trust_deception_institutions_v6:LTI-1
Claims: INV-007, ARC-104
Why now: Plan gap open on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-111 -- Allocation-gate decision stage on MECH-261 (integrate / partial_overlap / separate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** memory_lifecycle_v4:MEM-1
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-111
Title: Allocation-gate decision stage on MECH-261 (integrate / partial_overlap / separate)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): memory_lifecycle_v4:MEM-1
Claims: MECH-261, MECH-391
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-114 -- Raw-episode-preservation invariant (consolidation_output MUST NOT replace source_episode_evidence)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** memory_lifecycle_v4:MEM-4
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-114
Title: Raw-episode-preservation invariant (consolidation_output MUST NOT replace source_episode_evidence)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): memory_lifecycle_v4:MEM-4
Claims: ARC-007, ARC-020, INV-080
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-133 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap open on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-133
Title: Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-1
Claims: MECH-299, MECH-300
Why now: Plan gap open on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-140 -- Type-vs-token-vs-anchor representational fork (the first design decision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_representation_v4:OBJ-1
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-140
Title: Type-vs-token-vs-anchor representational fork (the first design decision)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): object_representation_v4:OBJ-1
Claims: ARC-080
Why now: Plan gap open on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-146 -- Smell-vs-sight adaptor-depth fork (the first design decision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** perceptual_adaptors_v4:PA-1
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-146
Title: Smell-vs-sight adaptor-depth fork (the first design decision)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): perceptual_adaptors_v4:PA-1
Claims: ARC-087, MECH-372
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-153 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-153
Title: Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): plasticity_neuromodulation_v4:PLW-1
Claims: INV-074, MECH-333
Why now: Plan gap open on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-171 -- z_self promoted from body-state latent to a stateful self-model (DR-13 temporal depth)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** self_model_v4:SELF-1
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-171
Title: z_self promoted from body-state latent to a stateful self-model (DR-13 temporal depth)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): self_model_v4:SELF-1
Claims: ARC-081
Why now: Plan gap open on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-179 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-179
Title: Substrate (blocked): SD-033b
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-261, MECH-263
Blocked by: SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
Why now: substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-180 -- Substrate (blocked): scaffolded_sd054_onboarding

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-180
Title: Substrate (blocked): scaffolded_sd054_onboarding
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-030, MECH-117, MECH-230, MECH-260, MECH-295, MECH-307
Blocked by: SD-054 [candidate_v3_pending]; MECH-307 [implemented]
Why now: substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-182 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-182
Title: Retest after substrate: ARC-046
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-046
Blocked by: ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-184 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-184
Title: Retest after substrate: ARC-060
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-060
Blocked by: escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-186 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); crf-availability-maintenance [pending_implementation]; free-text (via crf-availability-maintenance): targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented] (transitive via crf-availability-maintenance)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 6 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-186
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-062
Blocked by: ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); crf-availability-maintenance [pending_implementation]; free-text (via crf-availability-maintenance): targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented] (transitive via crf-availability-maintenance)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 6 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-190 -- Retest after substrate: ARC-063

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** crf-availability-maintenance [pending_implementation]; free-text (via crf-availability-maintenance): targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented] (transitive via crf-availability-maintenance)
- **Why now:** Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-190
Title: Retest after substrate: ARC-063
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-063
Blocked by: crf-availability-maintenance [pending_implementation]; free-text (via crf-availability-maintenance): targeted_review_arc_063_crf_rule_cell_persistence (lit-pull, blocking); ARC-062 [implemented] (transitive via crf-availability-maintenance)
Why now: Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-191 -- Retest after substrate: ARC-065

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-065 [phase_1_implemented]; Q-043 [no-substrate-entry] (transitive via ARC-065): Q-043 weight calibration; Q-044 [no-substrate-entry] (transitive via ARC-065): Q-044 three-arm ablation; Q-045 [no-substrate-entry] (transitive via ARC-065): Q-045 4-arm ablation; MECH-314a-Phase-2-impl [amend_implemented_pending_validation]; SD-056 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 6 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-191
Title: Retest after substrate: ARC-065
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-065
Blocked by: ARC-065 [phase_1_implemented]; Q-043 [no-substrate-entry] (transitive via ARC-065): Q-043 weight calibration; Q-044 [no-substrate-entry] (transitive via ARC-065): Q-044 three-arm ablation; Q-045 [no-substrate-entry] (transitive via ARC-065): Q-045 4-arm ablation; MECH-314a-Phase-2-impl [amend_implemented_pending_validation]; SD-056 [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 6 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-195 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-195
Title: Retest after substrate: ARC-068
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-068
Blocked by: escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-196 -- Retest after substrate: MECH-230

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-196
Title: Retest after substrate: MECH-230
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-230
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-200 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-200
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-201 -- Retest after substrate: MECH-262

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-201
Title: Retest after substrate: MECH-262
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-262
Blocked by: ARC-062 [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-202 -- Retest after substrate: MECH-266

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-202
Title: Retest after substrate: MECH-266
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-266
Blocked by: SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-015 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
- **Why now:** GATED ON V3-EXQ-666 (CRF-readiness diagnostic) PASS. The 654b autopsy-routed substrate enrichment LANDED 2026-06-11 (ARC-063 CandidateRuleField mature-pool amend, ree-v3 7e2e0ef; see governance_2026_06_11) -- the two opt-in flags crf_mature

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-015
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
Claims: MECH-309, ARC-062
Why now: GATED ON V3-EXQ-666 (CRF-readiness diagnostic) PASS. The 654b autopsy-routed substrate enrichment LANDED 2026-06-11 (ARC-063 CandidateRuleField mature-pool amend, ree-v3 7e2e0ef; see governance_2026_06_11) -- the two opt-in flags crf_mature

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-029 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
- **Why now:** PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is now load-bearing-CONFIRMED but 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-029
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
Claims: MECH-341, ARC-062, ARC-065
Why now: PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is now load-bearing-CONFIRMED but 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-064 -- Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** goal_pipeline:GAP-7
- **Blocked by:** goal_pipeline:GAP-2 [open]
- **Why now:** STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) in

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-064
Title: Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): goal_pipeline:GAP-7
Claims: MECH-229, MECH-230, MECH-117, ARC-030
Blocked by: goal_pipeline:GAP-2 [open]
Why now: STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) in

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-164 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625c
- **Why now:** RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend lands and the agent generates oscillating, non-monostrategy z_harm_a under the axis-(b) env overlay. SD-037 status is unchanged: the substrate_ceilin

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-164
Title: Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): sd_037_axis_b:P1b
Owner EXQ: V3-EXQ-625c
Claims: SD-037, MECH-281
Why now: RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend lands and the agent generates oscillating, non-monostrategy z_harm_a under the axis-(b) env overlay. SD-037 status is unchanged: the substrate_ceilin

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-181 -- Queue depth low (0 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-181
Title: Queue depth low (0 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-003 -- Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-2
- **Blocked by:** abstract_relational_reasoning_v6:ARR-1 [open]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-003
Title: Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-2
Claims: MECH-419
Blocked by: abstract_relational_reasoning_v6:ARR-1 [open]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-007 -- Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-6
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-007
Title: Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-6
Claims: ARC-103
Blocked by: abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-008 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-008
Title: FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-1
Claims: MECH-359
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-022 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Blocked by:** autobiographical_memory_v4:ABM-1 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-022
Title: Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-2
Claims: ARC-085
Blocked by: autobiographical_memory_v4:ABM-1 [open]
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-023 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-023
Title: Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-3
Claims: MECH-365
Blocked by: autobiographical_memory_v4:ABM-2 [blocked]
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-034 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Blocked by:** developmental_dmn_v4:DMN-1 [open]
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-034
Title: Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-2
Claims: Q-068
Blocked by: developmental_dmn_v4:DMN-1 [open]
Why now: Plan gap open on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-035 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-035
Title: PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-3
Claims: ARC-090
Blocked by: developmental_dmn_v4:DMN-2 [open]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-041 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** drives_motivation_v4:DRV-2
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-041
Title: Multidrive arbitration / orchestration policy (which drive wins when several are active)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): drives_motivation_v4:DRV-2
Claims: MECH-394, MECH-295
Blocked by: drives_motivation_v4:DRV-1 [open]
Why now: Plan gap blocked on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-044 -- Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-1
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-044
Title: Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-1
Claims: ARC-056
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-045 -- Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-2
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-045
Title: Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-2
Claims: ARC-096
Blocked by: ethics_as_coherence_v5:ETH-1 [blocked]
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-046 -- Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-3
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-046
Title: Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-3
Claims: ARC-097, MECH-411, MECH-412
Blocked by: ethics_as_coherence_v5:ETH-2 [blocked]
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-053 -- Stream-binding mechanism: route own motivational-affective streams across the other-model

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-3
- **Blocked by:** fast_empathy_v5:EMP-1 [open]; fast_empathy_v5:EMP-2 [open]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-053
Title: Stream-binding mechanism: route own motivational-affective streams across the other-model
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-3
Claims: MECH-405
Blocked by: fast_empathy_v5:EMP-1 [open]; fast_empathy_v5:EMP-2 [open]
Why now: Plan gap blocked on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-054 -- Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-4
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-054
Title: Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-4
Claims: MECH-406
Blocked by: fast_empathy_v5:EMP-3 [blocked]
Why now: Plan gap blocked on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-058 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-058
Title: PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-2
Claims: SD-033e
Blocked by: goal_deliberation_v4:GDL-1 [open]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-067 -- Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-3
- **Blocked by:** grammar_primitive_mining_v6:GRAM-1 [open]; grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-067
Title: Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-3
Claims: MECH-415, ARC-063
Blocked by: grammar_primitive_mining_v6:GRAM-1 [open]; grammar_primitive_mining_v6:GRAM-2 [open]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-070 -- Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-6
- **Blocked by:** grammar_primitive_mining_v6:GRAM-1 [open]; grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-070
Title: Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-6
Claims: ARC-101, ARC-009, INV-003
Blocked by: grammar_primitive_mining_v6:GRAM-1 [open]; grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-071 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-071
Title: GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-1
Claims: MECH-163
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-072 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-072
Title: PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-2
Claims: ARC-040
Blocked by: hippocampal_planning_v4:HPL-1 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-081 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-2
- **Blocked by:** inference_belief_state_v4:INF-1 [open]
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-081
Title: Inferred state must not collapse to perceived observation (invariant)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-2
Claims: INV-078
Blocked by: inference_belief_state_v4:INF-1 [open]
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-082 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-1 [open]; inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-082
Title: Belief-state hypothesis set (top-k latent-state hypotheses with precision)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-3
Claims: MECH-385
Blocked by: inference_belief_state_v4:INF-1 [open]; inference_belief_state_v4:INF-2 [open]
Why now: Plan gap blocked on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-084 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-084
Title: Safety-route inference (infer route to safety from partial map/cue/gradient)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-5
Claims: MECH-387
Blocked by: inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
Why now: Plan gap blocked on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-087 -- Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-1
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-087
Title: Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_affect_adaptor_v6:LAA-1
Claims: MECH-373, INV-003
Why now: Plan gap blocked on language_affect_adaptor_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_affect_adaptor_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-088 -- Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-2
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]
- **Why now:** Plan gap open on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-088
Title: Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_affect_adaptor_v6:LAA-2
Claims: INV-085
Blocked by: language_affect_adaptor_v6:LAA-1 [blocked]
Why now: Plan gap open on language_affect_adaptor_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_affect_adaptor_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-089 -- The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-3
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-089
Title: The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_affect_adaptor_v6:LAA-3
Claims: MECH-373
Blocked by: language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
Why now: Plan gap blocked on language_affect_adaptor_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_affect_adaptor_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-093 -- Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-2
- **Blocked by:** language_emergence_bootstrap_v6:LANG-1 [open]
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-093
Title: Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-2
Claims: ARC-099
Blocked by: language_emergence_bootstrap_v6:LANG-1 [open]
Why now: Plan gap open on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-094 -- Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-3
- **Blocked by:** language_emergence_bootstrap_v6:LANG-2 [open]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-094
Title: Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-3
Claims: MECH-014
Blocked by: language_emergence_bootstrap_v6:LANG-2 [open]
Why now: Plan gap blocked on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-095 -- Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-4
- **Blocked by:** language_emergence_bootstrap_v6:LANG-3 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-095
Title: Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-4
Claims: MECH-010, ARC-099
Blocked by: language_emergence_bootstrap_v6:LANG-3 [blocked]
Why now: Plan gap blocked on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-100 -- Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-2
- **Blocked by:** language_trust_deception_institutions_v6:LTI-1 [open]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-100
Title: Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-2
Claims: MECH-015
Blocked by: language_trust_deception_institutions_v6:LTI-1 [open]
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-101 -- Deception detection / honest-signal pressure (deception = modelling another model)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-3
- **Blocked by:** language_trust_deception_institutions_v6:LTI-1 [open]; language_trust_deception_institutions_v6:LTI-2 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-101
Title: Deception detection / honest-signal pressure (deception = modelling another model)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-3
Claims: MECH-015
Blocked by: language_trust_deception_institutions_v6:LTI-1 [open]; language_trust_deception_institutions_v6:LTI-2 [blocked]
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-104 -- Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-1
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-104
Title: Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-1
Claims: ARC-047, INV-043
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-105 -- Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-2
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-105
Title: Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-2
Claims: INV-043, MECH-158, INV-082
Blocked by: loveability_ethical_agency_v5:LOVE-1 [blocked]
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-106 -- Live unethical affordance: harmful action representable as a chooseable possibility (not absent)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-3
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-106
Title: Live unethical affordance: harmful action representable as a chooseable possibility (not absent)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-3
Claims: INV-083
Blocked by: loveability_ethical_agency_v5:LOVE-1 [blocked]
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-107 -- Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-4
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-107
Title: Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-4
Claims: MECH-413
Blocked by: loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-109 -- Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-6
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-109
Title: Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-6
Claims: INV-043, MECH-158, INV-084
Blocked by: loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-119 -- Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-1
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-119
Title: Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-1
Claims: MECH-031, MECH-032
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-120 -- Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-2
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-1 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-120
Title: Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-2
Claims: ARC-010
Blocked by: mirror_modelling_other_self_v5:MIRROR-1 [blocked]
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-121 -- Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-3
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-121
Title: Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-3
Claims: ARC-010, MECH-051
Blocked by: mirror_modelling_other_self_v5:MIRROR-2 [blocked]
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-122 -- Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-4
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-122
Title: Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-4
Claims: MECH-036, INV-005
Blocked by: mirror_modelling_other_self_v5:MIRROR-3 [blocked]
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-126 -- Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-1
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-126
Title: Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-1
Claims: INV-028, ARC-047
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-127 -- Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-2
- **Blocked by:** multi_agent_ecology_v5:MAE-1 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-127
Title: Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-2
Claims: INV-028, INV-005
Blocked by: multi_agent_ecology_v5:MAE-1 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-134 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-134
Title: PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-2
Claims: SD-045
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-138 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-138
Title: PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-6
Claims: MECH-299, MECH-300
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-141 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_representation_v4:OBJ-2
- **Blocked by:** object_representation_v4:OBJ-1 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-141
Title: PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_representation_v4:OBJ-2
Claims: ARC-080, ARC-006, MECH-045
Blocked by: object_representation_v4:OBJ-1 [open]
Why now: Plan gap open on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-147 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-147
Title: PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-2
Claims: MECH-372, ARC-019
Blocked by: perceptual_adaptors_v4:PA-1 [open]
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-150 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-150
Title: PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-5
Claims: Q-065, MECH-103, MECH-396
Blocked by: perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
Why now: Plan gap blocked on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-155 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Blocked by:** plasticity_neuromodulation_v4:PLW-2 [open]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-155
Title: PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-3
Claims: MECH-398
Blocked by: plasticity_neuromodulation_v4:PLW-2 [open]
Why now: Plan gap blocked on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-158 -- Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-1
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-158
Title: Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): relational_harm_moral_semantics_v5:RHM-1
Claims: MECH-129
Why now: Plan gap blocked on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-161 -- Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-4
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-161
Title: Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): relational_harm_moral_semantics_v5:RHM-4
Claims: MECH-164
Blocked by: relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
Why now: Plan gap blocked on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-172 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-2
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-172
Title: Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-2
Claims: SD-030
Blocked by: self_model_v4:SELF-1 [open]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-173 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-3
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-173
Title: z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-3
Claims: MECH-215, ARC-081
Blocked by: self_model_v4:SELF-1 [open]
Why now: Plan gap open on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-009 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-009
Title: Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): affect_expression_v4:AE-2
Claims: ARC-088
Why now: Plan gap in_progress on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-031 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460b/461b/463b/464b/466b/467b/468b (Phase 4/5 *b cohort -- 7 members, NOT the 9-member range '460b..468b' implies; 462b/465b were NEVER scoped (MECH-267 rule-binding + MECH-094 intrusive-sim behavioural arms deferred per sd033_governance Phase 4/5 deliverables -- do not hunt for them as missing); MECH-342 ecological = V3-EXQ-629)
- **Why now:** LIVE BLOCKER (2026-06-10): GAP-4 is gated on the scaffolded_sd054_onboarding goal-achievement/foraging-competence ceiling delivering RUNTIME GOAL COMPLETIONS -- still FALSE today (V3-EXQ-603m FAIL 2026-06-10T13:38Z; 603n full-curriculum-rea

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-031
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-460b/461b/463b/464b/466b/467b/468b (Phase 4/5 *b cohort -- 7 members, NOT the 9-member range '460b..468b' implies; 462b/465b were NEVER scoped (MECH-267 rule-binding + MECH-094 intrusive-sim behavioural arms deferred per sd033_governance Phase 4/5 deliverables -- do not hunt for them as missing); MECH-342 ecological = V3-EXQ-629)
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342
Why now: LIVE BLOCKER (2026-06-10): GAP-4 is gated on the scaffolded_sd054_onboarding goal-achievement/foraging-competence ceiling delivering RUNTIME GOAL COMPLETIONS -- still FALSE today (V3-EXQ-603m FAIL 2026-06-10T13:38Z; 603n full-curriculum-rea

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-063 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** open | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514l
- **Why now:** RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-063
Title: SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)
Lane: experiment | Skill: /queue-experiment
Status: open
Gap(s): goal_pipeline:GAP-2
Owner EXQ: V3-EXQ-514l
Claims: SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030
Why now: RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavio

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-178 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-178
Title: SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A
Lane: experiment | Skill: /queue-experiment
Status: upstream_blocked
Gap(s): sleep_substrate:GAP-2
Owner EXQ: V3-EXQ-265a
Claims: SD-017, ARC-045, MECH-166
Why now: Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/sleep_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-204 -- Proposal EXP-0137 (MECH-183)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-204
Title: Proposal EXP-0137 (MECH-183)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-183
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-205 -- Proposal EXP-0138 (MECH-329)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-205
Title: Proposal EXP-0138 (MECH-329)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-329
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-206 -- Proposal EXP-0145 (INV-048)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-206
Title: Proposal EXP-0145 (INV-048)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-048
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-207 -- Proposal EXP-0150 (MECH-025b)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-207
Title: Proposal EXP-0150 (MECH-025b)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-025b
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-208 -- Proposal EXP-0151 (MECH-044)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-208
Title: Proposal EXP-0151 (MECH-044)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-044
Why now: lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-033 -- V3 reduced form -- MECH-384 self-narration trace surface (the seed the ladder compresses)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** developmental_dmn_v4:DMN-1
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-033
Title: V3 reduced form -- MECH-384 self-narration trace surface (the seed the ladder compresses)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): developmental_dmn_v4:DMN-1
Claims: MECH-384, Q-068
Why now: Plan gap open on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-050 -- Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** ethics_as_coherence_v5:ETH-8
- **Why now:** Plan gap open on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-050
Title: Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): ethics_as_coherence_v5:ETH-8
Claims: ARC-097, INV-081, MECH-371
Why now: Plan gap open on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-110 -- Biology grounding completion (attachment / safe-base / repair / moral-emotion lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** loveability_ethical_agency_v5:LOVE-7
- **Why now:** Plan gap open on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-110
Title: Biology grounding completion (attachment / safe-base / repair / moral-emotion lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): loveability_ethical_agency_v5:LOVE-7
Claims: INV-043, INV-082
Why now: Plan gap open on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-152 -- Biology grounding completion (perceptual-manifold / colour-geometry / multisensory-binding lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** perceptual_adaptors_v4:PA-7
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-152
Title: Biology grounding completion (perceptual-manifold / colour-geometry / multisensory-binding lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): perceptual_adaptors_v4:PA-7
Claims: ARC-087, MECH-372, Q-065
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-163 -- Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-6
- **Why now:** Plan gap open on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-163
Title: Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): relational_harm_moral_semantics_v5:RHM-6
Claims: MECH-129, MECH-164
Why now: Plan gap open on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-004 -- Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-3
- **Blocked by:** abstract_relational_reasoning_v6:ARR-1 [open]; abstract_relational_reasoning_v6:ARR-2 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-004
Title: Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-3
Claims: MECH-420
Blocked by: abstract_relational_reasoning_v6:ARR-1 [open]; abstract_relational_reasoning_v6:ARR-2 [blocked]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-005 -- Analogy / structure-mapping across grounded domains (relational alignment, not surface match)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-4
- **Blocked by:** abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-005
Title: Analogy / structure-mapping across grounded domains (relational alignment, not surface match)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-4
Claims: MECH-421, Q-074
Blocked by: abstract_relational_reasoning_v6:ARR-3 [blocked]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-006 -- Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-5
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-006
Title: Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-5
Claims: MECH-422
Blocked by: abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-010 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-010
Title: Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-3
Claims: MECH-360
Blocked by: affect_expression_v4:AE-1 [blocked]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-011 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-011
Title: Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-4
Claims: MECH-361
Blocked by: affect_expression_v4:AE-1 [blocked]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-014 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-014
Title: Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-7
Claims: MECH-369, MECH-370, SD-045, Q-063
Blocked by: affect_expression_v4:AE-2 [in_progress]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-024 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-024
Title: Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-4
Claims: ARC-092, MECH-365
Blocked by: autobiographical_memory_v4:ABM-3 [blocked]
Why now: Plan gap open on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-025 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-025
Title: Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-5
Claims: MECH-368, Q-062
Blocked by: autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-036 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-036
Title: PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-4
Claims: MECH-380
Blocked by: developmental_dmn_v4:DMN-3 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-037 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-037
Title: PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-5
Claims: MECH-381
Blocked by: developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-043 -- Orienting/surveying drive: pre-approach active-sensing control state

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** drives_motivation_v4:DRV-4
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-043
Title: Orienting/surveying drive: pre-approach active-sensing control state
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): drives_motivation_v4:DRV-4
Claims: MECH-395
Blocked by: drives_motivation_v4:DRV-1 [open]
Why now: Plan gap blocked on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-047 -- Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-4
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-047
Title: Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-4
Claims: INV-081, ARC-098
Blocked by: ethics_as_coherence_v5:ETH-2 [blocked]
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-048 -- Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-5
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-048
Title: Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-5
Claims: MECH-164
Blocked by: ethics_as_coherence_v5:ETH-1 [blocked]
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-055 -- Residue-aware social repair: regret-residue after exploitation generates a repair-goal

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-5
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-055
Title: Residue-aware social repair: regret-residue after exploitation generates a repair-goal
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-5
Claims: MECH-407
Blocked by: fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
Why now: Plan gap blocked on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-056 -- Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-6
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-056
Title: Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-6
Claims: MECH-408, Q-073
Blocked by: fast_empathy_v5:EMP-3 [blocked]
Why now: Plan gap blocked on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-059 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-059
Title: PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-3
Claims: MECH-264
Blocked by: goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-060 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-060
Title: PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-4
Claims: MECH-265, SD-046
Blocked by: goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-061 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-061
Title: PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-5
Claims: MECH-389
Blocked by: goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-4 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-073 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-073
Title: DG-equivalent pattern separation before rollout proposal (MECH-147)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-3
Claims: MECH-147
Blocked by: hippocampal_planning_v4:HPL-1 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-074 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-074
Title: Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-4
Claims: MECH-148
Blocked by: hippocampal_planning_v4:HPL-1 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-075 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-075
Title: CA1 mismatch novelty gate on rollout injection (MECH-149)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-5
Claims: MECH-149
Blocked by: hippocampal_planning_v4:HPL-1 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-083 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-083
Title: Inferred affordance field (afford. not directly perceived; biases E3 candidates)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-4
Claims: MECH-386
Blocked by: inference_belief_state_v4:INF-3 [blocked]
Why now: Plan gap blocked on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-085 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-085
Title: Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-6
Claims: MECH-388
Blocked by: inference_belief_state_v4:INF-3 [blocked]
Why now: Plan gap blocked on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-090 -- Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-4
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-090
Title: Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_affect_adaptor_v6:LAA-4
Claims: MECH-418, MECH-031
Blocked by: language_affect_adaptor_v6:LAA-3 [blocked]
Why now: Plan gap blocked on language_affect_adaptor_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_affect_adaptor_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-091 -- Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-5
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-091
Title: Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_affect_adaptor_v6:LAA-5
Claims: MECH-373, INV-085
Blocked by: language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
Why now: Plan gap blocked on language_affect_adaptor_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_affect_adaptor_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-096 -- Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-5
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-096
Title: Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-5
Claims: ARC-063
Blocked by: language_emergence_bootstrap_v6:LANG-4 [blocked]
Why now: Plan gap blocked on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-097 -- Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-6
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-097
Title: Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-6
Claims: MECH-010, MECH-010
Blocked by: language_emergence_bootstrap_v6:LANG-4 [blocked]
Why now: Plan gap blocked on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-098 -- Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-7
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-098
Title: Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_emergence_bootstrap_v6:LANG-7
Claims: MECH-308
Blocked by: language_emergence_bootstrap_v6:LANG-4 [blocked]
Why now: Plan gap blocked on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-102 -- Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-4
- **Blocked by:** language_trust_deception_institutions_v6:LTI-1 [open]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-102
Title: Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-4
Claims: MECH-013
Blocked by: language_trust_deception_institutions_v6:LTI-1 [open]
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-103 -- Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-5
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-103
Title: Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-5
Claims: MECH-012
Blocked by: language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-108 -- Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** loveability_ethical_agency_v5:LOVE-5
- **Blocked by:** loveability_ethical_agency_v5:LOVE-4 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-108
Title: Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): loveability_ethical_agency_v5:LOVE-5
Claims: MECH-159, MECH-414
Blocked by: loveability_ethical_agency_v5:LOVE-4 [blocked]
Why now: Plan gap blocked on loveability_ethical_agency_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/loveability_ethical_agency_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-112 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Blocked by:** memory_lifecycle_v4:MEM-1 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-112
Title: Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-2
Claims: MECH-147, MECH-391
Blocked by: memory_lifecycle_v4:MEM-1 [open]
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-113 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Blocked by:** memory_lifecycle_v4:MEM-1 [open]
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-113
Title: False-linking-risk / reality-coherence cost term (the single aspect with no REE home)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-3
Claims: INV-079
Blocked by: memory_lifecycle_v4:MEM-1 [open]
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-115 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-115
Title: Provenance + contradiction-flag + rollback layer on consolidated memory
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-5
Claims: MECH-094, MECH-068, MECH-124, MECH-392
Blocked by: memory_lifecycle_v4:MEM-4 [open]
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-116 -- Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-6
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-116
Title: Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-6
Claims: MECH-257, ARC-035, MECH-393
Blocked by: memory_lifecycle_v4:MEM-4 [open]
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-123 -- Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-5
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
- **Why now:** Plan gap open on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-123
Title: Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-5
Claims: MECH-032, MECH-036, MECH-404
Blocked by: mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
Why now: Plan gap open on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-125 -- Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-7
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-125
Title: Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-7
Claims: MECH-052, MECH-127, INV-029
Blocked by: mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-128 -- Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-3
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-128
Title: Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-3
Claims: MECH-095, MECH-099
Blocked by: multi_agent_ecology_v5:MAE-2 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-129 -- Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-4
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-129
Title: Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-4
Claims: MECH-102
Blocked by: multi_agent_ecology_v5:MAE-2 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-130 -- Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-5
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-130
Title: Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-5
Claims: Q-028, MECH-402
Blocked by: multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-132 -- ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-7
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-132
Title: ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-7
Claims: ARC-010, INV-005
Blocked by: multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-135 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-135
Title: PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-3
Claims: SD-040
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-136 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-136
Title: PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-4
Claims: MECH-296, MECH-297
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-137 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-137
Title: PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-5
Claims: SD-042
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-142 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-142
Title: PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_representation_v4:OBJ-3
Claims: ARC-081
Blocked by: object_representation_v4:OBJ-2 [open]
Why now: Plan gap open on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-143 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-143
Title: PILLAR 3 -- tools/affordances object->action binding (ARC-082)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_representation_v4:OBJ-4
Claims: ARC-082
Blocked by: object_representation_v4:OBJ-2 [open]
Why now: Plan gap blocked on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-144 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-144
Title: PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_representation_v4:OBJ-5
Claims: ARC-083
Blocked by: object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
Why now: Plan gap blocked on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-148 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]; perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-148
Title: PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-3
Claims: ARC-087, MECH-372
Blocked by: perceptual_adaptors_v4:PA-1 [open]; perceptual_adaptors_v4:PA-2 [open]
Why now: Plan gap blocked on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-149 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-149
Title: Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-4
Claims: Q-065
Blocked by: perceptual_adaptors_v4:PA-3 [blocked]
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-156 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-156
Title: PILLAR B -- state-conditional plasticity-gain architectural commitment
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-4
Claims: ARC-093
Blocked by: plasticity_neuromodulation_v4:PLW-3 [blocked]
Why now: Plan gap blocked on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-157 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-157
Title: Layer-specificity adjudication (one global scalar vs per-substrate gates)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-7
Claims: Q-072
Blocked by: plasticity_neuromodulation_v4:PLW-4 [blocked]
Why now: Plan gap open on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-159 -- Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-2
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-159
Title: Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): relational_harm_moral_semantics_v5:RHM-2
Claims: MECH-130
Why now: Plan gap blocked on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-160 -- Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-3
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-160
Title: Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): relational_harm_moral_semantics_v5:RHM-3
Claims: MECH-409
Blocked by: relational_harm_moral_semantics_v5:RHM-1 [blocked]
Why now: Plan gap blocked on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-162 -- Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-5
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-4 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-162
Title: Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): relational_harm_moral_semantics_v5:RHM-5
Claims: MECH-410
Blocked by: relational_harm_moral_semantics_v5:RHM-4 [blocked]
Why now: Plan gap blocked on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-165 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [blocked_pending_substrate]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-165
Title: Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): sd_037_axis_b:P2
Claims: SD-037
Blocked by: sd_037_axis_b:P1b [blocked_pending_substrate]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-166 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-166
Title: Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): sd_037_axis_b:P3
Claims: SD-037, MECH-280, MECH-281
Blocked by: sd_037_axis_b:P2 [blocked]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-167 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-167
Title: Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): sd_037_axis_b:P4
Owner EXQ: V3-EXQ-483f
Claims: SD-037, MECH-280, MECH-281
Blocked by: sd_037_axis_b:P3 [blocked]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-168 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-168
Title: ARC-033 vs ARC-058 path arbitration (forensic 445h read)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): self_attribution:GAP-1
Owner EXQ: V3-EXQ-445h
Claims: ARC-033, ARC-058, MECH-258, MECH-260
Why now: Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-169 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-169
Title: SD-029 / MECH-256 retest under full substrate stack
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_attribution:GAP-2
Claims: SD-029, MECH-256, ARC-033, SD-013
Why now: RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-175 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-175
Title: z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-5
Claims: MECH-214
Blocked by: self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-176 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-176
Title: Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-6
Claims: MECH-214
Blocked by: self_model_v4:SELF-5 [blocked]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-177 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-177
Title: Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-7
Claims: INV-064
Blocked by: self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-016 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-016
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Owner EXQ: V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-017 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-017
Title: ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-I
Owner EXQ: V3-EXQ-606b
Claims: ARC-064, MECH-316, MECH-317, MECH-318
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-019 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-019
Title: MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-K
Owner EXQ: V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
Claims: MECH-319
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
Why now: IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-028 -- Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-A
- **Owner EXQ:** V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30; V3-EXQ-569f QUEUED 2026-06-09 (R1.b FP-2 matched-entropy action-contrastive behavioural falsifier on the 649-validated candidate_summary_source=e2_world_forward stack; supersedes 569d; ree-v3 db812e6)
- **Why now:** IN FLIGHT 2026-06-09 on V3-EXQ-569f (queued via /queue-experiment; supersedes V3-EXQ-569d). The substrate seam HAS landed and is 649-validated, so the FP-2 falsifier has resumed -- do NOT queue the dead V3-EXQ-569a (the 569a/b/c/d/e lineage

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-028
Title: Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-A
Owner EXQ: V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30; V3-EXQ-569f QUEUED 2026-06-09 (R1.b FP-2 matched-entropy action-contrastive behavioural falsifier on the 649-validated candidate_summary_source=e2_world_forward stack; supersedes 569d; ree-v3 db812e6)
Claims: ARC-065
Why now: IN FLIGHT 2026-06-09 on V3-EXQ-569f (queued via /queue-experiment; supersedes V3-EXQ-569d). The substrate seam HAS landed and is 649-validated, so the FP-2 falsifier has resumed -- do NOT queue the dead V3-EXQ-569a (the 569a/b/c/d/e lineage

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-030 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
- **Why now:** IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until 603i lands. On 603i PASS/non-vacuous readiness, queue the GAP-C successor retest; on FAIL or substrate_not_ready_requeue, route to failure-autopsy/im

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-030
Title: Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-C
Owner EXQ: V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
Claims: MECH-313, MECH-260, Q-045
Why now: IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until 603i lands. On 603i PASS/non-vacuous readiness, queue the GAP-C successor retest; on FAIL or substrate_not_ready_requeue, route to failure-autopsy/im

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-032 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485d (trained-OFC-head substrate-readiness diagnostic; the deferred trained-head arm, queued 2026-06-09; predecessors V3-EXQ-485c + V3-EXQ-485b representation-level MECH-263 functional-signature diagnostics, both PASS reviewed 2026-06-04, NOT a supersession lineage)
- **Why now:** Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_head / REEConfig.ofc_train_state_bias_head (default False -> last Linear zeroed, bit-identical OFF) + OFCAnalog.bias_head_parameters(); the SD-033b an

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-032
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485d (trained-OFC-head substrate-readiness diagnostic; the deferred trained-head arm, queued 2026-06-09; predecessors V3-EXQ-485c + V3-EXQ-485b representation-level MECH-263 functional-signature diagnostics, both PASS reviewed 2026-06-04, NOT a supersession lineage)
Claims: SD-033b, MECH-263
Why now: Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_head / REEConfig.ofc_train_state_bias_head (default False -> last Linear zeroed, bit-identical OFF) + OFCAnalog.bias_head_parameters(); the SD-033b an

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-078 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-078
Title: EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-13
Owner EXQ: V3-EXQ-590
Claims: DEV-NEED-003, MECH-314
Why now: Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-079 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-079
Title: EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-14
Owner EXQ: V3-EXQ-591
Claims: DEV-NEED-008, ARC-046
Why now: 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-118 -- Biology + source grounding completion (allocation-policy lit DONE; consolidation-faults source verify)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** memory_lifecycle_v4:MEM-8
- **Why now:** Plan gap in_progress on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-118
Title: Biology + source grounding completion (allocation-policy lit DONE; consolidation-faults source verify)
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): memory_lifecycle_v4:MEM-8
Claims: MECH-391, INV-080
Why now: Plan gap in_progress on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-139 -- Biology grounding completion for the abstraction substrates (chunking / options / type-prototype / theta-scaling lit-pul

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-8
- **Why now:** Plan gap in_progress on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-139
Title: Biology grounding completion for the abstraction substrates (chunking / options / type-prototype / theta-scaling lit-pul
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-8
Claims: SD-040, SD-045, SD-042
Why now: Plan gap in_progress on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-145 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-145
Title: Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): object_representation_v4:OBJ-6
Claims: ARC-080, ARC-006
Why now: Plan gap in_progress on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-012 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-012
Title: Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-5
Claims: MECH-355
Blocked by: affect_expression_v4:AE-2 [in_progress]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-013 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-013
Title: Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-6
Claims: MECH-364, Q-059
Blocked by: affect_expression_v4:AE-2 [in_progress]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-018 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-018
Title: MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): arc_062_rule_apprehension:GAP-J
Claims: MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: Plan gap blocked on arc_062_rule_apprehension.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-020 -- First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / 643c) re-mints its OFF baseline AND con

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arm_reuse_fingerprint:P1-auto
- **Owner EXQ:** V3-EXQ-610g (or 643c) -- pending; 610g gated on the 610f redesign successor, the IN-FLIGHT V3-EXQ-655 (NOT 656 -- see correction below)
- **Why now:** Plan gap blocked on arm_reuse_fingerprint.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-020
Title: First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / 643c) re-mints its OFF baseline AND con
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): arm_reuse_fingerprint:P1-auto
Owner EXQ: V3-EXQ-610g (or 643c) -- pending; 610g gated on the 610f redesign successor, the IN-FLIGHT V3-EXQ-655 (NOT 656 -- see correction below)
Why now: Plan gap blocked on arm_reuse_fingerprint.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arm_reuse_fingerprint_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-026 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-026
Title: Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-6
Claims: MECH-361
Blocked by: autobiographical_memory_v4:ABM-2 [blocked]
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-027 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-027
Title: Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-7
Claims: MECH-366
Blocked by: autobiographical_memory_v4:ABM-2 [blocked]
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-038 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-038
Title: Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-6
Claims: MECH-382
Blocked by: developmental_dmn_v4:DMN-2 [open]; developmental_dmn_v4:DMN-4 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-039 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-039
Title: Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-7
Claims: MECH-383
Blocked by: developmental_dmn_v4:DMN-4 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-042 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** drives_motivation_v4:DRV-3
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap open on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-042
Title: Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): drives_motivation_v4:DRV-3
Claims: MECH-394, SD-060
Blocked by: drives_motivation_v4:DRV-1 [open]
Why now: Plan gap open on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-049 -- Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** ethics_as_coherence_v5:ETH-6
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-049
Title: Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): ethics_as_coherence_v5:ETH-6
Claims: MECH-145, MECH-146
Blocked by: ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
Why now: Plan gap blocked on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-052 -- Open, extensible affect-stream taxonomy (handles, not a final ontology)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** fast_empathy_v5:EMP-2
- **Blocked by:** fast_empathy_v5:EMP-1 [open]
- **Why now:** Plan gap open on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-052
Title: Open, extensible affect-stream taxonomy (handles, not a final ontology)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-2
Claims: ARC-095
Blocked by: fast_empathy_v5:EMP-1 [open]
Why now: Plan gap open on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-062 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-062
Title: PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-6
Claims: SD-027, SD-028, MECH-254, MECH-255
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-066 -- Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-2
- **Blocked by:** grammar_primitive_mining_v6:GRAM-1 [open]
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-066
Title: Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-2
Claims: ARC-100
Blocked by: grammar_primitive_mining_v6:GRAM-1 [open]
Why now: Plan gap open on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-068 -- V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-4
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-068
Title: V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-4
Claims: MECH-416
Blocked by: grammar_primitive_mining_v6:GRAM-2 [open]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-069 -- Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-5
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-069
Title: Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-5
Claims: MECH-417
Blocked by: grammar_primitive_mining_v6:GRAM-2 [open]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-076 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-076
Title: ACh permissive write-gate on the surprise buffer (MECH-207)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-6
Claims: MECH-207
Blocked by: hippocampal_planning_v4:HPL-1 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-077 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-077
Title: Schema-primed rapid assimilation (INV-039)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): hippocampal_planning_v4:HPL-7
Claims: INV-039
Blocked by: hippocampal_planning_v4:HPL-2 [blocked]
Why now: Plan gap blocked on hippocampal_planning_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/hippocampal_planning_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-086 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** inference_belief_state_v4:INF-7
- **Blocked by:** inference_belief_state_v4:INF-1 [open]
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-086
Title: Inference failure-mode register + biology grounding (lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-7
Claims: Q-070
Blocked by: inference_belief_state_v4:INF-1 [open]
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-117 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-117
Title: Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-7
Claims: MECH-261, INV-039, INV-049, MECH-401
Blocked by: memory_lifecycle_v4:MEM-4 [open]
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-124 -- Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-6
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-124
Title: Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): mirror_modelling_other_self_v5:MIRROR-6
Claims: MECH-041
Blocked by: mirror_modelling_other_self_v5:MIRROR-2 [blocked]
Why now: Plan gap blocked on mirror_modelling_other_self_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mirror_modelling_other_self_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-131 -- Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** multi_agent_ecology_v5:MAE-6
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-131
Title: Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): multi_agent_ecology_v5:MAE-6
Claims: Q-029, MECH-403
Blocked by: multi_agent_ecology_v5:MAE-2 [blocked]
Why now: Plan gap blocked on multi_agent_ecology_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/multi_agent_ecology_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-151 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-151
Title: Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-6
Claims: MECH-372, ARC-019, MECH-397
Blocked by: perceptual_adaptors_v4:PA-1 [open]
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-154 -- Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / Sale)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** plasticity_neuromodulation_v4:PLW-2
- **Blocked by:** plasticity_neuromodulation_v4:PLW-1 [open]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-154
Title: Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / Sale)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-2
Claims: MECH-398, ARC-093
Blocked by: plasticity_neuromodulation_v4:PLW-1 [open]
Why now: Plan gap open on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-170 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-170
Title: MECH-257 dual-function 3-arm ablation re-queue
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_attribution:GAP-3
Claims: MECH-257, MECH-094
Blocked by: self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
Why now: Plan gap blocked on self_attribution.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260611-174 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_model_v4:SELF-4
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260611-174
Title: E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-4
Claims: MECH-215
Blocked by: self_model_v4:SELF-1 [open]
Why now: Plan gap open on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>
