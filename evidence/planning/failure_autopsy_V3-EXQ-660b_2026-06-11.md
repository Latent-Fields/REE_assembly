# Failure autopsy -- V3-EXQ-660b (MECH-341 within-class-representative-diversity GRADED confirmation, windowed-readout redesign)

- **Date (UTC):** 2026-06-11T15:37:58Z
- **Scope:** single (with a 3-iteration lineage measurement/framing pattern note)
- **Status:** confirmed (user-adjudicated at the Step-8 gate 2026-06-11: chose "non_contributory" + "retire the graded falsifier")
- **Routing:** governance reclassification of the manifest direction (weakens -> non_contributory) + RETIRE the graded-in-pool-size falsifier for MECH-341 (no 660c; no substrate work)
- **Target:** run_id `v3_exq_660b_mech341_within_class_pool_size_graded_windowed_readout_20260611T134330Z_v3`, queue_id V3-EXQ-660b, claim_ids [MECH-341]
- **Predecessor lineage:** V3-EXQ-660 (PASS/supports, STANDING -- NOT superseded); V3-EXQ-660a (FAIL/weakens self-route -> autopsied non_contributory, measurement_test_design_defect / phase-aggregate saturation; failure_autopsy_V3-EXQ-660a_2026-06-11); failure_autopsy_MECH-341-cluster_2026-05-31 (confirmed; established MECH-341 = score-layer preserver, load-bearing in-stack only).

---

## 1. Scope

V3-EXQ-660b is an **evidence** experiment (experiment_purpose=evidence, claim_ids=[MECH-341]): the windowed-readout redesign of V3-EXQ-660a, supersedes 660a, routed by failure_autopsy_V3-EXQ-660a_2026-06-11. It ran to completion (24/24 cells, 3 seeds x 8 arms), self-routed **FAIL / weakens** with
`interpretation_label = FAIL_lift_not_graded_under_sensitive_windowed_readout_fixed_structural_artifact`.
Governance cycle #4 (2026-06-11) walked this FAIL and **flagged it for autopsy rather than stamping an inline `evidence_direction`** -- the manifest's self-emitted `weakens` is LEFT PENDING with no governance evidence stamp. This skill adjudicates whether that `weakens` is a genuine falsification of MECH-341's within-class GRADED sub-axis, or a below-resolution / binary-not-graded situation.

## 2. Facts (no interpretation)

**Design.** Same scientific question + same agent/arms/env/budget as 660a; the ONLY change is the readout + the readiness gate. 660a's PRIMARY readout was a PHASE-AGGREGATE H(rep_signature | committed_class) that saturated and was tick-count-confounded. 660b replaces it with:
- PRIMARY: a per-decision **WINDOWED** H(rep|class) = mean over fixed 50-tick windows (removes the tick-count confound, preserves headroom).
- SECONDARY: a normalised [0,1] selected/available within-class efficiency.
- The phase-aggregate readout is carried for the 660a saturation contrast.

C_GRADED (PRIMARY, load-bearing, on the WINDOWED readout): per-seed paired lift Delta(K)=sampled-legacy monotone-nondecreasing across K AND Delta(K_max)-Delta(K_min) >= 0.05 nats on >= 2/3 seeds.

660b gates C_GRADED behind TWO readiness checks, EITHER unmet -> `substrate_not_ready_requeue` (non_contributory, NOT a weakens):
1. INPUT availability rises across K (== the 660a non-vacuity guard).
2. The SAMPLED-arm WINDOWED readout MOVES across K (range >= 0.05 nats -- the SAME statistic C_GRADED routes its lift on, asserted as a RANGE on the positive control). This is the explicit 660a-defect fix: the readout must register K before any weakens is reachable.

**Results (from the manifest).**
- **Readiness gate 1 MET (genuine).** Sampled within-class availability rose 4.99 -> 8.81 -> 17.62 -> 33.84 across K (rise 28.85 >> 0.25 floor). Pool honored (realized 16/32/64/128). criteria_non_degenerate.input_non_vacuity=true, pool_size_honored=true.
- **Readiness gate 2 MET but MARGINAL + NON-MONOTONE.** Sampled windowed-H by K = {16: 0.987, 32: 1.044, 64: 1.020, 128: 1.037}; range = 0.0568 >= 0.05 floor. criteria_non_degenerate.readout_sensitive=true. The positive control does NOT cleanly track K: it bumps at K=32 and settles; the 0.0568 "range" is dominated by the single K=32 excursion, not a dose-response.
- **C_GRADED FAILED 0/3 seeds.** Per-seed paired lift Delta(K) = sampled - legacy (windowed):
  - seed 42: {16: -0.0469, 32: +0.1043, 64: -0.0327, 128: -0.0097}, monotone=False, margin 0.0371 -> not graded
  - seed 43: {16: -0.0421, 32: -0.0277, 64: -0.0280, 128: -0.0323} (ALL NEGATIVE), monotone=False, margin 0.0097 -> not graded
  - seed 44: {16: -0.0343, 32: +0.0422, 64: +0.0362, 128: +0.0390}, monotone=False, margin 0.0733 -> not graded
  - Deltas are noise around zero, non-monotone, mostly negative.
