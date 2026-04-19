# Horing & Buchel 2022 -- Shared unsigned PE and modality-specific signed PE

**Citation.** Horing B, Buchel C. The human insula processes both modality-independent and pain-selective learning signals. PLoS Biology 2022; 20(5): e3001540. [DOI](https://doi.org/10.1371/journal.pbio.3001540). (According to PubMed.)

**What they did.** 47 adults learned associations between two cues and four unconditioned stimuli: painful heat at low/high intensity and loud sound at low/high intensity. They measured both BOLD and skin conductance as participants learned the cue-outcome mappings. Crucially, they separated two classes of prediction error: unsigned (how surprised was I?) and signed (was the outcome worse or better than expected?).

**Key finding.** Anterior insula activation correlated with unsigned intensity PE across both modalities. This is a shared, modality-independent aversive-surprise signal. Signed PE was modality-specific -- for pain only, dorsal posterior insula tracked the signed error. There was no equivalent sound-specific signed PE in the same region. The insula thus simultaneously runs two kinds of PE computation: a shared magnitude-of-surprise signal, and a stream-specific signed learning signal.

**What this does for the REE question.** This is the paper that actually resolves the architectural question. Two-layer structure: a shared surprise computation (which could be implemented as a common trunk) plus a modality-specific signed-PE machinery (which has to be per-stream because it carries direction information tied to the consumer that uses that direction). For REE: a shared expectation-generating substrate for the pain family, plus per-stream signed-PE heads. That is exactly "shared substrate with stream-specific heads" -- option (a).

If we read E2_harm_a and E2_harm_s as two heads on a shared trunk that computes "expected pain magnitude in this context," then the unsigned anterior-insula analog is the shared representation, and the signed dorsal-posterior analog (for sensory-discriminative) vs the ACC-affective analog (for affective-motivational, documented elsewhere) are the per-stream heads. This fits MECH-258 as currently written ("E2_harm_a shares substrate with E2_harm_s (ARC-033) -- same forward model architecture, different input stream").

**Where Horing is limited.** Within-pain sub-modalities (A-delta vs C) are not separable in BOLD. Sound is not a great proxy for C-fiber affective pain; the analogy leans on both being aversive but anatomically separate streams. The study uses associative learning rather than a forward-model paradigm proper, so "PE" here is a learning signal rather than explicitly a forward-model residual.

**Confidence reasoning.** This is the strongest single entry. Large N, peer-reviewed PLoS Biology, clean design that directly contrasts the architectural options. Confidence 0.88. I weight this the most in the synthesis recommendation.
