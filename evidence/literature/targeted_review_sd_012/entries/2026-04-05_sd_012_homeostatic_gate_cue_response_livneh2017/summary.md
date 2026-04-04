# Summary: Livneh et al. 2017 -- Homeostatic circuits gate food cue responses in insular cortex

**Entry:** 2026-04-05_sd_012_homeostatic_gate_cue_response_livneh2017
**Claim tested:** SD-012 (homeostatic drive modulation of goal seeding)
**Evidence direction:** supports
**Confidence:** 0.82

## Paper

Livneh, Y., Ramesh, R.N., Burgess, C.R., et al. (2017). Homeostatic circuits selectively gate food cue responses in insular cortex. *Nature*, 546, 611-616. DOI: 10.1038/nature22375

## Core finding

Using two-photon calcium imaging in awake, behaving mice (via microprism), Livneh et al. show that insular cortex neurons exhibit food-cue-biased responses during hunger that are selectively abolished under satiety. This is not a graded reduction but a selective suppression of cue-specific responses.

The gating is mediated by a defined circuit: AgRP (hunger) neurons -> paraventricular thalamus (PVT) -> basolateral amygdala (BLA) -> insular cortex. Chemogenetic activation of AgRP neurons in sated animals fully restores hunger-like food-cue response patterns in insular cortex, demonstrating the AgRP-to-cortex pathway is sufficient for drive-state-dependent cue gating.

## Relevance to SD-012

SD-012 proposes that drive_level gates z_goal seeding:
`effective_benefit = raw_benefit * (1.0 + drive_weight * drive_level)`

The Livneh et al. finding provides circuit-level mechanistic evidence for this principle:
- **Under satiety** (drive_level ~ 0): food-cue responses in insular cortex are abolished -- analogous to z_goal failing to seed
- **Under hunger** (drive_level ~ 1): food-cue responses are present and selective
- **Forced AgRP activation in sated animals**: restores cue responses -- analogous to forcing drive_level = 1

The paper is notable for showing gating of *cortical stimulus representations*, not just behavioral output. This is closer to the z_goal level (internal goal representation) than purely behavioral measures.

## Circuit pathway

AgRP neurons (arcuate nucleus) -> PVT -> BLA -> insular cortex

This circuit describes the biological implementation of what SD-012 captures as the drive_weight * drive_level term: a dedicated pathway by which need state amplifies the effective motivational salience of resource-relevant cues.

## Key caveats

- Insular cortex is primarily interoceptive; z_goal in REE is closer to a PFC/OFC planning-space latent vector. The mapping level differs.
- The paper demonstrates gating of sensory cue responses, not explicit goal representation formation (planned action sequences).
- Hunger-specific circuit; SD-012 is generic across need states.

## Evidence class

Circuit mechanism (in vivo two-photon calcium imaging + chemogenetics; Nature 2017).
