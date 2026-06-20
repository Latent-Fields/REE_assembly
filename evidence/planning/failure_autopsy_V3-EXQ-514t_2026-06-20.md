# Failure Autopsy -- V3-EXQ-514t (MECH-436 drive-state-modulated wanting; SD-049-PHASE-2 drive-coupling RETEST)

- **Generated:** 2026-06-20T06:42:22Z
- **Run:** `v3_exq_514t_sd049_phase2_mech436_drive_coupling_retest_20260620T031416Z_v3`
- **Queue id:** V3-EXQ-514t (supersedes V3-EXQ-514s); machine ree-cloud-3
- **Outcome:** FAIL, self-routed `evidence_direction: non_contributory`, `non_degenerate: true`
- **Self-route:** `interpretation.label = mech436_enrichment_insufficient_substrate_ceiling`; `route_reason = natural_below_margin_overshoot_still_flips_retune_sd049_phase2_amend`
- **Claim under test:** MECH-436 (`drive.wanting_drive_state_modulation`, candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate). The drive-coupling leg (b) split out of MECH-229 2026-06-16. Leg (a) wanting!=liking object-bound dissociation (MECH-229, V3-EXQ-514o PASS 0.80) is NOT under test and NOT weakened.
- **Scope:** single (7th run in the 514 lineage: 514l/m/p/q/r/s/t; the /claim-synthesis split already happened at 514q)
- **Verdict (user-adjudicated 2026-06-20):** **Clean self-route; substrate-ceiling PERSISTS. `non_contributory` / `substrate_ceiling` (UNCHANGED). NOT a weakens, NOT granularity debt.** The decisive new finding: the kappa-magnitude lever is now EXHAUSTED as a monotone repair -- doubling kappa (6.0 -> 12.0) REGRESSED the natural delta rather than improving it. Route: **`/queue-experiment` 514u measurement-redesign** (continuous incentive-amplitude metric at moderate kappa), NOT another kappa raise. MECH-436 / SD-049 disposition UNCHANGED (candidate / substrate_ceiling / pending_retest_after_substrate).

---

## 1. The pre-registered decision grid (514t arming the 514s bounded-kappa amend)

failure_autopsy_V3-EXQ-514s (confirmed 2026-06-18) found lever (b) standing-differential-depletion WORKED (enriched_spread 1.0) but kappa_scale=6.0 was short on 3/5 seeds (natural delta 0.064 < 0.15 margin; overshoot 4/5). It greenlit a BOUNDED kappa raise: `incentive_drive_kappa_scale` 6.0 -> 12.0 + `per_axis_restoration_fraction` 0.3 -> 0.15 (deeper standing spread). 514t re-runs the 514r/514s controls (overshoot + OFF/bank-disabled + recalibrated argmax-relevance + enriched-spread) on the raised-kappa substrate. The decision grid (manifest `interpretation.disambiguation`):

| branch | precondition | outcome |
|---|---|---|
| any readiness gate unmet | contact / argmax-relevance / OFF-floor / bank / enriched-spread | `substrate_not_ready_requeue`, non_contributory, NEVER a weakens |
| **supports** | natural delta >= `max(K_SD*pstdev(d), 0.15)` | MECH-436 substrate_ceiling -> **supports** (load-bearing promotion path) |
| **substrate_ceiling** | natural < margin BUT overshoot flips >= 2/3 seeds | enrichment insufficient -> retune amend. **NOT a weakens.** <- **514t landed here** |
| genuine_weakens | every readiness met AND overshoot CANNOT flip even at mag 5.0 | drive cannot carve wanting on the enriched substrate |

**514t reached the substrate_ceiling branch by the honest path:** all five non-vacuity preconditions passed first, then natural delta fell below margin while overshoot still flipped a supermajority. The script self-routed correctly; the autopsy confirms the self-route.

---

## 2. Facts -- non-vacuity first (all five preconditions MET)

