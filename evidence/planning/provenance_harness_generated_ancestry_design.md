# Provenance P1 — generated-ancestry harness design

**Date:** 2026-09-10
**Status (updated 2026-09-10, see the BUILD STATUS banner below):** originally a design note only. **The gate is now discharged and P1 is built and run** — see [`provenance_genealogy_probe_p0_result.md`](provenance_genealogy_probe_p0_result.md) and [`provenance_p1_result.md`](provenance_p1_result.md). Still: no claim registered or promoted, no queue entry, no edit to the ladder or the supplement. Recommendations to those documents appear in §10 as recommendations, not as changes.
**Chip:** `chip-20260910-provenance-harness-design-v3`
**Designs against:** [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) (REE_assembly `f7b19654d8`), §§3, 4, 7, 10
**Refines (does not replace):** [`provenance_false_evidence_multiplication_experiment_ladder.md`](provenance_false_evidence_multiplication_experiment_ladder.md), assay P1
**Scaffold audited:** `scripts/convergence_signal_synthetic_assay_001.py`, `scripts/convergence_signal_synthetic_assay_005.py`, and their result notes of 2026-09-09
**Biological motivation:** [`docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md`](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) §8, sources E33 and E43
**Literature fold-in (2026-09-10, after this document landed):** [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) (REE_assembly `b682aed66f`) swept the judgment class after this design was written. Its two consequences for P1 are folded in at **§1.1** (information value) and **§7.5** (the mandatory fluency-versus-cardinality control, `P1-R7`). Nothing else in this document is changed by it: the premise holds and `P1-R1`…`R4` all stand.
**Sibling chip:** `chip-20260910-provenance-p3-replay-design-v3` (replay amplification, P3). At the time of writing no `provenance_p3_replay*` artifact existed, so §6 below publishes the contract outright rather than reconciling against a landed sibling.

---

## 1. Verdict, up front

> ### BUILD STATUS — 2026-09-10: gate discharged, P1 built and run
>
> The verdict below ("it should not be built yet") was **correct when written and is now
> spent**. Both steps it gated have happened, and this banner exists so that a later reader
> does not re-gate or re-build work that is already on `master`.
>
> | Step | Outcome | Artifact |
> |---|---|---|
> | Probe **P0** (§9.3) | endogeneity sweep **PASSED** — ancestry loss here is *generated*, not stipulated; design-note falsifier 1 and supplement falsifier 2 do **not** fire | `scripts/provenance_genealogy_probe_p0.py`, [result](provenance_genealogy_probe_p0_result.md) (`b81f9764bc`) |
> | **P1** harness + assay | **every preregistered criterion passed** on three seed-pairs (MAIN M1–M4, `P1-R2`, `R3`, `R4`, `R7`, C1) | `scripts/provenance_genealogy_harness.py`, `scripts/provenance_p1_false_independence_assay.py`, [result](provenance_p1_result.md) (`062d774289`) |
>
> **The result that matters is P2, not H1.** "Ancestry loss inflates the effective-source
> count" is close to definitional once the readout treats unbound traces as separate
> sources. Swapping that default removes the effect entirely — `absent_policy = dependent`
> gives `N_eff` 1.117 → 1.000 against 1.117 → 4.869 under the independence default. **The
> locus is the readout's default for unknown ancestry, not the corruption**, which is why
> the supplement was right to promote P2. The obvious remedy, a *soft* default, does **not**
> work: once every binding is sub-threshold there is nothing left to interpolate from, so it
> degenerates to `independent` exactly where it was meant to help.
>
> Two further measured corrections to expectations set below: calibration is monotone in
> sign but **U-shaped in magnitude** (best at *moderate* ancestry loss), and there is **no
> divergence from the human pattern** — `ABSENT` and `FALSE_SPLIT` came out near-identical
> in both count and calibration, with `SOFT` already carrying most of the movement, so the
> §5.4 consequence-2 divergence report is not owed.

**The harness is buildable and the design below is concrete — but it should not be built yet, because its load-bearing premise is unproven and can be tested for a fraction of the cost.** *(Original verdict, superseded by the banner above.)*

Three verdicts, in the work-graph debt vocabulary:

| Question | Class | Consequence |
|---|---|---|
| Can the descendant-generation + genealogy-store + replay harness be built? | **complicated (buildable)** | No unknowns. It is new code, not an extension of assay 00N — see §9. |
| Does corrupting a genealogy *representation* through a process produce anything the stipulated-topology case does not? | **complex (probe-gated)** → **RESOLVED to `complicated (buildable)`** | This is Break A, and it is the whole value of P1. Gate it with probe **P0** (§9.3) before building the rest. **P0 passed; the gate is spent and P1 is built.** |
| Does the effective-source-count instrument have the resolution to see the effect above its own miscalibration? | **puzzle (known rules)** → **FACT OBTAINED** | A missing fact, obtainable by running the instrument against known topology in the same run (§8.2). **Measured: worst instrument \|signed error\| 0.2215, against an inflation of 3.494 — the floor is cleared 15.8x.** |
| If inflation appears only under `FALSE_SPLIT` and never under `ABSENT`/`SOFT`, what does the divergence from the human pattern mean? | **mystery (known data)** → **DID NOT ARISE** | Reframe, do not gather. **Measured: no divergence. `ABSENT` (N_eff 4.234, signed error +0.073) and `FALSE_SPLIT` (4.072, +0.066) are near-identical, and `SOFT` already carries most of the movement — the empirically loaded regimes are where the effect lives.** |
| Seed-to-seed variation in the count and calibration estimates | **aleatoric (irreducible)** | Hedge with a preregistered seed set, do not chase. |

