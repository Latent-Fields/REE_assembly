---
closure_plan:
  id: abstract_relational_reasoning_v6
  generation: v6
  title: "Abstract / relational / compositional reasoning at symbolic scale"
  registered: 2026-06-10
  last_updated: 2026-06-13
  scope_claims: [ARC-009, INV-003, INV-007, ARC-063, MECH-011, MECH-299, MECH-300, SD-040]
  sibling_plans:
    - grammar_primitive_mining_v6
    - language_emergence_bootstrap_v6
    - object_reasoning_abstraction_v4
    - mirror_modelling_other_self_v5
    - multi_agent_ecology_v5
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V6 (the LINGUISTIC mind tier, the final
    tier of the V4-individual / V5-social / V6-linguistic partition) has no
    experiments yet, so nodes carry no owner_exq and the drift checker stays
    dormant against them. Each node's readiness_gate lists the prerequisites that
    must land first -- and for V6 those are almost entirely UPSTREAM PLANS: the
    V5 social plans (multi_agent_ecology_v5, mirror_modelling_other_self_v5),
    the V6 language-acquisition plans (language_emergence_bootstrap_v6,
    grammar_primitive_mining_v6), the V4 object/abstraction substrate
    (object_reasoning_abstraction_v4), and the shared V3-completion gate MECH-163
    (multi-step hippocampal planning, the V4-entry gate). The spine is ARC-059:
    self -> objects -> others -> LANGUAGE. Language PRESUPPOSES the V5 social
    substrate and the V4 object/self substrate; symbolic-scale reasoning
    PRESUPPOSES language. This plan is therefore the LATEST tier of all -- it
    sits on top of the entire stack. generation: v6 keeps these nodes OUT of the
    V3 closure percentage (serve.py read_closure, generate_closure_snapshot.py,
    and check_closure_drift.py are all generation-aware). The central distinction
    this plan defends: this is reasoning AT LINGUISTIC SCALE (recombination via
    named symbols and grammar), categorically DISTINCT from the V4
    object_reasoning_abstraction substrate-level abstraction (theta-packaged
    units, action chunks, options, type-instance matches). The V4 abstraction is
    the SUBSTRATE the symbols name; this V6 abstraction is the recombination the
    NAMING unlocks. A node graduates from roadmap to closure-tracked by gaining an
    owner_exq once its first V6 experiment is queued -- which cannot honestly
    happen until the whole linguistic stack below it exists.
  nodes:
    - id: "abstract_relational_reasoning_v6:ARR-1"
      title: "Two-levels-of-abstraction distinction (the load-bearing scoping claim)"
      phase: 1
      status: done
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-102"]
      depends_on: []
      cross_plan_link: ["object_reasoning_abstraction_v4"]
      readiness_gate:
        - "No substrate prerequisite -- this is a DESIGN/SCOPING claim, registrable now as the spine of the plan: REE has TWO distinct abstraction layers and they must not be conflated"
        - "SUBSTRATE-level abstraction (V4, owned by object_reasoning_abstraction_v4): theta-packaged units (MECH-299), cognitive-map traversal at the active abstraction level (MECH-300), type-encoder prototypes (SD-040), action chunks / options. This is abstraction the agent COMPUTES OVER but cannot yet NAME or recombine arbitrarily."
        - "SYMBOLIC-scale abstraction (V6, this plan): compositional generalisation, analogy, propositional/relational inference over NAMED primitives. The recombination operator is the grammar/symbol layer, not the substrate."
      last_updated: 2026-06-13
      completion_note: "The first thing this plan must assert: symbolic reasoning is NOT just more of the V4 substrate abstraction. ARC-009 already commits language as a 'symbolic mediation and coordination layer'; this claim names the consequent reasoning capacity (recombination over symbols) as a distinct level. Like ARC-080's type-vs-token fork for objects, this is the scoping decision every node below inherits. Cheapest node; registrable now as the documentation spine. Reconciled 2026-06-13: claim(s) ARC-102 registered in claims.yaml; this design commitment/prohibition is the deliverable and is landed -- downstream nodes remain blocked on their substrate."
    - id: "abstract_relational_reasoning_v6:ARR-2"
      title: "Compositional generalisation over named primitives (recombine grounded symbols to novel combinations)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-419"]
      depends_on: ["abstract_relational_reasoning_v6:ARR-1"]
      cross_plan_link:
        - "language_emergence_bootstrap_v6"
        - "grammar_primitive_mining_v6"
        - "object_reasoning_abstraction_v4"
      blocking_on: "Requires grounded named primitives to recombine: stable symbol<->substrate bindings (language_emergence_bootstrap_v6) over the V4 object/action/type substrate (object_reasoning_abstraction_v4 SD-040 type-encoder, MECH-299/300 cognitive maps). No symbols to recombine until the emergence + grammar-mining plans land their primitive cuts."
      readiness_gate:
        - "language_emergence_bootstrap_v6: stable proto-symbols grounded to pre-linguistic primitives (object/action/self/other/rule) -- the recombinands"
        - "grammar_primitive_mining_v6: the noun->object / verb->affordance / role->agent cuts that supply the slot structure recombination fills"
        - "object_reasoning_abstraction_v4 SD-040 + MECH-299/300: the V4 substrate vocabulary the symbols name (type-instance units, cognitive-map nodes) -- the GROUND of every recombinand"
        - "ARC-009 + INV-003: language as symbolic mediation; language emerges as functional self-representation (not bolt-on) -- compositionality must be grounded, not imposed"
      last_updated: 2026-06-10
      completion_note: "The core symbolic-scale capacity: having grounded 'apple', 'push', 'red', 'left-of', the agent generalises to 'push the red apple left' without ever having seen that exact combination -- the systematic recombination LLMs/grammar exhibit. Grounded in the grammar_llms_v5 intake's predicate-argument-event family: 'agent does action to object in context'. Per the intake's anti-import discipline, compositionality MUST be mined from grounded substrate, never imported as transformer attention. Design-only; gated on the whole emergence + grammar stack."
    - id: "abstract_relational_reasoning_v6:ARR-3"
      title: "Relational / propositional inference over named relations (transitivity, role-binding, relational chaining)"
      phase: 2
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-420"]
      depends_on: ["abstract_relational_reasoning_v6:ARR-1", "abstract_relational_reasoning_v6:ARR-2"]
      cross_plan_link:
        - "object_reasoning_abstraction_v4"
        - "mirror_modelling_other_self_v5"
      blocking_on: "Relational inference over symbols needs both the named relations (ARR-2 compositional substrate) and the V4 cognitive-map traversal it externalises (MECH-300 traversal at the active abstraction level). Relations involving OTHERS (A trusts B, B owes C) additionally need the V5 other-model (mirror_modelling_other_self_v5)."
      readiness_gate:
        - "ARR-2 compositional generalisation in place (named relations exist as recombinable symbols)"
        - "object_reasoning_abstraction_v4 MECH-300: cognitive-map traversal at the active abstraction level -- relational chaining (A>B, B>C => A>C) is theta-sequence traversal of a SYMBOLIC/type-graph map, the V6 expression of an existing V4 traversal primitive"
        - "mirror_modelling_other_self_v5: a stable other-model so relations whose arguments are AGENTS (social/propositional relations) are representable, not only object-object spatial relations"
        - "ARC-063 CandidateRuleField: the 'context -> action-object -> outcome' rule shape is the pre-linguistic substrate propositional inference names and chains (per the grammar_llms_v5 ARC-063 bridge)"
      last_updated: 2026-06-10
      completion_note: "Reasoning over relations AS named objects: transitive inference, role-binding ('the giver vs the receiver'), chaining propositions. The substrate is MECH-300 cognitive-map traversal -- relational inference is traversal of a SYMBOLIC map. This is where the V4 traversal primitive (MECH-300) gets a genuinely V6 realisation: the map nodes are now named symbols, not raw type-instances. Design-only; gated on ARR-2 + the V5 other-model for social relations."
    - id: "abstract_relational_reasoning_v6:ARR-4"
      title: "Analogy / structure-mapping across grounded domains (relational alignment, not surface match)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-421", "Q-074"]
      depends_on: ["abstract_relational_reasoning_v6:ARR-3"]
      cross_plan_link: ["object_reasoning_abstraction_v4"]
      blocking_on: "Analogy requires relational structure to map BETWEEN (ARR-3) and at least two grounded domains with comparable relational scaffolds. Both presuppose the full symbolic + relational stack; the cross-domain alignment operator itself is unspecified (carries an open question)."
      readiness_gate:
        - "ARR-3 relational inference in place (relations exist as alignable structure, not just bound symbols)"
        - "Two or more grounded domains sharing relational structure (e.g. spatial containment <-> social inclusion; physical support <-> commitment 'holding up') so structure-mapping has source + target -- the V4 substrate (object_reasoning_abstraction_v4) supplies the grounded domains"
        - "Open question (carried): is analogy a SEPARATE V6 alignment operator, or does it FALL OUT of MECH-300 traversal over a shared symbolic map (same map, different entry points)? The biology-before-formal-definitions rule applies: a relational-reasoning/analogy lit-pull is a registration gate before this becomes more than candidate."
      last_updated: 2026-06-10
      completion_note: "The capstone symbolic capacity: mapping relational structure across domains regardless of surface features (Gentner structure-mapping). Highest-risk, most prose-heavy node here -- resist building an analogy MODULE; first test whether it emerges from the ARR-2/ARR-3 stack (mirrors fast_empathy_v5's no-module discipline). Carries the plan's OPEN QUESTION -- whether analogy is a distinct operator or an emergent traversal pattern over a shared symbolic map. Per feedback_biology_before_formal_definitions, needs a relational-reasoning lit-pull (Gentner; Penn/Holyoak/Povinelli relational reasoning) before promotion beyond candidate. Design-only; the most V6-horizon node."
    - id: "abstract_relational_reasoning_v6:ARR-5"
      title: "Grammatical realisation of the event-arc: tense / aspect / because / but / unless / done / again"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-422"]
      depends_on: ["abstract_relational_reasoning_v6:ARR-2", "abstract_relational_reasoning_v6:ARR-3"]
      cross_plan_link:
        - "grammar_primitive_mining_v6"
        - "language_emergence_bootstrap_v6"
      blocking_on: "The event-arc grammar can only NAME an arc the agent already runs. The arc substrate (initiate/persist/interrupt/reorient/resume/close) is partial in V3 (commit/completion via MECH-061/MECH-057a; interrupt->resume is the underdeveloped span, the Zeigarnik gap) and only fully matures across V4/V5. The grammatical layer that mints tense/aspect/connectives is owned by grammar_primitive_mining_v6."
      readiness_gate:
        - "ARR-2 + ARR-3: compositional + relational machinery to bind the connectives (because/but/unless are RELATIONS between propositions)"
        - "grammar_primitive_mining_v6: the aspect/tense/connective cuts mined from grammar as the linguistic realisation of the action arc (per thought_intake_2026-06-05_cross_version_missing_bits: the same arc appears in V3 cue->move->hazard->resume->contact and V5 grammar tense/aspect/because/but/unless/done/again)"
        - "The ActionEventArc spine itself (candidate cross-version primitive in the cross-version intake): initiate + persist + interrupt + reorient + resume + closure -- 'because' names causation, 'but/unless' names exception (ARC-063 tolerance-gated availability), 'done/again' names aspect/closure, 'stop/resume' names the interrupt span (project_interrupted_task_resumption_gap)"
      last_updated: 2026-06-10
      completion_note: "The concrete payoff of the event-arc spine at linguistic scale: grammatical aspect/tense/connectives are the SYMBOLIC RENDERING of the pre-linguistic action arc. 'unless' = ARC-063 exception/tolerance gate; 'because' = the causal link in the predicate-argument-event family; 'again/done' = aspect over the arc's closure. This is the tightest grounding in the cross-version + grammar_llms intakes -- the arc must EXIST (V3..V5) before grammar can name it. Design-only; gated on the compositional/relational stack + grammar mining."
    - id: "abstract_relational_reasoning_v6:ARR-6"
      title: "Symbolic reasoning cannot override embodied harm sensing (the V6 instance of INV-007)"
      phase: 4
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-103"]
      depends_on: ["abstract_relational_reasoning_v6:ARR-2", "abstract_relational_reasoning_v6:ARR-4"]
      cross_plan_link: ["ethics_as_coherence_v5"]
      blocking_on: "A constraint over the symbolic-reasoning machinery: it cannot be stated until that machinery (ARR-2 compositional, ARR-4 analogy) exists to be constrained. The harm-sensing authority it defers to is the V3/V5 embodied harm + ethics-as-coherence substrate."
      readiness_gate:
        - "ARR-2 + ARR-4 in place (a reasoning capacity powerful enough to need this guard -- compositional + analogical recombination can generate persuasive but harmful rationalisations)"
        - "INV-007 (active): language cannot override embodied harm sensing. This node is INV-007 lifted to the symbolic-REASONING level: compositional/analogical inference is also subordinate to harm sensing, never a route around it"
        - "MECH-011 (active dependency seed): language as a MULTIPLIER of ethical learning, NOT a substitute -- 'purely linguistic agents risk ethical drift and rationalisation loops'. ethics_as_coherence_v5 owns the coherence authority symbolic reasoning must not override"
      last_updated: 2026-06-10
      completion_note: "The safety claim of the linguistic tier. Symbolic recombination is exactly the machinery that produces rationalisation loops (MECH-011's warning); analogy can map a harmful action onto a benign frame. This node asserts the same subordination INV-007 fixes for language generally, now specifically for symbolic INFERENCE. Grounds in two ACTIVE claims (INV-007, MECH-011) -- the new claim is the inference-level instance, not a re-statement. Like fast_empathy_v5's no-scalar prohibition, this is a negative architectural commitment."
    - id: "abstract_relational_reasoning_v6:ARR-7"
      title: "Biology grounding for relational/compositional reasoning + analogy (lit-pull)"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-419", "MECH-421"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: compositional generalisation, relational inference, and analogy each instantiate formal concepts (systematicity, structure-mapping) and need a biology/cognitive-science lit-pull BEFORE registration beyond candidate"
        - "Targeted reviews to commission: relational reasoning + the relational-reasoning gap (Penn, Holyoak & Povinelli 2008); structure-mapping theory of analogy (Gentner 1983; Gentner & Markman); compositionality / systematicity in human cognition and its developmental emergence; the neural substrate of relational integration (rostrolateral PFC, Christoff/Bunge)"
        - "No substrate gate -- this can begin independently of the linguistic stack; it is a registration gate for ARR-2 and ARR-4 promotion, not a build dependency"
      last_updated: 2026-06-10
      completion_note: "Grounding debt tracker for the most prose-heavy tier in REE. None of the compositional/relational/analogy capacities here has a dedicated lit-pull yet. Deferred (not blocked) because the review can begin now, independent of substrate; but it gates ARR-2 and ARR-4 promotion beyond candidate. Mirrors OBJ-6 / EMP-7 grounding-debt nodes in the sibling plans."
