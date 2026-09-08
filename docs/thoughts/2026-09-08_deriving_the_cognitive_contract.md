# Thought: Deriving the Cognitive Contract

**Status:** active foundational thought / research programme  
**Domain:** cognifold, inter-engine communication, representation, compression, language, developmental architecture  
**Primary question:** What information must survive translation between specialised cognitive systems for them to constitute one unified mind?

---

## 1. Core idea

REE contains multiple specialised cognitive engines whose internal latent representations need not, and probably should not, be identical.

E1, E2, E3 and later specialised systems may differ in:

- representational geometry;
- temporal scale;
- compression level;
- learning dynamics;
- uncertainty representation;
- computational purpose;
- developmental history.

Nevertheless, if these systems form a single mind rather than a collection of cooperating agents, their representations must remain mutually intelligible in some deeper sense.

The central proposal of this thought is that **unified cognition requires an invariant-preserving cognitive contract between representational systems**.

The contract is not necessarily a common latent space.

It may instead consist of a small set of relations or properties that must remain recoverable whenever information is compressed, decompressed or translated from one cognitive representation into another.

The cognifold can therefore be understood not as a requirement that every subsystem share the same representation, but as the larger structure within which heterogeneous representations remain parts of a single intelligible cognitive world.

This provides an important distinction between a **cognifold** and a **braidling**.

A braidling may consist of several substantially independent cognitive systems communicating and coordinating with one another.

A cognifold is a single cognitive entity whose specialised systems may possess different internal representations but whose representations remain embedded in one mutually interpretable structure.

The question is therefore not:

> How do we force every engine to use the same latent space?

It is:

> What must remain invariant across translation for multiple latent spaces to constitute one mind?

---

## 2. Why this matters for REE

Without an explicit solution to this problem, REE risks one of two architectural failures.

### 2.1 Representation collapse

All engines could be required to operate through a single canonical representation.

This appears simple but may remove precisely the specialisation that makes multiple engines useful.

Different cognitive processes may benefit from radically different representations.

A fast forward predictor, a deep persistent generative model, episodic memory and trajectory-selection machinery need not organise information in the same way.

Forcing them into one latent geometry may:

- constrain learning;
- create unnecessary bottlenecks;
- make representations brittle;
- prevent developmental specialisation;
- confuse interface convenience with cognitive architecture.

### 2.2 Cognitive fragmentation

At the other extreme, engines could develop representations that become mutually uninterpretable.

The components might continue to exchange tensors or messages while progressively losing shared meaning.

This would be a particularly dangerous failure because the system could remain computationally active while ceasing to behave as a coherent single cognitive entity.

A mature REE therefore needs neither complete representational identity nor unrestricted representational independence.

It needs **structured translatability**.

---

## 3. The cognitive contract hypothesis

The working hypothesis is:

> There exists a relatively small set of cognitive relations whose preservation is sufficient to maintain meaningful translation between specialised representational systems.

These relations are referred to provisionally as **cognitive contract invariants**.

The term *invariant* should not imply that the representation itself is fixed.

An invariant may be implemented differently in different engines.

For example, the representation of temporal relation could be:

- an explicit scalar;
- a trajectory position;
- a recurrent-state relation;
- a geometric direction;
- an ordering relation between events;
- or something not yet anticipated.

What matters is that the relevant relation can be reconstructed when needed.

The invariant is therefore semantic or relational rather than necessarily representational.

---

## 4. The contract is not the schema

This distinction is essential.

Schemas encode contingent knowledge about a particular body, environment, history or learned conceptual organisation.

Schemas should be expected to change.

A human-like organism may develop schemas concerning:

- hands;
- faces;
- social roles;
- rooms;
- food;
- tools;
- language;
- interpersonal relationships.

A cognitively very different organism may possess none of these.

The cognitive contract should therefore sit at a different architectural level.

A useful provisional relationship is:

```text
Cognitive contract
        ↓
Representation / translation machinery
        ↓
Schemas
        ↓
Particular concepts, memories and environmental models
```

