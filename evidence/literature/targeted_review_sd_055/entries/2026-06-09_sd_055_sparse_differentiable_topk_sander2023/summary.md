# Sparse differentiable top-k: the principled caveat on SD-055's softmax-mean

**Claim:** SD-055 — replace the non-differentiable argmax/argsort elite-selection in `HippocampalModule.propose_trajectories()` with a softmax-weighted candidate mean, restoring gradient flow to SD-016 `cue_action_proj`.

**Source:** Sander ME, Puigcerver J, Djolonga J, Peyré G, Blondel M (2023), *Fast, Differentiable and Sparse Top-k: a Convex Analysis Perspective*, ICML 2023. [arXiv:2302.01425](https://arxiv.org/abs/2302.01425). Direction: **mixed** (confidence 0.68).

## What the paper does

The top-k operator returns a sparse vector marking the k largest entries, but it is discontinuous and so "difficult to incorporate in neural networks trained end-to-end with backpropagation." The paper recasts top-k as a linear program over the permutahedron (the convex hull of permutations of a vector) and smooths it with a p-norm regularization term. The payoff is an operator that is *simultaneously* differentiable **and** sparse — a combination the authors note prior relaxations did not achieve, observing that before their work "no approach is fully differentiable and sparse." They demonstrate the operators on weight pruning, fine-tuning vision transformers, and routing in sparse mixtures of experts, where faithful sparse selection at large scale matters.

## How it maps to SD-055 — and why it is mixed, not supporting

SD-055 sits squarely inside the family of methods this paper is about: it takes a discontinuous selection step (argsort + indexed elite-mean) and swaps in a smooth relaxation (a temperature-controlled softmax-weighted mean). On the supporting side, the paper independently confirms SD-055's framing of the problem — the discontinuous selection genuinely blocks backpropagation, and differentiable relaxations are the right tool. That part agrees with SD-055 and with the companion DCEM entry.

The reason I have logged this as `mixed` is the paper's central methodological argument cuts against SD-055's *specific* choice. SD-055 uses a **dense** relaxation: `softmax(-scores/T)` puts non-zero weight on *every* candidate and averages them. Sander et al. argue that dense, entropy/softmax-style relaxations sacrifice the sparsity that makes a relaxation a *faithful* surrogate for true top-k selection — the whole point of their contribution is to recover sparsity that softmax-type operators throw away. Translated to SD-055: the gradient is restored (the goal is met), but the soft aggregate may approximate the argsort elite-mean only loosely, and at high temperature or with a broad candidate spread it can drift toward the *centroid of the whole candidate set* rather than the best trajectory. If that happens, the gradient reaching `cue_action_proj` is real but points at the wrong target. The paper thereby supplies both a principled caveat on SD-055's approximation and a concrete upgrade path: if the softmax-mean proves too diffuse in practice, a sparse top-k operator of the kind this paper builds would preserve elite semantics while staying differentiable.

## Limitations of the critique

The critique is indirect and should not be over-weighted. Sander et al. neither study CEM planning nor test SD-055; their demonstrations are at large scale (thousands of experts or tokens), where dense relaxations are genuinely costly and imprecise. REE's CEM works over a *small* candidate pool, and SD-055 exposes a temperature `T` that, when lowered, concentrates the softmax weight near the argmax — so at REE's scale and a suitably low `T`, the dense softmax-mean may already approximate elite selection well enough that the sparsity advantage never bites. That is why mapping fidelity is moderate (0.62) and overall confidence is 0.68: the paper identifies the right theoretical weakness of SD-055's chosen operator, but whether that weakness is material at REE's scale is an empirical question SD-055's own validation (the `use_differentiable_cem` ablation) will have to settle.

## Why included

It is the honest counterweight to the DCEM entry. DCEM says "this technique works and is the precedent"; this paper says "the *dense* form SD-055 picked is the loosest member of the family, and here is why and what to do about it." Together they bracket SD-055: the direction is well-founded, the specific softmax-mean is a defensible but improvable first cut, and the temperature parameter is the knob that determines whether the known weakness matters.
