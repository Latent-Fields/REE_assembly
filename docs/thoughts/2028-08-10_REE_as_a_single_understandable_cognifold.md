REE as a single understandable cognifold

Date: 2026-08-10
Status: Unstructured thought / explanatory framing / public-communication proposal

My vision for REE is ultimately one single understandable cognifold.

There is a slightly paradoxical problem emerging as the architecture develops: the more I know about the individual mechanisms, the harder it becomes to see the thing as a whole. E1, E2, E3, hippocampal mechanisms, residue, goals, harm streams, salience, commitment, sleep, replay, neuromodulation and the growing collection of cortical and subcortical analogues are individually intelligible, but the growing list can obscure the much simpler object they collectively constitute.

A useful description is that REE-v3 is not a neural network. It is a hybrid dynamical system whose changing internal state is partly represented by PyTorch tensors, whose learned transformations are partly neural networks, and whose remaining machinery consists of explicit memories, gates, clocks, buffers, search processes and update rules.

PyTorch should not be mistaken for the cognitive architecture. It is better thought of as some of the mathematical tissue from which the architecture is constructed.

At a given moment, much of the immediate state of REE consists literally of collections of floating-point numbers: latent vectors representing self, world, affective state, temporal context, motivational context, harm, resources and other specialised quantities. These numbers have no intrinsic semantic meaning individually. Their meaning arises from how they are produced, what they predict, how they covary, how experience changes them, and how the rest of the system responds to them.

But the current latent vectors are not the whole mind.

There is also learned structure: the parameters of the encoders, predictors, recurrent systems and evaluators.

There is persistent state: recurrent hidden states, context-memory slots, hippocampal structures, residue fields, valence maps, goal attractors, familiarity, anchors, trajectory memories and other traces through which previous experience continues to affect the present.

And there is fixed dynamical architecture: clocks, gates, commitment and release conditions, replay rules, simulation/reality provenance, search procedures and the restrictions defining which components may alter which others.

The useful boundary therefore seems to be:

The REE cognifold is the total evolving internal state-space of the agent, together with the learned and fixed transformations that determine how that state can change.

One possible schematic description is:

[
M_t =
{
z_t,,
h_t,,
H_t,,
R_t,,
G_t,,
C_t;,
\theta
}
]

where:

* (z_t) is the current latent state;
* (h_t) is recurrent and predictive state;
* (H_t) is hippocampal and episodic structure;
* (R_t) is residue and learned valence terrain;
* (G_t) is goal and motivational state;
* (C_t) is control, commitment, precision, timing, gating and modulatory state;
* (\theta) is the learned structure of the system.

The dynamics can then be thought of approximately as:

[
M_{t+1}

F_{\theta}
(M_t,\ observation_t,\ action_t)
]

with the environment outside that boundary.

Seen this way, the many mechanisms are not separate little agents. They are structures constraining and transforming one continuously evolving state.

The whole loop becomes quite simple to state:

A structured state predicts, imagines possible futures, evaluates them, commits to action, acts, experiences the consequences, remembers them, and thereby changes the state from which it will predict, imagine, evaluate and act next time.

That may be one of the clearest descriptions yet of what REE is attempting to construct.

Public-facing implication

I think some version of this explanation should eventually sit somewhere prominent in the public-facing REE material, rather than requiring a reader to reconstruct the whole from the mechanism registry or architecture diagrams.

There should probably be a highly visible “What is REE, mechanically?”, “Inside an REE agent”, or “The REE cognifold” explanation that starts at this level and only then allows the reader to descend into E1/E2/E3, hippocampus, residue and individual mechanisms.

In particular, it should explain that “REE uses PyTorch” does not mean “REE is one neural network”. PyTorch provides tensors, differentiable transformations, neural-network components and learning machinery. REE specifies the organisation of those components and combines them with persistent state and explicitly designed dynamics.

A public reader should ideally be able to come away with one picture:

world → internal state → prediction and imagined trajectories → selection and commitment → action → consequences → changed internal state → repeat

The mechanism atlas can then be understood as an explanation of how different regions of that one cognifold contribute to the cycle.

This framing should remain explicitly architectural rather than phenomenological. Describing an integrated state-space as a cognifold does not establish consciousness, sentience or moral patienthood. It is a way of making the implemented computational object understandable.

The longer-term aspiration is that REE should remain understandable at this level even if the internal representational spaces eventually become vastly larger and richer. The cognifold may become complex; its organising dynamics should not become conceptually opaque merely because its learned contents do.