---
# Abstract / Relational / Compositional Reasoning at Symbolic Scale -- V6 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v6 (forward roadmap; LINGUISTIC mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the symbolic-scale reasoning the linguistic tier unlocks --
compositional generalisation, relational/propositional inference, analogy /
structure-mapping, and the grammatical realisation of the action arc -- around
one load-bearing scoping distinction (symbolic-scale abstraction is NOT the V4
substrate abstraction) and one safety constraint (symbolic reasoning is
subordinate to embodied harm sensing).

This is a **V6 (linguistic) tier** plan, the FINAL tier of the 3-tier partition
(V4 = individual mind, V5 = social, V6 = linguistic). The spine is **ARC-059**:
self -> objects -> others -> **LANGUAGE**. Language presupposes the V5 social
substrate (mirror modelling, other-modelling, joint attention) and the V4
object/self substrate; symbolic-scale REASONING presupposes language. This plan
therefore sits on top of the entire stack -- almost every node is gated behind an
upstream PLAN (the V6 emergence + grammar plans, the V5 social plans, the V4
object/abstraction plan, and the shared V3-completion gate MECH-163). It is a
*forward roadmap*, not a closure map: V6 has no experiments yet, so nodes carry
no `owner_exq` and the drift checker stays dormant. The value here is the
**readiness gates** -- exactly which upstream-tier prerequisites must land before
each symbolic-reasoning step is honest to build.

