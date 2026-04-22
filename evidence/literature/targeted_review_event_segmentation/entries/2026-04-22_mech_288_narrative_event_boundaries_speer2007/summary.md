# Speer, Zacks & Reynolds 2007 -- Human brain activity time-locked to narrative event boundaries

According to PubMed, this is the first direct fMRI evidence that event-boundary perception is associated with transient cortical activity. [DOI](https://doi.org/10.1111/j.1467-9280.2007.01920.x)

## What the paper does

Subjects read brief narratives describing everyday activities while fMRI recorded brain activity. They later re-read the same stories to mark large and small event boundaries. The authors then asked: do the moments later identified as boundaries show transient activity changes during the original reading? They do. And the activity is mediated by specific situational features -- changes in characters' goals, locations, objects, time, and other narrative dimensions.

## Findings relevant to MECH-288

Two findings matter here. First, boundaries are real neural events: there is detectable transient activity at the moments biology calls boundaries. This is the empirical complement to Zacks 2007's theoretical claim. Second, the boundary signal is multi-mediated -- it tracks changes in goals AND locations AND objects AND time. A substrate that only watched one latent stream (only z_world, say) would systematically miss boundaries biology does perceive.

## Mapping to REE

The substrate-level translation is twofold. (1) Event boundaries should emit a discrete segment_id transition rather than a continuous changing index -- biology shows transient activity at the boundary moment. (2) The event_segmenter should be able to read change signals from multiple latent streams in parallel (z_world for setting, z_self for action-mode shift, z_goal for goal change, etc.) and emit a boundary on any of them. This argues against a single-stream PE-threshold detector and toward an or-gate over multiple stream-specific change detectors.

## Limitations and caveats

fMRI BOLD activity lags by several seconds and integrates over many neurons. The "transient at boundary" signal is at this coarse scale, not at the single-substrate-step scale our event_segmenter operates at. The mapping is conceptual (boundaries produce discrete signals) not temporal. Second, the study uses narrative reading specifically -- a high-level semantic task whose mapping to a navigation-and-survival agent is not automatic.

## Confidence reasoning

0.78. The paper is widely cited but a single fMRI study with modest N. It supports MECH-288's premise that boundaries are real and multi-mediated, but it does not adjudicate between trigger criteria (PE-spike vs latent change-point vs task marker). For our purposes it is supporting evidence for the architecture, not for the specific algorithm.
