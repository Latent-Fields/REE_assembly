# Thought: Candidate Cognitive Invariants

**Date:** 2026-09-08  
**Status:** active evidence synthesis / red-team draft — **not digested**  
**Parent thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`  
**Related architecture:** `docs/architecture/cognitive_contract.md`  
**Canonical candidate ledger:** `evidence/planning/cognitive_contract_invariant_ledger.v1.json`  
**Ledger schema:** `evidence/planning/cognitive_contract_ledger_schema.v1.json`  
**Related language thought:** `docs/thoughts/2026-02-09_language.md`

> **Red-team revision note.** This revision deliberately tries to make the candidate set smaller, harder to satisfy, and less vulnerable to circularity. It also corrects an important bookkeeping error in the first draft: several working decomposition hypotheses had accidentally been assigned `CCI-*` identifiers already belonging to different records in the canonical ledger. In this document, `CCI-*` identifiers now refer **only** to canonical ledger records. New decomposition terms remain unnumbered hypotheses unless and until governance explicitly adds them to the ledger.
>
> The previous draft also cited three planning artefacts — an evidence pull, a narrowing preregistration, and a Stage-0 V3 substrate audit — that are not present on the repository default branch at this revision. They are therefore treated here as **planned artefacts/checks, not completed evidence**, until they are materialised and governed.

---

## 1. Why this thought exists

The parent thought, **Deriving the Cognitive Contract**, established a methodological claim: heterogeneous cognitive systems do not necessarily need identical latent geometries in order to belong to one coherent cognitive system. What they may need instead is reliable preservation of certain relations across representational handoffs.

That left the dangerous question unresolved:

> **Which relations?**

It would be easy to inspect human language, introspection, the present REE architecture, or familiar philosophical categories and write a plausible list. That would also be an excellent way to build our assumptions into the organism and later rediscover them as apparent necessities.

This thought therefore has a deliberately destructive purpose. It is not a catalogue of concepts that seem important. It is an attempt to **destroy, merge, demote, reclassify, or localise candidate invariants until the smallest empirically defensible set of cross-representational obligations remains**.

The working proposition is:

> A cognitive invariant is not a universal symbol, concept, feature, or shared latent coordinate. It is a relation whose recoverability across some representational transformation is required for heterogeneous cognitive processes to continue referring coherently to the same world, history, alternatives, and possible actions.

Nothing in the present candidate inventory is entitled to architectural status merely because it appears here.

---

## 2. The first red-team correction: there may be no single flat contract

The phrase **the cognitive contract** risks suggesting a universal packet header that every subsystem must transmit at every handoff. That is probably too strong.

A more defensible formulation is boundary-specific.

For a handoff from subsystem `A` to subsystem `B`, define a set of relations that `B` must be able to recover:

```text
I_AB = relations required by B that B cannot cheaply and reliably reconstruct locally
```

Different interfaces may therefore preserve different things. A sensory-to-world-model handoff, a hippocampal replay handoff, an E1-to-E2 predictive handoff, and a control-plane handoff need not carry the same relational payload.

The eventual cognitive contract may be better represented as a family of typed obligations:

```text
C = { A -> B : I_AB, tolerated distortion, receiver capability, fallback behaviour }
```

A **deep shared core**, if one exists, should emerge as the relations repeatedly required across many heterogeneous interfaces — not be assumed beforehand.

This matters immediately for candidates such as value, salience, confidence and commitment. They may be crucial at particular boundaries without being universal invariants of every internal representation.

---

## 3. The second red-team correction: counting primitives is not minimality

The first draft implicitly treated a shorter vocabulary as progress. That is useful but dangerously incomplete.

Any sufficiently rich cognitive state can be redescribed as one giant relation. Likewise, an arbitrarily complicated decoder can reconstruct many distinctions from a single continuous scalar. Declaring that everything has been reduced to “one typed graph” or “one latent” would therefore be formally compact and scientifically empty.

A reduction only counts if it reduces **total transferable complexity** without smuggling the lost distinctions into:

- the definition of the remaining relation,
- a more powerful decoder,
- hidden context tags,
- unconstrained numerical precision,
- recurrent hidden state,
- task-specific side channels,
- or expensive reconstruction machinery.

The relevant notion of minimality is therefore closer to **minimal sufficient transferable information under constrained encoders and receivers**, not “fewest English nouns”.

A future mathematical treatment should make this explicit with a rate/description-length or rate-distortion objective. Informally:

```text
contract cost
    ~= information rate
     + encoder/decoder complexity
     + context/side-channel complexity
     + reconstruction distortion
     + computational/latency cost
     + robustness cost
