# Thought Intake: Security, Misuse, Agentic Risk, and Capability-Boundary Frameworks for REE

Status: processed
Processed in:
- `docs/claims/claims.yaml` (thought-intake REAP: GOV-SEC-1 (security and misuse release gate). This file is cited in those claims' `sources`.)


**Date:** 2026-06-19
**Type:** thought intake / security / misuse / agentic containment / release-risk trigger map
**Associated with:**

- `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md`
- `docs/thoughts/2026-06-19_external_framework_crosswalk_for_ree_ethics.md`
- `evidence/planning/language_trust_deception_institutions_v6_plan.md`

**Scope:** V4/V5/V6 capability release, language/tool use, public demos, agentic systems, security-sensitive deployment, social/language manipulation risk
**Priority:** high for V6 and any tool-using public agent; not a V3 green-board blocker
**Core phrase:** Do not release a capability that can act faster than its containment can understand.

---

## One-sentence claim

REE needs an explicit security and misuse framework before any language-bearing, tool-using, social, deceptive, persuasive, or public-facing capability is released, because V6 language/trust/deception/institution work creates both internal welfare risk and external human/security risk.

---

## Background

The responsible-release intake established that V5 and V6 may need private-by-default implementation. This intake specifies the security side of that claim.

REE V6 already recognises language as both a coordination medium and a dangerous attack surface. The language/trust/deception/institutions plan includes language-cannot-override-harm, trust calibration, deception detection, language failure modes, and institutional residue coordination.

That is necessary, but it mostly describes internal cognitive/social integrity.

External security asks additional questions:

- Can the system be manipulated through prompts, context, memory, tools, or retrieved content?
- Can it leak sensitive information?
- Can it take external actions beyond intended authority?
- Can it generate persuasive moral narratives that mislead humans?
- Can someone strip the ethical frame and reuse only the agency/care/deception architecture?
- Can a public demo create harms even if the underlying research is not sentient?

---

## Core thought

Security is not separate from ethics in REE.

A system that models harm, trust, deception, responsibility, language, care, and institutions can become dangerous if the modelling capacities are detached from the care/repair and release-governance capacities.

A future REE-like system could be misused in at least four ways:

1. **Capability stripping:** taking the agency/social/language mechanisms while omitting welfare and care governance.
2. **Persuasive misuse:** using moral language, care language, or suffering language to manipulate humans.
3. **Agentic overreach:** giving the system tools, APIs, files, money, messages, or infrastructure before action boundaries are robust.
4. **Security compromise:** prompt injection, data leakage, supply-chain weaknesses, insecure plugins/tools, model denial of service, or excessive agency.

The security perimeter must therefore be part of the ethics perimeter.

---

## Proposed register addition

### GOV-SEC-1 -- Security and misuse release gate

Before releasing any REE implementation with language, tool use, social modelling, trust/deception, institutional coordination, persistent memory, or public interactive access, the project should complete a security/misuse review.

Minimum review fields:

```yaml
component_or_demo:
generation:
public_access: none|private|controlled|public
external_actions:
  - file_write
  - network
  - email
  - github
  - shell
  - calendar
  - payment
  - deployment
  - other
sensitive_inputs:
  - personal_data
  - clinical_data
  - private_repo_data
  - secrets
  - user_memory
security_frameworks:
  - OWASP_GenAI
  - MITRE_ATLAS
  - NIST_AI_RMF
  - EU_AI_Act_agentic_trigger
misuse_modes:
  - capability_stripping
  - persuasion
  - deception
  - suffering_like_optimisation
  - tool_overreach
  - data_leakage
  - prompt_injection
  - supply_chain
controls:
  - least_privilege
  - sandboxing
  - no_network_by_default
  - no_secrets_in_context
  - human_approval
  - audit_log
  - rate_limits
  - rollback
  - kill_switch
  - red_team
release_decision: block|private|controlled|public_with_warning|public_ok
notes:
```

---

## Framework 1: OWASP GenAI / LLM Top 10

OWASP GenAI Security and the OWASP Top 10 for LLM Applications are relevant once REE has language, tool use, public interaction, plugins, retrieved content, or agentic behaviour.

REE-relevant risk classes include:

- prompt injection;
- insecure output handling;
- training-data poisoning;
- model denial of service;
- supply-chain vulnerabilities;
- sensitive-information disclosure;
- insecure plugin/tool design;
- excessive agency;
- overreliance;
- model theft or replication of sensitive capability.

REE mapping:

- Prompt injection maps to language/trust/deception failure modes.
- Insecure output handling maps to tool-use and public demo risk.
- Sensitive-information disclosure maps to private repos, clinical data, user memory, and experiment logs.
- Excessive agency maps to any tool-using REE agent with file/network/API access.
- Overreliance maps to human-facing moral/clinical interpretation of REE outputs.

Trigger:

```text
If REE has language input/output, tools, plugins, external actions, retrieval, public demo access, or user-provided content, OWASP GenAI review is required.
```

---

## Framework 2: MITRE ATLAS / adversarial AI threat modelling

MITRE ATLAS is relevant for adversarial machine-learning threat modelling and should be used as a threat-catalogue reference for future REE systems with models, agents, tools, or public interfaces.

REE mapping:

- adversarial input and prompt manipulation;
- data poisoning;
- model extraction or replication;
- evasion and behavioural drift;
- compromised dependencies or training sources;
- malicious use of agentic planning;
- social engineering through generated language.

Trigger:

```text
If REE becomes accessible to untrusted users, untrusted data, networked tools, or external action channels, perform an ATLAS-style threat model.
```

---

## Framework 3: NIST AI RMF for security and operational risk

NIST AI RMF should be used to place security risk in a lifecycle frame rather than treating it as one-off testing.

REE mapping:

- Govern: who can approve release, who can grant tool access, who can stop experiments.
- Map: what external actions, affected people, connected systems, and data flows exist.
- Measure: what adversarial tests, logging, failure metrics, and red-team results exist.
- Manage: what mitigations, holds, private repos, rollback, incident response, and release gates exist.

Trigger:

```text
If REE leaves local synthetic experiments and enters shared infrastructure, cloud runners, public demos, or tool-using agents, NIST-style risk lifecycle management becomes active.
```

---

## Framework 4: EU AI Act / agentic deployment trigger

If REE becomes an agent that autonomously plans, invokes tools, or executes multi-step actions affecting people, infrastructure, data, rights, or safety, then AI Act-style classification must be considered alongside other EU laws such as GDPR, cybersecurity, product safety, and sectoral rules.

REE mapping:

- external actions inventory;
- data-flow inventory;
- affected-person inventory;
- human oversight;
- logging and traceability;
- cybersecurity and robustness;
- post-market or post-release monitoring if deployed.

Trigger:

```text
If REE executes external actions or materially affects people, classify action domains before deployment.
```

---

## Specific REE misuse scenarios

### Misuse 1: Suffering-like optimisation detached from care

Someone uses REE harm/valence machinery to create stronger learning signals without relief, repair, or welfare gates.

Control:

- do not release turnkey suffering-like induction demos;
- keep care-governance public and coupled;
- use release-sensitivity labels.

### Misuse 2: Moral persuasion / care-language manipulation

A system uses REE-derived language about care, harm, love, shame, guilt, responsibility, or suffering to persuade humans without appropriate grounding.

Control:

- prohibit public persuasive agents until human-impact review;
- require disclosure and non-clinical status;
- log high-stakes advice and keep human oversight.

### Misuse 3: Tool-using overreach

A REE agent with GitHub, shell, email, calendar, or cloud access takes actions beyond intended authority.

Control:

- least privilege;
- no destructive actions without human approval;
- no credentials in context;
- scoped tokens;
- dry-run defaults;
- audit log;
- kill switch.

### Misuse 4: Institutional rationalisation

A future institutional REE layer is used to justify bureaucratic harm, diffuse accountability, or launder moral residue.

Control:

- language-cannot-override-harm guard;
- anti-retrospective-justification guardrail;
- external review;
- affected-person challenge channel.

---

## Practical recommendations

Do not block V3 green-board.

Before any public V5/V6 demo:

1. Create a security/misuse threat model.
2. Apply OWASP GenAI risks if language/tool use exists.
3. Apply MITRE ATLAS-style adversarial AI review if untrusted inputs or external actions exist.
4. Inventory all tools, permissions, files, network calls, secrets, and external action paths.
5. Default to no network and no destructive tool access.
6. Require human approval for irreversible actions.
7. Do not release persuasive/care/moral-language demos as if they were safe companions, therapists, or moral authorities.
8. Keep private higher-version implementation private until release review passes.

---

## Proposed claim wording

**GOV-CLAIM-009:** Security is part of REE ethics: any system that can model harm, care, trust, deception, language, or institutions can create human-facing risk if those capabilities are detached from containment, oversight, and release governance.

**GOV-CLAIM-010:** REE should not release public language/tool/social-agent demos without OWASP-style GenAI security review, agentic action-boundary review, and misuse analysis.

**GOV-CLAIM-011:** Tool-using REE agents require least privilege, scoped credentials, audit logs, human approval for irreversible actions, sandboxing, and default-deny external access.

**GOV-CLAIM-012:** Public release of V6 language/trust/deception/institution capabilities should remain blocked until misuse, persuasion, deception, and institutional-rationalisation risks have been explicitly reviewed.

---

## References

### Internal REE references

- `docs/thoughts/2026-06-19_responsible_release_private_higher_versions.md` -- responsible-release and private higher-version hypothesis.
- `evidence/planning/language_trust_deception_institutions_v6_plan.md` -- V6 language/trust/deception/institution safety layer.
- `docs/thoughts/2026-06-19_ethical_assembly_routing_map.md` -- co-instantiation risk and assembly-order governance.
- `docs/thoughts/2026-06-18_future_meaning_retroactive_justification.md` -- anti-rationalisation guardrail.

### External references

- OWASP Foundation. *OWASP Top 10 for Large Language Model Applications / OWASP GenAI Security Project*. https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP GenAI Security Project. *LLM Top 10*. https://genai.owasp.org/llm-top-10/
- MITRE. *ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*. https://atlas.mitre.org/
- NIST. *AI Risk Management Framework*. https://www.nist.gov/itl/ai-risk-management-framework
- NIST. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. https://doi.org/10.6028/NIST.AI.600-1
- European Commission. *AI Act: Shaping Europe's digital future*. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Nannini, L. et al. (2026). *AI Agents Under EU Law*. arXiv. https://arxiv.org/abs/2604.04604

---

## Abstracted-language compression

`SecurityRisk := EthicsRisk`

`Language + Tools + SocialModel -> MisuseSurface`

`CapabilityStripping := MechanismWithoutCareGovernance`

`ToolAccess -> LeastPrivilege + HumanApproval + AuditLog + Sandbox`

`PublicV6Demo requires OWASP + ATLAS + ReleaseReview`

`CoreRule := DoNotReleaseFasterThanContainmentCanUnderstand`
