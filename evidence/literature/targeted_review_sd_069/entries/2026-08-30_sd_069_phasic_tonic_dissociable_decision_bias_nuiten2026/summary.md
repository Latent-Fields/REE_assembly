# Nuiten et al. 2026 -- phasic and tonic arousal separate on one decision readout

## What the paper did

Twenty-eight healthy men, a yes/no detection task with Gabor patches buried in dynamic noise, and a
strategic bias manipulation: aversive tones followed misses in one condition and false alarms in the
other, pushing subjects liberal or conservative. Pupillometry throughout, EEG alongside, and a
within-subject pharmacological design (atomoxetine to raise catecholamines, donepezil for
acetylcholine, placebo). Tonic arousal was operationalised as mean pupil diameter in the 500 ms
before stimulus onset; phasic arousal as the baseline-corrected, response-locked pupil response
between -590 and -270 ms relative to the behavioural response.

The dissociation is clean. Tonic pupil related to *inherent* decision criterion, task-independently
(pd > 0.999, mu = -0.05) -- more liberal responding at higher tonic arousal, with no interaction
with the bias manipulation. Phasic pupil related to *context-dependent strategic shifts*: the
task-induced bias was weakest on high-phasic-arousal trials, with a significant task-by-phasic-bin
interaction on the drift-diffusion starting point (pd > 0.999, mu = 0.004). The authors summarise it
as tonic arousal being associated with inherent bias while phasic arousal is associated with
strategic shifts.

## Why SD-069 needs this

SD-069 exists for one reason: a 2026-07-17 substrate scan found that MECH-063 sub-claim (ii) -- each
control axis carries independent tonic baseline *and* phasic event-burst degrees of freedom --
could not be tested behaviourally, because MECH-313's noise floor was the only tonic lever on the E3
softmax and nothing phasic sat beside it on a comparable readout. The claim's whole architectural
bet is that tonic and phasic are separately expressible on *the same* effective-temperature channel,
with distinguishable temporal signatures: a sustained lift for tonic, an event-locked transient for
phasic.

This study is the human evidence that such a split is real, measurable, and expressible on a single
decision readout rather than requiring two separate channels. The phasic component is explicitly
event-locked -- defined in a narrow window relative to the response -- and the tonic component is a
sustained pre-stimulus baseline. That is structurally the contrast V3-EXQ-779a is built to score:
dS_tonic sustained across the window, dR_phasic transient and decaying over the tail.

## The parameter mismatch, which I do not want to gloss

The shared readout here is decision *bias* -- criterion in signal-detection terms, starting point in
the DDM. SD-069's readout is pre-commit softmax *entropy*: decision stochasticity, not decision
preference. These are different parameters of the same choice distribution, and evidence that tonic
and phasic separate on one does not entail that they separate on the other. It is entirely coherent
for two levers to dissociate on where the distribution is centred while acting identically on how
spread out it is, which is exactly SD-069's falsifier (1). So this entry raises the prior that the
architecture is biologically sound; it does not stand in for the measurement.

Two smaller strains. The phasic window is defined relative to a behavioural response in a discrete
trial, and REE's tick loop has no such landmark. And pupil diameter is a peripheral proxy for LC-NE,
not a recording of it -- a point worth holding onto given that SD-069's whole lit basis is the
Aston-Jones and Cohen phasic mode.

## What the pharmacology does and does not add

Atomoxetine only trended toward more liberal bias (93% of posterior mass below zero), and donepezil
produced no robust effect. So the catecholaminergic attribution of the phasic effect is not causally
established here; the pupil results are correlational, and the authors say so. They also failed to
replicate prestimulus frontal theta and occipital alpha effects from earlier work, attributing the
divergence to task design and motivational context. That is honest reporting and it is also a
reminder that these dissociations are not yet robust across paradigms.

## Confidence

0.74. Design quality is high and the finding is close to the architectural point SD-069 needs, but
N=28 male-only, the key results are correlational, and the bias-versus-noise mismatch is a genuine
gap rather than a technicality.
