# Inter-Governance Workset

Generated: `2026-05-25T20:34:39Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **45** (ready 26, in_flight 2, blocked 6)
- Pending review: **0**
- Queue pending (unclaimed): **3**

- Live EXQs: V3-EXQ-543k, V3-EXQ-543l, V3-EXQ-591

## Work packages

### IGW-20260525-037 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-037
Title: Retest after substrate: ARC-062
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: ARC-062
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-038 -- Retest after substrate: INV-074

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-038
Title: Retest after substrate: INV-074
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-074
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-039 -- Retest after substrate: MECH-309

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-039
Title: Retest after substrate: MECH-309
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-309
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-040 -- Retest after substrate: MECH-334

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-040
Title: Retest after substrate: MECH-334
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-334
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-007 -- SD-033a bias head untrained (Go-side mechanically silent)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** commitment_closure:GAP-1
- **Owner EXQ:** V3-EXQ-598b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** GAP-1 closes on V3-EXQ-598b PASS (2-arm ablation). Scientific interpretation gated on V3-EXQ-543l contributory PASS (arc_062 GAP-B retest); 598b has hard startup gate on 543l so it runs only after GAP-B clears.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-007
Title: SD-033a bias head untrained (Go-side mechanically silent)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-1
Owner EXQ: V3-EXQ-598b
Claims: SD-033a, MECH-262, SD-034
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: GAP-1 closes on V3-EXQ-598b PASS (2-arm ablation). Scientific interpretation gated on V3-EXQ-543l contributory PASS (arc_062 GAP-B retest); 598b has hard startup gate on 543l so it runs only after GAP-B clears.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-020 -- Diagnose ERROR: V3-EXQ-455a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-455a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-020
Title: Diagnose ERROR: V3-EXQ-455a
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-455a
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-021 -- Diagnose ERROR: V3-EXQ-544

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-544
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-021
Title: Diagnose ERROR: V3-EXQ-544
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-544
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-022 -- Diagnose ERROR: V3-ONBOARD-smoke-EWIN-PC

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-022
Title: Diagnose ERROR: V3-ONBOARD-smoke-EWIN-PC
Lane: experiment | Skill: /diagnose-errors
Status: ready
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-023 -- Diagnose ERROR: V3-EXQ-375

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-375
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-023
Title: Diagnose ERROR: V3-EXQ-375
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-375
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-024 -- Diagnose ERROR: V3-ONBOARD-smoke-ree-cloud-1

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-024
Title: Diagnose ERROR: V3-ONBOARD-smoke-ree-cloud-1
Lane: experiment | Skill: /diagnose-errors
Status: ready
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-025 -- Diagnose ERROR: V3-EXQ-250a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-250a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-025
Title: Diagnose ERROR: V3-EXQ-250a
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-250a
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-026 -- Diagnose ERROR: V3-EXQ-495

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-495
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-026
Title: Diagnose ERROR: V3-EXQ-495
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-495
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-027 -- Diagnose ERROR: V3-EXQ-538

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-538
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-027
Title: Diagnose ERROR: V3-EXQ-538
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-538
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-028 -- Diagnose ERROR: V3-EXQ-244a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-244a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-028
Title: Diagnose ERROR: V3-EXQ-244a
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-244a
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-029 -- Diagnose ERROR: V3-EXQ-606a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-606a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-029
Title: Diagnose ERROR: V3-EXQ-606a
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-606a
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-030 -- Diagnose ERROR: V3-EXQ-598

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-598
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-030
Title: Diagnose ERROR: V3-EXQ-598
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-598
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-031 -- Diagnose ERROR: V3-EXQ-321b

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-321b
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-031
Title: Diagnose ERROR: V3-EXQ-321b
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-321b
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-032 -- Diagnose ERROR: V3-EXQ-250

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-250
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-032
Title: Diagnose ERROR: V3-EXQ-250
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-250
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-033 -- Diagnose ERROR: V3-EXQ-247

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-247
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-033
Title: Diagnose ERROR: V3-EXQ-247
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-247
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-034 -- Diagnose ERROR: V3-EXQ-267

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-267
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-034
Title: Diagnose ERROR: V3-EXQ-267
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-267
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-035 -- Diagnose ERROR: V3-EXQ-432

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-432
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-035
Title: Diagnose ERROR: V3-EXQ-432
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-432
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-036 -- Diagnose ERROR: V3-EXQ-498

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-498
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-036
Title: Diagnose ERROR: V3-EXQ-498
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-498
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-001 -- MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 33
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-543l
- **Why now:** V3-EXQ-543k ran 20260522T091714Z FAIL/mixed (mode_separation_score=0.483, below floor=0.5; basin stability criterion not met). Successor V3-EXQ-543l queued 2026-05-24: escalated MODE_SEPARATION_FLOOR 0.25->0.5 and P1_W_DEVIATION_AUX_WEIGHT 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-001
Title: MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): arc_062_rule_apprehension:GAP-B
Owner EXQ: V3-EXQ-543l
Claims: MECH-309, ARC-062
Why now: V3-EXQ-543k ran 20260522T091714Z FAIL/mixed (mode_separation_score=0.483, below floor=0.5; basin stability criterion not met). Successor V3-EXQ-543l queued 2026-05-24: escalated MODE_SEPARATION_FLOOR 0.25->0.5 and P1_W_DEVIATION_AUX_WEIGHT 

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-002 -- E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** arc_062_rule_apprehension:GAP-D
- **Owner EXQ:** V3-EXQ-598
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap in_progress on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-002
Title: E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-D
Owner EXQ: V3-EXQ-598
Claims: SD-033a, MECH-262
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: Plan gap in_progress on arc_062_rule_apprehension.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-008 -- OCD battery completeness (V3-EXQ-460..468)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 40
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-592
- **Why now:** Phase 2 DONE. V3-EXQ-592 re-queued 2026-05-21 (was dequeued without run). Monitor 592 on DLAPTOP-4.local; on PASS /queue-experiment Phase 4/5 *b cohort (460b/461/463b/464b/466b/467b/468b).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-008
Title: OCD battery completeness (V3-EXQ-460..468)
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-592
Claims: SD-034, MECH-266, MECH-267, MECH-268
Why now: Phase 2 DONE. V3-EXQ-592 re-queued 2026-05-21 (was dequeued without run). Monitor 592 on DLAPTOP-4.local; on PASS /queue-experiment Phase 4/5 *b cohort (460b/461/463b/464b/466b/467b/468b).

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-011 -- MECH-295 drive->liking->approach cascade Tier-1 retest cohort

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-4
- **Owner EXQ:** V3-EXQ-490g
- **Why now:** GAP-3 done (MECH-306 + V3-EXQ-582a PASS). ARC-065 SP-CEM default landed 2026-05-17 (V3-EXQ-567). Tier-1 StepHarness retest cohort (V3-EXQ-490g / 471a / 475a / 524a) active; V3-EXQ-483c ran 2026-05-23 FAIL non_contributory (measurement gap: 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-011
Title: MECH-295 drive->liking->approach cascade Tier-1 retest cohort
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): goal_pipeline:GAP-4
Owner EXQ: V3-EXQ-490g
Claims: MECH-295, ARC-030, MECH-117, Q-040
Why now: GAP-3 done (MECH-306 + V3-EXQ-582a PASS). ARC-065 SP-CEM default landed 2026-05-17 (V3-EXQ-567). Tier-1 StepHarness retest cohort (V3-EXQ-490g / 471a / 475a / 524a) active; V3-EXQ-483c ran 2026-05-23 FAIL non_contributory (measurement gap: 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-019 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** V3-EXQ-543l (queued 2026-05-24; escalated MODE_SEPARATION_FLOOR 0.5 + P1_W_DEVIATION_AUX_WEIGHT 0.3; supersedes 543k which FAIL/mixed 20260522T091714Z) is the active ARC-065 substrate gate. On 543l contributory PASS, re-queue 418m + 436b un

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-019
Title: SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A
Lane: experiment | Skill: /queue-experiment
Status: upstream_blocked
Gap(s): sleep_substrate:GAP-2
Owner EXQ: V3-EXQ-265a
Claims: SD-017, ARC-045, MECH-166
Why now: V3-EXQ-543l (queued 2026-05-24; escalated MODE_SEPARATION_FLOOR 0.5 + P1_W_DEVIATION_AUX_WEIGHT 0.3; supersedes 543k which FAIL/mixed 20260522T091714Z) is the active ARC-065 substrate gate. On 543l contributory PASS, re-queue 418m + 436b un

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/sleep_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-041 -- Proposal EXP-0007 (MECH-204)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert; mandatory_decision_checkpoint

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-041
Title: Proposal EXP-0007 (MECH-204)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-204
Why now: active_conflict; directional_conflict_alert; mandatory_decision_checkpoint

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-042 -- Proposal EXP-0010 (MECH-334)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert; low_exp_conf; mandatory_decision_checkpoint

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-042
Title: Proposal EXP-0010 (MECH-334)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-334
Why now: active_conflict; directional_conflict_alert; low_exp_conf; mandatory_decision_checkpoint

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-043 -- Proposal EXP-0029 (SD-049)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-043
Title: Proposal EXP-0029 (SD-049)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-049
Why now: active_conflict; directional_conflict_alert

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-044 -- Proposal EXP-0030 (MECH-302)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-044
Title: Proposal EXP-0030 (MECH-302)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-302
Why now: active_conflict; directional_conflict_alert

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-045 -- Proposal EXP-0032 (INV-074)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert; low_exp_conf

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-045
Title: Proposal EXP-0032 (INV-074)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-074
Why now: active_conflict; directional_conflict_alert; low_exp_conf

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-010 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514g
- **Why now:** Monostrategy root cause has a validated substrate fix (V3-EXQ-567 PASS, supports ARC-065: SP-CEM lifts natural action entropy 0.012->0.497, candidate support 1.007->2.810). V3-EXQ-550 settled that the blocker is NOT z_goal wiring. Retest un

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-010
Title: SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): goal_pipeline:GAP-2
Owner EXQ: V3-EXQ-514g
Claims: SD-049, SD-015, MECH-229, MECH-230, MECH-117, MECH-216, ARC-030, ARC-032, Q-030
Why now: Monostrategy root cause has a validated substrate fix (V3-EXQ-567 PASS, supports ARC-065: SP-CEM lifts natural action entropy 0.012->0.497, candidate support 1.007->2.810). V3-EXQ-550 settled that the blocker is NOT z_goal wiring. Retest un

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/goal_pipeline_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-016 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-016
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

### IGW-20260525-017 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 me

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-017
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

### IGW-20260525-003 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3-EXQ-605 FAIL NC 2026-05-21; V3-EXQ-603a queued 2026-05-24 (call-path fix)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** V3-EXQ-604/605 manifests landed FAIL non_contributory (identical arm entropies under SP-CEM+reef). V3-EXQ-603 pruned without run (was re-queued 2026-05-21T13:36Z but drained). V3-EXQ-603a queued 2026-05-24 (select_action call-path fix + FIF

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-003
Title: ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-H
Owner EXQ: V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3-EXQ-605 FAIL NC 2026-05-21; V3-EXQ-603a queued 2026-05-24 (call-path fix)
Claims: ARC-065, Q-043, Q-044, Q-045
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: V3-EXQ-604/605 manifests landed FAIL non_contributory (identical arm entropies under SP-CEM+reef). V3-EXQ-603 pruned without run (was re-queued 2026-05-21T13:36Z but drained). V3-EXQ-603a queued 2026-05-24 (select_action call-path fix + FIF

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-004 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** V3-EXQ-606b script committed to ree-v3 (gates_on_exq=V3-EXQ-543k; hard startup gate). V3-EXQ-543k ran 20260522T091714Z FAIL/mixed -- gate NOT cleared. V3-EXQ-606b ran dry_run=True 20260523T223001Z FAIL/weakens (C3 PASS, C1/C2 FAIL; ARM_2 se

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-004
Title: ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending
Lane: experiment | Skill: /queue-experiment
Status: partial
Gap(s): arc_062_rule_apprehension:GAP-I
Owner EXQ: V3-EXQ-606b
Claims: ARC-064, MECH-316, MECH-317, MECH-318
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: V3-EXQ-606b script committed to ree-v3 (gates_on_exq=V3-EXQ-543k; hard startup gate). V3-EXQ-543k ran 20260522T091714Z FAIL/mixed -- gate NOT cleared. V3-EXQ-606b ran dry_run=True 20260523T223001Z FAIL/weakens (C3 PASS, C1/C2 FAIL; ARM_2 se

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-006 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-608 falsifier queued 2026-05-24

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done); V3-EXQ-608 queued 2026-05-24
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [partial]
- **Why now:** Plan gap in_progress on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-006
Title: MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-608 falsifier queued 2026-05-24
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): arc_062_rule_apprehension:GAP-K
Owner EXQ: V3-EXQ-546 (done); V3-EXQ-608 queued 2026-05-24
Claims: MECH-319
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [partial]
Why now: Plan gap in_progress on arc_062_rule_apprehension.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-012 -- EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-11
- **Owner EXQ:** V3-EXQ-588b
- **Why now:** V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non_contributory for MECH-189 -- infant GoalState gate, not ContextMemory writes; env patches work (C2/C3). Do NOT re-queue 588. Follow-up V3-EXQ-588b go

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-012
Title: EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison
Lane: experiment | Skill: /queue-experiment
Status: in_progress
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

### IGW-20260525-013 -- EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-12
- **Owner EXQ:** V3-EXQ-589
- **Why now:** Plan gap in_progress on infant_substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-013
Title: EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): infant_substrate:GAP-12
Owner EXQ: V3-EXQ-589
Claims: DEV-NEED-001, DEV-NEED-007, ARC-065
Why now: Plan gap in_progress on infant_substrate.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-014 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** Plan gap in_progress on infant_substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-014
Title: EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): infant_substrate:GAP-13
Owner EXQ: V3-EXQ-590
Claims: DEV-NEED-003, MECH-314
Why now: Plan gap in_progress on infant_substrate.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-015 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 53
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** Plan gap in_progress on infant_substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-015
Title: EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): infant_substrate:GAP-14
Owner EXQ: V3-EXQ-591
Claims: DEV-NEED-008, ARC-046
Why now: Plan gap in_progress on infant_substrate.

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/infant_substrate_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-005 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-005
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

### IGW-20260525-009 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 58
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485b
- **Why now:** Plan gap blocked on commitment_closure.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-009
Title: SD-033b behavioural validation (devaluation + perceptual discrimination)
Lane: experiment | Skill: /queue-experiment
Status: blocked
Gap(s): commitment_closure:GAP-8
Owner EXQ: V3-EXQ-485b
Claims: SD-033b, MECH-263
Why now: Plan gap blocked on commitment_closure.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260525-018 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260525-018
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
