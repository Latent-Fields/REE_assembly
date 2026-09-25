# Transdiagnostic anxiety-related increases in information sampling (Rapp et al., 2024)

## What the paper did

Rapp and colleagues gave a transdiagnostic adult sample -- people with anxiety disorders,
compulsive disorders, or both (n = 35) alongside healthy controls (n = 23) -- a beads task
at three evidence-strength ratios (60:40, 75:25, 90:10). They fit two computational models:
a Bayesian belief-updating model over how each bead should shift confidence in the jar
identity, and a partially-observable-Markov-decision-process model that adds a subjective
cost parameter for committing to the wrong jar. The question was whether excess sampling in
this population comes from mis-weighting the evidence itself (an inferential account) or
from over-valuing the cost of being wrong (a valuation account).

## What is relevant to MECH-080

Q2 of the MECH-080 synthesis asks where anxiety belongs now that arm 2 (extension-biased
over-withholding under uncertainty) has been re-occupied by compulsivity, on the strength of
Hauser et al. 2017a's finding that the effect there loads specifically on compulsivity and
not on affective dimensions. This paper is the most direct test of that specificity claim
available: it uses the identical information-sampling paradigm, and it finds that *trait
anxiety*, continuously measured across the same transdiagnostic sample, predicts more
draws-to-decision -- most strongly at the hardest ratio -- and that this is carried by a
lower subjective-cost threshold, not by a difference in how the evidence itself is weighted.

That is not a clean re-assignment of anxiety back to arm 2. The sample mixes anxiety and
compulsivity rather than separating them, so the paper cannot itself say whether the two
share one valuation-based mechanism or whether anxiety's contribution here is really riding
on unmeasured compulsive symptoms in the same people. What it does establish is that Hauser's
"specific to compulsivity, not affective dimensions" reading is not the only result in the
literature -- a second, independently-run paradigm finds an anxiety-linked version of the
same over-sampling phenotype. The mechanism identified (a valuation parameter: how costly an
error feels) is also a different kind of quantity than Hauser's urgency-emergence account or
a static decision threshold, which matters for Q5's design-constraint list if this arm is
ever revisited computationally.

## Limitations

Modest, mixed clinical sample (n = 58 total, not an anxiety-only arm against controls).
Valuation parameter, not a diffusion-model boundary or REE's rollout_horizon -- one further
translation step than the already-banked Hauser entries. No loss-conditional (Huys-style)
truncation is tested; this paper speaks only to the extension/over-sampling side of Q2, not
to option (b) (re-homing anxiety as an arm-1-like conditional truncation variant).

## Confidence reasoning

0.62. Source quality is good -- purpose-built computational psychiatry design, peer-reviewed,
open access -- but the transdiagnostic, modestly-powered sample means this paper complicates
Hauser's specificity finding rather than overturning it. It is evidence that the arm-2
occupant question is not fully closed, not evidence for a specific alternative assignment.
