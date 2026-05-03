# Stirling, Hellewell, Ndlovu (2001): Self-Monitoring and Positive Symptom Severity

This 2001 *Psychopathology* paper is the replication entry in the
Frith-comparator pull. Forty DSM-III-R schizophrenia patients
performed a battery of self-monitoring tasks alongside thirty-six
healthy controls. Patients were impaired on two of the tasks. The
impairment survived covariate adjustment for IQ, attention, and
recognition memory — meaning the deficit is specific to
self-monitoring rather than a manifestation of global cognitive
slowing. Among patients, self-monitoring performance correlated with
the severity and extent of positive symptoms (delusions, hallucinations,
passivity).

The evidential weight Stirling et al. add to the Frith account is the
parametric gradient: not just "patients fail self-monitoring" but
"the degree of self-monitoring failure tracks positive-symptom
severity within patients." That dose-response signature is what
MECH-095 should reproduce in REE: parametric variation in comparator
competence (whether driven by SD-047 substrate enrichment, training
duration, or hyperparameters) should produce parametric variation in
downstream symptom-analog metrics. A REE implementation that produces
binary pass/fail on agency-detection without an intermediate gradient
is missing something.

The honest caveats are sample size (N=40 + N=36 is modest by current
clinical standards) and modality (the tasks are self-monitoring
batteries — including action-monitoring and verbal-self-monitoring —
not the specific tactile attenuation paradigm Blakemore 2000 used).
This is replication-supporting rather than definitive evidence; its
value is in showing the Frith signature reproduces across paradigms
and covariate-adjustment frameworks rather than living only in the
Blakemore tactile attenuation.

For MECH-095 the practical implication is constructive: a working
implementation should produce a graded counterfactual_forward gap that
correlates with downstream agency-tag reliability. SD-047 validation
should look for this gradient, not just for binary PASS/FAIL on the
discriminative pair. This dovetails with Asai 2016's S/N-slope finding
— the comparator's competence is a graded quantity, and graded
variation in competence should produce graded variation in
attribution accuracy.

Confidence reasoning: source quality is moderate (smaller sample,
older diagnostic framework, less prestigious venue than Blakemore).
Mapping fidelity is good because the self-monitoring-vs-symptom-
severity correlation is structurally what REE should reproduce.
Transfer risk is moderate due to task modality differences. Net
confidence ~0.74.

According to PubMed, [DOI: 10.1159/000049307](https://doi.org/10.1159/000049307).
