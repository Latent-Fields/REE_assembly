---
closure_plan:
  id: grammar_primitive_mining_v6
  generation: v6
  title: "Grammar & LLMs as primitive-mining scaffolds (mine, do NOT import architecture)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-009, INV-003, INV-007, ARC-063, ARC-062, ARC-059, MECH-278, MECH-373]
  sibling_plans:
    - multi_agent_ecology_v5
    - mirror_modelling_other_self_v5
    - fast_empathy_v5
    - ethics_as_coherence_v5
    - object_representation_v4
    - self_model_v4
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. V6 (the LINGUISTIC mind tier, the final
    tier of the V4-individual / V5-social / V6-linguistic partition) has no
    experiments and -- by design -- must not for a long time: language work is
    gated behind every pre-linguistic primitive (object / action / self / other /
    rule) being grounded first. Nodes therefore carry no owner_exq and the drift
    checker stays dormant against them. Each node's readiness_gate lists the
    prerequisites that must land before the V6 step is honest to build: the V5
    social plans (multi_agent_ecology_v5 supplies the social ecology that is the
    ENGINE of language; mirror_modelling_other_self_v5 + fast_empathy_v5 supply
    other-attribution; ethics_as_coherence_v5 supplies the coordination value),
    the V4 object/self plans (object_representation_v4 token-instance object-files;
    self_model_v4 self-attribution), and the V3 MECH-163 multi-step hippocampal
    planning gate. generation: v6 keeps these nodes OUT of the V3 closure
    percentage (serve.py read_closure, generate_closure_snapshot.py, and
    check_closure_drift.py are all generation-aware). The SPINE is ARC-059 carried
    to its terminus: self -> objects -> others -> LANGUAGE. This plan is the
    primitive-MINING discipline, NOT a plan to build a language module: grammar and
    LLM representations are treated as a MINE for identifying / naming / testing /
    recombining pre-linguistic primitives REE has already grounded -- never as an
    architecture to import (explicit, repeated cautions against transformer /
    LLM-architecture transfer). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V6 experiment is queued -- which cannot
    happen until the pre-linguistic substrate exists.
  nodes:
    - id: "grammar_primitive_mining_v6:GRAM-1"
      title: "Mine-not-import discipline: grammar/LLMs are a primitive MINE, never an architecture to transfer (load-bearing prohibition)"
      phase: 1
      status: open
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-100", "INV-003", "INV-007"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "No substrate prerequisite -- this is a DESIGN PROHIBITION + research-method commitment, registrable now as the spine of the whole plan: REE does NOT import transformer attention or LLM architecture; grammar and LLMs are MINED for primitive cuts only"
        - "Positive form: grammar is a fossil record of recurrent cognitive relations (agent, action, object, context, cue, outcome, cause, exception, self, other, rule, belief); for each grammatical primitive the method asks which PRE-LINGUISTIC REE substrate it binds to, and a cut is grounded ONLY if it changes perception / attention / action / memory / rule-availability / coordination"
        - "Consistency check against ACTIVE language claims: ARC-009 (language as symbolic-mediation/coordination LAYER over grounded substrate, not the origin of cognition), INV-003 (language emerges as functional self-representation, not a bolt-on), INV-007 (language cannot override embodied harm sensing) -- the prohibition is the corollary of all three; it does not contradict or re-scope them"
        - "Consistency check against the REE_convergence standing rule: external frameworks are mined-not-imported; this is the language/LLM instance of that rule"
      last_updated: 2026-06-10
      completion_note: "The CENTRAL contribution of the 2026-06-05 grammar/LLM intake (docs/thoughts/2026-06-05_Grammar_and_LLMS_as_V5_primitive-mining_scaffolds.md). Like ARC-012 (E3 needs no explicit ethical cost term) and the fast-empathy no-scalar prohibition (fast_empathy_v5:EMP-1), this is an architectural_commitment about what must NOT exist: there must be NO imported transformer block and NO 'language model' treated as a cognitive authority inside REE. Testable as a negative commitment -- any design that imports LLM architecture or rewards arbitrary ungrounded bitstrings violates it. Registrable now; it constrains every node below."
    - id: "grammar_primitive_mining_v6:GRAM-2"
      title: "Grammar->substrate mapping table (the mining artifact): per primitive, which substrate, which version, grounded-or-merely-named"
      phase: 1
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: ["ARC-100"]
      depends_on: ["grammar_primitive_mining_v6:GRAM-1"]
      cross_plan_link:
        - "object_representation_v4:OBJ-1"
        - "self_model_v4"
      readiness_gate:
        - "No substrate gate to AUTHOR the table -- it is a living V5/V6 design artifact (doc + method claim), but each ROW is only marked 'grounded' once its substrate exists"
        - "Table columns (from the intake Line A): grammatical primitive | candidate REE substrate | version (V3/V4/V5/V6) | grounded-or-merely-named | what experimental behaviour would show grounding"
        - "Seed rows already groundable in REE today: noun/NP -> object system (object_representation_v4 OBJ-1 type/token fork; MECH-278 object definition, currently BYPASSED in V3); verb/predicate -> action affordance (object_representation_v4:OBJ-4 / ARC-082); subject -> agent/self-attribution (self_model_v4; SD-003/SD-005); aspect -> event closure (start/ongoing/interrupted/resumed/completed/failed); modality -> affordance/constraint/norm/uncertainty; negation -> veto/inhibition/counterfactual boundary; conditional/exception -> tolerance-gated rule (ARC-063)"
        - "Do NOT overfit to English -- the durable rows are cross-linguistic: semantic role, reference, deixis, aspect, modality, negation, evidentiality, exception"
      last_updated: 2026-06-10
      completion_note: "The grammar->substrate table is the concrete deliverable of the mining method. The intake's Section 4 table is the seed. Most rows point at V4/V5 substrate that does not yet exist; the table's job is to keep each language-facing primitive HONEST about whether it is grounded or merely named. Cheapest node after GRAM-1; can land alongside it as the documentation pair. Frozen ontology is forbidden (would re-create the import error one level down) -- the table is provisional and extensible."
    - id: "grammar_primitive_mining_v6:GRAM-3"
      title: "Predicate-argument-event bridge to ARC-063 CandidateRuleField: render minted rules as 'if context, then action-object, causing outcome, unless exception'"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["MECH-415", "ARC-063"]
      depends_on: ["grammar_primitive_mining_v6:GRAM-1", "grammar_primitive_mining_v6:GRAM-2"]
      cross_plan_link: ["object_representation_v4:OBJ-1", "object_representation_v4:OBJ-4"]
      blocking_on: "The bridge can only NAME/QUERY rules that already exist as grounded pre-linguistic CandidateRule objects. ARC-063 v1 substrate landed in V3 (candidate_rule_field.py) but its rule_state is not yet behaviourally validated (gated on V3-EXQ-639 + the ARC-062 GAP-B re-run); and the action-object / outcome / exception slots the bridge renders presuppose token-instance objects (object_representation_v4:OBJ-1) and grounded affordances (OBJ-4), both V4. No rendering layer until the rules and their argument slots are grounded."
      readiness_gate:
        - "ARC-063 CandidateRuleField rule_state behaviourally validated (the rules to be rendered must exist and be differentiated, not vacuous) -- gated on the V3 substrate-readiness diagnostic + the ARC-062 weak-reading GAP-B behavioural re-run"
        - "The canonical shape: 'agent does action to object in context, causing outcome, unless hazard/exception interrupts' maps onto self/other-attribution -> action affordance -> object token -> context -> rule -> outcome -> exception -> interrupt -> resume -> closure (the intake's strongest primitive family)"
        - "The 'unless/except/but' exception grammar is a shadow of ARC-063 tolerance-gated rule AVAILABILITY (Tolerance-Principle gate); rendering exposes the gate without making language the rule substrate"
        - "Argument slots require grounded substrate: token-instance object (object_representation_v4:OBJ-1), grounded affordance (OBJ-4 / ARC-082), self/other-attribution (self_model_v4 + the V5 social plans)"
      last_updated: 2026-06-10
      completion_note: "The TIGHTEST connection in the intake (Section 6, Line C): grammar says ARC-063's already-engineered shape 'context -> action-object -> outcome' is the same relation language repeatedly encodes through predicates, arguments, roles, frames, conditionals, and exceptions. This grounds ARC-063 in linguistic typology and gives a future V6 layer a way to NAME, QUERY, COMPARE, and RECOMBINE rule structures -- without making language the rule substrate. Design-only today; blocked on ARC-063 rule-state validation + V4 argument-slot grounding."
    - id: "grammar_primitive_mining_v6:GRAM-4"
      title: "V5/V6 frame inventory: feeding / hazard / contact / interruption / help-harm / give-receive / request-response / belief-report / error-correction frames, each binding to REE substrates"
      phase: 2
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-416"]
      depends_on: ["grammar_primitive_mining_v6:GRAM-2"]
      cross_plan_link: ["fast_empathy_v5", "object_representation_v4:OBJ-4"]
      blocking_on: "A frame is a whole-scene structure (roles + participants + objects + relations + expected consequences). The help/harm, give/receive, request/response, and belief/report frames are intrinsically SOCIAL and require a stable other-model (the V5 social plans) plus grounded affordances (object_representation_v4:OBJ-4). Cannot bind to substrate that does not exist."
      readiness_gate:
        - "Frame semantics (Fillmore): words evoke whole scenes -- roles, participants, objects, relations, perspectives, expected consequences. Each frame must bind to REE substrates, not just words"
        - "Non-social frames (feeding/restoration, hazard/avoidance, contact/completion, interruption/resumption) can be seeded from V3/V4 substrate (SD-011 harm; the cue/contact/closure event arc)"
        - "Social frames (help/harm, give/receive, request/response, belief/report) require the V5 social ecology (multi_agent_ecology_v5) + other-attribution (mirror_modelling_other_self_v5 / fast_empathy_v5)"
        - "error/correction frame binds to the repair/clarification machinery the bootstrap hypothesis needs (GRAM-6)"
      last_updated: 2026-06-10
      completion_note: "The intake's Line E. The frame inventory is the second mining artifact (after the grammar->substrate table): a small, extensible set of scene-schemas, each pinned to its substrate. Non-social frames are nearly groundable; social frames wait on the V5 plans. Blocked rather than open because the most valuable frames are social and the substrate is V5."
    - id: "grammar_primitive_mining_v6:GRAM-5"
      title: "Aspect / event-arc as closure map: starting / ongoing / repeated / interrupted / resumed / completed / failed / abandoned"
      phase: 2
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: ["MECH-417"]
      depends_on: ["grammar_primitive_mining_v6:GRAM-2"]
      cross_plan_link: ["object_representation_v4:OBJ-4"]
      blocking_on: "Aspect is a map of the event arc (contact / interruption / closure / transition boundaries). The interrupted/resumed/abandoned distinctions presuppose grounded action affordances with completion + interruption conditions (object_representation_v4:OBJ-4 / ARC-082) and the interrupted-task resumption substrate (Zeigarnik / MECH-320 sketch), neither yet built. Names the arc before the arc exists."
      readiness_gate:
        - "Event Segmentation Theory: experience is segmented into events around prediction error and event-boundary updates -- directly overlaps REE's need for contact / interruption / closure / transition boundaries"
        - "Aspect categories (start / ongoing / repeated / interrupted / resumed / completed / failed / abandoned) are a candidate map for REE's closure and post-commit action arcs"
        - "Each action verb class must bind to: a possible action, a predicted state transition, a cost/harm profile, an object role, a completion condition, an interruption condition (the intake's Line F + Section 10 check)"
        - "Shares the event-arc spine with the twin 2026-06-05 cross-version intake (cross_version_missing_bits) -- the V5/V6 closure question"
      last_updated: 2026-06-10
      completion_note: "The intake's Line F. Aspect is the linguistic shadow of the event arc REE already needs for closure and resumption. Useful for the post-commit action arc, but it can only be validated once action affordances carry interruption/completion conditions (V4) and the resumption substrate exists. A naming-layer over the closure machinery, never a replacement for it."
    - id: "grammar_primitive_mining_v6:GRAM-6"
      title: "Language-bootstrap-from-ecology: proto-language stabilises from grounded proto-communication in the social ecology (grammar/LLMs = turbocharger, not engine)"
      phase: 3
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["ARC-101", "ARC-009", "INV-003"]
      depends_on: ["grammar_primitive_mining_v6:GRAM-1", "grammar_primitive_mining_v6:GRAM-3", "grammar_primitive_mining_v6:GRAM-4"]
      cross_plan_link:
        - "multi_agent_ecology_v5"
        - "mirror_modelling_other_self_v5"
        - "fast_empathy_v5"
        - "ethics_as_coherence_v5"
      blocking_on: "The bootstrap ENGINE is the social ecology, not grammar. It requires the full enabling-conditions set: shared world + object tokens (object_representation_v4) + action affordances (OBJ-4) + self-attribution (self_model_v4) + other-attribution (mirror_modelling_other_self_v5 / fast_empathy_v5) + joint attention + partial observability + social-coordination pressure (multi_agent_ecology_v5 + ethics_as_coherence_v5) + memory + a low-cost signalling channel + repair. None of the social-ecology enabling conditions exist before the V5 plans land, and those are gated behind MECH-163 (V4-social entry) + V4 substrate per DEV-NEED-021."
      readiness_gate:
        - "Sequence (the intake addendum): object/action/self/other substrates -> shared attention -> useful signals -> repeated signal/action/outcome regularities -> proto-conventions -> grammar-like compression -> language-facing V6 layer"
        - "Enabling conditions (intake addendum Section 2): shared world, object tokens, action affordances, self-attribution, other-attribution, joint attention, partial observability, social-coordination pressure, memory, low-cost signalling channel, partner variation, repair/clarification"
        - "Communication signals feed ARC-063 rule-apprehension: a signal can become part of a recurring context -> action-object -> outcome regularity (signal 'hazard-there' -> other reorients -> harm avoided); proto-signals may become candidate rules / social affordances (the GRAM-3 bridge)"
        - "MECH-163 multi-step hippocampal planning (V4-social entry gate) + the V5 social plans (multi_agent_ecology_v5 supplies the ecology that is the ENGINE; ethics_as_coherence_v5 supplies the coordination value that makes signals improve outcomes)"
        - "Do NOT reward arbitrary bitstrings unless grounded, reusable, and action-relevant; do NOT assume communication bootstraps without ecological pressure; do NOT assume human-interpretable language emerges automatically"
      last_updated: 2026-06-10
      completion_note: "The intake's addendum and the strongest forward prediction: if the V5 social ecology supplies shared attention + partial observability + coordination pressure + a low-cost channel + repair, then proto-language may PARTIALLY bootstrap from grounded proto-communication -- and the grammar/LLM scaffold becomes a turbocharger (recognise / stabilise / name / recombine the emerging communicative primitives) rather than the engine. Most heavily gated node: it consumes ALL the V5 social plans plus the V4 individual substrate. Per feedback_biology_before_formal_definitions this developmental/social claim needs the GRAM-7 lit-pull before promotion beyond candidate."
    - id: "grammar_primitive_mining_v6:GRAM-7"
      title: "LLM-as-mine-not-foundation discipline + biology/linguistics grounding (lit-pull): cognitive/construction grammar, frame semantics, semantic-role labelling, ESS, LLM thematic-role limits"
      phase: 2
      status: deferred
      severity: medium
      owner_exq: null
      unblocks_claims: ["ARC-100", "ARC-101"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Per project rule feedback_biology_before_formal_definitions: the primitive-mining method and the bootstrap hypothesis instantiate formal-linguistics concepts and need a linguistics/cognition lit-pull BEFORE registration beyond candidate"
        - "Seed anchors already in the intake: Cognitive Grammar (grammar is meaningful, not autonomous formal system); Construction Grammar (constructions = learned form-meaning pairings; aligns with rule-apprehension); Frame Semantics (Fillmore: words evoke scenes); semantic-role theory / SRL (who did what to whom, where, why, with what outcome); Event Segmentation Theory (event boundaries at prediction error); LLM thematic-role-interface limits (LLMs encode some syntax/role info but are not grounded organisms -- exactly the gap REE's grounding fills)"
        - "LLM discipline (Line D): use LLMs ONLY as hypothesis generators for candidate primitive cuts / grammar mappings / frame inventories; never as truth or cognitive authority; a signal is grounded only if it binds to REE substrate and changes attention / action / memory / rule-availability / coordination"
      last_updated: 2026-06-10
      completion_note: "Grounding-debt tracker for the linguistics side. The intake already cites the relevant literatures; what is missing is a dedicated, structured pull that pins each mining-method commitment and the bootstrap enabling-conditions to a source. Deferred (not blocked) because the lit-pull can begin independently of the substrate, but it is a registration gate for the grammar_mining_method and language_bootstrap_from_ecology claims. Carries the LLM-as-mine-not-foundation discipline (Line D) as a standing methodological commitment."
---
# Grammar & LLMs as Primitive-Mining Scaffolds -- V6 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v6 (forward roadmap; LINGUISTIC mind tier; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the language-tier discipline that treats grammar and LLM
representations as a MINE for pre-linguistic primitives REE has already grounded
-- never as an architecture to import -- around one prohibition (mine-not-import),
two mining artifacts (the grammar->substrate table, the frame inventory), the
predicate-argument-event bridge to ARC-063, an aspect/event-arc closure map, and
the language-bootstrap-from-ecology hypothesis. The grammar scaffold is a
turbocharger; the engine is the social ecology.

This is the **V6 (linguistic) tier** plan, the FINAL tier of the 3-tier
partition (V4 = individual mind, V5 = social, V6 = linguistic). The spine is
**ARC-059** carried to its terminus: self -> objects -> others -> **LANGUAGE**.
Language PRESUPPOSES the V5 social substrate (other-modelling, mirror modelling,
joint attention) and the V4 object/self substrate; the intake is explicit that
language work must wait until the pre-linguistic primitives (object / action /
self / other / rule) exist and are grounded -- "mine grammar and LLMs for
primitive cuts only after the organism has enough pre-linguistic grounding for
those cuts to bind onto." It is a *forward roadmap*, not a closure map: V6 has no
experiments yet (and must not for a long time), so nodes carry no `owner_exq` and
the drift checker stays dormant. The value here is the **readiness gates** -- for
each step, exactly which V4 individual-substrate, V5 social-substrate, and V3
completion prerequisites must land before the V6 step is honest to build.

---

## One-line framing

> The cognition that language compresses already EXISTS (or is being built) in
> REE pre-linguistically -- object tokens, action affordances, self/other
> attribution, ARC-063 rule apprehension. Grammar is a fossil record of those
> recurrent cognitive relations; LLMs are large mines of that fossil record. The
> V6 move is NOT to import an LLM (ARC-009/INV-003/INV-007 forbid making language
> the origin or the override of cognition) -- it is to MINE grammar and LLMs for
> the primitive cuts REE has already grounded, so those cuts become nameable,
> queryable, composable, and shareable. The strongest single mine is
> predicate-argument-event structure, which is the same shape ARC-063
> CandidateRuleField already mints. The strongest single prediction is that
> proto-language may PARTIALLY bootstrap from a grounded social ecology, with the
> grammar/LLM scaffold as turbocharger, not engine.

---

## The mining stack (one prohibition, two artifacts, one bridge, one bootstrap)

| Step | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| prohibition (mine-not-import) | GRAM-1 | NEWCLAIM (architectural_commitment / method) | V6 (registrable now) | none -- it is a design + method prohibition |
| grammar->substrate table | GRAM-2 | NEWCLAIM (method artifact) | V6 (doc step) | rows grounded only as substrates land |
| pred-arg-event -> ARC-063 bridge | GRAM-3 | NEWCLAIM (mechanism/method) + ARC-063 | V6 (blocked) | ARC-063 rule-state validated + V4 arg-slots |
| frame inventory | GRAM-4 | NEWCLAIM (method artifact) | V6 (blocked) | V5 social plans (social frames) |
| aspect / event-arc closure map | GRAM-5 | NEWCLAIM (method artifact) | V6 (blocked) | OBJ-4 affordances + resumption substrate |
| language bootstrap from ecology | GRAM-6 | NEWCLAIM (design hypothesis) + ARC-009/INV-003 | V6 (blocked) | ALL V5 social plans + V4 substrate + MECH-163 |
| linguistics/LLM grounding | GRAM-7 | (grounding debt) | cross-cutting | linguistics lit-pull + LLM-as-mine discipline |

---

## Why these are V6, not V5

The intake originally self-labelled "V5 primitive-mining scaffolds", but under
the 3-tier partition the SUBJECT of every node is intrinsically LINGUISTIC --
grammar, predicate-argument structure, frames, aspect, proto-language emergence.
The plan's own ordering puts language LAST: it presupposes the V5 social
substrate (the bootstrap engine is the social ecology) and the V4 object/self
substrate (the argument slots the rules render). That places the mining work
itself in the V6 linguistic tier, sitting on top of BOTH the V4 individual and V5
social substrates. The one near-term hook -- the ARC-063 exception-grammar bridge
-- is V6-as-naming-layer over a V3-landed (but not yet validated) rule field; it
still does not run until the rule field is behaviourally validated and the V4
argument slots exist.

Note the symmetry with the fast-empathy and ethics plans: like
`fast_empathy_v5:EMP-1` (no empathy scalar) and ARC-012 (no explicit ethical cost
term), the load-bearing claim here (GRAM-1) is an architectural commitment about
what must NOT exist -- no imported transformer block, no LLM treated as a
cognitive authority.

---

## What this plan deliberately does NOT do

- **Does NOT import LLM / transformer architecture.** That is the whole point
  (GRAM-1). Any future design that bolts a transformer block into REE or rewards
  arbitrary ungrounded bitstrings violates the plan's central claim.
- **Does NOT make language the rule substrate.** The ARC-063 bridge (GRAM-3)
  RENDERS and QUERIES rules that already exist pre-linguistically; it does not
  mint them. Rule minting stays with ARC-062 / ARC-063 / ARC-064.
- **Does NOT pull anything into V3, V4, or V5.** Registering this roadmap changes
  no behaviour at any tier. Every substantive node is blocked behind the V5 social
  plans and the V4 individual substrate.
- **Does NOT re-scope the ACTIVE language claims.** ARC-009 (language as a
  symbolic-mediation layer), INV-003 (language as functional self-representation),
  INV-007 (language cannot override embodied harm sensing) are established design;
  this plan is their downstream method, consistent with all three. They are NOT
  flagged for reassignment.
- **Does NOT overfit to English.** The durable mined primitives are
  cross-linguistic (semantic role, reference, deixis, aspect, modality, negation,
  evidentiality, exception).

---

## Source artefacts

| Artefact | Role |
|---|---|
| docs/thoughts/2026-06-05_Grammar_and_LLMS_as_V5_primitive-mining_scaffolds.md | primary source (the mine-not-import thesis + grammar->substrate table + Lines A-G + bootstrap addendum) |
| evidence/planning/thought_intake_2026-06-05_grammar_llms_v5_primitive_mining.md | the processed intake (novel = grammar->substrate map + pred-arg-event bridge to ARC-063 + bootstrap-from-ecology) |
| claims.yaml ARC-009 / INV-003 / INV-007 | the ACTIVE language claims this method is downstream of (NOT flagged) |
| claims.yaml ARC-063 / ARC-062 | CandidateRuleField (strong/weak rule apprehension) -- the pred-arg-event bridge target |
| claims.yaml ARC-059 / MECH-278 | the self->objects->others->language spine + the object definition the noun row binds to |
| claims.yaml MECH-373 | LanguageAffectAdaptor -- an intrinsically-linguistic claim currently tagged v5; see Reassignment flags |
| evidence/planning/object_representation_v4_plan.md / self_model_v4_plan.md | the V4 individual substrate (object tokens, self-attribution) the argument slots need |
| evidence/planning/multi_agent_ecology_v5_plan.md / mirror_modelling_other_self_v5_plan.md / fast_empathy_v5_plan.md / ethics_as_coherence_v5_plan.md | the V5 social ecology that is the ENGINE of the bootstrap |

---

## Decision log

- **2026-06-10** -- Plan registered as a V6 (linguistic tier) forward-roadmap,
  the final tier of the V4/V5/V6 partition. Seven nodes: GRAM-1 (mine-not-import
  prohibition, the spine), GRAM-2 (grammar->substrate table), GRAM-3
  (predicate-argument-event bridge to ARC-063), GRAM-4 (frame inventory), GRAM-5
  (aspect/event-arc closure map), GRAM-6 (language-bootstrap-from-ecology), GRAM-7
  (linguistics/LLM grounding debt + LLM-as-mine discipline). All substantive nodes
  gated behind the V5 social plans + V4 individual substrate + MECH-163 per
  ARC-059 / DEV-NEED-021. Five NEW prose-only candidate claims proposed (the
  mining method, the pred-arg-event rule bridge, the frame inventory, the aspect
  closure map, the bootstrap hypothesis). `generation: v6` set so the V3 closure %
  is unaffected. No claims.yaml edits (orchestrator merges).
- **2026-06-10** -- Reassignment flag raised for MECH-373 (LanguageAffectAdaptor):
  it is an INPUT adaptor ON the language channel (intrinsically linguistic) yet is
  currently tagged `implementation_phase: v5`. Recommended V6. ARC-009 / INV-003 /
  INV-007 are ACTIVE established design and deliberately NOT flagged; MECH-163 is
  the V3-completion / V4-social entry gate and stays v3.
