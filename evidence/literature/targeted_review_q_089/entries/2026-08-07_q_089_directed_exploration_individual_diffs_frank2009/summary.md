# Frank, Doll, Oas-Terpstra & Moreno (2009) — directed exploration is a real, individually-varying, dissociable mechanism

**Claim tested:** Q-089 — does epistemic-deficit-driven information-seeking (a MECH-482 accumulator + MECH-483 orient/survey regime) explain the observed cold-start competence split among seeds, as opposed to environmental difficulty, initialisation, premature death, or curriculum timing?

**Direction:** supports (mechanism plausibility only) · **Confidence:** 0.5

## What the paper did

According to PubMed, Frank et al. gave human adults a temporal decision-making task and fit a reinforcement-learning model that separates two behavioural tendencies: *exploitation* (incrementally adjusting responses toward options that have paid off) and *directed exploration* (choosing an option in proportion to Bayesian uncertainty about whether it might beat the current best). They then asked which genes predicted which parameter. Two striatal-dopamine genes (DARPP-32, DRD2) tracked exploitation; a prefrontal-dopamine gene (COMT) tracked directed exploration specifically. The model fits showed these were *independent* parameters of the same learning system. [DOI](https://doi.org/10.1038/nn.2342)

## Why it speaks to Q-089

Q-089's whole framing presupposes that an agent's tendency to seek information in proportion to resolvable uncertainty — REE's epistemic-deficit accumulator feeding an orient/survey regime — is a mechanism that (a) genuinely exists as something distinct from raw reward-learning, and (b) can vary from agent to agent. This paper is about as clean a demonstration of both as the human literature offers: directed exploration is not a re-description of good learning, it is a separable, uncertainty-proportional drive with its own neural substrate (prefrontal cortex, COMT), and it varies systematically across individuals. So the *premise* of Q-089 — that seeds could differ in how strongly and how early they resolve target-bound uncertainty, independently of how "good" they are — is biologically well-founded rather than a just-so story.

## The mapping, and where it breaks

The honest translation is narrow. What transfers is: "an uncertainty-proportional information-seeking parameter is real, dissociable, and individually variable." What does **not** transfer is the load-bearing part of Q-089 — that *variation in this parameter causes the competence split, and does so better than the initialisation / difficulty / premature-death / curriculum-timing alternatives*. Frank et al. never test a competence split at all; they correlate a genotype with a model parameter. The unit of variation is also wrong-shaped: between-human-genotype differences are a weak analogue for between-random-seed differences in one RL substrate, where there is no genome and the "directed-exploration parameter" is itself an emergent property of initialisation and dynamics — exactly the confound Q-089 is trying to hold constant. There is even a risk the mechanism is unobservable in REE: the task here *signals* uncertainty explicitly, whereas a sparse REE environment may not, so the orient-mode statistic Q-089 needs could be floor-pinned across seeds (the claim's own non-degeneracy precondition).

## Confidence reasoning

Source quality is high (0.85 — Nature Neuroscience, robust double dissociation, canonical). Mapping fidelity is only moderate (0.6): it grounds the mechanism's existence, not the causal-split test. Transfer risk is high (0.55: human genotype → RL seed; signalled-uncertainty task → sparse REE env). Net 0.5 — genuine support for the *plausibility* of Q-089's mechanism, contributing nothing to whether the mechanism actually out-explains the mundane confounds. It should raise the prior that the hypothesis is worth substrate-testing, not the posterior that it is true.
