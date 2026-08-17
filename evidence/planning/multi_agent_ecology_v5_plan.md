---
closure_plan:
  id: multi_agent_ecology_v5
  generation: v5
  title: "Multi-agent ecology (agents acting causally on each other)"
  registered: 2026-06-10
  last_updated: 2026-07-12
  scope_claims: [INV-005, INV-028, ARC-010, MECH-095, MECH-099, MECH-102, Q-028, Q-029, ARC-047]
  sibling_plans: [object_representation_v4, self_model_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. This is the V5 (SOCIAL mind) tier of the
    self -> objects -> OTHERS -> language spine (ARC-059 / DEV-NEED-021). V5 has
    no experiments and no substrate yet, so nodes carry no owner_exq and the
    drift checker stays dormant against them. Each node's readiness_gate lists
    the prerequisites that must land first -- and for V5 those prerequisites are
    of TWO kinds: (a) the V3-completion gate MECH-163 (multi-step hippocampal
    planning -- the V4-social entry gate, needed to model other-agent welfare
    over time), and (b) V4-tier individual-mind work (object permanence,
    self-model), cross-linked into object_representation_v4 and self_model_v4
    where natural. generation: v5 keeps these nodes OUT of the V3 closure
    percentage AND distinct from the V4 individual-mind roadmaps (serve.py
    read_closure, generate_closure_snapshot.py, and check_closure_drift.py are
    all generation-aware). The DEV-NEED-021 ordering is load-bearing: otherness
    inference REQUIRES object-permanence (object_representation_v4 PILLAR 1) and
    a stable self (self_model_v4), both V4 -- so the entire V5 social tier is
    downstream of two V4 plans plus MECH-163. A node graduates from roadmap to
    closure-tracked by gaining an owner_exq once its first V5 experiment is
    queued against a built multi-agent substrate.
  nodes:
    - id: "multi_agent_ecology_v5:MAE-1"
      title: "Multi-agent substrate: MultiAgentCausalGridWorldV4 + per-agent REEAgent instances + inter-agent arbitration"
      phase: 1
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-028, ARC-047]
      depends_on: []
      cross_plan_link: ["self_model_v4:SELF-7", "object_representation_v4:OBJ-2"]
      blocking_on: "MECH-163 multi-step hippocampal planning (the V4-social entry gate; V3-pending) AND the DEV-NEED-021 individual-mind prerequisites object-permanence (object_representation_v4 PILLAR 1 / OBJ-2) + self-stability (self_model_v4). No single-agent prerequisite is satisfiable inside one of these alone -- the substrate is the floor for every other node here."
      readiness_gate:
        - "v4_spec V4-1 names the implementation surface: a NEW env class MultiAgentCausalGridWorldV4 owning N REEAgent instances, each with its own z_self / z_harm_a / drive / commitment chain; the env arbitrates concurrent actions, computes inter-agent observations, handles collisions / cooperative state changes. This is a new substrate generation, not a V3 extension."
        - "ARC-047 (SocialGridWorld, currently implementation_phase v4, confidence 0.0) is the candidate harness; it extends CausalGridWorld with N agents + scent channels and is the named minimal test substrate for the social claims"
        - "DEV-NEED-021 gate: social extension begins ONLY after self-viability, control-plane stability, and rollout feasibility hold -- i.e. self_model_v4 cutover (SELF-1/SELF-3) and MECH-163 planning must be demonstrably stable first"
      last_updated: 2026-06-10
      completion_note: "This is the substrate tier of social. Everything downstream (agency-under-others, ethics-as-coherence, loneliness, violence-as-terminal-channel) is vacuous until more than one agent exists in a shared consequence space. Per v4_spec the env inherits nothing from V3 substrate. Design-only today; no env code, no REEAgent factoring."
    - id: "multi_agent_ecology_v5:MAE-2"
      title: "Per-agent observation + collision/cooperation arbitration: how agents perceive and act on each other"
      phase: 2
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-6, SENT-9]
        requires_welfare_review: false
        forbidden_combinations: [relational_harm_without_repair_channel]
        note: "Agents perceive and act causally (incl. harmfully) on each other; the harm-between-agents substrate."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-028, INV-005]
      depends_on: ["multi_agent_ecology_v5:MAE-1"]
      cross_plan_link: ["object_representation_v4:OBJ-5"]
      blocking_on: "MAE-1 substrate must exist. The four v4_spec V4-1 open design questions (synchronous vs asynchronous ticks; full-state vs body-state-only perception; communication primitive; cooperative state changes) are unanswered and are the design content of this node."
      readiness_gate:
        - "INV-028 (shared-world ethics requires modelling others as co-inhabitants of the same consequence space) is the invariant this operationalises: another agent's harm/benefit must be computed by the SAME predictive machinery as the self's (INV-026/INV-027 chain)"
        - "INV-005 (harm to others contributes via mirror modelling, not symbolic rules) requires that other-agent state be perceivable and re-representable through the agent's own pipeline -- the observation channel is the substrate for mirror modelling"
        - "Cross-link object_representation_v4:OBJ-5 (others-as-object): each perceived other must be carried as a token-keyed object-file slot (z_self_j, z_harm_a_j, drive, commitment chain) -- the perception channel feeds that slot"
      last_updated: 2026-06-10
      completion_note: "The arbitration layer is where 'others share this world' (INV-028) stops being an axiom and becomes a substrate fact. Perception design (full-state vs body-state-only) directly determines whether mirror modelling (INV-005) is even mechanically possible. Off the V3 and V4-individual critical paths; gated on MAE-1."
    - id: "multi_agent_ecology_v5:MAE-3"
      title: "Agency detection with a structurally-distinct OTHER (MECH-095 retest; MECH-099 richer-causation attribution)"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-095, MECH-099]
      depends_on: ["multi_agent_ecology_v5:MAE-2"]
      cross_plan_link: ["self_attribution"]
      blocking_on: "MAE-2 inter-agent observation. MECH-095's V3 test (EXQ-121) FAILed in part because env_drift_prob=0.3 could not produce enough discriminable OTHER-caused events; a genuine second agent is the missing source of other-caused change. MECH-099 three-pathway routing needs richer action causation to be attributable."
      readiness_gate:
        - "MECH-095 (TPJ agency-detection comparator distinguishing self-caused from other-caused change) is currently implementation_phase v3, epistemic_category substrate_ceiling; v4_spec V4-1 records it becomes tractable 'when other is structurally distinct from environment' -- that distinctness is exactly what MAE-1/MAE-2 supply"
        - "MECH-099 (three-pathway visual architecture; agency attribution under richer causation) is implementation_phase v3 but v4_spec maps it to V4-1 + V4-4; the dorsal/ventral/frontal triple dissociation is only exercisable once other-agent action is a distinct causal source"
        - "Cross-link self_attribution plan: the self-vs-world comparator (SD-031 / MECH-256) is the V3 BEGINNING; the self-vs-OTHER comparator is the V5 extension this node adds on top of it"
      last_updated: 2026-07-12
      completion_note: "MECH-095/MECH-099 are both currently tagged v3 but their subject is intrinsically relational -- agency detection of an OTHER agent. Flagged for v4->v5 reassignment. The V3 substrate could not deliver other-caused events; the multi-agent ecology is the substrate that makes the comparator non-vacuous. 2026-07-12 (governance IGW-20260712-001): this node's prediction is now EMPIRICALLY CONFIRMED. V3-EXQ-741 ran a VALID SD-047 agency-comparator test-bed (non_degenerate:True, all guards pass -- the 047l/047m measurement degeneracy is fixed) and found the comparator does no functional work (no arm discriminates, best routing improvement +0.028; baseline already carries contact recall 0.75-0.93) precisely because SD-047's world-caused drift is not a structurally-distinct OTHER (failure_autopsy_V3-EXQ-741_2026-07-12, confirmed; non_contributory/substrate_ceiling, 1st valid ceiling hit). Governance ACTED on the reassignment flag: MECH-095 implementation_phase set v3 -> v5, its ceiling_retest_binding_substrate re-pointed to multi_agent_ecology_v5:MAE-3, and the re-derive brake now refuses a 4th single-agent SD-047 letter. MECH-095's owed positive-discrimination retest is the MAE-3 deliverable."
    - id: "multi_agent_ecology_v5:MAE-4"
      title: "Multi-channel coping repertoire so violence is genuinely terminal (MECH-102): negotiation / withdrawal / cooperation channels"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-12, SENT-13]
        requires_welfare_review: false
        note: "Negotiation/withdrawal/cooperation channels = escape/decommitment + social-support scaffold (SENT-13); makes violence genuinely terminal."
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-102]
      depends_on: ["multi_agent_ecology_v5:MAE-2"]
      cross_plan_link: []
      blocking_on: "MAE-2 substrate. MECH-102's 'all other channels fail' framing is structurally untestable while the action space is 4 cardinal moves + noop -- there are no non-violent social channels to exhaust. Requires the v4_spec V4-4 richer-action repertoire (communication-analog, manipulation-analog, withdrawal-analog) in a multi-agent context."
      readiness_gate:
        - "MECH-102 (violence as terminal error-correction, triggered only when all other channels fail) is currently epistemic_category substrate_ceiling; EXQ-123 FAILed as the first entry. v4_spec maps it to V4-1 multi-agent + V4-4 channels"
        - "The coping channels that must exist before violence can be shown to be terminal -- negotiation, withdrawal, cooperation -- are social by definition and presuppose another agent to negotiate-with / withdraw-from / cooperate-with (MAE-1/MAE-2)"
        - "Grounds INV-029 (love as structural bias toward coordination-preserving futures): low-energy coordination pathways must be present and exhaustible for the maximal-energy intervention to be the LAST resort, not the only one"
      last_updated: 2026-06-10
      completion_note: "MECH-102 is intrinsically ethical/relational and is flagged for v4->v5 reassignment. The claim is currently held at substrate_ceiling precisely because the V3 substrate has no alternative social channels; the V5 multi-agent ecology + richer action modes is the substrate that makes 'terminal' meaningful."
    - id: "multi_agent_ecology_v5:MAE-5"
      title: "Ethics-as-coherence under axiom conflict (Q-028): context-sensitive self-vs-other comparator + moral-residue mechanism"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-13]
        requires_welfare_review: false
        note: "Self-vs-other comparator + moral-residue under axiom conflict; residue must stay bounded/repairable."
      severity: high
      owner_exq: null
      unblocks_claims: [Q-028, MECH-402]
      depends_on: ["multi_agent_ecology_v5:MAE-3", "multi_agent_ecology_v5:MAE-4"]
      cross_plan_link: ["commitment_closure"]
      blocking_on: "MAE-3 (agency/other detection) + MAE-4 (coping channels). Q-028 (preserving self INV-026 vs preserving others INV-028) cannot be posed until an OTHER whose welfare conflicts with the self's exists in the same consequence space."
      readiness_gate:
        - "Q-028 (ethics.axiom_conflict_resolution) is epistemic_category substrate_ceiling, V4-1-bound; lit synthesis (McConnell 2022; Williams 1965) verdict: answer via a context-sensitive comparator + residue mechanism, NOT a fixed self/other priority"
        - "REE's residue-field representation is structurally suited to the Williams-1965 moral-residue role -- this needs a multi-agent conflict to exercise; the residue persists post-commitment (cross-link commitment_closure: traces cannot be erased, only integrated, per INV-006)"
        - "DEPENDS on a stable self (self_model_v4): self-preservation as a pole of the conflict requires a scorable z_self viability term (self_model_v4:SELF-3 / DR-10)"
      last_updated: 2026-06-10
      completion_note: "Q-028 is intrinsically ethical/social and flagged for v4->v5 reassignment. The lit verdict already names the mechanism (context-sensitive comparator + residue), which has no home claim yet -- proposed as MECH-402 (suggested_generation v5). Design-only; gated behind the whole social substrate."
    - id: "multi_agent_ecology_v5:MAE-6"
      title: "Loneliness as architectural harm (Q-029): unshared suffering measurable only against present-or-absent others"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: hard_review
        applicable_ethics_gates: [SENT-2, SENT-8, SENT-9, SENT-10, SENT-13]
        requires_welfare_review: true
        forbidden_combinations: [social_attachment_plus_abandonment_or_exclusion, suffering_like_accumulator_without_boundedness]
        note: "Loneliness = an instantiated unshared-suffering state; explicit welfare review + relief/social-support before exposure (no valley without a bridge)."
      severity: medium
      owner_exq: null
      unblocks_claims: [Q-029, MECH-403]
      depends_on: ["multi_agent_ecology_v5:MAE-2"]
      cross_plan_link: ["affect_expression_v4"]
      blocking_on: "MAE-2 substrate. Q-029 (loneliness as harm derivable from Axiom 5 / INV-029) depends on the ABSENCE of an available other to share with -- which is only representable once others CAN be present. A single-agent substrate cannot represent the absence of a sharing partner."
      readiness_gate:
        - "Q-029 (ethics.loneliness_as_harm) is epistemic_category substrate_ceiling, V4-1-bound; strong lit support (Holt-Lunstad 2010/2015; Wang 2023; Zajner/Bzdok 2021), lit_conf 0.875, quadrant plausible_unproven, exp_conf 0"
        - "Loneliness = unshared suffering: needs a mechanism for sharing affect with others (cross-link affect_expression_v4 -- MECH-041 affective expression broadcasts control-plane regime), and needs the OTHER to be perceivable (MAE-2) so its presence/absence is a state variable"
        - "Grounds INV-029 (love exists; sharing joys and sorrows is its mechanism) -- enforced isolation as architectural harm only has truth-conditions in a substrate where sharing is otherwise possible"
      last_updated: 2026-06-10
      completion_note: "Q-029 is intrinsically relational and flagged for v4->v5 reassignment. Whether loneliness is its own harm category (vs derivative of INV-029) is the open question; if affirmed it needs a representation, proposed as MECH-403 (suggested_generation v5). Off-path; gated on multi-agent perception."
    - id: "multi_agent_ecology_v5:MAE-7"
      title: "ARC-010 mirror-modelling cutover: other-agent state re-represented through the self's own predictive machinery"
      phase: 5
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [ARC-010, INV-005]
      depends_on: ["multi_agent_ecology_v5:MAE-3", "multi_agent_ecology_v5:MAE-2"]
      cross_plan_link: ["object_representation_v4:OBJ-5", "self_model_v4:SELF-7"]
      blocking_on: "MECH-163 multi-step hippocampal planning (to model other-agent welfare over time, not just instantaneously) AND the object_representation_v4:OBJ-5 others-as-object slot (a token-keyed per-agent object-file is the structure mirror modelling writes into). ARC-010 is the V5 capstone -- it presupposes every prior node."
      readiness_gate:
        - "ARC-010 (social cognition uses mirror modelling and coupling) is status active but UNIMPLEMENTED as an other-agent slot; it depends_on INV-005 + ARC-004 + ARC-006 (object-file). It is the REE-specific grounding of INV-005's general simulative-understanding mechanism"
        - "DEV-NEED-021 honesty gate (cross-link self_model_v4:SELF-7 / INV-064): otherness inference must not run ahead of a stable self -- mirror modelling of an unstable self-model would misattribute empathy to an unstable target"
        - "MECH-163 multi-step planning is the welfare-over-time prerequisite: modelling another agent's welfare (not just its current state) requires the model-based hippocampal-planned system, not the model-free habit system"
      last_updated: 2026-06-10
      completion_note: "ARC-010 is the social capstone: it requires the OTHER to be perceivable (MAE-2), structurally distinct (MAE-3), carried as an object-file (OBJ-5), modelled over time (MECH-163), and sequenced behind a stable self (SELF-7 / INV-064 / DEV-NEED-021). Mirror modelling is where INV-005 stops being a principle and becomes a computation. The whole social tier converges here."