- **Phase-aggregate contrast (660a saturation tell, carried):** sampled phase-aggregate by K {16: 4.608, 32: 4.862, 64: 4.805, 128: 4.887}, range 0.280 -- still flat at ~4.6-4.9 nats (confirms the 660a defect existed; the windowed readout is the fix).

**Failed criterion type:** the load-bearing criterion that failed is a **discrimination** criterion (graded dose-response). The negative-control/absolute side (availability rise, pool honored) PASSED. "Negative control passes, discrimination fails" -- but here it resolves to measurement-resolution + claim-framing, NOT a substrate ceiling and NOT a falsification (Sections 5-7).

## 3. Claim-layer map

**MECH-341** (`ethics_engine_3.scoring_trajectory_class_diversity_preservation`): claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, pending_retest_after_substrate=true, implementation_phase=v3. depends_on ARC-065, ARC-033, SD-003, INV-076. The confirmed 2026-05-31 cluster autopsy fixed its role: **a score-layer PRESERVER of upstream-supplied candidate-pool diversity, load-bearing in the full stack only; in-isolation testing structurally unreachable**. Promotion gated on in-stack evidence (614a PASS_C2_C3_only, 569d matched-entropy PASS), not in-isolation R2.c clearance.

660/660a/660b probe a FINER sub-axis: that within-class representative *sampling* adds *graded* selected diversity as more representatives become available (pool size K). This is distinct from, and downstream of, the in-stack preservation role.

**Did the test let the claim express itself?** No -- for two compounding reasons.
1. The graded sub-claim could be read as a genuine negative only through a readout that demonstrably tracks K in the positive control. 660b's readout cleared the gate only MARGINALLY (0.0568 vs 0.05) and NON-MONOTONICALLY (0.987/1.044/1.020/1.037) -- so "readout demonstrably sensitive to K" is OVERSTATED. The substantive precondition (a clean monotone dose-response in the positive control, against which a flat sampled-legacy lift would be a real negative) is NOT met even though the numeric range threshold was. This is the V3-EXQ-642 / 660a "self-route is a hypothesis" pattern recurring one layer deeper.
2. More fundamentally: **graded-in-pool-size is not what MECH-341 asserts.** MECH-341 asserts E3 scoring PRESERVES trajectory-class diversity rather than COLLAPSES it -- a preservation / anti-collapse mechanism. A preserver's natural signature is BINARY / threshold (preserves available diversity vs collapses), NOT a marginal lift that scales monotonically with K. "Marginal within-class lift over legacy argmin scales with K" is a STRONGER, ADDED hypothesis that 660a introduced as a ratification convenience (under uniform within-class sampling, rep entropy ~= log(distinct reps), so pool size was the viable graded axis). A fixed (binary) benefit independent of K is CONSISTENT with the preservation claim, not a falsification of it.

So 660b is non-contributory ON MECH-341: it neither supports nor weakens the preservation claim. It is contributory as test-design / lever-character learning.

**claim_ids accuracy:** correct. 660b tests the within-class sub-axis of MECH-341 directly; the tag is appropriate. The defect is in the falsifier framing + readout resolution, not the tag.

## 4. Biological-reference triage

