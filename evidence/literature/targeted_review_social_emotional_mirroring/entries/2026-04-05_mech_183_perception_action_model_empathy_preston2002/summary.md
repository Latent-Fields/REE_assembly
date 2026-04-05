# Preston & de Waal (2002) -- Empathy: Its ultimate and proximate bases

**Claim tested:** MECH-183 -- z_beta leakage from attributed other-model into self affective processing

## What the paper finds

Preston and de Waal (2002) propose the Perception-Action Model (PAM) of empathy in a landmark theoretical synthesis with 40+ commentaries in Behavioral and Brain Sciences. The PAM's core proximate mechanism: "the perception of an object's state activates the subject's corresponding representations, which in turn activate somatic and autonomic responses." This activation is described as automatic and bottom-up -- not an inference step. The model predicts that familiarity and similarity with the other increase the coupling strength. Prefrontal modulation can then regulate or suppress this direct activation, producing the observed gradient from basic emotional contagion (purely automatic) through more complex empathic responses in primates. The PAM explains a wide range of behavioral phenomena including alarm calling, social facilitation, vicariousness of emotions, mother-infant responsiveness, and competitor modelling.

## Why this matters for MECH-183

MECH-183 claims that when the attributed other-model is sufficiently coupled (via OTHER_SELFLIKE tagging), the other agent's affective state activations leak directly into self's z_beta processing -- not as inference about the other, but as direct activation of the same affective states. This is the REE computational implementation of exactly the PAM mechanism. The key parallel is:

- PAM: perception of other's state -> direct activation of self's corresponding representations -> somatic/autonomic response
- MECH-183: other-model activation -> z_beta leakage -> self affective processing activated

The PAM's prediction that familiarity and similarity modulate coupling strength maps directly onto the OTHER_SELFLIKE tagging mechanism in MECH-183: tagging a closely coupled other agent would increase leakage coupling, consistent with the PAM's similarity/familiarity modulation.

## Where the PAM falls short of MECH-183

The PAM operates at the behavioral/psychological level and does not specify the computational substrate. MECH-183 makes a specific architectural claim: the leakage occurs at the level of a latent affective variable (z_beta) and is mediated by the attribution stream. The PAM cannot confirm this specific implementation. Additionally, the PAM's "corresponding representations" is ambiguous -- it could include inferential representations of the other's state that merely activate similar somatic responses, which would be a different mechanism from the direct-variable-leakage in MECH-183.

## Novelty implications

The PAM is the closest existing theoretical framework to MECH-183, and the two claims are closely parallel at the functional level. However, the PAM has never been formalized in a computational architecture with a specific latent variable (z_beta) and an attribution-stream coupling mechanism. The REE framing adds architectural specificity that the existing literature does not contain. MECH-183 is therefore PARTIAL in novelty: the functional description exists (PAM), but the specific computational implementation is novel.