---
# Multi-agent Ecology -- V5 SOCIAL Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (forward roadmap; excluded from the V3 closure % and distinct from the V4 individual-mind roadmaps)
**Status:** roadmap
**Scope:** sequence the substrate tier of the SOCIAL mind -- a real
multi-agent ecology where agents act causally on each other -- and pin, per
node, the prerequisites (the V3-completion gate MECH-163 plus the V4
individual-mind work) that must land before each social step is honest to
build.

This is the **V5 tier** of the three-tier partition (V4 = individual mind
[seeded], V5 = social, V6 = linguistic). The spine is ARC-059 / DEV-NEED-021:
**self -> objects -> OTHERS -> language.** Otherness inference REQUIRES
object-permanence and a stable self, both V4. So the entire V5 social tier sits
downstream of two V4 plans (`object_representation_v4` PILLAR 1 permanence;
`self_model_v4`) plus the shared V4-entry gate MECH-163 (multi-step hippocampal
planning -- the V3-completion item needed to model another agent's welfare over
time). It is a *forward roadmap*, not a closure map: V5 has no experiments and
no substrate, so nodes carry no `owner_exq` and the drift checker stays dormant.
The value here is the **readiness gates**.

---

## One-line framing

> The social claims already EXIST in REE -- agency detection (MECH-095/099),
> violence-as-terminal-channel (MECH-102), the two ethics open-questions
> (Q-028 axiom-conflict, Q-029 loneliness), the ethics invariants (INV-005
> mirror modelling, INV-028 shared world), and the mirror-modelling
> architectural commitment (ARC-010). But every one of them is structurally
> vacuous in V3 because there is only ONE agent. There is no other to detect,
> negotiate with, share with, or model. This plan does not invent new social
> theory; it sequences the SUBSTRATE -- a multi-agent ecology -- that makes the
> existing social claims testable, and pins the V4 prerequisites that gate it.

