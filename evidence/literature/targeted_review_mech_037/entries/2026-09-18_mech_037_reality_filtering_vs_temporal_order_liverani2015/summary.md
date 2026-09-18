# Reality filtering versus temporal order judgment (Liverani et al. 2015)

## What the paper does

Seventeen healthy adults performed a continuous recognition task that had been built to impose two
demands inside one paradigm and one time window. One demand was orbitofrontal reality filtering:
sensing whether an evoked memory refers to present reality and may be acted upon. The other was
temporal order judgment: knowing consciously *when*, in the recent past, something happened.
High-density evoked potentials were recorded throughout. The question had never been asked this way
before, which is why the paper matters here -- the two constructs are usually studied in separate
literatures with separate tasks, and any apparent relationship between them is then an artefact of
the comparison.

The result is a dissociation on both channels. Behaviourally, subjects were markedly slower and
less accurate at ordering than at filtering. Electrophysiologically, the two evoked similar
potentials at 240-280 ms -- the window in which reality filtering normally occurs -- and then
diverged rapidly, in amplitude and in estimated electrical source, from 310 to 360 ms and again
from 530 to 560 ms, engaging different brain areas. The authors' summary is that consciously
ordering memories in the immediate past is effortful and slow, in contrast to sensing a memory's
relation to the present. They add a clinical observation that I find the most pointed part of the
paper: failure of reality filtering has a well-known clinical manifestation, and failure of
temporal order judgment, as tested here, has none.

## Why it bears on MECH-037, and why it weakens it

MECH-037's operational checklist lists the gate's input signals as "hippocampal trace presence,
temporal ordering confidence, and recency flags", and its commitment rule is that E3 commitment
requires a provenance-gate pass for E1-derived content. So the claim asserts, fairly specifically,
that a temporal-ordering read-out is one of the things the gate consults. This paper is close to
the controlled test of that assertion, and the answer it gives is negative: in humans, the fast
pre-commitment filter and the temporal-ordering read-out are different processes with different
time courses and different sources, and the early similarity between them at 240-280 ms does not
survive 50 more milliseconds.

There is also an argument from latency that I think is stronger than the source dissociation. The
gate runs at 200-300 ms. The ordering judgment is slow and effortful. A gate that had to wait on an
ordering read-out could not run at gate speed. If REE builds the provenance gate as a consumer of a
temporal-ordering estimate, it will have built the slow deliberate process -- which is a real
cognitive function, but not the one whose failure produces confabulation.

## What I would do with this

Not retire the claim, but split its input list. MECH-037 currently bundles trace presence and
temporal ordering as though they were one signal; the human data says they are two, with different
speeds and different failure consequences. The claim's own non-degeneracy precondition already
insists the trace/ordering signal must vary across conditions rather than be held constant. This
paper sharpens that into a stronger requirement: trace presence and ordering confidence have to be
varied *independently*, or a null result will be uninterpretable -- one could have been doing all
the gating work while the other was inert.

## Limitations and confidence

Seventeen subjects, one laboratory, one paradigm. ERP source localisation is a coarse spatial
inference and "different brain areas" is a weaker anatomical statement than it sounds. And there is
a genuine escape route for MECH-037 that I want to state rather than bury: the temporal ordering
this paper tests is *conscious, reportable* order knowledge. REE's "temporal ordering confidence"
could be an implicit signal that never reaches report and that this paradigm therefore never
touches. That distinction is defensible -- but it is a hypothesis that has to be paid for with an
experiment, not asserted to dissolve the finding. I have set confidence at 0.74 and direction
`weakens`: the mapping to the claim's exact mechanism question is unusually tight, which is what
makes a modest-N single-lab study consequential here.
