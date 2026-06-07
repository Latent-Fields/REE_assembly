# Failure Autopsy -- V3-EXQ-648 (MECH-314a Phase-2 substrate-readiness)

- generated_utc: 2026-06-07T04:58:08Z
- run_id: `v3_exq_648_mech314a_phase2_substrate_readiness_20260607T025417Z_v3`
- queue_id: V3-EXQ-648
- outcome: FAIL, evidence_direction=non_contributory, claim_ids=[] (diagnostic)
- self-routed label: `phase2_wiring_does_not_support`
- gated substrate_queue entry: `MECH-314a-Phase-2-impl` (status `implemented_pending_validation`)
- scope: single (with a cross-reference to `modulatory-bias-selection-authority`)
- status: confirmed (interactive routing confirmed 2026-06-07)

---

## 1. One-paragraph verdict

The diagnostic FAILed its single load-bearing criterion (C2: visitation lifts
per-candidate bias spread) with the per-candidate curiosity bias range pinned at
**exactly 0.0 in every arm**, including the visitation-source positive control
(ARM_1) and the Candidate-5A visitation+one-hot arm (ARM_2_ON). This is **not** a
genuine "the Phase-2 wiring cannot work" null, and **not** claim falsification
(the run is claim-free). It is a **representation-boundary defect compounded by a
mis-specified readiness precondition**: the MECH-314a curiosity novelty is
computed on the hippocampal proposer's `candidate_world_summaries`
(`trajectory.world_states[:,0,:]`), whose cross-candidate spread is **< 0.01**,
while the readiness precondition measured a *different* representation -- the
SD-056-trained `e2.cand_world_pairwise_dist` (`e2.world_forward(z0, a_i)`) at
**0.1147** -- and declared the substrate ready. On correct adjudication the
self-route is a **`precondition_unmet`** (the V3-EXQ-642 lesson): the substrate
was never handed a differentiated candidate input to lift, so its zero-range bias
is an artifact of a collapsed input, not evidence against the Phase-2 mechanism.

---

## 2. Facts reconstruction (no interpretation)

Design: 4 cells x 3 seeds x 30 ep (P0=60 warmup, P1=20 measure), harm-free env
(num_hazards=0, so the Phase-1 residue source is empty by construction -- the F1
contrast the visitation source is meant to fix). Budget was deliberately bumped
(P0 20->60, P1 10->20) to the V3-EXQ-604a SD-056 budget so under-training could
not trivially trigger `substrate_not_ready_requeue`.

Arms: ARM_0 BASELINE (residue/never, SD-056 ON), ARM_1 VISITATION_ONLY
(visitation/never, SD-056 ON), ARM_2 VIS_ONEHOT_SD056_ON (Candidate-5A
visitation+auto-augment, SD-056 ON), ARM_2 VIS_ONEHOT_SD056_OFF (Candidate-5A
wiring, SD-056 untrained probe).

### Readiness preconditions -- BOTH MET

| precondition | measured | threshold | met |
|---|---|---|---|
| sd056_candidate_zworld_spread_supra_floor (ARM_1 `e2.cand_world_pairwise_dist`) | 0.114789 (3/3 seeds) | 0.05 | TRUE |
| rolled_out_zworld_magnitude_bounded (max across arms) | 0.233834 | 1.0e6 | TRUE |

So the run did **not** self-route to `substrate_not_ready_requeue`; it routed to a
substrate verdict.

### Criteria

| Criterion | load_bearing | passed | criteria_non_degenerate |
|---|---|---|---|
| C1 baseline_collapsed | false | TRUE | **FALSE** |
| **C2 visitation_lifts_per_candidate_bias_spread** | **TRUE** | **FALSE** | TRUE |
| C3 augmentation_engages_when_needed | false | FALSE | TRUE |
| C4 mech094_simulation_gate | false | TRUE | TRUE |

overall_pass=false; label=`phase2_wiring_does_not_support`.

### The pinned-zero signal

`curiosity_std_per_arm_mean` (per-candidate curiosity bias std across K):
ARM_0 = 0.0, ARM_1 = 0.0, ARM_2_ON = 1e-08, ARM_2_OFF = 1e-08.
`curiosity_bias_range_mean` = **0.0 in every single arm_result** (all 12 cells).
`c2_arm1_seeds_ok` = 0 / 3 (needs >= 0.80 positive-std fraction on >= 2 seeds).

The visitation buffer was populated and used: ARM_1 `n_buffer_appends_in_run` =
15478/15179/6216 across seeds; `novelty_source_counts` = {"visitation": N} on the
visitation arms. So this is **not** the V3-EXQ-604a empty-comparison-set cause
(residue field empty -> novelty None -> zero bias).