```

A candidate has genuinely been reduced only if the replacement lowers this total cost while preserving downstream function and robustness.

This is an anti-cheating rule for the entire programme.

---

## 4. Canonical ledger candidates: frozen names and identifiers

The current machine-readable ledger is the canonical bookkeeping source. The fourteen seeded candidates are:

| ID | Canonical candidate |
|---|---|
| `CCI-001` | identity continuity |
| `CCI-002` | temporal relation |
| `CCI-003` | reality status |
| `CCI-004` | agency |
| `CCI-005` | confidence / precision |
| `CCI-006` | equivalence / similarity |
| `CCI-007` | relational topology |
| `CCI-008` | magnitude / order |
| `CCI-009` | value / valence |
| `CCI-010` | goal relation |
| `CCI-011` | negation / absence |
| `CCI-012` | alternative branch status |
| `CCI-013` | commitment status |
| `CCI-014` | priority / relevance |

These are **candidates**, not primitives.

Several useful ideas below — source, provenance, ownership, generative lineage, intervention/control, viability and correspondence — are **working decomposition hypotheses**. They do not receive `CCI-*` identifiers merely because they may eventually explain one or more ledger candidates.

This distinction is important for REE_assembly ingestion: a thought may speculate freely, but it must not silently mutate the governed candidate ledger by identifier collision.

---

## 5. What would count as a genuine invariant?

A candidate should survive all of the following challenges.

### 5.1 Handoff relevance
The distinction must matter across at least one heterogeneous interface. A feature useful only inside a local representation is not automatically part of a cognitive contract.

### 5.2 Recoverability rather than coordinate identity
E1, E2, E3, hippocampal representations, body-state representations and later systems may encode the same relation in very different geometries. The question is whether the receiver can recover what matters, not whether latent coordinates align.

### 5.3 Consumer relevance
No interface should preserve every distinction. The receiver's actual downstream needs determine the obligation.

### 5.4 Irreducibility under constrained reconstruction
If the receiver can cheaply, robustly and rapidly reconstruct a candidate from an already-supported smaller basis, the candidate is probably a composite.

### 5.5 Transfer
The relation should survive remapped objects, held-out worlds, altered surface features, novel tasks, or changed latent parameterisations when its underlying structure is preserved.

### 5.6 Causal use
Selective corruption should produce a predicted cross-module failure. Mere correlation or post-hoc decodability is insufficient.

### 5.7 Nuisance resistance
The result must survive removal of trivial proxies such as task clocks, coordinates, object IDs, reward labels, response magnitude, episode indices, fixed branch IDs, and local surprise.

### 5.8 Computational availability
Information-theoretic reconstructability is not enough. A relation may be derivable in principle but unavailable to the actual receiver within its compute, latency, sample and robustness constraints.

This last criterion creates an important distinction:

- **logical reducibility** — a mathematician can derive it;
- **information-theoretic reducibility** — the needed information exists elsewhere;
- **computational reducibility** — the receiver can derive it with plausible resources;
- **operational reducibility** — the receiver can derive it reliably and quickly enough for the behaviour in question.

Only the last two are decisive for a functioning cognifold.

---

## 6. Decodability is not recoverability

A powerful nonlinear probe can often extract information that the downstream cognitive system itself cannot access. This creates a major false-positive route.

The programme should therefore distinguish:

```text
information present in latent
        !=
information cheaply decodable by a researcher
        !=
information recoverable by the receiving subsystem
        !=
