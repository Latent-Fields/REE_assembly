# Jang & Kim (2022) — the competence split is real, but initialisation entropy can produce it without any epistemic-deficit drive

**Claim tested:** Q-089 — does epistemic-deficit-driven information-seeking explain the cold-start competence split, as opposed to environmental difficulty, initialisation, premature death, or curriculum timing?

**Direction:** mixed · **Confidence:** 0.6

## What the paper did

According to PubMed, Jang & Kim studied how *initial policy entropy* — the randomness of the freshly-initialised agent's action distribution — affects exploration and eventual learning success in deep RL on discrete-action (Atari) tasks. Training 50 differently-initialised models across 8 games, they found: (1) low initial entropy significantly raises the probability of outright learning failure; (2) the natural distribution of initial entropy is biased toward low, exploration-inhibiting values; and (3) initial entropy depends on both the random weights and the task and is hard to control. They then introduced "entropy-aware initialisation," which seeds the agent with high initial entropy, and showed it sharply cut learning failures — e.g. Freeway 25→6, Pong 35→10, Qbert 9→0 failures out of 50 — and improved performance, stability and speed. [DOI](https://doi.org/10.3390/s22155845)

## Why it speaks to Q-089 — both ways

This is the most important single source in the pull, because it is a direct machine-class instance of the exact phenomenon Q-089 exists to explain, and it cuts against Q-089's mechanism at the same time.

**The supporting half.** Identical-architecture agents differing *only in random initialisation* either escape or fail to escape a competence floor, and which fate they meet is decided in the *early* learning stage. That is precisely the shape of REE's observed cold-start competence split: a variance in outcome across seeds, set early. So Q-089 is not chasing an artefact — seed-level competence splits are a real, reproducible, expected feature of RL cold-starts, and the split's early-stage locus matches the claim's confirming signature about early orient-mode entry.

**The weakening half.** The *cause* Jang & Kim identify is not an epistemic-deficit accumulator resolving target-bound uncertainty. It is initial policy entropy driving *undirected* exploration — the paper says low initial entropy "leads to learning failures by inhibiting exploration" because the agent repeats one action with high probability. That is exploration collapse, an initialisation phenomenon, and it is one of the very alternatives Q-089 lists as a disconfirmer ("initialisation"). Worse for the hypothesis, the split can be *largely removed* by an initialisation knob with no information-seeking mechanism invoked at all. So a simpler, mechanism-free account reproduces the headline signature Q-089 wants to attribute to MECH-482/MECH-483.

## The mapping caveat that matters

The crucial distinction is *directed vs undirected* exploration. Q-089's mechanism is directed, target-bound uncertainty resolution; Jang & Kim's driver is undirected policy entropy. So this is not a null result and not a refutation — it is evidence that a **rival explanation is real, large, and machine-class-appropriate**. It does not rule out that an epistemic-deficit signal *also* operates in REE. But it sets the bar Q-089's confirming experiment must clear: the epistemic-deficit trajectory statistic has to predict the split *over and above* an initial-entropy / undirected-exploration-collapse control. If REE's competence split turns out to be entropy-collapse under another name, Q-089 falsifies.

## Confidence reasoning

Source quality moderate (0.6 — Sensors is mid-tier, but this is a genuine controlled experiment with quantified per-task failure counts, not a think-piece). Mapping fidelity high (0.7): it directly instantiates a seed competence split *and* directly operationalises the initialisation confound. Transfer risk is the lowest in the set (0.35): deep RL, discrete action — the closest machine class to REE. Net 0.6, and the direction is genuinely mixed: it raises confidence that the split is real and worth explaining while lowering confidence that REE's specific epistemic-deficit mechanism is the explanation rather than initialisation.
