# Complementary Learning Systems, updated (Kumaran, Hassabis & McClelland, 2016) — grounding IMPL-027's best bridge, and trimming its modal language

## Which part of IMPL-027 this speaks to

Section 3 of the comparison document contains its strongest technical move, and the one least
dependent on rhetoric:

> REE derives the requirement for periodic offline phases (sleep-analog) from the fundamental
> incompatibility of model-use and model-update (INV-049). [...] NC's roadmap calls for
> "architectural separation of inference from parameter updates" — this is exactly the NC-language
> description of REE's offline/online phase separation.

That is a real correspondence, not a terminological one, and it deserves a source. IMPL-027 supplies
none — it points at claims.yaml INV-049 and leaves the argument to stand on its own. This entry
supplies the external grounding and, in doing so, shows the conclusion is well-supported while the
*modal* claim attached to it is not.

## What the paper argues

Kumaran, Hassabis and McClelland restate and update the complementary learning systems framework for
an audience that now includes people building artificial agents. Intelligent agents, they argue, need
two learning systems: a fast one that can acquire a specific experience in a single shot, and a slow
one that extracts structure gradually across many experiences. The two cannot be collapsed. Trying to
write new knowledge directly and rapidly into the slow, structured system produces catastrophic
interference — the new information overwrites the overlapping distributed representations that encode
what was already known. The resolution is interleaved replay: the fast system reinstates stored
experience, mixed with new material, so the slow system's updates are statistically well-conditioned.

The 2016 update matters for this pull because it deliberately generalises beyond biology. The paper
is addressed to agent design, and it engages the machine learning literature directly rather than
leaving the transfer to the reader.

## What this supports in IMPL-027

The architectural conclusion holds up well. A system that must simultaneously *use* a structured world
model to act and *revise* that model in light of new experience is in genuine difficulty if it tries
to do both at once — and the difficulty is not a quirk of neurons. It shows up in gradient-trained
artificial systems for the same reason. So IMPL-027 is right that the online/offline split is not a
biological detail REE imported by analogy, and right that the NC roadmap's "separation of inference
from parameter updates" is the same structural requirement stated in systems-engineering vocabulary.

This also strengthens the document's reading of the NC prototypes' failures. Catastrophic forgetting
when acquiring new capabilities is exactly the failure this literature predicts for a system with a
single learning pathway and no consolidation phase. IMPL-027 treats that failure as diagnostic, and
the diagnosis is sound.

## What it undercuts

The modal language. IMPL-027 says offline consolidation is "a general computational necessity, not a
biological contingency." The warrant available from this literature does not reach that far.

Catastrophic interference is a consequence of *overlapping distributed representations under gradient
learning*. It is a statistical fact about a class of representational scheme, not a theorem about any
system that uses and updates a model. A system with sufficiently sparse or orthogonalised
representations — or one that grows capacity rather than overwriting it — faces the problem far less
acutely. The honest form of the claim is that offline consolidation is required for a broad and
practically dominant class of systems, a class that includes both REE and the NC prototypes. That is
still a strong and useful claim. It is just not necessity.

I do not think this damages INV-049, which may well have an independent derivation I have not
examined here. What it damages is IMPL-027's *presentation* of INV-049 — asserting necessity, citing
nothing, in a document aimed at technical readers arriving from a literature where the statistical
version of this argument is common knowledge. That is an invitation to be dismissed on the one point
where the document is otherwise strongest.

## A note that connects to the rest of this pull

Demis Hassabis is a co-author here and the last author on the differentiable neural computer paper in
the sibling entry. That is not a criticism of either paper. It is directly relevant to IMPL-027
section 6's claim that the NC and REE programmes converge "from entirely different starting points":
the offline-consolidation argument REE relies on and the neural-computer lineage the NC roadmap
extends run partly through the same people. Independence is doing real work in that section and has
not been established.

## Confidence reasoning

0.70, direction `mixed`. Source quality 0.90 — canonical review by the framework's own originators,
written to address artificial agents explicitly, which is why transfer risk sits at 0.30, the lowest
in this pull: REE is not smuggling a biology result into an architecture argument unaided, because the
source itself makes the cross-domain move. Mapping fidelity 0.70 records the split: the architectural
conclusion maps cleanly, the necessity framing does not.

`mixed` rather than `supports` is a deliberate call. On the substance this paper is the best friend
IMPL-027 has in this pull. It is scored mixed because it simultaneously shows the document is
claiming more strongly than its own grounding allows, and that is information governance should see
rather than have averaged away into a supporting citation.
