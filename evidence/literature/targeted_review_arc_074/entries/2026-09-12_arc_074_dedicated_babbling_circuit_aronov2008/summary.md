# Aronov, Andalman & Fee 2008 -- babbling has its own circuit, not the adult circuit turned down

Juvenile zebra finches produce subsong, a succession of primitive and highly variable vocalisations
that is the closest avian analogue of human babbling. Aronov and colleagues asked which circuits
produce it. The answer is a clean double dissociation: subsong does *not* require HVC, the premotor
nucleus that is necessary for adult song, but it *does* require LMAN, a nucleus involved in learning
and not in adult singing. During babbling, LMAN neurons showed premotor correlations to vocal output
on a fast time scale. Juvenile singing, the authors conclude, is driven by a circuit distinct from
the one that produces the adult behaviour -- and they suggest the separation may be general to other
developing motor systems.

This is the strongest warrant I have found for ARC-074's central architectural move, and it bears on
the claim in a more specific way than "babbling is real and important". ARC-074 currently specifies
Phase 0 as a `Phase0Config` block that suppresses E3 weighting while Hebbian sensorimotor exploration
runs on the existing machinery -- Phase 1 with the reward weight set to zero, in effect. Aronov et al.
describe something architecturally different: a *separate generator*, whose output the mature pathway
later supersedes rather than inherits. If the biology is the guide, the faithful implementation is not
a suppression flag over one substrate but two substrates with a handoff. That is a considerably larger
build than the config block the claim currently proposes, and the difference is worth surfacing before
anyone implements against the claim text as written. Given the project's standing preference for
brain-like construction where feasible, this is exactly the sort of place where the cheap version and
the faithful version diverge early.

Now the limitation, which I think governance needs held clearly in view, because it is easy to read
this paper as settling more than it does. Aronov et al. establish that the babbling epoch has a
dedicated generator and that the adult circuit is not required for it. They do *not* establish that
babbling is necessary for the adult skill. The complementary experiment -- abolish the exploratory
epoch, then measure the mature song -- is not reported here. ARC-074's load-bearing assertion is a
necessity claim: that without Phase 0 the agent cold-starts E3 on a flat residue field and collapses
to monostrategy. Separateness is evidence about architecture; necessity is evidence about
consequence; this paper gives the first and not the second. The claim's own `what_would_answer`
already demands a two-arm A/B, and nothing in this entry substitutes for running it.

Transfer risk is the dominant discount at 0.45. Songbird vocal learning is among the most specialised
motor-learning substrates in biology -- genetically scaffolded, bounded by a hard critical period,
with a dedicated forebrain pathway that has no obvious counterpart in a general-purpose embodied
agent. The authors' generalisation to other developing motor systems is offered as a conjecture and
should be read as one. The separateness *principle* may well generalise while the circuit
organisation does not.

Confidence 0.72. Source quality 0.92 -- Science, Fee lab, a definitive design that has held up for
over fifteen years, and I have no real doubt about the finding. Mapping fidelity 0.72: the
architectural read-across is direct, but the separateness/necessity gap is a genuine ceiling on what
this entry can be used to argue.
