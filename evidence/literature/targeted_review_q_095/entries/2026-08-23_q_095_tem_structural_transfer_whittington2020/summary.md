# The Tolman-Eichenbaum Machine (Whittington et al., 2020)

**Claim tested:** Q-095 — does explicit coordinated episodic organisation add capability
beyond REE's existing trajectory-generation account, or is it a re-description?
**Direction: mixed**, confidence 0.74. This is the entry that most changes the shape of the
question rather than moving it toward one horn.

## What the paper did

TEM proposes that the hippocampal–entorhinal system runs on two ideas rather than a catalogue
of separate mechanisms. Medial entorhinal cells carry a *factorised* basis describing
structural knowledge — the relational form of an environment, abstracted away from what is
actually in it. Hippocampal cells bind that structural basis *conjunctively* to sensory
representations. The authors build a model on exactly those two commitments, train it on
sequential sensory prediction, and then look at what the units do.

What they do is a great deal of the hippocampal formation's zoo: grid, band, border and
object-vector cells appear in the entorhinal layer; place and landmark cells appear in the
hippocampal layer and remap between environments. The model also matches recordings from
complex *non-spatial* relational tasks, which is the point at which "spatial map" stops being
an adequate description. And it makes a novel prediction that the authors then confirm in
simultaneously recorded place and grid cells: remapping is not random. Structural knowledge
is preserved across the remap.

## Why this is mixed rather than supporting

It supports Q-095's ADDS-CAPABILITY horn at the level of description. A single coordinated
principle really does unify phenomena that REE currently carries as separate registered
mechanisms — MECH-154's addressable manifold, MECH-242's completion, MECH-074d's remapping
each show up here as facets of one thing rather than as five things that happen to co-occur.
That is the move Q-095 asks about, made by a serious paper, and it works.

It also earns a capability rather than asserting one, which matters given how easily this
question degenerates into scoring internal statistics. Structural transfer across remapping
is a *use* of the representation: knowledge survives a context change and is reusable. That
is the right currency — the same currency MECH-495's 2x2 specifies, downstream generalisation
rather than overlap or occupancy numbers.

But it weakens the same framing at the level of mechanism, and this is the part that would be
convenient to omit. TEM is trained on sensory prediction over trajectories. Nobody installed
an episodic organising principle; the organisation is what the prediction objective produces
once you give it a factorised structural code and a conjunctive binding operation. Read
alongside Stachenfeld et al. (2017) in this same directory, the pattern is consistent:
prediction objectives generate a lot of hippocampal-looking structure without being told to.

## The reformulation this suggests

The productive move is to notice that TEM's principle is *two* things, not six. Not
binding + segmentation + separation + completion + indexing + remapping treated as one
bundle, but: (i) factorise structure from sensory content, (ii) bind them conjunctively. The
rest follows.

So the sharper version of Q-095 may not be "does episodic organisation add capability over
trajectory generation" but rather "does REE's trajectory-generation account already contain a
factorised structural code and a conjunctive binding operation — and if it does not, is that
the entire missing piece?" That reformulation is worth carrying into whatever eventually
tests this, because it is cheaper to answer and it dissolves most of the six-way bundle into
two commitments that can be ablated independently.

## Limitations and mapping caveat

The gap to be honest about is representation versus behaviour. TEM's generalisation is
generalisation *of representation* across environments, confirmed against electrophysiology.
Q-095's `what_would_answer` asks for downstream generalisation and discrimination scored
behaviourally. Representational transfer is necessary for the behavioural claim but does not
establish it, and treating TEM's success as evidence that an REE-side coordinated principle
will improve task performance would be an unearned step. `mapping_fidelity` sits at 0.70 to
record that gap.

The failure signature worth carrying forward: remapping should *preserve* structural
relations. If an REE context switch scrambles relational structure, that is not a neutral
implementation choice — it is behaving unlike the biology this whole line of argument appeals
to.