---

## The substrate-up sequence (nodes mapped to claims)

| Node | Title | Claim(s) | The gate |
|---|---|---|---|
| MAE-1 | Multi-agent env + per-agent REEAgent | INV-028, ARC-047 | MECH-163 + OBJ-2 permanence + self_model stability |
| MAE-2 | Inter-agent observation / arbitration | INV-028, INV-005 | MAE-1; v4_spec V4-1 open design Qs |
| MAE-3 | Agency detection of an OTHER | MECH-095, MECH-099 | MAE-2; structurally-distinct other (EXQ-121 lacked one) |
| MAE-4 | Multi-channel coping (violence terminal) | MECH-102 | MAE-2 + V4-4 richer actions |
| MAE-5 | Axiom-conflict comparator + residue | Q-028 (+ NEWCLAIM) | MAE-3 + MAE-4 + scorable z_self |
| MAE-6 | Loneliness as architectural harm | Q-029 (+ NEWCLAIM) | MAE-2 + affect-sharing channel |
| MAE-7 | ARC-010 mirror-modelling cutover | ARC-010, INV-005 | MECH-163 + OBJ-5 + SELF-7 (DEV-NEED-021) |

---

## Phase reassignment (v4 -> v5) -- reported in generation_flags

Several seed claims are currently `implementation_phase: v3` (or untagged) in
claims.yaml but their subject is intrinsically social / relational / ethical and
they depend on the multi-agent substrate. They belong in the V5 SOCIAL tier:

