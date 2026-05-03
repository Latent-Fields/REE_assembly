# Ward, MacLean, Kirschner (2010): Stochastic Resonance and Neural Synchronization

This 2010 *PLoS ONE* paper from Larry Ward's group provides the
direct neural demonstration of the stochastic-resonance principle that
the SD-047 noise-sweep validation depends on. Healthy participants
performed a near-threshold auditory deviant-detection paradigm with
varying levels of added broadband noise. The 40 Hz transient response
in bilateral auditory cortex (with additional sources in posterior
cingulate cortex and superior frontal gyrus) was *enhanced* by added
noise rather than degraded. Synchronization between these regions in
alpha and gamma bands also increased with added noise. The signature
is non-monotonic: an intermediate noise level optimises both signal
detection and inter-region synchronization.

For the symmetric-over/under-attribution diagnostic-signature pull,
this is the empirical bridge between Asai 2016's agency-slope finding
and the broader architectural principle. Where Asai showed that
agency-rating slopes are S/N-dependent in psychophysical data, Ward
et al. show the same shape in direct neural data: comparator
competence (operationalised as 40 Hz response amplitude and
inter-region synchronization) has an optimum, not a monotonic
saturation point. The non-monotonic shape is biological reality, not
just psychophysical artifact.

For MECH-095 and SD-047 the load-bearing implication is concrete.
The SD-047 design doc revised the validation experiment to a 4-arm
noise-level sweep precisely because Asai's non-monotonicity predicted
that ON/OFF testing would be ambiguous between "SD-047 works" and
"SD-047 overshot calibration." Ward et al. supply the neural-level
evidence that this prediction is generic: human cortical
synchronization shows the same inverted U for substrate noise.
SD-047 is therefore expected to produce the inverted U at the
agency-detection level if MECH-095 implements anything resembling
the synchronization architecture human auditory cortex uses for
near-threshold detection. A flat or monotonic response curve in
SD-047 validation would be diagnostic of an architecture that lacks
this kind of substrate-noise-enabled signal enhancement — likely a
falsification rather than a calibration miss.

For the broader ai-cognitive-failure-taxonomy, stochastic resonance
supplies a generic architectural diagnostic. Comparator-failure modes
are likely substrate-noise-dependent. Diagnosing them via inverted-U
fitting on a noise sweep is more informative than binary
ON/OFF testing. This applies to provenance collapse, belief fixation,
and the other comparator-class failure modes too — a useful
methodological export from the Pull 4 work to the rest of the
taxonomy.

The honest weakness is paradigm specificity. Ward et al. measured
auditory perception of near-threshold pure tones, not agency
attribution. The mapping into MECH-095 is at the architectural-
principle level (stochastic resonance is a general phenomenon of
noise-enabled signal detection). Whether MECH-095's specific
implementation in REE V3 exhibits the inverted U is an empirical
question — exactly the question the SD-047 noise-sweep validation is
designed to answer.

Confidence reasoning: *PLoS ONE* venue (moderate prestige but
methodologically clean — high-density EEG, ICA, dipole fitting).
Mapping fidelity is moderate-high. Transfer risk is moderate due to
paradigm specificity. Net confidence ~0.74.

According to PubMed, [DOI: 10.1371/journal.pone.0014371](https://doi.org/10.1371/journal.pone.0014371).
