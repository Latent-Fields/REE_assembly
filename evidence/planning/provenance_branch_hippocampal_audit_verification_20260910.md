# Provenance branch — verification of the hippocampal-campaign audit, and two findings it missed

**Date:** 2026-09-10T19:14:52Z
**Status:** verification and assay refinement. Registers, promotes, implements, queues and scores nothing. Makes no diagnostic assertion about psychosis. Edits no prior artifact except a cross-reference block appended to the ladder (§9).
**Task as posed:** audit whether the hippocampal campaign warrants a substantive update to the provenance/psychosis branch.
**Answer:** the campaign question was already audited and answered today, correctly, and this document verifies that independently (§2). The update this document adds comes from two places the landed audit did not look: **inside REE's own claim registry** (§4) and **the internally-generated-repetition memory literature** (§5).

**Audited inputs, all on `REE_assembly origin/master` at time of writing:**

| Artifact | Commit |
|---|---|
| [`docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md`](../../docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md) §8 | `469632ebe3` |
| [`docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md`](../../docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md) | `b96dfa1dd6`, `dfd7af8bd0` |
| [`provenance_false_evidence_multiplication_experiment_ladder.md`](provenance_false_evidence_multiplication_experiment_ladder.md) | `ec103cf3c1` |
| [`provenance_psychosis_literature_pull_20260909.md`](provenance_psychosis_literature_pull_20260909.md) | `b9e1ba7885` |
| [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) | `f7b19654d8` |
| [`provenance_harness_generated_ancestry_design.md`](provenance_harness_generated_ancestry_design.md) (P1) | `f2869ac00e` |
| [`provenance_p3_replay_amplification_design.md`](provenance_p3_replay_amplification_design.md) (P3) | `0653724f99` |
| [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) | `b682aed66f` |

---

## 1. Verdict

**A substantive update is justified, and it is not the one the task anticipated.**

The hippocampal campaign's contribution to this branch was already audited at `f7b19654d8` (2026-09-10 06:51 UTC) and its three residual debts discharged at `f2869ac00e`, `0653724f99` and `b682aed66f` (18:54–19:00 UTC, minutes before this session began). Every specific requirement of the task — the five-step evidence audit, the separate treatment of retrospective memory linking / false contextual association / clinical source monitoring, the independent-observation control, the legitimate-computation control, the four separate readouts, and the refinement rather than duplication of P1/P3 — is already discharged in those documents. Re-deriving them would be duplication. §2 verifies them instead.

The update this document adds is three findings, in descending order of consequence:

1. **The branch has an unrecognised REE-internal neighbour, and the two lineages do not reference each other in either direction.** The `MECH-542 / MECH-543 / MECH-544` source-sensitive-permeability cluster was registered 2026-09-08 — *one day before* this branch opened — and `MECH-544`'s predicted routes already include "repeated fictional trajectories distorting perceived likelihood," which is this branch's step 4 driven by internal repetition. Its literature review already holds the imagination-inflation class and the fluency-versus-source-tag dissociation that the judgment-class tranche independently rediscovered ten hours later. §4.
2. **Break B — "step 5 has no evidence in any direction, in any class" — is too strong, and the correction changes what P3 measures.** There is a human evidence class in which repetition is *internally generated* rather than presented, it contains a monotonic dose-response on the source-attribution readout, and it has been run once in psychosis. It contains no cardinality measurement, so the branch's core verdict survives; what changes is that P3's discriminating contribution narrows to readouts 3 and 4, and inherits two documented confounds it does not currently control. §5.
3. **P1's genealogy representation commits REE to a stored-tag architecture that the founding source-monitoring framework denies** — and REE's own corpus already flagged exactly this divergence for `MECH-544`, with an empirical discriminator attached. §6.

None of the three weakens the campaign's §8 self-bounding, which §2 confirms is accurate. All three sit on the branch's own side of the boundary.

---

## 2. Verification of the landed audit

