# Daw, Gershman, Seymour, Dayan & Dolan 2011 — model-based influences on choices and striatal prediction errors

**Claims:** MECH-477 (primary), MECH-163 (secondary)
**Direction:** mixed · **confidence 0.62**

## What the paper did

This is the fMRI test of the 2005 proposal that already sits in this folder at confidence 0.79. The authors built the now-canonical two-step Markov task, whose whole purpose is to make model-based and model-free influences on choice separately identifiable from the choice statistics alone. Subjects showed both influences. Having established that, the authors could ask the question they actually cared about: is the ventral striatal prediction-error signal — the workhorse model-free correlate of the previous decade — really a pure model-free report?

It is not. The striatal signal reflected both model-free *and* model-based predictions. And the proportions in which it mixed them matched the proportions that best explained each subject's choices. The authors' own reading is that this "challenges the notion of a separate model-free learner and suggests a more integrated computational architecture."

## Why I have filed this as mixed rather than supports

It would be convenient to file this as straightforward support for MECH-477, and I do not think that is honest.

The supporting half is real and specific. If the neural mixing weight tracks the behavioural mixing weight subject by subject, something is setting a common proportion, and it is setting it *gradedly* — not flipping between two regimes. That is direct evidence for the parameterisation question the pull was owed on: arbitration in humans looks like a continuous weight, and it looks like the same weight is visible at both levels of description. Together with Lee 2014's explicit P(MB), the graded-versus-discrete question now has two independent lines of evidence pointing the same way, and I would treat "build it as a discrete switch" as the option that now needs defending.

The awkward half is that this paper is the strongest thing on file against the architecture MECH-477 inherits. MECH-477 asserts that two pathways *without* an arbitrator produce a flat recruitment response — that the dynamics require a third element. Daw 2011 shows an integrated value representation in which the two influences are already mixed at the point where you would have gone looking for the pure habit signal. An integrated architecture of that kind can produce graded, context-sensitive recruitment without anything you would want to call an arbitrator. Which means the observable MECH-477's falsifier keys on — a larger novel-minus-familiar recruitment delta with the arbitrator ON — is not by itself diagnostic of an arbitrator. Something else could produce it.

This is exactly why the claim's mandatory manipulation check is load-bearing rather than ceremonial. The `what_would_answer` text already requires that the arbitration weight be shown to vary with measured uncertainty, and treats a run without that demonstration as a readiness failure that scores nothing. Daw 2011 is the reason that clause should not be relaxed if the ON arm comes back looking good. A pretty delta with a dead arbitrator is a result this literature predicts is obtainable.

## Limitations and the transfer question

I want to be careful not to over-read the negative result. BOLD in ventral striatum sums over afferents from both pathways within a voxel, so apparent computational integration is partly a resolution artefact — you cannot distinguish "one integrated learner" from "two learners whose outputs converge on tissue I am averaging over" with this measurement. That ambiguity is a property of fMRI, not of brains, and REE's substrate has no equivalent limit: the two pathways are explicitly separate objects and can be read independently.

So the specific finding may simply not transfer. That is why this is `mixed` and not `weakens`. What does transfer, and what I would keep, is the epistemic lesson: the same group that produced this result went on to localise an arbitrator (Lee 2014, filed alongside), and both things are true at once. Two pathways can be computationally more entangled than the clean box diagram suggests *and* there can still be a comparator allocating control between them.

Confidence at 0.62 reflects a methodologically strong paper (source quality 0.90) whose bearing on this particular claim is genuinely two-sided (mapping fidelity 0.55, transfer risk 0.45). Reported as `lit_conf` only, not blended with experimental confidence; MECH-477 has no `exp_conf` yet, and V3-EXQ-786a stands as the already-measured OFF arm.
