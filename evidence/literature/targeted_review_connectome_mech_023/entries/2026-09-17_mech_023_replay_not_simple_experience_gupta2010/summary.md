# The simulation channel is promiscuous, and REE has closed it by fiat

MECH-023's third confirming criterion is the one that carries the ethical weight: hypothesis-tagged —
simulated, replayed, merely imagined — harm in region R must *not* produce the divergence that real
harm produces. Only what was actually done is supposed to shape the terrain. REE already enforces this
in the substrate: `ResidueField.accumulate` refuses hypothesis-tagged content, inheriting the MECH-094
gate. The question this entry asks is whether that enforcement is modelling biology or overruling it.

Gupta, van der Meer, Touretzky and Redish recorded hippocampal ensembles during sharp-wave ripples
while rats performed two distinct behavioural sequences on a multi-route maze. If replay were a simple
rehearsal of recent experience, its content should track what the animal just did. It does not.
Sequence B was replayed frequently after the animal had spent more than ten minutes performing
sequence A. Replay covered all physically available trajectories, including never-experienced novel
shortcuts. And the inversion that makes the result memorable: less-frequently-performed routes were
replayed *more* than heavily practised ones. The offline hippocampus spends its time on the paths the
animal did not take, weighted roughly inversely to how much it took them.

The tension with REE's architecture is structural rather than empirical, and I want to be precise
about where it sits. Gupta et al. establish replay *content*. They do not show that replayed sequences
write into the same substrate that carries aversive history, and they certainly do not show that a
replayed harm accrues residue. Replay could be entirely read-only with respect to the residue-bearing
geometry, in which case there is no conflict whatsoever and the MECH-094 gate is simply correct. What
the paper does is make the write-back question *live*: the structure ARC-013 names as the residue
substrate demonstrably traverses counterfactual paths, in volume, offline, as a matter of course. A
gate that refuses all such content is therefore a decision with a cost, not a transcription of how the
hippocampus works.

The cost is worth naming, because it is the interesting half. If simulated traversal never deforms the
geometry at all, then an agent cannot learn what to avoid by imagining it — every constraint has to be
purchased with a real committed harm. That is a strange kind of mind to build, and it sits awkwardly
beside REE's own commitment to imagination-driven learning elsewhere in the architecture. The plausible
resolution is that the gate is about *attribution* rather than about *influence*: replayed content may
legitimately shape the world model and the policy while being refused entry to the residue ledger,
because residue is a record of what this agent did and not of what it knows. If that is the intended
reading, it should be stated where the gate is implemented, since the code as written refuses the
content outright and the distinction does not survive in the refusal.

For the experiment itself, the practical consequence is small but real: criterion (iii) — that
hypothesis-tagged harm in R produces no divergence — is, in the V3 substrate, *true by construction*
rather than measured. A run that reports it as a confirmation is reporting that the refusal in
`accumulate` works, which is a unit test, not a finding. The criterion is only informative if the
simulated-harm arm is run through a path that could in principle reach the field, and the write is
refused at the tag check rather than never attempted.

Confidence 0.62, with mapping fidelity the limiting term at 0.5. The source is excellent — a
heavily cited Neuron paper whose central result has held up — but the inferential step from replay
content to residue write permissions is mine and not the authors'. Direction recorded as `weakens`
because it removes a biological warrant REE's gate might otherwise be thought to have; it does not
contradict any measurement the claim makes.
