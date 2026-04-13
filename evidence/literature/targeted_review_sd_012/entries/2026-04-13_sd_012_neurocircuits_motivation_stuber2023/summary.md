# Neurocircuits for Motivation

**Entry:** 2026-04-13_sd_012_neurocircuits_motivation_stuber2023
**Claim tested:** SD-012 (homeostatic drive modulation of z_goal seeding)
**Evidence direction:** supports
**Confidence:** 0.70

---

## What the paper does

Stuber (2023) is a leading-edge review published in Science that synthesises the current state of circuit-level understanding of motivated behaviour, covering feeding, drinking, and threat-escape across rodent experimental work. The paper's central argument is that drive-state-specific neural circuits regulate VTA dopamine neuron activity to reinforce ongoing or planned actions that fulfil current homeostatic demands, and that multiple motivated behaviours -- despite differing in their peripheral drive signals -- share a common approach/avoidance architecture mediated through this dopaminergic substrate.

The review does not present new primary data but draws on a rich empirical base including optogenetic circuit mapping, fibre photometry during naturalistic behaviour, and pharmacological dissections of drive states from reward processing. The framing is notable for its attempt to unify the neuroscience of diverse motivations under a single circuit logic: drive-state-specific circuits (hypothalamic, hindbrain) converge on VTA dopamine as a common effector for reinforcing drive-appropriate behaviour.

## Key findings

The review's most architecturally relevant claim for SD-012 is the hierarchy it describes: peripheral homeostatic signals (energy, hydration, threat state) are encoded in drive-state-specific circuits that project to VTA-DA, which then modulates reinforcement of approach actions. This is a multi-stage drive-to-action pipeline, not a direct drive-to-behaviour mapping. The intermediate layer -- VTA-DA reinforcement -- is the gain-controlled amplifier that SD-012's effective_benefit formula formalises.

The commonality claim is also important: diverse motivated behaviours share VTA-DA as a common reinforcement substrate despite having different drive sensors. This supports SD-012's generality: the drive_level * drive_weight scaling of benefit signals is not food-specific but a general architectural principle for any homeostatic-need-driven goal agent. An REE agent that generalises beyond food to arbitrary goals (SD-012's intended scope) is following exactly the circuit logic Stuber describes.

The paper notes that interoceptive and sensory cues initiate drive-specific responses that are then aligned with motivational demand through dopaminergic reinforcement. This sensory-interoceptive-to-motor pathway corresponds closely to the REE signal chain: benefit_exposure (sensory contact with reward) + drive_level (interoceptive energy state) -> effective_benefit -> z_goal seeding -> trajectory selection.

## REE translation

SD-012's functional restatement specifies effective_benefit = benefit_exposure * (1.0 + drive_weight * drive_level), which is a multiplicative drive-gain model: the same benefit signal (proximity to resource) produces a larger seeding-effective signal when drive is high. The Stuber review provides the circuit justification: drive-state circuits modulate VTA-DA reinforcement of approach actions, which is functionally equivalent to amplifying the behavioural impact of reward-proximate states under high drive.

The generalisation from food/water to arbitrary goals is directly supported by Stuber's claim that diverse motivated behaviours share the VTA-DA reinforcement substrate. This is a critical architectural requirement for SD-012 in REE: the agent must not be a food agent with drive modulation bolted on, but an agent whose homeostatic drive architecture is general.

One nuance: Stuber's framework describes reinforcement (learning from past outcomes) while SD-012's effective_benefit drives z_goal seeding (prospective goal latent formation). These are related but not identical: reinforcement updates policy weights, while z_goal seeding biases trajectory generation toward drive-appropriate goals. SD-012's architecture adds a prospective goal-representation layer on top of the retrospective reinforcement learning framework that Stuber describes. This is not a conflict -- it is a complementary extension -- but the mapping requires one additional inferential step.

## Limitations and caveats

Stuber's review does not specify the computational form of drive-state modulation of VTA-DA gain. Whether the modulation is linear, sigmoidal, or piecewise is not resolved. The review is also confined to rodent empirical circuits; the VTA-DA-reinforcement pathway is well-established in rodents but the drive-state-specific modulation circuits (AgRP-to-VTA, LH-to-VTA) have less characterised homologues in primates. The mapping to an artificial agent's latent stack is inferential.

The paper does not address the within-trial dynamics of drive state -- how quickly drive level falls or recovers -- which is important for SD-012's energy_decay = 0.01/step and resource_respawn_on_consume implementations. Biological drive recovery is multi-timescale (immediate satiation signal, slow hormone recovery, delayed nutrient absorption); SD-012 models this with a simple linear decay, which is an acknowledged simplification.

## Confidence reasoning

Source quality is very high for a Science leading-edge review synthesising a mature empirical literature. Mapping fidelity is moderate: the drive-state->VTA-DA->reinforcement pathway maps well onto SD-012's causal chain but the translation from VTA-DA reinforcement to z_goal seeding requires the additional step of specifying that z_goal is the latent representation that VTA-DA-reinforced policy biases toward. Transfer risk is moderate as this is the standard neuroscience-to-computational-architecture domain transfer. Confidence 0.70.
