# Perdomo, Zrnic, Mendler-Dunner & Hardt (2020) -- the formal half of responsibility flow

## Why this paper, for a connectome-tagged claim

ARC-015 carries a note from the 2026-08-25 epistemic-function cross-reference: the self-impact
attribution and responsibility-flow machinery bundled under this claim serves an *epistemic*
function alongside the ethical and agency one, preventing self-caused, action-solicited evidence
from being naively counted as independent confirmation of the prior that produced the committing
action. The sensorimotor literature (the Frith and Voss entries in this directory) covers the
attribution machinery. It does not formalise the epistemic hazard. This paper does.

## What the paper says

When predictions support decisions, they can influence the outcome they are trying to predict. The
authors call such predictions performative. Their first observation is diagnostic rather than
technical, and it is the one I find most useful: when performativity is ignored, it *surfaces as
distribution shift* -- and distribution shift is routinely addressed by retraining. So a structural
error about the agent's own causal role presents to the practitioner as a data problem, and gets
treated with more data.

The framework then defines performative stability: predictions calibrated not against past
outcomes, but against the future outcomes that manifest from acting on the prediction. The main
results are necessary and sufficient conditions for repeated retraining to converge to a
performatively stable point of nearly minimal loss. Outside those conditions, retraining on
self-influenced data need not converge at all. The setting strictly subsumes strategic
classification.

## The mapping to ARC-015

The phrase "calibrated not against past outcomes but against the outcomes that manifest from acting
on the prediction" is, I think, the cleanest available statement of what responsibility flow is
*for* in REE. An agent that commits an action, observes the consequence, and updates as though the
consequence were an independent draw from the world is not merely being epistemically impolite --
its updating is ill-posed. The prior produced the action; the action produced the evidence; the
evidence then confirms the prior. Without an explicit representation of the agent's own causal
contribution, there is no way to discount that loop, because from inside the system the
self-induced distribution and the world's distribution are the same distribution.

This is what elevates ARC-015 above a design preference. If self-impact is unrepresented, the
failure is not a bias to be corrected downstream; it is a missing term in the problem statement.
And the paper's diagnostic observation makes the failure hard to notice in practice: it will look
like drift, and drift invites retraining, and retraining is exactly the response that does not
help.

## Where I am careful

This is a theory of supervised risk minimisation under a distribution map. It is not a theory of
agent self-attribution, and I should not let the elegance of the fit obscure that. What it
establishes is that the *problem* ARC-015 names is real, structural, and not fixable by more data.
What it does not establish is that an explicit attribution mechanism of the kind ARC-015 posits is
the required solution -- performative stability is, in the framework, reachable by procedures that
never represent self-impact explicitly at all. So this supports the necessity of the *function*
more strongly than the necessity of the *mechanism*, and ARC-015 asserts both.

There is also an unverified assumption in the transfer: that E3's action-solicited evidence has the
distribution-map structure the framework requires. That seems plausible for a committing selector
acting into an environment it partially determines, but it has not been checked, and if the
dependence is not of that form the convergence results do not apply.

## Confidence

0.72. Strong, well-known source and a very close conceptual mapping to the epistemic reading in
ARC-015's notes; capped by the gap between "the problem is real" and "this mechanism is required",
which is the gap ARC-015 still has to close on its own.