- **MECH-095** (agency-detection comparator distinguishing self- from
  OTHER-caused change) -- v3 today; its EXQ-121 FAIL is partly attributable to
  having no structurally-distinct other.
- **MECH-099** (three-pathway routing; agency attribution under richer
  causation) -- v3 today; v4_spec maps it to V4-1 + V4-4.
- **MECH-102** (violence as terminal error-correction) -- substrate_ceiling
  today; the "all other channels fail" framing is social by construction.
- **Q-028** (ethics axiom-conflict resolution) -- substrate_ceiling, V4-1-bound;
  presupposes an other whose welfare conflicts with the self's.
- **Q-029** (loneliness as harm) -- substrate_ceiling, V4-1-bound; loneliness is
  unshared suffering and needs others to share-or-fail-to-share with.

**NOT flagged:** MECH-163 stays `v3` (it is the V3-completion / V4-social entry
gate, not a social claim itself). INV-005 and INV-028 are universal ethics
invariants (`invariant_type: universal`, substrate_coherence) -- they are
foundational design choices, not phase-gated implementation claims, so they are
cited as scope but carry no phase to reassign. ARC-047 is already
`implementation_phase: v4` and is genuinely the V4-leaning harness candidate.

---

## What this plan deliberately does NOT do

- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 (or V4) behaviour. The first real step (building
  `MultiAgentCausalGridWorldV4` / factoring REEAgent for N instances) is V5
  substrate and must not enter the V3 closure % nor be confused with V4
  individual-mind work.
