# Hippocampal Translation Maps — REE Archaeology

**Date:** 2026-09-09  
**Status:** archaeology / synthesis; not a claim registration, implementation decision, or experiment-queue mutation  
**Scope:** internal REE conceptual and experimental genealogy only. Biological adequacy of the resulting synthesis is **not** adjudicated here and requires a separate literature campaign.  
**Archaeology rule:** distinguish **direct genealogy**, **earlier precursor**, **independent convergence**, and **experimental convergence**. Do not infer historical dependence merely because later ideas resemble earlier ones.

## Question

The immediate question is whether the current intuition of the hippocampal system as potentially supporting **translation among differently organised representational systems** is new to REE, or whether it is a synthesis of ideas already present in separate parts of the project.

The answer from the live repository is:

> **REE has repeatedly approached the translation problem from different directions, but it has not previously contained one general “hippocampal translation maps” doctrine.**

There are at least four partially independent lineages:

1. an early **E2 ↔ hippocampal handoff / path-memory / replay** lineage;
2. a **developmental pruning and representational reorganisation** lineage;
3. a **decision-time representational transformation and mutual-legibility** lineage;
4. an **experimental z_world → consumer failure** lineage that has independently forced the same distinction between information being present and information being usable.

The useful new synthesis is therefore not “the hippocampus stores maps” and not “the hippocampus is a generic translator.” It is the narrower hypothesis that hippocampal/episodic machinery may help maintain, learn, select, or replay **relational mappings and reference frames** through which specialised systems remain mutually legible despite using different internal geometries.

That synthesis is plausible enough to organise the next research campaign, but is not yet an REE claim.

---

# 1. Archaeological method

This pass asks four questions of each relevant source:

1. **What computational problem was it originally trying to solve?**
2. **Did it explicitly propose translation, or only a precursor such as handoff, indexing, remapping, replay, or consumer-specific access?**
3. **Is there a documented parent/child relation, or only later conceptual resemblance?**
4. **What survives into the current synthesis without rewriting the historical source?**

Sources examined include, at minimum:

- `docs/thoughts/2026-02-09_e2_hpc_interface.md`
- `docs/architecture/hippocampal_systems.md`
- `docs/architecture/developmental_pruning_and_sparse_memory_cognifold.md`
- `docs/thoughts/2026-09-03_temporary_coordinated_representational_transformations.md`
- `docs/thoughts/2026-09-03_ree_as_predictive_sensorimotor_transformation.md`
- `docs/thoughts/2026-09-04_z_world_representation_contract.md`
- `docs/thoughts/2026-09-04_developmental_ontology_and_replay.md`
- `docs/thoughts/2026-09-07_mutual_legibility_communication_subspaces.md`
- `docs/thoughts/2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md`
- `docs/thoughts/2026-09-08_developmental_overcapacity_pruning_sparse_interfaces.md`
- `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`
- the V3 experimental lineage `978 → 1002 → 1008 → 1010`.

This document does **not** use resemblance to promote a new claim. It records the genealogy and identifies discriminating questions for later work.

---

# 2. Earliest currently evidenced precursor: E2 kernel → hippocampal rollout handoff

## 2.1 February 2026: division of computational labour

`2026-02-09_e2_hpc_interface.md` makes a clean early distinction:

- E2 is a **forward-prediction kernel**, producing short-horizon conditional transitions;
- hippocampal systems **chain those kernels into explicit multi-step rollouts**;
- the chaining occurs under E1 constraints and control-plane rollout parameters.

This is not yet a translation theory. It is, however, the earliest currently evidenced REE statement that one subsystem produces a representation/computational object that another system must organise into a different functional form.

The mature architecture record, `hippocampal_systems.md`, preserves and sharpens this as MECH-033. Importantly, the later V2 failure note says the interface can be **structurally present while passing the wrong type of representation**: chaining sensory-state predictions into the hippocampal pathway produced negligible benefit, and the handoff was reframed around E2 **action-consequence objects** rather than sensory transitions.

That is a major archaeological precursor to the present question.

The historical lesson was already:

```text
interface exists
+ information/prediction exists
+ wrong representational object crosses boundary
→ downstream system gains little
```

