# Cognitive contract literature pull — first convergence tranche

**Date:** 2026-09-08  
**Status:** research evidence / planning note; not a thought and not an architecture specification  
**Parent thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`  
**Parent intake:** `evidence/planning/thought_intake_2026-09-08_deriving_the_cognitive_contract.md`  
**Purpose:** perform the lit-pull explicitly owed by the intake before authoring Thought 2; derive candidate invariants independently enough to avoid reading the existing REE architecture back into itself.

---

## 1. Interim result

The literature already supports taking the cognitive-contract programme seriously, but it argues for a refinement of the original candidate list.

The strongest emerging hypothesis is **not** that high-level cognition contains primitive modules named MEMORY, PERCEPTION, IMAGINATION, SELF, OTHER, etc. The stronger cross-domain fit is that progressively compressed representations preserve a smaller set of **relations over representations**: sameness/identity, provenance/source, temporal position, agent/owner, causal control, actuality/possibility, epistemic confidence, value, and relational structure.

Higher-order modes such as *remembered*, *perceived*, *imagined* and *predicted* may then be bundles or regions in that coordinate system rather than irreducible primitive nodes.

This fits the current cognitive-contract thought's requirement that invariants be semantic/relational and recoverable rather than fixed data structures, while remaining a new empirical hypothesis rather than a registered conclusion.

---

## 2. A particularly important literature family: semantic primes and semantic maps

### 2.1 Natural Semantic Metalanguage (NSM)

The Natural Semantic Metalanguage programme (Wierzbicka; Goddard and collaborators) is unexpectedly close to the language-mining route proposed in the cognitive-contract discussion. It proposes a finite set of cross-linguistically recurrent, allegedly irreducible semantic primes plus combinatorial rules. The current published inventory is usually given as 65 primes.

The useful point for REE is **not** to accept the NSM inventory as true or universal. NSM is a substantive and contested linguistic theory, and its primes are claims about human semantics rather than demonstrated substrate-neutral cognitive invariants. Its value is as an independently-developed hypothesis generator.

The overlap with the present contract candidates is nevertheless striking. Published NSM groupings include:

- I / YOU / SOMEONE / SOMETHING / PEOPLE / BODY;
- KIND / PART;
- THIS / THE SAME / OTHER;
- ONE / TWO / SOME / ALL / MUCH-MANY;
- GOOD / BAD;
- THINK / KNOW / WANT / FEEL / SEE / HEAR;
- DO / HAPPEN / MOVE;
- existence / location / possession;
- LIVE / DIE;
- WHEN-TIME / NOW / BEFORE / AFTER;
- WHERE-PLACE / HERE / spatial relations;
- NOT / MAYBE / CAN / BECAUSE / IF;
- LIKE / WAY.

That gives an independently-generated language-side basis containing self/other, identity/sameness, part/kind relations, quantity, value, epistemic state, perception, agency/event, existence, life/death, time, space, modality, causality, negation and similarity.

More importantly, NSM explicitly proposes **combinatorial/syntactic properties of the primes**. That makes it relevant to the stronger REE hypothesis that grammar may expose not only candidate invariants but some rules by which invariant relations compose.

Key sources:

- Goddard C. *The Natural Semantic Metalanguage Approach*. Oxford Handbook of Linguistic Analysis (2015). DOI: 10.1093/oxfordhb/9780199677078.013.0018.
- Wierzbicka A. *Semantics: Primes and Universals*. Oxford University Press (1996).
- Goddard C. *The universal syntax of semantic primitives*. Language Sciences 19(3), 1997. DOI: 10.1016/S0388-0001(96)00059-9.
- Goddard C. *Semantic primes, semantic molecules, semantic templates*. Linguistics 50(3), 2012. DOI: 10.1515/ling-2012-0022.

**REE use:** high-value hypothesis generator; never a label source for training. Keep NSM-derived predictions held out from the latent-discovery experiments where possible.

### 2.2 Semantic maps

Semantic-map typology explicitly tries to represent cross-linguistic regularities in how meanings/functions cluster while separating recurrent structure from language-specific packaging. This is methodologically closer to the cognitive-contract problem than a hunt for one-to-one universal grammatical categories.

Key source:

- Georgakopoulos T. *Semantic Maps*. Oxford Bibliographies in Linguistics (2019; reviewed 2022). DOI: 10.1093/obo/9780199772810-0229.

**REE use:** mine *neighbourhood/adjacency structure among meanings*, not merely category names. If the same semantic neighbourhoods recur across unrelated languages, they may be evidence for relational geometry rather than a universal vocabulary.

### 2.3 Modern caution: most proposed grammatical universals do not survive strong controls

A 2025 Nature Human Behaviour study tested 191 proposed grammatical universals against Grambank while controlling for language genealogy and geography. Only 60/191 (31%) were supported by both major analyses. Hierarchical universals survived much better (24/30, 80%) than broad word-order universals.

Source:

- *Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses*. Nature Human Behaviour, published 2025, volume 10 (2026), 126–136. Article: s41562-025-02325-z.

**REE implication:** this strongly favours the planned discipline. Surface recurrence is weak evidence. **Relational/hierarchical constraints may be more promising than specific human grammatical categories.**

---

## 3. Developmental and comparative convergence

### 3.1 Core knowledge is already relationally organised

Spelke and Kinzler's influential review proposed early systems for representing objects, actions, number and space, with a possible fifth system for social partners. This is not a settled inventory, but it is a useful independent developmental decomposition.

- Spelke ES, Kinzler KD. *Core knowledge*. Developmental Science 10, 89–96 (2007). DOI: 10.1111/j.1467-7687.2007.00569.x.

The relevant feature is that the early systems are not a list of adult concepts. They concern **persistent entities, actions/agents, magnitude and relational location**.

### 3.2 Identity appears first as individuation and continuity, not as a symbolic ID

Developmental work on object individuation distinguishes several cues to identity: spatiotemporal continuity, object properties and kind information. Younger infants rely especially heavily on spatiotemporal information before integrating richer property/kind information.

- Xu F. *Object individuation and object identity in infancy: the role of spatiotemporal information, object property information, and language*. Acta Psychologica (1999), PMID 10504878.
- Xu F. *Sortal concepts, object individuation, and language*. Trends in Cognitive Sciences 11(9), 400–406 (2007). DOI: 10.1016/j.tics.2007.08.002.
- Cacchione T. *The foundations of object permanence*. Cognition 128(3), 397–406 (2013). DOI: 10.1016/j.cognition.2013.05.006.

A 2026 review of object-individuation work argues that by around the first birthday infants represent broad kind concepts such as OBJECT, ANIMATE and AGENT, while language and pedagogy contribute to later more specific kinds (PMID 39666554).

**REE implication:** candidate `identity` should probably be represented in the ledger as an **equivalence/continuity relation** with multiple evidential cues, not a predeclared object identifier. `kind` may be a later abstraction over individuation rather than the same primitive.

### 3.3 Agency is early, but likely composite

Infants reason about goal-directed agents and can use inferred mental states to predict actions. Developmental reviews treat agency, goals, epistemic states and counterfactual states as separable but interacting components.

- *Psychological Reasoning in Infancy*. Annual Review of Psychology 67 (2016). DOI: 10.1146/annurev-psych-010213-115033.

Comparative cognition also finds object permanence and social/gaze-following capacities across species, while warning that developmental paths vary.

- Gómez JC. *Species comparative studies and cognitive development*. Trends in Cognitive Sciences 9(3), 118–125 (2005). DOI: 10.1016/j.tics.2005.01.004.

**REE implication:** `agency` is a strong candidate family, but the literature argues against treating it as one indivisible scalar. A likely decomposition is actor/source + action + predicted consequence + causal/control relation.

---

## 4. Neuroscience convergence: structural bases linked to particular content

### 4.1 Cognitive maps generalise beyond physical space

A major hippocampal-entorhinal literature argues that map-like coding can organise arbitrary relationships among entities, not only physical locations.

- Behrens TEJ et al. *What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior*. Neuron 100(2), 490–509 (2018). DOI: 10.1016/j.neuron.2018.10.002.
- Garvert MM et al. *A map of abstract relational knowledge in the human hippocampal-entorhinal cortex*. eLife 6:e17086 (2017). DOI: 10.7554/eLife.17086.
- Park SA et al. *Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps*. Neuron 107(6), 1226–1238 (2020). DOI: 10.1016/j.neuron.2020.06.030.

This suggests that the high-level common currency may be **relations and transition structure** rather than shared sensory features.

### 4.2 Tolman-Eichenbaum Machine (TEM) is unusually relevant

The Tolman-Eichenbaum Machine formalises a division in which entorhinal-like representations provide a basis for **structural knowledge**, while hippocampal representations bind this structure to particular sensory content. The learned structural basis transfers across environments even when sensory representations remap.

- Whittington JCR et al. *The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation*. Cell 183(5), 1249–1263 (2020). DOI: 10.1016/j.cell.2020.10.024.

This is one of the closest biological/computational precedents found so far for the current REE idea: a higher or reusable representational basis can encode **how states relate** while lower/particular representations encode what the states happen to contain.

It does **not** establish the cognitive contract, but it makes the proposed separation between invariant relational structure and engine-specific content technically plausible.

### 4.3 Time is represented as an organising coordinate

Hippocampal time cells encode successive moments in structured experiences, integrating temporal context with other event dimensions.

- Eichenbaum H. *Time cells in the hippocampus: a new dimension for mapping memories*. Nature Reviews Neuroscience 15, 732–744 (2014). DOI: 10.1038/nrn3827.

**REE implication:** preserve temporal **ordering/context/trajectory** before assuming human-style metric time or tense categories. The likely invariant is relational temporal structure, with clock-like units contingent.

---

## 5. Representation source and reality status: the strongest new decomposition

Reality-monitoring research distinguishes externally generated perception from internally generated imagination/thought, but modern accounts do not treat this as a simple attached truth label.

The source-monitoring framework proposes that source is inferred from cues such as sensory detail, context and the cognitive operations involved in generation. A 2022 review argues that imagination and perception substantially share first-order neural mechanisms and that higher-level cortical systems evaluate cues to infer source. A 2026 fMRI meta-analysis separately examines external-source monitoring and reality monitoring.

- Simons JS, Garrison JR, Johnson MK. *Brain Mechanisms of Reality Monitoring*. Trends in Cognitive Sciences 21(6), 462–473 (2017). DOI: 10.1016/j.tics.2017.03.012.
- Dijkstra N, Kok P, Fleming SM. *Perceptual reality monitoring: Neural mechanisms dissociating imagination from reality*. Neuroscience & Biobehavioral Reviews 135, 104557 (2022). DOI: 10.1016/j.neubiorev.2022.104557.
- Martín-Luengo B et al. *External Source Monitoring and Reality Monitoring: Meta-Analysis of fMRI Studies*. Human Brain Mapping 47(11):e70614 (2026). DOI: 10.1002/hbm.70614.

Children's source monitoring develops substantially across childhood, with many experimental paradigms separating content recognition from attribution of origin.

- Li Q et al. *Methods and measures of source monitoring in children: A scoping review*. British Journal of Developmental Psychology 43(3), 529–561 (2025). DOI: 10.1111/bjdp.12523.

**Interim REE interpretation:** `perception`, `memory`, `imagination`, and `prediction` are poor candidates for four primitive contract fields. A more parsimonious basis may include at least:

1. **provenance/source** — where/through what process did this representation arise?;
2. **temporal relation** — when does its content belong?;
3. **actuality/commit status** — is the represented state currently treated as obtaining, rehearsed, recalled, possible, or counterfactual?;
4. **generation/control evidence** — was the representation internally generated, externally constrained, self-caused, etc?;
5. **confidence/precision** — how strongly should the source/status attribution itself be trusted?

The familiar mode labels may emerge from combinations of those coordinates.

---

## 6. Agency and confidence are also likely meta-relational

### 6.1 Agency

Sense-of-agency models combine prospective motor intention/prediction with retrospective comparison between predicted and observed consequences.

- Haggard P. *Sense of agency in the human brain*. Nature Reviews Neuroscience 18, 196–207 (2017). DOI: 10.1038/nrn.2017.14.
- Wen W, Imamizu H. *The sense of agency in perception, behaviour and human–machine interactions*. Nature Reviews Psychology 1, 211–222 (2022). DOI: 10.1038/s44159-022-00030-6.

A 2022 review cautions that 'sense of agency' can hide multiple partially dissociable mechanisms rather than one unitary faculty (PMID 35447600).

**REE implication:** the contract should preserve enough structure to reconstruct agency judgments, but `AGENCY` may be a **derived relation** over self/source, action, prediction, causality and control.

### 6.2 Confidence / metacognition

Confidence is a rich metacognitive variable related to uncertainty monitoring rather than merely a label on content.

- Fleming SM. *Metacognition and Confidence: A Review and Synthesis*. Annual Review of Psychology 75, 241–268 (2024). DOI: 10.1146/annurev-psych-022423-032425.

Comparative work reports uncertainty-monitoring and metacognition-like behaviour in several non-human species, while emphasising debate over associative explanations.

- Smith JD, Couchman JJ, Beran MJ. *Animal metacognition: a tale of two comparative psychologies*. Journal of Comparative Psychology 128(2), 115–131 (2014). DOI: 10.1037/a0033105.

Developmentally, metacognitive competence improves substantially over childhood; a 2025 review argues that representing alternative possibilities is an important developmental constraint (PMID 40533302).

**REE implication:** confidence/precision may belong to the contract as **metadata over representations and translations**, not necessarily as part of the semantic content being translated. This reinforces the parent intake's observation that REE currently lacks a distinct representation of *translation confidence*.

---

## 7. Machine-learning precedents for the narrowing-stack hypothesis

The user's proposed stack — progressively fewer nodes at higher levels — has close formal relatives, but the literature also shows why narrowing alone is insufficient.

### 7.1 Information Bottleneck

The Information Bottleneck principle explicitly trades compression of X into Z against preservation of information relevant to Y. It provides the right mathematical vocabulary for asking what can be discarded while preserving downstream utility.

- Wu T et al. *Learnability for the Information Bottleneck*. UAI / PMLR 115, 1050–1060 (2020).

A 2026 geometry-grounded representation-learning paper poses almost the exact measurement question we need: what bottleneck dimensionality is sufficient to preserve the mutual information required for prediction?

- Gulati P et al. *Mutual Information and Task-Relevant Latent Dimensionality*. PMLR 326, 262–293 (2026).

### 7.2 State abstraction and bisimulation

Reinforcement-learning state-abstraction work asks when different raw states may be treated as equivalent without losing the ability to choose good policies. Bisimulation-like abstractions preserve reward/transition structure; value-preserving abstractions formalise how information can be discarded while retaining near-optimal behaviour.

- Abel D et al. *Value Preserving State-Action Abstractions*. AISTATS / PMLR 108, 1639–1650 (2020).
- Hansen-Estruch P et al. *Bisimulation Makes Analogies in Goal-Conditioned Reinforcement Learning*. ICML / PMLR 162, 8407–8426 (2022).
- Panangaden P et al. *Policy Gradient Methods in the Presence of Symmetries and State Abstractions*. JMLR 25(71), 1–57 (2024).

A useful warning from the abstraction literature is that if the preservation objective is too weak, trivial or arbitrary abstractions can satisfy it. A narrow layer does not automatically learn meaningful invariants.

**REE implication:** the upper stack needs **multiple independent consumers/constraints** — e.g. prediction, control, reconstruction into heterogeneous engine spaces, memory integration, value/harm evaluation and source-status preservation. The features that survive *all* of these pressures are better candidates for the contract than features surviving one task.

---

## 8. First five candidate families after pruning

These are not architecture. They are the first ledger-ready families.

### A. Individuation / identity / sameness

Likely primitive form: a relation supporting `same entity across transformation/time` rather than a symbolic identity field.

### B. Temporal order / persistence / trajectory

Likely primitive form: ordered/relational temporal structure. Human tense categories and metric duration are probably derived or embodiment/culture-sensitive.

### C. Agent-source / causal control

Likely not one primitive. Candidate contract requirement is enough information to reconstruct whether a transition is self-produced/other-produced/ambient and whether an action controlled the outcome.

### D. Provenance / actuality / representational mode

The original `reality status` candidate should be split experimentally. Provenance and actuality/commitment can dissociate. Perception/memory/imagination/prediction are candidate *composites* over these coordinates plus time and control.

### E. Confidence / precision

Likely a cross-cutting meta-variable rather than object-level content. We need to test both content confidence and **translation confidence**.

---

## 9. A second candidate layer that should remain held out for the next pull

The following appear strongly enough in language and/or REE to warrant dedicated passes but should not be promoted from intuition yet:

- value / good-bad / harm-benefit;
- goal / want / viability;
- quantity / magnitude;
- part / kind / similarity;
- spatial relation generalised to state-space relation;
- negation;
- possibility / conditional / counterfactual;
- commitment;
- salience / relevance.

Natural Semantic Metalanguage is particularly rich here, but because it is language-derived it should not be allowed to dominate the ordering of the evidence search.

---

## 10. Experimental consequences now clear enough to pre-register

### Experiment family 1 — bottleneck sweep

Train otherwise-matched agents with progressively narrower upper latent widths. At every level measure downstream task performance, E1/E2/E3 reconstruction or cross-decoding, recoverability of independently labelled candidate relations, bridge complexity, dimensionality and geometry stability across seeds.

Question: **which relations remain recoverable furthest into the bottleneck?**

### Experiment family 2 — multi-consumer versus single-consumer compression

Compare a bottleneck trained for one downstream objective with one shared across heterogeneous consumers (prediction, control, memory, harm/value, translation back into engine-specific states).

Prediction: contract-like structure should be more likely under multi-consumer pressure; single-objective bottlenecks can retain task-specific arbitrary codes.

### Experiment family 3 — cross-world / cross-body transfer

Train related agents in environments with different sensory encodings, body/action affordances or surface statistics. Compare upper-latent geometry after aligning only by behaviour/relations, not raw observations.

Prediction: true architectural invariants should transfer better than sensory/schema-specific features.

### Experiment family 4 — held-out linguistic comparison

Do **not** train language-derived invariant labels. Once latent structure has been discovered, compare its independently recovered relational basis against NSM prime families, semantic-map neighbourhoods, robust Grambank hierarchical universals and evidentiality/modality typologies.

This turns language into a held-out convergence test rather than an oracle.

### Experiment family 5 — boundary lesions

At an inter-engine translator, selectively corrupt one recoverable relation while preserving the rest. Test the pre-registered failure signature from MECH-545.

The strongest first V3-tractable case remains the committed-versus-imagined/replay boundary already identified by the parent intake. This is relevant even though the cognitive-contract architecture is currently routed mainly to V4: the discovery methodology can begin in V3 without forcing a premature architecture change.

---

## 11. New conceptual model to carry into Thought 2

```text
CONTENT / LOCAL STATE
        +