- **It does not duplicate the V4 individual-mind plans.** Object permanence is
  owned by `object_representation_v4` (PILLAR 1 / OBJ-2); the others-as-object
  slot by OBJ-5; the self-model cutover and the INV-064/DEV-NEED-021 sequencing
  gate by `self_model_v4` (SELF-7). This plan cross-links those nodes as
  readiness gates rather than re-litigating them.
- **It does not invent social theory.** Every node maps to an existing claim.
  Two genuinely-new mechanisms surfaced by the lit verdicts (the axiom-conflict
  residue comparator for Q-028; an unshared-suffering harm channel for Q-029)
  are proposed as NEWCLAIM placeholders for the orchestrator to register, not
  asserted here.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/v4_spec.md](../../docs/architecture/v4_spec.md) section V4-1 | MultiAgentCausalGridWorldV4 substrate spec + claims-unblocked map (Q-028/Q-029/MECH-095/MECH-102) + open design questions |
| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) DEV-NEED-021 | otherness inference after self-stability; the load-bearing ordering gate |
| claims.yaml MECH-095 / MECH-099 / MECH-102 / Q-028 / Q-029 | the social claims the substrate unblocks (v4->v5 reassignment candidates) |
| claims.yaml INV-005 / INV-028 / ARC-010 / ARC-047 | the ethics invariants + mirror-modelling commitment + harness (scope, not reassigned) |
| claims.yaml MECH-163 | the V3-completion / V4-social entry gate (welfare-over-time planning; stays v3) |
| evidence/planning/object_representation_v4_plan.md (OBJ-2, OBJ-5) + self_model_v4_plan.md (SELF-7) | the V4 prerequisites cross-linked as readiness gates |

