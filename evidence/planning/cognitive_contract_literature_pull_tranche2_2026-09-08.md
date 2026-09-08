# Cognitive contract literature pull — second convergence and pruning tranche

**Date:** 2026-09-08  
**Status:** research evidence / planning note; not a thought and not an architecture specification  
**Parent thought:** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md`  
**Parent intake:** `evidence/planning/thought_intake_2026-09-08_deriving_the_cognitive_contract.md`  
**Previous tranche:** `evidence/planning/cognitive_contract_literature_pull_2026-09-08.md`  
**Purpose:** continue the evidence programme before authoring Thought 2, with emphasis on value, goals, quantity, same/different, kind/part, spatial/relational structure, negation, possibility/counterfactual status, commitment and salience/relevance.

---

## 1. Interim result: the candidate list is beginning to stratify

The second tranche strengthens the cognitive-contract programme but weakens the idea that every recurrent cognitive category should become a primitive.

A more useful provisional stratification is emerging:

### A. Strong architectural-relation candidates

- entity continuity / token identity;
- equivalence / same-different / similarity;
- relational topology and transition structure;
- temporal order / persistence;
- provenance / source / ownership;
- representational status: actual, candidate, remembered, simulated, counterfactual, committed;
- causal / control relation;
- negation / absence as an operator over represented states.

### B. Strong recurring structures that are probably composite

- agency;
- goal / wanting;
- perception, memory, imagination and prediction as named modes;
- commitment.

These look increasingly reconstructible from combinations of the relations in A plus evaluative/control metadata.

### C. Strong agentic or embodied/ecological candidates

- value / valence / harm-benefit;
- magnitude / quantity.

Both recur very widely, but recurrence does not yet establish that either belongs to a substrate-neutral contract for every possible unified cognitive system. They may instead be near-inevitable for embodied agents that must regulate viability and choose among alternatives.

### D. Likely control metadata rather than semantic content

- confidence / precision;
- salience / relevance / priority.

These may need to survive translation without being part of the represented proposition itself. This is especially relevant to the existing REE gap around **translation confidence**.

This stratification is provisional. It is deliberately not promoted to architecture.

---

## 2. Same/different, kind and part: relation before category

### 2.1 Language-side evidence

Natural Semantic Metalanguage (NSM) proposes `THE SAME`, `OTHER`, `LIKE`, `KIND` and `PART` among its semantic primes. This is useful as an independently generated hypothesis family, not as proof.

- Goddard C. *The Natural Semantic Metalanguage Approach*. Oxford Handbook of Linguistic Analysis. DOI: 10.1093/oxfordhb/9780199677078.013.0018.
- Goddard C. *The Natural Semantic Metalanguage Approach*. Oxford Handbook of Linguistic Analysis. DOI: 10.1093/oxfordhb/9780199544004.013.0018.

A useful counterweight is Holden's Denesųłiné analysis, which found some proposed NSM primes — including `kind` and `part` — problematic to posit as abstract lexical universals in that language.

- Holden J. *Semantic Primes in Denesųłiné: In Search of Some Lexical “Universals”*. International Journal of American Linguistics 85(1), 2019. DOI: 10.1086/700319.

**Interpretation:** `same/different` and similarity appear stronger as relational candidates than `KIND` or `PART` as universal primitive labels. Kind and part may be learned/derived ways of organising equivalence, containment and causal structure.

### 2.2 Developmental evidence

Prelinguistic infants can learn and generalise same/different relations; reviews argue that this ability develops before and independently of language.

- Ferry AL, Hespos SJ, Gentner D. *Prelinguistic Relational Concepts: Investigating Analogical Processing in Infants*. Child Development 86, 1386–1405 (2015). DOI: 10.1111/cdev.12381.
- Ferry AL et al. / related review: *The origins of same/different discrimination in human infants*. Current Opinion in Behavioral Sciences 37, 69–74 (2021). DOI: 10.1016/j.cobeha.2020.10.013.

A 2026 Psychological Review synthesis argues that by the first birthday infants represent broad sortal kinds such as OBJECT, ANIMATE and AGENT, while more specific basic-level kinds are substantially shaped by language and pedagogy.

- Croteau J, Cheries E, Xu F. *The development of kind concepts: Insights from object individuation*. Psychological Review 133(1), 134–155 (2026). DOI: 10.1037/rev0000527.

Infant object work also shows representation of parts, but part representation is tightly tied to object perception and figure-ground structure rather than demonstrating an abstract universal PART operator.

- Hayden A et al. *Parts, cavities, and object representation in infancy*. J Exp Psychol Hum Percept Perform 37(1), 314–317 (2011). DOI: 10.1037/a0020987.

**REE implication:** add a distinct candidate family for **equivalence/similarity**, separate from token identity. Keep kind/part as possible derived relational structures until stronger independent evidence says otherwise.

---

## 3. Space looks increasingly like a training ground for relational topology

The most important spatial result is not that `ABOVE`, `BELOW`, `NEAR`, etc. should be copied into a cognitive contract. It is that spatial coding may supply a reusable computational scaffold for representing **relations, adjacency, trajectories and transition structure** in non-spatial domains.

Relevant literature:

- Epstein RA et al. *The cognitive map in humans: spatial navigation and beyond*. Nature Neuroscience 20, 1504–1513 (2017). DOI: 10.1038/nn.4656.
- Wikenheiser AM, Schoenbaum G. *Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex*. Nature Reviews Neuroscience 17, 513–523 (2016). DOI: 10.1038/nrn.2016.56.
- Halford GS, Wilson WH, Phillips S. *Relational knowledge: the foundation of higher cognition*. Trends in Cognitive Sciences 14(11), 497–505 (2010). DOI: 10.1016/j.tics.2010.08.005.
- Gershman SJ. *The Successor Representation: Its Computational Logic and Neural Substrates*. Journal of Neuroscience 38(33), 7193–7200 (2018). DOI: 10.1523/JNEUROSCI.0151-18.2018.

Artificial-agent work reaches a closely related conclusion from another route. Bisimulation-based representation learning deliberately collapses raw states that differ in task-irrelevant appearance while preserving transition/reward structure relevant to control.

- Zhang A et al. *Learning Invariant Representations for Reinforcement Learning without Reconstruction*. ICLR 2021 / arXiv:2006.10742.
- Kemertas M, Aumentado-Armstrong T. *Towards Robust Bisimulation Metric Learning*. NeurIPS 2021.
- Hansen-Estruch P et al. *Bisimulation Makes Analogies in Goal-Conditioned Reinforcement Learning*. ICML / PMLR 162 (2022).

**Interim conclusion:** specific spatial coordinates are likely embodied/ecological. **Relational topology / transition geometry** is a stronger architectural candidate.

---

## 4. Quantity and magnitude: very real, but probably not universal-contract by default

Quantity is one of the strongest examples of a distinction that is biologically ancient and cross-species, yet may still be the wrong grain for the cognitive contract.

### Evidence for recurrence

Human infants represent number abstractly and approximately before language.

- Spelke ES. *Number*. In *What Babies Know* (2022), OUP.

Non-human species across very different phylogenies discriminate numerosity; comparative reviews include primates, birds, fish and insects.

- Brannon EM. *Comparative Cognition of Number Representation*. Oxford Handbook of Comparative Cognition (2012).
- Lorenzi E, Perrino M, Vallortigara G. *Numerosities and Other Magnitudes in the Brains: A Comparative View*. Frontiers in Psychology 12:641994 (2021). DOI: 10.3389/fpsyg.2021.641994.
- Nieder A. *Neuroethology of number sense across the animal kingdom*. Journal of Experimental Biology 224 (2021).

Neural representations can be abstract across modality and presentation format.

- Nieder A. *The neuronal code for number*. Nature Reviews Neuroscience 17, 366–382 (2016). DOI: 10.1038/nrn.2016.40.

Deep neural networks can acquire numerosity sensitivity under some training regimes, but the literature also contains strong cautions against overclaiming spontaneous number sense from standard networks.

- Testolin A et al. *Numerosity discrimination in deep neural networks: Initial competence, developmental refinement and experience statistics*. Cognition (2020), PMID 31977137.
- NeurIPS 2020, *On Numerosity of Deep Neural Networks* (important negative/corrective result).

A 2026 Trends in Cognitive Sciences review explicitly separates discovered numerical content from the representational formats that cultures and learning construct.

- *The making of number: from content to representation*. Trends in Cognitive Sciences (2026). DOI: 10.1016/j.tics.2025.12.011.

### REE interpretation

Do not promote `NUMBER` to the contract merely because it is recurrent. A more plausible candidate is **ordered magnitude / more-less / comparison**, with exact numerosity as one ecological specialisation. Even that may be an agentic/embodied invariant rather than a requirement of all unified cognition.

---

## 5. Value, harm and salience must be separated

### 5.1 Value is a genuine representational variable

Neuroeconomics provides evidence for partially common value representations across different reward types, especially in ventromedial prefrontal/orbitofrontal regions.

- Levy DJ, Glimcher PW. *The root of all value: a neural common currency for choice*. Current Opinion in Neurobiology 22(6), 1027–1038 (2012). PMID 22766486.
- *Representation of Anticipated Rewards and Punishments in the Human Brain*. Annual Review of Psychology (2025/2026 review).

But `value` is not one simple thing. Reward processing decomposes into learning, incentive motivation and hedonic components, and value signals must be distinguished experimentally from outcome identity, salience and motor/autonomic consequences.

- Berridge KC. *From prediction error to incentive salience: mesolimbic computation of reward motivation*. European Journal of Neuroscience 35, 1124–1143 (2012). PMID 22487042.
- O'Doherty JP. *The problem with value*. Neuroscience & Biobehavioral Reviews 43, 259–268 (2014). PMID 24726573.

### 5.2 Salience is not value

Neuroscience explicitly dissociates value from salience. Value is signed with appetitive/aversive direction; salience or priority can increase for both strongly positive and strongly negative events. Goal relevance further modifies priority.

- Kahnt T, Tobler PN. *Reward, Value, and Salience*. In *Decision Neuroscience* (2017).
- Fecteau JH, Munoz DP. *Salience, relevance, and firing: a priority map for target selection*. Trends in Cognitive Sciences 10(8), 382–390 (2006). PMID 16843702.
- Rust NC, Cohen MR. *Priority coding in the visual system*. Nature Reviews Neuroscience 23, 376–388 (2022). DOI: 10.1038/s41583-022-00582-9.

### 5.3 Development and comparative evidence

Reward/approach learning is present early in development, while infant social-evaluation work suggests early sensitivity to helpful versus harmful action but also contains important associative alternative explanations.

- Hamlin JK, Wynn K, Bloom P. *Social evaluation by preverbal infants*. Nature 450, 557–559 (2007). DOI: 10.1038/nature06288.
- Margoni F, Surian L. *Infants' evaluation of prosocial and antisocial agents: A meta-analysis*. Developmental Psychology 54(8), 1445–1455 (2018). DOI: 10.1037/dev0000538.
- Scarf D et al. *Social Evaluation or Simple Association?* PLOS ONE 7(8):e42698 (2012). DOI: 10.1371/journal.pone.0042698.

Goal-directed action in animals is classically demonstrated by sensitivity to contingency degradation and outcome devaluation: behavior changes when the represented outcome becomes less valuable.

- Dolan RJ, Dayan P. *Goals and Habits in the Brain*. Neuron 80(2), 312–325 (2013). PMID 24139036.
- O'Doherty JP et al. *Learning, Reward, and Decision Making*. Annual Review of Psychology 68, 73–100 (2017).
- Recent review: *Making and breaking habits: Revisiting the definitions and behavioral factors that influence habits in animals* (2023/2024), PMC10842199.

### Interim conclusion

For REE, value/harm-benefit is strongly supported as a necessary **agentic viability currency**, but this tranche does not justify calling it a substrate-neutral primitive of every possible cognifold. Salience/relevance looks more like control metadata governing which represented relations receive resources.

---

## 6. Goal / WANT is probably a composition, not a primitive node

NSM includes `WANT`, and infant cognition contains early representations of goal-directed action.

- Sommerville JA, Upshaw MB, Loucks J. *The nature of goal-directed action representations in infancy*. Advances in Child Development and Behavior 43, 351–387 (2012). PMID 23205418.
- *Goal representation in the infant brain*. Developmental Cognitive Neuroscience (2014), PMC3898941.
- *Infants' Understanding of Object-Directed Action: An Interdisciplinary Synthesis*. Frontiers in Psychology 7:111 (2016), PMID 26903918.

Animal outcome-devaluation work likewise shows representation of action-outcome relations plus the current value of the outcome.

This suggests a possible decomposition:

```text
GOAL-like state
  ~= represented future/outcome state
   + positive/negative value or need relation
   + agent/action controllability
   + temporal/prospective relation
   + sufficient commitment/priority to organise action
