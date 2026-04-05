# Kumaran, Hassabis & McClelland (2016) — CLS Theory Updated for Intelligent Agents

**Claim tested:** INV-049 -- offline update phases are a general computational necessity, not a biological contingency.

## Why a 2016 Update Matters for a 1995 Argument

The 1995 CLS paper made its case from connectionist simulations and neuropsychological data. By 2016, DeepMind's DQN agent had independently rediscovered the same solution: experience replay is necessary for stable deep reinforcement learning. Kumaran, Hassabis, and McClelland seized on this convergence as confirmation of a strong claim -- that the two-system, replay-based architecture is not a quirk of biological evolution but a computational necessity that any sufficiently powerful learning system will require. That is precisely what INV-049 asserts.

## The DQN Convergence

The paper makes the case directly: DQN, designed without any biological constraint, introduced experience replay as a technical necessity for stable training. Without it, the network suffered catastrophic interference -- exactly the failure mode the 1995 CLS paper predicted. This convergence is not circumstantial. It reflects the underlying mathematics: distributed representations plus sequential gradient updates equals instability. The solution -- store experiences, replay them during an offline or decoupled update phase, interleave with new learning -- is the same whether you are a mammalian hippocampus or a GPU cluster in London.

## Extensions Beyond the Basic Necessity Claim

The 2016 paper extends CLS in directions relevant to REE beyond the core necessity argument. First, it introduces goal-dependent weighting of replay content: the agent can selectively prioritise which experiences are replayed based on current goals, adding an adaptive dimension to what had been framed as a passive reactivation process. Second, it accommodates rapid neocortical learning for schema-consistent information -- some structure can bypass the slow integration process when it fits existing representations. These extensions matter for REE's architecture (the selectivity of E3-quiescence replay, MECH-092) but are not required for INV-049's more basic claim.

## Relevance to INV-049 and the 'Not a Biological Contingency' Framing

INV-049's critical word is 'general.' The claim is not that sleep-like offline phases are useful for biological brains -- that is uncontroversial. The claim is that any model-building agent with a certain computational profile will require them, regardless of substrate. Kumaran et al. 2016 provides the strongest available evidence for this universality: an artificial system with no evolutionary history and no biological constraints independently converged on the same architectural solution. If the offline replay phase were a biological contingency -- something evolution happened upon for reasons unrelated to the computational problem -- we would not expect to see it emerge independently in systems designed from first principles by engineers.

## Honest Uncertainties

The paper focuses specifically on dual-system architectures and does not attempt to prove that all possible learning systems require offline phases. A genuinely online Bayesian updater with perfect memory access, for instance, might in principle avoid catastrophic interference without a discrete offline phase. INV-049's universality claim therefore rests partly on the assumption that the REE architecture specifically falls within the class of systems this argument covers -- which it does, given the distributed latent representations in E1 and E2, but this should be stated rather than assumed.
