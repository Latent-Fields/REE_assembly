# MOSAIC model for sensorimotor learning and control

Haruno, Wolpert & Kawato (2001), *Neural Computation* 13(10):2201-2220. PMID 11570996. doi:10.1162/089976601750541778.

## What the paper did

MOSAIC (modular selection and identification for control) is an architecture built from multiple *paired* forward and inverse models. Each pair consists of a predictor -- what will happen if I issue this command in this context -- and a controller -- what command achieves my goal in this context. The pairing is the whole idea: a module's forward model is continuously scored against actual sensory feedback, and the resulting prediction accuracy becomes that module's *responsibility signal*. Responsibility does two things. It weights the module's contribution to the outgoing motor command, and it weights that module's own learning.

This 2001 paper extends and evaluates the architecture. The learning rule is derived both by gradient descent and by expectation-maximisation, with EM proving robust to initial conditions and learning parameters where gradient descent was not. Simulations of an object-manipulation task show the architecture learning to handle multiple objects, switching between them appropriately, and generalising to novel objects whose dynamics fall inside the polyhedron spanned by learned dynamics. When object shape is bound to dynamics and the model is then given a *novel* shape-dynamic pairing, it shows "inappropriate activation of modules ... followed by on-line correction."

## Why this bears on ARC-120

The other two supporting entries in this directory (Daw 2005, Lee 2014) establish that competence-gated authority is normatively right and neurally instantiated. MOSAIC establishes something different and, for an architectural commitment, arguably more useful: that it *works*, and that it can be learned end-to-end without a hand-designed gate. Nobody wrote the arbitration rule into MOSAIC. Responsibility falls out of each module's own prediction error. That matters for ARC-120's stronger reading -- that competence-gating is a general architectural principle rather than a family of ad hoc gates -- because it shows the principle admits a single uniform implementation.

MOSAIC also supplies an arrow ARC-120 does not currently state. Responsibility gates *learning* as well as control. An incompetent module is not merely denied authority over the output; it is prevented from updating on outcomes it did not cause. That is a genuinely separate protection, and it is worth asking whether REE's existing gates have it. If a module in REE is denied write authority but still updates its parameters from the resulting outcome, it accrues credit for a trajectory it did not steer, and the competence estimate that gates it becomes self-corrupting. I would flag this as the most actionable thing in this pull.

## Limits, and the failure modes worth carrying forward

This is simulation on object-manipulation dynamics -- no biological measurement, no memory-write or commitment authority, and a "competence" construct (one-step forward-model accuracy) far narrower than the developmental competence ARC-120's sequence describes. Motor control is also an unusually favourable case: reafference gives a clean, immediate, well-posed prediction error. Most of REE's authority domains do not have an equivalent, and the transfer risk is set at 0.40 for that reason rather than because the simulation is weak.

Three specific failure signatures are worth recording, because they are the kind of thing that only shows up when someone actually builds the thing. (1) The novel shape-dynamic pairing result: a competence gate keyed on a *proxy* for competence -- a context cue, a tag -- rather than on measured error will grant authority to the wrong module until reafference corrects it. (2) Generalisation held only inside the span of learned dynamics: a competence estimate has no validity outside the region over which competence was demonstrated, so a gate that extrapolates its own reliability estimate over-grants. (3) The gradient-descent/EM contrast: the competence signal is itself an estimate, and when it is badly estimated the gate fails in a way invisible from the gate's own outputs. All three are ways an architecture can honour ARC-120 in form and violate it in fact.

One honest note on direction. MOSAIC's responsibility signal is a soft weighting, not a threshold. It supports a *graded* reading of ARC-120 -- authority proportional to demonstrated competence -- more directly than an all-or-nothing gate. ARC-120 as written ("earned ... never granted merely because a computation exists") is compatible with both, but the graded reading is what this paper actually demonstrates.

## Confidence

0.72. Source quality 0.78 (well-regarded formalisation of an influential architecture; simulation-only). Mapping fidelity 0.72 -- strong for the competence->authority arrow and the learning-gating corollary, weak for the developmental-sequence and write-authority parts of the claim. Transfer risk 0.40, the highest in this pull, for the reafference-availability reason above.
