# Loftus et al. 2022 -- Ecological and social pressures interfere with homeostatic sleep regulation in the wild

According to PubMed: Loftus JC, Harel R, Nunez CL, Crofoot MC. *eLife* 2022;11:e73695. [DOI 10.7554/eLife.73695](https://doi.org/10.7554/eLife.73695) (PMID 35229719).

## What the paper did

Tracked a wild group of olive baboons (*Papio anubis*) with triaxial accelerometry and GPS, inferring sleep from movement, across many nights and multiple sleep sites. The design's key feature -- and the reason this entry carries as much weight as it does in the synthesis -- is that the homeostatic variables were **measured rather than assumed**: how long each animal had slept the previous night, and how much it had physically exerted itself during the preceding day.

## Core finding

Baboons slept less when in **less familiar locations** and when sleeping in **proximity to more group-mates** -- and did so *regardless of prior sleep duration or prior day's exertion*. They also did not compensate afterwards with more intense sleep bouts. Waking was synchronised among nearby group-mates through the night. The authors conclude that survival and social priorities outweigh the physiological drive to maintain sleep homeostasis.

## Why this matters for GAP-9

Two separate loads, and they are the two the chip explicitly asked about.

**1. It refutes the single-accumulating-scalar model, with the controls in place.** Plenty of sources establish that risk *matters* for sleep. This one establishes that accumulated homeostatic need was present, was quantified, and *lost anyway*. That is what makes an allostatic safety term a genuinely different logical type in the synthesis's Verdict 1 -- not a third addend into one drive scalar, but a term that can override the accumulator outright. If REE's within-life trigger is a single need threshold with no allostatic input, this paper is the direct prediction of how it will misbehave: the agent will sleep on schedule in exactly the places a real organism refuses to.

**2. The operative variable was location UNFAMILIARITY, with no current harm.** Nothing was attacking the baboons. The signal that suppressed sleep was an expectation about unobserved risk in an unfamiliar place. This is the cleanest field evidence available for the organism-review Section 8 question -- whether "safe enough to sleep" should key on *predicted future* harm rather than current harm level -- and it answers in the predicted direction. It also directly indicts a current-harm-sourced threat term (which is what MECH-286 has today): such a term is definitionally near-zero in exactly the situation this paper is about.

## Where the paper's coverage ends

Observational field data, so the ecological and social pressures are correlational rather than manipulated. The authors cannot cleanly separate predation risk from social disturbance -- both unfamiliarity and group-mate proximity were associated with lost sleep, and the latter is plausibly about jostling and social monitoring rather than predators. For REE this is largely moot, since there is no social channel and only the familiarity arm transfers; but the entry should not be cited as isolating predation specifically. Sleep is also inferred from accelerometry, not EEG, so nothing here speaks to sleep *architecture* (that is Lima 2005's contribution in this pull).

## Confidence reasoning

Source quality 0.92 -- eLife, peer-reviewed with published reviews, novel field methodology on a well-studied system. Mapping fidelity 0.90, unusually high: the paper measured and controlled for precisely the homeostatic quantities REE's MEL / Process-S analogue is meant to represent, so the override claim transfers as a direct architectural constraint rather than by analogy. Transfer risk 0.18 -- the correlational design is the main residual, and the confound (social vs predation) falls outside REE's substrate anyway. Confidence 0.92.

## Failure signatures for the cluster

1. **Flat sleep-onset rate across region novelty.** If REE's trigger is a pure need threshold, onset rate conditioned on region novelty or hazard density will be flat. A flat rate is the signature of the missing allostatic input.

2. **Current-harm threat term cannot reproduce this.** If a safety term is added but sourced from current harm (MECH-286's present sourcing), it will read near-zero in unfamiliar-but-not-yet-harmful regions -- the exact case this paper is about. Diagnostic: correlate the threat term against region novelty; near-zero correlation means the term is structurally incapable of reproducing the finding, independent of threshold tuning.
