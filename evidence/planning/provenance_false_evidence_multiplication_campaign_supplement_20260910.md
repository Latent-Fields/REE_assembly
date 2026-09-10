# Provenance / false-evidence multiplication — hippocampal-campaign audit supplement

**Date:** 2026-09-10
**Status:** audit and assay refinement. This document does **not** register, promote, implement, queue or score a claim, and makes no diagnostic assertion about psychosis.
**Parent thought:** [`docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md`](../../docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md)
**Ladder refined (not duplicated):** [`provenance_false_evidence_multiplication_experiment_ladder.md`](provenance_false_evidence_multiplication_experiment_ladder.md)
**Existing review:** [`provenance_psychosis_literature_pull_20260909.md`](provenance_psychosis_literature_pull_20260909.md)
**Audited input:** [`docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md`](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) §8
**Synthetic base audited:** convergence-signal assays 001–006 (`evidence/experiments/convergence_signal_synthetic_assay_00N/`, `scripts/convergence_signal_synthetic_assay_00N.py`)

---

## 1. Verdict

**An update is justified, and its substance is a correction plus two bounded refinements — not a new experiment family.**

Three findings, in descending order of consequence:

1. **The branch's own evidence map contains an error.** The 2026-09-09 literature pull records `dependent descendants become independent "votes"` as **"not directly established"**. That is wrong as stated. It *is* directly established — content-matched, ancestry-manipulated, confidence-measured — in healthy adults, by a judgment/social-cognition literature (§5) that neither prior pull searched. This changes what P1 is *for*.
2. **The hippocampal campaign's own §8 self-bounding is accurate, and this audit confirms it independently.** The campaign supplies no evidence for ancestry counting. What it *does* supply is a causal **descendant-generation and misbinding** mechanism class that the provenance branch previously had only as assumption (§6).
3. **No experiment of any class links the chain end to end, and the break is in a specific place** (§4): the mechanisms that *lose ancestry* and the readouts that *detect cardinality inflation* have never been placed in the same experiment, in any species, synthetic or biological. Step 5 (recursive amplification across replay) is untested everywhere — including in REE's own assays, none of which contains a replay loop at all.

The compact target of the ladder survives unchanged. What changes is that its first half now has biological mechanism candidates, its second half turns out to have a healthy-human baseline, and the join between them is the whole remaining scientific content.

---

## 2. Method, and the evidence classes kept separate

The instruction to treat retrospective memory linking, false contextual association and clinical source-monitoring as different evidence classes is load-bearing here, because the chain's apparent support comes from pooling classes that cannot substitute for one another. Six classes were kept distinct throughout:

| Class | Content | Readouts physically available |
|---|---|---|
| **C1** rodent causal memory manipulation | engram reactivation, offline co-reactivation, SWR perturbation | association strength, behaviour; **no** confidence, **no** source count |
| **C2** clinical source monitoring in psychosis | source/reality-monitoring meta-analyses, corollary discharge | source attribution, error rates, some confidence; **no** ancestry manipulation |
| **C3** human judgment / consensus evaluation | true-vs-false consensus, repeated-source prevalence | belief, confidence, estimated source count; ancestry **stipulated**, not induced |
| **C4** computational models | circular inference, self-healing codes | model fit, sufficiency; not an observation of a nervous system |
| **C5** clinical repetition-belief | illusory-truth in schizophrenia | belief change under repetition; no ancestry variable |
| **C6** REE synthetic assays 001–006 | dependence topology → allocation and confidence | all four readouts; dependence topology supplied **exogenously** |

A claim that the chain is supported is only admissible if it is supported *within* a class, or by an experiment that spans two of them. §4 shows no such experiment exists.

---

## 3. The five steps, audited against what actually exists

