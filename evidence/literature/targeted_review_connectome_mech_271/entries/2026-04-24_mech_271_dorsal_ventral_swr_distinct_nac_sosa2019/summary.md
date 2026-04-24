# Sosa, Joo & Frank (2019) -- "Dorsal and Ventral Hippocampal Sharp-Wave Ripples Activate Distinct Nucleus Accumbens Networks"

**Neuron** 105(4):725-741.e8. [DOI](https://doi.org/10.1016/j.neuron.2019.11.022). PMID 31864947.

*(According to PubMed.)*

## What the paper does

Sosa and colleagues recorded simultaneously from dorsal CA1, ventral CA1, and the nucleus accumbens (NAc) in rats performing an appetitive spatial task, and analysed how NAc firing was locked to SWRs originating in each hippocampal region. The key design choice is that dorsal and ventral CA1 generate their own SWRs, and those SWRs are typically asynchronous -- which lets the authors compare the NAc consequences of each source within the same animal and the same behavioural session, avoiding the confounds that separate-animal or separate-task designs would introduce.

Two results carry the paper. First, the NAc neurons that are activated (or inhibited) during dorsal-HC SWRs are a largely non-overlapping population from the NAc neurons activated during ventral-HC SWRs. These are distinct consumer ensembles, not the same population with different latencies. Second, the dorsal-HC-activated NAc subset is strongly enriched for neurons with task- and reward-related tuning; the ventral-HC-activated subset is not. The authors conclude that dorsal- and ventral-HC->NAc replay constitute "distinct channels of mnemonic processing" in the NAc, with the dorsal channel specialised for spatial-task and reward information.

## Findings relevant to MECH-271

MECH-271 is the claim that the hypothesis tag (MECH-094) is implemented as differential downstream routing of replay content, rather than as a shared-channel flag that downstream consumers must decode. Anchored replay, in this scheme, preferentially reaches consolidation-relevant consumers (subiculum-EC-neocortex, SD-033a lateral-PFC analog, viability-map writers); probe replay preferentially reaches affective-tagging and novelty-tracking consumers (BLA, NAc). The falsification condition for MECH-271 as an architecture is that downstream consumer populations are not cleanly separable at the source level -- that all replay is broadcast and consumer selectivity is done downstream by individual consumer populations filtering what they read.

Sosa et al. are the cleanest available falsification test, and they confirm the architecture rather than falsifying it. Different hippocampal source populations route to genuinely distinct NAc consumer populations, and those distinct consumer populations carry different functional tuning. This is the routing-architecture existence proof MECH-271 needs.

What Sosa et al. do *not* do is test the anchored/probe distinction directly. Their dissociation axis is dorsal/ventral, not anchored/probe. The relationship between these axes is an open question: MECH-271 does not claim that anchored replay is dorsal CA1 and probe replay is ventral CA1. What Sosa et al. establish is the more general architectural fact that HC->NAc replay supports source-specific routing with distinct downstream consumer populations. Given that infrastructure, MECH-271's claim that anchored vs probe is *one of* the source-side distinctions that engages differential routing becomes much more plausible than it would be if NAc were a single functional target.

## How it translates to REE

The translation has two steps. Step one is the routing-architecture step: "HC->NAc supports source-specific routing to distinct consumer populations" -- this is what Sosa et al. demonstrate and is exactly what MECH-271 asserts as an architectural shape. Step two is the functional-labelling step: "anchored and probe rollouts, as REE defines them, are one of the source-side distinctions that engages this routing infrastructure." This second step is not tested by Sosa et al., and remains an REE-side commitment that future V3 experiments would need to validate.

For REE's V3 substrate implementation, the lesson is architectural rather than quantitative. If MECH-271 is right, the HippocampalModule should not just tag rollouts as anchored or probe; it should publish them to different downstream consumer channels, and the consumers (SD-033a lateral PFC, BLA analog, viability-map writer, NAc curiosity tracking) should be wired to listen to their appropriate channels. Sosa et al. show that such a routing infrastructure exists in the biology; the V3 substrate decision is whether to mirror it.

## Limitations and caveats

The dorsal/ventral dissociation is not the anchored/probe dissociation, and the paper does not speak to the latter. The specific claim "anchored replay comes from dorsal CA1 and probe replay from ventral CA1" would be too strong an inference. MECH-271 is compatible with anchored vs probe being a cross-cutting distinction that operates within each of the dorsal and ventral channels, or being orthogonal entirely.

The task domain is spatial appetitive behaviour with reward; the reward-selective tuning of the dorsal-HC-activated NAc subset is measured in a context where reward is a primary behavioural variable. Generalising to REE's z_goal and z_harm_s streams, which are not literally reward in Sosa's sense, is a definitional step.

Only three regions are recorded. MECH-271's full routing hypothesis involves subiculum-EC-neocortex, lateral PFC, BLA, NAc, and fornix-Papez. Sosa et al. address only the HC->NAc arm. The other arms need their own evidence (the existing Jadhav 2016 entry addresses HC->PFC; Girardeau 2017 addresses HC->BLA).

## Confidence reasoning

Source quality is near-maximal: Neuron, Frank senior author (the authority on HC replay routing), genuinely difficult triple-site simultaneous electrophysiology with rigorous analysis. Mapping fidelity is 0.80 -- the highest among the MECH-271 entries -- because the paper directly demonstrates the routing-to-distinct-consumer-populations architecture that MECH-271 asserts. Transfer risk is low for the routing architecture itself (generic claim about hippocampal connectivity, demonstrated in rat, likely conserved in higher mammals) and moderate for the anchored/probe-onto-source-populations mapping (REE-side commitment not tested by the paper). Overall confidence 0.84 -- this should be the primary MECH-271 anchor for the routing architecture, with Jadhav 2016 as the HC->PFC evidence and Girardeau 2017 as the HC->BLA content-selectivity evidence.
