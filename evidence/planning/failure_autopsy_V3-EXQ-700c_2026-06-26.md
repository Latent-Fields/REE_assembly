# Failure Autopsy -- V3-EXQ-700c (ARC-108/MECH-450 same-layer-null settling; pre-registered terminal of the 700 lineage)

- **Generated (UTC):** 2026-06-26T04:46:05Z
- **Scope:** single target (700 lineage); convergent-endpoint context shared with V3-EXQ-706 (see Section 9)
- **Status:** confirmed (user-adjudicated 2026-06-26 -- Reading B / validity re-tune)
- **Claims tagged:** MECH-439 (F-dominance conversion ceiling; candidate / substrate_ceiling), ARC-108 (dopamine-gated learned channel-gating; candidate / substrate_conditional), MECH-450 (recurrent settling step; candidate / substrate_conditional)
- **Outcome:** FAIL -- self-route `substrate_not_ready_requeue` (precondition_unmet) -- evidence_direction `non_contributory` (all 3 claims)
- **Machine:** ree-cloud-3
- **Run:** `v3_exq_700c_arc108_sec7_learned_gating_settling_samelayer_null_20260625T220313Z_v3`
- **Supersedes:** V3-EXQ-700b

---

## 1. Facts -- reconstruction (no interpretation)

700c is the **same-layer null redesign** the confirmed `failure_autopsy_V3-EXQ-700b_2026-06-24` pre-registered as the terminal V3 letter: replace 700b's policy-softmax-temperature null (MECH-313 `use_noise_floor`, which was decoupled from the committed-class DV) with a frozen magnitude-matched random `W_lat` injected into the eligibility/settling field -- the same layer MECH-450 settling acts on -- gated behind per-arm `field_noise` so A0/A2/A3/C3 stay byte-identical to 700b.

5 arms x 6 seeds, phased P0/P1/P2, reef-bipartite foraging. Landed arithmetic envelope (demotion + adaptive floor 689e + go_nogo 689g + modulatory-authority/top_k k=3 569i) is a matched constant on all arms. PRIMARY DV = committed-action-class entropy on divergent seeds. Arms: A0_ENVELOPE_ONLY / A2_SETTLING_SIGNED / A3_BOTH_SIGNED / C3_SETTLING_UNSIGNED / ARM_NOISE (frozen magnitude-matched random W_lat settling-field null, `learned_settling_eta=0`).

### Acceptance criteria (manifest `result.acceptance_criteria`)

| field | value |
|---|---|
| preconditions_met | **False** |
| enough_divergent_seeds | True (3/3) |
| **noise_verified_lifting** | **False (n_noise_lifts_over_a0 = 0)** |
| **field_noise_magnitude_matched** | **False (ratio 41.42; band [0.25, 4.0])** |
| delta_t_carries_variance | True |
| learned_weights_moved | True |
| candidate_pool_divergent | True |
| C1_conversion | False (a2 1/3, a3 0/3, c3u 1/3 divergent seeds) |
| C2 grows | False |
| median_noise_wlat_range | 2.161 |
| median_settling_wlat_range | 0.052 |
| mean_committed_class_entropy_a0 | 0.909405 |
| mean_committed_class_entropy_a2_settling_signed | 0.924714 (+0.015) |
| mean_committed_class_entropy_a3_both_signed | 0.951682 (+0.042) |
| mean_committed_class_entropy_c3_settling_unsigned | 0.970209 (+0.061) |
| **mean_committed_class_entropy_noise_same_layer** | **0.859488 (-0.050 BELOW A0)** |

### Failed criterion type

`precondition_unmet` (readiness gate), NOT a discrimination/absolute criterion. Two unmet preconditions, both about the same-layer null:

1. **`field_noise_magnitude_matched` = 41.42** (band [0.25, 4.0]). The frozen-random `W_lat` at `FIELD_NOISE_WLAT_SCALE=0.5` produced a median range of 2.16, but the LEARNED settling arms only moved `W_lat` to a median range of 0.052 -- the random null is **~41x larger** than the structure the learning arms learn.
2. **`noise_verified_lifting` = 0/3.** Despite being 41x oversized, the noise arm's committed-class entropy (0.859) sits **below** A0 (0.909) -- the oversized random perturbation HURT diversity rather than lifting it. So the matched-noise floor never verified, and the C1 "strict-above-noise" bar is meaningless.

