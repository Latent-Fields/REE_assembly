# Kaufman et al. 2016 — the largest population component is the one that says nothing about which

**Claim:** SD-082 (`pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout`)
**Direction:** supports (premise, not fix) · **Confidence:** 0.78
**DOI:** [10.1523/ENEURO.0085-16.2016](https://doi.org/10.1523/ENEURO.0085-16.2016) (retrieved via PubMed, PMID 27761519)

## What the paper did

Kaufman and colleagues recorded from primary motor cortex and dorsal premotor cortex in two
macaques performing delayed reaches that varied in direction and in path (including curved and
obstacle-avoiding trajectories), and then asked a question about the *population* rather than
about single cells: of the time-varying activity patterns from which each neuron's response is
approximately composed, which ones care about *which* movement is being made, and which do not?
They identified components they call condition-invariant — components whose magnitude and time
course are nearly identical no matter which reach is executed — and compared them to the
direction-tuned components.

The result is the reason this paper is here. The largest condition-invariant component was *much
larger than any of the tuned components*: it explained more of the structure in individual-neuron
responses than the signal about movement identity did. And it occupied dimensions **orthogonal**
to those the tuned components occupied. Individual M1 and PMd neurons, the authors are careful to
say, essentially always reflected which movement was made — the untuned dominance is a property
of the population geometry, not of the cells.

## Why it matters for SD-082

SD-082 exists because of a measured structural zero. V3-EXQ-822 found a differentiated rule pool
(`on_rule_state_diff_mean` 0.644, `max_live` 16) that was behaviourally silent: propagation from
`rule_state` to the per-candidate action bias was exactly 0.0 on both arms, with
`zworld_cone_min_cosine` 0.963. The diagnosis was that the SD-033a bias head reads raw z_world
candidate summaries sitting in a common-mode cone, so every candidate's raw output overshoots
`bias_scale` in the same direction and the hard clamp maps them all to one rail.

What Kaufman et al. supply is that this geometry is not a simulation artefact. A real cortical
population, recorded in a real primate doing a real task, has a dominant component that carries no
information about *which*, with the discriminative content living in a much smaller subspace.
REE's z_world cone is an instance of a motif the brain also exhibits.

The orthogonality finding is the load-bearing part, and it is worth being precise about why.
SD-082(i) subtracts the across-candidate mean before the head. Whether that is a *repair* or a
*mutilation* depends entirely on the angle between the shared component and the discriminative
residual. If they are orthogonal — as Kaufman et al. measured in M1/PMd — subtraction removes the
variance that saturates the bound and leaves the discriminative geometry untouched. If they are
partially aligned, subtraction takes real signal with it. So this paper does not merely make
SD-082 plausible; it identifies the specific empirical condition under which SD-082's centering is
principled, and it reports that condition holding in cortex.

## Relation to the sibling dPCA entry

This directory already held an entry on Kobak et al.'s demixed PCA paper (landed `e41e28d6f3`),
which covers the *method* — condition-independent marginalisation as a general decomposition — and
reads it as the analytic form of SD-082's per-tick mean subtraction. The two are complementary
rather than redundant, and the division of labour is worth naming: Kobak et al. establish that
separating condition-independent from condition-dependent variance is a well-posed and general
operation; Kaufman et al. is the *measured instance* that supplies the two quantitative facts
SD-082 actually needs — that the condition-invariant component is the **largest** one, and that it
is **orthogonal** to the tuned dimensions. A method paper cannot tell you either of those about a
real population; only a recording can. Read the pair as method plus instance, and the instance is
where the licence for centering comes from.

## Limitations, and one that should change how we read V3-EXQ-822a

The honest boundary is that this is a *premise*-grounding paper, not a *fix*-grounding one.
Kaufman et al. subtract nothing in a working loop. Their decomposition is an offline dPCA over
trial-averaged data; SD-082 performs an online per-tick subtraction inside a forward pass. Nothing
here shows that any nervous system implements common-mode subtraction at a read-out, which is
precisely the mechanistic assertion SD-082 makes about lateral PFC. The transfer also crosses
areas (M1/PMd to a lateral-PFC analog) and representational kinds (firing-rate populations to a
learned encoder latent).

Two caveats bite harder than that, though.

First, the orthogonality that licenses centering **has not been measured in REE**. We have the cone
angle (0.963 min cosine) but not the angle between the common mode and the candidate-discriminative
direction. This matters for how V3-EXQ-822a's result should be read: the acceptance criterion is
`on_prop_delta_mean >= 0.001` with an ON>OFF contrast, which tests that propagation is *non-vacuous*
— it does not test that propagation is *faithful*. A centering operation that removed part of the
discriminative content would still clear that bar. Passing 822a is therefore necessary and not
sufficient; the question of whether the residual carries the rule information, rather than merely
carrying something, stays open after a PASS.

Second, and more interesting: in the biology, the large shared component is not nuisance. Its
timing predicts most of the trial-by-trial variance in reaction time — it is *when to move*.
SD-082 discards the analogous quantity unconditionally at the read-out. If anything in REE encodes
an overall urgency, salience or commitment level in the across-candidate mean summary, centering
destroys it, and the damage would not appear in `prop_delta` at all. It would appear somewhere
else, later, as a behaviour that got worse for no visible reason. That is the kind of failure this
architecture is worst at detecting, so it is worth naming now rather than after the fact.

## Confidence reasoning

Source quality 0.90 — primate single-unit population recordings from the Shenoy/Churchland
programme, established decomposition method, the key claim quantified rather than asserted.
Mapping fidelity 0.70 — deliberately not higher, because the paper evidences the geometry SD-082
presupposes rather than the operation SD-082 performs. Transfer risk 0.40 — the
dominant-shared-plus-small-tuned motif recurs across cortical populations, which lowers risk, but
the specific orthogonality that makes centering safe is the part REE has not checked.

Aggregate 0.78, above the component mean, because for an architectural design_decision the mapping
is the binding constraint and this mapping is unusually specific: the paper independently
characterises the exact pathology — a large shared component swamping discriminative content — that
V3-EXQ-822 measured as a structural zero in our own substrate.
