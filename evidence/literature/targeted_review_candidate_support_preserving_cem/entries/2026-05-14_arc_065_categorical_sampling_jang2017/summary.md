# Jang, Gu & Poole 2017 - Categorical Reparameterization with Gumbel-Softmax

[Google Research](https://research.google/pubs/categorical-reparameterization-with-gumbel-softmax/) - ICLR 2017.

## What the paper did

Jang, Gu and Poole introduce Gumbel-Softmax, a continuous relaxation for categorical sampling that allows gradients to pass through stochastic categorical choices. The method can be annealed toward categorical samples while remaining useful inside differentiable neural computation graphs.

## Why this matters for ARC-065

REE's immediate failure sits at a categorical boundary: the first action class is absent from the candidate set, so no downstream score bias can select it. Gumbel-Softmax is relevant because it names a principled way to make categorical alternatives explicit inside a learned proposer. It is especially relevant if later work replaces emergent action-object argmax decoding with a categorical-first-action proposal stage.

For V3-EXQ-563b, however, this should stay out of the implementation path. The smallest repair is diagnostic and default-off: measure first-action support, preserve or inject minimal one-hot candidates when support collapses, and record whether scaffold or support preservation was active.

## Limitations and confidence

This paper is not about CEM, MPC, or hippocampal planning. It supports the existence of a later categorical-sampling design family, not the immediate patch. Confidence is 0.58: relevant to the first-action boundary, but not direct evidence for support-preserving CEM.
