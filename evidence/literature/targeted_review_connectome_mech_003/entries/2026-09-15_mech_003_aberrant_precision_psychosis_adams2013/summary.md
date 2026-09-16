# The computational anatomy of psychosis (Adams, Stephan, Brown, Frith & Friston, 2013)

**Claim under test:** MECH-003 -- *Precision must be tau-scoped with lossy projections.*
**Direction:** supports

## Why this entry exists

MECH-003 does something most architecture claims do not: it names the clinical consequences of
violating it. Its "Prohibited Operations" section lists four architectural violations -- using
γ-scale surprise to directly raise δ-scale certainty, collapsing πγ…πδ into a single attention
scalar, letting E3 read untyped precision, letting precision bypass φ gating -- and asserts that
these "correspond to known failure modes: impulsivity, delusional certainty, manic over-commitment,
reward hacking."

That is a real commitment and it should be sourced rather than asserted. This paper is the best
available external warrant for the second item on the list.

## What the paper argues

Adams and colleagues treat psychotic symptoms as false inferences, on the premise that the brain is
an inference machine actively constructing hypotheses to explain its sensations. Their striking move
is a unification: hallucinosis, abnormal smooth pursuit eye movements, sensory attenuation deficits,
catatonia and delusions are all, they argue, expressions of *one* core pathology -- "an aberrant
encoding of precision." Not the content of any particular belief, but the confidence assigned to
beliefs, and specifically the *relative* confidence assigned to beliefs at different levels of a
predictive hierarchy. From the cognitive side they describe this as a failure of metacognition --
beliefs about beliefs -- which then confounds perceptual inference downstream. They supply a process
theory: hierarchical predictive coding, in which precision is encoded by post-synaptic gain on
error-reporting neurons, which in turn links the pathology to NMDA receptor function and dopaminergic
neuromodulation. Simulations of perceptual synthesis, smooth pursuit and agency attribution all run
on the same scheme with the same single lesion.

## How this bears on MECH-003

The relevant convergence is structural rather than detailed. Adams et al.'s claim is that what goes
wrong in psychosis is not any single level's precision but the *relationship between* levels'
precisions. That is the same shape as MECH-003's insistence that cross-τ influence must pass through
a projection operator which is slow and lossy. The whole point of requiring the operator to be lossy
is that a lossy operator *cannot* let a sharp fast spike set a slow belief's confidence -- it is
designed precisely to prevent the class of cross-level precision accident that Adams et al. say
produces psychosis. Read that way, MECH-003's projection constraints are not arbitrary engineering
hygiene; they are a deliberate architectural prophylaxis against a documented failure mode.

## The polarity problem, stated plainly

I do not want to let this pass, because it is the kind of thing that gets quietly assumed and then
cited back as settled. Adams et al.'s modelled pathology is **reduced precision of prior beliefs
relative to sensory evidence** -- high-level confidence too *low*. MECH-003's named violation is
"using γ-scale surprise to directly raise δ-scale certainty" -- high-level confidence driven too
*high* by a fast signal. On the face of it these point in opposite directions.

They can be reconciled, and the reconciliation is clinically familiar: if priors are weak, aberrant
sensory evidence forces a large revision of high-level belief to explain it, and the resulting
revised belief -- an explanation constructed under duress to account for a persistently surprising
world -- is then held with the pathological tenacity that makes it a delusion. That is a recognisable
account of delusion formation and it does connect the two framings. But it is an argument *we* are
making, not a result *they* report. Until REE writes it down explicitly, this entry supports
MECH-003's general thesis (cross-level precision relationships are where psychopathology lives) more
strongly than it supports MECH-003's specific violation clause.

## Limitations

The empirical content here is simulation, not patients: these are demonstrations that the proposed
pathology *can* generate psychosis-like behaviour in a model, not measurements showing that it *does*
in people. The unifying ambition -- one parameter change producing hallucinosis, catatonia and
delusions alike -- is simultaneously the paper's appeal and its evidential weakness, since a
mechanism that flexible is hard to falsify from symptom data. And the identification of precision
with post-synaptic gain, and thence with NMDA function and dopamine, is a strong implementational
commitment that is still contested; if it fails, the clinical mapping survives but the substrate
story MECH-003 leans on does not.

## Confidence

0.62 -- the lowest of the supporting entries in this directory, and deliberately so. The idea is the
right one and the authors are serious, but this is a theoretical review, the transfer chain runs from
simulated agents through clinical syndromes to REE's control architecture, and the polarity of the
modelled lesion does not match MECH-003's stated violation without an interpolating argument nobody
has yet written down.
