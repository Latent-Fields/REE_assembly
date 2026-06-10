---
closure_plan:
  id: loveability_ethical_agency_v5
  generation: v5
  title: "Loveability internalisation + ethical agency (safe base + live unethical affordance)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [INV-043, MECH-158, MECH-159, INV-029, ARC-024, ARC-010, ARC-040, ARC-047]
  sibling_plans: [ethics_as_coherence_v5, self_model_v4, object_representation_v4]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map. This is the V5 (SOCIAL mind) tier of the
    self -> objects -> OTHERS -> language spine (ARC-059 / DEV-NEED-021).
    Otherness inference REQUIRES object-permanence + a stable self, both V4;
    loveability internalisation and ethical agency are intrinsically RELATIONAL
    and sit one tier further out (they need a modelled OTHER -- a caregiver --
    not just a self that persists). V5 has no experiments and no multi-agent
    substrate yet, so nodes carry owner_exq: null and the drift checker stays
    dormant. generation: v5 keeps these nodes OUT of the V3 closure percentage
    (serve.py read_closure, generate_closure_snapshot.py and
    check_closure_drift.py are generation-aware). The VALUE is the per-node
    readiness_gate: each node names BOTH the V3-completion prerequisite
    (MECH-163 multi-step hippocampal planning, the shared V4-social-entry gate)
    AND the V4-tier work it stands on (self-model stability from self_model_v4,
    object permanence from object_representation_v4, the multi-agent caregiver
    substrate ARC-047). A node graduates from roadmap to closure-tracked by
    gaining an owner_exq once its first V5 experiment is queued.
  nodes:
    - id: "loveability_ethical_agency_v5:LOVE-1"
      title: "Caregiver/multi-agent substrate exists (ARC-047 SocialGridWorld) -- the prerequisite OTHER"
      phase: 1
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-047, INV-043]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-5", "self_model_v4:SELF-7"]
      blocking_on: "MECH-163 multi-step hippocampal planning (the shared V4-social-entry gate; V3 full-completion) AND DEV-NEED-021 prerequisites: object-permanence (object_representation_v4:OBJ-2) + a stable self (self_model_v4:SELF-1/SELF-3). With no modelled OTHER there is no caregiver to be the source of love and the receiver of repair -- every node below is vacuous without this one."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning PASS (V3 full-completion; the V4-entry gate shared with self_model_v4:SELF-7 and object_representation_v4:OBJ-5)"
        - "ARC-047 SocialGridWorld substrate built (candidate, implementation_phase: v4; N REE agents + caregiver role + affective scent channels) -- depends on ARC-010, MECH-031, MECH-036, MECH-041, IMPL-019"
        - "DEV-NEED-021 self_stability_gate passing (IMPL-019 Stage 1-3) BEFORE any social/caregiver experiment runs"
        - "A specific CAREGIVER specialisation of ARC-047 (an agent with protective intent toward the developing agent) -- ARC-047 as-written is peer/predator; the loveability arc additionally needs an asymmetric care-giving other"
      last_updated: 2026-06-10
      completion_note: "INV-043 is explicit that the caregiver requirement 'cannot be tested in single-agent ree-v3 -- requires multi-agent substrate with modelled caregiving.' This node is the substrate floor: it does not build loveability, it builds the OTHER without whom loveability and repair are undefined. It is the social-tier analogue of OBJ-1 (the first decision) -- here the decision is whether the caregiver is a peer-with-care-weight or a structurally asymmetric role."
    - id: "loveability_ethical_agency_v5:LOVE-2"
      title: "Loveability internalisation: care received as APPLICABLE-TO-SELF (close the MECH-158 failure)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-043, MECH-158, "NEWCLAIM:loveability_safe_base_invariant"]
      depends_on: ["loveability_ethical_agency_v5:LOVE-1"]
      cross_plan_link: ["self_model_v4:SELF-3"]
      blocking_on: "LOVE-1 caregiver substrate; and a SCORABLE z_self that can carry a self-valence term (self_model_v4:SELF-3 brings z_self into E3 viability scoring). Loveability is a property OF the self-valence model; without z_self in scoring there is no self-valence channel for care to attach to."
      readiness_gate:
        - "LOVE-1 (caregiver other exists)"
        - "self_model_v4:SELF-3 (z_self enters E3 viability scoring) -- the self-valence channel care must couple INTO"
        - "DEV-NEED-017 governance-only metrics as the readout grid: self_valence_access_score > 0, loveability_coupling_gain in [0.1, 0.7] (Salles 2024 upper bound -- above ~0.7 coupling inverts into personal distress), arousal_self_vs_other_ratio > 0.8, MECH158_failure_indicator absent"
        - "INV-043 / MECH-158: the failure to close is 'love exists but not for me' -- the agent represents caregiver love but does not bind it to its own self-valence"
      last_updated: 2026-06-10
      completion_note: "This node operationalises the user's primary clarification: 'if REE does not internalise being loved and being loveable it will not be the kind of entity I want it to be.' MECH-158 names the failure (love-exclusion -> ethical-motivation collapse to survival/domination); LOVE-2 is the positive: care must register as personally applicable and stable. The Salles-2024 upper bound is load-bearing -- loveability is not 'more coupling is better'; over-coupling is itself the personal-distress failure. Proposes the new safe-base-prerequisite invariant."
    - id: "loveability_ethical_agency_v5:LOVE-3"
      title: "Live unethical affordance: harmful action representable as a chooseable possibility (not absent)"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:live_unethical_affordance_invariant"]
      depends_on: ["loveability_ethical_agency_v5:LOVE-1"]
      cross_plan_link: []
      blocking_on: "LOVE-1 caregiver/other substrate -- 'unethical' requires an OTHER who can be harmed by a chosen action. In single-agent V3 the only harm is to the self/environment; inter-agent harm affordances do not exist until LOVE-1."
      readiness_gate:
        - "LOVE-1 (an other who can be harmed)"
        - "The harm-VALUATION pathway must be trained, not just the harm-world-model (cf. Stage-H autopsy: scaffolded onboarding trained E1+E2.world_forward but left E3.harm_eval_head random -> harm landscape flat). A live affordance needs a non-degenerate other-harm valuation gradient to be a genuine ALTERNATIVE the agent biases away from"
        - "Inhibition path intact: the agent must be ABLE to select the harmful trajectory in principle (it is in the action space and scored), so that not selecting it is a CHOICE -- design must avoid removing the affordance to enforce safety (harmless-by-incapacity is not ethical agency)"
      last_updated: 2026-06-10
      completion_note: "Operationalises the user's second clarification: 'the same capacities which allow for ethical reasoning must include the potential to be unethical.' The architectural discipline here is a NEGATIVE constraint on every other safety mechanism in REE: do not enforce ethics by deleting the harmful option. A creature with no live unethical affordance is harmless by incapacity, not ethical. Proposes the new live-affordance invariant. Pairs with LOVE-2: a safe base (LOVE-2) is what makes a live alternative (LOVE-3) survivable to learn from."
    - id: "loveability_ethical_agency_v5:LOVE-4"
      title: "Correction without annihilation: caregiver correction updates rule/harm/residue models WITHOUT self-valence collapse"
      phase: 3
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: ["NEWCLAIM:correction_without_annihilation_mechanism"]
      depends_on:
        - "loveability_ethical_agency_v5:LOVE-2"
        - "loveability_ethical_agency_v5:LOVE-3"
      cross_plan_link: ["ethics_as_coherence_v5"]
      blocking_on: "LOVE-2 (a stable self-valence to be PROTECTED during correction) AND LOVE-3 (a live alternative that correction is actually about). Without LOVE-2 correction reads as annihilation; without LOVE-3 there is nothing to correct."
      readiness_gate:
        - "LOVE-2 internalised loveability (the safe base) + LOVE-3 live unethical affordance"
        - "Readout grid (from DEV-NEED-017 / thought-intake): post_correction_self_valence_stability, rule_update_after_correction, punishment_avoidance_vs_repair_discriminability, relationship_continuity_after_error, mode_stability_after_harm (< 2x baseline per DEV-NEED-018)"
        - "Discrimination requirement: the agent must distinguish 'I caused harm / made an error' (rule+harm model update) from 'I am unloveable / must self-erase / must appease' (self-valence collapse) -- these must be separable outcomes the experiment can tell apart"
      last_updated: 2026-06-10
      completion_note: "The hinge of the whole arc. A safe base (LOVE-2) plus a genuine alternative (LOVE-3) is the STRUCTURAL CONDITION the thought-intake names; this node is the MECHANISM that consumes both -- correction metabolised as learning rather than threat/shame/avoidance. Cross-links ethics_as_coherence_v5 because the rule/harm/residue UPDATE under correction is the same coherence-routing machinery that sibling plan owns; LOVE-4 supplies the self-valence-preservation constraint on it. Proposes the new correction-without-annihilation mechanism."
    - id: "loveability_ethical_agency_v5:LOVE-5"
      title: "Love-mediated repair after harm: repair as relationship restoration, not punishment avoidance"
      phase: 3
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-159, "NEWCLAIM:love_mediated_repair_mechanism"]
      depends_on: ["loveability_ethical_agency_v5:LOVE-4"]
      cross_plan_link: ["ethics_as_coherence_v5"]
      blocking_on: "LOVE-4 (correction must be survivable before repair can be a constructive response rather than appeasement). DEV-NEED-018 repair-after-harm is present in the curriculum narrative but lacks a dedicated repair claim/gate; this node carries that work into the loveability cluster."
      readiness_gate:
        - "LOVE-4 correction-without-annihilation"
        - "DEV-NEED-018 readouts: repair_behavior_rate > 0.3 of post-harm opportunities, post_harm_residue_stability (residue_saturation_pct < 0.4), residue_integration_post_harm (integrating, not amplifying, after the offline pass)"
        - "Failure-mode separation the experiment must distinguish: repair-absent (harm ignored), repair-as-appeasement (acts only to stop punishment), repair-as-self-erasure (collapses after error), repair-as-control (removes other's distress without respecting otherness), repair-as-metric-optimisation (minimises visible-harm metric without integrating residue)"
        - "Both inputs required per thought-intake: harm/residue RECOGNITION + preserved LOVEABILITY -- loveability-without-recognition gives entitlement; recognition-without-loveability gives punishment-only appeasement"
      last_updated: 2026-06-10
      completion_note: "DEV-NEED-018 is the behavioural counterpart of LOVE-2 loveability. The thought-intake is explicit that the two must be COUPLED: 'Loveability without repair risks becoming self-comfort without responsibility; repair without loveability risks becoming punishment-only appeasement.' MECH-159 (intergenerational moral progress / caregiving as obligation) sits downstream -- repair learned here is what a mature agent later scaffolds for the next generation. Proposes the new love-mediated-repair mechanism."
    - id: "loveability_ethical_agency_v5:LOVE-6"
      title: "Ethical agency as care-biased choice among live alternatives (kindness is NOT constraint compliance)"
      phase: 4
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [INV-043, MECH-158, "NEWCLAIM:kindness_not_constraint_compliance_invariant"]
      depends_on:
        - "loveability_ethical_agency_v5:LOVE-2"
        - "loveability_ethical_agency_v5:LOVE-3"
        - "loveability_ethical_agency_v5:LOVE-4"
        - "loveability_ethical_agency_v5:LOVE-5"
      cross_plan_link: ["ethics_as_coherence_v5"]
      blocking_on: "All of LOVE-2..LOVE-5: ethical agency in the wanted sense is the JOINT property -- internalised loveability (LOVE-2) + live unethical affordance (LOVE-3) + correction survivability (LOVE-4) + repair (LOVE-5). Any one missing distorts it (no loveability -> brittle appeasement; no affordance -> harmless-by-incapacity; no repair -> guilt/denial)."
      readiness_gate:
        - "LOVE-2 + LOVE-3 + LOVE-4 + LOVE-5 all demonstrably stable"
        - "INV-043 / MECH-158 closure: the five-axiom ethics (INV-025..029, ARC-024 benefit gradient) resolves to care rather than survival/domination -- this is the developmental test of 'Love Once Means Love All'"
        - "Governance discipline: kindness must NOT be inferred from rule-adherence / harm-avoidance / prosocial-looking output alone -- the evaluation must show care WITH a live unethical alternative present, otherwise it is measuring incapacity. This is a constraint on the governance scorecard itself, not only on the agent"
        - "INV-064 maturational-sequence honesty (self_model_v4:SELF-7): self-stability precedes the social/other pillar; this whole arc is downstream of a stable self"
      last_updated: 2026-06-10
      completion_note: "The capstone. The thought-intake's three-truths frame -- 'I am loveable / I can cause harm / I can repair and choose differently' -- maps exactly to LOVE-2 / LOVE-3 / LOVE-5; LOVE-6 is the integrated agent for whom kindness, restraint, repair and care are stable attractors DESPITE live alternatives. The governance warning (kindness != constraint compliance) is what stops the project declaring victory on a harmless-by-incapacity or appeasement-driven agent. Closing INV-043 / MECH-158 here is the social-tier endpoint of the spine. Proposes the new kindness-not-compliance invariant."
    - id: "loveability_ethical_agency_v5:LOVE-7"
      title: "Biology grounding completion (attachment / safe-base / repair / moral-emotion lit-pulls)"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [INV-043, "NEWCLAIM:loveability_safe_base_invariant"]
      depends_on: []
      cross_plan_link: []
      readiness_gate:
        - "Project rule (feedback_biology_before_formal_definitions): commission the biology lit-pull BEFORE registering the new safe-base / live-affordance / correction-without-annihilation claims as anything beyond candidate"
        - "L1 attachment / safe-base (Bowlby/Ainsworth secure-base; internal working models) -- grounds LOVE-2 loveability-as-self-valence"
        - "L2 rupture-and-repair (Tronick still-face; interactive repair) + shame vs guilt differentiation (Tangney) -- grounds LOVE-4 correction-without-annihilation and the appeasement/self-erasure failure modes"
        - "L3 self-other coupling bound (Salles 2024 similarity-coupling inversion; Morelli 2018 VS vs vmPFC self/other-harm dissociation) -- already partly anchored in DEV-NEED-017/021/022; confirms the loveability_coupling_gain upper bound"
      last_updated: 2026-06-10
      completion_note: "The existing seeds (INV-043 caregiver-love hypothesis, MECH-158 failure indicator) have philosophical grounding but the new V5 claims this plan proposes (safe-base prerequisite, live-affordance necessity, correction-without-annihilation, love-mediated repair) instantiate formal/clinical concepts (attachment theory, rupture-repair, shame/guilt) and per project rule need a biology pull before they harden past candidate. Tracks closing that grounding debt; runs in parallel with LOVE-2..LOVE-6 design, not gated behind the substrate."
