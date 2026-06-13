# Badre & Frank 2012 — Hierarchical RL in cortico-striatal circuits (SD-042 options biological warrant)

**Claim grounded:** SD-042 (option library substrate).
**Direction:** supports (deliberately bounded). **Confidence:** 0.72.
**Role:** discharges OBJ-ABS-8's named "options-formalism check" under the biology-before-formal-definitions rule.

## Why this entry exists

SD-042 imports a *formal* construct — the Sutton-Precup-Singh (1999) options framework, where a reusable subroutine is an (initiation set, termination function, internal policy) triple. The project has a standing rule (`feedback_biology_before_formal_definitions`): a formal RL/control/information-theoretic construct must carry an explicit biological warrant *before* its substrate is built, because "philosophy-right / mechanism-wrong" is a recurring failure mode (SD-003, SD-010/011). Botvinick, Niv & Barto 2009 — already in this directory, now tagged SD-042 — is the framework anchor, but it is itself a theoretical review whose neural mapping is, by its own admission, partly inferential. So the node's remaining debt was a more empirical biological warrant. This entry supplies it.

## What the paper did

According to PubMed, Badre & Frank (2012, *Cerebral Cortex*; [DOI](https://doi.org/10.1093/cercor/bhr117)) tested predictions of a neural-circuit model (developed in the companion Frank & Badre 2011 computational paper) in which contextual representations in rostral frontal cortex influence the striatal gating of representations in more caudal frontal cortex, with reinforcement learning operating at each level of the hierarchy. Using a model-based reanalysis of a hierarchical reinforcement-learning task (abstract action-rule discovery), with trial-by-trial latent hypothesis-state estimates from a Bayesian "mixture of experts" model, the fMRI results validated the key prediction: there is evidence for an individual cortico-striatal circuit performing reinforcement learning of hierarchical structure *at a specific level of policy abstraction*, consistent with hierarchical control emerging from nested cortico-striatal circuits operating at different abstraction levels.

## How it maps, and where it stops

The mapping is honest about its own boundary. What Badre & Frank warrant is that a biological substrate — human cortico-striatal loops with a rostro-caudal frontal gradient — genuinely *learns and represents policy at nested levels of abstraction* via striatal gating. That is the substrate an option library would inhabit, and it establishes that hierarchical, temporally/contextually extended policy abstraction is not a purely formal convenience but something cortico-striatal circuits actually do. What it does **not** warrant is the option triple itself: the fMRI speaks to levels-of-abstraction and gating, not to initiation-sets, termination-functions, and hidden internal policies as the brain's representational format. Nor does it address how option boundaries are *discovered* from experience — the same open question Botvinick flagged.

So I read SD-042 as biologically licensed at the architecture level (a hierarchy-learning cortico-striatal substrate exists, options are a reasonable formalism for it) while its specific formal instantiation remains a V4 design choice to be tested, not a fact read off the biology. That is why this entry is pinned at 0.72 — below the chunking entries — with `mapping_fidelity` explicitly held at 0.62. The bounded confidence *is* the biology-before-formal-definitions discipline doing its job.

This raises SD-042's literature_confidence only. Experimental_confidence stays 0 (SD-042 is `implementation_phase: v4`, and it is the most environment-gated pillar in the plan — gridworld is definitively too simple to validate options) — **this promotes nothing.**
