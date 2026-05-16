# MAP-Elites: Illuminating Search Spaces (Mouret & Clune, 2015)

## What the paper did

Mouret and Clune asked a deceptively simple question: what if, instead of returning the single best solution to an optimisation problem, we returned the best solution across every interesting region of the solution space? Their answer is MAP-Elites (Multi-dimensional Archive of Phenotypic Elites). The algorithm divides a user-specified behavioral descriptor space into cells, and for each cell maintains only the single highest-fitness solution it has ever found. Mutations generate new candidate solutions; each candidate is evaluated on fitness and behavioral descriptors, and it replaces the current occupant of its cell only if it has higher fitness. Local competition within cells drives quality; coverage across cells drives diversity. No global competition means no single dominant strategy can crowd out all alternatives.

## Key findings

MAP-Elites produces archives that are simultaneously high-quality and highly diverse across the behavioral descriptor space -- what the authors call "illumination" of the search space. In three domains (modular neural networks, simulated soft robots, real soft robots), MAP-Elites fills the behavioral descriptor space with high-performing solutions that would be impossible to discover with traditional single-objective optimisation. The critical structural mechanism is local competition: solutions only compete with others in the same behavioral cell, so a fast forward-runner cannot eliminate a backward-runner or a jumper from the archive. Monostrategy is structurally prevented by the archive design, not by any explicit diversity reward.

## Translation to REE

The behavioral descriptor concept is the direct translation point for REE. The V_s monostrategy problem -- trained agents converging to a single fixed route -- is precisely the failure mode that MAP-Elites prevents at the archive level. For REE, the relevant behavioral descriptor would be something like: (region visited in the first third of the episode, region visited in the second third, whether foraging or safety-seeking was primary). If CEM candidate generation could maintain a soft archive biased toward under-represented behavioral cells, it would produce the equivalent of MAP-Elites within the per-step trajectory selection process. This is a more principled alternative to novelty-only exploration: not "have I seen this state before?" (MECH-314) but "do I have a high-quality solution for this behavioral region?" The key design question is what the behavioral descriptor dimensions should be for REE's navigation domain -- this requires explicit definition before implementation.

## Limitations and caveats

MAP-Elites is an offline, population-based algorithm. REE needs real-time diversity within a single-agent CEM. A direct port would require a behavioral archive that persists between steps and is updated online. The behavioral descriptor must be specified in advance; for REE, this means someone must decide which dimensions of trajectory variation count as "distinct behavioral modes" before the algorithm can maintain them. If the descriptor misses the relevant diversity axis (e.g. specifies action-type diversity but not route diversity), the archive will be diverse on the wrong dimensions. The archive grid also requires discretisation of a continuous behavioral space, which introduces granularity tradeoffs.

## Confidence

0.75. Foundational high-impact paper with strong structural argument. Transfer risk is the main moderator: the offline/population architecture requires significant adaptation to fit REE's real-time CEM setting. The behavioral descriptor insight -- that the right descriptor is the key design decision for diversity -- is directly actionable.
