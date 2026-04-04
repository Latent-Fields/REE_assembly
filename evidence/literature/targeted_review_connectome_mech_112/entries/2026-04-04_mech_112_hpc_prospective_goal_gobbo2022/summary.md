# Neuronal signature of spatial decision-making during navigation: prospective goal coding in CA1

**Gobbo et al. (2022), PNAS, DOI: 10.1073/pnas.2212152119**

## What the paper did

Gobbo and colleagues used wide-field calcium imaging to record from more than 1,000 CA1 neurons simultaneously in freely moving rats performing a spatial recency task. Each day, the rewarded goal location changed among three possible sites in a familiar arena. Rats had to encode and then recall which specific location was rewarded that day. The key innovation was examining neural activity in the startbox -- before the animal entered the arena and began navigating. The question was whether CA1 activity before movement could predict the goal the animal was about to seek.

## Key findings relevant to the claim

The central finding is that CA1 population activity in the startbox rose steadily in the period before arena entry, and this pre-movement activity was predictive of the day's specific goal location on correct trials. On error trials, this prospective goal signal was absent or degraded. Both single-cell activity and population-level decoding converged on the same conclusion: the hippocampus generates a prospective representation of the upcoming goal before navigation begins. This representation is not simply familiarity with the spatial context -- it specifically encodes which particular goal the animal is oriented toward on that day.

## Translation to REE (the mapping)

MECH-112 claims that E3 requires a structured latent goal representation that functions as a positive attractor -- providing terrain to navigate toward in the hippocampal planner, distinct from harm avoidance. Gobbo et al. provide the direct empirical demonstration: CA1 generates a prospective goal representation before action initiation, encoding the agent's current orientation toward a specific future state. In REE terms, this is the biological counterpart of z_goal seeding the hippocampal terrain before trajectory selection begins. The goal is not computed at reward delivery (liking) and it is not derived from harm avoidance; it is prospectively represented in CA1 before any outcome has been encountered on that episode.

The failure signature on error trials is particularly instructive: when the prospective goal signal is absent, navigation fails. This matches the MECH-112 prediction precisely -- without z_goal providing positive-attractor terrain, the hippocampal planner has no goal to navigate toward and trajectory selection degenerates. The behavioral degenerate case in the paper (error trials without prospective coding) is the behavioral equivalent of the quiescent policy that MECH-112 predicts for a harm-avoidance-only system.

## Limitations and caveats

The task uses spatial goals in a physical arena, and the transition from spatial goal representation to REE's abstract z_goal in latent space is non-trivial. Place cells encode geometric location; z_goal encodes a motivationally relevant future state in a high-dimensional latent manifold. The paper does not speak to persistence of the goal representation across multiple episodes or training sessions -- it measures a within-episode prospective signal. The daily-changing goal is externally set by the experimenter (baited location), so this is not a demonstration of intrinsically generated goal-directed behavior. The Morris lab context (schema and episodic memory research) means the design is optimised for episodic specificity, not motivational drive per se.

## Confidence reasoning

Source quality is high (PNAS, 2022, Morris lab, large-scale calcium imaging from more than 1,000 neurons). Mapping fidelity is good for the core claim that hippocampus encodes a prospective goal representation as a positive attractor, but moderate for the full MECH-112 requirements including persistence and integration with harm avoidance. Transfer risk is moderate given the spatial-to-abstract translation. The failure-signature evidence (absent prospective coding on error trials) strengthens the mapping. Overall confidence: 0.80.