This is recognisably the same class of problem now seen at `z_world → consumer`, although the February work did not describe it as “translation.”

## 2.2 Hippocampus as indexing, replay, and hypothesis injection

The same architecture document gives the hippocampal braid several properties relevant to later translation ideas:

- it stores **indexed trajectories**, not isolated states;
- it performs pattern separation and completion;
- it can inject structured remembered/counterfactual trajectories into predictive systems;
- it emits **routing signals for offline reprojection**;
- it provides context switching and one-shot episodic indexing;
- it is explicitly barred from directly deciding, valuing, or overwriting perception.

These constraints matter. They suggest that if a hippocampal translation role exists in REE, it should probably not be implemented as an unrestricted latent-to-latent super-decoder. The older architecture already treats hippocampal output as **structured hypothesis/index/routing content** that other systems consume under gating.

### Archaeological classification

**Type:** early precursor, not proven direct ancestor of the September mutual-legibility work.  
**Surviving contribution:** interfaces can fail because they pass the wrong representational object; hippocampal systems already sit at a boundary where structured predictive objects are chained, indexed, replayed, and reprojected.

---

# 3. A second early branch: hippocampal maps as learned relational geometry

The March reframe embedded in `hippocampal_systems.md` is especially relevant. ARC-018 moves viability mapping away from E1 prediction error and into a hippocampal map indexed by **E2 action-object coordinates**, updated by E3 harm/goal error.

This means the hippocampal map is not merely a stored spatial picture. It is a learned geometry over relations of the form:

```text
context + action consequence + experienced outcome
```

The architecture describes this as learned affordance/viability geometry under actual commitment.

That provides an important precursor to the present “translation map” intuition: a map can act as a **relational indexing surface** between what one system predicts (E2 action consequences), what another evaluates (E3 outcome error), and what can later be replayed or chained.

It still does not establish that the hippocampus translates arbitrary E1/E2/z_world geometries. But it makes the stronger synthesis historically less foreign to REE than it first appears.

### Archaeological classification

**Type:** architectural precursor.  
**Surviving contribution:** hippocampal maps can be indexed in the coordinate system of one subsystem while being labelled by consequences supplied by another; this is already a cross-system relational structure.

---

# 4. Independent developmental branch: dense exploration → sparse structured memory

## 4.1 June 2026: MECH-362 and Q-057

`developmental_pruning_and_sparse_memory_cognifold.md` predates the current over-capacity-decoder discussion by months.

It registers:

- **MECH-362:** subtractive developmental sparsification;
- **Q-057:** whether REE should distinguish an early over-connected exploratory substrate from a mature sparse/structured substrate.

The proposed trajectory is:

```text
over-connected exploratory phase
→ pruning / selection
→ sparse structured retrieval
```

and the document explicitly warns that pruning need not mean deletion: down-weighting, gating, or de-authorisation are possible computational analogues.

This is important archaeologically because the September intuition that a mature efficient interface might require a richer developmental starting point was **not** wholly new. The core dense-to-sparse developmental motif already existed in REE.

## 4.2 What the September overcapacity thought adds

The newer `2026-09-08_developmental_overcapacity_pruning_sparse_interfaces.md` is therefore best read as a **convergent extension**, not an origin story.

It adds several things not explicit in the June memory-circuit compass:

- overcapacity applied specifically to **inter-system interfaces/transformations**, not only recurrent memory connectivity;
- minimum bridge complexity `L(A → B)` as a developmental variable;
- the hypothesis that competence can rise while required bridge complexity falls;
- the same-final-capacity four-arm developmental test;
- especially the critical Arm D: reinitialise the final sparse architecture from birth to separate “good architecture discovered” from “developmental path itself mattered”;
- the idea of an over-capacity decoder as a **developmental scaffold/teacher candidate**, rather than a mature architectural component.

### Archaeological classification

**June → September relation:** independent precursor/convergence rather than a simple direct continuation unless a later intake explicitly links them.  
**Surviving contribution:** a future hippocampal translation system could plausibly begin permissive/overcomplete and mature toward sparse, low-complexity mappings; this remains a developmental hypothesis, not a V3 build instruction.

---

# 5. September reframing: from stored information to usable form

