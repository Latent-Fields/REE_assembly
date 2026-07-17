# Stachenfeld, Botvinick & Gershman (2017) -- The hippocampus as a predictive map

**Claim tested:** ARC-057 (approach emerges from the interaction of DA-mediated representational expansion and a curiosity drive; no explicit approach gradient in hippocampal terrain).
**Direction:** supports | **Confidence:** 0.62

## What the paper did

Stachenfeld and colleagues advance a normative account in which hippocampal place cells encode a *successor representation* (SR) -- roughly, the expected discounted future occupancy of states under the animal's current policy -- rather than a static map of present location. They show that this single idea reproduces a striking range of empirical phenomena: place fields skew backwards opposite the direction of travel, they cluster and subdivide near rewarded goal locations and around barriers, and grid cells fall out as a low-dimensional (eigenvector) decomposition of the same predictive map. The model is validated against rodent place- and grid-cell recordings and against human fMRI.

## Why it bears on ARC-057

ARC-057's central and most counter-intuitive commitment is that approach behaviour toward reward need not be produced by a stored value or "wanting" gradient in hippocampal terrain -- an observer *infers* an attractive gradient, but "there is no gradient; there is more map." Stachenfeld et al. give the cleanest neuroscientific instantiation of that logic I have found. Navigation and reward-sensitive behaviour in their model are read off the *structure* of the representation: place fields reorganise around goals, and the policy operates on that reshaped structure. Two mappings are worth naming precisely. First, the finding that place fields *cluster and subdivide* (finer resolution, more sub-fields) at rewarded locations is the biological analogue of REE's reward-driven representational expansion -- the MECH-232 / SD-024 leg -- arrived at from a completely independent modelling tradition. Second, that navigation then emerges from operating on this shaped map, rather than from a separate value field, is precisely ARC-057's "more map, not more gradient."

## Limitations and caveats

Two honest gaps keep this at 0.62. The representational scheme is a successor representation encoding future occupancy, *not* REE's DA-modulated RBF density expansion; the reshaping around reward is driven by the task's transition/reward structure, not by a phasic dopaminergic density signal. And there is no curiosity or information-seeking drive anywhere in the model -- approach follows the SR-derived policy, so the paper is silent on ARC-057's specific claim that a *uniform* curiosity drive (SD-025) operating on an *asymmetrically shaped* map is what converts structure into approach. There is also a subtler tension: because the SR is itself reward-weighted (expected occupancy discounts toward rewarded futures), a critic could argue an implicit value gradient is baked into the representation, softening the very implicit/explicit boundary ARC-057 leans on.

## Confidence reasoning

Source quality is high (foundational Nature Neuroscience model, extensively validated and widely built upon). Mapping fidelity is moderate: it strongly supports the "approach from representational structure, without an explicit gradient" premise, and even offers an independent analogue of reward-driven field subdivision, but it does not instantiate the DA-expansion x curiosity *interaction* that is the actual content of ARC-057. Transfer risk is moderate (hippocampal spatial map to REE's abstract RBF terrain; SR reward-weighting to REE's density-following). Net: a genuine, well-grounded support for the architectural thesis, weighted down for mechanism mismatch and the absence of the curiosity leg.
