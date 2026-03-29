# Willis & Westlund (1997) — Neuroanatomy of the pain system and of the pathways that modulate pain

**Source:** Journal of Clinical Neurophysiology 14(1):2-31. DOI: 10.1097/00004691-199701000-00002. PMID: 9013357.

## What the study did

William D. Willis and Karin N. Westlund's 1997 comprehensive review synthesises several decades of anatomical and physiological work characterising the ascending nociceptive pathways in detail. This is not a summary paper for general audiences but a technical reference: it covers the organisation of nociceptors, dorsal horn processing and sensitisation, and then systematically describes six ascending nociceptive pathways — spinothalamic, spinomesencephalic, spinoreticular, spinolimbic, spinocervical, and postsynaptic dorsal column pathways. The spinothalamic tract receives the longest treatment, consistent with its dominance in human pain transmission. Thalamic processing and cortical projections are described, and the descending modulatory systems (PAG, locus coeruleus, raphe, RVM, anterior pretectal nucleus) are detailed.

Willis was one of the two or three most important experimental neuroanatomists of the spinothalamic tract in the 20th century, having spent his career at the University of Texas Medical Branch using anterograde and retrograde tract-tracing, electrophysiology, and lesion studies to characterise STT organisation. This review represents a distillation of that body of work.

## Key findings

The central anatomical finding relevant to SD-011 is the lateral/medial division of the spinothalamic tract. The lateral STT projects primarily to the ventral posterolateral (VPL) thalamic nucleus, which relays nociceptive information to primary and secondary somatosensory cortex (S1, S2). This pathway is characterised by precise somatotopic organisation: lesions at different levels of the STT produce topographically predictable sensory loss, and VPL neurons respond to nociceptive input with spatial and intensity discrimination. This is the sensory-discriminative channel.

The medial STT projects to intralaminar and posterior thalamic nuclei (central lateral, parafascicular, posterior intralaminar complex). These nuclei have diffuse cortical projections targeting ACC, anterior insula, and prefrontal areas. Unlike the VPL pathway, the medial projection lacks precise somatotopy; it is characterised by large receptive fields and responses that are more related to arousal and motivational significance than to precise sensory discrimination. This is the affective-motivational channel.

Willis and Westlund also describe the spinomesencephalic and spinolimbic pathways, which provide additional fast routes for nociceptive information to reach the amygdala, periaqueductal gray (PAG), and hypothalamus — deepening the parallel between their anatomical description and the SD-011 two-stream model. These additional routes suggest that z_harm_a may receive convergent input from multiple ascending pathways, not only the medial STT.

The descending modulation systems described are relevant for REE's valence architecture: the PAG/RVM system provides harm-signal gating (equivalent to an attention or salience gate on z_harm_s), while the locus coeruleus noradrenergic system modulates arousal and attentional allocation across the pain system broadly.

## REE translation

This paper provides the most anatomically grounded evidence that the lateral/medial STT distinction constitutes a genuine biological separation of the two streams that SD-011 proposes. The key architectural point is that the divergence occurs early — at the level of spinal cord ascending projections — rather than being a late cortical computation. This early separation is what justifies treating z_harm_s and z_harm_a as distinct latent variables in the REE architecture rather than as two readout functions of a single upstream representation.

The additional ascending pathways (spinomesencephalic to PAG, spinolimbic to amygdala) suggest that z_harm_a in REE should be thought of as receiving convergent input from multiple fast harm-detection routes. The amygdalar projection in particular is relevant: amygdala receives direct spinal input and can generate immediate avoidance responses before cortical processing completes. In REE terms, this is an automatic z_harm_a activation that precedes deliberate evaluation — a fast pathway that could seede z_harm_a before z_harm_s has resolved the location/nature of the harm. This has implications for the relative timing of the two streams in the REE implementation.

## Limitations and caveats

The most important anatomical caveat is collateralisation: a non-trivial proportion of STT neurons send axon collaterals to both lateral and medial thalamic targets. If this is common, then z_harm_s and z_harm_a receive overlapping input from the same source neurons, and their functional independence arises from downstream processing rather than from genuinely separate input channels. The review does not fully quantify this, and the literature at the time was not settled. This caveat matters for whether the stream separation should be implemented at the input level in REE (truly independent input features) or at the processing level (shared input, divergent processing).

A second caveat is species: most of Willis and Westlund's primary data comes from cats and monkeys. Human clinical correlates (anterolateral cordotomy effects on pain) are broadly consistent with the lateral/medial distinction, but the precise organisation may differ. The cordotomy literature shows that lateral STT lesions produce loss of pain sensation (z_harm_s effects), while patients often retain some emotional response to pain even after lesions — supporting the stream separation in humans, but imprecisely.

## Confidence reasoning

Willis and Westlund 1997 is the definitive anatomical reference for the STT organisation underlying SD-011's proposed stream separation. Its authority is unquestioned in the pain anatomy literature. The confidence is modestly lower than Rainville 1997 and Craig 2002 because the transfer from animal anatomy to REE's computational architecture requires the most inferential distance — the gridworld harm signal is not generated by nociceptors, and there are no spinal cord neurons to draw a lateral/medial distinction from. What the paper provides is the biological justification for why the functional separation is a reasonable design choice, not a direct experimental demonstration in the REE domain. Confidence: 0.84.