---

## One-line framing

> REE already has SUBSTRATE-level abstraction (theta-packaged units MECH-299,
> cognitive-map traversal MECH-300, type-encoder prototypes SD-040, action
> chunks, options -- owned by `object_reasoning_abstraction_v4`). What it does
> NOT have, and cannot have until the linguistic stack exists, is abstraction at
> SYMBOLIC scale: systematic recombination of GROUNDED, NAMED primitives into
> novel combinations (compositionality), inference over named relations
> (transitivity, role-binding), and structure-mapping across domains (analogy).
> The V4 abstraction is the substrate the symbols name; this V6 abstraction is
> the recombination the naming unlocks. The grammatical connectives
> (tense/aspect/because/but/unless/done/again) are the symbolic rendering of the
> pre-linguistic action arc -- they NAME an arc the organism already runs.

---

## The reasoning stack (one distinction, four capacities, one guard)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| substrate-vs-symbolic distinction | ARR-1 | NEWCLAIM (design/scoping) | V6 (registrable now) | none -- scoping claim over ARC-009 |
| compositional generalisation | ARR-2 | NEWCLAIM (mechanism) | V6 (blocked) | emergence + grammar plans + V4 substrate |
| relational / propositional inference | ARR-3 | NEWCLAIM (mechanism) | V6 (blocked) | ARR-2 + MECH-300 + V5 other-model |
| analogy / structure-mapping | ARR-4 | NEWCLAIM (mechanism) + open Q | V6 (blocked) | ARR-3 + two grounded domains |
| event-arc grammar realisation | ARR-5 | NEWCLAIM (mechanism) | V6 (blocked) | ARR-2/3 + grammar_primitive_mining_v6 |
| harm-subordination guard | ARR-6 | NEWCLAIM (architectural_commitment) | V6 (blocked) | INV-007 + MECH-011 + ARR-2/4 |
| biology grounding | ARR-7 | (grounding debt) | cross-cutting | relational-reasoning / analogy lit-pull |

