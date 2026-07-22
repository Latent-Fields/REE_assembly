# Failure autopsy — V3-EXQ-794 (MECH-204 Phase 7 × SD-076 calibration loop 2×2)

**Scope:** single (two claims). **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z. **Promotes and demotes nothing.**

Run: `v3_exq_794_mech204_phase7_sd076_calibration_loop_2x2_20260721T113848Z_v3` ·
claims `[MECH-204, SD-076]` · purpose `diagnostic` ·
`supersedes v3_exq_774_mech173_rem_suppression_precision_calibration` ·
outcome **FAIL** · direction `inconclusive`
(`{SD-076: does_not_support, MECH-204: unknown}`) · self-route
`drift_source_insufficient_dv_still_tautological`.

---

## 1. Facts

Recording complete (`rec/v1`, `substrate_hash`, `machine_class`, `config`,
`seeds [0,1,2]`, `substrate_stable_across_run`). **No recording debt.**

Design: 2×2 ablation of **MECH-204 Phase 7 / Option B**
(`REEConfig.use_rem_precision_broadcast`, the *correction*) × **SD-076**
(`E3Config.use_waking_confidence_inflation`, the *drift source*), both landed
ree-v3 `8ac193d7ed` 2026-07-20. Both factors are ablated deliberately: a Phase-7-only
ablation would retest to an identical null that would read as a Phase-7 refutation
when nothing had been measured.

**The decisive numbers — every inflation arm is pinned at the same value.**

| Arm | `rv_final` | `overconfidence_score` | `calibration_ratio` |
|---|---|---|---|
| `ARM_OFF_OFF` | 0.005420 | −0.192123 | 1.2448 |
| `ARM_BCAST_ONLY` | 0.009832 | −0.507549 | 1.7999 |
| `ARM_INFL_LO` | **0.010000** | **−1.004111904519277** | **2.7564936387545953** |
| `ARM_INFL_HI` | **0.010000** | **−1.004111904519277** | **2.7564936387545953** |
| `ARM_BOTH_HI` | **0.010000** | **−1.004111904519277** | **2.7564936387545953** |
| `ARM_BOTH_LO` | **0.010000** | −1.004119469804949 | 2.756514046726147 |

`rv_final` is **exactly 0.010000** on all four inflation arms, and
`overconfidence_score` is **bit-identical to 15 significant figures** across LO, HI and
BOTH-HI. `arm_true_error_ref` is essentially constant across every arm
(0.003683–0.003700), so the denominator is not moving either.

Consequences recorded in the manifest itself:

- `per_arm_gate`: green `[ARM_OFF_OFF, ARM_BCAST_ONLY]`; **red**
  `[ARM_INFL_LO, ARM_BOTH_LO, ARM_INFL_HI, ARM_BOTH_HI]`, all failing
  `inflation_lowers_rv` (and BOTH_LO/BOTH_HI also `broadcast_moves_rv`).
- `criteria_non_degenerate`: `C1_inflation_creates_absolute_overconfidence` **false**,
  `C5_asymmetry_dose_response_monotone` **false**, `C2` **false**, `C3` **false**.
- `C1` (load-bearing): `n_seeds_overconfident` **0** at both LO and HI, min required 2.
- `C2` (load-bearing): `d_broadcast_under_drift_at_operative.per_seed` is **empty**,
  mean 0.0 — there was no operative drift level at which to evaluate the correction.
- `C4` (not load-bearing): **passed** — `ARM_OFF_OFF` at −0.192 reproduces 774's
  ceiling.

---

## 2. Adjudicating the direction — `does_not_support` is not earned

`rv_final` landing on **exactly 0.010000** on every inflation arm, with a bit-identical
DV at two nominally different asymmetry levels (LO and HI), is a **saturation
signature**, not a null. A genuine dose-response — even a null one — produces different
values at different doses with seed-level variance. Identical values to 15 significant
figures at two doses mean the quantity was clamped before the dose could express
itself. `arm_calibration_ratio` telling the same story (2.7564936387545953 at LO, HI
and BOTH-HI) confirms it is the *variable*, not the score function, that is pinned.

The manifest's own gate agrees: those four arms are **red**, their criteria are marked
`load_bearing: false` and `criteria_non_degenerate: false`, and the
`degeneracy_reason` states "Read the red arm(s) as unscored, NOT as a refutation."

