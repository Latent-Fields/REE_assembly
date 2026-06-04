# Inter-Governance Workset

Generated: `2026-06-04T06:13:21Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **44** (ready 14, in_flight 0, blocked 15)
- Pending review: **8**
- Queue pending (unclaimed): **0**

- Live EXQs: V3-EXQ-610e, V3-EXQ-634c

- Auto-absorbed retests (queued, suppressed from workset): INV-074 -> V3-EXQ-610e

## Work packages

### IGW-20260604-001 -- Complete governance review (8 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 8 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-001
Title: Complete governance review (8 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 8 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-002 -- Governance decision: SD-034

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 8
- **Why now:** promotion_demotion recommends demote_to_candidate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-002
Title: Governance decision: SD-034
Lane: governance | Skill: /governance
Status: ready
Claims: SD-034
Why now: promotion_demotion recommends demote_to_candidate.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-027 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** substrate_queue entry status=pending_implementation with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-027
Title: Implement substrate: ARC-046 (unblocks ARC-046)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-046, DEV-NEED-008
Blocked by: ready_blocked_by: V3 substrate prerequisite (NOT V4 deferral): goal-pipeline / training-regime substrate enrichment so trained policy survives SD-054 enrichment in default V3 config (V3-EXQ-603c FAIL 2026-05-27 -- requ; free-text: goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
Why now: substrate_queue entry status=pending_implementation with 2 unresolved prerequisite(s); blocks retest of ARC-046. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-029 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.
- **Why now:** substrate_queue entry status=candidate_v3_pending with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-029
Title: Implement substrate: SD-054 (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: SD-054, MECH-309, ARC-062
Blocked by: ready_blocked_by: V3-EXQ-543b PASS on the new gated-policy + reef + hazard_food_attraction substrate stack.
Why now: substrate_queue entry status=candidate_v3_pending with 1 unresolved prerequisite(s); blocks retest of ARC-062. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-031 -- Implement substrate: modulatory-bias-selection-authority (unblocks ARC-068)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready=false (no ready_blocked_by detail)
- **Why now:** substrate_queue entry status=implemented_pending_validation with 1 unresolved prerequisite(s); blocks retest of ARC-068. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-031
Title: Implement substrate: modulatory-bias-selection-authority (unblocks ARC-068)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: MECH-314, MECH-314a, MECH-314b, MECH-314c, Q-044, MECH-320
Blocked by: ready=false (no ready_blocked_by detail)
Why now: substrate_queue entry status=implemented_pending_validation with 1 unresolved prerequisite(s); blocks retest of ARC-068. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-034 -- Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** blocked | **Priority:** 20
- **Blocked by:** ready_blocked_by: V3-EXQ-634c (seeding-calibrated nursery: gating floor matched to seeding floor + GoalConfig seeding-magnitude sweep + consumption-event-gated G3) must clear the substrate readiness gates on >=2/3 seed; SD-054 [candidate_v3_pending]
- **Why now:** substrate_queue entry status=seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0) with 2 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-034
Title: Implement substrate: scaffolded_sd054_onboarding (unblocks MECH-230)
Lane: substrate | Skill: /implement-substrate
Status: blocked
Claims: ARC-030, MECH-117, MECH-230, MECH-260, MECH-295, MECH-307
Blocked by: ready_blocked_by: V3-EXQ-634c (seeding-calibrated nursery: gating floor matched to seeding floor + GoalConfig seeding-magnitude sweep + consumption-event-gated G3) must clear the substrate readiness gates on >=2/3 seed; SD-054 [candidate_v3_pending]
Why now: substrate_queue entry status=seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0) with 2 unresolved prerequisite(s); blocks retest of MECH-230. See blocked_by.

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-023 -- Substrate ready: MECH-341

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 25
- **Why now:** See ree-v3/ree_core/predictors/e3_score_diversity.py + REEConfig.e3_diversity_entropy_bias_scale + REEConfig.e3_diversity_min_classes_for_stratification. The retune is parameter-only; module surface a

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-023
Title: Substrate ready: MECH-341
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: MECH-341
Why now: See ree-v3/ree_core/predictors/e3_score_diversity.py + REEConfig.e3_diversity_entropy_bias_scale + REEConfig.e3_diversity_min_classes_for_stratification. The retune is parameter-only; module surface a

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-024 -- Substrate ready: MECH-090

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 25
- **Why now:** Substrate LANDED in two passes (R-c reading per synthesis verdict). Pass 1 (2026-05-28, within-tick decisiveness axis): ree-v3/ree_core/heartbeat/beta_gate.py (BetaGate.should_admit_elevation predicat

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-024
Title: Substrate ready: MECH-090
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: MECH-090, SD-034, MECH-266, MECH-267, MECH-268
Why now: Substrate LANDED in two passes (R-c reading per synthesis verdict). Pass 1 (2026-05-28, within-tick decisiveness axis): ree-v3/ree_core/heartbeat/beta_gate.py (BetaGate.should_admit_elevation predicat

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-026 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [pending_implementation]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
- **Why now:** Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-026
Title: Retest after substrate: ARC-046
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-046
Blocked by: ARC-046 [pending_implementation]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4; owned today by IGW-20260528-
Why now: Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-028 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-054 [candidate_v3_pending]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-028
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-062
Blocked by: SD-054 [candidate_v3_pending]
Why now: Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-030 -- Retest after substrate: ARC-068

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** modulatory-bias-selection-authority [implemented_pending_validation]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-030
Title: Retest after substrate: ARC-068
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-068
Blocked by: modulatory-bias-selection-authority [implemented_pending_validation]
Why now: Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-032 -- Retest after substrate: MECH-229

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-032
Title: Retest after substrate: MECH-229
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-229
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-033 -- Retest after substrate: MECH-230

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0)]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding)
- **Why now:** Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-033
Title: Retest after substrate: MECH-230
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-230
Blocked by: scaffolded_sd054_onboarding [seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0)]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding)
Why now: Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-035 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** scaffolded_sd054_onboarding [seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0)]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding)
- **Why now:** Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-035
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-260
Blocked by: scaffolded_sd054_onboarding [seeding_calibration_amend_implemented_pending_validation (V3-EXQ-634c); 634b validated consolidation half (G0/G0b 3/3, decay_only=0)]; SD-054 [candidate_v3_pending] (transitive via scaffolded_sd054_onboarding)
Why now: Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-036 -- Retest after substrate: MECH-262

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-036
Title: Retest after substrate: MECH-262
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-262
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-037 -- Retest after substrate: MECH-280

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-037
Title: Retest after substrate: MECH-280
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-280
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-038 -- Retest after substrate: MECH-281

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-038
Title: Retest after substrate: MECH-281
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-281
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-039 -- Retest after substrate: MECH-309

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-054 [candidate_v3_pending]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-039
Title: Retest after substrate: MECH-309
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-309
Blocked by: SD-054 [candidate_v3_pending]
Why now: Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-003 -- MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-543l
- **Why now:** 2026-05-27 GOVERNANCE UPDATE: V3-EXQ-543l ran 20260526T023059Z FAIL branch-e at escalated floor=0.5 / aux=0.3 with basin_stable=true; all four diff-ON gated arms 3/3 inert. failure_autopsy_V3-EXQ-543l_2026-05-27 (status: confirmed) applied:

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-003
Title: MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-543l
Claims: MECH-309, ARC-062
Why now: 2026-05-27 GOVERNANCE UPDATE: V3-EXQ-543l ran 20260526T023059Z FAIL branch-e at escalated floor=0.5 / aux=0.3 with basin_stable=true; all four diff-ON gated arms 3/3 inert. failure_autopsy_V3-EXQ-543l_2026-05-27 (status: confirmed) applied:

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-009 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-614d (terminal 2026-06-03: PASS C1/C3, FAIL C2; diagnostic/scoring-excluded; supersedes 614c; reviewed 2026-06-03 -- within-class temperature lever ACTIVE but ZERO committed-action authority; see governance_2026_06_03); V3-EXQ-614c (queued 2026-06-01 via /implement-substrate amend session; 4-arm within-class temperature sweep stratified_within_class_temperature in {None=legacy, 0.5, 1.0, 2.0} on SD-056-amended baseline; cross-plan beneficiary arc_062_rule_apprehension:GAP-B); V3-EXQ-614b FAIL_no_criterion 2026-05-31 (C1=False structural degeneracy + C2=0.087 below threshold + C3=True ALL_ON 0.800 nats; per-claim non_contributory on MECH-341 + ARC-065 via /governance; routed to amend per failure_autopsy_V3-EXQ-616 Sections 7 + 10 contingent path); V3-EXQ-614b (queued 2026-05-31T12:32Z via /queue-experiment; 3-arm behavioural re-run on SD-056-amended substrate, supersedes V3-EXQ-614a; 5 SD-056 amend lever flags applied uniformly across all 3 arms: e2_action_contrastive_multistep_enabled=True h=5, e2_rollout_output_norm_clamp_enabled=True ratio=2.0, e2_action_contrastive_enabled=True weight=0.01; same env_kwargs + acceptance criteria as 614a; 4-row interpretation grid copied verbatim + header note that under amended substrate PASS via C1 is now the load-bearing target since 614a established PASS via C2+C3); V3-EXQ-614a (queued 2026-05-30 via /diagnose-errors cluster-absorb post 41c3411 runner fix; 3-arm behavioural falsifier, same script as 614); V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611c PASS 2026-05-29T18:45Z (6-arm retune, supersedes V3-EXQ-611b manifest-recovery; C1 stratified_fires=true all OPT2/BOTH arms; C3 selected-class diversity=true all 6 arms; C4 monotone in scale=true; R2c_readiness=true all arms; C2 entropy_bonus_scale_commensurate=false but interpretation grid routes PASS_with_C1_and_C3 directly to behavioural successor); V3-EXQ-614 LOST to manifest-pipeline silent-drop cluster 2026-05-29T19:13:19Z (coordinator status=completed + zero results-table row, same signature as V3-EXQ-490h / V3-EXQ-592b autopsied 2026-05-30T06:02Z; runner-side fix ree-v3 commit 41c3411 already landed)
- **Why now:** V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_large_gap; substrate landed 2026-05-27 via /implement-substrate. V3-EXQ-611 substrate-readiness FAILed 2026-05-27T13:02Z on both validation channels: 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-009
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-614d (terminal 2026-06-03: PASS C1/C3, FAIL C2; diagnostic/scoring-excluded; supersedes 614c; reviewed 2026-06-03 -- within-class temperature lever ACTIVE but ZERO committed-action authority; see governance_2026_06_03); V3-EXQ-614c (queued 2026-06-01 via /implement-substrate amend session; 4-arm within-class temperature sweep stratified_within_class_temperature in {None=legacy, 0.5, 1.0, 2.0} on SD-056-amended baseline; cross-plan beneficiary arc_062_rule_apprehension:GAP-B); V3-EXQ-614b FAIL_no_criterion 2026-05-31 (C1=False structural degeneracy + C2=0.087 below threshold + C3=True ALL_ON 0.800 nats; per-claim non_contributory on MECH-341 + ARC-065 via /governance; routed to amend per failure_autopsy_V3-EXQ-616 Sections 7 + 10 contingent path); V3-EXQ-614b (queued 2026-05-31T12:32Z via /queue-experiment; 3-arm behavioural re-run on SD-056-amended substrate, supersedes V3-EXQ-614a; 5 SD-056 amend lever flags applied uniformly across all 3 arms: e2_action_contrastive_multistep_enabled=True h=5, e2_rollout_output_norm_clamp_enabled=True ratio=2.0, e2_action_contrastive_enabled=True weight=0.01; same env_kwargs + acceptance criteria as 614a; 4-row interpretation grid copied verbatim + header note that under amended substrate PASS via C1 is now the load-bearing target since 614a established PASS via C2+C3); V3-EXQ-614a (queued 2026-05-30 via /diagnose-errors cluster-absorb post 41c3411 runner fix; 3-arm behavioural falsifier, same script as 614); V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611c PASS 2026-05-29T18:45Z (6-arm retune, supersedes V3-EXQ-611b manifest-recovery; C1 stratified_fires=true all OPT2/BOTH arms; C3 selected-class diversity=true all 6 arms; C4 monotone in scale=true; R2c_readiness=true all arms; C2 entropy_bonus_scale_commensurate=false but interpretation grid routes PASS_with_C1_and_C3 directly to behavioural successor); V3-EXQ-614 LOST to manifest-pipeline silent-drop cluster 2026-05-29T19:13:19Z (coordinator status=completed + zero results-table row, same signature as V3-EXQ-490h / V3-EXQ-592b autopsied 2026-05-30T06:02Z; runner-side fix ree-v3 commit 41c3411 already landed)
Claims: MECH-341, ARC-062, ARC-065
Why now: V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_large_gap; substrate landed 2026-05-27 via /implement-substrate. V3-EXQ-611 substrate-readiness FAILed 2026-05-27T13:02Z on both validation channels: 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-025 -- Queue depth low (0 pending)

- **Lane:** ops | **Skill:** `(manual)` | **Status:** ready | **Priority:** 35
- **Why now:** Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-025
Title: Queue depth low (0 pending)
Lane: ops | Skill: (manual)
Status: ready
Why now: Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-015 -- Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 38
- **Gap(s):** goal_pipeline:GAP-7
- **Blocked by:** goal_pipeline:GAP-2 [blocked_pending_substrate]
- **Why now:** L1 sub-deliverable LANDED at the harness level (2026-06-03, see l1_2026_06_03 below): the 626-class Class-1 wiring defect is closed and a forced-seed positive control the harness can SEE is established (F0 unit contract 6/6 + V3-EXQ-626b qu

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-015
Title: Object-bound incentive-salience layer (L2-L3) + L1 harness positive control + L7 consumer-readout wiring audit
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): goal_pipeline:GAP-7
Claims: MECH-229, MECH-230, MECH-117, ARC-030
Blocked by: goal_pipeline:GAP-2 [blocked_pending_substrate]
Why now: L1 sub-deliverable LANDED at the harness level (2026-06-03, see l1_2026_06_03 below): the 626-class Class-1 wiring defect is closed and a forced-seed positive control the harness can SEE is established (F0 unit contract 6/6 + V3-EXQ-626b qu

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-011 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-460b..468b (Phase 4/5 *b cohort; MECH-342 ecological = V3-EXQ-629)
- **Why now:** MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes (2026-05-28 within-tick score_margin axis + 2026-05-29 across-tick CommitReadiness EMA / nav_competence axis; 523/523 contracts PASS masters OFF). V3-EXQ-592d (4

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-011
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

### IGW-20260604-013 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514l
- **Why now:** RESUME once the scaffolded_sd054_onboarding substrate-readiness gates pass (substrate_queue.ready=true: Stage-0 z_goal>0.4 AND P1 survival AND P2 benefit-contact AND P2 z_goal>0.4, each >=2/3 seeds), then re-issue the SD-049 Phase 2 behavio

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-013
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

### IGW-20260604-014 -- MECH-295 drive->liking->approach cascade Tier-1 retest cohort

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-4
- **Owner EXQ:** V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; evidence_direction_per_claim[MECH-295]=weakens; supersedes 490i; reviewed -- pending_review clear); lineage: V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i ran 2026-05-30 (superseded by 490j)
- **Why now:** Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 behavioural-necessity falsified, modulatory reading substrate-supported. NEXT is a governance decision (re-scope MECH-295 to modulatory + close GAP-4, O

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-014
Title: MECH-295 drive->liking->approach cascade Tier-1 retest cohort
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): goal_pipeline:GAP-4
Owner EXQ: V3-EXQ-490j TERMINAL 2026-05-31 (severed-bridge baseline; evidence_direction_per_claim[MECH-295]=weakens; supersedes 490i; reviewed -- pending_review clear); lineage: V3-EXQ-490g (FAIL 2026-05-29 cohort autopsy), V3-EXQ-490h FAIL silent-drop 2026-05-30 (runner bug 41c3411), V3-EXQ-490i ran 2026-05-30 (superseded by 490j)
Claims: MECH-295, ARC-030, MECH-117, Q-040
Why now: Tier-1 cohort TERMINAL (V3-EXQ-490j landed 2026-05-31, see last_updated_note): MECH-295 behavioural-necessity falsified, modulatory reading substrate-supported. NEXT is a governance decision (re-scope MECH-295 to modulatory + close GAP-4, O

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-022 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** Gate corrected 2026-05-30: prior gate 'V3-EXQ-543l contributory PASS' is dead. failure_autopsy_V3-EXQ-543l_2026-05-27 (confirmed) routed 543l to substrate_ceiling (FAIL branch-e at escalated floor=0.5 / aux=0.3, basin_stable=true, all four 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-022
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

### IGW-20260604-040 -- Proposal EXP-0076 (MECH-229)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-040
Title: Proposal EXP-0076 (MECH-229)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-229
Why now: active_conflict

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-041 -- Proposal EXP-0083 (ARC-049)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-041
Title: Proposal EXP-0083 (ARC-049)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: ARC-049
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-042 -- Proposal EXP-0084 (INV-059)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-042
Title: Proposal EXP-0084 (INV-059)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-059
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-043 -- Proposal EXP-0086 (Q-035)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-043
Title: Proposal EXP-0086 (Q-035)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: Q-035
Why now: lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-044 -- Proposal EXP-0087 (ARC-063)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-044
Title: Proposal EXP-0087 (ARC-063)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: ARC-063
Why now: insufficient_experimental_replication; lit_only_above_cap; low_exp_conf; missing_experimental_evidence; synthetic_signals_only

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-019 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-019
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

### IGW-20260604-020 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 me

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-020
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

### IGW-20260604-004 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3-EXQ-605 FAIL NC 2026-05-21; V3-EXQ-603a queued 2026-05-24 (call-path fix); V3-EXQ-544a queued 2026-05-29; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
- **Blocked by:** arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
- **Why now:** <!-- TODO: revise resume_condition to reflect V3-EXQ-544a state --> V3-EXQ-604/605 manifests landed FAIL non_contributory (identical arm entropies under SP-CEM+reef). V3-EXQ-603 pruned without run (was re-queued 2026-05-21T13:36Z but draine

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-004
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Owner EXQ: V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3-EXQ-605 FAIL NC 2026-05-21; V3-EXQ-603a queued 2026-05-24 (call-path fix); V3-EXQ-544a queued 2026-05-29; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
Why now: <!-- TODO: revise resume_condition to reflect V3-EXQ-544a state --> V3-EXQ-604/605 manifests landed FAIL non_contributory (identical arm entropies under SP-CEM+reef). V3-EXQ-603 pruned without run (was re-queued 2026-05-21T13:36Z but draine

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-005 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
- **Why now:** BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-005
Title: ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): arc_062_rule_apprehension:GAP-I
Owner EXQ: V3-EXQ-606b
Claims: ARC-064, MECH-316, MECH-317, MECH-318
Blocked by: arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
Why now: BLOCKED ON arc_062_rule_apprehension:GAP-B (status blocked_pending_substrate -- rule-creator/discriminator substrate that populates DIFFERENTIATED rule_state into SD-033a; scaffolded_sd054_onboarding is the candidate vehicle). The MECH-318 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-007 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier queued 2026-06-02

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 queued 2026-06-02 (experiment_purpose=evidence; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
- **Why now:** Plan gap in_progress on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-007
Title: MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-628 evidence falsifier queued 2026-06-02
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-K
Owner EXQ: V3-EXQ-546 (done, diagnostic/non_contributory); V3-EXQ-628 queued 2026-06-02 (experiment_purpose=evidence; replay/caller_sim=True admit_writes block-vs-admit rule_state divergence falsifier)
Claims: MECH-319
Blocked by: arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [blocked_pending_substrate]
Why now: Plan gap in_progress on arc_062_rule_apprehension.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-008 -- Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-A
- **Owner EXQ:** V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; FP-2 falsifier blocked on E2-world-forward per-candidate signal collapse; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
- **Why now:** <!-- TODO: revise resume_condition to reflect V3-EXQ-544a + V3-EXQ-569c state --> V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-008
Title: Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): behavioral_diversity_isolation:GAP-A
Owner EXQ: V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; FP-2 falsifier blocked on E2-world-forward per-candidate signal collapse; V3-EXQ-544a completed_supports 2026-05-30; V3-EXQ-569c claimed 2026-05-30
Claims: ARC-065
Why now: <!-- TODO: revise resume_condition to reflect V3-EXQ-544a + V3-EXQ-569c state --> V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path).

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-010 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-544/545 substrate PASS 5/5 (2026-05-10); V3-EXQ-603a/603b/603c all FAIL non_contributory (603c 2026-05-27T11:38Z, 8/12 cells aborted on P1 survival gate); cluster-absorbed into failure_autopsy_V3-EXQ-591_2026-05-27
- **Why now:** Cluster-absorbed (591 autopsy section 6: fourth member of the substrate-uniform z_goal-zero family alongside 591 / 540 / 590a). Per gov-correction-20260527T175054Z the cluster routes epistemic_category=substrate_ceiling V3 (substrate-enrich

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-010
Title: Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): behavioral_diversity_isolation:GAP-C
Owner EXQ: V3-EXQ-544/545 substrate PASS 5/5 (2026-05-10); V3-EXQ-603a/603b/603c all FAIL non_contributory (603c 2026-05-27T11:38Z, 8/12 cells aborted on P1 survival gate); cluster-absorbed into failure_autopsy_V3-EXQ-591_2026-05-27
Claims: MECH-313, MECH-260, Q-045
Why now: Cluster-absorbed (591 autopsy section 6: fourth member of the substrate-uniform z_goal-zero family alongside 591 / 540 / 590a). Per gov-correction-20260527T175054Z the cluster routes epistemic_category=substrate_ceiling V3 (substrate-enrich

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-012 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485b
- **Why now:** Plan gap in_progress on commitment_closure.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-012
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485b
Claims: SD-033b, MECH-263
Why now: Plan gap in_progress on commitment_closure.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-016 -- EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-11
- **Owner EXQ:** V3-EXQ-588b
- **Why now:** V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non_contributory for MECH-189 -- infant GoalState gate, not ContextMemory writes; env patches work (C2/C3). Do NOT re-queue 588. Follow-up V3-EXQ-588b go

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-016
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

### IGW-20260604-017 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** V3-EXQ-590 ran 20260525T084057Z procedural PASS but evidence_direction=pending_retest_after_substrate with MECH-314 + MECH-111 per-claim non_contributory: Goldilocks calibration is degenerate across novelty_bonus_weight 0.1..1.0 (all 5 arms

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-017
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

### IGW-20260604-018 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-018
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

### IGW-20260604-006 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-006
Title: MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)
Lane: plan | Skill: (plan reconcile)
Status: blocked
Gap(s): arc_062_rule_apprehension:GAP-J
Claims: MECH-312, MECH-312a, MECH-312b, MECH-312c, MECH-312d
Blocked by: arc_062_rule_apprehension:GAP-B [blocked_pending_substrate]
Why now: Plan gap blocked on arc_062_rule_apprehension.

Instructions:
- Update plan-of-record doc and closure frontmatter when complete.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260604-021 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260604-021
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
