# Inter-Governance Workset

Generated: `2026-06-09T21:02:54Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **59** (ready 8, in_flight 1, blocked 35)
- Pending review: **4**
- Queue pending (unclaimed): **0**

- Live EXQs: V3-EXQ-603l, V3-EXQ-640b, V3-EXQ-654a, V3-EXQ-655

- Auto-absorbed retests (queued, suppressed from workset): INV-074 -> V3-EXQ-655, MECH-309 -> V3-EXQ-654a, SD-059 -> V3-EXQ-603l

## Work packages

### IGW-20260609-001 -- Complete governance review (4 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 4 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-001
Title: Complete governance review (4 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 4 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-002 -- Governance decision: ARC-046

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 8
- **Why now:** promotion_demotion recommends hold_candidate_resolve_conflict.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-002
Title: Governance decision: ARC-046
Lane: governance | Skill: /governance
Status: ready
Claims: ARC-046
Why now: promotion_demotion recommends hold_candidate_resolve_conflict.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-036 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=implemented with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-036
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

### IGW-20260609-038 -- Implement substrate: escape-affordance-bridge (unblocks ARC-060)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
- **Why now:** substrate_queue entry status=pending_implementation with 5 unresolved prerequisite(s); blocks retest of ARC-060. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-038
Title: Implement substrate: escape-affordance-bridge (unblocks ARC-060)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-058, MECH-357, ARC-060, MECH-320, ARC-068, SD-054-readiness
Blocked by: ready=false (no ready_blocked_by detail); SD-058 [no-substrate-entry]: SD-058; MECH-357 [no-substrate-entry]: MECH-357; MECH-303 [no-substrate-entry]: MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry]: SD-011 (z_harm_a)
Why now: substrate_queue entry status=pending_implementation with 5 unresolved prerequisite(s); blocks retest of ARC-060. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-040 -- Implement substrate: ARC-062 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-040
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

### IGW-20260609-041 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.; ARC-062 [implemented]
- **Why now:** substrate_queue entry status=candidate_v3_pending with 2 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-041
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

### IGW-20260609-044 -- Implement substrate: SD-049 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 1 (env-only substrate) IMPLEMENTED 2026-05-03 (SD-047 file released). Phase 2 (z_resource encoder identity expansion + SD-032 consumer cascade reading per_axis_drive directly + V3-EXQ-514 behavi
- **Why now:** substrate_queue entry status=phase_1_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-044
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

### IGW-20260609-045 -- Implement substrate: SD-049-PHASE-2 (unblocks MECH-229)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: Phase 2 hybrid encoder IMPLEMENTED 2026-05-04 (Option C per verdict.md). V3-EXQ-514 behavioural validation queued. PASS unblocks SD-049 v3_pending clearance. FAIL on row-6 falsifier (joint ARM_2+ARM_3
- **Why now:** substrate_queue entry status=phase_2_implemented with 1 unresolved prerequisite(s); blocks retest of MECH-229. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-045
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

### IGW-20260609-047 -- Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-634c (seeding-calibrated nursery: gating floor matched to seeding floor + GoalConfig seeding-magnitude sweep + consumption-event-gated G3) must clear the substrate readiness gates on >=2/3 seed; SD-054 [candidate_v3_pending]; MECH-307 [implemented]
- **Why now:** substrate_queue entry status=curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold co

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-047
Title: Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-030, MECH-117, MECH-230, MECH-260, MECH-295, MECH-307
Blocked by: ready_blocked_by: V3-EXQ-634c (seeding-calibrated nursery: gating floor matched to seeding floor + GoalConfig seeding-magnitude sweep + consumption-event-gated G3) must clear the substrate readiness gates on >=2/3 seed; SD-054 [candidate_v3_pending]; MECH-307 [implemented]
Why now: substrate_queue entry status=curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold co

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-048 -- Implement substrate: MECH-307 (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-048
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

### IGW-20260609-052 -- Implement substrate: SD-033 (unblocks MECH-266)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail); MECH-094 [no-substrate-entry]: MECH-094; MECH-261 [no-substrate-entry]: MECH-261; ARC-035 [no-substrate-entry]: ARC-035; MECH-116 [no-substrate-entry]: MECH-116; MECH-151 [no-substrate-entry]: MECH-151; MECH-152 [no-substrate-entry]: MECH-152; MECH-235 [no-substrate-entry]: MECH-235
- **Why now:** substrate_queue entry status=unknown with 8 unresolved prerequisite(s); blocks retest of MECH-266. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-052
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

### IGW-20260609-054 -- Implement substrate: SD-037 (unblocks MECH-280)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-280. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-054
Title: Implement substrate: SD-037 (unblocks MECH-280)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-280, MECH-281
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented with 1 unresolved prerequisite(s); blocks retest of MECH-280. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-033 -- Substrate (blocked): SD-033b

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 25
- **Blocked by:** SD-033 [unknown]; MECH-263 [no-substrate-entry]: MECH-263; MECH-261 [no-substrate-entry]: MECH-261
- **Why now:** substrate_queue ready=true but 3 unresolved prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-033
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

### IGW-20260609-035 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [implemented]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-035
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

### IGW-20260609-037 -- Retest after substrate: ARC-060

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [pending_implementation]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-037
Title: Retest after substrate: ARC-060
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-060
Blocked by: escape-affordance-bridge [pending_implementation]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-039 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]; SD-054 [candidate_v3_pending]; ARC-062 [implemented] (transitive via SD-054)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-039
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

### IGW-20260609-042 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** escape-affordance-bridge [pending_implementation]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
- **Why now:** Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-042
Title: Retest after substrate: ARC-068
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-068
Blocked by: escape-affordance-bridge [pending_implementation]; SD-058 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-058; MECH-357 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-357; MECH-303 [no-substrate-entry] (transitive via escape-affordance-bridge): MECH-303/304 (safety; built, needs wiring); SD-011 [no-substrate-entry] (transitive via escape-affordance-bridge): SD-011 (z_harm_a)
Why now: Blocked by 5 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-043 -- Retest after substrate: MECH-229

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 2 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-043
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

### IGW-20260609-046 -- Retest after substrate: MECH-230

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-046
Title: Retest after substrate: MECH-230
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-230
Blocked by: SD-049 [phase_1_implemented]; SD-049-PHASE-2 [phase_2_implemented]; scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 5 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-049 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-049
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 3 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-050 -- Retest after substrate: MECH-262

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-062 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-050
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

### IGW-20260609-051 -- Retest after substrate: MECH-266

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
- **Why now:** Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-051
Title: Retest after substrate: MECH-266
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-266
Blocked by: SD-033 [unknown]; MECH-094 [no-substrate-entry] (transitive via SD-033): MECH-094; MECH-261 [no-substrate-entry] (transitive via SD-033): MECH-261; ARC-035 [no-substrate-entry] (transitive via SD-033): ARC-035; MECH-116 [no-substrate-entry] (transitive via SD-033): MECH-116; MECH-151 [no-substrate-entry] (transitive via SD-033): MECH-151; MECH-152 [no-substrate-entry] (transitive via SD-033): MECH-152; MECH-235 [no-substrate-entry] (transitive via SD-033): MECH-235; scaffolded_sd054_onboarding [curriculum_decomposition_IMPLEMENTED_2026_06_07 (isolated hazard-avoidance Stage-H between P0 and P1: goal-frozen, hazards present, foraging minimal, hfa=0, midline spawn; ree-v3 harness-layer, 85/85 scaffold contracts + 7/7 preflight PASS, bit-identical OFF). 603f PROVED goal-formation+ecological-seeding sound (seed 44 foraged 0.393 + seeded z_goal 0.450) -> sole GAP-2 blocker is the P1 survival/hazard-avoidance leg (G1 0/3). ready STAYS false until V3-EXQ-603g (Stage-H ON) clears G1>=2/3 AND G2>=2/3 AND ecological G3>=2/3 against the SAME gate.]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding); MECH-307 [implemented] (transitive via scaffolded_sd054_onboarding)
Why now: Blocked by 11 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-053 -- Retest after substrate: MECH-280

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-037 [implemented]
- **Why now:** substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-053
Title: Retest after substrate: MECH-280
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-280
Blocked by: SD-037 [implemented]
Why now: substrate_ceiling -- awaiting substrate enrichment; blocked by 1 unresolved prerequisite(s). See blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-015 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS; MECH-341 GAP-A-ready retest owed, not queued
- **Why now:** PARTIAL 2026-06-08. V3-EXQ-614e is fully autopsied and applied as non_contributory/substrate_ceiling, not pending adjudication. GAP-A is now ready via V3-EXQ-649 PASS, so queue the MECH-341 committed-class diversity retest on the GAP-A-read

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-015
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-614e autopsy applied 2026-06-07 (non_contributory substrate_ceiling; GAP-A blocker moved upstream); V3-EXQ-649 GAP-A readiness PASS; MECH-341 GAP-A-ready retest owed, not queued
Claims: MECH-341, ARC-062, ARC-065
Why now: PARTIAL 2026-06-08. V3-EXQ-614e is fully autopsied and applied as non_contributory/substrate_ceiling, not pending adjudication. GAP-A is now ready via V3-EXQ-649 PASS, so queue the MECH-341 committed-class diversity retest on the GAP-A-read

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-025 -- Phase 1b -- substrate-readiness diagnostic: re-run the V3-EXQ-620 protocol under SD-029 scheduled-external-hazard curric

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** sd_037_axis_b:P1b
- **Owner EXQ:** V3-EXQ-625c
- **Why now:** RESUME the Phase 1b gate (or its successor) once the behavioural-diversity substrate amend lands and the agent generates oscillating, non-monostrategy z_harm_a under the axis-(b) env overlay. SD-037 status is unchanged: the substrate_ceilin

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-025
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

### IGW-20260609-009 -- MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 33
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
- **Why now:** BOTH routed steps are now DONE (see governance_2026_06_09_amend_and_requeue): the crf_persist amend LANDED (ree-v3 9797e84) and V3-EXQ-654a is QUEUED (priority 250, machine any). RESUME when V3-EXQ-654a RUNS + lands a manifest + is reviewed

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-009
Title: MECH-309/ARC-062 behavioural falsifier now unblocked by CandidateRuleField + GAP-A + authority readiness
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-654a QUEUED 2026-06-09 (priority 250, machine any; supersedes V3-EXQ-654) -- the gated re-run on the landed cross-episode rule-persistence amend (ree-v3 main 9797e84). Single-variable ARM_OFF vs ARM_ON with crf_persist_rules_across_episode_reset=True (matured pool clears the C1c 0.30 floor), a frozen-encoder P1 trained-bias-head REINFORCE phase (GAP-D), and a propagation non-vacuity precondition (ARM_ON bias != ARM_OFF, else substrate_not_ready_requeue); committed-class entropy PRIMARY DV. PREDECESSOR V3-EXQ-654 TERMINAL FAIL 2026-06-09T08:18Z (non_contributory, confirmed failure_autopsy_V3-EXQ-654_2026-06-09): C1c readiness FAIL (CandidateRuleField cold-started per episode) gated out the C2 falsifier DV -- NOT a falsification.
Claims: MECH-309, ARC-062
Why now: BOTH routed steps are now DONE (see governance_2026_06_09_amend_and_requeue): the crf_persist amend LANDED (ree-v3 9797e84) and V3-EXQ-654a is QUEUED (priority 250, machine any). RESUME when V3-EXQ-654a RUNS + lands a manifest + is reviewed

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-034 -- Queue depth low (0 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-034
Title: Queue depth low (0 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-021 -- Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_pipeline:GAP-7
- **Blocked by:** goal_pipeline:GAP-2 [blocked_pending_substrate]
- **Why now:** STATUS 2026-06-05: the L2-L3-L4 object-binding + incentive-token substrate AND the L6-L7 cue-recall + dACC-readout layer ARE BUILT AND REGISTERED -- see l2l3_l6_l7_landed_2026_06_04 below. The earlier draft of this field (now superseded) in

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-021
Title: Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit
Lane: plan | Skill: (plan reconcile)
Status: blocked
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

### IGW-20260609-017 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629)
- **Why now:** MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes (2026-05-28 within-tick score_margin axis + 2026-05-29 across-tick CommitReadiness EMA / nav_competence axis; 523/523 contracts PASS masters OFF). V3-EXQ-592d (4

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-017
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629)
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090, MECH-342
Why now: MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes (2026-05-28 within-tick score_margin axis + 2026-05-29 across-tick CommitReadiness EMA / nav_competence axis; 523/523 contracts PASS masters OFF). V3-EXQ-592d (4

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-019 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514l
- **Why now:** RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-019
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

### IGW-20260609-020 -- MECH-295 drive->liking->approach cascade Tier-1 retest cohort

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-4
- **Owner EXQ:** V3-EXQ-490k TERMINAL 2026-06-04 (modulatory-sufficiency argmin-flip probe; ran PASS/probe_ran but non_contributory per confirmed failure_autopsy_V3-EXQ-490k -- ROW_2_fires_but_never_flips, mech295_bias_range_mean=0.0 so argmin cannot flip BY CONSTRUCTION; reviewed /governance 2026-06-04 pm); NEXT successor V3-EXQ-490L on enriched substrate with a pre-registered mech295_bias_range_mean>0 guard. Prior: V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; modulatory-not-necessary established at substrate-firing layer; supersedes 490i); lineage V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i (superseded by 490j)
- **Why now:** Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 behavioural-necessity falsified, modulatory reading substrate-supported. NEXT is a governance decision (re-scope MECH-295 to modulatory + close GAP-4, O

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-020
Title: MECH-295 drive->liking->approach cascade Tier-1 retest cohort
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): goal_pipeline:GAP-4
Owner EXQ: V3-EXQ-490k TERMINAL 2026-06-04 (modulatory-sufficiency argmin-flip probe; ran PASS/probe_ran but non_contributory per confirmed failure_autopsy_V3-EXQ-490k -- ROW_2_fires_but_never_flips, mech295_bias_range_mean=0.0 so argmin cannot flip BY CONSTRUCTION; reviewed /governance 2026-06-04 pm); NEXT successor V3-EXQ-490L on enriched substrate with a pre-registered mech295_bias_range_mean>0 guard. Prior: V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; modulatory-not-necessary established at substrate-firing layer; supersedes 490i); lineage V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i (superseded by 490j)
Claims: MECH-295, ARC-030, MECH-117, Q-040
Why now: Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 behavioural-necessity falsified, modulatory reading substrate-supported. NEXT is a governance decision (re-scope MECH-295 to modulatory + close GAP-4, O

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-032 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-032
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

### IGW-20260609-055 -- Proposal EXP-0033 (MECH-333)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** directional_conflict_alert; low_exp_conf

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-055
Title: Proposal EXP-0033 (MECH-333)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-333
Why now: directional_conflict_alert; low_exp_conf

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-056 -- Proposal EXP-0120 (MECH-316)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-056
Title: Proposal EXP-0120 (MECH-316)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-316
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-057 -- Proposal EXP-0121 (MECH-317)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-057
Title: Proposal EXP-0121 (MECH-317)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-317
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-058 -- Proposal EXP-0126 (MECH-CBBL-PROPOSED)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-058
Title: Proposal EXP-0126 (MECH-CBBL-PROPOSED)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-CBBL-PROPOSED
Why now: lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-059 -- Proposal EXP-0128 (MECH-172)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-059
Title: Proposal EXP-0128 (MECH-172)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-172
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-026 -- Phase 2 (re-application) -- deterministic p70 recalibration over the Phase-1b manifest; emit a non-empty per-knob overri

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P2
- **Blocked by:** sd_037_axis_b:P1b [blocked_pending_substrate]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-026
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

### IGW-20260609-027 -- Phase 3 (re-application) -- verification diagnostic: recalibrated thresholds lift consumer outputs above zero; acceptanc

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P3
- **Blocked by:** sd_037_axis_b:P2 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-027
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

### IGW-20260609-028 -- Phase 4 (re-application) -- V3-EXQ-483f behavioural validation (4-arm 2x2) on the axis-(b)-recalibrated substrate

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** sd_037_axis_b:P4
- **Owner EXQ:** V3-EXQ-483f
- **Blocked by:** sd_037_axis_b:P3 [blocked]
- **Why now:** Plan gap blocked on sd_037_axis_b.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-028
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

### IGW-20260609-029 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-029
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

### IGW-20260609-030 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 me

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-030
Title: SD-029 / MECH-256 retest under full substrate stack
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): self_attribution:GAP-2
Claims: SD-029, MECH-256, ARC-033, SD-013
Why now: Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 me

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/self_attribution_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-010 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-604c PASS 2026-06-07 closed the Q-044/MECH-314-family GAP-A-ready leg; V3-EXQ-544/545/544a historical diagnostics; Q-045/MECH-313/MECH-260 leg awaits behavioral_diversity_isolation:GAP-C / V3-EXQ-603i; GAP-B successor still owed
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** PARTIAL 2026-06-08. Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS on validated GAP-A; do not queue another GAP-H curiosity retest for that leg. Hold the remaining Q-045/MECH-313/MECH-260 survival/noise-floor leg until V3-EXQ-60

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-010
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

### IGW-20260609-011 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-011
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

### IGW-20260609-013 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier LANDED PASS (supports) 2026-

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 LANDED PASS 2026-06-02 (experiment_purpose=evidence; supports MECH-319; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier; 3/3 seeds)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** IN-PROGRESS 2026-06-08. V3-EXQ-628 has satisfied the MECH-319 replay/write-gate evidence slice; do not re-queue that slice. GAP-K closure waits on the GAP-B successor, GAP-H remaining legs, and GAP-I multi-rule-context substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-013
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

### IGW-20260609-014 -- Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-A
- **Owner EXQ:** V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
- **Why now:** <!-- TODO: revise resume_condition to reflect V3-EXQ-544a + V3-EXQ-569c state --> V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-014
Title: Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-A
Owner EXQ: V3-EXQ-649 PASS 2026-06-07T13:14Z (GAP-A shared-channel substrate-readiness VALIDATED READY; consumed cand_world_summaries spread 0.090>=0.05 floor); V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
Claims: ARC-065
Why now: <!-- TODO: revise resume_condition to reflect V3-EXQ-544a + V3-EXQ-569c state --> V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path).

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-016 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-603k (Stage-H harm-pathway training; queued 2026-06-09; owns the PRIMARY nav/survival-competence leg this node waits on). Predecessors absorbed: V3-EXQ-603i TERMINAL FAIL 2026-06-08 (non_contributory substrate_ceiling, autopsied + applied /governance 2026-06-09T04:30Z) surfaced two co-equal substrate gaps -- PRIMARY nav/survival-competence ceiling (-> 603k) + SECONDARY safety-half starvation, the latter now closed at the readiness layer by V3-EXQ-603j PASS 2026-06-09 (safety-half trained-signal; safety_signal 0.89; claim_ids=[]). Prior 603a/b/c/f/g/h lineage non_contributory substrate-ceiling
- **Why now:** IN FLIGHT 2026-06-08 on V3-EXQ-603i. Do not queue the Q-045/MECH-313/MECH-260 retest until 603i lands. On 603i PASS/non-vacuous readiness, queue the GAP-C successor retest; on FAIL or substrate_not_ready_requeue, route to failure-autopsy/im

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-016
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

### IGW-20260609-018 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485c + V3-EXQ-485b (co-equal sibling diagnostics, both PASS, reviewed 2026-06-04; representation-level MECH-263 functional-signature validation -- 485c task-role discrimination + 485b devaluation sensitivity; NOT a supersession lineage)
- **Why now:** Plan gap in_progress on commitment_closure.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-018
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485c + V3-EXQ-485b (co-equal sibling diagnostics, both PASS, reviewed 2026-06-04; representation-level MECH-263 functional-signature validation -- 485c task-role discrimination + 485b devaluation sensitivity; NOT a supersession lineage)
Claims: SD-033b, MECH-263
Why now: Plan gap in_progress on commitment_closure.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-022 -- EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-11
- **Owner EXQ:** V3-EXQ-588b
- **Why now:** V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non_contributory for MECH-189 -- infant GoalState gate, not ContextMemory writes; env patches work (C2/C3). Do NOT re-queue 588. Follow-up V3-EXQ-588b go

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-022
Title: EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-11
Owner EXQ: V3-EXQ-588b
Claims: DEV-NEED-006, MECH-189
Why now: V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non_contributory for MECH-189 -- infant GoalState gate, not ContextMemory writes; env patches work (C2/C3). Do NOT re-queue 588. Follow-up V3-EXQ-588b go

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-023 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** V3-EXQ-590 ran 20260525T084057Z procedural PASS but evidence_direction=pending_retest_after_substrate with MECH-314 + MECH-111 per-claim non_contributory: Goldilocks calibration is degenerate across novelty_bonus_weight 0.1..1.0 (all 5 arms

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-023
Title: EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): infant_substrate:GAP-13
Owner EXQ: V3-EXQ-590
Claims: DEV-NEED-003, MECH-314
Why now: V3-EXQ-590 ran 20260525T084057Z procedural PASS but evidence_direction=pending_retest_after_substrate with MECH-314 + MECH-111 per-claim non_contributory: Goldilocks calibration is degenerate across novelty_bonus_weight 0.1..1.0 (all 5 arms

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-024 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-024
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

### IGW-20260609-012 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-012
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

### IGW-20260609-031 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-031
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

### IGW-20260609-003 -- Held pending substrate: ARC-072

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-003
Title: Held pending substrate: ARC-072
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-072
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-004 -- Held pending substrate: MECH-121

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-004
Title: Held pending substrate: MECH-121
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-121
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-005 -- Held pending substrate: MECH-346

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-005
Title: Held pending substrate: MECH-346
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-346
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-006 -- Held pending substrate: MECH-347

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-006
Title: Held pending substrate: MECH-347
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-347
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-007 -- Held pending substrate: SD-055

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-007
Title: Held pending substrate: SD-055
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-055
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260609-008 -- Held pending substrate: SD-057

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 60
- **Blocked by:** V3 substrate implementation / per-claim retest
- **Why now:** promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260609-008
Title: Held pending substrate: SD-057
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-057
Blocked by: V3 substrate implementation / per-claim retest
Why now: promotion_demotion verdict is `hold_pending_v3_substrate` -- governance is HELD pending substrate, not a decision to make in /governance. Unblocks when the substrate lands AND a per-claim retest supplies V3 evidence.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>