Schema changes may alter what the organism knows.

Contract failure alters whether its cognitive systems can continue to understand one another.

This distinction may become particularly important during sleep or other periods of representational reorganisation.

If schemas are substantially rewritten, the contract may be one of the mechanisms that permits old and new representations to remain parts of the same cognitive history.

---

## 5. The contract is also not the REE_assembly claims invariant system

REE_assembly already contains machinery concerned with claims, evidence, provenance, dependency and truth maintenance.

Those invariants answer questions such as:

- What claim is this?
- Where did it come from?
- What evidence supports it?
- What other claims depend upon it?
- Has its status changed?

These are **epistemic and governance invariants for the development machinery**.

The cognitive contract proposed here concerns something different:

> What must be preserved when one cognitive representation is interpreted by another?

The two systems may nevertheless converge on surprisingly similar structures.

That possibility should be treated as an empirical clue rather than assumed equivalence.

If independently derived governance, linguistic, developmental and cognitive systems repeatedly require analogous primitives, that convergence may reveal something deeper.

However, deriving the cognitive contract from the existing claims machinery would be circular.

The correct approach is therefore to derive candidate contract features independently and later compare the resulting structures.

---

## 6. Candidate invariants are hypotheses, not architecture

The present discussion has already generated a provisional candidate set.

Possible contract dimensions include:

- identity;
- persistence;
- reference;
- agency;
- causality;
- temporal relation;
- process state or aspect;
- spatial relation;
- quantity;
- actuality / reality status;
- observation versus memory versus imagination;
- counterfactual status;
- uncertainty;
- confidence or precision;
- negation;
- value;
- harm / benefit significance;
- goal relevance;
- commitment;
- controllability;
- salience;
- social attribution.

This list should **not** be implemented as a specification.

It is a research inventory.

Several possibilities remain open:

1. some candidates may not be fundamental;
2. several may reduce to a more primitive relation;
3. some may be consequences of human embodiment;
4. some may be linguistic conveniences rather than cognitive necessities;
5. important invariants may be entirely absent from the present list.

The goal is therefore to **derive and prune**, not to accumulate.

---

## 7. Language as an inverse probe

A particularly promising route emerged from considering grammar.

If cognitive systems must preserve particular distinctions internally, communication between minds may repeatedly expose those distinctions.

Language could therefore provide an indirect record of what human cognition repeatedly finds important enough to communicate.

This reverses the usual direction of argument.

The proposal is not:

> Human grammar tells us how REE should think.

Instead:

> Recurrently grammaticalised distinctions may provide evidence about distinctions that human cognitive systems repeatedly need to preserve and communicate.

Cross-linguistic recurrence of structures involving such things as:

- agency;
- reference;
- number;
- tense;
- aspect;
- modality;
- evidentiality;
- negation;
- causation;
- conditionals;
- possession;
- social reference;

may therefore be mined as evidence for candidate invariants.

Language becomes an **inverse probe into cognitive interface requirements**.

This is particularly interesting because grammar may represent a highly compressed communication protocol.

If languages repeatedly develop efficient ways of transmitting certain relations, those relations may overlap with the information that internal cognitive systems must also preserve during translation.

This extends, rather than replaces, the earlier REE language thought in `docs/thoughts/2026-02-09_language.md`, which framed language as a compression and coordination layer built on preverbal cognitive structure.

---

## 8. But human language must not define the contract

This route carries a major contamination risk.

Human languages are produced by organisms that share:

- similar bodies;
- similar sensory systems;
- similar developmental trajectories;
- similar reproductive and social constraints;
- a largely shared terrestrial environment;
- common phylogenetic history.

Cross-linguistic universality therefore does not imply cognitive universality.

A feature could be universal among humans while remaining irrelevant to a radically different mind.

The evidence programme should consequently distinguish at least three classes.

### A. Candidate architectural invariants

Properties plausibly required by many kinds of unified cognitive systems.

### B. Embodied or ecological invariants

Properties highly recurrent because minds share particular bodies, environments or action problems.

