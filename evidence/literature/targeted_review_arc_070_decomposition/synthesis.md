# SYNTHESIS -- ARC-070 Policy Decomposition on Prediction Failure (imagination-side event segmentation)

**Pull commissioned:** 2026-05-10 from the policy_primitive_granularity architectural family registration session (ARC-069 parent + ARC-070 + ARC-071 candidate / pending_design).
**Companion pull (parallel):** ARC-071 composition-via-repeated-grounding -- decoupled within the cluster, sibling lit-pull running concurrently.
**Date:** 2026-05-10. **Entries:** 7 papers (Zacks event-segmentation theoretical anchor, Schacter constructive-episodic-simulation core network, Badre rostro-caudal hierarchy, Koechlin cascaded control, Pfeiffer-Foster hippocampal forward sweeps, Schapiro CLS-within-hippocampus, McGovern-Barto bottleneck-state subgoal discovery).
**Source attribution:** the per-paper records cite PubMed entries with DOIs and PMIDs as listed; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull was commissioned

ARC-070 was registered 2026-05-10 from the user's observation about the rollout-chaining work: "the imagined chains may need splitting up into more chained behaviours or sometimes a number of chained behaviours together being realised to better be represented by a single behaviour." The decomposition direction (zoom in / re-segment imagined chains when chunks fail to ground) is one of two inverse architectural moves missing from REE substrate. ARC-069 is the parent commitment that policy primitives are dynamic; ARC-070 is the decomposition operator; ARC-071 is the composition operator (parallel pull).

ARC-070 has a particularly delicate substrate-design question: REE already has MECH-269 V_s (region-conditioned predictability scalar) as the cleanest existing trigger candidate, AND has MECH-288 event_segmenter on the OBSERVATION side. The architecturally load-bearing question for this pull is whether biology supports SHARED MACHINERY between observation-side and imagination-side event segmentation (in which case ARC-070 should be a bidirectional extension of MECH-288), or SEPARATE machinery (in which case ARC-070 needs its own dedicated substrate). The former is much cheaper to implement and is consistent with the substrate-economy that REE has tried to maintain; the latter would require a parallel module.

Five falsifiable verdicts were pre-specified in the briefing. The synthesis settles each at a stated confidence; one of them carries a substantive substrate-economy reframe in favour of bidirectional shared machinery.

---

## R1 -- Trigger primary: V_s drop / E2 disagreement / completion failure / mid-execution PE

### Verdict: PRIMARY trigger is V_s DROP on the chunk's region (operationalising prediction-error-on-chunk in event-segmentation theory). E2 forward-model disagreement and completion-signal failure are CONVERGENT secondary signals. Mid-execution PE is a DISTINCT phase that the same mechanism handles via R4. Confidence 0.78.

The evidence cluster:

- **Zacks et al. 2007 (Psychol Bull, PMID 17338600)** -- theoretical anchor. Event boundaries are perceived when transient prediction errors arise on the working event model. The framework is substrate-agnostic about WHICH predictive system generates the error; what matters is that an error pulse on the active predictive stream marks the boundary. Confidence 0.84.
- **Schapiro et al. 2017 (Phil Trans Roy Soc B, PMID 27872368)** -- substrate grounding. The hippocampal trisynaptic pathway implements pattern separation, which IS a region-conditioned discriminability operation. V_s as REE's pattern-separation-strength readout has a candidate biological basis. Confidence 0.74.
- **Pfeiffer & Foster 2013 (Nature, PMID 23594744)** -- substrate evidence. Hippocampal forward sweeps elaborate trajectories with cue-dependent dynamics. The substrate that generates the chunked-primitive sequence is the substrate that can re-segment it on prediction failure. Confidence 0.78.

The synthesis recommends V_s drop on the chunk's region as the PRIMARY trigger because (a) Zacks's framework is the canonical statement of PE-as-trigger and the field has not produced a stronger alternative, (b) MECH-269 V_s already exists as REE substrate and gives ARC-070 a natural integration point, (c) V_s is region-conditioned which matches the chunk's region-attribution naturally, (d) Schapiro 2017's pattern-separation account gives V_s a candidate biological basis. The remaining trigger candidates listed in the briefing (E2 forward-model disagreement, completion-signal failure, mid-execution PE) are framed as CONVERGENT secondary signals that may co-fire with V_s drop in many cases but should not be the primary trigger because they each have narrower applicability:

