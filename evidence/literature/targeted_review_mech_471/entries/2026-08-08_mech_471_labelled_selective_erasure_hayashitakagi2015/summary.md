# Hayashi-Takagi et al. (2015) — Labelling and optical erasure of synaptic memory traces in the motor cortex

**Nature 525(7569):333-8 · [10.1038/nature15257](https://doi.org/10.1038/nature15257) · retrieved via PubMed (PMID 26352471, PMC4634641)**
**Claim tested: MECH-471 · direction: supports · confidence: 0.72**

## What the paper did

The authors built a synaptic optoprobe — AS-PaRac1, activated-synapse-targeting photoactivatable Rac1 — with two properties that happen to be exactly the two operations MECH-471 says the competence path lacks. First, it *labels* recently potentiated dendritic spines specifically, so you can look at a piece of motor cortex and see which synapses a particular recent learning episode wrote to. Second, it *induces the selective shrinkage* of the spines carrying that label, so you can undo those particular changes and leave the rest alone.

Applied to motor learning in mice, in vivo imaging showed that a motor learning task induced substantial synaptic remodelling in a small subset of neurons. Optically shrinking the potentiated spines disrupted the acquired motor learning. And — this is the part that matters most — the identical manipulation applied to spines evoked by a *distinct* motor task in the same cortical region did **not** affect the first learning. Their conclusion is that a newly acquired motor skill depends on the formation of a task-specific dense synaptic ensemble.

## Why this speaks to MECH-471

MECH-471 observes an asymmetry: the memory-consolidation path has bounded, attributable, provenance-carrying, rollback-capable editing registered for it (MECH-392, INV-080, MECH-401), and the behavioural-competence path has nothing equivalent. The obvious sceptical response to that observation is that the asymmetry might be principled rather than accidental — that competence, being distributed and procedural, simply is not the kind of thing you can attribute or revert, and the consolidation path has the discipline because it is the only path that can.

This paper is the best available answer to that sceptic. It shows, in a behavioural competence, that (a) a learning episode's write is *addressable* — you can tag which synapses it produced, which is provenance in the only sense that matters operationally; (b) that write is *revertible* — shrinking those spines removes the competence; and (c) the revert is *specific* — a different task's ensemble is untouched. That third point is not a bonus, it is the precondition for the other two being useful. A rollback operation without specificity would itself be a catastrophic-interference event, which is to say a cure identical to the disease.

Read alongside the Cichon & Gan entry in this directory, the picture is that competence storage in cortex is narrow, addressable and separable — the substrate properties a bounded/provenanced/rollback-capable discipline would need. The asymmetry MECH-471 names looks like a gap in what has been *registered*, not a reflection of what a competence substrate can support.

## Limitations — and the one that decides the confidence

The decisive caveat, and I do not want it buried: **the labelling and the erasure are both exogenous**. AS-PaRac1 is an engineered probe delivered by the experimenter, and the shrinkage is driven by light the experimenter shines. Nothing in this paper shows that the brain maintains its own provenance record over competence writes, or that it can revert one endogenously.

So the honest reading is an *affordance* claim: a competence update leaves a spatially addressable, tagged trace that **can** be selectively reverted. It is not the claim that biological competence learning **is** provenanced and rollback-capable. For REE's purposes the affordance reading is the one that does work — REE would be *building* this discipline, not discovering it, and what it needs to know is whether the operations are coherent over a competence substrate at all. But a governance reading that cited this as evidence the property exists in nature would be overclaiming, and I would push back on that in a promotion discussion.

A second caveat, which I think is under-appreciated. The competences here are rotarod and a second forelimb task — narrow, highly proceduralised, and plausibly the most spatially concentrated competences the mammalian brain stores. MECH-471 is explicit that a "skill" in REE is not a document and not a module: it is distributed across action objects, learned affordances, predictive models, hippocampal trajectories, goal-conditioned policies, rule-state persistence, control settings, and residue-shaped avoidance/repair tendencies. The clean addressability that makes optical erasure work here may simply not survive that degree of distribution. If REE builds provenance for competence updates, the hard part will very likely be that the "ensemble" spans representational kinds that have no common address space — a problem this preparation never has to face.

## Confidence reasoning

Source quality 0.90 — Nature, novel causal tooling, with the specificity control that makes the result interpretable rather than merely striking. Mapping fidelity 0.68, and it is the binding constraint: held deliberately below 0.7 by the exogenous-tooling caveat, because the difference between "the substrate admits this operation" and "the system performs this operation" is exactly the difference between a design argument and an empirical one. Had the paper demonstrated an endogenous labelling-and-reversion process it would sit near 0.85. Transfer risk 0.40 — higher than the Cichon & Gan entry, because what is being transferred is an experimental capability rather than a mechanism, and capability transfers depend on REE's substrate having an addressing scheme it does not obviously have. Aggregate 0.72.