The single most consequential design finding is in §7.2: **the legitimate-computation control (P1-R3) becomes mechanically clean once the confidence rule is written in assay 001's own form.** `log-odds = N_eff x logit(p)` has two terms; legitimate computation is licensed to raise `p` and forbidden to raise `N_eff`; false independence does the reverse. Both arms then produce rising confidence, both under one unmodified inference rule, and the discrimination is not a label the scorer applies. Without that decomposition, P1-R3 is the falsifier-5 trap the supplement warns about — a control that cannot separate the forbidden gain from ordinary competent inference.

The second is in §5.4: **decay and misbinding are different process families and they do not produce the same regimes.** A decay/interference process produces `SOFT` and `ABSENT` and essentially never produces `FALSE_SPLIT`, because losing a link cannot manufacture a positive belief in independence. `FALSE_SPLIT` requires a misbinding process — the E33 operation. The ladder treats the four conditions as one condition axis; they are two axes, and only one of them corresponds to the empirically loaded human case.

---

### 1.1 P1's information value is higher than the audit concluded (tranche §6.1)

The supplement concluded P1 is now worth running only "for the route" — humans already show the endpoint when ancestry is presented to them (§2), so the route is all that is left. The judgment-class tranche sharpens that, and the sharpening is an **increase**, not a discount.

The two studies that most directly vary apparent source number while holding content fixed — Weaver et al. 2007 (PMID 17484607) and O'Donnell et al. 2023 (PMID 37691811) — both attribute their own effect to retrieval **fluency/accessibility** rather than to any inference over source count. O'Donnell additionally manipulated repetition against source variability *orthogonally*, in the paradigm nearest to REE's construct (eyewitness memory), and found **no source-variability effect** in two experiments and a meta-analysis at `k = 8`.

So the human baseline may not be a genealogy phenomenon at all. That changes what P1 is:

```text
supplement's reading:  P1 is the ROUTE to a known endpoint
tranche's reading:     P1 asks whether the endpoint is REACHABLE that way in ANY system
```

Under the second reading a **negative** P1 is as informative as a positive one — it would say that cardinality inflation is not producible by corrupting an internal genealogy representation, which no human study has established either way. Neither result is a confirmation of published work. This raises the value of the whole rung and is the strongest argument for paying the probe-P0 cost (§9.3) rather than abandoning the design.

It also has a cost, and it is `P1-R7` (§7.5): if the human effect runs on fluency, then a `FALSE_SPLIT` positive **in a harness that cannot separate fluency from cardinality** inherits exactly the interpretive problem the human literature has, and is uninterpretable for the same reason.

---

## 2. What this design has to defeat

The supplement's Break A is not a gap in coverage; it is a specific accusation against the obvious design. Restated so that the requirement is unambiguous:

```text
assay 001  supplies dependence topology exogenously  (REGIMES = independent|copies|shared_bias|mixed)
assay 005  corrupts provenance LABELS handed to a reader (25%/10%, 50%/20%) and scores allocation regret
Yousif 2019 / Connor Desai 2022 / Weaver 2007
           STIPULATE ancestry in the stimulus materials, in healthy adults, content matched,
           and already obtain the confidence-inflation result
```

A P1 that hands a fixed evidence graph to a reader is the union of those three and contributes nothing. **The only remaining content of P1 is the route**: whether inflation of this shape is producible by corrupting a genealogy representation *inside* an inference architecture.

That makes "generated, not stipulated" a criterion the harness must satisfy demonstrably, not a stylistic preference. §3 states the criterion; §9.3 states how to test whether it can be met at all before committing to the build.

---

## 3. The endogeneity criterion

A harness satisfies **generated ancestry loss** if and only if all four hold:

1. **The manipulated knob is on memory/inference dynamics, not on the genealogy field.** Permitted knobs: binding decay rate, interference strength between similar traces, store capacity, retrieval-cue similarity threshold, reinstatement noise. Forbidden: any parameter whose argument is an ancestry edge, an ancestry label, or a mask indexed by true genealogy.
2. **Which links degrade is determined by trace content, timing and load — not by the experimenter.** Operationally: the set of degraded edges must vary across seeds at a fixed knob value, and must correlate with a content/timing statistic of the traces. If the degraded set is predictable from the knob alone without simulating, the process is stipulation wearing a dynamics label.
3. **No component on the inference path may read true ancestry.** Ground-truth genealogy exists only in the scorer. This is what makes the architecture's own effective-source count a measurement rather than a copy.
4. **The four named conditions are measured, not applied.** `VERIDICAL / SOFT / ABSENT / FALSE_SPLIT` are read off the architecture's genealogy representation after the dynamics have run (§5.3), and used to *stratify* results. They are outcomes, not treatments.

Point 4 is a real departure from P1 as the ladder writes it, and it costs something: the clean four-way condition contrast is replaced by a dose-response over the dynamics knob plus a post-hoc stratification. The compensation is that the dose-response is the causal claim Break A actually demands, and the stratification remains directly comparable to Yousif 2019's stipulated contrast. Report both; the stratified table is what makes the result legible against the human literature, and the dose-response is what makes it new.

**Non-tautology corollary.** Confidence must be derived from the count by a fixed inference rule that is not conditioned on which arm or condition is running. If the scorer can raise confidence in the corrupted arm by any route other than the count, the count is doing no work and the assay has measured its own bookkeeping. §7.2 depends on this and §8.1 restates it as a readout rule.

---

## 4. Deliverable 1 — what generates the descendants

### 4.1 Seed