information causally used by that subsystem
```

Evidence should become progressively stronger in that order.

Where possible, the relevant test should be **consumer-accessible recoverability**:

- use the receiver itself as the decoder;
- or restrict probes to a receiver-matched decoder class;
- report probe complexity and sample efficiency;
- compare against nuisance-matched baselines;
- and confirm causal use by perturbing the relation at the handoff.

A relation that is recoverable only by a large external probe should not be promoted as a cognitive contract invariant.

---

## 7. Red-team compression: from fourteen candidates toward three structural families and two fields

The strongest result of the present pass is that the fourteen ledger candidates do **not** currently look like fourteen independent primitives.

A more parsimonious hypothesis is that much of the apparent inventory may be generated from **three structural families plus two attached weighting fields**.

This is not a replacement ledger. It is a destructive model to test against the ledger.

### 7.1 Structural family A — correspondence / binding

Working hypothesis:

> heterogeneous systems require some way to preserve which token, event, state or relation in one representation corresponds to which in another or across time/context.

This may absorb much of:

- `CCI-001` identity continuity,
- `CCI-006` equivalence / similarity.

Identity could be a special case of correspondence constrained by continuity:

```text
identity-like relation
    ~= correspondence
     + continuity constraints
     + persistence through transformation
```

Equivalence could be correspondence under a specified respect or transformation:

```text
equivalence-like relation
    ~= correspondence under task/relation-preserving transformation
```

The merger must not be accepted merely because both can be described with the word “correspondence”. Identity should remain separate if persistent credit assignment, tracking or episodic binding requires information that equivalence does not supply.

**Red-team verdict:** strong merge candidate; preserve both canonical records until a controlled reduction succeeds.

### 7.2 Structural family B — directed event / trajectory structure

Working hypothesis:

> what matters may not be TIME and TOPOLOGY as separate primitives, but a structured relation among event instances: succession, persistence, reachability, branching, adjacency, duration and transition.

This may absorb much of:

- `CCI-002` temporal relation,
- `CCI-007` relational topology,
- part of `CCI-004` agency when transitions are action-conditioned.

A simple graph over state values is not enough. Recurrent states create cycles; the same state may occur at different moments; simultaneity and duration may matter. The relevant representation may need event tokens, a partial order, interval relations, or a trajectory structure rather than a scalar clock.

A useful decomposition is:

```text
directed event structure
    = event/token instances
    + ordered or partially ordered succession
    + reachable transition relations
    + persistence/correspondence across transitions
    + optional typed intervention edges
```

If action-labelled edges are sufficient to reconstruct controllability, much of explicit AGENCY may disappear from the deepest contract.

**Red-team verdict:** strong merge candidate for temporal relation + topology; agency should be forced to survive an intervention-labelled transition account before being treated as primitive.

### 7.3 Structural family C — generative context / anchoring / lineage

Working hypothesis:

> many epistemic-mode distinctions may reduce to where a representation sits in a generative lineage: which process produced it, which branch it belongs to, whether that branch is anchored to the current sensory worldline, and how it relates to other generated alternatives.

This family may explain much of:

- `CCI-003` reality status,
- `CCI-012` alternative branch status,
- source/provenance distinctions not currently represented as a canonical CCI record,
- self/other or ownership distinctions where these are needed.

Instead of a binary REALITY bit, a system may preserve relations such as:

```text
current sensory-anchored lineage
past reconstructed lineage
future predicted branch
internally generated hypothetical branch
counterfactual branch conditioned on altered premise
externally communicated lineage
```

“Actual” may then be a relation to the currently sensory-anchored worldline rather than a primitive category. Perception, memory, imagination, prediction and counterfactual reasoning could occupy different regions of this lineage structure.

This family also offers a more precise source-monitoring hypothesis: confusion may arise because lineage/anchoring information is degraded, not because a dedicated REALITY neuron or symbol has been lost.

**Red-team verdict:** strong reduction target for reality status + alternative branch status; provenance/ownership should remain unnumbered decomposition hypotheses until independently justified.

### 7.4 Attached field D — epistemic weight

`CCI-005 confidence / precision` may not be a structural relation of the same kind at all.

A receiver often needs to know not just what content arrived but how reliable the producer believes that content to be. Yet “confidence”, “uncertainty”, “precision”, “gain” and “metacognitive confidence” are not automatically the same quantity.

A better working hypothesis is an **epistemic weighting field** over states, edges or translations.

This field becomes a contract obligation only when the producer has reliability information that the receiver cannot cheaply reconstruct locally.

Important subcases must be distinguished:

- uncertainty about world state,
- uncertainty about a predicted transition,
- confidence in a memory/source,
- confidence in a translation itself,
- precision/gain used by control machinery,
- reportable metacognitive confidence.

**Red-team verdict:** keep `CCI-005`, but reclassify provisionally from “content primitive” to “possibly boundary-specific epistemic field”. Do not collapse these subtypes without evidence.

### 7.5 Attached field E — regulatory / viability weight

`CCI-009 value / valence` may likewise be a weighting field rather than a universal semantic primitive.

Signed reward or harm/benefit may emerge from a deeper relation between state/trajectory and organism viability or preferred regulatory ranges:

```text
regulatory value
    ~= predicted relation to viable/preferred states
     + direction/rate of change
     + horizon