```

This decomposition should be tested rather than assumed. For now, `goal` remains important contract content but is a weak candidate for an irreducible primitive.

---

## 7. Negation is more interesting than expected

NSM proposes `NOT` as a semantic prime. More importantly, recent developmental evidence is beginning to separate the concept of negation from the problem of learning its linguistic expression.

A 2026 study used international adoption to compare conceptually older children acquiring English with infant first-language learners. Both groups acquired English negation at similar points relative to their language development, supporting a **linguistic rather than conceptual bottleneck** for learning negation words.

- McDermott-Hinman A, Zimmerman S, Snedeker J, Feiman R. *Separating cognitive development from language development in the acquisition of negation using international adoption*. Journal of Experimental Psychology: General 155(7), 1629–1647 (2026). DOI: 10.1037/xge0001938; PMID 42241087.

A 2025 Cognition paper frames the live developmental question directly: infants may initially have restricted rejection/non-existence uses, or may have a broader negation concept whose linguistic mapping is difficult.

- Szabó E, Kovács ÁM. *Do early meanings of negation map onto a fully-fledged negation concept in infancy?* Cognition 254:105929 (2025). DOI: 10.1016/j.cognition.2024.105929.

**REE interpretation:** negation deserves promotion from a miscellaneous linguistic candidate to a serious contract-operator candidate. The most useful formulation may be **absence / non-obtaining / rejection of a represented relation**, rather than a language-like NOT token.

A future lesion assay is straightforward: preserve positive content but delete the ability to carry non-occurrence/absence across a boundary. Predicted failures include inability to reject hypotheses, represent missing expected events, or distinguish “not X” from absence of information about X.

---

## 8. Possibility and counterfactuality split into at least two levels

The developmental literature contains an apparent contradiction: infants and some non-human animals can act in ways consistent with tracking alternatives, yet preschool children often struggle on tasks requiring explicit representation of multiple possibilities.

A useful resolution distinguishes:

1. **minimal alternative-state representations** — multiple candidate trajectories/hypotheses can be generated and acted upon without an explicit modal concept;
2. **modal representations** — a representation is explicitly tagged as possible/necessary/impossible.

- Leahy B, Carey S. *The Acquisition of Modal Concepts*. Trends in Cognitive Sciences 24(1), 65–78 (2020). DOI: 10.1016/j.tics.2019.11.004; PMID 31870542.
- *Language as a mechanism for reasoning about possibilities*. Philosophical Transactions of the Royal Society B (2022), PMID 36314149.
- Ronfard S. *Possibility Judgments in Childhood: Is Uncertainty Monitoring the Missing Link?* Child Development Perspectives 19(4), 217–? (2025).
- Baumann L et al. *Understanding possibility through action: Young children's modal reasoning in agentive contexts*. Journal of Experimental Child Psychology 272:106594 (2026). DOI: 10.1016/j.jecp.2026.106594.

Counterfactual neuroscience likewise identifies representations of alternatives and their values rather than one monolithic counterfactual faculty.

- Armstrong MJ, Veleshnja O, Seghezzi S. *“I could have done otherwise”: The neural bases of counterfactual representations*. Neuroscience & Biobehavioral Reviews 180:106460 (2026). DOI: 10.1016/j.neubiorev.2025.106460.

Comparative future-oriented cognition is present in several taxa, but strong claims about explicit modal concepts remain contested.

- Clayton NS, Bussey TJ, Dickinson A. *Can animals recall the past and plan for the future?* Nature Reviews Neuroscience 4, 685–691 (2003).
- Osvath M, Martin-Ordas G. *The future of future-oriented cognition in non-humans: theory and the empirical case of the great apes*. Philosophical Transactions B 369 (2014), PMC4186238.

**REE implication:** the likely contract dimension is not a single `POSSIBLE` primitive. A better candidate is **representational branch/status**: obtaining versus candidate versus counterfactual versus committed, with explicit modal concepts potentially derived later.

---

## 9. Commitment is important, but probably a derived status relation

Commitment has a strong functional role: it stabilises expectations and action across changes in momentary preference. Psychological work on joint action deliberately seeks minimal, pre- or non-linguistic forms rather than defining commitment by explicit promises.

- Michael J, Sebanz N, Knoblich G. *The Sense of Commitment: A Minimal Approach*. Frontiers in Psychology 6:1968 (2016). DOI: 10.3389/fpsyg.2015.01968.
- *Every product needs a process: unpacking joint commitment as a process across species* (2022), PMID 35876205.
- *Just how joint is joint action in infancy?* review, PMID 25164940.

The literature suggests commitment is graded and depends on a structure involving agents, expected actions, mutual reliance, investment and persistence through changing incentives.

**REE interpretation:** `commitment` is unlikely to be a single irreducible cognitive primitive. It may be a higher-order status over an action/trajectory representation. Nevertheless, **commitment status must survive specific translations** in REE because the distinction between rehearsal and irreversible action is load-bearing (INV-012 / E3 commit gate).

This is a useful example of the difference between:

- a **contract primitive**; and
- a **derived contract field that is nevertheless mandatory at a particular boundary**.

Thought 2 should preserve that distinction.

---

## 10. Salience/relevance looks like priority metadata

Attention research increasingly describes selection in terms of **priority** rather than raw salience. Priority integrates bottom-up conspicuity with current goals/relevance and learned value.

This strongly suggests that salience/relevance belongs beside confidence/precision as **control metadata over representations**.

A cognifold translation may therefore need to preserve at least two distinct kinds of metadata:

```text
content confidence / epistemic precision
translation confidence / interface precision
priority / relevance / attentional weight
```

These should not be collapsed into value. Strongly harmful and strongly beneficial events can both be highly salient while having opposite value.

---

## 11. The narrowing-stack hypothesis now has a sharper mathematical form

The Information Bottleneck literature formalises the trade-off between compression and preservation of task-relevant information.

- Hu S et al. *A Survey on Information Bottleneck*. IEEE TPAMI 46(8), 5325–5344 (2024). DOI: 10.1109/TPAMI.2024.3366349; PMID 38358868.

Bisimulation and successor-representation work supplies a more agent-specific interpretation: raw state differences can be discarded if the representation preserves the **predictive, transition and outcome structure** required for future control.

This produces a stronger experimental prediction than “fewer nodes cause abstractions”:

> A narrowing latent hierarchy should preferentially preserve relations that remain simultaneously useful to multiple heterogeneous downstream consumers.

A single-task bottleneck can learn an arbitrary compact code. A multi-consumer bottleneck is much more constrained.

### Proposed experimental pressure set

Train a narrowing hierarchy without contract labels while requiring the compressed state to remain useful for:

- E1 persistent prediction;
- E2 rollout / counterfactual prediction;
- hippocampal indexing / replay;
- E3 trajectory scoring and commitment;
- harm/value evaluation;
- reconstruction into more than one engine-specific latent;
- behavior under changed surface features or schema remapping.

Then ask which relations remain decodable as width decreases.

### Strong held-out test

Derive candidate relations from the literature **before** interrogating the learned latent geometry. Freeze those candidates. Then test whether independently trained narrowing stacks recover equivalent relational structure across seeds, environments and body/schema changes.

The relevant success criterion is not one-to-one neuron correspondence. It is recoverable relational equivalence up to transformation.

---

## 12. Candidate coordinate families after tranche 2

This is a **research basis**, not architecture and not the contents of a message header.

### Core relational coordinates

1. **individuation / continuity** — same token across time/state;
2. **equivalence / similarity** — same/different/like relation among representations;
3. **relational topology / transition** — how states/entities are connected and can transform;
4. **temporal order / persistence** — before/after/current/trajectory relation.

### Representational-status coordinates

5. **provenance / source / ownership** — externally constrained, internally generated, self/other source;
6. **branch / actuality / commitment status** — obtaining, candidate, remembered, simulated, counterfactual, committed;
7. **causal / control relation** — actor, action, consequence and controllability structure.

### Operators

8. **negation / absence / non-obtaining** — a relation can be represented as not holding;
9. **comparison / ordered magnitude** — more/less, larger/smaller, stronger/weaker; exact number remains a possible specialisation.

### Agentic/evaluative coordinates

10. **value / valence / harm-benefit relation** — likely mandatory for viability-regulating agents, not yet shown substrate-universal;
11. **goal relation** — provisionally derived from future state + value + control + priority rather than primitive.

### Control metadata

12. **confidence / precision** — reliability of content/source/status;
13. **translation confidence** — reliability that a boundary preserved meaning;
14. **priority / relevance** — resource allocation/attention weight, distinct from value.

### Derived but boundary-critical

15. **commitment** — likely a structured status over a trajectory/action rather than a primitive, but mandatory at the rehearsal→action boundary.

This is a much smaller and more structured search space than the original 22-item inventory while preserving room for the evidence to delete, split or merge entries.

---

## 13. What this tranche rules against

The evidence now gives several useful negative constraints:

1. **Do not equate recurrence with fundamentality.** Quantity is highly recurrent and cross-species but may still be ecological/agentic rather than universal-contract.
2. **Do not equate salience with value.** The neuroscience explicitly dissociates them.
3. **Do not equate goal with value.** Goal-directed behavior additionally requires action-outcome and prospective structure.
4. **Do not equate possibility with explicit modal concepts.** Minimal alternative-state handling may precede modal representation.
5. **Do not equate commitment with a promise token.** Minimal commitment can be graded, implicit and pre-linguistic.
6. **Do not equate kind/part lexical recurrence with primitive relational status.** Cross-linguistic counterexamples matter.
7. **Do not assume a narrowing stack will discover useful invariants without multi-consumer pressure.** Bottlenecks preserve whatever their objective rewards.

---

## 14. Next evidence tranche before Thought 2

The programme is now mature enough that the next pass should be narrower, not broader.

Priority questions:

1. **Negation/absence:** does non-linguistic comparative cognition provide convincing evidence for representing non-occurrence, or is explicit negation unusually human/language-shaped?
2. **Equivalence vs identity:** are token continuity and same/different genuinely independent primitives or two operations over a single equivalence structure?
3. **Relational topology:** can the neural/AI literatures support a substrate-neutral formulation that unifies spatial maps, temporal sequences and abstract relations without becoming vacuous?
4. **Value:** does viability-regulating agency mathematically force a signed evaluative dimension, or can value be fully reconstructed from homeostatic prediction/error relations?
5. **Provenance/status:** can perception, memory, imagination and prediction be reconstructed experimentally from a smaller factorial basis?
6. **Metadata:** should confidence, translation-confidence and relevance be represented as separate channels, or can one general precision/priority calculus carry all three without characteristic failure?

Once those six questions have been pulled, Thought 2 can be written as a genuine evidence synthesis rather than an expanded brainstorm.
