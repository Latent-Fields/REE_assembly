# Biological organisation as closure of constraints (Montevil & Mossio, 2015) -- ARC-112

## What the paper did

This is the reference statement of the organisational-closure position. Montevil and Mossio
separate two causal regimes: *processes*, which are changes under non-equilibrium open
thermodynamic conditions, and *constraints*, which act on processes while themselves being
conserved -- exhibiting a symmetry -- at the relevant timescale. Biological organisation, they
argue, is what you get when a set of constraints depends on itself: each constraint is maintained
by others in the set and contributes to maintaining others in turn.

The definition is given precisely, and this is the part worth having. A set C of constraints
realises **overall closure** if, for each Ci in C:

1. Ci depends directly on at least one other constraint in C (Ci is *dependent*)
2. There is at least one Cj in C which depends on Ci (Ci is *generative*)

and C realises **strict closure** if it additionally satisfies

3. C cannot be split into two closed sets.

They are explicit about why condition 3 exists: it is "aimed at ensuring that the definition
applies only to one system (rather than two independent systems)".

They then propose, more tentatively, a graded version. Choose a volume of space V, let K(V) count
the closure-subject dependencies inside it, grow V, and watch dK(V,l) -- which should peak inside
an organism and collapse at its boundary, rising again as the volume reaches the next one. This
"tendency to closure" is offered as a measure of organisational integration and a tool for drawing
boundaries between mutually dependent organisms.

## The question this entry was asked to answer

The brief was specific: constraint closure gives a structural criterion for when a set of
processes constitutes one system, which is exactly ARC-112's assertion -- but check whether it
yields anything measurable or only a definition, and if it is purely definitional, say so and
score it accordingly rather than padding the pull.

The answer is that it splits cleanly in two, and the split is more interesting than either
verdict alone.

**The structural criterion is real, computable, and unusually well matched to ARC-112.** Condition
3 is the closest external formalisation of ARC-112's claim I have found in this cluster --
closer than Tognoli and Kelso, whose metastability framing is evocative but oscillator-bound.
ARC-112 says REE is neither a monolith nor a collection of independent modules. Strict closure
formalises the second disjunct exactly: a constraint set that cannot be partitioned into two
independently closed sets is one system, and one that can is two systems sharing a repository.

And it is checkable on REE today, with no experiment and no telemetry. Enumerate the architectural
constraints -- the scheduler's rate assignment, boundary broadcast, mode conditioning, the beta
commitment gate, residue feedback, harm-stream separation, hippocampal proposal routing -- draw
the direct-dependency edges among them, and evaluate conditions 1-3. Two diagnostics fall out
immediately. A constraint that is *dependent but not generative* is a consumer bolted onto the
federation rather than a member of it, which is precisely the sharpening MECH-466 proposes for the
boundary stream ("not merely a detector with a consumer"). And any bipartition of the graph into
two closed sets is a specific location where ARC-112 is locally false. That gives ARC-112
something to do that is not gated behind the Q-081 telemetry audit, which every other item in
cluster A is waiting on.

**The quantitative part does not transfer, and I do not think it can be made to.** dK(V,l) is
built out of physical space: grow a volume, count the dependencies enclosed, find the boundary
where the count collapses. REE has no spatial embedding, and there is no non-arbitrary substitute
for the volume-growth ordering -- any ordering one invents over REE's modules would determine the
answer. The authors are candid about the state of it, calling the treatment "still preliminary"
and footnoting that their notion of organised complexity is "adopted for the specific purposes of
this discussion". So the graded closure measure is a research direction in their own field, not a
tool.

The consequence for our cluster is worth stating plainly: **constraint closure serves ARC-112 and
does nothing for INV-091.** Strict closure is Boolean, and INV-091 is a claim about a band. A
criterion with no notion of degree in the dimension INV-091 cares about cannot detect
fragmentation-versus-collapse, and it would return the same verdict for a federation richly
integrated and one held together by a single trivial wire. That is a limit of the thread, and the
right response is to route INV-091's measurement need to the information-decomposition entries in
this directory rather than to stretch this one.

## Caveats

The transfer is not the usual GOV-ANALOGY-1 case -- this is theoretical biology, not a brain
result being read across -- but it is still a transfer, and a real one. The constraint/process
distinction is grounded in non-equilibrium thermodynamics and in constraints being conserved at a
timescale; neither has an obvious REE counterpart, so reading REE's architectural mechanisms as
"constraints" is an interpretation. More sharply: the graph the criterion runs on has to be built
by hand, and which mechanisms count as constraints and which dependencies count as direct are
analyst decisions that fix the verdict before any computation. This is not a measurement.

There is also a live objection in the literature -- Garson's liberality objection, that closure of
constraints is satisfied by simple systems nobody would call unified organisms. If the criterion
admits a thermostat loop, a REE constraint graph passing strict closure is weak evidence that REE
is a federation in any sense worth asserting.

## Confidence reasoning

0.50, and it is a genuine average of two components rather than uniform mediocrity: the
strict-closure condition maps onto ARC-112 at something like 0.8, the tendency-to-closure measure
at something like 0.2. Source quality is good but the paper is conceptual, dataless, and has an
unresolved objection standing against it.

Direction is `mixed` rather than `supports` because what the paper supplies is a *test* ARC-112
can be put to, with no indication of which way the test comes out, plus one thread (the graded
measure) that turned out not to transfer. Recording that second half is the point of the entry.

lit_conf only. exp_conf on ARC-112 -- and on Q-081, MECH-466 and INV-091 -- remains 0.0.
