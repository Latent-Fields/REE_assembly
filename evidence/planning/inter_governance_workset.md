# Inter-Governance Workset

Generated: `2026-05-29T06:46:33Z`
Schema: `inter_governance_workset/v1.1`

Regenerate: `/inter-governance-brief` or `python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.

UI: http://localhost:8000/workset

## Summary

- Items: **52** (ready 25, in_flight 1, blocked 11)
- Pending review: **6**
- Queue pending (unclaimed): **3**

- Live EXQs: V3-EXQ-592b

## Work packages

### IGW-20260529-001 -- Complete governance review (6 pending)

- **Lane:** governance | **Skill:** `/governance` | **Status:** ready | **Priority:** 1
- **Why now:** pending_review.md lists 6 item(s) -- must clear before new work packages.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-001
Title: Complete governance review (6 pending)
Lane: governance | Skill: /governance
Status: ready
Why now: pending_review.md lists 6 item(s) -- must clear before new work packages.

Instructions:
- Run /governance from REE_assembly; walk pending_review with user.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-037 -- Implement substrate: ARC-046 (unblocks ARC-046)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 20
- **Why now:** substrate_queue entry status=pending_implementation; unblocks retest of ARC-046 (pending_retest_after_substrate).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-037
Title: Implement substrate: ARC-046 (unblocks ARC-046)
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: ARC-046, DEV-NEED-008
Why now: substrate_queue entry status=pending_implementation; unblocks retest of ARC-046 (pending_retest_after_substrate).

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-039 -- Implement substrate: SD-054 (unblocks ARC-062)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 20
- **Why now:** substrate_queue entry status=candidate_v3_pending; unblocks retest of ARC-062 (pending_retest_after_substrate).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-039
Title: Implement substrate: SD-054 (unblocks ARC-062)
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: SD-054, MECH-309, ARC-062
Why now: substrate_queue entry status=candidate_v3_pending; unblocks retest of ARC-062 (pending_retest_after_substrate).

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-044 -- Implement substrate: ARC-065 (unblocks MECH-313)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 20
- **Why now:** substrate_queue entry status=phase_1_implemented; unblocks retest of MECH-313 (pending_retest_after_substrate).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-044
Title: Implement substrate: ARC-065 (unblocks MECH-313)
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: ARC-065, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c
Why now: substrate_queue entry status=phase_1_implemented; unblocks retest of MECH-313 (pending_retest_after_substrate).

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-045 -- Implement substrate: MECH-313 (unblocks MECH-313)

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 20
- **Why now:** substrate_queue entry status=candidate_substrate_landed; unblocks retest of MECH-313 (pending_retest_after_substrate).

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-045
Title: Implement substrate: MECH-313 (unblocks MECH-313)
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: MECH-313
Why now: substrate_queue entry status=candidate_substrate_landed; unblocks retest of MECH-313 (pending_retest_after_substrate).

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-025 -- Substrate ready: MECH-341

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 25
- **Why now:** See ree-v3/ree_core/predictors/e3_score_diversity.py + REEConfig.e3_diversity_entropy_bias_scale + REEConfig.e3_diversity_min_classes_for_stratification. The retune is parameter-only; module surface a

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-025
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

### IGW-20260529-026 -- Substrate ready: MECH-090

- **Lane:** substrate | **Skill:** `/implement-substrate` | **Status:** ready | **Priority:** 25
- **Why now:** Substrate LANDED 2026-05-28 (ree-v3 main). Code: ree-v3/ree_core/heartbeat/beta_gate.py (BetaGate.should_admit_elevation predicate + __init__ kwargs use_commit_readiness_gate / commit_readiness_floor 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-026
Title: Substrate ready: MECH-090
Lane: substrate | Skill: /implement-substrate
Status: ready
Claims: MECH-090, SD-034, MECH-266, MECH-267, MECH-268
Why now: Substrate LANDED 2026-05-28 (ree-v3 main). Code: ree-v3/ree_core/heartbeat/beta_gate.py (BetaGate.should_admit_elevation predicate + __init__ kwargs use_commit_readiness_gate / commit_readiness_floor 

Instructions:
- Use /implement-substrate for the SD/MECH named in title.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-036 -- Retest after substrate: ARC-046

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-046 [pending_implementation]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4)
- **Why now:** Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-036
Title: Retest after substrate: ARC-046
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: ARC-046
Blocked by: ARC-046 [pending_implementation]; free-text (via ARC-046): goal-pipeline / training-regime substrate enrichment within V3 (V3-EXQ-603c FAIL 2026-05-27; needs V3-scoped substrate fix, not V4)
Why now: Blocked by 2 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-038 -- Retest after substrate: ARC-062

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-054 [candidate_v3_pending]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-038
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

### IGW-20260529-040 -- Retest after substrate: INV-074

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-040
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

### IGW-20260529-041 -- Retest after substrate: MECH-260

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-041
Title: Retest after substrate: MECH-260
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-260
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-042 -- Retest after substrate: MECH-309

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** SD-054 [candidate_v3_pending]
- **Why now:** Blocked by 1 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-042
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

### IGW-20260529-043 -- Retest after substrate: MECH-313

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 28
- **Blocked by:** ARC-065 [phase_1_implemented]; Q-043 [no-substrate-entry] (transitive via ARC-065): Q-043 weight calibration; Q-044 [no-substrate-entry] (transitive via ARC-065): Q-044 three-arm ablation; Q-045 [no-substrate-entry] (transitive via ARC-065): Q-045 4-arm ablation; MECH-313 [candidate_substrate_landed]; Q-045 [no-substrate-entry] (transitive via MECH-313): Q-045 4-arm ablation
- **Why now:** Blocked by 6 unresolved substrate prerequisite(s) -- see blocked_by.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-043
Title: Retest after substrate: MECH-313
Lane: experiment | Skill: /queue-experiment
Status: blocked
Claims: MECH-313
Blocked by: ARC-065 [phase_1_implemented]; Q-043 [no-substrate-entry] (transitive via ARC-065): Q-043 weight calibration; Q-044 [no-substrate-entry] (transitive via ARC-065): Q-044 three-arm ablation; Q-045 [no-substrate-entry] (transitive via ARC-065): Q-045 4-arm ablation; MECH-313 [candidate_substrate_landed]; Q-045 [no-substrate-entry] (transitive via MECH-313): Q-045 4-arm ablation
Why now: Blocked by 6 unresolved substrate prerequisite(s) -- see blocked_by.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-046 -- Retest after substrate: MECH-334

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-046
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

### IGW-20260529-047 -- Retest after substrate: Q-045

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 28
- **Why now:** claims.yaml pending_retest_after_substrate=true.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-047
Title: Retest after substrate: Q-045
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: Q-045
Why now: claims.yaml pending_retest_after_substrate=true.

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-002 -- MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** arc_062_rule_apprehension:GAP-B
- **Owner EXQ:** V3-EXQ-543l
- **Why now:** 2026-05-27 GOVERNANCE UPDATE: V3-EXQ-543l ran 20260526T023059Z FAIL branch-e at escalated floor=0.5 / aux=0.3 with basin_stable=true; all four diff-ON gated arms 3/3 inert. failure_autopsy_V3-EXQ-543l_2026-05-27 (status: confirmed) applied:

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-002
Title: MECH-309/ARC-062 post-543k retest: escalated mode_separation_floor 0.5 + P1 deviation aux 0.3 (V3-EXQ-543l)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
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

### IGW-20260529-009 -- Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** behavioral_diversity_isolation:GAP-B
- **Owner EXQ:** V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611b retune validation queued 2026-05-28T17:25Z (claimed DLAPTOP-4.local @17:26:40Z, 6-arm factorial); B_only / ablate_B / ALL_ON behavioural falsifier TBD
- **Why now:** V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_large_gap; substrate landed 2026-05-27 via /implement-substrate. V3-EXQ-611 substrate-readiness FAILed 2026-05-27T13:02Z on both validation channels: 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-009
Title: Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): behavioral_diversity_isolation:GAP-B
Owner EXQ: V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611b retune validation queued 2026-05-28T17:25Z (claimed DLAPTOP-4.local @17:26:40Z, 6-arm factorial); B_only / ablate_B / ALL_ON behavioural falsifier TBD
Claims: MECH-341, ARC-062, ARC-065
Why now: V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_large_gap; substrate landed 2026-05-27 via /implement-substrate. V3-EXQ-611 substrate-readiness FAILed 2026-05-27T13:02Z on both validation channels: 

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-012 -- SD-033a bias head untrained (Go-side mechanically silent)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 30
- **Gap(s):** commitment_closure:GAP-1
- **Owner EXQ:** V3-EXQ-598b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** GAP-1 closes on V3-EXQ-598b PASS (2-arm ablation). Per failure_autopsy_V3-EXQ-543l_2026-05-27 sections 7+9, V3-EXQ-598b is the DISCRIMINATOR between substrate-enrichment (predicted PASS -- GAP-C/D routing consumer rescues differentiation) a

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-012
Title: SD-033a bias head untrained (Go-side mechanically silent)
Lane: experiment | Skill: /queue-experiment
Status: in_progress
Gap(s): commitment_closure:GAP-1
Owner EXQ: V3-EXQ-598b
Claims: SD-033a, MECH-262, SD-034
Blocked by: arc_062_rule_apprehension:GAP-B [in_progress]
Why now: GAP-1 closes on V3-EXQ-598b PASS (2-arm ablation). Per failure_autopsy_V3-EXQ-543l_2026-05-27 sections 7+9, V3-EXQ-598b is the DISCRIMINATOR between substrate-enrichment (predicted PASS -- GAP-C/D routing consumer rescues differentiation) a

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-027 -- Diagnose ERROR: V3-EXQ-455a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-455a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-027
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

### IGW-20260529-028 -- Diagnose ERROR: V3-EXQ-544

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-544
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-028
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

### IGW-20260529-029 -- Diagnose ERROR: V3-EXQ-610

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-610
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-029
Title: Diagnose ERROR: V3-EXQ-610
Lane: experiment | Skill: /diagnose-errors
Status: ready
Owner EXQ: V3-EXQ-610
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-030 -- Diagnose ERROR: V3-ONBOARD-smoke-EWIN-PC

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-030
Title: Diagnose ERROR: V3-ONBOARD-smoke-EWIN-PC
Lane: experiment | Skill: /diagnose-errors
Status: ready
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-031 -- Diagnose ERROR: V3-ONBOARD-smoke-ree-cloud-1

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-031
Title: Diagnose ERROR: V3-ONBOARD-smoke-ree-cloud-1
Lane: experiment | Skill: /diagnose-errors
Status: ready
Why now: Runner ERROR with no queued successor ().

Instructions:
- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-032 -- Diagnose ERROR: V3-EXQ-495

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-495
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-032
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

### IGW-20260529-033 -- Diagnose ERROR: V3-EXQ-538

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-538
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-033
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

### IGW-20260529-034 -- Diagnose ERROR: V3-EXQ-244a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-244a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-034
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

### IGW-20260529-035 -- Diagnose ERROR: V3-EXQ-606a

- **Lane:** experiment | **Skill:** `/diagnose-errors` | **Status:** ready | **Priority:** 30
- **Owner EXQ:** V3-EXQ-606a
- **Why now:** Runner ERROR with no queued successor ().

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-035
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

### IGW-20260529-003 -- E3 optimiser does not include lateral_pfc_analog.rule_bias_head.parameters() (SD-033a bias head untrained)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** arc_062_rule_apprehension:GAP-D
- **Owner EXQ:** V3-EXQ-598
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap in_progress on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-003
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

### IGW-20260529-016 -- MECH-295 drive->liking->approach cascade Tier-1 retest cohort

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 40
- **Gap(s):** goal_pipeline:GAP-4
- **Owner EXQ:** V3-EXQ-490g
- **Why now:** GAP-3 done (MECH-306 + V3-EXQ-582a PASS). ARC-065 SP-CEM default landed 2026-05-17 (V3-EXQ-567). Tier-1 StepHarness retest cohort (V3-EXQ-490g / 471a / 475a / 524a) active; V3-EXQ-483c ran 2026-05-23 FAIL non_contributory (measurement gap: 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-016
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

### IGW-20260529-024 -- SD-017 retest cohort (V3-EXQ-265a PASS 2026-05-09; V3-EXQ-418l + 436a reclassified non_contributory 2026-05-10 pending A

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** upstream_blocked | **Priority:** 40
- **Gap(s):** sleep_substrate:GAP-2
- **Owner EXQ:** V3-EXQ-265a
- **Why now:** V3-EXQ-543l (queued 2026-05-24; escalated MODE_SEPARATION_FLOOR 0.5 + P1_W_DEVIATION_AUX_WEIGHT 0.3; supersedes 543k which FAIL/mixed 20260522T091714Z) is the active ARC-065 substrate gate. On 543l contributory PASS, re-queue 418m + 436b un

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-024
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

### IGW-20260529-048 -- Proposal EXP-0009 (MECH-334)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert; low_exp_conf; mandatory_decision_checkpoint

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-048
Title: Proposal EXP-0009 (MECH-334)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-334
Why now: active_conflict; directional_conflict_alert; low_exp_conf; mandatory_decision_checkpoint

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-049 -- Proposal EXP-0027 (SD-049)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-049
Title: Proposal EXP-0027 (SD-049)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: SD-049
Why now: active_conflict; directional_conflict_alert

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-050 -- Proposal EXP-0028 (MECH-302)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-050
Title: Proposal EXP-0028 (MECH-302)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-302
Why now: active_conflict; directional_conflict_alert

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-051 -- Proposal EXP-0029 (INV-074)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** active_conflict; directional_conflict_alert; low_exp_conf

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-051
Title: Proposal EXP-0029 (INV-074)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: INV-074
Why now: active_conflict; directional_conflict_alert; low_exp_conf

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-052 -- Proposal EXP-0036 (MECH-295)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** ready | **Priority:** 40
- **Why now:** directional_conflict_alert

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-052
Title: Proposal EXP-0036 (MECH-295)
Lane: experiment | Skill: /queue-experiment
Status: ready
Claims: MECH-295
Why now: directional_conflict_alert

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-013 -- OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction

- **Lane:** experiment | **Skill:** `(monitor -- do not re-queue)` | **Status:** in_flight | **Priority:** 43
- **Gap(s):** commitment_closure:GAP-4
- **Owner EXQ:** V3-EXQ-592b
- **Why now:** MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes. 2026-05-28 within-tick decisiveness axis (score_margin gate; ree_core/heartbeat/beta_gate.py + agent.py wiring). 2026-05-29 across-tick motor-program readiness 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-013
Title: OCD battery completeness (V3-EXQ-460..468) + MECH-090 commit-entry conjunction
Lane: experiment | Skill: (monitor -- do not re-queue)
Status: in_flight
Gap(s): commitment_closure:GAP-4
Owner EXQ: V3-EXQ-592b
Claims: SD-034, MECH-266, MECH-267, MECH-268, MECH-090
Why now: MECH-090 R-c commit-entry readiness conjunction substrate LANDED in two passes. 2026-05-28 within-tick decisiveness axis (score_margin gate; ree_core/heartbeat/beta_gate.py + agent.py wiring). 2026-05-29 across-tick motor-program readiness 

Instructions:
- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.
- Plan doc: REE_assembly/evidence/planning/commitment_closure_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-015 -- SD-049 Phase 2 hybrid encoder behavioural validation (V3-EXQ-514 successor)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** goal_pipeline:GAP-2
- **Owner EXQ:** V3-EXQ-514g
- **Why now:** Monostrategy root cause has a validated substrate fix (V3-EXQ-567 PASS, supports ARC-065: SP-CEM lifts natural action entropy 0.012->0.497, candidate support 1.007->2.810). V3-EXQ-550 settled that the blocker is NOT z_goal wiring. Retest un

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-015
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

### IGW-20260529-021 -- ARC-033 vs ARC-058 path arbitration (forensic 445h read)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-1
- **Owner EXQ:** V3-EXQ-445h
- **Why now:** Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include 

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-021
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

### IGW-20260529-022 -- SD-029 / MECH-256 retest under full substrate stack

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 48
- **Gap(s):** self_attribution:GAP-2
- **Why now:** Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 me

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-022
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

### IGW-20260529-004 -- ARC-065 diversity-generation cluster: MECH-313 / MECH-314 substrates landed; Q-043 / Q-044 / Q-045 ablation EXQs pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-H
- **Owner EXQ:** V3-EXQ-544 + V3-EXQ-545 (done); V3-EXQ-604 + V3-EXQ-605 FAIL NC 2026-05-21; V3-EXQ-603a queued 2026-05-24 (call-path fix)
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** V3-EXQ-604/605 manifests landed FAIL non_contributory (identical arm entropies under SP-CEM+reef). V3-EXQ-603 pruned without run (was re-queued 2026-05-21T13:36Z but drained). V3-EXQ-603a queued 2026-05-24 (select_action call-path fix + FIF

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-004
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

### IGW-20260529-005 -- ARC-064 bottom-up rule-discovery cluster (MECH-316 / MECH-317 / MECH-318 absorption check done); empirical gate pending

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** partial | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-I
- **Owner EXQ:** V3-EXQ-606b
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** V3-EXQ-606b script committed to ree-v3 (gates_on_exq=V3-EXQ-543k; hard startup gate). V3-EXQ-543k ran 20260522T091714Z FAIL/mixed -- gate NOT cleared. V3-EXQ-606b ran dry_run=True 20260523T223001Z FAIL/weakens (C3 PASS, C1/C2 FAIL; ARM_2 se

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-005
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

### IGW-20260529-007 -- MECH-319 simulation-mode rule-write-gating: substrate landed; V3-EXQ-608 falsifier queued 2026-05-24

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** arc_062_rule_apprehension:GAP-K
- **Owner EXQ:** V3-EXQ-546 (done); V3-EXQ-608 queued 2026-05-24
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]; arc_062_rule_apprehension:GAP-H [partial]; arc_062_rule_apprehension:GAP-I [partial]
- **Why now:** Plan gap in_progress on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-007
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

### IGW-20260529-008 -- Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-A
- **Owner EXQ:** V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; FP-2 falsifier blocked on E2-world-forward per-candidate signal collapse
- **Why now:** V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path). V3-EXQ-569 matched-entropy sweep ran 2026-05-16 and was reclassified non_contribu

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-008
Title: Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)
Lane: experiment | Skill: /queue-experiment
Status: blocked_pending_substrate
Gap(s): behavioral_diversity_isolation:GAP-A
Owner EXQ: V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; FP-2 falsifier blocked on E2-world-forward per-candidate signal collapse
Claims: ARC-065
Why now: V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path). V3-EXQ-569 matched-entropy sweep ran 2026-05-16 and was reclassified non_contribu

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-010 -- Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked_pending_substrate | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-C
- **Owner EXQ:** V3-EXQ-544/545 substrate PASS 5/5 (2026-05-10); V3-EXQ-603a/603b/603c all FAIL non_contributory (603c 2026-05-27T11:38Z, 8/12 cells aborted on P1 survival gate); cluster-absorbed into failure_autopsy_V3-EXQ-591_2026-05-27
- **Why now:** Cluster-absorbed (591 autopsy section 6: fourth member of the substrate-uniform z_goal-zero family alongside 591 / 540 / 590a). Per gov-correction-20260527T175054Z the cluster routes epistemic_category=substrate_ceiling V3 (substrate-enrich

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-010
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

### IGW-20260529-011 -- Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** pending_governance_stamp | **Priority:** 50
- **Gap(s):** behavioral_diversity_isolation:GAP-D
- **Owner EXQ:** V3-EXQ-550 FAIL/supports MECH-269 (2026-05-11T20:18Z); V3-EXQ-601 PASS/supports MECH-269b (2026-05-21T12:02Z); R4.b reading flagged 2026-05-28 pending governance stamp; Q-040b behavioural sufficiency still open
- **Why now:** V3-EXQ-550 z_goal monostrategy falsifier landed 2026-05-11T20:18Z with outcome=FAIL but evidence_direction_per_claim={MECH-269: supports} (the wired-but-untrained goal pipeline did NOT break monostrategy at this probe depth, so the substrat

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-011
Title: Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)
Lane: experiment | Skill: /queue-experiment
Status: pending_governance_stamp
Gap(s): behavioral_diversity_isolation:GAP-D
Owner EXQ: V3-EXQ-550 FAIL/supports MECH-269 (2026-05-11T20:18Z); V3-EXQ-601 PASS/supports MECH-269b (2026-05-21T12:02Z); R4.b reading flagged 2026-05-28 pending governance stamp; Q-040b behavioural sufficiency still open
Claims: MECH-269, MECH-269b, Q-040
Why now: V3-EXQ-550 z_goal monostrategy falsifier landed 2026-05-11T20:18Z with outcome=FAIL but evidence_direction_per_claim={MECH-269: supports} (the wired-but-untrained goal pipeline did NOT break monostrategy at this probe depth, so the substrat

Instructions:
- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.
- Plan doc: REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
- Workset: http://localhost:8000/workset
```