## 5.1 Temporary Coordinated Representational Transformations (TCRT)

The 3 September TCRT thought is the major conceptual pivot.

Its central distinction is:

> information being present in a representation is not the same as that information being present in the form required by the computation currently being performed.

It proposes a temporary decision-relevant representation:

```text
R_(t,a) = T(S_t, D_t, a)
```

where rich substrate, directive state, and candidate action jointly determine a representation in which the current relationship becomes easier to use.

This is broader than hippocampus. TCRT is distributed and recurrent by design. The document explicitly resists introducing a single executive “packet assembler.”

For archaeology, this means the current hippocampal-translation idea must not supersede TCRT by saying “the hippocampus performs the translation.” A better relation is:

> hippocampal maps may be **one source of relational indexing, remembered context, candidate structure, or learned mappings that participate in TCRT**.

TCRT remains the more general computation.

## 5.2 Predictive sensorimotor transformation

The companion predictive-sensorimotor framing treats modules less as nouns and more as transformations over state. This makes the question “what form does information take at this interface?” more natural than asking which module “owns” a concept.

The hippocampal translation-map synthesis therefore fits best as a **transformational role** that may be distributed across hippocampal, entorhinal, predictive, and control processes rather than as an extra static representational store.

### Archaeological classification

**Type:** direct conceptual precursor to the current synthesis.  
**Surviving contribution:** translation is context/candidate-dependent transformation of relationships, not simply vector conversion.

---

# 6. Representation contract and replay: two complementary maintenance problems

## 6.1 `z_world` representation contract

The 4 September `z_world` contract asks what must survive the observation boundary so that the organism can discover its own useful ontology. It explicitly distinguishes:

- preserving consequential distinctions;
- avoiding premature over-compression;
- allowing categories to split/merge/reweight during development;
- temporary supervision scaffolds versus durable organising structure.

This is sender-side integrity.

It says, approximately:

```text
Do not destroy what future cognition will need.
```

It does **not** guarantee that what survives is conveniently readable by every consumer.

## 6.2 Developmental ontology and replay

`2026-09-04_developmental_ontology_and_replay.md` then asks whether replay can reorganise the representational scheme itself—splitting, merging, and reweighting categories after consequences reveal which distinctions mattered.

This creates two maintenance problems:

1. **representation maintenance:** what distinctions should exist?
2. **interface maintenance:** after those distinctions move, how do other systems continue to refer to them?

The second problem is not fully solved by the developmental-ontology thought itself. It becomes explicit in the later mutual-legibility work.

This is one of the clearest places where a hippocampal “translation map” becomes attractive: if replay changes the ontology, episodic/indexing machinery may need either to update old indices or to provide a bridge between old and new organisation.

But that is still a hypothesis. Replay could instead reorganise the source and consumers jointly through ordinary gradient learning, with no persistent translation map at all.

### Archaeological classification

**Type:** direct conceptual convergence with the later interface-maintenance problem.  
**Surviving contribution:** replay may reorganise representational categories; therefore stable memory and cross-system use require some solution to remapping/reference continuity.

---

# 7. Mutual legibility: translation becomes explicit

## 7.1 7 September: specialised systems need not share one latent language

`2026-09-07_mutual_legibility_communication_subspaces.md` is the point where the translation problem becomes explicit and systematic.

Its central proposal is that specialised systems may keep distinct high-dimensional internal representations while coordinating through:

- low-dimensional communication subspaces;
- low-complexity transformations;
- consumer-specific read surfaces;
- dynamically compatible interfaces.

It introduces the important ladder:

```text
encoded
→ decodable
→ natively accessible
→ bridgeable
→ pairing-specific
→ causally used
→ behaviourally useful
```

and later work adds recurrent stability.

This is much closer to the present intuition than the February handoff architecture.

It also introduces a bridge-complexity ladder:

```text
native readout
→ orthogonal map
→ affine map
→ low-rank adapter
→ constrained nonlinear bridge
→ high-capacity bridge as upper bound only
```

That ladder is the conceptual parent of interpreting 1010 correctly. An enormous decoder is useful as an **existence probe**; it is not automatically an appropriate mature cognitive interface.

## 7.2 Hippocampal relevance already appears here

