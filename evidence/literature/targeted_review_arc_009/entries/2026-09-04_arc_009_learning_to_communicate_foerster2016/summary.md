# The coordination half of ARC-009, demonstrated (Foerster et al. 2016)

## What the paper did

Foerster, Assael, de Freitas and Whiteson put multiple deep RL agents into partially-observable environments where no single agent can see enough to solve the task, and where a shared reward makes it worth their while to tell each other things. No protocol is supplied. The agents must invent one. Two methods are proposed: Reinforced Inter-Agent Learning (RIAL), which treats message selection as another discrete action learned by deep Q-learning, and Differentiable Inter-Agent Learning (DIAL), which exploits the fact that during *centralised* training the channel can be made differentiable, so error derivatives flow from the receiver back through the message into the sender. Execution remains decentralised. The environments are deliberately small and legible — communication riddles such as the switch riddle, plus multi-agent MNIST games.

## Why this speaks to ARC-009

ARC-009's `what_would_answer` field is unusually specific about what would count as evidence, and it describes almost exactly this experiment: two or more agents, a shared environment, information asymmetry, a discrete symbol channel, and a demonstration that agents with the channel beat a no-communication baseline. This paper is that experiment, run in a non-REE substrate, and it comes out positive. That is worth having on the record. It moves ARC-009's first criterion from "plausible in principle" to "demonstrated in principle" — the coordination benefit is not hypothetical, it is a reproducible result that a large subsequent literature has built on.

What I want to be careful about is the scope of what has been shown. ARC-009 says language is a symbolic *mediation and coordination* layer, and those are two different claims joined by an "and". Foerster et al. evidence the coordination half cleanly: a channel buys measurable task performance under information asymmetry, and the improvement is attributable to the channel because the baseline lacks it. The mediation half — the idea that symbols restructure or stand in for the agents' internal representations, which is the more interesting and more REE-specific reading — is untouched. The learned protocols here are opaque task-specific codes. They coordinate. There is no evidence that they mediate anything.

## Limitations

Three, and the first is the one I would flag to governance. DIAL, which produces the strongest results, works by backpropagating gradients *through* the communication channel during training. The channel is differentiable at learning time and discrete only at execution. That is a meaningful concession, because the case ARC-009 actually contemplates — two REE instances, separately instantiated, exchanging discrete symbols — is the harder one, and RIAL, the discrete-throughout variant, does worse. An architecture that reads this result as "discrete channels work" is reading past the mechanism that made it work.

Second, the protocols are learned per task and per agent pair. Nothing here demonstrates a protocol that survives a change of partner or a change of task. A *layer*, in the sense ARC-009 means, ought to be reusable; what is demonstrated is a bespoke code negotiated afresh each time. Third, the environments are small and hand-constructed, and the authors say plainly that a set of engineering innovations was essential for success — which tells you the effect is real but not robust to naive implementation.

## The substrate gap, stated plainly

ARC-009 is registered `epistemic_category: substrate_conditional`, and its own field notes are blunt about why: the multi-agent environment (ARC-047) is unbuilt and gated to v5, and the symbol channel (MECH-014) is a prose interface sketch with no implementation, no confidence score and no queued experiment. Neither layer exists in ree-v3. No amount of external literature changes that. What this entry does is establish that *if* both layers were built, the first of the claim's three evidence criteria would be likely to come out positive, because it already has elsewhere. That is a statement about the claim's plausibility and about the value of building the substrate — not a measurement of REE, and it should not be counted as one.

## Provenance

arXiv:1605.06676; published in Advances in Neural Information Processing Systems 29 (NIPS 2016), pp. 2137–2145. No DOI is assigned to the NIPS proceedings version; recorded as null rather than omitted, per the interface contract's "checked, none exists" convention.
