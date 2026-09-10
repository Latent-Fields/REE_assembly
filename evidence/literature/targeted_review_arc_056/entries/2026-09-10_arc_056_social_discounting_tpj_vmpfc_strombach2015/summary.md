# Other-regarding value folded into a single value signal (Strombach et al., 2015)

**Claim tested:** ARC-056 -- ethics-as-coherence: ethical trajectory selection as optimisation of shared temporal-depth coherence across self and represented others.
**Direction:** supports (form of the objective, not its content) | **Confidence:** 0.66

## What the paper did

Participants chose repeatedly between a large reward for themselves alone and a smaller reward shared with a specific other person, where that person sat at a self-reported social distance the participant had ranked in advance. Generosity declined with social distance, as it reliably does. The fMRI question was where that decline happens computationally.

Generous choices engaged the temporoparietal junction, with TPJ activity scaling to the social-distance-dependent conflict between selfish and generous motives. From functional coupling the authors propose a specific architecture: TPJ supports social discounting by *modulating* basic value signals in ventromedial prefrontal cortex, so that an otherwise exclusively own-reward value representation comes to incorporate social-distance-dependent other-regarding preferences.

## How this translates to REE

ARC-056 commits to a particular objective function -- `J_ethical(pi) = beta_self * D_V_self + sum_j beta_j * D_V_j` -- and two features of that form are architecturally contentious in a way that can be checked independently of whether the quantity is right.

The first is that other-regarding terms enter the *same scalar objective* as the self term. This is not the only available architecture: a large tradition holds that moral choice involves a distinct norm-following or rule-based system adjudicating against self-interest rather than being summed with it. The paper's central proposal is squarely the summation architecture -- one value representation, in vmPFC, modulated to carry both terms rather than a second system competing with the first.

The second is that the weight is *graded*, indexed by relational distance, rather than a categorical in-group/out-group switch. The scaling to social distance is continuous here, which is what the claim needs.

There is also a small but real bearing on ARC-056's LEG 1, the derivational leg, which asks whether `beta_j -> 0` recovers ARC-054's `J(pi)` exactly with no discontinuity. In this dataset the most socially distant condition simply is the unmodulated own-reward representation. The limit is continuous, not a regime change. That is the behaviour the claim predicts.

## Limitations and confidence reasoning

The mapping is of form, not of content, and the gap is precisely the distinctive part of ARC-056. What is weighted here is money. What ARC-056 says is weighted is `D_V` -- temporal-depth coherence of a modelled agent's trajectory. Every other-regarding utility model in behavioural economics predicts this result. So the entry supports the aggregation architecture the claim assumes while doing nothing whatever to distinguish ARC-056 from its rivals, and it must not be cited as though it did.

Two further boundaries. Social distance as operationalised -- a self-reported closeness rank over named acquaintances -- conflates the three sources ARC-056 derives `beta_j` from (inferred similarity, relational commitment, responsibility structure), so the paper cannot speak to whether that decomposition is right or whether `beta_j` is even one thing. And the TPJ-modulates-vmPFC architecture is proposed from correlational functional coupling; an architecture in which the aggregation happens elsewhere and vmPFC reads off the result would produce a similar signature.

Source quality is 0.82: PNAS, social distance manipulated parametrically within subject rather than compared across groups, and an explicit computational proposal rather than a blob report -- docked for the correlational coupling inference and a typical mid-2010s sample. Mapping fidelity is 0.66, strong on the aggregation form and the graded-weight prediction, weak on the identity of the quantity aggregated. Transfer risk is 0.35: human subjects, but laboratory monetary choice to a general ethical objective is a real extrapolation. The aggregate tracks mapping fidelity, since ARC-056 is an architectural commitment about the *form* of an objective function and that is exactly the part this paper touches.
