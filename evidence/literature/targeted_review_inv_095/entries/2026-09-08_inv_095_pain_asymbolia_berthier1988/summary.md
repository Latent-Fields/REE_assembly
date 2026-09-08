# Berthier, Starkstein & Leiguarda (1988) -- when the signal arrives but stops mattering

## What the paper did

Berthier and colleagues described six patients with asymbolia for pain following unilateral brain
damage. The defining feature was a dissociation: sensory function was normal -- these patients could
detect, localise and describe a noxious stimulus -- yet they showed "a lack of withdrawal and absent
or inadequate emotional responses to painful stimuli." Hemiparesis, sensory loss and neglect were
common accompaniments. Across all six, "the insular cortex was invariably damaged," and the authors
proposed that insular damage disconnects sensory cortex from limbic regions, so that nociceptive
information arrives without acquiring affective significance.

## Key findings relevant to the claim

This is the entry in the pull that comes closest to INV-095's own wording. The axiom's architectural
consequence is stated as: "harm matters because existence matters. If existence had no value, harm
signals would be noise rather than information." Pain asymbolia is the clinical instantiation of the
consequent. The signal is not noise in the information-theoretic sense -- it is transduced,
localised, and reportable. What has been removed is its status as being *about something that
matters*. And when that is removed, protective behaviour goes with it.

That matters for REE because it establishes that the two halves can come apart. Confirming that
`z_harm_a` and `z_harm_s` are computed, that `ResidueField` produces output, that the values are
graded and well-formed -- none of this establishes the axiom's consequence. A REE build could pass
every one of those checks and still be an asymbolic architecture: harm correctly represented,
correctly nowhere in the trajectory decision. INV-095's leg is therefore not trivially satisfied by
the 2026-08-07 audit finding that the machinery is live and wired. Wiring is a precondition, and
this paper is the reason to insist it is only that.

## How this translates to REE

The mapping runs to the weighting stage rather than the computation stage. INV-007's audit traced
the harm signal's reach into E3's harm-weighted trajectory scoring
(`ree_core/predictors/e3_selector.py`); Berthier et al. describe what happens in a biological system
when the analogous reach is severed while the upstream representation survives. The prediction for
REE is specific: an intervention that leaves `z_harm_a`/`z_harm_s` intact but removes their weight
in E3 selection should degrade hazard-avoidance behaviour, and should do so *without* degrading any
measure of harm representation quality. If a REE ablation shows degraded behaviour with intact
upstream harm encoding, this is the phenotype it has reproduced.

That also suggests a design refinement for the V3-EXQ-533 successor. A noise substitution and a
weight ablation are different experiments, and running the weight ablation as a positive control
would tell you whether your behavioural readout is sensitive enough to detect *any* harm-pathway
disruption before you ask the harder noise question. A null noise result is uninterpretable without
that control -- which may be part of what went wrong the first time.

## Limitations and confidence reasoning

The confounds are serious and I do not want to soften them. Hemiparesis, sensory loss and neglect
were all common in this series, and each can abolish withdrawal from a noxious stimulus on its own
terms. A hemiparetic patient may fail to withdraw because the motor pathway is damaged; a
neglecting patient may fail because the stimulus never reaches attention. Neither is a valuational
deficit, and a 1988 bedside examination with no quantitative behavioural measure is not equipped to
separate them. The insular attribution is a common-lesion inference across six uncontrolled cases,
not a manipulation.

There is also a mapping boundary. The lesion cuts a *connection*; INV-095's falsifier corrupts a
*signal*. Disconnection and uninformativeness are adjacent architectural failure modes but not the
same one, and a REE experiment could reproduce the first while leaving the second untested.

Confidence 0.63, with an unusual internal profile: source quality 0.62, mapping fidelity 0.80. That
inversion is the reason to include the entry despite its age. No better-controlled human study makes
this particular dissociation, and the dissociation -- signal present, mattering absent, behaviour
degraded -- is the specific thing INV-095's testable leg requires and that no amount of
signal-quality evidence can supply.
