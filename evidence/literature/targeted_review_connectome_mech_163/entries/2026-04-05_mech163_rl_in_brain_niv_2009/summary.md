# Niv 2009 -- Reinforcement Learning in the Brain: MECH-163 Mapping

**Source:** Niv, Y. (2009). Reinforcement learning in the brain. *Journal of Mathematical Psychology*, 53(3), 139-154. DOI: [10.1016/j.jmp.2008.12.005](https://doi.org/10.1016/j.jmp.2008.12.005)

---

## What the Paper Does

Niv 2009 is the canonical review establishing the neural implementation of reinforcement learning (RL) theory, with particular focus on the temporal difference (TD) prediction error framework and its correspondence to dopaminergic signalling. The paper traces the development from psychological conditioning theory through computational RL to neural substrates, culminating in a rigorous account of how the brain implements key RL algorithms.

The central empirical link established in the review is between TD prediction errors and phasic dopamine signals in the VTA and SNc. Schultz's electrophysiological work (reviewed and synthesised) showed that dopamine neurons fire not to rewards themselves but to reward-predictive cues (after learning) and are suppressed when expected rewards are omitted -- the signature of a prediction error signal. Niv systematically shows how this corresponds to the delta signal in TD learning.

The review distinguishes model-free RL (TD, Q-learning, SARSA) from model-based planning (dynamic programming over an internal environment model), establishing that both exist in the brain and serve complementary functions. Model-free learning is attributed to the dopamine-striatum axis; model-based planning is attributed to prefrontal cortex. This anatomical dissociation is treated as a principled architectural feature arising from the different computational properties of the two approaches.

## Key Findings for MECH-163

The critical findings for MECH-163 are:

1. **The SNc/VTA -> striatum axis implements TD/model-free learning**: phasic DA encodes the TD error delta = reward + gamma*V(s') - V(s). The habit system in REE (SNc/dorsal-striatum) is directly grounded in this mechanism.

2. **Model-free systems learn cached values, not world models**: TD algorithms store Q(s,a) or V(s) values that represent expected cumulative reward from a given state/action. These values do not encode the transition structure of the environment. When the environment changes (new contingencies, new harm consequences), the cached values become inaccurate and the system has no mechanism to detect this without new experience. This is the computational basis for MECH-163's claim that the habit system cannot attribute harm across novel contexts.

3. **Model-based planning requires an internal model**: Niv reviews dynamic programming approaches where the agent maintains T(s, a, s') (transition model) and R(s, a) (reward model) and computes values by simulating forward. This is what makes goal-directed action sensitive to immediate devaluation -- the agent can re-compute values through the model without retraining.

4. **Both systems coexist in the brain**: Niv notes that while model-free learning is efficient, it is rigid, and that the brain maintains both systems. The model-based system can override model-free choices in novel or changing contexts.

## REE Mapping to MECH-163

The REE habit system (SNc/dorsal-striatum) implements TD/model-free learning as described by Niv: it caches S-R associations via DA prediction error, makes approach efficient in familiar environments, and is the appropriate system for well-practiced resource acquisition. The inability of this system to attribute harm across novel contexts follows directly from the absence of a world model: without T(s, a, s'), the system cannot simulate what would happen if it took a harmful action in a new context.

The REE planned system (E3 hippocampal) implements model-based planning: it maintains a world model (in z_world, the harm/benefit residue field) and computes action values by simulating trajectories. The hippocampal contribution (which Niv treats as primarily episodic memory rather than action planning) is the REE extension: long-horizon harm/benefit trajectory evaluation requires hippocampal terrain representation, not just PFC action-outcome contingencies.

## Limitations and Confidence Reasoning

Niv 2009 focuses primarily on the model-free/TD arm of the dual-system architecture. The model-based planning arm receives less theoretical development relative to later literature. The hippocampal contribution to planning is not the focus of the review. The paper predates the clearer experimental demonstrations of the dorsomedial/dorsolateral striatum dissociation that Balleine & O'Doherty 2010 provide. The harm-attribution dimension of MECH-163 is not addressed. Confidence: 0.78.

*Based on article available via PubMed (PMID: 18926527) and Princeton University publication repository.*
