# Failure autopsy — V3-EXQ-786a (MECH-163 dual-system recruitment)

**Scope:** single. **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z. **Promotes and demotes nothing.**

Run: `v3_exq_786a_mech163_dual_system_recruitment_20260721T113809Z_v3` ·
claims `[MECH-163]` · purpose **`evidence`** · supersedes
`v3_exq_786_mech163_dual_system_recruitment_20260719T163935Z_v3` ·
outcome **FAIL** · direction **`weakens`** · self-route `no_differential_recruitment`.
**No adjudication flag** — this is a clean FAIL, not a flagged self-route.

---

## 1. Facts

Recording complete (`rec/v1`, `substrate_hash`, `machine_class`, `config`,
`seeds [0..7]`, `elapsed_seconds 15716`, `substrate_stable_across_run`, plus
`pre_registered` and `observation_dims` blocks). **No recording debt.**

**This is the strongest-designed run in the pending set.** Every reason a null could
be dismissed has been closed in advance:

| Check | Result |
|---|---|
| **Manipulation check, substantive leg** — familiarity discriminability AUC at the pre-registered bandwidth | **0.848** vs 0.7 bar ✅ |
| **Manipulation check, above-chance leg** — SEM lower bound vs the 0.5 null | **0.795** ✅ |
| `non_degenerate` | **true**, `degeneracy_reason` empty ✅ |
| n seeds | **8** (786 was superseded partly for power) |
| Robustness bar (`mean − k·SEM > margin`) | mean 0.00435, SEM 0.0325, LB **−0.0281** vs margin 0.02 ✗ |
| Cohen's d on the delta | **0.047** |
| Per-seed recruitment deltas | −0.006, **−0.206**, 0.021, 0.049, 0.039, 0.145, 0.004, −0.012 |

The load-bearing criterion `C1_recruitment_higher_on_novel` failed on **both** legs
(`absolute_leg_passed: false`, `standardized_leg_passed: false`).

786a also fixed a real design defect in its predecessor: 786's manipulation-check bar
was a raw mean-difference floor of 0.05, which was neither scale-free (the readout's
units are set by the tracker's bandwidth/EMA, so re-tuning the instrument moved the
gate) nor an overlap measure. AUC is invariant under monotone transforms and has a
principled null at 0.5. **The instrument critique was answered before the result was
taken.**

---

## 2. Claim-layer mapping — and the scope limit that must travel with the result

MECH-163 (`candidate`, `claim_type mechanism_hypothesis`, `implementation_phase v3`,
`depends_on [ARC-007, ARC-021, MECH-112, SD-012, INV-029, ARC-071]`). Its existing
`evidence_quality_note` records the 2026-04-03 `hold_pending_v3_substrate` gate: **9
lit supports, 0 genuine experimental entries.** This run is the first V3 experimental
evidence on the claim.

**Did the claim get a chance to express itself? For leg (1), yes.** The manipulation
check confirms the two layout populations were genuinely discriminable to the agent
(AUC 0.848), the readout is scale-free, n=8, and the run is non-degenerate. Practised
vs held-out layouts differed on four generating parameters (size 10→14, hazards 3→7,
resources 5→2, landmarks_b 2→5), all locally observable in the 5×5 field views, with
drift suppressed. That is a fair test of *novel-context differential recruitment*.

**But MECH-163 is broader than what was tested**, and the run says so itself
(`scope_note`): leg (2) long-horizon benefit accumulation is blocked by ARC-007's
STRICT value-flat proposals; leg (3) prosocial planning has no V3 substrate; and
ARC-071 (planned→habit transfer), which the 2026-05-10 targeted review established is
*the missing transition mechanism MECH-163 presupposes but does not specify*, is
**unbuilt**.

So the honest statement is: **one leg of three was tested fairly and returned a null.
The `weakens` direction is earned, and its scope is one leg.**

---

## 3. Biological-reference triage — the core move

**Closest mechanism:** the dual-system / goal-directed-vs-habitual distinction
(dorsomedial vs dorsolateral striatum; Balleine & Dickinson devaluation work; Daw's
model-based/model-free arbitration). The canonical finding is that **novelty and
uncertainty shift control toward the goal-directed/model-based system**, and that
extended practice shifts it toward the habitual system.

