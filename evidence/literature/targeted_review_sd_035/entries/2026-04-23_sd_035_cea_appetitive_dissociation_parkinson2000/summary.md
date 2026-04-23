# Summary: Parkinson et al. 2000 — CeA Drives Appetitive Pavlovian, BLA Does Not

**Source:** Parkinson, Robbins & Everitt (2000). *Dissociable roles of the central and basolateral amygdala in appetitive emotional learning.* The European Journal of Neuroscience 12(1): 405–413. [DOI: 10.1046/j.1460-9568.2000.00960.x](https://doi.org/10.1046/j.1460-9568.2000.00960.x)

## What the paper did

Parkinson and colleagues bilaterally lesioned either the CeA (central nucleus) or the BLA (basolateral area) in rats using excitotoxic agents and tested appetitive Pavlovian autoshaping — a paradigm in which animals approach a lever that predicts food delivery, even though lever presses are not required to obtain food. Sham-operated controls and lesion groups received standard training until asymptotic approach responding, then underwent extinction. Additional control groups were tested for general locomotion and sensory processing to rule out non-specific effects. Separate experiments with dorsal and ventral subiculum lesions served as hippocampal control groups.

## Key findings

CeA lesions robustly impaired Pavlovian autoshaping: CeA-lesioned rats showed markedly reduced conditioned approach (lever touching/entry) to the food-predictive CS compared to shams. BLA lesions produced no significant impairment of autoshaping performance. Dorsal and ventral subiculum lesions also had no effect, confirming that hippocampal processing is not required for this form of simple appetitive Pavlovian conditioning.

The dissociation is notable because it occurs in a purely appetitive, not aversive, context. CeA is commonly associated with fear and defensive behaviour. This paper demonstrates that CeA's mode-prior function extends across valences: it is required for motivational invigoration by conditioned stimuli regardless of whether the UCS is rewarding or aversive.

## REE mapping

SD-035 registers CeAAnalog as a domain-general salience-to-mode-prior stage: it receives z_harm_a (the harm-affective latent) but its output — mode_prior — biases SalienceCoordinator toward the harm-relevant operating mode. The Parkinson 2000 result provides an important boundary condition on this architecture: the CeA mode-prior function cannot be implemented as a *harm-only* gate. CeA operates whenever a conditioned stimulus signals motivationally significant outcomes, including appetitive ones.

This means CeAAnalog should respond to z_harm_a as a *threat-weighted* input — but its mode_prior emission should be architecturally capable of operating for any salient conditioned cue, not just harm cues. The selective_bias_harm design (where mode_prior only fires for z_harm_a above threshold) is therefore a simplification that will need to be revisited if SD-035 is extended to include appetitive conditioning contexts in the REE environment.

The hippocampal independence finding (subiculum lesions no effect) is also architecturally relevant: it confirms that CeA's mode-prior function does not require hippocampal memory retrieval for simple Pavlovian cue-conditioning. This supports SD-035's design placing CeAAnalog *upstream* of the HippocampalModule in the SalienceCoordinator pipeline, rather than downstream or in a hippocampal feedback loop.

## Limitations and caveats

Excitotoxic lesions remove CeA and BLA entirely for the life of the experiment — the dissociation is between presence and absence, not between different levels of modulatory activity as SD-035 implements. The extent to which a non-trainable arithmetic CeAAnalog (additive log-odds bias) recapitulates the plasticity-dependent aspects of CeA conditioning is an open question.

The autoshaping paradigm is simple, single-cue, and food-reinforced. REE's SalienceCoordinator integrates across multiple simultaneous mode inputs; whether CeA's role scales to multi-cue, multi-valence environments as SD-035 requires is not directly tested here.

## Confidence

0.72. Clean double-dissociation paper, solid method, from the Robbins/Everitt group (same group whose 2003 review is also in this directory). Moderating factors: appetitive-to-aversive generalisation and the irreversibility of the lesion method versus SD-035's modular add-on architecture.
