# Failure Autopsy -- V3-EXQ-693 (SD-049 Phase-2 4-arm substrate-gradient validation; WL non-vacuity unmet)

- **Generated:** 2026-06-20T15:24:03Z
- **Run:** `v3_exq_693_sd049_phase2_4arm_substrate_gradient_validation_20260620T143430Z_v3`
- **Queue id:** V3-EXQ-693 (queued as the "514l successor"); machine ree-cloud-1
- **Outcome:** FAIL, self-routed `evidence_direction: non_contributory` (SD-049 + SD-015), `readiness_route: substrate_not_ready_requeue`, `route_reason: non_vacuity_unmet`
- **Claims under test:** SD-049 (multi_resource_heterogeneity, candidate / substrate_ceiling / v3_pending) + SD-015 (z_resource_encoder, candidate / substrate_ceiling)
- **Scope:** single (but read against the parallel 514 lineage; see Section 6)
- **Verdict (user-adjudicated 2026-06-20):** **WL non-vacuity is an INSTRUMENTATION / measurement gap, NOT a substrate ceiling and NOT a claim falsification.** The self-route family (`substrate_not_ready_requeue` / `non_contributory` / never a weakens) is CORRECT; the *cause* is a stale WL-scoring harness, not the substrate. Route: **`/queue-experiment` 693a** (port the working 514r/s/t WL-scoring + non-vacuity precondition) **AND amend the SD-049-PHASE-2 substrate_queue entry** with the 693 failure record. SD-015's identity-recovery leg fired non-vacuously (probe 0.71-0.77) -> a narrow evidence_quality_note, NOT a supports entry.

---

## 1. Facts -- which guard failed

The composite acceptance gates on three non-vacuity legs (`non_vacuity_note`): **R1** consumption, **R2** identity-probe-fireable, **R3** WL-channel-fireable. The manifest:

| guard | value |
|---|---|
| R1_consumption | **true** |
| R2_identity_probe_fireable | **true** |
| R3_wl_channel_fireable | **false** <- the SOLE unmet guard |
| non_vacuity_met | false -> `substrate_not_ready_requeue` |

`R3` is the 514n same-statistic gate: it requires the bank to fire a real most-wanted-vs-last-consumed object-bound read. It did not.

**R3 is hard-zero across EVERY arm and seed** (`arm_summary`):

| arm | n_scored_wl_steps_total | run_bank_populated_frac | object_bound_wl_dissoc_fraction | distinct_tokens_max | drive_spread |
|---|---|---|---|---|---|
| ARM_0 (OFF, 1 type) | 0 | 0.0 | 0.0 | 0 (by design) | 0.0 |
| ARM_1 (2type) | 0 | 0.0 | 0.0 | 2 | 0.009 |
| ARM_2 (3type+novelty) | 0 | 0.0 | 0.0 | 3 | ~0.011 |
| ARM_3 (5type) | 0 | 0.0 | 0.0 | 5 | ~0.013 |

**What DID fire (this is not a dead run -- the failure is localized to the WL leg):**

- **Identity probe (R2 / C_ID): PASS.** ARM_1/2/3 `mean_probe_acc_identity` 0.71-0.77, pooled `n_identity_samples` ~3.5k-4.4k. (ARM_0 = 0.0 by design -- single resource type has no identity structure.)
- **Per-axis drive ANOVA (C_ANOVA): PASS.** `per_axis_drive_anova_f_max` up to 1480 vs pre-registered F-crit 4.605.
- **Tokens bind.** `distinct_tokens_max` = 2/3/5 = `n_resource_types` on every seed; `drive_spread_max` 0.009-0.015 (> floor 1e-3). So z_resource is populated, the SD-057 bank accrues per-object tokens, and per-axis drive is differentiated.

So z_resource, drive, consumption, and identity all express; the FAIL is precisely and only the **wanting != liking (object-bound)** scoring leg.

**Failed criterion class:** a non-vacuity precondition (R3), NOT a discrimination criterion -- the discrimination criteria (C_GR margin, C_WL fraction) were never reached because R3 gated them.

---

## 2. Code trace -- why R3 cannot fire in 693's harness

The WL read (`experiments/v3_exq_693_...py:582-596`, inside the per-contact block) scores a step only when, at one contact tick, ALL of: `most_wanted != None` AND `rtype != None` AND `n_distinct >= 2` hold simultaneously, then `run_bank_populated` additionally requires `scored_wl_steps >= MIN_SCORED_STEPS(5)`.

The bank machinery itself is sound (verified in `ree_core/goal.py`):
- `IncentiveTokenBank.update()` co-stores `base_value[k]` AND `z_object[k]` atomically (goal.py:533-534), so every accrued token has a stored embedding.
- `most_wanted()` returns non-None whenever the bank is non-empty with a stored embedding (goal.py:571-582).
- `GoalState.reset()` clears the bank **in place** (goal.py:820-821) -- it does NOT re-create it, so the experiment's once-captured `bank` reference (line 484) stays live across the per-episode `agent.reset()`. (Ruled out the stale-reference hypothesis.)
- `agent.update_z_goal(..., resource_type=rtype)` binds via that live bank (agent.py:7273-7299).

