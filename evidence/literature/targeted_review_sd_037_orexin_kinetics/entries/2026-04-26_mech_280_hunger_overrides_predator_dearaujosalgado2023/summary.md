# de Araujo Salgado et al. 2023 — hypothalamic toggling between food-seeking and self-preservation

## What the paper did

de Araujo Salgado and colleagues asked the behavioural arbitration question MECH-280 ultimately rests on: when a hungry animal sees a predator, what circuit decides whether it freezes or forages? They built a paradigm in which mice could choose between approaching food and remaining in shelter under acute predator presentation, and they varied caloric need across days. They then dissected the arbitration with cell-type-specific opto- and chemogenetics targeting the dorsal premammilary nucleus CCK cells (PMd-CCK), AgRP neurons of the arcuate, and their downstream targets in the bed nucleus of the stria terminalis (BNST), the lateral hypothalamus (LH), and the periaqueductal grey (PAG).

## Key findings relevant to MECH-280

Three results matter directly for the MECH-280 prediction. First, increased caloric need shifted the toggle: mice with greater hunger crossed into food-zone exposure under predator presentation that fully suppressed eating in sated controls. The transition was graded — there was no abrupt all-or-nothing switch — and depended on AgRP-pathway activity. Second, AgRP projections to the BNST and the LH were the route by which hunger potentiated food-seeking under threat; AgRP→PAG was not the bypass channel, but the LH was a relay. Third, predator presentation acutely inhibited AgRP firing, and PMd-CCK→PAG activation suppressed feeding under threat — so the freeze-versus-forage outcome was the resolution of two opposing population-level signals rather than a unidirectional hunger-wins rule.

This is essentially the behavioural dissociation MECH-280 names — drive-modulated raising of the freeze threshold so that, at high enough drive_level, the agent does not commit to freeze even under sustained threat — but characterised at the circuit level. The paper does not single out orexin within the LH; it characterises the broader hypothalamic-PAG arbitration of which the orexin / LH-PAG override projection is one instance.

## How this translates to REE

MECH-280 says theta_freeze_effective = theta_freeze_base × (1 + alpha_override × override_signal), with override_signal rising under sustained drive plus sustained threat. The paper supports the qualitative shape: (a) rising hunger does shift the freeze-versus-forage toggle, (b) the shift is graded rather than binary, (c) the circuit substrate runs through a hypothalamic node that converges on PAG, and (d) the shift can be perturbed bidirectionally by manipulating the upstream populations. The MECH-280 falsifiable prediction — that an agent with the override disabled remains frozen indefinitely while an agent with it enabled transitions at a drive-level threshold — is the experimental contrast this paper instantiates, with PMd-CCK / AgRP-pathway manipulation standing in for the override-on/off split.

## Limitations and caveats

The paper does not isolate the orexin contribution to the LH-PAG override. MECH-280 is named for orexin / peri-LC GABA → PAG specifically; this paper's manipulations are upstream of and parallel to that orexin channel, so its evidence pertains to the existence and behavioural shape of a hypothalamic-PAG override but not to the orexin scalar (alpha_override = 0.5, MECH-280's parameter) being the right gain. Two further caveats apply for transfer to REE: the paradigm uses acute, transient predator exposure rather than the prolonged sustained threat MECH-280 models, and the substrate is mouse rather than the conserved-mammal architecture REE assumes implicitly. Neither caveat is fatal — the foraging-under-threat arbitration is conserved across species — but the alpha_override scalar still has to be tuned by the SD-037 validation factorial rather than read off this paper.

## Confidence reasoning

I am giving this 0.82. Source quality is high (Neuron, cell-type-specific manipulations, replicated across paradigms). Mapping fidelity is high but discounted to 0.78 because the orexin channel is not isolated. Transfer risk is low-to-moderate (0.30) — the behavioural arbitration is conserved, but the precise gain on alpha_override is not constrained by this paper. The aggregate sits in the high-confidence band; this is the strongest direct anchor MECH-280 has, but it does not constrain the parameter.