Not a re-derivation. Each load-bearing factual claim of `f7b19654d8` was checked against the artifact it cites.

| Claim under check | Method | Result |
|---|---|---|
| The 2026-09-09 pull records `dependent descendants become independent "votes"` as **not directly established** | `/usr/bin/grep` on the pull | **Confirmed.** Line 556; adjacent rows 555 and 557 are the ancestry-loss and replay-cardinality rows, both also so marked |
| No REE assay contains a replay loop | `/usr/bin/grep -il replay` over all six `convergence_signal_synthetic_assay_00*.py` | **Confirmed**, exit 1, six files present |
| Assay 001: dependence-blind reader believes 0.98625; unanimity accuracy 0.70029; independence-aware 0.70168 | `evidence/experiments/convergence_signal_synthetic_assay_001/runs/20260909_seed7/manifest.json` | **Confirmed to all recorded digits** (`0.9862545956188494`, `0.70029`, `0.7016832519230698`). Derived figures check: over-confidence `0.28596`, independence-aware calibration error `0.00139` |
| The `N_eff` instrument is calibrated at the endpoints and drifts between | same manifest | **Confirmed** in shape: `n_eff` 5.0 / 1.00080 at the endpoints, 1.31529 and 2.72064 in the intermediate regimes |
| Thirteen cited PMIDs exist and carry the stated journal, year, volume, pages and DOI | NCBI E-utilities `efetch` | **All confirmed:** 31291546, 35149359, 35579865, 17484607, 32599310, 22683551, 39603232, 32437188, 41563579, 41497523, 40121821, 32721273, 37691811. The Yousif corrigendum (32721273) does point at 31291546 |
| Yousif 2019 content: participants *equally confident* in true and false consensus, robust immediately after explicitly endorsing the distinction | abstract | **Confirmed verbatim** |
| Xie & Hayes 2022 content: "only a minority of individuals conform to Bayesian predictions" | abstract | **Confirmed verbatim** |
| The consensus-illusion / source-independence paradigm has never been run in psychosis | eight independent `esearch` formulations, deliberately different from the tranche's (`"illusion of consensus" AND (schizophrenia OR psychosis OR delusion)`, `psychosis AND "source independence"`, `"source monitoring" AND "independent evidence"`, `"double counting" AND evidence AND belief`, `replay AND confidence AND "source memory"`, `delusion AND redundancy AND evidence`, `"redundancy neglect" AND memory`, `"circular inference" AND schizophrenia`); all returned hits inspected at title level | **Confirmed.** The seven hits on the consensus/psychosis query are term-expansion artifacts (Roelofs illusion, Parkinson's psychosis, magical thinking, McCollough effect); none is the paradigm. The negative is now doubly searched |
| The hippocampal campaign §8 self-bounding is accurate | §8 read against matrix rows E33/E34/E43 and the campaign's own debt 7 | **Confirmed.** §8 states the bound, names P1/P3 as the correct home, forbids a duplicate family, and already requires the four separate readouts, the independent-observation positive control and the legitimate-computation control. The task's requirements were largely anticipated *by the campaign itself* |

**No error was found in the landed audit.** Its verdict — update justified as a correction plus bounded refinement, not a new assay family — stands unmodified. The findings below are additions to it, not corrections of it.

One statement in it is now over-taken rather than wrong: §13 debts 3, 4 and 5 are discharged by `b682aed66f`, which swept the judgment class, established the psychosis-paradigm absence as properly searched, and established Moritz 2012 as unreplicated with no clinical follow-up in thirteen years.

---

## 3. Evidence classes, extended by one

The task's instruction to hold evidence classes apart is what produced findings 2 and 3. The landed supplement kept six classes (C1 rodent causal, C2 clinical source monitoring, C3 human judgment/consensus, C4 computational, C5 clinical repetition-belief, C6 REE synthetic). A seventh is needed, and its defining property is exactly the one the branch cares about:

