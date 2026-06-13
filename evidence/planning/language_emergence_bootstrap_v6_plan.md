---
closure_plan:
  id: language_emergence_bootstrap_v6
  generation: v6
  title: "Language emergence + bootstrap from social ecology (V6 LINGUISTIC umbrella)"
  registered: 2026-06-10
  last_updated: 2026-06-13
  scope_claims: [ARC-009, INV-003, INV-007, MECH-010, MECH-014, MECH-308]
  sibling_plans: [grammar_primitive_mining_v6, language_affect_adaptor_v6, multi_agent_ecology_v5, mirror_modelling_other_self_v5, fast_empathy_v5, ethics_as_coherence_v5, object_representation_v4, self_model_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V6 (the LINGUISTIC mind tier, final tier
    of the V4-individual / V5-social / V6-linguistic partition) has no experiments
    yet, so nodes carry no owner_exq and the drift checker stays dormant against
    them. Each node's readiness_gate lists the prerequisites that must land first
    -- and for V6 the gate is the WHOLE V5 social tier (multi_agent_ecology_v5,
    mirror_modelling_other_self_v5, fast_empathy_v5, ethics_as_coherence_v5) plus
    the V4 object/self substrate (object_representation_v4, self_model_v4) plus the
    shared MECH-163 multi-step hippocampal planning gate. The spine is ARC-059 /
    DEV-NEED-021: self -> objects -> OTHERS -> LANGUAGE. Language is the LAST stage:
    it PRESUPPOSES the social substrate (joint attention / OTHER_SELFLIKE
    detection, other-modelling) and the object/self substrate (object tokens,
    self-attribution). The bootstrap hypothesis is explicit that proto-language
    only stabilises AFTER the pre-linguistic primitives (object/action/self/other/
    rule) exist and are grounded; this plan therefore gates every node behind the
    social and individual tiers. generation: v6 keeps these nodes OUT of the V3
    closure percentage (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). This is the UMBRELLA + BOOTSTRAP
    area of the linguistic tier: it owns the emergence sequence and the enabling
    conditions; the grammar/primitive-mining scaffold and the language-affect adaptor
    are sibling V6 plans that consume the proto-signals this plan predicts will
    emerge. A node graduates from roadmap to closure-tracked by gaining an owner_exq
    once its first V6 experiment is queued.
  nodes:
    - id: "language_emergence_bootstrap_v6:LANG-1"
      title: "Bootstrap-not-bolt-on architectural commitment (the load-bearing spine: language emerges from social ecology, is never imported)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-003, ARC-009]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "No substrate prerequisite -- this is a DESIGN COMMITMENT, the spine of the whole plan, already carried by ACTIVE claims INV-003 (language emerges as functional self-representation, not a bolt-on) + ARC-009 (language is an emergent coordination/compression layer, NOT a value source / rule system / optimiser)"
        - "Positive form: language MUST emerge from making communication the cheapest way for already-social organisms to coordinate attention/action/warning/request/help/refusal/teaching; it is never a separate module bolted onto cognition (the engine is the social ecology; the grammar/LLM scaffold is a turbocharger -- grammar_primitive_mining_v6)"
        - "Prohibition the commitment implies: do NOT import transformer attention or LLM architecture into REE because language is useful; do NOT reward arbitrary bitstrings unless grounded, reusable, action-relevant (docs/architecture/language.md ARC-009; docs/thoughts/2026-06-05 cautions)"
      last_updated: 2026-06-13
      completion_note: "ARC-009 + INV-003 are ACTIVE established design (NOT reassignment candidates). This node restates them as the V6 spine: every node below is a specialisation of 'language is grounded emergent coordination, not bolted-on syntax'. It is the linguistic-tier analogue of fast_empathy_v5's no-empathy-scalar prohibition -- an architectural commitment about HOW language must arise, testable as a negative (any design that bolts a language module on, or imports LLM weights as the value layer, violates it). Reconciled 2026-06-13: claim(s) INV-003, ARC-009 registered in claims.yaml; this design commitment/prohibition is the deliverable and is landed -- downstream nodes remain blocked on their substrate."
    - id: "language_emergence_bootstrap_v6:LANG-2"
      title: "Enabling-conditions register: the pre-linguistic substrate inventory communication needs before it can bootstrap"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-099"]
      depends_on: ["language_emergence_bootstrap_v6:LANG-1"]
      cross_plan_link: ["object_representation_v4:OBJ-2", "self_model_v4", "mirror_modelling_other_self_v5:MIRROR-1", "multi_agent_ecology_v5:MAE-1"]
      readiness_gate:
        - "Documents (does NOT yet build) the enabling-condition checklist from the 2026-06-05 addendum: shared world, object tokens, action affordances, self-attribution, other-attribution, joint attention, partial observability, social coordination pressure, memory, rule apprehension, low-cost signalling channel, partner variation, repair"
        - "Each condition maps to a prerequisite tier: object tokens -> object_representation_v4 (OBJ-2 permanence); self-attribution -> self_model_v4; other-attribution + joint attention -> mirror_modelling_other_self_v5 (MIRROR-1 OTHER_SELFLIKE); coordination pressure + partial observability + partner variation -> multi_agent_ecology_v5 (MAE-1 substrate)"
        - "No substrate gate of its own -- this is a documentation+claim step that gives LANG-3..LANG-6 a checklist of what must be TRUE of the ecology before any signalling probe is non-vacuous; it is the V6 entry-readiness contract"
      last_updated: 2026-06-10
      completion_note: "The bootstrap addendum's central engineering content: language does NOT bootstrap from undifferentiated affective noise (emergence_and_bootstrapping.md) -- it needs a specific inventory of grounded pre-linguistic systems first. Registering the inventory as a claim makes the V6-entry gate machine-checkable: before any LANG-3 minimal-channel experiment is queued, every enabling condition must be satisfied by a landed V4/V5 node. Builds on MECH-010 (the abstract five-step bootstrap sequence); this sharpens MECH-010's preconditions into a falsifiable readiness contract."
    - id: "language_emergence_bootstrap_v6:LANG-3"
      title: "Minimal signalling channel: smallest signal that lets one agent alter another's attention or action (MECH-014)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-014]
      depends_on: ["language_emergence_bootstrap_v6:LANG-2"]
      cross_plan_link: ["multi_agent_ecology_v5:MAE-2", "mirror_modelling_other_self_v5:MIRROR-1"]
      blocking_on: "Requires a multi-agent substrate where agents perceive and act on each other (multi_agent_ecology_v5:MAE-1/MAE-2) AND a stable other-model that can be addressed (mirror_modelling_other_self_v5:MIRROR-1 OTHER_SELFLIKE), itself gated on MECH-163 + the V4 object/self substrate. No second agent to signal to until the V5 social tier lands."
      readiness_gate:
        - "MECH-014 (minimal signalling channel) is the existing seed: a low-cost interface exporting internal summaries (harm/degradation alerts, intent/commitment markers, uncertainty markers, stop/avoid priors) that other agents condition on, trust-weighted, unable to mask the receiver's embodied harm channels"
        - "V5 multi-agent substrate present: per-agent observation + the channel availability (multi_agent_ecology_v5:MAE-2) so there is a partner whose attention/action a signal could change"
        - "Candidate primitive signal set from the addendum (look / stop / go / danger / resource / here / there / help / wait / done): these are FUNCTION handles, not a frozen vocabulary; the probe asks whether ANY signal stabilises because it improves coordination, not whether it matches a human word"
      last_updated: 2026-06-10
      completion_note: "The first real linguistic-tier substrate step: instantiate MECH-014's pre-language interface inside the V5 ecology and test whether a minimal channel is USED. INV-007 (language cannot override embodied harm sensing) is a hard constraint on this channel from day one -- a signal MUST NOT be able to mask the receiver's harm sensing. Design-only today; gated on the V5 social substrate existing at all."
    - id: "language_emergence_bootstrap_v6:LANG-4"
      title: "Joint-attention coordination games: signalling emerges under partial observability + coordination pressure (the emergence driver)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-010, "ARC-099"]
      depends_on: ["language_emergence_bootstrap_v6:LANG-3"]
      cross_plan_link: ["mirror_modelling_other_self_v5:MIRROR-1", "multi_agent_ecology_v5:MAE-6"]
      blocking_on: "Needs the minimal channel (LANG-3) plus joint attention (mirror_modelling_other_self_v5:MIRROR-1 establishes OTHER_SELFLIKE; the joint-attention frame is its immediate consequence) and an information asymmetry (multi_agent_ecology_v5 partial-observability task design). All V5-or-later."
      readiness_gate:
        - "LANG-3 minimal channel in place (the thing whose use the games measure)"
        - "Joint-attention machinery: two agents able to attend to the same object/event (mirror_modelling_other_self_v5:MIRROR-1 OTHER_SELFLIKE detection -- the immediate precursor flagged in emergence_and_bootstrapping.md: WORLD predictions improve by conditioning on what the other attends to, creating simulation overhead that pressures externalisation)"
        - "Experiment design (intake Line B): social tasks where one agent has information about an object/resource/hazard the other lacks; the falsifiable question is whether signalling EMERGES because it improves coordination -- not whether it is engineered in"
      last_updated: 2026-06-10
      completion_note: "The positive emergence mechanism LANG-1 demands: language arises as a COMPRESSION layer once mutual simulation becomes expensive (ARC-009 joint-attention-and-compression-pressure section). This is the first V6 experiment candidate (would gain an owner_exq once the V5 ecology + joint-attention substrate exists). Tests MECH-010's claim that signalling emerges under partial observability + coordination benefit, not by reward-shaping a fixed vocabulary."
    - id: "language_emergence_bootstrap_v6:LANG-5"
      title: "Signal-to-rule minting: repeated signal/action/outcome regularities become CandidateRuleField rules (ARC-063 bridge)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["ARC-063"]
      depends_on: ["language_emergence_bootstrap_v6:LANG-4"]
      cross_plan_link: ["grammar_primitive_mining_v6"]
      blocking_on: "Requires stable proto-signals to exist (LANG-4) and the CandidateRuleField rule-apprehension substrate (ARC-063) to ingest signal as part of a context. ARC-063 straddles V3 but its grounding is incomplete; signal-as-rule-context is a V6 extension on top of an emergent-signal substrate that does not exist."
      readiness_gate:
        - "LANG-4 has produced repeated, useful signals (the regularity to be minted)"
        - "ARC-063 CandidateRuleField present and ingesting context -> action-object -> outcome regularities; the V6 extension is admitting a SIGNAL as part of the context: 'when signal S occurs in context C, action A by agent B leads to outcome O' (intake Line C)"
        - "INV-007 guard: a minted signal-rule MUST NOT become a value source or override embodied harm -- a signal-conditioned rule is a coordination affordance, never an ethical authority (ARC-009 'language reshapes the space in which ethical selection occurs; it does not generate ethics')"
      last_updated: 2026-06-10
      completion_note: "The bridge from emergent signalling to durable structure: proto-signals that repeat usefully become candidate rules / social affordances / proto-constructions. This is where the grammar_primitive_mining_v6 sibling becomes a turbocharger -- once a signal-rule is minted it can be NAMED and queried via the grammar scaffold (predicate-argument-event shape). Stays subordinate to INV-007: minting a rule never elevates language above harm sensing."
    - id: "language_emergence_bootstrap_v6:LANG-6"
      title: "Convention robustness: partner variation + repair distinguish true convention from overfitted co-adaptation"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-010", "MECH-010"]
      depends_on: ["language_emergence_bootstrap_v6:LANG-4"]
      cross_plan_link: ["multi_agent_ecology_v5:MAE-1"]
      blocking_on: "Partner variation needs MULTIPLE distinct partners in the ecology (multi_agent_ecology_v5:MAE-1 multi-agent substrate); repair needs the head-tilt / failed-signal feedback channel, which presupposes the joint-attention substrate (LANG-4). Both V5-or-later."
      readiness_gate:
        - "LANG-4 emergent signals exist; the ecology contains MORE than one possible partner (multi_agent_ecology_v5:MAE-1) so a signal can be tested against a partner it was NOT co-trained with (intake Line D)"
        - "Partner-variation criterion: a signal is a true communicative CONVENTION (not overfitted co-adaptation) only if it remains useful with a different partner -- the falsifier for spurious two-agent collusion"
        - "Repair criterion (intake Line E): failed communication must be LEARNABLE, not terminal -- failed signals should lead to altered signalling / repetition / attention-calling / fallback, not collapse. The head-tilt-as-uncertainty primitive (emergence_and_bootstrapping.md basic-expression catalog) is the minimal repair-pressure feedback channel"
      last_updated: 2026-06-10
      completion_note: "Two falsifiers that keep the emergence claim honest: partner-variation guards against declaring a co-adapted private code 'language', and repair guards against treating one-shot signalling success as a stable convention. Both ride the basic-expression catalog (emergence_and_bootstrapping.md): head-tilt for repair-pressure, mutual gaze for joint-attention re-establishment. Proposed as two separable candidate mechanisms (robustness + repair) because they fail independently."
    - id: "language_emergence_bootstrap_v6:LANG-7"
      title: "Language-as-play-game substrate reuse: the bootstrap runs inside play_mode, not a parallel language-acquisition module (MECH-308)"
      phase: 4
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-308]
      depends_on: ["language_emergence_bootstrap_v6:LANG-4"]
      cross_plan_link: []
      blocking_on: "MECH-308 runs the language game inside play_mode (INV-058 / MECH-194 / ARC-049), which is itself unimplemented in V3 (play_mode cluster is substrate-blocked -- no play_frame_tag, no synthetic-signal seeding). Cannot test play-mode-as-language-host until BOTH play_mode and the emergent-signalling substrate (LANG-4) exist."
      readiness_gate:
        - "MECH-308 is the existing seed (language acquisition tracks play_mode maturation; the basic-expression catalog is the bilateral frame-opening signal; conversational violations = synthetic z_harm; utterance-as-goal = synthetic z_goal; proto-symbols accrete as conditional modifiers)"
        - "play_mode substrate present (INV-058 / MECH-194 / ARC-049 / play_frame_tag) -- currently substrate-blocked per the play-mode cluster; this node inherits that block"
        - "Falsifiable prediction (emergence_and_bootstrapping.md): systems trained WITHOUT play_mode-like episodes fail to acquire socially-grounded compositional language even when pattern-matching imitation succeeds; loss-of-language under stress/fatigue should track loss-of-play-mode-availability, not selective module damage"
      last_updated: 2026-06-10
      completion_note: "The architectural payoff that avoids a separate language-acquisition module: if language is a specialised play game, REE needs only (a) the basic-expression catalog wired into play-mode frame opening, (b) play_mode, (c) a path for proto-symbols to accrete onto basic expressions as conditional modifiers. MECH-308 stays implementation_phase v3/v3_pending in claims.yaml (NOT reassigned here -- it is anchored to the play-mode substrate question, not flagged); this node tracks its V6 language-game cutover once both substrates land."
    - id: "language_emergence_bootstrap_v6:LANG-8"
      title: "Biology grounding for language emergence + the bootstrap enabling-conditions (lit-pull)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["ARC-099", "MECH-014"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: the NEW enabling-conditions + minimal-channel + signal-to-rule claims need a language-emergence / signalling-systems lit-pull BEFORE registration beyond candidate"
        - "Seed anchors present in the docs: joint attention as immediate precursor (Tomasello-style shared-intentionality lineage implied); the basic-expression catalog (play bow, head tilt, laughter, mutual gaze, distress vocalisation, approach cue, vocal mimicry, pointing); cross-species negation primitive (Steve the dog, Spitz 1957 9-12mo demonstrative head-shake); event-segmentation + frame-semantics lineage (grammar_primitive_mining_v6 owns the grammar-side literature)"
        - "Targeted review to commission: experimental / iterated-learning models of signalling-system emergence (e.g. signalling games, iterated learning, emergent-communication RL); developmental joint-attention -> proto-declarative pointing -> proto-symbol sequence; partial-observability / coordination-pressure as the emergence driver"
      last_updated: 2026-06-10
      completion_note: "Grounding-debt tracker. ARC-009 / INV-003 / INV-007 are established and carry their own legacy sources; the NEW enabling-conditions and minimal-channel claims this plan proposes do not yet have a dedicated language-emergence lit-pull. Deferred (not blocked) because it can begin independently of the substrate, but it is a registration gate for the LANG-2 / LANG-3 / LANG-5 / LANG-6 candidate claims' promotion beyond candidate."
