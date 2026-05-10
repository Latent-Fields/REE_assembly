# Friston, Rigoli, Ognibene, Mathys, Fitzgerald & Pezzulo 2015 — Active inference and epistemic value

[DOI](https://doi.org/10.1080/17588928.2015.1020053) · PMID 25689102 · *Cogn Neurosci* 6(4):187–214

## What the paper did

The operational instantiation of FEP for the explore-exploit dilemma. Agents are modelled as minimising the expected free energy of policies, which decomposes cleanly into two terms: extrinsic value (expected utility / reward, the standard RL objective) and epistemic value (information gain about the causes of valuable outcomes). The paper provides simulations on toy environments (T-mazes) showing that this framing reproduces both directed exploration (epistemic-value-driven) and softmax-style choice noise (which emerges as Bayes-optimal precision of policy beliefs). Crucially, the explore-exploit transition emerges naturally: when model uncertainty is high, epistemic value dominates and the agent explores; as uncertainty falls, extrinsic value takes over.

## Why this matters for ARC-065

This is the operational version of the structured-exploration arm. Where Friston 2010 (PMID 20068583) gives the unified-theory framing, this paper gives the explicit decomposition that REE could implement. Two key consequences for the cluster registration:

**R1 verdict reinforcement (both-channels-needed):** the active inference framework derives directed exploration (MECH-314) and stochastic decision noise (MECH-313) from the same optimisation principle, with softmax temperature as Bayes-optimal precision of policy beliefs. The two channels are not competitors but complementary terms in a single objective. This is the most theoretically satisfying answer to R1 and aligns with the empirical Wilson 2014 (PMID 25347535) both-channels finding.

**R4 verdict (continuous-AND-triggered hybrid):** epistemic value is computed continuously every tick from current model uncertainty, but its *dominance* over extrinsic value is triggered (active when uncertainty is high; recedes as uncertainty falls). This rejects the naive continuous-vs-triggered binary in favour of a continuous-presence-with-triggered-dominance reading. The MECH-312 dual-channel arbitration claim should accommodate this: ARC-065 is always running, but its weight on action selection rises and falls with model uncertainty.

## Limitations and confidence

Active inference is a specific theoretical framework that REE has not formally committed to. The paper's simulations are toy T-mazes; transfer to embodied open-ended grid-world REE is non-trivial. The Cognitive Neuroscience venue is lower-impact than NRN (paired with Friston 2010). REE should probably register the structured-exploration channel (MECH-314) without committing to active-inference-explicit instantiation — leaving the operational form open between active inference (Friston 2015), pragmatic intrinsic motivation (Schmidhuber/Pathak), and substrate-anchored novelty bonus (Wittmann 2008). Confidence aggregate 0.74.

## Failure signature it would falsify

If active inference's epistemic-value formulation is wrong about how biological agents arbitrate explore-exploit, any MECH-314 instantiation that uses information-gain-as-curiosity (vs novelty-bonus or learning-progress-as-curiosity) loses its theoretical grounding. The substrate-level prediction is testable: does the agent's exploration intensity track Bayes-optimal information gain, or does it track simpler proxies like novelty or learning progress?
