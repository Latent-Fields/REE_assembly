---
closure_plan:
  id: relational_harm_moral_semantics_v5
  generation: v5
  title: "Relational harm and moral semantics (harm-to-agency; love as terrain inference)"
  registered: 2026-06-10
  last_updated: 2026-06-12
  scope_claims: [MECH-129, MECH-130, MECH-164, INV-005, INV-028, MECH-127]
  sibling_plans: [multi_agent_ecology_v5, mirror_modelling_other_self_v5, self_model_v4, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. This is the V5 SOCIAL tier of the
    self -> objects -> OTHERS -> language spine (ARC-059 / DEV-NEED-021). V5 has
    no experiments, so nodes carry owner_exq: null and the drift checker stays
    dormant against them. The VALUE is the readiness_gate per node -- the
    prerequisites that must land first. For this plan those prerequisites are
    BOTH the V3-completion gate MECH-163 (multi-step hippocampal planning, the
    V4/social entry gate) AND V4-tier individual-mind work (object permanence,
    a stable self) reached via cross_plan_link to object_representation_v4 and
    self_model_v4, AND the two upstream V5 substrate plans this layer sits on
    top of: multi_agent_ecology_v5 (the env / agency substrate -- the OTHER
    must exist as an agent before its harm/care can be a semantics) and
    mirror_modelling_other_self_v5 (the inference machinery that reads the
    other's terrain). This plan is the MORAL-SEMANTICS layer ON TOP of those
    two: given other agents exist and their internal terrain is inferrable,
    what does harm to them MEAN (harm-to-agency vs harm-to-agent), how is
    novelty toward them typed so curiosity does not become chronic approach
    pressure on the dangerous, and how does care fall out of ordinary E3
    selection (love as agent-indexed terrain inference). generation: v5 keeps
    these nodes OUT of the V3 closure percentage (serve.py read_closure,
    generate_closure_snapshot.py, check_closure_drift.py are generation-aware).
    A node graduates from roadmap to closure-tracked by gaining an owner_exq
    once its first V5 experiment is queued.
  nodes:
    - id: "relational_harm_moral_semantics_v5:RHM-1"
      title: "Harm-to-agency signal: goal-interference over trajectory pairs (MECH-129), distinct from harm-to-agent"
      phase: 1
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-6, SENT-9]
        requires_welfare_review: false
        note: "Harm-to-agency (goal-interference over trajectory pairs) = Class-2 represented harm to another's agency."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-129]
      depends_on: []
      cross_plan_link: ["multi_agent_ecology_v5", "mirror_modelling_other_self_v5"]
      blocking_on: "Requires other-agent goal modelling -- the other's z_goal visible in shared state (mirror_modelling_other_self_v5) -- and a multi-agent env where trajectory pairs can collide non-physically (multi_agent_ecology_v5). MECH-129 names this a Level-3 prerequisite: cannot be implemented until MECH-128 + basic other-agent goal modelling exist."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning PASS (the V4/social entry gate; stays v3 -- it is the V3-completion gate, NOT a social claim)"
        - "Upstream V5 substrate: multi_agent_ecology_v5 supplies N agents + a goal-obstruction-without-contact scenario; mirror_modelling_other_self_v5 supplies the inferred other-z_goal that the interference signal is computed against"
        - "V3 has only harm-to-agent (SD-010 harm_bridge, SD-011 dual nociceptive streams, E3 harm eval): a cost localized to the agent's OWN trajectory. None of MECH-129's four discriminants (other's goal / obstruction / incidental-vs-constitutive / consent) are representable on self sensorimotor signals"
      last_updated: 2026-06-10
      completion_note: "MECH-129: the second harm category. A system that never collides (harm-to-agent solved) can still systematically undermine another agent's agency -- INV-028 (co-inhabitants with legitimate agency) cannot be operationally satisfied without a goal-interference signal computed over trajectory pairs and fed into E3 alongside the existing harm signal. This node is the first moral-semantics primitive; everything else in the plan presupposes it."
    - id: "relational_harm_moral_semantics_v5:RHM-2"
      title: "Agent-policy novelty typing (MECH-130): world-state novelty != agent-policy novelty"
      phase: 1
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-130]
      depends_on: []
      cross_plan_link: ["multi_agent_ecology_v5", "mirror_modelling_other_self_v5"]
      blocking_on: "Requires other agents to exist as structurally-novel entities (multi_agent_ecology_v5) and a per-agent policy model whose unpredictability can be measured separately from environmental novelty (mirror_modelling_other_self_v5). The failure mode is invisible single-agent."
      readiness_gate:
        - "MECH-111 curiosity/novelty signal is the V3 mechanism being TYPED -- it currently rewards approach to high-information states; in a single-agent world that is correct exploration reward"
        - "Upstream V5 substrate: other agents are partially-unpredictable by construction (they respond to you, carry their own goals, may maintain surface unpredictability); without typing, novelty reward chronically pulls toward the most dangerous (least predictable) agents and competes with harm avoidance on the SAME entity"
        - "Depends conceptually on RHM-1: the harm side of the conflict (harm-to-agent + harm-to-agency) must exist for the curiosity-vs-harm competition that MECH-130 prevents to be measurable"
      readiness_gate_note: "Sequenced phase 1 alongside RHM-1 because both are direct readouts on the multi-agent substrate, but RHM-2's failure is only diagnosable once RHM-1's harm semantics exist to compete with curiosity."
      last_updated: 2026-06-10
      completion_note: "MECH-130: untyped novelty reward creates chronic approach pressure toward partially-unpredictable agents regardless of harm risk. The fix is to split the novelty signal into world-state novelty (environmental features, keep rewarding) and agent-policy novelty (other agents, do NOT treat as perpetual high-information targets). A prerequisite hygiene step before love (RHM-4): you cannot weight another's terrain self-like if curiosity is independently dragging you onto them as information sources."
    - id: "relational_harm_moral_semantics_v5:RHM-3"
      title: "Consent / incidental-vs-constitutive qualifier on harm-to-agency (the discriminant layer of MECH-129)"
      phase: 2
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-12]
        requires_welfare_review: false
        note: "Consent / incidental-vs-constitutive qualifier = the refusal/permission discriminant (SENT-12 refusal channel)."
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-409"]
      depends_on: ["relational_harm_moral_semantics_v5:RHM-1"]
      cross_plan_link: ["mirror_modelling_other_self_v5"]
      blocking_on: "RHM-1 must materialise a goal-interference signal first; the qualifier discriminates WHICH interferences are morally weighted. Requires the other's commitment/consent state to be inferrable (mirror_modelling_other_self_v5)."
      readiness_gate:
        - "RHM-1 goal-interference signal exists (the thing being qualified)"
        - "MECH-129 lists four discriminants -- (1) what the other's goal is, (2) whether your action obstructs it, (3) whether the obstruction is incidental or constitutive, (4) whether the other consented. RHM-1 covers (1)+(2); this node covers (3)+(4): the difference between blocking a path the other could route around vs constitutively defeating their goal, and the difference between obstruction the other agreed to (a game, a contest) and obstruction they did not"
        - "mirror_modelling_other_self_v5 must expose an inferred other-commitment / consent state for (4); incidental-vs-constitutive (3) needs the other's full goal trajectory, not just current position"
      last_updated: 2026-06-10
      completion_note: "MECH-129 enumerates four discriminants but registers them as one mechanism; the consent / constitutive-vs-incidental qualifier is the part that turns a raw goal-interference signal into a moral signal (a contest is full obstruction yet not harm; a constitutive defeat is). This is genuinely-new capability beyond MECH-129's current statement, so it is proposed as a NEWCLAIM rather than folded silently into MECH-129. Off the V3 critical path; surfaces only once RHM-1 exists."
    - id: "relational_harm_moral_semantics_v5:RHM-4"
      title: "Love as agent-indexed terrain inference with self-like gradient weighting (MECH-164)"
      phase: 3
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9]
        requires_welfare_review: false
        note: "Love as agent-indexed terrain inference with self-like gradient weighting; care substrate."
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-164]
      depends_on:
        - "relational_harm_moral_semantics_v5:RHM-1"
        - "relational_harm_moral_semantics_v5:RHM-2"
      cross_plan_link: ["mirror_modelling_other_self_v5", "self_model_v4", "object_representation_v4"]
      blocking_on: "MECH-163 (the VTA/hippocampal planning system MECH-164 names as its planning substrate); a stable self before others (self_model_v4 + DEV-NEED-021); object persistence (object_representation_v4 OBJ-2 + OBJ-5 per-agent object-file slots) so the other whose terrain is inferred is a persistent token, not a transient percept."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning PASS -- MECH-164 explicitly requires it: 1-step greedy cannot navigate toward states that sustain another agent's goal trajectory or reduce their harm accumulation over time"
        - "mirror_modelling_other_self_v5 supplies component 1 (agent-indexed terrain instantiation: the hippocampal terrain seeded from the OTHER's goal/harm context, indexed to them not to self)"
        - "INV-005 is the negative-side precursor (harm to others enters cost via mirror modelling); MECH-164 generalises it to the FULL terrain -- both harm gradient AND goal gradient -- and makes the indexing requirement explicit. SD-011 dual-stream harm avoidance is present in V3; the missing half is agent-indexed GOAL-gradient inference + self-like weighting"
        - "DEV-NEED-021 / self_model_v4: a stable self is the prerequisite for self-like weighting -- structural symmetry in how own-terrain and other-terrain gradients are weighted presupposes a well-formed own-terrain (a stable self-model)"
      last_updated: 2026-06-10
      completion_note: "MECH-164 instantiates Axiom V: infer the other's goal+harm gradients, weight them with the SAME motivational force as one's own (not a discounted proxy), and care follows from ordinary E3 selection -- no separate ethics module (consistent with INV-001). This is the capstone moral-semantics node. It is load-bearing on RHM-1 (harm side) and RHM-2 (so curiosity is not confounding the weighting) and on the V4 individual-mind prerequisites via cross-plan link. The 'love once means love all' scope-expansion argument (Synthese Section 5) rides on this node."
    - id: "relational_harm_moral_semantics_v5:RHM-5"
      title: "Self-like weighting calibration: full-symmetry vs collapse vs callousness (the lambda the structural claim leaves open)"
      phase: 4
      status: blocked
      ethical_metadata:
        welfare_relevance: moderate
        applicable_ethics_gates: [SENT-9, SENT-13]
        requires_welfare_review: false
        note: "Self-like weighting calibration (full-symmetry vs collapse vs callousness) = a welfare-relevant tuning fork."
      severity: high
      owner_exq: null
      unblocks_claims: ["MECH-410"]
      depends_on: ["relational_harm_moral_semantics_v5:RHM-4"]
      cross_plan_link: ["mirror_modelling_other_self_v5"]
      blocking_on: "RHM-4 must land the structural mechanism (other-terrain enters E3) before its weighting can be calibrated. DEV-NEED-022 (empathy coupling calibration) names the same gap from the developmental side."
      readiness_gate:
        - "RHM-4 agent-indexed terrain inference live (the thing being weighted)"
        - "MECH-164 asserts structural symmetry (other-gradients weighted like own) but does NOT specify the developmental schedule: full self-like weighting from day one risks empathic collapse (overwhelm), too-low weighting is callousness. DEV-NEED-022 frames the same as lambda_empathy / v_other_veto calibration"
        - "Requires a per-agent inferred-confidence signal (mirror_modelling_other_self_v5) so weighting can scale with how well the other's terrain is actually inferred -- self-like weighting on a badly-inferred terrain is mis-attributed care (DEV-NEED-021 warns against empathy toward unstable targets)"
      last_updated: 2026-06-10
      completion_note: "MECH-164 fixes the STRUCTURE (symmetry) but the WEIGHT/SCHEDULE is open: how tightly does other-terrain couple, and how does it tighten over development without collapse or callousness. DEV-NEED-022 captures it as a developmental need but no claim operationalises the calibration mechanism. Proposed as NEWCLAIM (the calibration rule, not a restatement of MECH-164). Sequenced last; presupposes the structural mechanism exists to be calibrated."
    - id: "relational_harm_moral_semantics_v5:RHM-6"
      title: "Biology grounding for relational harm + love-as-care (harm-to-agency, ToM-of-goals, empathy-as-shared-circuit lit-pulls)"
      phase: 2
      status: closed
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-129, MECH-164]
      depends_on: []
      cross_plan_link: []
      governance_2026_06_12: >
        CLOSED by /lit-pull (IGW-20260612-167). Biology-grounding pull filed under
        evidence/literature/targeted_review_relational_harm_love_as_care/ (5 entries),
        rebuilt index -> MECH-129 literature_confidence 0.0 -> 0.80, MECH-164
        literature_confidence 0.0 -> 0.805. Coverage by strand: L2 ToM-of-goals
        grounded by Woodward 1998 (goal-object encoding, separable from sensorimotor
        path; MECH-129 prereq a / discriminant 1) + Gergely & Csibra 2003 (teleological
        stance / principle of rational action; the goal-inference rule, discriminant 2)
        + Baker, Saxe & Tenenbaum 2009 (inverse planning -- the computational
        instantiation of goal inference; bridges MECH-129 obstruction-detection AND
        MECH-164 component-1 agent-indexed terrain inference). L3 empathy-as-shared-circuit
        grounded by Singer et al. 2004 (empathy for pain re-uses the SELF's affective
        valuation code in AI/rostral-ACC; the negative-side self-like-weighting substrate)
        + Preston & de Waal 2002 (Perception-Action Model -- the proximate mechanism of
        MECH-164's self-like weighting, plus the similarity/familiarity/salience modulators
        that pre-figure the RHM-5 calibration variable). L1 harm-to-agency-as-distinct-from-
        physical-harm is grounded INDIRECTLY (the goal-representation + obstruction-detection
        substrate from L2 is the prerequisite for a goal-interference cost) and cross-checks
        cleanly against the existing targeted_review_blocked_agency_anger_stream dir, which
        already holds the frustration / blocked-goal literature from the OBSERVER's own side
        (CANDIDATE-blocked-agency-stream / SD-029, not MECH-129) -- so this pull extends
        rather than re-derives. RESIDUAL (does not block close): a dedicated paper treating
        goal-obstruction as a distinct AVERSIVE/cost signal toward another (vs the agency
        substrate) would further strengthen L1; surface it during the RHM-1 substrate-build
        session if the goal-interference signal needs sharper grounding. No claims.yaml
        edits (V5 candidate claims unchanged; lit and exp are decoupled signals -- this pull
        moves literature_confidence only, not experimental_confidence or status).
      readiness_gate:
        - "Project rule feedback_biology_before_formal_definitions: MECH-129 (harm-to-agency), MECH-130 (agent-policy novelty), MECH-164 (agent-indexed terrain inference) instantiate formal concepts (goal-interference, information-gain typing, Axiom V) and need a biology lit-pull BEFORE V5 substrate is built"
        - "L1 harm-to-agency / goal-obstruction as distinct from physical harm (developmental-harm + frustration / blocked-goal literature); L2 ToM-of-goals (Woodward goal-attribution, Csibra & Gergely teleological stance) -- shared anchor with the social pillar; L3 empathy as shared-circuit / self-other gradient overlap (Decety, Singer pain-empathy, Preston & de Waal perception-action model) for MECH-164"
        - "Cross-check against existing INV-005 / INV-028 source docs (2026-02-09_empathy.md, otherness_inference.md) so the pull extends rather than re-derives"
      last_updated: 2026-06-12
      completion_note: "MECH-129/130/164 carry no dedicated biology lit-pull. This node tracks closing that grounding debt before the V5 moral-semantics substrate is built. Distinct from the social-substrate pull (multi_agent_ecology_v5) and the mirror-inference pull (mirror_modelling_other_self_v5): this one is specifically the harm-SEMANTICS and empathy-circuit literature, not the agency or inference machinery. CLOSED 2026-06-12 -- see governance_2026_06_12 above (5 entries; MECH-129 + MECH-164 grounded across the ToM-of-goals and empathy-as-shared-circuit strands)."
