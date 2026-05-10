# Constantino & Daw 2015 -- Learning the opportunity cost of time in patch foraging

**Citation:** Constantino SM, Daw ND. Learning the opportunity cost of time in a patch-foraging task. *Cogn Affect Behav Neurosci*. 2015;15(4):837-53. PMID: 25917000. [DOI](https://doi.org/10.3758/s13415-015-0350-y).

## What the paper does

Constantino and Daw run two human behavioural experiments in a virtual patch-foraging task. Subjects forage for apples in a virtual environment, deciding whether to harvest a depleting tree (short delay, smaller reward, exponentially decelerating yield) or to move to a new tree (longer delay, replenished yield). Opportunity cost is varied parametrically across blocks. They then perform a head-to-head model comparison: the marginal-value-theorem (MVT) threshold-learning rule -- in which the opportunity-cost threshold is estimated as a long-window average over previous rewards, exactly Niv 2007's avg-reward-rate scalar -- is tested against temporal-difference (TD) learning, the predominant incremental learning theory in computational neuroscience. Trial-by-trial decisions are explained decisively better by the MVT threshold-learning rule. Subjects adjust to blockwise opportunity-cost changes with a kernel consistent with a slow EMA over reward history rather than a fast TD-style update. The paper's contribution is empirical: it tests, in humans, which kernel structure underlies opportunity-cost-driven decision-making.

## Why this matters for ARC-068

The R2 verdict on ARC-068's reward-rate kernel is the question this paper most directly answers. The user's R2 question lists three options: (a) CURRENT predicted reward rate (fast estimator), (b) HISTORICAL average reward rate (slow EMA), (c) both. Constantino & Daw 2015 give a decisive empirical answer in favour of (b), with two qualifications. First, the kernel must be slow enough to integrate across multiple trials but fast enough to track blockwise changes -- a window covering tens of episodes / minutes of agent-time, not a session-long flat average. Second, the model comparison was between MVT-threshold-learning and TD-learning specifically; the paper does not test a hybrid current+historical model, so option (c) is not directly ruled out, only deemed unnecessary for the data.

Combined with Niv 2007 (which derives the long-window kernel theoretically) and Kolling 2016 (which characterises a separate current-environmental scalar in dACC), the synthesis R2 verdict is: PRIMARY recommendation is the long-window historical EMA (Niv / Constantino-Daw kernel) for ARC-068 specifically. SECONDARY fallback is a hybrid estimator if the long-window kernel produces poor adaptation in highly non-stationary environments (a regime Constantino & Daw did not test). The Kolling current-environmental scalar is what SD-032b already uses; the kernel distinction between SD-032b (current-environmental) and ARC-068 (long-window historical) is what most cleanly separates them at the architectural level under the R1 verdict.

The paper also matters indirectly for R1 (substrate boundary). The MVT threshold-learning rule is the computational substrate for opportunity-cost-on-time; it is the same rule Niv attributes to mesolimbic DA. SD-032b's dACC foraging_value scalar is on a different point in the kernel space (current-environmental average per Kolling). The MVT-threshold-learning rule cleanly separates from the dACC foraging_value computation by kernel rather than by substrate. The R1 verdict therefore: the architectural separation is via TIMESCALE / KERNEL, not via SUBSTRATE.

## Caveats

The patch-foraging task is task-engaged. Subjects are deciding between explicit harvest-or-move actions. ARC-068's always-on framing fires when no specific task is in scope -- the well-fed-safe-familiar regime where no explicit foraging decision is being made. The kernel form (slow EMA over reward history) transfers principled to the always-on regime, but the empirical evidence is from task-engaged subjects. Treat Constantino & Daw 2015 as evidence for the kernel form, not for the always-on regime.

A second caveat: the model comparison was between two specific computational alternatives (MVT-threshold-learning vs TD). Other plausible models (current+historical hybrid; Kolling-style search-value-only; Bayesian-belief-updating) were not tested. The verdict 'long-window EMA wins' is correct for the MVT-vs-TD comparison; it does not mean other long-window models are ruled out.

A third caveat: the kernel window length is parametric in the paper's model fits but not deeply explored. Different subjects fit slightly different window lengths. For REE, the recommendation is to make the window length a configurable parameter and explore it empirically rather than fixing it from this paper's central tendency.

## Confidence reasoning

Source quality high (parametric human behavioural design, principled model comparison, peer-reviewed in a strong neuroscience journal). Mapping fidelity strong: the empirical question precisely matches R2; the design tests MVT against TD and finds MVT decisively better; the kernel implication transfers to ARC-068 as primary recommendation. Transfer risk moderate (human task-engaged subjects; ARC-068 cares about no-target regimes; kernel form transfers but not the regime itself). Aggregate 0.82.

According to PubMed, this paper appears under the cited PMID with the DOI as listed.
