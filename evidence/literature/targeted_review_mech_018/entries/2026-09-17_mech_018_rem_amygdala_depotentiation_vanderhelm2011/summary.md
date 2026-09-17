# REM sleep depotentiates amygdala activity to previous emotional experiences

## What the paper did

van der Helm and colleagues put healthy adults through an emotional-image viewing session, then
either a night of polysomnographically recorded sleep or an equivalent waking interval, then a
second viewing of the same images under fMRI. The question was whether the affective charge of an
already-encoded experience is lower the next day, and whether that reduction tracks REM sleep
specifically. It did: amygdala reactivity to the previously-seen emotional images dissipated
overnight, functional connectivity with prefrontal cortex was altered, and subjective emotionality
ratings fell. The degree of dissipation was associated with REM-sleep EEG physiology -- in
particular with the reduction in high-frequency (gamma-band) activity that indexes central
adrenergic tone.

## Why this bears on MECH-018

MECH-018 asserts four things happen to the residue field during a sleep cycle: residue at harm
contexts is PRESERVED, it becomes more CONTEXT-TIED, it is COMPRESSED, and the field becomes more
TRAVERSABLE -- fewer hippocampal proposals in non-harm regions are rejected on residue cost. This
paper is the clearest biological statement of the fourth readout. The affective tax levied by a
remembered aversive episode falls overnight, and it falls in a physiologically specific window
rather than simply with the passage of time. That is what REE wants its WRITEBACK phase to do: make
the agent able to move through a world it has been hurt in, without the hurt having been deleted.

The neuromodulatory account matters as much as the behavioural result. The proposed mechanism is not
attenuation-by-decay but reactivation under a changed neurochemical context: amygdala-hippocampal
networks replay the salient trace while noradrenaline is suppressed, so the trace is re-encoded
without its arousal tag. That is a two-part operation -- reactivate, then re-weight -- and it is the
shape `ResidueField.integrate` is supposed to have. The alternative the field could implement,
uniform multiplicative attenuation, has no reactivation step at all and no reason to be REM-specific.

## Limitations and where the mapping strains

I want to be careful not to let this paper carry more than it can. It shows reactivity falling; it
does not independently show that the memory was preserved. A residue field that simply erased
everything overnight would produce exactly this signature, and MECH-018 names that outcome as
FALSIFYING, not confirming. So this is support for readout (iv) and only weak, inferential support
for readout (i). Second, the REM association is correlational -- nothing in the design manipulated
REM to demonstrate that the dissipation follows it. Third, and most importantly for the claim as
written, the study contains no analogue of a specificity ratio, so it is silent on readout (ii), the
anti-over-generalisation function that is arguably the load-bearing half of MECH-018.

There is also a structural mismatch worth naming. Amygdala BOLD is a transient evoked response to a
re-presented stimulus. REE's residue is a persistent scalar field over z_world, and what makes it
matter is that it prices traversal of regions the agent was never explicitly shown. "Reactivity to a
re-presented image falls" and "the cost of proposing a nearby trajectory falls" coincide only under
REE's own architectural assumption that residue cost is what drives proposal rejection. That
assumption is reasonable and it is what the substrate implements, but it is an assumption.

## Confidence

0.62. The source is good and canonical, the mechanism is the right one, and the direction is
unambiguous. I have held it below 0.7 because the paper evidences one of four readouts cleanly, is
silent on the crux readout, and cannot by itself distinguish integration from the erasure the claim
pre-registers as its own falsification. It is the right anchor paper for this claim; it is not
sufficient evidence for it.
