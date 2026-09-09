# Haber, Fudge & McFarland (2000), "Striatonigrostriatal pathways in primates form an ascending spiral from the shell to the dorsolateral striatum"

**Claim tested:** MECH-004 (control-plane signal-to-knob wiring map)
**Direction:** mixed | **Confidence:** 0.68

## What the paper did

This is a tract-tracing study in macaques, and its subject is a question that the parallel-loops
orthodoxy of the 1980s had appeared to settle: are the limbic, associative and motor
cortico-basal ganglia circuits closed and separate? Haber and colleagues injected retrograde and
anterograde tracers across the striatum and reconstructed the striato-nigro-striatal
connectivity. What they found is that each striatal region does reciprocate with the dopamine
cells that innervate it -- so far, parallel loops -- but that it *also* projects to dopamine
cells lying just ventral to that reciprocal zone, and those cells innervate a striatal territory
lying more dorsolaterally. Iterate that step and the loops stop being parallel. They become a
spiral: the shell influences the core, the core influences the central striatum, the central
striatum influences the dorsolateral striatum. The authors offer it as "an anatomical basis for
the limbic/cognitive/motor interface via the ventral midbrain" -- a route by which motivation
reaches habit.

## What it says about MECH-004

The map's loop-vector section states that "implementation should treat loop precision as a
vector, not a scalar", naming P_value ~ DA_L, P_cognitive ~ DA_A, P_motor ~ DA_M, and it gives
the reason: to keep failure regimes interpretable, "for example, high value lock-in with low
cognitive stability", rather than collapsing to one confidence number. Haber et al. bear on this
in two opposite directions, which is why I have scored it mixed rather than picking one.

Supporting: the tripartition is real and it is the right one. These are anatomically
distinguishable territories with their own dopaminergic innervation, and the limbic /
associative / motor ordering is not an arbitrary carve-up imported for convenience -- it is what
the primate striatum looks like. If the map is going to have three loop axes, these are the
three.

Weakening: the word "vector" is doing work the anatomy will not support. A vector's components
are independent by construction; you can set each without disturbing the others. The spiral says
these three are a *directed cascade*. Limbic valuation state does not sit beside cognitive and
motor precision -- it feeds into them, with a specific ventral-to-dorsal sense and, importantly,
much less influence in the reverse direction. A control plane that exposes DA_L, DA_A and DA_M
as three orthogonal settable scalars is not implementing what the anatomy does, and it permits
configurations the biology has no path to reach.

The sharpest consequence is for monitoring rather than for representation. INV-022 lists its
failure signature as "single-scalar collapse / collinearity". But on this anatomy, *structured,
directed collinearity between the loop axes is what correct operation looks like* -- the loops
are supposed to be correlated, in a particular direction, because they are wired in series. A
detector that flags loop-axis correlation as a non-collapse violation will therefore fire on
healthy behaviour, and MECH-004 as written gives no way to distinguish the pathological collapse
it is worried about from the designed coupling it has inherited. That seems to me the most
actionable thing in this entry.

## Limitations and caveats

Two transfer risks compound, and they should be stated plainly rather than netted off.

First, this is connectivity, not function. Tracers establish what projects where. The
functional claim -- that limbic state actually modulates associative and then motor precision in
a behaving animal -- is an inference from wiring, and a reasonable one, but not a measurement.

Second, and more awkward: MECH-004 explicitly disclaims anatomical commitment. Its scope line
reads "Functional wiring (computational roles), not anatomical claims", and it says anatomical
mappings "are intentionally not asserted here". A purely anatomical result can then only reach
it by analogy. Someone could argue in good faith that the disclaimer immunises the map against
this paper entirely. I do not think that argument survives contact with the map's own text,
which borrows the DA_L / DA_A / DA_M vocabulary directly from this literature -- having taken
the partition, it seems to me it inherits the coupling that came attached to it. But the reading
is contestable, and the mixed score partly reflects that the entry's relevance is itself a
judgement call rather than a fact.

## Confidence reasoning

0.68. Source quality 0.88: a foundational primate anatomy paper, extensively replicated, whose
spiral organisation is now standard. Mapping fidelity 0.65 -- the tripartition maps exactly onto
the map's three loop axes, but what an anatomical result constrains in a self-declared
functional-only claim is genuinely arguable. Transfer risk 0.45 is the highest in this pull, and
deservedly: a macaque tracing study reaches an artificial control plane only through an analogy
the map itself invites, and connectivity does not entail information flow.
