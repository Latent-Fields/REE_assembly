# Bench & Lench 2013 — On the Function of Boredom

[DOI](https://doi.org/10.3390/bs3030459) · PMID 25379249 · *Behavioral Sciences* 3(3):459-472

## What the paper argues

A functional-emotion review that integrates disparate empirical strands — boredom proneness scales, sensation-seeking literature, school and work disengagement — under one functional account: boredom motivates the pursuit of new goals when the current goal is no longer beneficial. The paper is the canonical citation for the goal-pursuit-shift framing; it sits between Eastwood's definitional account and van Tilburg's emotion-differentiation work in conceptual depth, providing the integrative function-talk that the other two presuppose.

## Why this matters for ARC-067

The contribution is the *discharge condition*. Eastwood defines the state, Westgate decomposes its causes, van Tilburg differentiates it from neighbours; Bench & Lench specify what the state is *for*. For ARC-067 this means: the aversive accumulator is not just a flag of low-engagement, it is a recruiter of *trajectory shift*. This distinguishes ARC-067 architecturally from ARC-068 opportunity cost: opportunity cost penalises passive trajectories generally; boredom-driven shift penalises *this* trajectory specifically because the agent has been on it long enough for the engagement-rate to fall.

In ARC-067 implementation terms, this means the downstream of the engagement-rate aversive should bias E3 toward NEW candidate trajectories, not merely toward action over no-op. The cleanest mechanism is to couple the aversive output to a substrate-level inhibition of the recently-committed trajectory or trajectory-class — a sort of "stay off this path" recency penalty that activates above an aversive threshold. This composes naturally with the existing MECH-260 dACC anti-recency substrate; ARC-067 might effectively be MECH-260 anti-recency under explicit aversive control, fired by engagement-rate failure rather than by the dACC's own monitoring.

The boredom-proneness-and-risk-taking literature (cited extensively within Bench & Lench) provides a failure-mode anchor: pathological ARC-067 over-firing should reproduce risk-taking and impulsivity signatures. This is consistent with the boredom-proneness clinical literature and gives a candidate diagnostic for substrate calibration.

## Limitations and confidence

Behavioral Sciences (MDPI) is solid but not first-tier; the paper is review-level rather than original empirical work, and the goal-shift function is inferred from a heterogeneous body of empirical evidence rather than from a single direct test. The boredom-proneness scales literature is methodologically uneven and mixes trait and state measures. Confidence aggregate 0.66 — strong mapping fidelity for the goal-shift verdict, but source quality and methodological tightness lower than the Psych Review and Emotion entries.

## Failure signature it would falsify

An ARC-067 substrate that produces aversive valence but no trajectory shift (the agent registers the boredom signal but stays on the current trajectory) fails the Bench & Lench functional account directly. The discharge condition is *off this path*, not merely *act more*. A substrate that satisfies ARC-068 (acts in general) but fails to bias away from the recently-pursued trajectory is functionally inadequate. Conversely, indiscriminate trajectory switching (any new goal, regardless of expected value) is the pathological-ARC-067 failure mode that maps onto clinical impulsivity.
