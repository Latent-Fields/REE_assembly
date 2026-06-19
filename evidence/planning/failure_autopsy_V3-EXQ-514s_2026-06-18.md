# Failure Autopsy — V3-EXQ-514s (MECH-436 drive-state-modulated wanting; SD-049-PHASE-2 drive-coupling RETEST)

- **Generated:** 2026-06-18T16:05:18Z
- **Run:** `v3_exq_514s_sd049_phase2_mech436_drive_coupling_retest_20260618T064933Z_v3`
- **Queue id:** V3-EXQ-514s (supersedes V3-EXQ-514r); machine ree-cloud-3
- **Outcome:** FAIL, self-routed `evidence_direction: non_contributory`, `non_degenerate: true`
- **Self-route:** `interpretation.label = mech436_enrichment_insufficient_substrate_ceiling`; `route_reason = natural_below_margin_overshoot_still_flips_retune_sd049_phase2_amend`
- **Claim under test:** MECH-436 (`drive.wanting_drive_state_modulation`, candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate). The drive-coupling leg (b) split out of MECH-229 2026-06-16. Leg (a) wanting≠liking object-bound dissociation (MECH-229, V3-EXQ-514o PASS 0.80) is NOT under test and NOT weakened.
- **Scope:** single (6th run in the 514 lineage: 514l/m/p/q/r/s; the /claim-synthesis split already happened at 514q)
- **Verdict (user-adjudicated 2026-06-18):** **Clean self-route; substrate-ceiling PERSISTS but is now demonstrably PARTIALLY LIFTED. `non_contributory` / `substrate_ceiling` (UNCHANGED). NOT a weakens, NOT granularity debt.** Route `/implement-substrate` amend on SD-049-PHASE-2 (raise `incentive_drive_kappa_scale` above 6.0, bounded; optionally deepen standing spread) → re-issue V3-EXQ-514t. MECH-436 disposition UNCHANGED (candidate / substrate_ceiling / pending_retest_after_substrate).

---

## 1. The pre-registered decision grid (514s arming the 514r-greenlit amend)

failure_autopsy_V3-EXQ-514r (confirmed) overturned 514r's self-route to genuine_weakens and greenlit two no-op-default levers, **kappa LOAD-BEARING**, both landed in ree-v3 2026-06-17:

- **(a) `GoalConfig.incentive_drive_kappa_scale`** — scales the effective drive→score coupling so a realistic per-axis drive spread competes with REAL object `base_value` gaps (514r found real in-run gaps on seeds 45/46/47 exceed 0.5, so even magnitude-5.0 drive could not flip them at the old kappa=1.0). 514s ran at `kappa_scale=6.0`.
- **(b) `CausalGridWorldV2.per_axis_restoration_fraction`** — partial restoration (514s used 0.3) + a divergent `per_axis_drive_decay` leaves STANDING per-axis drive on restored axes, so the spread survives to the WL scoring moment instead of being equalised to ~0.006 by full-restore-to-0 (the 514q defect).

514s re-runs the 514r controls (overshoot + OFF/bank-disabled + recalibrated argmax-relevance readiness) on the enriched substrate, plus a NEW non-vacuity precondition (`enriched_spread_met`). The decision grid (script lines 730–770):

| branch | precondition | outcome |
|---|---|---|
| any readiness gate unmet | contact / argmax-relevance / OFF-floor / bank / **enriched-spread** | `substrate_not_ready_requeue`, non_contributory, NEVER a weakens |
| **supports** | natural delta ≥ `max(K_SD·pstdev(δ), 0.15)` | MECH-436 substrate_ceiling → **supports** (load-bearing promotion path) |
| **substrate_ceiling** | natural < margin BUT overshoot flips ≥ 2/3 seeds | enrichment insufficient → retune amend. **NOT a weakens.** ← **514s landed here** |
| genuine_weakens | every readiness met AND overshoot CANNOT flip even at mag 5.0 | drive cannot carve wanting on the enriched substrate |

**514s reached the substrate_ceiling branch by the honest path:** all five non-vacuity preconditions passed first, then natural delta fell below margin while overshoot still flipped a supermajority. This is the script self-routing correctly — and the autopsy confirms the self-route rather than overturning it (unlike 514r).

---

## 2. Facts — non-vacuity first (all five preconditions MET)

`non_degenerate=true`; the natural-delta test was non-vacuous:

