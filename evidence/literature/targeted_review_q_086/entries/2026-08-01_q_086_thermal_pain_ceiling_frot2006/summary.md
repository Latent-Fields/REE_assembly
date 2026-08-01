# Frot, Magnin, Mauguiere & Garcia-Larrea (2006) -- Human SII and posterior insula differently encode thermal laser stimuli

**What the paper did.** The authors recorded intracranial evoked potentials directly
from electrodes implanted in secondary somatosensory cortex (SII) and posterior
insula in patients undergoing presurgical evaluation for temporal lobe epilepsy.
Stimuli were brief CO2-laser thermal pulses of graded intensity, spanning
non-painful (sensory threshold) up through clearly painful levels. The design
question was whether these two anatomically adjacent, functionally coupled pain
processing regions encode stimulus intensity the same way across that full range.

**Key findings.** They diverge sharply above pain threshold. SII scales its
evoked-potential amplitude with stimulus intensity from sensory threshold up to
roughly the pain threshold, then plateaus -- a textbook ceiling/saturation effect
in which further increases in physical stimulus energy produce no further increase
in SII's response. Posterior insula does the opposite: it is largely silent below
pain threshold, then scales its response with intensity specifically in the
painful range, without the ceiling SII shows. The authors interpret SII as a
finer-grained discriminator across the sensory-to-mildly-painful range and
posterior insula as the channel that keeps discriminating once a stimulus is
unambiguously noxious.

**How this maps to Q-086.** Q-086 was framed as an either/or: is z_harm_a's
observed saturation at high hazard density a faithful ecological signal (chronic
suffering genuinely plateaus because the underlying threat has plateaued) or a
representational/calibration pathology (the readout mechanism itself has a ceiling
that has nothing to do with the true underlying intensity)? This paper's most
useful contribution is not evidence for one side over the other -- it is evidence
that the either/or framing may itself be under-specified. In the human brain, a
representational ceiling (SII) and a faithful high-intensity tracker (posterior
insula) coexist for the same stimulus class in the same organism at the same time.
Neither channel alone is "the" pain-intensity signal; the system's actual
sensitivity across the full range depends on having both. Read against REE's
architecture, this suggests the diagnostic question worth asking is not "is
z_harm_a's plateau real or artifact" as a single yes/no, but whether z_harm_a is
functioning as an SII-like categorical/threshold channel that is *expected* to
ceiling once harm crosses into a severe regime, and whether the substrate has (or
needs) a second, non-saturating channel -- closer to posterior insula -- to
preserve high-intensity discrimination for exactly the regime SII stops resolving.
That reframing is directly actionable: it points toward instrumenting a secondary,
deliberately-not-yet-saturated harm-tracking signal (candidate: something closer
to the sensory-tier z_harm_s the confirmed V3-EXQ-857 autopsy already flagged as
under-instrumented via min_eval_steps) rather than only asking whether the existing
z_harm_a channel is "broken."

**Limitations and caveats.** The stimulus paradigm here is a brief evoked response
to a single noxious pulse, not an accumulated, episode-level affective-load signal
of the kind z_harm_a is architecturally closer to -- there is a real temporal
disanalogy between "does this channel saturate to a discrete stimulus" and "does
this channel saturate as chronic load accumulates." The population is patients
with temporal lobe epilepsy, whose baseline pain processing may not be fully
representative of a healthy population, and the sample size in intracranial human
electrophysiology studies is necessarily small. This paper does not test anything
resembling REE's environment or hazard-density manipulation; it is cited purely
for the general principle it establishes about coexisting saturating and
non-saturating intensity channels in biological affective/nociceptive systems.

**Confidence reasoning.** Source quality is high -- direct intracranial human
recording is about as strong a design as exists for dissociating cortical
pain-intensity coding, and this is a well-cited, methodologically careful paper.
Mapping fidelity is moderate: the core phenomenon (representational ceiling
coexisting with a parallel faithful-tracking channel) translates cleanly as a
design principle, but the acute-evoked-response vs accumulated-load disanalogy is
real. Transfer risk is moderate-to-high given the cross-domain jump from human
intracranial pain electrophysiology to an RL agent's internal scalar harm
signal. Net confidence 0.68: supports the reading that representational ceilings
are a real, mechanistically well-grounded phenomenon (so a calibration-pathology
explanation for z_harm_a's plateau is entirely plausible on priors), while also
reframing the open question toward an actionable architectural follow-on rather
than settling it either way.
