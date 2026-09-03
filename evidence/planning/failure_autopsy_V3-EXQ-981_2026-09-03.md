# Failure autopsy — V3-EXQ-981 (MECH-027 control-plane pathological modes)

**Generated:** 2026-09-03T20:04:14Z · **Scope:** single · **Status:** confirmed at the /failure-autopsy Step 8 interactive gate, 2026-09-03
**Claim:** MECH-027 — *"Pathological modes reflect mis-tuned control-plane regimes."* · **Machine-readable:** `failure_autopsy_V3-EXQ-981_2026-09-03.json`

---

## 1. Verdict up front

**The run's self-route to `substrate_not_ready_requeue` is CORRECT**, and this autopsy confirms it. Four of eleven readiness preconditions failed. MECH-027 was never tested and takes no weight — this is the first run ever to tag it (GOV-REUSE-1: 0/973 manifests at authoring time).

## 2. The replay channel was structurally dead — precise root cause

`mech285_n_draws` read **0 on every one of 75 firings per block in the BASELINE arm**, where replay was supposed to be *unsuppressed*. `replay_channel_baseline_reachable` therefore failed (0.0 against a ≥ 1.0 threshold).

The sampler was neither missing nor unimplemented:

- **Not missing.** A missing sampler would have recorded the driver's `-1` sentinel, not 0. It drew 50 times per firing and received `None` each time.
- **Not unimplemented.** MECH-285 is implemented and contract-tested.
- **The pool was empty.** `AnchorSet.all_with_dual_trace()` was always empty. The only live anchor-install path is `consume_boundary_events` → `write_anchor`, which runs only when `sense()` emits `BoundaryEvent`s, which requires `hippocampal.use_event_segmenter` — **default `False` at `ree_core/utils/config.py:2761`, and the driver never sets it.** The driver sets `latent.use_event_classifier`, a different flag on a different sub-config.

**The three-flag recipe is incomplete, and it has now propagated.** V3-EXQ-909 is cited as the reachability precedent, but 909 inherited `use_event_segmenter=True` from V3-EXQ-906b's config, and **909's own precondition measured the CONFIGURED knob** (`draws_per_cycle` 50.0, "structural, all seeds"), not measured draws. `use_anchor_sets` + `use_mech285_sampler` + `use_mech272_routing` are necessary but not sufficient; `use_event_segmenter` is the missing fourth.

## 3. The positive control failed with reversed sign

`positive_control_hazard_sensitivity` — baseline avoidant-action rate in the HIGH hazard band minus the SAFE band — measured **−0.4307** against a +0.05 floor, on all three seeds (−0.026, −0.476, −0.789). Baseline agents were markedly *more* avoidant in the safe band. The DV/env pairing is not hazard-sensitive, which invalidates anything built on top of it.

## 4. Three criteria were unreachable by construction

- **`C1_false_alarm_elevation`** set a threshold of 2 × 0.5771 = **1.1542 on a DV bounded in [0,1]** — unattainable by any value once the pooled baseline exceeded 0.5, which it did on all three seeds.
- **`precision_margin_norm_elevated_under_hv`**: the baseline pooled margin is 0.99980, so the arithmetic ceiling on the elevation is **0.000195 against a floor of 0.01 — 51x larger**. The measured 0.000194 is **99.4% of all available headroom**. The manipulation extracted essentially everything physically available and still missed by 51x.
- **`commit_temperature_reduced_under_hv`** is **algebraically the same quantity** read through a different sample filter (`T_eff = 1.0 + alpha·(1 − margin)`, alpha = 1.0) — not an independent check, and equally unreachable.

And **`C2` "passed" on a ratio of two negatives**: `pooled_recovered_fraction` = −0.04355 / −0.05198 = 0.8377. HV was *below* baseline, so there was no elevation to revert. Red-team F6 moved C2 from per-seed to pooled precisely to stop sign-flips; the pooled form has the identical pathology when the pooled elevation is negative.