```

This could in turn help derive:

- `CCI-010` goal relation,
- `CCI-014` priority / relevance,
- some forms of persistent action organisation.

But viability is itself strongly embodied. It may be essential to REE as an organism while not belonging to the universal core of every cognitive handoff.

**Red-team verdict:** keep value/valence as a ledger candidate, but test it as an embodied/regulatory field and boundary-specific obligation rather than assuming universal contract status.

---

## 8. Candidate-by-candidate red-team adjudication

### `CCI-001` identity continuity
**Attack:** reduce to correspondence/binding plus continuity constraints over directed event structure.  
**Why it may survive:** persistent credit assignment and episodic integration may require continuity information that ordinary similarity cannot provide.  
**Current status:** strong candidate family, primitive status unproven.

### `CCI-002` temporal relation
**Attack:** reduce scalar or symbolic time to ordered event/trajectory structure.  
**Why it may survive:** duration, simultaneity, recurrence and temporal distance may require more than reachability.  
**Current status:** likely necessary relation family; representation unresolved.

### `CCI-003` reality status
**Attack:** derive from generative lineage + sensory anchoring + branch history.  
**Why it may survive:** receivers may need a fast explicit actuality signal when lineage reconstruction is too expensive or ambiguous.  
**Current status:** strong demotion/merge candidate.

### `CCI-004` agency
**Attack:** derive from action-labelled transition structure + correspondence/ownership + intervention sensitivity.  
**Why it may survive:** self-generated action, causal responsibility and controllability may dissociate despite identical transition statistics.  
**Current status:** presume composite until intervention-controlled lesions show irreducible residue.

### `CCI-005` confidence / precision
**Attack:** separate into multiple epistemic/control quantities and test whether receivers can infer each locally.  
**Why it may survive:** producer-private uncertainty often cannot be recovered from content alone.  
**Current status:** plausible boundary field; generic CONFIDENCE primitive rejected.

### `CCI-006` equivalence / similarity
**Attack:** derive from correspondence under transformation or receiver-local geometry.  
**Why it may survive:** relational generalisation may require explicit similarity/equivalence not preserved by raw latent distance.  
**Current status:** strong merge candidate with correspondence/binding.

### `CCI-007` relational topology
**Attack:** fold into directed event/trajectory structure.  
**Why it may survive:** topology can remain invariant under large sensory remappings and may be exactly what planners/predictors require.  
**Current status:** one of the strongest experimentally tractable relation families.

### `CCI-008` magnitude / order
**Attack:** derive from metric/embedding/comparator machinery local to the receiver.  
**Why it may survive:** ordinal structure may transfer where metric details do not.  
**Current status:** keep in ledger; presently outside the smallest core hypothesis.

### `CCI-009` value / valence
**Attack:** derive signed value from viability/preference + predicted direction of change.  
**Why it may survive:** cross-module coordination may require a compact signed regulatory signal even if it is derived upstream.  
**Current status:** regulatory field candidate, likely embodied/boundary-specific.

### `CCI-010` goal relation
**Attack:** derive from preferred future + persistence + controllability + regulatory weighting.  
**Why it may survive:** persistent commitment can display hysteresis not captured by instantaneous value.  
**Current status:** likely composite until proven otherwise.

### `CCI-011` negation / absence
**Attack:** reduce to expectation + context/time window + failure to obtain.  
**Why it may survive:** explicit absence can become useful when omitted events themselves must be represented and communicated.  
**Current status:** abstract logical negation strongly demoted; expected-absence relation remains testable.

### `CCI-012` alternative branch status
**Attack:** derive from generative lineage/branch structure.  
**Why it may survive:** treating counterfactual branches as actual is catastrophically consequential; a cheap explicit branch marker may be operationally necessary.  
**Current status:** strong candidate family, likely merge with generative context rather than independent primitive.

### `CCI-013` commitment status
**Attack:** treat as local control/policy state derived from confidence, value, persistence and branch status.  
**Why it may survive:** two equally valued/confident alternatives can differ in whether one has been selected for persistent policy execution.  
**Current status:** boundary/control candidate, not established world-content invariant.

### `CCI-014` priority / relevance
**Attack:** derive from expected epistemic gain + regulatory consequence + urgency + control needs.  
**Why it may survive:** cross-system scheduling may require explicit communicated priority.  
**Current status:** likely control-plane field or derived scheduler quantity rather than deep semantic invariant.

---

## 9. Familiar cognitive modes as composites

The red-team compression makes a stronger version of the earlier decomposition possible.

A cognitive mode may be reconstructed from:

```text
mode
    ~= generative lineage / anchor
     + location in event/trajectory structure
     + branch relation
     + epistemic weight
     + local update/control state