</details>

### IGW-20260529-017 -- EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-11
- **Owner EXQ:** V3-EXQ-588b
- **Why now:** V3-EXQ-588 FAIL reviewed 2026-05-20 (failure_autopsy_V3-EXQ-588_2026-05-19 confirmed): non_contributory for MECH-189 -- infant GoalState gate, not ContextMemory writes; env patches work (C2/C3). Do NOT re-queue 588. Follow-up V3-EXQ-588b go

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-017
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

### IGW-20260529-018 -- EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-12
- **Owner EXQ:** V3-EXQ-589
- **Why now:** Plan gap in_progress on infant_substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-018
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

### IGW-20260529-019 -- EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attra

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** in_progress | **Priority:** 50
- **Gap(s):** infant_substrate:GAP-13
- **Owner EXQ:** V3-EXQ-590
- **Why now:** Plan gap in_progress on infant_substrate.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-019
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

### IGW-20260529-006 -- MECH-312 precision-gating family registered (MECH-312a / MECH-312b / MECH-312c / MECH-312d sub-MECHs)

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** arc_062_rule_apprehension:GAP-J
- **Blocked by:** arc_062_rule_apprehension:GAP-B [in_progress]
- **Why now:** Plan gap blocked on arc_062_rule_apprehension.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-006
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

