# What is the symbol layer actually doing? (Chaabouni et al. 2020)

## What the paper did

Chaabouni and colleagues took the question the emergent-communication field had been circling — do these invented languages have anything like the compositionality of natural language? — and did the unglamorous work of measuring it properly. They built new compositionality metrics by borrowing from the disentanglement literature in representation learning, then ran systematic sweeps over sender/receiver games with synthetic attribute-value input spaces of varying size and several agent architectures. Not a single demonstration; a parameter study. Three results came out.

First, given sufficiently large input spaces, emergent languages do naturally develop the ability to refer to novel composite concepts. Second — and this is the finding that matters most here — there is *no correlation* between how compositional an emergent language is and how well it generalizes. Third, compositionality does confer an advantage, but in an unexpected place: transmission. More compositional languages are more easily picked up by new learners, including learners whose architecture differs from the original agents'. Their summary is that compositionality does not arise from simple generalization pressure, but if a language chances upon it, it is more likely to survive and thrive.

## Why this is the most useful of the three ARC-009 entries

ARC-009 says language is a symbolic mediation and coordination layer. The two papers filed alongside this one establish that the layer can exist and can be decoded. This one constrains what it could plausibly be *doing*, and it does so by removing an assumption that I suspect is doing quiet work in the claim.

The natural story behind "symbolic mediation" is compositional: symbols mediate because they decompose a situation into recombinable parts, and that decomposition is what buys generality. Chaabouni et al. decouple those. Generalization to novel combinations happens — result one — but it does not happen *because of* compositional structure, since the two are uncorrelated across their sweeps. If a REE symbol layer were built and passed a generalization test, that would tell us nothing about whether it had the compositional structure the claim's phrasing implies. And conversely, an architecture that assumed a discrete channel plus a coordination pressure would yield structured symbols would be assuming precisely what these sweeps contradict: compositionality has to be chanced upon, not merely incentivised.

I have recorded this as mixed rather than weakens, and deliberately so. It does not say ARC-009 is wrong. It says the claim is currently under-specified in a way that would matter the moment someone tried to test it — because "symbolic mediation" could name at least two different mechanisms, and the evidence says they come apart.

## The constructive finding

Result three is the one I would carry forward. The payoff of compositional structure lies in transmission across agents, including architecturally heterogeneous ones. That is a *population*-level coordination benefit, not a dyadic one, and it is arguably a better fit to what ARC-009 means by a mediation **layer** than anything in the two dyadic papers. A layer, if the word is doing work, is something that persists across agent pairs and outlives any particular pair's negotiated code — which is exactly the property Foerster et al.'s per-task bespoke protocols lacked, and exactly what compositionality is here shown to confer. If ARC-009's layer is ever built, this suggests the experiment worth running is not "do two agents coordinate better" but "does a third agent, arriving later and built differently, pick the code up".

## Limitations

The inputs are synthetic attribute-value vectors, not rich world models and certainly not REE latent states, so the mapping to `z_theta`/`z_delta` slices or residue flags is a genuine stretch. More seriously, the headline null result rests on compositionality metrics that are themselves new instruments; positional disentanglement and its relatives have contested construct validity, and a null measured with a contested instrument deserves less weight than a null measured with a settled one. I have set confidence at 0.74 — above the Lazaridou entry despite this being the negative result, on the view that a well-measured null over systematic sweeps is stronger evidence about an architectural question than a positive demonstration on a single engineered setup.

The substrate caveat holds as for both sibling entries. ARC-009 is `substrate_conditional`: ARC-047's multi-agent environment is unbuilt and gated to v5, MECH-014's channel is a prose sketch, and nothing in ree-v3 implements either. All three entries in this directory bear on what a built layer would be expected to do. None is a measurement of REE.

## Provenance

ACL Anthology 2020.acl-main.407, pp. 4427–4442. DOI: https://doi.org/10.18653/v1/2020.acl-main.407