---
# Relational Harm and Moral Semantics -- V5 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** the moral-semantics layer that sits ON TOP of the V5 multi-agent
substrate -- given that other agents exist and their internal terrain is
inferrable, define what harm to them MEANS (harm-to-agency vs harm-to-agent;
MECH-129), how novelty toward them is typed so curiosity does not become
chronic approach on the dangerous (MECH-130), and how care falls out of
ordinary E3 selection (love as agent-indexed terrain inference; MECH-164).

This is the **V5 SOCIAL tier** of the `self -> objects -> OTHERS -> language`
spine (ARC-059 / DEV-NEED-021). Otherness inference REQUIRES object-permanence
and a stable self, both V4 -- so every node here is gated on V4 individual-mind
work via cross-plan link, on the V3-completion gate MECH-163, and on the two
upstream V5 substrate plans. It is a *forward roadmap*, not a closure map: V5
has no experiments yet, so nodes carry no `owner_exq` and the drift checker
stays dormant. The value is the **readiness gates** -- for each moral-semantics
primitive, exactly which prerequisites must land first.

---

## One-line framing

> Harm and care already have a NEGATIVE-side precursor in REE (INV-005: harm to
> others enters the cost function via mirror modelling; SD-011 dual nociceptive
> streams give the agent harm sensitivity for itself). What is NOT done is the
> RELATIONAL semantics: a second harm category for goal-obstruction without
> contact (MECH-129), a typing of novelty so other-agents are not perpetual
> curiosity targets (MECH-130), and the positive-side capstone -- inferring the
> WHOLE of another's terrain (goal AND harm gradients) and weighting it
> self-like so that care is just ordinary E3 selection (MECH-164). These are
> V5: they presuppose other agents (multi_agent_ecology_v5), an inference
> engine to read them (mirror_modelling_other_self_v5), and the V4 prerequisites
> of object-permanence + a stable self.

