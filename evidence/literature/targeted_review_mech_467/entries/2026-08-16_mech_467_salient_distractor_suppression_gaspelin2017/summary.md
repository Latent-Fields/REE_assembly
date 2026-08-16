# Gaspelin & Luck 2018 -- inhibition in avoiding distraction by salient stimuli

## The debate and the resolution

Whether a salient stimulus involuntarily captures attention has been argued for thirty years, with each
side producing experiments the other could not accommodate. Gaspelin and Luck review the evidence for a
mechanism that dissolves the impasse: salient stimuli do attempt to capture, and capture can be prevented
if the stimulus is *suppressed before capture occurs*. Psychophysical probe measures, first-saccade
eye-tracking and ERP components converge on it -- and the ERP evidence is the load-bearing part, because
the Pd component indexes suppression at the encoding side rather than inferring it from the absence of a
behavioural consequence.

Crucially, suppression is not all-or-none across a session. It waxes and wanes with task demands and with
lapses of control.

## The half that supports MECH-467

MECH-467 needs sensory capture to be a real, separable stage -- not an automatic precursor that always
either happens or does not, tightly yoked to whether behaviour goes wrong. If capture were obligatory
whenever a salient distractor appeared, leg 1 would carry no independent information and the three-way
carve-up would collapse toward two.

This review establishes the opposite: leg 1 has its own control mechanism, which can succeed or fail
independently, and the failure is graded. That is what makes a three-way dissociation coherent as a thing
to look for.

## The half that corrects it, which is the reason I pulled the paper

MECH-467 carries a non-degeneracy guard: the distractor must actually be registered by the system --
non-zero sensory-capture rate in at least one arm -- because "a distractor the agent never encodes tests
nothing", and an all-floor battery self-routes `substrate_not_ready` rather than returning a verdict.

The reasoning is right and the operationalisation is not. Registered-then-suppressed and never-encoded
produce the *same* floor capture rate. That is the entire finding of this literature. So the guard, as
written, cannot tell the two apart, and it will fire `substrate_not_ready` on precisely the case where the
substrate handled the distractor correctly -- which is the most expensive way to be wrong, because a
self-route looks like a clean, well-behaved outcome rather than a defect.

The humans solve this with the Pd. REE has no Pd. What it would need is a direct read of whether the
distractor's features entered the active representation, independent of whether they altered selection --
some encoding-side probe of the representation itself. Absent that, leg 1's measurement and the
non-degeneracy guard are reading the same confounded quantity, and the guard adds no information beyond
what the leg-1 measure already provides.

I would treat this as a live design requirement for the successor battery rather than a footnote. V3-EXQ-874
already lost leg (c) to a 0/0 denominator; losing a rerun to a false `substrate_not_ready` on leg (a) would
be a second measurement-design defect on the same claim.

A smaller point: because suppression fluctuates within a session, a single aggregate capture rate across a
block averages over trials where suppression held and trials where it failed, and can report a mid-range
number describing no trial that actually happened. Trial-level distributions, not block means.

## Confidence

0.64. Strong review, genuinely mixed bearing -- it makes MECH-467's taxonomy more coherent and its guard
less trustworthy, and the second of those is the more actionable.
