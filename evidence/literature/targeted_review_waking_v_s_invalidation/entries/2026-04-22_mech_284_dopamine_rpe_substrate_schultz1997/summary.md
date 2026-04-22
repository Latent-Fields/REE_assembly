# Schultz, Dayan & Montague 1997 -- A Neural Substrate of Prediction and Reward

According to PubMed ([DOI](https://doi.org/10.1126/science.275.5306.1593)).

## What the paper does

Schultz1997 is the canonical synthesis paper that formalised midbrain dopamine activity as a temporal-difference reward prediction error. The empirical core, drawn largely from macaque VTA/SNc single-unit recordings during classical and instrumental conditioning, is the now-familiar three-signature pattern: phasic burst when an unsignalled reward arrives; transfer of the burst back to the earliest predictive cue once the cue is learned; and a depression -- a dip below baseline -- at the time the predicted reward fails to appear. Wrapping this in the Sutton-Barto TD framework, the authors argued that the dopamine fluctuation literally implements the RPE signal that drives reinforcement learning.

## Why it matters for V_s invalidation

For our purposes the dip is the load-bearing observation. It is, biologically, the brain's clearest example of a *single-event* "what I expected did not happen" signal -- and it is broadcast diffusely across striatum and frontal cortex via the mesocortical and nigrostriatal projections. If we are looking for a candidate trigger event for MECH-284's accumulator -- something that fires online, in the waking state, the moment a schema's prediction is violated -- the DA dip is the prototype.

But the mapping is partial. Schultz1997 frames the signal as reward-scalar: it is a prediction error about *value*, not about schema fit. V_s as we have defined it concerns whether a particular hippocampal anchor / regional schema is still *the right schema for this region* -- a model-validity question, not a value question. That is a non-trivial extension of the 1997 framework. Two later papers in this pull (Gardner-Schoenbaum-Gershman 2018; Wilson 2014) push DA toward a more general PE signal that can serve as a model-fit signal, and those carry more of the architectural weight. Treat Schultz1997 as the existence proof that the brain has a single-event broadcast violation signal of the right shape, not as a substrate for the accumulator.

## Clinical resonance

The dip-on-omission framing also gives us the cleanest clinical hook for the V3-EXQ-475 phenotype. In depression, phasic DA responses are blunted; in OCD and perseveration, the blunting is selective for "this routine isn't working" signals. If the trigger fires (dip happens) but the accumulator never integrates it (V_s for the stale anchor never falls), the agent will repeatedly notice failures and yet keep returning to the same behaviour. That is exactly what the freeze re-commit pattern looked like.

## Confidence reasoning

Source quality is essentially the ceiling -- this is *the* paper. Mapping fidelity is moderate (0.45) because the V_s construct is not the construct the paper measured. Transfer risk is moderate (0.40) because the basic DA-RPE biology generalises well from macaque to human, but the leap from value-PE to schema-validity-PE is large and is what later papers in this pull attempt. Aggregate confidence 0.55 -- the paper supports the *trigger-event existence* sub-claim of MECH-284 strongly and the *accumulator* sub-claim only by analogy.