**A run whose manipulation arms are all unscored has not tested the manipulation.**
`SD-076: does_not_support` therefore attributes to the claim a failure that belongs to
the implementation. It should be **`non_contributory`**.

`MECH-204: unknown` is **correct and stands.** C2 (does the broadcast correct
overconfidence under drift?) could not be evaluated at all — `per_seed` is empty
because C1 never established an operative drift level. MECH-204's correction was never
given anything to correct. The one MECH-204-relevant positive is C4: `ARM_OFF_OFF`
reproduces the 774 ceiling at −0.192, confirming the baseline regime is the one 774
diagnosed.

---

## 3. Claim-layer mapping

**SD-076** (`design_decision`, `candidate`, `depends_on [ARC-016]`, **empty**
`evidence_quality_note`, no prior autopsy). This is its first adjudication — and it
must not be its first `does_not_support`. Recommended direction:
**`non_contributory`**.

**MECH-204** (`mechanism_hypothesis`, `candidate`, `depends_on [MECH-123, MECH-186,
MECH-178, INV-045]`). Substrate implemented 2026-05-08 (SleepLoopManager WRITEBACK
consumer + F1 cross-cycle persistent zero-point EMA). Prior autopsies: 541 (2026-05-17,
`inconclusive_timescale`), 596-602 (2026-05-29), 606 (2026-05-29), 774 (2026-07-17,
`substrate_ceiling`). Direction `unknown` stands.

**Did the claims get a chance to express themselves?** SD-076: no — its lever ran into
a clamp. MECH-204: no — its correction had no drift to correct. Neither is falsified
by this run.

---

## 4. Biological-reference triage

**Closest mechanism:** REM-dependent recalibration of precision / confidence. The
waking-confidence-inflation source (SD-076) translates the well-evidenced observation
that confidence drifts upward during sustained waking (metacognitive overconfidence
under fatigue and sleep deprivation), and the Phase-7 broadcast (MECH-204) translates
REM-associated renormalisation of precision estimates via a cross-cycle zero-point.

**Dependencies:** a precision variable with genuine dynamic range on both sides of its
operating point, and a drift process slow relative to the recalibration cycle.

**Formal-definition import?** Partly — `running_variance` as a precision proxy is a
statistical import. The 774 autopsy already found the load-bearing consequence: the
**symmetric precision EMA makes `running_variance` track true prediction error by
construction**, pinning `overconfidence_score` near zero regardless of ablation (774
measured −0.000148 / −0.000918). The 794 design correctly moved the Phase-7 write-site
from E3-score space to precision space to escape the V3-EXQ-604c DV-invariance class.
That correction was right; it simply ran into a different wall.

**Does the failure resemble a missing-dependency signature?** Yes, and specifically:
biologically, confidence inflation is bounded by a *soft* saturating nonlinearity, not
a hard clip. A hard clamp at 0.01 with the variable pinned at the bound is an
engineering artefact with no biological analogue, and it destroys the dose-response the
design depends on.

**Lit status:** `partial` for MECH-204 (prior work exists in the 541/774 lineage); no
`targeted_review` for SD-076. A `/lit-pull` on **waking confidence drift dynamics and
its bounds** would inform whether the clamp should be raised or replaced with a
saturating nonlinearity — recorded as secondary.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested (both)** | SD-076's lever clamped; MECH-204's correction had no drift to correct. |
| Biological reference | **partial; divergence load-bearing** | Confidence drift is biologically bounded by a soft saturating nonlinearity; a hard clip at the operating bound is an engineering artefact that destroys the dose-response. |
| Prerequisites | **missing** | C2 requires an operative drift level, which C1 never established. |
| Implementation completeness | **partial — DOMINANT LAYER (SD-076)** | `rv_final` pinned at exactly 0.010000 on all four inflation arms with a bit-identical DV at two doses. Either the clamp sits at the operating point (no headroom), or the inflation acts with the wrong sign (the precondition is named `inflation_lowers_rv` and rv went **up** to the bound). |
| Environment adequacy | adequate | — |
| Measurement adequacy | **adequate — and it worked** | The per-arm gate, `criteria_non_degenerate` and the LO/HI dose contrast are exactly what exposed the saturation. Credit the 785-autopsy regime-conditioned gate pattern. |
| Integration adequacy | **coupled but unstable** | The 2×2 cannot resolve because one factor never varies. |
| Scale / capacity | **unknown** | n=3 seeds, but irrelevant while the arms are clamped. |

