# Achille, Rovere & Soatto (2019) — Critical Learning Periods in Deep Neural Networks

*ICLR 2019. arXiv:1711.08856 (submitted 2017-11-24; final 2019-02-25). [arXiv](https://arxiv.org/abs/1711.08856) · [DOI](https://doi.org/10.48550/arXiv.1711.08856).*

## What the paper did

This is the paper that lets INV-074 say "universal" with a straight face. Achille, Rovere and Soatto took the critical-period idea out of the kitten and put it into a convolutional network. They applied controlled stimulus deficits at different points in training and measured the consequences with Fisher Information — the sensitivity of the loss to the weights, a proxy for how much the network is still committing versus still exploring. The signature they found mirrors the biology with uncomfortable precision: information in the weights "rises rapidly in the early phases of training, and then decreases, preventing redistribution of information resources." Deficits imposed during that early high-plasticity window cause lasting impairment; the same deficits later are shrugged off with more training. Their own framing is the line that matters most for us: "critical periods are not restricted to biological systems, but can emerge naturally in learning systems."

## Why it matters for INV-074

INV-074 is an *invariant*, typed universal — a claim that the monostrategy-without-crystallization failure holds for any model-building agent under Hebbian-equivalent learning, not just for visual cortex. A universal claim grounded only in one sensory system would be over-reaching. Achille et al. are the substrate-independence pillar: they show the rise-then-collapse of plasticity, and the permanence of early deficits, in exactly the kind of system REE *is* — a gradient-trained deep network. Fisher Information here plays the role the inhibitory threshold plays in Fagiolini & Hensch: an instrumentable readout of the window closing. For a claim with zero prior literature entries, this is the entry that converts a suggestive biological analogy into a mechanism we should expect REE itself to exhibit. That is also why I weight transfer risk *low* rather than high — unusually for a cross-domain mapping — because the target domain (a deep net) is the source domain.

## Limitations and the honest caveat

The deficits Achille et al. study are sensory/input perturbations. INV-074's specific failure mode is narrower and more internal: a high-variance predictive pathway competitively suppressing a diversity circuit (ARC-065). The *mechanism* — information-plasticity collapse closing the option space — is shared and that is the load-bearing transfer. But the paper does not instrument a diversity-versus-dominant-pathway competition directly, so the mapping to REE's specific circuit is structural, not literal, and I have logged that as a failure signature. A second, more interesting caveat: severity scales with network size and deficit timing. INV-074 currently treats the crystallization schedule as fixed; this paper hints the window requirement may itself be capacity-dependent, which the claim should eventually absorb rather than ignore.

## Confidence

0.88, `supports` — the joint-strongest entry in this folder. Source quality is high (ICLR 2019, careful methodology). Mapping fidelity is high because the shared mechanism is exactly what the invariant needs, and transfer risk is genuinely low here since REE is itself a gradient-trained network. Together with Hubel & Wiesel and Fagiolini & Hensch, INV-074 now has its biological necessity, its causal gate, and its substrate-independent generalisation.
