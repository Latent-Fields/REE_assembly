# Louie, Grattan & Glimcher 2011 — cortex normalizes relative to the set, but it divides

**Claim:** SD-082 (`pfc.lateral_pfc.common_mode_invariant_trained_rule_to_action_readout`)
**Direction:** mixed · **Confidence:** 0.61
**DOI:** [10.1523/JNEUROSCI.1237-11.2011](https://doi.org/10.1523/JNEUROSCI.1237-11.2011) (retrieved via PubMed, PMID 21775606)

## What the paper did

Louie and colleagues recorded single units in macaque lateral intraparietal cortex during
value-guided saccadic choice, varying reward magnitudes across targets — including targets *outside*
the recorded neuron's response field. They asked whether an LIP neuron encodes what rational choice
theory would require, the absolute value of the option in its field, independent of what else is on
offer.

It does not. LIP neurons encode a relative value "explicitly dependent on the values of the other
available alternatives", and this context-dependence appears in baseline firing rates as well as in
stimulus-driven activity. The functional form is not a free fit: it is "precisely described by
divisive normalization" — the same gain-control computation behind extra-classical receptive-field
effects in visual cortex. The authors' framing is that normalization is a general mechanism of
cortical computation, extended here out of the sensory domain into value, and that it supplies the
mechanistic basis for context-dependent violations of rationality in choice behaviour.

## The half that supports SD-082

SD-082(i) makes a commitment before it makes an arithmetic choice: that the per-candidate quantity
feeding the lateral-PFC bias head should be computed **relative to the candidate set** rather than
per candidate in isolation. That commitment is open to an obvious objection — that conditioning on
the set is an engineering convenience which throws away information the agent might legitimately
need, and that a well-built read-out ought to be able to use each candidate's absolute summary.

This paper answers that objection with primate electrophysiology. A real decision circuit, in the
pathway that actually selects saccades, does not encode absolute option values. It encodes
set-relative ones, and it does so persistently enough to show up in baseline rates. Set-relative
conditioning of a choice-driving quantity is how the biology works.

## The half that undercuts it — and this is the point of the entry

The attested operation is **divisive**. SD-082's is **subtractive**. Under any other regime that
distinction might be a detail; under SD-008 it decides the outcome.

Take REE's measured situation: candidate summaries in a cone with `zworld_cone_min_cosine` 0.963.
Divide that set by a common denominator pooling the alternatives and you have a rescaled set of
vectors that are *exactly as collinear as before* — division changes magnitude, not angle. The bias
head would still see near-identical inputs, still push every candidate past `bias_scale` in the same
direction, and `prop_delta` would still be 0.0. Subtract the mean and the shared offset is gone and
the residual — the part that differs between candidates — is what the head now reads.

So the canonical cortical normalization is the one that **would not have repaired** the V3-EXQ-822
structural zero. This has a direct governance consequence, and I want to state it explicitly because
it is the kind of inference that gets made by accident: SD-082 **cannot** cite divisive
normalization as its biological warrant. Any reading of the form "normalization is canonical in
cortex, therefore SD-082 is biologically grounded" is invalid. SD-082's subtractive choice is
warranted by its ML precedent (dueling networks, where the operation and the reasoning both match)
and by the population-geometry premise (Kaufman et al., where the dominant shared component is
orthogonal to the tuned one and therefore safe to remove). It is not warranted by this paper, and
this paper is the one that a casual literature gesture would most likely reach for.

## A disagreement with the sibling entry, and how it resolves

This directory already contained an entry on Carandini & Heeger's canonical-normalization review
(landed in `e41e28d6f3` earlier the same day), and it reads the normalization literature as
supporting **both** SD-082 components at once: normalization "discounts the pooled common drive AND
bounds the response smoothly", one operation doing both of SD-082's jobs. My argument above cuts
against that. Rather than leave two entries in the same directory quietly contradicting each other,
here is the reconciliation, because working it through actually sharpens the claim.

Both are partly right, and they are right about *different halves*.

Divisive normalization **does** fix the saturation half. Dividing by a denominator that pools the
alternatives pulls an over-driven set back into dynamic range — which is precisely the clamp-rail
problem, every candidate overshooting `bias_scale` in the same direction. On that count the
Carandini entry is correct and my form-mismatch objection overstates.

Divisive normalization does **not** fix the signal-to-common-mode ratio. For summaries of the form
`x_i = c + δ_i` with `c >> δ`, division returns `(c + δ_i)/(σ + Kc)` — the small relative differences
are *preserved and rescaled*, not *exposed*. Subtraction returns `δ_i` itself. The discriminative
content goes from being a fraction of a percent of the signal to being the whole of it.

So SD-082's subtractive choice is better motivated than a flat "the biology divides, we subtract,
mismatch" reading would suggest: it does strictly more than the attested operation, and it does the
part that matters for a near-collinear candidate set. What remains true, and is the reason this entry
stays `mixed`, is that **the biological attestation covers only the weaker operation**. Cortex is
documented doing the thing that fixes saturation. It is not documented doing the thing that fixes
the ratio.

Neither sibling entry settles this, and governance should not treat either as having done so. The
discriminating measurement is REE-side, not literature-side: the angle between the z_world common
mode and the candidate-discriminative direction. If they are near-orthogonal (the Kaufman
condition), subtraction is clean and this whole question is closed. That measurement does not exist
yet.

## Two further caveats worth carrying

The normalization Louie et al. describe operates over *concurrently available* alternatives and is
a persistent circuit property. SD-082's centering is gated on `K >= 2` and computed per tick with no
memory, so a single-candidate tick receives no centering at all. The read-out's input statistics
therefore change discontinuously with candidate-set size. Whether that matters is untested — and a
mixed-K episode could produce tick-to-tick bias instability that a window-mean `prop_delta` would
average into invisibility.

The second is more interesting philosophically. The headline behavioural consequence of
normalization in this literature is **irrationality**: because coding is set-relative, adding a
third option changes the preference between two others. If SD-082's centering imports the same
context-dependence into the candidate bias — and structurally it does — then the bias on a candidate
becomes a function of which other candidates happen to be present on that tick. As biology that is
arguably a feature, and it is consistent with what this circuit demonstrably does. As architecture
it is a hazard for any downstream REE claim that treats the bias as a stable per-candidate property.
Worth checking before SD-082's centering is inherited by consumers beyond the SD-078 path.

## Confidence reasoning

Source quality 0.87 — J Neurosci, primate single units, the normalization model fitted
quantitatively against alternatives rather than asserted, and extended by the same group since
(Louie, Khaw & Glimcher 2013 PNAS, [10.1073/pnas.1217854110](https://doi.org/10.1073/pnas.1217854110),
carries it into monkey and human choice behaviour; Louie 2022 PLoS Comput Biol,
[10.1371/journal.pcbi.1010350](https://doi.org/10.1371/journal.pcbi.1010350), into asymmetric reward
coding in RL).

Mapping fidelity 0.50 — the lowest in this pull, deliberately. The paper evidences set-relative
coding, which SD-082 does assert; but the operation it attests to is the one that would not have
fixed our zero. A design_decision claim lives or dies on its mechanism, so a mismatch *at* the
mechanism is a halving, not a rounding error.

Transfer risk 0.50 — LIP to a lateral-PFC analog, and reward value to encoder latent, are both
substantive leaps. Normalization's claimed cortical generality mitigates without removing them.

Aggregate 0.61, mixed. This is the entry that keeps the pull honest.
