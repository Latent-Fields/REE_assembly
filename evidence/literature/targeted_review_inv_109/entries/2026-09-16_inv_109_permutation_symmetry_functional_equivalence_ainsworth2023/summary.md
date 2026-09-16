# Git Re-Basin: Merging Models modulo Permutation Symmetries (Ainsworth, Hayase & Srinivasa, ICLR 2023)

## Why this entry is in the pull

The other four entries in this directory support INV-109. This one is here to argue with it, and it is the entry I would want governance to read first if the claim is ever proposed as a pre-registration gate.

Ainsworth et al. observe that a neural network's hidden units carry no canonical ordering: permuting them, with the incoming and outgoing weights permuted to match, leaves the computed function untouched. So two networks that look far apart in weight space may be the same function wearing a different labelling. They build three algorithms for finding the permutation that aligns one model to a reference, and show that after alignment the two models sit in what is approximately a single convex basin -- including the first demonstration of zero-barrier linear mode connectivity between *independently trained* ResNets on CIFAR-10. The alignment "produces a functionally equivalent set of weights". They are also candid about the limits, closing with "shortcomings of the linear mode connectivity hypothesis, including a counterexample to the single basin theory".

## What it does and does not do to INV-109

It is important to be precise here, because the paper is easy to over-read in either direction.

It does **not** undercut INV-109's central assertion. INV-109 says that a claim naming a specific earlier endpoint -- "decoded the 1002/1008 latent", "the same frozen encoder" -- requires that endpoint to have been persisted and loaded. Permutation-equivalence is a fact about functions; it is not a fact about the tensor that was or was not saved to disk. If 1002 and 1008 persisted neither observations nor encoder weights, then 1010 did not load them, and no amount of basin geometry makes the inherited sentence a measured one. That half of INV-109 is untouched.

What it **does** undercut is the reading of the discriminator. INV-109 proposes "a recorded state hash at both endpoints, re-verified at every evaluation boundary, with a mismatch aborting rather than warning." Under permutation symmetry, a hash mismatch between two independently trained networks is not merely likely, it is essentially guaranteed -- the permutation alone is sufficient to produce it, before any question of whether the models differ in any way that matters. So the instrument is doing two quite different jobs and the claim's wording does not separate them:

- As a detector of **re-derivation versus loading**, `hash_tensor_state` is exactly right. If you loaded the endpoint, the hash matches; if you re-derived it, it does not. Near-perfect sensitivity and specificity for the thing INV-109 actually cares about.
- As a detector of **scientific consequence**, it is close to uninformative. A mismatch tells you almost nothing about whether the second model is a different object in any sense a reader would care about.

An abort-on-mismatch gate is defensible under the first reading and over-strong under the second. My recommendation, recorded here for governance rather than asserted as a finding, is that INV-109's discriminator sentence should say which of the two it means.

## The harder question it raises about 1008 and 1010

There is a more uncomfortable implication. The 1010 audit found matching participation ratios and in-band consumer-width values alongside differing weight deltas, and INV-109 reads that as "regime agrees, artifact differs". Ainsworth et al. raise the possibility that the regime agreement is evidence of *more* sameness than that framing concedes -- that two reproductions of a well-specified recipe might be functionally near-equivalent objects whose weight-space distance is largely bookkeeping.

I do not think this rescues the original sentence. "Functionally equivalent up to a permutation we did not compute" is not "the banked 1002/1008 latent", and the audit never had the evidence for the stronger claim regardless. But it does mean INV-109 should be careful not to slide from *the endpoint-identity claim is unsupported* (true, and the claim's real content) to *the two endpoints are scientifically different objects* (not established, and this paper is a reason to doubt it).

## Limitations

The demonstrations are on wide supervised vision classifiers, and width matters to their results -- they explicitly relate model width and training time to mode connectivity. The alignment does not happen by itself; it is produced by a matching algorithm run deliberately. And the authors themselves give a counterexample to the single-basin theory. Nothing here establishes that REE's episodic encoders, which are narrow and trained on short curricula, are permutation-alignable at all. Any appeal to this paper as grounds for relaxing INV-109 would have to demonstrate alignability on the actual architecture rather than assume it.

## Confidence

0.62. The venue and the work are strong (ICLR oral, top 5%); the discount is mapping, not quality. The paper speaks to what a weight difference *licenses you to infer* rather than to INV-109's actual assertion about endpoint provenance, and its central phenomenon is demonstrated on a model class some distance from REE's. Filed `mixed` because it genuinely cuts both ways: it leaves the claim's core intact while putting real pressure on the prescription attached to it.
