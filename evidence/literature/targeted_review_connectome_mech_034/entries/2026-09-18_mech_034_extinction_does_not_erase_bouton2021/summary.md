# Extinction does not erase -- why residue is entitled to persist

MECH-034's confirming criterion has two parts, and the second one gets less attention than it
deserves. It is not enough that harm and mismatch write different surfaces; the criterion also asks
that the surfaces behave differently *afterwards* -- residue at a harmed region should persist and
keep raising trajectory cost, while staleness at a perturbed region should decay with re-visitation
and route to replay rather than to cost. That is a claim about the shape of forgetting, and it needs
its own evidence.

Bouton, Maren and McNally's Physiological Reviews synthesis is the best available source for the harm
side of it. Their central finding, accumulated across decades of behavioural and circuit work, is
that neither Pavlovian nor instrumental extinction depends substantially on erasure of the original
learning. What extinction builds is new *inhibitory* learning, expressed primarily in the context
where it was acquired. The renewal effect is the clean demonstration: take the animal out of the
extinction context and the original conditioned responding comes back, because it was never removed.
At the circuit level this is a tripartite amygdala-prefrontal-hippocampal arrangement for Pavlovian
extinction, with prefrontal inhibition of amygdala fear ensembles doing the suppressing and
hippocampal-prefrontal circuits mediating relapse; instrumental extinction runs on distinct
corticostriatal, striatopallidal and striatohypothalamic ensembles.

## The mapping to residue

REE's residue is designed to be non-erasable. That is an architectural commitment, and the kind of
commitment that deserves to be interrogated rather than assumed -- it would be easy to read it as a
safety convenience rather than a principled design. This literature says it is principled. Biology
solved the same problem the same way: an organism that could have its harm learning subtracted by a
run of benign experience would be a dangerous organism, and evolution appears to have declined that
design. Contradicting evidence adds a context-gated inhibitor on top; it does not reach in and reduce
the original trace.

## Two things this does not do, and one warning

It does not compare against mismatch. The review is entirely about aversive and instrumental learning
persistence; it never asks how a state-prediction-error signal decays by contrast. MECH-034 asserts
an *asymmetry*, and this entry grounds only one of its two arms. I have set mapping fidelity at 0.58
for exactly that reason, and it is the lowest in this pull.

It is also a review. Review-level consensus maps less crisply onto a pre-registered effect-size bound
than a single measured study does, and MECH-034's falsifier is written in effect sizes.

The warning is the more useful contribution, and I would flag it to whoever builds the V3 arm.
Extinction is expressed *context-specifically*. Which means an apparent decay of residue, measured in
one context, can be a retrieval failure rather than an erasure. A V3 readout that evaluates
`ResidueField.evaluate` only at fixed region centres in the training configuration could report
residue decaying when it has merely become context-gated -- and would then score a confirming
criterion as failed for the wrong reason. If residue is meant to be non-erasable, the experiment
should probe for renewal, not only for persistence.

## Confidence

0.65, direction `supports`. Strong source, real relevance, but grounding one arm of a two-arm
asymmetry, and I would rather say that plainly than round it up.
