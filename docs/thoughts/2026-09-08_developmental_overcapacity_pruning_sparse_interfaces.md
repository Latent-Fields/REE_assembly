# Developmental Overcapacity, Pruning, and the Discovery of Sparse Interfaces

**Date:** 2026-09-08  
**Status:** thought / organising hypothesis / experimental programme  
**Scope:** developmental architecture; representation, interface learning, replay and pruning  

**Related thoughts:**
- `2026-09-04_developmental_ontology_and_replay.md`
- `2026-09-07_mutual_legibility_communication_subspaces.md`
- `2026-09-03_temporary_coordinated_representational_transformations.md`
- `2026-08-31_replay_driven_rebucketing_decision_relevant_representation.md`
- `2026-09-04_z_world_representation_contract.md`

## Core thought

A mature cognitive architecture may not be learnable most effectively when constrained to its mature capacity from the beginning.

Development may require a period of **transient overcapacity**: more connections, more candidate mappings, more accessible transformations, or more permissive interfaces than the mature system ultimately needs. Experience, action consequences, replay and internal regulation can then determine which relationships deserve to survive. The mature system can become smaller, sparser and more efficient **because development has discovered a useful organisation**, not simply because redundant machinery was removed.

The working proposition is:

> **Developmental overcapacity may function as a search and scaffolding regime from which sparse, structured, behaviourally useful representations and interfaces are selected. The final architecture may therefore depend on having passed through a richer developmental regime than it retains in maturity.**

This is stronger than the ordinary claim that large models are easier to train. It predicts that **developmental history itself can matter even when final capacity is held constant**.

---

## 1. Why this thought emerged

Recent REE work has repeatedly separated several questions that were previously easy to collapse:

- is information encoded?
- is it decodable by an external probe?
- is it natively accessible to the relevant consumer?
- can it be made accessible by a low-complexity bridge?
- is it causally used?
- does that use improve behaviour?

The mutual-legibility work formalised the possibility that specialised systems may retain distinct high-dimensional representations while communicating through narrower, consumer-specific subspaces. It also proposed a translation-complexity ladder, with very high-capacity decoders treated only as upper bounds.

That immediately creates a developmental question:

> If the mature system ought to require only a small, efficient interface, does that imply the small interface must also be sufficient during early development?

Not necessarily.

An early system may benefit from having many possible ways for one representation to influence another. Repeated experience can identify which mappings consistently preserve prediction, regulation, action and transfer. Those mappings can then be stabilised, compressed or distilled while others disappear.

The important possibility is therefore:

```text
early abundant accessibility
        ↓
experience-dependent selection
        ↓
structured specialisation
        ↓
pruned, efficient mature interfaces
```

Overcapacity in this picture is not the intended endpoint. It is part of the mechanism by which the endpoint becomes discoverable.

---

## 2. Biological analogue: hippocampal CA3 development

A particularly relevant biological analogue comes from Vargas-Barroso et al. (Nature Communications, 2026), who mapped recurrent CA3-to-CA3 connectivity across postnatal development in mouse hippocampus.

They report a developmental transformation from a **local, dense and relatively random recurrent network** into a **distributed, sparse and structured network**. At the same time, individual recurrent synapses become weaker: early in development, individual synaptic events can sometimes exert very strong influence, whereas the mature circuit increasingly requires convergent input. Their modelling suggests that these developmental changes improve particular aspects of associative-memory storage and retrieval.

Reference:

Vargas-Barroso V, Watson JF, Navas-Olive A, Schlögl A, Jonas P. *Developmental emergence of sparse and structured synaptic connectivity in the hippocampal CA3 memory circuit.* Nature Communications. 2026;17:5540. https://doi.org/10.1038/s41467-026-71914-x

A subsequent Trends in Neurosciences commentary characterises this as development moving through distinct computational regimes that together improve memory capacity:

Ulmer T, Donato F. *Development sculpts dense neural circuits to enhance memory capacity.* Trends in Neurosciences. 2026. https://doi.org/10.1016/j.tins.2026.07.008

The REE analogy must remain cautious. CA3 development does **not** establish that artificial cognitive systems require developmental overcapacity, nor that synaptic pruning maps directly onto decoder pruning. What it demonstrates is the plausibility of a more general principle:

> a useful mature sparse circuit may emerge through a developmentally distinct dense regime rather than being instantiated in mature form from the outset.

The biological result therefore motivates an experiment. It does not settle one.

---

## 3. Relationship to developmental ontology

`Developmental Ontology and Replay` already proposes that development may alter the representational scheme itself: categories can split, merge, be reweighted and acquire new causal meaning. Its proposed developmental trajectory ends with representations becoming **more compressed yet more behaviourally informative**.

The present thought supplies a possible mechanism for that trajectory.

If an immature system has many overlapping or weakly specialised representational and interface routes, it can preserve alternatives before their significance is known. Consequences can later determine which distinctions deserve stable representation and which mappings deserve privileged access to downstream systems.

Thus:

```text
immature representation:
many distinctions × many candidate routes × weak specialisation

mature representation:
fewer useful distinctions × structured routes × strong specialisation
```

Compression is therefore not merely deletion. It can be the end-state of **discovery**.

This also predicts that premature representational compression may be developmentally harmful even when the same compressed representation would work well after maturation.

---

## 4. Relationship to mutual legibility

The mutual-legibility thought defines a rough quantity:

```text
L(A -> B) = minimum bridge complexity required to preserve
            a predeclared functional criterion from A to B
```

Lower `L` means that two systems are more mutually legible.

A developmental-overcapacity hypothesis suggests a characteristic trajectory:

```text
L_early  >>  L_mature
```

while competence simultaneously rises.

That would mean that the early system may initially require a large or permissive mapping between two subsystems, but through development their representations and interface geometry become organised such that a much simpler bridge later suffices.

This gives a useful operational definition of developmental interface maturation:

> **maturation is not merely increasing performance; it is increasing performance while reducing the minimum interface complexity required to preserve the relevant function.**

The important counterfactual is equally clear: if bridge complexity remains high indefinitely, then the system may have learned to depend on an overcapacity crutch rather than developing mutual legibility.

---

## 5. Relationship to Temporary Coordinated Representational Transformations

Temporary Coordinated Representational Transformations (TCRT) proposes that the useful form of information may depend on current context, directive structures, predicted consequences and candidate action. A mature cognitive system may therefore possess several reusable ways of bringing the same underlying information into decision-relevant form.

Developmental overcapacity adds a history to this machinery.

Early in development there may be a **larger space of possible transformations** than the mature system eventually uses. Experience determines which transformations recur, which support successful prediction and regulation, which generalise, and which merely fit local episodes.

Those successful transformations can become increasingly low-complexity, routinised or structural.

A possible progression is:

```text
many weak candidate transformations
        ↓
context/consequence-sensitive recruitment
        ↓
repeatedly useful transformations stabilise
        ↓
redundant routes weaken or disappear
        ↓
small mature repertoire of efficient transformations
```

The resulting mature architecture may look elegant and economical precisely because development did not begin that way.

---

## 6. The overcapacity decoder as assay versus architecture

A very large decoder used in a frozen-latent experiment should not automatically be interpreted as a proposed REE component.

Its immediate experimental role is different:

> **Does there exist any learnable mapping from the frozen representation to the required functional output?**

A high-capacity decoder can therefore serve as an upper-bound instrument.

Two broad outcomes matter.

### 6.1 High-capacity decoder succeeds

If a large decoder can recover useful action or prediction from a representation that a policy-sized decoder cannot use, then the representation contains sufficient structure for some downstream map, but the mapping may be too difficult for the current native consumer.

That result would motivate the developmental question:

> Can a large early consumer discover the mapping and later transfer, distil or prune it into a much smaller mature interface?

The large decoder would become a **developmental scaffold or teacher candidate**, not a mature architectural commitment.

### 6.2 High-capacity decoder fails

If even an overcapacity decoder cannot recover the required function despite adequate fitting controls, then simply enlarging the consumer is unlikely to solve the problem.

Developmental overcapacity may instead need to occur upstream: in the encoder, recurrent world representation, hippocampal/replay system, or the interaction among them. The system may need more representational degrees of freedom while learning which distinctions should become stable.

Thus failure of an overcapacity decoder would not falsify developmental overcapacity in general. It would localise where that developmental freedom may need to exist.

---

## 7. The critical experiment: same mature capacity, different developmental history

