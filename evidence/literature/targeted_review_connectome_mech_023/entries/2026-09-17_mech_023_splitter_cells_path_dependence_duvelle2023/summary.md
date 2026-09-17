# Splitter cells: the cognitive map already refuses to be Markov

Duvelle, Grieves and van der Meer review two decades of work on what the field has come to call
*splitter cells* — hippocampal neurons that fire differently on a stretch of track the animal is
physically re-traversing, according to where it came from or where it is heading. The canonical
preparation is continuous alternation: the central stem of a T- or figure-of-eight maze is the same
stem on every lap, the animal's position, heading and running speed are matched, and yet a
substantial fraction of CA1 and CA3 cells fire at different rates depending on whether the last turn
was left or right. The review's contribution is not new data but the attempt to reconcile a
fragmented literature under two competing accounts — temporal context (the representation carries a
decaying trace of recent experience, which explains why splitting is graded with distance from the
divergence point) and latent state inference (the animal has assigned the two passes to different
hidden states, which explains why splitting is flexible and switches off when the task stops
requiring the distinction). The authors are explicit that neither account covers all the observed
properties.

The reason this matters for MECH-023 is almost embarrassingly direct. MECH-023 says that two agents
in the same state may differ because of how they arrived there, and that responsibility is therefore
path-dependent and non-Markovian. Splitter cells are the existence proof that a biological cognitive
map is built that way: matched present state, divergent representation, and the divergence traceable
to the path. If one wanted to argue that a mind's evaluation of its situation must reduce to its
current state — the FALSIFYING branch of the claim, where responsibility collapses to a Markov
property — this literature is the first obstacle. The hippocampus, the structure ARC-013 names as the
substrate for residue-as-latent-curvature, demonstrably does not encode position alone.

What the paper does *not* give us is the evaluative half. Every history that splits in these studies
is a task history — which arm was baited, which turn is required next — and none of them is a moral
history. The divergence is in the representation, not in a downstream ranking of what the animal will
commit to. MECH-023's CONFIRMING criteria require both: criterion (i) asks for rank divergence in the
E3 candidate set at a matched z_world, which is a *selector* readout, not a *map* readout. A splitter
signal could in principle be present and entirely ignored by the policy — and that is not a
hypothetical, because the review notes that splitting attenuates or disappears when the task no
longer demands it. Read carefully, this is REE's own falsifier stated in rodent terms: a residue field
can be live and still not be consulted.

The other honest caveat is that the *form* of the history dependence is unsettled. Temporal context
predicts a graded, decaying influence; latent state inference predicts something more like discrete
assignment to a hidden context. REE's residue field commits to a specific accumulation-and-decay
geometry over z_world, and this review is a warning that picking that form is a real modelling choice
with empirical consequences, not an implementation detail. If the MECH-023 experiment finds that the
A-vs-B divergence does not decay with distance from the harm event the way the residue field's kernel
assumes, that is informative about the kernel rather than about the claim.

Confidence at 0.78. Source quality is high — this is a well-regarded synthesis in eLife of a robust,
multiply-replicated phenomenon. Mapping fidelity is good but capped: the mechanism transfers, the
ethical content does not, and the representational-to-evaluative step is exactly the gap the REE
experiment is designed to close. Transfer risk is moderate rather than low, because REE's residue
field was deliberately built as a map-over-latent-space analogue of this literature, so the
correspondence is by design and not an after-the-fact resemblance.