---

## The moral-semantics layer (mapped to nodes)

| Primitive | Node | Claim | Phase leaning | The readiness gate |
|---|---|---|---|---|
| harm-to-agency signal | RHM-1 | MECH-129 | V5 (blocked) | MECH-163 + multi-agent env + inferred other-z_goal |
| agent-policy novelty typing | RHM-2 | MECH-130 | V5 (blocked) | MECH-111 split into world- vs agent-policy novelty |
| consent / constitutive qualifier | RHM-3 | NEWCLAIM | V5 (blocked) | RHM-1 signal + inferred other-commitment state |
| love as terrain inference | RHM-4 | MECH-164 | V5 (blocked, capstone) | MECH-163 + stable self + object persistence + RHM-1/RHM-2 |
| self-like weight calibration | RHM-5 | NEWCLAIM | V5 (blocked) | RHM-4 structure + DEV-NEED-022 lambda gap |
| biology grounding debt | RHM-6 | MECH-129/164 | cross-cutting | harm-to-agency / ToM-of-goals / empathy-circuit pulls |

---

## Boundary with the two upstream V5 plans

This plan is deliberately the **semantics**, not the **substrate** or the
**inference engine**:

- **`multi_agent_ecology_v5`** owns the env / agency substrate -- N agents, the
  shared consequence space, the predator/co-inhabitant scenarios. The OTHER
  must exist as an agent there before its harm/care can be a semantics here.