The mutual-legibility thought already identifies hippocampal-cortical communication subspaces and replay/interface maintenance as relevant biological analogues. It explicitly suggests that sleep may maintain three things separately:

1. the representation;
2. the index;
3. the interface.

That is very close to the current “translation map” research question.

### Archaeological classification

**Type:** direct parent lineage.  
**Surviving contribution:** consumer-specific low-dimensional bridges, translation complexity as an empirical variable, and separation of representation, index, and interface maintenance.

---

# 8. Translation becomes relational and state-dependent

## 8.1 8 September: receiver-conditioned translation

The child thought `2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md` explicitly replaces a simple map:

```text
T(sender)
```

with:

```text
T(sender, receiver, receiver context/position)
```

This is a major step toward the present hippocampal-map intuition.

If a remembered episode or relational map is useful only relative to the receiver's current query/state, then a translation cannot be understood as a permanent one-to-one coordinate conversion. The same source state can legitimately expose different aspects to E1, E2, E3, or another consumer.

The same thought also adds **recurrent stability**: a bridge can be useful once yet corrupt a recurrent system when applied repeatedly.

That creates a strong constraint on any hippocampal translation-map hypothesis:

> a useful translation must preserve the receiver's future dynamics, not merely improve one snapshot readout.

### Archaeological classification

**Type:** direct child of mutual legibility.  
**Surviving contribution:** translation is relational to the receiver and must be stable under repeated closed-loop use.

---

# 9. Reference frames and temporal gates: maps become relational coordinates rather than arbitrary decoders

The 9 September child thought `2026-09-09_shared_reference_frames_and_temporal_gates.md` adds two further variables.

Its working decomposition is:

```text
effective interface
= content
× communication subspace
× reference frame
× receiver context
× temporal gate
```

with recurrent stability as an additional constraint.

This matters because “translation map” can otherwise become too vague.

A **communication subspace** says which sender directions are exposed.

A **reference frame** says what those directions are relative to:

- self-relative direction;
- allocentric position;
- episode identity;
- temporal order;
- action candidate;
- predicted consequence;
- self/other relation;
- causal source;
- another learned relational coordinate.

Two modules could therefore each contain direction information and still fail to communicate because one encodes it egocentrically and another allocentrically, or because one indexes current observation while the other expects predicted post-action position.

The same thought adds a **temporal gate**: a correct mapping can fail if it is engaged outside the phase in which the receiver is receptive, plastic, replaying the relevant episode, or evaluating the relevant candidate.

This is the clearest internal precursor to a genuinely map-like translation concept:

> heterogeneous systems may communicate by preserving a shared relational index even when their full internal geometries remain different.

### Archaeological classification

**Type:** direct child/sibling within the mutual-legibility lineage.  
**Surviving contribution:** translation may be organised around shared relational reference frames and phase-specific engagement, not arbitrary state-to-state fitting.

---

# 10. Experimental convergence: 978 → 1002 → 1008 → 1010

This lineage is especially important because it arose from organism performance rather than from the conceptual literature campaign.

## 10.1 V3-EXQ-978

Directional resource information was already substantially linearly decodable from `z_world`, while explicitly training a directional supervision head did not materially improve competence.

This weakened the simplest explanation:

```text
observation contains direction
→ z_world throws it away
→ behaviour fails
```

and opened the distinction between information preservation and behavioural accessibility.

This directly triggered TCRT.

## 10.2 V3-EXQ-1002

A policy-sized supervised reader could map the raw resource field to oracle action extremely well, but performed poorly from frozen trained `z_world`.

This substantially weakened “ordinary reinforcement-learning consumer failure” as the sole explanation. The problem survived when credit assignment was removed.

## 10.3 V3-EXQ-1008

A 32-dimensional PCA projection of the full 250-dimensional world input preserved enough structure for a supervised reader to clear the oracle-action criterion, while trained `z_world` remained far lower. Therefore **32 dimensions themselves were not the sufficient explanation**.

Simple linear rebasing/whitening of the existing `z_world` also failed to rescue it.

The remaining fork became sharper:

- perhaps decision-relevant content is actually discarded during encoding;
- or perhaps it survives in a form requiring a more complex nonlinear transformation.

