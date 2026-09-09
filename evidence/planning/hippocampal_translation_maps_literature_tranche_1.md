# Hippocampal Translation Maps — Literature Tranche 1

**Date:** 2026-09-09  
**Status:** targeted literature synthesis / claim-overlap review; no claim promotion and no experiment-queue mutation  
**Parent archaeology:** `docs/thoughts/2026-09-09_hippocampal_translation_maps_ree_archaeology.md`  
**Related registered claims:** ARC-007, MECH-033, ARC-139, MECH-537, MECH-540, MECH-547, MECH-548, MECH-362, Q-057  
**Purpose:** test whether the archaeology's proposed “hippocampal translation map” synthesis is biologically defensible, identify the likely computational decomposition, preserve negative evidence, and determine whether new REE claims are warranted.

---

## 1. Executive result

The first literature tranche **does not support a doctrine in which the hippocampus is a generic latent-to-latent translator**.

It supports a narrower and more distributed picture:

1. **Explicit reference-frame conversion is strongly associated with retrosplenial–entorhinal circuitry.** Recent work shows a progression from more egocentric coding in anterior retrosplenial cortex toward more allocentric coding in posterior retrosplenial cortex, with a projection to medial entorhinal cortex enriched for integrated world-referenced signals.
2. **The hippocampal formation participates in relational mapping and low-dimensional interareal routing.** Large-scale 2026 recordings identify distinct low-dimensional communication subspaces linking upstream hippocampal populations, CA1 and retrosplenial cortex, with different subspaces recruited across experience and brain state.
3. **Hippocampal retrieval is strongly cue/context selective.** Indexing theory, human event-boundary reactivation and recall chronometry all support hippocampal pattern completion / indexing that selectively reinstates cortical content relevant to the current cue or context.
4. **Replay is selective and can reshape or maintain representations, but direct evidence that replay reduces the mathematical complexity of an inter-system translation is still absent.**
5. **Representational drift makes interface maintenance a real computational problem.** Hippocampal place-field expression changes across time and environments, while some underlying co-firing/manifold structure can remain more stable than the apparent place map.

The best current biological analogue for REE is therefore not:

```text
hippocampus = universal translator
```

but something closer to:

```text
specialised representations
      ↓
relational indexing / reference-frame registration
      ↓
context- and receiver-relevant retrieval
      ↓
low-dimensional interareal routing
      ↓
replay-dependent maintenance / reconfiguration
```

with the transformation distributed across hippocampal, entorhinal, retrosplenial and cortical partners.

---

## 2. Evidence stream A — explicit reference-frame transformation

### Alexander et al. 2023 — gated egocentric→allocentric transformations

Andrew S. Alexander, Jennifer C. Robinson, Chantal E. Stern, Michael E. Hasselmo. *Gated transformations from egocentric to allocentric reference frames involving retrosplenial cortex, entorhinal cortex, and hippocampus.* **Hippocampus** 33(5):465–487 (2023). DOI: `10.1002/hipo.23513`; PMID: `36861201`.

The review synthesises evidence for egocentric boundary coding in retrosplenial, postrhinal and entorhinal regions and models the conversion of sensory/body-centred coordinates into allocentric representations used by grid/place-cell systems. It discusses gain-field and phase-code mechanisms rather than treating translation as an arbitrary learned decoder.

**REE mapping:** supports the idea that *reference frame is part of an interface contract*. It does not localise the entire transformation to hippocampus and therefore argues against a hippocampus-only implementation.

### Yang et al. 2026 — projection-specific retrosplenial→MEC transformation

Youran Yang et al. *Anterior and posterior retrosplenial cortex employ distinct strategies for egocentric-allocentric transformation in spatial coding.* **PNAS** 123(31):e2600565123 (2026). DOI: `10.1073/pnas.2600565123`; PMID: `42520117`.