Closest reference mechanism: **trial-to-trial action variability within a chosen action category** -- songbird LMAN->RA variability injection (Olveczky/Fee), striatal exploration, Dhawale et al. 2017 motor variability. The mechanism CLASS has a clear biological existence proof. MECH-341 is a diversity-preservation regulator (Rigotti 2013 mixed selectivity; Padoa-Schioppa & Conen 2017 categorical preservation), NOT a formal-definition import (Pearl / Shannon / optimal-control), so the SD-003 "load-bearing divergence" trap does not apply and the primary output is NOT a lit-pull. A FAIL therefore defaults to a translation / measurement / framing gap until the biology says the mechanism itself is wrong -- which this experiment cannot show. `is_formal_import=false`, `lit_status=partial` (ARC-065-side anchored; MECH-341 lit-absent, acceptable for an algorithmic regulator). Biologically, within-class action variability is not expected to scale its marginal contribution monotonically with the size of the candidate pool -- it is a preserve-or-collapse property -- which reinforces the binary-not-graded reading.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear (NOT weakened)** | graded-in-K over-specifies a preservation claim; the result does not bear on MECH-341's actual assertion. |
| Biological reference | partial | within-class action variability; class has an existence proof; not a formal import -> default reading is measurement/framing gap, not falsification. Variability is preserve-or-collapse, not pool-size-graded. |
| Prerequisites | present | within_class_branch_active=true on all sampled seeds; 151-1105 within-class samples/arm; modulatory authority (gain 0.5) + e2_world_forward summary active; pool honored 16->128. |
| Implementation | complete | lever fires; availability provably moves 5->34; the windowed readout (the 660a fix) works as instrumentation. |
| Environment | adequate | SD-054 bipartite-reef supplies the first-action classes. |
| **Measurement** | **misleading / below-resolution (DOMINANT)** | the readout-sensitivity gate cleared only MARGINALLY (0.0568 vs 0.05) and NON-MONOTONICALLY (positive control 0.987/1.044/1.020/1.037 -- the "range" is one K=32 bump, not a dose-response). So a flat sampled-legacy lift cannot be read as a clean negative: the experiment lacks the resolution to detect a graded lift of MECH-341's magnitude at 50-tick windows / this K range. |
| Integration / Scale | adequate | 3 seeds x 8 arms, thousands of ticks; not a scale issue. |

