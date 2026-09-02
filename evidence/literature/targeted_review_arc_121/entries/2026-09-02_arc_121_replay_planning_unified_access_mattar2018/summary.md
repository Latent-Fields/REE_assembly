# Prioritized memory access explains planning and hippocampal replay

Mattar & Daw (2018, *Nature Neuroscience*) ask a deceptively small question -- which memories should an
agent access, and in what order, while deliberating -- and derive a normative answer: access memories
in descending order of the utility of accessing them, where utility factors into *gain* (how much the
policy would improve if this memory were backed up now) and *need* (how likely the agent is to occupy
that state in future). They then use non-local hippocampal replay as an observable window onto memory
access and show that this single prioritisation rule reproduces a long list of otherwise unrelated
place-cell findings: forward replay at choice points, reverse replay after reward, the reward and
novelty modulation of replay content, and replay of remote locations.

The finding that matters for ARC-121 is not the fit to place-cell data. It is the paper's own
statement of what the fit buys: the theory "unifies seemingly disparate proposed functions of replay
including planning, learning, and consolidation." Those three had accumulated separate literatures and
separate proposed mechanisms. What the paper shows is that they are not three functions at all -- they
are one operation, prioritised access to a common value-and-model representation, running under
different weightings of gain against need. Planning is the need-dominated regime; learning and
consolidation are the gain-dominated ones. This is ARC-121's thesis restricted to three of the
consumers it names, and it is the closest thing in this pull to a direct instance of the pattern the
claim asserts.

The translation into REE is correspondingly direct. If replay, planning and learning were built as
three mechanisms with private state, REE would be reproducing exactly the decomposition this paper
argues biology does not use. The alternative it licenses is the ARC-121 arrangement: one shared
epistemic-state object, and mechanisms that differ in the access regime they impose on it rather than
in what they operate on. That is a design recommendation with a real biological warrant behind it,
which is more than a framing claim usually gets.

Two limits keep this below the top confidence band, and both are worth stating plainly. The first is
scope: the shared object here is a value function plus a transition model over a small spatial MDP. It
is not knowledge, uncertainty, possibility and commitment bound together, which is what ARC-121
asserts converges. Most conspicuously, this paper says nothing whatever about harm or ethics
evaluation -- one of ARC-121's named consumers -- and neither does any other entry in this pull. That
gap is real and should not be papered over by the strength of the rest. The second limit is a
logical one. A single normative rule that explains several phenomena is compatible with those
phenomena being implemented by separate mechanisms that each happen to approximate the same optimum.
Behavioural and statistical fit of this kind is evidence that one *description* covers all three
functions; it is not a demonstration that one physical representation is read by all three. ARC-121
asserts the latter.

Confidence 0.78, weighted toward mapping fidelity because ARC-121 is architectural rather than
empirical. Source quality is high -- *Nature Neuroscience*, and the theory reproduces a broad body of
independently collected findings rather than one dataset. Transfer risk is set at 0.35 rather than
lower: the step from a spatial value structure to a general epistemic relationship is a genuine leap,
and it is REE's inference, not the authors'.
