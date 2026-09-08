# Mutual legibility without representational collapse

**Date:** 2026-09-07  
Status: processed
Intake: evidence/planning/thought_intake_2026-09-07_mutual_legibility.md
Claims registered: ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, INV-105

**Document type:** evidence-backed thought / falsifiable architectural hypothesis
**Scope:** REE-v3 closure implications plus broader developmental architecture; no claim promotion or experiment queue mutation in this document  
**Evidence campaign:** `evidence/planning/latent_interface_translation_campaign_20260907.md` and associated tranche notes  
**Companion implementation note:** `docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md`

## Core thought

A cognitive system may not need its specialised subsystems to converge upon one common internal representation. It may instead need them to remain **mutually legible**.

The distinction matters.

A system can contain task-relevant information without a downstream consumer being able to use it. It can also contain different high-dimensional representations of the same situation in different modules, while preserving only a lower-dimensional interface through which selected information is exchanged. Development may therefore improve integration without homogenising internal representations.

The working proposition is:

> **Specialised cognitive systems may preserve distinct high-dimensional internal representations while coordinating through low-dimensional, context-sensitive communication subspaces and low-complexity transformations. Development can increase both local specialisation and selective inter-system legibility. Replay and sleep may selectively stabilise or reconfigure these interfaces rather than globally aligning all representations.**

For REE, this suggests that some apparent representational failures may instead be failures of **routing, interface geometry, readout, or temporal compatibility**.

This thought extends, rather than replaces, the existing `z_world` representation contract. That document asks what information must survive the observation -> `z_world` boundary. The present document asks the next question:

> If the information survives, **where must it sit, in what geometry, and through what interface must it pass for the actual consumer to use it?**

---

## 1. Why this thought became necessary

### 1.1 The current z_world problem is no longer well described as simple compression loss

The 2026-09-07 waypoint-field DV-range probe (`ree-v3` commit `f00402c9`) measured directional information at the raw observation and after severe compression. Mean lift across five seeds was:

- raw observation: **+0.269**;
- random 275 -> 32 linear projection: **+0.211** (~78% retention);
- untrained SplitEncoder: **+0.167** (~62% retention).

A random projection that knows nothing about REE preserved a large fraction of the directional signal. Therefore a null downstream result cannot automatically be interpreted as "32 dimensions were too small" or "z_world discarded the information".

The relevant alternatives include:

1. the trained representation truly destroyed the information;
2. the information remains decodable but is badly organised for the native consumer;
3. the information occupies directions the consumer does not read;
4. the consumer receives the relevant directions but transforms them through a collapsing or untrained interface;
5. the consumer is sensitive to channel activity but not to the correct example-specific content;
6. the static information is present but the sender and receiver disagree about temporal dynamics.

These hypotheses are experimentally distinguishable.

### 1.2 REE already contains a crucial negative result

The representation -> authority -> selection analysis around SD-004/SD-080/V3-EXQ-817a is especially important.

The action-object representation was successfully made more consequence-structured. Controls indicated that the intended grounding took. Yet behaviour did not improve. The existing analysis localised a remaining open link at the consumer/decoder side: the improved representation still passed through an interface whose effective action decoding collapsed.

The lesson is not that representational quality does not matter. The lesson is that:

> **a representation can improve while behaviour remains unchanged because the consumer cannot express the improvement.**

That result should be treated as a prior for all future representation-side interventions.

### 1.3 REE already anticipated the complementary half

`2026-09-04_z_world_representation_contract.md` states that `z_world` need not expose a hand-written ontology or interpretable coordinate system. It must preserve distinctions that downstream systems need for prediction, counterfactual comparison, memory, planning and regulation.

`2026-08-31_replay_driven_rebucketing_decision_relevant_representation.md` proposes that replay can split, merge and reweight representations after consequences reveal which distinctions mattered, and that sleep-like decoupling may provide a safe period for maintenance of the representational coordinate system.

The present thought connects these two ideas by introducing **interface legibility as a separate developmental variable**.

---

## 2. The conceptual ladder: representation is not one thing

The literature on latent communication repeatedly exposes a problem that REE should make explicit in its own experimental vocabulary.

A variable can be:

1. **encoded** — statistically present in a representation;
2. **decodable** — recoverable by an external probe;
3. **natively accessible** — usable by the system's existing consumer;
4. **bridgeable** — made usable through a constrained map between frozen endpoints;
5. **pairing-specific** — useful specifically when the correct sender state is paired with the correct receiver situation;
6. **causally used** — interventions on its content alter downstream computation or behaviour;
7. **behaviourally useful** — its causal use improves adaptive performance.

These properties must not be collapsed.

A central doctrine for REE should therefore be:

> **decodable != accessible != bridgeable != pairing-specific != causally used != behaviourally beneficial.**

This matters because linear probes are easy to overread. A probe can demonstrate that information exists somewhere in a latent space while saying almost nothing about whether the native pathway ever accesses it.

---

## 3. External artificial-intelligence convergence

### 3.1 Mostik: independently trained systems may be bridgeable

Mostik publicly describes a bridge between frozen GLM-5.2 (753B) and Qwen-3.5 (4B) models. The large model produces an internal state; the bridge translates it; the smaller model performs generation. Mostik frames the problem explicitly as one of geometry: different models share some structure, but alignment should not be assumed to arise automatically.

This is currently a company-reported result rather than a fully disclosed, independently replicated scientific result. Its value for REE is therefore primarily conceptual and experimental: it motivates testing whether independently organised systems can be connected through relatively small learned transformations while leaving the systems themselves frozen.

Mostik should not be treated as proof that REE needs such bridges.

### 3.2 Interlat: heterogeneous latent communication is feasible

Du et al., ACL 2026, *Enabling Agents to Communicate Entirely in Latent Space*, demonstrate inter-agent communication using continuous last hidden states rather than text. Their experiments include heterogeneous model families and learned compression; the paper reports competitive performance with inference acceleration up to 24x under aggressive latent compression.

The important point is not the speedup. It is that a receiver can learn to exploit structured latent information from a differently organised sender without forcing both models to share weights or token vocabulary.

### 3.3 StateBridge: some incompatibilities may be shallow

Peng et al., 2026, *StateBridge*, align sender hidden states to a receiver input space using a closed-form orthogonal Procrustes transform plus norm calibration and vocabulary anchoring. The method is training-free at the bridge itself and reports best or tied-best results on most evaluated model-task pairs.

StateBridge should not be overgeneralised: its present evaluation does not establish arbitrary translation among independently trained heterogeneous agents in the strongest Mostik sense. But it supplies a crucial experimental idea for REE:

> **try the least expressive transformation first.**

If a rotation or affine map rescues a frozen interface, the problem was not a missing cognitive mechanism. It was a coordinate/interface mismatch.

### 3.4 Causal audits show why channel ablation is insufficient

Recent causal audits of latent channels replace transmitted states with:

- the correct paired state;
- a state from another example;
- zero;
- moment-matched random states.

Cheng, Das & Ramnath (2026) show a striking case where zeroing a relay cost 14.7 percentage points while substituting the wrong example's cache cost only 0.4 points. A channel can therefore be strongly load-bearing while its **example-specific informational content is barely load-bearing**.

This should become standard REE experimental hygiene wherever an internal message or bridge is claimed to carry meaningful content.

---

## 4. The stronger biological analogue: communication subspaces

Hyperalignment initially seemed the obvious biological analogue: different brains can preserve shared informational geometry despite idiosyncratic coordinates.

The communication-subspace literature is more directly relevant.

### 4.1 High-dimensional local computation, low-dimensional communication

Semedo and colleagues showed that interactions between cortical areas can be captured by low-dimensional subsets of the source population activity. Most dimensions important to local population activity need not be equally visible to another area.

Binish et al. (Nature Neuroscience, 2026) identify a communication subspace between human prefrontal and motor cortex. High-dimensional prefrontal activity supports contextual computation, while a lower-dimensional subspace selectively relays information predictive of context-dependent action. Activity in the communication subspace predicts behaviour better than either area's total activity considered alone.

This creates a direct hypothesis for REE:

> A task variable may be strongly encoded in the full sender latent but weakly represented in the **consumer-facing subspace**.

That produces the phenotype:

`external probe succeeds -> native behaviour fails`

without requiring information destruction.

### 4.2 The same neurons can participate in different interface geometries

Gonzalez et al. (Nature, 2026), studying the hippocampal-retrosplenial axis, show that different interfaces can recruit overlapping neuronal populations while arranging joint activity in substantially rotated communication subspaces.