---
# Language Emergence + Bootstrap from Social Ecology -- V6 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v6 (forward roadmap; LINGUISTIC mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** the UMBRELLA + BOOTSTRAP area of the linguistic tier. Sequence how
language EMERGES in REE -- from the architectural commitment that it is bootstrapped
not bolted on (ARC-009 / INV-003), through the enabling-conditions inventory the
social ecology must satisfy, the minimal signalling channel (MECH-014), the
joint-attention coordination games that drive emergence (MECH-010), signal-to-rule
minting (ARC-063 bridge), convention-robustness + repair falsifiers, and the
language-as-play-game substrate reuse (MECH-308) -- with biology grounding pinned as
a debt.

This is a **V6 (linguistic) tier** plan, the FINAL tier of the 3-tier partition
(V4 = individual mind, V5 = social, V6 = linguistic). The spine is **ARC-059 /
DEV-NEED-021**: self -> objects -> OTHERS -> **LANGUAGE**. Language is the last
stage: it PRESUPPOSES the V5 social substrate (joint attention / OTHER_SELFLIKE
detection, other-modelling, multi-agent coordination pressure) and the V4
object/self substrate (object tokens, object permanence, self-attribution). The
bootstrap hypothesis is explicit (docs/thoughts/2026-06-05) that proto-language
only stabilises AFTER the pre-linguistic primitives -- object/action/self/other/
rule -- exist and are grounded. Every node here is therefore gated behind the V5
social tier (multi_agent_ecology_v5, mirror_modelling_other_self_v5), the V4
individual tier (object_representation_v4, self_model_v4), and the shared
**MECH-163** multi-step hippocampal planning V4-social entry gate. It is a *forward
roadmap*, not a closure map: V6 has no experiments yet, so nodes carry no
`owner_exq` and the drift checker stays dormant. The value here is the **readiness
gates** -- for each emergence step, exactly which social/individual prerequisites
must land before the V6 linguistic step is honest to build.