Two-photon imaging in freely navigating mice identifies a functional gradient: anterior retrosplenial cortex is more dominated by egocentric boundary-vector coding, while posterior retrosplenial cortex shows stronger allocentric integration. A specialised posterior-RSC→medial-entorhinal projection is enriched for conjunctive neurons carrying integrated world-referenced signals.

**REE mapping:** this is the strongest first-tranche negative evidence against the phrase “hippocampal translator” if interpreted anatomically. The explicit coordinate conversion may occur substantially **before hippocampal place-code use**, in a distributed retrosplenial–entorhinal pathway.

**Architectural consequence:** retain “hippocampal translation maps” only as shorthand for a research problem. The candidate biological analogue is a **hippocampal–entorhinal–retrosplenial interface system**.

---

## 3. Evidence stream B — low-dimensional interareal routing

### Gonzalez et al. 2026 — hippocampal–retrosplenial communication subspaces

Joaquín Gonzalez et al. *Subspace communication in the hippocampal–retrosplenial axis.* **Nature** 655:192–201 (2026). DOI: `10.1038/s41586-026-10481-z`; PMID: `42129569`.

Large-scale simultaneous recordings across DG, CA3, CA2, CA1 and retrosplenial cortex identify low-dimensional communication subspaces that capture distinct input-output transformations through CA1. Overlapping neuronal pools can be recombined into different subspaces across partner regions, experiences and brain states. Post-experience sleep shows a plasticity–stability difference between hippocampal and cortical-facing subspaces.

**REE mapping:** strong biological anchor for ARC-139 / MECH-537. It makes a crucial distinction between a region's whole representation and the **low-dimensional directions actually visible to a particular partner**. It is compatible with receiver-specific read surfaces without establishing MECH-547's stronger receiver-state-conditioned map.

**Negative boundary:** pCCA subspace membership is not equivalent to synaptic translation; the study does not show that CA1 computes an arbitrary coordinate conversion or that sleep reduces bridge complexity `L(A→B)`.

---

## 4. Evidence stream C — cue/context-conditioned retrieval rather than fixed translation

### Teyler & Rudy 2007 — hippocampal indexing

Timothy J. Teyler, Jerry W. Rudy. *The hippocampal indexing theory and episodic memory: updating the index.* **Hippocampus** 17(12):1158–1169 (2007). DOI: `10.1002/hipo.20350`; PMID: `17696170`.

The hippocampus is proposed to store an index over distributed neocortical activity. A partial cue activates the hippocampal index, which then reactivates the corresponding cortical pattern.

**REE mapping:** this is highly relevant to the translation-map idea but also a strong rival interpretation. A hippocampal system can make heterogeneous cortical content mutually accessible by **indexing and reinstatement**, without translating one cortical latent into another.

### Staresina & Wimber 2019 — hippocampal pattern completion coordinates cortical reinstatement

Bernhard P. Staresina, Maria Wimber. *A Neural Chronometry of Memory Recall.* **Trends in Cognitive Sciences** 23(12):1071–1085 (2019). DOI: `10.1016/j.tics.2019.09.011`; PMID: `31672429`.

Electrophysiological work is synthesised into a sequence in which a retrieval cue reaches medial temporal structures, hippocampal pattern completion begins, and cortical memory reinstatement follows. Retrieval reverses aspects of perceptual information flow and is temporally structured.

**REE mapping:** supports a state/query-dependent interface more than a fixed bridge. The same stored episode need not expose all of its content; the current cue determines which cortical pattern is reinstated.

### Hahamy, Dubossarsky & Behrens 2023 — context-specific past-event reactivation

Avital Hahamy, Haim Dubossarsky, Timothy E. J. Behrens. *The human brain reactivates context-specific past information at event boundaries of naturalistic experiences.* **Nature Neuroscience** 26:1080–1089 (2023). DOI: `10.1038/s41593-023-01331-6`.

Past-event representations reactivate in hippocampus and default-mode regions specifically at boundaries in an ongoing narrative, and the reactivated events are those relevant to the current context.

**REE mapping:** adjacent support for MECH-547's idea that an interface can be conditioned by current receiver/context state. It is not evidence for a mathematical `T(sender,receiver)` transformation; it is evidence for **selective context-indexed retrieval**.

