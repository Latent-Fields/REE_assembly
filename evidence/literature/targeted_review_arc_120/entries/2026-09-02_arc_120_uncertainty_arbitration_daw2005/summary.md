# Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control

Daw, Niv & Dayan (2005), *Nature Neuroscience* 8(12):1704-1711. PMID 16286932. doi:10.1038/nn1560.

## What the paper did

This is a normative treatment, not an experiment. Daw and colleagues take as given the well-replicated dissociation between a prefrontal, model-based ("goal-directed") controller and a dorsolateral-striatal, model-free ("habitual") controller, and then ask the question that dissociation forces but rarely gets asked: given that both systems are present and both compute a complete answer on every trial, what decides which one moves the animal? They identify the underlying trade-off as computational simplicity against statistically efficient use of experience, and propose that arbitration follows a Bayesian principle -- each controller carries an estimate of the uncertainty in its own value predictions, and control goes to whichever is currently less uncertain, so that "each controller is deployed when it should be most accurate." They then show this single principle reproduces a wide range of existing findings about when behaviour looks goal-directed and when it looks habitual (overtraining, devaluation insensitivity, lesion dissociations).

## Why this bears on ARC-120

ARC-120 asserts that behavioural and write authority in REE is *earned* through demonstrated competence and never granted merely because a computation exists. Daw et al. is the cleanest statement I know of that same move in the biological literature, and it is worth being precise about the correspondence. Two controllers exist. Both are always computing. Neither is silenced. What is withheld is not the computation but the *authority over behaviour*, and the thing that grants it is a running estimate of the controller's own accuracy. That is ARC-120's "competence -> authority" arrow with the arbitration variable named explicitly.

The paper also makes a point ARC-120 does not, and which I think strengthens the claim rather than complicating it: a surfeit of control is *itself* a problem. Having two competent-enough systems creates a second-order choice problem that the architecture must solve, and solving it by default (a fixed blend, or a hardwired priority) throws away the very flexibility that motivated having two systems. That is an argument for competence-gating from the design side, independent of the developmental story.

## Limits of the mapping

Two things this does not do. First, the paper arbitrates over *action selection*, per trial. ARC-120's scope is broader -- it explicitly covers write authority (memory consolidation, commitment) as well as behavioural influence -- and nothing here speaks to whether the same principle governs what gets written to memory. Second, and more importantly, ARC-120's uncertainty here is a *momentary* quantity: how confident is this controller right now? ARC-120's "competence" is a *developmental* achievement, something a mechanism accrues over its lifetime and then keeps. These are related but not the same, and reading Daw et al. as direct evidence for the developmental sequence would overreach. It is direct evidence for the arbitration principle at the heart of that sequence.

Third, and this is a general limit on any literature pull for this claim: ARC-120 has two halves. The first (authority tracks competence) is a general architectural assertion that outside literature can bear on. The second -- that REE's four existing gates (ARC-107 per-event eligibility, SD-032b map stability, MECH-261 mode gating, MECH-094 real-vs-simulated tagging) are *instances of one principle* rather than four unrelated ad hoc gates -- is an internal claim about REE's own architecture. No paper can settle it. What external evidence can do is make the general principle credible enough that the unification is not merely a post-hoc tidy-up, and this paper does that.

## Confidence

0.74. Source quality is as high as it gets for a theory paper: canonical, cited into the thousands, with the arbitration idea subsequently given direct neural evidence (see the Lee et al. 2014 entry in this directory). Mapping fidelity is the binding constraint at 0.70 -- for an architectural claim I weight mapping heavily, and the momentary-uncertainty / developmental-competence gap is real. Transfer risk 0.30: the principle is stated normatively and is domain-general, which lowers the risk of an invalid transfer to a computational substrate, but the specific arbitration variable is narrower than what ARC-120 needs.
