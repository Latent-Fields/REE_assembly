# Wilson, Geana, White, Ludvig & Cohen (2014) — directed vs random exploration are separable strategies

**Claim tested:** Q-089 — does epistemic-deficit-driven information-seeking explain the cold-start competence split, as opposed to environmental difficulty, initialisation, premature death, or curriculum timing?

**Direction:** supports (construct validity) · **Confidence:** 0.5

## What the paper did

According to PubMed, Wilson et al. introduced the "Horizon task": participants make explore-exploit bandit choices in games that are either short (a single choice, horizon 1) or long (six sequential choices, horizon 6). By modelling behaviour across the two horizons they separated two exploration strategies — a *directed* strategy that biases choices toward the more informative (less-sampled) option, and a *random* strategy in which added decision noise produces exploration by chance. Both information seeking and decision noise increased in the long-horizon condition, showing that humans deploy — and can up- and down-regulate — both strategies in the service of exploration. [DOI](https://doi.org/10.1037/a0038199)

## Why it speaks to Q-089

REE's proposed mechanism draws exactly this line: an epistemic-deficit accumulator (MECH-482) driving an orient/survey regime (MECH-483) is the *directed*, information-seeking arm of exploration, as opposed to undirected policy stochasticity. The value of this paper for Q-089 is construct-level: it is the canonical demonstration that "directed exploration" is not just a re-description of exploration in general — it is a dissociable, quantifiable behavioural component that co-exists with, and is controllable independently of, exploration noise. That legitimises the Q-089 measurement plan of tracking an *information-seeking trajectory statistic* (orient-mode entry, uncertainty-reduction rate) separately from generic behavioural variability. If the two were not separable, the whole hypothesis would be unmeasurable.

## The mapping, and where it breaks

What transfers is the *decomposability* of exploration into a directed information-seeking channel and a random-noise channel — the partition REE needs to be able to draw in order to state Q-089 at all. What does **not** transfer is the causal core of Q-089. Wilson et al. manipulate directed exploration *within* each subject by changing the horizon; they do not show that agents differ *stably* in directed exploration, nor that such differences predict who ends up competent. And the task hands the learner exactly the two things a sparse REE cold-start withholds: an explicit reward structure and a defined horizon. In REE the orient/survey signal must emerge from the substrate itself, so the clean directed-exploration measure available here may be floor-pinned or degenerate across seeds — which is precisely the non-degeneracy precondition Q-089 flags as a self-route to `substrate_not_ready`. None of Q-089's disconfirming alternatives (initialisation, difficulty, premature death, curriculum) are touched.

## Confidence reasoning

Source quality high (0.8 — the field-defining Horizon-task paper). Mapping fidelity moderate (0.6): it validates the directed/random construct REE relies on but tests a within-subject manipulation rather than a between-seed competence split. Transfer risk high (0.55: signalled-horizon human bandit → sparse RL cold-start). Net 0.5 — genuine support for the *measurability and reality* of the directed-exploration channel, silent on whether variation in it explains the split.