---

## One-line framing

> Language already exists in REE as a DESIGN (ARC-009 coordination/compression
> layer, INV-003 emerges-not-bolted-on, INV-007 cannot-override-harm, MECH-010
> bootstrap sequence, MECH-014 minimal channel, MECH-308 language-as-play-game).
> What is NOT done -- and must NOT be done by importing an LLM as the value layer --
> is the EMERGENCE: making communication the cheapest way for already-social
> organisms to coordinate, so proto-signals stabilise from a grounded ecology. The
> engine is the social ecology; grammar (grammar_primitive_mining_v6) is only the
> turbocharger that names, compresses, and recombines the signals once they begin
> to appear.

---

## The emergence stack (one commitment, one inventory, one channel, one driver)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| bootstrap-not-bolt-on (spine) | LANG-1 | ARC-009 / INV-003 (active) | V6 (registrable now) | none -- it is a design commitment |
| enabling-conditions inventory | LANG-2 | NEWCLAIM (architectural_commitment) | V6 (doc step) | maps each condition to a V4/V5 prerequisite tier |
| minimal signalling channel | LANG-3 | MECH-014 + NEWCLAIM (mechanism) | V6 (blocked) | V5 multi-agent substrate + a partner to signal to |
| joint-attention emergence games | LANG-4 | MECH-010 (the emergence driver) | V6 (blocked) | LANG-3 + joint attention (MIRROR-1) + info asymmetry |
| signal-to-rule minting | LANG-5 | NEWCLAIM (mechanism) | V6 (blocked) | LANG-4 stable signals + ARC-063 CandidateRuleField |
| convention robustness + repair | LANG-6 | NEWCLAIM x2 (mechanism) | V6 (blocked) | LANG-4 + multiple partners + repair feedback channel |
| language-as-play-game | LANG-7 | MECH-308 | V6 (blocked) | play_mode substrate (substrate-blocked) + LANG-4 |
| biology grounding | LANG-8 | (grounding debt) | cross-cutting | language-emergence / signalling-systems lit-pull |