One latent proposition `H` in `{-1,+1}` and one world event `e0`: a noisy observation carrying signal about `H`. `e0` is stored as a **trace** — a content vector plus a source-family identifier plus a timestamp. Everything downstream is a function of the stored trace, never of `H`.

**The prohibition that makes the assay honest: no descendant generator may consult `H` or the world.** A generator that peeks at `H` is manufacturing a genuinely independent source, and the inflation it produces would be correct rather than false. The one deliberate exception is the ambiguous-perception kind (§4.2), where the world contribution is explicit, parameterised and included in the ground-truth source count.

### 4.2 The four descendant kinds

All four are functions of the stored trace. The ladder's four kinds map onto distinct generators:

| Kind | Generator | Biological motivation |
|---|---|---|
| **replay** | reinstatement of the stored trace with reinstatement noise; content = `trace + eta` | E43 (Zaki et al. 2024/25, PMID 39506117, DOI 10.1038/s41586-024-08168-4): offline ensemble co-reactivation causally links temporally separated memories. Replay is a *demonstrated* generator of cross-episode relations, which is exactly the descendant-producing process P1 and P3 assume. |
| **prediction** | forward model applied to the trace; content = `f(trace) + eta` | Prediction-generated descendants are the ladder's own category; E20/E32 constrain what counts as replay content (selected past experience, not current plan), which is why prediction is kept as a separate generator rather than folded into replay. |
| **retrieved-memory** | cue-driven partial retrieval; content = trace filtered through a retrieval cue, biased by cue-trace similarity | E34 (Berres et al.) supplies the behavioural source-binding-across-intervals result; the similarity-biased filter is what couples retrieval to the interference process in §5.2. |
| **ambiguous-perception** | `alpha * (top-down expectation from trace) + (1 - alpha) * (fresh low-SNR world sample)` | E33 (Ramirez et al. 2013, PMID 23888038): a reactivated internal context can acquire an association with an outcome experienced elsewhere — the causal existence proof for step 1, and the motivation for a percept that is part descendant and part world. |

### 4.3 Why the ambiguous-perception kind carries the design

`alpha` is a continuous dial between "pure descendant of `e0`" (`alpha = 1`) and "genuinely independent new observation" (`alpha = 0`). Three things follow, and they resolve the weakest joint in a design of this shape:

1. **The ground-truth effective source count becomes computable rather than stipulated.** The independent world information contributed by a descendant set is an analytic function of the `alpha` values and the noise terms. The scorer therefore has a *derived* target to score the architecture's `N_eff` readout against, instead of an experimenter-declared "the true count is 1".
2. **P1-R4 (§7.3) is the same dial at `alpha = 0`**, not a bolted-on arm. The positive control that shows the count readout has dynamic range in the correct direction is a point on an axis the assay already sweeps.
3. It gives the harness a principled statement of what "one lineage" means when descendants are not pure copies — a question assay 001 avoided by making `copies` literally `np.repeat`.

### 4.4 Holding content fixed

The ladder's critical criterion requires identical informational content across ancestry conditions. Enforce it mechanically, not by construction discipline:

- generate all trace and descendant content under **common random numbers**, from a content seed independent of the dynamics seed;
- vary only the genealogy-dynamics knob and the dynamics seed;
- **assert** that content hashes are bit-identical across ancestry conditions within a content seed, and fail the run if not.

An assertion is worth the line. Content drift across conditions is the single failure that would invalidate every readout simultaneously and would not be visible in any of them.

---

## 5. Deliverable 2 — what the genealogy representation is, and how it degrades

### 5.1 The representation

A **genealogy representation** is state the architecture carries and updates, consisting of:

- a set of traces, each with content, a source-family identifier, and a timestamp;
- a set of directed **ancestry edges** `(descendant -> ancestor)`, each carrying a **binding strength** in `[0,1]`;
- a derived **source-family partition** over traces, obtained by thresholding/clustering connected components of the edge set.

It is emphatically **not** a label handed to a reader. The difference from assay 005 is that 005's provenance labels are inputs to a posterior computation and are corrupted *before* the reader sees them; here the edge set is state the architecture maintains, and the inference path reads only what that state currently says. Assay 005's soft-provenance posterior is nonetheless the right *readout* layer over this state (§9.2) — `SOFT` is a distribution over shared ancestry, which is precisely what 005 computes well.

### 5.2 The degradation processes

Three process families, all satisfying the §3 endogeneity criterion. Each acts on binding strengths and edge structure; none takes an ancestry-indexed argument.

**Decay.** Binding strength declines with elapsed time at rate `tau`, independent of content. The knob is `tau`. Which edges fall below threshold first is determined by trace age, so it varies with the timing pattern the generators produced.

**Interference.** Binding strength between a descendant and its ancestor is reduced in proportion to the descendant's content similarity to *other* traces in the store — a similar competitor pulls the binding away. The knob is interference gain. This is the process most tightly coupled to §4.2's retrieval-cue filter, and the one whose degraded set is least predictable from the knob, because it depends on the realised content geometry.

**Misbinding.** With probability rising in content similarity, an edge is *re-pointed* to a different trace, or a descendant is assigned a fresh source-family identifier. The knob is misbinding rate. This is the E33 operation: a reactivated internal context acquiring an association with something experienced elsewhere.

### 5.3 The four conditions, defined on the representation

Measured after the dynamics have run, per episode, by comparing the architecture's edge set to the scorer's ground truth:

```text
VERIDICAL    all true ancestry edges present, binding strength above threshold,
             no spurious source families
SOFT         true edges present but binding strengths degraded into the
             uncertain band -- ancestry known as a distribution, not a fact
ABSENT       true edges fallen below threshold; ancestry unknown. NOT the same
             as a positive belief in independence
FALSE_SPLIT  descendants assigned to distinct source families -- a positive,
             confident, and wrong independence representation
```