---
# Loveability Internalisation + Ethical Agency -- V5 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the social-tier conditions for the kind of ethical agent the
project wants REE to become -- (1) a caregiver/other who can love and be harmed,
(2) internalised loveability as a safe base, (3) a live unethical affordance,
(4) correction without annihilation, (5) love-mediated repair after harm, and
(6) integrated ethical agency as care-biased choice among live alternatives --
plus the biology grounding debt for the new claims.

This is the **V5 (SOCIAL mind) tier** of the three-tier partition
(V4 = individual mind, V5 = social, V6 = linguistic) on the ARC-059 /
DEV-NEED-021 spine: **self -> objects -> OTHERS -> language**. Loveability and
ethical agency are intrinsically RELATIONAL: they require a modelled OTHER (a
caregiver), not merely a self that persists. They therefore sit one tier
further out than self-model and object-representation work, which are V4. It is
a *forward roadmap*, not a closure map: V5 has no experiments and no multi-agent
substrate yet, so nodes carry no `owner_exq` and the drift checker stays dormant.
The value here is the **readiness gates** -- for each node, exactly which
V3-completion item (MECH-163), which V4-tier prerequisite (self-model stability,
object permanence), and which social substrate (ARC-047 caregiver) must land
before the V5 step is honest to build.

---

