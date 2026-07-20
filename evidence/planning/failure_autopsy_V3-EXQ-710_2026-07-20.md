# Failure autopsy — V3-EXQ-710 (RE-ADJUDICATION)

**Generated** 2026-07-20T06:06Z · **Session** `xenodochial-yalow-6c788c` · **Status** confirmed (user-gated)
**Run** `v3_exq_710_disinhibitory_soft_competitive_settling_validation_20260703T112039Z_v3`
**Claims** MECH-140, MECH-450, MECH-439 · **Outcome** FAIL · **Manifest direction** `non_contributory` · `non_degenerate: true`

**Supersedes the finding of** [`failure_autopsy_V3-EXQ-710_2026-07-03.md`](failure_autopsy_V3-EXQ-710_2026-07-03.md)
(that autopsy's *readiness* adjudication stands; its *mechanistic finding* is withdrawn — see §5).

**Origin** [`hold_weighted_e3_readout_corpus_sweep_2026-07-20.md`](hold_weighted_e3_readout_corpus_sweep_2026-07-20.md) §4d
(REE_assembly `4ceb7d22f9`), itself commissioned by
[`failure_autopsy_V3-EXQ-699_2026-07-20.md`](failure_autopsy_V3-EXQ-699_2026-07-20.md) §11.1.

> **One line.** 710 carries two independent defects; the directional verdict they appear to threaten
> was already withdrawn seventeen days ago, so what they actually destroy is the *prior autopsy's own
> positive mechanistic finding* — and both defects trace to a single missing selector diagnostic.

---

## 1. What is NOT at stake (read this before §4d of the sweep)

The corpus sweep lists 710 under "Wholly disqualified findings" as
"`710` (**weakens MECH-140/MECH-450**)". That describes the **manifest self-route**, not live
governance state. The self-route was rejected on 2026-07-03:

- `claims.yaml` MECH-140 / MECH-450 / MECH-439 all carry `non_contributory` for this run.
- `claim_evidence.v1.json` L142295-142338 — three rows, `confidence: 0.0`, `scoring_excluded: non_contributory`.

**710 contributes zero numeric weight to any claim's confidence, and has since 2026-07-03.** No
directional verdict needs withdrawing. §4d's framing overstates the exposure; the real damage is
elsewhere and is described in §5.

## 2. Defect 1 — hold-weighted committed-class DV (CONFIRMED)

`experiments/v3_exq_710_disinhibitory_soft_competitive_settling_validation.py`:

```
:830   committed_class = int(action[0].argmax().item())      # select_action return value
:848   if is_p2:
:849       n_p2_ticks += 1
:850       committed_class_counts[committed_class] = committed_class_counts.get(committed_class, 0) + 1
```

`ree_core/agent.py:5430` returns the **held** action on `not ticks["e3_tick"]`, before `e3.select()`
is reached. The histogram is therefore weighted by hold duration (cadence default 10, varying 5-20
under MECH-093 arousal). The load-bearing `C1_intact_strict_above_off` is a `CONVERSION_MARGIN = 0.05`
nat margin on `committed_class_entropy_nats` — a **distribution-shape statistic**, DISQUALIFYING per
the 699/708 triage test. No diagnostics latch is touched, so `e3_diagnostics_staleness_lint` is
structurally blind (form-2 invisible to form-1).

### 2a. Correction to the sweep's headline asymmetry figure

The sweep attributes 710 "the worst arm exposure asymmetry in the corpus (**+152%**)". That figure is
**seed 45**, and seed 45 has `gapa_divergence: false` — it is **not a divergent seed and never enters
the C1 decision statistic** (`n_divergent_seeds = 3`; the deciding seeds are 42/44/46).

| seed | divergent | `A0_OFF` n_p2_ticks | `A1_INTACT` n_p2_ticks | spread | in C1? |
|---|---|---|---|---|---|
| 42 | yes | 1651 | 1830 | **+10.8%** | yes |
| 43 | yes | 19076 | 18390 | −3.6% | no (pool not div. on all arms) |
| 44 | yes | 2050 | 3254 | **+58.7%** | yes |
| 45 | **no** | 6903 | 2738 | **+152%** | **no** |
| 46 | yes | 2150 | 3312 | **+54.0%** | yes |
| 47 | yes | 5250 | 4405 | −16.1% | no |

**The disqualification stands regardless** — +54% to +59% on the deciding seeds is far outside the
arm-symmetric regime the 663 calibration bounds (that calibration bounds the defect *only* where arm
symmetry cancels it *and* the DV is a continuous magnitude; an entropy DV is excluded on the second
count alone). But the +152% belongs to a seed that does not decide anything, and the sweep's §4d
should be corrected so the entry is not later read as over-called.

**C1 margins on the deciding seeds** (margin 0.05): seed 42 clears by **+0.0213**; seed 44 shortfall
**0.2194**; seed 46 shortfall **0.2033**. 1/3.

## 3. Defect 2 — the ablation control is a sanity check mislabelled as a dissociation

`A0_OFF` and `A2_ABLATED` are **bit-identical on all six seeds** — identical `committed_class_entropy_nats`
*and* identical `n_p2_ticks`:

| seed | `A0_OFF` entropy | `A2_ABLATED` entropy | `A1_INTACT` entropy | A2 round_delta | A1 round_delta |
|---|---|---|---|---|---|
| 42 | 1.341800 | **1.341800** | 1.413118 | 10.070 | 5.244 |
| 43 | 0.687069 | **0.687069** | 0.695610 | — | — |
| 44 | 1.053432 | **1.053432** | 0.884071 | 9.361 | 8.011 |
| 45 | 0.938445 | **0.938445** | 1.101230 | 9.892 | 7.452 |
| 46 | 0.996082 | **0.996082** | 0.842767 | — | — |
| 47 | 0.479347 | **0.479347** | 0.686846 | — | — |

So `C2_intact_strict_above_ablated` is **numerically the same test as C1**, and the intended MECH-450
structural-edge dissociation **was never measured at all**.

**But the sharper statement is that this was analytically forced, not an accident.** `A2_ABLATED` sets
`scs_cross_class = 1.0` — a uniform kernel. A uniform kernel adds a constant across all eligible
candidates: rank-preserving, hence invisible to an `argmax` readout, *whatever the field does*. And
the field does plenty: **A2's round_delta (9.4-10.1) is consistently HIGHER than A1's (5.2-8.0)**.

The manifest's own diagnostic block says exactly this:

> `a2_ablated_rank_preserving_diagnostic.note`: "A2 uniform kernel is rank-preserving -> A2 entropy
> should be ~<= A1 entropy. `a2_unexpectedly_reordered` True means the uniform kernel reordered beyond
> the `A2_REORDER_FLAG_SLACK` slack (**a substrate anomaly to inspect, NOT a** [test])"

**`A2_ABLATED` is a rank-preservation sanity control that the criterion set mislabels as an ablation
dissociation.** C2 had zero statistical power *by construction* and could not have failed. That it was
marked `load_bearing: false` shows the design half-recognised this; that it was nonetheless
pre-registered as "C2 tests the structured-edge is load-bearing (PLOS ablation signature)" is the
defect. This is the 699 §11.6 tell — two nominally independent readouts agreeing exactly is a defect
signature, not a validation — and **it survives a DV repair**: correcting the entropy accumulation
leaves A2 exactly as rank-preserving as before.

## 4. Root cause — both defects are one missing selector diagnostic

The manifest concedes it:

> `reorder_rate_limitation_note`: "the selector does NOT expose the pre-settle within-eligible argmin
> as a running diagnostic, so a literal per-tick 'committed winner != one-shot argmin' reorder rate
> cannot be recorded in-run... the behavioural reorder is read at the DV level (A1 vs A0)"

That single gap produced **both** defects:

- it forced the DV to be a **hold-weighted per-env-step histogram** instead of a per-E3-tick statistic → defect 1;
- it forced the structural edge to be read as an **arm contrast** instead of a direct rank-change measurement → defect 2 (and the arm chosen for that contrast is analytically null).

**A per-E3-tick reorder rate would have been immune to both.** It is fresh-selection-gated by
construction (computed only where `e3.select()` runs, so hold duration cannot weight it), and it
measures the structured kernel's effect on the committed winner *directly* — requiring no ablation arm
at all, and therefore no rank-preserving-arm trap. This is why the routing in §8 is a build, not a
redesign: the redesign is not available until the readout exists.

## 5. What the defects actually destroy — the prior autopsy's finding, not the self-route

The 2026-07-03 autopsy correctly rejected the `weakens` self-route on **wrong-locus** grounds
(disinhibition is a between-loop channel deployed at a single F-collapsed selector). That structural
reading is independent of how entropy was counted and **stands**.

What does **not** stand is its *positive mechanistic finding*, which it used to make 710 load-bearing:

> "over an F-collapsed field graded lateral inhibition **SHARPENS the F-winner** rather than
> diversifying" — evidenced by "committed-class entropy REDUCED (seed44 −0.169, seed46 −0.153 nats);
> over the 3 divergent seeds INTACT (1.047) is BELOW OFF (1.130)"

Every number in that sentence is the contaminated DV. The "sharpens F" reading is what made 710 *"a
THIRD structurally-different conversion mechanism"* corroborating the single-arena ceiling, and it has
no valid instrument. Likewise the prior autopsy's use of the A2 bit-identity to license *"the
STRUCTURED class-surround kernel is the sole active ingredient"* — that inference's only informative
half (A1 vs A0) is the contaminated one.

**Consequence: 710's ceiling CORROBORATION is withdrawn, not merely its self-routed weakens.** The
direction of travel is the opposite of what §4d implies — the re-derive brake **decrements** rather
than fires (§7).

### 5a. What survives (threshold-invariant → SAFE per the 699/708 triage)

| Readout | Value | Why SAFE |
|---|---|---|
| `settling_field_moved` | A1 round_delta 5.24-8.01 vs A0 **exactly 0.0** | exact-zero baseline; duplication cannot manufacture a positive from an all-zero record |
| `eligible_set_non_degenerate` / `f_elig_frac_excluded_gt0` | **exactly 1.0**, all 6 seeds (floor 0.05) | saturated ratio, nowhere to move |
| `frac_pre_ge2` | **exactly 1.0**, all 6 seeds | saturated |
| A2 ≡ A0 **exact identity** under round_delta ~10 | bit-identical on all 6 | exact-identity reading; replication cannot manufacture or break bit-equality |
| `crf_matured`, `learning_engaged` | true | readiness battery, threshold-invariant |

Note the fourth row is a **genuine positive implementation finding and it is not withdrawn**: the
soft-competitive settling machinery is BUILT, LIVE, moves the field hard (round_delta ~10), and
provably preserves rank under a flat kernel with no side-effects or stray RNG draws. That is
non-trivial and worth keeping. What it does *not* buy is a dissociation.

**Verdict split — readiness INTACT, finding WITHDRAWN** (the 699 precedent, adjudicated separately).

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (was: not-fairly-tested) | the wrong-locus reading stands on structural grounds, but the evidence that *demonstrated* it (entropy reduction) is invalid. No claim fairly tested, and now none fairly *diagnosed* either. |
| Biological reference | clear | unchanged from 2026-07-03: VIP→SOM disinhibition (Keller 2020 necessary+sufficient; Rungratsameetaweemana/Aquino PLOS Biology 2026) is a faithful primitive; `lit_status: present`, not a formal import. |
| Prerequisites | missing | segregated loops with differentiated value absent (`use_loop_segregation=False` on all arms). Unchanged and independent of the defects. |
| Implementation | **complete** (upgraded) | the settling step is built and demonstrably live+rank-faithful — this is the one layer the defects *strengthen* confidence in. |
| Environment | wrong pressures | single F-dominated arena. Unchanged. |
| **Measurement** | **misleading** (was: "adequate (a win)") | the dominant layer. The 2026-07-03 autopsy scored measurement as an internal-validity **win**; both of its cited wins are defective — the DV is hold-weighted, and the A2 control is analytically null. |
| Integration | isolated | unchanged. |
| Scale | n/a | mechanism engaged fully. |

**Dominant diagnosis layer: measurement.** Recommended `epistemic_category`: **`measurement_invalid`**
(was `substrate_ceiling`) — the ceiling reading is not *refuted*, it is *unevidenced by this run*.

## 7. Re-derive brake — DECREMENTS, does not fire

This is a **re-adjudication of the same run**, not a new experiment. Counting it as a fresh hit would
double-count one run. Withdrawing 710's ceiling reading removes its hit from every count:

| Claim | Prior count (incl. 710) | After withdrawal | Same-arena re-letter still refused? |
|---|---|---|---|
| MECH-140 | 1 | **0** | **No** — the refusal now has no autopsy basis on this claim |
| MECH-450 | 5 | **4** | Yes, on the 700-lineage's independent grounds |
| MECH-439 | 11 | **10** | Yes, amply |

`re_derive_brake.fired: false` on this target, with `decrements: true`.

## 8. Routing — `implement-substrate` on selector instrumentation

Work-graph class: **`complicated (buildable)`** — a named build with no open question. Do not queue a
spike to re-confirm what is already known how to build.

**Build:** latch the **pre-settle within-eligible argmin** in `ree_core/predictors/e3_selector.py` as a
per-`select()` diagnostic, exposing a fresh-selection-gated `reorder_rate` (`committed winner !=
one-shot argmin`) plus per-select committed-class counts. Fresh-selection-gated by construction ⇒
immune to defect 1; direct rank-change measurement ⇒ removes the need for an ablation arm, hence
immune to defect 2.

**Explicitly NOT routed:** a same-claim single-arena re-letter (`710a`). Refused for MECH-450/MECH-439
on the standing brake, and pointless for all three until the readout exists — a corrected-DV re-run
without the latch reproduces defect 2 unchanged.

Blast radius beyond 710: every settling/conversion experiment reading committed-class distributions off
`select_action` inherits this instrument. The build is a corpus-level fix, which is why it outranks a
per-experiment redesign.

## 9. Illusory-conflict check (mandatory)

**GOV-CEIL-1 / MECH-439 ceiling-exhaustion demotion (2026-07-09).** Cites 10 hits
(689a/700/700a/700b/700c/700d/709/**710**/711/713). Withdrawing 710 → **9**. `CEILING_EXHAUSTION_N = 3`
(`scripts/check_substrate_ceiling_audit.py:107`). **The demotion STANDS** — no reversal owed, and the
co-equally-carried null reading (F-dominance is inert) is untouched. Governance should correct the
count to 9 and drop 710 from the named list in both `ceiling_routing_note` and `evidence_quality_note`,
pointing at this autopsy.

*Residual, flagged not resolved:* the sweep also disqualifies conversion legs in **711** and **713**,
and both are among the surviving 9. The 9 may itself be an overcount pending their re-adjudication.
This does not threaten the demotion (the margin to 3 is large) but the note should not imply 9 is final.

**MECH-140 — the real casualty.** 710 is its **sole** evidence row (`live_status.evidence.from =
failure_autopsy_V3-EXQ-710_2026-07-03`; `evidence: []`). Withdrawal leaves it with **zero valid
experimental evidence**, reverting it to lit-only (`lit_conf 0.695`, Keller 2020 / Aquino 2026).
Per the user gate: **`epistemic_category` drops `substrate_ceiling` → `standard`** — the ceiling
category was earned solely by the withdrawn reading; an untested claim is not a ceiling-blocked one.
Status stays `candidate`; `pending_retest_after_substrate` stays true; **promotes nothing**, and this
is emphatically **not** a demotion — MECH-140 is strong-lit / untested, the
novel-discovery-adjacent quadrant, *not* under-supported. `lit_conf` and `exp_conf` stay unblended.

**Narrow-supports check.** The 2026-07-03 autopsy set `narrow_supports_flag: true` on MECH-439 (single
pathway, single-arena corroboration only). Withdrawal removes a *narrow* support, not a broad one —
so it cannot create illusory conflict resolution in the other direction. The remaining MECH-439
supports are unchanged and were already flagged narrow.

**Data-integrity gap found in passing (not fixed here).** MECH-140's `evidence_quality_note` asserts
the claim "carries `hold_candidate_resolve_conflict`", but that hold exists **only as prose inside the
note**. Elsewhere in `claims.yaml` (~25 claims) the hold is a structured
`live_status.evidence.verdict: hold_candidate_resolve_conflict/applied`; MECH-140's `live_status.evidence.verdict`
is instead `non_contributory/substrate_ceiling`. The hold is therefore invisible to
`validate_claims.py`, the governance audit and the explorer. Flagged for governance.

## 10. Learning extracted

1. **A rank-preserving ablation arm is not an ablation.** Ablating a rank-based readout with a
   rank-preserving perturbation is analytically guaranteed null — zero power, cannot fail. Where an
   arm is *designed* rank-preserving (as A2's own diagnostic note declares), it is an **implementation
   sanity control** and must never be pre-registered as a dissociation criterion. Generalises past 710:
   check every ablation arm for whether its perturbation can, in principle, move the readout.
2. **The same number can be a validity win and a vacuity tell, about different things.** A2 ≡ A0 proves
   the settling machinery is side-effect-free and rank-faithful (real, keep it) *and* proves C2 is not a
   test (withdraw it). The 2026-07-03 autopsy scored only the first and inherited the second. Adjudicate
   what a control licenses, not just whether it behaved.
3. **A defect can destroy an autopsy's finding without touching the verdict it overrode.** 710's
   `weakens` was already dead; the casualty was the *diagnostic* reading that replaced it. When
   re-adjudicating a run that has a prior confirmed autopsy, check the autopsy's evidentiary basis
   separately from the manifest's — they can fail independently.
4. **A recording-limitation note in a manifest is a routing signal, not a footnote.** 710's
   `reorder_rate_limitation_note` names the exact missing readout that caused both defects, and it was
   written *at run time* — the information needed to prevent this was present and disclosed 17 days
   before the sweep found the defects. Treat a self-disclosed "we could not record X, so we read it at
   the DV level instead" as a first-class instrumentation finding at review time.
5. **Corpus-sweep headline statistics need per-seed attribution before they anchor a verdict.** 710's
   +152% belongs to a non-divergent seed excluded from the decision statistic; the deciding seeds run
   +11%/+59%/+54%. The disqualification survives, but a figure that does not enter the criterion should
   not be the figure quoted for it.
6. **When one instrumentation gap causes defects in two nominally independent criteria, fix the
   instrument, not the criteria.** Both of 710's defects are downstream of one absent selector
   diagnostic; a corrected-DV re-run repairs one and reproduces the other.

## 11. Draft `evidence_quality_note` text for governance

> **MECH-140 / MECH-450 / MECH-439 — append:**
>
> RE-ADJUDICATION 2026-07-20 (confirmed `failure_autopsy_V3-EXQ-710_2026-07-20`, user-gated): V3-EXQ-710
> carries TWO independent instrument defects and its 2026-07-03 ceiling CORROBORATION is WITHDRAWN
> (the 2026-07-03 rejection of the manifest's `weakens` self-route STANDS and is unaffected — that
> self-route has carried `confidence 0.0 / scoring_excluded` since 2026-07-03, so no directional weight
> changes). DEFECT 1: the load-bearing `C1_intact_strict_above_off` (0.05-nat margin on
> `committed_class_entropy_nats`) is accumulated per ENV STEP off the `select_action` return
> (`v3_exq_710_...py:830,848-852`), which `ree_core/agent.py:5430` returns HELD on non-E3 ticks — so the
> histogram is hold-weighted. A distribution-shape statistic is DISQUALIFYING per the 699/708 triage;
> arm exposure spread on the three DECIDING seeds is +11%/+59%/+54% (the corpus sweep's +152% headline is
> seed 45, which is NON-divergent and does not enter C1 — sweep §4d to be corrected), far outside the
> arm-symmetric regime the 663 calibration bounds. DEFECT 2 (survives a DV repair): `A2_ABLATED`
> (`scs_cross_class=1.0`, uniform kernel) is BIT-IDENTICAL to `A0_OFF` on all 6 seeds in entropy AND
> `n_p2_ticks`, so `C2` is numerically identical to `C1` and the intended MECH-450 structural-edge
> dissociation WAS NEVER MEASURED. This was analytically forced: a uniform kernel is rank-preserving and
> therefore invisible to an argmax readout whatever the field does (A2 round_delta 9.4-10.1, HIGHER than
> A1's 5.2-8.0) — the manifest's own `a2_ablated_rank_preserving_diagnostic` declares A2 rank-preserving
> by construction and calls reordering "a substrate anomaly to inspect, NOT a [test]". A2 is an
> IMPLEMENTATION SANITY CONTROL mislabelled as an ablation dissociation; C2 had zero power by design.
> CONSEQUENCE: the 2026-07-03 autopsy's positive mechanistic finding — "over an F-collapsed field the
> structured class-surround kernel SHARPENS the F-winner" (seed44 -0.169 / seed46 -0.153 nats; divergent
> INTACT 1.047 < OFF 1.130) — rests entirely on the contaminated DV and is WITHDRAWN, as is its
> inference that "the structured kernel is the sole active ingredient". 710 is therefore NO LONGER a
> third structurally-different mechanism corroborating the single-arena F-dominance ceiling. SURVIVES
> (threshold-invariant): `settling_field_moved` (A1 5.24-8.01 vs A0 exactly 0.0), `eligible_set_non_degenerate`
> and `frac_pre_ge2` (both exactly 1.0 on all 6 seeds), `crf_matured`, `learning_engaged`, and the A2
> exact-identity itself — a genuine POSITIVE implementation finding that the soft-competitive settling is
> BUILT, LIVE, moves the field hard and is provably rank-faithful and side-effect-free under a flat kernel.
> READINESS INTACT / FINDING WITHDRAWN (699 precedent). ROOT CAUSE of both defects is one gap the manifest
> self-disclosed (`reorder_rate_limitation_note`): the E3 selector does not expose the pre-settle
> within-eligible argmin, forcing a hold-weighted histogram DV and an arm-contrast structural read. ROUTED
> `implement-substrate` — latch the pre-settle within-eligible argmin in `ree_core/predictors/e3_selector.py`
> as a fresh-selection-gated per-`select()` reorder-rate diagnostic (`complicated (buildable)`); immune to
> BOTH defects and a corpus-level fix. A same-claim single-arena re-letter (710a) is REFUSED — a
> corrected-DV re-run without the latch reproduces defect 2 unchanged. RE-DERIVE BRAKE DECREMENTS (not
> fires): this is a re-adjudication of one run, so 710's hit is removed — MECH-140 1->0, MECH-450 5->4,
> MECH-439 11->10. `epistemic_category` MECH-140 `substrate_ceiling` -> `standard` (the ceiling category was
> earned solely by the withdrawn reading; MECH-140 now has ZERO valid experimental evidence and reverts to
> lit-only, `lit_conf` 0.695 Keller2020/Aquino2026 — strong-lit/UNTESTED, NOT under-supported, and NOT a
> demotion; `lit_conf` and `exp_conf` stay unblended). GOV-CEIL-1 (MECH-439): hit count 10 -> 9, drop 710
> from the named list; `CEILING_EXHAUSTION_N=3` so the 2026-07-09 exhaustion DEMOTION STANDS and the
> co-equal inert-mechanism null is untouched — note that 711 and 713 are also corpus-sweep-disqualified and
> remain among the 9, so 9 is an upper bound pending their re-adjudication. ILLUSORY-CONFLICT CHECK:
> withdrawal removes a NARROW support (`narrow_supports_flag` was already true on MECH-439, single-pathway
> single-arena), so it cannot manufacture illusory conflict resolution in either direction; remaining
> MECH-439 supports unchanged. All three claims stay `candidate` / `pending_retest_after_substrate` /
> PROMOTE NOTHING.

**Separate governance item (data integrity, not claim state):** MECH-140's note asserts a
`hold_candidate_resolve_conflict` that exists only as prose and is machine-invisible; either promote it
to a structured `live_status.evidence.verdict` or strike the assertion.

## 12. Recurrence / granularity-debt check

This is the **second** autopsy on target V3-EXQ-710 — but on the **same run**, re-adjudicating one
instrument, not a second failure with a different signature. The `/claim-synthesis` granularity-debt
trigger keys on *distinct failure signatures circling one claim*, which this is not.
**`granularity_debt_trigger.fires: false`** — recorded honestly so the GOV-GRAN-1 standing scan sees a
true negative rather than a dropped handoff.

## 13. Hypothesis-space ledger (Step 9b)

**Skipped cleanly, deliberately.** No question in `hypothesis_space_registry.v1.json` (10 questions)
carries 710, MECH-140 or MECH-450, so there is no pre-registered leg to resolve. And no
`fanout_recommendation` is emitted: the bottleneck routes to **one unambiguous build**, which is the
documented GOV-FANOUT-1 exemption. Registering a synthetic question here would pad the denominator
without a discrimination behind it.
