# Hasselmo, Bodelon & Wyble (2002) -- separate theta phases for encoding and retrieval

## What the paper did

This is a computational model of hippocampal CA3/CA1 circuitry in which the theta rhythm is not treated as
an epiphenomenon of the circuit but as a functional scheduler. Within each 100-300 ms cycle, the relative
strength of two input streams is modulated in antiphase: entorhinal afferents onto CA3 and CA1 are strong at
one phase, and CA3 recurrent input onto CA1 is strong at the opposite phase. The first condition favours
encoding, the second favours retrieval. A third element, and the one I find most interesting, is a
requirement on plasticity rather than on transmission: long-term potentiation at CA3 synapses must be
strongest at the phase where transmission through those synapses is weakest.

The task on which the payoff is demonstrated is reversal of prior learning -- the case where the network must
acquire an association that directly contradicts one it already holds.

## Why the choice of task matters

It would have been easy to demonstrate that phase separation helps in general and leave it there. Choosing
reversal is a sharper move, because reversal is precisely the case where encoding and retrieval are in
direct conflict over the same synapses. The old association is what retrieval will produce; the new one is
what encoding must write. If both run at once, the network encodes its own retrievals, and the old
association is continuously re-inscribed by the very process meant to overwrite it. That is proactive
interference, and it is a failure of independence, not of capacity.

This is what makes the paper a necessity argument rather than a correlation, and it is why I think it is the
right foundational entry for MECH-049. The claim REE is making is not that separation is tidy. It is that
without separation, one process silently modifies the substrate another process is reading, and the
modification is invisible from inside either process.

## How it translates to REE

MECH-049 worries about a specific failure: ethical constraint being "smoothed into optimisation gradients"
so that harm evaluation stops being a boundary and becomes just another term in the objective. Read through
this paper, that failure has the same shape as proactive interference. An evaluation stage that is supposed
to READ a proposal instead MODIFIES the parameters that generate proposals; over enough cycles the
constraint is absorbed into the generator, and the system now proposes only things it would have approved,
which looks like alignment and is actually the constraint having disappeared into the policy.

The anti-phase plasticity requirement is the part I would carry directly into REE design. The paper's rule
is not merely "do these things at different times" but "do not let a pathway learn at the moment it is most
influential." Translated: the phase in which harm evaluation most strongly shapes selection should be the
phase in which it is least able to write to the selector. That is a more specific and more testable design
constraint than MECH-049 currently states, and MECH-049 would be stronger for absorbing it.

## Limitations, and where the mapping strains

Two caveats, and the first is the serious one.

The separation demonstrated here is between two memory operations that interfere for a concrete, local
reason -- they are read and write on the same synaptic matrix. Proposal and harm evaluation in REE need not
share a matrix. If they do not, then the necessity argument does not transfer: temporal separation becomes a
redundant safeguard rather than the thing that makes independence possible. I do not think this sinks the
mapping, but it does mean MECH-049 owes an account of WHICH shared resource makes its stages interfere. If
the answer is "none", the claim is weaker than it reads; if the answer is "the precision/gradient pathway
that updates the selector", then this paper is almost exactly on point and the claim should say so.

Second, the separation in the model is sinusoidal and graded, not a hard gate. Encoding drive is never zero
during the retrieval phase, merely weaker. MECH-049 asks for EXPLICIT separation, and a graded modulation is
not that. If REE takes this paper as a licence for graded phase separation, it gets a harm evaluator that is
attenuated during proposal rather than absent -- which is the smoothing the claim exists to forbid. The
paper supports the claim; it does not license the weaker version of the claim.

## Confidence

0.72, direction supports. The form of the argument is right, the necessity framing is right, and the
plasticity/transmission antiphase rule is a genuine contribution to how MECH-049 should be specified. It is
held below 0.8 because it is a simulation whose central physiological prediction was untested at the time,
and because the operations it separates are not the operations MECH-049 separates. The ethical-constraint
limb of the claim gets no evidence from this paper at all -- for that, see the Alshiekh and Stooke entries
in this directory.