- E2 forward-model disagreement requires running BOTH chunk-grain and primitive-grain forward simulation in parallel, which doubles rollout cost and is not what biology appears to do (Pfeiffer-Foster's forward sweeps elaborate dynamically rather than compute parallel comparisons).
- Completion-signal failure (MECH-105 / ARC-028) only fires for chunks with explicit completion signals; not all chunked primitives have these.
- Mid-execution PE is a separate phase covered by R4; the same V_s mechanism can fire mid-execution.

The recommended child-MECH design therefore:

```
For each chunked primitive in the rollout proposal stream:
  Read V_s on the chunk's region (MECH-269 substrate)
  If V_s < V_s_decompose_threshold:
    Decompose the chunk into its sub-elements
    Re-evaluate the proposal stream over the decomposed sub-sequence
  Else:
    Keep the chunk at its current grain
```

The threshold V_s_decompose_threshold is a free parameter to be selected at child-MECH design time. The threshold may be different from MECH-269b's symmetric-V_s-gating threshold; ARC-070 reads V_s but does not gate via V_s in the MECH-269b sense, so the two consumers can have independent thresholds (this is checked against MECH-269b's symmetric-V_s-gating commitment in the substrate-disambiguation section below).

The R1 confidence is 0.78 -- moderate-high. The verdict is well-supported across multiple anchors, but the field has multiple viable trigger formalisations (PE pulses, novelty pulses, surprise pulses, free-energy minima) and the empirical disambiguation between them is not directly settled.

---

## R2 -- Observation/imagination substrate sharing: MECH-288 bidirectional or new module?

### Verdict: SHARED SUBSTRATE. ARC-070 should be implemented as a BIDIRECTIONAL EXTENSION of MECH-288 event_segmenter, accepting both observation and imagination input streams. NO new module required. Confidence 0.74.

THIS IS THE LOAD-BEARING VERDICT of this pull.

The evidence cluster:

- **Zacks et al. 2007 (Psychol Bull)** -- theoretical license. Event segmentation theory is substrate-agnostic about the input stream's source; the framework predicts the same machinery applies to any predictive stream the system processes, including imagination. Confidence 0.84 (R1 primary, R2 theoretical half).
- **Schacter, Addis & Buckner 2008 (Ann NY Acad Sci, PMID 18400923)** -- LOAD-BEARING empirical anchor for R2. The constructive-episodic-simulation core network (medial PFC, hippocampus, retrosplenial / posterior cingulate, inferior parietal lobule) is the SAME network for remembering past events and imagining future events. This is the strongest available empirical evidence that observation-side and imagination-side processing share neural substrate. Confidence 0.82.
- **Pfeiffer & Foster 2013 (Nature)** -- substrate consistency. The hippocampal forward-sweep mechanism that generates imagined trajectories is part of the same hippocampal substrate that processes observed activity sequences during memory and statistical learning. Confidence 0.78.
- **Schapiro et al. 2017 (Phil Trans Roy Soc B)** -- pathway-level grounding. The trisynaptic and monosynaptic pathways operate on whatever input the hippocampus receives, regardless of whether that input originated in observation or in rollout. Confidence 0.74.

The architectural recommendation: implement ARC-070 as a SECOND INPUT STREAM into the MECH-288 event_segmenter substrate. The segmenter is one mechanism with two read paths -- one consuming the observation stream, one consuming the rollout proposal stream -- and both reading from the same predictive engine (V_s). A re-segmentation pulse on either stream produces the same kind of output (a re-segmentation signal at the affected grain), differentiated only by which stream produced it.