---

## Why these are V6, not V5

The social substrate this plan consumes is genuinely V5 (multi-agent ecology,
joint attention, other-modelling, coordination pressure) and the object/self
substrate is V4. But the SUBJECT of every node here is intrinsically LINGUISTIC --
the emergence, stabilisation, and rule-minting of communicative SIGNALS over a
social ecology. That places the language work itself in the V6 linguistic tier,
sitting on top of the V5 social and V4 individual substrate. The prerequisite chain
is explicit in each readiness_gate; the work is V6. Language is the developmental
capstone of the ARC-059 spine, not a parallel track.

---

## What this plan deliberately does NOT do

- **Does NOT import an LLM as architecture or as a value layer.** That is the whole
  point (LANG-1 / ARC-009). Grammar and LLMs are MINES for primitive cuts
  (grammar_primitive_mining_v6), not the engine; the engine is the social ecology.
- **Does NOT pull anything into V3, V4, or V5.** Registering this roadmap changes no
  behaviour at any earlier tier. The first real signalling step (LANG-3) is gated
  on the V5 social substrate existing and is V6.
- **Does NOT queue the joint-attention emergence experiment.** It needs the V5
  multi-agent + joint-attention substrate that does not exist yet. LANG-4 carries
  the design; the owner_exq stays null until that substrate lands.
