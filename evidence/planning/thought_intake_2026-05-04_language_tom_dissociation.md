# Thought intake: language and theory-of-mind as early-separable specialist systems

**Date:** 2026-05-04 (raw); intake written 2026-06-05
**Status:** intake / candidate architectural constraint (NOT yet registered). Later-version
consideration; explicitly NOT a blocker for current non-social V3 work.
**Raw thought file:** `docs/thoughts/2026-05-04_Theory_of_mind_v_language.md`
**Origin:** 2026 Communications Biology study (children 3-9 + adults, fMRI + connectivity) --
language and theory-of-mind regions are already functionally/spatially distinct by age 3, with
non-overlapping resting-state connectivity fingerprints; no evidence they start merged and split.
**Anchors:** ARC-009 / ARC-010 (language emergence, fast empathy), language architecture docs,
and the sibling thoughts `2026-04-16_language_lateralisation` / `2026-05-04_Empathy_development`.

---

## 1. Core idea

REE should be **one committed agent with multiple specialist modelling systems**, not a doubled
mind. Language and theory-of-mind / fast-empathy should be **partially homologous but
developmentally separate** specialist processors over a shared self/world/action core -- distinct
routing, input histories, representational pressures, and gating. Strong ethical corollary: a
fluent language system is NOT the ethical substrate; **fluent language can imitate concern while
lacking the other-model + affective-relevance architecture needed for caring commitment.**

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Language as a specialist system over shared substrate | **Yes** -- ARC-009/ARC-010, language docs | Confirms |
| Fast empathy / other-modelling as distinct from language | **Partial** -- implied across empathy claims; the 2026-04-16 lateralisation thought argues the routing split | **Extension** -- this adds the *developmental* evidence (distinct from age 3, not later-disentangling) |
| **"Behaviourally integrated but architecturally separable"** as a design constraint | **No explicit claim** | **NOVEL** -- the registerable constraint |
| **Preserve agent unity** -- specialist systems, NOT duplicate agents (anti-fragmentation) | **No** | **NOVEL + safety-relevant** (avoids internal multi-agent fragmentation) |
| Fluent-language != ethical-substrate (fluency can mask immature fast empathy) | **No** | **NOVEL** -- important alignment-relevant claim |

**Verdict: a genuine architectural constraint**, with strong developmental-neuroscience support
but architectural extrapolation (the thought is honest about this: epistemic conf 0.68). It is
the *constraint* half of the same cluster whose *content* half is the fast-empathy stream-binding
intake.

## 3. Candidate claims

**REGISTERED 2026-08-07 -- ARC-123, INV-097, MECH-486, Q-091** (this intake was a genuine
3-month orphan: nothing in `claims.yaml` or any plan doc covered it, unlike its cluster siblings).
Placeholder-free mapping, in the order below:

| candidate | registered as |
|---|---|
| **ARC (language-tom-architecturally-separable)** | **ARC-123** `language.tom_architecturally_separable` |
| **INV (preserve-agent-unity)** | **INV-097** `architecture.agent_unity_not_duplication` (`invariant_type: universal`) |
| **MECH (interference-avoidance)** | **MECH-486** `language.tom_representational_interference` |
| **Q (fluency-masks-empathy)** | **Q-091** `language.fluency_masks_empathy` |

All four `status: candidate` / `epistemic_category: substrate_conditional` /
`implementation_phase: v4` / `version_relevance: v4_v5`, each carrying **DO NOT BUILD in V3** --
which preserves this intake's own scoping (section 5: V4-scope, explicitly not a V3 blocker).
Checked for prior ownership before registering: ARC-009/ARC-010 (language layer, mirror
modelling), ARC-094/MECH-405/MECH-408 (the fast-empathy stream-binding cluster, i.e. this
cluster's *content* half), INV-003/INV-007 (language emerges; language cannot override harm
sensing) -- all cross-referenced via `depends_on`, none of them covering the separability
constraint, the unity prohibition, the interference mechanism, or the fluency-masking question.
MECH-486 is the falsifiable member: ARC-123 and INV-097 are commitments, and if the interference
hypothesis comes back negative the architectural argument rests on the developmental evidence
alone.

**Still open, noticed while registering this file (NOT actioned here):** the routing/lateralisation
sibling `thought_intake_2026-04-16_language_lateralisation.md` has the same shape of gap -- its
"Candidate ARC (language.routing_vs_affect_separation)" and "Candidate MECH
(affect.bilateral_right_biased_coupling)" are prose-only and unregistered -- but
`thought_intake_audit.py` classifies that file `all_registered` because its candidate section
incidentally mentions the already-existing ARC-009. That is a real (narrow) blind spot in the
audit: an incidentally-cited existing id masks unregistered siblings in the same section.

- **ARC (language-tom-architecturally-separable)** -- in later REE, language and fast-empathy/ToM
  are implemented as partially-homologous but developmentally-separate specialist systems sharing
  the self/world/action core, with distinct connectivity / training / gating. *[novel]*
- **INV (preserve-agent-unity)** -- REE must not duplicate the whole agent to model language and
  social cognition; one agentic commitment architecture, multiple specialist modellers. *[novel;
  anti-fragmentation safety invariant]*
- **MECH (interference-avoidance)** -- language (discrete/reportable/sequential) and fast empathy
  (graded/affective/resonant) have conflicting representational pressures that degrade each other
  if forced into one workspace too early. *[novel; lit-anchored]*
- **Q (fluency-masks-empathy)** -- how should REE prevent fluent language from masking immature or
  absent fast-empathy development? *[open; alignment-relevant]*

## 4. Affected existing claims / docs

- ARC-009 / ARC-010, language architecture docs.
- Cluster siblings: `2026-04-16_language_lateralisation` (the routing/lateralisation half),
  `2026-05-04_Empathy_development` (the stream-binding content half). These three are ONE cluster.

## 5. Next steps (gated)

1. **Process as a cluster** with the two siblings (single governance pass; the three together
   make the "separable social/language specialist systems" argument from connectivity,
   lateralisation, and stream-binding angles).
2. V4-scope -- explicitly not a V3 blocker. The thought's own guidance: keep the core agent
   unified now, avoid prematurely merging language-report with future fast-empathy systems.
3. The "fluency != ethics" claim is alignment-relevant enough to flag for early registration even
   while the rest waits for the social substrate.

## 6. Cross-references

- Raw: `docs/thoughts/2026-05-04_Theory_of_mind_v_language.md` (Communications Biology 2026).
- Claims: ARC-009, ARC-010.
- Cluster: `2026-04-16_language_lateralisation`, `2026-05-04_Empathy_development`.