**Recommended `epistemic_category`: `competence_implementation_gap`.**
Explicitly **NOT** `substrate_ceiling` — recorded so neither MECH-204's nor SD-076's
brake count is inflated. (Note the contrast with 774, which *was* correctly a ceiling
reading about the symmetric EMA; 794 is a different failure at a different site.)

---

## 6. Learning extracted

1. **SD-076's `use_waking_confidence_inflation` has no usable headroom.** `rv_final` =
   exactly 0.010000 on all four inflation arms and `overconfidence_score` is
   bit-identical at LO and HI to 15 significant figures. The lever is pinned at a
   bound. Two candidate causes, both implementation-side and both cheap to check:
   **(a)** the clamp/upper bound on `running_variance` sits at or below the operating
   point, leaving no dynamic range; **(b)** the inflation has the wrong sign — the
   precondition is named `inflation_lowers_rv` and rv rose to the bound instead.
2. **A bit-identical DV across two nominally different doses is a saturation
   fingerprint and should be a standing lint.** Two dose levels producing the same
   value to 15 significant figures cannot be a null; it is a clamp. This is cheap to
   detect automatically (`per_level` values equal beyond float noise ⇒ refuse the
   dose-response criterion) and would have caught this without an autopsy. Related to
   but distinct from the existing `inert_arm_knob` lint (ree-v3 `c040d28`), which
   catches a declared-distinct arm pair that ran *identically* — here the arms ran
   with different knobs and produced identical output.
3. **The 785 per-arm gate pattern earned its keep.** Because the red arms were gated
   out rather than allowed to vacate the green ones, `ARM_OFF_OFF` and `ARM_BCAST_ONLY`
   remain scored and C4 could confirm the 774 ceiling reproduces (−0.192). Without it
   the whole run would have read as `precondition_unmet` and the C4 confirmation would
   have been lost.
4. **The Phase-7 write-site correction was right and is untouched by this failure.**
   Moving the broadcast from E3-score space to precision space escapes the V3-EXQ-604c
   DV-invariance class. That correction should not be revisited; only the drift source
   needs repair.
5. **Recording debt: none. The manifest contained its own diagnosis** — `per_arm_gate`,
   `criteria_non_degenerate`, `aggregates.arm_rv_final` and the LO/HI contrast were all
   recorded and are what made this adjudicable without a re-run.

---

## 7. Repair pathway

**Node classification:** `complicated (buildable)` — the fix is a named change (raise
or remove the clamp / correct the inflation sign) with no open scientific question.
Explicitly **not** `puzzle`: no spike is needed to learn what to build.

**Re-derive brake:** MECH-204 = **0** confirmed `substrate_ceiling` hits under R1–R3
across 5 autopsy targets; SD-076 = **0** (no prior targets). **Does not fire** for
either, and this autopsy adds no ceiling reading to either.

**Granularity-debt recurrence trigger: FIRES for MECH-204.** Five prior autopsy targets
across four files (541, 596-602, 606, 774) with differing signatures —
`inconclusive_timescale`, then a `substrate_ceiling` on the symmetric EMA, now an
implementation clamp on the paired drift source. Surfaced as a `/claim-synthesis`
recommendation on MECH-204 independent of this autopsy's own routing. **Does not fire
for SD-076** (first autopsy).

**Primary routing: `/implement-substrate`.**

`recommended_substrate_queue_entry.action = "create"`:

- `sd_id_suggested`: `sd_waking_confidence_inflation_headroom`
- **title**: Give SD-076 `use_waking_confidence_inflation` usable dynamic range —
  `running_variance` clamps at exactly 0.010000 on every inflation arm, pinning the
  DV bit-identically across dose levels
- **implementation_hint**: Determine whether the `running_variance` upper bound sits at
  or below the operating point (no headroom) or the inflation acts with the wrong sign
  (the precondition is `inflation_lowers_rv`; rv rose to the bound). Prefer a
  **saturating nonlinearity** over a hard clip — biologically, waking confidence drift
  is softly bounded, and a hard clip at the operating point destroys the dose-response
  the 2×2 design requires. Verify by asserting a strict LO≠HI separation in
  `rv_final` before the run is scored.
