# Sanders, Wilson & Gershman (2020) — Hippocampal Remapping as Hidden State Inference

**Journal:** eLife
**DOI:** 10.7554/eLife.51140
**PMID:** 32515352

## Relevance to ARC-042

Sanders et al. provide a Bayesian computational account of hippocampal context representation that directly grounds ARC-042's Phase 1 gate as a computational necessity.

## Core Framework

The paper argues that hippocampal place cell remapping is not a direct response to sensory change but is hidden state inference: the system maintains a posterior belief over latent environmental states that generated the current observations. The generative model uses a Chinese Restaurant Process (CRP) prior, parametrized by alpha, that determines the tendency to infer a new vs. existing context.

Key prediction: the quality of context discrimination at inference time is bounded by the quality of the learned prior. A flat prior (no experience with context distinctions) cannot support discrimination even given perfect observations.

## Mapping to ARC-042 Phase Structure

| ARC-042 Phase | Sanders et al. Analog |
|--------------|----------------------|
| Phase 0: Bootstrap world model | Flat CRP prior -- no context structure learned |
| Phase 1: Supervised context training | Prior update from labeled context experience |
| Phase 2: Frozen ContextMemory for gating | Trained prior used for context inference |

The Phase 1 gate in ARC-042 -- the requirement that ContextMemory must be trained before it is useful for evaluation -- is the computational equivalent of the Sanders et al. prediction: context inference (Phase 2) requires an informative prior (Phase 1), and Phase 0 alone cannot provide it.

## Specific Prediction Supporting ARC-042

In the Sanders et al. model, an agent with no prior experience of context distinctions (flat CRP prior, alpha -> infinity) treats every observation as equally likely to come from any context. This corresponds exactly to cosine_sim=1.0 in EXQ-187a: without Phase 1 training, all retrieved context vectors are identical because the system has no representation of what makes contexts different.

The model predicts that Phase 1 functions not merely as a warm-up but as a qualitative phase transition: before Phase 1 completes, the context module cannot discriminate (flat posterior); after Phase 1, it can (peaked posterior on correct context). This is the theoretical basis for ARC-042's gate as a necessary rather than optional step.

## Limitations

- CRP is a discrete generative model; ContextMemory uses continuous learned representations
- "When to remap" (the paper's focus) differs from "how to learn to discriminate" (ARC-042's focus)
- The paper does not specify how many exposures are required to make the prior informative (that is addressed by Law et al. 2016)
