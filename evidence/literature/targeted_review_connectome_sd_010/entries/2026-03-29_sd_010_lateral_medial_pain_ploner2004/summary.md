# Ploner & Schnitzler (2004) -- Cortical Representation of Pain

## What the paper did

Ploner and Schnitzler reviewed the cortical network for pain processing in humans, drawing on neuroimaging, electrophysiology, and lesion data available up to 2004. The review is framed around the parallel cortical areas consistently activated in pain studies: primary somatosensory cortex (S1), secondary somatosensory cortex (S2), insular cortex, and anterior cingulate cortex (ACC). The paper also addresses the temporal dynamics of cortical pain responses, in particular the distinction between first pain (fast, sharp) and second pain (slow, aching).

## Key findings relevant to SD-010

The review establishes that S1 cortex is principally responsible for the sensory-discriminative aspects of pain -- intensity estimation, spatial localisation, and quality discrimination. ACC, in contrast, is the primary cortical substrate for the affective dimension: how unpleasant the pain is and the motivational drive to escape or avoid it. S2 is positioned between these poles, contributing to recognition, learning, and memory of painful events.

The first-pain / second-pain dissociation is particularly relevant for SD-010. First pain is transmitted by fast-conducting A-delta fibres (neospinothalamic pathway) and is characterised by sharp, precisely localised sensation with rapid onset. It corresponds predominantly to activation of S1 cortex. Second pain is carried by slower C fibres (paleospinothalamic pathway), is diffuse and aching in character, and activates ACC more strongly than S1. This temporal dissociation at the cortical level provides a functional validation of the anatomical pathway distinction described by Willis and Westlund: the biological system really does route these two streams to different cortical processors.

## Translation to REE

SD-010 proposes a separate HarmEncoder for the harm stream. The Ploner/Schnitzler dissociation maps cleanly onto the SD-011 further split into z_harm_s and z_harm_a. z_harm_s (proximity/intensity, action-predictable) is the computational analogue of first pain -- sharp, localised, encoding "what and where." z_harm_a (accumulated homeostatic deviation, motivational urgency) is the analogue of second pain -- diffuse, slow-integrating, encoding "how urgent is escape." The fact that ACC lesions reduce affective unpleasantness while leaving sensory discrimination intact -- a finding mentioned in the review -- is direct evidence that the affective stream can be selectively disrupted without losing location/intensity coding. This is structurally analogous to SD-010's claim that z_harm can be separated from z_world without losing harm-specific signal.

## Limitations and caveats

This is a German-language review; only the English abstract was directly available for extraction. The 2004 date means it predates modern high-resolution fMRI and connectivity studies. The S1/ACC distinction, while robust, is not absolute: later work has shown S1 can encode some affective qualities (see Case et al. 2016 on affective touch), and ACC encodes some intensity information. The clean dissociation is best understood as a difference in relative weighting rather than categorical separation.

## Confidence reasoning

The source is a specialist review published in a peer-reviewed neurology journal, broadly consistent with the consensus literature. The first-pain/second-pain dissociation is well-replicated. The mapping to SD-010 is strong for the two-stream architecture (z_harm_s vs z_harm_a) but only indirectly supports the primary SD-010 claim about separating harm from world-state. Overall confidence 0.78.

Based on articles retrieved from PubMed. DOI: https://doi.org/10.1007/s00115-004-1739-y