## 10.4 V3-EXQ-1010

1010 is the direct over-capacity decoder discriminator.

Its conceptual role is:

```text
hold representation fixed
vary only decoder capacity
```

If a sufficiently expressive decoder can generalise from the frozen latent, then content survives and the problem moves toward **interface/reformatting complexity**.

If even very large decoders that can memorise the training data cannot generalise, while the PCA control does, then the case for **encode-time destruction of decision-relevant content** becomes much stronger.

The archaeological point does not depend on which way 1010 lands:

> the experiment sequence independently rediscovered the same hierarchy already present in the mutual-legibility thought: encoded/decodable/accessibility/bridgeability are different questions.

That is **experimental convergence**, not proof of the hippocampal translation-map hypothesis.

---

# 11. Genealogy versus convergence matrix

| Strand | Earliest currently evidenced form | Relation to current synthesis | Classification |
|---|---|---|---|
| E2 → hippocampal rollout | Feb 2026 E2 kernel/handoff | Different computational objects must cross a hippocampal boundary; wrong object can make a live interface useless | precursor |
| Hippocampal viability geometry | Mar reframe in ARC-018 | Map indexed in E2 action-object coordinates and labelled by E3 outcome error | precursor |
| Developmental sparsification | Jun MECH-362 / Q-057 | Early over-connected → mature sparse structure | independent precursor |
| TCRT | 3 Sep | Context/candidate-dependent transformation into usable relational form | direct conceptual parent |
| z_world representation contract | 4 Sep | Sender-side preservation of consequential distinctions | complementary parent |
| Developmental ontology/replay | 4 Sep | Replay can split/merge/reweight representation; creates index/interface-maintenance problem | convergent parent |
| Mutual legibility | 7 Sep | Explicit low-complexity translation and communication-subspace theory | direct parent |
| Receiver-conditioned translation | 8 Sep | `T(sender, receiver, context)`; recurrent stability | direct child |
| Developmental overcapacity interfaces | 8 Sep | Rich early translation space may later prune/distil | convergence with June + extension |
| Shared reference frames / temporal gates | 9 Sep | Cross-system common relational coordinates and phase-specific access | direct child/sibling |
| 978→1002→1008→1010 | Sep experimental lineage | Empirically separates information presence from native usability and bridge complexity | independent experimental convergence |

The repeated convergence is real. The genealogy is **not** one uninterrupted line. That distinction should be retained in future histories.

---

# 12. What “hippocampal translation map” should mean, if we use the phrase

The archaeology argues against defining it as:

```text
arbitrary latent A → arbitrary latent B decoder
```

That would duplicate the bridge concept and risks creating an unrestricted hidden cognitive module.

A narrower and more REE-consistent working definition is:

> **A hippocampal translation map is a learned, replayable relational indexing structure that helps a specialised consumer interpret selected content from another representational system by preserving or reconstructing the relevant relation among context, episode, candidate action, consequence, self/world state, and temporal phase.**

The word **map** matters because the object is relational/indexed.

The word **translation** matters because the same relation may be expressed differently in different systems.

The word **hippocampal** remains provisional because the biological campaign has not yet established that hippocampal circuitry performs a general translation function.

This definition deliberately leaves open whether the actual mechanism is:

- a sparse learned bridge;
- an episodic index that retrieves a receiver-compatible state;
- a shared relational frame;
- a replay-driven alignment process;
- a temporary overlay;
- a sequence of transformations distributed across hippocampus/entorhinal/predictive systems;
- or some combination.

---

# 13. Candidate computational roles exposed by the archaeology

The internal corpus suggests at least five separable roles that should not be collapsed prematurely.

## 13.1 Relational indexing

Bind episodes, actions, consequences, context, and temporal order so that heterogeneous systems can refer to the **same event/relation** without sharing identical coordinates.

## 13.2 Reference-frame mediation

Preserve or transform relations such as egocentric/allocentric position, action-relative consequence, episode identity, or trajectory phase.

## 13.3 Query-conditioned retrieval / translation

Use the current receiver state or query to determine which part of an episode/map becomes exposed.

This is closer to `T(sender, receiver, context)` than a fixed bridge.