**Recommended `epistemic_category` (manifest-level note, NOT a change to the claim's category):** `measurement_test_design_defect`. The claim's own epistemic_category is unchanged; MECH-341 stays candidate / v3_pending / pending_retest_after_substrate.

**The redesign worked as instrumentation but the falsifier framing is the residual defect.** 660b correctly fixed the 660a phase-aggregate saturation (the windowed readout has headroom; the phase-aggregate contrast confirms the old defect). What 660b exposed is that, even with the saturation defect removed, the graded-in-K sub-axis is (a) below the readout's resolution at this scale (the positive control barely tracks K), and (b) the wrong question for a preservation mechanism. The two reinforce: there may simply be no graded-in-K signal to find (binary preserver), which is exactly why the positive control doesn't track K either.

## 6. Lineage pattern (3 iterations on the graded sub-axis)

660b is the THIRD consecutive instance in the MECH-341 within-class lineage where the graded confirmation does not land:

| Run | Swept axis (input) | Readout | Result | Root cause |
|---|---|---|---|---|
| 660 | within-class temperature T=0.5/1.0/2.0 | phase-aggregate H(rep\|class) | byte-identical across T | within-class scores near-degenerate -> softmax ~uniform at every T; temperature knob structurally INERT |
| 660a | CEM pool size K=16->128 (avail 5->34) | phase-aggregate H(rep\|class) | flat ~4.6-4.9; C_ABS fails | phase-aggregate readout SATURATES + tick-count-confounded; blind to K |
| 660b | CEM pool size K=16->128 (avail 5->34) | WINDOWED H(rep\|class) | C_GRADED 0/3; deltas ~0, non-monotone | readout now sees K but only MARGINALLY/non-monotonically (gate cleared on a technicality); graded lift at/below resolution AND graded-in-K over-specifies the preservation claim |

**Structural property:** three different ways of asking "does MECH-341's within-class contribution scale GRADUALLY with available diversity" have all failed to deliver a clean dose-response. The 660 PASS already established the within-class lever is LOAD-BEARING (a fixed, detectable benefit, legacy 4.781 vs sampled 4.862 nats). The convergent read is now that the within-class contribution is a **BINARY load-bearing preserver, not a pool-size-graded lever** -- and "graded-in-K" is the wrong falsifier for a preservation mechanism. The fix is NOT a 4th readout iteration; it is to RETIRE the graded-in-K falsifier and let the binary preservation reading (660) stand.

## 7. Learning extracted

1. **Non-contributory, not falsification.** 660b does not weaken MECH-341: graded-in-pool-size over-specifies the preservation claim, and the readout-sensitivity gate cleared only on a marginal/non-monotone technicality, so a flat lift is not a clean negative.
2. **The redesign succeeded as instrumentation but exposed a framing defect.** The windowed readout fixed the 660a saturation (confirmed by the phase-aggregate contrast), yet the positive control still barely tracks K -- consistent with there being no graded-in-K signal to find (binary preserver).
3. **Retire the graded-in-K falsifier.** Three iterations (660 inert temperature -> 660a saturated -> 660b marginal/non-monotone) converge on "no clean graded dose-response." Do NOT queue a 4th readout iteration. Record the within-class lever as a BINARY load-bearing preserver; the 660 PASS is the claim-faithful established result.
4. **Narrow-supports flag.** MECH-341's surviving supports remain stack-only / single-pathway (614a PASS_C2_C3_only; 569d; 660 within-class load-bearing). The within-class GRADED sub-axis is UNESTABLISHED and is now RETIRED as a gate -- reclassifying 660b non_contributory must NOT be read as "MECH-341 conflict resolved" or as graded-axis clearance.
5. **660 stays standing.** 660b does not supersede 660 (it supersedes 660a). 660's in-stack within-class load-bearing PASS is preserved; the GRADED dose-response is removed as a ratification gate, not failed.
6. **GAP-B owner_exq.** behavioral_diversity_isolation:GAP-B currently points owner_exq at 660b. Recommendation (governance to apply): re-point owner_exq to V3-EXQ-660 (the standing PASS) and record that the graded ratification 660a/660b were chasing is REMOVED AS A GATE (graded-in-K over-specifies a preservation claim), not outstanding. Node stays partial; the binary preservation reading is the established GAP-B result for MECH-341.

## 8. Routing (user-confirmed at Step 8)

User chose "non_contributory" + "retire the graded falsifier" via AskUserQuestion 2026-06-11.

- **routing:** `governance-demotion` slot is NOT used. Routing = **governance reclassification only** (manifest direction weakens -> non_contributory) + RETIRE the graded-in-pool-size falsifier for MECH-341. NO /queue-experiment (no 660c). NO substrate_queue entry (availability rises correctly -- the substrate supplies the raw material; the issue is readout resolution + claim framing, not substrate). NO /diagnose-errors (ran to completion). NO governance demotion (highest threshold not met; promote/demote already suppressed via v3_pending).
- **recommended_evidence_direction (governance to apply on the manifest):** `non_contributory` (manifest currently carries `weakens` + `evidence_direction_per_claim[MECH-341]=weakens`; correct with an `evidence_direction_note`).
- **pending_retest_after_substrate:** retain TRUE on MECH-341 (already set).
- **narrow_supports_flag:** TRUE -- MECH-341's supports are stack-only; the within-class graded sub-axis is unestablished and retired as a gate.
- **GAP-B:** re-point owner_exq 660b -> 660; mark graded ratification removed-as-gate. Node stays partial.

## 9. Recommended `evidence_quality_note` (exact text for governance to write; this skill does not write it)

> "2026-06-11 failure autopsy (failure_autopsy_V3-EXQ-660b_2026-06-11): V3-EXQ-660b (within-class-representative-diversity GRADED confirmation; windowed-readout redesign of 660a, supersedes 660a) FAILed the load-bearing C_GRADED 0/3 seeds (per-seed sampled-legacy windowed deltas noise around zero, non-monotone, mostly negative) and self-routed weakens, but is reclassified **non_contributory (measurement_test_design_defect)**. Two compounding reasons the weakens does not hold: (1) the readout-sensitivity readiness gate cleared only MARGINALLY (sampled windowed-H range across K = 0.0568 vs 0.05 floor) and NON-MONOTONICALLY (windowed-H by K = 0.987/1.044/1.020/1.037 -- the positive control does NOT cleanly track K; the range is one K=32 excursion), so 'readout demonstrably sensitive to K' is overstated and a flat sampled-legacy lift is not a clean negative (V3-EXQ-642 / 660a self-route-is-a-hypothesis pattern, one layer deeper); (2) graded-in-pool-size over-specifies MECH-341, which asserts diversity PRESERVATION (a binary / preserve-or-collapse property), not a marginal lift that scales monotonically with candidate-pool size K. The windowed readout DID fix the 660a phase-aggregate saturation (carried phase-aggregate contrast still flat ~4.6-4.9), so 660b is contributory as instrumentation/lever-character learning -- it shows the within-class benefit does NOT scale with K (3rd convergent iteration: 660 inert temperature -> 660a saturated -> 660b marginal) -- but it adds nothing to MECH-341's preservation claim in either direction. ROUTING: RETIRE the graded-in-pool-size falsifier for MECH-341 (no 660c); the within-class lever is recorded as a BINARY load-bearing preserver, with V3-EXQ-660 (PASS/supports, within-class lift 4.862 vs legacy 4.781) the claim-faithful established result. MECH-341 NOT weakened. Its in-stack preserver role (614a PASS_C2_C3_only, 569d, 660) stands; the within-class GRADED sub-axis is UNESTABLISHED and removed as a gate -- narrow_supports_flag set. V3-EXQ-660 stays standing (660b supersedes 660a, not 660). behavioral_diversity_isolation:GAP-B owner_exq re-points 660b -> 660; graded ratification removed-as-gate. No substrate_queue entry (availability rose correctly; not a substrate gap). MECH-341 stays candidate / v3_pending / pending_retest_after_substrate."
