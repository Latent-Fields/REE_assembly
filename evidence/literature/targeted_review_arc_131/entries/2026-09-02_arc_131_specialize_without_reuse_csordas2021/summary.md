# Csordas, van Steenkiste & Schmidhuber (2021) -- networks specialize but do not reuse

**Claim tested:** ARC-131 (installability is a competence dissociable from isolated component-level validation)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

The authors built a measurement instrument for a question that had previously only been answered by
inspection: given a trained network, which weights are actually responsible for a given function?
They learn a binary mask over the weights, optimised so that the masked subnetwork performs the
target function -- yielding, for each function, an identified subnet. With that instrument they ask
two separable questions of several standard architectures across arithmetic tasks, SCAN, CFQ and the
Mathematics dataset. Does the network *specialize* (do distinct functions map to distinguishable
subnets)? And does it *reuse* (when the same underlying operation recurs, does the same subnet get
used)?

The answers came apart. Specialization holds; reuse does not. In their words, "many typical NNs
exhibit Pspecialize but not Preuse", and "common NNs fail to reuse submodules". Two details sharpen
this. Measured weight sharing between modules "does not reflect task similarity (as desired) but can
mostly be explained by rather trivial shared I/O interfaces" -- so overlap metrics score sharing that
is not functional. And on systematic generalization, "combination-specific weights are learned to
deal with certain command combinations, even when they are governed by the same rules"; the hard
split "depend[s] on exclusive weights, despite those being governed by the same underlying rules".
Reuse fails, they note, "even in this simple case".

## Why it bears on ARC-131

This is the strongest ML-side entry in this directory, and it is worth being precise about why. The
other computational entry here (Shazeer et al. 2017) documents non-recruitment as an obstacle it had
to engineer around. This paper *measures* the dissociation directly, inside a single trained system,
with two different probes: the mask says the competent subnet is present, and the network's
behaviour on cases that subnet covers says it is not being used. That is exactly the two-probe
structure ARC-131 implies is necessary. A component-level PASS establishes that an operation is
possible; a second, distinct measurement is required to establish that the composed system enters
the states where the operation runs. Csordas et al. show that the first probe reads positive while
the second reads negative, in ordinary networks, on ordinary tasks.

The I/O-interface finding is the one I would carry into REE's own audit practice most urgently. If
functional sharing cannot be inferred from parameter overlap, then by the same logic mechanism
engagement in REE cannot be inferred from a mechanism being wired in, configured, or present in the
call graph. Something must show it *running under conditions where its own claim assigns it a role*.
This is the diagnosis ARC-131 already records for the inert coalition controller -- present, typed,
never endogenously invoked -- generalised into a measurement principle.

## Limitations and caveats

The modules here emerge from end-to-end training on the composed task. They were not independently
validated and then installed, which is ARC-131's motivating case. So the transferable finding is the
weaker but still substantial one: module-existence and module-engagement dissociate and need
separate measurement. It is not evidence that REE's particular installation path will fail the same
way.

There is also a half of this paper that constrains ARC-131 rather than supporting it, and it should
be stated rather than quietly dropped: specialization *does* emerge, reliably, across architectures.
Composition is not a solvent that dissolves structure. What it fails to do is recruit structure
appropriately. Anyone reading ARC-131 as licence to expect that composed systems generically destroy
their components' competences is reading past this result.

Finally the setting: supervised algorithmic benchmarks, no closed action loop, no competing drives,
no resource or mode occupancy. Three of ARC-131's seven operating-condition channels have no
analogue at all here.

## Confidence reasoning

Source quality 0.80 -- peer-reviewed at ICLR, a genuinely novel and carefully validated instrument,
code released, and results consistent across several architectures and datasets. Mapping fidelity
0.75, the highest in this pull, because the paper's central distinction is close to isomorphic with
ARC-131's. Transfer risk 0.35, low for an ML source, because the construct being transferred (a
component exists but is not engaged in composition) is architecture-independent even though the
benchmarks are far from REE's setting. Aggregate 0.72, held below 0.8 by the training-time versus
installation-time mismatch, which is a real gap and not a formality.
