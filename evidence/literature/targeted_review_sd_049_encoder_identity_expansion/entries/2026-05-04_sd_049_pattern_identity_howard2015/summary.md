# Howard et al. 2015 -- Identity-specific vs identity-general reward coding

## What the paper did

Howard, Gottfried, Tobler, and Kahnt manipulated both the *value* and the *identity* of appetizing food odors (banana, garlic) in a human classical-conditioning fMRI paradigm. They used multivariate pattern analysis (MVPA) on activity in lateral OFC and vmPFC to decode whether each region's response was identity-specific (which-outcome) or identity-general (how-valuable). The dissociation is clean: lateral OFC carries identity-specific predictive signals, vmPFC carries identity-general value signals. They also report parallel functional coupling pathways -- OFC to piriform cortex (the olfactory-identity pipeline) and vmPFC to amygdala (the value-and-emotion pipeline) -- consistent with two substrates carrying complementary information about expected rewards.

## Why I pulled it for SD-049

This entry is the cleanest published evidence that human OFC encodes identity-specific predictive representations that are dissociable from value-general representations elsewhere. SD-049's z_resource is supposed to carry exactly this kind of identity-specific signal: which type of resource the agent is encountering or pursuing, separate from how-valuable-it-is-right-now. If lateral OFC is the biological structure REE's z_resource maps onto, then the MVPA-decodable distributed pattern Howard et al. identified is the relevant biological precedent -- and that precedent leans toward option B's learned embedding or option C's hybrid (embedding substrate with identity readout).

The lateral OFC vs vmPFC dissociation is independently architecturally interesting. It suggests a Phase 2 design refinement: not just z_resource carrying identity, but a parallel z_value head carrying identity-general value, with distinct downstream wiring. This is more elaborate than what Phase 2 has scoped, but worth flagging -- if Phase 2's identity-aware z_resource fails to produce wanting≠liking dissociation in V3-EXQ-514, the parallel-substrate architecture this paper documents may be where to look next.

## What MVPA cannot adjudicate

MVPA decodes identity from distributed activity patterns, but it cannot tell us whether the underlying substrate is a labeled-line population or a distributed similarity-preserving embedding. Both architectures would yield decodable identity-specific patterns -- in the labeled-line case, the patterns just happen to have low overlap across identities; in the distributed case, the patterns have a similarity structure where types from the same superordinate category (consummatory: food, water) cluster closer than across-category types (consummatory vs novelty). MVPA can in principle distinguish these by looking at the cross-decoding pattern, but Howard et al. did not run that analysis.

So this paper is a *mixed* signal: it supports option B/C against option A (because MVPA-based identity decoding is most naturally read as distributed pattern coding), but it does not adjudicate decisively. The Ballesta-Padoa-Schioppa 2019 single-unit data is more decisive on the labeled-line question. Read together, the two papers suggest a hybrid: distributed MVPA-decodable substrate at the regional level, but with labeled-line single-unit organisation when you record at high enough resolution. That is exactly option C.

## Confidence and verdict contribution

Source quality is high (PNAS, Kahnt has continued to replicate; cross-tag with the more recent Liu-Kahnt 2024 paper retrieved in the same lit-pull batch). Mapping fidelity is strong because the experimental variable is precisely z_resource's variable. Transfer risk is moderate (human vs REE substrate). Aggregate 0.79.

This entry pushes the verdict toward option B or option C. Combined with the two Schapiro entries below, the distributed-substrate / hybrid case is well-supported. The labeled-line evidence (Quiroga, Ballesta-Padoa-Schioppa) supports option A's *readout shape* but not necessarily the substrate.