- **`mirror_modelling_other_self_v5`** owns the inference machinery -- reading
  the other's z_goal / harm sensitivities / commitment state, agent-indexed
  terrain instantiation (MECH-164 component 1). This plan CONSUMES that
  inferred terrain; it does not build it.
- **This plan** owns the harm/care SEMANTICS over those two: what a goal
  collision MEANS (RHM-1/RHM-3), how curiosity toward agents is typed
  (RHM-2), and how the inferred terrain is weighted into E3 to produce care
  (RHM-4/RHM-5).

---

## What this plan deliberately does NOT pull into V3 (or claim to own)

- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour. SD-011 harm avoidance stays the V3 harm
  story; no harm-to-agency signal, no novelty typing, no agent-indexed terrain
  enters V3. The first real substrate step is V5 and must not enter V3 closure.
- **MECH-163 stays v3.** It is the V3-completion / V4-entry gate cited as a
  readiness prerequisite, NOT a social claim. It is not flagged for
  reassignment.
- **The agency substrate and the inference engine are NOT duplicated here.**
  multi_agent_ecology_v5 and mirror_modelling_other_self_v5 own them; this plan
  cross-links rather than restating MECH-031/032/036/041 or the env design.
- **The V4 individual-mind prerequisites are someone else's nodes.** Object
  permanence (object_representation_v4 OBJ-2) and a stable self
  (self_model_v4 + object_representation_v4 OBJ-3) are cross-plan links, not
  nodes here -- DEV-NEED-021 makes them prerequisites, not deliverables of the
  moral layer.

