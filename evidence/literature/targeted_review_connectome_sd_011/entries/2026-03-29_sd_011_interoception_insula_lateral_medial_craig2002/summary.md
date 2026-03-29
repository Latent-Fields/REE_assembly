# Craig AD (2002) — Interoception: the sense of the physiological condition of the body

**Source:** Nature Reviews Neuroscience 3(8):655-66. DOI: 10.1038/nrn894. PMID: 12154366.

## What the study did

A.D. (Bud) Craig's 2002 Nature Reviews Neuroscience paper is the founding document for what became the 'interoception as physiological sensing' framework. Craig synthesises comparative neuroanatomy, tract-tracing studies, and human neuroimaging to argue that a dedicated ascending pathway — beginning in lamina I of the spinal cord dorsal horn — carries a comprehensive sensory representation of the physiological state of the body to cortex via a specific thalamic relay (the parvocellular ventral posterior medial nucleus, VPMpc). This pathway projects to the posterior insula, where Craig proposes a cortical interoceptive map is constructed. The paper explicitly includes thermoreception, nociception, itch, visceral sensations, and metabolic signals as modalities carried by this lamina I route. It is the work that established the posterior insula as the primary cortical somatosensory interoceptive area — and distinguished it architecturally from the anterior insula, which Craig treats as the affective and motivational re-representation of interoceptive content.

## Key findings

Craig's most architecturally significant finding is the lamina I spinothalamo-cortical pathway to posterior insula: this is a dedicated, anatomically distinct channel from the classical lateral spinothalamic tract to VPL and S1. Where S1 gives a somatic topographic map (where on the body, intensity via somatotopy), the posterior insula gives a physiological state map (what kind of signal, functional significance). Craig further distinguishes the anterior insula, which receives re-entrant projections from posterior insula and integrates interoceptive information with emotional and motivational context — generating the felt quality of the sensation rather than its sensory description.

Critically, Craig contrasts this lateral STT / VPMpc / posterior insula route with the medial spinothalamic projections to intralaminar nuclei, ACC, and anterior insula, which he associates with affective and autonomic responses. These medial projections carry motivational urgency without the high-fidelity sensory topography of the lateral pathway. In primates, Craig argues, this distinction is sharper and more elaborated than in rodents — a phylogenetic gradient that supports its relevance to human (and AI) cognition.

## REE translation

This paper provides the anatomical substrate for SD-011's claim at a level of specificity that no other paper in this set achieves. The lamina I -> VPMpc -> posterior insula route is z_harm_s in biological wetware: it carries the sensory-discriminative harm signal — where, what kind, how intense — as a dedicated channel separable from the affective pathway. The anterior insula / ACC receiving medial projections corresponds to z_harm_a: it processes the motivational-affective dimension, the unpleasantness, the urgency of response.

The posterior/anterior insula distinction within Craig's model is particularly valuable for REE because it suggests that even at the cortical level, the two streams are topographically distinct (posterior insula = sensory; anterior insula = affective). This is more precise than the simple ACC vs. S1 framing from Rainville 1997 — it positions the affective stream in anterior insula as well as ACC, expanding the target cortex for z_harm_a. For REE's implementation, this suggests that z_harm_a should encode not just motivational priority but also autonomic and visceral response preparation — a richer signal than a simple unpleasantness scalar.

## Limitations and caveats

Craig's model has attracted substantial debate in the pain community. Critics (notably Iannetti and Mouraux) argue that the 'labelled line' view of posterior insula as a dedicated nociceptive/interoceptive cortex is too strong, and that posterior insula activations observed in pain fMRI studies reflect salience processing rather than pure sensory-discriminative function. This challenge does not invalidate the anatomical distinctions Craig draws, but it does weaken the inference that the posterior insula map is as informationally clean as he proposes.

A second caveat is species specificity: the lamina I pathway is best characterised in cats and non-human primates; the rodent homologue is controversial. Since most nociception mechanistic work is in rodents, there is a cross-species transfer concern for anyone trying to use this anatomy in a detailed biologically-constrained model.

For REE: the framework is operating at a functional abstraction level, not mapping individual neurons. The posterior/anterior insula and lateral/medial STT distinctions are being used to justify that separating z_harm_s from z_harm_a is a biologically grounded architectural choice — not to replicate the exact laminar anatomy. At that abstraction level, Craig 2002 is strongly supportive.

## Confidence reasoning

Craig's 2002 NRN paper is the single most cited account of the lateral/medial spinothalamic distinction and its cortical consequences. The mapping to SD-011 is direct and detailed. The caveats are real (debate about posterior insula specificity, species transfer) but do not challenge the basic two-channel claim — only its degree of anatomical purity. Confidence: 0.88.