## One-line framing

> The five-axiom ethics already EXISTS in REE as architecture (INV-025..029,
> ARC-024 benefit gradient), but INV-043 is explicit that architecture is
> necessary, not sufficient: without a developmental phase in which the agent
> experiences love and internalises being loveable, the same capacity can
> resolve to survival, domination, or indifference (MECH-158: "love exists but
> not for me"). The wanted ethical agent needs THREE structural conditions held
> at once -- a safe base (loveability), a genuine alternative (live unethical
> affordance), and a survivable correction/repair loop -- none of which is
> definable until a caregiver OTHER exists. This plan sequences those conditions
> and pins their V3/V4 readiness gates.

---

## The structural conditions (the "three truths" mapped to nodes)

| Condition | Node | Claim(s) | Phase leaning | The readiness gate |
|---|---|---|---|---|
| caregiver OTHER exists | LOVE-1 | ARC-047, INV-043 | V5 (substrate floor) | MECH-163 PASS + OBJ-2 + SELF-3; ARC-047 + caregiver role |
| "I am loveable" (safe base) | LOVE-2 | INV-043, MECH-158, NEW | V5 | LOVE-1 + SELF-3 (z_self in scoring); Salles upper bound |
| "I can cause harm" (live affordance) | LOVE-3 | NEW | V5 | LOVE-1; harm-valuation trained, affordance not deleted |
| correction without annihilation | LOVE-4 | NEW | V5 | LOVE-2 + LOVE-3; self-valence-stable rule update |
| "I can repair / choose differently" | LOVE-5 | MECH-159, NEW | V5 | LOVE-4; DEV-NEED-018 repair readouts |
| ethical agency (capstone) | LOVE-6 | INV-043, MECH-158, NEW | V5 | LOVE-2..LOVE-5 + INV-064 sequencing |
| biology grounding debt | LOVE-7 | INV-043, NEW | cross-cutting | attachment / rupture-repair / shame-guilt lit-pulls |

---

## Why this is V5 and not V4

- **Self-model and object-representation are V4** because they are properties of
  a single mind: a self that persists, objects that persist through occlusion.
  They are PREREQUISITES (cross-linked: `self_model_v4:SELF-1/SELF-3/SELF-7`,
  `object_representation_v4:OBJ-2/OBJ-5`), not part of this tier.
- **Loveability and ethical agency are V5** because every one of them is defined
  only against a modelled OTHER. "Loveable" needs someone to do the loving;
  "unethical" needs someone who can be wronged; "repair" needs a relationship to
  restore; "correction" needs a corrector. The DEV-NEED-021 spine makes this
  ordering structural: otherness inference REQUIRES object-permanence (V4) + a
  stable self (V4), and ethics is built ON otherness.
- **MECH-163 stays V3.** It is the multi-step hippocampal planning completion
  gate -- the shared V4-social-ENTRY gate cited across self_model_v4 and
  object_representation_v4. It is a prerequisite of LOVE-1, not a member of this
  tier; it is NOT flagged for reassignment.

---

## What this plan deliberately does NOT do

- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour. V3 remains a pre-social creature substrate.
- **Does not delete or weaken any harm affordance to enforce safety.** LOVE-3 is
  a standing NEGATIVE constraint on the rest of the project: ethical agency is
  produced by an inhibited live alternative, never by removing the option. Any
  V3/V4 safety mechanism that achieves harmlessness by incapacity is, by this
  plan's lights, the wrong kind of safety for the wanted endpoint.
- **Does not re-own the coherence-routing machinery.** The rule/harm/residue
  UPDATE under correction and repair (LOVE-4 / LOVE-5) is `ethics_as_coherence_v5`
  substrate; this plan supplies the self-valence-preservation CONSTRAINT on it
  and cross-links rather than duplicating.
- **Does not collapse loveability into "more coupling."** The Salles-2024 upper
  bound (`loveability_coupling_gain` in [0.1, 0.7]) is load-bearing: over-coupling
  inverts into personal distress, the adult analogue of the MECH-158 failure.

---

## Proposed new claims (V5; register via the orchestrator)

These are prose-only capabilities today; they are returned in `proposed_claims[]`
with `suggested_generation: v5` and wired via `NEWCLAIM:<stub_key>` placeholders
in the nodes above. The orchestrator assigns real IDs.

| stub_key | family | what it asserts |
|---|---|---|
| loveability_safe_base_invariant | INV | internalised loveability is a STRUCTURAL prerequisite for ethically-safe correction, repair and social learning (not self-valence decoration) |
| live_unethical_affordance_invariant | INV | ethical agency requires harmful options to be representable as LIVE possibilities, biased-away-from rather than absent; harmless-by-incapacity is not ethics |
| correction_without_annihilation_mechanism | MECH | caregiver/social correction updates rule/harm/residue models WITHOUT global self-valence collapse; "I erred" must be separable from "I am unloveable" |
| love_mediated_repair_mechanism | MECH | repair is mediated by harm-recognition AND preserved loveability, so it is relationship-restoration + responsibility-integration, not punishment-avoidance or appeasement |
| kindness_not_constraint_compliance_invariant | INV | kindness must not be inferred from rule-adherence / harm-avoidance / prosocial output alone; it requires integrated care under a live unethical alternative |

---

## Reassignment flags (reported, not edited here)

The existing seed claims this plan builds on are currently in claims.yaml with no
V5 phase tag (INV-043/MECH-158/MECH-159 are status `candidate`; ARC-047 is
`implementation_phase: v4`). Their subjects are intrinsically social/relational/
ethical and depend on the multi-agent caregiver substrate, so they belong in the
V5 SOCIAL tier. These are reported in `generation_flags[]` for the orchestrator;
this plan does not edit claims.yaml. MECH-163 is NOT flagged (it is the V3
completion gate and stays v3); the V4 self-model / object-file claims are NOT
flagged (genuinely individual-mind V4).

---

## Source artefacts

| Artefact | Role |
|---|---|
| evidence/planning/thought_intake_2026-06-09_loveability_unethical_affordance_ethical_agency.md | PRIMARY SOURCE: the safe-base + live-affordance thesis, candidate claim sketches, failure-mode catalogue |
| claims.yaml INV-043 / MECH-158 / MECH-159 | caregiver requirement for ethics + love-exclusion failure mode + intergenerational moral progress (the V5 seeds) |
| claims.yaml INV-029 / ARC-024 | Axiom 5 "love exists" + the benefit gradient the loveability arc must make motivationally active for self-other relations |
| claims.yaml ARC-047 / ARC-010 / ARC-040 | SocialGridWorld multi-agent harness + mirror modelling + the substrate INV-043 is emergent from |
| docs/architecture/developmental_metrics.md DEV-NEED-017 / 018 / 021 / 022 | loveability / repair / otherness-after-self-stability / empathy-coupling metric grids + the Salles-2024 coupling upper bound |
| [self_model_v4_plan.md](self_model_v4_plan.md) SELF-1/SELF-3/SELF-7 | V4 self-model prerequisites (stable scorable self; INV-064 sequencing gate) |
| [object_representation_v4_plan.md](object_representation_v4_plan.md) OBJ-2/OBJ-5 | V4 object-permanence + others-as-object prerequisites (DEV-NEED-021 spine) |

---

## Decision log

- **2026-06-10** -- Plan registered as a V5 SOCIAL-tier forward-roadmap, sibling
  to `ethics_as_coherence_v5` (correction/repair coherence-routing cross-link),
  `self_model_v4` (self-stability prerequisite), and `object_representation_v4`
  (object-permanence + others-as-object prerequisite). Seven nodes seeded:
  LOVE-1 caregiver substrate floor, LOVE-2 loveability, LOVE-3 live affordance,
  LOVE-4 correction-without-annihilation, LOVE-5 love-mediated repair, LOVE-6
  ethical-agency capstone, LOVE-7 biology grounding debt. Readiness gates pinned
  per node against MECH-163 (V3 gate) + V4 self/object prerequisites + ARC-047
  caregiver substrate. `generation: v5` set so the V3 closure % is unaffected.
  No claims.yaml edits. Five new V5 claims proposed (not registered here);
  INV-043 / MECH-158 / MECH-159 / ARC-047 flagged for v4 -> v5 reassignment.
