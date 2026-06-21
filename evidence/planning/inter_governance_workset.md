# Inter-Governance Workset

Generated: `2026-06-21T05:17:40Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **193** (ready 20, in_flight 2, blocked 149)
- Pending review: **3**
- Queue pending (unclaimed): **1**

- Live EXQs: V3-EXQ-689d, V3-EXQ-693a, V3-EXQ-695

- Auto-absorbed retests (queued, suppressed from workset): ARC-062 -> V3-EXQ-695, MECH-263 -> V3-EXQ-696, MECH-309 -> V3-EXQ-695, SD-015 -> V3-EXQ-693a, SD-033b -> V3-EXQ-696, SD-049 -> V3-EXQ-693a

## Work packages

### IGW-20260621-001 -- Complete governance review (3 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 3 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-001
Title: Complete governance review (3 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 3 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-168 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-168
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

### IGW-20260621-170 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-170
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

### IGW-20260621-172 -- Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-063)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); free-text: rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry]: MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
- **Why now:** substrate_queue entry status=conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon with 3 unresolved prerequisite(s); blocks retest of ARC-063. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-172
Title: Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-063)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260
Blocked by: ready=false (no ready_blocked_by detail); free-text: rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry]: MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
Why now: substrate_queue entry status=conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon with 3 unresolved prerequisite(s); blocks retest of ARC-063. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-176 -- Implement substrate: INF-ENV-003 (unblocks MECH-189)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-189. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-176
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

### IGW-20260621-178 -- Implement substrate: SD-049 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
- **Why now:** substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-178
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

### IGW-20260621-179 -- Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3; free-text: V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
- **Why now:** substrate_queue entry status=phase_2_implemented with 2 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-179
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

### IGW-20260621-181 -- Implement substrate: SD-054 (unblocks MECH-260)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-181
Title: Implement substrate: SD-054 (unblocks MECH-260)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-054, MECH-309, ARC-062
Blocked by: ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
Why now: substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-182 -- Implement substrate: MECH-307 (unblocks MECH-260)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-182
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

### IGW-20260621-183 -- Implement substrate: commitment-closure-control-plane (unblocks MECH-260)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); free-text: commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
- **Why now:** substrate_queue entry status=amend_implemented_pending_validation with 2 unresolved prerequisite(s); blocks retest of MECH-260. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-183
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

### IGW-20260621-185 -- Implement substrate: SD-033 (unblocks MECH-261)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
- **Why now:** substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-185
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

### IGW-20260621-186 -- Implement substrate: SD-033c (unblocks MECH-261)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); SD-033 [unknown]; ARC-035 [no-substrate-entry]: ARC-035; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue entry status=unknown with 7 unresolved prerequisite(s); blocks retest of MECH-261. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-186
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

### IGW-20260621-188 -- Implement substrate: ARC-062 (unblocks MECH-262)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-262. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-188
Title: Implement substrate: ARC-062 (unblocks MECH-262)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-309, ARC-062, SD-033a, MECH-262, SD-029
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-262. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-039 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Why now:** Plan gap open on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-039
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

### IGW-20260621-078 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** inference_belief_state_v4:INF-2
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-078
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

### IGW-20260621-089 -- Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** language_emergence_bootstrap_v6:LANG-2
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-089
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

### IGW-20260621-130 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** object_representation_v4:OBJ-2
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-130
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

### IGW-20260621-135 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-135
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

### IGW-20260621-158 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25
- **Gap(s):** self_model_v4:SELF-3
- **Why now:** Plan gap open on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-158
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

### IGW-20260621-164 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-164
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

### IGW-20260621-165 -- Substrate (blocked): scaffolded_sd054_onboarding

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-165
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

### IGW-20260621-167 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-167
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

### IGW-20260621-169 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-169
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

### IGW-20260621-171 -- Retest after substrate: ARC-063

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** f_dominance_conversion_ceiling [conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon]; free-text (via f_dominance_conversion_ceiling): rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
- **Why now:** Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-171
Title: Retest after substrate: ARC-063
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-063
Blocked by: f_dominance_conversion_ceiling [conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon]; free-text (via f_dominance_conversion_ceiling): rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
Why now: Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-173 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-173
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

### IGW-20260621-174 -- Retest after substrate: MECH-102

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** not v3-testable: MECH-102 epistemic_category=substrate_conditional
- **Why now:** Held by the governance V3-pending gate (MECH-102 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-174
Title: Retest after substrate: MECH-102
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-102
Blocked by: not v3-testable: MECH-102 epistemic_category=substrate_conditional
Why now: Held by the governance V3-pending gate (MECH-102 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-175 -- Retest after substrate: MECH-189

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** INF-ENV-003 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-175
Title: Retest after substrate: MECH-189
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-189
Blocked by: INF-ENV-003 [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-177 -- Retest after substrate: MECH-229

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
- **Why now:** Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-177
Title: Retest after substrate: MECH-229
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-229
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric (queued, supersedes 514t)
Why now: Blocked by 3 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-180 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/; f_dominance_conversion_ceiling [conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon]; free-text (via f_dominance_conversion_ceiling): rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 8 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-180
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/; f_dominance_conversion_ceiling [conflict_grade_near_tie_parametric_family_exhausted__build_rank_preserving_F_to_eligibility_demotion_MECH448_lead_MECH449_followon]; free-text (via f_dominance_conversion_ceiling): rank-preserving F->eligibility demotion lever build (MECH-448 lead; e3_selector.py, not yet built) -- ELEVATED to LEAD by user decision 2026-06-20 after V3-EXQ-; MECH-449 [no-substrate-entry] (transitive via f_dominance_conversion_ceiling): MECH-449 Go/No-Go eligibility governance (substrate_conditional, broader follow-on)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 8 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-184 -- Retest after substrate: MECH-261

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-033b [implemented]; SD-033 [unknown] (transitive via SD-033b); MECH-263 [no-substrate-entry] (transitive via SD-033b): MECH-263; MECH-261 [no-substrate-entry] (transitive via SD-033b): MECH-261; SD-033c [unknown]; SD-033 [unknown] (transitive via SD-033c); ARC-035 [no-substrate-entry] (transitive via SD-033c): ARC-035; MECH-151 [no-substrate-entry] (transitive via SD-033c): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033c): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033c): MECH-235; MECH-261 [no-substrate-entry] (transitive via SD-033c): MECH-261; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
- **Why now:** Blocked by 16 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-184
Title: Retest after substrate: MECH-261
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-261
Blocked by: SD-033b [implemented]; SD-033 [unknown] (transitive via SD-033b); MECH-263 [no-substrate-entry] (transitive via SD-033b): MECH-263; MECH-261 [no-substrate-entry] (transitive via SD-033b): MECH-261; SD-033c [unknown]; SD-033 [unknown] (transitive via SD-033c); ARC-035 [no-substrate-entry] (transitive via SD-033c): ARC-035; MECH-151 [no-substrate-entry] (transitive via SD-033c): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033c): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033c): MECH-235; MECH-261 [no-substrate-entry] (transitive via SD-033c): MECH-261; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); commitment-closure-control-plane [amend_implemented_pending_validation]; free-text (via commitment-closure-control-plane): commitment_closure:GAP-4 (460e ran 2026-06-17: terminal FAIL/non_contributory, self-routed substrate_not_ready_requeue on beta_engagement_both_arms 1/3; Legs A/
Why now: Blocked by 16 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-187 -- Retest after substrate: MECH-262

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-187
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

### IGW-20260621-015 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-654g RAN FAIL/non_contributory 2026-06-19T21:31Z (run_id v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier_20260619T213118Z_v3; ree-cloud-4; supersedes V3-EXQ-654f; reviewed /governance 2026-06-19). THE GAP-B BEHAVIOURAL LINEAGE TERMINUS: first run on the de-locked CRF stack wired to the 569i-validated top-k shortlist conversion. C1 (non-vacuity) FULLY MET on all 5 preconditions (class axis exercisable 1.0; GAP-A divergence 0.080 > 0.05; ARM_ON crf_frac_active 0.94 > 0.30; propagation non-vacuous, within-arm counterfactual delta 0.0021 nonzero -- the rule_state reaches committed action). C2 (PRIMARY committed-class entropy lift) FAILED: ARM_ON 0.6728 vs ARM_OFF 0.6614 = +0.011 nats, 0/3 seeds clear the 0.05-nat margin. Pre-registered C1-holds/C2-fails branch = non_contributory, the SHARED selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; MECH-439 F-dominance live root), NOT a MECH-309/ARC-062 falsification. SECOND independent behavioural channel after V3-EXQ-485h (OFC outcome-value bias) to corroborate MECH-439 as the live root. CRF instrumentation lineage CLEANLY TERMINATED (CRF done at 654f); residual is the F-dominance ceiling, not a 654-specific gap. Route: /implement-substrate (GAP-A gain/contrast amend); the OFC behavioural retest is sequenced behind the conversion-ceiling chain (ARC-065 569i top-k ceiling-lifted / 689a / 625e). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. PRIOR FRONTIER (now superseded) V3-EXQ-654f RAN FAIL/non_contributory 2026-06-18T00:52Z (run_id v3_exq_654f_arc062_gapb_rule_apprehension_behavioural_falsifier_20260618T005228Z_v3; ree-cloud-1; supersedes V3-EXQ-654e -- the recovery re-queue of the phantom-completed-no-manifest 654e, science unchanged; reviewed /governance 2026-06-18, non_contributory self-route, weights nothing; the CRF-gate calibration amend did not produce a contributory committed-class-entropy verdict, a 654g successor on a de-locked CRF/monostrategy substrate is owed). PRIOR FRONTIER V3-EXQ-654e QUEUED 2026-06-17 (ree-v3 main 488ec03; supersedes V3-EXQ-654d; claim_ids=[MECH-309, ARC-062]; priority 335, machine any) -- the GAP-B committed-class-entropy falsifier ported onto the CRF-GATE CALIBRATION AMEND (crf-availability-maintenance at the CRF locus, UNGATED from GAP-A; amend landed ree-v3 main 42895f6 2026-06-17). The 654d autopsy proved GAP-A de-collapse is the WRONG lever (gate-lockout independent of GAP-A); the amend's three CRF-locus levers (crf_mature_context_match_threshold=0.7 sharpen + crf_tolerance_conflict_cap=3 + crf_maintenance_couple_to_theta=True) are armed on ARM_ON so the maintained differentiated pool clears the conflict gate (contracts C20-C24 + smoke: crowded-pool frac_active 0.000->0.98). C1c crf_frac_active>=0.30 self-routing precondition RETAINED (now expected to clear; if not -> substrate_not_ready_requeue, NEVER a false weakens); conversion-ceiling off-ramp retained (C1 holds/C2 absent -> non_contributory + /implement-substrate or /claim-synthesis). AWAITING 654e RUN + REVIEW. PREDECESSOR: V3-EXQ-654d RAN FAIL/non_contributory 2026-06-16T15:27Z (ree-cloud-2; run_id v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3) -- REVIEWED + autopsied 2026-06-16 (failure_autopsy_V3-EXQ-654d_2026-06-16, status=confirmed). [QUEUED 2026-06-16T07:49Z, ree-v3 origin/main 927fe1c; supersedes V3-EXQ-654c; claim_ids=[MECH-309, ARC-062]; priority 315, machine any] -- the GAP-B falsifier ported onto the GAP-A DE-COLLAPSED substrate now that the gate cleared (V3-EXQ-684a PASS, conversion_mechanism_identified). Arms the 684a-validated ARM_STD_G2 conversion lever (modulatory_authority_normalize_basis=std + authority_gain=2.0 + use_modulatory_channel_routing + source=cand_world_summary) as a matched-stack constant on BOTH arms; only use_candidate_rule_field swept; CRF mature+maintenance+persist + trained-bias-head P1 unchanged; records crf_n_matched_last (the 654c discriminator). Pre-registered C1a/C1b/C1c/C1d preconditions each self-route substrate_not_ready_requeue (C1c crf_frac_active<0.30 routes to the CRF maintenance-theta amend, autopsy part ii -- NOT implemented in code, ready=False); three-branch map (PASS->supports; C1-holds/C2-fails->shared CONVERSION ceiling under ARM_STD_G2->non_contributory+/implement-substrate; C1-fails->substrate_not_ready_requeue); NO weakens branch. RESULT (failure_autopsy_V3-EXQ-654d_2026-06-16, confirmed): C1c FAILED again (crf_frac_active 0.0 all 3 ARM_ON seeds) -- the C1-fail branch. But 654d ARMED ARM_STD_G2 on both arms AND recorded the discriminator crf_mean_n_matched (7.08/7.29/8.70 -- the 654c-flagged instrument). LOAD-BEARING FINDING: the GAP-A conversion de-collapse is the WRONG LEVER for this gate -- ARM_STD_G2 de-collapsed the E3 selection channel (consumed_summary spread cleared the 0.05 floor 2/3 seeds) but NOT the CRF rule-match context KEY; the 16 differentiated rules (max_pairwise_dist 1.711) match 7-8/tick and ALL gate out (theta=0.15+0.25*(n_matched-1)~=1.65 >> maintenance_floor 0.45). mean_prop_counterfactual_delta=0.0 confirms the gated-out rule_state never reaches committed action. NON_CONTRIBUTORY, NO weakens -- the two CRF-locus faults the 654c autopsy named (context-key crowding + maintenance/theta calibration) remain un-amended (substrate bit-identical to 654c) and 654d proves them INDEPENDENT of the GAP-A selection conversion. ROUTE (user-confirmed): /implement-substrate AMEND crf-availability-maintenance at the CRF locus, UNGATED from GAP-A (couple maintained availability to theta(n_matched) [pure gate calibration] + de-collapse the CRF mint/match context key [distinct from the E3 channel] + keep frac_ACTIVE readiness gate); re-queue 654e on that gate, NOT on GAP-A. PREDECESSOR V3-EXQ-654c RAN FAIL/non_contributory 2026-06-15T12:38Z (run_id v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3; reviewed /governance 2026-06-15; supersedes V3-EXQ-654b; claim_ids=[MECH-309, ARC-062]) -- FAILed C1c arm_on_rule_field_differentiated_and_matured (crf_frac_active = 0.0 < 0.30) for the 4th consecutive iteration, but with an INVERTED signature confirmed by failure_autopsy_V3-EXQ-654c_2026-06-15 (status=confirmed): the 666c maintenance amend FIXED the retire-churn (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting stabilised at 12-16) so the pool now holds >=2 differentiated rules -- yet activation collapsed to exactly 0.0 because the GAP-A-collapsed e2_world_forward context (consumed_summary spread 0.0089 < 0.05) makes >=3 rules co-match, so gate_and_select theta = 0.15+0.25*(n_matched-1) >= 0.65 > maintenance_floor 0.45 and every matched rule is gated OUT. MAINTAINED != ACTIVE. C2 committed-class entropy DV never scored (C1 gates it). MECH-309/ARC-062 NOT weakened (non_contributory, substrate_ceiling, pending_retest_after_substrate). ROUTING (substrate_queue crf-availability-maintenance AMENDED + ready flipped True->False this cycle): de-collapse the CRF context key (sharpen/per-candidate-separate e2_world_forward feeding CRF mint/match, mirror GAP-A) + couple maintained availability to per-tick theta + upgrade the readiness gate to assert crf_frac_active>=0.30 (gate FIRING, not frac_maintained); re-queue the GAP-B falsifier (654d) ONLY AFTER GAP-A context de-collapse, since the CRF amend is necessary-but-not-sufficient while the shared monostrategy collapse persists. PREDECESSOR V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
- **Why now:** V3-EXQ-654g RAN + ADJUDICATED 2026-06-19 (FAIL/non_contributory; C1 fully met, C2 +0.011 nats 0/3 seeds = the SHARED MECH-439 F-dominance conversion ceiling, NOT a falsification). The CRF instrumentation lineage is CLEANLY TERMINATED; GAP-B

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-015
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-654g RAN FAIL/non_contributory 2026-06-19T21:31Z (run_id v3_exq_654g_arc062_gapb_rule_apprehension_behavioural_falsifier_20260619T213118Z_v3; ree-cloud-4; supersedes V3-EXQ-654f; reviewed /governance 2026-06-19). THE GAP-B BEHAVIOURAL LINEAGE TERMINUS: first run on the de-locked CRF stack wired to the 569i-validated top-k shortlist conversion. C1 (non-vacuity) FULLY MET on all 5 preconditions (class axis exercisable 1.0; GAP-A divergence 0.080 > 0.05; ARM_ON crf_frac_active 0.94 > 0.30; propagation non-vacuous, within-arm counterfactual delta 0.0021 nonzero -- the rule_state reaches committed action). C2 (PRIMARY committed-class entropy lift) FAILED: ARM_ON 0.6728 vs ARM_OFF 0.6614 = +0.011 nats, 0/3 seeds clear the 0.05-nat margin. Pre-registered C1-holds/C2-fails branch = non_contributory, the SHARED selection-authority CONVERSION ceiling (behavioral_diversity_isolation:GAP-A; MECH-439 F-dominance live root), NOT a MECH-309/ARC-062 falsification. SECOND independent behavioural channel after V3-EXQ-485h (OFC outcome-value bias) to corroborate MECH-439 as the live root. CRF instrumentation lineage CLEANLY TERMINATED (CRF done at 654f); residual is the F-dominance ceiling, not a 654-specific gap. Route: /implement-substrate (GAP-A gain/contrast amend); the OFC behavioural retest is sequenced behind the conversion-ceiling chain (ARC-065 569i top-k ceiling-lifted / 689a / 625e). MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate -- NOT weakened. PRIOR FRONTIER (now superseded) V3-EXQ-654f RAN FAIL/non_contributory 2026-06-18T00:52Z (run_id v3_exq_654f_arc062_gapb_rule_apprehension_behavioural_falsifier_20260618T005228Z_v3; ree-cloud-1; supersedes V3-EXQ-654e -- the recovery re-queue of the phantom-completed-no-manifest 654e, science unchanged; reviewed /governance 2026-06-18, non_contributory self-route, weights nothing; the CRF-gate calibration amend did not produce a contributory committed-class-entropy verdict, a 654g successor on a de-locked CRF/monostrategy substrate is owed). PRIOR FRONTIER V3-EXQ-654e QUEUED 2026-06-17 (ree-v3 main 488ec03; supersedes V3-EXQ-654d; claim_ids=[MECH-309, ARC-062]; priority 335, machine any) -- the GAP-B committed-class-entropy falsifier ported onto the CRF-GATE CALIBRATION AMEND (crf-availability-maintenance at the CRF locus, UNGATED from GAP-A; amend landed ree-v3 main 42895f6 2026-06-17). The 654d autopsy proved GAP-A de-collapse is the WRONG lever (gate-lockout independent of GAP-A); the amend's three CRF-locus levers (crf_mature_context_match_threshold=0.7 sharpen + crf_tolerance_conflict_cap=3 + crf_maintenance_couple_to_theta=True) are armed on ARM_ON so the maintained differentiated pool clears the conflict gate (contracts C20-C24 + smoke: crowded-pool frac_active 0.000->0.98). C1c crf_frac_active>=0.30 self-routing precondition RETAINED (now expected to clear; if not -> substrate_not_ready_requeue, NEVER a false weakens); conversion-ceiling off-ramp retained (C1 holds/C2 absent -> non_contributory + /implement-substrate or /claim-synthesis). AWAITING 654e RUN + REVIEW. PREDECESSOR: V3-EXQ-654d RAN FAIL/non_contributory 2026-06-16T15:27Z (ree-cloud-2; run_id v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3) -- REVIEWED + autopsied 2026-06-16 (failure_autopsy_V3-EXQ-654d_2026-06-16, status=confirmed). [QUEUED 2026-06-16T07:49Z, ree-v3 origin/main 927fe1c; supersedes V3-EXQ-654c; claim_ids=[MECH-309, ARC-062]; priority 315, machine any] -- the GAP-B falsifier ported onto the GAP-A DE-COLLAPSED substrate now that the gate cleared (V3-EXQ-684a PASS, conversion_mechanism_identified). Arms the 684a-validated ARM_STD_G2 conversion lever (modulatory_authority_normalize_basis=std + authority_gain=2.0 + use_modulatory_channel_routing + source=cand_world_summary) as a matched-stack constant on BOTH arms; only use_candidate_rule_field swept; CRF mature+maintenance+persist + trained-bias-head P1 unchanged; records crf_n_matched_last (the 654c discriminator). Pre-registered C1a/C1b/C1c/C1d preconditions each self-route substrate_not_ready_requeue (C1c crf_frac_active<0.30 routes to the CRF maintenance-theta amend, autopsy part ii -- NOT implemented in code, ready=False); three-branch map (PASS->supports; C1-holds/C2-fails->shared CONVERSION ceiling under ARM_STD_G2->non_contributory+/implement-substrate; C1-fails->substrate_not_ready_requeue); NO weakens branch. RESULT (failure_autopsy_V3-EXQ-654d_2026-06-16, confirmed): C1c FAILED again (crf_frac_active 0.0 all 3 ARM_ON seeds) -- the C1-fail branch. But 654d ARMED ARM_STD_G2 on both arms AND recorded the discriminator crf_mean_n_matched (7.08/7.29/8.70 -- the 654c-flagged instrument). LOAD-BEARING FINDING: the GAP-A conversion de-collapse is the WRONG LEVER for this gate -- ARM_STD_G2 de-collapsed the E3 selection channel (consumed_summary spread cleared the 0.05 floor 2/3 seeds) but NOT the CRF rule-match context KEY; the 16 differentiated rules (max_pairwise_dist 1.711) match 7-8/tick and ALL gate out (theta=0.15+0.25*(n_matched-1)~=1.65 >> maintenance_floor 0.45). mean_prop_counterfactual_delta=0.0 confirms the gated-out rule_state never reaches committed action. NON_CONTRIBUTORY, NO weakens -- the two CRF-locus faults the 654c autopsy named (context-key crowding + maintenance/theta calibration) remain un-amended (substrate bit-identical to 654c) and 654d proves them INDEPENDENT of the GAP-A selection conversion. ROUTE (user-confirmed): /implement-substrate AMEND crf-availability-maintenance at the CRF locus, UNGATED from GAP-A (couple maintained availability to theta(n_matched) [pure gate calibration] + de-collapse the CRF mint/match context key [distinct from the E3 channel] + keep frac_ACTIVE readiness gate); re-queue 654e on that gate, NOT on GAP-A. PREDECESSOR V3-EXQ-654c RAN FAIL/non_contributory 2026-06-15T12:38Z (run_id v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3; reviewed /governance 2026-06-15; supersedes V3-EXQ-654b; claim_ids=[MECH-309, ARC-062]) -- FAILed C1c arm_on_rule_field_differentiated_and_matured (crf_frac_active = 0.0 < 0.30) for the 4th consecutive iteration, but with an INVERTED signature confirmed by failure_autopsy_V3-EXQ-654c_2026-06-15 (status=confirmed): the 666c maintenance amend FIXED the retire-churn (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting stabilised at 12-16) so the pool now holds >=2 differentiated rules -- yet activation collapsed to exactly 0.0 because the GAP-A-collapsed e2_world_forward context (consumed_summary spread 0.0089 < 0.05) makes >=3 rules co-match, so gate_and_select theta = 0.15+0.25*(n_matched-1) >= 0.65 > maintenance_floor 0.45 and every matched rule is gated OUT. MAINTAINED != ACTIVE. C2 committed-class entropy DV never scored (C1 gates it). MECH-309/ARC-062 NOT weakened (non_contributory, substrate_ceiling, pending_retest_after_substrate). ROUTING (substrate_queue crf-availability-maintenance AMENDED + ready flipped True->False this cycle): de-collapse the CRF context key (sharpen/per-candidate-separate e2_world_forward feeding CRF mint/match, mirror GAP-A) + couple maintained availability to per-tick theta + upgrade the readiness gate to assert crf_frac_active>=0.30 (gate FIRING, not frac_maintained); re-queue the GAP-B falsifier (654d) ONLY AFTER GAP-A context de-collapse, since the CRF amend is necessary-but-not-sufficient while the shared monostrategy collapse persists. PREDECESSOR V3-EXQ-654b TERMINAL FAIL 2026-06-10T20:05Z (non_contributory, substrate_not_ready_requeue; reviewed /governance 2026-06-10) -- the longer-maturation (P0+P1 100->240 ep) re-run of 654a still did NOT clear the C1c crf_frac_active>=0.30 floor (measured 0.130), so the committed-class falsifier DV never scored; supersedes V3-EXQ-654a. PREDECESSOR V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
Claims: MECH-309, ARC-062
Why now: V3-EXQ-654g RAN + ADJUDICATED 2026-06-19 (FAIL/non_contributory; C1 fully met, C2 +0.011 nats 0/3 seeds = the SHARED MECH-439 F-dominance conversion ceiling, NOT a falsification). The CRF instrumentation lineage is CLEANLY TERMINATED; GAP-B

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-027 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-660b TERMINAL FAIL 2026-06-11T13:43Z is the lineage FRONTIER (reclassified non_contributory / measurement_test_design_defect at governance cycle #5; the graded-in-K falsifier is RETIRED, no 660c; NOT a weakens) -- owner_exq leads with the frontier letter as of the 2026-06-12 closure-drift reconcile (advancing 660 -> 660b, the same convention as this cycle's 514m->514n / 485e->485f advances) so the structural lineage-advanced flag clears; the STANDING GAP-B EVIDENCE is UNCHANGED = predecessor V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z for MECH-341 (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; the binary within-class preserver is established). Owner re-pointed 660b -> 660 at governance cycle #5 2026-06-11 per confirmed failure_autopsy_V3-EXQ-660b: the graded-in-pool-size ratification the 660a/660b lineage was chasing is REMOVED AS A GATE (graded-in-K over-specifies a PRESERVATION claim), not outstanding -- no 660c. RETIRED graded-falsifier lineage: V3-EXQ-660b TERMINAL FAIL/weakens 2026-06-11T13:43Z (windowed-readout redesign of 660a, supersedes 660a; both readiness gates passed yet C_GRADED 0/3 seeds, sensitivity gate cleared only marginally 0.0568 + non-monotonically) was reclassified non_contributory (measurement_test_design_defect) at cycle #5, NOT a weakens; V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
- **Why now:** MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-027
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-660b TERMINAL FAIL 2026-06-11T13:43Z is the lineage FRONTIER (reclassified non_contributory / measurement_test_design_defect at governance cycle #5; the graded-in-K falsifier is RETIRED, no 660c; NOT a weakens) -- owner_exq leads with the frontier letter as of the 2026-06-12 closure-drift reconcile (advancing 660 -> 660b, the same convention as this cycle's 514m->514n / 485e->485f advances) so the structural lineage-advanced flag clears; the STANDING GAP-B EVIDENCE is UNCHANGED = predecessor V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z for MECH-341 (within-class-representative-diversity lift 4.862 vs legacy 4.781 nats; the binary within-class preserver is established). Owner re-pointed 660b -> 660 at governance cycle #5 2026-06-11 per confirmed failure_autopsy_V3-EXQ-660b: the graded-in-pool-size ratification the 660a/660b lineage was chasing is REMOVED AS A GATE (graded-in-K over-specifies a PRESERVATION claim), not outstanding -- no 660c. RETIRED graded-falsifier lineage: V3-EXQ-660b TERMINAL FAIL/weakens 2026-06-11T13:43Z (windowed-readout redesign of 660a, supersedes 660a; both readiness gates passed yet C_GRADED 0/3 seeds, sensitivity gate cleared only marginally 0.0568 + non-monotonically) was reclassified non_contributory (measurement_test_design_defect) at cycle #5, NOT a weakens; V3-EXQ-660a TERMINAL FAIL/weakens 2026-06-11T03:26Z (graded-confirmation CEM pool-size dose-response; C_GRADED graded on only 1/3 seeds -> the within-class lift does NOT scale with pool size; preconditions MET; FLAGGED for /failure-autopsy, LEFT PENDING 2026-06-11 governance, no evidence stamp applied; NO supersede of 660). PREDECESSOR + STANDING EVIDENCE V3-EXQ-660 LANDED PASS/supports 2026-06-10T04:41Z (MECH-341 within-class-representative-diversity retest on the GAP-A-ready/authority-ready stack; within_class_rep_cond_entropy PRIMARY DV, swept 4.862 vs legacy 4.781 nats; supersedes 614e; folded into claims.yaml 2026-06-10, MECH-341 supports / v3_pending HELD -- this base supports is preserved regardless of the 660a graded-axis FAIL). Earlier predecessor: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling); V3-EXQ-649 GAP-A readiness PASS
Claims: MECH-341, ARC-062, ARC-065
Why now: MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-031 -- Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I (falsifier front) + GAP-J (build front)]

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** biology_grounding_convergence_v4:BG-2
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-031
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

### IGW-20260621-124 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap blocked_pending_substrate on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-124
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

### IGW-20260621-150 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625e
- **Why now:** RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-150
Title: Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): sd_037_axis_b:P1b
Owner EXQ: V3-EXQ-625e
Claims: SD-037, MECH-281
Why now: RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-029 -- F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 33
- **Gap(s):** behavioral_diversity_isolation:GAP-I
- **Owner EXQ:** V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER, now the LIVE owner of this node's ceiling-lift (queued 2026-06-20, landed ree-v3 main 8d87d4a; coordinator DB pending on ree-cloud-3; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py). It tests the rung-2 constitutional build lever (use_f_eligibility_demotion in e3_selector.py) carried by the child build node behavioral_diversity_isolation:GAP-J; a PASS (committed-class entropy strict-above the conflict-grade controls >=2/3, acceptance bar arc_107_selector_constitution_design_2026-06-20.md s4) lifts MECH-439's substrate_ceiling and unblocks the held downstream retests. PROMOTES NOTHING (MECH-448 stays candidate; governance applies only when 689d scores). PREDECESSOR (SETTLED, history): V3-EXQ-689a SETTLED 2026-06-20 FAIL/non_contributory (readiness met, non_degenerate) -- the pre-registered A1B1 (gap-scaled BOTH levers) gate did NOT fire (committed-class entropy 0.387 = baseline, 0/3 strict-above the collapsed AND the gap-blind controls) -> the conflict-grade near-tie parametric family is EXHAUSTED (substrate_queue f_dominance_conversion_ceiling status). Load-bearing 2x2 dissociation: Factor B alone (A0B1 gap-scaled commit-T) converted 0.850 on 2/3 seeds, Factor A width inert (0.440), destructive A x B. MECH-439 -> substrate_ceiling / pending_retest_after_substrate (governance 7419453d1d). The falsifier front escalated to the rung-2 CONSTITUTIONAL BUILD (rank-preserving F->eligibility demotion, MECH-448 lead / MECH-449 follow-on) carried by GAP-J, and 689d is that build's falsifier. This node stays in-progress as the root-tracking parent; GAP-J owns the forward build work.
- **Why now:** 689a SETTLED FAIL (A1B1 0/3 above both control sets; conflict-grade near-tie family exhausted). Root NOT lifted -- this parent node stays in-progress tracking the F-dominance ceiling; forward work moved to the child build node behavioral_di

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-029
Title: F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): behavioral_diversity_isolation:GAP-I
Owner EXQ: V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER, now the LIVE owner of this node's ceiling-lift (queued 2026-06-20, landed ree-v3 main 8d87d4a; coordinator DB pending on ree-cloud-3; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py). It tests the rung-2 constitutional build lever (use_f_eligibility_demotion in e3_selector.py) carried by the child build node behavioral_diversity_isolation:GAP-J; a PASS (committed-class entropy strict-above the conflict-grade controls >=2/3, acceptance bar arc_107_selector_constitution_design_2026-06-20.md s4) lifts MECH-439's substrate_ceiling and unblocks the held downstream retests. PROMOTES NOTHING (MECH-448 stays candidate; governance applies only when 689d scores). PREDECESSOR (SETTLED, history): V3-EXQ-689a SETTLED 2026-06-20 FAIL/non_contributory (readiness met, non_degenerate) -- the pre-registered A1B1 (gap-scaled BOTH levers) gate did NOT fire (committed-class entropy 0.387 = baseline, 0/3 strict-above the collapsed AND the gap-blind controls) -> the conflict-grade near-tie parametric family is EXHAUSTED (substrate_queue f_dominance_conversion_ceiling status). Load-bearing 2x2 dissociation: Factor B alone (A0B1 gap-scaled commit-T) converted 0.850 on 2/3 seeds, Factor A width inert (0.440), destructive A x B. MECH-439 -> substrate_ceiling / pending_retest_after_substrate (governance 7419453d1d). The falsifier front escalated to the rung-2 CONSTITUTIONAL BUILD (rank-preserving F->eligibility demotion, MECH-448 lead / MECH-449 follow-on) carried by GAP-J, and 689d is that build's falsifier. This node stays in-progress as the root-tracking parent; GAP-J owns the forward build work.
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260, Q-045, SD-037, MECH-445, MECH-446
Why now: 689a SETTLED FAIL (A1B1 0/3 above both control sets; conflict-grade near-tie family exhausted). Root NOT lifted -- this parent node stays in-progress tracking the F-dominance ceiling; forward work moved to the child build node behavioral_di

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-030 -- ARC-107 basal-ganglia E3 selector-constitution BUILD -- the OPENING build front, child of GAP-I's F-dominance falsifier 

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 33
- **Gap(s):** behavioral_diversity_isolation:GAP-J
- **Owner EXQ:** V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER (689a-successor), now queued + ingested (ree-v3 main 8d87d4a; coordinator DB pending ree-cloud-3; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py). This node's LEAD lever MECH-448 is BUILT + LANDED (ree-v3 main 4c9b3c9; e3_selector.py use_f_eligibility_demotion / f_eligibility_envelope_floor / f_eligibility_dn_sigma, no-op default, bit-identical OFF), so the build front is no longer 'not yet an experiment' -- its falsifier is in flight. 689d arms ARM_OFF (hard top-k F-prefix = 569i lever) vs ARM_ON (graded DN envelope) + a VERIFIED-LIFTING matched-noise control on the GAP-A foraging substrate; non-vacuity precondition f_eligibility_excluded_count>0. A 689d PASS (committed-class entropy strict-above the conflict-grade controls >=2/3, acceptance arc_107_selector_constitution_design_2026-06-20.md s4) CLOSES this node and lifts GAP-I's MECH-439 ceiling. PROMOTES NOTHING (MECH-448 stays candidate; governance applies only when 689d scores). MECH-449 (Go/No-Go follow-on) builds ONLY if demotion alone is insufficient.
- **Blocked by:** behavioral_diversity_isolation:GAP-I [in_progress]
- **Why now:** IN-PROGRESS -- build front now has its falsifier in flight (owner V3-EXQ-689d). The build sequence (design note s6) has executed through the falsifier: ARC-106 grounding lit-pull DONE; /claim-synthesis re-grain DONE (MECH-447 superseded by 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-030
Title: ARC-107 basal-ganglia E3 selector-constitution BUILD -- the OPENING build front, child of GAP-I's F-dominance falsifier 
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): behavioral_diversity_isolation:GAP-J
Owner EXQ: V3-EXQ-689d -- the MECH-448 (ARC-107) rank-preserving F->eligibility demotion FALSIFIER (689a-successor), now queued + ingested (ree-v3 main 8d87d4a; coordinator DB pending ree-cloud-3; script experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py). This node's LEAD lever MECH-448 is BUILT + LANDED (ree-v3 main 4c9b3c9; e3_selector.py use_f_eligibility_demotion / f_eligibility_envelope_floor / f_eligibility_dn_sigma, no-op default, bit-identical OFF), so the build front is no longer 'not yet an experiment' -- its falsifier is in flight. 689d arms ARM_OFF (hard top-k F-prefix = 569i lever) vs ARM_ON (graded DN envelope) + a VERIFIED-LIFTING matched-noise control on the GAP-A foraging substrate; non-vacuity precondition f_eligibility_excluded_count>0. A 689d PASS (committed-class entropy strict-above the conflict-grade controls >=2/3, acceptance arc_107_selector_constitution_design_2026-06-20.md s4) CLOSES this node and lifts GAP-I's MECH-439 ceiling. PROMOTES NOTHING (MECH-448 stays candidate; governance applies only when 689d scores). MECH-449 (Go/No-Go follow-on) builds ONLY if demotion alone is insufficient.
Claims: ARC-107, MECH-448, MECH-449, Q-078
Blocked by: behavioral_diversity_isolation:GAP-I [in_progress]
Why now: IN-PROGRESS -- build front now has its falsifier in flight (owner V3-EXQ-689d). The build sequence (design note s6) has executed through the falsifier: ARC-106 grounding lit-pull DONE; /claim-synthesis re-grain DONE (MECH-447 superseded by 

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-106 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-106
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

### IGW-20260621-108 -- Retrieval-scope vs action-authority split (reflection-retrieval != action-authority-retrieval)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35
- **Gap(s):** memory_lifecycle_v4:MEM-6
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-108
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

### IGW-20260621-166 -- Queue depth low (1 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-166
Title: Queue depth low (1 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-002 -- Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-2
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-002
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

### IGW-20260621-006 -- Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** abstract_relational_reasoning_v6:ARR-6
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-006
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

### IGW-20260621-007 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-007
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

### IGW-20260621-020 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-020
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

### IGW-20260621-021 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-021
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

### IGW-20260621-040 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-040
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

### IGW-20260621-045 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** drives_motivation_v4:DRV-2
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-045
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

### IGW-20260621-048 -- Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-1
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-048
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

### IGW-20260621-049 -- Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-2
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-049
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

### IGW-20260621-050 -- Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** ethics_as_coherence_v5:ETH-3
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-050
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

### IGW-20260621-055 -- Stream-binding mechanism: route own motivational-affective streams across the other-model

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-3
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-055
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

### IGW-20260621-056 -- Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** fast_empathy_v5:EMP-4
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-056
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

### IGW-20260621-059 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-059
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

### IGW-20260621-065 -- Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-3
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-065
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

### IGW-20260621-068 -- Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** grammar_primitive_mining_v6:GRAM-6
- **Blocked by:** grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-068
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

### IGW-20260621-069 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-069
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

### IGW-20260621-070 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-070
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

### IGW-20260621-079 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-079
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

### IGW-20260621-081 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-081
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

### IGW-20260621-084 -- Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-1
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-084
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

### IGW-20260621-085 -- Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-2
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]
- **Why now:** Plan gap open on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-085
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

### IGW-20260621-086 -- The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_affect_adaptor_v6:LAA-3
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-086
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

### IGW-20260621-090 -- Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-3
- **Blocked by:** language_emergence_bootstrap_v6:LANG-2 [open]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-090
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

### IGW-20260621-091 -- Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_emergence_bootstrap_v6:LANG-4
- **Blocked by:** language_emergence_bootstrap_v6:LANG-3 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-091
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

### IGW-20260621-095 -- Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-2
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-095
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

### IGW-20260621-096 -- Deception detection / honest-signal pressure (deception = modelling another model)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** language_trust_deception_institutions_v6:LTI-3
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-096
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

### IGW-20260621-099 -- Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-1
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-099
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

### IGW-20260621-100 -- Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-2
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-100
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

### IGW-20260621-101 -- Live unethical affordance: harmful action representable as a chooseable possibility (not absent)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-3
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-101
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

### IGW-20260621-102 -- Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-4
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-102
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

### IGW-20260621-104 -- Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** loveability_ethical_agency_v5:LOVE-6
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-104
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

### IGW-20260621-110 -- Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-1
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-110
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

### IGW-20260621-111 -- Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-2
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-1 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-111
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

### IGW-20260621-112 -- Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-3
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-112
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

### IGW-20260621-113 -- Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-4
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-113
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

### IGW-20260621-117 -- Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-1
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-117
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

### IGW-20260621-118 -- Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** multi_agent_ecology_v5:MAE-2
- **Blocked by:** multi_agent_ecology_v5:MAE-1 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-118
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

### IGW-20260621-125 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-125
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

### IGW-20260621-129 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-129
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

### IGW-20260621-138 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-138
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

### IGW-20260621-140 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-140
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

### IGW-20260621-141 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-141
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

### IGW-20260621-144 -- Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-1
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-144
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

### IGW-20260621-147 -- Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-4
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-147
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

### IGW-20260621-157 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** self_model_v4:SELF-2
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-157
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

### IGW-20260621-008 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-008
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

### IGW-20260621-032 -- Commitment / de-commit latch grounding L1 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** biology_grounding_convergence_v4:BG-3
- **Blocked by:** biology_grounding_convergence_v4:BG-2 [in_progress]
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-032
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

### IGW-20260621-037 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460i (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5; coordinator DB + /queue/active confirmed, machine_affinity ree-cloud-3 -- the LIVE in-flight de-commit falsifier of MECH-445/446 on the rung-6 COMMIT/RELEASE-DURATION lever = graded natural-commit-occupancy release [ree_core/policy/natural_commit_urgency.py NaturalCommitUrgencyRelease, built ree-v3 main ab2c1a9 2026-06-20]; see governance_2026_06_20b + resume_condition). PREDECESSOR V3-EXQ-460h RAN terminal FAIL/non_contributory 2026-06-20 (confirmed failure_autopsy_V3-EXQ-460h_2026-06-20). [HISTORICAL 460h owner record:] V3-EXQ-460h (QUEUED 2026-06-19, ree-v3 main b46c777, supersedes V3-EXQ-460g, ingested in the coordinator DB; the refractory-INDEPENDENT commit-intent retest of the re-grained SD-034 closure cluster -- same de-commit MAGNITUDE lever + within-arm around-closure C2 occupancy-delta DV, but with non-vacuity gated on sd034_n_closure_commit_intent>0; claim_ids=[MECH-446 scored, MECH-445 precondition]). Predecessor V3-EXQ-460g RAN terminal FAIL/non_contributory 2026-06-19T18:57Z (supersedes 460f; confirmed failure_autopsy_V3-EXQ-460g_2026-06-19, applied by governance-cycle-20260619T2013Z), self-routed substrate_not_ready_requeue: the 460f-prescribed de-commit MAGNITUDE lever (committed-run-scaled Leg-B refractory) was SELF-DEFEATING -- the scaled refractory pinned at the 60-tick cap on ~530-560-step runs and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the tightened non-vacuity gate counts collapsed (sd034_n_closure_coupled_elevations 36->0 seed42, closure_coupling_nonvacuous 0/3) even though the refractory HAS authority (seed-42 within-arm occupancy 0.333->0.0, C2 PASS). 7th SD-034-lineage autopsy -> the granularity-debt WATCH ITEM fired: /claim-synthesis decomposed the coarse SD-034 closure claim (2026-06-19, applied REE_assembly master 6a35087fd6) into SD-034 narrowed umbrella + MECH-445 (closure->beta coupling engagement) + MECH-446 (de-commit-authority magnitude), both candidate/v3_pending/pending_retest_after_substrate; /implement-substrate landed the refractory-independent commit-intent amend (ree-v3 main 167b3b7) that decouples the MECH-446 magnitude lever from the MECH-445 coupling-engagement non-vacuity metric. See governance_2026_06_19b. (Lineage 460f + 468e -- the de-commit and perseveration sides of the beta-engagement amend, BOTH RAN + AUTOPSIED 2026-06-18, together confirming ONE structural property [de-commit/release fires with correct sign but sub-threshold authority magnitude] via TWO independent DVs -- detail in governance_2026_06_18/_18b; 460e in governance_2026_06_17; 460d/468d + *c cohort in governance_2026_06_13/_12b. 468f still separately owed. 462b/465b NEVER scoped -- MECH-267 + MECH-094 behavioural arms deferred per sd033_governance Phase 4/5; do not hunt for them.)
- **Why now:** Advances/closes on the V3-EXQ-460i RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5, coordinator DB + /queue/active, machine_affinity ree-cloud-3) on the rung-6 COMMIT/RELEASE-DURATION leve

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-037
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-460i (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5; coordinator DB + /queue/active confirmed, machine_affinity ree-cloud-3 -- the LIVE in-flight de-commit falsifier of MECH-445/446 on the rung-6 COMMIT/RELEASE-DURATION lever = graded natural-commit-occupancy release [ree_core/policy/natural_commit_urgency.py NaturalCommitUrgencyRelease, built ree-v3 main ab2c1a9 2026-06-20]; see governance_2026_06_20b + resume_condition). PREDECESSOR V3-EXQ-460h RAN terminal FAIL/non_contributory 2026-06-20 (confirmed failure_autopsy_V3-EXQ-460h_2026-06-20). [HISTORICAL 460h owner record:] V3-EXQ-460h (QUEUED 2026-06-19, ree-v3 main b46c777, supersedes V3-EXQ-460g, ingested in the coordinator DB; the refractory-INDEPENDENT commit-intent retest of the re-grained SD-034 closure cluster -- same de-commit MAGNITUDE lever + within-arm around-closure C2 occupancy-delta DV, but with non-vacuity gated on sd034_n_closure_commit_intent>0; claim_ids=[MECH-446 scored, MECH-445 precondition]). Predecessor V3-EXQ-460g RAN terminal FAIL/non_contributory 2026-06-19T18:57Z (supersedes 460f; confirmed failure_autopsy_V3-EXQ-460g_2026-06-19, applied by governance-cycle-20260619T2013Z), self-routed substrate_not_ready_requeue: the 460f-prescribed de-commit MAGNITUDE lever (committed-run-scaled Leg-B refractory) was SELF-DEFEATING -- the scaled refractory pinned at the 60-tick cap on ~530-560-step runs and BetaGate.elevate() is a no-op while the refractory is active, so the closure-coupled re-elevations the tightened non-vacuity gate counts collapsed (sd034_n_closure_coupled_elevations 36->0 seed42, closure_coupling_nonvacuous 0/3) even though the refractory HAS authority (seed-42 within-arm occupancy 0.333->0.0, C2 PASS). 7th SD-034-lineage autopsy -> the granularity-debt WATCH ITEM fired: /claim-synthesis decomposed the coarse SD-034 closure claim (2026-06-19, applied REE_assembly master 6a35087fd6) into SD-034 narrowed umbrella + MECH-445 (closure->beta coupling engagement) + MECH-446 (de-commit-authority magnitude), both candidate/v3_pending/pending_retest_after_substrate; /implement-substrate landed the refractory-independent commit-intent amend (ree-v3 main 167b3b7) that decouples the MECH-446 magnitude lever from the MECH-445 coupling-engagement non-vacuity metric. See governance_2026_06_19b. (Lineage 460f + 468e -- the de-commit and perseveration sides of the beta-engagement amend, BOTH RAN + AUTOPSIED 2026-06-18, together confirming ONE structural property [de-commit/release fires with correct sign but sub-threshold authority magnitude] via TWO independent DVs -- detail in governance_2026_06_18/_18b; 460e in governance_2026_06_17; 460d/468d + *c cohort in governance_2026_06_13/_12b. 468f still separately owed. 462b/465b NEVER scoped -- MECH-267 + MECH-094 behavioural arms deferred per sd033_governance Phase 4/5; do not hunt for them.)
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342
Why now: Advances/closes on the V3-EXQ-460i RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-20, ree-v3 main 21903a5, coordinator DB + /queue/active, machine_affinity ree-cloud-3) on the rung-6 COMMIT/RELEASE-DURATION leve

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-163 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-163
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

### IGW-20260621-189 -- Proposal EXP-0155 (MECH-191)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-189
Title: Proposal EXP-0155 (MECH-191)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-191
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-190 -- Proposal EXP-0189 (ARC-050)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-190
Title: Proposal EXP-0189 (ARC-050)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: ARC-050
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-191 -- Proposal EXP-0191 (INV-050)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-191
Title: Proposal EXP-0191 (INV-050)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-050
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-192 -- Proposal EXP-0193 (INV-065)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-192
Title: Proposal EXP-0193 (INV-065)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-065
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-193 -- Proposal EXP-0195 (MECH-085)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-193
Title: Proposal EXP-0195 (MECH-085)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-085
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-033 -- Drive / incentive salience grounding L2 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** biology_grounding_convergence_v4:BG-4
- **Why now:** Plan gap open on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-033
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

### IGW-20260621-034 -- Goal / wanting layer grounding L1 -> L2

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** biology_grounding_convergence_v4:BG-5
- **Why now:** Plan gap open on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-034
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

### IGW-20260621-064 -- Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** grammar_primitive_mining_v6:GRAM-2
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-064
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

### IGW-20260621-083 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** inference_belief_state_v4:INF-7
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-083
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

### IGW-20260621-139 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-139
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

### IGW-20260621-003 -- Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-3
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-003
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

### IGW-20260621-004 -- Analogy / structure-mapping across grounded domains (relational alignment, not surface match)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-4
- **Blocked by:** abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-004
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

### IGW-20260621-005 -- Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** abstract_relational_reasoning_v6:ARR-5
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-005
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

### IGW-20260621-009 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-009
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

### IGW-20260621-010 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-010
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

### IGW-20260621-013 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]; affect_expression_v4:AE-10 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-013
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

### IGW-20260621-014 -- Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** affect_expression_v4:AE-10
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-014
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

### IGW-20260621-022 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-022
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

### IGW-20260621-023 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-023
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

### IGW-20260621-041 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-041
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

### IGW-20260621-042 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-042
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

### IGW-20260621-047 -- Orienting/surveying drive: pre-approach active-sensing control state

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** drives_motivation_v4:DRV-4
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-047
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

### IGW-20260621-051 -- Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-4
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-051
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

### IGW-20260621-052 -- Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** ethics_as_coherence_v5:ETH-5
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-052
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

### IGW-20260621-057 -- Residue-aware social repair: regret-residue after exploitation generates a repair-goal

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-5
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-057
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

### IGW-20260621-058 -- Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** fast_empathy_v5:EMP-6
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-058
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

### IGW-20260621-060 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-060
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

### IGW-20260621-061 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-061
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

### IGW-20260621-062 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-062
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

### IGW-20260621-071 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-071
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

### IGW-20260621-072 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-072
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

### IGW-20260621-073 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-073
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

### IGW-20260621-080 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-080
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

### IGW-20260621-082 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-082
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

### IGW-20260621-087 -- Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-4
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-087
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

### IGW-20260621-088 -- Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_affect_adaptor_v6:LAA-5
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-088
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

### IGW-20260621-092 -- Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-5
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-092
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

### IGW-20260621-093 -- Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-6
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-093
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

### IGW-20260621-094 -- Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_emergence_bootstrap_v6:LANG-7
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-094
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

### IGW-20260621-097 -- Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-4
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-097
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

### IGW-20260621-098 -- Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** language_trust_deception_institutions_v6:LTI-5
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-098
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

### IGW-20260621-103 -- Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** loveability_ethical_agency_v5:LOVE-5
- **Blocked by:** loveability_ethical_agency_v5:LOVE-4 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-103
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

### IGW-20260621-105 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-105
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

### IGW-20260621-107 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-107
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

### IGW-20260621-114 -- Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-5
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
- **Why now:** Plan gap open on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-114
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

### IGW-20260621-116 -- Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-7
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-116
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

### IGW-20260621-119 -- Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-3
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-119
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

### IGW-20260621-120 -- Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-4
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-120
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

### IGW-20260621-121 -- Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-5
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-121
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

### IGW-20260621-123 -- ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** multi_agent_ecology_v5:MAE-7
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-123
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

### IGW-20260621-126 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-126
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

### IGW-20260621-127 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-127
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

### IGW-20260621-128 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-128
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

### IGW-20260621-131 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-131
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

### IGW-20260621-132 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-132
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

### IGW-20260621-133 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-133
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

### IGW-20260621-136 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-136
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

### IGW-20260621-137 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-137
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

### IGW-20260621-142 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-142
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

### IGW-20260621-143 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-143
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

### IGW-20260621-145 -- Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-2
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-145
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

### IGW-20260621-146 -- Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-3
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-146
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

### IGW-20260621-148 -- Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-5
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-4 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-148
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

### IGW-20260621-151 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [in_progress]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-151
Title: Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): sd_037_axis_b:P2
Claims: SD-037
Blocked by: sd_037_axis_b:P1b [in_progress]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-152 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-152
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

### IGW-20260621-153 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-153
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

### IGW-20260621-154 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-154
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

### IGW-20260621-155 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-155
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

### IGW-20260621-160 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-160
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

### IGW-20260621-161 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-161
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

### IGW-20260621-162 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-3 [open]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-162
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

### IGW-20260621-016 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg now owned by V3-EXQ-687 (QUEUED 2026-06-17, the registered 4-arm tonic-noise ablation on the survival-competent scaffolded_sd054_onboarding substrate that 603q PASSed on; AWAITING RUN+REVIEW); GAP-B successor still owed
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-016
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Owner EXQ: V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg now owned by V3-EXQ-687 (QUEUED 2026-06-17, the registered 4-arm tonic-noise ablation on the survival-competent scaffolded_sd054_onboarding substrate that 603q PASSed on; AWAITING RUN+REVIEW); GAP-B successor still owed
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-017 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-017
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

### IGW-20260621-019 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-019
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

### IGW-20260621-026 -- Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imaginat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** autobiographical_memory_v4:ABM-9
- **Why now:** Plan gap closed on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-026
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

### IGW-20260621-028 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
- **Why now:** AWAITING V3-EXQ-603q RUN+REVIEW 2026-06-16 (the AUTHORITATIVE current state; see governance_2026_06_16). The Branch-B harm-pathway stabilization amend is LANDED (experiments/scaffolded_sd054_onboarding.py: decoupled encoder LR scaffold_harm

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-028
Title: Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-C
Owner EXQ: V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
Claims: MECH-313, MECH-260, Q-045
Why now: AWAITING V3-EXQ-603q RUN+REVIEW 2026-06-16 (the AUTHORITATIVE current state; see governance_2026_06_16). The Branch-B harm-pathway stabilization amend is LANDED (experiments/scaffolded_sd054_onboarding.py: decoupled encoder LR scaffold_harm

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-038 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485h RAN FAIL 2026-06-19T19:27Z (supersedes V3-EXQ-485g; 2nd non-vacuous trained-OFC-head test -- an even LARGER cross-candidate bias range 0.50 vs 485g 0.17, head delta 5.63, still ZERO behavioural conversion; self-stamped weakens NEUTRALIZED to non_contributory, flagged for a fresh /failure-autopsy, left PENDING -- see governance_2026_06_19b). PRIOR FRONTIER V3-EXQ-485g RAN FAIL 2026-06-19T14:54Z on ree-cloud-3 (supersedes V3-EXQ-485f; trained-OFC-head behavioural arm, claim_ids=[SD-033b, MECH-263]). Readiness MET this time (the 485f vacuity fix worked: OFC bias cross-candidate range 0.171 >= the re-aligned 0.05 DV floor; head genuinely trained, weight-delta 6.32, 120 grad updates / 3683 outcome-coupled loss terms) but the load-bearing behavioural DVs FAIL (C1 devaluation_selection_shift {0.001,0.0,0.010} << 0.05; C2 between-context TV ~0). The trained head produced real cross-candidate bias RANGE with ZERO behavioural conversion -- the MECH-439 F-dominance conversion-ceiling signature (F ~88-89% of E3 committed-selection variance, V3-EXQ-571). FLAGGED for /failure-autopsy by governance-20260619T1455Z (user-confirmed): the self-stamped weakens was NEUTRALIZED to non_contributory pending adjudication of genuine-weakens vs conversion-ceiling/substrate_ceiling; SD-033b/MECH-263 exp_conf 0.325->0.0, conflict-resolution rec auto-resolved, both stay pending_retest_after_substrate. NOT marked reviewed (stays in pending_review until the autopsy resolves). 485f marked superseded. Lineage owner advanced 485f -> 485g. PREDECESSORS: 485e (FAIL/non_contributory, autopsied 2026-06-11), 485d (substrate-readiness diagnostic), 485c/485b representation-level MECH-263 diagnostics PASS 2026-06-04 (NOT a supersession lineage).
- **Why now:** Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_head / REEConfig.ofc_train_state_bias_head (default False -> last Linear zeroed, bit-identical OFF) + OFCAnalog.bias_head_parameters(); the SD-033b an

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-038
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485h RAN FAIL 2026-06-19T19:27Z (supersedes V3-EXQ-485g; 2nd non-vacuous trained-OFC-head test -- an even LARGER cross-candidate bias range 0.50 vs 485g 0.17, head delta 5.63, still ZERO behavioural conversion; self-stamped weakens NEUTRALIZED to non_contributory, flagged for a fresh /failure-autopsy, left PENDING -- see governance_2026_06_19b). PRIOR FRONTIER V3-EXQ-485g RAN FAIL 2026-06-19T14:54Z on ree-cloud-3 (supersedes V3-EXQ-485f; trained-OFC-head behavioural arm, claim_ids=[SD-033b, MECH-263]). Readiness MET this time (the 485f vacuity fix worked: OFC bias cross-candidate range 0.171 >= the re-aligned 0.05 DV floor; head genuinely trained, weight-delta 6.32, 120 grad updates / 3683 outcome-coupled loss terms) but the load-bearing behavioural DVs FAIL (C1 devaluation_selection_shift {0.001,0.0,0.010} << 0.05; C2 between-context TV ~0). The trained head produced real cross-candidate bias RANGE with ZERO behavioural conversion -- the MECH-439 F-dominance conversion-ceiling signature (F ~88-89% of E3 committed-selection variance, V3-EXQ-571). FLAGGED for /failure-autopsy by governance-20260619T1455Z (user-confirmed): the self-stamped weakens was NEUTRALIZED to non_contributory pending adjudication of genuine-weakens vs conversion-ceiling/substrate_ceiling; SD-033b/MECH-263 exp_conf 0.325->0.0, conflict-resolution rec auto-resolved, both stay pending_retest_after_substrate. NOT marked reviewed (stays in pending_review until the autopsy resolves). 485f marked superseded. Lineage owner advanced 485f -> 485g. PREDECESSORS: 485e (FAIL/non_contributory, autopsied 2026-06-11), 485d (substrate-readiness diagnostic), 485c/485b representation-level MECH-263 diagnostics PASS 2026-06-04 (NOT a supersession lineage).
Claims: SD-033b, MECH-263
Why now: Trained-OFC-head SUBSTRATE landed 2026-06-09 (ree-v3 382db2c): OFCConfig.train_state_bias_head / REEConfig.ofc_train_state_bias_head (default False -> last Linear zeroed, bit-identical OFF) + OFCAnalog.bias_head_parameters(); the SD-033b an

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260621-046 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** drives_motivation_v4:DRV-3
- **Why now:** Plan gap closed on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-046
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

### IGW-20260621-054 -- Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** ethics_as_coherence_v5:ETH-8
- **Why now:** Plan gap closed on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-054
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

### IGW-20260621-076 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-076
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

### IGW-20260621-077 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-077
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

### IGW-20260621-134 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-134
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

### IGW-20260621-149 -- Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-6
- **Why now:** Plan gap closed on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-149
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

### IGW-20260621-159 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** self_model_v4:SELF-4
- **Owner EXQ:** V4-EXQ-001
- **Why now:** AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-159
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

### IGW-20260621-011 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-011
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

### IGW-20260621-012 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-012
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

### IGW-20260621-018 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-018
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

### IGW-20260621-024 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-024
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

### IGW-20260621-025 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-025
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

### IGW-20260621-035 -- Attention (distributed precision-selection) grounding -- containment, not a module

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** biology_grounding_convergence_v4:BG-6
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-035
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

### IGW-20260621-036 -- Ethics / commitment policy grounding (or honest 'no clean analog')

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** biology_grounding_convergence_v4:BG-7
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-036
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

### IGW-20260621-043 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [open]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-043
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

### IGW-20260621-044 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-044
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

### IGW-20260621-053 -- Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** ethics_as_coherence_v5:ETH-6
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-053
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

### IGW-20260621-063 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-063
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

### IGW-20260621-066 -- V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-4
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-066
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

### IGW-20260621-067 -- Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** grammar_primitive_mining_v6:GRAM-5
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-067
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

### IGW-20260621-074 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-074
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

### IGW-20260621-075 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-075
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

### IGW-20260621-109 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-109
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

### IGW-20260621-115 -- Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-6
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-115
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

### IGW-20260621-122 -- Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** multi_agent_ecology_v5:MAE-6
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-122
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

### IGW-20260621-156 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260621-156
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
