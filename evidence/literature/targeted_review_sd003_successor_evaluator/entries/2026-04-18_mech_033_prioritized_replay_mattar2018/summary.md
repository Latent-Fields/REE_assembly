# Mattar & Daw (2018). Prioritized memory access explains planning and hippocampal replay. *Nature Neuroscience*.

## What the paper does

Mattar and Daw set themselves a unification problem. The hippocampal replay literature had accumulated a long list of phenomena -- forward sweeps during planning, reverse replay after reward, replay content biased toward goal states, replay following a route before the animal has ever traversed it -- and these had been accounted for piecemeal, each paper producing a model that explained one set of observations and stayed silent on the others. The question was whether a single algorithmic principle could generate the whole family.

Their proposal is that replay is a form of prioritized memory access, and the priority function is the expected value of computation: which state-transition update, if performed now, would most improve the agent's future behavior? The striking property of this derivation is that forward replay emerges for one reason (propagate value from future rewards to current actions, i.e. planning) and reverse replay emerges for another (propagate value from just-observed rewards back along the recent trajectory, i.e. credit assignment). Same algorithm, different conditions, opposite directions. When they simulate this, the output matches a range of empirical replay statistics across multiple independent datasets -- directionality, content selection, frequency -- with no additional parameters.

## Findings

Two findings from the paper matter for the SD-003 successor question, and they matter a lot.

First: planning (evaluator mode, pre-action rollout scoring) and credit assignment (comparator mode, post-outcome attribution) are, in the Mattar-Daw framework, *the same operation* run over the same state-transition model, with the difference being which state's value is the source of the propagation and which direction the updates travel. Forward replay takes expected future value and pushes it backward through the transition model to compute what to do next. Reverse replay takes realized reward and pushes it backward through recent experience to update which actions were responsible. The underlying forward model is shared. It is the same neural substrate being read in different modes.

Second: the prioritization rule (expected value of computation) naturally predicts when the system switches modes. When there is anticipated future reward and action is needed, the system generates forward sweeps. When an outcome has just arrived and it differs from prediction, reverse replay runs. The switching is not a top-down flag; it falls out of which updates have the highest expected value.

## REE mapping

This paper is the piece of literature most directly relevant to the SD-003 successor's central architectural choice. The question -- should REE's evaluator circuitry and comparator circuitry share a forward model or run separate ones? -- has a clean answer in Mattar-Daw: one forward model, two modes, driven by a prioritization rule that makes the switching emergent rather than hardcoded.

For ARC-018 and MECH-033, the framework gives us not just biological precedent for forward-model-based rollouts but a principled algorithm for which rollouts to generate and in what order. For the SD-003 successor specifically, it argues that E2_harm_s can plausibly serve both modes -- pre-action evaluator (forward replay over harm-state transitions for planning) and post-action comparator (reverse replay for harm credit assignment) -- with the same learned harm-stream forward model. This would simplify REE's architecture considerably: one forward model per stream, run in two modes, rather than four separate modules.

For MECH-102 (violence as terminal error correction), the framework offers a natural failure-mode prediction. Terminal error correction in this vocabulary would be the state where the prioritized-replay system has found no low-energy-coordination path with positive expected future value -- the forward sweeps return only trajectories whose expected value is below threshold, and the system is forced into the high-energy tail of the action distribution. The Mattar-Daw formulation does not describe this directly, but its structure makes the prediction available.

## Where the mapping is imperfect

The theory is reward-based; the REE harm stream requires the analogous harm-based formulation (prioritize state-transition updates by expected reduction in future harm). The math is the same; the empirical validation is not there. Second, the Mattar-Daw framework assumes a unified state-transition model. REE's stream separation (SD-010, SD-011) commits to z_world and z_harm_s being distinct streams with distinct forward models; if each stream runs its own prioritized-replay process, the framework needs to be extended to handle parallel, stream-separated replay. The paper does not address this and offers no empirical constraint on whether biological replay is stream-separated.

## Confidence reasoning

Source quality very high (Nature Neuroscience, Mattar + Daw, landmark paper). Mapping fidelity unusually high for this review -- the paper formalizes exactly the "same substrate, different modes" question the SD-003 successor is trying to answer, and comes down on the side of shared substrate. Transfer risk lower than most theoretical-to-REE transfers because the reward-to-harm analogy preserves the mathematical structure: the theorem about prioritized memory access is about update-priority derivation, and the derivation goes through whether the target is reward or harm. Confidence 0.82 -- the single most useful paper in this wave for the central architectural question.