The cleanest test should compare developmental histories that converge on the **same final capacity**.

### Arm A — small throughout

Train the mature-sized interface or subsystem from the start.

This is the conventional baseline.

### Arm B — large then prune/distil

Begin with substantial excess capacity. During development, progressively prune, compress, distil or otherwise restrict the system until its final parameter/interface capacity matches Arm A.

### Arm C — large throughout

Retain the large system permanently.

This measures what raw capacity itself buys and prevents mistaking a simple capacity advantage for a developmental effect.

### Arm D — final pruned architecture from birth

Take the final architecture, sparsity mask, interface structure or selected routes produced by Arm B. Reinitialise it and train it from the beginning under the same developmental curriculum.

This arm is essential.

If Arm B outperforms Arm A, the effect could merely mean that pruning discovered a better small architecture. But if Arm B also outperforms Arm D despite B and D having the same final architecture, then the stronger conclusion becomes available:

> **the developmental path through overcapacity contributed something that the final architecture alone could not reproduce.**

Schematically:

```text
final capacity(B) = final capacity(D)
architecture(B)   ≈ architecture(D)

but

competence(B) > competence(D)
```

would be evidence that **developmental history matters**.

---

## 8. What should determine pruning?

Naive magnitude pruning would be useful as a control but is unlikely to capture the full hypothesis.

REE has unusually rich candidate signals for deciding which relationships deserve retention:

- predictive contribution;
- reduction of persistent prediction error;
- harm/benefit relevance;
- controllability discrimination;
- counterfactual usefulness;
- action-selection contribution;
- replay recurrence;
- transfer across contexts;
- stability across developmental stages;
- utility to more than one downstream consumer;
- maintenance of uncertainty where premature collapse would be dangerous.

This suggests testing multiple pruning rules rather than assuming that small weights are equivalent to irrelevant relationships.

The biologically interesting version is not merely:

```text
keep strongest connection
```

but something closer to:

```text
keep relationships repeatedly shown to matter
under prediction, action, regulation and replay
```

The relevant quantity may therefore be **functional persistence**, not weight magnitude.

---

## 9. Replay and sleep may be particularly important at the transition

If development changes representational geometry while interfaces are being reduced, pruning poses a coordination problem.

A route can appear unnecessary only because its consumer has not yet adapted to a new representation. Conversely, an apparently useful route may merely preserve an obsolete coding convention.

Replay or sleep-like offline periods could provide a safer environment for:

1. testing which old episodes remain reconstructable;
2. comparing alternate candidate mappings without immediate behavioural cost;
3. re-indexing memories after representational change;
4. stabilising newly useful communication subspaces;
5. weakening redundant routes;
6. checking that pruning has not destroyed important counterfactual or regulatory distinctions.

This predicts that pruning during unrestricted online learning may be less stable than pruning coupled to replay/consolidation.

A particularly strong result would be that replay allows **greater compression at equal or better transfer performance**.

---

## 10. Developmental critical periods and graceful freezing

If transient overcapacity is useful, there may also be an optimal time to remove it.

Pruning too early could freeze accidental distinctions before enough consequences have been observed. Pruning too late could allow the organism to become dependent on expensive idiosyncratic pathways that are difficult to simplify.

This creates a REE analogue of a developmental critical-period problem:

```text
too early  -> premature commitment
well timed -> structured compression
 too late  -> entrenched overfitting / interface dependence
```

The timing variable should therefore itself be experimentally manipulated.

A mature system may also require **graceful freezing** rather than complete rigidity: most structure stabilises, while limited plasticity remains available for genuinely novel environments or new developmental stages.

---

## 11. Falsifiable predictions

The developmental-overcapacity hypothesis predicts at least the following.

1. **Large-to-small developmental schedules can outperform small-from-start schedules at matched final capacity.**
2. **The advantage should persist beyond the training distribution**, otherwise overcapacity may merely improve memorisation.
3. **A reinitialised copy of the final pruned architecture may perform worse than the system that developed into it.**
4. **Minimum bridge complexity between specialised subsystems should fall over development while competence rises.**
5. **Pruning guided by behavioural/predictive relevance should outperform indiscriminate magnitude pruning if functional selection matters.**
6. **Replay-assisted pruning should preserve more transfer and causal structure than equally aggressive online-only pruning if offline reorganisation is important.**
7. **Useful mature representations may become lower-dimensional or sparser without losing, and potentially while increasing, downstream accessibility.**
8. **Premature compression should selectively impair distinctions whose relevance is only revealed later in the developmental curriculum.**