**Dependencies in real brains — and this is where the null becomes informative.**
Differential recruitment is not a property of having two systems; it is a property of
an **arbitrator** that reads uncertainty and reallocates control. In the biology that
arbitrator is a distinct computational element (Daw's uncertainty-based arbitration;
Lee/Shimojo/O'Doherty's reliability-based arbitration in vlPFC/FPC). **A system with
two pathways and no arbitrator shows exactly the null observed here**: both pathways
are engaged, neither is preferentially recruited, and the recruitment delta sits at
zero with a small SD.

The measured picture matches that signature closely — delta mean 0.0044, d 0.047,
seven of eight seeds inside ±0.15 — a *flat* response, not a noisy or bimodal one.

**Formal-definition import?** No. MECH-163 is a biologically-grounded dual-systems
claim, not a formal import; `is_formal_import: false`. **Lit status: present** — 9 lit
supports plus the `targeted_review_arc_071_composition` synthesis (lit_conf 0.848).
No `/lit-pull` commission is owed.

**Does the failure resemble a missing-dependency signature?** **Yes.** ARC-071 is named
in `depends_on` and is **unbuilt**, and the 2026-05-10 review already identified it as
the missing transition mechanism. A dual-system claim tested without its transition /
arbitration machinery is being tested with a known dependency absent. That does **not**
make the run non-contributory — the leg-(1) prediction is real and was fairly tested —
but it does bound how far the `weakens` can reach.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened, narrowly** | Leg (1) tested fairly and returned a null. Legs (2) and (3) untested; the claim as a whole is not falsified. |
| Biological reference | **clear** | Dual-systems is well-evidenced; the null matches the *no-arbitrator* signature specifically. |
| Prerequisites | **missing** | ARC-071 (planned→habit transfer) unbuilt and named in `depends_on`; no arbitration element in the substrate. |
| Implementation completeness | **partial — symbol without functional role** | Two pathways exist; the mechanism that *selects between them under novelty* does not. |
| Environment adequacy | **adequate** | Four generating parameters varied, all locally observable, drift suppressed; manipulation check confirms discriminability. |
| Measurement adequacy | **adequate** | AUC readout is scale-free with a principled null; robustness bar is `mean − SEM > margin`; both criterion legs recomputable from their own measured/threshold pairs. |
| Integration adequacy | **partially coupled** | Pathways present, arbitration absent. |
| Scale / capacity | **adequate** | n=8; `sample_size_improvable: true` but LB −0.028 vs margin 0.02 with d 0.047 means more seeds would not rescue this effect size. |

**Recommended `epistemic_category`: `standard`.** A fairly-tested, adequately-powered,
non-degenerate null. Explicitly **not** `substrate_ceiling` and not a measurement
defect — the instrument was repaired before the result was taken.

**Recommended `evidence_direction`: `weakens` — STANDS**, with a mandatory scope
qualifier in the `evidence_quality_note`.

---

## 5. Learning extracted

1. **The first genuine V3 experimental evidence on MECH-163 is a null on leg (1).**
   After a 2026-04-03 `hold_pending_v3_substrate` with 9 lit supports and 0
   experimental entries, this is the claim's first experimental datum, and it does not
   support differential recruitment under novelty. Report `lit_conf` and `exp_conf`
   **separately**: 9 lit supports and 1 experimental weakens do not blend.
2. **The null has a specific biological shape: no arbitrator.** Delta mean 0.0044 with
   d 0.047 and seven of eight seeds within ±0.15 is a *flat* response. In the reference
   biology, differential recruitment is produced by an uncertainty/reliability
   arbitrator, not by the mere existence of two pathways. **This FAIL is therefore
   positive evidence for the necessity of an arbitration element** — which is
   precisely what ARC-071 names and what the substrate lacks.
3. **786's manipulation-check repair is validated and generalisable.** Replacing a raw
   mean-difference floor with an AUC bar made the gate scale-free and gave it a
   principled null at 0.5 — closing the "re-tuning the instrument moves the gate"
   hazard. Adopt this wherever a manipulation check is currently a raw-difference
   floor.
4. **More seeds will not rescue this.** `sample_size_improvable: true` is technically
   correct, but with d = 0.047 the effect is not underpowered — it is absent at the
   scale the claim predicts. Do not route this to a power re-run.

---

## 6. Repair pathway

**Node classification:** `complicated (buildable)` for the substrate half — ARC-071 is
a named build with no open scientific question — and `mystery (known data)` for the
claim half: we already have the data, and the frame ("MECH-163 as one claim") is what
needs reworking. Not `puzzle`; more runs will not settle it.

