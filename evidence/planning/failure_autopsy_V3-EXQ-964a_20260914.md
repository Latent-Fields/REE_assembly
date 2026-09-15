# Failure autopsy -- V3-EXQ-964a (MECH-482 / SD-102 epistemic-deficit accumulator: multi-target readiness validation)

- **Status:** `confirmed` (staging mode -- headless session; routing NOT finalised)
- **Generated:** 2026-09-14T16:46:10Z
- **Run:** `v3_exq_964a_mech482_epistemic_deficit_multitarget_readiness_20260911T174949Z_v3`
- **Supersedes:** `V3-EXQ-964` (failure_autopsy_V3-EXQ-964_2026-08-30, confirmed)
- **Purpose:** `diagnostic`, `claim_ids: ["MECH-482"]`
- **Dry-run gate:** clean (`dry_run: false`; checked via `check_dry_run_citations.py`, 2 clean)
- **Recording:** `validate_recording.py` reports OK, no always-core gaps.
- **This artifact was revised after an independent adversarial red-team pass (Step 7c, VERDICT: CONTESTED).** The corrections are incorporated throughout; Section 4 records what changed and why.

## 1. Facts

| Criterion | Load-bearing | Measured | Threshold | Result |
|---|---|---|---|---|
| C1 multitarget regime reached | yes | 14.0 (min over seeds) | 2.0 | **PASS** |
| C2 readout differentiates | yes | 0.004422 (min over seeds) | 1e-12 | **PASS** |
| C3 downstream consumer can diverge | yes | 0.0 | 1e-9 | **FAIL** |
| C4 instrument control bit-identical | yes (negative control) | 0.0 | 1e-9 | **PASS** |
| C5 pre-readiness reproduces collapse | no (supporting) | 1.0 | <=1.0 | **PASS** |

Per-arm readiness gate: `all_green: true`. The magnitude-reachability precondition (`lp_perturbation_can_reach_argmax_margin`) is `applies: true` on ARM_READINESS only (it is scoped out, `applies: false`, on ARM_PREREADINESS) and read as `met: true` there. **Section 4 below shows this "met" reading is not informative** -- read that section before treating the readiness-gate PASS as license to call C3's zero "a real measurement."

Accumulator state, ARM_READINESS, all three seeds:

| Seed | `max_n_targets` | `max_lp_dev_range` | `n_margin_reads` | `n_zero_margin_ticks` | `n_flip_reachable_strict` | `max_pert_over_margin` | `min_argmax_margin` |
|---|---|---|---|---|---|---|---|
| 71 | 15 | 0.00734 | 34 | 2 | 0 | 0.0304 | **-4.1410** |
| 101 | 16 | 0.00442 | 55 | 4 | 0 | 0.1473 | **-1.3599** |
| 202 | 14 | 0.00612 | 28 | 4 | 0 | 0.2328 | **-1.1294** |

`ARM_PREREADINESS` (the reference/collapse control): `max_n_targets == 1` on all 3 seeds, confirming the OLD V3-EXQ-964 collapse is reproduced by the pre-readiness knobs alone. **`n_margin_reads`, `n_zero_margin_ticks`, `n_flip_reachable_strict` and `min_argmax_margin` are BYTE-IDENTICAL to the ARM_READINESS row above at every seed** (34/2/0/-4.1410, 55/4/0/-1.3599, 28/4/0/-1.1294) -- only `max_pert_over_margin` differs (exactly 0.0 on ARM_PREREADINESS, since its own perturbation is a constant shift). This identity is the basis of Section 4's finding.

## 2. The decisive finding -- the readiness build works; the downstream picture is unresolved, not merely "config-limited"

**C1 and C2 now pass non-arithmetically.** Unlike V3-EXQ-964 (where `n_targets == 1` forced a *constant* readout by construction), this run's `ARM_READINESS` reaches 14-16 persistent targets and a genuinely varying per-candidate readout (`max_lp_dev_range` 4.4e-3 to 7.3e-3, eight-plus orders above the 1e-12 floor). This closes exactly the gap V3-EXQ-964's autopsy named as the substrate blocker (`sd_epistemic_deficit_multitarget_readiness`), independently confirmed by C5's measured collapse control. **This part of the finding is unaffected by Section 4 and stands.**

