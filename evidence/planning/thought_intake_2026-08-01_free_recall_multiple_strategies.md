# Thought Intake: Free recall strategy pluralism and index-scaffold retrieval

**Source email:** `REE: this surely affects recall of policies/apprehended rules and bottom up perceptual builds.`  
**Email timestamp:** 2026-07-21T16:44:27Z  
**Processed:** 2026-08-01T23:07:39Z  
**Classification:** thought intake / architecture cross-check. Not a scored literature record. Not a V3 substrate task.  
**Registration:** NONE. No claims.yaml entries, experiment queue entries, or evidence-weighted literature records created.

---

## Executive Summary

Li et al. (2026) train RNNs with an episodic memory buffer on free recall and find that human-like recall patterns can arise from multiple mechanisms. Some trained models behave like Temporal Context Model variants, using drifting content/context dynamics. The strongest models instead discover an item-independent positional index code: list positions act as stable retrieval addresses, and content is bound to those addresses during encoding. The authors treat this as a computational analog of a memory-palace or method-of-loci strategy.

The paper is relevant to REE, but it should not be overclaimed. It is a computational modeling paper with behavioral comparison to human PEERS data, not direct hippocampal, dACC, or theta evidence. Its useful REE extraction is architectural: recall behavior is underdetermined by behavior alone; index-scaffold retrieval, temporal-context retrieval, semantic/content retrieval, and externally cued retrieval can all be rational in different task regimes.

This refines how REE should think about recalling policies, apprehended rules, and bottom-up perceptual builds. A single "memory search" mechanism is too blunt. REE likely needs task-conditioned retrieval modes: positional/index traversal when full ordered recall is the objective; content/context matching when flexible rule retrieval is required; and recency suppression when recent-state working memory would otherwise dominate the retrieval cue.

No immediate EXQ should be queued. The paper suggests future diagnostics for memory-mode gating and retrieval-cue competition, but the current V3 bottlenecks are substrate/readout competence issues, not an absence of this specific recall-strategy abstraction.

---

## Primary Source

- Li, M., Jensen, K. T., Zhang, Q., Lu, Q., and Mattar, M. G. (2026). **A neural network model of free recall learns multiple memory strategies.** *Nature Machine Intelligence*. https://doi.org/10.1038/s42256-026-01274-0
- Nature publication date: 2026-07-20.
- Full methods and figures checked from the bioRxiv preprint: https://doi.org/10.1101/2025.09.25.678592, version posted 2026-07-06. The preprint is not itself peer reviewed, but the article has a Nature Machine Intelligence version.
- Code availability: `https://github.com/Veritaria/rnn-free-recall`.
- Human comparison data: PEERS immediate free-recall dataset, public via the University of Pennsylvania memory lab.

---

## Scientific Summary

The model is a GRU "context module" plus a slot-based episodic memory module. During study, each item updates the recurrent hidden state and the resulting state is stored in memory. During response, the current hidden state queries stored memories by cosine similarity, retrieves one, and updates the state. The model is trained with advantage actor-critic reinforcement learning to maximize correct recalls, with penalties for repeated or wrong recalls. The task does not instruct a recall order.

Key findings:

- Trained models cluster into three strategies: a memory-palace-like strategy, a TCM-like forward strategy, and a TCM-like backward strategy.
- The memory-palace-like models show near-perfect forward recall and hidden-state trajectories dominated by item index rather than item identity.
- In a key-value memory variant, keys preferentially encode index while values preferentially encode identity. This is the cleanest implementation-level motif for REE: retrieval addresses and retrieved content can be separated.
- The memory-palace strategy is not simply incompatible with temporal context. The models still carry decaying item information and smooth temporal dynamics, but the stable positional scaffold dominates retrieval.
- Higher long-horizon reward weighting increases memory-palace adoption. Optimizing for the whole list favors index-scaffold retrieval over short-horizon recency solutions.
- Preserved working memory biases the model toward a backward/recency strategy. Flushing or resetting working memory suppresses recency and favors the memory-palace strategy.
- The index strategy is more robust to hidden-state noise than the TCM-like strategies, and noisy training environments increase the probability that models discover it.
- External temporal context shifts models toward TCM-like strategies when it is available as an input. If the same external context is present at both encoding and retrieval, it can itself become a location-like cue.
- Semantic item structure reduces reliance on memory-palace indexing: the model recalls semantically similar items together instead of following pure positional order.
- A conditional free-recall task, where retrieval must be guided by item features, eliminates the memory-palace solution even under settings that otherwise promote it.