### Song et al. 2026 — causally relevant reinstatement updates current representation

Hayoung Song, Jin Ke, Rhea Madhogarhia, Yuan Chang Leong, Monica D. Rosenberg. *Cortical reinstatement of causally related events sparks narrative insights by updating neural representation patterns.* **Nature Communications** 17:7362 (2026). DOI: `10.1038/s41467-026-73914-3`; PMID: `42270596`.

When participants infer a causal relation in a scrambled narrative, patterns corresponding to causally relevant past events are reinstated across cortex before insight and are associated with shifts in the current situational representation.

**REE mapping:** supports a relational rather than similarity-only retrieval principle: the useful past representation is selected because of its relation to the current problem. This fits query-conditioned retrieval and TCRT, but the paper does not establish hippocampus as the transformation locus.

---

## 5. Evidence stream D — replay selects and maintains consequential experience

### Yang et al. 2024 — sharp-wave ripples select experiences for later replay

Wannan Yang, Chen Sun, Roman Huszár, Thomas Hainmueller, Kirill Kiselev, György Buzsáki. *Selection of experience for memory by hippocampal sharp wave ripples.* **Science** 383:1478–1483 (2024). DOI: `10.1126/science.adk8261`; PMID: `38547293`.

Awake sharp-wave ripple content preferentially reflects particular recent trials, and those trials are preferentially replayed during subsequent sleep.

**REE mapping:** replay is not a uniform backup operation. It selectively re-exposes particular event/index structures to later offline processing. This is compatible with interface maintenance being consequence-weighted rather than global.

**Negative boundary:** selection for replay is not evidence that replay performs coordinate translation, nor that it reduces bridge complexity.

### Gonzalez et al. 2026 again — interface-specific sleep dynamics

The CA1–CA3 versus CA1–RSC subspaces show different post-experience sleep relationships to replay and stability. This supports MECH-540's *selective interface maintenance* framing at an adjacent level, not its stronger claim that sleep should lower minimum mapping complexity.

---

## 6. Evidence stream E — representational drift and stable relational structure

### Fenton 2024 — remapping may preserve underlying manifold organisation

André A. Fenton. *Remapping revisited: how the hippocampus represents different spaces.* **Nature Reviews Neuroscience** 25:428–448 (2024). DOI: `10.1038/s41583-024-00817-x`; PMID: `38714834`.

The perspective argues that place-field remapping can coexist with more stable subsecond co-firing relationships and internally organised manifold structure; the manifold can be registered to different environments rather than wholly rebuilt.

**REE mapping:** very relevant to the distinction between changing local coordinates and preserving a relation that another system can track. An interface may need to follow **registration of a stable relational structure**, not learn an arbitrary fresh mapping after every representational change.

### Madar et al. 2025 — continuous representational shifting under plasticity

Antoine D. Madar, Anqi Jiang, Can Dong, Mark E. J. Sheffield. *Synaptic plasticity rules driving representational shifting in the hippocampus.* **Nature Neuroscience** (2025). PMID: `40113934`.

Behavioural-timescale synaptic plasticity best explains trial-by-trial place-field shifting, and plasticity events continue to generate population-level representational drift during exploration.

**REE mapping:** establishes the maintenance problem: useful local representation can remain plastic even after competence appears. It does not demonstrate a compensating translation map, but it makes a permanently fixed bridge biologically less plausible.

---

## 7. Strongest interpretation after tranche 1

A biologically disciplined working model is:

```text
sensory / egocentric codes
        ↓
RSC / parahippocampal / entorhinal reference-frame transformation
        ↓
hippocampal relational indexing / pattern separation-completion
        ↓
CA1 low-dimensional partner-specific routing
        ↓
context/query-selected cortical reinstatement
        ↓
replay selectively reactivates and reconfigures useful relations
```

This is a **distributed transformation-and-indexing system**.