## 13.4 Replay-based interface maintenance

When source or receiver representations reorganise during development, replay may help re-establish which indices/mappings still correspond to the same consequential structure.

## 13.5 Developmental scaffold and pruning

An immature system may permit many candidate mappings or broad associations, later pruning toward a sparse set of reliable cross-system relations.

These could all coexist, but each should get its own falsifier.

---

# 14. A provisional unifying equation

The archaeology suggests a richer interface model than a fixed bridge:

```text
U_(A→B,t)
= F(
    content_A,
    communication_subspace_(A→B),
    relational_frame,
    state_B,
    episodic/context_index,
    candidate_or_query,
    temporal_gate,
    developmental_history
  )
```

subject to:

```text
recurrent_stability > threshold
```

where `U_(A→B,t)` is not a new permanent latent ontology but the **usable influence** of A on B at that moment.

A hippocampal system could contribute to the `episodic/context_index`, `relational_frame`, `candidate_or_query`, and replay/development terms without being solely responsible for `F`.

This preserves TCRT's distributed nature while giving the hippocampal research campaign something concrete to look for.

---

# 15. Falsifiable assay family implied by the archaeology

The next campaign should not ask only “does a hippocampal bridge work?” It should discriminate among the roles above.

## A. Translation-complexity ladder

Freeze sender and receiver. Compare:

1. native readout;
2. orthogonal map;
3. affine map;
4. low-rank adapter;
5. constrained nonlinear bridge;
6. high-capacity upper-bound decoder.

Measure held-out functional recovery, not training fit alone.

## B. Receiver-conditioning test

Compare matched-capacity:

```text
T(A)
vs
T(A,B)
```

and permute B. If receiver conditioning matters only because of extra capacity, receiver permutation should not selectively destroy the gain.

## C. Reference-frame permutation

Hold content statistics approximately constant while rotating/permuting a relational frame such as:

- egocentric direction;
- allocentric anchor;
- episode identity;
- action-candidate index;
- temporal phase.

If correct content remains decodable but downstream use collapses specifically when the frame is mismatched, reference-frame mediation gains support.

## D. Correct-pair versus wrong-pair assay

Supply:

- correct sender state;
- wrong-example sender state;
- zero;
- moment-matched random state.

A channel that is merely load-bearing but not semantically specific should fail this distinction.

## E. Temporal-gating assay

Deliver the same correctly paired interface content:

- at the target replay/prediction/action phase;
- early-shifted;
- late-shifted;
- phase shuffled;
- not delivered.

Match amount/amplitude of communication where possible.

## F. Recurrent-stability assay

Compare one-step success with repeated closed-loop application. Measure:

- task performance over horizon;
- receiver-manifold drift;
- gain amplification;
- repeated evidence double-counting;
- dynamic compatibility.

## G. Developmental overcapacity/pruning assay

At matched final capacity:

1. small throughout;
2. large → prune/distil;
3. large throughout;
4. final pruned architecture reinitialised and trained from birth.

Arm 2 > Arm 4 is the key developmental-history discriminator.

## H. Replay-remapping assay

Change a representation or interface during development, then compare:

- no replay;
- neutral replay;
- consequence-linked replay.

Ask whether replay restores low-complexity cross-system use while preserving held-out behavioural transfer.

---

# 16. Negative explanations to preserve

The archaeology should make the research programme **more falsifiable**, not more inevitable.

The hippocampal-translation-map synthesis is weakened if:

- 1010 or later work shows the relevant content is simply destroyed at encode time;
- a small fixed native reader solves the interface after ordinary training;
- end-to-end joint learning makes explicit mappings unnecessary;
- representation and consumer naturally co-adapt without replay/index maintenance;
- a single shared communication subspace explains results without any hippocampal contribution;
- frame permutations do not matter once content is preserved;
- receiver-conditioned bridges add no benefit beyond matched extra capacity;
- replay changes memory strength but not interface complexity or transfer;
- developmental overcapacity confers no advantage at matched final architecture;
- apparent translation effects reduce to ordinary optimisation or memorisation;
- biological evidence shows hippocampal involvement is better explained by episodic retrieval/navigation without a general cross-system mapping role.

