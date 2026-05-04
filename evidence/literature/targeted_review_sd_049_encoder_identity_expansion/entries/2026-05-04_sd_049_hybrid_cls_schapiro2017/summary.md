# Schapiro et al. 2017 -- Complementary learning systems within the hippocampus

## What the paper did

Schapiro, Turk-Browne, Botvinick, and Norman built a neural-network model of hippocampal subfields that respects known anatomical projections: entorhinal cortex projects directly to CA1 (the monosynaptic pathway) and also through dentate gyrus and CA3 (the trisynaptic pathway). They trained the model on sequences exhibiting temporal community structure -- the same kind of regularity Schapiro et al. 2016 (companion paper, cross-tag entry) had shown hippocampus learns -- and asked which pathway supports which computational function.

The result is clean: the monosynaptic pathway supports statistical learning of similarity-preserving regularities (community structure becomes encoded as overlap in the CA1 representations, item similarity reflects graph proximity). The trisynaptic pathway supports per-episode pattern separation (DG sparsifies, CA3's recurrent dynamics reactivate stored episodes). Apparent regularities can emerge from the trisynaptic side via associative reactivation, but the specialised statistical-learning pathway is the monosynaptic one. The architectural commitment is that the brain handles the labeled-line vs distributed-coding trade-off by having both anatomical pathways and reading them out for different purposes.

## Why I pulled it for SD-049

This paper is the architectural resolution of the tension that runs through the rest of the slate. Quiroga (sparse readout) and Ballesta-Padoa-Schioppa (labeled-line OFC) push toward option A. Schapiro 2016 (distributed similarity-preserving substrate) and Howard 2015 (MVPA pattern-based identity) push toward option B. The Schapiro 2017 paper explicitly says: the biological architecture is BOTH. Two pathways, two read-outs, two computational roles.

This is direct biological licensing for option C in the SD-049 verdict: a hybrid where the supervision target is one-hot identity (option A's labeled-line shape, served by the trisynaptic-analog) AND the substrate is a similarity-preserving learned embedding (option B's distributed shape, served by the monosynaptic-analog). REE z_resource under option C would have an identity-classifier head supervised on resource-type tags, backed by a distributed learned embedding component whose similarity structure is allowed to develop across types.

## What option C would actually look like in REE

The translation to a single MLP encoder is non-trivial. The Schapiro model has anatomically distinct pathways with different cell types and connectivity patterns. REE's z_resource is a single MLP head consuming `world_obs` and producing a 32-dim latent. A clean Phase 2 implementation of option C would need to commit to what "two pathways" means at the encoder layer. Three reasonable instantiations:

1. **Shared-backbone-split-heads:** shared trunk MLP -> two heads in parallel, one identity-classifier (supervised on type tags), one embedding output (shaped by similarity-preserving auxiliary loss e.g. contrastive). The shared trunk is the monosynaptic-analog; the identity head is the trisynaptic-analog readout. z_resource is the concatenation of both head outputs.

2. **Single-output-with-supervision:** a single embedding head, with an identity-classifier *training-only* head riding on top of it during P0 phase, then frozen and removed at P2. z_resource is just the embedding, but the supervision signal during training is one-hot identity classification. This is what most modern multi-task representation learning does.

3. **Two parallel encoders:** entirely independent encoders for the two paths, concatenated at z_resource. Cleanest separation but doubles parameter count and loses any cross-pathway learning.

Option 1 looks closest to the Schapiro architecture and is probably the right Phase 2 commitment if the verdict lands at option C. Option 2 is what most ML papers do and is engineering-friendly. Option 3 is excessive.

## Confidence and verdict contribution

Source quality is high (Schapiro/Norman/Botvinick collaboration; canonical CLS modeling). Mapping fidelity strong because the bi-pathway architecture is exactly what option C licenses. Transfer risk modest. Aggregate 0.82.

Verdict contribution: this entry is the load-bearing argument for option C hybrid over either pure option A or pure option B. The biology is bi-pathway; the engineering choice in Phase 2 is whether to instantiate both pathways at the encoder level (option C) or pick one and accept the trade-off (option A or B). My read of the cohort is that option C is biologically the most faithful, but its Phase 2 implementation cost is substantially higher than option A's. The verdict.md needs to weigh this trade-off against the V3-EXQ-514 acceptance criteria and the Phase 2 timeline.
