# Arm immobilization causes cortical plastic changes and locally decreases sleep slow wave activity (Huber et al., 2006)

## What the paper did

This is the companion experiment to Huber et al. (2004), run in the opposite direction. Instead of
adding a learning load to a circumscribed cortical region and asking whether local sleep intensity
rises, the authors immobilized one arm for twelve waking hours and asked whether it falls. They
verified the intended effect independently: motor performance deteriorated, and both somatosensory
and motor evoked potentials over contralateral sensorimotor cortex decreased, which is the signature
of local synaptic depression rather than an inference from the sleep data itself. During the
subsequent night, slow wave activity over that same cortical territory was markedly reduced.

The authors' conclusion is symmetrical and worth quoting in its own terms: cortical plasticity is
linked to local sleep regulation without learning in the classical sense, and when synaptic strength
is reduced, local sleep need is reduced with it.

## Why this is the most relevant paper in the pull, and also the most uncomfortable

Everything else here manipulates input upward. INV-063 is a claim about what happens when input goes
*down* -- it is a starvation claim -- and this is the only entry that actually starves something and
watches. That directional match is genuine and is why I have marked it `supports`: it establishes
that the offline system is not indifferent to impoverished input, which is the minimal precondition
for expecting any signal at all in a low-intake arm.

But I do not want to file this paper without saying plainly that its result is the deflationary
reading of our own claim. What reduced input produced was *less sleep need*. Not degraded
consolidation; not starved replay; a correctly downregulated budget. On that reading, an agent in a
low-entropy environment is not suffering -- it has less to consolidate and schedules less
consolidation, and the whole "starvation" framing is a category error dressed in clinical language.
That is INV-050's proportional drive, and it is the account this literature most naturally supports.

INV-063 only becomes a distinct claim if the offline budget is pinned and function degrades anyway.
This paper is the strongest available evidence that in biology those two axes are not naturally
separable -- intake and budget move together, by design, because that is what sleep homeostasis *is*.
Which means our P2 gate (`use_mel_consumer=False`, zero cross-arm variance in SWS writes and REM
rollouts, asserted from measured output) is not a formality to be waved through. It is the entire
experiment. Without it we will measure the Huber 2006 result in simulation and mistake it for
INV-063.

## A second confound the paper surfaces for our design

Immobilization degraded waking motor performance as well as reducing sleep SWA. The offline change
is therefore confounded with an online competence change pointing the same way. Our intake ladder
has precisely this exposure: the lowest-intake arm may simply be a less competent agent, and any
offline DV read from it carries that competence difference. We already recorded this hazard as the
reason for excluding the E2 motor-learning leg from INV-063's falsifier, but this paper is a reminder
that the hazard is not confined to the excluded leg -- it applies to leg B's frozen-battery world
prediction too, which is part of why that leg is measured as a pre/post *difference* on the same
frozen probe rather than as an absolute.

## Confidence

0.58. High source quality (0.85) -- within-subject, with an explicit manipulation check that the
intended synaptic depression occurred, which is the same discipline our P1 gate demands and worth
noting the biology practised first. What limits it is mapping fidelity (0.5): an immobilized arm is a
poor semantic match for a low-entropy environment, and the DV sits once again on the quantity axis.
I would cite this as the reason to expect a signal in the low arms, and equally as the reason to
distrust that signal until P2 is demonstrably satisfied.

According to PubMed: [DOI 10.1038/nn1758](https://doi.org/10.1038/nn1758), PMID 16936722.