### C. Human linguistic conventions

Structures that arise from communication efficiency, historical contingency or cultural evolution without being fundamental to cognition.

The distinction cannot simply be asserted.

It must be investigated.

---

## 9. The research method: triangulation rather than linguistic imitation

The cognitive contract should be derived through **independent convergence across evidence domains**.

For every proposed invariant, the research programme should ask whether comparable structure appears in:

### Cross-linguistic typology

Does the distinction recur across unrelated languages?

Is it obligatorily encoded?

Does it repeatedly emerge through unrelated grammatical systems?

### Developmental cognition

Does the distinction appear before language?

At what developmental stage?

Does it emerge before explicit symbolic instruction?

### Neuroscience

Are there distributed representations that preserve the distinction across different tasks or modalities?

Are there known mechanisms for translating between representational systems while retaining it?

### Comparative cognition

Is the distinction identifiable in non-human animals?

Does it appear in species with substantially different sensory or behavioural ecologies?

### Artificial systems

Do independently trained agents discover analogous variables when solving sufficiently general problems?

Does removing the distinction produce characteristic failures?

### REE itself

Does a proposed invariant become necessary when E1, E2, E3 or other systems exchange representations?

Can an engine learn without it?

Can it translate around it?

What fails if the invariant is deliberately destroyed?

The strength of a candidate therefore comes from **consilience**, not from any single literature.

---

## 10. Contract failure as an experimental tool

The strongest test of an invariant may not be whether it appears in successful cognition but what happens when it is absent.

Each candidate should therefore have a corresponding **contract lesion assay**.

Examples might include:

### Identity lesion

Two representations cannot reliably determine whether they concern the same entity.

Predicted failures:

- broken persistence;
- duplicated selves or objects;
- incoherent credit assignment;
- unstable memory integration.

### Temporal lesion

Translation preserves content but not temporal relation.

Predicted failures:

- cause/effect inversion;
- inability to distinguish present state from anticipated state;
- confused planning;
- memory/prediction contamination.

### Reality-status lesion

Observed, remembered, simulated and counterfactual states become difficult to distinguish.

Predicted failures:

- confabulation-like behaviour;
- false commitment to imagined states;
- impaired counterfactual learning;
- psychosis-like representational errors.

### Agency lesion

Events remain representable but controllability and actor relation are lost.

Predicted failures:

- poor action learning;
- external/internal attribution errors;
- impaired responsibility assignment;
- failure of intentional planning.

### Confidence lesion

Content translates but uncertainty does not.

Predicted failures:

- overcommitment;
- underreaction to reliable predictions;
- inappropriate belief updating;
- failure of precision-sensitive integration.

The lesion approach converts an abstract philosophical proposal into an experimentally tractable programme.

---

## 11. Compression and decompression

Translation between cognitive engines is unlikely to mean exhaustive copying of internal state.

A useful interface must compress.

The important question is therefore:

> What information cannot be discarded without damaging unity?

This gives an information-theoretic interpretation of the cognitive contract.

Let an internal state in engine A be:

`x_A`

A translation into engine B might involve:

`x_A → C_A(x_A) → T_AB → D_B → x'_B`

where:

- `C_A` performs compression;
- `T_AB` performs translation;
- `D_B` reconstructs a representation usable by B.

The contract does not require:

`x'_B = x_A`

Indeed, equality may be meaningless because the spaces differ.

Instead, for some set of invariant relations `I`:

`I(x_A) ≈ I(x'_B)`

The central mathematical problem is therefore not representation matching.

It is **invariant preservation under lossy translation**.

This deserves a separate mathematical treatment, but the conceptual consequence is already important:

> Good cognitive compression is compression that discards representation-specific detail while preserving the relations required for unified cognition.

---

## 12. A possible explanation for grammar

This framework also creates a testable hypothesis concerning language.

If certain relations must already be preserved during internal cognitive translation, external communication may inherit the same requirements.

A possible developmental chain is therefore:

```text
Cognitive invariants
        ↓
Internal representational contracts
        ↓
Repeated compression/translation pressures
        ↓
Proto-grammatical relational structure
        ↓
External language
```

On this account, grammar does not need to begin as a language-specific faculty.

Some grammatical structure could emerge because communication must preserve relations already important for cognition.

This is not yet a theory of grammar.

It is a research hypothesis.

Importantly, it can be investigated in both directions:

- derive candidate invariants from cognition and ask whether language expresses them;
- mine recurrent linguistic distinctions and ask whether they correspond to independently supported cognitive invariants.

Agreement between the two directions would be substantially more informative than either alone.

---

## 13. Developmental implications for REE

REE should probably not begin with a fully specified mature cognitive contract.

Biological cognition develops.

Some interface requirements may initially be coarse and later differentiate.

For example, a primitive organism might initially represent something resembling:

```text
self-caused / not-self-caused
```

before developing richer structures involving:

```text
agency
intention
control
responsibility
social attribution
```

Similarly:

```text
here / not-here
```

might precede sophisticated spatial relations.

And:

```text
now / not-now
```

might precede richer temporal ordering.

This suggests that REE should distinguish:

- **contract primitives**;
- **derived contract structure**;
- **learned schemas**.

Development itself may reveal which distinctions are genuinely foundational.

A feature that must exist before substantial learning can occur is a stronger candidate for architectural status than one that appears only after extensive experience.

---

## 14. Flexibility is a design requirement

The cognitive contract must not become another rigid ontology.

A successful design should allow:

- different engines to encode invariants differently;
- new representational systems to be added;
- schemas to reorganise;
- the meaning of higher-level variables to develop;
- representations to become more compressed with experience;
- entirely new contract dimensions to emerge if necessary.

The contract should therefore specify **recoverable relationships**, not fixed data structures.

Where possible, REE should test whether interfaces can learn transformations while being constrained only by invariant-preservation requirements.

This would allow representational specialisation without fragmentation.

---

## 15. Relationship to the cognifold

This thought suggests a sharper definition of the cognifold.

The cognifold is not simply a latent space.

It is the larger mutually interpretable representational structure of a unified cognitive system.

Its unity may arise from overlapping transformations among many latent spaces rather than from the existence of one universal representation.

A cognifold may therefore contain:

- local manifolds;
- specialised latent spaces;
- shared subspaces;
- learned translators;
- compression/decompression pathways;
- recurrent loops;
- invariant relations spanning those systems.

The relevant biological analogy may consequently be distributed rather than anatomical.

Association cortex, hippocampal indexing, thalamic routing, recurrent corticocortical communication, multimodal convergence and structures such as the claustrum may each provide partial inspiration.

No single biological structure needs to correspond to the cognifold.

The important biological lesson may instead be that a brain maintains unity while permitting extensive representational heterogeneity.

---

## 16. Relationship to braidlings

The same framework may eventually provide a principled distinction between a cognifold and a braidling.

Consider two systems that communicate extremely effectively.

If each can cease communication while remaining an independently coherent cognitive entity, their communication may constitute coordination between minds.

If, by contrast, representational systems depend on invariant-preserving transformations throughout normal cognition and jointly maintain one persistent self/world structure, they may instead constitute parts of one cognifold.

This distinction is currently conceptual rather than formal, but the cognitive contract may eventually help operationalise it.

A future question is therefore:

> At what point does translation between cognitive systems constitute internal cognition rather than communication between agents?

---

## 17. Scope and non-goals

This thought does **not** claim that:

- the candidate invariant set is already known;
- human grammar is a universal grammar of cognition;
- every REE engine should share the same latent geometry;
- the claustrum or any other single brain structure implements the cognifold;
- cognitive unity can already be reduced to a complete mathematical criterion;
- the existing claims matrix provides the cognitive contract.

It defines a discovery programme for testing those possibilities while minimising architectural contamination.

---

## 18. Pollution risks

Because this work could influence fundamental REE architecture, it needs unusually strong safeguards against premature commitment.

### Do not implement the candidate list directly

The present candidates are hypotheses.

