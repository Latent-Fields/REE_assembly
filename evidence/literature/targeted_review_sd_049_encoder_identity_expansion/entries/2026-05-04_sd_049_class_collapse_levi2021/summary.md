# Levi et al. 2021 -- Class collapse in metric learning (engineering counsel)

## What the paper did

Levi, Xiao, Wang, and Darrell prove theoretically -- and demonstrate empirically on fine-grained image retrieval benchmarks -- that under reasonable noise assumptions, margin-based metric-learning losses (triplet loss, contrastive loss with margin) tend to project all samples of one class onto a single point in the embedding space. The intra-class diversity that exists in the input distribution (different views, different sub-cluster structure) is destroyed. This is what they call "class collapse." Their proposed mitigation is a small modification to positive sampling: instead of averaging across all same-class positives in the batch, each sample selects its single nearest same-class counterpart as its positive, which permits the embedding to retain multiple sub-clusters per class.

## Why I pulled it for SD-049 Phase 2

The SD-049 Phase 2 design has to commit to an encoder architecture for resource-type identity. Option B (learned low-D embedding) and option C (hybrid with embedding component) both rely on training a learned embedding. The dominant engineering risk for both is collapse during training -- a hazard already documented in REE's own history at EXQ-166b/c/d, where joint training of an encoder with a downstream head produced head-collapse signatures.

This paper documents the canonical failure mode for learned embeddings in multi-class supervision: even without joint-training fragility, the loss surface itself biases the embedding toward representational collapse when intra-class diversity is present. For SD-049's novelty type, intra-class diversity is intrinsic -- novelty cells differ in their per-cell familiarity, which is the structurally-distinct signal MECH-229 wanting/liking dissociation cares about. Under a naively-trained option B encoder, all novelty cells could collapse to a single z_resource point, losing the familiar-vs-unfamiliar distinction.

## What this paper licenses, and what it does not license

Per the implement-substrate skill rule on Layer 7 ML/AI parallels: this is engineering counsel, not architectural authority. The paper does not say anything about whether biological identity coding is sparse or distributed -- those are biological questions answered by the Quiroga / Ballesta / Schapiro / Howard entries above. What this paper licenses is a Phase 2 implementation-level hazard: under option B or C, the training loop must explicitly include anti-collapse mechanisms, or the encoder will fail to learn the within-type structure SD-049's downstream consumers need.

The mitigation strategies that apply directly:

1. **Adaptive same-class sampling** (Levi's proposed fix): retain multiple sub-clusters per class by sampling nearest-positive rather than averaging.
2. **Phased training** (REE's existing pattern from EXQ-166b/c/d analysis): P0 train identity-classifier head on supervised one-hot tags with frozen / weakly-coupled encoder; P1 freeze the head and unfreeze the encoder; P2 evaluate. Phased training avoids the joint-training-collapse pattern by decoupling head learning from encoder learning.
3. **Auxiliary supervision targets** (SD-018 precedent in REE): force the encoder to represent multiple distinct features (identity, familiarity, magnitude) via parallel auxiliary heads that pull in different directions, preventing collapse to any single dimension.

## How this affects the verdict

Under option A (one-hot identity slot + magnitude latent), there is no embedding to collapse -- the architecture is collapse-immune by construction. The supervision is on a discrete classifier head, not on a continuous embedding. This is the engineering-conservative default and the one that matches REE's existing SD-015 substrate (use_resource_encoder pattern with discrete identity classifier).

Under option B or C, the Phase 2 implementation cost is materially higher because anti-collapse mechanisms have to be designed into the training loop. The verdict.md needs to weigh: is the biological similarity-preserving signal that option B/C licenses worth the engineering cost, given that V3-EXQ-514 acceptance criteria can probably be hit by option A alone?

## Confidence

Source quality is high (ICCV 2021, peer-reviewed top-tier CV venue). Mapping fidelity moderate -- this paper documents one of several training hazards Phase 2 will face, not all of which apply to all option-B implementations. Transfer risk is substantial because the source paper is fine-grained image retrieval, not REE's grid-world resource-encoder context. Aggregate 0.74. The paper is properly read as a flag on option B/C's Phase 2 cost, not as an argument against the architecture itself.