| Class | Repetition is… | Readouts physically available |
|---|---|---|
| **C3** human judgment / consensus | **presented** in the stimulus (three reports, one primary source) | belief, confidence, estimated source count |
| **C7** internally-generated repetition (imagination inflation) | **generated by the participant**, on instruction, from their own memory/imagery | occurrence confidence, source attribution, dose-response in repetition count; **no** source-count measure |

C7 is not a subdivision of C3 and not a subdivision of C5. C5 (illusory truth) repeats *the same external statement*. C3 *presents* a source structure once. C7 is the only located human class in which **the participant's own internal generative process is the thing that repeats**, which is the operation P3 manipulates. That is why its absence from both prior pulls matters, and why adding it changes P3 rather than merely lengthening a bibliography.

---

## 4. Finding 1 — the unrecognised REE-internal neighbour

`MECH-542`, `MECH-543` and `MECH-544` were registered 2026-09-08 from the 2026-09-07 culture-as-distributed-precommit package, all `status: candidate`, `implementation_phase: v4`, located at `docs/architecture/culture_distributed_precommit.md`. `MECH-544` — *"Permeability pathology and source-tag decay"* — asserts that the selective permeability enabling cultural learning necessarily creates its failure modes, and lists among its predicted routes, verbatim from `claims.yaml`:

> repeated fictional trajectories distorting perceived likelihood

That is internal repetition raising a likelihood estimate with no new external evidence. It is this branch's step 4, reached by this branch's step 5's mechanism, registered as a claim one day before the branch's parent thought was written.

**The gap is bidirectional and was checked in both directions.** No provenance-branch artifact (thought, ladder, either pull, the campaign audit, the P1 or P3 design) mentions `MECH-542/543/544` or the word *permeability*. Neither the culture thought-intake nor the architecture document mentions false independence, evidence cardinality, or independent-source count. Two lineages, same repository, one day apart, no edge between them.

`MECH-544`'s literature review (`evidence/literature/targeted_review_source_sensitive_permeability/`) already contains:

- **Garry, Manning, Loftus & Sherman 1996**, *Imagination inflation: imagining a childhood event inflates confidence that it occurred*, Psychon Bull Rev 3(2):208–214, [DOI 10.3758/BF03212420](https://doi.org/10.3758/BF03212420), PMID 24213869 — supports at 0.65. **Already in the REE corpus.**
- **Johnson, Hashtroudi & Lindsay 1993**, *Source monitoring*, Psychol Bull 114(1):3–28, PMID 8346328 — supports at 0.72. **Already in the REE corpus**, and the anchor of §6 below.

And it already draws the distinction the judgment-class tranche independently arrived at ten hours later as P1's missing control: that imagination inflation has two routes, *source misattribution* (generated detail recovered and mistaken for experience) and *familiarity misattribution* (imagining raises fluency, fluency is read as occurrence), and that "an assay that scored every occurrence error as tag decay would be conflating the two."

### The demarcation, which is the useful product of this finding

The two branches must be **distinguished, not merged**, and the distinguishing variable is already one of this branch's four readouts:

```text
MECH-544  permeability:  a hypothetical-source frame fails to PROTECT a variable
                         it should protect (occurrence, source truth, responsibility)
                         -> moves readouts 1, 2 and 4

this branch cardinality: one lineage is COUNTED as several independent witnesses
                         -> moves readout 3, and 4 through it
```

They share readouts 2 and 4 and differ on readout 3. This is the sharpest available statement of what the provenance branch uniquely contributes, and it comes from inside REE rather than from the literature. It also names a live duplication risk: **an assay that manipulates internal repetition and measures occurrence confidence is `MECH-544`'s assay.** Only the addition of readout 3 makes it P3's. P3's design should say so, because without that sentence the two claim lineages will converge on one experiment and each will read the other's result as its own.

One asymmetry worth recording: `MECH-544` is `implementation_phase: v4`, and this branch's assays are synthetic and unphased. The demarcation is therefore about *what each assay is evidence for*, not about scheduling.

---

## 5. Finding 2 — Break B is over-stated, and the correction narrows P3

Break B, as landed, says step 5 "is currently supported by no evidence in any direction, positive or negative — it is unaddressed rather than weakly addressed," and the P3 design repeats this. **On the cardinality and calibration readouts that is exactly right and this document does not disturb it.** On the source-attribution readout it is wrong: C7 contains a repetition dose-response, and it has been run in psychosis.

All sources below were verified by `efetch`, and corpus-novelty was checked by grep over the whole of `REE_assembly`: **every one is new to the REE corpus** (0 files each for PMIDs 9519694, 15209367, 11531226, 20488556, 38324581, 40748997). Garry 1996 (§4) and Johnson 1993 are the class's only prior representatives, both under `MECH-544` rather than under this branch.

**Goff & Roediger 1998**, *Imagination inflation for action events: repeated imaginings lead to illusory recollections*, Mem Cognit 26(1):20–33, [DOI 10.3758/bf03211367](https://doi.org/10.3758/bf03211367), PMID 9519694.
Two experiments. Participants heard, performed, or imagined performing simple action statements; in a second session they imagined performing actions **one, three, or five times**; a third session required them to judge whether each statement had been *carried out, imagined, or merely heard* — a source-monitoring test. Primary finding: **increasing the number of imaginings caused participants to remember having performed an action they had not**, for statements heard-but-not-performed and for statements never heard at all.

This is P3's replay-count axis, already run, in healthy humans, with a monotonic result — on readout 2.

**Sharman, Garry & Beuke 2004**, *Imagination or exposure causes imagination inflation*, Am J Psychol 117(2):157–168, PMID 15209367.
Confidence in childhood events rated, then complex fictitious events imagined **or paraphrased** 0, 1, 3 or 5 times, then re-rated. Confidence rose "regardless of whether they were imagined or paraphrased," and there was **no repetition effect beyond that of a single exposure**; the authors attribute the effect to processing fluency.

So on the *confidence* readout the dose-response is flat beyond one exposure, while on the *source-attribution* readout (Goff & Roediger) it is monotonic. Materials differ (simple action statements versus complex fictitious autobiographical events), so this is not a direct contradiction — but it is a **readout dissociation on the replay-count axis**, in the direction that vindicates the branch's insistence on never collapsing the four readouts, and no branch document currently records it.

**Pezdek & Eddy 2001**, *Imagination inflation: a statistical artifact of regression toward the mean*, Mem Cognit 29(5):707–718, discussion 719–729, [DOI 10.3758/bf03200473](https://doi.org/10.3758/bf03200473), PMID 11531226.
Reproduced Garry 1996 and replicated its result — and showed that ratings for events initially rated *high* in likelihood *decreased* under the same conditions, for imagined targets, non-imagined targets and controls alike. Conclusion: the effect attributed to imagination inflation is a regression-toward-the-mean artifact of the pre/post rating design.

This is a specific, documented, methodological threat to any measurement of the form *"confidence rises with replay count at fixed external evidence"* — which is P3's dangerous signature, stated in the ladder and in the P3 design. It is survivable, and §7 says how.

**Mammarella, Altamura, Padalino, Petito, Fairfield & Bellomo 2010**, *False memories in schizophrenia? An imagination inflation study*, Psychiatry Res 179(3):267–273, [DOI 10.1016/j.psychres.2009.05.005](https://doi.org/10.1016/j.psychres.2009.05.005), PMID 20488556.
A group with psychosis and a control group performed or imagined performing action statements **one or four times**, with a source-monitoring discrimination test 24 h later. Two findings, and their combination is what matters: patients **were** more susceptible to source-monitoring errors, especially judging an imagined action as performed; **both groups showed comparable levels of imagination inflation.**

**Dudek & Polczyk 2024 (protocol) / 2025 (results)**, *Memory distrust and imagination inflation: a registered report*, PLoS One 19(2):e0297774, PMID 38324581 → PLoS One 20(8):e0327638, PMID 40748997.
Registered report, N=279 completed. Memory distrust as a trait was **unrelated** to imagination inflation; the predicted state effect in participants sensitised to discrepancies by source and/or perspective cues was **not confirmed**. A registered-report-grade null on the individual-difference route. (Stated precisely: the cueing manipulation failed to *moderate*; the study was not designed as a main-effect test of cue efficacy, and should not be read as one.)

### What this changes

1. **Break B should be restated, not withdrawn.** The accurate form: *step 5 has no evidence in any direction on effective independent-source count or calibration, in any class. On source attribution it has a healthy-human monotonic dose-response (Goff & Roediger 1998), a flat-beyond-one-exposure result on the confidence readout with a fluency explanation (Sharman 2004), an artifact critique of that confidence measure (Pezdek & Eddy 2001), and one clinical run (Mammarella 2010).* That is a stronger and more useful claim than "unaddressed," because it tells P3 which readout it is the first to measure.
2. **P3's information value is not reduced — it is re-pointed.** P3 remains the branch's highest-information unrun assay. What changes is why: not because nothing is known about replay-count effects, but because everything known about them is on the readout the branch says is *not* the pathology. A P3 that found a replay-count main effect on readout 2 alone would be reproducing Goff & Roediger 1998 in silico, and should be predeclared as such rather than reported as a finding.
3. **The reframed psychosis question of supplement §5.2 has one existing, directly relevant data point, and it is partly negative.** Mammarella 2010 found the baseline capacity difference (elevated source-monitoring errors in patients) **without** the amplification difference (comparable inflation across groups). Read against the reframing — is the discrimination capacity selectively unavailable, or merely not deployed? — the located clinical evidence supports *elevated baseline source-attribution error*, and does **not** support *elevated repetition-driven amplification*. The recursive-amplification limb of the psychosis extension is now weakly disfavoured on its nearest available clinical measurement, and this should be recorded as such rather than left as an open conjecture. It remains a single small study on a different readout from the branch's target; it is a constraint, not a refutation.
4. **The clinical-bridge statement needs widening.** The supplement and the tranche both record Moritz 2012 as the *only* located clinical repetition-belief bridge. Mammarella 2010 is a second, and on the branch's own criteria a better one: an in-person clinical sample, a source-monitoring discrimination task rather than a subjective-truth rating, and a manipulation of the repetition count of **internally generated** content rather than of an external statement. It carries its own limits (small clinical sample, single site, 2010, no located replication) and no assay should depend on it alone.
5. **The fluency rival is now triple-sourced and needed at two rungs.** The tranche derived it from Weaver 2007 and O'Donnell 2023 for P1; Sharman 2004 supplies it for P3; and `MECH-544`'s own review already recorded it as the familiarity-misattribution route. A corrupted genealogy that yields four separately-retrievable descendants also yields four retrieval events, so fluency will explain a positive result at either rung unless excluded by design.

**What C7 does not do:** it contains no measure of effective independent-source count, no manipulation of an ancestry representation, and no calibration-against-ground-truth. It does not close Break A, does not close the cardinality half of Break B, and licenses no psychosis inference of its own beyond Mammarella 2010's own stated finding.

---

## 6. Finding 3 — P1's stored-tag architecture, and an existing REE flag against it

The P1 harness design (§5.1–5.2 of `f2869ac00e`) specifies a genealogy representation as **state the architecture carries**: traces with source-family identifiers, directed ancestry edges carrying binding strengths in `[0,1]`, and a derived source-family partition obtained by thresholding connected components. Three degradation processes act on that state: **decay** (binding strength declines with elapsed time at rate `tau`), **interference** (binding reduced in proportion to content similarity to competitors), and **misbinding** (edges re-pointed with probability rising in content similarity). The four conditions are defined by comparing that edge set to ground truth.

That is a stored-tag architecture with a decay law. REE's own corpus already records, against `MECH-544`, that the founding framework denies the premise:

> MECH-544 speaks of source-tag decay, which presumes a tag that is stored and then weakens. The source-monitoring framework's central commitment is that there is no such tag: source is reconstructed each time, from features.

Johnson, Hashtroudi & Lindsay 1993's account is that memories do not arrive labelled — source is *attributed at retrieval*, by judgement processes weighing the qualitative characteristics of a remembered experience (perceptual detail, contextual and semantic accompaniment, recorded cognitive operations) against criteria that shift with task, motivation and care. Misattributions increase as candidate sources resemble each other, and occur while content is remembered accurately.

**This is not a transfer caveat; it has an empirical signature, already stated in the corpus.** A stored-tag system's errors track storage interval and interference. An attribution system's errors track the similarity between candidate sources and the decision criterion in force, and are **manipulable at retrieval without touching storage at all**.

P1's *interference* process is content-similarity-driven and therefore partially attribution-like, and its *misbinding* process is similarity-gated — so the design is not naively a pure decay model. But the similarity acts on **stored binding strength**, and the design carries **no retrieval-time criterion**: nothing in it can be manipulated at read time while storage is held fixed. So the divergence stands, and it is consequential in the way the corpus already warned: if REE reproduces the human phenomenon through a decaying stored edge set, it will have reproduced it by a route the biology does not use, and the two will come apart under retrieval manipulations.

**The remedy is an arm, not a redesign, and it is cheap because P1 already computes the partition by thresholding.** Add a **retrieval-attribution variant** in which the source-family partition is computed *at read time* from qualitative trace features against a **shiftable criterion**, with the stored edge set either absent or held constant. Then run the discriminator the corpus supplies:

```text
stored-tag route:      errors scale with elapsed interval and with interference load;
                       unchanged by a read-time criterion shift at fixed storage
attribution route:     errors scale with candidate-source similarity and with the
                       criterion; movable at read time with storage untouched
```

If both routes produce the same cardinality inflation, that is a genuinely strong result — the effect is architecture-independent, and the branch's engineering rule applies more widely than to systems that store genealogy. If only the stored-tag route produces it, P1's positive result is about REE's chosen implementation rather than about provenance representation in general, and must be reported that way. Either outcome is worth more than the current design's silence, and the choice `MECH-544`'s review says is "worth deciding deliberately rather than inheriting" is exactly this one.

---

## 7. Refinements — additions to P1 and P3, replacing nothing

Continuing the numbering of the landed supplement (`P1-R1`…`R4`, `P3-R1`…`R3`) and the tranche's fluency control. Recommendations; no edit made to either design document.

### P1-R5 — retrieval-attribution arm (from §6)

As specified in §6: a read-time attribution variant with a shiftable criterion, scored by the stored-tag-versus-attribution discriminator. **Predeclare which route the architecture implements before running**, because the design currently implements one without recording that a choice was made.

### P1-R6 — declare the `MECH-544` boundary in the design

One paragraph, stating that readouts 1, 2 and 4 alone are `MECH-544`'s territory and that P1's distinctive product is readout 3. Cheap, and it is what prevents two candidate claims from consuming one experiment's result.

### P3-R4 — regression-to-the-mean control (from Pezdek & Eddy 2001)

Mandatory, and it is the control most likely to be omitted because the synthetic setting makes it feel unnecessary. Two requirements:

1. **Prefer a per-count judgement to a pre/post confidence delta.** Goff & Roediger's dose-response survived the artifact critique that felled Garry's pre/post design precisely because a source-attribution judgement at each count is not a repeated rating of the same scale. P3 should read out at each replay count rather than differencing an initial and final confidence.
2. **If a pre/post delta is used anywhere, carry matched un-replayed items through the identical measurement schedule, and report their trajectory alongside.** Pezdek & Eddy's diagnostic was that the controls moved too, and in the mirror direction for initially-high items. A P3 that cannot show its un-replayed arm staying flat has not excluded the artifact.

Stated in the synthetic setting: any confidence readout that is itself noisy and re-measured will regress, and a monotone-looking rise across `0, 1, 2, 4, 8, 16` can be produced by measurement schedule alone.

### P3-R5 — exposure-without-internal-generation arm (from Sharman 2004)

P3-R1 already stratifies replay by kind (content rehearsal / relational linking / prediction-generated). Add a fourth level that is **not internal generation at all**: re-exposure to the trace without running the generative process. Sharman 2004 found paraphrasing as effective as imagining, and no effect beyond one exposure — so if REE's replay effect is reproduced by re-exposure, the result is fluency and not genealogy, whatever the ancestry condition says.

### P3-R6 — predeclare the Goff & Roediger outcome as a known result

A replay-count main effect on **readout 2 alone** (source attribution) is the *expected* human pattern and must be predeclared as a null-for-H2, not reported as a discovery. The dangerous signature requires readouts 3 and 4 to move, at flat readout 2 or in addition to it.

### P3-R7 — the clinical comparator, with its direction stated

Where P3 reports against a clinical comparator, Mammarella 2010 is the nearest one and its direction is *unfavourable* to the amplification limb: elevated baseline source error, comparable inflation. Record it as the constraint it is, so a positive P3 result is not read as confirming a clinical pattern the located clinical evidence does not show.

---

## 8. The four readouts, and why this document does not change them

Unchanged, and now with a fifth reason to keep them separate:

```text
1. association strength                  (did a relation form?)
2. source attribution                    (P(external | representation))
3. effective independent-source count    (the cardinality variable)
4. calibration against world truth       (confidence vs observed accuracy)
```

The reasons already on record: the `N_eff` instrument is itself miscalibrated away from the endpoints, so 4 must never be derived from 3; readout 1 rising with 3 flat is the E43 adaptive-linking signature; readout 2 moving with 3 and 4 flat is H0, a live and respectable result. Added here: **C7 dissociates readouts 2 and 4 on the replay-count axis itself** — monotonic on 2 (Goff & Roediger), flat-beyond-one-exposure on the confidence measure (Sharman) — and the `MECH-544` boundary is drawn *on readout 3*. A design that collapsed any pair would lose the demarcation between two REE claim lineages, not merely a measurement.

---

## 9. Ladder attachment

The ladder (`ec103cf3c1`) is unmodified since creation and contains **no reference to any of the four refinement artifacts** that now refine it — the audit supplement, the P1 harness design, the P3 design, or the judgment-class tranche. Each of those documents correctly declines to edit the ladder ("recommendations only — no edit made"), with the consequence that a session reading the ladder alone would see P1 and P3 in their unrefined form and none of the controls.

This document appends a cross-reference block to the ladder naming the five artifacts and what each contributes. It changes no rung, no condition, no readout and no stop condition. That is the whole of the edit; the refinements remain recommendations in their own documents, which is where the branch has chosen to keep them.

---

## 10. Falsifiers introduced by this document

The three findings above are themselves falsifiable, and their falsifiers are not the branch's:

1. **Finding 1 fails** if `MECH-544`'s "repeated fictional trajectories distorting perceived likelihood" turns out to be about likelihood-of-*future*-occurrence (a possibility estimate, which `MECH-542` explicitly *permits* to update) rather than perceived past occurrence. Then the two lineages do not overlap, the demarcation is unnecessary, and only the shared literature stands. The claim text supports the occurrence reading, but this was not adjudicated with the claim's owner.
2. **Finding 2's clinical limb fails** if Mammarella 2010's comparable-inflation result is underpowered for the group × repetition interaction. It is a single small clinical study reporting a null interaction, which is the weakest kind of null; the power analysis was not located and should be checked before the constraint bears any weight.
3. **Finding 3 fails** if P1's interference process, being content-similarity-driven, already reproduces attribution-route error scaling — in which case the retrieval-attribution arm is redundant rather than discriminating. This is directly checkable in the harness before building the arm: does interference load alone move errors with candidate-source similarity at fixed interval?
4. **The C7 class as a whole becomes inadmissible to this branch** if the imagination-inflation effect is wholly regression to the mean (Pezdek & Eddy's strong reading). Goff & Roediger's count-graded source-attribution result is not vulnerable in that way, so the class survives on that measure even under the strong reading — but the confidence-readout members (Garry 1996, Sharman 2004, Dudek 2025) would then be uninformative about step 4.

---

## 11. Epistemic boundary

- **No psychosis inference is drawn from any rodent or synthetic result.** The only clinical statements here rest on two human clinical studies (Mammarella 2010, Moritz 2012), both stated with their limits, and their combined direction is *deflationary* for the recursive-amplification limb.
- **C7 is human, and its healthy-adult members say nothing about psychosis.** Garry 1996, Goff & Roediger 1998, Sharman 2004, Pezdek & Eddy 2001 and Dudek 2025 are non-clinical and must not be transported to a clinical claim.
- **The strongest clinical statement still justified is unchanged** from the 2026-09-09 pull, and this document does not extend it: source- and self-monitoring abnormalities are repeatedly observed in psychosis, particularly around hallucinations, and are neither universal nor sufficient. Mammarella 2010 is consistent with that and adds that the *repetition-driven amplification* of source error may not differ by group.
- **Nothing here is a claim registration, promotion, demotion, queue mutation or scoring event**, and no substrate code was read or written. `MECH-542/543/544` were read from `claims.yaml` and not modified.
- The engineering rule — *a hypothesis must not cite its own descendants as independent witnesses* — survives all three findings. §4's demarcation makes it *narrower* and therefore more defensible: it is a constraint on evidence **cardinality**, distinct from the permeability constraint on which variables a hypothetical source frame may update.

---

## 12. Debts this document leaves

1. **The `MECH-544` demarcation is unowned.** §4 draws it; nobody has ratified it. It belongs in front of governance as a claim-relationship question (are `MECH-544` and this branch's cardinality target distinct mechanisms, or one claim registered twice from two directions?), not in a planning document. Not chipped here — governance owns claim dispositions.
2. **C7 was located by one targeted query family**, not swept. Forty-one PubMed records match `"imagination inflation"`, of which six are cited here and the rest were read at title level only. A dedicated tranche is owed if the class is to bear more than the design-control weight given it here.
3. **Mammarella 2010's power for its null interaction is unchecked**, and finding 2's clinical limb rests on it (§10.2).
4. **Libby 2003** (*Imagery perspective and source monitoring in imagination inflation*, Mem Cognit 31(7):1072–1081, PMID 14704022) and **Thomas, Bulevich & Loftus 2003** (*Exploring the role of repetition and sensory elaboration in the imagination inflation effect*, Mem Cognit 31(4):630–640, PMID 12872878) were located and verified as records but **not read**. The second in particular separates repetition from sensory elaboration, which is a P3-R5 refinement, and should be read before P3 is built.
5. **Break A remains the branch**, unchanged and undischarged. Nothing in this document brings the join any closer; C7 has no cardinality readout either.

---

## Compact statement

> The hippocampal campaign question was already audited correctly and its debts already discharged; this document verifies that rather than re-deriving it, and finds no error. The substantive update lies elsewhere. The branch's nearest neighbour is not in the literature but in REE's own registry — `MECH-544` already predicts internal repetition distorting perceived likelihood, and the two lineages are separated by exactly one of this branch's four readouts, the effective independent-source count. And step 5 is not unaddressed: internally-generated repetition already shows a monotonic dose-response on **source attribution** in healthy adults, a flat one on **confidence** with a fluency explanation and a regression-to-the-mean critique, and one clinical run in which patients made more source errors but showed *no more* repetition-driven inflation. P3 is therefore still the highest-information unrun assay — but it is the first measurement of readouts 3 and 4 across replay, not the first measurement of anything across replay, and it inherits three confounds that the class it was unaware of has already documented.