The distinction between `ABSENT` and `FALSE_SPLIT` is the one the whole assay turns on, and it is the reason P2 ("does unknown ancestry default to independent?") is a *sub-measurement of P1's readout layer* rather than a separate architecture. `ABSENT` states the architecture does not know; whether that gets consumed as independence is a property of the readout rule, and it is measurable in the same run.

### 5.4 Decay and misbinding do not produce the same regimes

This is the finding that most changes P1 as written.

```text
decay / interference  ->  VERIDICAL -> SOFT -> ABSENT   (a loss of information)
misbinding            ->  VERIDICAL -> FALSE_SPLIT      (a creation of false information)
```

Losing a link cannot manufacture a positive belief in independence; it can only produce ignorance. `FALSE_SPLIT` requires a process that actively re-points or re-labels. The ladder's four conditions are therefore **two axes, not one**, and P1's dose-response must be run over both knobs — a decay sweep and a misbinding sweep — with the regime stratification (§5.3) applied to each.

> **Correction from probe P0 (result note §5): the two halves of this prediction are
> different KINDS of claim, and only one of them is empirical.**
>
> - "The decay axis yields `SOFT` and `ABSENT` as distinct, populated regimes" is a genuine
>   empirical question. P0 answered it affirmatively.
> - "Decay never yields `FALSE_SPLIT`" is **definitional given the §5.1 representation**, not
>   a finding. The architecture's confident edges initially point only at true ancestors; a
>   loss process can lower a strength but can neither raise a strength on an edge to a
>   foreign trace nor assert a fresh family identifier. P0 measured 0.000 `FALSE_SPLIT` at
>   every decay knob on every seed, and that had to happen.
>
> Recording the second as an empirical result would over-credit the design. Recording it as
> an entailment makes something useful visible instead: **a `FALSE_SPLIT` observed under a
> pure loss process would indicate a representation bug, not a discovery.**

Two consequences worth stating plainly:

1. **Per supplement §5.4, `SOFT`/`ABSENT` are the empirically loaded conditions** — Connor Desai 2022 locates the human effect under *ambiguity* about independence, not under a presented false split. Those are exactly the regimes the decay axis produces naturally, which is a convenient alignment rather than a designed one.
2. **If the architecture inflates only under `FALSE_SPLIT` and not under `ABSENT`/`SOFT`, that is divergence from the human pattern and must be reported as divergence, not scored as a pass.** The supplement already requires this; the two-axis design is what makes it visible, because a single-axis condition contrast would present both as "ancestry corrupted".

---

## 6. Genealogy contract (for P3)

The eight operations the harness exposes. This is a contract, not an implementation: it fixes what goes in and what comes out, so that the P3 replay-amplification assay can be designed against it without waiting on the build. Items 4-7 are the four readouts of supplement §10 and **must remain separately readable — none may be derived from another**. Item 8 is not one of those four and is easy to omit, because P1 barely uses it; P3-R2 and P3-R3 require it.

```text
1. spawn_descendant(ancestor_id, kind, rng) -> descendant_id
     kind in {replay, prediction, retrieved_memory, ambiguous_perception}.
     Creates a trace whose content derives from the ancestor's stored trace, and
     records an ancestry edge at full binding strength. May not read H or the
     world, except the parameterised world term of ambiguous_perception.

2. degrade(process, knob_value, steps) -> degradation_report
     process in {decay, interference, misbinding}. Advances the genealogy
     representation under that dynamics for the given number of steps.
     Takes NO ancestry-indexed argument (endogeneity criterion, s3).
     The report describes what happened; it is not an instruction.

3. replay(descendant_id, n) -> [descendant_id, ...]
     Drives n replay cycles, returning the descendants produced. P3 drives
     n in {0,1,2,4,8,16} through this operation. Replay and degrade are
     separate calls, so P3 can interleave them or hold one fixed.

4. association_strength(trace_a, trace_b) -> float
     Strength of the formed relation between two traces. The E43/E33-class
     readout: did a relation form?

5. source_attribution(trace_id) -> distribution
     P(external | representation), plus the trace's current source-family
     assignment. The C2/C3-class readout.

6. effective_source_count(trace_set) -> float
     N_eff as the ARCHITECTURE computes it from its own genealogy
     representation. Never from ground truth. This is the cardinality variable.

7. calibration(belief_id) -> (confidence, observed_accuracy, signed_error)
     Confidence in H, and accuracy against world truth, returned as a pair.
     Returned together and never collapsed: assay 001's N_eff instrument is
     itself miscalibrated away from the endpoints (+0.038 shared_bias,
     -0.027 mixed), so a count-derived confidence bakes the instrument's
     error into the result.

8. retrieval_fidelity(descendant_id) -> float
     Reconstruction quality of the descendant's content against the true seed
     content. Distinct from (7), which is about H, and from (4), which is about
     a relation. P3-R2 needs it to show replay improving fidelity while source
     count stays flat; P3-R3 matches on it before any ancestry x replay
     interaction is admissible.
```

**Two constraints on the contract as a whole, which P3 should be able to rely on:**

- **Ground truth is scorer-only.** Operations 1-6 and 8 are on the inference path and have no access to true ancestry, `H`, or the true source count. Operation 7 is a scorer operation by construction, since it compares against world truth; it must not be callable from anything that feeds back into the architecture's state.
- **`degrade` and `replay` are independent.** P3's design requires holding external evidence fixed while sweeping replay count, and separately requires stratifying by ancestry regime. Those are two orthogonal calls, and the harness must not couple them (for example, by advancing decay inside `replay`). If a build finds that coupling unavoidable, that is a contract change and P3 must be told.

