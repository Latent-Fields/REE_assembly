# Inter-Governance Workset

Generated: `2026-06-27T09:56:31Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **201** (ready 20, in_flight 0, blocked 149)
- Pending review: **4**
- Queue pending (unclaimed): **0**

- Live EXQs: V3-EXQ-700d

- Auto-absorbed retests (queued, suppressed from workset): MECH-439 -> V3-EXQ-700d

## Work packages

### IGW-20260627-001 -- Complete governance review (4 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 4 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-001
Title: Complete governance review (4 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 4 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-176 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-176
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

### IGW-20260627-178 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-178
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

### IGW-20260627-180 -- Implement substrate: ARC-062 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-180
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

### IGW-20260627-181 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-181
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

### IGW-20260627-182 -- Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Lead lever MECH-448 is BUILT (ree-v3 main 4c9b3c9) + VALIDATED (V3-EXQ-689d PASS all 4 criteria) + PROMOTED candidate->provisional (governance-cycle-20260621T0639Z); the selection-face conversion ceil; MECH-449 [no-substrate-entry]: MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
- **Why now:** substrate_queue entry status=mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-182
Title: Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260
Blocked by: ready_blocked_by: Lead lever MECH-448 is BUILT (ree-v3 main 4c9b3c9) + VALIDATED (V3-EXQ-689d PASS all 4 criteria) + PROMOTED candidate->provisional (governance-cycle-20260621T0639Z); the selection-face conversion ceil; MECH-449 [no-substrate-entry]: MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
Why now: substrate_queue entry status=mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-187 -- Implement substrate: INF-ENV-003 (unblocks MECH-189)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-189. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-187
Title: Implement substrate: INF-ENV-003 (unblocks MECH-189)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: DEV-NEED-006, MECH-189
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-189. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-189 -- Implement substrate: SD-049 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
- **Why now:** substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-189
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

### IGW-20260627-190 -- Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3; free-text: V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
- **Why now:** substrate_queue entry status=phase_2_implemented with 2 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-190
Title: Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3; free-text: V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
Why now: substrate_queue entry status=phase_2_implemented with 2 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-192 -- Implement substrate: MECH-307 (unblocks MECH-260)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-192
Title: Implement substrate: MECH-307 (unblocks MECH-260)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: Q-040, SD-049, SD-015, MECH-111, SD-032b, ARC-030
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-193 -- Implement substrate: commitment-closure-control-plane (unblocks MECH-260)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); free-text: commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
- **Why now:** substrate_queue entry status=amend_implemented_pending_validation with 2 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-193
Title: Implement substrate: commitment-closure-control-plane (unblocks MECH-260)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-034, MECH-260, MECH-268, MECH-090, MECH-261
Blocked by: ready=false (no ready_blocked_by detail); free-text: commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
Why now: substrate_queue entry status=amend_implemented_pending_validation with 2 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-195 -- Implement substrate: SD-033 (unblocks MECH-261)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
- **Why now:** substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-195
Title: Implement substrate: SD-033 (unblocks MECH-261)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-033a, SD-033b, SD-033c, SD-033d, SD-033e, SD-034
Blocked by: ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
Why now: substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-196 -- Implement substrate: SD-033c (unblocks MECH-261)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); SD-033 [unknown]; ARC-035 [no-substrate-entry]: ARC-035; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue entry status=unknown with 7 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-196
Title: Implement substrate: SD-033c (unblocks MECH-261)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-261, MECH-264
Blocked by: ready=false (no ready_blocked_by detail); SD-033 [unknown]; ARC-035 [no-substrate-entry]: ARC-035; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235; MECH-261 [no-substrate-entry]: MECH-261
Why now: substrate_queue entry status=unknown with 7 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-046 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-046
Title: Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): developmental_dmn_v4:DMN-2
Claims: Q-068
Why now: Plan gap open on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-085 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** inference_belief_state_v4:INF-2
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-085
Title: Inferred state must not collapse to perceived observation (invariant)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): inference_belief_state_v4:INF-2
Claims: INV-078
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-096 -- Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** language_emergence_bootstrap_v6:LANG-2
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-096
Title: Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): language_emergence_bootstrap_v6:LANG-2
Claims: ARC-099
Why now: Plan gap open on language_emergence_bootstrap_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_emergence_bootstrap_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-137 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_representation_v4:OBJ-2
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-137
Title: PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): object_representation_v4:OBJ-2
Claims: ARC-080, ARC-006, MECH-045
Why now: Plan gap open on object_representation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_representation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-142 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-142
Title: PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): perceptual_adaptors_v4:PA-2
Claims: MECH-372, ARC-019
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-165 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** self_model_v4:SELF-3
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-165
Title: z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): self_model_v4:SELF-3
Claims: MECH-215, ARC-081
Why now: Plan gap open on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-172 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-172
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

### IGW-20260627-173 -- Substrate (blocked): scaffolded_sd054_onboarding

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-173
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

### IGW-20260627-175 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-175
Title: Retest after substrate: ARC-046
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-046
Blocked by: ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-177 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-177
Title: Retest after substrate: ARC-060
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-060
Blocked by: escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-179 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-179
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-062
Blocked by: ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-183 -- Retest after substrate: ARC-063

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
- **Why now:** Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-183
Title: Retest after substrate: ARC-063
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-063
Blocked by: f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
Why now: Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-184 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-184
Title: Retest after substrate: ARC-068
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-068
Blocked by: escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-185 -- Retest after substrate: MECH-102

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** not v3-testable: MECH-102 epistemic_category=substrate_conditional
- **Why now:** Held by the governance V3-pending gate (MECH-102 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-185
Title: Retest after substrate: MECH-102
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-102
Blocked by: not v3-testable: MECH-102 epistemic_category=substrate_conditional
Why now: Held by the governance V3-pending gate (MECH-102 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-186 -- Retest after substrate: MECH-189

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** INF-ENV-003 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-186
Title: Retest after substrate: MECH-189
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-189
Blocked by: INF-ENV-003 [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-188 -- Retest after substrate: MECH-229

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
- **Why now:** Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-188
Title: Retest after substrate: MECH-229
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-229
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
Why now: Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-191 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/; f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 7 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-191
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/; f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__downstream_behavioural_retests_654h_485i_445h_625e_queued_pending__decommit_release_duration_face_rung6_OPEN_460j_queued__MECH449_gonogo_governance_opponency_leg_BUILT_2026_06_21_falsifier_V3_EXQ_689g_queued__PROMOTES_NOTHING_until_scores]; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance falsifier V3-EXQ-689g (BUILT 2026-06-21 via /implement-substrate, no-op default
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 7 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-194 -- Retest after substrate: MECH-261

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-033b [implemented]; SD-033 [unknown] (transitive via SD-033b); MECH-263 [no-substrate-entry] (transitive via SD-033b): MECH-263; MECH-261 [no-substrate-entry] (transitive via SD-033b): MECH-261; SD-033c [unknown]; SD-033 [unknown] (transitive via SD-033c); ARC-035 [no-substrate-entry] (transitive via SD-033c): ARC-035; MECH-151 [no-substrate-entry] (transitive via SD-033c): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033c): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033c): MECH-235; MECH-261 [no-substrate-entry] (transitive via SD-033c): MECH-261; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
- **Why now:** Blocked by 16 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-194
Title: Retest after substrate: MECH-261
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-261
Blocked by: SD-033b [implemented]; SD-033 [unknown] (transitive via SD-033b); MECH-263 [no-substrate-entry] (transitive via SD-033b): MECH-263; MECH-261 [no-substrate-entry] (transitive via SD-033b): MECH-261; SD-033c [unknown]; SD-033 [unknown] (transitive via SD-033c); ARC-035 [no-substrate-entry] (transitive via SD-033c): ARC-035; MECH-151 [no-substrate-entry] (transitive via SD-033c): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033c): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033c): MECH-235; MECH-261 [no-substrate-entry] (transitive via SD-033c): MECH-261; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
Why now: Blocked by 16 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-015 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-654j RAN TERMINAL FAIL/non_contributory 2026-06-22T13:59Z (run_id v3_exq_654j_arc062_gapb_rule_apprehension_nogo_behavioural_falsifier_20260622T135939Z_v3; supersedes V3-EXQ-654i; claim_ids=[MECH-309, ARC-062]). CONFIRMED failure_autopsy_V3-EXQ-654j_2026-06-22 (governance-apply 2026-06-22, user-approved): pre-registered FAIL(C1 holds, C2 fails) clean substrate-ceiling -- all seven C1 readiness/non-vacuity gates met & non-degenerate, incl. C1f confirming the MECH-449 active No-Go live & suppressing (1.55) on BOTH arms -- yet the load-bearing C2 committed-class entropy lift FAILED (1/3 seeds). Both ARC-107 eligibility-governance legs (MECH-448 demotion @654i, MECH-449 Go/No-Go @654j) PASS at the selection face yet NEITHER converts to committed-class behavioural diversity: the conversion ceiling is structural and downstream of selection. Cross-substrate-corroborated by V3-EXQ-485m (OFC devaluation face -- 3rd convergent fails-C2-alone datum). Claims UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). RE-DERIVE BRAKE FIRED (18th MECH-309 / 19th ARC-062); further eligibility-governance letters refused. Factor-B next-route SUPERSEDED by V3-EXQ-689c (refuted at the selection face); corrected route = root-C rung-6 (PARKED; closure-exclusive de-commit substrate built 2026-06-22) or V4, NOT another GAP-B eligibility/commit-T letter. Status stays in-progress (GAP-B closes only on a PASS C2 lift). PROMOTES NOTHING. [HISTORY] V3-EXQ-654i RAN TERMINAL FAIL/non_contributory 2026-06-22T01:47Z (run_id v3_exq_654i_arc062_gapb_rule_apprehension_behavioural_falsifier_20260622T014706Z_v3; supersedes V3-EXQ-654h; claim_ids=[MECH-309, ARC-062]). CONFIRMED failure_autopsy_V3-EXQ-654i_2026-06-22 (governance 2026-06-22, user-approved): pre-registered FAIL(C1 holds, C2 fails) clean substrate-ceiling -- all C1 readiness/non-vacuity gates met & non-degenerate (rule field 0.913, propagation 0.027, MECH-448 demotion live excluding 18.4) but the load-bearing C2 committed-class entropy lift FAILED: the differentiated rule-apprehension bias reaches committed action but does not convert to committed-class diversity even under live demotion. Conversion ceiling persists despite demotion; NOT an ARC-062/MECH-309 falsification (claims UNWEAKENED, substrate_ceiling / pending_retest_after_substrate behind MECH-449). RE-DERIVE BRAKE FIRED (17 prior substrate_ceiling autopsies): refuse a same-substrate 654j re-queue -- the next test must engage the MECH-449 Go/No-Go active No-Go (built 2026-06-21; falsifier V3-EXQ-689g PASSED + MECH-449 PROMOTED candidate->provisional 2026-06-22). [HISTORY] V3-EXQ-654i was queued 2026-06-21 as THE GAP-B FALSIFIER PORTED ONTO THE MECH-448 (ARC-107) RANK-PRESERVING F->ELIGIBILITY DEMOTION CONVERSION, NOW WITH 485j-STYLE PER-(arm,seed) ENVELOPE-FLOOR CALIBRATION so the demotion lever genuinely EXCLUDES on the SPREAD arc_062 F pool: ports the 654g/654h GAP-B committed-class-entropy falsifier with use_f_eligibility_demotion=True armed as a matched-stack constant on BOTH arms (the f_demotion mode overrides the 569i top_k per ree-v3/ree_core/predictors/e3_selector.py), ONLY use_candidate_rule_field swept, PLUS a per-(arm,seed) f_eligibility_envelope_floor calibrated below the bank's measured max per-candidate merit-share so f_eligibility_excluded_count>0 (the fix for the 654h all-admit no-op recorded below). 654i ALSO scores a fired-but-non-converting outcome as a genuine MECH-309/ARC-062 weakens rather than another silent no-op requeue (the 654h-autopsy safeguard). A 654i PASS is the first downstream confirmation that the MECH-448 demotion lever (promoted PROVISIONAL 2026-06-21 on the V3-EXQ-689d PASS) generalises off the GAP-A foraging substrate onto the GAP-B rule-apprehension composite; a 654i PASS would also close behavioral_diversity_isolation:GAP-I. PROMOTES NOTHING until 654i runs -- MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. [HISTORY] V3-EXQ-654h RAN FAIL/non_contributory 2026-06-21T17:57Z (run_id v3_exq_654h_arc062_gapb_rule_apprehension_behavioural_falsifier_20260621T175704Z_v3; ree-cloud-3; supersedes V3-EXQ-654g; reviewed + autopsied failure_autopsy_V3-EXQ-654h_2026-06-21, status=confirmed). FIVE of six self-route gates PASSED (committed_class_axis_exercisable 1.0; GAP-A consumed_summary divergence 0.0226 > floor; rule-field differentiated+matured 0.872; propagation non-vacuity 0.0195 > 0.001) but the MECH-448 non-degeneracy gate FAILED: f_eligibility_excluded_count==0 -- the 689d-validated config (f_eligibility_envelope_floor=0.30, dn_sigma=0.0) admitted EVERY candidate because the arc_062 rule-apprehension bank yields a SPREAD/non-divergent F pool (no candidate clears the absolute 0.30 merit-share floor) -> all-admit fallback -> ARM_ON==ARM_OFF -> the F->eligibility demotion is a STRUCTURAL NO-OP, so the C2 committed-class-entropy-lift DV never ran through a genuinely-demoted selector. IDENTICAL no-op-envelope signature to V3-EXQ-485i (same MECH-448 lever, OFC bank) -- 654h is its arc_062-bank twin. The C1e non-degeneracy gate did its job (self-routed substrate_not_ready_requeue, NO false weakens). NOT a MECH-309/ARC-062 falsification. The 654i re-queue gate was CLEARED by failure_autopsy_V3-EXQ-485j (MECH-448 demotion GENERALISES off GAP-A for the discrimination/committed-diversity family that 654 tests; the one 485j signature that did NOT convert was the orthogonal devaluation/value family, pinned to a devalued-head/test-design gap -> 485k). Routed: /queue-experiment 654i (485j-style per-(arm,seed) envelope-floor calibration onto the arc_062 bank) + amend f_dominance_conversion_ceiling. 7th autopsy in the MECH-309/ARC-062 series (654/b/c/d/f/g/h); NO /claim-synthesis (the shared selector locus is already decomposed by the ARC-107 BG-selector constitution MECH-448 demotion / MECH-449 Go/No-Go). [HISTORY] V3-EXQ-654g RAN FAIL/non_contributory 2026-06-19T21:31Z (run_id v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier_20260619T213118Z_v3; ree-cloud-4; supersedes V3-EXQ-654f; reviewed /governance 2026-06-19). THE GAP-B BEHAVIOURAL LINEAGE TERMINUS: first run on the de-locked CRF stack wired to the 569i-validated top-k shortlist conversion. C1 (non-vacuity) FULLY MET on all 5 preconditions (class axis exercisable 1.0; GAP-A divergence 0.080 > 0.05; ARM_ON crf_frac_active 0.94 > 0.30; propagation non-vacuous, within-arm counterfactual delta 0.0021 nonzero -- the rule_state reaches committed action). C2 (PRIMARY committed-class entropy lift) FAILED: ARM_ON 0.6728 vs ARM_OFF 0.6614 = +0.011 nats, 0/3 seeds clear the 0.05-nat margin. Pre-registered C1-holds/C2-fails branch = non_contributory, the SHARED selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; MECH-439 F-dominance live root), NOT a MECH-309/ARC-062 falsification. SECOND independent behavioural channel after V3-EXQ-485h (OFC outcome-value bias) to corroborate MECH-439 as the live root. CRF instrumentation lineage CLEANLY TERMINATED (CRF done at 654f); residual is the F-dominance ceiling, not a 654-specific gap. Route: /implement-substrate (GAP-A gain/contrast amend); the OFC behavioural retest is sequenced behind the conversion-ceiling chain (ARC-065 569i top-k ceiling-lifted / 689a / 625e). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. PRIOR FRONTIER (now superseded) V3-EXQ-654f RAN FAIL/non_contributory 2026-06-18T00:52Z (run_id v3_exq_654f_arc062_gapb_rule_apprehension_behavioural_falsifier_20260618T005228Z_v3; ree-cloud-1; supersedes V3-EXQ-654e -- the recovery re-queue of the phantom-completed-no-manifest 654e, science unchanged; reviewed /governance 2026-06-18, non_contributory self-route, weights nothing; the CRF-gate calibration amend did not produce a contributory committed-class-entropy verdict, a 654g successor on a de-locked CRF/monostrategy substrate is owed). PRIOR FRONTIER V3-EXQ-654e QUEUED 2026-06-17 (ree-v3 main 488ec03; supersedes V3-EXQ-654d; claim_ids=[MECH-309, ARC-062]; priority 335, machine any) -- the GAP-B committed-class-entropy falsifier ported onto the CRF-GATE CALIBRATION AMEND (crf-availability-maintenance at the CRF locus, UNGATED from GAP-A; amend landed ree-v3 main 42895f6 2026-06-17). The 654d autopsy proved GAP-A de-collapse is the WRONG lever (gate-lockout independent of GAP-A); the amend's three CRF-locus levers (crf_mature_context_match_threshold=0.7 sharpen + crf_tolerance_conflict_cap=3 + crf_maintenance_couple_to_theta=True) are armed on ARM_ON so the maintained differentiated pool clears the conflict gate (contracts C20-C24 + smoke: crowded-pool frac_active 0.000->0.98). C1c crf_frac_active>=0.30 self-routing precondition RETAINED (now expected to clear; if not -> substrate_not_ready_requeue, NEVER a false weakens); conversion-ceiling off-ramp retained (C1 holds/C2 absent -> non_contributory + /implement-substrate or /claim-synthesis). AWAITING 654e RUN + REVIEW. PREDECESSOR: V3-EXQ-654d RAN FAIL/non_contributory 2026-06-16T15:27Z (ree-cloud-2; run_id v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3) -- REVIEWED + autopsied 2026-06-16 (failure_autopsy_V3-EXQ-654d_2026-06-16, status=confirmed). [QUEUED 2026-06-16T07:49Z, ree-v3 origin/main 927fe1c; supersedes V3-EXQ-654c; claim_ids=[MECH-309, ARC-062]; priority 315, machine any] -- the GAP-B falsifier ported onto the GAP-A DE-COLLAPSED substrate now that the gate cleared (V3-EXQ-684a PASS, conversion_mechanism_identified). Arms the 684a-validated ARM_STD_G2 conversion lever (modulatory_authority_normalize_basis=std + authority_gain=2.0 + use_modulatory_channel_routing + source=cand_world_summary) as a matched-stack constant on BOTH arms; only use_candidate_rule_field swept; CRF mature+maintenance+persist + trained-bias-head P1 unchanged; records crf_n_matched_last (the 654c discriminator). Pre-registered C1a/C1b/C1c/C1d preconditions each self-route substrate_not_ready_requeue (C1c crf_frac_active<0.30 routes to the CRF maintenance-theta amend, autopsy part ii -- NOT implemented in code, ready=False); three-branch map (PASS->supports; C1-holds/C2-fails->shared CONVERSION ceiling under ARM_STD_G2->non_contributory+/implement-substrate; C1-fails->substrate_not_ready_requeue); NO weakens branch. RESULT (failure_autopsy_V3-EXQ-654d_2026-06-16, confirmed): C1c FAILED again (crf_frac_active 0.0 all 3 ARM_ON seeds) -- the C1-fail branch. But 654d ARMED ARM_STD_G2 on both arms AND recorded the discriminator crf_mean_n_matched (7.08/7.29/8.70 -- the 654c-flagged instrument). LOAD-BEARING FINDING: the GAP-A conversion de-collapse is the WRONG LEVER for this gate -- ARM_STD_G2 de-collapsed the E3 selection channel (consumed_summary spread cleared the 0.05 floor 2/3 seeds) but NOT the CRF rule-match context KEY; the 16 differentiated rules (max_pairwise_dist 1.711) match 7-8/tick and ALL gate out (theta=0.15+0.25*(n_matched-1)~=1.65 >> maintenance_floor 0.45). mean_prop_counterfactual_delta=0.0 confirms the gated-out rule_state never reaches committed action. NON_CONTRIBUTORY, NO weakens -- the two CRF-locus faults the 654c autopsy named (context-key crowding + maintenance/theta calibration) remain un-amended (substrate bit-identical to 654c) and 654d proves them INDEPENDENT of the GAP-A selection conversion. ROUTE (user-confirmed): /implement-substrate AMEND crf-availability-maintenance at the CRF locus, UNGATED from GAP-A (couple maintained availability to theta(n_matched) [pure gate calibration] + de-collapse the CRF mint/match context key [distinct from the E3 channel] + keep frac_ACTIVE readiness gate); re-queue 654e on that gate, NOT on GAP-A. PREDECESSOR V3-EXQ-654c RAN FAIL/non_contributory 2026-06-15T12:38Z (run_id v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3; reviewed /governance 2026-06-15; supersedes V3-EXQ-654b; claim_ids=[MECH-309, ARC-062]) -- FAILed C1c arm_on_rule_field_differentiated_and_matured (crf_frac_active = 0.0 < 0.30) for the 4th consecutive iteration, but with an INVERTED signature confirmed by failure_autopsy_V3-EXQ-654c_2026-06-15 (status=confirmed): the 666c maintenance amend FIXED the retire-churn (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting stabilised at 12-16) so the pool now holds >=2 differentiated rules -- yet activation collapsed to exactly 0.0 because the GAP-A-collapsed e2_world_forward context (consumed_summary spread 0.0089 < 0.05) makes >=3 rules co-match, so gate_and_select theta = 0.15+0.25*(n_matched-1) >= 0.65 > maintenance_floor 0.45 and every matched rule is gated OUT. MAINTAINED != ACTIVE. C2 committed-class entropy DV never scored (C1 gates it). MECH-309/ARC-062 NOT weakened (non_contributory, substrate_ceiling, pending_retest_after_substrate). ROUTING (substrate_queue crf-availability-maintenance AMENDED + ready flipped True->False this cycle): de-collapse the CRF context key (sharpen/per-candidate-separate e2_world_forward feeding CRF mint/match, mirror GAP-A) + couple maintained availability to per-tick theta + upgrade the readiness gate to assert crf_frac_active>=0.30 (gate FIRING, not frac_maintained); re-queue the GAP-B falsifier (654d) ONLY AFTER GAP-A context de-collapse, since the CRF amend is necessary-but-not-sufficient while the shared monostrategy collapse persists. PREDECESSOR V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
- **Why now:** V3-EXQ-654h QUEUED + PENDING 2026-06-21 (pending on ree-cloud-3; supersedes V3-EXQ-654g). The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (pro

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-015
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-654j RAN TERMINAL FAIL/non_contributory 2026-06-22T13:59Z (run_id v3_exq_654j_arc062_gapb_rule_apprehension_nogo_behavioural_falsifier_20260622T135939Z_v3; supersedes V3-EXQ-654i; claim_ids=[MECH-309, ARC-062]). CONFIRMED failure_autopsy_V3-EXQ-654j_2026-06-22 (governance-apply 2026-06-22, user-approved): pre-registered FAIL(C1 holds, C2 fails) clean substrate-ceiling -- all seven C1 readiness/non-vacuity gates met & non-degenerate, incl. C1f confirming the MECH-449 active No-Go live & suppressing (1.55) on BOTH arms -- yet the load-bearing C2 committed-class entropy lift FAILED (1/3 seeds). Both ARC-107 eligibility-governance legs (MECH-448 demotion @654i, MECH-449 Go/No-Go @654j) PASS at the selection face yet NEITHER converts to committed-class behavioural diversity: the conversion ceiling is structural and downstream of selection. Cross-substrate-corroborated by V3-EXQ-485m (OFC devaluation face -- 3rd convergent fails-C2-alone datum). Claims UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). RE-DERIVE BRAKE FIRED (18th MECH-309 / 19th ARC-062); further eligibility-governance letters refused. Factor-B next-route SUPERSEDED by V3-EXQ-689c (refuted at the selection face); corrected route = root-C rung-6 (PARKED; closure-exclusive de-commit substrate built 2026-06-22) or V4, NOT another GAP-B eligibility/commit-T letter. Status stays in-progress (GAP-B closes only on a PASS C2 lift). PROMOTES NOTHING. [HISTORY] V3-EXQ-654i RAN TERMINAL FAIL/non_contributory 2026-06-22T01:47Z (run_id v3_exq_654i_arc062_gapb_rule_apprehension_behavioural_falsifier_20260622T014706Z_v3; supersedes V3-EXQ-654h; claim_ids=[MECH-309, ARC-062]). CONFIRMED failure_autopsy_V3-EXQ-654i_2026-06-22 (governance 2026-06-22, user-approved): pre-registered FAIL(C1 holds, C2 fails) clean substrate-ceiling -- all C1 readiness/non-vacuity gates met & non-degenerate (rule field 0.913, propagation 0.027, MECH-448 demotion live excluding 18.4) but the load-bearing C2 committed-class entropy lift FAILED: the differentiated rule-apprehension bias reaches committed action but does not convert to committed-class diversity even under live demotion. Conversion ceiling persists despite demotion; NOT an ARC-062/MECH-309 falsification (claims UNWEAKENED, substrate_ceiling / pending_retest_after_substrate behind MECH-449). RE-DERIVE BRAKE FIRED (17 prior substrate_ceiling autopsies): refuse a same-substrate 654j re-queue -- the next test must engage the MECH-449 Go/No-Go active No-Go (built 2026-06-21; falsifier V3-EXQ-689g PASSED + MECH-449 PROMOTED candidate->provisional 2026-06-22). [HISTORY] V3-EXQ-654i was queued 2026-06-21 as THE GAP-B FALSIFIER PORTED ONTO THE MECH-448 (ARC-107) RANK-PRESERVING F->ELIGIBILITY DEMOTION CONVERSION, NOW WITH 485j-STYLE PER-(arm,seed) ENVELOPE-FLOOR CALIBRATION so the demotion lever genuinely EXCLUDES on the SPREAD arc_062 F pool: ports the 654g/654h GAP-B committed-class-entropy falsifier with use_f_eligibility_demotion=True armed as a matched-stack constant on BOTH arms (the f_demotion mode overrides the 569i top_k per ree-v3/ree_core/predictors/e3_selector.py), ONLY use_candidate_rule_field swept, PLUS a per-(arm,seed) f_eligibility_envelope_floor calibrated below the bank's measured max per-candidate merit-share so f_eligibility_excluded_count>0 (the fix for the 654h all-admit no-op recorded below). 654i ALSO scores a fired-but-non-converting outcome as a genuine MECH-309/ARC-062 weakens rather than another silent no-op requeue (the 654h-autopsy safeguard). A 654i PASS is the first downstream confirmation that the MECH-448 demotion lever (promoted PROVISIONAL 2026-06-21 on the V3-EXQ-689d PASS) generalises off the GAP-A foraging substrate onto the GAP-B rule-apprehension composite; a 654i PASS would also close behavioral_diversity_isolation:GAP-I. PROMOTES NOTHING until 654i runs -- MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. [HISTORY] V3-EXQ-654h RAN FAIL/non_contributory 2026-06-21T17:57Z (run_id v3_exq_654h_arc062_gapb_rule_apprehension_behavioural_falsifier_20260621T175704Z_v3; ree-cloud-3; supersedes V3-EXQ-654g; reviewed + autopsied failure_autopsy_V3-EXQ-654h_2026-06-21, status=confirmed). FIVE of six self-route gates PASSED (committed_class_axis_exercisable 1.0; GAP-A consumed_summary divergence 0.0226 > floor; rule-field differentiated+matured 0.872; propagation non-vacuity 0.0195 > 0.001) but the MECH-448 non-degeneracy gate FAILED: f_eligibility_excluded_count==0 -- the 689d-validated config (f_eligibility_envelope_floor=0.30, dn_sigma=0.0) admitted EVERY candidate because the arc_062 rule-apprehension bank yields a SPREAD/non-divergent F pool (no candidate clears the absolute 0.30 merit-share floor) -> all-admit fallback -> ARM_ON==ARM_OFF -> the F->eligibility demotion is a STRUCTURAL NO-OP, so the C2 committed-class-entropy-lift DV never ran through a genuinely-demoted selector. IDENTICAL no-op-envelope signature to V3-EXQ-485i (same MECH-448 lever, OFC bank) -- 654h is its arc_062-bank twin. The C1e non-degeneracy gate did its job (self-routed substrate_not_ready_requeue, NO false weakens). NOT a MECH-309/ARC-062 falsification. The 654i re-queue gate was CLEARED by failure_autopsy_V3-EXQ-485j (MECH-448 demotion GENERALISES off GAP-A for the discrimination/committed-diversity family that 654 tests; the one 485j signature that did NOT convert was the orthogonal devaluation/value family, pinned to a devalued-head/test-design gap -> 485k). Routed: /queue-experiment 654i (485j-style per-(arm,seed) envelope-floor calibration onto the arc_062 bank) + amend f_dominance_conversion_ceiling. 7th autopsy in the MECH-309/ARC-062 series (654/b/c/d/f/g/h); NO /claim-synthesis (the shared selector locus is already decomposed by the ARC-107 BG-selector constitution MECH-448 demotion / MECH-449 Go/No-Go). [HISTORY] V3-EXQ-654g RAN FAIL/non_contributory 2026-06-19T21:31Z (run_id v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier_20260619T213118Z_v3; ree-cloud-4; supersedes V3-EXQ-654f; reviewed /governance 2026-06-19). THE GAP-B BEHAVIOURAL LINEAGE TERMINUS: first run on the de-locked CRF stack wired to the 569i-validated top-k shortlist conversion. C1 (non-vacuity) FULLY MET on all 5 preconditions (class axis exercisable 1.0; GAP-A divergence 0.080 > 0.05; ARM_ON crf_frac_active 0.94 > 0.30; propagation non-vacuous, within-arm counterfactual delta 0.0021 nonzero -- the rule_state reaches committed action). C2 (PRIMARY committed-class entropy lift) FAILED: ARM_ON 0.6728 vs ARM_OFF 0.6614 = +0.011 nats, 0/3 seeds clear the 0.05-nat margin. Pre-registered C1-holds/C2-fails branch = non_contributory, the SHARED selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; MECH-439 F-dominance live root), NOT a MECH-309/ARC-062 falsification. SECOND independent behavioural channel after V3-EXQ-485h (OFC outcome-value bias) to corroborate MECH-439 as the live root. CRF instrumentation lineage CLEANLY TERMINATED (CRF done at 654f); residual is the F-dominance ceiling, not a 654-specific gap. Route: /implement-substrate (GAP-A gain/contrast amend); the OFC behavioural retest is sequenced behind the conversion-ceiling chain (ARC-065 569i top-k ceiling-lifted / 689a / 625e). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. PRIOR FRONTIER (now superseded) V3-EXQ-654f RAN FAIL/non_contributory 2026-06-18T00:52Z (run_id v3_exq_654f_arc062_gapb_rule_apprehension_behavioural_falsifier_20260618T005228Z_v3; ree-cloud-1; supersedes V3-EXQ-654e -- the recovery re-queue of the phantom-completed-no-manifest 654e, science unchanged; reviewed /governance 2026-06-18, non_contributory self-route, weights nothing; the CRF-gate calibration amend did not produce a contributory committed-class-entropy verdict, a 654g successor on a de-locked CRF/monostrategy substrate is owed). PRIOR FRONTIER V3-EXQ-654e QUEUED 2026-06-17 (ree-v3 main 488ec03; supersedes V3-EXQ-654d; claim_ids=[MECH-309, ARC-062]; priority 335, machine any) -- the GAP-B committed-class-entropy falsifier ported onto the CRF-GATE CALIBRATION AMEND (crf-availability-maintenance at the CRF locus, UNGATED from GAP-A; amend landed ree-v3 main 42895f6 2026-06-17). The 654d autopsy proved GAP-A de-collapse is the WRONG lever (gate-lockout independent of GAP-A); the amend's three CRF-locus levers (crf_mature_context_match_threshold=0.7 sharpen + crf_tolerance_conflict_cap=3 + crf_maintenance_couple_to_theta=True) are armed on ARM_ON so the maintained differentiated pool clears the conflict gate (contracts C20-C24 + smoke: crowded-pool frac_active 0.000->0.98). C1c crf_frac_active>=0.30 self-routing precondition RETAINED (now expected to clear; if not -> substrate_not_ready_requeue, NEVER a false weakens); conversion-ceiling off-ramp retained (C1 holds/C2 absent -> non_contributory + /implement-substrate or /claim-synthesis). AWAITING 654e RUN + REVIEW. PREDECESSOR: V3-EXQ-654d RAN FAIL/non_contributory 2026-06-16T15:27Z (ree-cloud-2; run_id v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3) -- REVIEWED + autopsied 2026-06-16 (failure_autopsy_V3-EXQ-654d_2026-06-16, status=confirmed). [QUEUED 2026-06-16T07:49Z, ree-v3 origin/main 927fe1c; supersedes V3-EXQ-654c; claim_ids=[MECH-309, ARC-062]; priority 315, machine any] -- the GAP-B falsifier ported onto the GAP-A DE-COLLAPSED substrate now that the gate cleared (V3-EXQ-684a PASS, conversion_mechanism_identified). Arms the 684a-validated ARM_STD_G2 conversion lever (modulatory_authority_normalize_basis=std + authority_gain=2.0 + use_modulatory_channel_routing + source=cand_world_summary) as a matched-stack constant on BOTH arms; only use_candidate_rule_field swept; CRF mature+maintenance+persist + trained-bias-head P1 unchanged; records crf_n_matched_last (the 654c discriminator). Pre-registered C1a/C1b/C1c/C1d preconditions each self-route substrate_not_ready_requeue (C1c crf_frac_active<0.30 routes to the CRF maintenance-theta amend, autopsy part ii -- NOT implemented in code, ready=False); three-branch map (PASS->supports; C1-holds/C2-fails->shared CONVERSION ceiling under ARM_STD_G2->non_contributory+/implement-substrate; C1-fails->substrate_not_ready_requeue); NO weakens branch. RESULT (failure_autopsy_V3-EXQ-654d_2026-06-16, confirmed): C1c FAILED again (crf_frac_active 0.0 all 3 ARM_ON seeds) -- the C1-fail branch. But 654d ARMED ARM_STD_G2 on both arms AND recorded the discriminator crf_mean_n_matched (7.08/7.29/8.70 -- the 654c-flagged instrument). LOAD-BEARING FINDING: the GAP-A conversion de-collapse is the WRONG LEVER for this gate -- ARM_STD_G2 de-collapsed the E3 selection channel (consumed_summary spread cleared the 0.05 floor 2/3 seeds) but NOT the CRF rule-match context KEY; the 16 differentiated rules (max_pairwise_dist 1.711) match 7-8/tick and ALL gate out (theta=0.15+0.25*(n_matched-1)~=1.65 >> maintenance_floor 0.45). mean_prop_counterfactual_delta=0.0 confirms the gated-out rule_state never reaches committed action. NON_CONTRIBUTORY, NO weakens -- the two CRF-locus faults the 654c autopsy named (context-key crowding + maintenance/theta calibration) remain un-amended (substrate bit-identical to 654c) and 654d proves them INDEPENDENT of the GAP-A selection conversion. ROUTE (user-confirmed): /implement-substrate AMEND crf-availability-maintenance at the CRF locus, UNGATED from GAP-A (couple maintained availability to theta(n_matched) [pure gate calibration] + de-collapse the CRF mint/match context key [distinct from the E3 channel] + keep frac_ACTIVE readiness gate); re-queue 654e on that gate, NOT on GAP-A. PREDECESSOR V3-EXQ-654c RAN FAIL/non_contributory 2026-06-15T12:38Z (run_id v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3; reviewed /governance 2026-06-15; supersedes V3-EXQ-654b; claim_ids=[MECH-309, ARC-062]) -- FAILed C1c arm_on_rule_field_differentiated_and_matured (crf_frac_active = 0.0 < 0.30) for the 4th consecutive iteration, but with an INVERTED signature confirmed by failure_autopsy_V3-EXQ-654c_2026-06-15 (status=confirmed): the 666c maintenance amend FIXED the retire-churn (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting stabilised at 12-16) so the pool now holds >=2 differentiated rules -- yet activation collapsed to exactly 0.0 because the GAP-A-collapsed e2_world_forward context (consumed_summary spread 0.0089 < 0.05) makes >=3 rules co-match, so gate_and_select theta = 0.15+0.25*(n_matched-1) >= 0.65 > maintenance_floor 0.45 and every matched rule is gated OUT. MAINTAINED != ACTIVE. C2 committed-class entropy DV never scored (C1 gates it). MECH-309/ARC-062 NOT weakened (non_contributory, substrate_ceiling, pending_retest_after_substrate). ROUTING (substrate_queue crf-availability-maintenance AMENDED + ready flipped True->False this cycle): de-collapse the CRF context key (sharpen/per-candidate-separate e2_world_forward feeding CRF mint/match, mirror GAP-A) + couple maintained availability to per-tick theta + upgrade the readiness gate to assert crf_frac_active>=0.30 (gate FIRING, not frac_maintained); re-queue the GAP-B falsifier (654d) ONLY AFTER GAP-A context de-collapse, since the CRF amend is necessary-but-not-sufficient while the shared monostrategy collapse persists. PREDECESSOR V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
Claims: MECH-309, ARC-062
Why now: V3-EXQ-654h QUEUED + PENDING 2026-06-21 (pending on ree-cloud-3; supersedes V3-EXQ-654g). The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (pro

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-027 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-660b TERMINAL FAIL 2026-06-11T13:43Z is the lineage FRONTIER (reclassified non_contributory / measurement_test_design_defect at governance cycle #5; the graded-in-K falsifier is RETIRED, no 660c; NOT a weakens) -- owner_exq leads with the frontier letter as of the 2026-06-12 closure-drift reconcile (advancing 660 -> 660b, the same convention as this cycle's 514m->514n / 485e->485f advances) so the structural lineage-advanced flag clears; the STANDING GAP-B EVIDENCE is UNCHANGED = predecessor V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z for MECH-341 (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; the binary within-class preserver is established). Owner re-pointed 660b -> 660 at governance cycle #5 2026-06-11 per confirmed failure_autopsy_V3-EXQ-660b: the graded-in-pool-size ratification the 660a/660b lineage was chasing is REMOVED AS A GATE (graded-in-K over-specifies a PRESERVATION claim), not outstanding -- no 660c. RETIRED graded-falsifier lineage: V3-EXQ-660b TERMINAL FAIL/weakens 2026-06-11T13:43Z (windowed-readout redesign of 660a, supersedes 660a; both readiness gates passed yet C_GRADED 0/3 seeds, sensitivity gate cleared only marginally 0.0568 + non-monotonically) was reclassified non_contributory (measurement_test_design_defect) at cycle #5, NOT a weakens; V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
- **Why now:** MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-027
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-660b TERMINAL FAIL 2026-06-11T13:43Z is the lineage FRONTIER (reclassified non_contributory / measurement_test_design_defect at governance cycle #5; the graded-in-K falsifier is RETIRED, no 660c; NOT a weakens) -- owner_exq leads with the frontier letter as of the 2026-06-12 closure-drift reconcile (advancing 660 -> 660b, the same convention as this cycle's 514m->514n / 485e->485f advances) so the structural lineage-advanced flag clears; the STANDING GAP-B EVIDENCE is UNCHANGED = predecessor V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z for MECH-341 (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; the binary within-class preserver is established). Owner re-pointed 660b -> 660 at governance cycle #5 2026-06-11 per confirmed failure_autopsy_V3-EXQ-660b: the graded-in-pool-size ratification the 660a/660b lineage was chasing is REMOVED AS A GATE (graded-in-K over-specifies a PRESERVATION claim), not outstanding -- no 660c. RETIRED graded-falsifier lineage: V3-EXQ-660b TERMINAL FAIL/weakens 2026-06-11T13:43Z (windowed-readout redesign of 660a, supersedes 660a; both readiness gates passed yet C_GRADED 0/3 seeds, sensitivity gate cleared only marginally 0.0568 + non-monotonically) was reclassified non_contributory (measurement_test_design_defect) at cycle #5, NOT a weakens; V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
Claims: MECH-341, ARC-062, ARC-065
Why now: MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-029 -- F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-I
- **Owner EXQ:** V3-EXQ-689g -- the MECH-449 Go/No-Go conversion falsifier -- RAN PASS/supports 2026-06-21T20:55Z (run_id v3_exq_689g_mech449_go_nogo_conversion_falsifier_20260621T205542Z_v3): conversion_rate_per_seed [1.0, 1.0, 1.0] (3/3 seeds convert a previously-gated channel), 0 safety violations, specificity_pass; the active No-Go converts a channel rank-preserving demotion (MECH-448) structurally cannot. On it, governance 2026-06-22 PROMOTED MECH-449 candidate->provisional (decision_log appended). LINEAGE ADVANCED: the rung-2 demotion lever (689d) PASSED and PROMOTED MECH-448->provisional 2026-06-21; V3-EXQ-689e (channel-adaptive envelope readiness, claim-free diagnostic) RAN PASS 2026-06-21T22:42Z (adaptive floor engages across the arc_062 + OFC banks); V3-EXQ-689f (No-Go-necessity falsifier, diagnostic/non_contributory) established the demotion-insufficient regime (undesirable_admit 0.866 demotion-only vs 0.0 No-Go) -- the build trigger for MECH-449. The conversion-ceiling lift is now SELECTION-FACE established for both demotion (MECH-448) and active No-Go (MECH-449); residual = downstream BEHAVIOURAL conversion (654i/485k still substrate_ceiling/pending_retest behind MECH-449 -- the active No-Go must be exercised on the behavioural harness; re-derive brake fired). [HISTORY] V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER (queued 2026-06-20, landed ree-v3 main 8d87d4a; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py) tested the rung-2 constitutional build lever (use_f_eligibility_demotion in e3_selector.py) carried by the child build node behavioral_diversity_isolation:GAP-J; a PASS lifts MECH-439's substrate_ceiling and unblocks the held downstream retests. PREDECESSOR (SETTLED, history): V3-EXQ-689a SETTLED 2026-06-20 FAIL/non_contributory (readiness met, non_degenerate) -- the pre-registered A1B1 (gap-scaled BOTH levers) gate did NOT fire (committed-class entropy 0.387 = baseline, 0/3 strict-above the collapsed AND the gap-blind controls) -> the conflict-grade near-tie parametric family is EXHAUSTED (substrate_queue f_dominance_conversion_ceiling status). Load-bearing 2x2 dissociation: Factor B alone (A0B1 gap-scaled commit-T) converted 0.850 on 2/3 seeds, Factor A width inert (0.440), destructive A x B. MECH-439 -> substrate_ceiling / pending_retest_after_substrate (governance 7419453d1d). The falsifier front escalated to the rung-2 CONSTITUTIONAL BUILD (rank-preserving F->eligibility demotion, MECH-448 lead / MECH-449 follow-on) carried by GAP-J, and 689d is that build's falsifier. This node stays in-progress as the root-tracking parent; GAP-J owns the forward build work.
- **Why now:** CEILING LIFTED 2026-06-21 (V3-EXQ-689d PASS) -- DOWNSTREAM RETESTS NOW UNBLOCKED. The conflict-grade near-tie parametric family was exhausted by 689a (A1B1 0/3); the constitutional rung-2 build (rank-preserving F->eligibility demotion, MECH

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-029
Title: F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-I
Owner EXQ: V3-EXQ-689g -- the MECH-449 Go/No-Go conversion falsifier -- RAN PASS/supports 2026-06-21T20:55Z (run_id v3_exq_689g_mech449_go_nogo_conversion_falsifier_20260621T205542Z_v3): conversion_rate_per_seed [1.0, 1.0, 1.0] (3/3 seeds convert a previously-gated channel), 0 safety violations, specificity_pass; the active No-Go converts a channel rank-preserving demotion (MECH-448) structurally cannot. On it, governance 2026-06-22 PROMOTED MECH-449 candidate->provisional (decision_log appended). LINEAGE ADVANCED: the rung-2 demotion lever (689d) PASSED and PROMOTED MECH-448->provisional 2026-06-21; V3-EXQ-689e (channel-adaptive envelope readiness, claim-free diagnostic) RAN PASS 2026-06-21T22:42Z (adaptive floor engages across the arc_062 + OFC banks); V3-EXQ-689f (No-Go-necessity falsifier, diagnostic/non_contributory) established the demotion-insufficient regime (undesirable_admit 0.866 demotion-only vs 0.0 No-Go) -- the build trigger for MECH-449. The conversion-ceiling lift is now SELECTION-FACE established for both demotion (MECH-448) and active No-Go (MECH-449); residual = downstream BEHAVIOURAL conversion (654i/485k still substrate_ceiling/pending_retest behind MECH-449 -- the active No-Go must be exercised on the behavioural harness; re-derive brake fired). [HISTORY] V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER (queued 2026-06-20, landed ree-v3 main 8d87d4a; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py) tested the rung-2 constitutional build lever (use_f_eligibility_demotion in e3_selector.py) carried by the child build node behavioral_diversity_isolation:GAP-J; a PASS lifts MECH-439's substrate_ceiling and unblocks the held downstream retests. PREDECESSOR (SETTLED, history): V3-EXQ-689a SETTLED 2026-06-20 FAIL/non_contributory (readiness met, non_degenerate) -- the pre-registered A1B1 (gap-scaled BOTH levers) gate did NOT fire (committed-class entropy 0.387 = baseline, 0/3 strict-above the collapsed AND the gap-blind controls) -> the conflict-grade near-tie parametric family is EXHAUSTED (substrate_queue f_dominance_conversion_ceiling status). Load-bearing 2x2 dissociation: Factor B alone (A0B1 gap-scaled commit-T) converted 0.850 on 2/3 seeds, Factor A width inert (0.440), destructive A x B. MECH-439 -> substrate_ceiling / pending_retest_after_substrate (governance 7419453d1d). The falsifier front escalated to the rung-2 CONSTITUTIONAL BUILD (rank-preserving F->eligibility demotion, MECH-448 lead / MECH-449 follow-on) carried by GAP-J, and 689d is that build's falsifier. This node stays in-progress as the root-tracking parent; GAP-J owns the forward build work.
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260, Q-045, SD-037, MECH-445, MECH-446
Why now: CEILING LIFTED 2026-06-21 (V3-EXQ-689d PASS) -- DOWNSTREAM RETESTS NOW UNBLOCKED. The conflict-grade near-tie parametric family was exhausted by 689a (A1B1 0/3); the constitutional rung-2 build (rank-preserving F->eligibility demotion, MECH

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-030 -- ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-K
- **Owner EXQ:** V3-EXQ-700c (ARC-108 sec-7 learned-gating settling falsifier; brake-EXEMPT PRE-REGISTERED TERMINAL with a same-layer frozen magnitude-matched random W_lat null; claim_ids=[MECH-439, ARC-108, MECH-450]; CLAIMED/running as of 2026-06-24). Lineage V3-EXQ-700 -> 700a -> 700b -> 700c (each supersedes its predecessor; failure_autopsy_V3-EXQ-700b_2026-06-24 is the routing record). Any further null -> the loop-segregation build (ARC-110), REAPPOINTED V4->V3 2026-06-24 and GATED on V3-EXQ-704 (MECH-451); no further V3 700-lineage same-arena letters.
- **Why now:** Plan gap assembling on behavioral_diversity_isolation.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-030
Title: ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): behavioral_diversity_isolation:GAP-K
Owner EXQ: V3-EXQ-700c (ARC-108 sec-7 learned-gating settling falsifier; brake-EXEMPT PRE-REGISTERED TERMINAL with a same-layer frozen magnitude-matched random W_lat null; claim_ids=[MECH-439, ARC-108, MECH-450]; CLAIMED/running as of 2026-06-24). Lineage V3-EXQ-700 -> 700a -> 700b -> 700c (each supersedes its predecessor; failure_autopsy_V3-EXQ-700b_2026-06-24 is the routing record). Any further null -> the loop-segregation build (ARC-110), REAPPOINTED V4->V3 2026-06-24 and GATED on V3-EXQ-704 (MECH-451); no further V3 700-lineage same-arena letters.
Claims: MECH-439, ARC-108, MECH-450
Why now: Plan gap assembling on behavioral_diversity_isolation.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-031 -- Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I (falsifier front) + GAP-J (build front)]

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** biology_grounding_convergence_v4:BG-2
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-031
Title: Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I (falsifier front) + GAP-J (build front)]
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): biology_grounding_convergence_v4:BG-2
Claims: MECH-439, ARC-107, MECH-448, MECH-449
Why now: Plan gap in_progress on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-040 -- Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30
- **Gap(s):** conversion_ceiling_campaign:CAMPAIGN
- **Owner EXQ:** null -- umbrella; owned via child prong nodes
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-040
Title: Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:CAMPAIGN
Owner EXQ: null -- umbrella; owned via child prong nodes
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-041 -- Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30
- **Gap(s):** conversion_ceiling_campaign:P-comp
- **Owner EXQ:** V3-EXQ-699 (queued 2026-06-22; awaiting run)
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-041
Title: Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): conversion_ceiling_campaign:P-comp
Owner EXQ: V3-EXQ-699 (queued 2026-06-22; awaiting run)
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-042 -- Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-comm

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30
- **Gap(s):** conversion_ceiling_campaign:P2-rootC
- **Owner EXQ:** V3-EXQ-460l (SUPERSEDES 460k; RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z; confirmed failure_autopsy_V3-EXQ-460l_2026-06-23 -- substrate_not_ready_requeue, closure-coupled hold never armed; re-derive brake FIRED -> implement-substrate amend f_dominance_conversion_ceiling, REFUSE a 460m re-queue). Build the F-independent closure-coupled-hold arming substrate next; the validation re-test follows the build.
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-042
Title: Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-comm
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): conversion_ceiling_campaign:P2-rootC
Owner EXQ: V3-EXQ-460l (SUPERSEDES 460k; RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z; confirmed failure_autopsy_V3-EXQ-460l_2026-06-23 -- substrate_not_ready_requeue, closure-coupled hold never armed; re-derive brake FIRED -> implement-substrate amend f_dominance_conversion_ceiling, REFUSE a 460m re-queue). Build the F-independent closure-coupled-hold arming substrate next; the validation re-test follows the build.
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-044 -- The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30
- **Gap(s):** conversion_ceiling_campaign:FULLSTACK
- **Owner EXQ:** null -- composite, gated on child prongs
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-044
Title: The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, 
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:FULLSTACK
Owner EXQ: null -- composite, gated on child prongs
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-045 -- Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was n

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30
- **Gap(s):** conversion_ceiling_campaign:P4-learned-gating
- **Owner EXQ:** null -- mirror prong; build owned by behavioral_diversity_isolation:GAP-K (V3-EXQ-700c, TERMINAL; supersedes V3-EXQ-700 -> 700a -> 700b)
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-045
Title: Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was n
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): conversion_ceiling_campaign:P4-learned-gating
Owner EXQ: null -- mirror prong; build owned by behavioral_diversity_isolation:GAP-K (V3-EXQ-700c, TERMINAL; supersedes V3-EXQ-700 -> 700a -> 700b)
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-131 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap blocked_pending_substrate on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-131
Title: Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-1
Claims: MECH-299, MECH-300
Why now: Plan gap blocked_pending_substrate on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-157 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625e RAN TERMINAL FAIL/non_contributory 2026-06-20 (run_id v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3; reviewed; removed from queue). CONFIRMED failure_autopsy_V3-EXQ-625e_2026-06-20: the recalibrated axis-(b) MEASUREMENT threat still could not clear candidate-pool collapse -- z_harm_a remained pinned (0 crossings of 0.4), R3 conversion 1/3, R4 committed-entropy 0/3 -- because the 569i conversion PASS is ENV-CONDITIONAL and does NOT propagate to a threat-engaged candidate pool. The autopsy consolidated 625e into the MECH-439 F-dominance conversion-ceiling cluster (governance 46816d2f1a). The R3/R4 non-vacuity guards fired (self-routed substrate_not_ready_requeue, NEVER a weakens). SD-037/MECH-280/MECH-281 UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). PROMOTES NOTHING.
- **Why now:** RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-157
Title: Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): sd_037_axis_b:P1b
Owner EXQ: V3-EXQ-625e RAN TERMINAL FAIL/non_contributory 2026-06-20 (run_id v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3; reviewed; removed from queue). CONFIRMED failure_autopsy_V3-EXQ-625e_2026-06-20: the recalibrated axis-(b) MEASUREMENT threat still could not clear candidate-pool collapse -- z_harm_a remained pinned (0 crossings of 0.4), R3 conversion 1/3, R4 committed-entropy 0/3 -- because the 569i conversion PASS is ENV-CONDITIONAL and does NOT propagate to a threat-engaged candidate pool. The autopsy consolidated 625e into the MECH-439 F-dominance conversion-ceiling cluster (governance 46816d2f1a). The R3/R4 non-vacuity guards fired (self-routed substrate_not_ready_requeue, NEVER a weakens). SD-037/MECH-280/MECH-281 UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). PROMOTES NOTHING.
Claims: SD-037, MECH-281
Why now: RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-113 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-113
Title: False-linking-risk / reality-coherence cost term (the single aspect with no REE home)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): memory_lifecycle_v4:MEM-3
Claims: INV-079
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-115 -- Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35
- **Gap(s):** memory_lifecycle_v4:MEM-6
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-115
Title: Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): memory_lifecycle_v4:MEM-6
Claims: MECH-257, ARC-035, MECH-393
Why now: Plan gap open on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-174 -- Queue depth low (0 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-174
Title: Queue depth low (0 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-002 -- Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-2
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-002
Title: Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-2
Claims: MECH-419
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-006 -- Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-6
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-006
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

### IGW-20260627-007 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-007
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

### IGW-20260627-020 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-020
Title: Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): autobiographical_memory_v4:ABM-2
Claims: ARC-085
Why now: Plan gap blocked on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-021 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-021
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

### IGW-20260627-047 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-047
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

### IGW-20260627-052 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** drives_motivation_v4:DRV-2
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-052
Title: Multidrive arbitration / orchestration policy (which drive wins when several are active)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): drives_motivation_v4:DRV-2
Claims: MECH-394, MECH-435, MECH-295
Why now: Plan gap blocked on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-055 -- Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-1
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-055
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

### IGW-20260627-056 -- Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-2
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-056
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

### IGW-20260627-057 -- Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-3
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-057
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

### IGW-20260627-062 -- Stream-binding mechanism: route own motivational-affective streams across the other-model

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-3
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-062
Title: Stream-binding mechanism: route own motivational-affective streams across the other-model
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): fast_empathy_v5:EMP-3
Claims: MECH-405
Why now: Plan gap blocked on fast_empathy_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/fast_empathy_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-063 -- Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-4
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-063
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

### IGW-20260627-066 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-066
Title: PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-2
Claims: SD-033e
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-072 -- Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-3
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-072
Title: Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-3
Claims: MECH-415, ARC-063
Blocked by: grammar_primitive_mining_v6:GRAM-2 [open]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-075 -- Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-6
- **Blocked by:** grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-075
Title: Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): grammar_primitive_mining_v6:GRAM-6
Claims: ARC-101, ARC-009, INV-003
Blocked by: grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
Why now: Plan gap blocked on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-076 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-076
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

### IGW-20260627-077 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-077
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

### IGW-20260627-086 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-086
Title: Belief-state hypothesis set (top-k latent-state hypotheses with precision)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): inference_belief_state_v4:INF-3
Claims: MECH-385
Blocked by: inference_belief_state_v4:INF-2 [open]
Why now: Plan gap blocked on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-088 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-088
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

### IGW-20260627-091 -- Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-1
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-091
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

### IGW-20260627-092 -- Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-2
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]
- **Why now:** Plan gap open on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-092
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

### IGW-20260627-093 -- The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-3
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-093
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

### IGW-20260627-097 -- Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-3
- **Blocked by:** language_emergence_bootstrap_v6:LANG-2 [open]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-097
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

### IGW-20260627-098 -- Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-4
- **Blocked by:** language_emergence_bootstrap_v6:LANG-3 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-098
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

### IGW-20260627-102 -- Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-2
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-102
Title: Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-2
Claims: MECH-015
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-103 -- Deception detection / honest-signal pressure (deception = modelling another model)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-3
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-103
Title: Deception detection / honest-signal pressure (deception = modelling another model)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-3
Claims: MECH-015
Blocked by: language_trust_deception_institutions_v6:LTI-2 [blocked]
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-106 -- Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-1
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-106
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

### IGW-20260627-107 -- Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-2
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-107
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

### IGW-20260627-108 -- Live unethical affordance: harmful action representable as a chooseable possibility (not absent)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-3
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-108
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

### IGW-20260627-109 -- Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-4
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-109
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

### IGW-20260627-111 -- Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-6
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-111
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

### IGW-20260627-117 -- Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-1
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-117
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

### IGW-20260627-118 -- Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-2
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-1 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-118
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

### IGW-20260627-119 -- Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-3
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-119
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

### IGW-20260627-120 -- Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-4
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-120
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

### IGW-20260627-124 -- Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-1
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-124
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

### IGW-20260627-125 -- Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-2
- **Blocked by:** multi_agent_ecology_v5:MAE-1 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-125
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

### IGW-20260627-132 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-132
Title: PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-2
Claims: SD-045
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-136 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-136
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

### IGW-20260627-145 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-145
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

### IGW-20260627-147 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-147
Title: Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-1
Claims: INV-074, MECH-333
Why now: Plan gap blocked on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-148 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-148
Title: PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): plasticity_neuromodulation_v4:PLW-3
Claims: MECH-398
Why now: Plan gap blocked on plasticity_neuromodulation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/plasticity_neuromodulation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-151 -- Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-1
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-151
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

### IGW-20260627-154 -- Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-4
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-154
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

### IGW-20260627-164 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-2
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-164
Title: Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-2
Claims: SD-030
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-008 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-008
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

### IGW-20260627-032 -- Commitment / de-commit latch grounding L1 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** biology_grounding_convergence_v4:BG-3
- **Blocked by:** biology_grounding_convergence_v4:BG-2 [in_progress]
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-032
Title: Commitment / de-commit latch grounding L1 -> L3
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): biology_grounding_convergence_v4:BG-3
Claims: SD-034, MECH-090
Blocked by: biology_grounding_convergence_v4:BG-2 [in_progress]
Why now: Plan gap in_progress on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-037 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460l (SUPERSEDES V3-EXQ-460k; RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z on ree-cloud-4 -- the ARC-108 JOB-2 control-plane L0/L1/L2 falsifier [rho_t maintenance ramp + habenula negative-delta_t de-commit DRIVER pair, ree-v3 main c5614ab]; clean substrate_not_ready_requeue at readiness gate 3 (closure_exclusive_eval_did_not_arm_hold): ncl_hold_closure_armed_total=0 AND ncl_hold_reassert_total=0 on every arm/seed -- the closure-coupled latch-hold never armed in a real eval, INDEPENDENTLY CONFIRMING the 460k wiring diagnosis (_closure_commit_active gated on the F-driven e3._committed_trajectory). L0 also not monolithic (mean per-commit hold ~1.2 vs floor 5.0); rho_peak_max=0. The JOB-2 DRIVER pair is UNEXERCISABLE on this substrate; the habenula INPUT (JOB-1 signed-RPE delta_t) is live (n_neg_delta_ticks 834-1117) = a narrow JOB-1-RPE positive only, NOT JOB-2 control-plane evidence. CONFIRMED failure_autopsy_V3-EXQ-460l_2026-06-23 (interactive gate); re-derive brake FIRED on MECH-445/446 (5th lineage autopsy 460h..460l) -> route /implement-substrate amend f_dominance_conversion_ceiling (closure-coupled-hold arming, F-independent of the natural commit), REFUSE a 460m re-queue; see governance_2026_06_23. PROMOTES NOTHING). [HISTORICAL 460k owner record:] V3-EXQ-460k (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943; machine_affinity any; supersedes V3-EXQ-460j; the rung-6 commit/release-DURATION lever retest on the now-BUILT closure-exclusive de-commit eval substrate [closure_exclusive_decommit_eval=True on every arm, ree-v3 main e52158d]; NEW gate 2.5 closure_exclusive_eval_armed self-routes substrate_not_ready_requeue if the eval mode does not arm the closure-coupled hold; SEVEN readiness gates; claim_ids=[MECH-446 scored, MECH-445 precondition], experiment_purpose=evidence; PROMOTES NOTHING until it scores; see governance_2026_06_22 + resume_condition). [HISTORICAL 460j owner record:] V3-EXQ-460j (QUEUED + INGESTED 2026-06-21, ree-v3 main f425f89; machine_affinity ree-cloud-3; gate-3 sustained-hold redesign + no-op-default natural_commit_latch_hold lever, superseded V3-EXQ-460i; RAN terminal FAIL/non_contributory 2026-06-21T11:55Z, self-routed substrate_not_ready_requeue route_reason=off_baseline_not_sustained per governance_2026_06_21c; rung-6 lever PARKED per failure_autopsy_V3-EXQ-460j_2026-06-21, then the named dissociable closure-exclusive de-commit eval substrate was BUILT ree-v3 main e52158d -- see governance_2026_06_21b). PREDECESSOR V3-EXQ-460i RAN terminal FAIL/non_contributory 2026-06-21 (self-routed substrate_not_ready_requeue at readiness gate 3 -- lever correctly armed but the 460h sustained-hold regime did not reproduce, CO_OCCURRENCE DV never ran; confirmed failure_autopsy_V3-EXQ-460i_2026-06-21, applied governance-cycle-20260621T0639Z). [HISTORICAL 460i owner record:] V3-EXQ-460i (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5; coordinator DB + /queue/active confirmed, machine_affinity ree-cloud-3 -- the de-commit falsifier of MECH-445/446 on the rung-6 COMMIT/RELEASE-DURATION lever = graded natural-commit-occupancy release [ree_core/policy/natural_commit_urgency.py NaturalCommitUrgencyRelease, built ree-v3 main ab2c1a9 2026-06-20]; see governance_2026_06_20b + resume_condition). PREDECESSOR V3-EXQ-460h RAN terminal FAIL/non_contributory 2026-06-20 (confirmed failure_autopsy_V3-EXQ-460h_2026-06-20). [HISTORICAL 460h owner record:] V3-EXQ-460h (QUEUED 2026-06-19, ree-v3 main b46c777, supersedes V3-EXQ-460g, ingested in the coordinator DB; the refractory-INDEPENDENT commit-intent retest of the re-grained SD-034 closure cluster -- same de-commit MAGNITUDE lever + within-arm around-closure C2 occupancy-delta DV, but with non-vacuity gated on sd034_n_closure_commit_intent>0; claim_ids=[MECH-446 scored, MECH-445 precondition]). Predecessor V3-EXQ-460g RAN terminal FAIL/non_contributory 2026-06-19T18:57Z (supersedes 460f; confirmed failure_autopsy_V3-EXQ-460g_2026-06-19, applied by governance-cycle-20260619T2013Z), self-routed substrate_not_ready_requeue: the 460f-prescribed de-commit MAGNITUDE lever (committed-run-scaled Leg-B refractory) was SELF-DEFEATING -- the scaled refractory pinned at the 60-tick cap on ~530-560-step runs and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the tightened non-vacuity gate counts collapsed (sd034_n_closure_coupled_elevations 36->0 seed42, closure_coupling_nonvacuous 0/3) even though the refractory HAS authority (seed-42 within-arm occupancy 0.333->0.0, C2 PASS). 7th SD-034-lineage autopsy -> the granularity-debt WATCH ITEM fired: /claim-synthesis decomposed the coarse SD-034 closure claim (2026-06-19, applied REE_assembly master 6a35087fd6) into SD-034 narrowed umbrella + MECH-445 (closure->beta coupling engagement) + MECH-446 (de-commit-authority magnitude), both candidate/v3_pending/pending_retest_after_substrate; /implement-substrate landed the refractory-independent commit-intent amend (ree-v3 main 167b3b7) that decouples the MECH-446 magnitude lever from the MECH-445 coupling-engagement non-vacuity metric. See governance_2026_06_19b. (Lineage 460f + 468e -- the de-commit and perseveration sides of the beta-engagement amend, BOTH RAN + AUTOPSIED 2026-06-18, together confirming ONE structural property [de-commit/release fires with correct sign but sub-threshold authority magnitude] via TWO independent DVs -- detail in governance_2026_06_18/_18b; 460e in governance_2026_06_17; 460d/468d + *c cohort in governance_2026_06_13/_12b. 468f still separately owed. 462b/465b NEVER scoped -- MECH-267 + MECH-094 behavioural arms deferred per sd033_governance Phase 4/5; do not hunt for them.)
- **Why now:** Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN ter

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-037
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-460l (SUPERSEDES V3-EXQ-460k; RAN terminal FAIL/non_contributory 2026-06-22T22:17:57Z on ree-cloud-4 -- the ARC-108 JOB-2 control-plane L0/L1/L2 falsifier [rho_t maintenance ramp + habenula negative-delta_t de-commit DRIVER pair, ree-v3 main c5614ab]; clean substrate_not_ready_requeue at readiness gate 3 (closure_exclusive_eval_did_not_arm_hold): ncl_hold_closure_armed_total=0 AND ncl_hold_reassert_total=0 on every arm/seed -- the closure-coupled latch-hold never armed in a real eval, INDEPENDENTLY CONFIRMING the 460k wiring diagnosis (_closure_commit_active gated on the F-driven e3._committed_trajectory). L0 also not monolithic (mean per-commit hold ~1.2 vs floor 5.0); rho_peak_max=0. The JOB-2 DRIVER pair is UNEXERCISABLE on this substrate; the habenula INPUT (JOB-1 signed-RPE delta_t) is live (n_neg_delta_ticks 834-1117) = a narrow JOB-1-RPE positive only, NOT JOB-2 control-plane evidence. CONFIRMED failure_autopsy_V3-EXQ-460l_2026-06-23 (interactive gate); re-derive brake FIRED on MECH-445/446 (5th lineage autopsy 460h..460l) -> route /implement-substrate amend f_dominance_conversion_ceiling (closure-coupled-hold arming, F-independent of the natural commit), REFUSE a 460m re-queue; see governance_2026_06_23. PROMOTES NOTHING). [HISTORICAL 460k owner record:] V3-EXQ-460k (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943; machine_affinity any; supersedes V3-EXQ-460j; the rung-6 commit/release-DURATION lever retest on the now-BUILT closure-exclusive de-commit eval substrate [closure_exclusive_decommit_eval=True on every arm, ree-v3 main e52158d]; NEW gate 2.5 closure_exclusive_eval_armed self-routes substrate_not_ready_requeue if the eval mode does not arm the closure-coupled hold; SEVEN readiness gates; claim_ids=[MECH-446 scored, MECH-445 precondition], experiment_purpose=evidence; PROMOTES NOTHING until it scores; see governance_2026_06_22 + resume_condition). [HISTORICAL 460j owner record:] V3-EXQ-460j (QUEUED + INGESTED 2026-06-21, ree-v3 main f425f89; machine_affinity ree-cloud-3; gate-3 sustained-hold redesign + no-op-default natural_commit_latch_hold lever, superseded V3-EXQ-460i; RAN terminal FAIL/non_contributory 2026-06-21T11:55Z, self-routed substrate_not_ready_requeue route_reason=off_baseline_not_sustained per governance_2026_06_21c; rung-6 lever PARKED per failure_autopsy_V3-EXQ-460j_2026-06-21, then the named dissociable closure-exclusive de-commit eval substrate was BUILT ree-v3 main e52158d -- see governance_2026_06_21b). PREDECESSOR V3-EXQ-460i RAN terminal FAIL/non_contributory 2026-06-21 (self-routed substrate_not_ready_requeue at readiness gate 3 -- lever correctly armed but the 460h sustained-hold regime did not reproduce, CO_OCCURRENCE DV never ran; confirmed failure_autopsy_V3-EXQ-460i_2026-06-21, applied governance-cycle-20260621T0639Z). [HISTORICAL 460i owner record:] V3-EXQ-460i (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5; coordinator DB + /queue/active confirmed, machine_affinity ree-cloud-3 -- the de-commit falsifier of MECH-445/446 on the rung-6 COMMIT/RELEASE-DURATION lever = graded natural-commit-occupancy release [ree_core/policy/natural_commit_urgency.py NaturalCommitUrgencyRelease, built ree-v3 main ab2c1a9 2026-06-20]; see governance_2026_06_20b + resume_condition). PREDECESSOR V3-EXQ-460h RAN terminal FAIL/non_contributory 2026-06-20 (confirmed failure_autopsy_V3-EXQ-460h_2026-06-20). [HISTORICAL 460h owner record:] V3-EXQ-460h (QUEUED 2026-06-19, ree-v3 main b46c777, supersedes V3-EXQ-460g, ingested in the coordinator DB; the refractory-INDEPENDENT commit-intent retest of the re-grained SD-034 closure cluster -- same de-commit MAGNITUDE lever + within-arm around-closure C2 occupancy-delta DV, but with non-vacuity gated on sd034_n_closure_commit_intent>0; claim_ids=[MECH-446 scored, MECH-445 precondition]). Predecessor V3-EXQ-460g RAN terminal FAIL/non_contributory 2026-06-19T18:57Z (supersedes 460f; confirmed failure_autopsy_V3-EXQ-460g_2026-06-19, applied by governance-cycle-20260619T2013Z), self-routed substrate_not_ready_requeue: the 460f-prescribed de-commit MAGNITUDE lever (committed-run-scaled Leg-B refractory) was SELF-DEFEATING -- the scaled refractory pinned at the 60-tick cap on ~530-560-step runs and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the tightened non-vacuity gate counts collapsed (sd034_n_closure_coupled_elevations 36->0 seed42, closure_coupling_nonvacuous 0/3) even though the refractory HAS authority (seed-42 within-arm occupancy 0.333->0.0, C2 PASS). 7th SD-034-lineage autopsy -> the granularity-debt WATCH ITEM fired: /claim-synthesis decomposed the coarse SD-034 closure claim (2026-06-19, applied REE_assembly master 6a35087fd6) into SD-034 narrowed umbrella + MECH-445 (closure->beta coupling engagement) + MECH-446 (de-commit-authority magnitude), both candidate/v3_pending/pending_retest_after_substrate; /implement-substrate landed the refractory-independent commit-intent amend (ree-v3 main 167b3b7) that decouples the MECH-446 magnitude lever from the MECH-445 coupling-engagement non-vacuity metric. See governance_2026_06_19b. (Lineage 460f + 468e -- the de-commit and perseveration sides of the beta-engagement amend, BOTH RAN + AUTOPSIED 2026-06-18, together confirming ONE structural property [de-commit/release fires with correct sign but sub-threshold authority magnitude] via TWO independent DVs -- detail in governance_2026_06_18/_18b; 460e in governance_2026_06_17; 460d/468d + *c cohort in governance_2026_06_13/_12b. 468f still separately owed. 462b/465b NEVER scoped -- MECH-267 + MECH-094 behavioural arms deferred per sd033_governance Phase 4/5; do not hunt for them.)
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342
Why now: Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN ter

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-171 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-171
Title: SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A
Lane: experiment | Skill: /queue-experiment
Status: upstream_blocked
Gap(s): sleep_substrate:GAP-2
Owner EXQ: V3-EXQ-265a
Claims: SD-017, ARC-045, MECH-166
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/sleep_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-197 -- Proposal for Q-064

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-197
Title: Proposal for Q-064
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: Q-064
Proposal backlog id (stable): EVB-0310
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-198 -- Proposal for MECH-085

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-198
Title: Proposal for MECH-085
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-085
Proposal backlog id (stable): EVB-0340
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-199 -- Proposal for MECH-179

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-199
Title: Proposal for MECH-179
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-179
Proposal backlog id (stable): EVB-0102
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-200 -- Proposal for MECH-182

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-200
Title: Proposal for MECH-182
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-182
Proposal backlog id (stable): EVB-0103
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-201 -- Proposal for MECH-184

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-201
Title: Proposal for MECH-184
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-184
Proposal backlog id (stable): EVB-0104
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-033 -- Drive / incentive salience grounding L2 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** biology_grounding_convergence_v4:BG-4
- **Why now:** Plan gap open on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-033
Title: Drive / incentive salience grounding L2 -> L3
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): biology_grounding_convergence_v4:BG-4
Claims: MECH-436
Why now: Plan gap open on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-034 -- Goal / wanting layer grounding L1 -> L2

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** biology_grounding_convergence_v4:BG-5
- **Why now:** Plan gap open on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-034
Title: Goal / wanting layer grounding L1 -> L2
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): biology_grounding_convergence_v4:BG-5
Why now: Plan gap open on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-071 -- Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** grammar_primitive_mining_v6:GRAM-2
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-071
Title: Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): grammar_primitive_mining_v6:GRAM-2
Claims: ARC-100
Why now: Plan gap open on grammar_primitive_mining_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/grammar_primitive_mining_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-090 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** inference_belief_state_v4:INF-7
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-090
Title: Inference failure-mode register + biology grounding (lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): inference_belief_state_v4:INF-7
Claims: Q-070
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-146 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-146
Title: Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): perceptual_adaptors_v4:PA-6
Claims: MECH-372, ARC-019, MECH-397
Why now: Plan gap open on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-003 -- Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-3
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-003
Title: Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): abstract_relational_reasoning_v6:ARR-3
Claims: MECH-420
Blocked by: abstract_relational_reasoning_v6:ARR-2 [blocked]
Why now: Plan gap blocked on abstract_relational_reasoning_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/abstract_relational_reasoning_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-004 -- Analogy / structure-mapping across grounded domains (relational alignment, not surface match)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-4
- **Blocked by:** abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-004
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

### IGW-20260627-005 -- Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-5
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-005
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

### IGW-20260627-009 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-009
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

### IGW-20260627-010 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-010
Title: Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-4
Blocked by: affect_expression_v4:AE-1 [blocked]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-013 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]; affect_expression_v4:AE-10 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-013
Title: Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-7
Claims: MECH-370, Q-063
Blocked by: affect_expression_v4:AE-2 [in_progress]; affect_expression_v4:AE-10 [blocked]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-014 -- Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-10
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-014
Title: Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction 
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): affect_expression_v4:AE-10
Claims: MECH-369
Blocked by: affect_expression_v4:AE-2 [in_progress]
Why now: Plan gap blocked on affect_expression_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/affect_expression_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-022 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-022
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

### IGW-20260627-023 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-023
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

### IGW-20260627-048 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-048
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

### IGW-20260627-049 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-049
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

### IGW-20260627-054 -- Orienting/surveying drive: pre-approach active-sensing control state

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** drives_motivation_v4:DRV-4
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-054
Title: Orienting/surveying drive: pre-approach active-sensing control state
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): drives_motivation_v4:DRV-4
Claims: MECH-395
Why now: Plan gap blocked on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-058 -- Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-4
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-058
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

### IGW-20260627-059 -- Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-5
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-059
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

### IGW-20260627-064 -- Residue-aware social repair: regret-residue after exploitation generates a repair-goal

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-5
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-064
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

### IGW-20260627-065 -- Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-6
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-065
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

### IGW-20260627-067 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-067
Title: PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-3
Claims: MECH-264
Blocked by: goal_deliberation_v4:GDL-2 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-068 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-068
Title: PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-4
Claims: MECH-265, SD-046
Blocked by: goal_deliberation_v4:GDL-2 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-069 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-069
Title: PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_deliberation_v4:GDL-5
Claims: MECH-389
Blocked by: goal_deliberation_v4:GDL-4 [blocked]
Why now: Plan gap blocked on goal_deliberation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_deliberation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-078 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-078
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

### IGW-20260627-079 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-079
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

### IGW-20260627-080 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-080
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

### IGW-20260627-087 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-087
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

### IGW-20260627-089 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-089
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

### IGW-20260627-094 -- Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-4
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-094
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

### IGW-20260627-095 -- Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-5
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-095
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

### IGW-20260627-099 -- Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-5
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-099
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

### IGW-20260627-100 -- Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-6
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-100
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

### IGW-20260627-101 -- Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-7
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-101
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

### IGW-20260627-104 -- Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-4
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-104
Title: Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): language_trust_deception_institutions_v6:LTI-4
Claims: MECH-013
Why now: Plan gap blocked on language_trust_deception_institutions_v6.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/language_trust_deception_institutions_v6_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-105 -- Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-5
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-105
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

### IGW-20260627-110 -- Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** loveability_ethical_agency_v5:LOVE-5
- **Blocked by:** loveability_ethical_agency_v5:LOVE-4 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-110
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

### IGW-20260627-112 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-112
Title: Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-2
Claims: MECH-391
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-114 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-114
Title: Provenance + contradiction-flag + rollback layer on consolidated memory
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-5
Claims: MECH-094, MECH-068, MECH-124, MECH-392
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-121 -- Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-5
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
- **Why now:** Plan gap open on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-121
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

### IGW-20260627-123 -- Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-7
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-123
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

### IGW-20260627-126 -- Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-3
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-126
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

### IGW-20260627-127 -- Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-4
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-127
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

### IGW-20260627-128 -- Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-5
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-128
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

### IGW-20260627-130 -- ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-7
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-130
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

### IGW-20260627-133 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-133
Title: PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-3
Claims: SD-040
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-134 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-134
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

### IGW-20260627-135 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-135
Title: PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): object_reasoning_abstraction_v4:OBJ-ABS-5
Claims: SD-042
Blocked by: object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
Why now: Plan gap blocked on object_reasoning_abstraction_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/object_reasoning_abstraction_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-138 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-138
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

### IGW-20260627-139 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-139
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

### IGW-20260627-140 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-140
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

### IGW-20260627-143 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-143
Title: PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): perceptual_adaptors_v4:PA-3
Claims: ARC-087, MECH-372
Blocked by: perceptual_adaptors_v4:PA-2 [open]
Why now: Plan gap blocked on perceptual_adaptors_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/perceptual_adaptors_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-144 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-144
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

### IGW-20260627-149 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-149
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

### IGW-20260627-150 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-150
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

### IGW-20260627-152 -- Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-2
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-152
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

### IGW-20260627-153 -- Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-3
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-153
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

### IGW-20260627-155 -- Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-5
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-4 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-155
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

### IGW-20260627-158 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [assembling]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-158
Title: Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): sd_037_axis_b:P2
Claims: SD-037
Blocked by: sd_037_axis_b:P1b [assembling]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-159 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-159
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

### IGW-20260627-160 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-160
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
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-161 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-161
Title: ARC-033 vs ARC-058 path arbitration (forensic 445h read)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): self_attribution:GAP-1
Owner EXQ: V3-EXQ-445h
Claims: ARC-033, ARC-058, MECH-258, MECH-260
Why now: Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-162 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-162
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

### IGW-20260627-167 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-167
Title: z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-5
Claims: MECH-214
Blocked by: self_model_v4:SELF-3 [open]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-168 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-168
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

### IGW-20260627-169 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-169
Title: Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-7
Claims: INV-064
Blocked by: self_model_v4:SELF-3 [open]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-016 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** [H1 curiosity leg, DONE] V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg (MECH-314a promoted provisional); V3-EXQ-544/545/544a historical diagnostics. [H2 noise-floor leg, OPEN] Q-045/MECH-313/MECH-260 leg: V3-EXQ-687 RAN TERMINAL FAIL/non_contributory 2026-06-18 (the 4-arm tonic-noise ablation; CONFIRMED failure_autopsy_V3-EXQ-687_2026-06-18, self-routed substrate_not_ready_requeue -- a post-softmax temperature does not move the argmax, the non-propagation root; reviewed; removed from queue). The 687-successor (arming the 569i conversion stack + a dacc_max_suppression>0 non-vacuity precondition) is OWED but unqueued, blocked on behavioral_diversity_isolation:GAP-C; convergence candidate fix MECH-440 (NoisyNet weight-noise) decision_due 2026-07-02. GAP-B successor still owed.
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-016
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Owner EXQ: [H1 curiosity leg, DONE] V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg (MECH-314a promoted provisional); V3-EXQ-544/545/544a historical diagnostics. [H2 noise-floor leg, OPEN] Q-045/MECH-313/MECH-260 leg: V3-EXQ-687 RAN TERMINAL FAIL/non_contributory 2026-06-18 (the 4-arm tonic-noise ablation; CONFIRMED failure_autopsy_V3-EXQ-687_2026-06-18, self-routed substrate_not_ready_requeue -- a post-softmax temperature does not move the argmax, the non-propagation root; reviewed; removed from queue). The 687-successor (arming the 569i conversion stack + a dacc_max_suppression>0 non-vacuity precondition) is OWED but unqueued, blocked on behavioral_diversity_isolation:GAP-C; convergence candidate fix MECH-440 (NoisyNet weight-noise) decision_due 2026-07-02. GAP-B successor still owed.
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-017 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-017
Title: ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-I
Owner EXQ: V3-EXQ-606b
Claims: ARC-064, MECH-318
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-019 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-019
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
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-026 -- Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imaginat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** autobiographical_memory_v4:ABM-9
- **Why now:** Plan gap closed on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-026
Title: Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imaginat
Lane: plan | Skill: (plan reconcile)
Status: closed
Gap(s): autobiographical_memory_v4:ABM-9
Claims: ARC-085, MECH-365, MECH-366, MECH-368, MECH-361
Why now: Plan gap closed on autobiographical_memory_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/autobiographical_memory_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-028 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
- **Why now:** AWAITING V3-EXQ-603q RUN+REVIEW 2026-06-16 (the AUTHORITATIVE current state; see governance_2026_06_16). The Branch-B harm-pathway stabilization amend is LANDED (experiments/scaffolded_sd054_onboarding.py: decoupled encoder LR scaffold_harm

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-028
Title: Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-C
Owner EXQ: V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
Claims: MECH-313, MECH-260, Q-045
Why now: AWAITING V3-EXQ-603q RUN+REVIEW 2026-06-16 (the AUTHORITATIVE current state; see governance_2026_06_16). The Branch-B harm-pathway stabilization amend is LANDED (experiments/scaffolded_sd054_onboarding.py: decoupled encoder LR scaffold_harm

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-038 -- OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + ME

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-4-battery
- **Owner EXQ:** V3-EXQ-466e
- **Blocked by:** commitment_closure:GAP-4 [in_progress]
- **Why now:** 466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-038
Title: OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + ME
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-4-battery
Owner EXQ: V3-EXQ-466e
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-342
Blocked by: commitment_closure:GAP-4 [in_progress]
Why now: 466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which th

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-039 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485m RAN TERMINAL FAIL/non_contributory 2026-06-22T14:33Z (run_id v3_exq_485m_sd033b_devaluation_decoupled_head_behavioural_20260622T143349Z_v3; ree-cloud-4; supersedes V3-EXQ-485l; claim_ids=[SD-033b, MECH-263]). CONFIRMED failure_autopsy_V3-EXQ-485m_2026-06-22 (governance-apply 2026-06-22, user-approved): on the BUILT decoupled devaluation_bias_head (ree-v3 758956f) the 485l clamp-starvation is FIXED -- C1 devaluation behavioural shift 3/3, MECH-449 No-Go engages 2/3, devalued bias range supra-floor 3/3 (mechanism EXERCISED not falsified) -- but C1b vector-inversion 1/3 and C2 committed-class separation 1/3 still FAIL. Ruling out the magnitude artifact, the valuation face does NOT convert in isolation. 3rd convergent fails-C2-alone datum (654i demotion, 654j Go/No-Go, 485m OFC): conversion is emergent from the assembled stack, not any single selection-face lever. P3-ofc FACE-VALIDATED -> folds into conversion_ceiling_campaign:FULLSTACK co-armed arm (use_ofc_devaluation_head ON). Re-derive brake FIRED (11th); a 485n isolated valuation-face re-queue is REFUSED; next test is the co-armed full-stack arm. Status stays in-progress (GAP-8 closes only on a behavioural PASS). Claims UNWEAKENED -- SD-033b/MECH-263 stay candidate / substrate_conditional / pending_retest_after_substrate. PROMOTES NOTHING. [HISTORY] V3-EXQ-485l QUEUED 2026-06-22 (supersedes V3-EXQ-485k; ree-v3 origin/main queue, script tracked) -- the GAP-8 successor frontier, AWAITING RUN: the MECH-449-engaging corrected OFC outcome-devaluation behavioural retest. ENGAGES the now-built MECH-449 Go/No-Go eligibility constitution (built 2026-06-21; falsifier V3-EXQ-689g PASSED; MECH-449 promoted candidate->provisional 2026-06-22) to drive the active No-Go WITHDRAWAL at the devaluation comparison that demotion-alone (MECH-448, rank-preserving) structurally CANNOT express -- the root the 485e->k lineage kept re-deriving (readiness-met / DVs-vacuous). Five fixes vs 485k: use_go_nogo_constitution=True matched-constant on both arms + injected viability No-Go = active WITHDRAWAL; in-band re-rank devaluation gain (no +/-0.5 OFC clamp saturation); 485j C2 discrimination protected; scored bias-vector l2/cosine inversion DV (C1b); use_f_eligibility_adaptive_floor; PLUS per-seed readiness preconditions (>=2/3, the 485k aggregate-max / 642 same-statistic fix). claim_ids=[SD-033b, MECH-263], experiment_purpose=evidence. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate. PROMOTES NOTHING until it scores; governance applies after the run. [HISTORY] PREDECESSOR V3-EXQ-485k RAN FAIL 2026-06-21T19:25Z (supersedes V3-EXQ-485j; manifest v3_exq_485k_sd033b_demotion_devalued_rerank_behavioural_20260621T192541Z_v3) -- the prior GAP-8 successor frontier; self-routed substrate_not_ready_requeue / non_contributory / non_degenerate:false (scoring_excluded, NO governance weight). NEW SIGNATURE vs the 485e-j lineage: for the FIRST time ALL FOUR readiness/non-vacuity preconditions MET (high-threat bias range 0.423; FIX-2 devalued-state bias range 0.107 >= 0.05; head weight-delta 5.64; MECH-448 f_eligibility_excluded_count=5 > 0 -- the envelope FIRED, not all-admit) yet BOTH load-bearing behavioural DVs came out VACUOUS (C1 devaluation passed=false/non_degenerate=false; C2 discrimination passed=false/non_degenerate=false -- a REGRESSION, C2 CONVERTED in 485j; C3 silence control clean). The self-routed substrate_not_ready_requeue label is QUESTIONABLE (readiness was actually met), so this is a readiness-met / DVs-vacuous puzzle, NOT a clean substrate-not-ready -- the 'self-route is a hypothesis, not a verdict' case. FLAGGED for /failure-autopsy by governance-cycle-20260621T1919Z (user-confirmed via AskUserQuestion): diagnose why both DVs went vacuous despite readiness met, and whether FIX-1's re-ranking devalued driver regressed the 485j C2 conversion; flag the 485e->k /claim-synthesis recurrence. LEFT PENDING this cycle (no evidence stamp beyond the manifest's self-reported non_contributory). FIX 1 = re-ranking devalued-state OFC driver (inverted high-threat outcome-coupling); FIX 2 = C1 readiness retargeted to the devalued-state range. claim_ids=[SD-033b, MECH-263]. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate. [HISTORY] PREDECESSOR V3-EXQ-485j QUEUED 2026-06-21 (supersedes V3-EXQ-485i; ree-v3 main 4680c0d, coordinator-ingested; priority 410, machine_affinity any, claim_ids=[SD-033b, MECH-263], experiment_purpose=evidence) RAN FAIL 2026-06-21T18:00Z -- SPLIT result: C2 task-role discrimination CONVERTED (between-context TV 1.0 on 2/3 seeds; ARM_1 demotion-off control 0.0 all seeds) = first cross-substrate corroboration the MECH-448 demotion lever generalises off GAP-A to the OFC channel (MECH-448 untagged on this manifest); C1 devaluation below the non-vacuity floor (devalued-state bias range ~0.02; C1 precondition mis-targeted the high-threat range = the 642 same-statistic miss). Manifest self-stamped weakens OVERTURNED -> non_contributory both claims by confirmed failure_autopsy_V3-EXQ-485j_2026-06-21 + governance-cycle-20260621T1919Z (index rebuilt, SD-033b/MECH-263 genuine_exp weakens 1->0); superseded_by 485k. Re-ran the trained-OFC-head C1/C2 behavioural DVs through the real E3.select() on the MECH-448 demotion-enabled selector with the f_eligibility_envelope_floor CALIBRATED per-(arm,seed). PROMOTES NOTHING. [HISTORY] PREDECESSOR V3-EXQ-485i RAN FAIL 2026-06-21T12:42Z / self-routed substrate_not_ready_requeue / non_contributory / non_degenerate:false (scoring_excluded -- carries NO governance weight; failure_autopsy_V3-EXQ-485i_2026-06-21 status=confirmed, user-adjudicated): readiness MET (OFC bias cross-candidate range 0.368, state_bias_head weight-delta 5.39) but the MECH-448 F->eligibility demotion lever SILENTLY DID NOT ENGAGE -- f_eligibility_excluded_count==0, the 0.30 absolute merit-share floor admitted ALL 8 candidates on every seed (the OFC-isolated SD-054 reef/forage bank's SPREAD F leaves the best candidate at <30% share), so the demotion-ON test arm collapsed to the demotion-OFF arm (ARM_2==ARM_1, the F-dominance ceiling control) and C1/C2 never ran through a genuinely-demoted selector. A behavioural-harness envelope-calibration miss, NOT a SD-033b/MECH-263 weakens and NOT a MECH-439 F-variance problem. owner_exq lead repointed 485i -> 485j with the 485i/485h/485g records preserved; last_updated bumped. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate (485j PROMOTES NOTHING until it scores). PREDECESSOR V3-EXQ-485h RAN FAIL 2026-06-19T19:27Z (supersedes V3-EXQ-485g; 2nd non-vacuous trained-OFC-head test -- an even LARGER cross-candidate bias range 0.50 vs 485g 0.17, head delta 5.63, still ZERO behavioural conversion; self-stamped weakens NEUTRALIZED to non_contributory, flagged for a fresh /failure-autopsy, left PENDING -- see governance_2026_06_19b). PRIOR FRONTIER V3-EXQ-485g RAN FAIL 2026-06-19T14:54Z on ree-cloud-3 (supersedes V3-EXQ-485f; trained-OFC-head behavioural arm, claim_ids=[SD-033b, MECH-263]). Readiness MET this time (the 485f vacuity fix worked: OFC bias cross-candidate range 0.171 >= the re-aligned 0.05 DV floor; head genuinely trained, weight-delta 6.32, 120 grad updates / 3683 outcome-coupled loss terms) but the load-bearing behavioural DVs FAIL (C1 devaluation_selection_shift {0.001,0.0,0.010} << 0.05; C2 between-context TV ~0). The trained head produced real cross-candidate bias RANGE with ZERO behavioural conversion -- the MECH-439 F-dominance conversion-ceiling signature (F ~88-89% of E3 committed-selection variance, V3-EXQ-571). FLAGGED for /failure-autopsy by governance-20260619T1455Z (user-confirmed): the self-stamped weakens was NEUTRALIZED to non_contributory pending adjudication of genuine-weakens vs conversion-ceiling/substrate_ceiling; SD-033b/MECH-263 exp_conf 0.325->0.0, conflict-resolution rec auto-resolved, both stay pending_retest_after_substrate. NOT marked reviewed (stays in pending_review until the autopsy resolves). 485f marked superseded. Lineage owner advanced 485f -> 485g. PREDECESSORS: 485e (FAIL/non_contributory, autopsied 2026-06-11), 485d (substrate-readiness diagnostic), 485c/485b representation-level MECH-263 diagnostics PASS 2026-06-04 (NOT a supersession lineage).
- **Why now:** OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabl

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-039
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485m RAN TERMINAL FAIL/non_contributory 2026-06-22T14:33Z (run_id v3_exq_485m_sd033b_devaluation_decoupled_head_behavioural_20260622T143349Z_v3; ree-cloud-4; supersedes V3-EXQ-485l; claim_ids=[SD-033b, MECH-263]). CONFIRMED failure_autopsy_V3-EXQ-485m_2026-06-22 (governance-apply 2026-06-22, user-approved): on the BUILT decoupled devaluation_bias_head (ree-v3 758956f) the 485l clamp-starvation is FIXED -- C1 devaluation behavioural shift 3/3, MECH-449 No-Go engages 2/3, devalued bias range supra-floor 3/3 (mechanism EXERCISED not falsified) -- but C1b vector-inversion 1/3 and C2 committed-class separation 1/3 still FAIL. Ruling out the magnitude artifact, the valuation face does NOT convert in isolation. 3rd convergent fails-C2-alone datum (654i demotion, 654j Go/No-Go, 485m OFC): conversion is emergent from the assembled stack, not any single selection-face lever. P3-ofc FACE-VALIDATED -> folds into conversion_ceiling_campaign:FULLSTACK co-armed arm (use_ofc_devaluation_head ON). Re-derive brake FIRED (11th); a 485n isolated valuation-face re-queue is REFUSED; next test is the co-armed full-stack arm. Status stays in-progress (GAP-8 closes only on a behavioural PASS). Claims UNWEAKENED -- SD-033b/MECH-263 stay candidate / substrate_conditional / pending_retest_after_substrate. PROMOTES NOTHING. [HISTORY] V3-EXQ-485l QUEUED 2026-06-22 (supersedes V3-EXQ-485k; ree-v3 origin/main queue, script tracked) -- the GAP-8 successor frontier, AWAITING RUN: the MECH-449-engaging corrected OFC outcome-devaluation behavioural retest. ENGAGES the now-built MECH-449 Go/No-Go eligibility constitution (built 2026-06-21; falsifier V3-EXQ-689g PASSED; MECH-449 promoted candidate->provisional 2026-06-22) to drive the active No-Go WITHDRAWAL at the devaluation comparison that demotion-alone (MECH-448, rank-preserving) structurally CANNOT express -- the root the 485e->k lineage kept re-deriving (readiness-met / DVs-vacuous). Five fixes vs 485k: use_go_nogo_constitution=True matched-constant on both arms + injected viability No-Go = active WITHDRAWAL; in-band re-rank devaluation gain (no +/-0.5 OFC clamp saturation); 485j C2 discrimination protected; scored bias-vector l2/cosine inversion DV (C1b); use_f_eligibility_adaptive_floor; PLUS per-seed readiness preconditions (>=2/3, the 485k aggregate-max / 642 same-statistic fix). claim_ids=[SD-033b, MECH-263], experiment_purpose=evidence. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate. PROMOTES NOTHING until it scores; governance applies after the run. [HISTORY] PREDECESSOR V3-EXQ-485k RAN FAIL 2026-06-21T19:25Z (supersedes V3-EXQ-485j; manifest v3_exq_485k_sd033b_demotion_devalued_rerank_behavioural_20260621T192541Z_v3) -- the prior GAP-8 successor frontier; self-routed substrate_not_ready_requeue / non_contributory / non_degenerate:false (scoring_excluded, NO governance weight). NEW SIGNATURE vs the 485e-j lineage: for the FIRST time ALL FOUR readiness/non-vacuity preconditions MET (high-threat bias range 0.423; FIX-2 devalued-state bias range 0.107 >= 0.05; head weight-delta 5.64; MECH-448 f_eligibility_excluded_count=5 > 0 -- the envelope FIRED, not all-admit) yet BOTH load-bearing behavioural DVs came out VACUOUS (C1 devaluation passed=false/non_degenerate=false; C2 discrimination passed=false/non_degenerate=false -- a REGRESSION, C2 CONVERTED in 485j; C3 silence control clean). The self-routed substrate_not_ready_requeue label is QUESTIONABLE (readiness was actually met), so this is a readiness-met / DVs-vacuous puzzle, NOT a clean substrate-not-ready -- the 'self-route is a hypothesis, not a verdict' case. FLAGGED for /failure-autopsy by governance-cycle-20260621T1919Z (user-confirmed via AskUserQuestion): diagnose why both DVs went vacuous despite readiness met, and whether FIX-1's re-ranking devalued driver regressed the 485j C2 conversion; flag the 485e->k /claim-synthesis recurrence. LEFT PENDING this cycle (no evidence stamp beyond the manifest's self-reported non_contributory). FIX 1 = re-ranking devalued-state OFC driver (inverted high-threat outcome-coupling); FIX 2 = C1 readiness retargeted to the devalued-state range. claim_ids=[SD-033b, MECH-263]. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate. [HISTORY] PREDECESSOR V3-EXQ-485j QUEUED 2026-06-21 (supersedes V3-EXQ-485i; ree-v3 main 4680c0d, coordinator-ingested; priority 410, machine_affinity any, claim_ids=[SD-033b, MECH-263], experiment_purpose=evidence) RAN FAIL 2026-06-21T18:00Z -- SPLIT result: C2 task-role discrimination CONVERTED (between-context TV 1.0 on 2/3 seeds; ARM_1 demotion-off control 0.0 all seeds) = first cross-substrate corroboration the MECH-448 demotion lever generalises off GAP-A to the OFC channel (MECH-448 untagged on this manifest); C1 devaluation below the non-vacuity floor (devalued-state bias range ~0.02; C1 precondition mis-targeted the high-threat range = the 642 same-statistic miss). Manifest self-stamped weakens OVERTURNED -> non_contributory both claims by confirmed failure_autopsy_V3-EXQ-485j_2026-06-21 + governance-cycle-20260621T1919Z (index rebuilt, SD-033b/MECH-263 genuine_exp weakens 1->0); superseded_by 485k. Re-ran the trained-OFC-head C1/C2 behavioural DVs through the real E3.select() on the MECH-448 demotion-enabled selector with the f_eligibility_envelope_floor CALIBRATED per-(arm,seed). PROMOTES NOTHING. [HISTORY] PREDECESSOR V3-EXQ-485i RAN FAIL 2026-06-21T12:42Z / self-routed substrate_not_ready_requeue / non_contributory / non_degenerate:false (scoring_excluded -- carries NO governance weight; failure_autopsy_V3-EXQ-485i_2026-06-21 status=confirmed, user-adjudicated): readiness MET (OFC bias cross-candidate range 0.368, state_bias_head weight-delta 5.39) but the MECH-448 F->eligibility demotion lever SILENTLY DID NOT ENGAGE -- f_eligibility_excluded_count==0, the 0.30 absolute merit-share floor admitted ALL 8 candidates on every seed (the OFC-isolated SD-054 reef/forage bank's SPREAD F leaves the best candidate at <30% share), so the demotion-ON test arm collapsed to the demotion-OFF arm (ARM_2==ARM_1, the F-dominance ceiling control) and C1/C2 never ran through a genuinely-demoted selector. A behavioural-harness envelope-calibration miss, NOT a SD-033b/MECH-263 weakens and NOT a MECH-439 F-variance problem. owner_exq lead repointed 485i -> 485j with the 485i/485h/485g records preserved; last_updated bumped. NO claims.yaml status change -- SD-033b/MECH-263 stay candidate / substrate_ceiling / pending_retest_after_substrate (485j PROMOTES NOTHING until it scores). PREDECESSOR V3-EXQ-485h RAN FAIL 2026-06-19T19:27Z (supersedes V3-EXQ-485g; 2nd non-vacuous trained-OFC-head test -- an even LARGER cross-candidate bias range 0.50 vs 485g 0.17, head delta 5.63, still ZERO behavioural conversion; self-stamped weakens NEUTRALIZED to non_contributory, flagged for a fresh /failure-autopsy, left PENDING -- see governance_2026_06_19b). PRIOR FRONTIER V3-EXQ-485g RAN FAIL 2026-06-19T14:54Z on ree-cloud-3 (supersedes V3-EXQ-485f; trained-OFC-head behavioural arm, claim_ids=[SD-033b, MECH-263]). Readiness MET this time (the 485f vacuity fix worked: OFC bias cross-candidate range 0.171 >= the re-aligned 0.05 DV floor; head genuinely trained, weight-delta 6.32, 120 grad updates / 3683 outcome-coupled loss terms) but the load-bearing behavioural DVs FAIL (C1 devaluation_selection_shift {0.001,0.0,0.010} << 0.05; C2 between-context TV ~0). The trained head produced real cross-candidate bias RANGE with ZERO behavioural conversion -- the MECH-439 F-dominance conversion-ceiling signature (F ~88-89% of E3 committed-selection variance, V3-EXQ-571). FLAGGED for /failure-autopsy by governance-20260619T1455Z (user-confirmed): the self-stamped weakens was NEUTRALIZED to non_contributory pending adjudication of genuine-weakens vs conversion-ceiling/substrate_ceiling; SD-033b/MECH-263 exp_conf 0.325->0.0, conflict-resolution rec auto-resolved, both stay pending_retest_after_substrate. NOT marked reviewed (stays in pending_review until the autopsy resolves). 485f marked superseded. Lineage owner advanced 485f -> 485g. PREDECESSORS: 485e (FAIL/non_contributory, autopsied 2026-06-11), 485d (substrate-readiness diagnostic), 485c/485b representation-level MECH-263 diagnostics PASS 2026-06-04 (NOT a supersession lineage).
Claims: SD-033b, MECH-263
Why now: OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabl

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-043 -- Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 50
- **Gap(s):** conversion_ceiling_campaign:P3-ofc
- **Owner EXQ:** V3-EXQ-485m (RAN terminal FAIL/non_contributory 2026-06-22; OFC face FACE-VALIDATED -> composition-ready for FULLSTACK with use_ofc_devaluation_head ON)
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-043
Title: Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F
Lane: experiment | Skill: /queue-experiment
Status: assembling
Gap(s): conversion_ceiling_campaign:P3-ofc
Owner EXQ: V3-EXQ-485m (RAN terminal FAIL/non_contributory 2026-06-22; OFC face FACE-VALIDATED -> composition-ready for FULLSTACK with use_ofc_devaluation_head ON)
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-053 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** drives_motivation_v4:DRV-3
- **Why now:** Plan gap closed on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-053
Title: Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)
Lane: plan | Skill: (plan reconcile)
Status: closed
Gap(s): drives_motivation_v4:DRV-3
Claims: MECH-394, SD-060
Why now: Plan gap closed on drives_motivation_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/drives_motivation_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-061 -- Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** ethics_as_coherence_v5:ETH-8
- **Why now:** Plan gap closed on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-061
Title: Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-
Lane: plan | Skill: (plan reconcile)
Status: closed
Gap(s): ethics_as_coherence_v5:ETH-8
Claims: ARC-097, INV-081, MECH-371
Why now: Plan gap closed on ethics_as_coherence_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ethics_as_coherence_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-083 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-705b
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-083
Title: EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): infant_substrate:GAP-13
Owner EXQ: V3-EXQ-705b
Claims: DEV-NEED-003, MECH-314
Why now: Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-084 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-084
Title: EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-14
Owner EXQ: V3-EXQ-591
Claims: DEV-NEED-008, ARC-046
Why now: 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-141 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-141
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

### IGW-20260627-156 -- Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-6
- **Why now:** Plan gap closed on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-156
Title: Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: closed
Gap(s): relational_harm_moral_semantics_v5:RHM-6
Claims: MECH-129, MECH-164
Why now: Plan gap closed on relational_harm_moral_semantics_v5.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/relational_harm_moral_semantics_v5_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-166 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** self_model_v4:SELF-4
- **Owner EXQ:** V4-EXQ-001
- **Why now:** AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-166
Title: E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): self_model_v4:SELF-4
Owner EXQ: V4-EXQ-001
Claims: MECH-215
Why now: AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-170 -- Own-future-option uncertainty: does REE need an explicit self-model of its OWN future option-space (second-order uncerta

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50
- **Gap(s):** self_model_v4:SELF-9
- **Why now:** Plan gap assembling on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-170
Title: Own-future-option uncertainty: does REE need an explicit self-model of its OWN future option-space (second-order uncerta
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): self_model_v4:SELF-9
Why now: Plan gap assembling on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-011 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-011
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

### IGW-20260627-012 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-012
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

### IGW-20260627-018 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-018
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

### IGW-20260627-024 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-024
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

### IGW-20260627-025 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-025
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

### IGW-20260627-035 -- Attention (distributed precision-selection) grounding -- containment, not a module

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** biology_grounding_convergence_v4:BG-6
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-035
Title: Attention (distributed precision-selection) grounding -- containment, not a module
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): biology_grounding_convergence_v4:BG-6
Why now: Plan gap blocked on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-036 -- Ethics / commitment policy grounding (or honest 'no clean analog')

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** biology_grounding_convergence_v4:BG-7
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-036
Title: Ethics / commitment policy grounding (or honest 'no clean analog')
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): biology_grounding_convergence_v4:BG-7
Why now: Plan gap blocked on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-050 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-050
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

### IGW-20260627-051 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-051
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

### IGW-20260627-060 -- Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** ethics_as_coherence_v5:ETH-6
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-060
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

### IGW-20260627-070 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-070
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

### IGW-20260627-073 -- V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-4
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-073
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

### IGW-20260627-074 -- Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-5
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-074
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

### IGW-20260627-081 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-081
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

### IGW-20260627-082 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-082
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

### IGW-20260627-116 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-116
Title: Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): memory_lifecycle_v4:MEM-7
Claims: MECH-261, INV-039, INV-049, MECH-401
Why now: Plan gap blocked on memory_lifecycle_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/memory_lifecycle_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260627-122 -- Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-6
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-122
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

### IGW-20260627-129 -- Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** multi_agent_ecology_v5:MAE-6
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-129
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

### IGW-20260627-163 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260627-163
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