This is important conceptually. A "representation" need not belong to a cleanly segregated population. The same substrate can participate in multiple relational geometries depending on which input/output interface is active.

For REE, this argues against prematurely creating duplicated representations whenever two consumers appear to need different information formats. A single rich latent may support several **selective projections or communication subspaces**.

### 4.3 Specialisation and integration can increase together

Developmental neuroscience shows that hippocampal subregions can become more functionally specialised while preferential cortical connectivity simultaneously strengthens.

This suggests a useful developmental prediction:

> **local specialisation can rise at the same time as interface legibility rises.**

REE should therefore not use increasing representational similarity between E1, E2, hippocampus and E3 as its default marker of maturation.

A more plausible mature system may be one in which each subsystem becomes better at its own computation while the **small amount of information that needs to cross each boundary becomes increasingly well organised for that boundary**.

---

## 5. A representation may be adequate only relative to its decoder

Spens & Burgess (Nature Communications, 2026) propose a model of hippocampo-neocortical interaction in which episodic memories are stored in compressed conceptual form and reconstructed by a neocortical generative model. In that formulation, compression is not judged by whether the compact trace contains a self-sufficient literal copy of the experience. It is judged by whether the appropriate receiver can reconstruct what is needed.

This resonates directly with MECH-532, registered in REE before the present Mostik discussion: a designated compression site should be paired with a trained decompression/readout stage before ceiling nulls measured there are considered interpretable.

The broader principle is:

> **representation adequacy is relational.**

A compressed state cannot always be judged independently of the consumer that reads it.

This does not mean any decoder may rescue any representation. A sufficiently powerful decoder can become a covert second cognitive system. The strength of the claim depends on the complexity of the mapping required.

Hence the importance of a **translation-complexity ladder**:

- native readout;
- orthogonal transformation;
- affine transformation;
- low-rank adapter;
- constrained nonlinear bridge;
- high-capacity bridge as an upper bound only.

The simpler the bridge that works, the stronger the evidence that the sender already contained an appropriately structured representation.

---

## 6. Static alignment may still be the wrong target

Representations in REE are not static lookup tables. E1 and E2 are predictive dynamical systems.

NoMAD (Nonlinear Manifold Alignment with Dynamics) shows that neural-manifold alignment becomes more stable when temporal dynamics constrain the mapping, rather than treating each state as an independent point.

For REE, this means a bridge should not be judged only by whether:

`B(z_t)` resembles a receiver state.

It should also be judged by whether:

`B(z_{t+1})`

is compatible with where the receiver expects its own state to evolve from `B(z_t)` under the relevant action/context.

A pointwise map can succeed while destroying transition geometry.

Therefore **dynamic mutual legibility** may be a more important quantity than static similarity.

---

## 7. Sleep and replay: from global alignment to selective interface maintenance

The strongest version of the early hypothesis was:

> sleep may make independently specialised representations easier to translate.

The current evidence supports a more nuanced version.

Gonzalez et al. report different stability/plasticity behaviour across hippocampal communication subspaces during post-learning sleep. Some interfaces show learning-related reactivation and plasticity, whereas cortical-facing mappings can remain comparatively stable.

This suggests a **plasticity-stability division of labour** among interfaces.

The REE hypothesis should therefore be:

> **offline consolidation selectively changes interface geometry where adaptation is useful while preserving stable mappings whose continuity is required by downstream consumers.**

This sits naturally beside the existing replay/rebucketing thought. Sleep may maintain at least three things:

1. **the representation itself** — split/merge/reweight equivalence classes;
2. **the index** — keep episodic access coherent after representational change;
3. **the interface** — adjust or stabilise the subspace through which another subsystem reads the revised representation.

This third function is the new addition.

Crucially, the campaign has not yet found direct biological evidence that sleep reduces a formal bridge-complexity metric between two independently specialised systems. That remains a **REE hypothesis**, not an established neuroscience claim.

---

## 8. Mutual legibility as a developmental variable

The concept can be operationalised.

For two systems A and B, define a family of constrained mappings `T_k` of increasing complexity. At a developmental checkpoint, ask what minimum class is required to preserve the task-relevant structure that B needs from A.

A rough measure is:

`L(A -> B) = minimum bridge complexity achieving a predeclared held-out functional criterion`

where the criterion includes both correct content use and distribution/dynamics checks.

Lower `L` means greater mutual legibility.

But lower is not always better in isolation. If two systems become identical because one loses its specialisation, `L` might decrease while overall cognition worsens.

Therefore development should track at least two axes:

- **local specialisation/competence**;
- **cross-system mutual legibility**.

A mature result of interest would be:

`specialisation up + mutual legibility up`

rather than global convergence.

---

## 9. Communication subspaces as interface contracts

The existing `z_world` representation contract is mostly sender-facing: do not throw away distinctions the organism repeatedly needs.

This thought suggests a complementary **interface contract**:

> For each consumer, the sender must expose the distinctions that consumer needs in a subspace and temporal geometry that the consumer can reliably access, without requiring the sender's full internal representation to be homogenised around that consumer.

A good interface therefore has several properties:

- **content sufficiency:** required distinctions are present;
- **selective exposure:** relevant content overlaps the consumer-facing subspace;
- **low translation complexity:** mapping does not require a second cognition engine;
- **dynamic compatibility:** transition structure survives;
- **pairing specificity:** correct episode/state content matters;
- **causal efficacy:** perturbing the relevant subspace alters the predicted downstream computation;
- **specialisation preservation:** improving the interface does not force the sender to abandon useful local structure.

This could eventually become a family of explicit architectural invariants, but it should first remain an experimental hypothesis.

---

## 10. Implications for specific REE boundaries

### 10.1 observation -> z_world

Question: did the encoder destroy information, or merely rotate/entangle it relative to downstream readers?

The random-projection result means the null baseline must not be zero. A trained `z_world` should be compared against dimensionality-matched random projections and against its native consumer-facing subspace.

### 10.2 z_world -> E1/E2

E1 and E2 need not consume the same directions of `z_world`.

The relevant question is whether each has an appropriate low-dimensional read surface for the distinctions it needs. If E1 needs transition persistence while E2 needs action-contingent local geometry, forcing all information into one globally optimised coordinate system may be unnecessary or harmful.

### 10.3 E1 <-> E2

Parallel predictive systems may develop distinct state geometries. Mutual legibility may concern only action-conditioned consequence structure, uncertainty, or a subset of predictive state.

A bridge that preserves pointwise states but not rollout dynamics is especially suspect here.

### 10.4 ContextMemory

Current held-out linear probes ask what is written and remains decodable. The next question is whether the **retrieval/consumer pathway reads the same content-bearing directions**.

ContextMemory may be a particularly clean location for separating encoded, retrieved, and causally used content.

### 10.5 hippocampus -> E3 / planning consumer

The action-object history already shows why representation-side grounding can fail through a collapsing decoder.

The planner interface is therefore a prime candidate for communication-subspace analysis: which dimensions of hippocampal/proposal state actually alter E3 comparison and committed action?

### 10.6 sleep/replay interfaces

The existing `force_sleep_cycle_at_eval_boundary` substrate makes within-run pre/post interface measurements possible without resetting the entire organism.

This creates a direct path to testing whether one sleep cycle changes:

- sender content;
- communication-subspace rank;
- task-variable overlap with that subspace;
- required bridge complexity;
- downstream behavioural sensitivity.

---

## 11. Competing hypotheses

The thought should be protected from becoming self-sealing. At least five alternatives should remain live.

### H1 — Information-loss hypothesis

The sender genuinely discards task-relevant information. No reasonable frozen-endpoint bridge can recover consumer performance, while richer source inputs can.

### H2 — Coordinate-mismatch hypothesis

The information is present and a low-complexity transformation makes it usable.

### H3 — Communication-subspace routing hypothesis

The full sender contains the information, but the native consumer-facing subspace excludes or attenuates it.

### H4 — Consumer-computation hypothesis

The relevant information reaches the consumer, but the consumer's own computation is inadequate.

### H5 — Generic-channel hypothesis

Performance depends on the presence/statistics of an internal channel more than on its correct example-specific content.

### H6 — Dynamic-mismatch hypothesis

Static information is mutually decodable, but sender and receiver transition geometries are incompatible over trajectories.

Different REE failures may instantiate different hypotheses. The goal is not to prove one universal interface mechanism.