`non_degenerate=true`; the natural-delta test was non-vacuous:

- **Contact guard:** 5/6 seeds (`guard_fraction=0.833`; seed 44 excluded). `contact_non_vacuity_met=true`.
- **Recalibrated argmax-relevance readiness -- `pc_argmax_relevance_frac=1.0`.** Every guard-passing seed: overshoot flips a constructed realistic base_value gap while natural-magnitude drive does NOT. The overshoot magnitude is proven argmax-relevant.
- **OFF / bank-disabled floor -- `off_floor_frac=1.0`.** `wl_off_floor_fraction=0.0` on every seed: bank bypassed -> wanting==liking -> zero dissociation, by construction. The non-zero natural/overshoot dissociation is genuinely bank-driven (also bounds the kappa caveat: drive is not manufacturing a comparator artifact -- OFF floor is hard zero).
- **Bank populated -- `run_bank_populated_frac=1.0`** (`distinct_tokens_max=3` every seed; `n_scored_wl_steps_total=72`).
- **ENRICHED-SPREAD -- `enriched_spread_met=true`, frac 1.0.** `mean_drive_spread_max=0.192`; per-seed `[0.191, 0.198, 0.228, 0.153, 0.191]`, floor `MIN_ENRICHED_SPREAD=0.1`. **The env amend (lever b) is working** -- the standing differential per-axis spread is ~0.19 and argmax-relevant.

**Natural-magnitude drive delta (the supports gate):** `mean_wl_drive_delta=-0.0367`, `sd_wl_drive_delta=0.1881` -> `effect_margin = max(1.0*0.1881, 0.15) = 0.1881` -> `C_WL_DRIVE_coupled_dissociation=false`. Per-seed `[-0.333, 0.0, -0.150, 0.100, 0.200]` -> **1/5 clears the margin individually (47: 0.200); 2/5 (42: -0.333, 44: -0.150) are STRONGLY NEGATIVE.**

**Overshoot (magnitude 5.0):** `per_seed_overshoot_flips=[T,F,T,T,T]` -> 4/5 flip (`overshoot_seed_pass_frac=0.8` >= 2/3); `mean_overshoot_flip_fraction=0.8`.

**Failed criterion class:** discrimination (the supports gate). Negative-control / absolute criteria (OFF floor, bank, contact, enriched-spread, argmax-relevance) all PASS -- the classic substrate-ceiling fingerprint.

---

## 3. The decisive learning -- the kappa-magnitude lever is EXHAUSTED (non-monotone regression)

This is the load-bearing output and what distinguishes 514t from 514s. The 514s autopsy predicted "lever (b) done; lever (a) kappa just needs to go higher (bounded)." 514t tested that exact prediction at kappa 12.0 + restoration 0.15:

| Run | kappa_scale | restoration_fraction | natural-delta mean | sd | n >= margin | n < 0 | overshoot flips |
|---|---|---|---|---|---|---|---|
| 514q (06-16) | 1.0 | 1.0 (full restore) | exact 0.0 all 5 | ~0 | 0/5 | 0 | not run |
| 514r (06-17) | 1.0 | 1.0 | 0.022 (one seed 0.111) | -- | 0/5 | -- | 2/5 |
| 514s (06-18) | 6.0 | 0.30 | **+0.064** | 0.109 | 2/5 | 0 | 4/5 |
| **514t (06-20)** | **12.0** | **0.15** | **-0.037** | **0.188** | **1/5** | **2/5** | **4/5** |

