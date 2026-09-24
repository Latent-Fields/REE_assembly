# Salinas & Sejnowski 2001 -- gain modulation as general computation

**What it says.** Gain modulation, where one input turns another's effect up or down without changing what the neuron is selective for, is everywhere in cortex: parietal eye-position gain fields, attention, navigation, object recognition. The review's theoretical point is that a *population* of gain-modulated neurons forms a basis from which a downstream readout can compute coordinate transformations and invariant responses. In other words, gain across a population can change which mapping is computed, not just how large its output is.

**Why it cuts both ways for ARC-111.** The claim's falsifier rests on one discriminator: a gain model "can rescale a fixed policy but cannot REORDER it," so a context-dependent reordering of committed channels would count as evidence for the weight form. This review shows the discriminator only holds when gain acts on a single output. Put gain on a hidden population and read it out with fixed weights, and gain alone can reorder. So a reordering result would not, by itself, separate the two forms.

**What it means in practice.** For REE as shipped, the concern may be academic. Terrain weight, precision and write gating are mostly scalars on outputs or channels, which cannot reorder. But if the ARC-111 experiment ever puts the gain-only control on a richer representation, the control arm could produce the effect the claim attributes to weights. The falsifier should say explicitly that its gain arm is output-level, or the test isn't a test.

**Confidence.** 0.55, recorded as `mixed`. It supports "output gain isn't enough," but it weakens "reordering proves weights."
