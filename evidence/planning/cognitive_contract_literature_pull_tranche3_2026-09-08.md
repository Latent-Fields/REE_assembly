# Cognitive contract literature pull — third pruning tranche

**Date:** 2026-09-08  
**Status:** research evidence / planning note; not a thought and not an architecture specification  
**Parent thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`  
**Previous evidence:** `cognitive_contract_literature_pull_2026-09-08.md`, `cognitive_contract_literature_pull_tranche2_2026-09-08.md`  
**Purpose:** answer the six narrow questions left by tranche 2 before authoring Thought 2.

---

## 1. Executive result

The six-question pass materially narrows the hypothesis space.

The strongest new result is the discovery of a directly adjacent literature: **the relational bottleneck**. Webb et al. (2024) define a relational bottleneck as restricting information passed from perceptual systems to downstream reasoning systems so that downstream processing receives relations rather than the attributes of individual inputs. The authors give an information-theoretic formulation and review neural-network implementations that acquire abstract, symbol-like structure and systematic generalisation. Campbell & Cohen (CogSci 2024) further report that a relational bottleneck induced low-dimensional/factorised, approximately orthogonal feature representations without pre-specified symbolic primitives.

This is extremely close to — but importantly not identical with — the present REE hypothesis. Webb et al. **impose a relation-selective bottleneck**. The REE hypothesis asks whether a narrowing, multi-consumer hierarchy can **discover which relations need to survive** without being told the candidate relations. The relational-bottleneck architecture is therefore a valuable positive control, not the answer to be copied.

Key sources:
- Webb TW et al. *The relational bottleneck as an inductive bias for efficient abstraction*. Trends Cogn Sci 28(9), 829–843 (2024). DOI: 10.1016/j.tics.2024.04.001; PMID 38729852.
- Campbell D, Cohen JD. *A Relational Inductive Bias for Dimensional Abstraction in Neural Networks*. CogSci 2024 / arXiv:2402.18426.

The remaining questions yield these provisional answers:

1. **Negation:** non-occurrence/omission is represented far below human language, but this does not establish an abstract logical NOT primitive. Preserve *non-obtaining / expected-but-absent* before postulating negation as logic.
2. **Identity vs equivalence:** keep them separate for now. Identity is diachronic token continuity; equivalence/similarity is a relation that can generalise across different tokens. They may eventually reduce to one relation algebra, but current evidence supports distinct computational jobs.
3. **Relational topology:** can now be made non-vacuous as predictive/transition structure — adjacency, reachability and transition probabilities or their sufficient transform — independent of surface state attributes.
4. **Value:** viability does not force a primitive signed scalar value. Reward/value can be *derived* from homeostatic drive reduction, while viability theory can specify admissible states without ranking all viable states. The deeper candidate is a viability/preference constraint or ordering; valence may be a useful derived currency for embodied agents.
5. **Provenance/status:** memory, imagination and future prediction share substantial representational machinery, while perception/imagination discrimination is inferred from multiple cues. This strongly favours a factorial basis over primitive MEMORY/PERCEPTION/IMAGINATION/PREDICTION labels.
6. **Metadata:** confidence/precision and priority/salience are not one thing. Translation confidence is best treated provisionally as *confidence whose object is a translation*, rather than a new primitive. Priority may often be recomputed locally and should not be assumed contract-mandatory.

---

## 2. Negation: preserve absence/non-obtaining, not a language-like NOT token

The key comparative/neural evidence comes from **omission responses**. When an expected stimulus is withheld, nervous systems can generate temporally specific responses despite there being no external stimulus at that moment. A 2026 review synthesising omission work across species and modalities reports content-specific anticipatory and omission signals and argues that some paradigms reveal internally generated representations of the *missing expected content*.

- Yaron A et al. *“Nothing” Really Matters: What Omission Responses Reveal About the Predictive Brain*. Eur J Neurosci 63(10):e70566 (2026). DOI: 10.1111/ejn.70566; PMID 42210581.
- *Neural Substrates and Models of Omission Responses and Predictive Processes*. Front Neural Circuits (2022), PMID 35177967.

Reward-prediction-error work provides a particularly clean animal example: once reward is expected, omission produces a timed negative dopamine response at the moment reward should have arrived.

- Watabe-Uchida M, Eshel N, Uchida N. *Neural Circuitry of Reward Prediction Error*. Annu Rev Neurosci 40, 373–394 (2017). DOI: 10.1146/annurev-neuro-072116-031109.

This supports the existence of a representation equivalent to:

```text
expected(X, t) + observed_absence(X, t) -> violation / non-obtaining
```

It does **not** establish a domain-general logical operator with the full semantics of human `NOT`.

**Contract consequence:** rename the target from `negation` toward **non-obtaining / absence relative to a represented expectation**. A later developmental/language layer may abstract this into logical negation.

**Lesion refinement:** distinguish `unknown(X)` from `known-not-obtaining(X)`. If the boundary cannot carry that distinction, a receiver should confuse absence of evidence with evidence of absence and fail to register omitted expected events.

---

## 3. Identity and equivalence are related but should not yet be merged

Two independent literatures point to different jobs:

### Token identity / continuity

Infant object-individuation work asks whether an object now is the *same persisting token* as an object earlier. Spatiotemporal continuity is especially important early, with property and kind information incorporated later.

- Xu F. *Object individuation and object identity in infancy*. Acta Psychol (1999), PMID 10504878.
- Croteau J, Cheries E, Xu F. *The development of kind concepts: Insights from object individuation*. Psychol Rev 133(1), 134–155 (2026). DOI: 10.1037/rev0000527.

### Equivalence / same-different relation

Comparative work asks whether distinct stimuli stand in an abstract SAME/DIFFERENT relation and whether that relation transfers to novel items. Pigeons, monkeys and numerous other species can generalise same/different under appropriate training, although mechanisms and breadth of transfer vary.

- Wright AA, Katz JS. *Mechanisms of same/different concept learning in primates and avians*. Behav Processes 72, 234–254 (2006). DOI: 10.1016/j.beproc.2006.03.009; PMID 16621333.
- Wasserman EA et al. *Issues in the comparative cognition of same/different abstract-concept learning*. Curr Opin Behav Sci 37 (2021).
- Ferry AL, Hespos SJ, Gentner D. *Prelinguistic Relational Concepts*. Child Dev 86, 1386–1405 (2015). DOI: 10.1111/cdev.12381.

These operations can be dissociated conceptually:

```text
IDENTITY:      is A_t1 the persisting token A_t2?
EQUIVALENCE:   do A and B stand in a same/similar relation despite being distinct tokens?
```

A single deeper relation algebra may eventually implement both, but merging them now would erase a useful lesion distinction.

**Predicted double dissociation:**
- identity lesion -> duplicate/lost objects, broken credit/memory continuity;
- equivalence lesion -> intact token tracking but poor analogy, category transfer and schema reuse.

---

## 4. Relational topology can be stated precisely enough to test

The phrase `relational structure` risks becoming vacuous. The neural and computational literatures let us sharpen it.

Garvert et al. learned an *implicit graph* over object transitions. Hippocampal-entorhinal representational distances recovered the graph structure even though the stimuli were non-spatial and participants were unaware of the graph. The authors found the results compatible with predictive/successor-like distances rather than requiring Euclidean embedding.

- Garvert MM et al. *A map of abstract relational knowledge in the human hippocampal–entorhinal cortex*. eLife 6:e17086 (2017). DOI: 10.7554/eLife.17086.

A review of cognitive maps/graphs makes the same formulation explicit: a successor representation describes a state by the distribution of states likely to follow it, therefore encoding graph/transition structure.

- Behrens/graph literature: *Structuring Knowledge with Cognitive Maps and Cognitive Graphs*. Trends Cogn Sci (2021), PMCID PMC7746605.
- Gershman SJ. *The Successor Representation: Its Computational Logic and Neural Substrates*. J Neurosci 38, 7193–7200 (2018). DOI: 10.1523/JNEUROSCI.0151-18.2018.

The relational-bottleneck work provides the abstraction complement: restricting downstream flow to relations can induce efficient abstraction and generalisation.

**Operational contract candidate:**

> Preserve enough of the transition/adjacency kernel that the receiving engine can reconstruct behaviorally relevant reachability, ordering and structural equivalence, while allowing the surface coordinates of states to change.

Possible formal objects include:
- adjacency/reachability relation `A(i,j)`;
- transition kernel `P(s'|s,a)` or action-conditional analogue;
- successor representation `M = (I - gamma P)^-1` or learned approximation;
- lower-dimensional sufficient transform preserving the above for required downstream tasks.

This is much narrower than “preserve all relations.”

---

## 5. Value: viability/preference may be deeper than scalar valence

The strongest conclusion of this pass is **not** that value disappears. It is that a primitive signed `VALUE` scalar is not mathematically forced by the mere requirement to remain alive or coherent.

### Homeostatic reinforcement learning derives reward from regulation

Keramati & Gutkin define primary reward in terms of reduction of homeostatic drive. On their formulation, reward-seeking can be derived from the underlying objective of physiological stability.

- Keramati M, Gutkin B. *Homeostatic reinforcement learning for integrating reward collection and physiological stability*. eLife 3:e04811 (2014). DOI: 10.7554/eLife.04811; PMID 25457346.

A later review makes the construction explicit: a drive function maps homeostatic state to motivational drive and **reductions in drive are operationally reward values**; it also discusses survival constraints and active inference as alternatives/extensions.

- *Neurocomputational theories of homeostatic control* (2019), PMID 31395433.

### Viability theory needs a constraint set, not a total value ranking

Viability theory asks whether trajectories can remain inside an admissible set under available controls. In its basic form, it does not require every viable state to receive a signed scalar value or rank.

Therefore:

```text
viability constraint / preferred region
          ↓ possible derivation
signed drive change / value / valence
          ↓ possible use
tradeoff, motivation, learning, action selection
```

Active-inference accounts likewise require preferred outcomes/priors; they do not eliminate preference specification by mathematics alone.

- Pezzulo G et al. *Active Inference, homeostatic regulation and adaptive behavioural control*. Prog Neurobiol 134, 17–35 (2015). DOI: 10.1016/j.pneurobio.2015.09.001.
- Millidge B et al. *Whence the Expected Free Energy?* Neural Comput 33, 447–482 (2021). DOI: 10.1162/neco_a_01354.

**Contract consequence:** keep REE's harm/benefit/value machinery exactly where it is operationally needed, but for the substrate-neutral cognitive-contract search replace `VALUE is primitive` with a competing pair:

- H1: signed evaluative relation must be preserved;
- H2: viability/preference constraints are fundamental and signed value is a derived compression useful to embodied agents.

This is an excellent target for the narrowing-stack experiment because the two hypotheses make different predictions about what survives at the narrowest shared layers.

---

## 6. Perception, memory, imagination and prediction: a factorial basis is now the leading hypothesis

Three bodies of evidence converge here.

### Memory and future imagination share a constructive system

Remembering past events and imagining future events recruit a strongly overlapping core network and share constructive/recombinatorial processes.

- Schacter DL, Addis DR. *The cognitive neuroscience of constructive memory: remembering the past and imagining the future*. Phil Trans R Soc B (2007). DOI: 10.1098/rstb.2007.2087; PMID 17395575.
- Schacter DL et al. *The Future of Memory: Remembering, Imagining, and the Brain*. Neuron 76, 677–694 (2012). PMID 23177955.
- Mullally SL, Maguire EA. *Memory, Imagination, and Predicting the Future: A Common Brain Mechanism?* (2014), PMCID PMC4232337.

### Perception and imagination also share first-order machinery

Reality monitoring is needed precisely because imagery/perception overlap. Modern frameworks infer source from multiple sensory and cognitive cues rather than assuming a dedicated source label attached to content.

- Dijkstra N, Kok P, Fleming SM. *Perceptual reality monitoring*. Neurosci Biobehav Rev 135:104557 (2022). DOI: 10.1016/j.neubiorev.2022.104557.
- Dijkstra N et al. *A neural basis for distinguishing imagination from reality*. Neuron 113, 2536–2542.e4 (2025). DOI: 10.1016/j.neuron.2025.05.015.
- Shea N et al. *Why do we need imagination–reality monitoring?* Neuroscience of Consciousness (2026). DOI: 10.1093/nc/niag048.

### Consequence

The leading basis is no longer four primitive mode labels. A better factorial hypothesis is:

```text
CONTENT
+ GENERATION/SOURCE evidence      external constraint ↔ internal generation
+ TEMPORAL relation              past ↔ present ↔ future/non-temporal
+ BRANCH/OBTAINING status        obtaining ↔ candidate ↔ counterfactual
+ COMMITMENT/update status       rehearsal ↔ belief/action update
+ OWNERSHIP/AGENT source         self ↔ other ↔ ambient
+ CONFIDENCE in those inferences
```

Then familiar modes occupy regions/combinations in this space rather than being fundamental atoms.

This is directly testable: train probes for these factorial axes and compare their cross-engine/cross-context generalisation against probes for the coarse labels MEMORY/PERCEPTION/IMAGINATION/PREDICTION.

---

## 7. Confidence, precision, salience and priority should not be collapsed

Fleming's metacognition review distinguishes confidence/uncertainty representations from first-order task content and frames propositional confidence as an inference informed by models of both the world and one's cognitive system.

- Fleming SM. *Metacognition and Confidence: A Review and Synthesis*. Annu Rev Psychol 75, 241–268 (2024). DOI: 10.1146/annurev-psych-022423-032425.

Attention/salience theory gives a second dissociation. Parr & Friston distinguish attentional gain/precision from salience; Fecteau & Munoz argue that `priority` combines bottom-up salience and task relevance.

- Parr T, Friston KJ. *Attention or salience?* Curr Opin Psychol 29, 1–5 (2019). DOI: 10.1016/j.copsyc.2018.10.006; PMID 30359960.
- Fecteau JH, Munoz DP. *Salience, relevance, and firing: a priority map for target selection*. Trends Cogn Sci 10, 382–390 (2006). DOI: 10.1016/j.tics.2006.06.011.

**Provisional decomposition:**

- **content confidence / epistemic precision** — how reliable is this state/inference?;
- **translation confidence** — how reliable is my reconstruction of another engine's meaning?;
- **priority/relevance** — how much resource/action-selection weight should this state receive now?;
- **salience/sampling value** — how useful/urgent is further engagement with this source?

The first two may be the **same metacognitive operation with different objects**. Do not create a new primitive solely because one confidence estimate concerns a bridge.

Priority is more plausibly downstream control metadata. If a receiver can reconstruct value, uncertainty, goal relevance and urgency, it may recompute its own priority. Therefore priority should not be admitted to the universal contract until a lesion shows that recomputation is insufficient.

---

## 8. Revised minimal search basis before Thought 2

The evidence now supports a much sharper hierarchy.

### Tier 1 — strongest contract candidates

1. **token continuity / identity**
2. **equivalence / similarity**
3. **predictive relational topology / transition structure**
4. **temporal order / persistence**
5. **source / ownership / provenance**
6. **branch / obtaining / update status**
7. **causal-control relation**
8. **epistemic confidence / precision**

### Tier 2 — plausible operators or derived but broadly required structures

9. **non-obtaining / expected absence** (candidate precursor to negation)
10. **ordered magnitude / comparison**
11. **viability/preference relation** (candidate deeper basis for valence/value)

### Tier 3 — likely composites

- agency = source/ownership + action + prediction + causal/control;
- perception/memory/imagination/prediction = source + temporal + branch/update status + confidence;
- goal = prospective state + viability/value + controllability + priority;
- commitment = branch/update status + persistence/irreversibility + agent relation;
- exact number = magnitude/individuation specialisation;
- kind/part = learned abstractions over equivalence/topology/containment until proven otherwise;
- salience/priority = control policy metadata, possibly locally recomputable.

### Tier 4 — not yet justified as contract primitives

- human grammatical categories merely because they recur;
- named neuroanatomical modules;
- a universal scalar `VALUE`;
- a universal scalar `AGENCY`;
- explicit modal logic;
- a language-like NOT token.

---

## 9. Direct implication for the user's narrowing-stack hypothesis

The relational-bottleneck literature gives a decisive control condition for the experiment.

A strong design should compare at least four regimes:

```text
A. wide/shared-capacity control
B. width-only narrowing
C. imposed relational bottleneck (positive-control architecture)
D. unlabeled multi-consumer narrowing (REE hypothesis)
```

If D spontaneously approaches C's relational/factorised geometry while retaining better task-specific richness than C, that would support the claim that the cognitive contract can be *discovered* by compression pressure rather than prescribed.

If B does so as well, the special multi-consumer story is unnecessary.
If only C does so, the contract probably needs a stronger architectural inductive bias.
If none do so, the upper-stack intuition is wrong in its current form.

This is now sufficiently precise to pre-register without installing candidate invariant labels into training.

---

## 10. Readiness judgement

The evidence programme has crossed an important threshold. We are now ready to author **Thought 2: Candidate Cognitive Invariants** as an evidence synthesis rather than a brainstorm.

One separate artefact should accompany it: a pre-registered **narrowing-stack / relational-bottleneck assay design**. That assay belongs in evidence/planning rather than in the thought itself, so that the thought cannot silently mutate the experiment after results are seen.