---

## Reassignment flags (v4 -> v5)

The three seed mechanisms are currently `implementation_phase: v4` in
claims.yaml but are intrinsically SOCIAL / relational / ethical -- their
subject matter does not exist until the multi-agent substrate exists. They
belong in the V5 SOCIAL tier, not the V4 individual-mind tier:

- **MECH-129** (harm-to-agency = obstruction of another agent's goal-pursuit):
  the claim itself states it "cannot be implemented until ... basic other-agent
  goal modelling exist[s]" -- a multi-agent prerequisite. Subject:
  `coherence.relational_harm`.
- **MECH-130** (agent-policy novelty typing): the failure mode is defined
  entirely over OTHER agents as structurally-novel entities; invisible
  single-agent. Subject: `curiosity.agent_novelty_typing`.
- **MECH-164** (love as agent-indexed terrain inference): instantiates Axiom V
  over OTHER agents' terrain; its own evidence note says it "awaits V4 social
  extension substrate" -- i.e. the social/multi-agent layer, which this
  partition assigns to V5. Subject: `love.agent_indexed_terrain_inference`.

These are reported in `generation_flags[]`. MECH-163 is NOT flagged (V3
completion gate). No claims.yaml edits are made by this plan.

---

## New capabilities proposed (not registered here)

Two nodes surface genuinely-new capability beyond the seed claims' current
statements; both are returned in `proposed_claims[]` for the orchestrator to
register (with real IDs replacing the NEWCLAIM placeholders):

- **`obstruction_consent_qualifier`** (RHM-3): MECH-129 enumerates four
  discriminants but registers them as one mechanism; the consent /
  constitutive-vs-incidental qualifier that turns a raw goal-interference
  signal into a MORAL signal is distinct mechanism, not a restatement.
- **`self_like_weight_calibration`** (RHM-5): MECH-164 fixes the STRUCTURE
  (self-like symmetry) but leaves the WEIGHT/SCHEDULE open; DEV-NEED-022 names
  the gap but no claim operationalises the calibration. The calibration rule
  (how coupling tightens over development without collapse or callousness) is
  new.

---

## Source artefacts

| Artefact | Role |
|---|---|
| claims.yaml MECH-129 / MECH-130 / MECH-164 | the three seed mechanisms (all `implementation_phase: v4`, flagged -> v5) |
| docs/architecture/harm.md#mech-129 | harm-to-agency definition + four discriminants |
| docs/architecture/curiosity.md#mech-130 | agent-policy novelty typing + three failure modes |
| docs/thoughts/2026-03-24_MULTIAGENT_VALENCE_AVERSIVE_COMPLEXITY.md | source for MECH-129/130 |
| claims.yaml INV-005 / INV-028 | the negative-side precursor + shared-world ethics invariant (universal; readiness, not nodes) |
| docs/architecture/developmental_needs_register.md DEV-NEED-021 / DEV-NEED-022 | self-stability-before-otherness gate + empathy-coupling-calibration gap |
| evidence/planning/self_model_v4_plan.md / object_representation_v4_plan.md | the V4 individual-mind prerequisites (cross-plan links) |
| MECH-164 notes (Synthese/Minds+Machines Axiom V derivation) | "love once means love all" scope-expansion argument |

---

## Decision log

- **2026-06-10** -- Plan registered as a V5 SOCIAL-tier forward-roadmap, sibling
  to `multi_agent_ecology_v5` (agency substrate) and
  `mirror_modelling_other_self_v5` (inference engine), with V4 cross-links to
  `self_model_v4` + `object_representation_v4` (DEV-NEED-021 prerequisites).
  Six nodes: RHM-1 (MECH-129 harm-to-agency), RHM-2 (MECH-130 novelty typing),
  RHM-3 (consent/constitutive qualifier, NEWCLAIM), RHM-4 (MECH-164 love as
  terrain inference, capstone), RHM-5 (self-like weight calibration, NEWCLAIM),
  RHM-6 (biology grounding debt). Readiness gates pinned per node.
  `generation: v5` set so the V3 closure % is unaffected. No claims.yaml edits.
- **2026-06-12** -- RHM-6 biology-grounding debt CLOSED via /lit-pull
  (IGW-20260612-167). Filed 5 entries under
  `evidence/literature/targeted_review_relational_harm_love_as_care/`:
  ToM-of-goals strand (Woodward 1998 goal-object encoding; Gergely & Csibra 2003
  teleological stance; Baker, Saxe & Tenenbaum 2009 inverse planning) grounding
  MECH-129's goal-representation + obstruction-detection substrate and MECH-164's
  agent-indexed terrain inference (component 1); empathy-as-shared-circuit strand
  (Singer et al. 2004 shared affective pain code; Preston & de Waal 2002
  Perception-Action Model) grounding MECH-164's self-like weighting and surfacing
  the RHM-5 calibration modulators. Index rebuilt: MECH-129 literature_confidence
  0.0 -> 0.80, MECH-164 0.0 -> 0.805. L1 (harm-to-agency vs physical harm) grounded
  indirectly via the goal-inference substrate + cross-check against the existing
  `targeted_review_blocked_agency_anger_stream` dir (observer-side frustration /
  blocked-goal literature, tagged to CANDIDATE-blocked-agency-stream / SD-029, not
  MECH-129) -- the pull extends rather than re-derives. No claims.yaml edits (lit/exp
  decoupled; this moves literature_confidence only). RHM-6 status open -> closed.
- **2026-06-10** -- Flagged MECH-129 / MECH-130 / MECH-164 for v4 -> v5
  reassignment (intrinsically social/relational/ethical; subject matter does
  not exist until the multi-agent substrate exists). MECH-163 deliberately NOT
  flagged -- it is the V3-completion gate. Area assessed as MOSTLY REAPED: the
  three seed mechanisms are registered; two new capabilities (consent qualifier,
  weight calibration) are proposed rather than folded silently into MECH-129/164.