---

## Why this is V6, not V4 (the load-bearing distinction)

The seed material is explicit that this tier is **distinct from**
`object_reasoning_abstraction_v4`. That V4 plan owns SUBSTRATE-level abstraction:
the unit packaged into a theta cycle (MECH-299), cognitive-map traversal at the
active abstraction level (MECH-300), the type-encoder prototype (SD-040), action
chunks and options. Those are abstractions the agent COMPUTES OVER -- but cannot
yet NAME, query, or recombine arbitrarily.

This V6 plan owns abstraction at **linguistic scale**: recombination via named
symbols and grammar. The recombination operator is the symbol/grammar layer
(owned by `language_emergence_bootstrap_v6` and `grammar_primitive_mining_v6`),
not the substrate. ARR-1 is the load-bearing scoping claim that keeps the two
levels from being conflated -- the analogue of ARC-080's type-vs-token fork for
objects. Conflating them would either (a) over-claim that V4 already does
symbolic reasoning, or (b) try to build symbolic recombination directly on the
substrate without the intervening symbol layer -- exactly the grammar-first error
the grammar_llms_v5 intake forbids.

---

## The grounding chain (where each capacity binds)

- **ARC-009 / INV-003** -- language as symbolic mediation; language emerges as
  functional self-representation, not a bolt-on. The compositional capacity must
  be GROUNDED (recombining symbols that point at real substrate), never imposed
  as syntax over ungrounded tokens.
