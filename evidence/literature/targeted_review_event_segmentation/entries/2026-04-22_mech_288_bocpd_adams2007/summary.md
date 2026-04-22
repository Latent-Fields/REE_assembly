# Adams & MacKay 2007 -- Bayesian Online Changepoint Detection

This is the canonical reference for online Bayesian change-point detection. [DOI](https://doi.org/10.48550/arXiv.0710.3742). arXiv preprint 0710.3742.

## What the paper does

Adams and MacKay derive an exact online algorithm for inferring the most recent change-point in a univariate time series. The algorithm maintains a posterior distribution over the run-length (time since the last change-point), updated by message-passing each step. Given a parametric model of the segment data and a hazard function for change-point occurrence, the run-length posterior gives a calibrated probability that a change-point occurred at any past timestep -- including the current one.

## Findings relevant to MECH-288

BOCPD is the substrate-algorithm candidate (a) in the MECH-288 spec's question 4. Its decisive advantages over threshold-on-PE (candidate c): (i) provides a calibrated probability of boundary, not a thresholded indicator -- which gives MECH-287 a graded broadcast strength rather than binary fire; (ii) handles non-Gaussian segment distributions via choice of parametric model; (iii) has well-understood pruning techniques to keep the posterior bounded. Its disadvantages: (i) requires a parametric assumption about within-segment data distribution; (ii) more compute than threshold-on-PE per step.

## Mapping to REE

MECH-288 substrate algorithm candidate (a) BOCPD: maintain a run-length posterior over each watched stream (z_world, z_self motor-sensory, z_goal); emit a boundary when posterior probability of run-length=0 exceeds a threshold (or use the posterior mass directly as a graded boundary signal for MECH-287). For Phase 2 implementation, BOCPD on z_world with a Gaussian segment model is the simplest principled starting point. The hazard rate becomes a tunable hyperparameter controlling expected segment length.

A pragmatic alternative for the fast-scale (sensory) segmenter: threshold-on-PE per Heilbron 2018 evidence is biologically supported and cheaper. BOCPD for the slow-scale integrative segmenter where calibrated boundary probability has more value (it controls MECH-287 broadcast strength).

## Limitations and caveats

BOCPD is a generic time-series algorithm with no biological grounding. It is included as the engineering candidate that best mirrors what biology computes when one frames event boundaries as latent change-points. Biological circuits are not BOCPD; BOCPD is what an engineer would write to capture the same computational role. The substrate plan should not claim BOCPD is biologically plausible -- only that it is the computational analogue of the Baldassano HMM with online inference rather than batch.

## Confidence reasoning

0.80 supports (algorithm guidance). Highly cited engineering reference. Mapping fidelity high for the algorithm-design lesson. Transfer risk moderate because BOCPD has no biological grounding -- it is the substrate-engineering candidate, not the biology.