---

## 7. Deliverable 4 — the controls, with predeclared signatures

> Four controls were specified by the supplement (`P1-R1`…`R4`; `P1-R1` — descendants generated, not stipulated — is §3/§4 rather than an arm here). A **fifth is mandatory** and was added after this document landed: `P1-R7`, §7.5. Two further refinements were specified in a companion artifact, [`provenance_branch_hippocampal_audit_verification_20260910.md`](provenance_branch_hippocampal_audit_verification_20260910.md) §7: `P1-R5` (retrieval-attribution arm), which is **not** restated here and was run separately (`provenance_p1r5_retrieval_attribution_result.md`); and `P1-R6` (the `MECH-544` boundary declaration), which **is** now discharged in this document at §8.3, because it is a statement about the readouts. `P1-R5` and `P1-R7` are **different axes** and neither substitutes for the other: `P1-R5` asks *where source structure lives* (stored tag versus reconstructed at retrieval); `P1-R7` asks *what confidence tracks* (represented source count versus number of retrieval events).

### 7.1 P1-R2 — adaptive-linking control (from E43)

Two descendants derived from **genuinely different world events**, linked offline by the replay/linking operation. Zaki et al. show this is a normal, useful operation.

```text
correct:   association strength RISES, effective independent-source count STAYS AT 2
failure:   effective source count FALLS below 2 -- distinct sources collapsed
```

The failure direction here is the opposite of the assay's main hypothesis, and it must be detectable rather than silently scored as a pass. An architecture that collapses distinct sources whenever it links them is not conservative; it is broken in the other direction, and a P1 that only looks for inflation would report it as a clean null.

### 7.2 P1-R3 — legitimate-computation control (anchored to E30)

**The most important control in the ladder, and the one that decides whether the hypothesis is testable as posed.** Hold the external observation set fixed; permit repeated computation that demonstrably improves the estimate of the *original* event.

```text
legitimate computation:  calibration IMPROVES, effective source count UNCHANGED
false independence:      effective source count RISES, calibration DEGRADES
```

The control is only meaningful if **both arms produce rising confidence**. If the legitimate arm's confidence stayed flat, the contrast would be trivial and would test nothing. The design requirement is therefore that confidence rises in both, correctly in one and incorrectly in the other, under one unmodified inference rule.

**How to make that mechanical.** Write the confidence rule in assay 001's own form, which already has exactly the two terms needed:

```text
log-odds(H) = N_eff * logit(p)

legitimate computation  raises p     -- better extraction from the SAME e0 means the
                                        single source is effectively more reliable on
                                        this decision; ground-truth accuracy rises with
                                        it, so calibration holds or improves.
                                        N_eff must stay at 1.

false independence      raises N_eff -- the genealogy representation has lost the
                                        shared ancestry, so descendants are counted as
                                        separate sources. p is unchanged, ground-truth
                                        accuracy is unchanged, so confidence overshoots
                                        and calibration degrades.
```

One rule, two terms, and only one term is licensed by each arm. The discrimination is not a label the scorer applies after the fact, and the rule is not conditioned on which arm is running — which is what §3's non-tautology corollary demands. This maps directly onto the existing `independence_aware_confidence` form in `convergence_signal_synthetic_assay_001.py`, and it is the strongest single argument that the confidence layer of the existing scaffold is reusable even though its state layer is not.

**If a build cannot realise this decomposition, supplement falsifier 5 fires**: the hypothesis is untestable under the chosen instruments and the instruments must be rebuilt before any result is reported. That is a legitimate outcome and should be reported as one.

### 7.3 P1-R4 — genuinely independent new observation

A real second world observation is added. This is §4.3's dial at `alpha = 0`.

```text
correct:   effective source count RISES, confidence RISES, calibration PRESERVED
```

Without this arm a null under corruption is uninterpretable, because a count readout that never moves in the correct direction is indistinguishable from a count readout that is broken. Sweeping `alpha` continuously rather than testing only the endpoint additionally gives a monotonicity check: the architecture's `N_eff` should track the analytic ground-truth count across the dial, and the shape of any departure is informative about the instrument.

### 7.4 Content held constant across ancestry conditions

Mechanically enforced by common random numbers plus a content-hash assertion (§4.4). Listed as a control because it is one, and because it is the control whose violation would be invisible in every readout.

---

### 7.5 P1-R7 — fluency versus cardinality (MANDATORY; tranche §6.1)

**The rival hypothesis P1 has to beat, and the one `P1-R1`…`R4` do not cover.** Weaver 2007 and O'Donnell 2023 both conclude that human over-weighting of apparently multiple sources runs on retrieval fluency rather than on a representation of source count (§1.1). The exposure inside P1 is mechanical, not merely conceptual:

> a corrupted genealogy that produces four separately-retrievable descendants also produces four retrieval events.

The two candidate causes are therefore **confounded by construction** in the main design, and if confidence inflation appears under `FALSE_SPLIT` the fluency account explains it without any genealogy representation being consulted or misread — which is the entire content of P1 (§2).

**The arm.** Hold the ancestry representation **intact and correct** — `VERIDICAL`, verified by the §5.3 regime classifier, not assumed — and vary the number of retrieval/reinstatement events over the **same descendant set**. Descendant cardinality is held fixed; only retrieval-event count moves. In the §6 contract idiom this is repeated reads through operations 5–8 at a fixed edge set, with `degrade` not advanced and no descendant spawned; note that this requires `replay` to support a non-descendant-generating mode, the same `mode = in_place` capability P3's healthy-replay gate depends on.

