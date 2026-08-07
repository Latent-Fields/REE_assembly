# Kanen et al. 2021 — Serotonin Depletion Impairs Reversal Learning (Dose-Dependently)

**Claim tested:** ARC-005 ("Control plane routes precision and modes")
**Direction:** supports · **Confidence:** 0.74

## What the paper did

Two independent experiments (N = 97 total), double-blind, randomized, placebo-controlled. Healthy volunteers underwent acute tryptophan depletion — lowering brain serotonin — and then performed serial reversal tasks: instrumental (stimulus–response–outcome, learning which action is optimal and re-learning when contingencies flip) in Experiment 1, and Pavlovian (skin-conductance responses to a shock-predictive cue that swaps) in Experiment 2. According to PubMed / Nature, depletion impaired the updating of both actions and autonomic responses to changed contingencies, and — the load-bearing detail — the **reversal deficit magnitude correlated with the extent of tryptophan depletion**.

## Why this is the most on-target channel entry

REE names channel 1 as "5-HT rigidity" — the serotonergic setting governing how readily the agent abandons a committed strategy. This is the direct biological homologue: serotonin causally and dose-dependently sets how readily behavior updates to changed contingencies. And the *dose-dependence* is the single most important feature for ARC-005, because it is exactly the property V3-EXQ-848b's load-bearing criterion, `C_precision_monotonicity`, is trying to demonstrate: the downstream readout should track the channel setting **monotonically**. Here the biology delivers that monotonicity cleanly at N=97 — the more you lower serotonin, the larger the flexibility deficit.

## What it says about REE's ~180×-below-noise result

The contrast is stark and it is the point of including this entry. REE's implementation of this very channel produces only 4/10 units clearing |rho| ≥ 0.6 and a raw effect ~180× smaller than cross-seed noise. The biological homologue of the same neuromodulator produces a replicable, behaviorally consequential, *dose-graded* downstream effect. Biology does not predict that manipulating the serotonergic rigidity channel yields a near-noise-floor footprint; it predicts a monotone, detectable one. That gap is more consistent with the 848a implementation finding — the dACC adapter never trained on non-degenerate goal_proximity, its response 4–7 orders of magnitude below the scale of the other bias components — than with a genuine biological ceiling. The channel *should* route; REE's current wiring of it largely does not.

## Honest caveats

The construct bridge is the main one, and I have kept mapping_fidelity at 0.68 because of it: reversal learning is a cognitive-*flexibility* readout, and serotonin's role in flexibility is far better established than its identification with "precision-weighting" *per se*. So this entry supports "REE's channel-1 neuromodulator has a real, dose-dependent, monotonic downstream effect in the biology" — strong evidence that the channel routes — without claiming reversal deficit and E3 log10-precision are the same measurement. Acute tryptophan depletion is also a strong, global manipulation, an upper bound relative to REE's within-range ladder step.

*According to PubMed. Kanen JW, Apergis-Schoute AM, Yellowlees R, et al. Molecular Psychiatry 2021;26(12):7200-7210. [DOI](https://doi.org/10.1038/s41380-021-01240-9)*