This is substantially cheaper than building a parallel imagination-side module and is consistent with the substrate-economy REE has tried to maintain. The pattern matches MECH-269b's relationship to MECH-269 -- a single V_s primitive substrate consumed by multiple readers (MECH-269b at the cortical-rollout layer, ARC-070 at the rollout-proposal layer); now MECH-288 event_segmenter substrate consumed by both observation and imagination streams.

The confidence is 0.74 -- moderate. The recommendation is strongly licensed by the theoretical framework (Zacks 2007 substrate-agnostic) and by the network-level empirical evidence (Schacter 2008 shared core network), but the gap between SHARED NETWORK and SHARED MECHANISM is real -- two computational processes can co-activate the same brain regions without being algorithmically identical. The synthesis treats the bidirectional-shared-substrate recommendation as the DEFAULT child-MECH design, with the following falsifiable architectural prediction:

> **R2 falsification test:** ablating the MECH-288 event_segmenter substrate (or its biological correlate) should impair BOTH observation-side and imagination-side decomposition. If a clinical or computational dissociation is found where one is impaired without the other, the bidirectional-shared-substrate hypothesis is falsified and a parallel-but-coupled architecture is required.

This is the single most architecturally consequential verdict from the pull. The recommendation simplifies the substrate registry significantly: instead of two parallel decomposition mechanisms, REE gets one bidirectional event_segmenter that handles both input streams, with the V_s primitive feeding both via region-conditioned predictability.

The R2 verdict explicitly answers the briefing's pre-specified question: SHARED SUBSTRATE recommended; ARC-070 is a bidirectional extension of MECH-288 rather than a new module.

---

## R3 -- Hierarchy depth: multi-level vs single-level decomposition

### Verdict: MULTI-LEVEL hierarchy supported. ARC-070's child-MECH design should permit recursive decomposition (chunk -> sub-chunk -> primitive), with implementation depth bounded at 3-4 levels for tractability. Confidence 0.78.

The evidence cluster:

- **Badre & D'Esposito 2009 (Nat Rev Neurosci, PMID 19672274)** -- empirical anchor. The rostro-caudal frontal-cortex gradient instantiates AT LEAST 3-4 distinguishable levels of action abstraction (response, feature, dimension, context / task-set, episode). Multi-level hierarchical organisation is empirically well-documented. Confidence 0.78.
- **Koechlin & Summerfield 2007 (Trends Cogn Sci, PMID 17475536)** -- theoretical anchor. The cascade model formalises multi-level hierarchical control as the dominant computational organisation of executive control. Confidence 0.74.
- **Zacks et al. 2007** -- corroborating. Event segmentation theory predicts hierarchically nested boundaries (coarse and fine grain) from the same PE mechanism applied at multiple levels of representation. Confidence 0.84.
- **Schapiro et al. 2017** -- substrate grounding. The hippocampus has at least two parallel representational pathways (trisynaptic, monosynaptic) supporting different grain levels; the multi-level capability is native to the substrate. Confidence 0.74.

Multi-level hierarchy is supported by both empirical and theoretical anchors. The implementation recommendation is recursive decomposition with a hard depth cap (3-4 levels suggested, with backoff to flat-grain if no prediction-failure signal arrives within the cap). The cap is for engineering tractability rather than principled architectural reasons.

A subsidiary question deferred to child-MECH design: should the recursion be implicit (a single decomposition operator called recursively on its own output) or explicit (level-tagged primitive pools with a decomposition operator that maps level-N to level-N-1)? The literature licenses either; Schapiro's pathway-distinction supports level-tagged pools; Koechlin's cascade structure also supports level-tagged channels; the simplest implementation is single-operator recursion, but the richer level-tagged design integrates better with ARC-062 grain-invariant rule apprehension (an open Q-claim from the family doc).

The R3 confidence is 0.78. The verdict is well-supported across anchors but the depth cap is a design choice rather than a literature-licensed parameter, so the verdict's implementation grade has irreducible uncertainty.

---

## R4 -- Mid-execution decomposition vs pre-commitment-only

### Verdict: BOTH supported. ARC-070 should support pre-commitment decomposition (during rollout / pre-MECH-094-commit) AND mid-execution decomposition (during ongoing motor activity, when prediction error arrives at the chunk's mid-point). The same V_s-trigger mechanism handles both phases; the difference is the input stream phase, not the mechanism. Confidence 0.66.

