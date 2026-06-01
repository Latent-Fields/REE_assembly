# Failure autopsy -- V3-EXQ-614c (MECH-341 stratified within-class temperature sweep)

- **Date (UTC):** 2026-06-01T16:46:43Z
- **Scope:** single (one FAIL); lineage context with V3-EXQ-614 / 614a / 614b / 611 / 608 (MECH-341 lineage)
- **Status:** confirmed (user verdict at Step 8 gate 2026-06-01: scope=both, routing=non_contributory + supersede + /queue-experiment)
- **Routing:** governance reclassification + /queue-experiment for a corrected successor (614d). No /diagnose-errors loop (no crash; ran to completion).
- **Predecessor autopsies:** failure_autopsy_V3-EXQ-614b_2026-05-31.{md,json}; failure_autopsy_V3-EXQ-616_2026-05-31.{md,json} (Sections 7 + 10 routed this sweep); failure_autopsy_MECH-341-cluster_2026-05-31.{md,json}

## 1. Target and scope

V3-EXQ-614c is the within-class temperature sweep named by failure_autopsy_V3-EXQ-616_2026-05-31 Sections 7 + 10 as Part (a) of the 2026-06-01 MECH-341 amend validation. It runs 4 arms on the SD-056-amended baseline (614b ARM_2 ALL_ON config), varying only the new `e3_diversity_stratified_within_class_temperature` lever:

- ARM_0_LEGACY: within-class temperature = None (legacy argmin)
- ARM_1_T_0_5: 0.5
- ARM_2_T_1_0: 1.0
- ARM_3_T_2_0: 2.0

Single-target scope. claim_ids = [MECH-341] (correctly tagged: ARC-065 was deliberately dropped because only the Layer-B within-class sub-axis is varied; per claim_ids accuracy rule). experiment_purpose = evidence.

Manifest: `evidence/experiments/v3_exq_614c_mech341_stratified_within_class_temperature_sweep_20260601T124509Z_v3.json` (machine DLAPTOP-4.local, 2026-06-01T12:45:09Z, dry_run=false).

## 2. Facts (manifest reconstruction -- facts only)

- outcome: FAIL; evidence_direction (run-level): weakens; evidence_direction_per_claim: {MECH-341: weakens}
- interpretation_label (script grid): `FAIL_C1_regression_against_614b_routes_to_amend_autopsy` (the (c1=False) cell)
- p0_episodes=30, p1_episodes=60, steps_per_episode=200, seeds=[42,43,44], 12/12 cells completed (no crashes, no non-finite actions)

Acceptance criteria as recorded:
- **C1** (legacy regression band, ARM_0 per-seed entropy in [0.720, 0.880], >=2/3 seeds): **False**; `C1_legacy_seeds_in_band` = 0; `C1_legacy_per_seed_entropies` = [1.176725, 0.529833, 0.693086]
- **C2** (within-class lift, any of ARM_1/2/3 mean entropy >= 0.800 on >=2/3 seeds): **False**; per-arm lift seed counts {ARM_1: 1, ARM_2: 1, ARM_3: 1}
- **C3** (substrate-readiness, all arms frac_pre_ge2 > 0.3 on >=2/3 seeds): **True**; all 4 arms 3/3 seeds

**The smoking-gun fact:** ARM_1_T_0_5, ARM_2_T_1_0, and ARM_3_T_2_0 are **bit-identical to each other, per seed**:

| Seed | ARM_0 (None) selected_entropy | ARM_1 (0.5) | ARM_2 (1.0) | ARM_3 (2.0) | ARM_1/2/3 n_p1_ticks |
|---|---|---|---|---|---|
| 42 | 1.176725 | 1.230675 | 1.230675 | 1.230675 | 1480 |
| 43 | 0.529833 | 0.521660 | 0.521660 | 0.521660 | 10225 |
| 44 | 0.693086 | 0.693138 | 0.693138 | 0.693138 | 1195 |

