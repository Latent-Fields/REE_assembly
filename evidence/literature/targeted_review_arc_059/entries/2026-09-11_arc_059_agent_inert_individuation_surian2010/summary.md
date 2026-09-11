# Agents are individuated before features are (Surian & Caldi, 2010)

## What the paper did

Two violation-of-expectancy experiments with 10-month-olds. Infants watched two different objects
appear and disappear one at a time from behind a screen; then the screen came away, revealing either
one object or two. If the infant has individuated the two entities during familiarisation, the
one-object outcome is the surprising one.

The manipulation is the contrast between the experiments. In Experiment 1 the pair was one
self-moving, non-rigid agent and one inert object -- a category difference, carried by motion.
In Experiment 2 the pair was two different agents -- a featural difference, carried by shape and
surface. Infants looked longer at the one-object outcome in Experiment 1, indicating they had kept
two entities in mind. In Experiment 2 they showed no preference either way. The authors conclude
that dynamic information supports agent detection in individuation tasks *before* shape or surface
features can do the same work, and that the sortals `agent` and `inert object` are available before
12 months without much help from language.

## How this bears on ARC-059

This is the sharper of the two challenges in today's pull, and it lands on the less-defended half of
the claim. ARC-059 states the stage-3 gate plainly: "without object-schemas the agent cannot
recognise other-agents as a distinguished subclass of objects." The architecture is hierarchical --
objects first, then a subclass of them marked out as agents. Surian and Caldi describe a system
that does not look hierarchical in that way. The agent/inert distinction is doing individuation work
at an age when the featural machinery that would have to underlie a general object schema is not yet
supporting the same inference. If anything, the dependency runs the other way round at 10 months.

The natural REE response is that an object-schema is not a *featural* schema, and I think that
response is legitimate rather than evasive -- stage 2 in ARC-059 is object-schema formation via
*experimental action on the world*, which is precisely the kind of learning that would encode
dynamics and affordances rather than shape and colour. On that reading, the self-motion cue infants
are using is already inside stage 2, not prior to it, and the paper stops being a counterexample.
But that response has a cost: it makes stage 2 and stage 3 harder to dissociate experimentally,
because the cue that distinguishes agents is then part of what stage 2 builds. An ablation designed
to withhold stage 2 and test stage 3 would be withholding the very representation it wants to probe.

## Limitations, and what I would not conclude

A 10-month cross-section shows what is available at 10 months, not what was acquired first. The two
experiments differ in the *kind* of difference presented, not in the infants' developmental history,
so nothing here tracks an ordering over time -- it is a dissociation in current competence being read
as evidence about construction order, which is an inference the data underdetermine. There is also
the general caveat attaching to violation-of-expectancy work: looking-time differences at these
sample sizes have not always survived replication, and a null in Experiment 2 is a weaker foundation
than a positive effect would be.

So I have recorded this as `weakens` at 0.58 rather than anything stronger. The value of the entry
is less the verdict than the design warning it carries: it identifies a specific way the stage-2 →
stage-3 ablation could come back null for reasons that have nothing to do with the ordering being
wrong -- namely that the agent cue was never actually withheld.
