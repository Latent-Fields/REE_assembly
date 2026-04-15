# Neural correlates of causal attribution in social situations: who is to blame?

**Source:** Seidel et al. (2009), Social Neuroscience. DOI: 10.1080/17470911003615997

## The core question

Before we can hold an agent responsible for harm, something in the mind must first resolve a prior question: was this actually that agent's doing? MECH-072 proposes that REE should implement a foreseeable-harm gate -- a discriminator that asks, at the moment harm-residue might be written, whether the agent could plausibly have caused and foreseen that harm. Seidel and colleagues used fMRI to ask what the biological version of that discriminator looks like.

## What they did and found

Thirty healthy participants lay in an fMRI scanner reading sentences describing everyday social events -- positive events (you won a prize) and negative events (your friend was hurt) -- and judged whether the main cause was internal (self) or external (someone or something else). This is a verbal, retrospective judgment task, not a real-time action task. But it is perhaps the most direct available window into the neural system that partitions causal ownership of outcomes.

The dissociation was anatomically clean. Internal (self) attributions selectively activated the right temporoparietal junction (TPJ). External attributions recruited a left-lateralised network: left TPJ, precuneus, superior and medial frontal gyrus. This fronto-temporoparietal network is consistent with a system that must model another agent's perspective (what the external cause did and why) while maintaining a distinct channel for self-referential causal attribution.

More striking for MECH-072 was the striato-cingulate signature for self-serving attribution direction: attributing positive events internally and negative events externally -- the classic self-serving bias -- specifically activated dorsal striatum and dorsal anterior cingulate. This suggests that the brain's attribution gate is not a neutral Bayesian discriminator. It is modulated by valence, and there is a reward-related system that may bias which channel gets written.

## What this means for the discriminator-gate design

MECH-072's gate is a learned discriminator on (z_world_delta, is_agent_caused) pairs. The Seidel finding provides biological grounding for the existence of such a discriminator: the brain does maintain separate computational channels for self-caused and externally-caused attribution of outcomes, implemented in a fronto-temporoparietal circuit with striato-cingulate modulation. The right TPJ as a hub for self-attribution is consistent with REE's z_world residue channel being indexed to the agent's own causal footprint.

The striato-cingulate involvement also carries a cautionary note. In biological systems, this gate appears to be valence-modulated -- the organism tends to attribute harmful outcomes to external causes. If REE's discriminator were similarly biased, it would systematically undercount agent-caused harm. MECH-072's explicit foreseeable-harm threshold (a factual judgment, not a self-serving one) is precisely the architectural correction for this biological failure mode.

## Caveats and transfer risk

The paradigm is verbal and retrospective. Attribution was a deliberate explicit judgment about fictional scenarios, not a real-time write gate operating during action-outcome sequences. The mechanisms for rapid, implicit, action-contingent attribution are almost certainly different from the circuits engaged here. The mapping to MECH-072 is at the level of functional analogy -- the brain maintains a discriminator between self-caused and externally-caused outcomes -- not mechanistic identity. The transfer from verbal social cognition to embodied reinforcement learning is a real gap.
