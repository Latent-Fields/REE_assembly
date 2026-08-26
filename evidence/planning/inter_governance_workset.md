# Inter-Governance Workset

Generated: `2026-08-26T08:04:24Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **242** (ready 22, in_flight 0, blocked 165)
- By generation: clinical 11, meta 4, process 13, v3 75, v4 76, v5 38, v6 25
- Pending review: **0**
- Queue pending (unclaimed): **0**

- Live EXQs: V3-EXQ-906c, V3-EXQ-949

- Evidence-covered retests (already ran post-substrate; held for a /governance disposition, NOT re-queued): MECH-074d -> v3_exq_894c_mech074d_bla_entropy_weight_sweep_20260810T212602Z_v3, MECH-152 -> v3_exq_922a_sd016_mech152_softsel_ablation_20260814T183708Z_v3, Q-081 -> v3_exq_865_q081_zgoal_reach_preflight_scan_20260801T221346Z_v3

## Work packages

### IGW-20260826-219 -- Implement substrate: SD-049-PHASE-2 (unblocks ARC-030)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3; free-text: V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric -- RAN 2026-06-20T22:30Z, PASS, evidence_direction=supports (v3_exq_514u_sd049_phase2_mec
- **Why now:** substrate_queue entry status=phase_2_implemented with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-219
Title: Implement substrate: SD-049-PHASE-2 (unblocks ARC-030)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030
Blocked by: ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3; free-text: V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric -- RAN 2026-06-20T22:30Z, PASS, evidence_direction=supports (v3_exq_514u_sd049_phase2_mec
Why now: substrate_queue entry status=phase_2_implemented with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-220 -- Implement substrate: SD-054 (unblocks ARC-030)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): the named gate RAN and d; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-220
Title: Implement substrate: SD-054 (unblocks ARC-030)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-054, MECH-309, ARC-062
Blocked by: ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): the named gate RAN and d; ARC-062 [implemented]
Why now: substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-221 -- Implement substrate: mech457_competence_bootstrap_explorer (unblocks ARC-030)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-229 [no-substrate-entry]: MECH-229
- **Why now:** substrate_queue entry status=blocked_pending_discrimination with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-221
Title: Implement substrate: mech457_competence_bootstrap_explorer (unblocks ARC-030)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-030, INV-034, INV-088, MECH-457, Q-021
Blocked by: ready=false (no ready_blocked_by detail); MECH-229 [no-substrate-entry]: MECH-229
Why now: substrate_queue entry status=blocked_pending_discrimination with 2 unresolved prerequisite(s); blocks retest of ARC-030. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-225 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs a V3-scoped substrate fix, not V4). OWNER CORRECTED 2026-08-0
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-225
Title: Implement substrate: ARC-046 (unblocks ARC-046)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-046, DEV-NEED-008
Blocked by: ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs a V3-scoped substrate fix, not V4). OWNER CORRECTED 2026-08-0
Why now: substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-227 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): V3-EXQ-603l is NOT in fl; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-227
Title: Implement substrate: escape-affordance-bridge (unblocks ARC-060)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-058, MECH-357, ARC-060, MECH-320, ARC-068, SD-054-readiness
Blocked by: ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): V3-EXQ-603l is NOT in fl; SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
Why now: substrate_queue entry status=IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-233 -- Implement substrate: v4_loop_segregation (unblocks ARC-108)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20 | **Generation:** v3
- **Blocked by:** ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): the pre-emption gate CLE; ARC-109 [no-substrate-entry]: ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry]: MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry]: MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
- **Why now:** substrate_queue entry status=implemented with 4 unresolved prerequisite(s); blocks retest of ARC-108. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-233
Title: Implement substrate: v4_loop_segregation (unblocks ARC-108)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-439, ARC-108, MECH-450, ARC-110, MECH-451, MECH-314
Blocked by: ready_blocked_by: STALE TEXT CORRECTED 2026-08-07T18:17Z (session metaworker-chip-20260807-substrate-queue-stale-gating-audit; companion sweep to the ARC-065 GAP-A fix REE_assembly ffb4dbc4fc): the pre-emption gate CLE; ARC-109 [no-substrate-entry]: ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry]: MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry]: MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
Why now: substrate_queue entry status=implemented with 4 unresolved prerequisite(s); blocks retest of ARC-108. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-096 -- Inferred state must not collapse to perceived observation (invariant)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-2
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-096
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

### IGW-20260826-107 -- Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-2
- **Why now:** Plan gap open on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-107
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

### IGW-20260826-148 -- PILLAR 1 -- token-instance object-file substrate (permanence through occlusion)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-2
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-148
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

### IGW-20260826-160 -- PILLAR A -- low-adaptor (smell/gradient) primitive: near-raw orientation signal as the earliest V4 sense

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 25 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-2
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-160
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

### IGW-20260826-214 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25 | **Generation:** v3
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-214
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

### IGW-20260826-215 -- Substrate (blocked): scaffolded_sd054_onboarding

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25 | **Generation:** v3
- **Blocked by:** SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-215
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

### IGW-20260826-216 -- Substrate (blocked): SD-SLEEP-ENTRY-PRESSURE

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25 | **Generation:** v3
- **Blocked by:** MECH-286 [no-substrate-entry]: MECH-286 sleep-onset gate re-shaping (synthesis Section 5.3 step 2 -- currently OFF because its threat term reads a chan; GAP-5b [no-substrate-entry]: GAP-5b ecological MEL producer (parked -- CausalGridWorldV2 MEL is noise-level, so any ecological validation of this bui
- **Why now:** substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-216
Title: Substrate (blocked): SD-SLEEP-ENTRY-PRESSURE
Lane: substrate | Skill: /implement-substrate
Status: blocked
Blocked by: MECH-286 [no-substrate-entry]: MECH-286 sleep-onset gate re-shaping (synthesis Section 5.3 step 2 -- currently OFF because its threat term reads a chan; GAP-5b [no-substrate-entry]: GAP-5b ecological MEL producer (parked -- CausalGridWorldV2 MEL is noise-level, so any ecological validation of this bui
Why now: substrate_queue ready=true but 2 unresolved prerequisite(s) -- see blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-218 -- Retest after substrate: ARC-030

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric -- RAN 2026-06-20T22:30Z, PASS, evidence_direction=supports (v3_exq_514u_sd049_phase2_mec; MECH-307 [implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); mech457_competence_bootstrap_explorer [blocked_pending_discrimination]; MECH-229 [no-substrate-entry] (transitive via mech457_competence_bootstrap_explorer): MECH-229
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 9 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-218
Title: Retest after substrate: ARC-030
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-030
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; free-text (via SD-049-PHASE-2): V3-EXQ-514u measurement-redesign continuous incentive-amplitude metric -- RAN 2026-06-20T22:30Z, PASS, evidence_direction=supports (v3_exq_514u_sd049_phase2_mec; MECH-307 [implemented]; scaffolded_sd054_onboarding [G1/G2/G3 ecological legs CLEARED 2026-06-10 (V3-EXQ-603m: P1 survival 3/3, P2 contact 3/3, P2 ecological consumption-gated z_goal 2/3; non-vacuity MET harm_eval range 0.075 + reached-P2-alive 3/3). Builds on the harm-pathway-survival leg VALIDATED 2026-06-09 (V3-EXQ-603k PASS). 603m FAILed the pre-registered gate at G0 ONLY -- the Stage-0 nursery positive control z_goal>0.4 held 1/3 (0.477/0.389/0.371), missing by 0.011/0.029. Confirmed autopsy failure_autopsy_V3-EXQ-603m_2026-06-10: G0 is a measurement/developmental-sequencing artifact (mature ecological 0.4 threshold applied to the un-warmed Stage-0 substrate; ecological P2 z_goal exceeds nursery z_goal for every seed), NOT a foraging/goal-formation failure. ready STAYS false: residual = the corrected-G0 re-validation V3-EXQ-603n (queued 2026-06-10; G0 measured post-Stage-0b-consolidation OR positive-control floor >0.3, G3 unchanged at the load-bearing ecological 0.4). RESOLVED 2026-06-11: V3-EXQ-603n PASSED (ree-cloud-2 2026-06-10T20:14:27Z) -- corrected G0 cleared 3/3 at the recalibrated Stage-0 positive-control floor 0.3, G3 held at the load-bearing ecological 0.4, all four legs >=2/3, non-vacuity met. ready FLIPPED true; see readiness_flip_2026_06_11. goal_pipeline:GAP-2 Stage B (SD-049 Phase-2 behavioural validation, V3-EXQ-514l successor) now queueable.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding); mech457_competence_bootstrap_explorer [blocked_pending_discrimination]; MECH-229 [no-substrate-entry] (transitive via mech457_competence_bootstrap_explorer): MECH-229
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 9 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-222 -- Retest after substrate: ARC-041

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** not v3-testable: ARC-041 epistemic_category=substrate_conditional
- **Why now:** Held by the governance V3-pending gate (ARC-041 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-222
Title: Retest after substrate: ARC-041
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-041
Blocked by: not v3-testable: ARC-041 epistemic_category=substrate_conditional
Why now: Held by the governance V3-pending gate (ARC-041 epistemic_category=substrate_conditional) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-223 -- Retest after substrate: ARC-045

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION [implemented_validated_result_non_contributory]; contextmemory-write-path-addressing-degeneracy [implemented_pending_validation]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-223
Title: Retest after substrate: ARC-045
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-045
Blocked by: MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION [implemented_validated_result_non_contributory]; contextmemory-write-path-addressing-degeneracy [implemented_pending_validation]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-224 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs a V3-scoped substrate fix, not V4). OWNER CORRECTED 2026-08-0
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-224
Title: Retest after substrate: ARC-046
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-046
Blocked by: ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs a V3-scoped substrate fix, not V4). OWNER CORRECTED 2026-08-0
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-226 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-226
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

### IGW-20260826-228 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054); f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 4 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-228
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

### IGW-20260826-229 -- Retest after substrate: ARC-063

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** f_dominance_conversion_ceiling [mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__mech449_gonogo_leg_BUILT_falsifier_V3_EXQ_689g_RAN_PASS_PROMOTED_provisional_2026_06_22__selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD__cross_loop_arbitration_reweighting_route_EXHAUSTED_709_711_713_autopsy_2026_07_05__no_new_build_owed__downstream_behavioural_retests_654h_485i_625e_RAN_FAIL_substrate_not_ready_requeue__445h_RAN_weakens__GAP_A_lift_generalisation_NOT_yet_demonstrated__decommit_release_duration_face_rung6_460_lineage_460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-229
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

### IGW-20260826-230 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** escape-affordance-bridge [IMPLEMENTED (affordance-indexed avoidance credit wired; MECH-302 relief half + MECH-303/304 safety half built+wired into instrumental avoidance). SAFETY HALF VALIDATED at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (trained safety_signal 0.893 >= 0.5 floor + under-threat gate 0.584 >= 0.1; load-bearing G1_on_safety_credits_via_trained_signal PASS; claim_ids=[], non_contributory, reviewed). Relief half already credited non-vacuously (603i relief_credit_frac 0.67). Both bridge halves now credit; the scored 4-arm behavioural validation V3-EXQ-603l (ARM_BASE_IA_ONLY / ARM_RELIEF_BRIDGE / ARM_SAFETY_BRIDGE / ARM_RELIEF_SAFETY_BRIDGE; G_H >= 2/3 AND G_H > ARM_BASE_IA_ONLY) is IN FLIGHT. ready STAYS false until 603l scores.]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built+wired; trained-signal validated V3-EXQ-603j); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-230
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

### IGW-20260826-231 -- Retest after substrate: ARC-070

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** not v3-testable: ARC-070 v3_pending
- **Why now:** Held by the governance V3-pending gate (ARC-070 v3_pending) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-231
Title: Retest after substrate: ARC-070
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-070
Blocked by: not v3-testable: ARC-070 v3_pending
Why now: Held by the governance V3-pending gate (ARC-070 v3_pending) -- a /queue-experiment cannot yield contributory evidence. See blocked_by. (R5; mirrors R1.)

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-232 -- Retest after substrate: ARC-108

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28 | **Generation:** v3
- **Blocked by:** v4_loop_segregation [implemented]; ARC-109 [no-substrate-entry] (transitive via v4_loop_segregation): ARC-109 (D1/D2 population split -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 2026-06-27;; MECH-452 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-452 (loop-local eligibility traces -- V3 built co-requisite, reappointed V4->V3 2026-06-24; built no-op-default 202; MECH-451 [no-substrate-entry] (transitive via v4_loop_segregation): MECH-451 (intermediate finer-channel falsifier -- V3 cheap rung; exhaust first, may pre-empt this build)
- **Why now:** Blocked by 4 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-232
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

### IGW-20260826-016 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Why now:** V3-EXQ-654h QUEUED + PENDING 2026-06-21 (pending on ree-cloud-3; supersedes V3-EXQ-654g). The MECH-439 F-dominance conversion ceiling has been LIFTED operationally by the MECH-448 (ARC-107) rank-preserving F->eligibility demotion lever (pro

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-016
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

### IGW-20260826-029 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Why now:** MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250). The only OPEN GAP-B strand is ARC-062: queue its falsifier ONLY after the shared GAP-A modulatory-bias-selection-authority substrate lands (the 569g->682-gated com

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-029
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

### IGW-20260826-032 -- F-dominance committed-selection variance monopoly (MECH-439) -- the GENERAL root behind GAP-A's local conversion ceiling

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-I
- **Why now:** CEILING LIFTED 2026-06-21 (V3-EXQ-689d PASS) -- DOWNSTREAM RETESTS NOW UNBLOCKED. The conflict-grade near-tie parametric family was exhausted by 689a (A1B1 0/3); the constitutional rung-2 build (rank-preserving F->eligibility demotion, MECH

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-032
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

### IGW-20260826-033 -- ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-K
- **Why now:** NOT EXHAUSTED -- CORRECTED 2026-08-12. Reopening requires a CORRECTED-DV INSTRUMENT, not a re-letter. The 2026-07-06 exhaustion recorded here was WITHDRAWN 2026-07-20 by confirmed failure_autopsy_V3-EXQ-711-713_2026-07-20 (REE_assembly acef

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-033
Title: ARC-108 learned cortico-striatal gating + MECH-450 recurrent-settling step -- the next MECH-439 attack after GAP-J. Turn
Lane: plan | Skill: (plan reconcile)
Status: assembling
Gap(s): behavioral_diversity_isolation:GAP-K
Claims: MECH-439, ARC-108, MECH-450
Why now: NOT EXHAUSTED -- CORRECTED 2026-08-12. Reopening requires a CORRECTED-DV INSTRUMENT, not a re-letter. The 2026-07-06 exhaustion recorded here was WITHDRAWN 2026-07-20 by confirmed failure_autopsy_V3-EXQ-711-713_2026-07-20 (REE_assembly acef

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-042 -- Umbrella: assemble the multi-face substrate that converts per-candidate diversity to committed-class diversity

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:CAMPAIGN
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-042
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

### IGW-20260826-043 -- Selection-face composition: does MECH-448 demotion x MECH-449 Go/No-Go compound or cancel at committed-class entropy (C2

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P-comp
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-043
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

### IGW-20260826-044 -- Commit-duration face (root C, MECH-445/446): de-commit authority on a substrate where natural-commit and closure-de-comm

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P2-rootC
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-044
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

### IGW-20260826-046 -- The real test: co-armed full-stack arm (demotion + Go/No-Go + floor + root-C + OFC ON), sweep use_candidate_rule_field, 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:FULLSTACK
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-046
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

### IGW-20260826-047 -- Learned-gating face (ARC-108 / MECH-450): make the ARC-107 arithmetic BG arbitration LEARNABLE. The selection face was n

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P4-learned-gating
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-047
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

### IGW-20260826-048 -- GENERATION face (the missing 6th face, MECH-458): per-candidate strategy diversity may be generation-LIMITED, not merely

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:GENERATION
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-048
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

### IGW-20260826-142 -- Substrate-vocabulary expansion is the gating fork (atomic-only V3 has no second granularity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 30 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-1
- **Why now:** Plan gap blocked_pending_substrate on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-142
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

### IGW-20260826-181 -- Capability floor before structure -- isolate can-it-act from does-structure-help

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** meta
- **Gap(s):** WS-1
- **Why now:** Plan gap in_progress on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-181
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

### IGW-20260826-191 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** assembling | **Priority:** 30 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625e RAN TERMINAL FAIL/non_contributory 2026-06-20 (run_id v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3; reviewed; removed from queue). CONFIRMED failure_autopsy_V3-EXQ-625e_2026-06-20: the recalibrated axis-(b) MEASUREMENT threat still could not clear candidate-pool collapse -- z_harm_a remained pinned (0 crossings of 0.4), R3 conversion 1/3, R4 committed-entropy 0/3 -- because the 569i conversion PASS is ENV-CONDITIONAL and does NOT propagate to a threat-engaged candidate pool. The autopsy consolidated 625e into the MECH-439 F-dominance conversion-ceiling cluster (governance 46816d2f1a). The R3/R4 non-vacuity guards fired (self-routed substrate_not_ready_requeue, NEVER a weakens). SD-037/MECH-280/MECH-281 UNWEAKENED (substrate_ceiling / pending_retest_after_substrate). PROMOTES NOTHING.
- **Why now:** RESUME the Phase 1b gate via a redesigned successor (V3-EXQ-625d, JOINT-COMPOSITE-ON) once behavioral_diversity_isolation demonstrates that scoring-layer diversity reaches COMMITTED ACTION (dynamic behavioural sequences) -- the GAP-A 569-li

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-191
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

### IGW-20260826-200 -- z_self enters E3 viability scoring (DR-10): bodily state modulates trajectory viability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-3
- **Why now:** AWAITING V4-EXQ-003 RUN + REVIEW (DR-10 pilot). On PASS (a decisive per-candidate self-viability changes selection vs OFF): the z_self-in-E3 viability wiring is live; the ecological z_self-derived auto-source is the next build, and DR-10 + 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-200
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

### IGW-20260826-210 -- Prerequisites + design finalization (WireGuard coverage audit, schema/endpoint spec, degrade-path spec)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 30 | **Generation:** process
- **Gap(s):** PHASE-0
- **Why now:** Plan gap in_progress on task_claim_chip_coordinator_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-210
Title: Prerequisites + design finalization (WireGuard coverage audit, schema/endpoint spec, degrade-path spec)
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): PHASE-0
Why now: Plan gap in_progress on task_claim_chip_coordinator_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-123 -- Wire agent-directed hazard pursuit into Stage-H onboarding curriculum; run the discrimination test agent-directed pursui

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** v3
- **Gap(s):** mech357_avoidance_efficacy:BUILD
- **Why now:** Plan gap open on mech357_avoidance_efficacy.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-123
Title: Wire agent-directed hazard pursuit into Stage-H onboarding curriculum; run the discrimination test agent-directed pursui
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): mech357_avoidance_efficacy:BUILD
Claims: MECH-357
Why now: Plan gap open on mech357_avoidance_efficacy.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/mech357_avoidance_efficacy_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-125 -- False-linking-risk / reality-coherence cost term (the single aspect with no REE home)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-3
- **Why now:** Plan gap open on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-125
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

### IGW-20260826-154 -- epistemic_deficit: persistent target-bound model-inadequacy accumulator

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** v3
- **Gap(s):** orienting_epistemic_deficit_v3:ORNT-2
- **Why now:** Two-step gate; neither step is owned today. (1) The design doc mech314bc_percandidate_extension_staged_2026-08-08.md receives its owed user review, releasing its follow-on routing. (2) The SD-063 E2WorldUncertaintyHead training loop lands a

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-154
Title: epistemic_deficit: persistent target-bound model-inadequacy accumulator
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): orienting_epistemic_deficit_v3:ORNT-2
Claims: MECH-482
Why now: Two-step gate; neither step is owned today. (1) The design doc mech314bc_percandidate_extension_staged_2026-08-08.md receives its owed user review, releasing its follow-on routing. (2) The SD-063 E2WorldUncertaintyHead training loop lands a

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/orienting_epistemic_deficit_v3_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-176 -- Frame-tag failure modes: derealization, delusion, commitment-gate (developmental etiology)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:FRAME-TAG
- **Why now:** Plan gap open on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-176
Title: Frame-tag failure modes: derealization, delusion, commitment-gate (developmental etiology)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): clinical_failure_modes:FRAME-TAG
Claims: INV-061, MECH-200, MECH-201, MECH-202
Why now: Plan gap open on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-182 -- Ceiling-claim demotion rule (new GOV-* pre-registered falsification/demotion rule)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** meta
- **Gap(s):** WS-2
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-182
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

### IGW-20260826-209 -- 185 of 269 remaining drift-candidate pairs (69%) record a substrate_hash but no substrate_commit.commit, so no diff exis

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 35 | **Generation:** process
- **Gap(s):** substrate_stability:substrate-commit-coverage
- **Why now:** Plan gap open on substrate_stability_and_drift_detection.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-209
Title: 185 of 269 remaining drift-candidate pairs (69%) record a substrate_hash but no substrate_commit.commit, so no diff exis
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): substrate_stability:substrate-commit-coverage
Why now: Plan gap open on substrate_stability_and_drift_detection.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-217 -- Queue depth low (0 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35 | **Generation:** v3
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-217
Title: Queue depth low (0 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-003 -- Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-2
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-003
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

### IGW-20260826-007 -- Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-6
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-4 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-007
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

### IGW-20260826-008 -- FOUNDATION -- per-candidate multi-channel affect vector substrate (MECH-359)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-1
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-008
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

### IGW-20260826-022 -- Unified autobiographical event-token store (ARC-085): ONE self-tagged store backing both replay and prospective simulati

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-2
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-022
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

### IGW-20260826-023 -- Provenance-bearing event token + one-way committed-vs-imagined gate (MECH-365)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-3
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-023
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

### IGW-20260826-051 -- Graded action-status + self-reference-frame vocabulary decision (Q-068 fork)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-2
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-051
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

### IGW-20260826-052 -- PILLAR -- externalised DMN play scaffold (ARC-090): simulation pushed outward into objects/roles/as-if worlds

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-3
- **Blocked by:** developmental_dmn_v4:DMN-2 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-052
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

### IGW-20260826-057 -- Multidrive arbitration / orchestration policy (which drive wins when several are active)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** drives_motivation_v4:DRV-2
- **Why now:** Plan gap blocked on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-057
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

### IGW-20260826-060 -- Multi-agent D_V substrate: extend temporal-depth coherence optimisation over self AND represented others (ARC-056 entry)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-1
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-060
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

### IGW-20260826-061 -- Typed causal-attribution ontology: ownership tags for self / world / body / model / commitment / OTHER / shared / accide

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-2
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-061
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

### IGW-20260826-062 -- Guilt-as-repair routing: self-attributed harm opens repair-search + policy-update pathways (E3 repair-trajectory generat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-3
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-062
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

### IGW-20260826-069 -- Stream-binding mechanism: route own motivational-affective streams across the other-model

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-3
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-069
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

### IGW-20260826-070 -- Falsifiable dissociation: prediction != reciprocity-reward != residue-aware repair (A/B/C/D)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-4
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-070
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

### IGW-20260826-073 -- Experiment A -- REE-native J-lens dispositional readout (does REE have a J-space?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:A
- **Why now:** Plan gap blocked on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-073
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

### IGW-20260826-075 -- Experiment B -- workspace-ablation cliff (cliff vs graceful degradation; the SD-064 falsifier)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:B
- **Blocked by:** global_workspace_jlens:GATE-B [open]
- **Why now:** Resume ONLY after GATE-B builds + smoke-tests the SD-027/MECH-254 V3 top-k access gate. Then queue the MECH-254 four-cell factorial {gate off, gate only, template only, both on} in a task that REQUIRES multi-step committed-action integratio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-075
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

### IGW-20260826-077 -- PILLAR 1 -- frontopolar-analog deliberation substrate (SD-033e module + mode transitions)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-2
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-077
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

### IGW-20260826-083 -- Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-3
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-083
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

### IGW-20260826-086 -- Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (gram

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-6
- **Blocked by:** grammar_primitive_mining_v6:GRAM-3 [blocked]; grammar_primitive_mining_v6:GRAM-4 [blocked]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-086
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

### IGW-20260826-087 -- GATE -- multi-step hippocampally-planned system validated in V3 (MECH-163)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-1
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-087
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

### IGW-20260826-088 -- PILLAR -- dorsal/ventral hippocampal functional segregation (ARC-040)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-2
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-088
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

### IGW-20260826-097 -- Belief-state hypothesis set (top-k latent-state hypotheses with precision)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-3
- **Blocked by:** inference_belief_state_v4:INF-2 [open]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-097
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

### IGW-20260826-099 -- Safety-route inference (infer route to safety from partial map/cue/gradient)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-5
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]; inference_belief_state_v4:INF-4 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-099
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

### IGW-20260826-102 -- Pre-linguistic-grounding gate: no affect adaptor before object/self/other primitives exist (the load-bearing ordering)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-1
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-102
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

### IGW-20260826-103 -- Uncertainty-propagation invariant: parsed affect enters as a hypothesis (distribution), NEVER as ground truth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-2
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]
- **Why now:** Plan gap open on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-103
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

### IGW-20260826-104 -- The adaptor itself: a lightweight LanguageAffectAdaptor (SLM-class) text -> distribution-over-affect

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-3
- **Blocked by:** language_affect_adaptor_v6:LAA-1 [blocked]; language_affect_adaptor_v6:LAA-2 [open]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-104
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

### IGW-20260826-108 -- Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-3
- **Blocked by:** language_emergence_bootstrap_v6:LANG-2 [open]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-108
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

### IGW-20260826-109 -- Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergenc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-4
- **Blocked by:** language_emergence_bootstrap_v6:LANG-3 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-109
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

### IGW-20260826-113 -- Trust-calibration over linguistic signals (sender-reliability estimate weights symbolic updates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-2
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-113
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

### IGW-20260826-114 -- Deception detection / honest-signal pressure (deception = modelling another model)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-3
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-114
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

### IGW-20260826-117 -- Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-1
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-117
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

### IGW-20260826-118 -- Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-2
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-118
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

### IGW-20260826-119 -- Live unethical affordance: harmful action representable as a chooseable possibility (not absent)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-3
- **Blocked by:** loveability_ethical_agency_v5:LOVE-1 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-119
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

### IGW-20260826-120 -- Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-4
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-120
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

### IGW-20260826-122 -- Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-6
- **Blocked by:** loveability_ethical_agency_v5:LOVE-2 [blocked]; loveability_ethical_agency_v5:LOVE-3 [blocked]; loveability_ethical_agency_v5:LOVE-4 [blocked]; loveability_ethical_agency_v5:LOVE-5 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-122
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

### IGW-20260826-128 -- Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-1
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-128
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

### IGW-20260826-129 -- Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive clo

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-2
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-1 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-129
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

### IGW-20260826-130 -- Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales oth

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-3
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-130
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

### IGW-20260826-131 -- Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-4
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-131
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

### IGW-20260826-135 -- Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-1
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-135
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

### IGW-20260826-136 -- Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-2
- **Blocked by:** multi_agent_ecology_v5:MAE-1 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-136
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

### IGW-20260826-143 -- PILLAR A -- action-chunk cache (SD-045): the first reusable-unit substrate, model-free habit pathway

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-2
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-143
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

### IGW-20260826-147 -- PILLAR D -- theta-packaging + cognitive-map traversal scale to the active abstraction level (MECH-299 / MECH-300)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-6
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-2 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]; object_reasoning_abstraction_v4:OBJ-ABS-5 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-147
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

### IGW-20260826-163 -- PILLAR C -- cross-modal negotiation currency: making heterogeneous sense geometries mutually negotiable in one world mod

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-5
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]; perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-163
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

### IGW-20260826-165 -- Opening-vs-closure asymmetry framing + the V3-conservative-is-insufficient gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-1
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-165
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

### IGW-20260826-166 -- PILLAR A -- ACh-analog basal-forebrain plasticity-gain gate

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-3
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-166
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

### IGW-20260826-169 -- Re-pose ARC-070's prediction-failure decomposition trigger off the saturated region-V_s proxy onto a rank-based forward-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 38 | **Generation:** v3
- **Gap(s):** policy_decomposition_trigger:REPOSE
- **Owner EXQ:** V3-EXQ-938
- **Why now:** 2026-08-21 governance applied confirmed failure_autopsy_V3-EXQ-938_2026-08-20: non_contributory (null at this grain, not a detected negative). Lettered 938 successor and fourth env-axis escalation REFUSED. ARC-070/MECH-321 stay candidate wi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-169
Title: Re-pose ARC-070's prediction-failure decomposition trigger off the saturated region-V_s proxy onto a rank-based forward-
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): policy_decomposition_trigger:REPOSE
Owner EXQ: V3-EXQ-938
Claims: ARC-070, MECH-321
Why now: 2026-08-21 governance applied confirmed failure_autopsy_V3-EXQ-938_2026-08-20: non_contributory (null at this grain, not a detected negative). Lettered 938 successor and fourth env-axis escalation REFUSED. ARC-070/MECH-321 stay candidate wi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/policy_decomposition_trigger_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-185 -- Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-1
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-185
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

### IGW-20260826-188 -- Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-4
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]; relational_harm_moral_semantics_v5:RHM-2 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-188
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

### IGW-20260826-199 -- Finish self-attribution: complete the per-stream comparator topology (SD-030 z_self stream)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-2
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-199
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

### IGW-20260826-009 -- Anti-collapse MAP consolidation (ARC-088) -- audit distinctness across the affect stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-2
- **Why now:** Plan gap in_progress on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-009
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

### IGW-20260826-034 -- Commitment / de-commit latch grounding L1 -> L3

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-3
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-034
Title: Commitment / de-commit latch grounding L1 -> L3
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): biology_grounding_convergence_v4:BG-3
Claims: SD-034, MECH-090
Why now: Plan gap in_progress on biology_grounding_convergence_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/biology_grounding_convergence_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-038 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-4
- **Why now:** Advances/closes on the V3-EXQ-460k RESULT -- the LIVE in-flight de-commit falsifier (QUEUED + INGESTED 2026-06-22, ree-v3 main 979a943, coordinator /queue/active via git reconcile, machine_affinity any; supersedes V3-EXQ-460j, which RAN ter

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-038
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

### IGW-20260826-049 -- Phase 1 -- emit a derived gitignored SQLite read-model from build_experiment_indexes.py at the point it already writes c

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** pending | **Priority:** 40 | **Generation:** process
- **Gap(s):** derived_evidence_index:P1
- **Why now:** Plan gap pending on derived_evidence_index.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-049
Title: Phase 1 -- emit a derived gitignored SQLite read-model from build_experiment_indexes.py at the point it already writes c
Lane: plan | Skill: (plan reconcile)
Status: pending
Gap(s): derived_evidence_index:P1
Why now: Plan gap pending on derived_evidence_index.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/derived_evidence_index_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-059 -- Phase 2 (Option B): pairwise MRF + damped loopy belief propagation, additive output schema, evidence-flow animation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 40 | **Generation:** meta
- **Gap(s):** PHASE-2
- **Why now:** Plan gap in_progress on epistemic_overlay.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-059
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

### IGW-20260826-157 -- MECH-489 validation: defensive-orienting phasic behavioural chain

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40 | **Generation:** v3
- **Gap(s):** orienting_epistemic_deficit_v3:ORNT-6
- **Owner EXQ:** V3-EXQ-910b
- **Why now:** The claims.yaml substrate blocker is cleared; this node is not blocked on any further build. Remaining open question is whether the MIXED read (driven by the C1 legacy-vs-new-tap discrepancy, not by C2 valence-gating) warrants a further dis

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-157
Title: MECH-489 validation: defensive-orienting phasic behavioural chain
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): orienting_epistemic_deficit_v3:ORNT-6
Owner EXQ: V3-EXQ-910b
Claims: MECH-489
Why now: The claims.yaml substrate blocker is cleared; this node is not blocked on any further build. Remaining open question is whether the MIXED read (driven by the C1 legacy-vs-new-tap discrepancy, not by C2 valence-gating) warrants a further dis

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Plan doc: REE_assembly/evidence/planning/orienting_epistemic_deficit_v3_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-170 -- 2x2 motivational state taxonomy + three-stage pipeline (depression / GAD)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 40 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:MOTIVATIONAL-TAXONOMY
- **Why now:** Plan gap partial on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-170
Title: 2x2 motivational state taxonomy + three-stage pipeline (depression / GAD)
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): clinical_failure_modes:MOTIVATIONAL-TAXONOMY
Claims: INV-054, MECH-186, MECH-187, MECH-188
Why now: Plan gap partial on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-171 -- Catatonia subtype II: harm-stream lock-in (SD-036 decay regulator, MECH-279 PAG freeze gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 40 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:CATATONIA-II
- **Why now:** Plan gap partial on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-171
Title: Catatonia subtype II: harm-stream lock-in (SD-036 decay regulator, MECH-279 PAG freeze gate)
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): clinical_failure_modes:CATATONIA-II
Claims: SD-036
Why now: Plan gap partial on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-172 -- OCD as a three-layer architectural failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 40 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:OCD-THREE-LAYER
- **Why now:** Plan gap partial on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-172
Title: OCD as a three-layer architectural failure
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): clinical_failure_modes:OCD-THREE-LAYER
Claims: MECH-260, SD-045, SD-046
Why now: Plan gap partial on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-206 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** upstream_blocked | **Priority:** 40 | **Generation:** v3
- **Gap(s):** sleep_substrate:GAP-2
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-206
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

### IGW-20260826-211 -- Shadow: coordinator mirrors TASK_CLAIMS/TASK_CHIPS state read-only; git stays authoritative

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** not_started | **Priority:** 40 | **Generation:** process
- **Gap(s):** PHASE-1
- **Why now:** Plan gap not_started on task_claim_chip_coordinator_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-211
Title: Shadow: coordinator mirrors TASK_CLAIMS/TASK_CHIPS state read-only; git stays authoritative
Lane: plan | Skill: (plan reconcile)
Status: not_started
Gap(s): PHASE-1
Why now: Plan gap not_started on task_claim_chip_coordinator_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-212 -- Claim-authority cutover: task_claim.py/chip_ledger.py call the coordinator; git becomes state-change materialization

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** not_started | **Priority:** 40 | **Generation:** process
- **Gap(s):** PHASE-2
- **Why now:** Plan gap not_started on task_claim_chip_coordinator_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-212
Title: Claim-authority cutover: task_claim.py/chip_ledger.py call the coordinator; git becomes state-change materialization
Lane: plan | Skill: (plan reconcile)
Status: not_started
Gap(s): PHASE-2
Why now: Plan gap not_started on task_claim_chip_coordinator_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-068 -- Extend the same 'grep serve.py's computed dicts against what the frontend renders' technique to closure.html (B3)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** process
- **Gap(s):** explorer_ui_improvement:CLOSURE-PAGE-AUDIT
- **Why now:** Plan gap open on explorer_ui_improvement.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-068
Title: Extend the same 'grep serve.py's computed dicts against what the frontend renders' technique to closure.html (B3)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): explorer_ui_improvement:CLOSURE-PAGE-AUDIT
Why now: Plan gap open on explorer_ui_improvement.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/explorer_ui_improvement_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-082 -- Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merel

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-2
- **Why now:** Plan gap open on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-082
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

### IGW-20260826-101 -- Inference failure-mode register + biology grounding (lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-7
- **Why now:** Plan gap open on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-101
Title: Inference failure-mode register + biology grounding (lit-pulls)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): inference_belief_state_v4:INF-7
Claims: Q-070, MECH-434
Why now: Plan gap open on inference_belief_state_v4.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/inference_belief_state_v4_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-164 -- Adaptor-maturity curriculum gate: each sense admitted when its adaptor is mature, not all at once

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-6
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-164
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

### IGW-20260826-177 -- Self-model failure modes: E1 schema poverty vs E2 capacity degradation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:SELF-MODEL-DEGRADATION
- **Why now:** Plan gap open on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-177
Title: Self-model failure modes: E1 schema poverty vs E2 capacity degradation
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): clinical_failure_modes:SELF-MODEL-DEGRADATION
Claims: INV-064, MECH-214, MECH-215
Why now: Plan gap open on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-178 -- Narcolepsy and cataplexy: bilateral orexin-loss failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:NARCOLEPSY-CATAPLEXY
- **Why now:** Plan gap open on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-178
Title: Narcolepsy and cataplexy: bilateral orexin-loss failure
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): clinical_failure_modes:NARCOLEPSY-CATAPLEXY
Claims: MECH-281
Why now: Plan gap open on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-179 -- Difficulty-gated proposal entropy: stuck-state cognition (working hypothesis)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:PROPOSAL-ENTROPY
- **Why now:** Plan gap open on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-179
Title: Difficulty-gated proposal entropy: stuck-state cognition (working hypothesis)
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): clinical_failure_modes:PROPOSAL-ENTROPY
Claims: MECH-343, Q-056
Why now: Plan gap open on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-183 -- Minimal 2-agent world (put any load on the ethics thesis, currently V5-only)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** v5
- **Gap(s):** WS-10
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-183
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

### IGW-20260826-184 -- Early-gating vs late-judging demo (REE early commit-gating beats a Constitutional-AI-style late judge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** meta
- **Gap(s):** WS-11
- **Why now:** Plan gap open on ree_ai_design_critique.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-184
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

### IGW-20260826-207 -- Phase 2 -- surface Phase-0/1 candidates in /governance or morning-digest (pending_review.md-style derived report or an I

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** ready | **Priority:** 45 | **Generation:** process
- **Gap(s):** substrate_stability:P2-governance-surface
- **Why now:** Plan gap open on substrate_stability_and_drift_detection.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-207
Title: Phase 2 -- surface Phase-0/1 candidates in /governance or morning-digest (pending_review.md-style derived report or an I
Lane: plan | Skill: (plan reconcile)
Status: ready
Gap(s): substrate_stability:P2-governance-surface
Why now: Plan gap open on substrate_stability_and_drift_detection.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-004 -- Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-3
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-004
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

### IGW-20260826-005 -- Analogy / structure-mapping across grounded domains (relational alignment, not surface match)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-4
- **Blocked by:** abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-005
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

### IGW-20260826-006 -- Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** abstract_relational_reasoning_v6:ARR-5
- **Blocked by:** abstract_relational_reasoning_v6:ARR-2 [blocked]; abstract_relational_reasoning_v6:ARR-3 [blocked]
- **Why now:** Plan gap blocked on abstract_relational_reasoning_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-006
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

### IGW-20260826-010 -- Expression as emergent action geometry (MECH-360) -- the readout side of the affect vector

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-3
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-010
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

### IGW-20260826-011 -- Candidate-gradient hippocampal episode schema (MECH-361) -- affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-4
- **Blocked by:** affect_expression_v4:AE-1 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-011
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

### IGW-20260826-014 -- Compulsion-risk substrate -- slow modulator (MECH-369) + composed readout (MECH-370) + chunk-cache loop (SD-045) + value

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-7
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]; affect_expression_v4:AE-10 [blocked]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-014
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

### IGW-20260826-015 -- Slow value-INDEPENDENT decommit-friction / engagement-release modulator substrate (the slow-modulator-class distinction 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-10
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-015
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

### IGW-20260826-024 -- Imagination-learning licit/forbidden principle (ARC-level, folded into the provenance gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-4
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]
- **Why now:** Plan gap open on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-024
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

### IGW-20260826-025 -- Event-level write-authority gate over the durable model-update path (MECH-368) + its falsifier (Q-062)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-5
- **Blocked by:** autobiographical_memory_v4:ABM-3 [blocked]; autobiographical_memory_v4:ABM-4 [open]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-025
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

### IGW-20260826-053 -- PILLAR -- private speech as external cognitive-control surface (MECH-380): Vygotskian internalisation ladder

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-4
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-053
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

### IGW-20260826-054 -- PILLAR -- developmental compression ladder (MECH-381): externalise-then-internalise across the whole curriculum

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-5
- **Blocked by:** developmental_dmn_v4:DMN-3 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-054
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

### IGW-20260826-063 -- Anti-shame safety invariants: no-global-self-condemnation write + containment-not-shame autonomy suspension

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-4
- **Blocked by:** ethics_as_coherence_v5:ETH-2 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-063
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

### IGW-20260826-064 -- Love as agent-indexed terrain inference: infer another agent's goal/harm gradients and weight them with self-equal motiv

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-5
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-064
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

### IGW-20260826-071 -- Residue-aware social repair: regret-residue after exploitation generates a repair-goal

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-5
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]; fast_empathy_v5:EMP-4 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-071
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

### IGW-20260826-072 -- Developmental ordering of other-bound streams: protective streams before appetitive (safety gate)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** fast_empathy_v5:EMP-6
- **Blocked by:** fast_empathy_v5:EMP-3 [blocked]
- **Why now:** Plan gap blocked on fast_empathy_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-072
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

### IGW-20260826-074 -- SD-027 / MECH-254 V3 boundary top-k access-gate build (use_boundary_access_gate, no-op-default)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:GATE-B
- **Blocked by:** global_workspace_jlens:A [blocked]
- **Why now:** Plan gap open on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-074
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

### IGW-20260826-078 -- PILLAR 2 -- counterfactual-value tracking and switch-to-alternative gate (MECH-264)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-3
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-078
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

### IGW-20260826-079 -- PILLAR 3 -- relative-importance monitoring across competing goals + dACC cross-slot arbitrator (MECH-265, SD-046)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-4
- **Blocked by:** goal_deliberation_v4:GDL-2 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-079
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

### IGW-20260826-080 -- PILLAR 4 -- interrupted-task resumption / Zeigarnik (the event-arc's weak interrupt->reorient->resume span)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-5
- **Blocked by:** goal_deliberation_v4:GDL-4 [blocked]
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-080
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

### IGW-20260826-089 -- DG-equivalent pattern separation before rollout proposal (MECH-147)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-3
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-089
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

### IGW-20260826-090 -- Pure time cells -- temporal scaffolding for E3 credit assignment (MECH-148)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-4
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-090
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

### IGW-20260826-091 -- CA1 mismatch novelty gate on rollout injection (MECH-149)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-5
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-091
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

### IGW-20260826-098 -- Inferred affordance field (afford. not directly perceived; biases E3 candidates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-4
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-098
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

### IGW-20260826-100 -- Epistemic action pressure (information-gathering as survival-relevant, not just curiosity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** inference_belief_state_v4:INF-6
- **Blocked by:** inference_belief_state_v4:INF-3 [blocked]
- **Why now:** Plan gap blocked on inference_belief_state_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-100
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

### IGW-20260826-105 -- Consumption wiring: parsed other-affect prior feeds the V5 empathy stream-binding layer (not a parallel path)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-4
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-105
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

### IGW-20260826-106 -- Falsifiable test: language-parsed affect must change other-directed behaviour vs literal-semantics-only baseline (and mu

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_affect_adaptor_v6:LAA-5
- **Blocked by:** language_affect_adaptor_v6:LAA-3 [blocked]; language_affect_adaptor_v6:LAA-4 [blocked]
- **Why now:** Plan gap blocked on language_affect_adaptor_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-106
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

### IGW-20260826-110 -- Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-5
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-110
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

### IGW-20260826-111 -- Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-6
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-111
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

### IGW-20260826-112 -- Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_emergence_bootstrap_v6:LANG-7
- **Blocked by:** language_emergence_bootstrap_v6:LANG-4 [blocked]
- **Why now:** Plan gap blocked on language_emergence_bootstrap_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-112
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

### IGW-20260826-115 -- Language failure modes as REE pathologies (rationalisation / ideological capture / bureaucratic dissociation / moral lic

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-4
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-115
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

### IGW-20260826-116 -- Institutions as multi-agent linguistic coordination structures (residue absorb / diffuse / deny)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v6
- **Gap(s):** language_trust_deception_institutions_v6:LTI-5
- **Blocked by:** language_trust_deception_institutions_v6:LTI-2 [blocked]; language_trust_deception_institutions_v6:LTI-4 [blocked]
- **Why now:** Plan gap blocked on language_trust_deception_institutions_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-116
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

### IGW-20260826-121 -- Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** loveability_ethical_agency_v5:LOVE-5
- **Blocked by:** loveability_ethical_agency_v5:LOVE-4 [blocked]
- **Why now:** Plan gap blocked on loveability_ethical_agency_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-121
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

### IGW-20260826-124 -- Explicit active-separation operation (separate != failed-integration) + DG pattern-separation pairing

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-2
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-124
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

### IGW-20260826-126 -- Provenance + contradiction-flag + rollback layer on consolidated memory

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-5
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-126
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

### IGW-20260826-132 -- Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-5
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-3 [blocked]; mirror_modelling_other_self_v5:MIRROR-4 [blocked]
- **Why now:** Plan gap open on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-132
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

### IGW-20260826-134 -- Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-7
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-4 [blocked]; mirror_modelling_other_self_v5:MIRROR-6 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-134
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

### IGW-20260826-137 -- Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-3
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-137
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

### IGW-20260826-138 -- Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation cha

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-4
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-138
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

### IGW-20260826-139 -- Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-5
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-4 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-139
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

### IGW-20260826-141 -- ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-7
- **Blocked by:** multi_agent_ecology_v5:MAE-3 [blocked]; multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-141
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

### IGW-20260826-144 -- PILLAR B -- type-encoder + category prototypes (SD-040): type-keyed anchors over z_world

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-3
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-144
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

### IGW-20260826-145 -- PILLAR B retrieval -- prototype-readout operator + type-V_s gating (MECH-296 / MECH-297)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-4
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-3 [blocked]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-145
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

### IGW-20260826-146 -- PILLAR C -- option library (SD-042): named reusable subroutines (init-set / termination / internal-policy)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_reasoning_abstraction_v4:OBJ-ABS-5
- **Blocked by:** object_reasoning_abstraction_v4:OBJ-ABS-1 [blocked_pending_substrate]
- **Why now:** Plan gap blocked on object_reasoning_abstraction_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-146
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

### IGW-20260826-149 -- PILLAR 2 -- self-as-object cutover (ARC-081): z_self -> privileged object-file slot

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-3
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap open on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-149
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

### IGW-20260826-150 -- PILLAR 3 -- tools/affordances object->action binding (ARC-082)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-4
- **Blocked by:** object_representation_v4:OBJ-2 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-150
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

### IGW-20260826-151 -- PILLAR 4 -- others-as-object (ARC-083): per-agent token-keyed object-file slots

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-5
- **Blocked by:** object_representation_v4:OBJ-2 [open]; object_representation_v4:OBJ-3 [open]
- **Why now:** Plan gap blocked on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-151
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

### IGW-20260826-153 -- Pre-approach orienting/surveying mode (cue-triggered, narrow vector resolution)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** orienting_epistemic_deficit_v3:ORNT-1
- **Why now:** Plan gap blocked on orienting_epistemic_deficit_v3.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-153
Title: Pre-approach orienting/surveying mode (cue-triggered, narrow vector resolution)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): orienting_epistemic_deficit_v3:ORNT-1
Claims: MECH-395
Why now: Plan gap blocked on orienting_epistemic_deficit_v3.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/orienting_epistemic_deficit_v3_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-161 -- PILLAR B -- deep-adaptor (sight) perceptual-manifold constructor: metric/geometry before world-model entry

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-3
- **Blocked by:** perceptual_adaptors_v4:PA-2 [open]
- **Why now:** Plan gap blocked on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-161
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

### IGW-20260826-162 -- Metric-origin fork: per-sense perceptual metric LEARNED from similarity statistics vs partly DEFINED (structural prior)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** perceptual_adaptors_v4:PA-4
- **Blocked by:** perceptual_adaptors_v4:PA-3 [blocked]
- **Why now:** Plan gap open on perceptual_adaptors_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-162
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

### IGW-20260826-167 -- PILLAR B -- state-conditional plasticity-gain architectural commitment

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-4
- **Blocked by:** plasticity_neuromodulation_v4:PLW-3 [blocked]
- **Why now:** Plan gap blocked on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-167
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

### IGW-20260826-168 -- Layer-specificity adjudication (one global scalar vs per-substrate gates)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** plasticity_neuromodulation_v4:PLW-7
- **Blocked by:** plasticity_neuromodulation_v4:PLW-4 [blocked]
- **Why now:** Plan gap open on plasticity_neuromodulation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-168
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

### IGW-20260826-186 -- Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-2
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-186
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

### IGW-20260826-187 -- Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-3
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-1 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-187
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

### IGW-20260826-189 -- Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-5
- **Blocked by:** relational_harm_moral_semantics_v5:RHM-4 [blocked]
- **Why now:** Plan gap blocked on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-189
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

### IGW-20260826-192 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [assembling]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-192
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

### IGW-20260826-193 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-193
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

### IGW-20260826-194 -- Phase 4 (re-application) -- terminal behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate; NO EXQ i

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** sd_037_axis_b:P4
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-194
Title: Phase 4 (re-application) -- terminal behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate; NO EXQ i
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): sd_037_axis_b:P4
Claims: SD-037, MECH-280, MECH-281
Blocked by: sd_037_axis_b:P3 [blocked]
Why now: Plan gap blocked on sd_037_axis_b.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-195 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-195
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

### IGW-20260826-196 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-2
- **Why now:** RE-ADJUDICATED 2026-06-09 (gap-A substrate re-read). The 2026-05-16 gate ('retest unblockable once SP-CEM lands in the main agent action path') is STALE and was satisfiable the day after it was written: ARC-065 SP-CEM was LANDED AS MAIN-PAT

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-196
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

### IGW-20260826-202 -- z_self-domain goal representation (DR-11): self-state goals representable, not just world-location goals

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-5
- **Blocked by:** self_model_v4:SELF-3 [in_progress]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-202
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

### IGW-20260826-203 -- Proxy/hedonic dissociating environment (DR-14): substrate that surfaces the wanting-without-satisfaction failure

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-6
- **Blocked by:** self_model_v4:SELF-5 [blocked]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-203
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

### IGW-20260826-204 -- Maturational-sequence honesty gate (INV-064): self-stability must precede the social/other pillar

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-7
- **Blocked by:** self_model_v4:SELF-3 [in_progress]
- **Why now:** Plan gap blocked on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-204
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

### IGW-20260826-017 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-017
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

### IGW-20260826-018 -- ARC-064 bottom-up rule-discovery cluster (MECH-318 absorption check done; MECH-316 / MECH-317 checks STILL OPEN -- see G

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-018
Title: ARC-064 bottom-up rule-discovery cluster (MECH-318 absorption check done; MECH-316 / MECH-317 checks STILL OPEN -- see G
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

### IGW-20260826-019 -- ARC-064 absorption checks for MECH-316 (cross-episode regularities) + MECH-317 (behavioural-pattern compression) -- doc-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-I-absorption
- **Blocked by:** arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** Plan gap blocked_pending_substrate on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-019
Title: ARC-064 absorption checks for MECH-316 (cross-episode regularities) + MECH-317 (behavioural-pattern compression) -- doc-
Lane: plan | Skill: (plan reconcile)
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-I-absorption
Claims: MECH-316, MECH-317
Blocked by: arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
Why now: Plan gap blocked_pending_substrate on arc_062_rule_apprehension.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-021 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-021
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

### IGW-20260826-028 -- Biology grounding completion (emotional-modulation-of-consolidation write-weight, source/provenance monitoring, imaginat

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-9
- **Why now:** Plan gap closed on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-028
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

### IGW-20260826-030 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Why now:** REFRESHED 2026-06-27 (the stale '603q is QUEUED / AWAITING RUN+REVIEW' framing below is SUPERSEDED -- V3-EXQ-603q RAN PASS 2026-06-17, SD-059/MECH-358 settled). CURRENT STATE: the survival/harm-pathway prereq is CLEARED; the 687 frontier RA

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-030
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

### IGW-20260826-035 -- Goal / wanting layer grounding L1 -> L2 [L2 REACHED 2026-07-07 via on-file anchors]

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-5
- **Why now:** Plan gap in_progress on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-035
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

### IGW-20260826-039 -- OCD-battery completeness: the *b behavioural cohort (460b/461/463b/464b/466b/467b/468b) for SD-034/MECH-266/267/268 + ME

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-4-battery
- **Blocked by:** commitment_closure:GAP-4 [in_progress]
- **Why now:** 466e RAN + PASSED (governance-cycle-20260625T0420Z). The SD-034 residue-discharge battery arm is DONE; the residual node openness is the commitment-DEPENDENT arms (461/464b/467b/468b for MECH-266/267/268, 629-lineage for MECH-342), which th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-039
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

### IGW-20260826-041 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-8
- **Why now:** OWNER FRONTIER = V3-EXQ-485j (QUEUED 2026-06-21, pending; supersedes 485i). 485j re-runs the trained-OFC-head C1 devaluation_selection_shift + C2 between-context-TV behavioural DVs through the real E3.select() on the MECH-448 demotion-enabl

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-041
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

### IGW-20260826-045 -- Valuation face (SD-033b/MECH-263): decoupled OFC devaluation head feeding F

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v3
- **Gap(s):** conversion_ceiling_campaign:P3-ofc
- **Why now:** Plan gap assembling on conversion_ceiling_campaign.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-045
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

### IGW-20260826-050 -- Phase 2 -- cut over the six identified consumers, incl. a /api/claims/summary endpoint replacing explorer.html's 10 MB p

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** pending | **Priority:** 50 | **Generation:** process
- **Gap(s):** derived_evidence_index:P2
- **Blocked by:** derived_evidence_index:P1 [pending]
- **Why now:** Plan gap pending on derived_evidence_index.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-050
Title: Phase 2 -- cut over the six identified consumers, incl. a /api/claims/summary endpoint replacing explorer.html's 10 MB p
Lane: plan | Skill: (plan reconcile)
Status: pending
Gap(s): derived_evidence_index:P2
Blocked by: derived_evidence_index:P1 [pending]
Why now: Plan gap pending on derived_evidence_index.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/derived_evidence_index_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-058 -- Drive-arbitration biology grounding (multidrive competition / drive hierarchy lit-pull)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v4
- **Gap(s):** drives_motivation_v4:DRV-3
- **Why now:** Plan gap closed on drives_motivation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-058
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

### IGW-20260826-066 -- Biology grounding: guilt-as-reparative-motivation vs shame-as-withdrawal, moral-repair, typed-causal-attribution, and p-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-8
- **Why now:** Plan gap closed on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-066
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

### IGW-20260826-067 -- Dark mode via prefers-color-scheme (C1), inline-hex-to-CSS-variable migration (C2), More-menu reorganisation (C3)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 50 | **Generation:** process
- **Gap(s):** explorer_ui_improvement:VISUAL
- **Why now:** Plan gap partial on explorer_ui_improvement.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-067
Title: Dark mode via prefers-color-scheme (C1), inline-hex-to-CSS-variable migration (C2), More-menu reorganisation (C3)
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): explorer_ui_improvement:VISUAL
Why now: Plan gap partial on explorer_ui_improvement.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/explorer_ui_improvement_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-094 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v3
- **Gap(s):** infant_substrate:GAP-13
- **Why now:** Re-pointed 2026-06-09. Routing substrate landed + load-bearing-ready (V3-EXQ-648a C2 PASS; V3-EXQ-649 GAP-A shared-channel PASS). DO NOT re-queue V3-EXQ-590 on the MECH-111 novelty_bonus_weight design (still broadcast). RESUME path: once th

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-094
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

### IGW-20260826-095 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked_pending_substrate | **Priority:** 50 | **Generation:** v3
- **Gap(s):** infant_substrate:GAP-14
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-095
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

### IGW-20260826-152 -- Biology grounding completion (object-files / permanence / affordances / self / ToM lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** object_representation_v4:OBJ-6
- **Why now:** Plan gap in_progress on object_representation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-152
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

### IGW-20260826-158 -- Unify the pack skeleton (sync build_runpack_docs + pack_writer.write_pack delegate to one shared skeleton)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** parked | **Priority:** 50 | **Generation:** process
- **Gap(s):** STEP-7.1
- **Why now:** Plan gap parked on pack_writer_single_writer_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-158
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

### IGW-20260826-159 -- Carry the always-core through sync into the pack (substrate_hash/config/seeds/machine/elapsed_seconds + rich governance 

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** parked_indefinite | **Priority:** 50 | **Generation:** process
- **Gap(s):** STEP-7.2
- **Why now:** Plan gap parked_indefinite on pack_writer_single_writer_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-159
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

### IGW-20260826-173 -- Hyperarousal insomnia and schema-repair starvation (PTSD chronicity)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 50 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:PTSD-HYPERAROUSAL-INSOMNIA
- **Why now:** Plan gap partial on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-173
Title: Hyperarousal insomnia and schema-repair starvation (PTSD chronicity)
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): clinical_failure_modes:PTSD-HYPERAROUSAL-INSOMNIA
Claims: MECH-286
Why now: Plan gap partial on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-174 -- Dream phenomenology as diagnostic and treatment-response marker

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** partial | **Priority:** 50 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:DREAM-PHENOMENOLOGY
- **Why now:** Plan gap partial on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-174
Title: Dream phenomenology as diagnostic and treatment-response marker
Lane: plan | Skill: (plan reconcile)
Status: partial
Gap(s): clinical_failure_modes:DREAM-PHENOMENOLOGY
Claims: INV-062, MECH-206, MECH-208, MECH-209, MECH-210
Why now: Plan gap partial on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-175 -- Serotonergic cross-state architecture (replay salience tagging, REM-gate zero-point)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:SEROTONERGIC-CROSS-STATE
- **Why now:** Plan gap in_progress on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-175
Title: Serotonergic cross-state architecture (replay salience tagging, REM-gate zero-point)
Lane: plan | Skill: (plan reconcile)
Status: in_progress
Gap(s): clinical_failure_modes:SEROTONERGIC-CROSS-STATE
Claims: MECH-203
Why now: Plan gap in_progress on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-180 -- Pharmacological predictions registry + receptor-subtype resolution layer

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** tracked | **Priority:** 50 | **Generation:** clinical
- **Gap(s):** clinical_failure_modes:PHARMACOLOGICAL-PREDICTIONS
- **Blocked by:** clinical_failure_modes:CATATONIA-II [partial]; clinical_failure_modes:SEROTONERGIC-CROSS-STATE [in_progress]; clinical_failure_modes:MOTIVATIONAL-TAXONOMY [partial]
- **Why now:** Plan gap tracked on clinical_failure_modes.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-180
Title: Pharmacological predictions registry + receptor-subtype resolution layer
Lane: plan | Skill: (plan reconcile)
Status: tracked
Gap(s): clinical_failure_modes:PHARMACOLOGICAL-PREDICTIONS
Blocked by: clinical_failure_modes:CATATONIA-II [partial]; clinical_failure_modes:SEROTONERGIC-CROSS-STATE [in_progress]; clinical_failure_modes:MOTIVATIONAL-TAXONOMY [partial]
Why now: Plan gap tracked on clinical_failure_modes.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/psychiatric_failure_modes_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-190 -- Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** v5
- **Gap(s):** relational_harm_moral_semantics_v5:RHM-6
- **Why now:** Plan gap closed on relational_harm_moral_semantics_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-190
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

### IGW-20260826-201 -- E2 prediction error modulates E3 confidence (DR-12): PE-magnitude signals trajectory unreliability

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** in_progress | **Priority:** 50 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-4
- **Why now:** AWAITING V4-EXQ-001 RUN + REVIEW (DR-12 pilot, queued ree-v3/main 394ccf4). On PASS (dr12_pe_conditioning_changes_selection): the E2-PE -> E3-confidence wiring is live; queue the ecological-evidence successor (region-PE auto-source) that sc

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-201
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

### IGW-20260826-205 -- Own-future-option uncertainty: does REE need an explicit self-model of its OWN future option-space (second-order uncerta

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** assembling | **Priority:** 50 | **Generation:** v4
- **Gap(s):** self_model_v4:SELF-9
- **Why now:** Plan gap assembling on self_model_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-205
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

### IGW-20260826-208 -- Extend the inertness-idiom filter with further gate-recognition patterns beyond P1e's cached-state-check, to move check_

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** closed | **Priority:** 50 | **Generation:** process
- **Gap(s):** substrate_stability:P1f-more-gate-idioms
- **Why now:** Plan gap closed on substrate_stability_and_drift_detection.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-208
Title: Extend the inertness-idiom filter with further gate-recognition patterns beyond P1e's cached-state-check, to move check_
Lane: plan | Skill: (plan reconcile)
Status: closed
Gap(s): substrate_stability:P1f-more-gate-idioms
Why now: Plan gap closed on substrate_stability_and_drift_detection.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-213 -- Harden: monitoring, CLAUDE.md rewrite to reflect the new default, decommission what is safe to decommission

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** not_started | **Priority:** 50 | **Generation:** process
- **Gap(s):** PHASE-3
- **Why now:** Plan gap not_started on task_claim_chip_coordinator_migration.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-213
Title: Harden: monitoring, CLAUDE.md rewrite to reflect the new default, decommission what is safe to decommission
Lane: plan | Skill: (plan reconcile)
Status: not_started
Gap(s): PHASE-3
Why now: Plan gap not_started on task_claim_chip_coordinator_migration.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-234 -- Confirm evidence: MECH-191 (lit 0.86, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0291 status=blocked_substrate: functional-state channels do not externalize >=2 differentially-active, cross-architecturally-consistent dimensions; scalar channel-norm readouts of tonic accumulators are satu
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (metaworker-chip-20260803-igw-confirm-mech191) recorded EXP-0291 status=blocked_substrate in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs un

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-234
Title: Confirm evidence: MECH-191 (lit 0.86, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-191
Blocked by: experiment_proposals.v1.json EXP-0291 status=blocked_substrate: functional-state channels do not externalize >=2 differentially-active, cross-architecturally-consistent dimensions; scalar channel-norm readouts of tonic accumulators are satu
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (metaworker-chip-20260803-igw-confirm-mech191) recorded EXP-0291 status=blocked_substrate in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs un

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-235 -- Confirm evidence: MECH-269 (lit 0.84, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0579 status=deferred_substrate_not_ready: GOV-CONFIRM-1 SELF-ROUTE, 2026-08-04T01:15:12Z, session metaworker-chip-20260804-igw-confirm-mech269 (chip-20260804-igw-confirm-mech269, IGW-20260804-231 stable_hash
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (metaworker-chip-20260804-igw-confirm-mech269) recorded EXP-0579 status=deferred_substrate_not_ready in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer ar

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-235
Title: Confirm evidence: MECH-269 (lit 0.84, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-269
Blocked by: experiment_proposals.v1.json EXP-0579 status=deferred_substrate_not_ready: GOV-CONFIRM-1 SELF-ROUTE, 2026-08-04T01:15:12Z, session metaworker-chip-20260804-igw-confirm-mech269 (chip-20260804-igw-confirm-mech269, IGW-20260804-231 stable_hash
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (metaworker-chip-20260804-igw-confirm-mech269) recorded EXP-0579 status=deferred_substrate_not_ready in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer ar

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-236 -- Confirm evidence: MECH-489 (lit 0.83, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 55 | **Generation:** v3
- **Why now:** GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.83, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-236
Title: Confirm evidence: MECH-489 (lit 0.83, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-489
Why now: GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), lit_conf 0.83, ZERO experimental evidence. Scope a WALL-INDEPENDENT representation/functional-signature confirming DV (self-route substrate_not_ready_requeue if only a behavi

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-237 -- Confirm evidence: MECH-282 (lit 0.82, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0524 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_600a) already ran (supports) but is held pending substrate, not promotable by an identical rerun.
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0524 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-237
Title: Confirm evidence: MECH-282 (lit 0.82, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-282
Blocked by: experiment_proposals.v1.json EXP-0524 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_600a) already ran (supports) but is held pending substrate, not promotable by an identical rerun.
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0524 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-238 -- Confirm evidence: MECH-338 (lit 0.79, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0344 status=gated: MECH-338 is the 'select-face' child mechanism of ARC-077 (EXP-0311): 'Structural slot only; hard-gated on the GAP-L biology lit-pull.' Same absent caregiver-agent substrate as its parent.
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (elastic-merkle-e0cca8) recorded EXP-0344 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-238
Title: Confirm evidence: MECH-338 (lit 0.79, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-338
Blocked by: experiment_proposals.v1.json EXP-0344 status=gated: MECH-338 is the 'select-face' child mechanism of ARC-077 (EXP-0311): 'Structural slot only; hard-gated on the GAP-L biology lit-pull.' Same absent caregiver-agent substrate as its parent.
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (elastic-merkle-e0cca8) recorded EXP-0344 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-239 -- Confirm evidence: SD-099 (lit 0.78, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0330 status=gated: GOV-REUSE-1 (/queue-experiment Step 2.4) routes this to 'do not queue': BOTH halves of SD-099's own what_would_answer are already accounted for, so a fresh targeted probe would be duplicat
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (igw-229-proposal-for-sd-099) recorded EXP-0330 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-239
Title: Confirm evidence: SD-099 (lit 0.78, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: SD-099
Blocked by: experiment_proposals.v1.json EXP-0330 status=gated: GOV-REUSE-1 (/queue-experiment Step 2.4) routes this to 'do not queue': BOTH halves of SD-099's own what_would_answer are already accounted for, so a fresh targeted probe would be duplicat
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (igw-229-proposal-for-sd-099) recorded EXP-0330 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-240 -- Confirm evidence: MECH-186 (lit 0.74, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0098 status=gated: the exact test this proposes (floor clamp on VALENCE_WANTING, i.e. 'valence_wanting_floor') has already run twice: v3_exq_251_mech186_valence_wanting_floor (runs ...1775504875_v3 and ...17
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (elastic-merkle-e0cca8) recorded EXP-0098 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-240
Title: Confirm evidence: MECH-186 (lit 0.74, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-186
Blocked by: experiment_proposals.v1.json EXP-0098 status=gated: the exact test this proposes (floor clamp on VALENCE_WANTING, i.e. 'valence_wanting_floor') has already run twice: v3_exq_251_mech186_valence_wanting_floor (runs ...1775504875_v3 and ...17
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (elastic-merkle-e0cca8) recorded EXP-0098 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-241 -- Confirm evidence: MECH-340 (lit 0.69, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0547 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_607) already ran (supports) but is held pending substrate.
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0547 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-241
Title: Confirm evidence: MECH-340 (lit 0.69, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-340
Blocked by: experiment_proposals.v1.json EXP-0547 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_607) already ran (supports) but is held pending substrate.
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0547 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-242 -- Confirm evidence: MECH-339 (lit 0.67, exp ~0)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 55 | **Generation:** v3
- **Blocked by:** experiment_proposals.v1.json EXP-0534 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_594) already ran (supports) but is held pending substrate.
- **Why now:** ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0534 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-242
Title: Confirm evidence: MECH-339 (lit 0.67, exp ~0)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-339
Blocked by: experiment_proposals.v1.json EXP-0534 status=gated: hold_pending_v3_substrate governance verdict + v3_pending=true; suggested design (v3_exq_594) already ran (supports) but is held pending substrate.
Why now: ALREADY ADJUDICATED -- do not re-investigate. A prior session (determined-ritchie-55a3a6) recorded EXP-0534 status=gated in experiment_proposals.v1.json. See blocked_by; re-runs of this confirmer are NO-OPs until that status is cleared.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Design the experiment for the Claims id above (the stable target). To read the backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-012 -- Soothing / comfort autonomic state-gain modulator (MECH-355) -- V4-social

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-5
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-012
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

### IGW-20260826-013 -- Laughter regime-transition discharge (MECH-364) + crying/distress-vocalisation analogue and laughter-valence adjudicatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** affect_expression_v4:AE-6
- **Blocked by:** affect_expression_v4:AE-2 [in_progress]
- **Why now:** Plan gap blocked on affect_expression_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-013
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

### IGW-20260826-020 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-020
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

### IGW-20260826-026 -- Candidate-gradient episode content schema (MECH-361): affect gradient as write-weight + retrieval-query

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-6
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-026
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

### IGW-20260826-027 -- Switchable episodic perspective tag (MECH-366): participant/observer viewpoint as a represented, switchable property

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** autobiographical_memory_v4:ABM-7
- **Blocked by:** autobiographical_memory_v4:ABM-2 [blocked]
- **Why now:** Plan gap blocked on autobiographical_memory_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-027
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

### IGW-20260826-031 -- Theory 7 (blocked on GAP-B): MECH-314 curiosity weight (Goldilocks calibration)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** behavioral_diversity_isolation:GAP-G
- **Blocked by:** behavioral_diversity_isolation:GAP-B [partial]
- **Why now:** BLOCKED ON behavioral_diversity_isolation:GAP-B only (status partial, severity load-bearing -- behavioural-diversity landing). Gate 1 of this node's original two-gate hold HAS CLEARED and its text is superseded: per-candidate RBF novelty la

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-031
Title: Theory 7 (blocked on GAP-B): MECH-314 curiosity weight (Goldilocks calibration)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): behavioral_diversity_isolation:GAP-G
Claims: MECH-314, MECH-314a
Blocked by: behavioral_diversity_isolation:GAP-B [partial]
Why now: BLOCKED ON behavioral_diversity_isolation:GAP-B only (status partial, severity load-bearing -- behavioural-diversity landing). Gate 1 of this node's original two-gate hold HAS CLEARED and its text is superseded: per-candidate RBF novelty la

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-036 -- Attention (distributed precision-selection) grounding -- containment, not a module

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-6
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-036
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

### IGW-20260826-037 -- Ethics / commitment policy grounding (or honest 'no clean analog')

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** biology_grounding_convergence_v4:BG-7
- **Why now:** Plan gap blocked on biology_grounding_convergence_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-037
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

### IGW-20260826-040 -- MECH-091 salient-event trigger wiring (2 of 3 triggers unwired; phase_reset itself is built)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** commitment_closure:GAP-7
- **Why now:** Plan gap blocked on commitment_closure.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-040
Title: MECH-091 salient-event trigger wiring (2 of 3 triggers unwired; phase_reset itself is built)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): commitment_closure:GAP-7
Claims: MECH-091
Why now: Plan gap blocked on commitment_closure.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-055 -- Distancing operator (MECH-382): first/third-person reframe as an arbitration-altering control move

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-6
- **Blocked by:** developmental_dmn_v4:DMN-2 [blocked]; developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-055
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

### IGW-20260826-056 -- Labels as top-down perceptual-control signals (MECH-383): self-directed labels tune perceptual search

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** developmental_dmn_v4:DMN-7
- **Blocked by:** developmental_dmn_v4:DMN-4 [blocked]
- **Why now:** Plan gap blocked on developmental_dmn_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-056
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

### IGW-20260826-065 -- Prescriptive + diagnostic ethical-trajectory certification: CBF forward-invariance + backward-reachability barrier certi

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** ethics_as_coherence_v5:ETH-6
- **Blocked by:** ethics_as_coherence_v5:ETH-1 [blocked]; ethics_as_coherence_v5:ETH-5 [blocked]
- **Why now:** Plan gap blocked on ethics_as_coherence_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-065
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

### IGW-20260826-076 -- MECH-191 cross-architecture legibility unblock check (does A's dispositional readout resolve the tonic-channel gap?)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** global_workspace_jlens:MECH-191
- **Blocked by:** global_workspace_jlens:A [blocked]
- **Why now:** Plan gap open on global_workspace_jlens.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-076
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

### IGW-20260826-081 -- PILLAR 5 -- capacity-limited E3 access gate + attentional template (SD-027/SD-028/MECH-254/MECH-255) feeding deliberatio

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** goal_deliberation_v4:GDL-6
- **Why now:** Plan gap blocked on goal_deliberation_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-081
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

### IGW-20260826-084 -- V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-4
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-084
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

### IGW-20260826-085 -- Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandone

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v6
- **Gap(s):** grammar_primitive_mining_v6:GRAM-5
- **Blocked by:** grammar_primitive_mining_v6:GRAM-2 [open]
- **Why now:** Plan gap blocked on grammar_primitive_mining_v6.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-085
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

### IGW-20260826-092 -- ACh permissive write-gate on the surprise buffer (MECH-207)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-6
- **Blocked by:** hippocampal_planning_v4:HPL-1 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-092
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

### IGW-20260826-093 -- Schema-primed rapid assimilation (INV-039)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** hippocampal_planning_v4:HPL-7
- **Blocked by:** hippocampal_planning_v4:HPL-2 [blocked]
- **Why now:** Plan gap blocked on hippocampal_planning_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-093
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

### IGW-20260826-127 -- Gated-write-authority on consolidation (over-frequent rewriting is a failure mode)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v4
- **Gap(s):** memory_lifecycle_v4:MEM-7
- **Why now:** Plan gap blocked on memory_lifecycle_v4.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-127
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

### IGW-20260826-133 -- Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** mirror_modelling_other_self_v5:MIRROR-6
- **Blocked by:** mirror_modelling_other_self_v5:MIRROR-2 [blocked]
- **Why now:** Plan gap blocked on mirror_modelling_other_self_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-133
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

### IGW-20260826-140 -- Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v5
- **Gap(s):** multi_agent_ecology_v5:MAE-6
- **Blocked by:** multi_agent_ecology_v5:MAE-2 [blocked]
- **Why now:** Plan gap blocked on multi_agent_ecology_v5.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-140
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

### IGW-20260826-155 -- orient/survey: third primitive behavioural regime (diffuse, epistemic_deficit-driven)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** orienting_epistemic_deficit_v3:ORNT-3
- **Blocked by:** orienting_epistemic_deficit_v3:ORNT-2 [open]
- **Why now:** Plan gap open on orienting_epistemic_deficit_v3.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-155
Title: orient/survey: third primitive behavioural regime (diffuse, epistemic_deficit-driven)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): orienting_epistemic_deficit_v3:ORNT-3
Claims: MECH-483
Blocked by: orienting_epistemic_deficit_v3:ORNT-2 [open]
Why now: Plan gap open on orienting_epistemic_deficit_v3.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/orienting_epistemic_deficit_v3_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-156 -- Open Q: does epistemic-deficit-driven orienting explain the cold-start competence split?

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** orienting_epistemic_deficit_v3:ORNT-4
- **Blocked by:** orienting_epistemic_deficit_v3:ORNT-2 [open]; orienting_epistemic_deficit_v3:ORNT-3 [open]
- **Why now:** Plan gap open on orienting_epistemic_deficit_v3.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-156
Title: Open Q: does epistemic-deficit-driven orienting explain the cold-start competence split?
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): orienting_epistemic_deficit_v3:ORNT-4
Claims: Q-089
Blocked by: orienting_epistemic_deficit_v3:ORNT-2 [open]; orienting_epistemic_deficit_v3:ORNT-3 [open]
Why now: Plan gap open on orienting_epistemic_deficit_v3.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/orienting_epistemic_deficit_v3_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-197 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-197
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

### IGW-20260826-198 -- SD-031 z_world causal-footprint comparator: V3 discriminative validation

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58 | **Generation:** v3
- **Gap(s):** self_attribution:GAP-6
- **Why now:** Both halves of the claims.yaml SD-031 evidence_quality_note gate must hold before the discriminative/attribution arm is queued: world_dim >= 128 AND behavioural diversity live in the main agent path. The claim registry states this as a proh

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-198
Title: SD-031 z_world causal-footprint comparator: V3 discriminative validation
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_attribution:GAP-6
Claims: SD-031
Why now: Both halves of the claims.yaml SD-031 evidence_quality_note gate must hold before the discriminative/attribution arm is queued: world_dim >= 128 AND behavioural diversity live in the main agent path. The claim registry states this as a proh

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-001 -- Held pending substrate: Q-094

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60 | **Generation:** v3
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-001
Title: Held pending substrate: Q-094
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: Q-094
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260826-002 -- Held pending substrate: Q-095

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60 | **Generation:** v3
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260826-002
Title: Held pending substrate: Q-095
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: Q-095
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>