### Do not infer universality from human language

Human typology is one evidence source.

### Do not retrofit the evidence to REE's existing architecture

Independent derivation is essential.

### Do not assume one universal latent representation

Translation may be sufficient.

### Do not confuse repeated usefulness with fundamentality

A variable can be useful in many tasks without being required for unified cognition.

### Preserve negative findings

If an apparently fundamental invariant proves unnecessary, that result is scientifically valuable.

---

## 19. Proposed evidence ledger

Each candidate invariant should eventually receive an evidence record containing:

| Field | Question |
|---|---|
| Candidate | What relation is proposed? |
| Definition | What precisely must be preserved? |
| Linguistic evidence | Does it recur cross-linguistically? |
| Developmental evidence | Does it appear before language or explicit teaching? |
| Neural evidence | Is there evidence for modality- or subsystem-independent representation? |
| Comparative evidence | Does it appear outside humans? |
| Artificial-agent evidence | Does it emerge independently in learned systems? |
| REE evidence | Is it already required or spontaneously represented? |
| Lesion prediction | What should fail if it is removed? |
| Alternative explanation | Could embodiment, culture or task structure explain it? |
| Classification | Architectural / embodied / cultural / uncertain |
| Confidence | How strong is the present case? |

The objective is not to maximise the number of invariants.

The objective is to find the **smallest defensible set**.

---

## 20. Engineering output

The research programme should eventually produce a **Cognitive Contract Specification**.

That specification might define:

1. required invariant relations;
2. optional or developmental relations;
3. how an engine declares what it can encode;
4. how translators are trained or discovered;
5. how invariant preservation is tested;
6. tolerated reconstruction error;
7. contract lesion assays;
8. monitoring for representational drift;
9. behaviour when translation confidence is low;
10. rules for adding or retiring contract dimensions.

The specification should remain independent of any particular latent geometry.

---

## 21. Immediate work programme

This thought suggests four linked pieces of work.

### Thought 1 — Deriving the Cognitive Contract

This document.

Defines the research question and methodology.

### Thought 2 — Candidate Cognitive Invariants

Systematic evidence synthesis across linguistics, development, neuroscience, comparative cognition and artificial systems.

Produces a ranked and pruned candidate set.

### Thought 3 — Compression, Decompression and the Cognifold

Examines how heterogeneous representations can remain mutually interpretable while preserving specialisation.

Includes biological analogues and mechanisms of representational translation.

### Thought 4 — Mathematics of Invariant-Preserving Cognitive Translation

Formalises translation between latent spaces, information loss, sufficient representations, recoverability and possible measures of cognifold coherence.

These documents should inform one another but should not be collapsed prematurely.

---

## 22. Falsifiable claims

The programme should generate experimentally vulnerable claims.

Among them:

1. Removing some candidate relations from inter-engine translation will produce reproducible cognitive fragmentation or characteristic behavioural deficits.
2. Truly architectural invariants should recur across more than one independent evidence domain.
3. Human-language universals that lack developmental, comparative or computational support are more likely to reflect embodiment or cultural history than fundamental cognition.
4. Engines should be able to maintain different latent geometries while preserving coherent behaviour if the appropriate invariants remain recoverable.
5. Enforcing complete latent alignment should not be necessary for cognifold unity.
6. Schema reorganisation should be substantially less disruptive when cognitive-contract relations remain stable.
7. Some grammar-like structure may emerge spontaneously if communicating systems are required to transmit invariant-rich cognitive states efficiently.

These claims provide routes by which the proposal can fail.

That is important.

---

## 23. Central principle

The guiding principle is:

> **Unity does not require representational sameness. It requires preservation of the relations that allow representations to remain about the same cognitive world.**

The cognifold may therefore be less like a single language spoken everywhere in the mind and more like a continuously maintained web of mutually translatable representations.

Discovering the minimum structure required to sustain that web may reveal something important both about REE and about cognition more generally.

The goal is not to impose a grammar of thought.

It is to discover the **minimum invariant-preserving contract for unified cognition**.