RELATIONAL COORDINATES
    identity / sameness
    temporal position / order
    source / provenance
    self-other ownership
    action / causal-control relation
    actuality / possibility / commitment
    confidence / precision
    value / relevance   [not yet fully pulled]
        ↓
combinations yield familiar modes
        ↓
perceived / remembered / imagined / predicted / intended / committed
```

This is deliberately a **factorisation hypothesis**, not a specification. The next evidence pass should actively seek counterexamples and alternative factorizations.

---

## 12. What is sufficiently progressed before Thought 2

We now have:

1. an independently motivated language programme (NSM + semantic maps + modern universals controls) that substantially overlaps the candidate contract without being derived from REE;
2. developmental evidence that early cognition privileges object continuity/identity, actions/agents, number, space and social partners;
3. neuroscience showing transferable relational structure and abstract cognitive maps, with TEM especially relevant to structure-versus-content factorisation;
4. reality/source-monitoring evidence arguing that representational mode is inferred from multiple cues rather than stored as one monolithic label;
5. agency literature arguing for a composite comparator structure;
6. metacognitive/comparative evidence for confidence/uncertainty monitoring;
7. formal machine-learning tools for testing which information survives lossy abstraction and how much latent dimensionality is sufficient;
8. a concrete anti-contamination experiment plan in which language remains held out.

This is enough to populate the initial invariant ledger and enough to make Thought 2 evidence-led rather than speculative. It is **not** yet enough to fix the contract or implement a canonical upper latent.