```

Very roughly:

- **perception-like:** present sensory-anchored lineage;
- **memory-like:** past event structure reconstructed into the present but anchored to a lineage believed to have obtained;
- **imagination-like:** internally generated lineage without commitment to current-world anchoring;
- **prediction-like:** future branch generated from current anchored state with graded epistemic weight;
- **counterfactual-like:** branch generated under an explicitly altered premise and marked as non-current lineage.

These are not definitions to hard-code. They are reduction hypotheses.

A powerful result would be that mode labels can be removed entirely while downstream systems continue to distinguish these cases from the lower-dimensional relational structure. A falsifying result would be that same-structure states still require an irreducible mode signal to avoid systematic confusion.

---

## 10. Agency, goal, negation and salience as deliberately vulnerable composites

### Agency

```text
agency-like organisation
    ~= action-labelled event/transition structure
     + intervention sensitivity
     + correspondence/ownership where required
     + regulatory consequence
```

The key assay is whether action-effect competence survives without a dedicated agency representation.

### Goal

```text
goal-like organisation
    ~= candidate future state
     + regulatory preference/viability
     + persistence over time
     + controllability
     + policy/commitment state
```

### Negation-like processing

```text
absence-like representation
    ~= expected event/token
     + defined context/time window
     + failure to obtain
```

This is intentionally weaker than abstract logical `NOT`.

### Salience / priority

```text
priority-like signal
    ~= expected epistemic consequence
     + expected regulatory consequence
     + urgency
     + control bottleneck
