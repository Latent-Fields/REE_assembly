# Tervo et al. 2014 -- LC-NE gating of stochastic behavioural variability (MECH-313)

According to PubMed, Tervo, Proskurin, Manakov, Kabra, Vollmer, Branson & Karpova (2014),
*Behavioral variability through stochastic choice and its gating by anterior cingulate cortex*,
Cell ([DOI](https://doi.org/10.1016/j.cell.2014.08.037)).

**What the paper did.** Rats faced virtual competitors. Like primates, they normally used
history- and model-based (strategic) play. But when pitted against a competitor they could *not*
beat by counter-prediction, they switched into a **"stochastic" mode** in which outcomes
associated with their own actions were ignored and normal ACC engagement was suppressed. Using
circuit perturbations in transgenic rats, the authors showed that switching between the strategic
and stochastic modes is controlled by **locus coeruleus (noradrenergic) input into ACC**: under
uncertainty about environmental rules, changed noradrenergic input alters ACC output and prevents
erroneous beliefs from guiding decisions, thereby *enabling behavioural variation*.

**Why it matters for MECH-313.** This is the strongest of the three anchors for the CDQ-002
refinement, and it is *causal* rather than correlational. It establishes both properties the
NoisyNet import proposes to add to MECH-313:
- **State-conditioning:** the noradrenergic variability signal is engaged specifically by
  environmental uncertainty/uncontrollability -- not applied uniformly.
- **Self-annealing:** when a model-based strategy is winning, the stochastic mode is suppressed
  (ACC re-engaged). The exploration "floor" recedes as the environment becomes controllable.

Together with Aston-Jones & Cohen's adaptive-gain theory, this says plainly that MECH-313's
currently-registered *state-independent* floor is biologically under-specified: the LC-NE tonic
exploration signal is gated by uncertainty and annealed by control. NoisyNet's learned,
state-dependent, self-annealing parametric noise is therefore the biologically *correct* shape of
the mechanism, which is what this lit-pull needed to establish before registration.

**Caveat and confidence.** Tervo's "stochastic mode" is a competitive-game phenomenon in rats and
reads more like a discrete mode gate than a graded, continuously self-annealing per-parameter
sigma; the mapping to a smooth learned-sigma is an interpretation, and rodent-to-REE transfer
applies. The paper also does not address whether the variability propagates to a committed/argmax
action -- the REE-side V3-EXQ-687 question that the candidate's own falsifier must answer. I score
it `supports` at 0.82: high source quality (Cell; causal circuit perturbation), high mapping
fidelity (the LC-NE -> behavioural-variability pathway is exactly MECH-313's substrate, and the
uncertainty-gating maps cleanly onto state-conditioning + self-annealing), moderate-to-high
transfer risk.
