# Curiosity-driven Exploration by Self-supervised Prediction (Pathak et al., 2017) — MECH-457

## What the paper did

Pathak, Agrawal, Efros & Darrell proposed the Intrinsic Curiosity Module (ICM). Rather than predict raw observations (which would reward noise), ICM learns a feature space via an *inverse* dynamics model — predict the action that took the agent from state to next-state — so the features retain only what the agent's actions can influence. A *forward* model then predicts the next feature vector; its prediction error is the intrinsic reward. Layered on an A3C actor-critic, a curious agent solved sparse- and even zero-extrinsic-reward VizDoom navigation and made progress on Super Mario Bros., reportedly clearing in under 100M frames tasks that vanilla A2C failed to solve in 500M.

## Why it is relevant, and why it is `mixed`

This is the second existence-proof on the unsupervised-explorer side of the live MECH-457 discrimination (the first being RND). It reinforces that an intrinsic signal computed only from the agent's own experience — no expert, no demonstrations — can drive competent action learning under sparse reward, on top of exactly the actor-critic policy object MECH-457 says REE needs. That supports keeping "build a better explorer" alive as the H-optim leg's hypothesis.

I marked it `mixed` rather than `supports` deliberately, because the same research programme is the clearest catalogue of *why an intrinsic bonus can fail*. The forward-prediction bonus is drawn to inherently unpredictable stimuli — the "noisy-TV" problem — where an agent can be captured maximising surprise at a stochastic source instead of pursuing the task; the follow-up large-scale study by the same group made this failure explicit. And curiosity only helps to the degree the inverse-dynamics features happen to capture the task-relevant, action-controllable degrees of freedom; where they do not, the bonus points nowhere useful. For a governance record whose job is to decide *explorer vs scaffold*, presenting ICM as an unqualified win would be dishonest — it is evidence that the explorer path is real but not that it is robust.

## The mapping and its caveat

The mechanism transfers cleanly in form: an intrinsic bonus over a policy-gradient actor-critic is precisely the shape of the deferred H-optim leg. What does not transfer for free is the *environment structure*. ICM's wins are in visually rich navigation/platforming with strong action-controllable regularities; REE's D3 5x5-view forage may or may not offer the kind of learnable structure ICM's features exploit. So this entry cuts both ways: it says the explorer path has legs, and it says the leg genuinely needs to be *run* rather than assumed, because the very mechanism that could rescue REE has documented ways of stalling on a task like foraging.

## Confidence reasoning

0.66, `mixed`. Source quality is high (ICML 2017, foundational and widely replicated). Mapping fidelity is moderate — the algorithmic shape maps onto the H-optim leg but the demonstrated tasks are unlike REE forage. Transfer risk is raised specifically by the noisy-TV and feature-space-dependence failure modes, which are live possibilities in REE's environment. Read alongside RND (supports, stronger) and the DQfD/DAgger scaffold entries, this keeps the two build targets in genuine tension pending the empirical leg.
