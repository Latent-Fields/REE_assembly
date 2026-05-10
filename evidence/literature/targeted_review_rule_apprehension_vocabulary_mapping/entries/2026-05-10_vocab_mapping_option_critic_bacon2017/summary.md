# Bacon, Harb & Precup 2017 -- Option-Critic: end-to-end option discovery

## What the paper did

Bacon, Harb and Precup take the formal options framework of Sutton, Precup & Singh 1999 and derive *policy-gradient theorems* for both (a) the intra-option policy and (b) the termination function, allowing end-to-end learning of options from environment reward. The key technical contribution is showing that the gradient of the discounted return with respect to the termination parameters has a clean form that can be learned alongside the option policy and the policy-over-options, with no pseudo-rewards, no pre-specified subgoals, and no separate option-discovery phase. They demonstrate the algorithm on tabular Four-Rooms, Pinball, and Atari games.

## Key findings relevant to the rule-apprehension vocabulary question

If Sutton-Precup-Singh 1999 gave the formalism for what an option *is*, Bacon 2017 gave the algorithm for how an option is *learned*. That is exactly the missing ingredient when REE's ARC-064 + MECH-317 are read as option-discovery machinery: there is a published, well-tested architecture, with policy-gradient theorems, that does the job end-to-end without subgoals.

The mapping to the working REE terminology:
- *Intra-option policy* = the rule's behavioural content (the policy fragment ARC-062's gated_policy implements).
- *Termination function* = MECH-317's chunk boundary / the "this rule no longer applies" signal.
- *Policy-over-options* = ARC-062's gating layer / discriminator.

So the rule-apprehension cluster can be re-read end-to-end as a (gating-policy, intra-option-policy, termination) triple, learned via the option-critic gradient.

## How the findings translate to REE

The transfer is direct for ARC-062 (top-down rule application) and the chunking arm of ARC-064 (the MECH-317 dorsolateral-striatum action-chunking analog). Both have a clear option-critic counterpart. Transfer to MECH-316 (hippocampal-monosynaptic-CLS-analog cross-episode-regularity-extraction) is partial -- regularity-extraction without a reward signal is closer to Eysenbach 2018 DIAYN's mutual-information-with-skill-label territory than to option-critic's reward-driven gradient.

There is a particularly useful diagnostic transfer here. Option-critic has a well-known failure mode called *option-collapse*: under naive training, the discovered options either degenerate to extremely short single-step options (trivial) or become indistinguishable from each other (also trivial). The literature has spent eight years developing regularisation tricks to prevent this (entropy regularisation on terminations, deliberation-cost penalties, etc.). REE's V3-EXQ-543 hit option-collapse: the gated-policy ARM_1c at-init produced inert gating, and seed-2 was byte-identical to the baseline arm -- the same diagnostic pattern. We get a body of mitigation literature for free if we adopt this vocabulary.

## Limitations and caveats

Option-critic requires a reward signal to drive learning. The reward-agnostic part of ARC-064 -- regularity extraction over the trajectory record without value signal -- does not fit cleanly. The Atari/four-rooms empirical setting is also far from REE's continuous-state substrate; transfer is plausible but not free.

The biggest caveat for vocabulary-mapping purposes: option-critic learns options *jointly with the policy-over-options* in a single end-to-end optimisation. REE's design separates ARC-062 (top-down rule application) and ARC-064 (bottom-up rule discovery) into different timescales (online vs partly offline), which option-critic does not directly model. A faithful adoption would either flatten this separation or extend option-critic with offline-replay-mediated option discovery (Pull 2 territory).

## Confidence reasoning

Scored 0.82. Source quality high (peer-reviewed AAAI 2017, code published, well-cited). Mapping fidelity high because option-critic is the dominant framework for end-to-end option discovery with reward. Transfer risk moderate-high (0.40) because reward dependence and Atari-style action spaces don't transfer literally. The diagnostic-transfer of option-collapse is the unexpected bonus -- it gives REE a literature on a failure mode it has independently encountered, which is exactly the kind of inheritance Pull 4 was commissioned to find.
