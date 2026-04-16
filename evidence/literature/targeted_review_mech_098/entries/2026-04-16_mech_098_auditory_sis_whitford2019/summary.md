# Summary: Whitford 2019 -- Speaking-Induced Suppression of the Auditory Cortex in Humans and Its Relevance to Schizophrenia

**Source:** Whitford TJ. Biol Psychiatry Cogn Neurosci Neuroimaging. 2019;4(9):791-804. DOI: 10.1016/j.bpsc.2019.05.011
**Claims tested:** MECH-098 (reafference cancellation), MECH-094 (hypothesis tag)
**Evidence direction:** supports | **Confidence:** 0.78

## What the paper did

Whitford reviews approximately three decades of research on speaking-induced suppression (SIS) of auditory cortex -- the well-established finding that self-generated speech sounds produce smaller N1 auditory evoked potentials than externally generated sounds matched for acoustic properties. The review synthesizes the non-human animal evidence, the human EEG/MEG literature using the Talk-Listen paradigm, the proposed corollary discharge mechanism (efference copy from inferior frontal gyrus to auditory cortex), and a growing body of work showing subnormal SIS in schizophrenia. The clinical section proposes that failure of corollary discharge tagging -- failing to mark one's own speech (inner or outer) as self-generated -- provides a mechanistic account of auditory hallucinations and delusions of control.

## Key findings

The core empirical finding is robust and widely replicated: when you speak, your N1 auditory response to your own voice is attenuated relative to hearing the same sound played back externally. This suppression depends on the motor intention to speak -- it occurs for predictable self-generated sounds and not for unpredictable ones. The suppression is present in non-human primates and birds, establishing phylogenetic continuity. In the human fMRI and EEG literature, efference copies from inferior frontal gyrus (Broca's area and surrounding speech motor regions) are transmitted to auditory cortex prior to speech onset. The N1 suppression tracks the accuracy of the prediction: more predictable sounds produce more suppression; unpredictable or externally generated sounds produce full N1 amplitude.

In schizophrenia, multiple labs have found subnormal SIS -- the N1 response to self-generated speech is not attenuated normally. Whitford proposes this reflects a deficit in corollary discharge from speech motor areas. The clinical implication is that auditory hallucinations arise when inner speech is generated without proper corollary discharge tagging, so the agent does not recognize it as self-generated and experiences it as an external voice.

## Translation to REE

This paper is relevant to MECH-098 because it provides the best-replicated human evidence for corollary discharge cancellation operating in a non-visual sensory domain. The principle is identical: motor planning areas generate an efference copy that travels to sensory cortex before the reafferent signal arrives; this prediction attenuates the cortical response to the expected, self-generated sensory event. In REE terms, this is E2_self predicting the expected sensory consequence of an action and routing that prediction to the encoder cancellation gate.

The schizophrenia finding is directly relevant to MECH-094 (hypothesis tag loss). Whitford's account maps precisely onto the REE claim: tag loss means self-generated outputs are processed by the sensory pathway as if they were external events. Auditory hallucinations are the phenomenological consequence of this failure -- the agent experiences their own inner speech as coming from outside. In REE architecture, this would correspond to the encoder treating self-caused latent changes in z_world as genuine world-state updates rather than reafference. The model would fail to learn world-state transitions accurately because it would be training on its own outputs as if they were environmental responses.

## Limitations and caveats

The SIS mechanism is vocal-motor specific. Speech motor planning areas generate the corollary discharge for vocalization; whether an analogous system operates for proprioceptive/vestibular self-motion during navigation is a separate question. The transfer to MECH-098's visual perspective-shift mechanism requires treating the SIS literature as evidence for the general principle of motor-to-sensory corollary discharge cancellation, not for the specific optic flow subtraction mechanism.

The N1 suppression is also a sub-perceptual modulation -- people still hear their own voice clearly despite the N1 attenuation. So SIS is better understood as a differential gain adjustment on the reafferent signal than as a true cancellation to zero, which is relevant for calibrating expectations about the completeness of MECH-098's cancellation operation in REE.

The schizophrenia connection is correlational at the clinical level. Whether the SIS deficit is the cause or a marker of the pathophysiology underlying psychosis is unresolved.

## Confidence reasoning

0.78. Included primarily for two reasons: (1) it provides the most replicated human evidence for corollary discharge cancellation operating via forward-model prediction at a cortical level, supporting MECH-098's general mechanism; and (2) the schizophrenia clinical evidence for corollary discharge failure provides loss-of-function support for MECH-094. Mapping fidelity is moderate (0.65) because the vocalization domain is not the navigational perspective-shift domain of MECH-098. Transfer risk is meaningful (0.40). This entry provides convergence across modalities; the stronger evidence for the visual reafference mechanism is in the Gu 2008, Wolpert 1998, and Sommer 2006 papers.