**Predeclared signatures:**

```text
cardinality effect:  confidence tracks represented source COUNT,
                     flat across retrieval-event count at fixed count
fluency effect:      confidence tracks RETRIEVAL EVENTS,
                     present even with ancestry correctly represented
```

**Interpretation, fixed in advance.** A fluency signature here does not falsify H1 — it says the instrument cannot attribute an inflation to cardinality, so the `FALSE_SPLIT` result cannot be read as one. Concretely:

| `P1-R7` outcome | What the main `FALSE_SPLIT` result may be reported as |
|---|---|
| flat across retrieval events at fixed count | cardinality is separable; a `FALSE_SPLIT` inflation is attributable to the genealogy representation |
| confidence rises with retrieval events under `VERIDICAL` | **fluency is live and uncontrolled** — report the `FALSE_SPLIT` inflation as *not attributable*, alongside the `P1-R7` curve |
| both move, and the effects are additive/separable in the fitted model | report the decomposition, with the cardinality component as the P1 result |

**An architecture in which these two are not separable has the same interpretive problem the human literature has, and a positive `FALSE_SPLIT` result would be uninterpretable.** That failure mode belongs with the other two of §11 — it is a reportable outcome, not something to design around after the fact.

Two boundaries, so this control is not over-read. It is a control on the **route**, not a test of the human effect: no synthetic result here bears on which mechanism the human literature runs on. And it is not the instrument-calibration floor of §8.2 — that floor asks whether an inflation clears the count instrument's own *bias*; `P1-R7` asks whether an inflation that does clear it is attributable to *count at all*. Both are required, and passing one says nothing about the other.

---

## 8. Deliverable 5 — four readouts, never collapsed

### 8.1 The readouts

```text
1. association strength                 did a relation form?          (E43/E33 class)
2. source attribution                   P(external | representation)  (C2/C3 class)
3. effective independent-source count   the cardinality variable
4. calibration against world truth      confidence vs observed accuracy
```

Reported separately and both, per supplement §10. **Count and calibration are never derived one from the other.** Assay 001's own result shows why: its `N_eff` correction is well calibrated at the endpoints (absolute error 0.00096 independent, 0.00139 copies) and drifts in between (`shared_bias` +0.038 over-confident, `mixed` -0.027 under-confident). A count-derived confidence would bake that drift into the headline number.

Two signatures worth naming in advance, both of which are respectable results:

- readout 1 rising with readout 3 flat is the **E43 adaptive-linking signature** (P1-R2 passing);
- readout 2 changing with readouts 3 and 4 flat is the **H0 source-label-only outcome**, and the supplement is right that it remains the most likely single outcome.

### 8.2 The instrument-calibration floor — a required companion measurement

Because readout 3 is an instrument with known drift, P1 must additionally measure **the instrument's own error against known topology in the same run**: feed the readout a set of traces whose ground-truth genealogy the scorer holds, and record its signed error. Then apply a predeclared interpretability floor:

```text
if |measured inflation| <= |instrument error on matched known topology|
    the result is uninterpretable, and must be reported as uninterpretable
    rather than as a null or as a positive
```

This is the `puzzle (known rules)` item from §1: a missing fact, cheaply obtainable, that determines whether any P1 number can be read at all. It is not optional, and it is not the same as reporting a confidence interval — it is the instrument's *bias*, not its variance.

### 8.3 P1-R6 — the `MECH-544` boundary, declared on the readouts