So the bank populates (`distinct_tokens_max` = n_types confirms it) and `most_wanted` is fireable. The leg is hard-zero because **693's per-contact scoring conjunction never co-activates** -- the harness does not reproduce the conditions under which the 514-lineage WL read scores (Section 6). This is a translation/measurement gap: 693 has the *symbol* of the WL read but not the scoring conditions that make it fire.

---

## 3. Claim-layer mapping

- **SD-049** (multi_resource_heterogeneity): 693's WL-dissociation deliverable is the load-bearing test, and it was never reached. **Correctly `non_contributory`** -- the run yields no WL information about SD-049. The substrate (SD-049 Phase-1 env + Phase-2 encoder) is NOT implicated; it is proven working in the 514 lineage on the same machinery.
- **SD-015** (z_resource_encoder): the **identity-recovery probe FIRED and PASSED** (probe acc 0.71-0.77, ~4.4k samples) -- a genuine non-vacuous positive for SD-015's z_resource discriminability deliverable. The blanket `non_contributory` (composite-FAIL) under-credits this leg. **narrow_supports_flag = true** -> governance should record an evidence_quality_note (NOT a supports entry; the composite run FAILed and the WL leg is vacuous).

`claim_ids = [SD-049, SD-015]` are accurate for what the experiment *intends* to test; both are correctly kept non_contributory at the run level.

---

## 4. Biological-reference triage

- **Closest mechanism:** incentive salience as object-bound, drive-modulated wanting that can dissociate from consummatory liking (Berridge; specific PIT, Corbit/Balleine). Grounded; the WL!=liking dissociation is a sound translation.
- **Formal import?** No -- the dissociation is a direct biological reading, already validated structurally (the 514 lineage scores it).
- **Does the failure match a missing dependency?** No. It matches a MEASUREMENT-harness signature: the substrate carries the read (tokens bind, drive differentiates, most_wanted fireable) but 693's scoring instrumentation never co-activates. Brains remain the existence proof for the class -> default reading is a translation/instrumentation gap, NOT falsification.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | WL leg never expressed; SD-015 identity leg DID express (probe 0.71-0.77). |
| Biological reference | clear | Berridge wanting!=liking / specific PIT; FAIL not at biology. |
| Prerequisites / dependency | **present** | tokens bind (distinct=n_types), per-axis drive spread present, identity discriminable. |
| Implementation | **partial -- stale harness** | 693's WL-scoring conjunction is a pre-514n fork; does not reproduce the working 514t scoring conditions. |
| Environment | adequate | contacts present (~50-150 events/run), all resource types contacted. |
| Measurement | **under-instrumented (THE layer)** | R3 non-vacuity guard structurally cannot fire in 693's fork; the whole composite gates on it. |
| Integration | partially coupled | bank <-> z_goal seeding reached; the WL *readout* is the broken coupling. |
| Scale | adequate | 3 seeds x 4 arms; thousands of identity/ANOVA samples. |

**Recommended `epistemic_category`: UNCHANGED (`non_contributory` re-queue family; NOT `substrate_ceiling`).** The self-route landed in the right family; the cause is harness instrumentation.

**Secondary flag (NOT adjudicated -- gated behind R3):** the C_GR discrimination-margin lift ARM_2-ARM_0 = **0.0067** (threshold 0.4; negative -0.0087 in ARM_3). Even where it would fire, z_goal does not discriminate resource identity in the non-saturating margin sense, despite the linear probe reading identity off z_resource at 0.71-0.77. This may be the *real* SD-049 Phase-2 conversion question once WL vacuity is fixed -- carry it into 693a's design as a watch item; do NOT conclude on it here (it was never adjudicated this run).

---

## 6. The load-bearing cross-experiment contrast (why this is a harness gap, not a ceiling)

693 was queued as the **"514l successor"** (`git log`: 6b630eb, "queue V3-EXQ-693: SD-049 Phase-2 4-arm substrate-gradient validation (514l successor)"). It forked from V3-EXQ-514**l** (2026-06-03) -- *before* the 514n -> ... -> 514t bank-population / non-vacuity fixes landed in that lineage.

The contemporaneous 514 lineage (514r/s/t) exercises the **same** SD-049-PHASE-2 + SD-057 `IncentiveTokenBank.most_wanted` object-bound wanting!=liking machinery and populates the WL channel cleanly:

| run | run_bank_populated_frac | n_scored_wl_steps_total |
|---|---|---|
| **V3-EXQ-693** (this) | **0.0** all arms | **0** all arms |
| V3-EXQ-514t (2026-06-20) | **1.0** | **72** |

So the WL channel IS scoreable on the live substrate; 693's WL-scoring harness has drifted from the working version. The method_note's claim that 693 adopts "the 514m vacuity fix, from V3-EXQ-514n" is only partially realized -- the metric read was copied but the bank-POPULATION / scoring conditions that actually make R3 fire (514o+ enrichments) were not ported into this fork. This is the canonical clone-inherits-quirks failure (memory: cloned experiments inherit progress/scoring quirks; source fixes do NOT auto-propagate across separate files).

