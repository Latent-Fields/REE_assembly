# Funahashi, Bruce & Goldman-Rakic (1989) — Mnemonic coding of visual space in dlPFC

**Claim:** ARC-063 (rule-apprehension architectural slot, strong reading: a distributed CandidateRule field with tolerance-gated availability). **Direction:** supports (fork-A side of the maintenance fork). **Confidence:** 0.74.

## What the paper did

Funahashi and colleagues recorded single units in the dorsolateral prefrontal cortex (principal sulcus) of macaques performing an oculomotor delayed-response task: a brief peripheral cue, a delay of several seconds during which the monkey fixates centrally and nothing is on screen, then a saccade to the remembered location. The signature finding is that individual PFC neurons fire *tonically and selectively* through the delay, with each neuron's elevated firing tuned to a particular cued location ("memory fields"). The representation of the absent cue is carried by sustained spiking across the input-absent epoch, and the delay activity predicts the upcoming response. This is the canonical empirical anchor for the "persistent delay-period activity" account of working memory — fork A in the V3-EXQ-666 autopsy.

## Why it matters for the CRF

This is the **existence proof for the class** ARC-063 instantiates. The brain demonstrably maintains a behaviourally-relevant latent across an epoch in which its driving input is gone, which is precisely what the CandidateRuleField needs: a minted rule must stay "available" between the moments its context recurs. For the CRF's *currently-matched-and-selected* rule, Funahashi licenses a sustained-activity maintenance term — keep the engaged rule's availability elevated for a window after it fires, rather than letting it decay immediately. That is the disciplined reading of fork A.

## The caveat that keeps this from settling the fork

The delayed-response paradigm holds exactly **one** engaged item per trial — the cue that was just shown and will imminently be acted on. It is the attended, selected memorandum. The CRF's actual failure mode (666: `crf_frac_active` collapses to 0.016 once rules are differentiated via e2_world_forward) is not maintaining the *engaged* rule but holding a **pool of ≥2 differentiated rules**, each of which matches only a narrow slice of contexts and is *unselected* on the overwhelming majority of ticks. Funahashi shows nothing about whether an unselected, sparsely-matching rule keeps firing across the long gaps between its matches. Reading this paper as "every available rule must keep spiking every tick" would over-extend it — and that over-extension is exactly the assumption baked into the CRF's per-tick `availability` EMA that the autopsy identified as wrong. So this paper supports fork A *for the engaged rule only*; it cannot underwrite a persistent-firing maintenance scheme for the whole available pool.

## Confidence reasoning

Source quality is near-ceiling (foundational, heavily replicated primate electrophysiology). I discount mapping fidelity to 0.55 because the single-engaged-item paradigm is only a partial match to the CRF's multi-rule-pool maintenance problem, and transfer risk is moderate (macaque PFC to a discrete software rule-field is a mechanism-class transfer). The honest position: this paper proves the maintenance *function* is real and gives fork A a foothold for the selected rule, but the more recent literature (Mongillo 2008; Stokes 2015; Lundqvist 2018, all in this review) is what actually adjudicates *how* an unattended pool is held — and it pushes toward activity-silent maintenance.
