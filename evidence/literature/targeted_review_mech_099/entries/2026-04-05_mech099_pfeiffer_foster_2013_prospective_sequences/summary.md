# Pfeiffer & Foster 2013 -- Hippocampal Sequences as Prospective Goal-Path Generator

**Source:** Pfeiffer BE, Foster DJ. "Hippocampal place-cell sequences depict future paths to remembered goals." *Nature* 497:74-79, 2013. DOI: [10.1038/nature12112](https://doi.org/10.1038/nature12112). PMID: 23594744

**Claim evidenced:** MECH-099

---

## What the paper did

Pfeiffer and Foster recorded CA1 place cell ensembles in freely-moving rats navigating an open circular arena with a moveable goal box containing food reward. During brief awake immobility events at the arena perimeter, they decoded the population activity to identify sequential place-cell firing. They tracked whether these sequences were biased toward trajectories leading from the animal's current position to the goal location, and whether this held for novel start-goal combinations.

## Key findings relevant to REE

Before initiating navigation toward a goal, the hippocampus generates brief sequential activations of place cells that trace future paths from current location to the goal. The sequences are strongly biased toward goal-directed paths -- not random or past-path retracing. Critically, this works for novel start-goal combinations, demonstrating that the representation is not a stored route memory but a generative read-out from a spatial map that can construct novel trajectories to any known goal.

The sequences are prospective (they represent where the animal is about to go, not where it has been), occur at the choice point or rest moment, and are updated dynamically based on where the goal currently is.

## Translation to REE

MECH-099 posits that the residue field is a persistent spatial map that the hippocampal module reads out to generate context-sensitive trajectories. Pfeiffer and Foster directly instantiate this read-out mechanism: the hippocampus uses its spatial map to produce prospective trajectory sequences toward a remembered target. In MECH-099, the target is a harm-minimum or benefit-maximum region of the residue field, not a food reward box -- but the read-out mechanism (generate sequence from current position toward remembered target location) is architecturally identical.

The novel-start-goal result is particularly important: it rules out route-level storage and confirms that trajectory generation is a computation over a persistent spatial structure. This is the key feature MECH-099 requires -- the residue field must support generation of trajectories to locations that may not have been directly traversed in sequence before.

## Limitations and caveats

The goal is a reward location (food), not a harm-avoidance target. The residue field in REE is primarily a harm-tracking structure. Whether the same sequence-generation mechanism operates for avoidance goals (navigate away from harm-rich region, or toward harm-free corridor) is not directly tested and may involve different hippocampal-amygdala circuitry. The sequences here occur during awake immobility, not during offline consolidation phases; their relationship to the replay events that maintain the persistent residue field (MECH-121) requires inference.

## Confidence reasoning

Confidence 0.80. Landmark Nature paper, high quality. Excellent support for the trajectory read-out mechanism in MECH-099. Moderate gap on the harm/benefit accumulation dimension -- this paper establishes the geometry of context-sensitive trajectory generation, but does not address how the map is updated by harm history over time.