**Granularity-debt check.** This is the ~8th autopsy circling SD-049 (514l/m/p/q/r/s/t + 693). BUT the lineage already RESOLVED the granularity debt at 514q (the MECH-229 -> MECH-436 drive-coupling split). 693 tests a *different* deliverable (the SD-049/SD-015 4-arm gradient), and its FAIL is a harness gap with the SAME signature, not a new divergent failure mode. **No further `/claim-synthesis` warranted** (consistent with the 514t verdict).

---

## 7. Repair pathway + routing (user-confirmed 2026-06-20)

**PRIMARY -- `/queue-experiment` 693a (measurement re-issue, NEW letter, same scientific question).** Port the working 514r/s/t WL-scoring harness into the 693 fork: the `most_wanted`-vs-last-consumed object-bound read + the non-vacuity precondition + the bank-population conditions that make R3 fire (514t scores 72 WL steps). Keep the 4-arm substrate gradient (OFF / 2-type / 3-type+novelty / 5-type) and the identity + ANOVA legs unchanged. Carry the C_GR near-zero-margin observation as a watch item (Section 5 secondary flag). Pre-registered: the three non-vacuity guards self-route `substrate_not_ready_requeue` if still unmet, NEVER a false weakens.

**SECONDARY -- amend SD-049-PHASE-2 substrate_queue entry** with the 693 failure record (user directive: open the substrate gap). The amend RECORDS that the WL-readout harness in the 693 fork is stale relative to the 514t lineage and routes the next iteration to the harness port; it is NOT a request to build a new substrate lever (the SD-049/SD-057 substrate is proven working by 514t). This makes the IGW workset's `blocked_by` reflect the WL-harness-port retest.

**Draft `evidence_quality_note` for SD-049 (governance writes it):**

> 2026-06-20 (failure_autopsy_V3-EXQ-693, confirmed): V3-EXQ-693 FAIL self-routed substrate_not_ready_requeue / non_vacuity_unmet (R3 WL-channel-fireable=false). non_contributory -- CORRECT, NOT a weakens. Root cause is an INSTRUMENTATION gap, NOT a substrate ceiling: 693 forked from V3-EXQ-514l (pre-514n) and its wanting!=liking scoring harness is hard-zero (n_scored_wl_steps_total=0, run_bank_populated_frac=0.0 across all 4 arms / 3 seeds) while the contemporaneous 514t lineage scores the SAME IncentiveTokenBank.most_wanted object-bound read cleanly (run_bank_populated_frac=1.0, 72 scored WL steps). Tokens DO bind (distinct_tokens_max = n_resource_types 2/3/5), per-axis drive spread present (0.009-0.015), identity probe PASS (0.71-0.77, ~4.4k samples), ANOVA PASS (F up to 1480) -- the FAIL is localized solely to the WL scoring leg. SD-049 stays candidate / substrate_ceiling / v3_pending (UNCHANGED; the run yields no WL information). Route: /queue-experiment 693a porting the working 514r/s/t WL-scoring + non-vacuity precondition; amend SD-049-PHASE-2 substrate_queue with this failure record. WATCH (gated, unadjudicated this run): C_GR discrimination-margin lift ARM_2-ARM_0=0.0067 (threshold 0.4; -0.0087 ARM_3) -- the likely real conversion question once WL vacuity is fixed. NOT a /claim-synthesis trigger (the 514q split already resolved the lineage granularity debt).

**Draft `evidence_quality_note` for SD-015 (governance writes it):**

> 2026-06-20 (failure_autopsy_V3-EXQ-693, confirmed): run-level non_contributory (composite FAIL via R3 WL non-vacuity), but NARROW positive worth recording -- 693's identity-recovery probe fired non-vacuously for SD-015 z_resource discriminability (mean_probe_acc_identity 0.71-0.77 across ARM_1/2/3, pooled ~3.5k-4.4k samples; ARM_0=0 by single-type design). This is a per-leg partial credit, NOT a supports entry (the composite run FAILed and the WL leg is vacuous). SD-015 stays candidate / substrate_ceiling. The identity-recovery leg will re-score in 693a on the harness-fixed run.

---

## 8. Routing decision the user confirmed

- **Verdict:** WL non-vacuity = instrumentation/measurement gap (stale 514l fork), NOT substrate ceiling, NOT falsification. Self-route family correct.
- **SD-049 / SD-015:** candidate / substrate_ceiling / v3_pending -- UNCHANGED; both stay non_contributory + pending_retest_after_substrate.
- **Routing:** `/queue-experiment` 693a (port 514t WL-scoring harness) + amend SD-049-PHASE-2 substrate_queue with the 693 failure record.
- **SD-015:** narrow evidence_quality_note (identity leg PASS), narrow_supports_flag=true; NOT a supports entry.
- **Watch item:** C_GR near-zero discrimination-margin lift, carry into 693a (gated, unadjudicated here).
- **No `/claim-synthesis`** (514q split already resolved the lineage granularity debt).

Analysis + handoff only -- governance applies the disposition to claims.yaml / substrate_queue / review_tracker.
