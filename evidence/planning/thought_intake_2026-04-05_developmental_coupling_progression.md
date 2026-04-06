# Thought Intake: Developmental Coupling Progression -- Innate Signals to Language

**Date:** 2026-04-05
**Session type:** Design conversation (Claude Code)
**Extends:** `evidence/planning/thought_intake_2026-04-06_steve_signal_legibility_language_bootstrap.md` (ARC-048 language bootstrap), `evidence/planning/thought_intake_2026-04-05_steve_dog_emotional_mirroring.md` (MECH-182/183 signal legibility)
**Output:** Thought intake only. No claims registered this session.

---

## Prompt

Daniel's observation (verbatim):

> So in infancy social coupling signals are innate. Caregivers are competent and coupling is
> successful in meeting infants needs. Infant bonds and thrives. Then perhaps in toddler stage the
> child learns and trusts social coupling signals from caregiver. These become solidified when
> learning window closes. Then childhood phases begin and learning through play and language
> development can proceed with social coupling signals enabling social passing of knowledge and play.

Context: Daniel is working out what must be needed for REE to actually work, including the last
planned phase of language acquisition. This is about the developmental curriculum a full REE agent
would need to traverse.

---

## What's New vs. Existing REE Docs

| Topic | Status |
|-------|--------|
| Stereotyped signal repertoire (MECH-191) | Already covered |
| Signal legibility prerequisite (MECH-192) | Already covered |
| Social reward reinforcement loop (MECH-193) | Already covered |
| Language as high-bandwidth externalization (ARC-048) | Already covered |
| **Strict developmental phase ordering: coupling must consolidate before play/language** | **NEW** |
| **Sensitive period in social coupling -- plasticity narrows after consolidation** | **NEW** |
| **Phase 2 consolidation as obligate process (closes around whatever pattern exists, adaptive or not)** | **NEW** |
| **Play requires coupling consolidation as prerequisite (not concurrent)** | **NEW** |
| **Language acquisition requires trusted coupling channel as prerequisite** | **NEW** |
| **Two distinct consolidation candidates: signal repertoire vs. trust calibration** | **NEW -- open question for literature** |

---

## The Four-Phase Progression

### Phase 1: Infancy -- Innate coupling, external regulation

The agent arrives with hardwired social coupling signals (cry-comfort, face orientation, neonatal
imitation). It does not model the caregiver -- it emits signals and receives regulation. The
caregiver IS the harm-avoidance system at this stage. This is E1-level: sensory prediction,
distress signals, comfort receipt. No planning, no self-model needed.

### Phase 2: Toddlerhood -- Coupling consolidation (sensitive period)

The agent builds an internal model of the caregiver as reliable co-regulator. Coupling signals
shift from reflexive to trusted. A sensitive period narrows -- after consolidation, social coupling
becomes a background assumption rather than something requiring ongoing verification. This frees
cognitive capacity for downstream phases.

**Critical property:** Consolidation is obligate. The window narrows regardless of whether coupling
was successful. Neglect, inconsistency, or abuse produce avoidant, anxious, or disorganized
attachment patterns -- the mechanism still consolidates, but around a maladaptive prior. This means
the consolidation mechanism is not contingent on success; it is a developmental clock.

**Open question (two candidates for what narrows):**
1. Signal repertoire -- which social signals the agent responds to
2. Trust calibration -- how much weight the agent assigns to social coupling signals

Both are plausible. If both narrow, they may do so on different timescales. Literature pull needed.

### Phase 3: Childhood -- Play and exploration

With coupling consolidated as a background assumption, the agent can explore freely. Play tests
action-outcome contingencies without catastrophic consequences. The trusted coupling channel
provides the safety net -- the agent can take risks because the co-regulatory relationship is
load-bearing.

**Key dependency:** Play MUST come after coupling consolidation, not concurrent with it. The agent
cannot explore freely while still uncertain whether the safety net is reliable. Consolidation
converts coupling from "maybe reliable" to "background assumption," freeing resources for
exploration.

