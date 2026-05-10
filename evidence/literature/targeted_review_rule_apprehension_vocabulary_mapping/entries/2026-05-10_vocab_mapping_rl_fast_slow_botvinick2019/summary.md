# Botvinick et al. 2019 -- Reinforcement Learning, Fast and Slow

## What the paper did

Botvinick, Ritter, Wang, Kurth-Nelson, Blundell and Hassabis wrote a synthesis review for Trends in Cognitive Sciences arguing that the deep-RL sample-efficiency problem is solved in biological brains by two complementary fast-learning mechanisms layered on top of slow gradient-based RL:

1. **Episodic memory-based RL** -- stored episodes are retrieved and used to bootstrap rapid generalisation. Neural counterpart: hippocampal episodic memory.
2. **Meta-learning** -- slow training over a task distribution shapes a network into one capable of fast within-episode adaptation. Neural counterpart: prefrontal meta-RL (Wang 2018).

The two mechanisms are complementary and address different aspects of fast learning: episodic memory handles cross-episode generalisation when relevant past episodes exist; meta-learning handles within-episode adaptation when no relevant past episodes exist but the current task is from a distribution the agent has been trained on.

## Key findings relevant to the rule-apprehension vocabulary question

For Pull 4, the paper supplies the most parsimonious *cluster-level* organising structure available. The mapping to the proposed REE cluster is direct:

- **MECH-316 (cross-episode-regularity-extraction, hippocampal-monosynaptic-CLS-analog)** = *episodic-memory-based RL*. Hippocampal storage of past episodes; retrieval-based generalisation.
- **ARC-062 + MECH-318 (top-down rule application + rule-state abstraction)** = *prefrontal meta-RL*. Per Wang 2018 entry, these collapse into one mechanism.
- **MECH-317 (behavioural-pattern-compression, dorsolateral-striatum-analog)** = *option formation* (covered by the options-framework entries 1-3 in this pull).

The implication for cluster registration: the proposed sub-MECHs partition cleanly into two functional roles (episodic-memory vs meta-RL) plus the option-formation arm. That is a tighter organising structure than the current REE proposal of MECH-316 + MECH-317 + MECH-318 as three separate sub-mechanisms.

## How the findings translate to REE

Three concrete implications:

1. **R2 vocabulary inheritance**: the fast/slow split gives REE a clean way to talk about the bottom-up rule discovery pathway. MECH-316 = episodic RL; the meta-RL collapse = ARC-062 + MECH-318.

2. **R3 candidate REE divergence**: the fast/slow dichotomy may oversimplify REE's three-timescale picture. Pull 2 R3 identified online (within-episode), online-quiet-period (awake replay, Karlsson 2009), and offline (sleep consolidation, Stickgold 2013) as three distinct timescales. Botvinick 2019 collapses the latter two. Whether the third timescale is genuinely architecturally distinct or a refinement is open. If distinct, it is a KEEP-AS-IS for REE.

3. **R5 sequencing impact**: the fast/slow framing reorganises the MECH-316/317/318 cluster shape. The current Pull 2 proposal has three sub-MECHs as parallel children of ARC-064; the Botvinick 2019 framing reorganises them as MECH-316 (episodic-RL arm) + MECH-317 (option-formation arm) under ARC-064, with ARC-062 + MECH-318 collapsed under a "meta-RL" anchor that may be a separate cluster or absorbed.

## Limitations and caveats

The fast/slow dichotomy is a *useful organising structure*, not a settled empirical fact. Active debate remains on whether episodic-memory RL and meta-RL are really architecturally distinct (the Wang 2018 framework can in principle implement both via recurrent state + replay buffer; arguably the dichotomy is not fundamental). Adopting the vocabulary commits REE to a specific synthesis lineage.

The paper is also a review rather than original empirical work. The empirical anchoring is in the cited primary literature, not in the review itself.

The biggest caveat: the fast/slow framing may collapse REE's three-timescale structure into two. If REE has independently identified three distinct timescales (online + awake-replay + sleep-replay) and these are genuinely separate, that is a finer-grained timing structure than the Botvinick 2019 framework provides. R3 territory.

## Confidence reasoning

Scored 0.78. Source quality high (top-tier review venue, well-cited). Mapping_fidelity high (0.80) for the cluster-level fast/slow split. Transfer_risk low-moderate (0.30) because review papers transfer well as vocabulary-source documents. The paper feeds R2 (vocabulary inheritance: episodic-RL + meta-RL), R3 (three-timescale REE divergence candidate), and R5 (cluster shape reorganisation: MECH-316 + MECH-317 under ARC-064, ARC-062 + MECH-318 under meta-RL anchor).
