# The Differentiable Neural Computer (Graves et al., 2016) — why IMPL-027's convergence argument is weaker than it looks

## Why this paper is in an IMPL-027 pull at all

IMPL-027 does not cite it. That is the point of including it.

The comparison document closes, in section 6, with its most rhetorically ambitious move:

> That both programmes converge on commitment boundaries, memory stratification, offline
> consolidation, and incommensurable learning channels — from entirely different starting points —
> suggests these are genuinely necessary structures, not design choices.

This is an argument from independent convergence, and arguments of that form live or die on the
independence premise. If two programmes drank from the same well, their agreement is inheritance,
not corroboration. So the question worth asking of the literature is not "is REE right about
commitment gating" — no comparison document can settle that — but "were the NC roadmap's
requirements arrived at independently of the tradition REE also draws on?" This paper is the
cleanest evidence that the answer is: less than IMPL-027 assumes.

## What the paper did

Graves and twenty co-authors introduced the *differentiable neural computer*: a neural network
coupled to an external memory matrix it can read from and write to, "analogous to the random-access
memory in a conventional computer." The controller learns, by gradient descent alone, to allocate
memory, to write records, and to follow the temporal links between them. They demonstrated it on
tasks that defeat recurrent networks without external storage — shortest-path and inference queries
over the London Underground graph and over family trees, and a block-puzzle planning task learned
by reinforcement.

The framing is what matters here. This is, explicitly and in Nature in 2016, a *neural computer*:
the project of dissolving the boundary between a learned network and an addressable machine, with
separation of computation from a persistent addressable store as its organising idea.

## The bearing on IMPL-027

Three things follow, and I want to be careful to claim only the third.

First, the vocabulary is not new. "Neural computer," addressable memory, routine reuse across
contexts, and the failure of recurrent hidden state to carry structure over long horizons were all
in play a decade before the NC roadmap. The 2026 paper's contribution is the *completeness* framing
and the I/O-trace instantiation, not the ambition.

Second, the lineage is shared, and shared in a specific way that touches REE. The DNC comes out of
DeepMind; Demis Hassabis is its last author. He is also a co-author on the complementary learning
systems paper that REE leans on for INV-049's offline/online separation. So the two "entirely
different starting points" in IMPL-027's section 6 are, at minimum, adjacent — the memory-augmented
neural computation line and the CLS line run through the same institution and partly the same people,
and REE_convergence has separately ingested the DNC as an external framework in its own right.

Third — and this is the only claim I want to make — the independence premise is *undischarged*.
I am not asserting that the NC authors derived their four requirements from the DNC. They may well
have arrived at them from systems-engineering pressure, exactly as IMPL-027 says. What I am saying
is that IMPL-027 currently offers no argument for independence, and there is a visible common
ancestor that a sceptical technical reader will reach for immediately. An argument from convergence
that does not address its most obvious defeater is doing less work than it appears to.

## What this does *not* touch

Nothing here bears on whether commitment gating, the residue field, or phase separation are correct
or necessary. The DNC is architecturally unlike both REE and NC: its memory is an explicit,
hand-specified differentiable matrix, not a learned runtime state and not a valenced viability map.
It would be a mistake — the same mistake, one level up — to read the DNC as a *third* convergent
instance and take that as strengthening the necessity argument. Three programmes in one literature
agreeing is not three independent draws.

## Confidence reasoning

0.68, direction `weakens`. Source quality is high: peer-reviewed Nature, canonical, heavily
replicated. Mapping fidelity sits at 0.65 because the paper says nothing whatever about REE or about
the NC roadmap — the bearing is inferential and assembled by me, and I would rather say so plainly
than dress it up. Transfer risk 0.40, because judgements about intellectual independence are
genuinely contestable and a reasonable reader could hold that the NC requirements are
convergently-derived after all.

The constructive version of this finding is small and cheap: section 6 does not need to be retracted,
it needs a sentence acknowledging the memory-augmented-computation precedent and saying why the
authors nevertheless take the arrival to be independent. As written, the strongest paragraph in
IMPL-027 is also its most exposed one.
