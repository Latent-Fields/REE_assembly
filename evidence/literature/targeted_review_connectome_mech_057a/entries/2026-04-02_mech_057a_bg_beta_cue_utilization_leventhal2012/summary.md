# Leventhal et al. (2012) — Basal Ganglia Beta Oscillations Accompany Cue Utilization

## What the paper does

Leventhal and colleagues recorded simultaneously from motor cortex and basal ganglia in rats performing a cue-guided behavior task. They found that brief beta (~20 Hz) oscillations occurred simultaneously throughout the cortical-BG network. Crucially, beta power increased after cues were used to determine motor output — not simply when movements were suppressed. This challenged the purely inhibitory view of beta and suggested instead that beta reflects a "post-decision stabilized state" that reduces interference from alternative potential actions.

## Relevance to MECH-057a

This paper reframes beta from "movement suppression" to "commitment stabilization" — a critical distinction for MECH-057a. The claim is not that committed sequences suppress all neural activity, but that they suppress *precision updates* (new information that could change the action plan). Leventhal et al.'s finding that beta increases after cue utilization (decision commitment), not just during movement hold, directly supports this interpretation.

In REE, this maps onto MECH-090's BetaGate: after the agent commits to an action sequence, beta elevation in the E3 -> action_selection pathway suppresses new precision-weighted inputs from modifying the chosen trajectory. The completion event (or salient interruption) phase-resets beta, re-opening the update channel.

## The transient vs sustained question

The paper shows transient post-cue beta bursts, not sustained elevation across extended sequences. This is the same timescale concern as with Schmidt et al.'s review: does beta maintain commitment across a multi-step sequence, or does it reset at each step? If the latter, then MECH-057a's sequence-level suppression claim needs either (a) evidence of sustained sequence-level beta, or (b) a mechanism that maintains commitment at a slower timescale than individual beta bursts.

## Confidence reasoning

High-quality electrophysiology in a top journal. The commitment-stabilization reframing is directly relevant. Confidence moderated by the single-trial vs multi-step gap and the rat-to-computational transfer.