- **Does NOT re-litigate the social substrate itself.** Joint attention,
  OTHER_SELFLIKE detection, and the multi-agent ecology are owned by
  mirror_modelling_other_self_v5 and multi_agent_ecology_v5; this plan CONSUMES a
  social ecology and asks whether language emerges from it.
- **Does NOT own the grammar scaffold or the affect adaptor.** The
  grammar-to-substrate mining table + predicate-argument-event bridge is
  grammar_primitive_mining_v6; the language->affect input adaptor (MECH-373) is
  language_affect_adaptor_v6. This plan owns the EMERGENCE of the signals those
  siblings consume.

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/architecture/language.md | ARC-009 symbolic-mediation contract + joint-attention/compression pressure + the four core functions |
| docs/architecture/language/emergence_and_bootstrapping.md | MECH-010 five-step bootstrap sequence + the basic-expression catalog + language-as-play-game (MECH-308) + cross-species negation primitive |
| docs/architecture/language/minimal_signalling_channel.md | MECH-014 pre-language interface sketch + trust-weighting + harm-non-masking constraint |
| docs/thoughts/2026-06-05_Grammar_and_LLMS_as_V5_primitive-mining_scaffolds.md (addendum) | the language-bootstrap-from-ecology hypothesis: enabling conditions, signal-to-rule, partner variation, repair, Lines A-F |
| evidence/planning/thought_intake_2026-06-05_grammar_llms_v5_primitive_mining.md | the intake (mine-not-import; containment-only; twin of cross_version intake) |
| claims.yaml ARC-009 / INV-003 / INV-007 | the active language design (NOT flagged -- established) |
| claims.yaml MECH-010 / MECH-014 / MECH-308 | the bootstrap sequence / minimal channel / language-as-play-game seeds |
| claims.yaml ARC-059 / developmental_needs_register DEV-NEED-021 | the self -> objects -> others -> LANGUAGE maturational spine |
| claims.yaml MECH-163 | the V4-social entry gate (stays v3 -- NOT flagged) |

