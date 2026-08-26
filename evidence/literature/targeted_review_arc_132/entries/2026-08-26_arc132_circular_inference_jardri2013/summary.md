# Jardri & Deneve (2013) -- Circular inferences in schizophrenia

**Claims tested:** ARC-132 (attractor-property differentiation), MECH-514 (counterfactual replay for attractor testing)
**Evidence direction:** supports (narrow) | **Confidence:** 0.35

## What the paper did

Jardri and Deneve build a hierarchical Bayesian message-passing model of cortical inference and
ask what happens when the balance between excitatory and inhibitory signalling in that hierarchy
is subtly disturbed. Their answer is a specific, mechanistic one: bottom-up sensory evidence and
top-down predictions, which should be discounted for the shared causal history they accumulate as
they pass back and forth through the hierarchy, instead get counted again and again -- a loop they
name "circular belief propagation." The model is not a metaphor; it is a working simulation that
the authors show reproduces several distinct clinical phenomena from this single mechanism at
once: erroneous perceptions and hallucinations, overconfident probabilistic judgements, learned
causal connections between events that are not actually related, and a paradoxical resistance to
perceptual illusions that a normally-calibrated visual system would fall for.

## Key findings relevant to the claim

The paper's central move -- one mechanism, several symptom clusters, all traceable to information
being double-counted rather than correctly discounted -- is the same qualitative shape as the
self-reinforcing loop the raw thought behind ARC-132 and MECH-514 describes: an attractor biases
what gets perceived and retrieved, that bias shapes what gets replayed, and the replayed material
is then miscounted as fresh, independent confirmation of the very attractor that produced it. In
both cases the failure is not that the system reasons badly in the abstract -- it is that content
generated *by* the system's own current state gets treated as evidence *about* the world, without
the bookkeeping needed to recognise it as non-independent. That is exactly the "central danger"
the raw thought names: material generated or interpreted through the attractor is counted as
independent evidence for it.

## How this maps to REE

ARC-132 argues the fix is architectural: an attractor's carried quantities (predictive
reliability, epistemic confidence, familiarity, affective valence, salience, action urgency,
self-relevance, source confidence) must stay separately readable, so that e.g. strong emotional
urgency or high familiarity cannot silently stand in for actual epistemic reliability. MECH-514
argues the fix is procedural: an offline protocol that keeps anchored evidence separate from its
interpretation and tags every replay-derived item with its provenance, so that ten simulations of
one episode are never miscounted as ten independent samples. Jardri and Deneve's model is real,
mechanistic evidence that failing to do *some* version of this bookkeeping -- discounting
reverberating, non-independent signal in a hierarchical inference system -- is a genuine way to
produce pathological overconfidence and spurious causal learning, not a hypothetical concern.
That corroborates why both claims treat the failure mode as worth designing against.

## Limitations and caveats

This is not a test of either claim, and I want to be honest about the size of the jump. Jardri
and Deneve's model concerns a specific circuit-level mechanism (excitatory/inhibitory imbalance)
in a hierarchical Bayesian message-passing scheme, evaluated against a clinical human population
with schizophrenia. Neither ARC-132's multi-axis carried-property architecture nor MECH-514's
cross-model counterfactual-replay protocol has any direct counterpart in the paper -- there is no
attractor with eight separable axes here, and no offline model-comparison procedure. The transfer
is cross-domain in two ways at once: clinical population to artificial architecture, and one
specific algorithmic failure to a general design principle. The raw thought's own "evidential
boundary" section is explicit that this literature is cited as failure-mode inspiration only, and
both claims' registration notes repeat that discipline -- this paper does not, and should not be
read to, establish that psychosis is one unitary precision failure, that axis-conflation is its
demonstrated mechanism, or that REE's specific remedies are what biology actually does.

## Confidence reasoning

Source quality is high -- this is a canonical, well-cited, peer-reviewed computational psychiatry
paper with a working model, not a speculative review. But mapping fidelity is kept moderate-low
and transfer risk is scored high, per the lit-pull calibration guidance to weight mapping fidelity
heavily for architectural claims: the structural analogy (non-independent signal double-counted as
confirmation) is genuine and worth recording, but it is an analogy, not a direct test, and both
target claims are explicit that this citation should not be leaned on for more than that. The
resulting confidence (0.35) sits in the "weak/ambiguous mapping" band by design -- this entry
supports the failure-mode motivation for ARC-132 and MECH-514 without hardening either claim.
