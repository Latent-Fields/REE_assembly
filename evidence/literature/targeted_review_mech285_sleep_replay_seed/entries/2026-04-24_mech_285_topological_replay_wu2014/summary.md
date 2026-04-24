# Wu & Foster 2014 -- replay captures experienced topology

## What the paper did

Rats explored a novel forked (T/Y-variant) environment while place cells were recorded from CA1. The analysis asked whether the structure of post-run replay events -- their recruitment of cell populations, directionality, and associated sharp-wave-ripple substructure -- reflected the environmental topology the animal had sampled, or whether replay was a looser read-out of all activated cells.

## Key findings relevant to MECH-285

Three findings constrain the seed-state distribution. First, replays of divergent trajectories through the same forked segment recruited the same cells at the same firing rates to represent the shared portion, and different cells for the divergent arms -- replay respects the branching structure. Second, replay direction flipped at the fork, indicating that directional and spatial structure were both preserved. Third, the local field potential ripples associated with replay exhibited substructure mapping onto the maze topology. Notably, these replays appeared rapidly, after small numbers of experiences.

## Translation to REE

For MECH-285 the relevant question is: what is the shape of the seed-state distribution feeding the sleep consumer? Wu & Foster establish that seeds are not uniform across place cells. Replay content respects the experienced topology -- seed states cluster where the animal has been, and the branching structure of paths is preserved in the recruited-cell population and in the ripple structure itself. This biases the prior on the MECH-285 sampler: whatever weighting scheme is used (narrow-active-only, broad-with-staleness, salience-driven), it operates over an experience-structured graph, not a flat uniform pool.

This constrains but does not settle the narrow-vs-broad question. The observation that divergent futures from a shared start get represented is consistent with a broader-than-current-trajectory seed pool -- the animal is not just replaying its most recent run but something richer. The paper's structural finding is most usefully read as: MECH-285's sampler must be compatible with an experience-graph-structured prior, not with uniform sampling.

## Limitations and caveats

The paper studies awake replay, not sleep replay. The inferential leap to offline sleep consumers is not trivial -- awake SWR content is known to differ in important ways from sleep SWR content (Joo & Frank 2018 review this explicitly). The paper also does not vary staleness or reward across maze regions, so it cannot test MECH-285's priority-shape question. Its contribution is structural -- whatever MECH-285 does, it inherits this experience-conditioned prior.

## Confidence reasoning

Source quality is high. Mapping fidelity is moderate -- the paper addresses seed-structure but not the priority or timing questions MECH-285 foregrounds. Transfer risk is moderate (awake-to-sleep, rat-to-silicon). Aggregate confidence 0.68: a useful structural constraint rather than a direct adjudication.
