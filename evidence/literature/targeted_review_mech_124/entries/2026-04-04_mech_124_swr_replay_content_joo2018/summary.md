# SWR Replay Is Salience-Weighted: The Mechanistic Basis for Harm-Biased Offline Replay

**Joo, H.R. & Frank, L.M. (2018). The hippocampal sharp wave-ripple in memory retrieval for immediate use and consolidation. *Nature Reviews Neuroscience*, 19(12), 744-757. DOI: 10.1038/s41583-018-0077-1**

---

## What the paper did

Joo and Frank wrote a comprehensive mechanistic review of hippocampal sharp wave-ripple (SWR) biology, covering their physiological properties, their role in both awake and sleep-state memory retrieval, and their contribution to offline consolidation. The review synthesises electrophysiological data from rodent studies to characterise when SWRs occur, what content they carry, and how that content is related to prior experience. Crucially for MECH-124, the review establishes that SWR replay is not a faithful, uniform re-run of all recent experience -- it is content-biased by the salience of the encoded events, particularly by reward magnitude and novelty.

## Key findings relevant to MECH-124

The central finding for MECH-124 is that SWR replay content is reward-weighted: higher reward magnitude increases the rate of reverse replay events, whereas decreases in reward magnitude reduce it. SWRs occur preferentially after novel rewarding experiences, with rates particularly elevated immediately after reward receipt in unfamiliar locations. This establishes that the offline replay system is not sampling experience uniformly but is already weighting its sampling by motivational salience.

This is the mechanistic precondition for MECH-124. If SWR replay (instantiated in REE as MECH-121) samples experience in proportion to salience, then a residue field that is harm-dominant will produce a harm-dominant replay schedule. Consolidation then amplifies what is most replayed. The MECH-124 loop -- harm salience -> harm-biased replay -> harm amplification -> stronger harm predictions -> further harm salience -- follows directly from the biology. The paper does not describe this as a failure mode; it is the ordinary function of an adaptive memory system that prioritises the consolidation of motivationally significant events.

## Translation to REE

For the MECH-124 risk diagnostic, the relevant question is: at the end of a V3 training episode, is z_goal salience competitive with z_harm salience in the residue field? If z_goal salience is systematically lower (as the EXQ-085 series suggests it can be), then a MECH-121-implementing replay system would disproportionately schedule harm traces for consolidation. Joo & Frank's reward-magnitude modulation finding supports the hypothesis that this would produce exactly the imbalance MECH-124 predicts: goal representations weakened by under-consolidation, harm predictions amplified by over-consolidation, and a self-amplifying loop establishing itself as the agent encounters fewer benefit experiences and more harm experiences as a consequence.

The paper also identifies that novel experiences -- not just rewarding ones -- elevate SWR rates. If harm events have novelty properties (unexpected, intense, first-encounter), this could further bias replay toward harm early in training, when both harm salience and harm novelty are high relative to goal salience.

## Limitations and caveats

This is primarily a reward-replay paper. The claim that aversive/threat salience biases SWR content analogously to reward salience is a reasonable extrapolation but is not directly established by Joo & Frank. There is less literature on aversive-replay bias than on reward-replay bias, and the evidence for symmetric treatment of positive and negative valence in SWR content selection is incomplete. Additionally, all primary data is from rodent electrophysiology; the REE SWR-equivalent (MECH-121) is a computational abstraction, and the mapping to biological SWRs requires careful interpretation.

## Confidence reasoning

Confidence is 0.76: exceptional source quality (Nature Reviews Neuroscience, Loren Frank), but mapping fidelity is reduced because the paper addresses reward-biased replay and the threat/harm inference requires extrapolation. The paper is best read as providing the mechanistic basis for salience-weighted replay (the foundation of MECH-121 and hence MECH-124) rather than direct evidence for harm-trace dominance. The inference is sound but carries more transfer risk than the Pace-Schott and van der Helm entries.
