# Baldassano et al. 2017 -- Discovering event structure in continuous narrative perception and memory

According to PubMed, this is the foundational fMRI demonstration that cortical activity during continuous narrative is naturally structured into a nested hierarchy of events. [DOI](https://doi.org/10.1016/j.neuron.2017.06.041)

## What the paper does

Subjects watched a TV episode (BBC Sherlock) or listened to an audio narrative while fMRI measured cortical activity. The authors fit a hidden Markov model to each cortical region's activity, where the HMM is constrained to find a sequence of stable-pattern states with sharp transitions between them. They did this without using any external annotation -- the boundaries are discovered from the data. They then asked: how many events does each region split the narrative into? And do high-order event boundaries trigger hippocampal activity that predicts later memory?

The answers: early sensory regions produced many short events (seconds); high-order regions (angular gyrus, posterior medial cortex, mPFC) produced fewer long events (tens of seconds to minutes). The hierarchy is genuinely nested -- long-event boundaries align with subsets of short-event boundaries. And boundaries at the integrative scale drove hippocampal activity that predicted free-recall reinstatement.

## Findings relevant to MECH-288

Three findings carry. (1) Boundary detection in biology is hierarchical, not flat. A single segment_id stream cannot capture what biology actually does. (2) The HMM (stable-state with sharp transitions) is itself a workable substrate algorithm -- this is a "latent change-point under variational inference" instantiation, MECH-288 trigger criterion (b) algorithm candidate (d) in the spec's Q4. (3) Integrative-scale boundaries drive hippocampal activity. This is direct evidence for the (c) coupling option in MECH-287 question 3: the broadcast trigger is downstream of integrative-scale boundary detection.

## Mapping to REE

The substrate recommendations are concrete. (a) The event_segmenter should support a hierarchy of segment_ids. The simplest non-trivial implementation is two scales: a fast scale tracking sensory-stream change (z_world, z_self motor-sensory) and a slow scale tracking integrative-stream change (z_goal, z_world long-time-constant component). Segment IDs key the substrate as outer.inner (e.g. "goal_segment.action_subsegment"). (b) The slow-scale boundary should drive MECH-287 broadcast at the moment of detection -- one less component for MECH-287 to carry on its own. (c) The HMM/latent-change-point algorithm class is empirically validated; threshold-on-PE remains an alternative for the fast scale because it is cheaper.

## Limitations and caveats

Baldassano's hierarchy emerges from cortical region anatomy via fMRI; the substrate's hierarchy must emerge from architectural choice -- which streams to watch with which time constants. The paper does not tell us what those time constants are for an artificial agent. Nor does it adjudicate the extreme of "every region has its own timescale" vs "there are 2-3 canonical timescales" -- the data are smoothly graded.

A second caveat: the HMM method assumes that segments are discrete stable-state intervals. If the underlying latent streams transition smoothly, the HMM will introduce sharp cuts where there are none. For REE, this is conservative for an event_segmenter (false positives in stable regions are cheap; false negatives at real change-points are expensive).

## Confidence reasoning

0.90. Neuron, widely cited, methodologically rigorous, with direct hippocampal-coupling evidence. Mapping fidelity is high because the hierarchical-timescale finding is exactly the empirical content of MECH-288 question 2, and the HMM method is one of the algorithm candidates from question 4. Transfer risk is the usual fMRI-to-substrate concern.