A particularly important caution is:

> **“Hippocampus participates in a task involving two representational systems” is not evidence that hippocampus translates between them.**

The biology campaign should demand causal or representational evidence that distinguishes indexing, retrieval, routing, and translation.

---

# 17. What is genuinely new after the archaeology

The project already had:

- E2→hippocampal handoff;
- hippocampal path/viability maps;
- hypothesis injection and replay;
- developmental sparsification;
- TCRT;
- replay-driven ontology change;
- mutual legibility;
- receiver-conditioned translation;
- shared reference frames;
- temporal gates;
- developmental interface overcapacity.

The new contribution is therefore **the synthesis of those pieces around a specific candidate hippocampal role**:

> **Hippocampal/episodic machinery may provide learned relational indices and replayable reference structures through which otherwise differently organised predictive systems can bring selected information into mutually usable form. These mappings may be receiver- and context-dependent, phase-gated, recurrently constrained, and developmentally simplified.**

That statement should remain a **research hypothesis**, not a registered claim, until the biological campaign determines whether the hippocampal analogy is supported beyond navigation/episodic-memory generalities.

---

# 18. Relationship to V3 and experiment 1010

This archaeology does **not** require waiting for V3-EXQ-1010.

1010 changes which V3 branch becomes urgent:

### If an over-capacity decoder succeeds

Then the frozen `z_world` contains a learnable action-relevant mapping that the current native consumer cannot express. The mutual-legibility/translation programme becomes immediately relevant to the V3 bottleneck.

The next question is not “install the giant decoder.” It is:

> what is the **minimum constrained transformation** that recovers the useful relation, and can development/replay make that transformation simpler?

### If the over-capacity decoder fails

Then the immediate V3 repair probably moves upstream to the encoder/objective because the required relation is not recoverably present in the frozen latent.

But the hippocampal translation-map programme remains relevant to later architecture: newly learned representations will still need to remain mutually legible across E1, E2, hippocampal memory, E3, and changing developmental ontologies.

Thus 1010 controls **priority**, not the validity of the archaeological synthesis.

---

# 19. Archaeological conclusion

The repository does **not** show that REE has always had a hidden theory of hippocampal translation maps.

It shows something more useful:

1. February architecture already made hippocampus a handoff/index/replay system and discovered that a live interface can fail because the **wrong representational object** crosses it.
2. March viability mapping made hippocampal geometry a **cross-system relational map** indexed by E2 action consequences and labelled by E3 outcome signals.
3. June developmental work independently introduced **over-connected → sparse structured** maturation.
4. September TCRT reframed competence around putting present information into the **form required by the current computation**.
5. Developmental ontology/replay introduced the problem of maintaining identity/reference while categories themselves change.
6. Mutual legibility made low-complexity cross-system translation explicit.
7. Receiver-conditioned translation, recurrent stability, shared reference frames, and temporal gates progressively turned a fixed bridge into a **state-, relation-, and phase-dependent interface**.
8. Independently, the 978→1002→1008→1010 experimental sequence has forced the same distinction empirically.

The strongest synthesis that survives the archaeology is therefore:

> **REE may need not one universal representational language but mechanisms that preserve relational continuity among specialised representations. Hippocampal/episodic machinery is a serious candidate for contributing learned maps, indices, replay and reference-frame structure to that process, but it should not yet be promoted to a generic “translation engine.”**

That is the correct starting point for the next phase: a targeted biological and computational-neuroscience campaign asking **what hippocampal/entorhinal circuits actually map between, how those mappings are learned and remapped, which reference frames they preserve, how replay changes them, and whether any evidence supports genuine cross-system translation rather than ordinary retrieval or routing.**

---

## Routing from this archaeology

- **No new claim registration.**
- **No V3 build.**
- **No experiment queue mutation.**
- Preserve the current phrase **“hippocampal translation maps”** as a research label only.
- Next research stage: biological/computational literature campaign, with explicit negative-evidence pass.
- Formal-maths stage should operate on the unifying interface equation above and keep hippocampal implementation optional.
- When V3-EXQ-1010 lands, use its result to choose which part of the translation-complexity ladder becomes immediately relevant to V3, without rewriting this archaeology retrospectively.
