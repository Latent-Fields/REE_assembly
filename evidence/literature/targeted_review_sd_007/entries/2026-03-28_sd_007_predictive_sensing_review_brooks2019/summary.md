# Brooks & Cullen 2019 — Predictive Sensing: The Role of Motor Signals in Sensory Processing

Based on articles retrieved from PubMed (DOI: [10.1016/j.bpsc.2019.06.003](https://doi.org/10.1016/j.bpsc.2019.06.003)).

## What the paper did

Brooks and Cullen wrote a comprehensive review of the circuit-level evidence for motor-signal-based reafference cancellation across sensory modalities — somatosensory, vestibular, auditory, and visual. The paper synthesises findings from multiple species and experimental paradigms, drawing out both common principles and important differences between modalities in where and how cancellation is implemented.

## Key findings

The review establishes several principles relevant to SD-007:

First, the strategy of cancelling self-generated sensory input via motor signals is general — it is not a specialisation of one sensory system but a common computational principle implemented at the earliest stages of central sensory processing across modalities.

Second, the cerebellum and cerebellum-like structures are central to this computation. They receive efference copies of motor commands and compute predictions of the expected sensory reafference. These predictions are subtracted (or gate) the actual sensory signal.

Third, and most important for SD-007's design choices, visual reafference cancellation operates at cortical stages rather than at the subcortical first relays used by vestibular and somatosensory systems. Motor-related inputs to visual cortical areas cancel visually-evoked responses to self-generated movement. This means the appropriate biological analogue for SD-007's latent-level subtraction is specifically the cortical visual implementation, not the brainstem vestibular one — and the cortical implementation is precisely a transformation of a higher-level representation, consistent with SD-007's placement of the predictor at the latent encoding stage.

The review also discusses the continuous calibration requirement: the brain must continuously update the relationship between motor commands and their expected sensory consequences as these relationships change (growth, injury, environmental perturbation). A predictor that is only trained initially would drift.

## REE mapping

SD-007 implements: z_world_corrected = z_world_raw - ReafferencePredictor(z_world_raw_prev, a_prev). This review provides the cross-modal endorsement that the principle is sound — motor signals do cancel sensory reafference in visual processing, and they do so at a representational (cortical/latent) level. The paper's description of cerebellum-like structures computing predictive subtraction is the biological specification that SD-007 approximates with a learned neural network predictor.

The distinction between exafferent (externally generated) and reafferent (self-generated) sensory input that the paper frames is exactly the distinction SD-007 needs to maintain: z_world_corrected should contain only exafferent world changes, not the perspective shift caused by the agent's own locomotion.

## Limitations and caveats

As a review, this paper synthesises evidence rather than generating primary data. The visual processing section is necessarily more heterogeneous than the vestibular section, which has more controlled single-unit literature. The specific cortical areas and circuit mechanisms for visual reafference cancellation in primates remain more contested than the vestibular nucleus circuit. For SD-007, the main caveat is that the biological calibration dynamics are not currently modelled — the ReafferencePredictor is trained during an initial phase but the continuous recalibration described in the review is not implemented.

## Confidence reasoning

Confidence is 0.80 — the highest of the four entries for SD-007. This is because the review directly covers visual processing, reducing modality transfer risk, and provides a principled cross-modal framework that endorses SD-007's design. The source quality is high (Cullen lab, established review, covers extensive primary literature). The main uncertainty is the abstraction gap between the biological motor command and the REE discrete action token.