```

If a downstream subsystem can recompute this cheaply, `CCI-014` does not need to cross that handoff.

---

## 11. A warning against the vacuous “one graph” solution

The three structural families can themselves be written as one typed relational graph with weighted nodes and edges. This is mathematically convenient and scientifically dangerous.

It would be trivial to say:

> cognition only needs one invariant: the full typed relation graph.

That is not a reduction. It merely renames the entire problem.

A valid collapse must satisfy three requirements:

1. **Lower total description/rate cost** under fixed assumptions about precision and decoder power.
2. **Preserve discriminating predictions** — the reduced model must still predict distinct failure signatures when different information is corrupted.
3. **Improve transfer or efficiency** — the reduced representation should generalise or communicate better than an unconstrained equivalent-capacity code.

Therefore “correspondence”, “event structure” and “generative lineage” should themselves be attacked. They are useful only if they compress multiple candidates without hiding equal complexity inside their type system.

---

## 12. Lesions, ablations and compensation: a stronger causal standard

Deleting a latent coordinate and observing worse behaviour is not enough.

Ablation can fail in two opposite directions:

- it can cause an **off-manifold lesion**, damaging many unrelated computations and falsely making a candidate look necessary;
- or the organism can **compensate** through an alternative pathway, falsely making the original mechanism look unnecessary if only post-adaptation behaviour is examined.

For each candidate or reduced family, the causal assay should therefore include where feasible:

1. acute perturbation with weights frozen;
2. matched random/subspace information-loss controls;
3. within-manifold counterfactual replacement or resampling rather than only zeroing;
4. nuisance-matched perturbations preserving total energy/rate;
5. receiver-side recoverability measurement;
6. behavioural and internal error signatures;
7. continued lesion with controlled adaptation;
8. measurement of alternative-pathway recruitment and recovery;
9. restoration/rescue where possible.

The interpretation must distinguish:

- **normally used**,
- **causally important in the intact system**,
- **uniquely necessary**,
- **replaceable after adaptation**,
- **functionally recoverable through compensation**.

A compensated system may show that the *function* is important while the original *mechanism* is not unique. That is particularly relevant to a distributed cognifold, where multiple realisation may be a feature rather than a nuisance.

---

## 13. The narrowing latent stack becomes a discovery experiment, not an assumption

The user's narrowing-stack intuition now gives this thought a powerful independent test.

Suppose successive latent levels are constrained so that less transferable information can survive at greater height. If several heterogeneous consumers must continue to predict, reconstruct, remember and control successfully, then representations useful only to one local geometry should become increasingly expensive. Relations useful across consumers, contexts and remappings may preferentially survive.

But **fewer nodes is not by itself an information bottleneck**. A small number of unconstrained continuous variables can still carry a large amount of information.

The experiment therefore needs explicit capacity pressure such as:

- finite numerical precision,
- injected noise,
- quantisation,
- sparsity/activity budget,
- entropy or rate regularisation,
- variational/KL constraints,
- or an explicit rate-distortion budget.

A cleaner family of conditions is:

```text
A  wide / weakly constrained control
B  width-narrowed only
C  true rate-constrained single-consumer bottleneck
D  true rate-constrained multi-consumer bottleneck, unlabeled
E  relation-supervised bottleneck, positive control
F  capacity-matched nuisance/random-relation control
```

The important condition is **D**. Candidate invariant labels remain sealed from its training objective.

Evidence for spontaneous invariant discovery would require more than probe success. At increasing stack height we would want to see, across seeds:

- lower recoverability of irrelevant particulars;
- preserved or improved receiver-accessible recoverability of transferable relations;
- survival under object/world remapping;
- multi-consumer utility exceeding single-consumer/rate-matched controls;
- increasingly economical decoding rather than only more powerful-probe decodability;
- selective causal failure when the emergent relation is perturbed;
- and no hidden side channel carrying the discarded detail.

A striking result would be that the upper hierarchy converges toward the independently predicted structural families **without being taught their names**.

A negative result is equally useful. It may show that narrowing alone produces entangled arbitrary codes, that explicit relational inductive bias is needed, or that the contract is dynamically negotiated rather than statically represented.

---

## 14. The most important experimental separation: structural content versus attached fields

The **3 + 2** hypothesis makes a concrete prediction.

Structural relations and weighting fields should behave differently under transfer.

### Structural families
Correspondence, event/trajectory structure and generative lineage should tend to survive remapping when the world relation remains the same despite changed surface features.

### Attached fields
Epistemic and regulatory weights may vary strongly with current uncertainty, needs, goals, physiology and task regime even when structural content is unchanged.

This yields clean crossed experiments:

- hold structure fixed while changing confidence;
- hold structure fixed while changing viability/value;
- hold confidence fixed while changing branch lineage;
- hold value fixed while changing controllability;
- hold sensory content fixed while changing source/generative path.

If structural and weighting variables cannot be dissociated, the 3 + 2 model is wrong or too simple.

---

## 15. Candidate-specific failure signatures after compression

The following remain hypotheses, not definitions.

- **correspondence/binding failure:** tracker fragmentation, unstable cross-representation reference, repeated relearning, credit-assignment and episodic binding errors;
- **directed event/trajectory failure:** sequence inversion, reachability errors, rollout confusion, causal-order mistakes, failure to distinguish recurrent instances of the same state;
- **generative lineage/anchoring failure:** observed/generated confusion, memory/prediction contamination, counterfactual branches treated as experienced, confabulation-like model drift;
- **epistemic-weight failure:** preserved content but pathological over-weighting, under-weighting, unstable update or calibration failure;
- **regulatory-weight failure:** preserved world structure but disorganised preserve/avoid trade-offs, poor prioritisation, or failure to organise trajectories relative to viable states;
- **intervention/control residue, if irreducible:** passive prediction preserved with selective loss of action-effect learning and controllability attribution;
- **expected-absence residue, if irreducible:** inability to represent omitted expected events despite intact raw surprise.

If these signatures do not dissociate under nuisance-controlled perturbation, the candidate boundaries should be redrawn rather than defended.

---

## 16. Strong falsifiers of the programme

The cognitive-contract programme should itself be vulnerable to failure.

Several outcomes would weaken it substantially:

1. **No reusable compact structure exists.** Different consumers repeatedly require unrelated task-specific exchange variables.
2. **Ordinary latent geometry is operationally enough.** Actual receiving modules cheaply reconstruct every required distinction without any stable cross-system relation family.
3. **Probe-only invariants dominate.** Candidate information is externally decodable but unavailable or unused by receivers.
4. **Lesion specificity disappears.** Controlled corruption produces only generic information loss.
5. **Cross-domain convergence evaporates.** Linguistic, developmental, neural, comparative and artificial-system evidence support incompatible structures.
6. **Remapping destroys transfer.** Apparent invariants depend on coordinates, object IDs, task labels or fixed environmental statistics.
7. **Multi-consumer bottlenecks do not favour transferable relations.** Unlabelled multi-consumer compression behaves like ordinary narrowing or memorises particulars.
8. **The basis continually expands.** Every new task requires another named invariant and total description cost fails to fall.
9. **The reduction only works by decoder inflation.** Fewer transmitted variables require increasingly powerful or task-specific reconstruction machinery.
10. **Boundary-specificity defeats a shared core.** Useful obligations exist, but their overlap across the cognitive graph is negligible.

Any of these would be a scientific result, not a reason to redefine the contract until it becomes unfalsifiable.

---

## 17. Developmental and linguistic predictions after the red-team pass

If the deepest contract is relational rather than linguistic, much of the structural skeleton should operate before explicit language.

The prediction is not that infants possess adult concepts called CAUSE, REALITY, NEGATION or GOAL. It is that early cognition may preserve enough lower-level structure for continuity, ordered events, expected transitions, alternative possibilities, source/anchoring, confidence-sensitive learning and regulatory preference.

Language could then label, compress, combine and communicate these relations.

The relation to grammar remains asymmetric:

> language can suggest distinctions worth testing, but nonlinguistic evidence must decide whether they are deep cognitive obligations.

If independently discovered REE representations and nonlinguistic biological evidence later converge on structures resembling tense, aspect, modality, evidentiality, agency, negation or comparison, that would be much more interesting than building those categories into the model and rediscovering them.

---

## 18. Implication for the cognifold

The red-team revision makes the cognifold idea sharper.

A cognifold need not share one canonical latent space and may not even share one globally flat cognitive contract. It may instead consist of specialised representational spaces linked by a graph of transformations whose **boundary-specific obligations collectively preserve coherent reference, history, alternatives, epistemic weighting and action organisation**.

Unity could therefore be a property of the transformation network rather than of any one representation.

This also gives a future way to distinguish cognifold from braidling:

- a **cognifold** may consist of systems whose independent local representations are incomplete without recurrent, invariant-preserving participation in one jointly maintained world/history/action structure;
- a **braidling** may consist of independently coherent cognitive entities that can preserve their own world/history/action structures while communicating through an external channel.

This remains a hypothesis for the later cognifold thought, not a settled criterion.

---

## 19. Revised promotion hierarchy

**Stage 0 — named canonical candidate**  
The relation exists in the governed ledger.

**Stage 1 — cross-domain recurrence**  
Independent evidence domains suggest structurally similar functionality.

**Stage 2 — transferable receiver-accessible recoverability**  
The relation can be recovered by a plausible receiver across held-out content, tasks or remappings.

**Stage 3 — causal handoff dependence**  
Selective nuisance-controlled corruption produces the predicted deficit at a relevant interface.

**Stage 4 — irreducibility under constrained reconstruction**  
A smaller basis cannot reproduce the function without excessive rate, decoder, context, latency or robustness cost.

**Stage 5 — adaptation-aware characterisation**  
Compensation, alternative pathways and rescue are understood well enough to distinguish functional necessity from mechanism uniqueness.

**Stage 6 — boundary scope established**  
We know which handoffs require the relation and which can reconstruct or omit it.

Only then should a candidate be considered for stronger architectural treatment.

---

## 20. Immediate work programme

### 20.1 Keep Thought 2 undigested
No candidate should be promoted from this red-team pass. This document is doing ontology destruction, not architecture declaration.

### 20.2 Preserve the canonical fourteen-record ledger as the baseline
Do not rewrite the initial candidate set after seeing results. Future merges, demotions and additions should be versioned.

### 20.3 Materialise the missing planned artefacts before citing them as evidence
The evidence pull, narrowing preregistration and Stage-0 V3 substrate audit previously named in this thought are not present on the default branch at this revision. Either create them through the normal evidence/governance route or remove them permanently. Until then, claims depending on them remain hypotheses/checks.

### 20.4 Run forced-merger tests first
Highest-value attacks are:

```text
CCI-001 identity
 + CCI-006 equivalence
        -> correspondence/binding ?