| Step | Best available evidence | Class | Status |
|---|---|---|---|
| 1. memory binding / source-label error | Ramirez et al. 2013 (E33) optogenetic false contextual association; Damiani 2022 (PMID 35124869) / 2024 (PMID 38039688) source-monitoring impairment in psychosis | C1, C2 | **established**, in both classes, by different manipulations |
| 2. loss of causal ancestry | Zaki et al. 2024/25 (E43) offline ensemble co-reactivation links memories across days | C1 | **not established.** E43 demonstrates *linking*, which is the creation of a relation, not the loss of one. No study measures an ancestry representation degrading |
| 3. increased estimated independent-source count | Yousif, Aboody & Keil 2019 (PMID 31291546); Connor Desai, Xie & Hayes 2022 (PMID 35149359); Weaver et al. 2007 (PMID 17484607) | C3 | **established in healthy humans** (see §5) |
| 4. confidence / calibration change | same C3 sources; REE assay 001 quantifies it against ground truth | C3, C6 | **established**, and quantified synthetically |
| 5. recursive amplification across replay | — | — | **untested in every class.** No REE assay contains a replay loop; no clinical or rodent study measures cardinality across replay cycles |

### The synthetic half, stated precisely

REE assay 001 already links step 3 → step 4 → miscalibration, with numbers:

```text
copied unanimity (one lineage, five votes)
  dependence-blind reader believes   0.98625
  observed unanimity accuracy        0.70029
  -> ~0.286 absolute over-confidence, verified against ground truth

independence-aware reader believes   0.70168   (abs. calibration error 0.00139)
```

This is a demonstration that losing dependence structure inflates confidence by a large, measurable, calibration-checkable amount. It is **not** a demonstration that a *provenance error* causes that loss: assay 001 supplies the topology exogenously (`independent / mixed / shared_bias / copies`); nothing in it generates descendants or corrupts a genealogy.

Assay 005 is the closest existing approach to P1 and is **not** the same experiment. It corrupts provenance labels across three profiles (`clean` 0/0, `moderate` 25% missing / 10% wrong, `harsh` 50% missing / 20% wrong) and scores **query-allocation regret and oracle utility**. Posteriors are computed as an intermediate, and a `hard_cluster_count` exists inside the method, but neither effective-source count nor confidence inflation is a registered criterion. Its finding — soft provenance degrades more gracefully than hard categorical ancestry — is about **decision quality under label noise**, not about evidence cardinality.

A caution that must survive into P1: assay 001's own `N_eff` correction is well calibrated only at the endpoints, and drifts in between (`shared_bias` +0.038 over-confident; `mixed` −0.027 under-confident). **Effective source count is therefore an instrument that itself needs calibration reporting** — it cannot be read as if it were ground truth. This is a further reason to report count and calibration as separate readouts rather than deriving one from the other.

---

## 4. The two structural breaks

**Break A — nothing joins ancestry-loss mechanisms to cardinality readouts.**

The two halves of the chain are established in different classes, and the classes are separated by exactly the thing the hypothesis asserts:

```text
C1 (rodent):  can INDUCE binding/ancestry corruption causally
              cannot MEASURE source count or calibrated confidence

C3 (human):   can MEASURE source count and calibrated confidence
              does not INDUCE ancestry loss -- it STIPULATES ancestry in the
              stimulus materials ("these three reports trace to one primary source")

C6 (REE):     can measure everything
              supplies dependence topology exogenously; no descendant generation
```

No located experiment induces ancestry loss *through a memory or inference process* and then measures the resulting independence estimate. That join — not either half — is the branch's remaining content, and it is the reason the branch is still worth running rather than being closed as already-known.

**Break B — step 5 has no implementation anywhere.**

`grep -il replay scripts/convergence_signal_synthetic_assay_00*.py` returns nothing. P3 is entirely unimplemented, and the clinical and rodent literatures supply no cardinality-across-replay measurement either. The recursive-amplification hypothesis H2 is currently supported by no evidence in any direction, positive or negative — it is unaddressed rather than weakly addressed.

---

## 5. The correction: false independence is a healthy-human baseline, not a psychosis signature