**The committed action never moves, and -- after the Step 7c red-team pass -- the reason cannot yet be pinned on configuration.** Across all 3 seeds and 540 total yoked comparisons, `yoked_divergence_frac_max == 0.0`. This session's first-draft reading treated the magnitude-reachability precondition's PASS as evidence this was a genuine (if underpowered) test of C3, distinguishable from V3-EXQ-964's arithmetic zero, and recommended raising `curiosity_learning_progress_weight`. **An independent adversarial red-team pass overturned that reading; see Section 4.**

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | C1/C2/C5 real and non-arithmetic; whether MECH-482's mechanism was ever given a genuine chance to move the committed action in this run is UNRESOLVED (Section 4), not merely unsupported |
| Biological reference | partial | unchanged from V3-EXQ-964; the mechanism is still not behaviourally tested (committed action never moves) |
| Prerequisites | **NOW MET** | multitarget regime + non-constant readout both achieved, non-arithmetically, confirmed by the C5 collapse control |
| Implementation | complete (readiness geometry); DEFECTIVE one layer downstream | the magnitude-reachability instrument does not discriminate a flippable arm from a provably-unflippable one (Section 4) |
| Environment | adequate (readiness sub-question); untested (downstream-competition sub-question) | 3x60-step CausalGridWorldV2 cleared the multitarget floor with margin; whether a richer/longer environment changes the F-balance is untested |
| Measurement | **DEFECTIVE at the reachability-instrument layer** | see Section 4 -- the "reachable via tie" counter is arm-invariant and several counted "ties" are strictly negative margins |
| Integration | partially coupled | signal reaches the committed-selection layer (117 non-latched margin reads) but the apparent "near miss" is shown to be an instrument artifact |
| Scale | cannot yet be diagnosed as the limiting factor | without a working reachability instrument, "raise the weight/sample" is not yet a grounded prescription (Section 4) |

