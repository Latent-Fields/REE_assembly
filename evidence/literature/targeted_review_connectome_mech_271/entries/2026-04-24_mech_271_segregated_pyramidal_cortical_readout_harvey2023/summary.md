# Harvey, Robinson, Liu, Oliva & Fernandez-Ruiz (2023) -- "Hippocampo-cortical circuits for selective memory encoding, routing, and replay"

**Neuron** 111(13):2076-2090.e9. [DOI](https://doi.org/10.1016/j.neuron.2023.04.015). PMID 37196658.

*(According to PubMed.)*

## What the paper does

Harvey and colleagues reject the premise that CA1 pyramidal cells are a homogeneous population and test what happens when anatomical identity of those cells is treated as a first-class variable. They record simultaneously from CA1 and multiple cortical targets in rats performing spatial-and-reward tasks, analyse the assembly structure of CA1 activity with attention to which pyramidal subpopulation each assembly belongs to, examine what content each subpopulation encodes, and trace which cortical targets selectively read out each subpopulation. The final step is to examine how replay events coordinate activity across specific hippocampo-cortical pairs.

The summary result is that cellular identity matters, strongly. Segregated CA1 pyramidal-cell subpopulations encode either trajectory-and-choice-specific information or reward-configuration information -- these are mostly disjoint subpopulations with distinct functional specialisations. Their activity is selectively read out by different cortical targets; a subpopulation with trajectory tuning reaches one set of cortical consumers, a subpopulation with reward tuning reaches a different set. And during replay, distinct hippocampo-cortical assemblies coordinate the reactivation of complementary memory representations, rather than all cortical targets reading a single shared replay broadcast.

## Findings relevant to MECH-271

MECH-271 asserts that the hypothesis tag (MECH-094) is implemented architecturally as differential downstream routing rather than as a source-side flag that all consumers must decode. The architectural shape MECH-271 proposes is: the hippocampal source organises rollouts into typed channels; each channel reaches a selected subset of consumers; consumers read only their own channel. The key falsification target is the alternative that replay is broadcast and all consumers receive all content.

Harvey et al. falsify the broadcast alternative at the cellular level. CA1 is not a single source; it is a collection of content-typed subpopulations whose outputs reach selected cortical consumers. Different hippocampo-cortical assemblies coordinate the replay of different content. This is the architectural fact MECH-271 depends on, established in rat by rigorous multi-region electrophysiology.

The cellular-level organisation is a stronger match to MECH-271 than the regional (dorsal/ventral) organisation Sosa et al. exploit. REE's stream-local view (z_world, z_harm_s, z_goal, z_self) is not naturally a regional distinction -- it is a content-type distinction that can plausibly live across a cellular-subpopulation organisation more easily than across a coarse dorsal/ventral split. Harvey et al. establish the cellular-subpopulation substrate.

## How it translates to REE

The architectural import is: do not implement HippocampalModule.propose_trajectories as a flat broadcast with downstream tag-based filtering. Implement it as a publish-to-typed-channels system where each channel has a specified consumer subset. The typing may be anchored-vs-probe, stream-local-content, pre-commit-vs-post-commit, or some combination of these; the architectural commitment is that the typing is source-side and the routing is selective.

This is consistent with the V3 substrate commitment implied in the MECH-269 design doc: publish anchored rollouts to the channels consumed by E1 consolidation, SD-033a lateral PFC, and the viability-map writer; publish probe rollouts to the channels consumed by BLA (affective tagging) and the NAc curiosity/novelty scaffolding. Harvey et al. provide the cellular-biological evidence that such a source-side-typed routing architecture is what the mammalian hippocampus actually does.

## Limitations and caveats

The content types Harvey et al. identify (trajectory-and-choice, reward-configuration) are specific to the task paradigm (spatial-and-reward) and are not identical to REE's stream types. Mapping from these biological content types to REE's z_world / z_harm_s / z_goal / z_self is a design-time decision, not an inference drawn from the paper.

Harvey et al. do not test the anchored vs probe distinction; their content-type distinction is orthogonal to it. MECH-271's specific claim that anchored and probe rollouts route differentially (anchored to consolidation; probe to affective-tagging and novelty) remains an REE-side commitment that these experiments do not directly address. What is established is the routing-with-cellular-selectivity architecture; what is not established is that REE's specific type axis is one of the axes this architecture supports.

The paper characterises hippocampo-cortical routing; it does not comprehensively address the subcortical consumers (BLA, NAc, fornix-Papez) that MECH-271 also implicates. The cortical-side evidence here combines with Sosa et al. 2019 for the NAc-side evidence and with Girardeau et al. 2017 for the BLA-side evidence to cover the subcortical arm.

## Confidence reasoning

Source quality is near-maximal: Neuron, Fernandez-Ruiz senior author, rigorous multi-region simultaneous electrophysiology with anatomical identification of subpopulations. Mapping fidelity is 0.82 -- the highest of the MECH-271 entries -- because the paper directly demonstrates cellular-level routing-with-selective-readout, which is the architectural shape MECH-271 proposes. Transfer risk is low for the routing architecture (well-supported generic finding, likely species-conserved) and moderate for the REE-specific labelling of REE streams and anchored/probe onto biological subpopulations. Overall confidence 0.86 -- this is the primary MECH-271 anchor for the cellular-level organisation of differential routing.