The three temperature settings {0.5, 1.0, 2.0} produced identical class counts, identical n_p0/n_p1 tick counts, and identical entropies in every seed. The three positive temperatures differ from ARM_0 (None) but not from each other.

## 3. Claim-layer map

**MECH-341** -- `ethics_engine_3.scoring_trajectory_class_diversity_preservation`. claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, implementation_phase=v3. The within-class temperature lever is the 2026-06-01 amend's score-layer sub-axis.

claim_ids accuracy: correctly tagged. No inherited / contaminated tags.

**Did the experiment test the claim under conditions where the within-class lever could express itself? NO.** Two independent test-design defects (Section 5) mean neither failing criterion carries information about MECH-341's claim text. The legacy path did not regress; the lever's effect was not measurable by the instrument used.

## 4. Biological-reference triage

Closest analogue: BG / cortico-striatal winner-take-all selection with downstream entropy-regulating modulation (as in the MECH-341 cluster autopsy 2026-05-29). The within-class proportional sampling lever is an algorithmic regulator (Mnih 2016 entropy regulariser family; Rigotti 2013 mixed-selectivity preservation), not a translation of a named biological mechanism.

- is_formal_import: false; divergence: n/a; lit_status: absent (acceptable for an algorithmic regulator)

The FAIL is **not** a biology-divergence finding. It is an instrumentation / test-design defect.

## 5. Root-cause: two test-design defects

### Defect 1 -- C2 is structurally vacuous (the within-class lever is not measurable by this instrument)

The substrate (`ree-v3/ree_core/predictors/e3_score_diversity.py:226-313`, `stratified_select`) consults the within-class temperature only when a first-action class has **>= 2 candidates** (line 269: `if within_temp is None or len(class_idxs) < 2:` -> legacy argmin short-circuit). When it does fire, it draws the within-class representative via `torch.multinomial(softmax(-class_scores / T), 1)` (lines 282-283). The lever therefore affects only **which within-class candidate becomes the committed action** -- a property of the *committed selection path*.

The experiment, however, measures `selected_class_entropy_nats` from its **own** helper `_per_class_score_stats` (script lines 696-697): `sel_idx = scores_t.argmin()` over `agent.e3.last_scores`, i.e. the **score-layer argmin** class. That quantity is upstream of, and independent from, the within-class temperature lever. The lever can influence this metric only indirectly, by changing the committed action and hence the downstream rollout.

Consequences:
- Across {0.5, 1.0, 2.0} the reported metric is **bit-identical** (Section 2 table) -- zero discriminative signal for the C2 "which temperature wins / does proportional sampling add diversity" question.
- The manifest does not record the within-class firing diagnostics that the substrate exposes (`mech341_n_within_class_sampled`, `mech341_last_within_class_sampled`, `mech341_last_within_class_temperature`, available via `E3ScoreDiversity.get_state()`), so we cannot even confirm how often the within-class branch fired or whether multi-candidate classes are common enough for the lever to matter at all. Most plausibly, multi-candidate-per-class events are rare in the SD-054 reef env, so the lever is a near-total no-op on the measured quantity.

C2 cannot do its job: it asks a within-class question of a score-layer (across-class argmin) metric that is temperature-invariant by construction.

### Defect 2 -- C1 regression predicate mis-specified (per-seed band vs cross-seed-mean reference)

C1 checks each ARM_0 seed's entropy against the band [0.720, 0.880] (= 614b ARM_2 ALL_ON **cross-seed mean** 0.800 +/- 10%) and requires >= 2/3 seeds in band (script lines 1033-1042). ARM_0's per-seed entropies are [1.177, 0.530, 0.693]; their **cross-seed mean is 0.7999** -- essentially exactly the 0.800 reference, i.e. **no regression**. But because the per-seed values have high cross-seed variance (one seed locks 5 classes, one 3, one 2), **0 of 3** land inside the +/-10% band, so C1 = False.

