# Thought Intake: External Framework Crosswalk for REE Ethics

Status: processed
Processed in:
- `docs/claims/claims.yaml` (thought-intake REAP: GOV-EXT-1 (external framework crosswalk -- internal REE ethics must remain externally legible). This file is cited in those claims' `sources`.)


**Date:** 2026-06-19
**Type:** thought intake / external ethics and legal framework crosswalk
**Associated with:**

- `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md`
- `docs/thoughts/2026-06-18_sentience_welfare_risk_register.md`
- `docs/thoughts/2026-06-19_ethical_assembly_routing_map.md`
- `docs/architecture/established_ethical_systems.md`

**Scope:** V3 public substrate, V4 individual-mind, V5 social-mind, V6 language/trust/deception/institutions, future public/human-facing deployment
**Priority:** high as governance scaffolding; not a V3 green-board blocker
**Core phrase:** Internal REE ethics must remain externally legible.

---

## One-sentence claim

REE needs a standing crosswalk against external AI, legal, human-rights, standards, data-protection, health, security, research-ethics, and AI-welfare frameworks so that internal REE ethics does not become self-validating or illegible to the outside world.

---

## Background

REE now has a growing internal ethics sequence: sentience/welfare risk, creation ethics, pre-meaning suffering, anti-retrospective justification, ethical assembly routing, and responsible release/private higher-version governance.

That internal sequence is necessary but not sufficient.

If REE develops higher versions, especially V5 social-mind or V6 language/trust/deception/institution layers, its ethics must be legible through external frameworks as well. REE may eventually touch areas covered by AI regulation, human-rights due diligence, AI risk management standards, data protection, medical-device/health AI governance, cybersecurity, research ethics, and artificial-welfare scholarship.

This intake does not claim that all frameworks legally apply to current REE-v3. It creates a trigger map so that future stages do not discover external obligations late.

---

## Core thought

REE can have an internal ethical architecture, but it should not be allowed to validate itself only by its own terms.

External frameworks provide three forms of discipline:

1. **Legal discipline** -- what obligations may apply if a system is deployed, public-facing, high-risk, data-processing, clinical, or agentic.
2. **Institutional discipline** -- how risk management, documentation, roles, auditability, and review should be structured.
3. **Moral translation** -- how REE's own categories map to autonomy, dignity, rights, fairness, transparency, accountability, human oversight, security, consent, data protection, and research ethics.

The purpose is not to subordinate REE to every external checklist. The purpose is to prevent REE ethics from becoming private language.

---

## Proposed register addition

### GOV-EXT-1 -- External framework crosswalk

Before V4/V5/V6 capability-bearing work is released, REE should maintain a crosswalk that maps each ethically active component to relevant external frameworks.

Minimum fields:

```yaml
component_or_plan:
generation: v3|v4|v5|v6|public_deployment|clinical
capability_type:
  - self_model
  - autobiographical_memory
  - negative_valence
  - social_mind
  - language
  - trust_deception
  - institution
  - human_facing
  - clinical_or_health
  - personal_data
  - tool_use_or_external_action
frameworks_triggered:
  - EU_AI_Act
  - Council_of_Europe_AI_Convention
  - NIST_AI_RMF
  - ISO_IEC_42001
  - ISO_IEC_23894
  - OECD_AI_Principles
  - GDPR_DPIA
  - WHO_Health_AI
  - Medical_Device_Regulation
  - OWASP_GenAI
  - MITRE_ATLAS
  - Belmont_Helsinki_CIOMS
  - AI_Welfare_Consciousness
status: not_applicable|watch|mapping_needed|review_required|do_not_release_until_review
notes:
```

---

## Framework 1: EU AI Act

The EU AI Act should be treated as the primary legal/regulatory watch framework for Ireland/EU.

Current REE-v3 is a research substrate, not a deployed high-risk system. However, later REE versions could trigger AI Act analysis if they become:

- human-facing AI systems;
- clinical or health-related systems;
- education, employment, public-service, justice, law-enforcement, migration, biometric, or emotion-recognition-adjacent systems;
- general-purpose AI components;
- systems that interact with users and need transparency/disclosure;
- agentic systems that act in the world or materially affect people.

REE relevance:

- Create an `AI Act trigger map` before any public-facing or institution-facing release.
- Treat high-risk use contexts as deployment gates, not merely feature labels.
- Distinguish research code, demo systems, public interactive systems, clinical tools, and deployed decision-support systems.
- Do not describe REE as safe for high-risk use without conformity-style documentation and review.

Suggested trigger phrase:

> If REE affects people's access to services, health, education, work, rights, safety, or institutional decisions, AI Act-style risk classification is required before use.

---

## Framework 2: Council of Europe AI Convention / human-rights framework

The Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law is relevant even where REE is not yet legally in scope, because it frames AI as a human-rights and democratic-governance problem.

REE relevance:

- Map REE's external impact to human dignity, autonomy, equality, non-discrimination, privacy/data protection, transparency, oversight, accountability, reliability, and safe innovation.
- Create a human-rights impact register before any REE system affects people outside toy/synthetic experiments.
- Include challengeability, complaint, notice, transparency, and affected-person rights in future human-facing designs.
- Treat institutional deployment as a special risk class.

Suggested trigger phrase:

> If REE significantly affects a person, group, community, institution, or democratic process, it needs a human-rights impact assessment, not merely an internal harm metric.

---

## Framework 3: NIST AI Risk Management Framework

NIST AI RMF is useful operationally because it turns responsible AI into a lifecycle discipline rather than a list of principles.

REE relevance:

- Map REE's claim-governed loop to NIST-like functions: Govern, Map, Measure, Manage.
- Use the framework to organise risk ownership, evidence review, metric validity, failure modes, monitoring, and post-release response.
- Build an AI risk register that sits alongside claims.yaml rather than replacing it.

Potential mapping:

```text
REE claims/governance loop -> NIST Govern
Roadmaps + component trigger maps -> NIST Map
Experiments + manifests + audits -> NIST Measure
Holds + release gates + private repos + mitigations -> NIST Manage
```

Suggested trigger phrase:

> Every V4/V5/V6 capability should have a risk-management state, not only an epistemic-confidence state.

---

## Framework 4: ISO/IEC 42001 and ISO/IEC 23894

ISO/IEC 42001 is relevant as a future management-system skeleton, even if REE is not seeking certification. ISO/IEC 23894 is relevant as an AI risk-management guide.

REE relevance:

- Define roles, responsibilities, risk processes, release approvals, incident review, documentation, change control, and continual improvement.
- Keep a lightweight version while REE is solo/hobbyist, but structure files so they could later mature into a real AI management system.
- Create a Statement-of-Applicability-style note for which controls are relevant at each version.

Suggested trigger phrase:

> Before REE becomes a public or collaborative AI system, it needs explicit management-system artefacts: scope, roles, risks, controls, review, and improvement.

---

## Framework 5: OECD AI Principles

The OECD AI Principles provide a public-facing, interoperable responsible-AI vocabulary: human rights, democratic values, fairness, privacy, transparency/explainability, robustness, security, safety, accountability, inclusive growth, sustainability, and wellbeing.

REE relevance:

- Use OECD principles as a public-facing summary layer.
- Map REE's internal values into language recognisable to policymakers and non-technical reviewers.
- Use the OECD lifecycle definition to keep release/deployment categories clear.

Suggested trigger phrase:

> REE's internal ethical vocabulary should be translatable into OECD-style trustworthy-AI language without loss of caution.

---

## Immediate recommended artefact

Create later:

`docs/governance/external_framework_crosswalk.md`

Initial columns:

```yaml
version:
component:
public_or_private:
framework:
trigger:
obligation_or_principle:
REE_mapping:
required_artifact:
status:
reviewer:
notes:
```

---

## Non-blocking / blocking status

This crosswalk should not block V3 green-board.

It should block:

- public V4 self-model/autobiographical/affective-memory implementation if no framework mapping exists;
- V5 social-mind implementation release if human-rights/research/welfare mapping is absent;
- V6 language/trust/deception/institution release if AI Act/security/human-rights mapping is absent;
- any clinical, patient-facing, or service-facing use without health/data/research governance.

---

## Proposed claim wording

**GOV-CLAIM-001:** REE internal ethics must remain externally legible; each higher-version capability should be mapped against relevant legal, human-rights, AI-risk, standards, data-protection, health, security, research-ethics, and AI-welfare frameworks before public release.

**GOV-CLAIM-002:** Current V3 research substrate does not require full regulatory treatment as a deployed high-risk AI system, but future human-facing, clinical, institutional, language-agentic, or public deployment contexts may trigger external obligations.

**GOV-CLAIM-003:** REE should treat legal and external ethical frameworks as trigger maps and translation layers, not as replacements for internal care, welfare, and assembly-order governance.

**GOV-CLAIM-004:** A capability is not release-ready merely because it is scientifically interesting or internally coherent; it must also be externally classifiable, documented, reviewable, and bounded.

---

## References

### Internal REE references

- `docs/START_HERE_HOW_REE_DEVELOPS.md` -- claim-governed experimental loop.
- `docs/architecture/established_ethical_systems.md` -- REE derivation of autonomy, justice, rights, care, research ethics, professional ethics, precaution, sustainability, and responsible innovation.
- `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md` -- release governance and private higher-version hypothesis.
- `docs/thoughts/2026-06-19_ethical_assembly_routing_map.md` -- co-instantiation and assembly-order governance.

### External references

- European Commission. *AI Act: Shaping Europe's digital future*. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
- Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*. https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence
- NIST. *AI Risk Management Framework*. https://www.nist.gov/itl/ai-risk-management-framework
- NIST. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. https://doi.org/10.6028/NIST.AI.600-1
- ISO. *ISO/IEC 42001:2023 Artificial intelligence management system*. https://www.iso.org/standard/81230.html
- ISO. *ISO/IEC 23894 Artificial intelligence risk management*. https://www.iso.org/standard/77304.html
- OECD. *OECD AI Principles overview*. https://oecd.ai/en/ai-principles

---

## Abstracted-language compression

`REE_InternalEthics requires ExternalLegibility`

`ExternalFrameworks := AIAct + CoE_HumanRights + NIST_RMF + ISO42001 + OECD`

`CurrentV3 := research_substrate, not_deployed_high_risk_system`

`FutureTrigger := human_facing OR clinical OR institutional OR language_agentic OR public_deployment`

`ReleaseReady := internally_coherent AND externally_classifiable AND documented AND reviewable AND bounded`
