# Inter-Governance Workset

Generated: `2026-06-10T21:05:49Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **138** (ready 20, in_flight 0, blocked 99)
- Pending review: **2**
- Queue pending (unclaimed): **1**

- Live EXQs: V3-EXQ-591c, V3-EXQ-603o, V3-EXQ-655, V3-EXQ-660a

- Auto-absorbed retests (queued, suppressed from workset): INV-074 -> V3-EXQ-655, MECH-341 -> V3-EXQ-660a, SD-059 -> V3-EXQ-603o

## Work packages

### IGW-20260610-001 -- Complete governance review (2 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 2 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-001
Title: Complete governance review (2 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 2 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-113 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-113
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

### IGW-20260610-115 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-115
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

### IGW-20260610-117 -- Implement substrate: ARC-062 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-117
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

### IGW-20260610-118 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-118
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

### IGW-20260610-120 -- Implement substrate: ARC-065 (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Q-044 three-arm ablation + Q-045 4-arm ablation pending substrate-landing of all four child substrates (MECH-313/314/318/319).; Q-043 [no-substrate-entry]: Q-043 weight calibration; Q-044 [no-substrate-entry]: Q-044 three-arm ablation; Q-045 [no-substrate-entry]: Q-045 4-arm ablation
- **Why now:** substrate_queue entry status=phase_1_implemented with 4 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-120
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

### IGW-20260610-121 -- Implement substrate: MECH-314a-Phase-2-impl (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Amend implemented 2026-06-07 (e2.world_forward novelty source); validation pending V3-EXQ-648a substrate-readiness PASS (curiosity_candidate_source='e2_world_forward' + readiness precondition re-targe
- **Why now:** substrate_queue entry status=amend_implemented_pending_validation with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-121
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

### IGW-20260610-122 -- Implement substrate: SD-056 (unblocks ARC-065)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-065. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-122
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

### IGW-20260610-125 -- Implement substrate: SD-049 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
- **Why now:** substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-125
Title: Implement substrate: SD-049 (unblocks MECH-229)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
Why now: substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-126 -- Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3
- **Why now:** substrate_queue entry status=phase_2_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-126
Title: Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3
Why now: substrate_queue entry status=phase_2_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-128 -- Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Full three-leg scaffolded-readiness run (Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds) with scaffold_train_harm_pathway ON must clear before ready=True; SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue entry status=G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-128
Title: Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-030, MECH-117, MECH-230, MECH-260, MECH-295, MECH-307
Blocked by: ready_blocked_by: Full three-leg scaffolded-readiness run (Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds) with scaffold_train_harm_pathway ON must clear before ready=True; SD-054 [candidate_v3_pending]; MECH-307 [implemented]
Why now: substrate_queue entry status=G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-129 -- Implement substrate: MECH-307 (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-129
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

### IGW-20260610-133 -- Implement substrate: SD-033 (unblocks MECH-266)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
- **Why now:** substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-266. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-133
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

### IGW-20260610-015 -- Memory-type taxonomy decision (Q-060): distinct autobiographical-event type, or a tag on episodic content?

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** autobiographical_memory_v4:ABM-1
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-015
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

### IGW-20260610-034 -- Non-terminal drive register (drives beyond hunger/thirst as first-class axes)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** drives_motivation_v4:DRV-1
- **Why now:** Plan gap open on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-034
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

### IGW-20260610-038 -- Single-slot vs multi-slot fork (the first design decision: does V4 widen GoalState to N>=2?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** goal_deliberation_v4:GDL-1
- **Why now:** Plan gap open on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-038
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

### IGW-20260610-055 -- Name + route the inference layer (V3 architecture note, no substrate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** inference_belief_state_v4:INF-1
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-055
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

### IGW-20260610-062 -- Allocation-gate decision stage on MECH-261 (integrate / partial_overlap / separate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** memory_lifecycle_v4:MEM-1
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-062
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

### IGW-20260610-065 -- Raw-episode-preservation invariant (consolidation_output MUST NOT replace source_episode_evidence)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** memory_lifecycle_v4:MEM-4
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-065
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

### IGW-20260610-070 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap open on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-070
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

### IGW-20260610-077 -- Type-vs-token-vs-anchor representational fork (the first design decision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_representation_v4:OBJ-1
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-077
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

### IGW-20260610-083 -- Smell-vs-sight adaptor-depth fork (the first design decision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** perceptual_adaptors_v4:PA-1
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-083
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

### IGW-20260610-090 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-090
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

### IGW-20260610-102 -- z_self promoted from body-state latent to a stateful self-model (DR-13 temporal depth)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** self_model_v4:SELF-1
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-102
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

### IGW-20260610-110 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-110
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

### IGW-20260610-112 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-112
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

### IGW-20260610-114 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-114
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

### IGW-20260610-116 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-116
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-062
Blocked by: ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-119 -- Retest after substrate: ARC-065

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-065 [phase_1_implemented]; Q-043 [no-substrate-entry] (transitive via ARC-065): Q-043 weight calibration; Q-044 [no-substrate-entry] (transitive via ARC-065): Q-044 three-arm ablation; Q-045 [no-substrate-entry] (transitive via ARC-065): Q-045 4-arm ablation; MECH-314a-Phase-2-impl [amend_implemented_pending_validation]; SD-056 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 6 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-119
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

### IGW-20260610-123 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-123
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

### IGW-20260610-124 -- Retest after substrate: MECH-229

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-124
Title: Retest after substrate: MECH-229
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-229
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-127 -- Retest after substrate: MECH-230

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-127
Title: Retest after substrate: MECH-230
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-230
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-130 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-130
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-131 -- Retest after substrate: MECH-262

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-131
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

### IGW-20260610-132 -- Retest after substrate: MECH-266

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-132
Title: Retest after substrate: MECH-266
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-266
Blocked by: SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). On 603n PASS flip ready=true.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-009 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
- **Why now:** BOTH routed steps are now DONE (see governance_2026_06_09_amend_and_requeue): the crf_persist amend LANDED (ree-v3 9797e84) and V3-EXQ-654a is QUEUED (priority 250, machine any). RESUME when V3-EXQ-654a RUNS + lands a manifest + is reviewed

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-009
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
Claims: MECH-309, ARC-062
Why now: BOTH routed steps are now DONE (see governance_2026_06_09_amend_and_requeue): the crf_persist amend LANDED (ree-v3 9797e84) and V3-EXQ-654a is QUEUED (priority 250, machine any). RESUME when V3-EXQ-654a RUNS + lands a manifest + is reviewed

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-023 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e). Governance folded into claims.yaml 2026-06-10 (MECH-341 supports, v3_pending HELD). Predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS
- **Why now:** PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is now load-bearing-CONFIRMED but 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-023
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e). Governance folded into claims.yaml 2026-06-10 (MECH-341 supports, v3_pending HELD). Predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS
Claims: MECH-341, ARC-062, ARC-065
Why now: PARTIAL 2026-06-10. V3-EXQ-660 has LANDED PASS/supports (2026-06-10T04:41Z) -- do NOT re-queue it; its C1+C2 branch fired and governance is folded into claims.yaml. The within-class-representative sub-axis is now load-bearing-CONFIRMED but 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-045 -- Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** goal_pipeline:GAP-7
- **Blocked by:** goal_pipeline:GAP-2 [blocked_pending_substrate]
- **Why now:** STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) in

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-045
Title: Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): goal_pipeline:GAP-7
Claims: MECH-229, MECH-230, MECH-117, ARC-030
Blocked by: goal_pipeline:GAP-2 [blocked_pending_substrate]
Why now: STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) in

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-095 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625c
- **Why now:** RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend lands and the agent generates oscillating, non-monostrategy z_harm_a under the axis-(b) env overlay. SD-037 status is unchanged: the substrate_ceilin

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-095
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

### IGW-20260610-111 -- Queue depth low (1 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-111
Title: Queue depth low (1 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-002 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-002
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

### IGW-20260610-016 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Blocked by:** autobiographical_memory_v4:ABM-1 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-016
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

### IGW-20260610-017 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-017
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

### IGW-20260610-028 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Blocked by:** developmental_dmn_v4:DMN-1 [open]
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-028
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

### IGW-20260610-029 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-029
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

### IGW-20260610-035 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** drives_motivation_v4:DRV-2
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-035
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

### IGW-20260610-039 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-039
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

### IGW-20260610-046 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-046
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

### IGW-20260610-047 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-047
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

### IGW-20260610-056 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-2
- **Blocked by:** inference_belief_state_v4:INF-1 [open]
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-056
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

### IGW-20260610-057 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-1 [open]; inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-057
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

### IGW-20260610-059 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-059
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

### IGW-20260610-071 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-071
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

### IGW-20260610-075 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-075
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

### IGW-20260610-078 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_representation_v4:OBJ-2
- **Blocked by:** object_representation_v4:OBJ-1 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-078
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

### IGW-20260610-084 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-084
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

### IGW-20260610-087 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-087
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

### IGW-20260610-092 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Blocked by:** plasticity_neuromodulation_v4:PLW-2 [open]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-092
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

### IGW-20260610-103 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-2
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-103
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

### IGW-20260610-104 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-3
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-104
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

### IGW-20260610-003 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-003
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

### IGW-20260610-025 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460b/461b/463b/464b/466b/467b/468b (Phase 4/5 *b cohort -- 7 members, NOT the 9-member range '460b..468b' implies; 462b/465b were NEVER scoped (MECH-267 rule-binding + MECH-094 intrusive-sim behavioural arms deferred per sd033_governance Phase 4/5 deliverables -- do not hunt for them as missing); MECH-342 ecological = V3-EXQ-629)
- **Why now:** LIVE BLOCKER (2026-06-10): GAP-4 is gated on the scaffolded_sd054_onboarding goal-achievement/foraging-competence ceiling delivering RUNTIME GOAL COMPLETIONS -- still FALSE today (V3-EXQ-603m FAIL 2026-06-10T13:38Z; 603n full-curriculum-rea

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-025
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

### IGW-20260610-044 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514l
- **Why now:** RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-044
Title: SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
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

### IGW-20260610-109 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-109
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

### IGW-20260610-134 -- Proposal EXP-0136 (MECH-183)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-134
Title: Proposal EXP-0136 (MECH-183)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-183
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-135 -- Proposal EXP-0137 (MECH-329)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-135
Title: Proposal EXP-0137 (MECH-329)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-329
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-136 -- Proposal EXP-0144 (INV-048)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-136
Title: Proposal EXP-0144 (INV-048)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-048
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-137 -- Proposal EXP-0145 (MECH-025b)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-137
Title: Proposal EXP-0145 (MECH-025b)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-025b
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-138 -- Proposal EXP-0150 (MECH-044)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-138
Title: Proposal EXP-0150 (MECH-044)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-044
Why now: lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-027 -- V3 reduced form -- MECH-384 self-narration trace surface (the seed the ladder compresses)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** developmental_dmn_v4:DMN-1
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-027
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

### IGW-20260610-089 -- Biology grounding completion (perceptual-manifold / colour-geometry / multisensory-binding lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** perceptual_adaptors_v4:PA-7
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-089
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

### IGW-20260610-004 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-004
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

### IGW-20260610-005 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-005
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

### IGW-20260610-008 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-008
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

### IGW-20260610-018 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-018
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

### IGW-20260610-019 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-019
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

### IGW-20260610-030 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-030
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

### IGW-20260610-031 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-031
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

### IGW-20260610-037 -- Orienting/surveying drive: pre-approach active-sensing control state

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** drives_motivation_v4:DRV-4
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-037
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

### IGW-20260610-040 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-040
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

### IGW-20260610-041 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-041
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

### IGW-20260610-042 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-1 [open]; goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-042
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

### IGW-20260610-048 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-048
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

### IGW-20260610-049 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-049
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

### IGW-20260610-050 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-050
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

### IGW-20260610-058 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-058
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

### IGW-20260610-060 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-060
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

### IGW-20260610-063 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Blocked by:** memory_lifecycle_v4:MEM-1 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-063
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

### IGW-20260610-064 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Blocked by:** memory_lifecycle_v4:MEM-1 [open]
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-064
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

### IGW-20260610-066 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-066
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

### IGW-20260610-067 -- Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-6
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-067
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

### IGW-20260610-072 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-072
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

### IGW-20260610-073 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-073
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

### IGW-20260610-074 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [open]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-074
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

### IGW-20260610-079 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-079
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

### IGW-20260610-080 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-080
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

### IGW-20260610-081 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-081
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

### IGW-20260610-085 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]; perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-085
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

### IGW-20260610-086 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-086
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

### IGW-20260610-093 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-093
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

### IGW-20260610-094 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-094
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

### IGW-20260610-096 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [blocked_pending_substrate]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-096
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

### IGW-20260610-097 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-097
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

### IGW-20260610-098 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-098
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

### IGW-20260610-099 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-099
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

### IGW-20260610-100 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-100
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

### IGW-20260610-106 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-106
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

### IGW-20260610-107 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-107
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

### IGW-20260610-108 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-1 [open]; self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-108
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

### IGW-20260610-010 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-010
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

### IGW-20260610-011 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-011
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

### IGW-20260610-013 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-013
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

### IGW-20260610-022 -- Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-A
- **Owner EXQ:** V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30; V3-EXQ-569f QUEUED 2026-06-09 (R1.b FP-2 matched-entropy action-contrastive behavioural falsifier on the 649-validated candidate_summary_source=e2_world_forward stack; supersedes 569d; ree-v3 db812e6)
- **Why now:** IN FLIGHT 2026-06-09 on V3-EXQ-569f (queued via /queue-experiment; supersedes V3-EXQ-569d). The substrate seam HAS landed and is 649-validated, so the FP-2 falsifier has resumed -- do NOT queue the dead V3-EXQ-569a (the 569a/b/c/d/e lineage

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-022
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

### IGW-20260610-024 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
- **Why now:** IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until 603i lands. On 603i PASS/non-vacuous readiness, queue the GAP-C successor retest; on FAIL or substrate_not_ready_requeue, route to failure-autopsy/im

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-024
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

### IGW-20260610-026 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485d (trained-OFC-head substrate-readiness diagnostic; the deferred trained-head arm, queued 2026-06-09; predecessors V3-EXQ-485c + V3-EXQ-485b representation-level MECH-263 functional-signature diagnostics, both PASS reviewed 2026-06-04, NOT a supersession lineage)
- **Why now:** Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_head / REEConfig.ofc_train_state_bias_head (default False -> last Linear zeroed, bit-identical OFF) + OFCAnalog.bias_head_parameters(); the SD-033b an

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-026
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

### IGW-20260610-053 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-053
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

### IGW-20260610-054 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-054
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

### IGW-20260610-069 -- Biology + source grounding completion (allocation-policy lit DONE; consolidation-faults source verify)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** memory_lifecycle_v4:MEM-8
- **Why now:** Plan gap in_progress on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-069
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

### IGW-20260610-076 -- Biology grounding completion for the abstraction substrates (chunking / options / type-prototype / theta-scaling lit-pul

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-8
- **Why now:** Plan gap in_progress on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-076
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

### IGW-20260610-082 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-082
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

### IGW-20260610-006 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-006
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

### IGW-20260610-007 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-007
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

### IGW-20260610-012 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-012
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

### IGW-20260610-014 -- First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / 643c) re-mints its OFF baseline AND con

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arm_reuse_fingerprint:P1-auto
- **Owner EXQ:** V3-EXQ-610g (or 643c) -- pending; 610g gated on V3-EXQ-656
- **Why now:** Plan gap blocked on arm_reuse_fingerprint.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-014
Title: First AUTOMATED index-HIT in the wild -- next genuinely-needed iteration (610g / 643c) re-mints its OFF baseline AND con
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): arm_reuse_fingerprint:P1-auto
Owner EXQ: V3-EXQ-610g (or 643c) -- pending; 610g gated on V3-EXQ-656
Why now: Plan gap blocked on arm_reuse_fingerprint.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arm_reuse_fingerprint_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260610-020 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-020
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

### IGW-20260610-021 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-021
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

### IGW-20260610-032 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-032
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

### IGW-20260610-033 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-033
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

### IGW-20260610-036 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** drives_motivation_v4:DRV-3
- **Blocked by:** drives_motivation_v4:DRV-1 [open]
- **Why now:** Plan gap open on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-036
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

### IGW-20260610-043 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-043
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

### IGW-20260610-051 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-051
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

### IGW-20260610-052 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-052
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

### IGW-20260610-061 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** inference_belief_state_v4:INF-7
- **Blocked by:** inference_belief_state_v4:INF-1 [open]
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-061
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

### IGW-20260610-068 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Blocked by:** memory_lifecycle_v4:MEM-4 [open]
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-068
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

### IGW-20260610-088 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Blocked by:** perceptual_adaptors_v4:PA-1 [open]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-088
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

### IGW-20260610-091 -- Biology grounding lit-pull (Hensch / Bear-Singer / Froemke / Kilgard / Sale)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** plasticity_neuromodulation_v4:PLW-2
- **Blocked by:** plasticity_neuromodulation_v4:PLW-1 [open]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-091
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

### IGW-20260610-101 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-101
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

### IGW-20260610-105 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_model_v4:SELF-4
- **Blocked by:** self_model_v4:SELF-1 [open]
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260610-105
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
