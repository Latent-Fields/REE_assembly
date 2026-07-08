# Failure Autopsy -- V3-EXQ-718a (SD-MEL-CONSUMER measured-MEL cadence re-validation)

- **Generated:** 2026-07-08T06:16:47Z
- **Scope:** single
- **Status:** confirmed (user gate 2026-07-08: diagnosis "Accept as stated"; routing "Bank capability + re-park ecological")
- **Run:** `v3_exq_718a_sdmelconsumer_measured_mel_cadence_validation_20260707T203329Z_v3`
- **Queue:** V3-EXQ-718a (experiment_purpose=diagnostic; supersedes V3-EXQ-718; PROMOTES NOTHING)
- **Claims:** INV-050 (three-drive sleep regulation; the learning/MEL drive sets overnight-update sufficiency), MECH-180 (novelty / high-MEL episodes adaptively upregulate the learning drive of sleep)
- **Outcome:** FAIL; self-routed `mel_control_degenerate`; `evidence_direction: non_contributory`
- **Adjudicated reading:** self-route MISLABELS the cause -> corrected to `mel_consumer_capable_ecological_novelty_not_graded`; non_contributory; NOT weakened, NOT cleared

---

## 1. Facts (no interpretation)

Test-bed redesign of V3-EXQ-718, routed from `failure_autopsy_V3-EXQ-718_2026-07-07`. 6 arms/seed x seeds 42/123/456:
`ARM_0_NONE_ON` / `ARM_1_LOW_ON` / `ARM_2_MED_ON` / `ARM_3_HIGH_ON` (4 graded-novelty ecological consumer-ON arms), `ARM_4_HIGH_OFF` (matched-novelty consumer-OFF pinned control), `ARM_5_INJECT_PC` (graded MEL injected by construction). DV = cumulative_sws_writes + rem_rollouts over 6 wake-sleep cycles.

- **Readiness R: PASS** (`readiness_frac 1.0`). Both preconditions met on all seeds: frozen-probe `conv_rel_drop` 0.973-0.984 (>= 0.10, `conv_frac 1.0`); injection-PC per-cycle DV monotone + spread (`inject_pc_frac 1.0`).
- **C1 (LOAD-BEARING: DV monotone non-decreasing in MEASURED per-arm mean MEL, on the 4 ecological ON arms sorted by measured MEL, >= 2/3 seeds): PASS 3/3 (`c1_frac 1.0`).**
  - seed 42: order NONE<MED<HIGH<LOW; mel `[2.59, 2.94, 3.35, 3.38]e-5`; DV `[56, 62, 72, 73]` -- monotone + spread OK.
  - seed 123: order MED<NONE<LOW<HIGH; mel `[1.44, 1.59, 1.76, 2.67]e-5`; DV `[82, 91, 100, 151]` -- monotone + spread OK.
  - seed 456: order HIGH<LOW<NONE<MED; mel `[3.69, 3.95, 3.98, 4.73]e-5`; DV `[74, 79, 80, 95]` -- monotone + spread OK.
- **C2 (control non-degeneracy, NOT load-bearing): FAIL 1/3 (`c2_frac 0.333`).** OFF arm `per_cycle_count_variance = 0.0` (pinned SWS=5/REM=10 -> dv_off_high = 90) on ALL seeds; `c2_pinned_ok = true` every seed. The failure is ENTIRELY the `on_gt_off` component: ARM_3_HIGH_ON DV > OFF DV only on seed 123 (151 > 90); seeds 42 (72 < 90) + 456 (74 < 90) fail.
- **C3 (injection positive control, capability, NOT load-bearing): PASS 3/3 (`inject_pc_frac 1.0`).** ARM_5 per-cycle DV `[9, 13, 18, 24, 30, 38]` (seed 42) exact-monotone-tracks injected `INJECT_LEVELS [0.6, 0.9, 1.2, 1.6, 2.0, 2.5]`; `factor_by_cycle` == the injected levels to 1e-15. Given cleanly-graded MEL, the consumer produces cleanly-graded offline duration.

**Which criterion failed:** the non-load-bearing C2, on `on_gt_off`, on 2/3 seeds. The load-bearing C1 PASSED. Readiness + C3 PASSED.

