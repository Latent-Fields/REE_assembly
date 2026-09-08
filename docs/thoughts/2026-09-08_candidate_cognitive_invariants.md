# Thought: Candidate Cognitive Invariants

**Date:** 2026-09-08  
**Status:** active evidence synthesis / draft — not digested  
**Parent thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`  
**Related architecture:** `docs/architecture/cognitive_contract.md`  
**Evidence ledger:** `evidence/planning/cognitive_contract_invariant_ledger.v1.json`  
**Ledger schema:** `evidence/planning/cognitive_contract_ledger_schema.v1.json`  
**Evidence pulls:** `evidence/planning/cognitive_contract_evidence_pull_2026-09-08.md`, `evidence/planning/cognitive_contract_evidence_pull_2026-09-08_b.md`  
**Experimental preregistration:** `evidence/planning/cognitive_contract_narrowing_preregistration_2026-09-08.md`  
**V3 substrate audit:** `evidence/planning/cognitive_contract_stage0_v3_substrate_audit_2026-09-08.md`  
**Related language thought:** `docs/thoughts/2026-02-09_language.md`

---

## 1. Why this thought exists

The parent thought, **Deriving the Cognitive Contract**, established a methodological claim: heterogeneous cognitive systems do not necessarily need identical latent geometries in order to belong to one coherent cognitive system. What they may need instead is reliable preservation of certain relations across representational handoffs.

That left the dangerous question unresolved: **which relations?**

It would be easy to answer this by inspecting human language, introspection, the existing REE architecture, or familiar philosophical categories and then writing a plausible list. That would also be an excellent way to build our assumptions into the system and later rediscover them as apparent necessities.

This thought therefore has a deliberately destructive purpose. It is not a catalogue of concepts that seem important. It is an attempt to **destroy, merge, demote, or reclassify candidate invariants until the smallest defensible cognitive contract remains**.

The working proposition is:

> A cognitive invariant is not a universal symbol, concept, feature, or shared latent coordinate. It is a relation whose recoverability across representational transformations may be required for heterogeneous cognitive processes to continue referring coherently to the same world, history, alternatives, and possible actions.

Nothing in the present candidate inventory is yet entitled to architectural status merely because it appears in this document.

---

## 2. What would count as an invariant?

A candidate should be treated as a possible cognitive invariant only when several conditions are at least plausible.

First, it must matter **across a handoff**. A distinction that is useful only within one representation does not need to belong to a contract between representations.

Second, it must be **recoverable rather than coordinate-identical**. E1, E2, E3, hippocampal representations, body-state representations and later systems may encode the same relation in very different geometries. The contract concerns what survives translation, not how it is locally implemented.

Third, the relation should be **consumer-relevant**. No representation should be forced to preserve every possible distinction. The contract is conditional on what downstream cognition actually requires.

Fourth, a candidate should survive an **irreducibility challenge**. If a downstream consumer can cheaply and reliably reconstruct a proposed invariant from simpler relations already present, the proposed invariant may be a composite rather than a primitive contract item.

Fifth, the candidate must survive **nuisance controls and alternative explanations**. Apparent identity may merely be an object ID. Apparent time may merely be the task clock. Apparent confidence may merely be response strength. Apparent source may merely be familiarity. Apparent salience may merely be local surprise.

Finally, a strong candidate should generate a **specific causal failure mode when lost**. If deleting it makes no distinctive difference, or if the effect disappears as soon as the system adapts or nuisance variables are controlled, it should not be promoted simply because it is decodable.

This suggests five classes that must not be conflated:

1. **Architectural invariant:** a relation that must remain recoverable across some heterogeneous cognitive handoffs.
2. **Derived composite:** a useful higher-order distinction reconstructed from more primitive relations.
3. **Embodied/ecological regularity:** recurrent because agents like us inhabit bodies and worlds with particular structures.
4. **Cultural/linguistic convention:** recurrent because human communicative systems have conventionalised it.
5. **Local representational convenience:** useful to one module or implementation but unnecessary as a cross-system contract.

The present evidence ledger therefore keeps `architectural / embodied / cultural / uncertain` classification explicit and preserves counterevidence rather than allowing candidate accumulation to masquerade as progress.

---

## 3. Method: triangulation with a promotion barrier

The evidence programme deliberately samples independent domains:

- cross-linguistic typology and grammar,
- developmental cognition,
- neuroscience,
- comparative cognition,
- artificial agents and representation learning,
- REE-specific recordings and experiments,
- causal lesion/ablation evidence,
- counterevidence and simpler alternative explanations.

Language remains useful as an **inverse probe**: recurrent grammatical distinctions can tell us what kinds of relations human minds repeatedly need to make communicable. But linguistic recurrence cannot promote a candidate by itself. Human languages share phylogeny, bodies, sensory systems, ecological constraints and social problems. A language universal may therefore be cognitively deep, merely embodied, or historically conventional.

Likewise, the current REE architecture cannot be used as the source of truth. REE is an experimental system in which the hypotheses can be tested. It must not become circular evidence for distinctions that were placed there by design.

A candidate should therefore face four promotion gates:

### Gate A — recurrence
The relation recurs across genuinely independent evidence domains or computational settings.

### Gate B — transfer
The relation remains useful under remapping, novel content, held-out worlds, new tasks, or different internal representational geometries.

### Gate C — irreducibility
The relation is not cheaply and reliably reconstructable from a smaller already-supported basis.

### Gate D — causal necessity
Selective loss or corruption produces the predicted cross-module failure, with acute and adaptation-aware lesions distinguished.

Decodability alone is insufficient. Linguistic namability is insufficient. Familiarity is insufficient. REE implementation history is insufficient.

---

## 4. The candidate field has already begun to shrink

The first evidence passes suggest that the flat initial brainstorm was too large. Several familiar cognitive categories may be better understood as **composites produced from a smaller relational basis**.

The current working arrangement is approximately:

### Stronger first-line candidates

- token continuity / identity,
- equivalence / similarity relation,
- predictive relational topology / transition,
- temporal order / persistence,
- source / ownership / provenance,
- branch / obtaining / hypothetical status,
- causal / control relation,
- epistemic confidence / precision.

### Plausible second-layer candidates

- non-obtaining / expected absence,
- ordered magnitude / comparison,
- viability / preference.

### Current likely composites or implementation-level products

- agency,
- perception,
- memory,
- imagination,
- prediction,
- goal,
- commitment,
- exact number,
- kind / part,
- salience / priority,
- signed harm / benefit / value.

This ordering is deliberately provisional. It is more important that the programme be capable of **demoting a persuasive candidate** than that the present ranking be correct.

---

## 5. Candidate family I: referential and structural relations

### 5.1 Token continuity / identity — `CCI-001 identity_continuity`

The candidate is deliberately narrower than philosophical identity or selfhood. The question is whether heterogeneous systems need some recoverable relation equivalent to **this token now is continuous with that token then**.

Without such a relation, a system may be unable to accumulate evidence about persistent entities, bind consequences back to earlier states, or maintain stable reference during representational change. A failure could look like tracker fragmentation: the same entity repeatedly becomes a new entity for downstream cognition.

The counterargument is strong. Apparent identity may be supplied by low-level segmentation, object tracking, spatial continuity, body organisation, or environmental IDs. If so, identity need not be a separate contract primitive.

The decisive test is therefore not whether identity can be decoded in one task. It is whether **multiscale continuity generalises across held-out content and representations after trivial trackers and task IDs have been removed**, and whether corrupting that relation causes selective continuity and credit-assignment failure.

Current stance: **plausible, but unresolved**.

### 5.2 Equivalence / similarity — `CCI-006 relational_equivalence`

A cognitive system frequently needs to preserve that two states, objects, actions, episodes or patterns are equivalent in some task-relevant respect even when their raw features differ.

This is one of the most interesting points of contact with work on relational bottlenecks: abstraction can improve when downstream systems receive relations rather than all object-specific particulars. That literature is a useful positive control, not proof that REE requires an explicit equivalence primitive.

The difficult alternative is that similarity is simply what a good latent geometry already supplies. If downstream consumers can robustly derive equivalence from distance, topology, or learned metrics, adding a special contract item would be redundant.

The candidate therefore survives only if relation-specific generalisation appears across held-out objects/tasks **after controlling raw latent distance and content features**, and if destroying the relation selectively damages analogy or transfer.

Current stance: **promising relational family; primitive status unresolved**.

### 5.3 Temporal order / persistence — `CCI-002 temporal_order`

A system that remembers, predicts or plans appears to require some way to preserve earlier/later, duration, persistence or sequence.

But time is especially vulnerable to false promotion. An experiment can accidentally provide temporal order through an episode counter, environment clock, sequence index, recurrent state, spatial progression or event container. A neural or artificial system may never need an explicit scalar notion of time.

The deeper candidate may therefore be **ordered succession** rather than clock time. What matters may be that one state precedes or follows another in a trajectory and that some tokens persist across that ordering.

Promotion should require decoding and causal usefulness of temporal relation under nuisance control for external clocks and event labels, plus predicted sequencing/rollout errors after lesion.

Current stance: **likely important relation, but representation and primitive status uncertain**.

### 5.4 Predictive relational topology / transition — `CCI-007 transition_topology`

This candidate currently looks unusually useful for REE.

The relation is not an object's coordinate. It is the structure of **what can follow what**: adjacency, successor, reachability, fork, transition probability, controllable path, or predictive neighbourhood. Such structure can survive large remappings of raw sensory representation while retaining exactly the information a predictor or planner needs.

This makes transition topology a particularly strong test of invariant-preserving translation. If the world is remapped but the successor/reachability structure is conserved, a representation that genuinely captures topology should transfer better than one that merely memorises coordinates or appearances.

The alternative is that transition structure belongs inside a predictive dynamics model rather than in any handoff contract. If every downstream system can reconstruct it cheaply from local dynamics, explicit preservation is unnecessary.

The decisive question is therefore whether a heterogeneous consumer loses planning/prediction competence when topology is selectively distorted despite preserved local state features, and whether the relevant relation transfers across remapped worlds.

Current stance: **one of the strongest experimentally tractable candidates**.

---

## 6. Candidate family II: epistemic and modal relations

This family may turn out to be where familiar cognitive modes are decomposed most dramatically.

### 6.1 Source / provenance — `CCI-008 source_provenance`

A representation can contain the same apparent content while differing in where that content came from: direct observation, another subsystem, replay, inference, imagination, prediction, testimony, or cached memory.

The key claim is not that the brain necessarily attaches a symbolic source tag. It is that **some relation to generator or evidence source may need to remain recoverable** when content crosses systems.

The obvious alternative is that source is reconstructed probabilistically from familiarity, sensory detail, confidence, content statistics and context. If so, provenance may be a derived judgment rather than a primitive contract relation.

This should be tested with same-content states in which source is manipulated while confidence and content are controlled.

Current stance: **important candidate family; likely needs merging analysis with ownership**.

### 6.2 Source / ownership — `CCI-011 source_ownership`

Ownership asks a slightly different question from provenance: was a state, action, proposition or trajectory generated by self, other, environment, or another subsystem?

The distinction may be critical for credit assignment, agency, replay routing and social attribution. But it may also be inseparable from provenance once nuisance factors are removed.

A good experiment should swap self-/other-generated or perceived/internally-generated status while matching the content and confidence of the state. If downstream weighting, routing or learning fails in a characteristic way, ownership gains support. If ordinary provenance plus content explains everything, the two candidates should merge.

Current stance: **likely part of a source family; separate primitive status unproven**.

### 6.3 Branch / obtaining status — `CCI-012 branch_obtaining_status`

One of the most consequential distinctions for a predictive organism is whether a represented state **obtains**, is merely expected, is imagined, is counterfactual, is a candidate branch, or has been rejected.

This is potentially more fundamental than the familiar categories of perception, memory, imagination and prediction. Those modes may be partly reconstructed from combinations of source, temporal position, branch status, confidence and update state.

REE gives this candidate a particularly clean failure prediction: if an imagined or counterfactual trajectory is replayed or learned from as though it had actually occurred, the organism should develop confabulation-like world-model drift or incorrect credit assignment.

The key reduction challenge is whether branch status is independently necessary once source, time and confidence are known.

Current stance: **promising candidate; high value for direct REE lesion testing**.

### 6.4 Epistemic confidence / precision — `CCI-003 confidence_precision`

Cognition does not merely represent content; it weights content differently according to reliability, expected precision or confidence. That weighting affects learning, action selection, conflict resolution and belief update.

The important caution is that **uncertainty, neural precision, metacognitive confidence and reportable task confidence may not be one thing**. Evidence for one should not automatically promote a generic CONFIDENCE primitive.

For the contract, the narrower question is whether a receiving system needs some recoverable estimate of the reliability or weighting of incoming information that cannot be reconstructed locally from the content itself.

A selective lesion should therefore produce characteristic over-weighting, under-weighting or miscalibration without simply deleting the represented content.

Current stance: **one of the stronger candidates, with internal decomposition still required**.

### 6.5 Epistemic update / commitment status — `CCI-013 epistemic_update_commitment`

Two representations may have the same content and similar confidence while differing profoundly in cognitive status: one may be an observation eligible for world-model update, another a hypothesis under evaluation, another a rejected possibility retained for counterfactual reasoning.

This suggests a possible contract dimension for **what the system is currently entitled or instructed to do with the representation**.

The reduction challenge is severe. Update status may be recoverable from source, branch status, confidence, freshness/update clocks, or local task state. If so, no new primitive is needed.

The decisive assay requires same-content, same-confidence states with different update eligibility or commitment status. Only an independently decodable state with causal downstream consequences deserves promotion.

Current stance: **hold as candidate, but presume composite until shown otherwise**.

### 6.6 Non-obtaining / expected absence — `CCI-005 expected_absence`

The original temptation was to write **negation**. The evidence so far counsels against that.

Nonlinguistic systems can respond specifically when an expected item or event fails to occur. That supports a relation closer to:

> X was expected in this position or branch, and X did not obtain.

This is much weaker than a universal logical `NOT`, and that weakness is useful. It may be sufficient for an organism to learn omission, failed expectation, absent reward, missing conspecific, blocked transition or violated prediction. Abstract negation could later emerge from repeated use of this more primitive relation.

The major alternative is that no absence relation is required at all: ordinary prediction error or surprise may account for the behaviour.

Promotion therefore requires an omission-with-held-expectation signal that survives controls for input energy, surprise and salience, and whose loss selectively impairs reasoning about omitted expected events.

Current stance: **retain in reduced form; do not promote abstract negation**.

---

## 7. Candidate family III: agentive and regulatory relations

### 7.1 Causal / control relation — `CCI-004 causal_control`

Agents need more than passive transition knowledge. Some transitions depend on their interventions; others happen independently. A useful relation may therefore distinguish **what follows** from **what can be made to follow by action**.

This is closely related to agency but need not be equivalent to it. Agency may be a composite built from intervention sensitivity, ownership, transition topology and value/viability.

The alternative is that a sufficiently rich action-conditioned transition model already contains everything required; no separate causal/control invariant is necessary.

A decisive assay therefore needs intervention sensitivity after controlling for ordinary temporal succession, similarity and identity. If lesion damages action-effect learning or counterfactual control while leaving passive prediction relatively intact, the candidate strengthens.

Current stance: **important relational hypothesis; likely coupled to transition topology**.

### 7.2 Viability / preference — `CCI-009 value_viability`

This candidate has become more interesting precisely because the first evidence pass weakened the naive version of it.

REE naturally speaks in terms of harm, benefit and value. But homeostatic reinforcement-learning approaches show that signed reward can arise from regulatory structure: an organism has preferred or viable states, and movement toward or away from those states generates reward-like signals.

Two rival hypotheses must therefore remain alive:

**H1 — signed value is itself a contract invariant.**  
A receiving system needs something equivalent to positive/negative value or harm/benefit preserved across handoffs.

**H2 — viability/preferred-state relation is deeper.**  
The system needs a representation of viable/preferred state plus directional movement relative to it; signed value is derived.

REE can discriminate these. If a system preserves viability distance and change direction while signed value is removed, does behaviour remain coherent? Conversely, can signed value substitute for richer viability relations across new conditions?

Current stance: **retain the viability/preference family; actively try to demote signed value as a primitive**.

### 7.3 Goal / commitment — `CCI-010 goal_commitment`

Goals feel fundamental because they dominate deliberate cognition. That does not mean GOAL is a primitive contract item.

A goal may be reconstructed from:

- a represented future state,
- viability or preference,
- persistence over time,
- action/control structure,
- confidence,
- update/commitment status.

If those relations are already available, an explicit goal representation may be a useful local compression rather than something every cognitive handoff must preserve.

The proper experiment is therefore to control for value, confidence and transition structure and ask whether an additional persistent commitment state remains necessary.

Current stance: **likely composite until proven otherwise**.

### 7.4 Salience / priority — `CCI-014 salience_priority`

Salience and attention are clearly important for cognition, but their importance does not automatically make them semantic invariants.

A priority or gain signal may instead belong to the control plane: it tells a subsystem **what to process now**, rather than **what the represented content means**. If each subsystem can recompute priority from local surprise, value, need and confidence, it need not cross the contract at all.

The candidate should only survive if priority/gain itself must be communicated across heterogeneous systems and if its lesion produces coordination failure while content remains intact.

Current stance: **more likely control-policy information than deep representational invariant; retain as a challenge case**.

---

## 8. Compression hypotheses: familiar cognitive modes may not be primitives

One of the strongest consequences of the evidence synthesis is that familiar words for modes of cognition may name **regions in a lower-dimensional relational space** rather than independent primitive states.

A useful provisional decomposition is:

```text
cognitive mode
    ≈ source / ownership
      × temporal relation
      × branch / obtaining status
      × update / commitment status
      × confidence / precision
