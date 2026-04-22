# Brunec et al. 2018 -- Multiple scales of representation along the hippocampal anteroposterior axis in humans

According to PubMed, this fMRI study showed a graded gradient of temporal scales along the human hippocampal long axis, mirroring the rodent dorsal/ventral place-field gradient. [DOI](https://doi.org/10.1016/j.cub.2018.05.016)

## What the paper does

fMRI of healthy human adults during navigation and rest. The authors measured voxel-time-course autocorrelation (signal stability over time) along the anteroposterior axis of the hippocampus. Anterior HC showed slower BOLD signal change and higher autocorrelation; posterior HC showed faster signal change and lower autocorrelation. The gradient is continuous, not stepped, and parallels the rodent ventral/dorsal place-field-size gradient.

## Findings relevant to MECH-288

This addresses the spec's question 5 directly: is place-cell-field-scale a parametric refinement of the same algorithm or a fundamentally different substrate? Brunec answers: parametric refinement. Place-cell-field-scale (posterior HC, fast) and event-segment / schema-scale (anterior HC, coarse) sit on a continuous gradient of one anatomically-graded substrate.

## Mapping to REE

Q5 verdict: place-cell-field scale and event-segment scale are parametric variants of ONE substrate, not separate substrates. The MECH-288 event_segmenter should use the same boundary-detection algorithm with different time-constant parameters per scale, rather than implementing separate detectors. Concretely: parameterise the event_segmenter with `tau` (smoothing time-constant) and `min_segment_length`. Setting `tau` short and `min_segment_length` short gives place-cell-field-scale resolution; setting them long gives event-segment-scale resolution. Different downstream consumers can subscribe to different parameter settings.

This is consistent with the v_s_foundation SYNTHESIS verdict 1: default to schema/event-segment but support multi-scale. The Brunec gradient gives the architectural justification for the "parametric multi-scale" approach.

## Limitations and caveats

The gradient is observed in human BOLD; the substrate-level analogue (different time constants in different anchor-set keys) is an architectural inference. The paper does not directly test multi-scale event-segmentation -- it shows the timescale gradient in resting-state and navigation BOLD. The transfer to MECH-288 is via the inference that one algorithm with parametric scales is a better fit to biology than separate substrates per scale.

## Confidence reasoning

0.74. Current Biology, well-controlled. Mapping moderate-to-high for the architectural Q5 verdict (parametric refinement vs separate substrate). The paper does not directly test event segmentation but the gradient evidence is exactly the architectural lesson.