This is a category error: comparing high-variance per-seed values against a band derived from a *mean*. Three seeds with this spread can essentially never all fall within +/-10% of their own mean. C1 = False is a predicate-construction artifact, not a real regression of the legacy path.

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | intact | Legacy path did NOT regress (ARM_0 cross-seed mean 0.7999 ~= 0.800 reference). MECH-341's claim text is untested by this run, not falsified. |
| Biological reference | partial | Algorithmic regulator; no biology divergence in play. |
| Prerequisites | present | SD-056 amend + scaffolded substrate landed; substrate fires (C3 frac_pre_ge2=1.0 all arms). |
| Implementation | complete (substrate) / defective (harness) | The substrate lever is implemented and gated correctly; the experiment harness measures the wrong quantity and omits the lever's diagnostics. |
| Environment | adequate-but-coupling | SD-054 reef env likely produces few multi-candidate-per-class pools, starving the within-class branch; not recorded. |
| Measurement | **under-instrumented + mis-specified** (dominant) | C2 metric is temperature-invariant by construction; within-class diagnostics not recorded; C1 predicate compares per-seed values to a cross-seed-mean band. |
| Integration | coupled-and-stable | Full stack ran cleanly, no NaN/Inf, 12/12 cells. |
| Scale | adequate | 4 arms x 3 seeds x 90 ep x 200 steps. |

**Dominant diagnosis layer:** Measurement / test-design. Both failing criteria (C1, C2) are defective; the only sound criterion (C3 substrate-readiness) PASSed. The `weakens MECH-341` reading is an artifact of the instrument, not evidence about the claim.

**Recommended `epistemic_category`:** none / instrumentation defect. This is NOT substrate_ceiling (the substrate fires; the claim is V3-tractable and was already validated in-stack at C3 ALL_ON on this substrate). It is the same class as the V3-EXQ-626 harness-bug FAIL: a test that could not express the mechanism it set out to measure.

## 7. Learning extracted

1. **A temperature sweep over a quantity measured at the score-layer argmin cannot discriminate a within-class (committed-path) lever.** The within-class temperature changes the committed within-class representative, not the across-class argmin class. To detect it, a successor must measure the *committed-action* class distribution (the experiment already collects `committed_classes_p1_counts` -- that is the temperature-sensitive signal, not `selected_classes_p1`) and/or read the E3 within-class diagnostics directly.
2. **Record the lever's own firing diagnostics.** Any within-class temperature experiment MUST surface `mech341_n_within_class_sampled` / `mech341_last_within_class_sampled` per seed. Bit-identical arms across temperatures with no firing-rate field cannot be interpreted; the diagnostic would have caught this at smoke-test.
3. **Regression-guard predicates must compare like-to-like.** A band built from a cross-seed *mean* must be checked against the successor's cross-seed *mean* (or a per-seed-distribution-aware test), not against per-seed membership. The 0.10-fraction band on a high-variance 3-seed metric is structurally unmeetable per-seed.
4. **Multi-candidate-per-class frequency is a precondition for the within-class lever.** If the candidate pool rarely puts >=2 trajectories in one first-action class, the within-class branch never fires and the lever is a no-op regardless of T. A successor should either enlarge the candidate pool or first confirm (via the firing-rate diagnostic) that the branch fires often enough to be testable.
5. **Lineage note:** this is the third 614-lineage run whose headline FAIL is an instrument/test-design artifact rather than evidence against MECH-341 (614a PASS_C2_C3_only; 614b C2 threshold-drift near-miss; 614c vacuous sweep). The pattern reinforces the MECH-341 cluster reading: MECH-341 is a score-layer preserver whose marginal effect is hard to isolate, and the difficulty has repeatedly been in the *measurement*, not the mechanism.

## 8. Repair pathway and routing decision (user-confirmed at Step 8)

User-confirmed 2026-06-01 via AskUserQuestion: scope=both (614c + 610a); 614c routing = **MECH-341 non_contributory + supersede + /queue-experiment for a corrected 614d**.