```

For example, very roughly:

- **perception** may be present-directed, externally sourced, obtaining, update-eligible content;
- **memory** may be past-directed, internally reconstructed but externally anchored, treated as having obtained;
- **imagination** may be internally generated, non-obtaining or uncommitted content;
- **prediction** may be future-directed, candidate-branch content with graded confidence;
- **counterfactual** may be explicitly non-obtaining branch content conditioned on an alternative premise.

These descriptions are not definitions to hard-code. They are **reduction hypotheses**. Their value is experimental: if the modes can be reconstructed from smaller relations and lesions of those relations reproduce mode-confusion errors, then PERCEPTION, MEMORY, IMAGINATION and PREDICTION should not be placed separately into the deepest cognitive contract.

This also offers a possible computational account of source-monitoring and reality-monitoring errors. Failure need not mean loss of a dedicated REALITY variable; it may arise from corruption in the relational combination by which cognitive status is inferred.

---

## 9. Other likely composites

### Agency

A provisional decomposition is:

```text
agency
    ≈ transition topology
      + intervention/control sensitivity
      + source/ownership
      + temporal continuity
      + viability/relevance
```

An organism can therefore develop richer agency without requiring a single primitive AGENCY coordinate.

### Goal

```text
goal
    ≈ candidate future state
      + viability/preference
      + persistence
      + control possibility
      + commitment/update status