- **Contact guard:** 5/6 seeds (`guard_fraction=0.833`; seed 44 excluded). `contact_non_vacuity_met=true`.
- **Recalibrated argmax-relevance readiness — `pc_argmax_relevance_frac=1.0`.** Every guard-passing seed: overshoot flips a constructed realistic base_value gap while natural-magnitude drive does NOT (`pc_overshoot_flips=true`, `pc_natural_flips=false`). The overshoot magnitude is proven argmax-relevant.
- **OFF / bank-disabled floor — `off_floor_frac=1.0`.** `wl_off_floor_fraction=0.0` on every seed: bank bypassed → wanting==liking → zero dissociation, by construction. The non-zero natural/overshoot dissociation is genuinely bank-driven, not a comparator artifact. (Also bounds the kappa caveat: drive is not swamping liking — OFF floor is hard zero.)
- **Bank populated — `run_bank_populated_frac=1.0`** (`distinct_tokens_max=3` every seed; `n_scored_wl_steps_total=75`).
- **ENRICHED-SPREAD (NEW for 514s) — `enriched_spread_met=true`, frac 1.0.** `mean_drive_spread_max=0.211`; per-seed `[0.210, 0.231, 0.190, 0.233, 0.192]`, floor `MIN_ENRICHED_SPREAD=0.1`. **This is the decisive evidence the env amend WORKED** — the standing differential per-axis spread is now ~0.2 (vs 514q's equalised ~0.006), and it is argmax-relevant.

**Natural-magnitude drive delta (the supports gate):** `mean_wl_drive_delta=0.064`, `sd_wl_drive_delta=0.109` → `effect_margin = max(1.0·0.109, 0.15) = 0.15` → `C_WL_DRIVE_coupled_dissociation=false`. Per-seed `[-0.0667, 0.1765, 0.0, 0.2105, 0.0]` → **2/5 seeds (43: 0.176, 46: 0.211) individually clear the 0.15 margin; 3/5 (42: -0.067, 44: 0.0, 45: 0.0) sit at/below 0.**

**Overshoot (magnitude 5.0):** `per_seed_overshoot_flips=[T,T,T,T,F]` → 4/5 flip (`overshoot_seed_pass_frac=0.8` ≥ 2/3); `mean_overshoot_flip_fraction=0.747`.

**Failed criterion class:** discrimination (the supports gate). Negative-control / absolute criteria (OFF floor, bank, contact, enriched-spread, argmax-relevance) all PASS — the classic substrate-ceiling fingerprint, here with the substrate one calibration-step short of clearing the discrimination gate.

---

## 3. The decisive learning — the amend PARTIALLY worked

This is what distinguishes 514s from every prior run in the lineage, and is the load-bearing output of this autopsy:

| Run | per-axis spread at scoring | kappa_scale | natural delta | overshoot flips |
|---|---|---|---|---|
| 514q (06-16) | ~0.006 (equalised by full restore) | 1.0 | **exact 0.0** all 5 seeds | not run |
| 514r (06-17) | ~0 natural | 1.0 | 0.0 (one seed 0.111), mean 0.022 | 2/5 |
| **514s (06-18)** | **0.19–0.23 (standing, lever-b worked)** | **6.0** | **bimodal [0, 0.2]; 2/5 ≥ margin, mean 0.064** | **4/5** |

- **Lever (b) — standing differential depletion — SUCCEEDED.** `per_axis_restoration_fraction=0.3` + divergent decay produced an argmax-relevant standing spread (~0.2) on ALL seeds, fixing the 514q equalisation defect. `enriched_spread_met=1.0` is the direct evidence.
- **Natural coupling moved from structurally-zero to present-on-some-seeds.** 514q was byte-identical 0.0; 514s is bimodal — on 2/5 seeds natural-magnitude drive now carves at/above the margin. The mechanism is no longer inert at natural magnitude.
- **Overshoot rose 2/5 → 4/5** (kappa-scaling lifted the overshoot arm too).

**Why it still fails the gate — the residual shortfall is localized.** The WL-dissociation metric is **argmax-flip-gated**: the natural delta registers only when natural drive *flips* most_wanted against the real object `base_value` landscape. On 3/5 seeds, the real base_value gaps still exceed what `kappa_scale=6.0 × spread~0.2` overcomes at natural magnitude — only the ~25×-larger overshoot drive (5.0) flips there. So the gap is **the kappa-scaling lever (a): 6.0 is insufficient** — exactly the half 514r flagged as load-bearing. Lever (b) is done; lever (a) needs to go higher.

A secondary measurement subtlety: the argmax-flip-counter discards genuine *sub-flip continuous re-weighting* (drive shifting the wanting score toward the depleted axis without crossing the argmax boundary), which is itself genuine incentive-salience modulation. Surfaced as a fork (Section 7), but the user-confirmed primary route is the kappa amend.

---

## 4. Claim-layer mapping

- **MECH-436** (`drive.wanting_drive_state_modulation`, candidate, epistemic_category substrate_ceiling, v3_pending, pending_retest_after_substrate): asserts the homeostatic drive STATE re-weights most_wanted (`most_wanted = argmax base_value[k]·(1 + kappa·per_axis_drive[k])`). 514s tests this directly and lets it express — overshoot 4/5 + natural-clear 2/5 prove the channel carries and natural drive CAN carve on the seeds where base_value gaps are surmountable. The FAIL bears on amend MAGNITUDE (kappa), not on the claim.
- **MECH-229 leg (a)** (wanting≠liking object-bound dissociation, provisional; established V3-EXQ-514o PASS 0.80): NOT under test, NOT weakened. 514s `mean_object_bound_wl_dissoc_fraction=0.724` — consistent, not the load-bearing statistic. **PROTECT.** The hard-zero OFF floor (Section 2) additionally confirms drive is not swamping liking, so the kappa amend has not encroached on leg-(a).

`claim_ids=[MECH-436]` is correct and single — no inheritance error (the 514r-era `[MECH-229]` umbrella tag was already corrected at the split).

---

## 5. Biological-reference triage

- **Closest mechanism:** incentive salience as **drive/state-modulated cue attraction** (Berridge 2006; Smith/Berridge/Aldridge 2011 PNAS — DA stimulation amplified ONLY the incentive-salience component, dissociable from liking; DiFeliceantonio/Berridge 2016 — limbic activation dynamically + competitively amplifies cue attraction). Lit present (`targeted_review_connectome_mech_347`).
- **Formal import?** No — incentive salience IS drive/state-modulated cue attraction; the biology directly grounds the claim. The coupling gain kappa has no a-priori "correct" value, so scaling it so a realistic drive spread competes with object base_value is **legitimate substrate calibration, not p-hacking** — bounded by the constraint that drive must not *dominate* base_value (which would break leg-(a) wanting≠liking and lift the OFF floor off zero; both are currently honest).
- **Does the failure match a missing-dependency signature?** Yes, and now a PARTIALLY-FILLED one: the mechanism consumes a differential homeostatic-depletion signal scaled by kappa. The bimodal [0, 0.2] natural delta is the signature of "drive re-weights wanting mainly when options are close in base value" — biologically reasonable (incentive salience tips choice most when liking-values are near-equal). Brains remain an existence proof for the class → the default reading is a dependency/magnitude gap, NOT falsification. The overshoot control (4/5) confirms it.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | overshoot 4/5 + natural-clear 2/5 prove the channel carries and natural drive can carve where base_value gaps are surmountable; FAIL bears on kappa magnitude. Leg-(a) MECH-229 untouched. |
| Biological reference | clear | Berridge incentive salience; partial/bimodal expression matches "drive re-weights mainly when options are close in base value." |
| Prerequisites / dependency | **present (lever b) / partial (lever a)** | standing differential per-axis depletion now present (spread ~0.2, enriched_spread 1.0); residual shortfall is the kappa coupling gain (scale 6.0 short of real base_value gaps on 3/5 seeds). |
| Implementation | adequate | `most_wanted` responds; natural flips 2/5, overshoot 4/5; kappa=6.0 sub-threshold vs real base_value on 3/5. |
| Environment | **adequate (improved)** | the env amend produced the standing spread it was built for; no longer "too sparse" (the 514q defect is cured). |
| Measurement | adequate but **coarse** | WL dissociation is argmax-flip-gated → discards continuous sub-flip re-weighting that is itself genuine drive modulation. Fork in Section 7. |
| Integration | coupled | bank → most_wanted reached; overshoot + natural (2/5) move it. |
| Scale | adequate | 6 seeds, 75 scored WL steps. |

**Recommended `epistemic_category`: `substrate_ceiling` (UNCHANGED).** **Recommended `evidence_direction`: `non_contributory`** (scoring-excluded; `pending_retest_after_substrate: true`).

---

## 7. Repair pathway + routing (user-confirmed 2026-06-18)

**Routing: `/implement-substrate`** — `recommended_substrate_queue_entry.action = amend` on the existing `SD-049-PHASE-2` entry. This is the **2nd** failure record on the MECH-436 drive-coupling leg (after 514r), so amend (do not create a duplicate substrate entry).

- **Lever (a) is load-bearing and confirmed insufficient at 6.0.** Raise `incentive_drive_kappa_scale` above 6.0 so natural-magnitude drive × standing spread (~0.2) overcomes real object base_value gaps on a SUPERMAJORITY (≥ 2/3) of seeds, not just 2/5. **Bound it:** keep drive from *dominating* base_value — the promotion still requires NATURAL (not overshoot) drive to carve, the OFF floor must stay hard-zero, and leg-(a) wanting≠liking must remain intact. (A kappa so large that drive overrides liking would over-shoot the claim.)
- **Lever (b) is done** (spread ~0.2 met on all seeds); optionally deepen it further (`per_axis_restoration_fraction` below 0.3) only if raising kappa alone does not close the gap.
- **Re-issue V3-EXQ-514t** (the 514r overshoot + OFF + recalibrated-argmax-relevance + enriched-spread controls, on the higher-kappa substrate). Promotion target unchanged: natural delta `mean(WL_drive − WL_nodrive) ≥ max(k·pstdev(δ), 0.15)` on ≥ 2/3 seeds → MECH-436 substrate_ceiling → supports.

**Deferred measurement fork (NOT this cycle, per user):** a continuous incentive-amplitude metric (how far drive shifts the wanting score toward the depleted axis, even without flipping the argmax) alongside the flip-gated WL delta would capture sub-flip drive modulation the current metric discards. Recorded for a later iteration if the kappa amend stalls.

**Draft `evidence_quality_note` (for MECH-436; governance writes it):**

> 2026-06-18 (failure_autopsy_V3-EXQ-514s, confirmed): clean self-route; substrate-ceiling PARTIALLY LIFTED. 514s armed the 514r-greenlit SD-049-PHASE-2 amend (kappa_scale=6.0 + per_axis_restoration_fraction=0.3). The self-route to mech436_enrichment_insufficient_substrate_ceiling is CORRECT and reached by the honest path: all five non-vacuity preconditions MET — contact 5/6, argmax-relevance pc_frac=1.0, OFF/bank-disabled floor 1.0 (hard zero), bank populated 1.0, and the NEW enriched-spread precondition MET (mean_drive_spread_max=0.211, per-seed 0.19–0.23, floor 0.1) — proving lever (b) standing-differential-depletion WORKED (vs 514q's equalised ~0.006). Natural drive-coupled delta mean 0.064 < margin 0.15 (sd 0.109; per-seed [-0.067, 0.176, 0.0, 0.211, 0.0] → 2/5 clear the margin individually), while overshoot (mag 5.0) still flips most_wanted on 4/5 guard-passing seeds (≥2/3) → enrichment insufficient, NOT a weakens. The load-bearing new finding: the amend PARTIALLY worked — natural coupling moved from 514q's byte-identical 0.0 to a bimodal [0, 0.2] (present on 2/5 seeds), overshoot rose 2/5→4/5. The residual shortfall is localized to the kappa-scaling lever (a): the WL metric is argmax-flip-gated, and on 3/5 seeds the real object base_value gaps still exceed what kappa_scale=6.0 × standing-spread~0.2 overcomes at natural magnitude (only the ~25×-larger overshoot flips there). MECH-436 stays candidate / substrate_ceiling / pending_retest_after_substrate (UNCHANGED — confirmed correct, NOT weakened, NOT promoted, NOT granularity debt: same signature as 514q/514r, now partially mitigated, so NO /claim-synthesis). Route: /implement-substrate amend SD-049-PHASE-2 — raise incentive_drive_kappa_scale above 6.0 (bounded so drive does not swamp base_value: OFF floor stays 0, leg-(a) wanting≠liking intact), optionally deepen standing spread; re-issue V3-EXQ-514t. MECH-229 leg (a) wanting≠liking (V3-EXQ-514o PASS 0.80) UNAFFECTED. No demotion.

**Granularity-debt check.** 6th run / 3rd autopsy circling MECH-436 (514q split, 514r, 514s). The recurrence trigger fires on a *different* failure signature each time; here the signature is the SAME (natural drive below the argmax-flip threshold vs real base_value), now partially mitigated by a working env amend — convergent, not divergent. The /claim-synthesis split already resolved the granularity debt at 514q. **No further /claim-synthesis routing warranted** (consistent with the task instruction).

---

## 8. Routing decision the user confirmed

- **Verdict:** clean self-route; substrate-ceiling PARTIALLY lifted. `non_contributory` / `substrate_ceiling`. Not a weakens, not granularity debt.
- **MECH-436:** candidate / substrate_ceiling / pending_retest_after_substrate — UNCHANGED.
- **Routing:** `/implement-substrate` amend SD-049-PHASE-2 — raise `incentive_drive_kappa_scale` above 6.0 (bounded), optionally deepen standing spread; re-issue V3-EXQ-514t. Continuous-metric measurement fork deferred.
- **MECH-229 leg (a):** untouched.

Analysis + handoff only — governance applies the disposition to claims.yaml / substrate_queue / review_tracker.