The word “map” remains useful if it means a structure preserving relations and reference, not a literal Euclidean chart and not a universal vector translator.

---

## 8. Claim-overlap decision

### No new claim is minted by tranche 1

The literature does not yet justify a new broad claim that “hippocampus translates between representational systems.” Doing so would collapse several separable mechanisms and would overstate the anatomical evidence.

Current evidence maps onto existing claims:

- **ARC-139 / MECH-537:** low-dimensional communication subspaces and integration without global convergence — strongly relevant (Gonzalez 2026).
- **MECH-540:** selective offline interface maintenance — adjacent support, but bridge-complexity reduction remains an REE-only prediction.
- **MECH-547:** current cue/context can determine which stored content is exposed/reinstated — biological analogue supported, but a true receiver-state-conditioned latent transformation remains unproven.
- **MECH-548:** dynamic stability is biologically motivated by ongoing drift and changing subspaces, but recursive off-manifold compounding / semantic double-counting are not directly established by the neuroscience literature.
- **ARC-007 / MECH-033:** relational path/index/replay architecture remains relevant.
- **MECH-362 / Q-057:** developmental overcapacity→sparsification remains a separate developmental line.

The **unprocessed shared-reference-frame thought** is the correct location for any future claim about reference-frame mediation. Tranche 1 argues that such a claim, if minted, should be distributed (`RSC/entorhinal/hippocampal interface`) rather than hippocampus-exclusive.

---

## 9. Negative-evidence ledger

The hippocampal-translation-map programme should be weakened if any of the following survive targeted review/experiment:

1. **Indexing alone suffices:** hippocampal intervention changes which cortical ensemble is reinstated but no evidence requires translation between representational geometries.
2. **Reference conversion is upstream:** RSC→MEC transformation fully accounts for egocentric→allocentric conversion; hippocampus simply consumes the converted representation.
3. **Static shared manifold suffices:** apparent translation is only registration to a stable relational manifold, not an active map between codes.
4. **Ordinary joint learning suffices:** sender and receiver co-adapt directly and no persistent bridge/index maintenance process is needed.
5. **Replay preserves memories but not interfaces:** offline reactivation improves recall while minimum bridge complexity and cross-system causal use remain unchanged.
6. **Context-specific retrieval does not require receiver conditioning:** sender-side cue selection alone explains the effect; a `T(A,B)` mapping adds nothing beyond `T(A)`.

These are genuine rivals, not implementation details.

---

## 10. Next literature tranches

### Tranche 2 — CA1 / entorhinal transformation mechanics

Questions:
- Does CA1 explicitly transform CA3-separated codes into entorhinal/cortical-readable overlapping codes?
- What is experimentally established versus inherited from Complementary Learning Systems models?
- Are there partner-specific output channels or projection-defined subspaces in CA1 beyond the RSC axis?

### Tranche 3 — replay as interface maintenance

Questions:
- Does replay maintain alignment between two changing representational systems, or only reactivate content?
- Is there evidence for post-replay reductions in decoder/bridge complexity?
- Do sleep/ripple interventions alter interareal communication geometry causally?

### Tranche 4 — development

Questions:
- Do hippocampal/entorhinal/RSC interfaces themselves begin overconnected and sparsify?
- Does developmental pruning preferentially preserve cross-system relations rather than strong weights?
- Can the same mature sparse circuit be learned directly from birth, or is the dense developmental path necessary?

---

## 11. Literature debt from already-minted claims

MECH-547 and MECH-548 were registered on 2026-09-08 after the main mutual-legibility literature pull. They therefore owe a dedicated literature pull rather than inheriting the parent claims' evidence.

This tranche closes that debt separately under:

`evidence/literature/targeted_review_mech_547_548_receiver_conditioned_recurrent_interface/`

The pull is deliberately expected to be **mixed/adjacent rather than strongly supportive**: the neuroscience literature supports context-selective retrieval, changing interareal subspaces and representational drift, while the exact `T(sender,receiver)` and recurrent-clean-base mechanisms remain REE hypotheses.
