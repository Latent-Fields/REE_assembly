# Blakemore, Smith, Steel, Johnstone, Frith (2000): Tactile Self-Other Attenuation in Passivity

This is the empirical paper that supplied the Frith comparator account
of passivity phenomena with its canonical clinical signature. Healthy
participants and psychiatric controls without hallucinations or
passivity report self-produced tactile stimulation as less intense,
less tickly, and less pleasant than identical externally produced
stimulation — the well-known sensory attenuation that comes from
subtracting predicted self-caused afference. Patients with auditory
hallucinations and/or passivity experiences fail to show that
attenuation. The effect tracks symptom presence rather than primary
diagnosis, which is why this paper became foundational: the
self-monitoring breakdown is the syndrome's computational signature,
not a side-effect of schizophrenia per se.

For SD-047 and MECH-095 the mapping is unusually direct. MECH-095's
expected output is the agency-detection comparator's
counterfactual_forward gap; the working version produces a clear
gap for self-caused vs externally-caused state change, the failed
version produces near-equal gaps. The Blakemore measurement —
self-vs-other attenuation in tactile rating — is the same quantity in
a different modality. A V3-EXQ-506 with C1-C3 failures looks
structurally like the patients in Blakemore's study: the comparator's
output is flat, regardless of whether the input was self-caused or
not. SD-047's substrate enrichment is the proposed substrate-side fix;
the Blakemore signature is the kind of clean output an enriched
substrate should restore.

The honest caveat is the modality shift. Blakemore tested tactile
attenuation; MECH-095's V3 implementation reads hazard-field state
change. The architectural principle (working comparator produces
self-vs-other attenuation; failed comparator produces flat output) is
the same; the underlying sensory channel is not. This is licit
transfer at the architectural level, but no claim is made that the V3
substrate produces the specific tactile pleasantness rating Blakemore
measured.

The clinical finding also constrains REE in a useful direction. Any
proposed REE architecture that fails to reproduce a self-vs-other
attenuation signature on its native input modality fails the clinical
test that the V3 architecture is supposed to be modeling. This is a
falsifiability hook: an SD-047 implementation that produces flat
counterfactual_forward gaps regardless of substrate enrichment would
mean either (a) MECH-095 is implemented wrong, or (b) the V3
architecture as a whole lacks the comparator machinery the Blakemore
study identifies as load-bearing in humans.

Confidence reasoning: source quality is very high (Frith lab,
Psychological Medicine, canonical paradigm). Mapping fidelity is high
because the measured quantity is structurally identical to MECH-095's
expected output. Transfer risk is moderate due to the modality shift.
Net confidence ~0.82.

According to PubMed, [DOI: 10.1017/s0033291799002676](https://doi.org/10.1017/s0033291799002676).