## 2. The self-route is a hypothesis, not a verdict -- and this one MISLABELS the cause

Self-route map (script lines 780-796): readiness met + NOT(C1 & C2) + NOT(C2 & !C1) -> `else` -> `mel_control_degenerate`. The `else` fires whenever `c2_pass` is False. The docstring (lines 110-111) defines that label as **"OFF control not pinned / not separated."**

The facts **refute** that meaning: `c2_pinned_ok = true` on all three seeds (`ARM_4_HIGH_OFF per_cycle_count_variance = 0.0` every seed). The OFF control is perfectly pinned and separated. C2 failed only on `on_gt_off`: the ecological HIGH arm's measured MEL sat at/below its calibrated reference, so the consumer scaled DV to <= the OFF baseline (90). The routing logic has no branch for "C1 passes but the ecological arms sit below reference so C2's on_gt_off fails," so it dumped the run into the wrong (degenerate-control) bucket.

**Corrected label:** `mel_consumer_capable_ecological_novelty_not_graded` -- the sibling branch, whose documented meaning (script lines 103-109) exactly matches the facts: the injection PC proves the consumer responds to graded MEL, so the ecological result means the foraging did not produce graded (above-reference) MEL -- a measurement/environment gap, NOT a substrate ceiling, NOT a falsification.

## 3. Claim-layer mapping

- **INV-050** -- `invariant`, `invariant_type: emergent`, `emergent_from: [SD-017]`; `candidate`; `pending_substrate_reconfirmation: true`; `pending_retest_after_substrate: true`; `epistemic_category: substrate_ceiling` (kept conservative by governance in the 718 cycle). UN-DEFERRED 2026-07-07 (user override); SD-MEL-CONSUMER minted + landed.
- **MECH-180** -- `mechanism_hypothesis`; `candidate`; `v3_pending: true`; `pending_retest_after_substrate: true`. `lit_conf 0.887` (Wilson & McNaughton 1994, Tononi & Cirelli 2003, Stickgold 2001, Louie & Wilson 2001) / `exp_conf 0`. Prior experimental evidence 677 (non_contributory + scheduler-pinned degenerate), 718 (non_contributory, novelty->MEL non-monotone).

**Did the test let the claims express?** Link (ii) MEL->cadence: yes, and it works (injection PC). Link (i) novelty->graded-above-reference-MEL: no -- the ecological arms did not produce a graded MEL gradient above the calibrated stable-base reference, so the end-to-end novelty-adaptive-cadence prediction could not be fairly tested.

## 4. Biological-reference triage

- **Closest mechanism:** novelty / prediction-error-driven upregulation of sleep pressure + consolidation intensity (Process S / synaptic-homeostasis; SWS power, spindle density, replay rate scaling with prior-day novelty + PE load). MECH-180's lit basis is strong and directly biological (not a formal import), `lit_conf 0.887`.
- **The REE translation is two mediated links:** (i) novelty -> waking MEL (mean per-step e3 prediction-error load); (ii) MEL -> offline-phase duration (SD-MEL-CONSUMER).
- **Does the failure match a missing-dependency signature?** Yes, and biologically legible: an agent whose world model has fully converged on a small environment has little residual learning-load to sleep off -- Process-S-from-learning would be flat. That is exactly what the ecological arms show (residual MEL ~1e-5, noise-dominated, scrambled vs novelty level). The gap is at link (i) / the environment, not at the consumer or the claim.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not tested end-to-end) | link (ii) works; link (i) not exercised -> the ecological claim was not fairly tested |
| Biological reference | clear | MECH-180 lit basis strong (0.887); mechanism class well-grounded; failure matches a converged-world / no-learning-load signature |
| Prerequisites | present | SD-MEL-CONSUMER built + landed + functional (ree-v3 main 909292c) |
| Implementation | complete | consumer LIVE: injection PC exact-tracks injected MEL; C1 monotone in measured MEL; OFF pinned |
| Environment | wrong pressures | CausalGridWorldV2 world model converges too completely (`conv_rel_drop ~0.98`, `probe_pe ~1e-4`); residual ecological MEL ~1e-5 noise-level; drift-novelty does not lift MEL above the stable-base reference; measured-MEL arm ordering SCRAMBLED vs intended novelty level on all 3 seeds |
| Measurement | misleading (self-route label) | `mel_control_degenerate` mislabels: OFF control IS pinned; C2 failed on `on_gt_off` because ecological MEL sat below reference. Separately, C1's PASS is NEAR-DEGENERATE -- DV is a deterministic monotone function of MEL (`factor = 1 + gain*(mel/ref - 1)`), so DV-monotone-in-measured-MEL is close to tautological and does NOT independently establish link (i) |
| Integration | coupled | consumer + scheduler correctly integrated (engages via SleepLoopManager.force_cycle + per-step update_residue) |
| Scale | adequate | 3 seeds x 6 cycles; DV small-integer quantisation adds monotonicity brittleness, secondary |