The strongest scientific lesson is strategy pluralism. Temporal contiguity, forward recall, and recency effects are behavioral signatures, not mechanism identifiers. The same surface behavior can be produced by a drifting context code, an index scaffold, a semantic cue structure, or a mixture of them.

---

## Existing Repository Correspondence

| Repository asset | Correspondence | Verdict |
|---|---|---|
| `docs/architecture/e1.md` / **MECH-154** | E1 is already framed as an addressable associative manifold supporting pattern completion, traversal, and pointer-like addressing. The index-code result is computationally sympathetic to addressable retrieval, but it is not biological evidence for E1. | **Refines interpretation.** Addressing should not be collapsed into content drift. |
| `docs/architecture/e1.md` / **MECH-155** | MECH-155 claims that spatial navigation is a special case of general associative indexing. The memory-palace result is a direct computational analog of non-spatial sequence recall using location-like indices. | **Non-scored support by analogy.** Strong transfer risk. |
| `docs/architecture/e1.md` / **MECH-156** | MECH-156 links theta to sequential traversal across indexed representations. The paper supports the need for ordered traversal, but it does not measure oscillations and does not adjudicate theta. | **Scope refinement only.** No claim-confidence change. |
| `docs/architecture/approach_avoidance_symmetry.md` / **MECH-116** and **ARC-032** | The paper shows that preserved recurrent working memory can bias retrieval toward recency, while reset/noise can favor positional indexing. MECH-116 is about goal context maintenance, not list recall; this source warns that working-memory persistence is not always beneficial. | **Cautionary refinement.** Do not treat maintenance as globally good. |
| `docs/architecture/rule_apprehension_layer.md` / **MECH-338** | Cue-driven context-bound rule retrieval is already registered for socially scaffolded rule recall. The paper adds a computational caution: context cues, semantic cues, and positional indices can compete or substitute depending on task demand. | **Refines retrieval-mode gating.** |
| `docs/architecture/arc_063_candidate_rule_field.md` | Candidate rules have context tags and availability gates. The conditional-recall result maps to rule retrieval better than pure free recall does: policies/rules need content-based retrieval, not only ordered list replay. | **Useful design caution.** |
| `evidence/literature/targeted_review_mech_154_156_e1_manifold/` | Existing review already covers hippocampal indexing, cognitive maps, abstract spaces, and theta traversal. This source is incremental and computational, not a replacement for the biological review. | **Do not open a duplicate review.** |
| `evidence/literature/targeted_review_socially_scaffolded_rule_population/` | Tulving/encoding-specificity and Godden/Baddeley context-dependent recall are already present, including replication caveats. This paper provides a modern modeling complement: matching context can become a retrieval scaffold, while mismatched context can impair the strategy. | **Cross-link only.** |
| **MECH-260**, **SD-038**, **MECH-289** | The source shows that suppressing recency can unlock a non-recency retrieval strategy, but it does not localize this to dACC or hippocampal SWR. It is not evidence for dACC bias suppression or CEM anti-recency. | **Analogy only.** No governance change. |

---

## Architectural Implications

1. **Behavioral recall patterns are not mechanism-identifying.** Temporal contiguity and forward recall do not prove a TCM-like temporal-context substrate. A stable index scaffold can produce similar or better behavior. REE literature entries should avoid inferring mechanism from recall order alone.