- **Doubling kappa REGRESSED the natural delta, it did not improve it.** Mean crossed from +0.064 (514s) to -0.037 (514t); SD ballooned 0.109 -> 0.188; the count clearing the margin DROPPED 2/5 -> 1/5; two seeds went strongly NEGATIVE (42: -0.333, 44: -0.150).
- **What a negative `wl_drive_delta` means.** `wl_drive_delta = wl_natural_fraction - wl_nodrive_fraction` (both = fraction of scored steps where `most_wanted argmax != consumed_tag`). A negative delta means natural drive *reduced* the wanting!=liking dissociation on those seeds -- drive pushed `most_wanted` TOWARD the just-consumed (liking) target, the opposite of MECH-436's prediction.
- **Mechanism of the regression.** `wanting[k] = base_value[k] * (1 + kappa_eff * per_axis_drive[k])` with `kappa_eff = incentive_drive_kappa_weight(2.0) * incentive_drive_kappa_scale(12.0) = 24`. At kappa_eff=24 the drive term dominates `base_value`, so `most_wanted -> argmax(per_axis_drive)`, which flips chaotically through a near-tie object landscape depending on the in-run per-axis depletion structure. The argmax-flip-gated WL metric registers this as a sign-unstable, high-variance delta -- exactly the ballooning SD + negative seeds observed. **At 6.0 the drive was competitive-but-subdominant (bimodal positive); at 12.0 it over-amplified into argmax destabilisation.** There is no monotone "more kappa" that cleanly clears the flip gate.
- **Lever (b) is done** (enriched_spread ~0.19 met on all seeds); the regression is NOT a spread failure.

**Conclusion: the "needs more kappa" hypothesis is FALSIFIED as the repair path.** The remaining suspect is the MEASUREMENT layer: the argmax-flip-gated WL delta is coarse (discards continuous sub-flip re-weighting that is itself genuine incentive-salience modulation) AND interacts pathologically with high kappa. The 514s autopsy Section 7 already recorded this fork: "a continuous incentive-amplitude metric ... Recorded for a later iteration IF the kappa amend stalls." The kappa amend has now stalled (worse than 514s) -- the deferred measurement fork is now the live route.

---

## 4. Claim-layer mapping

- **MECH-436** (`drive.wanting_drive_state_modulation`, candidate, epistemic_category substrate_ceiling, v3_pending, pending_retest_after_substrate): asserts the homeostatic drive STATE re-weights most_wanted (`most_wanted = argmax base_value[k]*(1 + kappa*per_axis_drive[k])`). 514t tests this directly and lets it express -- overshoot 4/5 proves the channel carries at adequate magnitude. The FAIL bears on lever CALIBRATION (kappa magnitude over-amplifies) + the flip-gated MEASUREMENT, NOT on the claim.
- **MECH-229 leg (a)** (wanting!=liking object-bound dissociation, established V3-EXQ-514o PASS 0.80): NOT under test, NOT weakened. 514t `mean_object_bound_wl_dissoc_fraction=0.657` -- consistent, not the load-bearing statistic. **PROTECT.** The hard-zero OFF floor confirms drive is not swamping liking via a comparator artifact.

`claim_ids=[MECH-436]` is correct and single -- no inheritance error (the split corrected the umbrella tag at 514q).

---

## 5. Biological-reference triage