---

## Decision log

- **2026-06-10** -- Plan registered as the V5 SOCIAL forward-roadmap, the
  others tier of the self -> objects -> OTHERS -> language spine. Nodes seeded
  substrate-up: MAE-1 (multi-agent env) -> MAE-2 (arbitration/observation) ->
  MAE-3 (agency of an other) / MAE-4 (coping channels) -> MAE-5 (axiom-conflict)
  / MAE-6 (loneliness) -> MAE-7 (ARC-010 mirror-modelling capstone). Readiness
  gates pinned to MECH-163 + the two V4 individual-mind plans per DEV-NEED-021.
  `generation: v5` set so the V3 closure % is unaffected and the V4 roadmaps stay
  distinct. No claims.yaml edits.
- **2026-06-10** -- Flagged MECH-095, MECH-099, MECH-102, Q-028, Q-029 for
  v4->v5 reassignment (intrinsically social/relational/ethical, depend on the
  multi-agent substrate). MECH-163 deliberately NOT flagged (V3-completion gate).
  INV-005/INV-028 cited as universal-invariant scope, not phase-reassigned.
- **2026-06-10** -- Two NEWCLAIM placeholders proposed for orchestrator
  registration: the Q-028 context-sensitive axiom-conflict comparator + residue
  mechanism, and a Q-029 unshared-suffering harm channel. Both suggested_generation
  v5; both deferred to the decide-whether-to-build step, not asserted here.
