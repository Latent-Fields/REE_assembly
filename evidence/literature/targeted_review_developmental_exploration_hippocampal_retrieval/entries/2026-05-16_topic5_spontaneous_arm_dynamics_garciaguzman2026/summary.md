# Infants' spontaneous movements explore arm dynamics
**Garcia-Guzman et al. (2026) -- Communications Biology**

## What the paper did

Garcia-Guzman, Ros, and Luque at the University of Granada used RGB-D motion capture and YouTube video recordings of 20 infants (producing 270+ spontaneous movement units) to ask a pointed question: are infant spontaneous movements simply the output of an immature, noisy motor system, or do they systematically probe a different region of the action space than goal-directed reaching? They introduced a synthetic data-driven approach -- generating comparison datasets by sampling movements from inverse dynamics models calibrated to the infant arm -- so they could compare empirical spontaneous movements against movements that are kinematically reaching-like but computationally generated.

## Key findings

The results are striking. Spontaneous movements engaged arm dynamics more extensively than reaching-like motions: acceleration distributions were skewed toward trajectories that maximize dynamic excitation of the arm, not trajectories that minimize jerk or optimize for a spatial target. The kinematic space explored by spontaneous movements showed significantly higher variability than goal-directed reaching. Both effects held at the individual infant level and at the cluster level when movements were grouped by type.

## REE translation

For REE, this paper provides direct empirical support for the claim that behavioral diversity generation (ARC-065) is not a degraded or noisy version of goal-directed action -- it is a distinct functional mode optimized for different objectives. The infant is not failing to reach; it is succeeding at probing the dynamics of its own body. This is the developmental logic behind INV-073: an agent that skips this exploration phase cannot discover what its action space is capable of.

The practical implication for REE's infant substrate is that the diversity metric should include coverage of the action-dynamic range, not just action-index entropy. An agent that repeatedly selects the same 3 actions at high confidence but varies their timing would score zero on dynamic richness even with apparently high temporal variability.

## Limitations and caveats

The study measures arm movement only; it is silent on lower-limb, locomotor, or whole-body exploration. The comparison assumes a clean categorical distinction between spontaneous and reaching-like movements that may blur in naturalistic settings. The paper does not measure what representational structure the infant builds from this exploration, so the claim that dynamic richness is functionally necessary remains inferential.

## Confidence reasoning

Strong empirical paper in a Nature-family journal with a thoughtful synthetic comparison design. Confidence 0.82 -- minor deduction for the limited scope (arms only) and the inference gap between kinematic richness and representational benefit.