The evidence cluster:

- **Pfeiffer & Foster 2013 (Nature)** -- substrate evidence. Forward sweeps are generated during ongoing navigation, including during motor activity. The substrate that generates trajectories is online during execution, not just pre-commitment. Confidence 0.78.
- **Zacks et al. 2007** -- framework consistency. Event boundaries are detected on the predictive engine's stream regardless of execution phase; the same PE mechanism fires on observed-during-execution streams as on simulated streams. Confidence 0.84.
- **Schacter, Addis & Buckner 2008** -- network-level support. The constructive-simulation network is engaged across multiple phases (planning, ongoing experience, retrospection); the substrate is not phase-restricted. Confidence 0.82.

The recommendation: ARC-070's child-MECH should support both phases. During rollout (pre-commitment), V_s is read on the proposed chunk's region; if low, decompose. During execution (post-MECH-094-commit), if the agent has executed N of M chunk steps and the next predicted state has diverged from observation, V_s on the REMAINING chunk content can be read; if low, decompose the remainder.

A key constraint from MECH-094 (hypothesis_tag): pre-commitment decomposition fires during simulation and DOES NOT write residue / does not chunk via composition (these are simulation-only operations). Post-commitment mid-execution decomposition fires during waking action and DOES WRITE residue / DOES interact with the action stream. The single mechanism therefore needs to BE AWARE OF the hypothesis_tag state and adjust its downstream effects accordingly. This is consistent with the broader MECH-094 architectural pattern; the synthesis flags this as a child-MECH-design constraint.

Note also that mid-execution decomposition is closely related to the reactive-replanning / motor-error-correction literature, where the agent updates its plan on the fly when sensorimotor feedback diverges from prediction. REE has not registered an explicit reactive-replanning slot; the mid-execution branch of ARC-070 may serve double duty here, providing the substrate for both decomposition-on-mid-execution-PE and the broader reactive-replanning function. A child-Q-claim on whether these are the same or distinct mechanisms is appropriate.

The R4 confidence is 0.66 -- the lowest of the five verdicts, reflecting the relative thinness of mid-execution-specific empirical evidence (the anchors document the substrate but do not directly demonstrate mid-execution decomposition firing). The synthesis recommends conservative implementation (support both phases via the same mechanism with hypothesis_tag-conditional downstream effects) and a child-MECH validation experiment that tests mid-execution decomposition against pre-commitment-only.

---

## R5 -- Bottleneck-state vs error-driven decomposition: same mechanism or distinct?

### Verdict: DISTINCT MECHANISMS with overlapping outputs on a subset of tasks. ARC-070's PRIMARY trigger should be error-driven (PE / V_s drop, biologically anchored); BOTTLENECK-AWARE secondary signals are a complementary fallback design but should NOT be the primary mechanism. Confidence 0.74.

The evidence cluster:

- **McGovern & Barto 2001 (ICML)** -- foil paper. Bottleneck-state subgoal discovery uses statistical-frequency analysis on success paths to identify decomposition targets. The mechanism is distinct from PE-driven event segmentation in its triggering signal (frequency on paths vs PE pulse) and applicability (requires repeated traversals; cannot do one-shot decomposition). Confidence 0.62 (mixed direction; foil rather than anchor).
- **Zacks et al. 2007** -- primary mechanism. Event boundaries are PE-driven; this is the canonical biologically-supported trigger. Confidence 0.84.
- **Schacter, Addis & Buckner 2008** -- network-level evidence for the PE-driven mechanism (the constructive-simulation network is the predictive-error-generating substrate, not a statistical-frequency analyser). Confidence 0.82.

The two mechanisms are distinct but their outputs frequently overlap. Bottleneck states in a state-action graph are often also high-PE states because they are decision-critical junctures where the agent's predictions are most uncertain (multiple paths converge or diverge). The PE-driven mechanism therefore tends to fire AT bottleneck states even though it is not LOOKING FOR them. This explains why the McGovern-Barto bottleneck framing has empirical traction in many tasks despite using a different signal.

