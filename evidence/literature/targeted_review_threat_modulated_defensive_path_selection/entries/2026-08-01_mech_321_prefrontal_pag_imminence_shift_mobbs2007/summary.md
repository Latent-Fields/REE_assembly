# Mobbs et al. 2007 -- When fear is near: threat imminence elicits prefrontal-periaqueductal gray shifts in humans

**Source**: Mobbs D, Petrovic P, Marchant JL, Hassabis D, Weiskopf N, Seymour B, Dolan RJ, Frith CD (2007). *Science* 317(5841):1079-1083. [DOI 10.1126/science.1144298](https://doi.org/10.1126/science.1144298). PMID 17717184, PMC2648508.

## What the paper did

This is the canonical human-neuroimaging demonstration of imminence-dependent defensive control, and the natural companion to Fanselow's rodent-based PIC work. The authors built an active-avoidance fMRI paradigm: volunteers were chased through a virtual maze by a predator capable of catching and mildly shocking them, so threat proximity could be manipulated continuously and precisely while brain activity was recorded.

## Key findings relevant to the claim

As the virtual predator drew closer, control of behavior did not merely intensify within one region — it SHIFTED between regions: activity moved from the ventromedial prefrontal cortex (dominant when the threat was distant) to the periaqueductal gray (dominant when the threat was close and contact imminent). This shift was steepest, and PAG dominance most pronounced, specifically when a HIGH degree of pain was anticipated — the categorical shift itself scaled with harm magnitude, not proximity alone. Imminence-driven PAG activity also tracked subjective dread and inversely tracked confidence of escape.

## How this translates to REE

This is the strongest single piece of evidence in the pull for the "threshold/switch" side of the design question's central choice. It is not merely that a response gets bigger as threat gets closer — the system that is IN CONTROL changes character. For SD-hazard-aware-policy-decomposition, the direct implication is that the redecomposition selection step's logic itself should plausibly change CHARACTER as `z_harm_a` crosses a high-imminence boundary — for example, switching from "score and weight-blend among several surviving candidate tiles" to "restrict to the single lowest-harm candidate, overriding ordinary structural cost considerations" — rather than only reweighting a continuous score. The interaction finding (shift steepest under high anticipated pain) is also directly actionable: it argues a REE functional form should let imminence/proximity and harm-magnitude interact (e.g. multiplicatively) rather than treating them as independent additive terms.

## Limitations and caveats

This is correlational human fMRI of whole-brain regional activation dominance during an artificial virtual-predator paradigm with mild anticipated pain standing in for real threat — a standard, acknowledged limitation of the human fear-imaging literature, and it says nothing directly about which candidate sub-plan gets selected among several structurally-decomposed options, since REE's redecomposition junction has no literal vmPFC/PAG analog. The mapping to REE is at the level of "defensive control undergoes a genuine regime change with imminence, and that regime change interacts with harm magnitude" — not a specific quantitative boundary value REE could import directly.

## Confidence reasoning

Top-tier venue, elegant and precisely-controlled paradigm, and one of the most cited and replicated findings in the human threat-imminence literature (it is the foundational citation both the Mobbs 2020 review and Fanselow's more recent syntheses in this pull build on). Confidence 0.88: very high source quality and good mapping fidelity to the categorical-shift half of the design question, moderated only by the expected transfer risk of a whole-brain human-imaging paradigm mapped onto an internal REE computation.