**Recommended `epistemic_category`:** measurement / environment (test-bed producer) gap -- **NOT substrate_ceiling** at the consumer, **NOT falsification**. (Governance may leave INV-050's stored `epistemic_category: substrate_ceiling` untouched, conservative, as in the 718 cycle; the note carries the environment-producer-gap framing either way.)

## 6. Consumer capability is PROVEN -- but it is a narrow, single-pathway positive

The injection PC (C3) is a clean, load-bearing capability existence proof: graded MEL injected by construction -> per-cycle DV `[9,13,18,24,30,38]` exact-monotone, all seeds. This validates the CONSUMER half of the mechanism (the thing SD-MEL-CONSUMER built provably works). **But it is a single-pathway (injection-only) positive:** it supports "the MEL consumer exists and translates graded MEL -> graded offline duration," NOT the full ecological invariant INV-050/MECH-180 assert (that real graded waking experience produces the graded MEL). It therefore does NOT clear `v3_pending` and does NOT count as ecological support. (Skill narrow-supports check: the only "support" here is the injection capability; the ecological pathway is not demonstrated -- no illusory conflict resolution.)

## 7. Re-derive brake (MOVE-3) -- FIRES

Prior `failure_autopsy_*.json` for the claims with recommended `substrate_ceiling` OR `non_contributory`:
- **INV-050: 5 prior** -- 701, 701a, 701b, 701c, 718 (all non_contributory). This run makes it the **6th**.
- **MECH-180: 2 prior** -- 677, 718. This run makes it the **3rd**.

Threshold = 2. The brake **FIRES**. But the named upstream substrate SD-MEL-CONSUMER is **already built + demonstrably functional** (the consumer half the brake's usual "build the substrate" remedy targets is done). The load-bearing consequence therefore falls on the REFUSAL clause:

- **REFUSE a same-environment ecological re-grade re-queue (a hypothetical V3-EXQ-718b).** Re-grading the novelty drift schedule on the SAME CausalGridWorldV2, SAME claim_ids, SAME ecological demonstration is "another letter circling the same ceiling" -- exactly the 7-12x lettered-iteration burn the brake exists to stop. This is the 6th consecutive non_contributory on INV-050's sleep-drive demonstration.
- The brake's mechanical `route_to: implement-substrate` remedy is **superseded by the user's 2026-07-08 disposition** (see Step 8): the consumer substrate is already built, and the remaining gap is an off-critical-path ENVIRONMENT producer demonstration that is not worth further compute now. Building a new graded-MEL environment substrate was offered and declined.

## 8. Repair pathway -- BANK capability + RE-PARK ecological (user disposition 2026-07-08)

User gate (2026-07-08): diagnosis "Accept as stated"; routing "Bank capability + re-park ecological (Recommended)".

- **Bank the consumer capability** as the terminal validated result of SD-MEL-CONSUMER: the injection PC proves the consumer translates graded MEL -> graded offline duration. SD-MEL-CONSUMER's build + consumer-level validation is COMPLETE.
- **Re-park the ecological end-to-end demonstration** (novelty -> graded above-reference MEL -> graded sleep). It is environment-blocked in CausalGridWorldV2 and off the V3 conversion-ceiling critical path. This mirrors INV-050's pre-2026-07-07 parked state; it is a deliberate defer, not undone work.
- **No new substrate build owed now.** A graded-MEL environment/test-bed (continual-shift / non-converging world that sustains a graded above-reference model-error gradient) is the ONLY untested route to an ecological demonstration, but it is explicitly deferred. If the ecological demonstration is ever un-parked, that environment substrate -- NOT another same-environment re-grade -- is the entry point.
- **No re-queue.** The brake refuses V3-EXQ-718b.

**Governance actions (this skill does NOT apply them):**
1. Apply the non_contributory `evidence_quality_note` (Step 9 draft) to INV-050 + MECH-180. Status UNCHANGED (both stay `candidate`; MECH-180 `v3_pending`; both `pending_retest_after_substrate`). NOT weakened, NOT cleared.
2. Amend `substrate_queue SD-MEL-CONSUMER`: append the 718a `failure_record` entry; record consumer-capability VALIDATED (injection PC) + ecological end-to-end RE-PARKED (user 2026-07-08); status may move `implemented_validation_owed` -> `implemented` (consumer validated; ecological demo re-parked, no build owed) per governance judgement.
3. Mark run `v3_exq_718a_..._20260707T203329Z_v3` reviewed (claim-tagged non_contributory).
4. Reconcile the plan-of-record: `sleep_substrate:GAP-5b` -> re-parked / no owed successor (the owner_exq chain 718 -> 718a terminates; no 718b).

## 9. Draft `evidence_quality_note` (governance to write; NOT written here)

**INV-050 / MECH-180 (shared):**
> V3-EXQ-718a (confirmed failure_autopsy_V3-EXQ-718a_2026-07-08; SD-MEL-CONSUMER measured-MEL cadence re-validation, diagnostic; supersedes 718) -> non_contributory + pending_retest_after_substrate (status UNCHANGED; MECH-180 v3_pending STAYS). The self-route label `mel_control_degenerate` is REFUTED: the OFF control IS pinned (per_cycle_count_variance 0.0, all seeds); C2 failed only on `on_gt_off` (ecological HIGH DV 72/74 < OFF baseline 90 on seeds 42/456). Corrected reading = `mel_consumer_capable_ecological_novelty_not_graded`. CONSUMER CAPABILITY PROVEN: the injection positive control (C3) shows graded MEL -> exact-monotone graded offline duration ([9,13,18,24,30,38] tracking [0.6..2.5], all seeds); C1 (DV monotone in MEASURED MEL) also passes but is near-degenerate (DV is a deterministic function of MEL). What FAILED is link (i): the ecological novelty arms did not produce a graded above-reference waking MEL gradient (measured MEL ~1e-5, noise-level, scrambled vs novelty level) because CausalGridWorldV2's world model converges too completely (conv_rel_drop ~0.98) to sustain ecological learning-load -- an environment/test-bed producer gap, same root as 718, NOT a substrate ceiling and NOT a falsification. NOT weakened (ecological claim not fairly tested; biology strong, lit_conf 0.887; consumer works), NOT cleared (injection capability is a narrow single-pathway positive; the ecological invariant is not demonstrated). Re-derive brake FIRES (6th non_contributory INV-050 / 3rd MECH-180) -> REFUSE a same-environment re-grade re-queue (V3-EXQ-718b). User disposition 2026-07-08: BANK the consumer capability as SD-MEL-CONSUMER's terminal validated result; RE-PARK the ecological end-to-end demonstration (off the V3 critical path; environment-blocked). No new substrate build owed now; if un-parked, a graded-MEL environment/test-bed (non-converging world) is the entry point, not another letter.

## 10. Routing summary

- **INV-050:** non_contributory; status unchanged; NOT weakened, NOT cleared; pending_retest_after_substrate stays. Consumer capability banked; ecological demonstration re-parked.
- **MECH-180:** non_contributory; status unchanged; `v3_pending` stays; NOT weakened, NOT cleared.
- **Substrate:** amend `SD-MEL-CONSUMER` -- append 718a failure record; consumer capability VALIDATED (injection PC); ecological end-to-end RE-PARKED (user 2026-07-08); NO new build owed. Re-derive brake refuses V3-EXQ-718b.
- **Experiment:** NONE. No re-queue (brake refuses same-environment re-grade).
- **Plan-of-record:** `sleep_substrate:GAP-5b` owner chain 718 -> 718a terminates; re-parked; no owed successor.
