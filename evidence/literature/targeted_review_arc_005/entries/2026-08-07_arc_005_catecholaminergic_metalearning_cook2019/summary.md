# Cook et al. 2019 — Catecholaminergic Modulation of Meta-Learning

**Claim tested:** ARC-005 ("Control plane routes precision and modes")
**Direction:** supports · **Confidence:** 0.73

## What the paper did

102 healthy adults completed a probabilistic reinforcement-learning task with interleaved *stable* phases (fixed reinforcement probability) and *volatile* phases (probabilities changing every 10–30 trials), under the catecholamine transporter blocker methylphenidate versus placebo. The question was whether enhancing catecholamine function changes a *meta-learning* parameter — the learning rate — as a function of environmental volatility. According to PubMed / eLife, it did: under methylphenidate, participants showed higher learning rates in volatile relative to stable phases than under placebo, a causal demonstration that a catecholaminergic control channel adjusts how strongly evidence updates belief given the uncertainty regime. The effect was significant for *direct experiential* learning but not for *inferred-value* learning.

## Why this is the tightest mapping in the review

Of the four entries, this one maps most literally onto what ARC-005 says the control plane does. "Learning rate as a function of volatility" *is* a precision-weighting readout — it is the quantity that says how much incoming evidence should move the internal state given current uncertainty, which is precisely what a precision router routes. So this paper is the cleanest biological instance of "a control channel causally routes a precision readout," which is the ARC-005 existence claim. On the existence question, it is a clear supports.

## What it adds to the magnitude story

Two things. First, *detectability*: the routing effect was a real, statistically significant shift in a 102-person sample — precision routing in the biology produces a footprint that a well-powered study detects, categorically unlike REE channel 1's ~180×-below-noise effect, which no comparable sample would recover. Second, *pathway-specificity*: the effect appeared for experiential learning but not inferred-value learning. That is the biological version of REE's channel-by-channel asymmetry — a precision manipulation only routes where the neuromodulator is actually wired into the update. The REE analogue of the "inferred-value" pathway is a channel wired to a degenerate or off-scale upstream signal (channel 1's dACC adapter reading collapsed goal_proximity): the manipulation lands on nothing, and the readout stays flat not because precision-routing is biologically negligible but because *this particular* channel is not transmitting.

## Caveats

Methylphenidate elevates both dopamine and noradrenaline, so this is not a clean single-channel manipulation, and the effect is expressed as a model-fit learning-rate parameter rather than a single standardized Cohen's d — which is why I lean on Nuiten 2024 for the precise magnitude and use this paper for detectability and pathway-specificity. As with every pharmacology entry, the drug push is stronger than REE's within-range ladder step, so these are effect sizes for a strong intervention.

*According to PubMed. Cook JL, Swart JC, Frobose MI, Diaconescu AO, Geurts DE, den Ouden HE, Cools R. eLife 2019;8:e51439. [DOI](https://doi.org/10.7554/eLife.51439)*
