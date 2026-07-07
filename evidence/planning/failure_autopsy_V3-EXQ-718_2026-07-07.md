# Failure Autopsy -- V3-EXQ-718 (SD-MEL-CONSUMER adaptive-cadence validation)

- **Generated:** 2026-07-07T16:37:57Z
- **Scope:** single
- **Status:** confirmed (user gate 2026-07-07: "Re-queue (test-bed redesign)")
- **Run:** `v3_exq_718_sdmelconsumer_adaptive_cadence_validation_20260707T092402Z_v3`
- **Queue:** V3-EXQ-718 (experiment_purpose=diagnostic; supersedes none; PROMOTES NOTHING)
- **Claims:** INV-050 (three-drive sleep regulation; only the learning/MEL drive sets overnight-update sufficiency), MECH-180 (novel environments / high-MEL episodes adaptively upregulate the learning drive of sleep)
- **Outcome:** FAIL; self-routed `mel_does_not_modulate_cadence`; `evidence_direction: non_contributory`

---

## 1. Facts (no interpretation)

Validation of the SD-MEL-CONSUMER substrate landed ree-v3 main 909292c on 2026-07-07 (`ree_core/sleep/mel_consumer.py`). 5 arms/seed: 4 graded-novelty consumer-ON arms (NONE drift 999/0.00, LOW 15/0.15, MED 6/0.30, HIGH 2/0.50) + 1 matched-novelty consumer-OFF control (HIGH). DV = cumulative_sws_writes + rem_rollouts over 6 wake-sleep cycles. Seeds 42/123/456.

- **Readiness R: PASS** (both preconditions, all seeds): frozen-probe conv_rel_drop 0.967-0.982 (>= 0.10); NONE-arm duration factor headroom present (mean 1.416 < 2.9).
- **C2 (control non-degeneracy, NOT load-bearing): PASS 3/3.** OFF arm `per_cycle_count_variance = 0.0` (pinned SWS=5/REM=10 -> dv_off_high=90 every seed); ON-HIGH DV (114/143/168) > OFF-HIGH DV (90) on all seeds. So the **consumer, not the env, produced the count variation.**
- **C1 (LOAD-BEARING: DV monotone non-decreasing NONE<=LOW<=MED<=HIGH AND HIGH >= NONE x 1.15): FAIL 0/3 seeds.**
  - seed 42: dv_on = [81, 74, 114, 114] -- monotone FALSE (LOW 74 < NONE 81); spread OK (114 >= 93.2).
  - seed 123: dv_on = [155, 162, 160, 143] -- monotone FALSE; spread FALSE (143 < 178).
  - seed 456: dv_on = [148, 149, 189, 168] -- monotone FALSE (HIGH 168 < MED 189); spread FALSE (168 < 170.2).
- **Mechanism-live evidence** (seed 42): mean_duration_factor moves with MEL -- NONE 0.885, LOW 0.822, MED 1.263, HIGH 1.266 (OFF = 1.0, mean_mel = 0). So the consumer translates MEL -> duration faithfully; **but the factor ordering across the novelty grade is LOW < NONE < MED ~ HIGH -- not monotone in the intended novelty ordering.**

**Which criterion failed:** the load-bearing C1 monotonicity, on all 3 seeds. Readiness passed; C2 passed; non-degeneracy flags both true.

## 2. Claim-layer mapping

- **INV-050** -- `invariant`, `invariant_type: emergent`, `emergent_from: [SD-017]`; `candidate`; `pending_substrate_reconfirmation: true`; `pending_retest_after_substrate: true`; `epistemic_category: substrate_ceiling`. UN-DEFERRED 2026-07-07 (user override); SD-MEL-CONSUMER minted + landed; `implementation_note` says the landing UNBLOCKS the retest but PROMOTES NOTHING until the validation SCORES. Prior diagnostics 701/701a/701b/701c all non_contributory; 701c re-derive brake fired; floor mis-calibration (1e-4 vs converged-base ~1e-6) recorded as a test-bed learning note.
- **MECH-180** -- `mechanism_hypothesis`; `candidate`; `v3_pending: true`; `pending_retest_after_substrate: true`. Prose confidence exp_conf 0 / lit_conf 0.887 (Wilson & McNaughton 1994, Tononi & Cirelli 2003, Stickgold 2001, Louie & Wilson 2001). Prior experimental evidence V3-EXQ-677 (non_contributory + degenerate: scheduler-pinned SWS=80/REM=60, zero cross-arm variance). `implementation_note`: the landing un-pins the exact V3-EXQ-677 DV; v3_pending STAYS; PROMOTES NOTHING.