### Phase 4: Language acquisition

Language adds bandwidth and resolution to a channel that already exists (ARC-048). Pre-linguistic:
yelp -> "I hurt." Linguistic: "My leg hurts when I walk on wet grass." Same referent architecture,
higher resolution.

**Key dependencies:**
- Requires Phase 2 (trusted coupling channel) -- language is received from trusted caregivers. An
  agent without consolidated coupling has no basis for treating linguistic input as reliable signal
  rather than noise.
- Requires Phase 3 (play-derived action-outcome repertoire) -- linguistic labels attach to
  experiential referents built during play. Without the referent repertoire, language is ungrounded
  symbols.

Language transforms the architecture: the agent can receive compressed models of situations never
encountered, reason about counterfactuals verbally, and participate in normative discourse. Ethical
reasoning becomes linguistic, not just embodied.

---

## Architectural Implications for REE

1. **Strict ordering constraint on training curriculum.** Each phase depends on the prior completing.
   You cannot shortcut Phase 2 -> Phase 4; the dependencies are load-bearing, not pedagogical.

2. **Phase 2 is architecturally special.** It is the only phase where a learning window must narrow
   for the system to progress. The others are additive (new capabilities stacked on existing ones);
   Phase 2 is consolidative (plasticity reduction in a specific pathway).

3. **The failure mode is informative for design.** If Phase 2 consolidation fails (couples around
   maladaptive prior), all downstream phases are compromised: play becomes unsafe (no reliable
   safety net), language becomes untrustable (no reliable signal source). This maps to attachment
   disruption pathways in developmental psychopathology.

4. **Caregiver competence is a design requirement, not an assumption.** Phase 1 assumes the
   training environment provides appropriate regulatory responses. This is a constraint on
   environment/curriculum design -- the "caregiver" must be competent for the progression to work.

---

## Affected Existing Claims

| Claim ID | Title (short) | Relation |
|----------|---------------|----------|
| ARC-048 | Language as high-bandwidth externalization | This intake specifies the developmental prerequisites for ARC-048 to be achievable |
| MECH-191 | Stereotyped signals as causal externalizations | Phase 1 innate signals are the starting repertoire |
| MECH-192 | Signal legibility prerequisite | Phase 2 consolidation determines whether legibility produces coordination |
| MECH-193 | Social reward reinforces coupling | Self-strengthening loop operates during Phase 2 consolidation |
| INV-057 | Cross-species legibility = functional specificity | Phase 1 innate signals ground this invariant |

No conflicts with existing claims. The progression provides ordering and dependency structure
over mechanisms already registered.

---

## Candidate Claims (NOT registered -- for future session)

### INV-0xx: Developmental ordering constraint

Social coupling consolidation must precede exploratory play, and play must precede language
acquisition. Each phase depends on the prior completing. The ordering is structural (load-bearing
dependencies), not merely pedagogical.

### MECH-1xx: Sensitive period narrows social coupling plasticity

A sensitive period in social coupling reduces plasticity after consolidation. The consolidation is
obligate -- it occurs regardless of coupling quality, closing around whatever pattern exists
(adaptive or maladaptive). Open question: does the signal repertoire narrow, the trust calibration
narrow, or both?

### ARC-0xx: REE training curriculum must implement sequential developmental phases

The REE training curriculum must implement four sequential phases: (1) innate coupling with
competent environment, (2) coupling consolidation with plasticity reduction, (3) play/exploration
with consolidated safety net, (4) language acquisition over trusted channel. Skipping or
reordering phases produces an agent with compromised social and ethical capabilities.

---

## Next Steps

1. Register candidate claims in `docs/claims/claims.yaml` (future session)
2. Literature pull: attachment sensitive periods -- what specifically consolidates and on what timescale
3. Literature pull: play as dependent on secure attachment (Bowlby/Ainsworth secure base literature)
4. Architecture doc: developmental curriculum design for REE training phases
5. Connect to existing `social.md` and ARC-048 architecture stubs
