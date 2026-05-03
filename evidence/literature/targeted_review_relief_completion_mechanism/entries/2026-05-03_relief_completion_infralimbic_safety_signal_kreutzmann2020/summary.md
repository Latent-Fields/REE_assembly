# Kreutzmann, Jovanovic & Fendt 2020 — Infralimbic cortex activity is required for the expression but not the acquisition of conditioned safety

## What the paper did

Kreutzmann's group conditioned rats on a safety paradigm — a CS- that was explicitly *unpaired* with the shock US, so it came to predict the *absence* of the aversive event — and tested whether the infralimbic cortex (IL) is required for either learning the safety association or expressing it. They used local muscimol injections to temporarily inactivate the IL either before conditioning (to test acquisition) or before retrieval (to test expression), and ran the same tests on the prelimbic cortex (PL) as a control for adjacent-region nonspecificity.

## Key finding

Inactivating the IL before conditioning had no effect on acquisition. The animals could still learn the safety association with their IL silenced. But inactivating the IL before retrieval completely abolished the expression of safety — the safety-CS no longer attenuated startle. PL inactivation during expression had no effect. So the safety-cue prediction is *encoded* somewhere else but *expressed* through an IL-specific route.

This dovetails with the broader literature on IL function in fear extinction and with the Meyer 2019 finding (in this slate's neighbourhood) that ventral-hippocampus-to-PL projections matter for conditioned inhibition. The picture that emerges is that the predictive encoding of safety has its own circuit, distinct from both the amygdalar fear circuit and the ventral-striatal relief-completion circuit.

## How it translates to REE

This is the entry that prevents the slate from being a clean win for Model 1. The Andreatta 2012 and Navratilova 2012 results establish that the relief-completion *event* reuses reward-circuit machinery. This entry shows that the predictive encoding of safety *cues* has its own substrate (IL) that is dissociable from both reward and aversive circuits. So the architectural question is more subtle than the original M1/M2 framing.

The cleanest reading is hybrid:
- **Relief-completion event itself** (Model 1): fires the same downstream tag-and-release pipeline as goal-achievement. MECH-057a (commitment release / beta gate drop), MECH-091 (phase reset), MECH-094 (categorical write gate) can all be reused, with polarity set at the input (suffering-derivative crossing threshold) rather than via parallel circuitry.
- **Safety-cue prediction** (Model 2 / parallel): an IL-equivalent encoder that learns "this cue predicts relief / safety / threat-absence" as a separate predictive structure from "things liked." This is what gets read out when the agent decides whether the current context is safe enough to release the avoidance commitment in the first place.

For REE the implementation implication is that the completion event can be a single MECH that reuses existing infrastructure, but the safety-cue learning probably wants its own MECH and may map onto different downstream behaviour (modulating commitment thresholds, guiding approach toward safety-associated stimuli, etc.).

## Limitations and caveats

Conditioned safety here uses the explicitly-unpaired procedure, which produces a CS- that predicts threat *absence*. There is a behavioural dissociation in the literature (Andreatta 2017) between threat-absence and threat-termination signals — they are not interchangeable. So the IL result is most directly relevant to threat-absence prediction; the threat-termination (relief proper) story may have a different anatomical pattern. This is one of the reasons the recommendation has to be hybrid rather than a clean Model 2.

The paper does not record from the IL during relief itself, only during safety expression. So the strong claim — IL is *not* part of the completion-event circuit — is consistent with the data but not directly tested.

## Confidence

Source quality is good (Psychopharmacology, well-controlled with PL comparison and both sexes). Mapping fidelity is moderate because the paradigm tests one specific operationalisation. Transfer risk is moderate. Net confidence 0.74, weakens — in the sense that it weakens the simple Model 1 reading by surfacing a parallel substrate for safety-cue prediction.
