# Inter-Governance Workset

Generated: `2026-07-18T07:51:52Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **231** (ready 23, in_flight 0, blocked 148)
- By generation: meta 4, process 2, v3 84, v4 78, v5 38, v6 25
- Pending review: **2**
- Queue pending (unclaimed): **2**

- Auto-absorbed retests (queued, suppressed from workset): MECH-457 -> V3-EXQ-780

## Work packages

### IGW-20260718-001 -- Complete governance review (2 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1 | **Generation:** v3
- **Why now:** pending_review.md lists 2 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-001
Title: Complete governance review (2 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 2 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-002 -- Governance decision: INV-088

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 8 | **Generation:** v3
- **Why now:** promotion_demotion recommends hold_candidate_resolve_conflict.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-002
Title: Governance decision: INV-088
Lane: governance | Skill: /governance
Status: ready
Claims: INV-088
Why now: promotion_demotion recommends hold_candidate_resolve_conflict.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-187 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-187
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

### IGW-20260718-189 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: V3-EXQ-603l scored 4-arm escape-affordance-bridge behavioural validation must clear G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY before ready=True. Both non-vacuity readiness prereqs are now GREEN: relief ha; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-189
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

### IGW-20260718-191 -- Implement substrate: ARC-062 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-191
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

### IGW-20260718-192 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-192
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

### IGW-20260718-193 -- Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: RECOMPUTED 2026-07-06 (session ecstatic-pare-45f7ad). Both selection-face levers are BUILT + VALIDATED + PROMOTED-provisional: MECH-448 (demotion; V3-EXQ-689d PASS, promoted governance-cycle-20260621T
- **Why now:** substrate_queue entry status=mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substr

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-193
Title: Implement substrate: f_dominance_conversion_ceiling (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260
Blocked by: ready_blocked_by: RECOMPUTED 2026-07-06 (session ecstatic-pare-45f7ad). Both selection-face levers are BUILT + VALIDATED + PROMOTED-provisional: MECH-448 (demotion; V3-EXQ-689d PASS, promoted governance-cycle-20260621T
Why now: substrate_queue entry status=mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substr

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-197 -- Implement substrate: v4_loop_segregation (unblocks ARC-108)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: V3-generation substrate (REAPPOINTED V4->V3 2026-06-24, user-directed): recouped onto the V3 critical path because it attacks MECH-439, the standing V3 conversion-ceiling closure blocker. Built/V3-fro; ARC-109 [no-substrate-entry]: ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry]: MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry]: MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
- **Why now:** substrate_queue entry status=implemented with 4 unresolved prerequisite(s); blocks retest of ARC-108. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-197
Title: Implement substrate: v4_loop_segregation (unblocks ARC-108)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-439, ARC-108, MECH-450, ARC-110, MECH-451, MECH-314
Blocked by: ready_blocked_by: V3-generation substrate (REAPPOINTED V4->V3 2026-06-24, user-directed): recouped onto the V3 critical path because it attacks MECH-439, the standing V3 conversion-ceiling closure blocker. Built/V3-fro; ARC-109 [no-substrate-entry]: ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry]: MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry]: MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
Why now: substrate_queue entry status=implemented with 4 unresolved prerequisite(s); blocks retest of ARC-108. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-200 -- Implement substrate: SD-MEL-CONSUMER (unblocks INV-050)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of INV-050. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-200
Title: Implement substrate: SD-MEL-CONSUMER (unblocks INV-050)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: INV-050, MECH-180
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of INV-050. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-091 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-2
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-091
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

### IGW-20260718-102 -- Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-2
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-102
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

### IGW-20260718-142 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-2
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-142
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

### IGW-20260718-149 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-149
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

### IGW-20260718-183 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25 | **Generation:** v3
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-183
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

### IGW-20260718-184 -- Substrate (blocked): scaffolded_sd054_onboarding

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25 | **Generation:** v3
- **Blocked by:** SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-184
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

### IGW-20260718-186 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-186
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

### IGW-20260718-188 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-188
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

### IGW-20260718-190 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 4 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-190
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-062
Blocked by: ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 4 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-194 -- Retest after substrate: ARC-063

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-194
Title: Retest after substrate: ARC-063
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-063
Blocked by: f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
Why now: Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-195 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-195
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

### IGW-20260718-196 -- Retest after substrate: ARC-108

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** v4_loop_segregation [implemented]; ARC-109 [no-substrate-entry] (transitive via v4_loop_segregation): ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
- **Why now:** Blocked by 4 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-196
Title: Retest after substrate: ARC-108
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-108
Blocked by: v4_loop_segregation [implemented]; ARC-109 [no-substrate-entry] (transitive via v4_loop_segregation): ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
Why now: Blocked by 4 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-198 -- Retest after substrate: ARC-110

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** v4_loop_segregation [implemented]; ARC-109 [no-substrate-entry] (transitive via v4_loop_segregation): ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
- **Why now:** Blocked by 4 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-198
Title: Retest after substrate: ARC-110
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-110
Blocked by: v4_loop_segregation [implemented]; ARC-109 [no-substrate-entry] (transitive via v4_loop_segregation): ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
Why now: Blocked by 4 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-199 -- Retest after substrate: INV-050

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** SD-MEL-CONSUMER [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-199
Title: Retest after substrate: INV-050
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: INV-050
Blocked by: SD-MEL-CONSUMER [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-201 -- Retest after substrate: INV-089

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28 | **Generation:** v3
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-201
Title: Retest after substrate: INV-089
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-089
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-202 -- Retest after substrate: MECH-095

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** not v3-testable: MECH-095 epistemic_category=substrate_ceiling
- **Why now:** Held by the governance V3-pending gate (MECH-095 epistemic_category=substrate_ceiling) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-202
Title: Retest after substrate: MECH-095
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-095
Blocked by: not v3-testable: MECH-095 epistemic_category=substrate_ceiling
Why now: Held by the governance V3-pending gate (MECH-095 epistemic_category=substrate_ceiling) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-016 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Why now:** V3-EXQ-654h QUEUED + PENDING 2026-06-21 (pending on ree-cloud-3; supersedes V3-EXQ-654g). The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (pro

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-016
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-B
Claims: MECH-309, ARC-062
Why now: V3-EXQ-654h QUEUED + PENDING 2026-06-21 (pending on ree-cloud-3; supersedes V3-EXQ-654g). The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (pro

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-028 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Why now:** MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-028
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Claims: MECH-341, ARC-062, ARC-065
Why now: MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-030 -- F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-I
- **Why now:** CEILING LIFTED 2026-06-21 (V3-EXQ-689d PASS) -- DOWNSTREAM RETESTS NOW UNBLOCKED. The conflict-grade near-tie parametric family was exhausted by 689a (A1B1 0/3); the constitutional rung-2 build (rank-preserving F->eligibility demotion, MECH

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-030
Title: F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-I
Claims: MECH-439, MECH-309, ARC-062, ARC-063, MECH-263, MECH-260, Q-045, SD-037, MECH-445, MECH-446
Why now: CEILING LIFTED 2026-06-21 (V3-EXQ-689d PASS) -- DOWNSTREAM RETESTS NOW UNBLOCKED. The conflict-grade near-tie parametric family was exhausted by 689a (A1B1 0/3); the constitutional rung-2 build (rank-preserving F->eligibility demotion, MECH

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-031 -- ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-K
- **Why now:** EXHAUSTED 2026-07-06 -- no further work owed. The cross-loop-arbitration-REWEIGHTING conversion route this node owned (learned gating 709 / ascending-spiral 711 / bounded parity controller 713) ran to terminal and does NOT convert committed

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-031
Title: ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): behavioral_diversity_isolation:GAP-K
Claims: MECH-439, ARC-108, MECH-450
Why now: EXHAUSTED 2026-07-06 -- no further work owed. The cross-loop-arbitration-REWEIGHTING conversion route this node owned (learned gating 709 / ascending-spiral 711 / bounded parity controller 713) ran to terminal and does NOT convert committed

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-032 -- Action selector (E3) grounding L2 -> L3 [V3 instance -- mirrors GAP-I (falsifier front) + GAP-J (build front)]

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-2
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-032
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

### IGW-20260718-040 -- Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:CAMPAIGN
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-040
Title: Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:CAMPAIGN
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-041 -- Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P-comp
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-041
Title: Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:P-comp
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-042 -- Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-comm

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P2-rootC
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-042
Title: Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-comm
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:P2-rootC
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-044 -- The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:FULLSTACK
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-044
Title: The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, 
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:FULLSTACK
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-045 -- Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was n

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P4-learned-gating
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-045
Title: Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was n
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:P4-learned-gating
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-046 -- GENERATION face (the missing 6th face, MECH-458): per-candidate strategy diversity may be generation-LIMITED, not merely

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:GENERATION
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-046
Title: GENERATION face (the missing 6th face, MECH-458): per-candidate strategy diversity may be generation-LIMITED, not merely
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:GENERATION
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-136 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap blocked_pending_substrate on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-136
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

### IGW-20260718-158 -- Capability floor before structure -- isolate can-it-act from does-structure-help

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** meta
- **Gap(s):** WS-1
- **Why now:** Plan gap in_progress on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-158
Title: Capability floor before structure -- isolate can-it-act from does-structure-help
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): WS-1
Why now: Plan gap in_progress on ree_ai_design_critique.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ree_ai_design_critique_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-168 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625e RAN TERMINAL FAIL/non_contributory 2026-06-20 (run_id v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3; reviewed; removed from queue). CONFIRMED failure_autopsy_V3-EXQ-625e_2026-06-20: the recalibrated axis-(b) MEASUREMENT threat still could not clear candidate-pool collapse -- z_harm_a remained pinned (0 crossings of 0.4), R3 conversion 1/3, R4 committed-entropy 0/3 -- because the 569i conversion PASS is ENV-CONDITIONAL and does NOT propagate to a threat-engaged candidate pool. The autopsy consolidated 625e into the MECH-439 F-dominance conversion-ceiling cluster (governance 46816d2f1a). The R3/R4 non-vacuity guards fired (self-routed substrate_not_ready_requeue, NEVER a weakens). SD-037/MECH-280/MECH-281 UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). PROMOTES NOTHING.
- **Why now:** RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-168
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

### IGW-20260718-176 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-3
- **Why now:** AWAITING V4-EXQ-003 RUN + REVIEW (DR-10 pilot). On PASS (a decisive per-candidate self-viability changes selection vs OFF): the z_self-in-E3 viability wiring is live; the ecological z_self-derived auto-source is the next build, and DR-10 + 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-176
Title: z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): self_model_v4:SELF-3
Claims: MECH-215, ARC-081
Why now: AWAITING V4-EXQ-003 RUN + REVIEW (DR-10 pilot). On PASS (a decisive per-candidate self-viability changes selection vs OFF): the z_self-in-E3 viability wiring is live; the ecological z_self-derived auto-source is the next build, and DR-10 + 

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-119 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-119
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

### IGW-20260718-159 -- Ceiling-claim demotion rule (new GOV-* pre-registered falsification/demotion rule)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** meta
- **Gap(s):** WS-2
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-159
Title: Ceiling-claim demotion rule (new GOV-* pre-registered falsification/demotion rule)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): WS-2
Why now: Plan gap open on ree_ai_design_critique.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ree_ai_design_critique_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-185 -- Queue depth low (2 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35 | **Generation:** v3
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-185
Title: Queue depth low (2 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-003 -- Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-2
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-003
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

### IGW-20260718-007 -- Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-6
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-007
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

### IGW-20260718-008 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-008
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

### IGW-20260718-021 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-021
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

### IGW-20260718-022 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-022
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

### IGW-20260718-047 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-047
Title: Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-2
Claims: Q-068
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-048 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-048
Title: PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-3
Claims: ARC-090
Blocked by: developmental_dmn_v4:DMN-2 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-053 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** drives_motivation_v4:DRV-2
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-053
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

### IGW-20260718-057 -- Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-1
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-057
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

### IGW-20260718-058 -- Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-2
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-058
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

### IGW-20260718-059 -- Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-3
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-059
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

### IGW-20260718-064 -- Stream-binding mechanism: route own motivational-affective streams across the other-model

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-3
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-064
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

### IGW-20260718-065 -- Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-4
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-065
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

### IGW-20260718-068 -- Experiment A -- REE-native J-lens dispositional readout (does REE have a J-space?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:A
- **Why now:** Plan gap blocked on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-068
Title: Experiment A -- REE-native J-lens dispositional readout (does REE have a J-space?)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): global_workspace_jlens:A
Claims: SD-064, MECH-191
Why now: Plan gap blocked on global_workspace_jlens.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/global_workspace_jlens_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-070 -- Experiment B -- workspace-ablation cliff (cliff vs graceful degradation; the SD-064 falsifier)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:B
- **Blocked by:** global_workspace_jlens:GATE-B [open]
- **Why now:** Resume ONLY after GATE-B builds + smoke-tests the SD-027/MECH-254 V3 top-k access gate. Then queue the MECH-254 four-cell factorial {gate off, gate only, template only, both on} in a task that REQUIRES multi-step committed-action integratio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-070
Title: Experiment B -- workspace-ablation cliff (cliff vs graceful degradation; the SD-064 falsifier)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): global_workspace_jlens:B
Claims: SD-064, SD-027, MECH-254
Blocked by: global_workspace_jlens:GATE-B [open]
Why now: Resume ONLY after GATE-B builds + smoke-tests the SD-027/MECH-254 V3 top-k access gate. Then queue the MECH-254 four-cell factorial {gate off, gate only, template only, both on} in a task that REQUIRES multi-step committed-action integratio

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/global_workspace_jlens_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-072 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-072
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

### IGW-20260718-078 -- Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-3
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-078
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

### IGW-20260718-081 -- Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-6
- **Blocked by:** grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-081
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

### IGW-20260718-082 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-082
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

### IGW-20260718-083 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-083
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

### IGW-20260718-092 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-092
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

### IGW-20260718-094 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-094
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

### IGW-20260718-097 -- Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-1
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-097
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

### IGW-20260718-098 -- Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-2
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]
- **Why now:** Plan gap open on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-098
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

### IGW-20260718-099 -- The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-3
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-099
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

### IGW-20260718-103 -- Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-3
- **Blocked by:** language_emergence_bootstrap_v6:LANG-2 [open]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-103
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

### IGW-20260718-104 -- Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-4
- **Blocked by:** language_emergence_bootstrap_v6:LANG-3 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-104
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

### IGW-20260718-108 -- Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-2
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-108
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

### IGW-20260718-109 -- Deception detection / honest-signal pressure (deception = modelling another model)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-3
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-109
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

### IGW-20260718-112 -- Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-1
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-112
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

### IGW-20260718-113 -- Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-2
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-113
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

### IGW-20260718-114 -- Live unethical affordance: harmful action representable as a chooseable possibility (not absent)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-3
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-114
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

### IGW-20260718-115 -- Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-4
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-115
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

### IGW-20260718-117 -- Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-6
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-117
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

### IGW-20260718-122 -- Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-1
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-122
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

### IGW-20260718-123 -- Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-2
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-1 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-123
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

### IGW-20260718-124 -- Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-3
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-124
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

### IGW-20260718-125 -- Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-4
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-125
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

### IGW-20260718-129 -- Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-1
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-129
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

### IGW-20260718-130 -- Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-2
- **Blocked by:** multi_agent_ecology_v5:MAE-1 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-130
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

### IGW-20260718-137 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-137
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

### IGW-20260718-141 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-141
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

### IGW-20260718-152 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-152
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

### IGW-20260718-154 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-154
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

### IGW-20260718-155 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-155
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

### IGW-20260718-162 -- Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-1
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-162
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

### IGW-20260718-165 -- Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-4
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-165
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

### IGW-20260718-175 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-2
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-175
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

### IGW-20260718-009 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-009
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

### IGW-20260718-033 -- Commitment / de-commit latch grounding L1 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-3
- **Blocked by:** biology_grounding_convergence_v4:BG-2 [in_progress]
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-033
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

### IGW-20260718-037 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-4
- **Why now:** Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN ter

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-037
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): commitment_closure:GAP-4
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342
Why now: Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN ter

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-056 -- Phase 2 (Option B): pairwise MRF + damped loopy belief propagation, additive output schema, evidence-flow animation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** meta
- **Gap(s):** PHASE-2
- **Why now:** Plan gap in_progress on epistemic_overlay.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-056
Title: Phase 2 (Option B): pairwise MRF + damped loopy belief propagation, additive output schema, evidence-flow animation
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): PHASE-2
Why now: Plan gap in_progress on epistemic_overlay.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/epistemic_overlay_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-182 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** upstream_blocked | **Priority:** 40 | **Generation:** v3
- **Gap(s):** sleep_substrate:GAP-2
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-182
Title: SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A
Lane: plan | Skill: (plan reconcile)
Status: upstream_blocked
Gap(s): sleep_substrate:GAP-2
Claims: SD-017, ARC-045, MECH-166
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sleep_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-203 -- Proposal for MECH-177

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40 | **Generation:** v3
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-203
Title: Proposal for MECH-177
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-177
Proposal backlog id (stable): EVB-0119
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-204 -- Proposal for MECH-244

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40 | **Generation:** v3
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-204
Title: Proposal for MECH-244
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-244
Proposal backlog id (stable): EVB-0121
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-205 -- Proposal for MECH-245

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40 | **Generation:** v3
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-205
Title: Proposal for MECH-245
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-245
Proposal backlog id (stable): EVB-0122
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-206 -- Proposal for INV-041

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40 | **Generation:** v3
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-206
Title: Proposal for INV-041
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-041
Proposal backlog id (stable): EVB-0316
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-207 -- Proposal for INV-056

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40 | **Generation:** v3
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-207
Title: Proposal for INV-056
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-056
Proposal backlog id (stable): EVB-0317
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-077 -- Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-2
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-077
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

### IGW-20260718-096 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-7
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-096
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

### IGW-20260718-153 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-153
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

### IGW-20260718-160 -- Minimal 2-agent world (put any load on the ethics thesis, currently V5-only)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v5
- **Gap(s):** WS-10
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-160
Title: Minimal 2-agent world (put any load on the ethics thesis, currently V5-only)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): WS-10
Why now: Plan gap open on ree_ai_design_critique.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ree_ai_design_critique_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-161 -- Early-gating vs late-judging demo (REE early commit-gating beats a Constitutional-AI-style late judge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** meta
- **Gap(s):** WS-11
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-161
Title: Early-gating vs late-judging demo (REE early commit-gating beats a Constitutional-AI-style late judge)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): WS-11
Why now: Plan gap open on ree_ai_design_critique.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/ree_ai_design_critique_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-004 -- Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-3
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-004
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

### IGW-20260718-005 -- Analogy / structure-mapping across grounded domains (relational alignment, not surface match)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-4
- **Blocked by:** abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-005
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

### IGW-20260718-006 -- Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-5
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-006
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

### IGW-20260718-010 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-010
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

### IGW-20260718-011 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-011
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

### IGW-20260718-014 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]; affect_expression_v4:AE-10 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-014
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

### IGW-20260718-015 -- Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-10
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-015
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

### IGW-20260718-023 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-023
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

### IGW-20260718-024 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-024
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

### IGW-20260718-049 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-049
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

### IGW-20260718-050 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-050
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

### IGW-20260718-055 -- Orienting/surveying drive: pre-approach active-sensing control state

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** drives_motivation_v4:DRV-4
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-055
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

### IGW-20260718-060 -- Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-4
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-060
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

### IGW-20260718-061 -- Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-5
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-061
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

### IGW-20260718-066 -- Residue-aware social repair: regret-residue after exploitation generates a repair-goal

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-5
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-066
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

### IGW-20260718-067 -- Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-6
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-067
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

### IGW-20260718-069 -- SD-027 / MECH-254 V3 boundary top-k access-gate build (use_boundary_access_gate, no-op-default)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:GATE-B
- **Blocked by:** global_workspace_jlens:A [blocked]
- **Why now:** Plan gap open on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-069
Title: SD-027 / MECH-254 V3 boundary top-k access-gate build (use_boundary_access_gate, no-op-default)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): global_workspace_jlens:GATE-B
Claims: SD-064, SD-027, MECH-254
Blocked by: global_workspace_jlens:A [blocked]
Why now: Plan gap open on global_workspace_jlens.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/global_workspace_jlens_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-073 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-073
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

### IGW-20260718-074 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-074
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

### IGW-20260718-075 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-075
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

### IGW-20260718-084 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-084
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

### IGW-20260718-085 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-085
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

### IGW-20260718-086 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-086
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

### IGW-20260718-093 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-093
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

### IGW-20260718-095 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-095
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

### IGW-20260718-100 -- Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-4
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-100
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

### IGW-20260718-101 -- Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-5
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-101
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

### IGW-20260718-105 -- Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-5
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-105
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

### IGW-20260718-106 -- Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-6
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-106
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

### IGW-20260718-107 -- Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-7
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-107
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

### IGW-20260718-110 -- Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-4
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-110
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

### IGW-20260718-111 -- Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-5
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-111
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

### IGW-20260718-116 -- Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-5
- **Blocked by:** loveability_ethical_agency_v5:LOVE-4 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-116
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

### IGW-20260718-118 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-118
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

### IGW-20260718-120 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-120
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

### IGW-20260718-126 -- Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-5
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
- **Why now:** Plan gap open on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-126
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

### IGW-20260718-128 -- Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-7
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-128
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

### IGW-20260718-131 -- Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-3
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-131
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

### IGW-20260718-132 -- Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-4
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-132
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

### IGW-20260718-133 -- Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-5
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-133
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

### IGW-20260718-135 -- ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-7
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-135
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

### IGW-20260718-138 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-138
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

### IGW-20260718-139 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-139
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

### IGW-20260718-140 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-140
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

### IGW-20260718-143 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-143
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

### IGW-20260718-144 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-144
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

### IGW-20260718-145 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-145
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

### IGW-20260718-150 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-150
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

### IGW-20260718-151 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-151
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

### IGW-20260718-156 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-156
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

### IGW-20260718-157 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-157
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

### IGW-20260718-163 -- Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-2
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-163
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

### IGW-20260718-164 -- Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-3
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-164
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

### IGW-20260718-166 -- Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-5
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-4 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-166
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

### IGW-20260718-169 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [assembling]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-169
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

### IGW-20260718-170 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-170
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

### IGW-20260718-171 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-171
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

### IGW-20260718-172 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-172
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

### IGW-20260718-173 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-173
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

### IGW-20260718-178 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-3 [in_progress]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-178
Title: z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-5
Claims: MECH-214
Blocked by: self_model_v4:SELF-3 [in_progress]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-179 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-179
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

### IGW-20260718-180 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-3 [in_progress]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-180
Title: Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_model_v4:SELF-7
Claims: INV-064
Blocked by: self_model_v4:SELF-3 [in_progress]
Why now: Plan gap blocked on self_model_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-017 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-017
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-018 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-018
Title: ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-I
Claims: ARC-064, MECH-318
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-020 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-020
Title: MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-K
Claims: MECH-319
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
Why now: IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-027 -- Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imaginat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-9
- **Why now:** Plan gap closed on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-027
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

### IGW-20260718-029 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Why now:** REFRESHED 2026-06-27 (the stale '603q is QUEUED / AWAITING RUN+REVIEW' framing below is SUPERSEDED -- V3-EXQ-603q RAN PASS 2026-06-17, SD-059/MECH-358 settled). CURRENT STATE: the survival/harm-pathway prereq is CLEARED; the 687 frontier RA

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-029
Title: Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-C
Claims: MECH-313, MECH-260, Q-045
Why now: REFRESHED 2026-06-27 (the stale '603q is QUEUED / AWAITING RUN+REVIEW' framing below is SUPERSEDED -- V3-EXQ-603q RAN PASS 2026-06-17, SD-059/MECH-358 settled). CURRENT STATE: the survival/harm-pathway prereq is CLEARED; the 687 frontier RA

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-034 -- Goal / wanting layer grounding L1 -> L2 [L2 REACHED 2026-07-07 via on-file anchors]

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-5
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-034
Title: Goal / wanting layer grounding L1 -> L2 [L2 REACHED 2026-07-07 via on-file anchors]
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): biology_grounding_convergence_v4:BG-5
Why now: Plan gap in_progress on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-038 -- OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + ME

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-4-battery
- **Blocked by:** commitment_closure:GAP-4 [in_progress]
- **Why now:** 466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-038
Title: OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + ME
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): commitment_closure:GAP-4-battery
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-342
Blocked by: commitment_closure:GAP-4 [in_progress]
Why now: 466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which th

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-039 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-8
- **Why now:** OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabl

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-039
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): commitment_closure:GAP-8
Claims: SD-033b, MECH-263
Why now: OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabl

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-043 -- Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P3-ofc
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-043
Title: Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): conversion_ceiling_campaign:P3-ofc
Why now: Plan gap assembling on conversion_ceiling_campaign.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/conversion_ceiling_campaign_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-054 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v4
- **Gap(s):** drives_motivation_v4:DRV-3
- **Why now:** Plan gap closed on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-054
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

### IGW-20260718-063 -- Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-8
- **Why now:** Plan gap closed on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-063
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

### IGW-20260718-089 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** infant_substrate:GAP-13
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-089
Title: EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): infant_substrate:GAP-13
Claims: DEV-NEED-003, MECH-314
Why now: Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-090 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 50 | **Generation:** v3
- **Gap(s):** infant_substrate:GAP-14
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-090
Title: EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-14
Claims: DEV-NEED-008, ARC-046
Why now: 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-146 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-146
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

### IGW-20260718-147 -- Unify the pack skeleton (sync build_runpack_docs + pack_writer.write_pack delegate to one shared skeleton)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** parked | **Priority:** 50 | **Generation:** process
- **Gap(s):** STEP-7.1
- **Why now:** Plan gap parked on pack_writer_single_writer_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-147
Title: Unify the pack skeleton (sync build_runpack_docs + pack_writer.write_pack delegate to one shared skeleton)
Lane: plan | Skill: (plan reconcile)
Status: parked
Gap(s): STEP-7.1
Why now: Plan gap parked on pack_writer_single_writer_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/pack_writer_single_writer_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-148 -- Carry the always-core through sync into the pack (substrate_hash/config/seeds/machine/elapsed_seconds + rich governance 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** parked_indefinite | **Priority:** 50 | **Generation:** process
- **Gap(s):** STEP-7.2
- **Why now:** Plan gap parked_indefinite on pack_writer_single_writer_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-148
Title: Carry the always-core through sync into the pack (substrate_hash/config/seeds/machine/elapsed_seconds + rich governance 
Lane: plan | Skill: (plan reconcile)
Status: parked_indefinite
Gap(s): STEP-7.2
Why now: Plan gap parked_indefinite on pack_writer_single_writer_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/pack_writer_single_writer_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-167 -- Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-6
- **Why now:** Plan gap closed on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-167
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

### IGW-20260718-177 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-4
- **Why now:** AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-177
Title: E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): self_model_v4:SELF-4
Claims: MECH-215
Why now: AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_model_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-181 -- Own-future-option uncertainty: does REE need an explicit self-model of its OWN future option-space (second-order uncerta

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-9
- **Why now:** Plan gap assembling on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-181
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

### IGW-20260718-208 -- Confirm evidence: MECH-163 (lit 0.89, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.89, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-208
Title: Confirm evidence: MECH-163 (lit 0.89, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-163
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.89, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-209 -- Confirm evidence: MECH-203 (lit 0.88, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-209
Title: Confirm evidence: MECH-203 (lit 0.88, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-203
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-210 -- Confirm evidence: MECH-166 (lit 0.88, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-210
Title: Confirm evidence: MECH-166 (lit 0.88, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-166
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-211 -- Confirm evidence: MECH-122 (lit 0.88, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-211
Title: Confirm evidence: MECH-122 (lit 0.88, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-122
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-212 -- Confirm evidence: MECH-292 (lit 0.88, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-212
Title: Confirm evidence: MECH-292 (lit 0.88, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-292
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.88, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-213 -- Confirm evidence: MECH-267 (lit 0.87, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-213
Title: Confirm evidence: MECH-267 (lit 0.87, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-267
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-214 -- Confirm evidence: MECH-293 (lit 0.87, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-214
Title: Confirm evidence: MECH-293 (lit 0.87, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-293
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-215 -- Confirm evidence: SD-014 (lit 0.87, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-215
Title: Confirm evidence: SD-014 (lit 0.87, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-014
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-216 -- Confirm evidence: MECH-191 (lit 0.87, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-216
Title: Confirm evidence: MECH-191 (lit 0.87, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-191
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-217 -- Confirm evidence: MECH-074 (lit 0.87, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-217
Title: Confirm evidence: MECH-074 (lit 0.87, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-074
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.87, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-218 -- Confirm evidence: SD-039 (lit 0.86, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.86, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-218
Title: Confirm evidence: SD-039 (lit 0.86, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-039
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.86, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-219 -- Confirm evidence: MECH-269 (lit 0.85, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.85, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-219
Title: Confirm evidence: MECH-269 (lit 0.85, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-269
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.85, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-220 -- Confirm evidence: INV-064 (lit 0.85, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.85, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-220
Title: Confirm evidence: INV-064 (lit 0.85, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-064
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.85, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-221 -- Confirm evidence: MECH-282 (lit 0.83, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.83, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-221
Title: Confirm evidence: MECH-282 (lit 0.83, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-282
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.83, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-222 -- Confirm evidence: MECH-286 (lit 0.82, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.82, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-222
Title: Confirm evidence: MECH-286 (lit 0.82, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-286
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.82, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-223 -- Confirm evidence: MECH-074d (lit 0.81, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.81, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-223
Title: Confirm evidence: MECH-074d (lit 0.81, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-074d
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.81, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-224 -- Confirm evidence: SD-036 (lit 0.81, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.81, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-224
Title: Confirm evidence: SD-036 (lit 0.81, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-036
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.81, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-225 -- Confirm evidence: MECH-338 (lit 0.80, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.80, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-225
Title: Confirm evidence: MECH-338 (lit 0.80, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-338
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.80, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-226 -- Confirm evidence: MECH-232 (lit 0.79, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.79, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-226
Title: Confirm evidence: MECH-232 (lit 0.79, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-232
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.79, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-227 -- Confirm evidence: SD-055 (lit 0.76, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.76, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-227
Title: Confirm evidence: SD-055 (lit 0.76, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-055
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.76, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-228 -- Confirm evidence: MECH-074c (lit 0.76, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.76, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-228
Title: Confirm evidence: MECH-074c (lit 0.76, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-074c
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.76, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-229 -- Confirm evidence: SD-009 (lit 0.73, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.73, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-229
Title: Confirm evidence: SD-009 (lit 0.73, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-009
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.73, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-230 -- Confirm evidence: MECH-340 (lit 0.69, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.69, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-230
Title: Confirm evidence: MECH-340 (lit 0.69, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-340
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.69, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-231 -- Confirm evidence: MECH-339 (lit 0.68, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** surfaced | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.68, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-231
Title: Confirm evidence: MECH-339 (lit 0.68, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-339
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.68, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-012 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-012
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

### IGW-20260718-013 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-013
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

### IGW-20260718-019 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-019
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

### IGW-20260718-025 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-025
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

### IGW-20260718-026 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-026
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

### IGW-20260718-035 -- Attention (distributed precision-selection) grounding -- containment, not a module

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-6
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-035
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

### IGW-20260718-036 -- Ethics / commitment policy grounding (or honest 'no clean analog')

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-7
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-036
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

### IGW-20260718-051 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-051
Title: Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): developmental_dmn_v4:DMN-6
Claims: MECH-382
Blocked by: developmental_dmn_v4:DMN-2 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
Why now: Plan gap blocked on developmental_dmn_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/developmental_dmn_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-052 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-052
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

### IGW-20260718-062 -- Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-6
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-062
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

### IGW-20260718-071 -- MECH-191 cross-architecture legibility unblock check (does A's dispositional readout resolve the tonic-channel gap?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:MECH-191
- **Blocked by:** global_workspace_jlens:A [blocked]
- **Why now:** Plan gap open on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-071
Title: MECH-191 cross-architecture legibility unblock check (does A's dispositional readout resolve the tonic-channel gap?)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): global_workspace_jlens:MECH-191
Claims: MECH-191
Blocked by: global_workspace_jlens:A [blocked]
Why now: Plan gap open on global_workspace_jlens.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/global_workspace_jlens_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260718-076 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-076
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

### IGW-20260718-079 -- V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-4
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-079
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

### IGW-20260718-080 -- Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-5
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-080
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

### IGW-20260718-087 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-087
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

### IGW-20260718-088 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-088
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

### IGW-20260718-121 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-121
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

### IGW-20260718-127 -- Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-6
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-127
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

### IGW-20260718-134 -- Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-6
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-134
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

### IGW-20260718-174 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260718-174
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
