# Rule and O'Leary 2022 -- the lineage-free rival, verified down to its parameters

This anchor is cited by two claims with opposite valence, which is why it carries an
`evidence_direction_per_claim`. For MECH-562 it is the subject: the claim asserts that receiver-local
self-healing is the standing rival to every cross-system interface-repair result, and this paper is where
that rule comes from. For MECH-553 it is the named competitor: if a stable readout can track a drifting code
with no explicit lineage representation, then lineage-free dependency estimation might match explicit
genealogy, and compressed causal genealogy earns no keep. Both claims recorded it as `NOT INDEPENDENTLY
VERIFIED`.

The citation is exact -- *PNAS* 119(7):e2106692119, doi 10.1073/pnas.2106692119, PMID 35145024, PMC8851551,
Rule and O'Leary -- and the abstract matches the claims' description: "interactions between Hebbian learning
and single-cell homeostasis can exploit redundancy in a distributed population code to compensate for gradual
changes in tuning", achieved "without external error feedback", with recurrent feedback of partially
stabilised readouts correcting residual inconsistency. What is worth reporting is that I went further and
checked MECH-562's *specific* parametric assertions against the open-access full text, because those are the
kind of second-hand detail that decays silently. All of them hold, verbatim:

- "populations of 100 units that encode theta and whose tunings evolve independently" -- the claim's "100
  encoding units";
- "Each weight evolves as a discrete-time Ornstein-Uhlenbeck (OU) process" -- the claim's "Ornstein-Uhlenbeck-
  like process";
- "we resampled the weights for single encoding units one-at-a-time from a standard normal distribution.
  Self-healing plasticity rules were run each time 5 out of the 100 encoding features changed" -- the claim's
  "abrupt per-feature resampling, plasticity applied after each five of 100 features change";
- and the disclaimer: "The simplest interpretation of Eq. 5 is a premise or ansatz: Learning rates should be
  modulated by homeostatic errors. This is a prediction that will need to be experimentally confirmed" --
  which is exactly MECH-562's "the authors themselves describe the Hebbian-homeostatic coupling as an ANSATZ
  awaiting physiological confirmation".

Whoever wrote that note read the paper properly. The note can now be cited as verified rather than as
second-hand.

The direction split needs stating plainly. For MECH-562 the paper *supports* the claim, in the specific sense
that the claim asserts this rival exists and must be beaten -- confirming the rival's existence confirms the
claim's content. For MECH-553 it *weakens*, because MECH-553 proposes compressed causal genealogy as the
representation that discharges INV-107, and this paper is the standing argument that no such representation
may be needed. But I want to be careful not to overstate the weakening, because MECH-553's notes already are.
Rule and O'Leary show that a readout can maintain *performance* through drift without lineage. They do not
show, and never attempt, that a lineage-free estimator can recover the *dependency structure between two
items* -- whether these two pieces of evidence share an origin. That is a different question, and it is the
one MECH-553 actually claims. The rival is real and the P6 rung of the ladder is the right place to settle
it; this paper alone does not settle it.

Confidence 0.66. Source quality is high -- PNAS, clean specification, reproducible. The discount is that it is
a model of a mechanism whose central coupling the authors explicitly decline to claim is physiological, and
that the compensation demonstrated is for gradual drift or a few units at a time rather than wholesale
reconfiguration. Per `feedback_lit_exp_decoupled`, none of this raises either claim's confidence.