---

## 12. Predictions

If this thought is useful, several predictions follow.

1. **Some current REE nulls will show substantial task information in the full sender latent but little overlap with the native consumer communication subspace.**
2. **At least some failures will be rescued by orthogonal or low-rank transformations between frozen endpoints.**
3. **Such rescue will not occur uniformly; some loci will prove to be genuine information-loss or consumer-computation failures.**
4. **Correct-pair versus mismatched-pair controls will split apparent communication effects into content-specific and generic-channel classes.**
5. **Development can increase local subsystem differentiation while reducing the complexity of the mappings required at selected interfaces.**
6. **Sleep/replay effects will be interface-specific rather than globally alignment-increasing.** Some mappings may become more plastic, others more stable.
7. **Dynamic alignment measures will explain failures that static linear decoding misses, particularly for E1/E2 rollout interfaces.**
8. **Training a compression without its consumer/readout will continue to produce misleading ceiling nulls, consistent with MECH-532.**

---

## 13. What would falsify or materially weaken the thought?

The broadest version would be weakened if:

- across relevant REE interfaces, task information is either absent or already natively accessible, leaving little evidence for routing/geometry mismatch;
- constrained bridges consistently fail while high-capacity nonlinear networks succeed only by learning new task computation;
- consumer-facing subspaces are not lower-dimensional or selective in the relevant interfaces;
- correct-vs-mismatched controls show that apparent interface rescues are primarily generic-channel effects;
- developmental or sleep manipulations change individual representations but produce no systematic change in interface measurements;
- a simpler explanation such as missing supervision, dead gradients, or inadequate candidate diversity explains the same failures more directly.

A null at one interface should not falsify the general possibility. But repeated failure across the specifically predicted current loci should substantially reduce confidence.

---

## 14. Architectural implications if supported

This thought does **not** yet imply permanent bridge modules.

The safest progression is:

1. use bridges and subspace methods as external diagnostic instruments;
2. establish content-specific causal use with frozen endpoints;
3. determine whether the required mapping is simple and stable;
4. identify whether an existing REE pathway ought already to learn that mapping;
5. only then consider architectural implementation.

If implementation becomes justified, the likely pattern is not a universal latent translator. More plausible options include:

- small consumer-specific projections;
- explicit trained decompression/readout pairing at designated compression sites;
- low-rank communication surfaces learned under consumer loss while protecting sender specialisation;
- context-gated subspace routing;
- sleep/offline recalibration for plastic interfaces;
- stable scaffolds for interfaces whose coordinate continuity is more important than rapid plasticity;
- dynamics-aware interface objectives for predictive systems.

Any permanent interface must remain subject to non-oracularity, provenance, and hypothesis-versus-observation separation constraints already present in REE.

---

## 15. Relationship to ARC-121 and shared epistemic state

ARC-121 currently explores a shared epistemic-state object framing. The present evidence introduces a serious alternative interpretation:

A system may share **format or selectively translated content** without sharing one literal state object.

Possible architectures include:

1. one common epistemic object consumed by multiple systems;
2. specialised state objects with a shared low-dimensional interface format;
3. specialised state objects connected by context-specific translations;
4. a hybrid: common invariant core plus specialised private dimensions.

The communication-subspace evidence makes options 2-4 credible enough that ARC-121 should not be used to prejudge the issue. No claim change is proposed here.

---

## 16. Relationship to multiple realizability and compensation

The recent compensatory-amplification framing becomes more interesting under this model.

If function can be realised through several internal pathways, compensation may depend not only on whether an alternative representation exists but whether downstream systems can become **legible to it**.

A compensatory pathway might therefore emerge through:

- strengthening an existing communication subspace;
- rotating which dimensions are exposed to a consumer;
- recruiting a new low-rank readout;
- changing temporal coupling;
- allowing replay to retune cross-system correspondence.

Thus multiple realizability is not merely a property of internal representations. It may also be a property of **interfaces among representations**.

---

## 17. Working synthesis

The emerging picture is not of one latent world model gradually becoming universal.

It is closer to a federation:

```text
rich specialised representation A
        |       private dimensions
        |\
        | \ communication subspace A->B
        |  \
        v   v
     consumer B ---- specialised local dynamics
        |
        | communication subspace B->C
        v
     consumer C
```

