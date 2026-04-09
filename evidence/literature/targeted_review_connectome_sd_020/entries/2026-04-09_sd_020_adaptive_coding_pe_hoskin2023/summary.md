# Summary: Hoskin and Talmi (2023) -- Adaptive coding of pain prediction error in the anterior insula

**Entry:** 2026-04-09_sd_020_adaptive_coding_pe_hoskin2023
**Claim tested:** SD-020
**Evidence direction:** supports

## What the study did

Hoskin and Talmi applied an axiomatic approach to identify adaptive coding of pain prediction error in fMRI data from 19 healthy adults who performed a cued-pain task. In adaptive coding, neural responses reflect the local context of stimulation rather than absolute magnitude -- a response pattern seen in value coding in orbitofrontal cortex and is mathematically related to relative rather than absolute PE. The axiomatic approach tests for this pattern non-parametrically, without assuming a specific generative model for how predictions are formed. Participants received thermal pain stimuli at varying intensities preceded by predictive cues, and BOLD responses were analysed for evidence of context-relative (adaptive) coding.

## Key findings

The left dorsal anterior insula showed a pattern consistent with adaptively coded pain prediction error. Specifically, signals in this region were sensitive to both the predicted pain magnitude (at the time of cue delivery, reflecting expectation) and the unexpectedness of pain delivery (at the time of stimulus, reflecting PE), with responses calibrated to local context rather than absolute magnitude. The authors describe this as the first evidence that anterior insula codes pain PE adaptively -- responding to how much pain deviated from contextual prediction, not to how much pain there was.

## REE translation

SD-020's central claim is that z_harm_a should encode how surprising the current threat level is rather than how high it is. Hoskin and Talmi's finding is a direct fMRI demonstration of this: anterior insula responds to the unexpectedness of threat relative to context. The SD-020 redesign of the auxiliary loss target -- replacing raw harm accumulation with the mismatch between predicted and actual harm -- directly implements adaptive/contextual PE coding. E3 urgency driven by this signal will be highest when harm escalates unexpectedly, which is precisely when behavioural policy update is most needed.

## Limitations and caveats

The sample (N=19) is small by contemporary fMRI standards and replication in larger cohorts is warranted. The axiomatic approach, while principled, is less established in pain neuroscience than standard model-based PE decomposition (as used by Geuter 2017 and Horing 2022), and the two approaches may not be directly comparable in terms of what 'PE' means. The mapping from 'adaptive coding' to 'precision-weighted PE' as formulated in predictive coding theory requires an inferential step that the paper itself does not make explicit. The study used only thermal pain in healthy adults; generalisation to the broader harm signals REE encounters requires an assumption.

## Confidence reasoning

Confidence 0.82. Source quality moderate-high: European Journal of Pain, peer-reviewed, principled methodology, but smaller sample. Mapping fidelity high: 'unexpectedness not absolute magnitude' is a verbatim restatement of SD-020. The slight discount from Horing 2022 reflects the smaller sample and the gap between adaptive coding and formal precision-weighted PE. This paper complements Geuter 2017 and Horing 2022 by providing an independent methodological approach that converges on the same conclusion.