2. **Retrieval address and retrieved content should remain separable.** The key-value model result is the cleanest REE-relevant primitive: keys can carry index/context/address information while values carry item or policy content. This is relevant to CandidateRule retrieval, ghost-goal ranking, and hippocampal anchor selection.

3. **Working-memory persistence has a tradeoff.** Persistent state is useful for maintaining goals and current context, but it can also over-weight the most recent item/action/rule. REE should distinguish "maintain the active goal" from "let recent state dominate memory search."

4. **Recency suppression is a mode-setting operation, not a universal bonus.** In this task, reducing recency enables whole-list positional retrieval. In content-based retrieval, that same positional strategy becomes suboptimal. This matters for MECH-260/SD-038 interpretation: anti-recency should be task- and value-conditioned, not a flat penalty.

5. **Policy/rule recall likely needs content-sensitive retrieval more than pure index traversal.** The user's email specifically flags policies, apprehended rules, and bottom-up perceptual builds. Those are closer to conditional free recall than to independent-item free recall: the agent usually needs the rule relevant to the current cue, not the next item in an ordered list.

6. **External context can act as either drift cue or stable locus.** If context drifts between encoding and retrieval, it pushes toward TCM-like temporal retrieval. If context matches across phases, it can become a location-like retrieval scaffold. REE's context tags should therefore record both context content and whether the context is expected to be reinstatable.

7. **Semantic structure competes with positional structure.** When items have semantic features, the model uses them. For REE, a strong semantic/rule abstraction should sometimes override sequence order, especially when retrieving a policy by applicability rather than reciting a stored chain.

---

## Existing Claims Strengthened

No existing claim receives scored evidence from this intake.

Non-scored, analogy-level support:

- **MECH-154 / MECH-155:** supports the plausibility of addressable/indexed retrieval as a general computational motif. The transfer is from artificial RNNs to REE architecture, not from neuroscience to REE.
- **MECH-338:** strengthens the design intuition that contextual cues can select among stored rules, but the paper is about word-list recall and does not involve social scaffolding or rule learning.
- **MECH-260 / SD-038 / MECH-289:** weakly supports anti-recency as a useful ingredient for escaping recency-locked retrieval, but provides no localization or biological substrate evidence.

---

## Existing Claims Weakened

No registered claim should be weakened.

The paper does weaken an over-broad reading that would treat any temporal-contiguity recall pattern as evidence for a single TCM-like mechanism. If any future REE note relies on that inference, it should be corrected: temporal-contiguity behavior is compatible with several mechanisms.

---

## Mechanisms Refined

No mechanism is directly changed. The refinement is a retrieval-mode vocabulary:

| Retrieval mode | Operational signature | REE analog |
|---|---|---|
| Positional/index scaffold | Stable, item-independent address; systematic forward traversal | E1/E3 indexed traversal, memory-palace-like anchor sequence |
| Drifting temporal context | Smooth state evolution; retrieval cued by nearby temporal states | context-dependent recall, recency-biased memory search |
| Semantic/content retrieval | Recall by item features or rule applicability | CandidateRule selection, policy recall under current cue |
| Matched external context | Encoding context reinstated at retrieval becomes a stable cue | context-tagged rule retrieval, safety/harm context reinstatement |
| Anti-recency reset | Recent working-memory state suppressed to avoid last-item dominance | dACC/hippocampal anti-recency motifs, but only task-conditioned |

This vocabulary should be used cautiously. It is a design lens, not a claim registration.

---

## Alternative Interpretations

