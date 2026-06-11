# Failure autopsy -- V3-EXQ-660a (MECH-341 within-class-representative-diversity graded confirmation)

- **Date (UTC):** 2026-06-11T06:02:46Z
- **Scope:** single (with a cross-lineage measurement-ceiling pattern note)
- **Status:** confirmed (user-adjudicated at the Step-8 gate 2026-06-11; chose "non-contributory + redesign readout")
- **Routing:** /queue-experiment (measurement/test-design redesign) + governance reclassification of the manifest direction
- **Target:** run_id `v3_exq_660a_mech341_within_class_pool_size_graded_confirmation_20260611T032653Z_v3`, queue_id V3-EXQ-660a, claim_ids [MECH-341]
- **Predecessor lineage:** V3-EXQ-660 (PASS, standing -- NOT superseded by 660a); failure_autopsy_MECH-341-cluster_2026-05-31 (confirmed; established MECH-341 = score-layer preserver, load-bearing in-stack only)

---

## 1. Scope

V3-EXQ-660a is an **evidence** experiment (experiment_purpose=evidence, claim_ids=[MECH-341]), the graded-confirmation successor to V3-EXQ-660. It ran to completion (24/24 cells, 3 seeds x 8 arms), self-routed **FAIL / weakens** with
`interpretation_label = FAIL_lift_not_graded_fixed_structural_artifact_independent_of_pool_size`.
It is the sole pending FAIL flagged by the 2026-06-11 governance walk. Adjudicated here as the diagnosis the manifest's `weakens` self-route was a hypothesis for.

## 2. Facts (no interpretation)

**Design.** 660 found the within-class-representative lever load-bearing (legacy argmin H=4.781 vs sampled 4.862, ~0.08 nats) but its temperature sweep was byte-identical across T=0.5/1.0/2.0 (near-degenerate within-class scores -> softmax ~uniform at every T). 660a holds within-class temperature fixed (None legacy / 1.0 sampled) and sweeps the **CEM pool size K in {16,32,64,128}** (`cfg.hippocampal.num_candidates`) -- the count of available within-class representatives -- across 8 arms (legacy/sampled x 4 K). PRIMARY readout: `within_class_rep_cond_entropy = H(rep_signature | committed_class)`. PRIMARY criterion C_GRADED: per-seed paired lift Delta(K)=sampled-legacy monotone-nondecreasing across K AND Delta(128)-Delta(16) >= 0.05 nats on >= 2/3 seeds.

**Results (from the manifest).**
- **Non-vacuity MET.** Per-tick within-class availability (`mean_distinct_within_class_reps`, sampled) rose monotonically: 4.99 -> 8.81 -> 17.62 -> 33.84 across K (rise 28.85 >> 0.25 floor). Pool size honored (realized 16/32/64/128). The graded axis demonstrably moves the input.
- **C_GRADED FAILED** (n_seeds_graded = 1, need >= 2). Per-seed paired lift Delta(K):
  - seed 42: {16: -0.227, 32: -0.085, 64: -0.044, 128: +0.120}, monotone=True, margin 0.347 -> graded
  - seed 43: {16: +0.007, 32: +0.035, 64: -0.091, 128: +0.064}, monotone=False -> not graded
  - seed 44: {16: -0.160, 32: +0.563, 64: -0.232, 128: +0.159}, monotone=False -> not graded
- **C_ABS FAILED** (supporting, non-gating). Absolute SAMPLED entropy by K: {16: 4.608, 32: 4.862, 64: 4.805, 128: 4.887} -- essentially **flat** at ~4.6-4.9 nats despite availability rising 5->34.

**Failed criterion type:** the PRIMARY criterion that failed is a **discrimination** criterion (graded dose-response). The negative-control/absolute side (non-vacuity, pool-honored) PASSED. "Negative control passes, discrimination fails" -- but here it resolves to a measurement insufficiency, not a substrate ceiling (see Section 5).

## 3. Claim-layer map

**MECH-341** (`ethics_engine_3.scoring_trajectory_class_diversity_preservation`): claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, pending_retest_after_substrate=true, implementation_phase=v3. Layer-B (post-CEM scoring) diversity-PRESERVATION substrate. The confirmed 2026-05-31 cluster autopsy fixed its role: a **score-layer preserver of upstream-supplied candidate-pool diversity, load-bearing in the full stack only; in-isolation testing is structurally unreachable**; promotion is gated on in-stack evidence (614a PASS_C2_C3_only, 569d matched-entropy PASS), not in-isolation R2.c clearance.