The architectural recommendation: PE-driven primary, bottleneck-aware secondary as optional. ARC-070's primary trigger is V_s drop on the chunk's region (PE-driven, biologically anchored, applicable to one-shot scenarios). A secondary bottleneck-aware signal -- a chunked primitive's region containing a bottleneck-state-like topology -- could be used as an offline / consolidation-phase decomposition target. This dovetails with the ARC-071 composition pull: chunks form during repeated execution, and the chunks may be examined offline for bottleneck structure and pre-decomposed at bottleneck boundaries to seed the rollout proposal stream with already-grain-appropriate variants.

The R5 verdict is therefore: NOT the same mechanism. ARC-070's primary trigger is PE-driven (Zacks-style); McGovern-Barto's bottleneck framing is a distinct mechanism that REE could implement at the consolidation-phase boundary or as an offline analysis pass on chunked primitives. Both can co-exist; only the PE-driven one is essential for ARC-070 itself.

The R5 confidence is 0.74. The verdict is clearly settled in favour of distinct-mechanisms-with-overlapping-outputs, and the architectural recommendation (PE primary, bottleneck secondary) is reasonably well-supported.

---

## What this pull does NOT settle

Items deferred to subsequent pulls or future sessions:

1. **The specific V_s_decompose_threshold value.** A free parameter in the child-MECH design. The literature does not directly settle this; the threshold should be chosen via parametric sweep on a child-MECH validation experiment.
2. **Whether ARC-070's recursive-decomposition depth should be hard-capped or softly bounded.** R3 verdict supports multi-level; the specific cap (3 vs 4 vs adaptive) is implementation choice.
3. **Implicit-recursion vs explicit-level-tagging implementation.** R3 leaves both as viable; the choice depends on how ARC-062 grain-invariant rule apprehension is designed.
4. **Mid-execution-decomposition vs reactive-replanning unification or separation.** R4 leaves this as a child-Q-claim. The synthesis flags mid-execution-PE as a candidate substrate for both functions, but whether they collapse or stay distinct is open.
5. **Bottleneck-aware secondary signal design.** R5 verdict allows an offline / consolidation-phase bottleneck analysis as a secondary path; whether REE implements this depends on the ARC-071 composition pull's findings about offline chunk analysis.
6. **Cross-link with V_s symmetric gating (MECH-269b).** ARC-070 will be the SECOND major V_s consumer after MECH-269b. The two consumers can have independent thresholds (per-consumer parameterisation) but the V_s primitive should be a single substrate, not duplicated. This is an integration question for child-MECH design, not a literature question.
7. **MECH-094 hypothesis_tag interaction in mid-execution branch.** The R4 mid-execution decomposition needs hypothesis_tag-aware downstream effects (residue write only post-commitment); the specific implementation depends on the broader hypothesis_tag substrate's API.
8. **Validation experiment design for ARC-070's primary child MECH.** A discriminative-pair experiment would compare: (ARM_0) ARC-070 OFF baseline -- chunks fire at constant grain regardless of V_s; (ARM_1) ARC-070 ON, V_s-drop trigger -- chunks decompose when V_s drops below threshold on chunk's region; (ARM_2) ARC-070 ON, bottleneck-state trigger only -- chunks decompose at bottleneck states regardless of V_s. Predicted result: ARM_0 = chunks blindly fire and execute, paying prediction-failure cost at execution; ARM_1 = chunks decompose pre-commitment when V_s indicates unreliability, agent executes finer-grain plans; ARM_2 = decomposition is rare on one-shot tasks but appears on repeated structures. The R5-predicted differential between ARM_1 and ARM_2 falsifies the primary-mechanism choice.
9. **ARC-071 composition mechanism shape.** Sibling pull (parallel session). The two are decoupled at execution but share the parent commitment; ARC-071's child-MECH design will inform whether composition is purely repetition-driven or also informed by V_s positivity (a V_s-positive analog of ARC-070's V_s-negative trigger).

---

## Recommended next actions

