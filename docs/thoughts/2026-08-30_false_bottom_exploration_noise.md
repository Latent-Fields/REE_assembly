Status: raw thought intake
Date: 2026-08-30
Scope: REE exploration; attractor escape; MECH-440 interpretation and future testing
Authority: exploratory programme thought; does not itself alter MECH-440 claim status, governance, or experiment interpretation
Processing note: preserve V3-EXQ-959 as genuine evidence against the current operationalisation. The proposal is to distinguish low-level action noise from a broader stuckness-triggered attractor-escape function, not to explain away a clean negative result.

# False bottoms, attractor escape, and what exploration noise is for

## Originating thought

The current MECH-440 noisy-selection mechanism may be testing the wrong conception of exploration.

The motivating intuition is not simply:

> **When several immediate actions have similar scores, add noise.**

It is closer to:

> **When you cannot figure something out, you start trying random stuff.**

The purpose of injected variation is therefore not randomness for its own sake. It is to help the organism escape a **false bottom**: an attractor that is locally stable and appears low-energy, but is actually a dead end relative to a better solution elsewhere in the landscape.

A false bottom can be especially difficult because the system may be highly confident. The problem is not necessarily uncertainty. The problem is persistent failure despite settling.

## Implication for MECH-440

V3-EXQ-959 cleanly weakens the stronger current MECH-440 story that noisy selection should preferentially affect near-tie states and self-anneal there. The experiment was non-vacuous and its readiness gates were green. That result should stand.

However, it may not test the most important ecological function of exploration noise.

The present implementation perturbs low-level candidate action scores. In a small bounded gridworld, where ordinary action variation already samples much of the immediate action space, such perturbations may create behavioural diversity without creating useful **strategic exploration**.

The deeper function may instead be:

**persistent unresolvedness or repeated failure**  
→ **temporarily inject energy/variation**  
→ **escape the current attractor**  
→ **search alternative trajectories/strategies/representations**  
→ **discover a lower-energy basin**  
→ **settle again and reduce exploration**.

This is closer to a triggered, organism-level analogue of annealing than to continuous generic action noise.

## The trigger should distinguish uncertainty from stuckness

Near-equal candidate scores are not necessarily a reason to explore. Two understood actions may simply be similarly good.

Conversely, a false bottom can produce high confidence: all currently represented candidates may strongly support the same failing strategy.

Potential stuckness signals include:

- persistent prediction error or model/outcome mismatch;
- repeated failure to reduce an active need or goal error;
- recurrent return to the same state/trajectory basin with poor outcomes;
- repeated unsuccessful action sequences despite high attractor confidence;
- failure of expected trajectory value to improve over time;
- persistent discrepancy between confidence and realised outcomes;
- repeated selection of the same strategy after evidence that it is inadequate.

The important signal may therefore be **confidence without successful resolution**, not uncertainty alone.

## The perturbation may need to occur above the immediate action level

Low-level action noise can remain useful, but it should not necessarily carry the whole exploration function.

Persistent stuckness may justify progressively broader perturbation of:

- candidate trajectories;
- strategy or policy proposals;
- counterfactual hypotheses;
- remembered routes or retrieved attractors;
- goal decompositions;
- model assumptions;
- the precision/authority of the currently dominant attractor;
- which representations are admitted into competition.

A small failure might perturb immediate actions. A persistent false bottom might require temporarily weakening the dominant attractor and reopening alternatives that ordinary settling suppresses.

## Better V3 test ecology

A useful experiment should create a genuine false bottom rather than merely measuring whether noise changes action selection.

Candidate environments include:

- a locally attractive resource policy that prevents discovery of a better delayed-return strategy;
- a barrier where the shortest apparent path is blocked and success requires an initially counterproductive detour;
- an environmental rule change that makes a previously successful learned policy persistently fail;
- a sparse-reward problem where the successful solution requires several individually unrewarding actions;
- a recurrent loop whose local choices all appear reasonable but whose basin is globally suboptimal.

Compare at least:

1. no exploration perturbation;
2. ordinary low-level random action/score noise;
3. stuckness-triggered strategy or trajectory perturbation.

The important dependent variables should be organism-level:

- probability of escaping the false basin;
- latency to discover the better solution;
- quality of the basin ultimately reached;
- whether exploration decreases after successful resolution;
- whether the discovered strategy is retained;
- whether the mechanism avoids unnecessary exploration when the existing strategy is actually adequate.

## Working correction

The stronger candidate formulation is:

> **Exploration noise exists to let the organism escape an apparently stable but persistently inadequate attractor and discover a better basin.**

Or more simply:

> **Noise should help the creature get out of a false bottom.**

This reframes MECH-440 away from "uncertain therefore random" and toward **"settled but unresolved therefore reopen the search space."**

The V3-EXQ-959 negative remains valuable: it shows that the current near-tie/self-annealing formulation does not reliably provide this richer function. The next step should be conceptual re-scoping and a false-bottom ecology, not merely tuning sigma.