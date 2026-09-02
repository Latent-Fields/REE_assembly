# Orbitofrontal cortex as a cognitive map of task space

Wilson, Takahashi, Schoenbaum & Niv (2014, *Neuron*) propose that orbitofrontal cortex does one thing:
it labels the current task state, providing an abstraction over currently available information that
reinforcement learning elsewhere in the brain then consumes. The proposal earns its keep by
reinterpreting a scattered set of classic OFC findings -- reversal learning, delayed alternation,
extinction, devaluation -- as consequences of a damaged state representation rather than as separate
deficits, and by accounting for the more recent observation that OFC lesions degrade the firing of VTA
dopamine neurons during reinforcement learning. Their emphasis falls on task states containing
*unobservable* information, held for instance in working memory, since that is where a labelled state
abstraction earns its keep over raw perception.

Of the entries in this pull, this is the closest structural match to ARC-121's producer/consumer shape.
The paper does not merely say that a shared format exists; it says one region maintains a state object
and other mechanisms use it. That is the arrangement ARC-121 asserts REE is converging on, stated in
the source's own terms rather than reconstructed from them. The emphasis on unobservable content
matters too: it is what makes the maintained object *epistemic* rather than merely perceptual. A state
label that only summarised sensory input would not bear on ARC-121 at all; one that carries what the
agent believes about latent situation structure is exactly the kind of object the claim is about.

The honest limits are two. First, the demonstrated consumer set is narrow -- reinforcement learning
and dopaminergic prediction error, not the heterogeneous consumer list ARC-121 names. Nothing here
shows harm or ethics evaluation, or possibility representation, reading the same state label, and
ARC-121's interest lies substantially in the claim that those heterogeneous consumers converge.
Second, "task state" is narrower than "epistemic state": it is a partition of a task's latent
situations, not knowledge, uncertainty and commitment bound into one object. Reading this paper as
support for the full claim would overstate it; reading it as support for the producer/consumer
*architecture* is fair.

There is also a status caveat. This is a unifying theory that reinterprets existing findings and then
generates predictions to discriminate itself from rivals -- the authors say as much. It is not a
decisive test, and the decade since has both extended the account and complicated the strict
OFC-as-state-space reading.

Confidence 0.70. Source quality 0.8 -- a highly cited *Neuron* theory paper with genuine explanatory
reach across independent datasets, but not itself a new measurement. Transfer risk 0.4, the highest
among the supporting entries, because the rodent task-state construct sits several abstraction levels
below REE's z_world-scale epistemic object.