1. **Update the ARC-070 evidence_quality_note in claims.yaml** to reference this synthesis with the lit_conf computed below, and to flag the R2 substrate-economy reframe (bidirectional shared substrate with MECH-288 recommended). The functional_restatement update is a smaller follow-up; stash for the child-MECH design session.
2. **Update the family doc** (`docs/architecture/policy_primitive_granularity.md`) ARC-070 anchor cluster: keep all six pre-registered anchors as primary; add Schacter, Addis & Buckner 2008 to the primary anchor list (it is the load-bearing R2 anchor that the briefing did not pre-register but that turned out to be essential). Add a "MECH-288 bidirectional substrate" cross-reference noting ARC-070 is recommended as a bidirectional extension of MECH-288 rather than a new module.
3. **Register the bidirectional-substrate recommendation** as a child-MECH-level design constraint: the first child MECH for ARC-070 should be implemented as a second input path into MECH-288 substrate, not as a parallel module. This is an architectural commitment with cross-cutting consequences for MECH-288's API and for V_s consumer documentation.
4. **Queue the first ARC-070 validation experiment** (V_s-drop primary vs bottleneck-state secondary discriminative pair) once R1 is confirmed via child-MECH design pass. The queue-experiment skill should produce the script + queue entry.
5. **Cross-check with MECH-269b symmetric V_s gating** at child-MECH design time. ARC-070 will be the second major V_s consumer; the two readers can have independent thresholds but should share the V_s primitive substrate, not duplicate it.
6. **Defer the ARC-071 composition pull's outcome integration** until the parallel sibling pull is closed. The R5 verdict's bottleneck-aware secondary recommendation may be re-shaped by ARC-071's findings about chunk-formation dynamics.

---

## Per-paper summary index

| Entry | DOI | Verdict it informs | Direction | Confidence |
|---|---|---|---|---|
| Zacks et al. 2007 | [10.1037/0033-2909.133.2.273](https://doi.org/10.1037/0033-2909.133.2.273) | R1 primary, R2 theoretical, R3 corroborating, R5 primary | supports | 0.84 |
| Schacter, Addis & Buckner 2008 | [10.1196/annals.1440.001](https://doi.org/10.1196/annals.1440.001) | R2 LOAD-BEARING empirical | supports | 0.82 |
| Badre & D'Esposito 2009 | [10.1038/nrn2667](https://doi.org/10.1038/nrn2667) | R3 empirical anchor | supports | 0.78 |
| Pfeiffer & Foster 2013 | [10.1038/nature12112](https://doi.org/10.1038/nature12112) | R1 substrate, R3, R4 substrate | supports | 0.78 |
| Koechlin & Summerfield 2007 | [10.1016/j.tics.2007.04.005](https://doi.org/10.1016/j.tics.2007.04.005) | R3 theoretical anchor, R5 hybrid | supports | 0.74 |
| Schapiro et al. 2017 | [10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049) | R1 substrate, R2 pathway grounding, R3 multi-grain | supports | 0.74 |
| McGovern & Barto 2001 | [10.5555/645530.655681](https://doi.org/10.5555/645530.655681) | R5 foil (distinct mechanism) | mixed | 0.62 |

**Aggregate ARC-070 lit_conf:** expected to land in the 0.74-0.78 range, supports-direction net (6 supports + 1 mixed; load-bearing supports cluster Zacks / Schacter / Badre / Pfeiffer-Foster averaging 0.81). The mixed-direction entry on McGovern-Barto applies specifically to the rejected bottleneck-state-as-primary-trigger sub-hypothesis, not to the architectural commitment ARC-070 names. The aggregate framing is "supports the architectural commitment with strong substrate attribution to V_s-drop primary trigger and bidirectional shared substrate with MECH-288; rejects bottleneck-state framing as primary in favour of PE-driven primary".

According to PubMed, all entries in this synthesis are sourced from PubMed-indexed literature with DOIs and PMIDs as cited above (with the exception of McGovern & Barto 2001, which is an ICML conference paper indexed by ACM with the cited DOI and a public copy on UMass Scholarworks).
