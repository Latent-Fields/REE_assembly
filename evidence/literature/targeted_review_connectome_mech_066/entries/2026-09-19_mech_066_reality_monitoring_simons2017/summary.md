# Brain Mechanisms of Reality Monitoring (Simons, Garrison & Johnson, 2017)

## What the paper does

This is the field's consolidating review of reality monitoring: the set of processes by which a mind decides whether a given piece of content came from inside it or from the world. Simons, Garrison and Johnson synthesise functional neuroimaging, lesion and clinical evidence around a neurocognitive account, with anterior medial prefrontal cortex and the morphology of the paracingulate sulcus as recurring substrates, and they trace the continuum of failures -- from the ordinary, benign confusions between remembered and imagined experience that healthy cognition routinely produces, through to clinically significant misattribution.

Marcia Johnson's source-monitoring framework is the intellectual spine of this literature, and the review's value for our purposes is that it treats the discrimination as a *mechanism with a substrate* rather than as a property that falls out of representational differences.

## Why this bears on MECH-066

MECH-066 contains a modal word -- pre-commit and post-commit channels **must** stay separated at durable write boundaries. Modal claims in this registry are the hardest to evidence, because a design document can always assert a *must* and an experiment can usually only show a *helps*. The strongest available argument for a *must* is that the reference system builds dedicated machinery to achieve the thing, and that the machinery's failure is recognisable as damage rather than as variation.

That is exactly what this review establishes. If keeping internally generated content distinct from externally originating content were guaranteed by having two channels, there would be no reality-monitoring mechanism to review, no anterior mPFC contribution to find, no paracingulate morphology correlating with misattribution, and no clinical phenomenology at the far end. The existence of the literature is the argument.

I want to be careful about one thing here, because the sloppy version of this point is common and wrong. The relevant failure is *misattribution of source* -- internally generated content assigned an external origin. That is a specific, mechanistically-characterised error, and it is not interchangeable with "hallucination" as a catch-all, nor with confabulation, which has a different structure and different antecedents. The review's own framing is the careful one: a continuum of source-attribution failures whose severe end includes hallucinations, not an identity between the two. The third failure signature I recorded is the architecturally useful reading: instantiating a pre-commit and a post-commit channel does not implement the separation, it only creates the two things that need separating.

## The limitation, which is a locus mismatch and not a minor one

Reality monitoring as reviewed here is largely **retrospective**. The question is about an item already stored: where did this come from? MECH-066 asserts a **prospective** constraint: the pre-commit channel must not write into the durable store in the first place.

These come apart in both directions, and the review does not distinguish them. A system with flawless write-boundary enforcement could still fail retrospective attribution -- both channels wrote to their correct loci, but the provenance tag was lost or was never recorded. Conversely, a system with perfect source tags could have a thoroughly contaminated write locus, and would then be able to tell you accurately that its durable store is full of material it should never have consolidated. REE's actual enforcement, in `update_residue` accepting only post-commit harm and `compute_prediction_loss` training E1 only on actual observations, is of the prospective kind. This review evidences that the discrimination problem is real and mechanism-requiring; it does not evidence that the write boundary is where the solution belongs.

That is why `mapping_fidelity` is 0.55 and why this entry sits below the Kaufman null-space entry despite arguably making the stronger modal argument. The modal force is better here; the locus is worse.

## Confidence

0.66. Source quality 0.85 -- this is the authoritative review by the people who built the framework. The discount is almost entirely the retrospective/prospective mismatch, with a smaller `transfer_risk` contribution for the usual reason that a clinical-population continuum does not straightforwardly index an architectural requirement in a non-clinical artificial system.

The second failure signature is the one with immediate consequences for how we would ever test this: the failures are graded, not binary. If we design a write-boundary audit for MECH-066 expecting a clean breach signature, we may be looking for the wrong shape. Partial contamination is the reference system's normal operating regime.
