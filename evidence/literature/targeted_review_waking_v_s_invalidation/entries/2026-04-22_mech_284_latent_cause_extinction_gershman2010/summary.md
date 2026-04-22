# Gershman, Blei & Niv 2010 -- Context, Learning, and Extinction

According to PubMed ([DOI](https://doi.org/10.1037/a0017808)).

## What the paper does

Gershman, Blei, and Niv reformulate context-dependent learning and extinction in normative Bayesian terms. The core move is to treat the observer as inferring, online, which of an unbounded set of latent causes is currently generating the observed contingencies. Extinction in this framework is not erasure of the original learning -- it is the inference of a new latent cause that better explains the new observations. Renewal of the original response in the original context follows naturally: when the original context returns, the posterior shifts back toward the original latent cause. Latent inhibition is similarly recast as a prior bias toward attributing pre-conditioning observations to a "no-relationship" latent cause. Critically, the same machinery explains why young animals and hippocampally lesioned animals lose context-dependence: their capacity to infer new latent causes is restricted.

## Why it matters for V_s invalidation

This paper is the load-bearing computational frame for the entire V_s architecture. The latent-cause posterior over the current observation IS V_s for the currently anchored cause. High posterior = the anchor is still the right model = high V_s. Low posterior together with high posterior on a competing latent cause = the anchor should be invalidated and a new one should take over. MECH-284's accumulator is the Bayesian update integrating new observations into the posterior. MECH-269's anchor reset is the moment the posterior over a competing cause crosses a threshold sufficient to license switching the operative anchor.

The reason this paper carries more architectural weight than any of the empirical neuroscience papers is that it provides the *form* the brain's solution must take. Whatever circuits implement this -- OFC for state-label, DA for generalized PE, alEC/DG for interference detection, LHb for reward-omission triggers -- they are implementing some version of the Bayesian update Gershman et al wrote down. The empirical papers tell us where; the Gershman framework tells us what.

## Architectural implications

The framework gives us clean answers to several of the architectural questions in the spec:

- **Local vs broadcast.** The latent-cause posterior is local to the current task / context, but the trigger for revising it (a single observation that is unlikely under the current cause) can be a broadcast scalar. Both are consistent with the Bayesian framework.
- **Single failure vs accumulation.** The framework predicts accumulation in the form of evidence-integration toward the new posterior; a single mismatched observation shifts the posterior modestly, sustained mismatches shift it strongly. This matches the V3-EXQ-475 phenotype: single events register (modest posterior shift) but the system never accumulates enough evidence to flip the operative posterior.
- **Proportional vs threshold.** The posterior itself is graded but the read-out (which latent cause is operative for downstream computation) can be threshold-crossing, consistent with discrete re-anchoring after sustained graded change.
- **Coupling to replay priority.** Gershman 2017 (next paper) extends this framework explicitly to memory modification, which is the bridge to the offline MECH-285 replay-priority story.

## Clinical resonance

The "restricted capacity to infer new latent causes" failure mode -- young animals, hippocampal lesions -- maps to a wide range of clinical perseveration syndromes. OCD's compulsive routines persist despite repeated counter-evidence because the system cannot cross the posterior threshold to license inferring that the underlying cause has changed. PTSD's cued re-experiencing is the symmetric failure: the system maintains the original latent cause as competitive even when overwhelming new evidence should have inferred a new cause. Both are consistent with MECH-284's accumulator dynamics being implementation-specific failures of the Gershman framework.

## Confidence reasoning

Mapping fidelity 0.92 -- the highest in the pull. The framework essentially defines V_s. Source quality high (Psych Review). Transfer risk low because the framework is computational and species-general. Aggregate 0.82 -- the highest paper-level confidence in this set, reflecting that this paper does the computational work the rest of the architecture rests on.