```

### Signed value

```text
signed value
    ≈ distance from preferred/viable state
      + direction of predicted or actual change
```

### Negation-like processing

```text
negation-like processing
    ≈ represented expectation
      + branch/obtaining status
      + expected item fails to obtain
```

### Exact number

Exact number should remain outside the minimal basis until there is evidence that it cannot be reduced to object individuation, ordered magnitude, comparison and learned symbolic machinery. The existence of human number grammar is not enough.

### Kind / part relations

These may turn out to be genuine structural invariants, but they currently have less direct support in the ledger than identity, equivalence and transition. They should be investigated rather than assumed.

---

## 10. A provisional minimal basis hypothesis

The current evidence is not sufficient to declare a minimal cognitive contract. It is sufficient to formulate a **minimal-basis hypothesis to attack**.

### Structural / referential

1. **identity continuity** — what remains the same token across change,
2. **relational equivalence** — what counts as similar/equivalent in a relevant respect,
3. **temporal order** — earlier/later/persistence or ordered succession,
4. **transition topology** — what can follow/reach what.

### Modal / epistemic

5. **source / ownership** — where content or action came from,
6. **branch / obtaining status** — actual/candidate/counterfactual/non-obtaining,
7. **confidence / precision** — how strongly the information should be weighted.

### Agentive / regulatory

8. **intervention / control** — which transitions are action-dependent,
9. **viability / preference** — relation to preferred or survivable states.

### Possible additional relation, currently under pressure to reduce

10. **update / commitment status** — whether content is eligible to alter the persistent model or action policy.

This is not a ten-item specification. It is a compact target for destructive testing. The expected scientific result is that some items merge, some split, some disappear and some currently missing relation proves necessary.

---

## 11. Candidate dependency graph

Thinking in dependencies rather than a flat vocabulary may be more productive:

```text
identity + temporal order
    └── persistence / continuity

