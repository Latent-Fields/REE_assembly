# Crowell et al. 2016 — Refuge distance and concealment in sympatric herbivores

According to PubMed: Crowell, Shipley, Camp, Rachlow, Forbey & Johnson 2016, *Ecology and Evolution* 6(9):2865–76. [DOI 10.1002/ece3.1940](https://doi.org/10.1002/ece3.1940) (PMID 27069587, PMC4803802).

## What the paper does

Comparative behavioural ecology in sagebrush-steppe with two sympatric rabbit species: pygmy rabbit (*Brachylagus idahoensis*, small obligate burrower, sagebrush specialist) and mountain cottontail (*Sylvilagus nuttallii*, larger habitat generalist, does not rely on burrow refuges). Both were offered food patches varying in concealment cover (terrestrial vs aerial) and distance from a burrow refuge. The authors measured patch-selection preferences across multiple manipulations.

## Two species, two policies

The experiment surfaced a clean dissociation. Both species preferred concealment over its absence, but they preferred *different* kinds of concealment: pygmy rabbits preferred terrestrial concealment (cover from below — relevant for terrestrial predators that hunt rabbits at ground level); mountain cottontails preferred aerial concealment (cover from above — relevant for raptors). Only pygmy rabbits preferred food patches closer to their burrow refuge; mountain cottontails — being habitat generalists not reliant on burrows — instead traded off terrestrial concealment for visibility to detect approaching terrestrial predators.

The authors interpret the species difference as reflecting *different perceived predation risks*: each species has internalised the predator regime that matters for its body size and ecology, and weights its policy accordingly.

## Why this matters for R4 (refuge-distance gradient)

SD-054's reef substrate exposes a continuous refuge-distance gradient through its 5×5 normalised Manhattan-decay scent kernel. ARC-062's discriminator should weight this gradient when valuing forage-zone patches, biasing forage-zone score downward as a function of distance from reef. Pygmy-rabbit-style "closer-is-better" is the predicted refuge-substrate-dependent behaviour for an obligate-refuge-using agent; mountain-cottontail-style "concealment-elsewhere-can-substitute" is the alternative policy when refuge is not load-bearing.

For ARC-062 + SD-054 specifically, the agent is a single instance facing a single substrate — there is no "second species" comparison in the experimental design. But the species-difference anchor is informative for cross-seed variation: different gated-policy initialisations may produce different effective policies, with some seeds settling on pygmy-rabbit-style refuge-tracking and others on mountain-cottontail-style concealment-substitution. The Phase 2 falsifier ARM_1 might profitably surface this as a positive prediction test (across-seed variation in refuge-distance sensitivity), joining the Eccard 2020 within-population variation anchor.

## Why this matters for MECH-309

MECH-309 says strict gradient descent collapses to a single regime. Crowell's species-difference data is *not* a within-species personality finding (that's Eccard 2020); it is a between-species architectural finding — different evolutionary lineages have produced different solutions to the same risk-vs-resource trade-off in the same environment. The biological message: the optimal policy is not unique, and which policy gets crystallised depends on the agent's structural commitments (body size, refuge dependence, sensory modality) interacting with the substrate. ARC-062 weak reading at the score_bias level can produce a single solution; ARC-063 strong reading's distributed `CandidateRule` field is the architecture that explicitly accommodates *multiple* coexisting valid policies. Pull B does not arbitrate this; it surfaces the question.

## Mapping caveat

Sagebrush-steppe rabbits and coral reef fish operate in fundamentally different ecological regimes — mammalian terrestrial herbivore facing aerial and terrestrial predators, vs teleost aquatic mid-trophic-level facing reef-resident piscivores. The architectural reading — refuge proximity gradient as a continuous policy variable — transfers across taxa; the specific quantitative ratios do not. Body size and species-specific anti-predator strategy are highly relevant. For SD-054, the agent is one instance of one architecture; the species-comparison anchor is informative for cross-seed variation in ARM_1 more than for within-instance calibration.

## Confidence reasoning

Source quality 0.78 — solid *Ecology and Evolution* paper with comparative behavioural ecology design, two-species n adequate. Mapping fidelity 0.68 — herbivore-vs-fish ecology is a substantial transfer step; the gradient-of-distance principle transfers but specific calibration does not. Transfer risk 0.40 — mammalian-burrow-refuge mechanisms differ from fish-coral-refuge mechanisms in detail. Confidence 0.74 reflects: useful refuge-distance gradient anchor for SD-054's spatial structure with a high-transfer-risk caveat captured in `mapping_caveat`.

## Failure signature for the cluster

If ARC-062 weak reading produces refuge-distance preference that is *insensitive* to substrate spatial variation — e.g., reef proximity does not influence foraging-patch choice in ARM_1 — Crowell predicts this is a failure of spatial-context coupling. Real refuge-using animals weigh refuge proximity directly into patch valuation; ARC-062 should reproduce this if reef proximity is correctly wired into `z_world`. Diagnostic: regress ARM_1's `reef_visit_fraction` against agent distance from reef across the episode; PASS = monotone relationship; FAIL = invariant patch-choice across the spatial gradient, indicating the discriminator is not gating on reef-proximity.
