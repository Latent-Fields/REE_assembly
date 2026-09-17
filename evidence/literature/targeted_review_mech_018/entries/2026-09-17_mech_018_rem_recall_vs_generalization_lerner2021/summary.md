# REM sleep can have inverse effects on recall and generalization of fear memories

## What the paper did

Lerner and colleagues begin from an honest statement of the problem: REM sleep is known to modulate
fear-memory consolidation, and the published findings contradict each other about which direction it
modulates in. Their move is to stop treating "fear memory" as one quantity. Using sleep-deprivation
protocols across two complementary experiments, and a fear-conditioning paradigm built so that
participants must discriminate between coexisting threat and safety signals, they measured recall of
the original conditioned threat and generalisation to novel situations separately, with skin
conductance responses and fMRI.

The two came apart. REM sleep impaired recall of the original threat memories. The same REM sleep
improved the ability to generalise those memories to novel situations in which threat had to be told
from safety. The authors propose that both follow from how predictive the threat/safety balance was
for a given stimulus, and relate this to the REM recalibration hypothesis.

## Why this is the most important paper in this pull

MECH-018 asserts that a single sleep-phase operation does four things at once, and its confirming
criterion is explicit that the integration arm must beat both a no-sleep and a naive-decay arm
sign-consistently across seeds. That is a conjunctive claim. Conjunctive claims are vulnerable in a
particular way: they fail not when the mechanism does nothing, but when the mechanism does something
and the somethings point in different directions.

This paper is the biological demonstration that the two most important conjuncts -- preservation of
the original aversive trace, and improved contextual discrimination -- can dissociate under exactly
the physiology REE is modelling. Whatever REM is doing here, it is not free. The discriminative gain
was bought with a recall cost. If `ResidueField.integrate` is wired into `SleepLoopManager._run_cycle`
and the resulting run shows the specificity ratio rising while residue at the recorded harm
locations drops below its floor, MECH-018 does not get to call that a partial success. It has
pre-registered that outcome as FALSIFYING -- "integration ERASES ... the moral-injury-overload fix
has become forgetting" -- and this paper says that is the empirically live outcome, not a remote one.

## The caveat that keeps this from being a straightforward weakening

I do not think this entry licenses reading MECH-018 as probably false, and I want to be precise
about why. The paper's "generalisation" is not REE's "over-generalisation". Lerner et al. mean
correctly extending a learned threat structure to novel discriminative situations -- a competence.
MECH-018 means residue bleeding from harm contexts into equidistant non-harm ones -- a failure. A
system can improve on the first while getting worse on the second, or better on both. So the SIGN of
the generalisation result does not import cleanly into REE's specificity ratio. What imports cleanly
is the dissociation itself: that the operation has separable effects on the two readouts, and that
they need not agree.

Two further limits. The reconciling predictiveness account is offered post hoc, so it explains the
dissociation without having predicted it, and a post-hoc account that can absorb either direction is
a weak constraint on REE. And the paradigm is bespoke and, so far as I can tell, not independently
replicated, so the dissociation itself should be held as a serious possibility rather than an
established fact.

## Confidence

0.55, direction mixed. This is the right confidence for an entry whose value is that it establishes
a tension rather than resolves one. It should be read alongside the Denis et al. entry in this same
directory, which supports the conjunction, and the Davidson et al. null, which finds no sleep effect
on the generalisation gradient at all. Three competent groups, three different answers on the crux
readout, is itself the finding: readout (ii) is where MECH-018 will actually be decided, and the
literature will not decide it for us.
