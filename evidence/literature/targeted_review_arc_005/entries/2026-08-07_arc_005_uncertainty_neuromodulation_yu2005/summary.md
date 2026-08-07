# Yu & Dayan 2005 — Uncertainty, Neuromodulation, and Attention

**Claim tested:** ARC-005 ("Control plane routes precision and modes")
**Direction:** supports (mechanism-grounding) · **Confidence:** 0.72

## What the paper did

Yu and Dayan build a normative, approximate-Bayesian model in which two neuromodulators carry two flavours of uncertainty: acetylcholine reports *expected* uncertainty (the known unreliability of a predictive cue within a stable context), and norepinephrine reports *unexpected* uncertainty (a gross, unsignalled change of context). The model's core move is that these signals set the *precision-weighting* of the inference: when uncertainty about top-down predictions is high, the system down-weights its priors and lets bottom-up sensory evidence dominate, and vice versa. They show this reproduces a swathe of physiological, pharmacological, and behavioural findings in attentional-cueing tasks.

## Why it is the right anchor for ARC-005

ARC-005's own autopsy (V3-EXQ-848b) names this literature explicitly: the claim's biological reference is "norepinephrine/dACC-mediated precision-weighting of prediction error in hierarchical predictive coding (Yu & Dayan 2005; Friston precision-weighting)". This paper is therefore the *formal import* the claim rests on — the biological warrant that a control channel can exert causal authority over precision, dissociable from the content being processed. That is exactly the existence claim ARC-005 makes (the plane *routes*, it is not an epiphenomenal readout). On the question of whether the mechanism is real, this is a clean supports.

## What it does — and does not — tell us about magnitude

The commissioning question for this whole review is whether REE's raw channel-1 effect (~1e-3 log10-precision-units, ~180× smaller than the ~0.18 cross-seed SD) is a genuinely tiny-but-real biological effect or the signature of an undertrained implementation. This paper cannot answer that directly, because it is a model, not a measured intervention — it establishes that precision-weighting is *functionally load-bearing* (it changes how much evidence updates belief) but does not quantify the downstream shift a within-range channel manipulation should produce. It does, however, sharpen the interpretive frame: in this model the neuromodulatory gain is *multiplicative on the inference*, so a channel that is architecturally invariant under normal committed operation, or one reading a collapsed upstream signal whose response is 4–7 orders of magnitude off the scale of the other bias components (precisely the dACC-adapter defect 848a identified), is not implementing this mechanism at all — it is present but mute. The quantitative "how big should the effect be" work is carried by the pharmacology entries in this review (Nuiten 2024, Cook 2019, Kanen 2021).

## Honesty on the caveat

The transfer risk here is real and I have not hidden it in the confidence (0.72, held down by transfer_risk = 0.45): a normative model of biological ACh/NE does not automatically license quantitative predictions for REE's engineered channel. It grounds the *mechanism* and the *direction* of ARC-005, not the effect size. Treat this entry as establishing "the routing mechanism REE claims is biologically real and consequential," and lean on the empirical entries for "and here is roughly how large its footprint should be."

*According to PubMed / Cell Press. Yu AJ, Dayan P. Neuron 2005;46(4):681-692. [DOI](https://doi.org/10.1016/j.neuron.2005.04.026)*
