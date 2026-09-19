# Surprise signals in anterior cingulate cortex: unsigned reward prediction errors

Hayden, Heilbronner, Pearson & Platt (2011), *The Journal of Neuroscience* 31(11):4178-4187.
DOI [10.1523/JNEUROSCI.4652-10.2011](https://doi.org/10.1523/JNEUROSCI.4652-10.2011) - PMID 21411658
- PMC3070460. Retrieved via PubMed.

## What the paper does

Single-unit recordings from macaque dorsal anterior cingulate cortex during a probabilistic choice
task. The finding: dACC responses to outcomes were enhanced when the outcome was *surprising* --
and enhanced for both unexpectedly large and unexpectedly small rewards. Valence did not matter;
surprisingness did. Trial-to-trial shifts in behavioural preference tracked that same
surprisingness. A control condition in which outcome probabilities were hidden reduced the neuronal
responses, consistent with expectation being what makes surprise possible in the first place -- a
neat internal check against the obvious alternative account.

The authors state the consequence plainly: these patterns are inconsistent with dACC neurons
tracking *signed* reward prediction errors the way dopamine neurons do. They also rule out conflict
signalling, and link the dACC reward modulation instead to attention and motor-control processes
driving behavioural adjustment.

## How it bears on MECH-055

MECH-055's axis 3 is "signed PE precision from a genuine forward-model-based precision-weighted PE
on BOTH harm and benefit sides", and the claim locates the harm half in a dACC-consumed harm
forward-model PE -- which, per MECH-054's 2026-08-08 finding, is currently the only half REE
actually has. If the primate dACC carries unsigned surprise, then the dACC naming is not doing the
work it appears to be doing. REE may still have a perfectly well-defined signed harm PE as a
computational object; what it loses is the appeal to anatomical homology as independent support for
that object being signed and harm-specific. The weakening is against the claim's warrant, not
against its internal coherence, and this entry is recorded as `weakens` on that narrower basis.

## The more useful consequence: the collapse risk may be in the wrong place

MECH-055's COLLAPSE-RISK CHECK asks whether `VALENCE_HARM_DISCRIMINATIVE` and the dACC harm PE are
one scalar wearing two labels. Hayden et al. suggest a different pairing is the live one.

REE's residue field already carries `VALENCE_SURPRISE` (index 3, unsigned prediction-error magnitude
by construction) alongside `VALENCE_POSITIVE_SURPRISE` and `VALENCE_NEGATIVE_SURPRISE` (indices 4
and 5, signed, and written only when `use_mech307_split_surprise` is enabled -- zero otherwise). If
the dACC-named channel is functionally an unsigned surprise magnitude, then the tightest redundancy
in REE is between that channel and `VALENCE_SURPRISE`, not between it and
`VALENCE_HARM_DISCRIMINATIVE`. A distinctness test that checks only the pair the claim names can
come back clean while the real collapse sits in a pair the claim never tests. That is worth writing
into the experiment design before it is run, not discovered afterwards.

There is a third point the paper makes that REE should not skip past: the dACC signal's documented
downstream role here is *behavioural adjustment* -- attention and motor control -- not valenced
affect. An architecture that routes a dACC-named signal into an affect vector is not licensed by
this result.

## Limits, stated honestly

The dACC signed-versus-unsigned question is contested, not settled. Other primate and human work
reports signed value and outcome-valence coding in nearby cingulate territory, and "dACC" is
delineated differently across labs. One well-executed study should move the prior without closing
the question.

More constraining for our purposes: the task varies reward *magnitude* and contains no punishment or
harm condition at all. Strictly, the paper shows dACC surprise coding is insensitive to valence
across the reward-magnitude axis -- not across an appetitive/aversive axis. REE's harm channel
concerns the latter. The inference to the harm side is an extrapolation and is flagged as such in
the record's `mapping_caveat`.

## Confidence

0.75. Source quality 0.84: careful work, well-designed hidden-probability control, strong lab; but
two animals, one task, one region, arguing into a contested literature. Mapping fidelity 0.70 --
the signed/unsigned distinction is exactly what MECH-055 leans on, docked because there is no
aversive arm. Transfer risk 0.40: macaque electrophysiology to a named module in an artificial
agent, where the module's *name* is carrying argumentative weight the biology may not support.