- **unblocks_claims**: `[SD-076, MECH-204]`
- **priority_suggested**: 2 (one fresh failure record; blocks 2 claims but neither is
  on a critical path)
- **failure_record_entry**: run `v3_exq_794_...`, metric "`rv_final` exactly 0.010000
  on all 4 inflation arms; `overconfidence_score` bit-identical (−1.004111904519277) at
  LO and HI; 0 of 3 seeds overconfident against a min of 2", target "strict LO≠HI
  separation in `rv_final` with `n_seeds_overconfident >= 2` at some level".

**Secondary:** after the substrate lands, `/queue-experiment` a same-question re-run
(**794a**) of the identical 2×2. Do **not** re-queue before then — the design is sound
and re-running it against the same clamp reproduces the same pinned arms.

**Secondary:** `/lit-pull` commission `targeted_review_sd_076_waking_confidence_drift`
on the dynamics and bounds of waking confidence drift, to inform the saturating-
nonlinearity choice.

### Draft `evidence_quality_note` — SD-076 (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-794, diagnostic, claim_ids=[MECH-204, SD-076];
> failure_autopsy_V3-EXQ-794_2026-07-22). **The recorded `does_not_support` for SD-076
> is WITHDRAWN and revised to `non_contributory` — SD-076 was never validly tested.**
> `running_variance` finished at **exactly 0.010000** on all four inflation arms and
> `overconfidence_score` was **bit-identical to 15 significant figures**
> (−1.004111904519277) at the LO and HI asymmetry levels, with `calibration_ratio`
> likewise identical (2.7564936387545953). Two nominally different doses producing the
> same value beyond float noise is a saturation signature, not a null: the variable was
> clamped before the dose could express itself. The manifest's own per-arm gate agrees —
> all four inflation arms are RED on `inflation_lowers_rv`, their criteria are marked
> `load_bearing: false` / `criteria_non_degenerate: false`, and the `degeneracy_reason`
> states "Read the red arm(s) as unscored, NOT as a refutation."
> `competence_implementation_gap`, explicitly NOT substrate_ceiling. Routed to
> `/implement-substrate` (`sd_waking_confidence_inflation_headroom`: raise or replace
> the hard clamp with a saturating nonlinearity, and check the inflation sign), then a
> same-question 794a re-run of the identical 2×2. SD-076 stays `candidate`;
> `pending_retest_after_substrate` set.

### Draft `evidence_quality_note` — MECH-204 (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-794, diagnostic, `unknown` — weights nothing;
> failure_autopsy_V3-EXQ-794_2026-07-22). Direction `unknown` **stands**. Phase 7 /
> Option B (`use_rem_precision_broadcast`) could not be evaluated: C2 asks whether the
> broadcast corrects overconfidence **under drift**, and
> `d_broadcast_under_drift_at_operative.per_seed` is **empty** because C1 never
> established an operative drift level — the SD-076 drift source clamped (see the
> SD-076 note). The correction had nothing to correct. Two positives are recorded and
> should not be lost: **C4 PASSED** — `ARM_OFF_OFF` at −0.192 reproduces the
> V3-EXQ-774 ceiling, confirming the baseline regime is the one 774 diagnosed — and the
> 794 design's relocation of the Phase-7 write-site from E3-score space to precision
> space correctly escapes the V3-EXQ-604c DV-invariance class and should not be
> revisited. `competence_implementation_gap` (upstream, in the paired drift source),
> explicitly NOT substrate_ceiling. MECH-204 stays `candidate`;
> `pending_retest_after_substrate` set, blocked on
> `sd_waking_confidence_inflation_headroom`. Granularity-debt recurrence fires (5 prior
> autopsy targets, differing signatures): routed to `/claim-synthesis`.

---

## 8. Frozen-ledger delta (Step 9b)

**None.** Neither MECH-204 nor SD-076 has a question in
`hypothesis_space_registry.v1.json`, and this autopsy emits no `fanout_recommendation`
— the bottleneck routes to a single unambiguous build, which is the documented
GOV-FANOUT-1 exemption. Nothing to pre-register; nothing to resolve.

## 9. Confirmed routing (user-adjudicated 2026-07-22)

User confirmed **"794: SD-076 `does_not_support` → `non_contributory`"**, with the
implementation-fix route.