- **MECH-300 / MECH-299 / SD-040** (V4) -- the substrate vocabulary the symbols
  name. Relational inference (ARR-3) is the V6 realisation of MECH-300's
  cognitive-map traversal, now over a SYMBOLIC/type-graph map whose nodes are
  named.
- **ARC-063 CandidateRuleField** -- the `context -> action-object -> outcome
  unless exception` rule shape is the pre-linguistic substrate that propositional
  inference (ARR-3) and the 'unless/because' connectives (ARR-5) name and chain.
  This is the grammar_llms_v5 intake's one near-term bridge.
- **The ActionEventArc spine** (cross-version intake) -- initiate / persist /
  interrupt / reorient / resume / close. ARR-5 asserts that grammatical
  aspect/tense/connectives are the symbolic rendering of this arc; the arc must
  exist (V3..V5) before grammar can name it.
- **INV-007 / MECH-011** (active) -- language cannot override embodied harm
  sensing; language is a multiplier, not a substitute, and purely linguistic
  agents risk rationalisation loops. ARR-6 lifts this guard to the symbolic
  INFERENCE level.

---

## What this plan deliberately does NOT do

- **Does NOT import LLM / transformer architecture.** Per the grammar_llms_v5
  intake's anti-import discipline: grammar and LLMs are MINED for primitive
  structure, not imported as architecture. Compositionality must be mined from
  grounded substrate; an analogy module is resisted until analogy is shown NOT to
  emerge from the ARR-2/ARR-3 stack (ARR-4, mirroring fast_empathy_v5's no-module
  discipline).
