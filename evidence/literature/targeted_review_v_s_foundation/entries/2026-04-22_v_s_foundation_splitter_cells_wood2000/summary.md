# Wood, Dudchenko, Robitsek & Eichenbaum 2000 -- Hippocampal neurons encode information about different types of memory episodes occurring in the same location

DOI: [10.1016/s0896-6273(00)00071-4](https://doi.org/10.1016/s0896-6273(00)00071-4) -- Neuron (PubMed 11055443)

## What the paper did

Recorded hippocampal complex-spike (CA1 pyramidal) neurons in rats running continuous spatial alternation on a modified T-maze. The decisive test: examine firing as the rat traverses the central stem (held constant in position, heading, and running speed) and ask whether neurons fire differently depending on whether the trial is a left-turn or right-turn episode.

## Findings relevant to V_s foundation

Two-thirds of CA1 cells fired differentially on the central stem depending on trial type, after controlling for position, heading, and speed. These are the canonical "splitter cells." The interpretation: hippocampal place coding is not a pure (x, y) lookup; the active representation at a location depends on the trajectory context (past or future). This means the same physical location can be encoded by different population states depending on which episodic context the animal is in.

## Translation to REE / MECH-269 / MECH-272

This is the strongest single piece of evidence that anchors should be (place, context) pairs rather than place alone. The biology refuses pure place-indexing: even when rats hold position, heading, and speed identical, two-thirds of CA1 cells fire differently based on the trial type they are in. Translating this to the V_s foundation substrate, an anchor keyed only on place will collapse two distinct (place, context) attractors into one and lose the disambiguation that biology preserves.

The architectural commitment in the spec -- regions are environmentally-grounded chunks, V_s is per-stream -- is consistent with this if the per-stream V_s vector is treated as the context that disambiguates which (place, stream-mixture) anchor is active. The Wood paper is biological evidence that this is the right granularity choice: anchors must carry context information beyond physical place. MECH-272 routing then has a clean mapping: the routing decision is which (place, stream-mixture) attractor to activate when the animal arrives at a given physical location, with the stream-mixture providing the disambiguator.

The paper does not specify what aspect of context is being encoded -- prospective coding (where you are going), retrospective coding (where you came from), or trial-type abstract context. Subsequent work (Frank, Brown & Wilson 2000, Catanese, Viggiano et al, Bahar) has parsed these into separate phenomena. For the V_s substrate, the takeaway is: any of these would map onto a different stream-mixture, and the substrate must support stream-mixture as part of the anchor key.

## Limitations and caveats

Two-thirds is a majority but not unanimous; one-third of cells fired similarly on both trial types (pure place coding). The substrate must accommodate both regimes -- some anchors carry only place, others carry (place, context). The recordings are CA1 only; the upstream CA3 and DG contributions are not directly assayed. The behavioural paradigm is highly stereotyped continuous alternation, which may exaggerate the trial-type signal relative to less structured contexts. Rodent only.

## Confidence reasoning

Source quality very high (Neuron, Eichenbaum lab, foundational citation). Mapping fidelity is high for the qualitative claim (anchors must support context disambiguation beyond pure place). Transfer risk is moderate -- the stereotyped alternation paradigm may inflate the splitter signal relative to naturalistic contexts, but the qualitative phenomenon is robust across many follow-ups.