- **Closest mechanism:** incentive salience as **drive/state-modulated cue attraction** (Berridge 2006; Smith/Berridge/Aldridge 2011 PNAS; DiFeliceantonio/Berridge 2016). Lit present (`targeted_review_connectome_mech_347`).
- **Formal import?** No -- incentive salience IS drive/state-modulated cue attraction; the biology directly grounds the claim. The coupling gain kappa has no a-priori "correct" value, so scaling it is legitimate substrate calibration -- BUT 514t shows it is bounded ABOVE as well as below: at kappa_eff=24 drive begins to DOMINATE base_value, which is biologically wrong (a sated agent should still want a clearly-better object; cf. the 514s C8 bounded-raise contract). The 12.0 operating point overshot that bound.
- **Does the failure match a missing-dependency signature?** It matches a CALIBRATION-band + MEASUREMENT signature, not a missing dependency: the standing spread is present, the channel carries (overshoot), and the regression is over-amplification read through a coarse flip-gate. Brains remain an existence proof for the class -> the default reading is a calibration/measurement gap, NOT falsification. The overshoot control (4/5) confirms it.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | overshoot 4/5 proves the channel carries at adequate magnitude; FAIL bears on kappa calibration + flip-gated measurement. Leg-(a) MECH-229 untouched. |
| Biological reference | clear | Berridge incentive salience; kappa is bounded above (drive must not dominate base_value) -- 12.0 overshot. |
| Prerequisites / dependency | **present** | standing differential per-axis depletion present (spread ~0.19, enriched_spread 1.0); lever (b) done. |
| Implementation | adequate (over-amplified) | `most_wanted` responds; at kappa_eff=24 it over-amplifies into argmax destabilisation (sign-unstable delta). |
| Environment | **adequate** | the env amend produced the standing spread it was built for. |
| Measurement | **under-instrumented (THE suspect layer)** | WL dissociation is argmax-flip-gated -> discards continuous sub-flip re-weighting (itself genuine drive modulation) AND interacts pathologically with high kappa (chaotic flips -> SD explosion -> false-negative + sign instability). |
| Integration | coupled | bank -> most_wanted reached; overshoot + 1/5 natural move it. |
| Scale | adequate | 6 seeds, 72 scored WL steps. |

**Recommended `epistemic_category`: `substrate_ceiling` (UNCHANGED). Recommended `evidence_direction`: `non_contributory`** (scoring-excluded; `pending_retest_after_substrate: true`).

---

## 7. Repair pathway + routing (user-confirmed 2026-06-20)

**Routing: `/queue-experiment` 514u -- MEASUREMENT REDESIGN** (NOT another kappa raise; the kappa-magnitude lever is exhausted -- direct evidence it regresses, non-monotone).

- **Add a CONTINUOUS incentive-amplitude metric** alongside the flip-gated WL delta: how far natural drive shifts the wanting SCORE toward the depleted axis, even without crossing the argmax boundary. This captures the sub-flip re-weighting the current metric discards and is robust to the argmax-destabilisation that exploded the flip-gated SD at high kappa. The continuous metric resolves whether drive consistently re-weights toward the depleted axis (supporting MECH-436) even when argmax flips are noisy.
- **Revert kappa toward a MODERATE value** (toward 6.0, the bimodal-positive point) or sweep BOUNDED in (1.0, 6.0]; do NOT raise above 6.0. The 514s C8 bounded-kappa invariant (drive must not dominate base_value) is the upper bound; 12.0 violated it.
- **Lever (b) is done** (enriched_spread met on all seeds); do not deepen restoration further.
- Pre-registered promotion target (continuous metric): a drive-coupled amplitude shift toward the depleted axis >= an effect-size floor on >= 2/3 seeds, with the overshoot positive control retained and the OFF/bank-disabled control flooring at zero.

**Substrate_queue:** `amend` SD-049-PHASE-2 with the 514t failure_record. The amend RECORDS the kappa-magnitude exhaustion (6.0 positive-but-short, 12.0 noisy-negative, non-monotone) and re-routes the next iteration to the measurement redesign + moderate kappa. This is NOT a request to build another env/kappa lever -- the substrate enrichment is adequate; the 514u redesign is a `/queue-experiment` metric change. The amend is the record + the routing note so the workset generator's `blocked_by` reflects the measurement-redesign retest.

**Draft `evidence_quality_note` (for MECH-436; governance writes it):**

