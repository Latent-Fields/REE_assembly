# Learning Invariant Representations for Reinforcement Learning without Reconstruction (Zhang et al., ICLR 2021)

## What the paper did

This is the paper that made "stop reconstructing" a respectable position in RL representation learning. Zhang and colleagues train an encoder so that distances in latent space equal **bisimulation distances** in state space -- a metric that calls two states similar when they behave the same way, i.e. when they yield the same rewards and transition to behaviourally similar states. The representation is therefore defined by what the agent will *do*, not by what the observation *looks like*. They evaluate on visual MuJoCo tasks from the DeepMind Control Suite in three regimes (default, simple moving distractors, natural-video backgrounds) and on a first-person CARLA highway-driving task, where they report 46.8% better final performance than the next best baseline.

## The diagnosis, which is what this entry is for

The constructive half of the paper matters less to us than its statement of the problem, which is the crispest in the literature:

> "such methods are task-agnostic: the models represent all dynamic elements they observe in the world, whether they are relevant to the task or not"

and the design goal that follows:

> "Rather than learning control-agnostic representations that focus on accurate reconstruction of clouds and buildings, we would rather achieve a more compressed representation from a lossy encoder, which only retains state information relevant to our task."

SD-106 *is* a lossy encoder trained by a task-agnostic criterion. The paper's diagnosis says what such an encoder does with a bounded budget: it represents whatever varies, roughly in proportion to how much it varies. Set against V3-EXQ-1041's numbers, this is the ML-empirical form of the reading that autopsy labelled **(b) which-directions** -- the code sits at 0.951-0.980 of the PCA-32 ceiling, having compressed generically about as well as a 32-dimensional linear code can, while the consumer rung reads 0.719 oracle-action agreement against a 0.85 bar. Nothing about that pattern requires the encoder to be under-trained or the mechanism to be broken. It is what a variance-ordered budget looks like when the decision-relevant directions are not the high-variance ones.

## The moderator, which the paper supplies against itself

The result is conditional, and the paper is honest about it. In the **default, distractor-free setting a reconstruction-based method (SLAC) generally performs best**; the bisimulation encoder's advantage appears only once simple or natural-video distractors are introduced. So this paper does not license "reconstruction is the wrong objective" full stop. It licenses "reconstruction is the wrong objective *where task-irrelevant variance is large*" -- and the distractors here are introduced artificially, at a magnitude chosen to make the point.

That is the crux for SD-106, and it is an unmeasured quantity. REE's P0a rollout buffer has never been characterised on that axis. The direction of this evidence transfers; its magnitude does not.

## Two further cautions

The positive proposal has aged less well than the negative diagnosis. Later work -- including the Tomar et al. entry in this same pull, and the NeurIPS 2023 "Pitfalls of Bisimulation-based Methods" paper -- reports that the bisimulation loss itself can degrade performance, and that DBC with its metric ablated can beat DBC with it. I am relying on this entry for the diagnosis, not for the remedy; a DBC-shaped successor to SD-106 should not be read as validated by it.

And bisimulation needs a reward or equivalent behavioural signal to define behavioural similarity at all. SD-106's objective runs in a P0 warmup under a RandomPolicy. If no informative behavioural signal exists at that point in the curriculum, a direct transplant is not merely harder, it is inapplicable as specified -- which is a design constraint on any task-conditioned successor, not a defect of this paper.

## Confidence

0.78, the highest in this pull. Source quality 0.88: a heavily-cited ICLR paper with released code, a theoretical basis in bisimulation metrics, and results across two distinct domains. Mapping fidelity 0.72 -- the structural analogy (bounded lossy encoder, task-agnostic objective, downstream control consumer) is tight, while the observation modality and the source of task-irrelevant variance are quite different from REE's. Transfer risk is set at 0.42 rather than lower specifically because the result is moderator-dependent and REE currently sits on the unmeasured side of that moderator.