- **Model artifact.** The memory-palace strategy may be favored by the specific RNN-plus-memory-buffer architecture, list length, reward function, and reset manipulation. It may not generalize to richer tasks or biological brains.
- **Task artifact.** Free recall of independent items rewards ordered exhaustive retrieval. REE policy recall is usually conditional, content-sensitive, and embedded in action. The conditional free-recall result is therefore more REE-relevant than the pure free-recall optimum.
- **Behavioral analogy only.** The PEERS comparison shows that human behavior can resemble the three model clusters, but it does not prove humans use the model's internal mechanisms.
- **Existing-claim absorption.** Most of the useful pieces already have homes: E1 indexing, MECH-338 cue retrieval, hippocampal anti-recency, and rule-field context tags. This source does not warrant a new standalone claim.

---

## Transfer Risks

- **Artificial model to REE:** The source is an optimized neural network model. Mapping it to REE is architectural analogy, not biological grounding.
- **Free recall to policy recall:** Recalling word lists is not the same as recalling policies, rules, or perceptual builds under action pressure.
- **No direct neural localization:** The paper does not show hippocampal, PFC, dACC, theta, or SWR mechanisms. It should not be used as localization evidence.
- **Optimization objective matters:** Whole-list reward and recency reset are load-bearing. Different reward structure shifts the strategy.
- **Human comparison is behavioral:** PEERS data anchor the behavioral patterns, not the internal codes.

---

## Candidate Experiments

None queued.

Possible future diagnostic, only after the relevant V3 memory/rule substrate is ready:

- Compare retrieval under three cue regimes: positional/index cue, semantic/content cue, and matched external-context cue.
- Add a recency-dominance manipulation: preserved current hidden state versus reset/noisy hidden state.
- PASS would not be "memory palace is best." PASS would be a mode-gating result: the system should shift retrieval mode when task demand changes.

This should not be appended to `experiment_queue.json` now. The current substrate bottlenecks around rule-policy competence and committed-action diversity are more basic than this retrieval-mode dissociation.

---

## Implementation Implications

No immediate implementation task.

If this idea recurs across future sources, the likely substrate direction is not a new memory module. It is a retrieval-mode gate over existing structures:

- `retrieval_mode = index_scaffold | temporal_context | semantic_content | matched_context`
- key/value or address/content separation for memory/rule retrieval;
- task-conditioned anti-recency strength rather than a flat recency penalty;
- diagnostics that record whether retrieval was driven by index, context, semantic similarity, or recent-state carryover.

This belongs after existing rule and hippocampal substrates can demonstrate basic non-degenerate retrieval.

---

## Governance Implications

No governance update is required now.

Claims.yaml was deliberately left untouched because:

- the paper is indirect computational-model evidence;
- another active session currently owns `REE_assembly/docs/claims/claims.yaml`;
- the relevant claim families already exist and do not need duplicate registration;
- scored evidence would overstate the source's biological authority.

Recommended future governance discipline: any literature entry using behavioral recall order as evidence should state whether the mechanism is actually identified. Behavioral contiguity alone should be treated as weak mechanism evidence unless paired with neural, lesion, representation-decoding, or targeted-ablation data.

---

## Cross-links

- `docs/architecture/e1.md`
- `docs/architecture/approach_avoidance_symmetry.md`
- `docs/architecture/rule_apprehension_layer.md`
- `docs/architecture/arc_063_candidate_rule_field.md`
- `docs/architecture/hippocampal_systems.md`
- `evidence/literature/targeted_review_mech_154_156_e1_manifold/`
- `evidence/literature/targeted_review_socially_scaffolded_rule_population/`
- `evidence/planning/thought_intake_2026-07-19_multiple_relational_graph_organisations_hippocampal.md`
- `evidence/planning/thought_intake_2026-06-06_contextual_memory_allocation_gate.md`

---

## Overall Recommendation

Preserve this as a thought intake. Do not create a new claim, queue an experiment, or change confidence scores.

Use the paper as a caution against single-mechanism readings of recall. For REE, the actionable abstraction is retrieval-mode gating: the right retrieval cue depends on whether the agent is trying to reproduce an ordered sequence, retrieve a context-bound rule, search by content, or avoid a recency trap.