### z_world spread vs augmentation engagement (the tell)

`pairwise_dist_per_arm_mean` (= `e2.cand_world_pairwise_dist`): ARM_0/ARM_1/
ARM_2_ON all 0.114789 (identical -- e2 state independent of curiosity config);
ARM_2_OFF 0.016563 (SD-056 untrained -> e2 near-collapsed).

`augmentation_engage_frac_per_arm_mean`: ARM_2_ON = **0.862**, ARM_2_OFF =
**0.900**. The auto-augmentation policy engages only when
`_candidate_spread(candidate_world_summaries) < curiosity_min_spread_threshold`
(0.01) for consecutive ticks. **ARM_2_ON engaged ~86% of ticks despite its
`e2.cand_world_pairwise_dist` being 0.1147 (>> 0.01).** That is only possible if
`_candidate_spread` is measuring a *different, collapsed* representation than the
`e2.cand_world_pairwise_dist` the readiness gate measured.

C4 sub-probe: buffer admitted 12/12 waking appends, 0/12 simulation
(hypothesis_tag=True) appends -- MECH-094 gate clean.

---

## 3. Root cause (confirmed against `ree-v3/ree_core/policy/structured_curiosity.py`)

There are **two distinct "candidate z_world" representations** in play:

1. `e2.cand_world_pairwise_dist(z0, actions_K)` -- rolls each candidate's first
   action through `e2.world_forward`. **SD-056 trains exactly this** to be
   action-divergent -> 0.1147. The readiness precondition measures this.
2. `candidate_world_summaries` = `trajectory.world_states[:,0,:]` -- the
   hippocampal CEM proposer's per-candidate first-step world summaries. **This is
   what `StructuredCuriosity._compute_novelty` / `_compute_novelty_phase2`
   actually consume** (`structured_curiosity.py:460-709`), and what
   `_candidate_spread` (lines 563-577) feeds into the auto-augmentation latch.

`_compute_novelty` (lines 685-709) computes, per candidate i:
`min_dists[i] = min_j ||sig_i - center_j||` over the visitation-buffer centers,
then `novelty[i] = min_dists[i] / mean_norm`. With the candidate summaries
collapsed to a sub-0.01 ball and a dense 256-entry visitation buffer covering that
same region, every candidate's min-distance-to-buffer is near-identical ->
**zero-range novelty -> zero-range curiosity bias -> C2 fails.**

The 86-90% auto-augmentation engagement in *every* arm (including SD-056-ON) is the
direct evidence that `candidate_world_summaries` spread is < 0.01 even when the
SD-056 `e2.world_forward` spread is 0.1147. **The SD-056 divergence lives in a
representation the MECH-314a novelty never reads.** The one-hot augmentation bypass
(lines 688-699: cat first-action one-hot, zero-pad centers) also failed to lift the
range (ARM_2_ON std 1e-08) because a monostrategy-collapsed proposer emits
near-identical first actions -> near-identical one-hots -> no per-candidate
differentiation injected.

### Why the self-route label is wrong

The readiness precondition description asserts it measures "**the SAME
cross-candidate range statistic C2 routes on**". It does not. C2 routes on the
curiosity bias derived from `candidate_world_summaries`; the precondition measured
`e2.cand_world_pairwise_dist`. The precondition gave a **false READY**. The
C2-relevant precondition -- proposer-summary spread -- is **unmet (< 0.01)** and was
never checked. Correctly adjudicated, this run should have self-routed
`substrate_not_ready_requeue` / `precondition_unmet`, NOT a substrate verdict.
This is the canonical V3-EXQ-642 failure mode (a diagnostic's branch assumption
was unmet, so the verdict label mislabels the cause).

---

## 4. Biological-reference triage

Closest mechanism: MECH-314a striatal/hippocampal novelty signal (Wittmann 2008
VTA-hippocampal novelty; RPE-independent). Biological novelty operates over
**distinct candidate representations** (distinct place/object codes). The REE
translation requires the candidate representations entering the novelty comparison
to actually differ. When the proposer collapses every considered option onto the
same world-state code (the monostrategy signature), the novelty signal has nothing
to differentiate -- exactly what would happen biologically if all options mapped to
one hippocampal representation. The FAIL therefore matches a **missing-dependency
signature**, not a falsification: the absent dependency is *candidate-representation
diversity at the proposer->novelty boundary*. Not a formal-definition import; no
new lit-pull warranted.

---

