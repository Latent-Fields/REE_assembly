# Stokes (2015) — 'Activity-silent' working memory in prefrontal cortex: a dynamic coding framework

**Claim:** ARC-063 (CandidateRule field with tolerance-gated availability). **Direction:** supports (fork-B side; and motivates a readout redefinition). **Confidence:** 0.76.

## What the paper argues

Stokes synthesises a body of human (EEG/MEG multivariate pattern analysis, TMS-reactivation) and monkey electrophysiology evidence to make one sharp point: **persistent elevated firing does not reliably accompany working-memory maintenance.** Delay activity waxes and wanes with the *momentary task-relevance* of the memorandum, and a memory can be decoded back out after a period in which the population was effectively silent. From this he argues that working memory is held not as ongoing spikes but in an **"activity-silent"** substrate — rapid short-term changes in effective synaptic connectivity, a hidden state that transforms how the network responds to subsequent input. The latent is recovered by *probing* (a new input perturbs the network and the stored pattern re-emerges), not by reading a continuous firing trace. This is the framework form of fork B in the V3-EXQ-666 autopsy.

## Why this is the load-bearing paper for the CRF fix

The CRF's failure in V3-EXQ-666 is structurally identical to the dissociation Stokes describes. Once e2_world_forward gives the CRF genuine differentiation (ARM_2: 10–16 distinct rules, pairwise distance 1.71), each rule matches only a narrow slice of contexts and is *unselected on almost every tick*. Under the current scheme its availability is an activity-dependent EMA that decays every tick and is only refreshed on match, so between sparse matches it erodes toward the retire floor and `crf_frac_active` collapses to 0.016. Stokes says the brain does not solve this by making unselected items keep firing — it solves it by holding them **silently** and reactivating them on probe. That yields two concrete prescriptions for the substrate:

1. **Maintenance should be latent, not activity-dependent.** A minted, differentiated rule's availability should persist across context-absent ticks as a synaptic-trace-like hidden state. Decay should be driven by interference/capacity (other rules overwriting the store), *not* by elapsed ticks-without-a-match. The per-tick `mature_availability_decay` is the offending term.

2. **The readiness readout is measuring the wrong thing.** `crf_frac_active` counts ticks on which a rule is actively firing (matched-and-gated). But a silently-maintained rule is *available yet silent* — its context simply hasn't recurred this tick. The biologically-faithful readout is the **fraction of differentiated rules whose maintained availability would clear threshold if their context recurred** — a "maintained/available pool" metric — independent of whether any context is present right now. This directly answers the autopsy's open question (fork B "would change the readiness readout, not just the credit dynamics"): yes, it does.

## Caveat

This is a framework review, not a single decisive experiment. The activity-silent substrate is *inferred* from the dissociation between decodable memory and absent persistent firing; it is not directly imaged as synaptic weights. And mapping an inferred cortical hidden state onto a discrete rule-field availability scalar is a mechanism-class analogy, not a literal synaptic-weight correspondence. But the central dissociation — memory retained while neurons are silent — is exactly the CRF's situation, which is why mapping fidelity is high (0.82).

## Confidence reasoning

High mapping fidelity because the paper's core phenomenon *is* the CRF's problem. Source quality strong-for-a-review but below the primary electrophysiology anchors. Transfer risk low-moderate: the activity-silent principle is now supported across species and modalities and is the mainstream reading of the maintenance debate.
