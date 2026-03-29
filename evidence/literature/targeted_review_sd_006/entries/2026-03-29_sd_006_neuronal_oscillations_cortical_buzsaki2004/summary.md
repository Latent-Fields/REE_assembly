# Neuronal Oscillations in Cortical Networks

**Buzsaki & Draguhn (2004) -- Science**

## What the paper did

This landmark Science review synthesises evidence for the functional role of cortical oscillations across the full frequency spectrum, from ultra-slow oscillations (<0.1 Hz) through delta, theta, alpha, beta, gamma, and ripple frequencies (>100 Hz). The central argument is that neuronal oscillations are not noise or epiphenomena but are a preserved and necessary feature of cortical computation: they bias input selection, temporally bind neurons into co-active assemblies, and facilitate the synaptic plasticity needed for learning and memory consolidation. The authors review evidence that these oscillations are phylogenetically preserved across species from insects to primates, implying strong selection pressure -- they solve a problem that brains repeatedly need to solve. The paper's most influential contribution is the framing of oscillations as temporal coordinate systems: different cognitive states and processes are associated with characteristic frequency bands, and the coexistence of multiple bands in the same tissue reflects the operation of multiple simultaneous computational processes at different timescales.

## Key findings relevant to SD-006

The paper establishes four claims that directly support SD-006. First, characteristic oscillatory rates are real and functionally necessary -- not arbitrary artifacts of network connectivity. Second, different cognitive processes are associated with different frequency bands: theta (~4-8 Hz) with navigation, working memory, and deliberative processing; gamma (~30-80 Hz) with fast sensory-motor processing and local assembly formation; beta (~12-30 Hz) with motor status quo and long-range synchronisation. Third, these rates coexist in the same tissue simultaneously, with faster oscillations nested within slower ones (gamma within theta). Fourth, the rates are used for temporal multiplexing -- multiple processes share the same tissue by operating at different rates, with timing relationships carrying information about the sequence and context of events.

SD-006 implements exactly this principle: E3 (deliberative planning) runs at a theta-analogous rate, E2 (fast motor loop) at a gamma-analogous rate, and E1 (consolidation) at still slower rates. The paper provides the evolutionary and functional rationale for why this rate hierarchy exists in biological systems and why it should be preserved in a system designed to model the same computations.

## Mapping to REE

The Buzsaki-Draguhn framework provides the broadest available theoretical support for SD-006's design principle. Where the Lisman-Jensen theta-gamma code review (also cited) focuses specifically on working memory item storage, the Buzsaki-Draguhn review situates multi-rate computation in the broader context of all cortical processing. The most direct mapping is between the theta-gamma nesting scheme and E3-E2 nesting: E2 completes approximately 9 fast evaluation cycles for each E3 deliberative cycle (from EXQ-052b, e3_tick_ratio ~0.109), which is consistent with the ~9:1 ratio of gamma subcycles per theta cycle in hippocampal recordings. The paper's argument that oscillatory multiplexing allows multiple processes to coexist in the same neural substrate without mutual interference maps onto SD-006's async execution model: E1, E2, and E3 share a simulated environment but run at characteristic rates without waiting for each other.

## Limitations and caveats

The review covers all oscillation bands without specifically arguing for asynchronous multi-module rate separation. Inter-areal synchronisation is one of the reviewed mechanisms (different regions synchronise at shared frequencies to coordinate communication), which is a different implementation from SD-006's asynchronous architecture. SD-006 achieves rate separation by running modules at different step counts, not by phase-locking modules to shared oscillatory cycles. Whether these are equivalent implementations depends on the specific computational role of phase, which the review discusses but does not resolve. The mapping from continuous biological Hz to discrete simulation timestep ratios also requires calibration not available from this paper.

## Confidence reasoning

Science review by a leading figure in systems oscillations neuroscience, >6000 citations, canonical in the field. The paper establishes without serious dispute that characteristic oscillatory rates are functionally necessary and preserved. The mapping to SD-006's multi-rate architecture is direct at the conceptual level but requires translation steps (continuous-to-discrete, biological-to-computational). Confidence is set at 0.77 -- high, reflecting the quality of the evidence and the directness of the rate-hierarchy mapping, but not maximum, reflecting the remaining translation steps and the generality of the review.