### The two facts that distinguish 700c from 700b

- **The null is broken in a NEW way.** 700b's null was *decoupled-inert* (policy temperature, 0.001 over A0). 700c's same-layer null is *magnitude-mismatched* (41x too big, drove entropy below A0). The redesign moved the null to the correct LAYER but at the wrong SCALE.
- **The learned-settling signal WEAKENED.** 700b: a2 +0.037 / a3 +0.051 / c3u +0.123 with majority divergent-seed C1 coverage (a2 2/3, a3 2/4, c3u 4/4). 700c: a2 +0.015 / a3 +0.042 / c3u +0.061 with collapsed coverage (a2 1/3, a3 **0/3**, c3u 1/3). The settling arms still beat A0 (and the mis-scaled noise) in the MEANS, monotonically, but no longer pass C1 per-seed.

---

## 2. Claim-layer mapping

The experiment did **not** test the claims under conditions where they could express themselves -- the conversion DV was gated behind a non-vacuity precondition (a verified, magnitude-matched null) that failed. `claim_ids` are correct: MECH-439 = the conversion ceiling under attack; ARC-108 (w_chan) + MECH-450 (W_lat settling) = the learned levers being tested. All three `candidate`, `implementation_phase: v3`; MECH-439 `substrate_ceiling`, ARC-108/MECH-450 `substrate_conditional`. **PROMOTES NOTHING, WEAKENS NOTHING.** The self-route `non_contributory` is SOUND.

---

## 3. Biological-reference triage

Unchanged from the 700-cluster / 700b autopsies and reconfirmed:
- **ARC-108** -- faithful BG three-factor dopaminergic plasticity (cortico-striatal eligibility x signed RPE; D1-LTP/D2-LTD). Not a formal import. Lit present (`targeted_review_connectome_mech_439`).
- **MECH-450** -- faithful BG/pallidal recurrent winner-take-most settling (Mink surround inhibition). Not a formal import.
- **Missing-dependency signature:** biological BG action selection runs over multiple parallel cortico-BG-thalamic loops. A single foraging arena cannot exercise loop-segregated committed diversity OR (per 700b) furnish a valid committed-class null. The repeated null breakage is the concrete face of that single-arena limit.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | conversion could not express -- the null was invalid (magnitude 41x off), so C1 is not trustworthy |
| Biological reference | clear | faithful three-factor DA plasticity + recurrent settling; lit present |
| Prerequisites | present | ARC-108/MECH-450 built + engaged; w_chan + W_lat move; delta_t variance; settling moves the field |
| Implementation | complete-and-engaged | learning machinery runs; settling arms lift A0 in the means |
| Environment | binding constraint (single arena) | reef-bipartite single arena structurally hard to furnish a valid committed-class null |
| Measurement | **ROOT (dominant)** | the same-layer null was injected at the right LAYER but the wrong SCALE (FIELD_NOISE_WLAT_SCALE=0.5 -> range 2.16 = 41x the learned 0.052). A one-time scale re-tune to ~0.012 makes the null magnitude-matched. This is a CALIBRATION artifact, the V3-EXQ-642 invalid-precondition family -- identical in shape to V3-EXQ-704 (ARM_NOISE 176.9x). |
| Integration | coupled | learning composes inside the F-bounded eligible set |
| Scale | adequate | 6 seeds x 5 arms x phased; the gap is null SCALE, not budget |

**Dominant diagnosis:** measurement / calibration ROOT -- the same-layer null's `FIELD_NOISE_WLAT_SCALE` is mis-calibrated relative to the realised learned `W_lat` range. Recommended `epistemic_category`: NO CHANGE (MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional). Recommended `evidence_direction`: `non_contributory` (matches the self-route), `pending_retest_after_substrate`.

---

## 5. Lineage pattern (700 / 700a / 700b / 700c)

The null has been broken across the whole lineage, but the breakage MODE changed at 700c:

| run | null design | null outcome | learned-settling lift |
|---|---|---|---|
| 700 | policy temperature alpha=1.0 | 1/3 lift | seed-42 only (+0.25, beat noise) |
| 700a | policy temperature alpha=1.0 | 0/3 (pool collapsed) | unscoreable |
| 700b | policy temperature alpha=2.0 | 0/3 (decoupled-inert) | a2 +0.037 / a3 +0.051 / c3u +0.123 (majority) |
| **700c** | **same-layer frozen W_lat, scale 0.5** | **0/3 (magnitude 41x too big, drove entropy below A0)** | **a2 +0.015 / a3 +0.042 / c3u +0.061 (1/3, 0/3, 1/3)** |

700c moved the null to the correct LAYER (the 700b autopsy's recommendation) and the breakage flipped from "too inert" to "too large." That is a *new* failure mode reachable by a single scale re-tune -- not the same lever circling the same ceiling.

---

## 6. Re-derive brake -- NOT FIRED (brake-lock recorded)

Mechanically the brake would fire on a CLEAN ceiling (MECH-439 would be the 6th, ARC-108 4th, MECH-450 3rd substrate_ceiling/non_contributory autopsy). **It does NOT fire here**, by the same logic that exempted V3-EXQ-705 (not 705b): this is a confounded / invalid-precondition self-route (the magnitude-mismatched null), **not** a clean ceiling. The conversion DV was never validly tested -- a 41x-oversized random null is not the magnitude-matched bar the design requires. The brake fires on a fair-and-still-ceilinged result, not on a broken instrument.

**Brake-lock recorded:** the NEXT time the 700 lineage produces a result with a VALID magnitude-matched same-layer null AND the learned settling still adds nothing, the brake FIRES and routes to V4 ARC-110 loop-segregation with no further V3 letters. 700d is the one validity-fixed letter the lock permits; a 700e on the same broken null would not be.

**This 700d re-tune is brake-exempt** because it is a measurement-validity fix (re-calibrate `FIELD_NOISE_WLAT_SCALE` to the realised learned range), the same class as 704->704b and 705->705b -- NOT another iteration of a fair test against a known ceiling.

---

## 7. Learning extracted + routing (user-adjudicated 2026-06-26: Reading B / validity re-tune)

**Learning:**
1. A same-layer (eligibility/settling-field) null is the correct LAYER (confirmed: it is coupled to the committed-class DV, unlike 700b's temperature null), but its magnitude must be matched to the realised learned `W_lat` range at run time, not a fixed scale. `FIELD_NOISE_WLAT_SCALE=0.5` overshot by 41x.
2. The unsigned C3 settling arm's `W_lat` blows up (per-arm ranges 1.9-4.8) because abs-RPE accumulates without sign cancellation -- a secondary calibration note for the re-tune (the median is dominated by the 12 small A2/A3 cells, so `median_settling_wlat_range`=0.052 is the right match target, not the C3 tail).
3. The learned-settling signal weakened from 700b to 700c; whether that is a real per-seed effect or a divergent-seed-subset artifact is unresolved and is exactly what a validly-nulled 700d would settle.

**Routing: `/queue-experiment` V3-EXQ-700d (validity re-tune; brake-exempt).**
- Re-tune the same-layer null so its frozen-random `W_lat` range is matched to the REALISED median learned settling range at run time (target ~0.012 absolute, or compute the scale from the in-run learned range so the match is automatic), bringing `field_noise_magnitude_matched` into [0.25, 4.0].
- Strengthen the readiness gate so a near-vacuous match (or a noise arm that drives entropy BELOW A0) self-routes `substrate_not_ready_requeue` rather than scoring.
- Keep all 700c design (5 arms, settling layer, matched arithmetic envelope, reef-bipartite, phased P0/P1/P2, committed-action-class entropy DV).
- `claim_ids=[MECH-439, ARC-108, MECH-450]`; `experiment_purpose=evidence`; PROMOTES NOTHING.
- Pre-register 700d as **terminal for the validity question**: if the magnitude-matched null verifies AND the learned settling still does not lift, escalate to V4 ARC-110 (no more V3 letters) -- this trips the brake-lock.

**`recommended_substrate_queue_entry.action = amend`** (target `v4_loop_segregation`) -- additive bookkeeping ONLY: record 700c as a `metric_trajectory` / `failure_record` data point on the gated entry to preserve the convergent-endpoint signal (Section 9). This does NOT change the entry's `ready=false` / gated status and does NOT force the build; the immediate routing is the 700d re-test. No new substrate is required for 700d (the settling substrate is built; the fix is to the experiment null scale).

**Demotion threshold NOT reached** -- the claims were never validly tested. MECH-439 stays substrate_ceiling; ARC-108/MECH-450 stay substrate_conditional; all `pending_retest_after_substrate`.

---

## 8. Draft `evidence_quality_note` (for governance to write -- do not write here)

> V3-EXQ-700c (same-layer-null redesign of the ARC-108/MECH-450 learned-gating settling falsifier; supersedes V3-EXQ-700b) FAIL / non_contributory (MECH-439, ARC-108, MECH-450). Self-route `substrate_not_ready_requeue`: the same-layer frozen-random W_lat null came in at 41.42x the realised learned settling range (median noise 2.16 vs learned 0.052; `field_noise_magnitude_matched` band [0.25,4.0] FAILED) and drove committed-class entropy BELOW A0 (0.859 vs 0.909; `noise_verified_lifting` 0/3) -- the matched-noise floor never verified, so C1 strict-above-noise is meaningless. Autopsy 2026-06-26: this is a calibration artifact (the same-layer null is the correct layer per the 700b autopsy, but FIELD_NOISE_WLAT_SCALE=0.5 overshot), the V3-EXQ-642 invalid-precondition family, identical in shape to V3-EXQ-704's 176.9x mismatch. The learned-settling signal weakened from 700b (a2 +0.037/a3 +0.051/c3u +0.123, majority) to 700c (a2 +0.015/a3 +0.042/c3u +0.061; a2 1/3, a3 0/3, c3u 1/3) but still lifts A0 in the means -- whether that drop is real is exactly what a validly-nulled 700d settles. Re-derive brake NOT fired (invalid-precondition, not a clean ceiling); brake-LOCK recorded (next VALID-null no-lift fires it -> V4 ARC-110, no more V3 letters). Routing: /queue-experiment 700d re-tuning the same-layer null scale to the realised learned range (brake-exempt validity fix); recommended_substrate_queue_entry amend = additive trajectory record on the gated v4_loop_segregation entry (does not un-gate). No promotion/demotion; pending_retest_after_substrate.

---

## 9. Convergent endpoint (cross-claim signal -- user-directed to record)

V3-EXQ-700c (settling-conversion lineage; MECH-439/ARC-108/MECH-450) and V3-EXQ-706 (curiosity-conversion lineage; MECH-314) -- autopsied the same session -- both ultimately point to **V4 ARC-110 loop-segregation** as the escalation, reached from structurally different mechanisms. They are NOT a cluster by failure shape (700c = magnitude-mismatched null; 706 = degenerate temperature null + seed-imbalance), but they share a **measurement lesson that IS the convergent signal**:

> On the V3 single foraging arena, neither conversion test could furnish a VALID committed-class null. 700b's temperature null was decoupled-inert; 700c's same-layer null was magnitude-mismatched (41x); 706's temperature null was byte-identical-inert (ARM_NOISE == ARM_FONLY on all seeds). The committed-class-entropy DV is decoupled from temperature/scale-mismatched perturbations by the F-bounded eligibility constitution -- a valid null must be a same-layer, magnitude-matched perturbation, and even that is hard to calibrate on one arena.

This independently strengthens the 700b "single arena is the binding constraint" argument: it now holds across BOTH the settling and curiosity routes. Each lineage gets ONE validity-fixed V3 letter (700d / 706b) before the V4 jump; if either's validly-nulled re-test still shows no conversion, that is the decisive escalation to ARC-110. Recorded as a `failure_record` trajectory point on the gated `v4_loop_segregation` substrate entry (additive; does not un-gate).