This is the substantive update, and it did not come from the hippocampal campaign — it came from auditing the branch's own "not established" row against a literature neither prior pull searched. The REE corpus contains no prior mention of any of it.

**Yousif, Aboody & Keil 2019, _The Illusion of Consensus: A Failure to Distinguish Between True and False Consensus_, Psychol Sci 30(8):1195–1204. [DOI 10.1177/0956797619856844](https://doi.org/10.1177/0956797619856844), PMID 31291546** (erratum Psychol Sci 2020;31(8):1053).
Four experiments. Participants were **equally confident** in conclusions drawn from a true consensus (multiple independent primary sources) and a false consensus (multiple reports tracing to one primary source), with content held constant. The effect persisted immediately after participants had explicitly stated that true consensus was more believable.

That is the P1 design, already run, in healthy adults, and it satisfies the ladder's critical criterion for H1.

**Connor Desai, Xie & Hayes 2022, _Getting to the source of the illusion of consensus_, Cognition 223:105023. [DOI 10.1016/j.cognition.2022.105023](https://doi.org/10.1016/j.cognition.2022.105023), PMID 35149359.**
Four experiments locate the moderator: the illusion appears when the **independence relation is ambiguous**, and attenuates when independence between primary sources is made explicit. People retain the capacity to discriminate; they do not deploy it by default under ambiguity.

**Weaver, Garcia, Schwarz & Miller 2007, _Inferring the popularity of an opinion from its familiarity: a repetitive voice can sound like a chorus_, J Pers Soc Psychol 92(5):821–833. [DOI 10.1037/0022-3514.92.5.821](https://doi.org/10.1037/0022-3514.92.5.821), PMID 17484607.**
Six experiments. Repeated expression by **one** group member inflates estimated prevalence of the opinion, and the effect holds even when perceivers are consciously aware all statements came from one speaker. Mechanism attributed to accessibility rather than deliberate inference about repetition.

### What this changes

1. **The row in the evidence map is wrong and should be read as corrected here.** `dependent descendants become independent votes` is directly established. What remains unestablished is the *ancestry-loss route* to it (Break A) — the C3 studies never corrupt a genealogy, they present one.
2. **The psychosis question is reframed, and narrowed.** If false independence is the healthy default under ambiguity, then "psychosis inflates confidence by losing ancestry" is the wrong hypothesis shape — the baseline already does that. The defensible question becomes: **is the independence-discrimination capacity that Connor Desai 2022 shows is recoverable under explicit cueing selectively unavailable, or not deployed, in psychosis?** That is a different and more tractable claim than a lesion-style account, and it is congruent with the existing pull's finding that source-monitoring deficits are heterogeneous and neither necessary nor sufficient.
3. **P1's purpose changes.** P1 is no longer a first demonstration that ancestry corruption can inflate confidence — humans already show that. P1's value is now the **route**: whether an inflation of this shape can be produced by corrupting a genealogy *representation* inside an inference architecture, rather than by presenting misleading source information to an intact one.
4. **The ambiguity finding upgrades P2 from housekeeping to a primary result.** Connor Desai 2022 makes `ABSENT` / `SOFT` the scientifically loaded conditions, not `FALSE_SPLIT`. The ladder's P2 question ("does unknown ancestry default to independent?") is now the condition under which the human effect actually appears. A REE architecture that shows inflation only under explicit `FALSE_SPLIT` and not under `ABSENT` would be diverging from the human pattern, and that divergence should be reported rather than treated as a pass.

**Weakest link in this class, stated:** these are non-clinical judgment studies with stipulated source structure. They establish the cardinality step and its ambiguity moderator. They say nothing about memory, replay, or psychosis, and must not be transported to any of those.

**The one clinical bridge located, with its weakness:** Moritz, Köther, Woodward, Veckenstedt, Dechêne & Stahl 2012, _Repetition is good? An Internet trial on the illusory truth effect in schizophrenia and nonclinical participants_, J Behav Ther Exp Psychiatry 43(4):1058–1063. [DOI 10.1016/j.jbtep.2012.04.004](https://doi.org/10.1016/j.jbtep.2012.04.004), PMID 22683551. Repetition raised subjective truth in both groups; patients high on positive symptoms showed an **excessive** truth effect for delusion-relevant emotional items. Limits are severe and acknowledged by the authors: online recruitment, probable but not externally validated diagnoses, no psychiatric control group. It is also repetition of the *same statement*, not descendants of a lineage counted as independent witnesses. Treat as suggestive of a clinical amplification of repetition-driven belief, and as no evidence at all about ancestry cardinality.

---

## 6. What the hippocampal campaign actually contributes

Audited against §8 of the adjudication, which claims a real but bounded connection. **That bounding is correct.** E33, E43 and E34 do not show descendants treated as independent witnesses, do not show source uncertainty inflating confidence, and do not bear on psychosis. Nothing in the campaign's 43-source matrix supplies a cardinality or calibration readout, because no rodent preparation can.

The campaign's contribution is to a part of the chain the branch previously held only as an assumption: **that a nervous system contains machinery which generates dependent descendants and can misbind them.**

| Campaign source | What it licenses for the provenance branch | What it does not license |
|---|---|---|
| **E33** Ramirez et al. 2013, PMID 23888038 | Binding is causally manipulable; a reactivated internal context can acquire an association with an outcome experienced elsewhere. Step 1 has a causal existence proof. | Nothing about counting. Fear generalisation is not confidence inflation. |
| **E43** Zaki et al. 2024/25, [DOI 10.1038/s41586-024-08168-4](https://doi.org/10.1038/s41586-024-08168-4), PMID 39506117 | Offline co-reactivation causally links temporally separated memories. Replay is a *demonstrated* generator of cross-episode relations — the descendant-generating process P1 and P3 assume. | Nothing about ancestry loss or independence. In E43 the linking is **adaptive**, which makes it a control, not a pathology model (§7). |
| **E42** van de Ven et al. 2016 | Offline reactivation perturbation is tractable and its effects are *selective* by assembly stability — so a replay manipulation must stratify, not treat replay as one thing. | Not universal map repair. |
| **E20 / E32** SWR blockade negative; Gillespie et al. 2021 | Replay content reflects selected past experience rather than current plan, and blocking it does not degrade everything. Constrains what a "replay descendant" is and supplies the healthy-replay arm. | No evidence replay adds evidential weight. |
| **E30** Rule & O'Leary 2022, [DOI 10.1073/pnas.2106692119](https://doi.org/10.1073/pnas.2106692119), PMID 35145024 | A named, formal rival for **P6**: a stable readout can track a drifting code with no explicit lineage representation. This is the ladder's own stop condition ("dependence can be handled equally well without genealogy") given a concrete implementation to compete against. | Not proof that biology lacks genealogy. |
| **E34** Berres et al. 2024/25 | Source binding can be maintained across sleep intervals — behavioural only. | No hippocampal causality; no confidence inflation. |

**Net:** the campaign converts P1's descendant-generation step and P3's replay manipulation from stipulation into biologically motivated design, and hands P6 its strongest competitor. It moves no step of the chain from unestablished to established. This warrants refinement of P1/P3/P6 — and specifically **not** a separate hippocampal-provenance assay family, which would duplicate the ladder.

---

## 7. Refinements to P1 (replacing nothing; adding four requirements)

P1 as written creates four descendants of `e0/H` and varies ancestry representation. Retained. Added:

**P1-R1 — descendants must be *generated*, not stipulated.** The distinguishing content of this branch is Break A: humans already show the cardinality error when ancestry is *presented* to them. P1 earns its place only if the replay/retrieval/prediction descendants are produced by the architecture's own processes and the ancestry representation is corrupted *inside* it. A version of P1 that hands a fixed evidence graph to a reader reproduces assay 001 plus Yousif 2019 and adds nothing.

**P1-R2 — an adaptive-linking positive control, from E43.** Zaki et al. show offline linking of two genuinely distinct experiences is a normal, useful operation. P1 must include an arm where two descendants derive from **genuinely different world events** and are linked offline. Correct behaviour is that association strength rises while effective independent-source count stays at two. An architecture that raises the count here is failing in the opposite direction — collapsing distinct sources — and that failure must be detectable, not silently scored as a pass.

**P1-R3 — a legitimate-computation control, anchored to E30.** Confidence may rise lawfully when further computation extracts previously unused information from a fixed observation; this is the forbidden gain's nearest neighbour and the easiest thing to mistake for it. Required arm: hold the external observation set fixed, permit repeated computation that demonstrably improves an estimate of the *original* event (the E30 regime — a readout tracking a drifting code without new evidence, with no ancestry variable at all). The predeclared correct signature is:

```text
legitimate computation:  calibration improves, effective source count UNCHANGED
false independence:      effective source count rises, calibration DEGRADES
```

A design that cannot separate these two has not tested the hypothesis. This is the single most important control in the ladder, because a false positive here would be indistinguishable from ordinary competent inference.

**P1-R4 — genuinely independent new observation control.** Already implied by the ladder's global red-team list; promoted to a required P1 arm. Adding a real second world observation must raise both count and confidence, with calibration preserved. This is the positive control that shows the count readout has dynamic range in the correct direction, without which a null under corruption is uninterpretable.

---

## 8. Refinements to P3

**P3-R1 — stratify replay by kind, per E42/E32.** Replay is not one operation. The design must separate (a) content rehearsal of a single episode, (b) relational linking across episodes (the E43 operation), and (c) prediction-generated descendants. The dangerous signature — confidence rising monotonically with replay count at fixed external evidence — is only interpretable if it is attributable to one of these. A replay-count main effect pooled across kinds is not a result.

**P3-R2 — the healthy-replay arm is mandatory and must be able to pass.** E20's SWR-blockade negative and E30's self-healing codes both indicate that offline processing can improve representation without adding evidence. P3 needs an arm in which replay improves retrieval fidelity while effective source count stays flat, and it must be possible for this arm to produce that result. If every replay arm inflates the count, the instrument is measuring replay exposure, not genealogy.

**P3-R3 — match retrieval quality before attributing an interaction to ancestry.** Corrupted-ancestry conditions may also retrieve better or worse. The ancestry × replay-count interaction is only admissible at matched retrieval quality; otherwise the interaction is a retrieval effect wearing a provenance label. This mirrors the campaign's own repeated requirement to match local competence before claiming an interface effect.

**P3 falsifier, restated with the campaign's addition:** no ancestry × replay-count interaction at fixed external evidence *and matched retrieval quality* weakens H2. Given Break B, H2 currently has no evidence in either direction — P3 is the branch's highest-information unrun assay, and this should be stated plainly rather than left implicit behind P1.

---

## 9. Refinements to P2 and P6

**P2** is promoted in priority per §5.4: Connor Desai 2022 makes ambiguity-about-independence the empirically identified trigger of the human effect, so P2's three defaults (independent / maximally dependent / distribution over shared ancestry) are testing the exact condition under which the phenomenon is known to appear. P2 should report against the human pattern as an external comparator, not only against internal regret.

**P6** gains E30 as the named implementation to beat. The comparison should be explicit genealogy vs. E30-style lineage-free tracking vs. no genealogy, at matched information. If the lineage-free tracker matches explicit genealogy on calibration and duplicate-evidence resistance, the ladder's stop condition ("dependence can be handled equally well without genealogy") fires — and E30 is the concrete thing that would fire it.

---

## 10. Four readouts, never collapsed

Kept separate at every rung, as the parent ladder, the prior pull and this audit all independently require:

```text
1. association strength        (E43/E33 class -- did a relation form?)
2. source attribution          (P(external | representation); C2/C3 class)
3. effective independent-source count   (the cardinality variable)
4. calibration against world truth      (confidence vs observed accuracy)
```

Readouts 3 and 4 must be reported **separately and both**, not with one derived from the other: assay 001 shows the `N_eff` instrument is itself miscalibrated away from the endpoints (§3), so a count-derived confidence would bake the instrument's error into the result. Readout 1 rising with 3 flat is the E43 adaptive-linking signature. Readout 2 changing with 3 and 4 flat is the H0 source-label-only outcome, which remains a live and respectable result.

---

## 11. Falsifiers after this audit

The branch weakens or should be abandoned if:

1. content-matched ancestry corruption changes source attribution and association strength but leaves effective source count and calibration intact (**H0**, and still the most likely single outcome);
2. inflation appears only when ancestry is *presented* as split, and never when a genealogy representation is corrupted internally — the branch then reduces to Yousif 2019 and contributes nothing beyond it (**this is the Break A falsifier, and the sharpest one**);
3. E30-style lineage-free dependence tracking matches explicit genealogy on calibration and duplicate resistance (**P6 stop condition, now with a named competitor**);
4. no ancestry × replay-count interaction survives matched retrieval quality (**H2 falsified**);
5. the legitimate-computation control (P1-R3) is indistinguishable from the false-independence signature under the chosen instruments — the hypothesis is then untestable as posed and the instruments must be rebuilt before any result is reported;
6. the effect requires an explicit hand-coded provenance-error → confidence bonus rather than emerging from the inference rule;
7. confidence effects disappear once task performance is matched.

A negative result remains informative: it would separate source attribution from evidence cardinality, which the clinical literature has never done.

---

## 12. Epistemic boundary

- **No psychosis inference is drawn from any rodent or synthetic result here.** C1 preparations cannot measure confidence or source count; C6 is a synthetic architecture. Neither is evidence about a clinical syndrome, and the direction of travel is one-way: the clinical literature constrains the assays, the assays do not license clinical claims.
- **The C3 finding is about healthy adults**, and its principal consequence (§5.2) is *deflationary* for the psychosis framing: it removes "confidence inflates when ancestry is lost" from the set of things psychosis needs to explain, and replaces it with the narrower question of whether the discrimination capacity is deployed.
- The strongest statement still justified is the one the existing pull already reached, and this audit does not extend it: source- and self-monitoring abnormalities are repeatedly observed in psychosis, particularly around hallucinations, and are neither universal nor sufficient.
- The engineering rule — *a hypothesis must not cite its own descendants as independent witnesses* — survives all of the above, and is now supported by a healthy-human demonstration that the failure mode is the default rather than an exotic one. Its value to error-tolerant artificial cognition does not depend on the psychosis analogy holding.

---

## 13. Remaining debts

1. **Break A is the branch.** Design P1 so that ancestry loss is internal and generated (P1-R1), or the branch has no content beyond published human work.
2. **Break B is unaddressed.** P3 has no implementation; no assay contains a replay loop.
3. The C3 literature was not exhaustively swept — this audit located it by targeted query against a specific wrong row in the evidence map. A dedicated tranche over judgment/testimony/redundancy-neglect work is owed before the corrected row is treated as final.
4. Whether the consensus-illusion paradigm has ever been run in psychosis or delusion-proneness was searched and **nothing was located**; absence of a located study is not proof of absence, and this is the most direct empirical test of the reframed question in §5.2.
5. Moritz 2012 (PMID 22683551) is the only clinical repetition-belief bridge found and is methodologically weak; it needs replication status checked before it bears any load.

---

## Compact statement

> The hippocampal campaign supplies the machinery that generates dependent descendants and can misbind them, and nothing about counting them — exactly as its own §8 states. The audit's larger finding is elsewhere: treating one lineage as several independent witnesses is a documented **healthy-human default under ancestry ambiguity**, not an unestablished conjecture and not a psychosis signature. What no experiment in any class has done is join the two — induce ancestry loss through a memory or inference process and then measure the independence estimate it produces. That join, and the untouched replay-amplification interaction, are the whole of what P1 and P3 remain worth running for.