A footnote worth keeping: `replay_channel_non_degenerate` "passed" vacuously at `measured == threshold == 0.0`. `p0_readiness_gate` applies the inclusive `m <= t` when no `comparator` key is present, and the measured quantity is a non-negative count pinned at 0 by construction — it could not have failed. Only its paired reachability check carried information.

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | untested | 4 of 11 preconditions failed; correct self-route |
| Biological reference | clear | hypervigilance as elevated precision / short horizon / suppressed consolidation |
| Prerequisites | **missing** | anchor pool empty — `use_event_segmenter` off |
| Implementation | partial | Builds 1 and 2 both engaged (commit temp on 75.4% of selections; 25 sleep firings/block) |
| Environment | wrong pressures | positive control reversed, −0.4307 |
| Measurement | misleading | three criteria unreachable by construction |
| Integration | partially coupled | consumer chain ran on an empty set |
| Scale | adequate | |

**Failure location (GOV-FAILLOC-1): MIXED** — emphatically not chargeable to REE. MECH-027 has never been tested.

## 6. Routing

**`/queue-experiment`** — re-queue as **V3-EXQ-981a** with three fixes, all of which must land together:

1. Set `hippocampal.use_event_segmenter = True` (a config correction, not a build — the flag already exists).
2. Re-derive `C1`'s threshold so it lies inside the DV's [0,1] range.
3. Establish a hazard-sensitive DV/env pairing **first** — the positive control must pass before anything is built on top of it.

**Substrate: `action: none`, deliberately.** The replay fix is a config correction; `substrate_queue` has no entry covering the empty-anchor-pool gap because there is no *missing* substrate (MECH-285/288/272 are all `implemented` with empty failure_records). The **saturation** half is already covered by the existing `MECH465-COMMIT-GATE-HEADROOM` entry (`pending_implementation`, ready, one open failure_record recording 25–48x below threshold) — registered against MECH-465 rather than MECH-027, and now independently re-hit here at 51x. Governance may wish to add this run to *that* entry's failure_record. The generalised lint is recommended once, from the V3-EXQ-993 target of `failure_autopsy_ext-claim-probe-cluster_2026-09-03`.

## 7. Learning extracted

1. **The V3-EXQ-909 three-flag replay recipe is incomplete** and has now propagated into a second driver. It needs `hippocampal.use_event_segmenter`, whose default is `False`. 909 itself never demonstrated measured draws.
2. **A precondition that measures a CONFIGURED knob is not a reachability check.** 909's read `draws_per_cycle = 50`; 981's read measured draws = 0 under the same nominal configuration.
3. A readiness check whose measured quantity is a non-negative count with threshold 0 and inclusive direction `upper` **cannot fail**. It is informative only when paired with a reachability check on the same instrument — as it was here.
4. **A multiplicative pass threshold (2x baseline) on a DV bounded in [0,1] is unattainable whenever the baseline exceeds 0.5** — a purely arithmetic error no amount of running can overcome, and one a static lint could catch.
5. Two preconditions can be **algebraically the same quantity wearing different names**, giving false reassurance of independent confirmation.

## 8. Read-across

This run supplies the two most extreme instances of the DV-headroom structural finding registered on the V3-EXQ-993 target of the EXT cluster artifact: a threshold outside a bounded DV's range, and a 51x shortfall against an arithmetic ceiling set by a saturated baseline. Whether `MECH465-COMMIT-GATE-HEADROOM` should be generalised, or the new lint should subsume it, is a governance decision — not adjudicated here.

## 9. Red-team pass

Cross-model adversarial review (Fable). Verdict: **CONFIRMED** — every load-bearing number recomputes, and the `use_event_segmenter` root cause verifies against source (default `False`, absent from 981's flags, present in 909's). One line-number error corrected (`config.py:2761`, not 2707).