---

## Decision log

- **2026-06-10** -- Plan registered as the UMBRELLA + BOOTSTRAP area of the V6
  (linguistic tier) forward-roadmap, final tier of the V4/V5/V6 partition. Eight
  nodes: LANG-1 (bootstrap-not-bolt-on commitment, the spine, on active ARC-009 /
  INV-003), LANG-2 (enabling-conditions inventory), LANG-3 (minimal signalling
  channel, on MECH-014), LANG-4 (joint-attention emergence games, the driver, on
  MECH-010), LANG-5 (signal-to-rule minting, ARC-063 bridge), LANG-6 (convention
  robustness + repair), LANG-7 (language-as-play-game substrate reuse, on MECH-308),
  LANG-8 (biology grounding debt). All gated behind the V5 social tier
  (multi_agent_ecology_v5, mirror_modelling_other_self_v5) + V4 individual tier
  (object_representation_v4, self_model_v4) + MECH-163 per the ARC-059 / DEV-NEED-021
  spine. Five NEW candidate claims proposed (enabling-conditions inventory,
  minimal-channel mechanism, signal-to-rule minting, convention robustness, signal
  repair). `generation: v6` set so the V3 closure % is unaffected. No claims.yaml
  edits (orchestrator merges).
- **2026-06-10** -- Reassignment flags: NONE applied here. ARC-009 / INV-003 /
  INV-007 are ACTIVE established design and are deliberately NOT flagged. MECH-010 /
  MECH-014 / MECH-308 are candidate language seeds carried as scope claims; MECH-308
  stays anchored to the play-mode substrate question (implementation_phase v3 /
  v3_pending) and is NOT flagged. MECH-163 deliberately NOT flagged (V4-social entry
  gate, stays v3). The clearly-linguistic MECH-373 language-affect adaptor (currently
  implementation_phase v5) is owned by the sibling language_affect_adaptor_v6 plan,
  which carries its v5->v6 reassignment flag -- not duplicated here.