Repair pathway: **measurement / test-design redesign** -> `/queue-experiment` for V3-EXQ-614d. The corrected design must:
- (C1) compare ARM_0 **cross-seed mean** to the [0.720, 0.880] band (or use a distribution-aware regression test), not per-seed band membership.
- (C2) measure the **committed-action** class distribution (`committed_classes_p1_counts`) and/or the E3 within-class selection diagnostics, since the score-layer `argmin(last_scores)` metric is temperature-invariant by construction. Record `mech341_n_within_class_sampled` per seed and gate interpretability on the within-class branch firing at a minimum rate.
- Optionally enlarge the candidate pool / lower `min_classes_for_stratification` pressure so multi-candidate-per-class events are common enough for the lever to act.

No new substrate_queue entry (substrate fires as designed; the gap is in the experiment harness). No /diagnose-errors (no crash). The supersede + non_contributory disposition removes 614c from indexer scoring so its artifact-driven `weakens` does not weight MECH-341 governance.

## 9. Recommended evidence_quality_note + manifest disposition (governance to write, not this skill)

Manifest disposition: set `evidence_direction = superseded` (superseded_by = the eventual 614d) on the 614c flat manifest once 614d is queued; in the interim, override `evidence_direction_per_claim` to `{MECH-341: non_contributory}` with the note below. Per-claim direction recommended: **MECH-341 = non_contributory**, `pending_retest_after_substrate` = false (this is not a substrate gap; it is `pending_retest_after_corrected_harness` -- gated on V3-EXQ-614d).

Recommended `evidence_quality_note` text for MECH-341:

> "2026-06-01 autopsy (failure_autopsy_V3-EXQ-614c_2026-06-01): V3-EXQ-614c (4-arm within-class temperature sweep {None,0.5,1.0,2.0} on the SD-056-amended baseline) FAILed via the script's C1-regression cell, but both failing criteria are test-design defects, so the run is non_contributory for MECH-341 rather than weakens. (1) C2 vacuous: ARM_1/2/3 (T=0.5/1.0/2.0) are bit-identical per seed because the reported `selected_class_entropy_nats` is measured at the score-layer argmin(last_scores), which is upstream of and independent from the within-class temperature lever (the lever only changes the committed within-class representative inside stratified_select, e3_score_diversity.py:269-284, and only when a class has >=2 candidates). The within-class firing diagnostics (mech341_n_within_class_sampled) were not recorded, so the lever's engagement is unconfirmed. (2) C1 mis-specified: it checks per-seed ARM_0 entropy against [0.720,0.880] (614b cross-seed mean 0.800 +/-10%) needing >=2/3 seeds in band; ARM_0 per-seed entropies [1.177,0.530,0.693] have cross-seed mean 0.7999 (~=0.800, no regression) but 0/3 land in the band due to cross-seed variance. C3 substrate-readiness PASSed 3/3 on all 4 arms (substrate fires). Routed to /queue-experiment for V3-EXQ-614d: measure the committed-action class distribution and the E3 within-class diagnostics (the score-layer argmin metric is temperature-invariant by construction), and fix C1 to compare cross-seed means. pending_retest_after_corrected_harness (gated on V3-EXQ-614d). Same instrumentation-defect class as the V3-EXQ-626 harness-bug FAIL; not substrate_ceiling -- substrate is V3-tractable and already validated in-stack at C3 ALL_ON on this substrate."

## 10. Routing field for /governance

- routing: governance-reclassification + queue-experiment (614d)
- target claims: [MECH-341]
- per-claim evidence_direction overrides: {MECH-341: non_contributory}
- pending_retest_after_substrate: false; pending_retest_after_corrected_harness: true (gated on V3-EXQ-614d)
- narrow_supports_flag: false
- recommended_substrate_queue_entry.action: none (substrate fires as designed; the gap is the experiment harness)
- no /diagnose-errors loop: the FAIL is a test-design/instrumentation defect, not a crash
