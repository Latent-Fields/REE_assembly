# Wilson, Reinhard, Westgate, Gilbert et al. 2014 — Just Think: The Challenges of the Disengaged Mind

[DOI](https://doi.org/10.1126/science.1250830) · PMID 24994650 · *Science* 345:75-77

## What the paper argues

Eleven studies asking what happens when people are placed in a room alone with no external task and instructed simply to think. The participants reported finding the experience unpleasant; preferred mundane external activities to staying with their thoughts; and, in the most-cited demonstration, many chose to self-administer painful electric shocks rather than continue with nothing to do. The effect held across age, gender, instruction variations, and task framings. The paper's contribution is the existence proof: enforced low-engagement is *actively aversive enough to recruit costly action against the self*, which is a remarkable empirical claim and one of the strongest behavioural demonstrations that the do-nothing baseline is not neutral.

## Why this matters for ARC-067

This is the load-bearing R3 paper for the routing-channel verdict. ARC-067's architectural commitment is that boredom-aversive routes through the same downstream consumer as actual harm — engagement-poverty competes for action-selection priority on the same axis as discomfort. The self-shock finding is the cleanest available evidence that this commitment is empirically correct: humans treat boredom-aversive and physical pain-aversive as *exchangeable* enough to trade one for the other. This supports routing through z_harm_a (affective harm stream, SD-011) rather than through a parallel non-aversive engagement-rate scalar that converges only at action-selection. Routing through z_harm_a means the boredom and pain signals are added on the same axis, which is exactly what Wilson's participants behaviourally demonstrate when they choose shock over continued disengagement.

For the R2 timescale verdict, the 6-15 minute experimental window establishes that ACUTE boredom (tens of episodes scale on the REE side) is measurable within a single session. The substrate cannot only produce aversive accumulation over chronic horizons; the acute mechanism must fire on the order of minutes-of-real-time. This anchors the acute side of the R2 split that the user pre-registered as candidate.

For the architectural commitment more broadly, Wilson 2014 is also the strongest empirical pushback against any REE design that treats no-op as zero-cost. The current REE substrate effectively does this — a well-fed safe familiar agent has no gradient to act, with only MECH-313 noise floor preventing inertia. Wilson's finding shows that humans do not occupy this no-cost-no-op equilibrium, and the family-level non_deficit_action_drives commitment is partly *about* matching this human signature.

## Limitations and confidence

The experimental paradigm is enforced disengagement — participants cannot leave and have no available task. ARC-067's natural setting is open-ended foraging where the agent could in principle act but engagement-by-current-actions is low. The mapping is conceptually direct (Wilson's setup is essentially the human version of the well-fed-safe-familiar-no-z_goal regime ARC-067 targets), but the quantitative thresholds — how many minutes until aversive crosses act-recruiting threshold, what proportion of capacity-states cross — are not directly transferable. Confidence aggregate 0.78 — Science venue and 11-study design put source quality near ceiling; mapping fidelity strong for the routing-channel and architectural-commitment verdicts; modest transfer-risk reservation for the enforced-vs-open-ended-disengagement gap.

## Failure signature it would falsify

An REE substrate that treats no-op as zero-cost — no aversive accumulation under enforced disengagement — fails to reproduce the Wilson finding directly. The agent should, after a sufficient interval, prefer a costly action (a small but nonzero z_harm cost or resource cost) to continued no-op when no other action is available. This is the cleanest single-experiment validation criterion for ARC-067 the literature provides.