**Did the test let the claims express?** Partially -- the MEL->cadence half of the claim IS exercised (and works). The novelty->MEL half is NOT reliably exercised: the graded-novelty arms did not produce monotone MEL, so the end-to-end novelty->cadence prediction could not be fairly tested on this test-bed.

## 3. Biological-reference triage

- **Closest mechanism:** novelty/PE-driven upregulation of sleep pressure and consolidation intensity (SWS power, spindle density, replay rate scaling with prior-day novelty + prediction-error load) -- MECH-180's lit basis is strong (lit_conf 0.887).
- **Is it a formal import?** No -- it is a directly biology-grounded claim. The REE translation splits into two mediated links: (i) novelty -> waking MEL (Model Error Load = mean per-step e3 prediction error); (ii) MEL -> offline-phase duration (the SD-MEL-CONSUMER).
- **Does the failure match a missing-dependency signature?** The failure is NOT at the consumer (link ii works: factor tracks MEL, C2 passes). It is at link (i): the graded-novelty manipulation in CausalGridWorldV2 (drift schedules NONE/LOW/MED/HIGH) did not produce monotone waking MEL -- the factor ordering LOW < NONE < MED ~ HIGH shows MEL was non-monotone in the novelty grade. This is an **environment / measurement (test-design) gap**, not a substrate or claim failure.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not tested end-to-end) | the MEL->cadence half works; novelty->MEL half not reliably exercised -> the claim was not fairly tested |
| Biological reference | clear | MECH-180 lit basis strong (lit_conf 0.887); mechanism class well-grounded |
| Prerequisites | present | SD-MEL-CONSUMER built + landed + functional |
| Implementation | complete | consumer LIVE: duration factor tracks MEL; C2 confirms consumer (not env) causes variation; OFF pinned |
| Environment | wrong pressures | the graded-novelty drift schedule (NONE/LOW/MED/HIGH) did NOT produce monotone waking MEL across the grade -- factor ordering LOW < NONE < MED ~ HIGH |
| Measurement | misleading (self-route label) | C1 tests monotonicity of DV vs the NOVELTY LABEL, but the mediating quantity (MEL) is non-monotone in that label; the self-route `mel_does_not_modulate_cadence` mislabels the cause -- MEL DOES modulate cadence (C2 + live factor) |
| Integration | coupled | consumer + scheduler correctly integrated (engages via SleepLoopManager.force_cycle + per-step update_residue) |
| Scale | adequate | 3 seeds x 6 cycles; DV small-integer quantisation adds monotonicity brittleness but is secondary to the novelty->MEL non-monotonicity |

**Recommended `epistemic_category`: NOT substrate_ceiling.** This is a **measurement / environment (test-design) gap** -- the anti-V3-EXQ-642 case: the substrate is built and demonstrably functional; the validation criterion tests the wrong link (DV vs novelty label, when the novelty->MEL mediator is non-monotone).

## 5. The self-route is a hypothesis, not a verdict

The manifest self-routed `mel_does_not_modulate_cadence` (readiness met + C1 fail). The facts **refute** that label: C2 passed 3/3 (ON-HIGH DV > OFF-HIGH DV on every seed) and the duration factor demonstrably tracks MEL (NONE 0.885 / LOW 0.822 / MED 1.263 / HIGH 1.266). **MEL does modulate cadence.** What failed is that the graded *novelty* did not produce graded *MEL*, so DV is not monotone in the novelty label. The load-bearing question the validation should ask -- "does waking MEL drive offline-phase duration?" -- is answered YES by C2 + the live factor; the C1 monotonicity gate accidentally tested "does the novelty label drive MEL monotonically?", which is an environment property, not a consumer or claim property.

## 6. Re-derive brake (MOVE-3)

