# Eccard, Liesenjohann & Dammhahn 2020 — Among-individual differences in foraging under perceived risk

According to PubMed: Eccard, Liesenjohann & Dammhahn 2020, *Oecologia* 194(4):621–34. [DOI 10.1007/s00442-020-04773-y](https://doi.org/10.1007/s00442-020-04773-y) (PMID 33141325, PMC7683444).

## What the paper does

Twenty-one common voles (*Microtus arvalis*) tested in artificial laboratory landscapes with manipulated perceived risk during feeding-in-patch and during travel-between-patches. Two food patches varied in perceived risk; ground cover was the manipulated variable. The authors measured feeding duration, food consumption, transitions between patches, and evenness of resource exploitation, separately for each individual across multiple risk conditions.

## Two key findings

1. **Risk-type dissociation**: voles distinguished risk during feeding from risk during travelling. High risk during feeding reduced feeding duration and consumption more strongly than risk while travelling. Risk during travelling modified the risk-during-feeding effects on between-patch transitions and on evenness of resource exploitation. Two distinct rules, two distinct policy components.

2. **Foraging personalities**: across all risk conditions, individuals differed *consistently* in when and how long they exploited resources and how much risk they accepted. Among-individual differences in foraging behaviour were associated with consistent patterns of resource exploitation that led to unequal payoffs in the same environment.

## Why this matters for R4 (tolerance-window calibration)

R4 asks what the appropriate acceptance window is for ARC-062's Phase 2 falsifier. Eccard et al's data give two distinct calibration implications:

1. **Across-seed variation is the predicted signature, not seed-convergence**. Real animals in the same population settle on different policies. ARM_1 ARC-062 across seeds should show *between-seed variation* in allocation matching the inter-individual spread Eccard reports. Seed-convergence to a single ratio in ARM_1 would be biologically anomalous — a sign that the discriminator + heads have collapsed across what should be policy-divergent initial conditions. The tolerance window for the acceptance threshold should specify a *range* of plausible allocations and a *minimum spread* across seeds, not a single mean.

2. **Risk-type dissociation is testable on SD-054**. The substrate has two risk types: risk during foraging (food-attracted hazards in forage zone) and risk during transit (transition between reef and forage zone). ARC-062's discriminator should reproduce the Eccard dissociation if it has correctly internalised the risk-type structure of the substrate. The Phase 2 falsifier should include a metric that distinguishes feeding-risk modulation from transit-risk modulation; PASS = the two manipulations move different metrics, FAIL = they move the same metric, indicating the discriminator collapses across risk-type cues.

## Why this matters for MECH-309

MECH-309 says that without a rule-apprehension layer, gradient descent finds the smoothest single regime. Eccard's data shows that even *real animals* have multiple regimes simultaneously expressed in a population — different individuals running different policies. The single-regime collapse MECH-309 predicts for parametric-policy learners is therefore a *more severe* form of monomodality than what biology exhibits: biology produces between-individual diversity even when within-individual policy is consistent. ARC-062's gated-policy + discriminator architecture should reproduce both within-individual context-dependence AND between-individual policy-diversity.

The architectural commitment for ARC-062's Phase 2 falsifier is therefore not just "ARM_1 produces context-dependent allocation" but "ARM_1 produces context-dependent allocation with substantial cross-seed variation". Both are necessary; either alone is insufficient.

## Mapping caveat

Common voles in artificial mesocosms is a controlled but small-scale system (n=21). The "foraging personality" framing implies that consistent inter-individual variation may have a substantial heritable / developmental component that is not captured by trial-by-trial gradient descent in ARC-062's joint training. The seed-variation analog in ARC-062 captures policy-divergence-from-different-initialisations but not heritable personality structure — partial mapping rather than full equivalence. Vole-to-fish transfer carries the usual species caveat.

## Confidence reasoning

Source quality 0.82 — solid *Oecologia* paper with controlled laboratory design and clear individual-level behavioural data. Mapping fidelity 0.78 — directly informs the tolerance-window question for the Phase 2 falsifier; the risk-type dissociation finding maps cleanly to SD-054's two risk types. Transfer risk 0.28 — vole-to-fish species transfer plus the heritable-vs-trained personality distinction. Confidence 0.79 reflects: solid empirical anchor for cross-seed variation as the predicted signature, with the personality-vs-trained-policy gap captured in `mapping_caveat`.

## Failure signatures for the cluster

1. **Seed-convergent allocation in ARM_1**: if ARC-062 weak reading produces no across-seed variation in refuge-vs-forage allocation, Eccard predicts this is a failure of policy-head differentiation. Real animals have consistent inter-individual variation arising from policy / personality differences, not just from state. Diagnostic: cross-seed coefficient of variation in ARM_1's `reef_visit_fraction` should match Eccard's reported among-individual spread within tolerance.

2. **Risk-type collapse**: if ARM_1 ARC-062 produces variation across seeds that does *not* track manipulated risk type (feeding-risk vs transit-risk), Eccard shows real voles distinguish these cleanly. ARC-062 should reproduce the dissociation. Failure to dissociate indicates the discriminator is collapsing across distinct risk-type cues — directly relevant to whether the multi-stream input (Pull A's R1 verdict) is being utilised.