Each subsystem may preserve dimensions invisible or irrelevant to its neighbours. What matters is that the right distinctions become available at the right boundaries, in a geometry and temporal regime the receiver can use.

Development then has at least three simultaneous jobs:

1. improve local representations;
2. determine what information should cross each boundary;
3. maintain or revise the mappings through which that information becomes usable.

Replay and sleep may contribute to all three, but not necessarily in the same direction at every interface.

The main architectural principle is therefore:

> **Integration does not require representational sameness. It requires selective mutual legibility.**

And the main experimental principle is:

> **Before declaring a representation inadequate, determine whether the needed information is absent, merely inaccessible to the native consumer, outside the active communication subspace, dynamically incompatible, or present only as a generic channel effect.**

---

## 18. Evidence status summary

### Established / directly supported externally

- latent communication can transmit useful information without text (Interlat);
- constrained geometric alignment can sometimes support latent-state transfer (StateBridge);
- channel dependence can be dissociated from example-specific content by mismatched-message causal audits;
- cortical/hippocampal systems can communicate through lower-dimensional subspaces embedded in higher-dimensional local activity;
- local specialisation and selective connectivity can co-develop;
- compressed hippocampal-like representations can be useful relative to a generative receiver;
- dynamics can improve latent-manifold alignment stability.

### Supported by REE internal evidence

- strong dimensional compression need not erase the waypoint-direction signal (`f00402c9`);
- representation improvement can fail to alter behaviour through a collapsing downstream interface (V3-EXQ-817a lineage);
- REE already requires paired compression/decompression at at least one designated locus before ceiling nulls are interpreted (MECH-532);
- replay/sleep substrate exists for within-run offline interventions.

### Plausible REE interpretation

- some current z_world/consumer failures may reflect communication-subspace mismatch rather than absent information;
- E1, E2, hippocampus and E3 may benefit from preserving specialised private geometry with selective read surfaces.

### New REE hypothesis

- development and/or sleep can improve **mutual legibility** between specialised REE systems while preserving or increasing their local specialisation;
- different interfaces may have different plasticity/stability schedules during offline consolidation.

---

## 19. Key external references

- Mostik. *Latent communication between AI models* (public technical description, 2026). https://mostik.ai/read-more
- Du Z et al. *Enabling Agents to Communicate Entirely in Latent Space*. ACL 2026. DOI: 10.18653/v1/2026.acl-long.1248.
- Peng Y et al. *StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems*. arXiv:2608.13317 (2026).
- Cheng J, Das S, Ramnath R. *When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs*. arXiv:2608.04893 (2026).
- Zhang H, Emu M. *Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM*. arXiv:2607.26773 (2026).
- Semedo JD et al. *Cortical areas interact through a communication subspace*. Neuron (2019).
- Binish N et al. *A communication subspace relays context-dependent actions from human prefrontal to motor cortex*. Nature Neuroscience 29, 1690-1698 (2026). DOI: 10.1038/s41593-026-02290-4.
- Gonzalez J et al. *Subspace communication in the hippocampal-retrosplenial axis*. Nature 655, 192-201 (2026). DOI: 10.1038/s41586-026-10481-z.
- Spens E, Burgess N. *Hippocampo-neocortical interaction as compressive retrieval-augmented generation*. Nature Communications 17, 7971 (2026). DOI: 10.1038/s41467-026-74357-6.
- Karpowicz BM et al. *Stabilizing brain-computer interfaces through alignment of latent dynamics* (NoMAD). Nature Biomedical Engineering / open manuscript record, 2025.

## 20. REE internal anchors

- `docs/thoughts/2026-09-04_z_world_representation_contract.md`
- `docs/thoughts/2026-08-31_replay_driven_rebucketing_decision_relevant_representation.md`
- `evidence/planning/latent_interface_translation_campaign_20260907.md`
- `ree-v3` `f00402c9` — waypoint-field DV-range probe
- `ree-v3` `14c44906` — V3-EXQ-1008 z_world adequacy/re-basing portfolio
- `REE_assembly` `0c125b019` — representation->authority->selection correction and V3-EXQ-817a interpretation
- `REE_assembly` `bd1e457f9` — MECH-532 compression/decompression-pairing registration
- `ree-v3` `de26949aa` — force sleep cycle at eval boundary
