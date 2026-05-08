# The neurophysiological bases of emotion: an fMRI study of the affective circumplex (Posner, Russell et al. 2009)

## What the paper did

Posner, Russell and colleagues (Human Brain Mapping 2009) ran fMRI in ten subjects who rated emotion-denoting words along two dimensions: valence (positive vs negative) and arousal (high vs low). The contrast of interest was BOLD signal correlated with each dimension separately, testing the circumplex model's prediction that two underlying neurophysiological systems subserve these dimensions.

## Key findings relevant to the SD-014 question

Two distinct neural networks mediate the two dimensions. Valence ratings correlated with insula and lateral PFC. Arousal ratings correlated with parahippocampus and dorsal anterior cingulate. These networks are separable: subjects who rated a word as low-valence-and-high-arousal (e.g. "rage") did not produce the same BOLD pattern as subjects who rated a different word as high-valence-and-high-arousal (e.g. "ecstasy"). The two-dimensional circumplex is reflected at the neural level.

For SD-014 this is the *psychometric foundation* for the 5th-channel proposal. The circumplex model implies that affect is at minimum two-dimensional: valence × arousal. A single-axis valence representation (like SD-014's current 4-component vector along the wanting / liking / harm / surprise axes) collapses one of these dimensions. High-arousal-positive (excitement) and low-arousal-positive (calm contentment, satisfaction) cannot be distinguished by valence amplitude alone — they need an arousal dimension.

REE has z_beta as the arousal-modulating latent (MECH-093). One reading is that z_beta + the existing valence channels already constitute a 2D representation. The other reading is that z_beta modulates timing (heartbeat rate) rather than carrying a representation of *anticipatory positive arousal at this location* — which is what VALENCE_EXCITEMENT would carry as a residue-field write. The circumplex literature supports the second reading: arousal is a representational dimension of affect, not just a global state modulator.

## How this maps to REE

The architectural implication is that VALENCE_EXCITEMENT (high-arousal-positive) and VALENCE_DREAD (high-arousal-negative) would bring SD-014 into alignment with the two-dimensional circumplex. The existing channels are valence-specific (positive: wanting, liking; negative: harm; reactive: surprise) but do not represent the arousal dimension at the residue-field level. The circumplex model predicts that representational adequacy requires both dimensions, not just one.

A counter-reading: REE could keep the residue field one-dimensional and use z_beta + valence-channel-amplitude jointly to represent arousal at consumer sites (e.g. MECH-205 surprise-gated replay could weight by z_beta_arousal × VALENCE_WANTING). That would be cheaper but more error-prone (consumers would have to know to do the joint read at every site).

## Limitations and caveats

The circumplex model is a psychometric framework derived from self-report data, not a strict neuroanatomical claim. The fMRI mapping is robust at the network level (multiple studies show similar valence-arousal dissociation) but the specific regions vary across paradigms. The paper does not arbitrate between "two channels" vs "one channel modulated by arousal scalar" as architectural choices for a computational model.

## Confidence reasoning

0.72. Solid source, clear support for the 2D representation principle. Lower than the Knutson MID papers because the mapping is more architectural than mechanistic — Posner 2009 motivates representational adequacy rather than the specific channel addition.

Source: PubMed via PMID 18344175. [DOI](https://doi.org/10.1002/hbm.20553).
