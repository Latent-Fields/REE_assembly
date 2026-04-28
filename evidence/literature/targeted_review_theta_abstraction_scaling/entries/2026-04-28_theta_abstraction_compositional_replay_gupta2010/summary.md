# Gupta, van der Meer, Touretzky & Redish 2010 — Hippocampal replay is not a simple function of experience

According to PubMed: Gupta, van der Meer, Touretzky & Redish. *Neuron* 65(5):695-705 (2010). [DOI 10.1016/j.neuron.2010.01.034](https://doi.org/10.1016/j.neuron.2010.01.034). PMID 20223204.

## What the paper did

The authors recorded from rat dorsal CA1 during a behavioural paradigm that gave them precise control over experience frequency on a task with two distinct learned sequences (A and B). They then asked what content sharp-wave-ripple replay events carry — specifically, whether replay simply reactivates recent or frequently-experienced trajectories, as the dominant theoretical account at the time predicted.

The answer is no, in three converging ways:

1. **Forward and backward replay of B occurred when rats had been performing A for more than 10 minutes.** Replay carries non-current content, not just recent experience.
2. **Replay of the non-local B was MORE frequent when B was infrequently experienced.** This inverts the simple "more experience → more replay" prediction.
3. **The hippocampus constructed never-experienced novel-path sequences.** Replay events covered trajectories the rat had never run; the construction was generative, not retrieval.

The authors interpret this as replay reflecting "all physically available trajectories within the environment, suggesting a role in active learning and maintenance of the cognitive map" — i.e. replay is compositional, generative, and structure-preserving, not a literal re-run of past experience.

## Why this matters for REE's question

This paper directly validates the architectural reading that hippocampal replay is *compositional* rather than experience-replicating. For REE this matters at two layers.

First, it supports the existing MECH-285 design choice. The sleep replay sampler is priority-weighted by staleness rather than by recency or frequency — closer to the Gupta 2010 inverse-experience-frequency result than to a naive replay-the-last-trajectory approach. Without an inverse-frequency or staleness signal, MECH-285 would over-weight recent experience and miss the architectural function the biology actually performs.

Second, it supports the compositional-recombination reading of MECH-292 and MECH-293. The ranked ghost-goal bank scores anchors by `wanting × goal-match × staleness × recoverability` rather than by recency. Waking ghost-goal probes seed CEM from anchors whose stored z_goal_snapshot cosine-matches the current z_goal — explicitly compositional, drawing from non-recent stored traces. Gupta 2010 grounds this as biologically faithful.

For the user's architectural prediction about theta-packaging-scales-with-substrate, Gupta 2010 contributes the compositional dimension. Theta-cycle replay isn't just "what happened" packaged into a cycle; it's "what *could* happen" — sequences that the cognitive map supports, whether or not they were experienced. As REE adds chunk / type / option substrates, the compositional capacity of replay extends naturally: the cognitive map now contains chunks and types and options as nodes, and compositional replay can construct sequences over them in the same way it constructs novel spatial paths in 2010.

## What it does NOT settle

The "novel paths" the paper observes are spatial trajectories within the rat's physical environment. Whether the same compositional capacity extends to abstract / type-level / option-level dimensions is a plausible architectural extension but not directly demonstrated. Bellmund 2018 (separate entry) provides the conceptual frame for cognitive maps spanning non-spatial domains; Schapiro 2017 (from the type-prototype lit-pull) provides the dual-pathway architecture that would let replay construct type-level sequences. But the direct empirical demonstration of "replay constructs novel type-level paths after type-substrate consolidation" is not yet in the literature.

The inverse-experience-frequency finding for non-current B is counterintuitive and may not transfer cleanly to a staleness-weighted REE sampler. MECH-285 weights anchors by accumulated staleness; Gupta 2010 weights non-current sequence reactivation by *inverse* recent experience. The two correlate (both downweight recently-experienced material) but the precise priority function may need refinement based on this signal.

## Confidence reasoning

I sit this at 0.85. Source quality 0.88 — *Neuron*, controlled experience-frequency manipulation, decisive single-unit methodology. Mapping fidelity 0.78 because the compositional / generative reading of replay maps directly onto MECH-285 / MECH-292 / MECH-293 architecture and validates the existing priority-weighted approach against naive recency-replay alternatives. Transfer risk 0.30 because the compositional-replay-spans-cognitive-map result transfers naturally to whatever cognitive map REE builds, including the type and option extensions planned for V4.