**Failure-location (GOV-FAILLOC-1).** This is a diagnostic substrate-readiness check, not an organism-level "REE failed" claim (the driver's own combination rule states this explicitly), so the REE-FAILED framing does not apply regardless of the rows below. Read narrowly: Implementation reads *complete* for the readiness geometry but *defective* for the reachability instrument; Measurement reads defective at the same layer. Net classification: **MIXED, with an open INSTRUMENT DEFECT at the reachability-gate layer that must be fixed before C3 can be adjudicated at all.**

## 4. Adversarial red-team pass (Step 7c) -- VERDICT: CONTESTED

An independent verifier (model: opus, different from this drafting session, which runs on Sonnet 5) was given the raw manifest, driver source and predecessor autopsy with this session's reasoning withheld, required to recompute load-bearing numbers from the manifest's own cells before reading this `.md`'s prose.

**Arithmetic: all clean.** Every stated number (max_n_targets, max_lp_dev_range, the 540/0 yoked comparisons, 117 margin reads, 10 zero-margin ticks, 0 strict, max_pert_over_margin 0.232751, 423 latched ticks) was independently recomputed from `arm_results[].accumulator` and matched exactly. No arithmetic defect.

**FINDING 1 (CONTESTING, confirmed by this session's own follow-up recompute) -- the magnitude-reachability gate's PASS is not evidence of reachability.**

1. **The predicate counts NEGATIVE margins as "ties."** Driver `v3_exq_964a_..._readiness.py:458`: `if fmargin <= 0.0:` (not `== 0.0`). `min_argmax_margin` for ARM_READINESS is **-4.141 / -1.360 / -1.129** across the three seeds -- strictly negative, not near-zero. Per `ree_core/predictors/e3_selector.py`'s `decisiveness_margin(arbitration_aware=True)` semantics, a negative value means the committed candidate was **not** the score argmin: either arbitration had already overridden the score-based choice (in which case perturbing the score cannot move the committed action -- the opposite of flippable), or `last_scores` is a pre-arbitration stale snapshot (in which case the margin describes the wrong quantity entirely). Either reading breaks the "genuinely reachable via tie-breaking" interpretation the artifact's first draft gave these ticks.
2. **The counter is BYTE-IDENTICAL on the arm where a flip is impossible by construction.** `n_margin_reads`, `n_flip_reachable_ticks`, `n_zero_margin_ticks` and `min_argmax_margin` are **exactly the same** on ARM_PREREADINESS as on ARM_READINESS at every seed (see the facts table in Section 1) -- even though the manifest's own `per_arm_gate.green[].scoped_out` note for ARM_PREREADINESS states its perturbation "cannot move an argmax at ANY magnitude," and its `max_pert_over_margin` is exactly 0.0 on every seed. A counter that returns the identical value on an arm structurally incapable of the thing it claims to measure is measuring something else -- almost certainly the base (F-only, pre-perturbation) arbitration state, which does not depend on the epistemic-deficit knobs that differ between the two arms at all.
3. **The predecessor autopsy named the fix, and this driver declined it without adjudicating the decision against this behaviour.** `failure_autopsy_V3-EXQ-964_2026-08-30.json`'s `learning_extracted[1]`: "A negative control establishes specificity, not sensitivity ... A positive control -- inject a synthetic two-target deficit and confirm the argmax flips -- would have made the zero interpretable in one cheap step." This driver's own docstring (lines 177-183) states: "NO VERIFY-LIFT ARM IS INCLUDED, deliberately ... The margin instrumentation above is the honest substitute: it MEASURES reachability per tick instead of manufacturing it." Findings 1 and 2 above show the substitute does not do that job, and the design contains no demonstration that the yoked-divergence detector CAN fire at all under any condition.

**Consequence:** the artifact's original framing of C3 as "a real measurement, not an arithmetic zero" is **not supported**. C1/C2/C5 realness is untouched and stands; only the C3-layer framing changes. Section 3's Measurement/Implementation/Scale rows, the `recommended_evidence_quality_note`, and the routing (Section 6) have all been revised accordingly.

**FINDING 2 (CONTESTING) -- the original "4-5x weight raise" sizing is fragile and contradicts the driver's own stated variability.** Sizing a weight multiplier off `max_pert_over_margin`'s single best tick per seed reaches parity on only 1 tick of 1 seed out of 117 margin reads (seed 202 needs ~4.3x; seed 101 needs ~6.8x; **seed 71 needs ~32.9x**). The driver's own docstring records a **22x** run-to-run swing in the underlying `lp_dev_range` statistic at fixed seed/config (measured on repeated dry-runs), and separately estimates **~1.7e3x** would be needed for parity from a smoke-scale measurement -- two to three orders of magnitude apart from a naive 4-5x extrapolation. The specific multiplier recommendation is withdrawn; Section 6 now asks for a corrected instrument and/or positive control before any weight is chosen at all.

**Attack surfaces checked and found CLEAN** (not re-litigated here): the re-derive-brake producer release (formally correct and substantively defensible; unaffected by Findings 1-2 since an instrument/test-design category is equally non-counting under R3); the driver-caveat over-extension question in principle (real in the abstract, but Finding 1 shows the run is materially the shortfall case the "configuration" remedy addresses, once grounded in the measured 0.233/strict-zero facts rather than the gate's formal pass); the `per_claim_recommendation.change` field's already-true-tail check (MECH-482 carries no stored `evidence_direction`, so `mixed -> non_contributory` is a genuine change); the `resolved` vs `superseded` verb on the prior failure_record item (correct as `resolved` -- something was fixed); aggregate-vs-cell contradictions (none beyond Finding 1's own arm-identity observation); GOV-FANOUT-1 applicability (correctly not invoked -- this is a single named fix, not a hypothesis discrimination).

**Minor hygiene fixes applied in this revision** (none rose to CONTESTED): `max_distinct_targets_matched == 0` on ARM_READINESS at every seed is now recorded and adjudicated as a diagnostic-only figure under `rbf_weighted` (the driver's own docstring lines 64-81 state the matched-mask is not consulted in that readout mode); the `resolved_note` now quotes the prior failure_record item's "(equivalently ...)" parenthetical verbatim rather than eliding it; the new failure_record_entry now carries `run_role: post_build`; the substrate_queue amend now suggests `status_phase: validation_pending`; Section 1's table no longer implies the magnitude gate was evaluated identically on both arms (it is scoped out on ARM_PREREADINESS); "zero-margin tie" terminology is now qualified with the negative-margin sub-case called out separately.

## 5. Learning extracted

- A substrate-readiness build can be genuinely validated (real, non-arithmetic C1/C2, confirmed by a measured collapse control) while the claim it was built to test still receives zero support -- these are two separable facts, and both must be recorded distinctly.
- **A reachability instrument that passes its own threshold is not evidence of reachability unless it is shown to discriminate a positive case from a case where reachability is impossible by construction.** Here the instrument returned byte-identical counts on the real arm and on a provably-inert control arm -- proof it was measuring an arm-invariant quantity, not the perturbation under test.
- A driver that declines a predecessor's recommended remedy (here, a positive control) should state what would falsify its substitute, not merely assert the substitute is more honest than a manufactured effect.
- Do not size a configuration fix off a single run's single extremum without checking it against the driver's own stated run-to-run variability -- here a 22x swing and a ~1.7e3x independent estimate were both available and both contradicted the naive sizing.
- F-dominance at the committed-selection layer resembles the "single-arena F-dominated selector" pattern already documented for other mechanisms (V3-EXQ-569g/684/700/709/710, which motivated the segregated-loop substrate `v4_loop_segregation`/ARC-110) -- but this autopsy does not yet claim MECH-482 has hit that ceiling, since the reachability instrument itself is not yet trustworthy.

## 6. Routing (proposed -- awaiting confirmation)

**`queue-experiment`** -- re-pose the readiness/selection-relevance question (new letter) with, in this priority order:

1. **A corrected reachability instrument**: the tie predicate should read `fmargin == 0.0` exactly (not `<= 0.0`), paired with an assertion that the differential perturbation on that exact tick is non-zero -- and/or a demonstrated positive control (a case, real or synthetic, where the instrument registers a genuine flip) before its "reachable" count is trusted again.
2. **A positive-control (verify-lift) arm**, per the predecessor autopsy's original recommendation: inject a synthetic deficit large enough to force a demonstrable argmax flip, confirming the yoked-divergence detector CAN fire at all under this harness.
3. Only once (1) or (2) is in place: a weight/sample adjustment informed by the corrected instrument's own readings -- NOT sized off this run's `max_pert_over_margin` alone, given the driver's own documented 22x run-to-run swing and ~1.7e3x smoke-based estimate.
4. Recording whether an observed yoked divergence coincides with a recorded reachable-tick, once the instrument itself is trustworthy.

**Re-derive brake: explicit producer release, not fired** (Section 4's findings do not change this -- an instrument/test-design reading is equally non-counting under the R3 convention). See the JSON artifact's `re_derive_brake` block for the full, red-team-updated reasoning.

**Substrate queue:** `amend` `sd_epistemic_deficit_multitarget_readiness` -- mark the ORIGINAL failure_record item (`v3_exq_964_...`) `resolved` (the multitarget-readiness gap it named is closed), suggest `status_phase: validation_pending`, and append a NEW open failure_record item naming the reachability-instrument defect this run surfaces.

## 7. Recommended per-claim disposition

**MECH-482** -- direction `non_contributory` (unchanged from V3-EXQ-964, but now for a third, distinct reason -- an unresolved instrument question, not a config shortfall); `epistemic_category` **stays** `substrate_conditional`; status **stays** `candidate`; `recommended_diagnostic_evidence_adjudicated: true`. What changes is the `evidence_quality_note`, which must record that the multitarget-readiness substrate build is validated (C1/C2 real) but that the reachability instrument meant to certify C3's zero as a genuine test was itself shown, by an independent red-team pass, to be uninformative -- so this remains non-contributory to MECH-482's own hypothesis pending a corrected instrument.

## Step 7b -- mechanical pre-routing checks

`autopsy_pre_routing_checks.py --json`: **`fire_count: 0`** (re-run after both `.json` and `.md` existed). No existing driver, substrate entry, or literature-absence claim conflicts with this artifact's recommendations.

---

**Human confirmation:** confirmed 2026-09-15T01:14:02Z at the /governance Step 2b walk (cycle governance-20260915) with the recommended dispositions; the staged status line above was `awaiting_human_confirmation`.
