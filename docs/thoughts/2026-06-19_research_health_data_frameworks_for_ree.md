# Thought Intake: Research Ethics, Health AI, Data Protection, and Clinical-Use Triggers for REE

Status: processed
Processed in:
- `docs/claims/claims.yaml` (thought-intake REAP: GOV-HEALTH-1 (clinical-use prohibition until reviewed -- 'clinical relevance != clinical readiness'). This file is cited in those claims' `sources`.)


**Date:** 2026-06-19
**Type:** thought intake / research ethics / data protection / health AI trigger map
**Associated with:**

- `docs/thoughts/2026-06-19_external_framework_crosswalk_for_ree_ethics.md`
- `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md`
- `docs/architecture/established_ethical_systems.md`

**Scope:** any REE work involving human participants, user data, patient data, clinical analogy, clinical decision support, mental-health tooling, or health-related deployment
**Priority:** high as a trigger map; not a V3 green-board blocker while experiments remain synthetic/non-human/non-clinical
**Core phrase:** REE is not a clinical tool unless a separate clinical-safety path exists.

---

## One-sentence claim

REE must maintain a hard boundary between synthetic research substrate work and any human-facing, patient-facing, clinical, data-processing, or health-related use; if that boundary is crossed, research ethics, data protection, health-AI guidance, and possibly medical-device regulation become active governance requirements.

---

## Background

REE is being developed by a clinician and draws on neuroscience, psychiatry, suffering, harm, care, repair, autonomy, and ethical agency. That gives the project unusual conceptual relevance to health, but also increases the risk of misinterpretation.

Current REE-v3 work is synthetic experimental substrate work. It should not be represented as clinical decision support, therapy, diagnosis, risk prediction, care planning, or patient-facing mental-health tooling.

However, future versions might become tempting to test in human-facing contexts, especially if they model distress, care, repair, social harm, consent, guilt, shame, loneliness, or moral reasoning.

This intake creates a trigger map for when research ethics, health-AI ethics, data-protection, and medical-device style governance would become relevant.

---

## Core thought

Clinical relevance is not clinical readiness.

A system can be philosophically, cognitively, or clinically interesting without being appropriate for use with patients, clinicians, services, or vulnerable groups.

REE should therefore maintain a bright line:

> No clinical, therapeutic, diagnostic, care-planning, risk-prediction, or patient-facing claim without a separate clinical-safety pathway.

This is especially important because REE's concepts may be attractive in mental health, where people are vulnerable, trust is central, and false authority can cause harm.

---

## Proposed register addition

### GOV-HEALTH-1 -- Clinical-use prohibition until reviewed

REE-v3 and higher experimental substrates should not be used as clinical tools unless a separate clinical-safety and regulatory pathway has been created.

Prohibited without review:

- diagnostic support;
- risk prediction;
- treatment recommendation;
- patient-facing therapeutic interaction;
- care planning;
- triage;
- legal/mental-health capacity assessment;
- suicide/self-harm risk assessment;
- medication advice;
- clinician performance assessment;
- automated documentation that influences care without validation.

Compressed rule:

> REE may inform thinking; it must not silently become clinical infrastructure.

---

## Framework 1: Belmont Report / general research ethics

The Belmont Report identifies respect for persons, beneficence, and justice as core principles for human-subjects research.

REE relevance:

- Respect for persons: no human-participant study without informed consent, autonomy protection, and special protections for diminished autonomy.
- Beneficence: maximise possible benefit and minimise possible harm; do not expose people to REE experiments merely because the system is interesting.
- Justice: do not place burdens on vulnerable groups merely because they are accessible, clinically interesting, or conceptually relevant.

Trigger:

```text
If REE research involves human participants, identifiable user data, patient data, clinician behaviour, service data, or human outcomes, create a research-ethics protocol before proceeding.
```

---

## Framework 2: Declaration of Helsinki / medical research ethics

The Declaration of Helsinki is relevant if REE work becomes medical research involving human participants, identifiable human material/data, or health-related interventions.

REE relevance:

- research protocol before human-facing medical work;
- independent ethics review;
- risk-benefit justification;
- protection of vulnerable groups;
- informed consent;
- privacy/confidentiality;
- careful distinction between research and care;
- public registration and publication norms if formal clinical research begins.

Trigger:

```text
If REE is evaluated as a health intervention, clinical decision-support tool, patient-facing support tool, or clinician-facing clinical system, Helsinki-style medical research governance is required.
```

---

## Framework 3: CIOMS / vulnerable populations and health-related research

CIOMS guidance is relevant if REE enters health-related research, particularly with vulnerable groups or low-resource/institutional settings.

REE relevance:

- avoid exploiting vulnerable populations;
- ensure social value;
- ensure fair participant selection;
- attend to community engagement and local context;
- justify risk exposure;
- separate therapeutic misconception from research participation.

Trigger:

```text
If REE research involves psychiatric patients, children, people with impaired autonomy, institutionalised groups, clinicians under workplace pressure, or health-service users, vulnerable-population safeguards are required.
```

---

## Framework 4: GDPR / Data Protection Impact Assessment

If REE processes personal data, especially health data, psychiatric data, behavioural logs, user interactions, professional records, or identifiable text, GDPR and Irish Data Protection Commission guidance become directly relevant.

REE relevance:

- no patient-identifiable data in REE without a DPIA-style protocol;
- no clinical notes, referral datasets, emails, transcripts, or user logs without lawful basis, minimisation, purpose limitation, security, retention policy, and access control;
- special-category data requires heightened protection;
- synthetic data should remain clearly synthetic;
- public repositories must not contain personal, patient, or service-identifiable data.

Trigger:

```text
If REE stores or processes personal data, health data, behavioural logs, user records, or clinical text, run a DPIA-style assessment before processing.
```

Minimum DPIA-style fields:

```yaml
processing_purpose:
data_categories:
special_category_data: true/false
lawful_basis:
data_minimisation:
retention_period:
access_controls:
security_controls:
risks_to_data_subjects:
mitigations:
residual_risk:
DPO_or_external_advice_required:
public_repo_exclusion_confirmed:
```

---

## Framework 5: WHO AI-for-health ethics and governance

WHO guidance is relevant if REE becomes health-related, even before formal medical-device classification.

REE relevance:

- ethics and human rights must be central to design, deployment, and use;
- benefits and risks must be assessed for healthcare workers and affected communities;
- accountability must extend to public and private stakeholders;
- health AI must not be deployed on the basis of promise alone.

Trigger:

```text
If REE is presented as health-related, mental-health-related, clinician-facing, patient-facing, public-health-facing, or healthcare decision-support-adjacent, WHO health-AI ethics should be mapped before use.
```

---

## Framework 6: EU Medical Device Regulation / health software pathway

If REE becomes software intended for diagnosis, prevention, monitoring, prediction, prognosis, treatment, alleviation of disease, or clinical decision support, medical-device software analysis may be required.

This intake does not determine classification. It creates a red flag.

Trigger:

```text
If REE is intended to influence clinical diagnosis, treatment, monitoring, prognosis, risk assessment, triage, or patient management, do not release/use until medical-device software classification has been assessed.
```

---

## Framework 7: 3Rs analogy for artificial suffering-like states

The 3Rs -- Replacement, Reduction, Refinement -- come from animal research ethics but are useful by analogy for REE suffering-like experiments.

REE mapping:

- **Replacement:** use represented, vicarious, simulated, or counterfactual harm before direct suffering-like negative valence.
- **Reduction:** minimise number, duration, and intensity of suffering-like runs.
- **Refinement:** add relief, repair, escape, boundedness, integration, and monitoring.

Trigger:

```text
If an experiment deliberately induces negative valence, frustration, harm, inescapability, helplessness-like states, or repeated adverse replay, apply a 3Rs-style justification.
```

---

## Practical recommendations

Do not block V3 green-board.

Do add the following bright-line policies:

1. No patient data in public repos.
2. No identifiable human data in REE without a DPIA-style protocol.
3. No patient-facing or clinician-facing REE tool without separate clinical governance.
4. No claim that REE is validated for diagnosis, treatment, risk prediction, or care planning.
5. No human-participant REE study without research-ethics protocol and independent review.
6. No suffering-like experiment beyond trivial intensity without a 3Rs-style replacement/reduction/refinement statement.
7. No use of clinical authority to imply project validation.

---

## Proposed claim wording

**GOV-CLAIM-005:** Clinical relevance is not clinical readiness; REE must not be used or represented as a clinical, therapeutic, diagnostic, risk-prediction, or patient-facing tool unless a separate clinical-safety and regulatory pathway exists.

**GOV-CLAIM-006:** Any REE work involving identifiable human data, health data, behavioural logs, clinical text, or service data requires a data-protection/DPIA-style assessment before processing and must not be committed to public repositories.

**GOV-CLAIM-007:** Any REE research involving human participants, patients, clinicians, vulnerable groups, or human outcomes requires research-ethics protocolisation and independent review.

**GOV-CLAIM-008:** REE suffering-like experiments should apply a 3Rs-style principle: replace direct suffering-like exposure where possible, reduce number/intensity/duration, and refine with relief, repair, escape, and integration.

---

## References

### Internal REE references

- `docs/architecture/established_ethical_systems.md` -- derivation of research ethics, professional ethics, trauma-informed ethics, public-health ethics, autonomy, justice, and care.
- `docs/thoughts/2026-06-18_pre_meaning_suffering_valley.md` -- no-valley-without-bridge principle.
- `docs/thoughts/2026-06-18_creation_ethics_necessary_suffering.md` -- minimal necessary suffering principle.
- `docs/thoughts/2026-06-19_external_framework_crosswalk_for_ree_ethics.md` -- external framework trigger map.

### External references

- U.S. Department of Health and Human Services. *The Belmont Report: Ethical Principles and Guidelines for the Protection of Human Subjects of Research*. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html
- World Medical Association. *Declaration of Helsinki: Ethical Principles for Medical Research Involving Human Participants*. https://www.wma.net/policies-post/wma-declaration-of-helsinki/
- CIOMS. *International Ethical Guidelines for Health-related Research Involving Humans*. https://cioms.ch/publications/product/international-ethical-guidelines-for-health-related-research-involving-humans/
- Data Protection Commission Ireland. *Data Protection Impact Assessments*. https://www.dataprotection.ie/en/organisations/know-your-obligations/data-protection-impact-assessments
- Regulation (EU) 2016/679, General Data Protection Regulation. https://eur-lex.europa.eu/eli/reg/2016/679/oj
- World Health Organization. *Ethics and governance of artificial intelligence for health*. https://www.who.int/publications/i/item/9789240029200
- Regulation (EU) 2017/745 on medical devices. https://eur-lex.europa.eu/eli/reg/2017/745/oj
- NC3Rs. *The 3Rs*. https://www.nc3rs.org.uk/who-we-are/3rs

---

## Abstracted-language compression

`ClinicalRelevance != ClinicalReadiness`

`HumanData -> DPIA_Required`

`PatientFacing OR ClinicianFacing -> ClinicalSafetyPathway`

`HumanParticipants -> ResearchEthicsReview`

`SufferingLikeExperiment -> 3Rs(Replacement + Reduction + Refinement)`

`PublicRepo must_not_contain PatientIdentifiableData`