`MECH-542` / `MECH-543` / `MECH-544` (source-sensitive permeability, registered 2026-09-08, one day before this branch's parent thought) are an unrecognised REE-internal neighbour of this branch, and `MECH-544`'s predicted routes already include *"repeated fictional trajectories distorting perceived likelihood"* — this branch's step 4, reached by its step 5's mechanism. Neither lineage referenced the other in either direction. The remedy is to **distinguish the two, not merge them**, and the distinguishing variable is one of §8.1's own four readouts:

```text
MECH-544  permeability:  a hypothetical-source frame fails to PROTECT a variable
                         it should protect (occurrence, source truth, responsibility)
                         -> moves readouts 1, 2 and 4

P1        false independence: dependent descendants are counted as several
                         independent sources
                         -> readout 3 is P1's DISTINCTIVE product
```

**A result that moves only readouts 1, 2 and 4 is `MECH-544`'s, not P1's, and must not be counted as evidence for this branch.** That is what stops two candidate claims consuming one experiment's result — the failure this declaration exists to prevent.

**This is no longer only an argument; `P1-R5` measured it.** On the retrieval-attribution route, sixteen in-place retrieval events at fixed cardinality and fixed storage moved **readout 2** by −33.5% relative (`p_external` 0.0824 → 0.0547) while moving **readout 3** by −0.025 — and on the stored-tag route both were exactly zero (`provenance_p1r5_retrieval_attribution_result.md`, findings A9a/A9b). A fluency-driven, `MECH-544`-shaped mechanism reached the readouts this boundary assigns to `MECH-544`, and did not reach the one it assigns to P1. The demarcation survives its first empirical test.

**Two consequences, both narrowing.** (a) `P1-R5` showed the fluency effect is **route-specific and readout-specific**, so `P1-R7`'s clearance of the fluency rival ("fluency is not live") holds for the stored-tag route and must not be carried to an attribution architecture — and this boundary is therefore route-conditional, not absolute. (b) The boundary is stated over readouts, so it only does its work while §8.1's rule holds: the four readouts reported **separately, never one derived from another**.

---

## 9. Deliverable 6 — feasibility and cost

### 9.1 What the existing scaffold cannot do

Assays 001-006 are vote-matrix samplers. Each draws votes conditioned on a label, with dependence injected at construction time (`np.repeat` for copies, a shared vote row for shared bias, cluster structure in 005/006). There is **no time index, no persistent store, no state that survives a trial, and no replay loop** — the supplement's `grep -il replay` returning nothing is a property of the architecture, not an oversight.

So the harness is not an extension of assay 00N in the sense of adding a regime. Four things have no counterpart in the existing scripts and must be built:

- a trace store with persistence across time steps;
- the four descendant generators (§4.2);
- the genealogy representation and its three degradation processes (§5.1-5.2);
- a replay loop, which P3 requires and P1 needs for the replay descendant kind.

### 9.2 What genuinely is reusable

More than the previous paragraph suggests, and the split is clean: **the state layer is new; the scoring and confidence layer is not.**

| Reusable | From | Used for |
|---|---|---|
| world/label generator and observed-accuracy comparison | 001 `generate_votes`, `summarize_regime` | calibration against world truth (readout 4) |
| `N_eff * logit(p)` confidence form | 001 `independence_aware_confidence` | the P1-R3 discriminator (§7.2) — this is the important one |
| dependency estimation from residual correlation | 001 `estimate_dependency` | a lineage-free comparator, and P6's E30 rival |
| soft-provenance posterior over ancestry | 005 `soft_posterior` | the `SOFT` condition's readout layer (§5.1) |
| preregistered-criteria block, manifest/CSV banking, seeded CLI | 001 `main`, `evaluate_preregistered_criteria` | run banking under the existing convention |

### 9.3 The gate — probe P0 before building P1

> **DISCHARGED 2026-09-10.** P0 was built and run (`scripts/provenance_genealogy_probe_p0.py`,
> [result](provenance_genealogy_probe_p0_result.md), REE_assembly `b81f9764bc`). Sweep (b)
> **passed**: all three degradation processes vary their degraded edge set across dynamics
> seeds at a fixed store (Jaccard 0.15–0.56) *and* predict it from a content/timing statistic
> (Spearman +0.66 to +0.93, p < 0.001), while all three discriminative comparators failed
> exactly the clauses predeclared for them. Sweep (a) failed one clause (A1) on **grid
> resolution rather than process behaviour** — episode-level `SOFT` goes as
> `(1 − p_absent_edge)^n_edges`, compressing the transition into a window the preregistered
> `tau` grid stepped over; a finer grid reaches 0.372 where the threshold was 0.10. **The
> text below is retained as the specification P0 was built to; it is no longer an instruction.**

**P1 should not be built until the endogeneity criterion is shown to be satisfiable, and that can be tested cheaply.** Probe P0 builds *only* the genealogy store, the three degradation processes, and the regime classifier (§5.3). No descendant content, no confidence, no calibration, no readouts 2-4.

It asks two questions:

```text
(a) NON-DEGENERACY   Does a sweep over the decay/interference knob and the
                     misbinding knob produce all four regimes at usable
                     frequencies -- in particular, does the decay axis produce
                     SOFT and ABSENT as distinct, populated regimes rather than
                     collapsing straight to ABSENT?

(b) ENDOGENEITY      At a fixed knob value, does the SET of degraded edges vary
                     across dynamics seeds, and does it correlate with a
                     content/timing statistic of the traces? If the degraded set
                     is predictable from the knob alone, the process is
                     stipulation with extra steps and P1 has no content.
```

If (b) fails, **supplement falsifier 2 fires early and cheaply** — the branch reduces to Yousif 2019 and contributes nothing beyond it, and that is worth knowing for the cost of a probe rather than the cost of a harness. If (a) fails but (b) passes, the process families need reworking before P1, not abandonment.

### 9.4 Cost

Rough magnitudes, stated as estimates rather than measurements:

| Item | Scale | Note |
|---|---|---|
| **Probe P0** | small — of the order of 150-250 lines, hours of work | Store + three processes + regime classifier + a sweep. No content, no readouts. Gates everything below. |
| **Harness module** | of the order of a few hundred lines | Trace store, four generators, genealogy representation, three processes, the eight contract operations. Shared with P3 — this is why §6 exists. |
| **P1 driver + prereg + result note** | comparable to assay 005 (280 lines) plus its two documents | Dose-response over two knobs, four controls, four readouts, instrument-calibration companion, seed set. |
| **P3 driver** | additional, designed by the sibling chip | Reuses the harness module via §6; should not need to touch the store. |

The harness module is the shared cost and it is charged once. That is the argument for building the module against the §6 contract rather than letting P1 and P3 each grow their own state layer.

### 9.5 Build guidance carried forward from P0 and P1 (added 2026-09-10)

Four things the builds established that this design did not anticipate. The first three are
P0 result-note §7 recommendations 1–3, realised in the P1 build; **all four bind P3 too.**

1. **Select knob grids by per-edge degradation rate, not a priori.** A grid chosen on the
   knob scale can step over the entire episode-level transition, which is exactly how P0's
   criterion A1 failed. Calibrate each axis so its sample points span per-edge `ABSENT`
   rates of roughly 1–30%.
2. **Make edge-level stratification primary, episode-level secondary.** §5.3 defines the
   four conditions per episode, and the worst-edge rule turns a graded edge-level population
   into a near-binary episode-level one. Report both, and say which is which.
3. **Exposure-matching is a design requirement, not a detail.** Any statistic that
   correlates with how long a trace has been in the store correlates with degradation for
   reasons that have nothing to do with content. P0 hit this directly: an unmatched noise
   comparator passed the content-dependence criterion at rho +0.83 while carrying no
   structure at all, purely because older edges accumulate more applications. This is the
   same discipline as `P3-R3`'s "match retrieval quality before attributing an interaction
   to ancestry", and it should be stated once rather than rediscovered per readout.
4. **Two facts about the state layer that the P1 build found load-bearing** (P1 result §2).
   **Ancestry and association must be separate edge sets** — with one set, `P1-R2` cannot
   pass by construction, because linking two descendants of different world events would
   raise the pairwise dependency term and drive the count *down*, which is the very failure
   the control exists to detect. And **initial binding strength must be derived from content,
   not set to 1.0** — a flat 1.0 binds an `alpha = 0` descendant as tightly as a pure replay,
   leaving the count with no dynamic range across the §4.3 dial and making `P1-R4`
   unpassable.

---

## 10. Recommendations to the ladder and the supplement

Recorded here as recommendations. This session did not edit either document.

1. **P1's four conditions should be re-specified as measured regimes, not applied treatments** (§3.4, §5.3). As written, P1 lists `VERIDICAL / SOFT / ABSENT / FALSE_SPLIT` as conditions, which reads as a treatment axis and would license precisely the stipulated design Break A rules out.
2. **P1's condition axis should be split in two** (§5.4). Decay/interference produces `SOFT`/`ABSENT`; misbinding produces `FALSE_SPLIT`. Running one knob and reporting four conditions would conflate a loss of information with the creation of false information.
3. **Add the instrument-calibration floor as a required companion measurement** (§8.2). The supplement establishes that `N_eff` is a drifting instrument and correctly concludes that count and calibration must be reported separately; it stops short of requiring the instrument's bias to be measured in-run, without which the separation does not tell you whether the headline number clears the noise.
4. **P2 is a sub-measurement of P1's readout layer, not a separate architecture** (§5.3). Whether `ABSENT` is consumed as independence is a property of the readout rule over the same genealogy representation, and is measurable in the same run. Given the supplement's promotion of P2 to a primary result, this is a cost saving rather than a demotion.
5. **The ambiguous-perception descendant kind should be parameterised rather than categorical** (§4.3). It is the only one of the four that spans the descendant/independent-source boundary, and parameterising it makes the ground-truth source count computable instead of declared — which is otherwise the weakest joint in the design.
6. **State in P1 that no descendant generator may consult `H`** (§4.1). It is implied by "descendants of `e0`" but it is the assumption whose quiet violation would produce a spurious positive that looks exactly like the hypothesis.

---

7. **`P1-R7` (fluency versus cardinality) is mandatory, not optional** (§7.5). It is the one control the supplement's list does not contain and the one whose absence makes a positive result uninterpretable.
8. **Record that P1's information value rose rather than fell** (§1.1). The supplement's "worth running for the route" understates it: if the human effect is fluency, the endpoint's reachability by this route is itself open, and a negative P1 is a result rather than a replication of published work.

---

## 11. Falsifiers specific to this design

Supplement §11 stands. This design adds three failure modes of its own, all of which should be reported rather than worked around:

1. **Probe P0's endogeneity question (b) fails.** The degraded edge set is predictable from the knob alone. The harness cannot generate ancestry loss, only stipulate it, and P1 reduces to published work. This is supplement falsifier 2, reached cheaply.
2. **The P1-R3 decomposition cannot be realised** — no inference rule separates the licensed rise in `p` from the forbidden rise in `N_eff` without conditioning on the arm. This is supplement falsifier 5: untestable as posed, instruments need rebuilding.
3. **Measured inflation does not clear the instrument-calibration floor** (§8.2). The result is uninterpretable, and must be reported as uninterpretable rather than as a null.
4. **`P1-R7` shows fluency and cardinality are not separable in the harness** (§7.5). Confidence tracks retrieval-event count even under a correct `VERIDICAL` genealogy, so an inflation under `FALSE_SPLIT` cannot be attributed to the count. Report as not attributable — this is a distinct outcome from a null and from the §8.2 floor failure.

---

## 12. Epistemic boundary

- Nothing here is evidence about psychosis. The design is a synthetic architecture; C1 preparations cannot measure confidence or source count, and the direction of travel is one-way — the clinical literature constrains the assays, the assays license no clinical claim.
- The C3 result (Yousif 2019, Connor Desai 2022, Weaver 2007) is about healthy adults with stipulated source structure. It is used here only to establish what P1 must *not* merely reproduce.
- The hippocampal sources (E33, E43, E42, E20/E32, E34) motivate the generators and the misbinding process. They supply no cardinality or calibration readout and none is claimed from them; §6 of the supplement bounds this correctly and this design does not extend it.
- **~~The design is unbuilt and ungated.~~ SUPERSEDED 2026-09-10.** Its central premise — that ancestry loss can be generated rather than stipulated in a harness of this class — was untested when this was written. It has since been **tested and upheld** by probe P0 (§9.3), and P1 is built and run. What remains untested is stated positively in the P1 result note's own epistemic boundary: nothing here bears on humans or on psychosis, nothing here says which mechanism the *human* effect runs on, and the result is about the **stored-tag** route only (`P1-R5`, predeclared).

---

## Compact statement

> Humans already show the confidence-inflation result when ancestry is presented to them, so P1 earns its place only by corrupting a genealogy representation from the inside. That requires a knob on memory dynamics rather than on the ancestry field, a decay axis and a misbinding axis rather than one four-way condition, and a confidence rule whose two terms let legitimate computation and false independence both raise confidence while only one of them raises the count. All of that is buildable. Whether the first of those requirements can actually be met is the branch's remaining unknown, and a probe settles it for a fraction of the harness.
