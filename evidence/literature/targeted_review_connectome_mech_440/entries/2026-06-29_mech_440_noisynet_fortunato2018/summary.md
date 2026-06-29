# Fortunato et al. (2018) — Noisy Networks for Exploration

**Claim tested:** MECH-440 (state-conditioned self-annealing noise floor; NoisyNet learned-parametric-weight-noise analog)
**Direction:** supports · **Confidence:** 0.85
**Source:** ICLR 2018; arXiv:1706.10295. [DOI 10.48550/arXiv.1706.10295](https://doi.org/10.48550/arXiv.1706.10295) · <https://arxiv.org/abs/1706.10295>

## What the paper did

NoisyNet adds parametric noise directly to a network's weights and lets the *scale* of that noise be learned. Each weight (or, in the factorised-Gaussian variant, each input and output unit) carries a trainable standard-deviation parameter sigma; both the mean weights and the sigmas are optimised by ordinary gradient descent. The induced stochasticity in the weights propagates through the forward pass into the policy, so the agent's action choices vary — and that variation *is* the exploration mechanism. Fortunato et al. replace the conventional heuristics (epsilon-greedy for DQN/dueling, entropy reward for A3C) with NoisyNet and report substantially higher Atari scores across a wide range of games, in some cases moving the agent from sub- to super-human. The factorised variant exists specifically to cut the number of noise random variables from one-per-weight to one-per-input-plus-one-per-output.

## Why it is near-identity for MECH-440

MECH-440 names NoisyNet as its external analog, and the match is unusually tight — this is not a cross-domain analogy but essentially the algorithmic specification of the claim. MECH-440 asks for learned per-parameter factorised-Gaussian weight noise at the E3 selection head, and it asks for three specific properties, each of which NoisyNet exhibits:

1. **It propagates into the committed action.** This is the crux. MECH-313's tonic floor was registered as a post-softmax temperature, and V3-EXQ-687 found it *non-propagating* — invisible to the argmax (selected_action_entropy = 0.0, the entropy-only artefact the degeneracy gate caught). NoisyNet's noise lives in the weights, upstream of the argmax, so it changes *which* action is selected rather than being a discarded pre-commit perturbation. That is exactly the failure mode MECH-440 is built to escape.
2. **It is state-conditioned by construction.** Weight noise multiplies state-dependent activations, so the same sigma perturbs different states differently — no hand-set per-state schedule required. MECH-313's state-independence was the biologically under-specified part; NoisyNet supplies the state-conditioning for free.
3. **It self-anneals.** Because sigma is gradient-trained, it falls where the policy is confident and (in principle) stays up where exploration still pays, so the floor does not wash out uniformly.

The build is already staged behind a no-op default (sigma_init = 0 / flag OFF ⇒ bit-identical), which is the right way to introduce it.

## The honest boundary — why this is support, not proof

NoisyNet is demonstrated on Atari value-based agents. It establishes that learned weight noise propagates into action selection and improves exploration *in general*. It does **not** establish that the mechanism relieves REE's *specific* committed-action-diversity ceiling (MECH-439, F at 88–89% of committed-selection variance). Two concrete reasons to withhold full confidence:

- The same-day confirmed cluster autopsy `failure_autopsy_704b-706b-conversion-ceiling_2026-06-27` re-rooted the committed-action-class conversion ceiling. If that root sits *upstream* of the selection head, then weight noise at the E3 head can change which action is argmax without increasing the diversity of committed action *classes* — i.e., reproduce the 687 entropy-only artefact in a new guise. Propagation into selection is necessary but may not be sufficient.
- The "stays up where exploration pays" property is a property of the gradient, not a guarantee. On a task that does not reward exploration, learned sigma can anneal toward zero everywhere and the floor collapses.

So I read this as strong, well-specified support for the *mechanism* — confidence 0.85, with mapping fidelity high (0.92) because it is the named analog and transfer risk the binding term (0.45) because the REE-specific benefit is exactly what the pending V3 validation experiment must decide, and the 704b–706b autopsy gives a real path by which it could fail. The literature tells us the tool is the right tool; it does not tell us the ceiling will yield to it.