Each of these can fail independently. The thought should not be protected by treating every result as compatible with it.

---

## 12. Red team

Several simpler explanations must be actively excluded.

### Ordinary optimisation advantage

Overparameterised networks are often easier to optimise. A large-to-small advantage may therefore reflect optimisation mechanics rather than a developmental principle.

Controls should match training compute where possible and distinguish transient optimisation assistance from learned developmental structure.

### Architecture search only

Pruning may simply discover a good sparse architecture. Arm D is designed specifically to test this rival.

### Knowledge distillation artefact

If the large system acts as a teacher, the benefit may reduce to ordinary distillation. That would still be useful engineering but would weaken the stronger claim that organismal developmental history matters.

### Irreversible early mistakes

Overcapacity could increase the number of spurious routes and make pathological attractors more likely. Development may benefit from strong early constraints rather than abundance.

### Mature capacity may genuinely be insufficient

If the large-throughout arm is strong while every pruned arm collapses, the correct conclusion may simply be that the proposed mature bottleneck is too narrow.

### Biological analogy may be superficial

CA3 synaptic development concerns a biological recurrent memory circuit with developmental processes that have no necessary analogue in artificial neural networks. The analogy is hypothesis-generating only.

---

## 13. Implications for REE developmental design

The main architectural warning is:

> **Do not infer from the desired mature architecture that development should begin with the same bottlenecks.**

This matters for `z_world`, E1/E2 interfaces, hippocampal/replay pathways, goal/directive influence and later E3 selection.

A mature REE might ultimately use:

- compact world representations;
- sparse communication subspaces;
- low-complexity inter-module bridges;
- small repertoires of recurring transformations;
- selective and stable memory indices.

But imposing all of those restrictions at developmental time zero could prevent the organism from discovering which distinctions and interfaces deserve to survive.

The developmental programme should therefore distinguish:

```text
mature architectural constraints
```

from

```text
developmental search/scaffolding capacity
```

They need not be identical.

---

## 14. Minimal implementation programme

Before adding permanent new machinery, the following sequence would provide discriminating evidence.

### Stage 1 — measure developmental bridge complexity

At existing developmental checkpoints, freeze sender and receiver representations and measure the minimum bridge class required to recover a fixed held-out functional criterion.

Track whether `L(A -> B)` naturally falls with development.

### Stage 2 — controlled overcapacity schedule

Choose one currently limiting interface and train matched cohorts using:

- mature-size from start;
- overcapacity -> progressive reduction;
- overcapacity retained;
- final sparse architecture reinitialised from start.

Keep the environmental curriculum identical.

### Stage 3 — transfer and counterfactual tests

Evaluate not only training competence but:

- held-out layouts;
- changed action semantics where appropriate;
- delayed consequence distinctions;
- cue reassignment;
- replay-dependent recoding;
- consumer-specific accessibility.

### Stage 4 — replay/pruning interaction

Repeat the reduction schedule with and without offline replay while matching update count.

### Stage 5 — inspect what survived

Ask whether retained pathways correspond to:

- stable regulatory distinctions;
- task-relevant communication subspaces;
- repeated transformation motifs;
- predictive or counterfactual usefulness;
- or merely large parameter magnitude.

Only after these assays should developmental overcapacity become an architectural commitment.

---

## 15. Strongest version of the hypothesis

The strongest claim generated by this thought is not:

> bigger networks are useful early.

It is:

> **Some mature cognitive organisations may be historically inaccessible from their own final architecture. They may need to be reached through a transiently richer developmental state that allows relationships to be explored before experience selects which ones should become sparse, stable and mutually legible.**

That claim is experimentally dangerous in the useful sense: it can be disproved by showing that matched mature architectures trained from birth perform just as well as systems that develop into them.

If it survives, however, it would change how REE should think about developmental efficiency. The goal would no longer be to make the infant architecture look like a small version of the adult architecture.

The goal would be to give development enough room to **discover the adult architecture**.