### IGW-20260529-014 -- SD-033b behavioural validation (devaluation + perceptual discrimination)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 58
- **Gap(s):** commitment_closure:GAP-8
- **Owner EXQ:** V3-EXQ-485b
- **Why now:** Plan gap blocked on commitment_closure.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-014
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

### IGW-20260529-020 -- EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)

- **Lane:** experiment | **Skill:** `/queue-experiment` | **Status:** blocked | **Priority:** 58
- **Gap(s):** infant_substrate:GAP-14
- **Owner EXQ:** V3-EXQ-591
- **Why now:** 2026-05-27 governance: V3-EXQ-591 ran 20260526T184231Z FAIL/does_not_support (substrate-uniform; 1/7 gate criteria across all 3 arms x 5 seeds; only trivial C3 residue_cov saturation). failure_autopsy_V3-EXQ-591_2026-05-27 (status: confirme

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-020
Title: EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)
Lane: experiment | Skill: /queue-experiment
Status: blocked
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

### IGW-20260529-023 -- MECH-257 dual-function 3-arm ablation re-queue

- **Lane:** plan | **Skill:** `(plan reconcile)` | **Status:** blocked | **Priority:** 58
- **Gap(s):** self_attribution:GAP-3
- **Blocked by:** self_attribution:GAP-1 [blocked]; self_attribution:GAP-2 [blocked]
- **Why now:** Plan gap blocked on self_attribution.

<details><summary>Agent brief (copy-paste)</summary>

```
REE inter-governance work item: IGW-20260529-023
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