CCI-002 temporal relation
 + CCI-007 relational topology
        -> directed event/trajectory structure ?

CCI-003 reality status
 + CCI-012 alternative branch status
 + unnumbered provenance/anchoring hypotheses
        -> generative lineage ?

CCI-004 agency
        -> action-labelled transition structure
         + intervention sensitivity
         + ownership/correspondence ?

CCI-009 value
        -> viability/preference
         + direction of change ?

CCI-010 goal
 + CCI-013 commitment
 + CCI-014 priority
        -> regulatory/control composites ?

CCI-011 negation/absence
        -> expectation + failure-to-obtain ?
```

### 20.5 Attack `CCI-005` separately
Confidence/precision is at high risk of becoming an overloaded label. Separate state uncertainty, translation confidence, control precision and metacognitive confidence before deciding whether any common invariant exists.

### 20.6 Build the narrowing experiment as a true capacity experiment
Width alone is insufficient. Rate-match conditions and seal candidate labels from the unlabeled multi-consumer condition.

### 20.7 Measure receiver access, not only external probes
The receiver's own capacity and causal use should be central to promotion.

### 20.8 Preserve compensation as data
Acute loss, adapted recovery and alternative pathway recruitment should all be measured. Recovery must not be misread as proof that the original function was irrelevant.

### 20.9 Preserve the language firewall
Do not use grammatical labels as supervision for invariant discovery. Return to language only after nonlinguistic/artificial analyses have been frozen wherever feasible.

---

## 21. Red-team verdict

The provisional “nine-ish” basis from the first draft does **not** survive this pass unchanged.

The current stronger compression hypothesis is:

```text
STRUCTURAL SKELETON
  A. correspondence / binding
  B. directed event / trajectory structure
  C. generative context / anchoring / lineage

