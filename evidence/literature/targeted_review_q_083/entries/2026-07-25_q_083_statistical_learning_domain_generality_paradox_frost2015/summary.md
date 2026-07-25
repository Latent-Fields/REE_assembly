# Frost, Armstrong, Siegelman & Christiansen (2015) -- the domain-generality paradox

## What the paper does

This is a theoretical review written to explain an embarrassment. Statistical learning had been treated for two decades as the canonical domain-general mechanism: a single capacity for extracting distributional structure, indifferent to what the structure is made of. Then researchers began doing the obvious test -- give the same person the same formal regularity in two modalities and see whether performance correlates -- and the correlations came back weak or absent. Frost and colleagues take that result seriously instead of explaining it away. Their proposal is that statistical learning is a set of domain-general computational *principles* that get instantiated separately in each modality, and each instantiation inherits the constraints of the brain regions doing the work. So the computation is shared and the performance is not.

## Why this is the right paper for Q-083

Q-083 asks whether REE needs separate regularity-apprehension systems per domain, or one domain-general apprehender inheriting domain structure from its inputs. I registered that as a binary fork. This paper's contribution is to say the binary is malformed, and to say it on the basis of a literature that spent twenty years assuming the first horn and then failed to find it.

The third option -- shared computation, per-domain instantiation, constraint-driven divergence in observed performance -- is not a fudge between the two arms. It makes a different prediction from either. A purely domain-general apprehender predicts transfer under matched structure. A purely domain-specific set of apprehenders predicts no transfer. The constrained-instantiation account predicts transfer that is real at the level of learning principles but largely invisible in cross-domain performance correlations, because the rate-limiting step is the domain's own input encoding rather than the shared apprehension computation.

That matters for how Q-083 should eventually be tested, and it is a warning about the test design already written into the claim. Q-083's `what_would_answer` specifies cross-domain transfer under matched structure, with a non-degeneracy precondition that single-domain apprehension be demonstrated above floor in both domains separately. This paper says that precondition is necessary but not sufficient: two domains can both be above floor and still differ enough in their input constraints that a genuine shared apprehender produces a null transfer result. A null would then be uninterpretable in exactly the way the claim was trying to avoid.

## Limitations and the transfer I am not entitled to

The paper divides the world by modality -- auditory, visual, tactile -- and by stimulus type. Q-083 divides it by domain: causal, social, ethical, motor, spatial, relational. These are not the same partition, and the paper offers nothing directly on whether constraint-driven specificity survives the change of partition. It is at least arguable that the domain partition is *more* forgiving, since two domains can share a modality; it is equally arguable that it is less forgiving, since social and ethical regularities may differ from causal ones in ways deeper than sensory encoding. I do not know which, and neither does this paper.

Second, this is human behavioural statistical learning over largely passive exposure to sequences. REE's apprehension happens inside an agent that acts, has goals, and gets consequences. The paper's constraints are perceptual; REE's may be motivational or policy-level. Third, it is a review and a framework rather than a decisive experiment, so its authority is the authority of a synthesis.

## Confidence

I have put this at 0.78 with mapping fidelity weighted heavily, since Q-083 is an architectural claim rather than an empirical one and what I want from the literature is a constraint on the architecture rather than a measurement. The paper delivers that: it tells me the fork I registered probably has three tines, and it tells me the near-term risk in my own proposed test is a false negative rather than a false positive. It does not tell me whether REE's domains behave like the paper's modalities, and Q-083 remains substrate-blocked regardless -- V3 has one domain, so there is nothing to transfer between. This entry constrains the eventual V4 design; it does not unblock it.