identity + equivalence + transition topology
    └── transferable world structure

source/ownership + time + branch status + confidence + update status
    └── cognitive mode / epistemic status
       ├── perception-like
       ├── memory-like
       ├── imagination-like
       ├── prediction-like
       └── counterfactual-like

transition topology + intervention + ownership
    └── agency / controllability

viability + predicted state + temporal persistence + control
    └── goal-like organisation

expectation + branch/non-obtaining
    └── omission / negation-like processing
```

A dependency graph creates stronger tests than a list. If a proposed composite remains fully functional when its supposed higher-level label is absent but the lower-level relations survive, the higher-level item should be demoted. If the composite cannot be reconstructed, the graph is wrong and the missing relation becomes a new candidate.

---

## 12. The relational bottleneck result changes the experiment

Independent artificial-system work on relational bottlenecks is important because it demonstrates that abstraction can improve when information flow is constrained toward relational structure rather than object-specific content.

For REE, however, the more interesting hypothesis is stronger:

> If several heterogeneous downstream consumers must share a narrowing representation, optimisation pressure may discover which relations are worth preserving even when those relations are not labelled in advance.

This is why the preregistered comparison matters:

```text
A  wide representation control
B  narrowing alone
C  narrowing for one consumer only
D  imposed relational bottleneck — positive control
E  unlabeled multi-consumer narrowing — REE hypothesis
```

The candidate ledger must remain sealed from training. Language-derived labels must remain sealed until the latent analysis has been frozen. Otherwise the experiment merely manufactures the expected answer.

A particularly strong result would be that condition E preferentially preserves transferable relational information, outperforms B and C, and approaches the relation-favouring positive control D without being told which candidate relations to encode.

Equally important are the negative outcomes. If narrowing alone performs as well as multi-consumer narrowing, the special multi-consumer account weakens. If only the imposed relational bottleneck succeeds, explicit relational inductive bias may be necessary. If neither succeeds, the measurement regime may be inadequate. If the unlabeled condition preserves irrelevant particulars rather than transferable structure, the central hypothesis is directly challenged.

---

## 13. REE gives us causal tests rather than correlations

The current V3 substrate is useful precisely because E1, E2, E3 and hippocampal/trajectory systems are heterogeneous consumers rather than copies of a single representation.

The Stage-0 audit also produced an important negative result: the existing latent stack is **not** a simple monotonic narrowing hierarchy. The current approximate flow includes `z_self` and `z_world` feeding a wider `z_beta`, then narrower `z_theta` and `z_delta`. We therefore cannot inspect present-day V3 and retroactively claim that it already demonstrated invariant discovery through compression.

That forces a cleaner experiment: obtain a canonical frozen dataset of full latent vectors, validity/freshness state and behaviour, then train competing bottleneck/translation conditions offline. This protects the organism from architectural contamination while the hypothesis is being tested.

For each candidate relation, the strongest workflow is:

1. **Decode/reconstruct** the relation from held-out latent states.
2. **Control nuisance variables** that could trivially reveal it.
3. **Test transfer** under remapped objects/worlds/tasks.
4. **Corrupt only that relation** at a relevant handoff with weights frozen.
5. Measure the predicted acute functional deficit.
6. Maintain the lesion while allowing controlled adaptation.
7. Determine whether another representation or pathway compensates.

The distinction between acute and adaptation-aware lesion is essential. A distributed cognitive system may recover function after losing an important mechanism. Recovery would show multiple realisability or compensation, not that the original mechanism never mattered.

---

## 14. Candidate-specific lesion signatures

The following signatures are hypotheses to test, not definitions:

- **identity continuity loss:** repeated relearning of the same entity, tracker fragmentation, unstable credit assignment, episodic binding failures;
- **temporal order loss:** sequence inversion, planning confusion, inappropriate mixing of memory and prediction, impaired causal ordering;
- **transition-topology loss:** preserved local feature recognition but degraded reachability, route selection and counterfactual rollout;
- **source/ownership loss:** self/other or observed/generated confusion, replay misrouting, inappropriate evidential weighting;
- **branch/obtaining loss:** counterfactual or imagined trajectories treated as experienced, confabulation-like model drift, incorrect learning from rejected branches;
- **confidence/precision loss:** preserved content with pathological over-weighting, under-weighting, instability or calibration failure;
- **control/intervention loss:** passive prediction retained while action-effect learning and controllability attribution degrade;
- **viability/preference loss:** impaired preserve/avoid trade-offs and inability to organise action relative to preferred states;
- **expected-absence loss:** specific failure to represent omitted expected events despite intact raw surprise detection;
- **update/commitment loss:** hypotheses, observations and rejected branches become inappropriately interchangeable in persistent model update.

If lesions do not dissociate in these ways, candidate boundaries should be redrawn rather than defended.

---

## 15. Strong falsifiers of the entire programme

The cognitive-contract hypothesis should itself be vulnerable to failure.

Several outcomes would weaken it substantially:

1. **No compact basis exists.** Different consumers repeatedly require unrelated, task-specific exchange variables with little reusable relational structure.
2. **Ordinary latent geometry is enough.** Every apparent invariant can be cheaply and robustly reconstructed locally, making a special contract layer unnecessary.
3. **Lesion specificity disappears.** Candidate corruption produces only generic information loss once nuisance factors are controlled.
4. **Cross-domain convergence evaporates.** Linguistic, developmental, neural, comparative and artificial-system evidence cluster around different relations with no coherent common basis.
5. **Remapping destroys transfer.** Candidate relations appear decodable only while object identities, coordinates, task labels or environmental statistics are preserved.
6. **Heterogeneous consumers do not discover shared relational structure.** Multi-consumer compression behaves no differently from ordinary narrowing or memorises particulars instead.
7. **The basis continually expands without compression.** If every new task requires another named invariant, we have probably reinvented an ontology rather than discovered a contract.

A successful research programme should reduce description length, not merely accumulate vocabulary.

---

## 16. Implication for the cognifold

Even a validated cognitive contract would not by itself prove that a system is one mind. It would, however, provide a much sharper operational account of what unity could require.

A cognifold need not be one latent manifold. It may be a collection of local manifolds, specialised predictors, memories, control systems and learned translators whose representations are mutually non-isomorphic.

What makes them function as one cognitive system may be that the relations required for shared reference, prediction, epistemic status and action remain recoverable across their interfaces.

This suggests a future distinction between cognifold and braidling:

- in a **cognifold**, specialised systems participate in one continuously maintained self/world/history/alternative structure through dependency on invariant-preserving internal transformations;
- in a **braidling**, coherent cognitive entities can remain independently organised and communicate through an inter-agent channel.

That boundary remains unresolved and belongs mainly to the later cognifold thought. The present work supplies the candidate relations and assays needed to make the distinction testable rather than metaphorical.

---

## 17. Why grammar remains interesting after the pruning

The reduced candidate set still looks suspiciously grammar-like: reference and identity, temporal order, modality/actuality, evidential source, confidence/evidential strength, negation/absence, agency/control, comparison and value all have linguistic reflexes.

The correct inference remains asymmetric.

We should not say:

> language contains these categories, therefore cognition must contain these primitives.

We may eventually be able to say something weaker and more interesting:

> if independent cognitive evidence repeatedly identifies a small set of relations that heterogeneous systems must preserve, then grammar may be understood partly as a public compression scheme for transmitting those already-useful relations between minds.

Under that account, grammar would not create the contract. It would exploit and conventionalise distinctions that cognition already benefits from preserving.

This prediction should remain sealed until nonlinguistic and REE analyses are frozen wherever possible.

---

## 18. Developmental prediction

If the deepest contract is relational rather than linguistic, much of it should appear functionally **before explicit language**.

The relevant developmental question is not whether infants possess adult concepts such as CAUSE, REALITY, NEGATION or GOAL. It is whether early cognition already preserves enough lower-level relational structure to support continuity, expectation, omission, control learning, source discrimination, preference and alternative trajectories.

Later language could then label, compress, combine and communicate these relations rather than creating them ex nihilo.

This gives a useful test for candidate ranking: relations that appear only after particular linguistic or cultural training should be treated with suspicion as deep architectural invariants unless independent evidence shows an earlier nonlinguistic precursor.

---

## 19. A practical promotion hierarchy

Rather than assigning a binary primitive/not-primitive label, candidates should move through a staged hierarchy:

**Stage 0 — named candidate**  
There is enough motivation to keep an entry in the ledger.

**Stage 1 — cross-domain recurrence**  
Independent evidence domains suggest a structurally similar distinction.

**Stage 2 — transferable decodability**  
The relation can be recovered across held-out content, tasks or representation remappings.

**Stage 3 — causal handoff dependence**  
Selective lesion produces a predicted deficit at a relevant interface.

**Stage 4 — irreducibility challenge survived**  
The effect is not fully explained by a smaller set of already-supported relations or locally reconstructable state.

**Stage 5 — adaptation-aware characterisation**  
The system's capacity or failure to compensate is understood, distinguishing necessity of function from exclusivity of mechanism.

Only after this sequence should a candidate be considered for stronger architectural treatment. Even then, the claim should specify **which handoffs and consumers require it** rather than declaring a universal representation for the whole organism.

---

## 20. Immediate work programme

The next empirical work should not expand the prose list. It should make the list harder to survive.

### 20.1 Freeze the present ledger as a baseline
The current fourteen candidate records provide a useful pre-observation snapshot. Future merges, demotions and additions should be versioned so that later knowledge cannot rewrite what was expected beforehand.

### 20.2 Complete Dataset-A / Stage-1 execution manifest
Freeze exact V3 configuration, seeds, episodes, latent recordings, freshness/validity filtering, transition and reachability labels, environment remappings, train/validation/held-out splits and go/no-go criteria before observing candidate-level results.

### 20.3 Begin with relations that have strong discriminating experiments
Transition topology, confidence/precision, branch/obtaining status and source/ownership are particularly useful because they generate distinct nuisance-controlled tests and failures.

### 20.4 Force candidate mergers
In particular:

- test `source_provenance` against `source_ownership`;
- test `branch_obtaining_status` against source + time + confidence;
- test `epistemic_update_commitment` against source + branch + confidence + update clocks;
- test `causal_control` against action-conditioned transition topology;
- test signed value against viability/preference + directional change;
- test salience/priority against locally recomputed surprise + value + need + confidence.

### 20.5 Preserve the language firewall
Do not use the linguistic candidate labels as supervision for the unlabeled narrowing condition. Language can be returned to after the relational structure recovered from the artificial organism has been frozen.

### 20.6 Preserve negative results
A demoted invariant is a scientific result, not a failed idea. The most valuable outcome may be discovering that several intuitively fundamental human categories are compressions of a much smaller machine-level basis.

---

## 21. Current best prediction

The present best guess is not that REE will reveal a miniature human grammar inside its latent spaces.

It is that heterogeneous cognitive consumers will place pressure on shared representations to preserve a **small relational skeleton**: continuity, succession, transition, source, obtaining status, reliability, control and viability, with richer concepts reconstructed from combinations of those relations.

If that occurs without candidate labels being supplied during training, it would support a powerful account of cognitive unity:

> a mind can remain one thing while its internal systems represent the world differently, provided the transformations between them preserve enough relational structure for the systems to keep talking about the same world.

If it does not occur, the failure will still be informative. We may discover that unity requires richer shared geometry, task-specific interfaces, dynamically negotiated contracts, or something closer to explicit message passing between semi-independent systems.

---

## 22. Central principle

> **The cognitive contract should contain no distinction merely because humans can name it. A distinction belongs only if heterogeneous cognitive systems repeatedly need it, cannot reliably reconstruct it from cheaper information, and fail in a specific way when it is lost.**

The goal is therefore not to find the most elegant list of cognitive primitives. It is to find the **smallest empirically defensible set of recoverable relations that allows heterogeneous representations to remain parts of one coherent cognition**.

That is the candidate basis to be attacked.