> 2026-06-20 (failure_autopsy_V3-EXQ-514t, confirmed): clean self-route; substrate-ceiling PERSISTS. 514t armed the 514s bounded-kappa amend (kappa_scale=12.0 + per_axis_restoration_fraction=0.15). The self-route to mech436_enrichment_insufficient_substrate_ceiling is CORRECT and reached by the honest path: all five non-vacuity preconditions MET -- contact 5/6, argmax-relevance pc_frac=1.0, OFF/bank-disabled floor 1.0 (hard zero), bank populated 1.0, enriched-spread MET (mean_drive_spread_max=0.192, per-seed 0.15-0.23, floor 0.1, lever (b) WORKING). Natural drive-coupled delta mean -0.037 +/- 0.188 (margin 0.188; per-seed [-0.333, 0.0, -0.150, 0.100, 0.200] -> 1/5 clears, 2/5 STRONGLY NEGATIVE), while overshoot (mag 5.0) still flips most_wanted on 4/5 guard-passing seeds (>= 2/3) -> enrichment insufficient, NOT a weakens. THE LOAD-BEARING NEW FINDING: the kappa-magnitude lever is EXHAUSTED as a monotone repair. Doubling kappa 6.0 -> 12.0 REGRESSED the natural delta rather than improving it (514s mean +0.064 / sd 0.109 / 2-of-5-clear -> 514t mean -0.037 / sd 0.188 / 1-of-5-clear, two seeds strongly negative). At kappa_eff=24 the drive term over-amplifies base_value and most_wanted -> argmax(per_axis_drive), flipping chaotically through a near-tie landscape that the argmax-flip-gated WL metric reads as sign-unstable noise. The "needs more kappa" hypothesis is FALSIFIED; the suspect is now the MEASUREMENT layer (flip-gated delta discards continuous sub-flip re-weighting AND interacts pathologically with high kappa). MECH-436 stays candidate / substrate_ceiling / pending_retest_after_substrate (UNCHANGED -- confirmed correct, NOT weakened, NOT promoted, NOT granularity debt: same signature as 514q/r/s, now with a falsified monotone-kappa lever, so NO /claim-synthesis). Route: /queue-experiment 514u measurement-redesign -- add a CONTINUOUS incentive-amplitude metric (drive's sub-flip shift of the wanting score toward the depleted axis) alongside the flip-gated delta, at a MODERATE kappa (toward 6.0; do NOT exceed 6.0, the 514s C8 bounded-kappa invariant). MECH-229 leg (a) wanting!=liking (V3-EXQ-514o PASS 0.80) UNAFFECTED. No demotion.

**Granularity-debt check.** 7th run / 5th autopsy circling MECH-436 (514q split, 514r, 514s, 514t). The recurrence trigger fires on a *different* failure signature each time; here the signature is the SAME (natural drive below the argmax-flip threshold vs real base_value), now extended by a falsified monotone-kappa lever -- convergent, not divergent. The /claim-synthesis split already resolved the granularity debt at 514q. **No further /claim-synthesis routing warranted** (consistent with the task instruction).

---

## 8. Routing decision the user confirmed

- **Verdict:** clean self-route; substrate-ceiling persists. `non_contributory` / `substrate_ceiling`. Not a weakens, not granularity debt.
- **MECH-436:** candidate / substrate_ceiling / pending_retest_after_substrate -- UNCHANGED.
- **Routing:** `/queue-experiment` 514u measurement-redesign (continuous incentive-amplitude metric at moderate kappa); the kappa-magnitude lever is exhausted, do NOT raise kappa again.
- **Supersession:** 514t supersedes 514s; governance sets `evidence_direction: superseded` on the 514s manifest.
- **substrate_queue:** amend SD-049-PHASE-2 with the 514t failure_record + kappa-exhausted / measurement-redesign note.
- **Indexing:** 514t landed AFTER the 2026-06-20T06:18Z pipeline index build, so its run_id is not yet in claim_evidence.v1.json. Governance must (a) set `evidence_direction: non_contributory` + `non_degenerate` is already true so the indexer marks it `scoring_excluded`, (b) add `v3_exq_514t_..._20260620T031416Z_v3` to review_tracker reviewed_run_ids, (c) rebuild the index so it enters claim_evidence.v1.json as scoring-excluded, (d) apply the 514s supersession.
- **MECH-229 leg (a):** untouched.

Analysis + handoff only -- governance applies the disposition to claims.yaml / substrate_queue / review_tracker.
