# Literature Summary: 2026-03-22_sd005_mirror_neurons_shared_representation_keysers2009

## Claims Tested

- `SD-005`

## Source

- Keysers C, Gazzola V (2009). *Expanding the mirror: vicarious activity for actions, emotions, and sensations*. Current Opinion in Neurobiology, 19(6): 666-671.
- DOI: `10.1016/j.conb.2009.10.006`
- URL: `https://www.sciencedirect.com/science/article/pii/S0959438809001585`

## Source Wording

Neuroimaging and single-unit recording studies in humans and macaques demonstrate that a network of cortical regions -- premotor cortex (BA 44/6), secondary somatosensory cortex (SII) / parietal operculum, and anterior insula -- activate both when an individual executes an action or experiences a sensation/emotion themselves, and when they observe another individual performing or experiencing the same thing. This 'shared manifold' or vicarious activation constitutes a common neural code for self and other. Importantly, the vicarious response during observation is typically modulated (not identical) to the response during first-person execution -- prefrontal circuits can suppress the full vicarious response to prevent confusion between executed and observed events. The authors argue this shared representation underlies social understanding by simulating others in one's own motor and sensory systems, without requiring a separate 'theory of mind' module for all social computation.

## REE Translation

**SD-005 (z_self/z_world split) -- mixed/disconfirming direction**:

The shared manifold finding creates a challenge for the strict z_self/z_world split proposed in SD-005. The argument from the Farrer & Frith (2002) entry is that insula encodes self-attribution (z_self candidate) and TPJ encodes external-attribution (z_world candidate). Keysers & Gazzola complicate this: the anterior insula -- one of the candidate z_self substrates -- also activates for observed others' sensations and emotions. If z_self's substrate is not dedicated to self-representation but partially shared with other-person representation, the encoder-head separation proposed in V3 cannot simply reflect an anatomically clean substrate split.

More precisely: the evidence suggests that the insula encodes a generalised simulation of the relevant state (pain, emotion, sensation) regardless of whether self or other is the source, with modulation by a gating/suppression mechanism during first-person execution. In REE terms, this is compatible with two architecturally distinct accounts:

1. **Fused account (disconfirming SD-005)**: z_self and z_world share a common encoder that is contextually modulated -- they are not architecturally separable but are dynamically distinguished by a context signal. This would make separate encoder heads for z_self/z_world an implementation choice that may not reflect the biology, and would predict cross-contamination without active suppression.

2. **Gated-separation account (compatible with SD-005 with modification)**: The overlap is managed by active prefrontal gating that suppresses the vicarious channel during first-person action. z_self and z_world can still be separated at the representational level, but the separation requires a gating mechanism (hypothesis tag, commit/simulate mode flag -- consistent with MECH-094) rather than being a static architectural property of separate encoder heads.

The gated-separation account is more parsimonious with the full literature (including the Farrer & Frith dissociation), but it means SD-005 V3 implementation needs to explicitly account for the suppression of z_world contamination during self-execution, and vice versa.

## Caveat

The mirror system literature is primarily about social cognition: understanding other people's actions, sensations, and emotions. z_world in SD-005 is predominantly about impersonal world-state modelling -- physical consequences, residue-field harm, environmental changes not caused by any agent. The shared manifold finding may not generalise to the self vs impersonal-world contrast. The disconfirming force of this evidence is strongest for SD-005's social-attribution component and weakest for its physical-world component. Additionally, the mirror neuron literature remains contested (Hickok 2009, Lingnau et al. 2009) -- the vicarious activation phenomena are robust, but their interpretation as a true 'shared code' vs a co-activation of functionally distinct representations is debated.

## Direction and Confidence

- `evidence_direction`: `mixed`
- `confidence`: `0.68`