**Re-derive brake:** MECH-163 = **0** confirmed `substrate_ceiling` hits under R1–R3.
**Does not fire**, and this autopsy adds no ceiling reading.

**Granularity-debt recurrence trigger: FIRES.** This is the **second** autopsy circling
MECH-163 (`failure_autopsy_V3-EXQ-786_2026-07-20` preceded it), and the two have
**different failure signatures** — 786 was an instrument defect (non-scale-free
manipulation-check bar), 786a is a substantive null with the instrument repaired. Per
the standing rule, one autopsy is a diagnosis and the second on the same target is a
pattern. The claim bundles three legs with three different blockers (leg 2 blocked by
ARC-007 value-flat proposals, leg 3 with no V3 substrate at all, leg 1 now nulled
without ARC-071) — that is the classic granularity-debt shape: a coarse claim that is
several claims.

**Routing: `/claim-synthesis` on MECH-163** (proposal-first, lit-grounded
decomposition into testable children), **plus** `/implement-substrate` on the
arbitration/transfer dependency.

| Recommendation | Detail |
|---|---|
| `/claim-synthesis` | Decompose MECH-163 into its three legs as separately-testable children, each carrying its own blocker. Leg (1) already has an experimental datum; legs (2)/(3) are substrate-blocked and should say so in their own right rather than inheriting a parent's confidence. |
| `/implement-substrate` — **create** | `sd_dualsystem_uncertainty_arbitration`: an uncertainty/reliability-based arbitrator that reallocates control between the two pathways, per the Daw / Lee-O'Doherty reference. Unblocks MECH-163 leg (1) retest and is the mechanism ARC-071 presupposes. `priority_suggested: 2` (one fresh failure record; blocks 1 claim leg directly). |

`/lit-pull`: **not owed** — lit coverage is present (9 supports plus the ARC-071
targeted review).

### Draft `evidence_quality_note` (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-786a, **evidence**, claim_ids=[MECH-163], `weakens`;
> failure_autopsy_V3-EXQ-786a_2026-07-22). **`weakens` STANDS, scoped to leg (1)
> only.** This is MECH-163's first genuine V3 experimental evidence (the 2026-04-03
> hold recorded 9 lit supports, 0 experimental entries). The test was fair and the
> instrument was repaired first: the manipulation check passed on both legs
> (familiarity discriminability AUC 0.848 vs a 0.7 bar; SEM lower bound 0.795 vs the
> 0.5 null), replacing 786's raw mean-difference floor of 0.05 which was neither
> scale-free nor an overlap measure. n=8, `non_degenerate: true`. The load-bearing
> criterion `C1_recruitment_higher_on_novel` failed on both the absolute and
> standardized legs: recruitment delta mean 0.00435, SEM 0.0325, lower bound −0.0281
> against a 0.02 margin, Cohen's d **0.047**. That is an absent effect, not an
> underpowered one — do not route to a power re-run. **SCOPE: leg (1) novel-context
> recruitment ONLY.** Leg (2) long-horizon benefit accumulation is blocked by ARC-007
> STRICT value-flat proposals; leg (3) prosocial planning has no V3 substrate; and
> ARC-071 (planned→habit transfer) — which the 2026-05-10
> `targeted_review_arc_071_composition` synthesis (lit_conf 0.848) established is the
> missing transition mechanism MECH-163 presupposes but does not specify — is unbuilt.
> The null's shape is diagnostic: a flat response (7 of 8 seeds within ±0.15) is the
> signature of two pathways with **no arbitrator**, and in the reference biology
> differential recruitment is produced by uncertainty/reliability-based arbitration
> (Daw; Lee/Shimojo/O'Doherty), not by the existence of two pathways. Read as positive
> evidence for the necessity of an arbitration element. `lit_conf` and `exp_conf` must
> be reported separately — 9 lit supports and 1 experimental weakens do not blend.
> Granularity-debt recurrence fires (second autopsy, different signature): routed to
> `/claim-synthesis`.

---

## 7. Frozen-ledger delta (Step 9b)

**None.** MECH-163 has no question in `hypothesis_space_registry.v1.json`, and this
autopsy emits no `fanout_recommendation` — the routing is a single unambiguous build
(the arbitrator) plus a claim decomposition, not a discrimination among ≥2 live
hypotheses. Nothing to pre-register; nothing to resolve.

## 8. Confirmed routing (user-adjudicated 2026-07-22)

User confirmed **"786a: weakens STANDS, scope-narrowed"**, including the
`/claim-synthesis` recurrence route.