ATTACHED FIELDS
  D. epistemic weight
  E. regulatory / viability weight
```

with intervention/control, commitment, goal, priority, absence, magnitude and other familiar categories forced to prove that they contain irreducible information not already available from this basis or locally reconstructable at the relevant boundary.

Even **3 + 2 is not a target answer**. It is simply the smallest hypothesis currently worth attacking without collapsing into the vacuous claim that “everything is one typed graph”.

No candidate is promoted by this revision.

---

## 22. Current best prediction

The most interesting outcome would not be discovery of a miniature human grammar inside REE.

It would be that heterogeneous cognitive consumers, when forced through genuine information bottlenecks and required to remain mutually useful, spontaneously preserve a compact structure resembling:

- correspondences that keep reference stable,
- directed event relations that preserve succession and possibility,
- generative lineage that separates current world, memory and alternatives,
- epistemic weighting that preserves reliability where it cannot be locally reconstructed,
- and regulatory weighting that preserves organism-relevant preference where needed.

Richer concepts could then arise as local reconstructions or compressions over that structure.

If this happens without candidate labels being supplied, and if the relations survive remapping, receiver-access tests and causal perturbation, it would be evidence that a cognitive contract can **emerge from the demands of maintaining one cognition across heterogeneous representational spaces**.

If it does not happen, the alternatives are equally informative: richer shared geometry, interface-specific message passing, dynamically negotiated contracts, or something closer to coordination among semi-independent systems may be required.

---

## 23. Central principle

> **The cognitive contract should contain no distinction merely because humans can name it, and no reduction should count merely because humans can rename it. A relation belongs only when a real receiving system repeatedly needs it, cannot reconstruct it cheaply and robustly from a smaller basis, and fails in a specific way when it is lost.**

The goal is not the shortest vocabulary. It is the **smallest causally and computationally sufficient transferable structure that lets heterogeneous representations remain parts of one coherent cognition**.