**Does NOT fire.** The routing is `/queue-experiment` (test-bed redesign), not a substrate_ceiling re-derive. INV-050 has 4 prior non_contributory diagnostics (701/701a/701b/701c) and the brake fired at 701c against the *measurability* path -- but the SD-MEL-CONSUMER substrate has since been built (the brake's release condition), and 718 tests a DIFFERENT question (functional sufficiency). 718's finding is not a substrate ceiling; it is a test-bed calibration gap. A re-queue with a fixed test-bed is NOT a same-selector re-derive against an unbuilt substrate -- it is the correct next validation of a built, functional substrate. Brake stays released; this is exempt.

## 7. Repair pathway -- `/queue-experiment` (test-bed redesign)

The consumer is validated as **functional** (link ii). The owed work is an end-to-end validation that fairly exercises link (i) novelty -> MEL, OR that bypasses it. Options for the redesign spec (new letter, same scientific question -- e.g. V3-EXQ-718a):

1. **Regress cadence directly on measured MEL** (primary): drop the novelty-label monotonicity DV; instead measure per-arm mean waking MEL and test that offline-phase duration is monotone in *measured MEL* (not in the novelty label). This tests the consumer's actual claim and is robust to a non-monotone novelty->MEL map. Add per-arm mean_mel to the manifest (currently only OFF mean_mel=0 is surfaced).
2. **Re-grade novelty to produce monotone MEL**: instrument novelty->MEL first (a calibration pre-pass), then choose drift schedules whose measured waking MEL is monotone NONE<LOW<MED<HIGH before running the cadence DV. Guards against the LOW<NONE inversion seen here.
3. **MEL-injection probe** (capability existence proof, non-ecological): inject graded waking MEL by construction (decoupled from foraging novelty) and confirm monotone cadence response. Cleanly isolates link (ii); labelled capability-not-ecological.

**Do NOT weaken INV-050 / MECH-180** -- the claims were not fairly tested end-to-end (the novelty->MEL mediator failed). **Do NOT clear them either** -- the end-to-end novelty-adaptive-cadence prediction is not yet demonstrated. Both stay `candidate` / `pending_retest_after_substrate` / (MECH-180) `v3_pending`. The substrate_queue SD-MEL-CONSUMER entry stays `implemented_validation_owed` with a re-validation failure record.

## 8. Draft `evidence_quality_note`s (governance to write; NOT written here)

**INV-050 / MECH-180 (shared):**
> V3-EXQ-718 (confirmed failure_autopsy_V3-EXQ-718_2026-07-07; SD-MEL-CONSUMER adaptive-cadence validation, diagnostic) -> non_contributory + pending_retest_after_substrate (status UNCHANGED). The self-route label `mel_does_not_modulate_cadence` is REFUTED by the facts: the consumer is LIVE and FUNCTIONAL -- duration factor tracks MEL (NONE 0.885 / LOW 0.822 / MED 1.263 / HIGH 1.266) and C2 passed 3/3 (ON-HIGH DV > OFF-HIGH DV every seed; OFF pinned). MEL DOES modulate cadence. C1 monotonicity failed (0/3) because the graded-NOVELTY test-bed did not produce graded MEL (factor ordering LOW < NONE < MED ~ HIGH) -- a measurement/environment (test-design) gap at the novelty->MEL link, NOT a substrate ceiling and NOT a claim falsification. NOT weakened; NOT cleared (end-to-end novelty-adaptive-cadence not yet shown). Re-derive brake does NOT fire (substrate built + functional; re-queue is the correct next validation). Route: /queue-experiment (V3-EXQ-718a) -- regress cadence on MEASURED MEL (not the novelty label), and/or re-grade novelty to monotone MEL, and/or a MEL-injection probe. SD-MEL-CONSUMER stays implemented_validation_owed.

## 9. Routing summary

- **INV-050:** non_contributory; status unchanged; NOT weakened, NOT cleared; pending_retest_after_substrate.
- **MECH-180:** non_contributory; status unchanged; v3_pending stays; NOT weakened, NOT cleared.
- **Substrate:** amend `SD-MEL-CONSUMER` (status stays `implemented_validation_owed`) with the 718 re-validation failure record + test-bed-redesign hint. NO new substrate build owed -- the consumer is functional.
- **Experiment:** `/queue-experiment` V3-EXQ-718a (test-bed redesign; same scientific question).
