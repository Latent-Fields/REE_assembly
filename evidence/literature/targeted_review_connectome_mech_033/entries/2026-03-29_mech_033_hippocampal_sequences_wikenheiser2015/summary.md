# Summary: Wikenheiser & Redish (2015) — "Hippocampal theta sequences reflect current goals"

**Entry ID:** 2026-03-29_mech_033_hippocampal_sequences_wikenheiser2015
**Claim tested:** MECH-033 (E2 forward-prediction kernels seed hippocampal rollouts)
**Evidence direction:** supports | **Confidence:** 0.74

---

> **PROVENANCE NOTE (2026-08-14, chip `chip-20260814-lit-unrecoverable-identifiers`, and 2026-08-18, chip `chip-20260816-lit-provenance-quarantine`).**
> `source.title` and `source.doi` were repaired on 2026-08-14. The record previously declared the title
> *"Decoupled traversals of the hippocampal sequence reflect decisions about the future"* and
> the DOI `10.1038/nn.3945`. No paper with that title exists (Crossref bibliographic search
> returns nothing resembling it), and `10.1038/nn.3945` is Zhang et al., *"Dopaminergic and
> glutamatergic microdomains in a subset of rodent mesoaccumbens axons"* (Nat Neurosci 18:386-392)
> — an unrelated paper. The record's own `pmid` `25559082` was already correct and is what
> recovered the work: Wikenheiser & Redish, *"Hippocampal theta sequences reflect current goals"*,
> Nat Neurosci 18(2):289-294, DOI `10.1038/nn.3909`. Declared authors, year and venue all already
> matched that paper, so only the title and DOI were wrong.
>
> **RESOLVED 2026-08-18 (GFLAG-0028, quarantine-pending-re-extraction, governance cycle 2026-08-16).**
> The "What the paper did" section below previously described a T-maze with probabilistic reward and
> vicarious-trial-and-error head-scanning at a stationary choice point — the paradigm of Johnson &
> Redish (2007), not of the cited nn.3909 paper. It has now been rewritten against the actual paper:
> a circular-track delay-based foraging task (three feeder sites, rat chooses to wait or move on), whose
> result is that theta look-ahead extends farther on journeys to more distant goals, predicts the
> destination, and does not depend on distance already travelled. Abstract via Europe PMC
> (EXT_ID:25559082); task-structure detail corroborated via secondary sources since PMC full text
> (PMC4428659) sits behind a bot check. `confidence`, `evidence_direction` and `mapping` were re-derived
> against the correct paper (see `record.json`).

---

## What the paper did

Wikenheiser and Redish recorded from hippocampal place cells (CA1) in rats trained to forage on a circular track containing three feeder sites. At each site the rat faced a foraging decision: wait an assigned delay to collect reward there, or move on to the next site — moving on is optimal when the current site's remaining wait exceeds what the next site would require. This is a continuous, repeated foraging task rather than a discrete two-alternative choice point. Using a Bayesian decoder applied within individual theta cycles, the authors reconstructed the "represented position" encoded by the population of active place cells at each moment and asked how far ahead of the animal's true position that represented location extended, and how that look-ahead distance related to the animal's current goal (its intended next feeder).

## Key findings relevant to MECH-033

Theta-cycle look-ahead distance was not fixed — it varied moment-by-moment with the rat's goal. Look-ahead extended significantly farther on journeys toward more distant goals than on journeys toward nearer ones, and the extent of look-ahead was predictive of which site the animal was actually heading to. Critically, the authors also tested the reverse relationship: on arrival at a goal, look-ahead distance was similar regardless of how far the animal had just travelled to get there — that is, the scaling was specifically with prospective (upcoming) goal distance, not retrospective (already-covered) distance. This dissociation is the paper's central result: hippocampal theta sequences encode a forward-looking, goal-referenced representation of the path ahead, not a generic trace of recent locomotion.

## Translation to REE

MECH-033 claims that E2, the fast forward-transition kernel, seeds hippocampal rollouts by iterated application: given z_t and a candidate action, E2 predicts z_{t+1}, and the rollout is built by chaining this prediction forward. A rollout generated this way should, in principle, have a length that reflects how far ahead the evaluation needs to reach — closer goals need fewer forward-kernel applications, distant goals need more. Wikenheiser & Redish's central finding — that theta-sequence look-ahead distance scales specifically with distance to the prospective goal, not with the distance already travelled — is a close behavioural analog of exactly this property. It is stronger and more specific evidence for a kernel-chaining-style rollout mechanism than a generic "the hippocampus projects forward" result would be, because it shows the length of the forward projection is itself goal-distance-calibrated, which is what an iterated forward model matched to a target would need to produce. The destination-predictive property of the sequence is also consistent with the E3-evaluation-of-E2-rollouts framing: the endpoint of the projected sequence carries information about the choice being evaluated.

## Limitations and caveats

The paper documents the *output* of the hippocampal forward process (goal-distance-scaled theta look-ahead) but, as with the previous mis-cited description, does not identify the *circuit input* that seeds or sets the scaling of the sequence. Whether a fast forward-predictor analogous to E2 generates each step, or whether the scaling emerges from intrinsic hippocampal attractor dynamics or a cortical top-down signal, is not resolved by this paper. MECH-033 makes a specific mechanistic claim about E2's role; this paper is consistent with but does not distinguish E2-seeding from these alternatives. The task is continuous delay-based foraging on a circular track (rodent), with no discrete T-junction choice point — a different behavioural structure from multi-step abstract planning, and REE's z_world is an abstract conceptual latent space, not a spatial map.

## Confidence reasoning

Source quality is high: in-vivo tetrode recording during active foraging, published in Nature Neuroscience, with a clean and quantitative prospective/retrospective dissociation rather than a qualitative description. Mapping fidelity is good-to-moderate: the goal-distance scaling of look-ahead is a specific, falsifiable signature that a forward-kernel-chaining rollout would need to produce, which is a tighter mapping than a generic "prospective sequence" result — but the source does not identify a discrete forward-predictor circuit, so the E2-specific attribution remains an REE-side inference. Transfer risk is moderate: continuous circular-track foraging vs multi-step abstract planning, rodent vs architecture. Overall confidence 0.74 — solid empirical support for goal-distance-scaled hippocampal forward rollouts, now correctly grounded in the paper this record actually cites, with the same category of mechanistic gap (seeding circuit unidentified) as the previous description carried.
