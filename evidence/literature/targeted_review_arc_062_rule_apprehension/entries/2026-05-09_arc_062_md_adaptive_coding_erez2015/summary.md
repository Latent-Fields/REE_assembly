# Erez & Duncan 2015 — Behavioural-relevance modulation of categorical discrimination in human frontoparietal cortex

According to PubMed: Erez & Duncan 2015, *J Neurosci* 35(36):12383–93. [DOI 10.1523/JNEUROSCI.1134-15.2015](https://doi.org/10.1523/JNEUROSCI.1134-15.2015) (PMID 26354907, PMC4563032).

## What the paper does

Human fMRI multivoxel pattern analysis during a cued-detection categorisation task. Participants detected whether an image from one of two target visual categories was present in a display. The authors measured how the multivoxel response patterns in MD-network regions (frontoparietal cortex) discriminated between visual categories that differed in their *current behavioural status*.

The key finding: categorical discrimination in the MD network is *modulated by behavioural relevance*. Distinctions between categories with different behavioural status (e.g. between a target and a non-target) were significantly discriminated; distinctions between categories with the same behavioural status (e.g. between two targets) were not discriminated above chance. Aspects of the task that were orthogonal to the behavioural decision did not modulate categorical discrimination — the modulation is selective to what currently matters.

## Why this matters for the ARC-062 architecture

This is the upstream story for ARC-062's discriminator. ARC-062 proposes a learned context discriminator that gates between policy heads — that is engineering shorthand for *adaptive coding*. Erez & Duncan establish that the human MD network does this naturally: it preferentially encodes task-relevant distinctions and suppresses task-irrelevant ones at the multivoxel-pattern level. The mechanism is the rule-context-modulated adaptive coding that Duncan's broader theoretical framework predicts; the empirical demonstration here is the direct evidence.

For ARC-062 weak reading, the implication is that the gated-policy + discriminator architecture is the simplest engineering instantiation of adaptive coding. The biology achieves the property at the population level via task-dependent representational modulation across the MD network; the engineering design tries to achieve a useful subset of this with two policy heads + a soft discriminator. Whether the engineering subset is sufficient for the SD-054 monomodal-collapse falsifier is the empirical question the cluster's Phase 2 experiment is designed to answer.

## How this connects to Mitchell 2016 (sibling entry)

The MD network Mitchell et al. delineated anatomically in macaques, Erez & Duncan show is *task-modulated* in humans. Together, the two entries establish: (a) the substrate is anatomically distributed across frontoparietal + insular sites (R1 multi-stream + R3 distributed multi-site), and (b) the substrate's representational content is task-context-modulated (the adaptive-coding mechanism that ARC-062 instantiates). Neither paper alone closes the architectural decision; together they license the multi-stream + distributed-multi-site framing as the V3-end-state target, with ARC-062 as the V3-tractable Phase 1 simplification.

## Mapping caveat

Erez & Duncan's categories are *perceptual* (visual object distinctions) under a cued-detection task, not procedural rules. The bridge from "multivoxel patterns reflect behaviourally relevant perceptual categories" to "discriminator output gates rule-conditioned policy heads" is a level-of-implementation step. mvpa is a population-level decoding finding, not a single-cell or single-circuit gating finding. The phenomenon is real and biologically primary; the level-of-implementation gap means the paper cannot directly prescribe the discriminator architecture — only confirm that adaptive coding by behavioural relevance is the function the architecture should implement.

## Confidence reasoning

Source quality 0.82 — solid *J Neurosci*, peer-reviewed, methodologically clean mvpa. Mapping fidelity 0.68 — adaptive coding by behavioural relevance is established, but mvpa is population-level rather than circuit-level. Transfer risk 0.22 — human MD findings transfer well to macaque MD (Mitchell 2016) and to REE's distributed substrate. Confidence 0.74 reflects: solid functional anchor for the adaptive-coding principle minus the level-of-implementation gap.

## Failure signature for the cluster

If ARC-062 weak reading PASSes the SD-054 falsifier behaviourally but multivoxel-style decoding of the discriminator's hidden representations cannot recover the reef-vs-forage context distinction (i.e., the adaptive-coding signature is absent at the representation level), Erez & Duncan's evidence predicts the discriminator has not internalised the relevant cut. The architectural choice would have surface-level success without the underlying rule-context representation, which would generalise poorly to substrate enrichment (SD-049 multi-resource heterogeneity, SD-047 multi-source dynamics) where the relevant cut moves. Diagnostic: train a linear probe to recover reef-vs-forage from the discriminator's pre-softmax logits; PASS = decoding above chance, FAIL = decoding at chance despite behavioural success.