660/660a probe a NEWER, FINER sub-axis: that the within-class representative *sampling* (stratified_select's within-class lever) specifically adds *graded* selected diversity as more representatives become available. This sub-claim is distinct from, and downstream of, the in-stack preservation role.

**Did the test let the claim express itself?** No. The graded sub-claim could express itself only through a readout that resolves *per-decision* selected within-class diversity. The chosen readout cannot (Section 5). So 660a is non-contributory on the graded question -- it does not weaken MECH-341.

**claim_ids accuracy:** correct. 660a tests the within-class sub-axis of MECH-341 directly; the tag is appropriate. The measurement defect is in the readout, not the tag.

## 4. Biological-reference triage

Closest reference mechanism: **trial-to-trial motor/action variability within a chosen action category** -- songbird LMAN->RA variability injection (Olveczky/Fee), striatal exploration, Dhawale et al. 2017 motor variability. The mechanism CLASS has a clear biological existence proof. MECH-341 is a diversity-preservation heuristic (Mnih 2016 entropy / Padoa-Schioppa & Conen 2017 categorical preservation), NOT a formal-definition import (Pearl/Shannon/optimal-control), so the SD-003 "load-bearing divergence" trap does not apply and the primary output is NOT a lit-pull. A FAIL therefore defaults to a translation/measurement gap until the biology says the mechanism itself is wrong -- which this experiment cannot show. `is_formal_import=false`, `lit_status=partial` (ARC-065-side anchored; MECH-341 lit-absent, acceptable for an algorithmic regulator).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (NOT weakened) | The graded sub-claim could not express itself under this readout; cannot dissociate "lever ignores the larger pool" from "metric is blind to it". |
| Biological reference | partial | within-class action variability; class has an existence proof; not a formal import -> default reading is measurement gap, not falsification. |
| Prerequisites | present | SP-CEM + MECH-341 stratified-select operative; within_class_branch_active=true; 151-1104 within-class samples/arm; modulatory authority + e2_world_forward summary active. |
| Implementation | complete | lever fires; pool size honored 16->128; availability provably moves 5->34. |
| Environment | adequate | SD-054 bipartite-reef supplies the first-action classes. |
| **Measurement** | **misleading / under-instrumented (DOMINANT)** | `within_class_rep_cond_entropy = H(rep_signature \| committed_class)` is a PHASE-AGGREGATE over every P1 tick (`selected_pairs` appended once per tick at e3_selector readout; entropy computed once at phase end). It (a) SATURATES -- absolute sampled entropy flat ~4.6-4.9 across K while availability rises 5->34 (C_ABS failure is the direct tell); and (b) is CONFOUNDED BY TICK COUNT -- seed 43 (~10k ticks) sits at ~6.3 nats in BOTH arms, seeds 42/44 (~1-2k ticks) at ~3.7-4.6, so the metric tracks accumulated phase coverage, not per-decision diversity. The lift (sampled - legacy) is a difference of two saturating tick-count-confounded aggregates -> noise-dominated, no dose-response possible even in principle. |
| Integration / Scale | adequate | n/a -- 3 seeds x 8 arms, thousands of ticks. |

**Recommended `epistemic_category` (manifest-level note, NOT a change to the claim's category):** `measurement_test_design_defect`. The claim's own epistemic_category is unchanged; MECH-341 stays candidate / v3_pending / pending_retest_after_substrate.

**The same-statistic guard the design missed.** 660a's non-vacuity gate keyed on `mean_distinct_within_class_reps` (the per-tick INPUT availability) -- which rises correctly -- but the C_GRADED criterion keyed on the phase-aggregate ENTROPY readout. The guard verified the lever has more raw material; it did NOT verify the readout can register the lever using it. C_ABS (absolute sampled entropy rises with K) was reported but non-gating; had it gated, the run would have self-routed substrate_not_ready rather than weakens. This is the V3-EXQ-642 "self-route is a hypothesis" pattern at the readout layer.

## 6. Cross-lineage measurement-ceiling pattern (note, not a separate cluster autopsy)

660a is the SECOND consecutive instance in the MECH-341 within-class lineage where the chosen diversity readout cannot register the lever's input axis:

| Run | Swept axis (input, moves) | Readout (output, flat) | Read |
|---|---|---|---|
| 660 | within-class temperature T=0.5/1.0/2.0 | within_class_rep_cond_entropy byte-identical across T | near-degenerate within-class scores -> softmax ~uniform; readout couldn't see T |
| 660a | CEM pool size K=16->128 (availability 5->34) | within_class_rep_cond_entropy flat ~4.6-4.9; C_ABS fails | phase-aggregate readout saturates + tick-count-confounded; couldn't see K |

(616's bit-identical-across-scale FAIL is a DISTINCT root cause -- single-class CEM proposer pool under B_only isolation -- and is NOT folded in here.) The structural property: **MECH-341's within-class contribution keeps being measured with a phase-aggregate conditional-entropy readout that saturates, so the graded sub-question stays unanswerable.** The fix is a per-decision / per-window readout with headroom, not more sweeps on the existing metric.

## 7. Learning extracted

1. **Measurement gap, not falsification.** 660a is non-contributory on MECH-341's within-class GRADED sub-axis: the readout cannot dissociate a flat lever from a blind metric.
2. **The non-vacuity guard was necessary but not sufficient.** It guarded the INPUT (availability) but the OUTPUT readout saturates; C_ABS's failure is direct evidence the output is insensitive to the guarded input.
3. **Narrow-supports flag.** MECH-341's surviving supports are stack-only / single-pathway (614a PASS_C2_C3_only; in-isolation unreachable). The within-class graded sub-axis remains UNESTABLISHED -- 660 suggestive but readout-degenerate, 660a non-contributory. Reclassifying 660a as non_contributory must NOT be read as "MECH-341 conflict resolved": its only positive evidence is the in-stack preserver role.
4. **660 stays standing.** 660a does not supersede 660 (and was designed not to). 660's in-stack within-class load-bearing reading is preserved; only the GRADED dose-response is unmeasured.
5. **Redesign spec (for the /queue-experiment successor).** Replace the phase-aggregate H(rep|class) with a readout that has per-decision resolution and headroom, e.g. (a) windowed H(rep|class) over fixed-length tick windows then averaged (removes the tick-count confound), or (b) a [0,1] selected-vs-available efficiency = distinct-within-class-reps-selected / distinct-within-class-reps-available per matched tick (cannot trivially saturate), then test whether THAT per-decision lift scales with K. Keep the availability non-vacuity gate AND add a readout-sensitivity gate (the new readout must move with K in the sampled arm before C_GRADED is scored). New EXQ number warranted only if the scientific question changes; a same-question readout fix is an alphabetic successor (660b).

## 8. Routing (user-confirmed at Step 8)

User chose "Non-contributory + redesign readout" via AskUserQuestion 2026-06-11.

- **routing:** `queue-experiment` (measurement/test-design redesign; per-decision/windowed within-class diversity readout with headroom + readout-sensitivity gate).
- **recommended_evidence_direction (governance to apply on the manifest):** `non_contributory` (the manifest currently carries `weakens` + `evidence_direction_per_claim[MECH-341]=weakens`; correct it with an `evidence_direction_note`).
- **pending_retest_after_substrate:** retain TRUE on MECH-341 (already set).
- **narrow_supports_flag:** TRUE -- MECH-341's supports are stack-only; the within-class graded sub-axis is unestablished.
- **no substrate_queue entry, no /diagnose-errors, no governance demotion.** 660 stays standing (not superseded).

## 9. Recommended `evidence_quality_note` (exact text for governance to write; this skill does not write it)

> "2026-06-11 failure autopsy (failure_autopsy_V3-EXQ-660a_2026-06-11): V3-EXQ-660a (within-class-representative-diversity GRADED confirmation; CEM pool-size sweep K=16->128) FAILed C_GRADED (1/3 seeds graded) and self-routed weakens, but is reclassified **non_contributory (measurement_test_design_defect)**. Root cause: the primary readout `within_class_rep_cond_entropy = H(rep_signature | committed_class)` is a PHASE-AGGREGATE over every P1 tick that SATURATES (absolute sampled entropy flat ~4.6-4.9 nats while per-tick within-class availability rose 5->34; C_ABS failed) and is CONFOUNDED BY TICK COUNT (seed 43 ~10k ticks -> ~6.3 nats in BOTH legacy and sampled arms vs seeds 42/44 ~1-2k ticks -> ~3.7-4.6). The graded axis (pool size) provably moves the INPUT (non-vacuity met) but the readout cannot register a per-decision diversity benefit, so the run cannot adjudicate the graded sub-claim. MECH-341 NOT weakened. Its in-stack preserver role (614a PASS_C2_C3_only, 569d) stands; the within-class GRADED sub-axis remains UNESTABLISHED (660 readout-degenerate, 660a non-contributory) -- narrow_supports_flag set. V3-EXQ-660 stays standing (660a does not supersede it). Route: /queue-experiment redesign with a per-decision/windowed within-class diversity readout with headroom (windowed H(rep|class), or selected-vs-available efficiency in [0,1]) plus a readout-sensitivity gate; same-question readout fix = alphabetic successor (660b). MECH-341 stays candidate / v3_pending / pending_retest_after_substrate."