- **Does NOT pull anything into V3 (or V4, or V5).** This is the latest tier of
  all. Every reasoning node is gated behind the emergence + grammar V6 plans, the
  V5 social plans, and the V4 object/abstraction plan. Registering this roadmap
  changes no behaviour at any lower tier.
- **Does NOT re-own language emergence or grammar mining.** The symbol<->substrate
  bindings and the grammatical cuts are owned by `language_emergence_bootstrap_v6`
  and `grammar_primitive_mining_v6`; this plan CONSUMES grounded named symbols and
  reasons over them.
- **Does NOT re-own the V4 substrate abstraction.** Theta packaging (MECH-299),
  cognitive-map traversal (MECH-300), the type-encoder (SD-040), chunks and
  options are owned by `object_reasoning_abstraction_v4`; this plan names ARR-1 as
  the distinct symbolic level built on top of them.

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-06-05_grammar_llms_v5_primitive_mining.md | grammar->substrate mining table; predicate-argument-event family; anti-import discipline; ARC-063 bridge |
| evidence/planning/thought_intake_2026-06-05_cross_version_missing_bits.md | the ActionEventArc spine (initiate/persist/interrupt/resume/close) realised in grammar tense/aspect/because/but/unless/done/again |
| docs/architecture/language/language_and_learning.md (MECH-011) | language as multiplier-not-substitute; rationalisation-loop warning (grounds ARR-6) |
| claims.yaml ARC-009 / INV-003 / INV-007 | active language commitments: symbolic mediation; emergence-not-bolt-on; harm-sensing supremacy |
| claims.yaml ARC-063 | CandidateRuleField -- the rule shape propositional inference + 'unless' grammar names |
| claims.yaml MECH-299 / MECH-300 / SD-040 | the V4 SUBSTRATE-level abstraction this tier is explicitly distinguished FROM (owned by object_reasoning_abstraction_v4) |
| claims.yaml ARC-059 | the self -> objects -> others -> LANGUAGE maturational spine |

---

## Decision log

- **2026-06-10** -- Plan registered as a V6 (linguistic tier) forward-roadmap,
  the final tier of the V4/V5/V6 partition. Seven nodes: ARR-1 (substrate-vs-
  symbolic scoping distinction, the spine), ARR-2 (compositional generalisation),
  ARR-3 (relational/propositional inference), ARR-4 (analogy/structure-mapping +
  open Q), ARR-5 (event-arc grammatical realisation), ARR-6 (harm-subordination
  guard), ARR-7 (biology grounding debt). All reasoning nodes gated behind the V6
  emergence + grammar plans, the V5 social plans, and the V4 object/abstraction
  plan. Seven NEW claims proposed (the scoping distinction, compositional
  generalisation, relational inference, analogy, event-arc grammar realisation,
  the harm-subordination guard, and an open Q on whether analogy is a separate
  operator). `generation: v6` set so the V3 closure % is unaffected. No claims.yaml
  edits (orchestrator merges).
- **2026-06-10** -- Reassignment flag raised for MECH-373 (LanguageAffectAdaptor,
  currently implementation_phase v5 / version_relevance v4_v5): it is an
  intrinsically LINGUISTIC component (parses affect from LANGUAGE on the language
  channel) and reads more naturally as V6. ACTIVE language claims ARC-009 /
  INV-003 / INV-007 deliberately NOT flagged (established design, correctly
  active). MECH-163 deliberately NOT flagged (V3-completion / V4-entry gate, stays
  v3). MECH-299 / MECH-300 / SD-040 left as v4 (the substrate this tier is
  distinguished FROM, consumed not re-scoped).
