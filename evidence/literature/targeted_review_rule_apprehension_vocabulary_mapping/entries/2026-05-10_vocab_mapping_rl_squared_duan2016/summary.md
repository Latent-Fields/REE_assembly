# Duan et al. 2016 -- RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning

## What the paper did

Duan, Schulman, Chen, Bartlett, Sutskever and Abbeel (the OpenAI lab) introduced RL^2, the foundational ML implementation of meta-reinforcement-learning. The key idea: a recurrent neural network is trained with reinforcement learning across a *distribution of MDPs* (different tasks drawn from a common task-family). After training, the recurrent network's hidden state functions as a fast inner-loop RL algorithm: presented with a new MDP from the distribution, the network adapts its behaviour within an episode purely through its recurrent dynamics, with no weight updates. The slow outer-loop RL training (across MDPs) shapes the recurrent network into one that can act as a fast learner. Empirically demonstrated on bandit tasks, small grid-world navigation, and a "visited-in-the-past" visual recognition task.

## Key findings relevant to the rule-apprehension vocabulary question

RL^2 is the concrete ML implementation that grounds the Wang 2018 biological-mapping paper. For Pull 4 it matters because:

1. It provides a *directly transferable algorithm* for the meta-RL collapse of ARC-062 + MECH-318. There is no special architecture required -- a recurrent network trained on a distribution of contexts will spontaneously develop the rule-application machinery in its hidden state.

2. It gives REE a precise training-schedule prescription: the slow outer-loop is the multi-context training distribution; the fast inner-loop is recurrent-state adaptation within an episode. For REE this means the design lever is the *training schedule*, not the architecture.

3. It validates the parsimony argument: if RL^2 works in REE's substrate, ARC-062 (gated_policy + discriminator) and MECH-318 (rule-state abstraction) really do collapse into "recurrent state of a meta-RL-trained network". No separate substrates needed.

## How the findings translate to REE

The transfer is direct at the algorithmic level:

- *Slow outer-loop* = REE's multi-context training schedule. The latent stack is trained across different SD-029 hazard regimes, different goal configurations, etc.
- *Fast inner-loop* = REE's latent stack recurrent dynamics during an episode. Within-episode adaptation should emerge in the recurrent state.
- *Rule-application machinery* = the within-episode adaptation behaviour. There is no separate ARC-062 or MECH-318 -- both collapse into "what the trained recurrent network does".

For V3-EXQ-543b design (Pull 4 R5), this gives a specific arm to add: *meta-RL baseline*. Train the existing latent-stack with multi-context RL; test whether within-episode context-conditioned behaviour emerges. If yes, the explicit ARC-062 + MECH-318 substrates are redundant -- the cluster collapses on parsimony grounds. If no, the explicit substrates are doing something the meta-RL training cannot recover.

## Limitations and caveats

RL^2 has well-known limitations that REE inherits if it adopts the framework:

1. *Hidden-state capacity is finite*. The meta-learned algorithm specialises to the training distribution and does not generalise outside it. For REE this means the meta-RL framing only works if the V3 substrate trains across enough varied contexts -- a substantial training-schedule design constraint.

2. *Sample complexity is high*. RL^2 needs many MDPs in its training distribution to develop a useful inner-loop. The biological reading (Wang 2018) doesn't have a clean answer for how the brain gets enough varied training experience.

3. *No clean handling of online-vs-offline timing*. Like meta-RL more broadly, RL^2 does not model the within-episode-online vs across-episode-offline distinction Pull 2 R3 identified.

The empirical demonstrations are on simulated bandit and small-maze tasks. Transfer to REE's continuous-state long-horizon substrate is plausible but not zero-shot.

## Confidence reasoning

Scored 0.74. Source quality moderate-high (preprint, well-cited at 1500+, OpenAI authorship, but not formally peer-reviewed in the original form). Mapping_fidelity high (0.74) for the algorithmic transfer to ARC-062 + MECH-318 unification. Transfer_risk moderate-high (0.45) due to bandit-style empirical regime and limited-capacity hidden state. The paper feeds R2 (RL^2 as inheritable algorithm) and R5 (V3-EXQ-543b should add a meta-RL baseline arm to test whether the explicit cluster substrates are redundant beyond what RL^2-style training produces).