## 5. Four/eight-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free) | Does not weight any claim; MECH-314 not under direct test. |
| Biological reference | clear | Wittmann 2008 striatal novelty; failure = "all options share one representation" missing-dependency signature. |
| Prerequisites | **missing** | Candidate-representation diversity at the proposer summary boundary; SD-056 divergence does not reach `trajectory.world_states[:,0,:]`. |
| Implementation | **partial** | Visitation buffer wired + populating (15478 appends); augmentation engages; decomp records -- but novelty consumes the collapsed proposer representation. Symbol-of-mechanism present, functional-role absent. |
| Environment | adequate | Harm-free env was deliberate (tests the visitation fix for F1); buffer non-empty, so that part worked. |
| Measurement | **misleading** | Readiness precondition measures `e2.cand_world_pairwise_dist`; C2 routes on the proposer-summary-derived bias. The precondition is not the statistic C2 consumes despite claiming to be. |
| Integration | **broken at the boundary** | SD-056 -> MECH-314a handoff: e2.world_forward divergence not inherited by the proposer's first-step world summaries. |
| Scale / capacity | adequate | Budget bumped to 60/20; under-training ruled out; e2 IS trained (0.1147). |

Recommended epistemic shape (informational; claim-free so no manifest write):
`precondition_unmet` (corrects the manifest's `phase2_wiring_does_not_support`).

---

## 6. Relation to `modulatory-bias-selection-authority` (V3-EXQ-643a)

The authority lever was validated 2026-06-06 (V3-EXQ-643a PASS, after the float32
catastrophic-cancellation fix), and its own substrate_queue entry already records
the boundary this run lands on: *"scaling zero is still zero ... must guard
curiosity_bias_abs_mean > 0 before testing curiosity"* (643a memo; 604a record:
`curiosity_bias_abs_mean = 0.0`). V3-EXQ-648 is the **upstream** confirmation: the
curiosity bias is zero-*range* *before* it reaches authority scaling, so the
(working) authority lever has nothing to scale. 648 is therefore relevant to
`modulatory-bias-selection-authority` as a cross-reference, but the **fault is
upstream** -- in the MECH-314a Phase-2 curiosity-bias generation path.

---

## 7. Learning extracted

1. The MECH-314a Phase-2 curiosity novelty reads the hippocampal proposer's
   `trajectory.world_states[:,0,:]`, **not** the SD-056-trained
   `e2.world_forward(z0, a_i)` predictions. SD-056's action-conditional divergence
   does not propagate to this representation; the handoff is broken at the
   representation boundary.
2. A substrate-readiness precondition must gate on **the exact statistic the
   load-bearing criterion consumes**. 648's precondition measured a different
   (SD-056-divergent) representation than C2's curiosity bias (proposer-summary
   derived), producing a false READY and mislabelling the verdict.
3. The visitation buffer fixed F1 (empty comparison set on harm-free runs) but
   cannot manufacture per-candidate differentiation from a collapsed candidate
   input; the one-hot bypass also fails when the proposer is monostrategy-collapsed
   (identical first actions -> identical one-hots).

---

## 8. Repair pathway (routing confirmed interactively 2026-06-07)

**Routing: implement-substrate (amend) + queue-experiment (re-queue).**

Substrate amend (`MECH-314a-Phase-2-impl`, action=amend):
- Compute per-candidate MECH-314a novelty from the **SD-056-divergent
  `e2.world_forward(z0, a_i)` per-candidate predictions** (the representation the
  readiness gate already validates at 0.1147), rather than the proposer's collapsed
  `trajectory.world_states[:,0,:]`.
- Correct the readiness precondition (and the auto-augmentation `_candidate_spread`)
  to measure the **same representation the curiosity bias consumes**, so a collapsed
  input self-routes `substrate_not_ready_requeue` instead of a false READY.

Re-queue (via `/queue-experiment`): **V3-EXQ-648a** substrate-readiness diagnostic
on the amended substrate, with the corrected precondition. Keep the 60/20 budget,
the 4-cell design, and the C1-C4 grid; PASS gates V3-EXQ-590b + the section-8
MECH-314a/MECH-314/ARC-065 governance updates as before.

No claim demotion (claim-free diagnostic). No lit-pull (mechanism biologically
sound; the gap is the V3 representation handoff).

Draft `evidence_quality_note` (for the eventual MECH-314 governance touch, NOT
written here): *"V3-EXQ-648 (MECH-314a Phase-2 readiness) FAILed C2 because the
curiosity novelty consumed the hippocampal proposer's collapsed
trajectory.world_states[:,0,:] (spread <0.01) rather than the SD-056-divergent
e2.world_forward predictions (0.1147); readiness precondition mis-measured the
representation and gave a false READY. Not evidence against MECH-314a; pending
retest V3-EXQ-648a on the amended substrate (novelty fed from e2.world_forward +
precondition corrected)."*

`pending_retest_after_substrate`: true. The "supports" set for MECH-314a remains
narrow/unestablished -- this run is non_contributory.
