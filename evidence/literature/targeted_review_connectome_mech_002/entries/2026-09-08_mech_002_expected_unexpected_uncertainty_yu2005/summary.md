# Yu & Dayan (2005) -- Uncertainty, neuromodulation, and attention

**Claim tested:** MECH-002 (Precision control analogues shape cognitive regimes)
**Direction:** supports | **Confidence:** 0.85

## What the paper did

Yu and Dayan asked a normative question: if a brain is doing Bayesian inference in an environment
that is both noisy *and* liable to change without warning, how many kinds of uncertainty does it
have to track? Their answer is at least two, and the distinction is not a matter of degree. There is
the uncertainty you expect -- you know this cue is only 70% valid, and you have known that for a
while -- and there is the uncertainty that arrives when the world stops being the world you had a
model of. The first tells you how much to trust a prediction *within* your current context model.
The second tells you the context model itself may be void. They propose acetylcholine carries the
former (expected uncertainty) and norepinephrine the latter (unexpected uncertainty), and they
formalise this in a Bayesian model of attentional cueing, then walk it against a substantial body of
pharmacological, lesion and behavioural data.

The paper is theory plus synthesis rather than a new experiment, and it is worth being clear about
that when weighing it. Its force comes from the normative argument -- that the two signals *must* be
separable because they license opposite responses -- rather than from a single decisive measurement.

## Findings relevant to MECH-002

MECH-002 ends its regime list with a design constraint: "expected uncertainty (ACh-like) must be
separated from unexpected uncertainty (NE-like); they are distinct control channels, not a single
precision scalar." That sentence is very nearly this paper's abstract. So the honest description of
what this entry does for the claim is that it supplies the *reason* the constraint is a constraint
rather than an implementation preference. If you collapse the two into one scalar gain, you lose the
ability to distinguish "the evidence is noisy, weight it accordingly" from "the evidence is fine and
my model is wrong" -- and those two situations call for opposite updates. Down-weighting the
likelihood is right in the first case and catastrophic in the second.

That maps onto two of MECH-002's four regimes fairly directly. The ACh-like regime (raise
`alpha_gamma`, force perceptual updating against top-down prediction) is the expected-uncertainty
channel doing its job: when the cue is known-unreliable, let the sensory data speak. The NE-like
regime (transient gain on surprising input, reset priors, break phase-locks, suspend temporal
collapse) is the unexpected-uncertainty channel: do not re-weight within the model, abandon it.

## How this translates to REE, and where it strains

The translation is good at the level of *architecture* and weaker at the level of *knobs*. REE
indexes precision by hierarchical depth, `alpha_k`. Yu and Dayan index uncertainty by its role in a
specific generative model -- cue validity within a context, plus a hazard rate over context
switches. These are different axes. A given depth can be implicated in either kind of uncertainty
depending on the inferential situation, so it would be a mis-reading to treat `alpha_gamma` as
literally "the ACh level" or to assume the NE channel acts at exactly one depth. What transfers
cleanly is the two-channel requirement itself; what does not transfer is a one-to-one identification
of channels with depths.

Two further limits. First, the paper covers only two of MECH-002's four analogues -- it says nothing
about dopamine or serotonin, which are evidenced separately in this directory (Friston et al. 2012;
Miyazaki et al. 2014). Second, and more interesting as a constraint on implementation, Yu and Dayan
explicitly say the two signals interact, and that the interaction is "part-antagonistic,
part-synergistic". An REE implementation that exposes the ACh-like and NE-like channels as two
freely and independently settable scalars would be *simpler* than the source model, not equivalent
to it. That is worth flagging as a place the architecture could be quietly wrong in a way that only
shows up when both channels are driven hard at once.

## Confidence reasoning

Source quality 0.90: Neuron, foundational, and the framework has held up as an organising idea for
twenty years. Discounted from higher only because it is theory plus review, not a new empirical
dissociation. Mapping fidelity 0.90: MECH-002's design constraint is close to a paraphrase of the
thesis, which is about as high as mapping fidelity gets. Transfer risk 0.25: the depth-indexed
parameterisation is genuinely not the paper's parameterisation.

Aggregate 0.85, weighted toward mapping fidelity as the skill directs for architectural claims. The
one thing this entry does *not* establish is MECH-002's stronger reading -- that precision shifts
produce qualitatively distinct regimes with distinct phenomenology, rather than graded changes in
inference. Yu and Dayan give us the channels; they do not give us the regimes. That gap is real and
is not closed by any entry in this directory.
