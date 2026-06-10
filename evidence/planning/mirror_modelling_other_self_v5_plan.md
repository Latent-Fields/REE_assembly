---
closure_plan:
  id: mirror_modelling_other_self_v5
  generation: v5
  title: "Mirror modelling: others modelled by reusing the self-model (others-as-self / ToM)"
  registered: 2026-06-10
  last_updated: 2026-06-10
  scope_claims: [ARC-010, MECH-031, MECH-032, MECH-036, MECH-041, MECH-051, MECH-052, MECH-127, ARC-047, ARC-083, INV-005]
  sibling_plans: [object_representation_v4, self_model_v4, goal_pipeline]
  roadmap_note: >
    FORWARD ROADMAP, not a closure map, and the V5 (SOCIAL mind) tier of the
    three-tier partition (V4 = individual mind, V5 = social, V6 = linguistic).
    The spine is ARC-059 / DEV-NEED-021: self -> objects -> OTHERS -> language.
    Otherness inference REQUIRES object-permanence AND a stable self, both V4 --
    so every node here carries a cross_plan_link or readiness_gate back to a V4
    sibling node (object_representation_v4:OBJ-2 permanence, OBJ-3/SELF-* self),
    plus the shared MECH-163 multi-step hippocampal planning gate (the V3
    completion item that is the V4-social entry gate; it stays v3, never flagged).
    Nodes carry owner_exq: null and the drift checker stays dormant against them.
    The VALUE is the readiness_gate per node -- exactly which V4-tier and
    V3-completion prerequisites must land before each V5 social-substrate step is
    honest to build. generation: v5 keeps these nodes OUT of the V3 closure
    percentage (serve.py read_closure, generate_closure_snapshot.py,
    check_closure_drift.py are generation-aware). A node graduates from roadmap
    to closure-tracked by gaining an owner_exq once its first V5 experiment is
    queued. The central architectural bet of this plan: REE does NOT build a
    separate "other-model" -- it REUSES the self generative model (ARC-010) to
    simulate others at reduced precision-coupling; the work is the coupling
    apparatus, not a second self.
  nodes:
    - id: "mirror_modelling_other_self_v5:MIRROR-1"
      title: "Otherness inference: tag an entity OTHER_SELFLIKE without symbolic identity (MECH-031/032)"
      phase: 1
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-031, MECH-032]
      depends_on: []
      cross_plan_link: ["object_representation_v4:OBJ-5"]
      blocking_on: "DEV-NEED-021 prerequisite: others-as-object slots (object_representation_v4:OBJ-5) require object-permanence (OBJ-2) + self-stability (OBJ-3/self_model_v4) to exist first. There is no entity to tag OTHER_SELFLIKE until a token-keyed other-object slot can hold it."
      readiness_gate:
        - "object_representation_v4:OBJ-5 (others-as-object: per-agent token-keyed slot) -- the slot MECH-031's tag attaches to; itself gated on OBJ-2 permanence + OBJ-3 self"
        - "social.md otherness-inference rule is design-only: an entity is OTHER when it behaves coherently + predicts similarly to self but does NOT respond to self action commands (no interoceptive closure, loose action-prediction coupling)"
        - "MECH-032 high-recall bias: OTHER_SELFLIKE detection biased toward false-positives -- early false positives are cheaper than false negatives (which block empathy coupling entirely); calibration tightens over development"
      last_updated: 2026-06-10
      completion_note: "First V5 social step: the agent must mark a perceived entity as another agent BEFORE any social interpretation runs. Otherness is inferred from coupling structure (behaves like self, but self-actions do not control it), never assigned symbolically. This is the entry door of the whole tier; everything below presupposes the tag exists."
    - id: "mirror_modelling_other_self_v5:MIRROR-2"
      title: "Reuse the self generative model to SIMULATE the other (ARC-010): shared L-space, reduced precision, no interoceptive closure"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-010]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-1"]
      cross_plan_link: ["self_model_v4:SELF-1", "object_representation_v4:OBJ-3"]
      blocking_on: "Requires a stable, stateful self-model to mirror FROM. self_model_v4:SELF-1 (z_self promoted from EMA body-latent to a stateful self-model with temporal depth) is the thing reused; until z_self is a real recurrent self-model there is nothing to instantiate at reduced coupling for the other."
      readiness_gate:
        - "self_model_v4:SELF-1 -- a stateful self-model (DR-13 temporal depth) is the generative model ARC-010 reuses; mirroring an EMA body-snapshot would simulate an instantaneous body, not an agent"
        - "ARC-010 mechanism (social.md): same latent variables as self (shared L-space), lower precision gains (alpha_k reduced for the other), no direct interoceptive error correction, coupling strength modulates resonance"
        - "MECH-163 multi-step hippocampal planning (V3-completion / V4-social entry gate): simulating another agent's trajectory over time needs the model-based planner; 1-step greedy cannot roll out another agent's policy"
      last_updated: 2026-06-10
      completion_note: "The architectural heart of the plan: REE does NOT learn a second model for the other. It runs the SELF generative model with the other's observed state as input, at reduced precision-coupling and without interoceptive closure. This is why a stable self (SELF-1) is a hard prerequisite -- the other-model IS the self-model under a coupling transform."
    - id: "mirror_modelling_other_self_v5:MIRROR-3"
      title: "Precision-weighted coupling apparatus (ARC-010 signed coupling): the alpha_k / coupling-strength control that scales other-impact"
      phase: 2
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [ARC-010, MECH-051]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-2"]
      cross_plan_link: []
      blocking_on: "Coupling can only be scaled once there is a mirrored other-model (MIRROR-2) to couple TO. The coupling-strength control (structural similarity, temporal synchrony, interaction history) is meaningless without a running mirror simulation."
      readiness_gate:
        - "ARC-010 signed-coupling clarification (social.md): coupling must remain SIGNED -- predicted other-benefit AND other-harm both influence selection; harm retains stronger veto authority (MIRROR-4); benefit gives approach/repair pressure without becoming a standalone objective"
        - "INV-001 / ARC-012 constraint: no explicit moral reward module -- coupling is a control-plane weight (relational distance scales harm-weighting + coupling strength inside trajectory evaluation), NOT an added ethical cost term"
        - "MECH-051 (oxytocin/vasopressin analogues modulate relational topology + mode priors) -- the developmental/contextual knob on coupling strength; recalibrated during offline sleep (cross-cuts sleep substrate, not this plan)"
      last_updated: 2026-06-10
      completion_note: "The coupling control is the dial that turns mirror-simulation output into selection pressure. It must be SIGNED (benefit + harm) to stay aligned with ARC-012's no-explicit-cost-term commitment while avoiding a purely aversive social model. MECH-051 is the relational-topology modulator on this dial; its full sleep-recalibration loop is out of scope here."
    - id: "mirror_modelling_other_self_v5:MIRROR-4"
      title: "Empathy veto + harm-equivalence: predicted other-degradation treated as homologous to self-harm (INV-005, MECH-036)"
      phase: 3
      status: blocked
      severity: load-bearing
      owner_exq: null
      unblocks_claims: [MECH-036, INV-005]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-3"]
      cross_plan_link: []
      blocking_on: "Harm-via-mirror (INV-005) and the catastrophic-other-harm veto (MECH-036) presuppose a running, coupled mirror simulation (MIRROR-3) that can predict another agent's degradation. No coupled other-model => no predicted other-harm to veto."
      readiness_gate:
        - "INV-005 (universal invariant): harm to others contributes via mirror modelling, NOT symbolic rules -- predicted degradation in the mirrored other is homologous to self-degradation, discounted by coupling strength (the Harm Equivalence Principle)"
        - "MECH-036 veto threshold: other-harm triggers a veto ONLY under high-certainty catastrophic outcomes; coupling parameters (lambda_empathy, v_other_veto) set and adapt the threshold"
        - "Requires MIRROR-2 mirror + MIRROR-3 signed coupling live, so the harm channel has a predicted-other-state to act on; this is where moral residue R forms without direct self-harm"
      last_updated: 2026-06-10
      completion_note: "This node operationalises the ethical payoff of the whole tier: harm-to-other becomes ethically load-bearing PURELY through mirror simulation + coupling, with no symbolic moral rule (INV-005). The veto (MECH-036) is the asymmetric authority that lets catastrophic predicted other-harm interrupt selection. This is the substrate where REE ethics becomes genuinely social."
    - id: "mirror_modelling_other_self_v5:MIRROR-5"
      title: "Gain-calibration window: low/high/miscalibrated coupling failure modes (psychopathy / overwhelm / burnout)"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-032, MECH-036, "MECH-404"]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-3", "mirror_modelling_other_self_v5:MIRROR-4"]
      cross_plan_link: []
      readiness_gate:
        - "social.md failure-mode taxonomy is design-only: LOW gain = psychopathy/callousness; EXCESSIVE gain = empathic overwhelm/paralysis; MISCALIBRATED gain = burnout/moral injury"
        - "Requires both the coupling dial (MIRROR-3) and the harm-equivalence channel (MIRROR-4) to be live so that gain can be varied and the three failure regimes surfaced as distinct behavioural signatures"
        - "NEW capability gap: REE owns the dial (MIRROR-3) and the failure taxonomy (prose) but has NO claim asserting that mirror-coupling gain must be HOMEOSTATICALLY regulated (kept in a window) -- the three failure modes are precisely the boundaries of that window"
      last_updated: 2026-06-10
      completion_note: "The clinically richest node: the SAME coupling apparatus produces psychopathy (gain too low), empathic overwhelm (too high), and burnout (miscalibrated) at the edges of its operating window. This is a falsifiable prediction -- the three pathologies should be reachable by sweeping a single gain parameter -- and it motivates the only proposed new claim: a gain-homeostasis regulator. Off the V3 critical path; V5 measurement substrate (SocialGridWorld, ARC-047)."
    - id: "mirror_modelling_other_self_v5:MIRROR-6"
      title: "Affective expression as mode-broadcast: emit own control-plane regime to reduce the OTHER'S prediction load (MECH-041)"
      phase: 4
      status: blocked
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-041]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-2"]
      cross_plan_link: ["object_representation_v4:OBJ-5"]
      blocking_on: "MECH-041 is the RECIPROCAL of mirroring: it presupposes that other agents are themselves mirror-modellers reading my broadcast. It needs the multi-agent harness (ARC-047 SocialGridWorld scent channels) and the mirror loop (MIRROR-2) live on both sides."
      readiness_gate:
        - "ARC-047 SocialGridWorld harness (currently v4, flag-recommended v5): the seven scent channels (wanting, seeking, alarm, harm_stress, direction, celebration, defense) ARE the MECH-041 mode-broadcast substrate -- affective state leaked as diffusing gradient fields"
        - "MECH-041 mechanism: affective expression is semi-involuntary control-plane-regime broadcast; a receiving agent uses ARC-010 mirror modelling (MIRROR-2) to interpret the scent as the sender's internal state, reducing its own prediction load"
        - "Reciprocity requirement: meaningful only when >=2 agents each run the MIRROR-2 loop -- one broadcasts, the other mirror-interprets; single-agent training cannot surface it"
      last_updated: 2026-06-10
      completion_note: "The other half of the social loop: not just reading others, but BROADCASTING own state so others can read me cheaply. MECH-041 turns affect into a communication channel (the pre-linguistic bridge toward V6 language). The ARC-047 scent fields are exactly this broadcast medium; this node graduates first when SocialGridWorld gains its first owner_exq."
    - id: "mirror_modelling_other_self_v5:MIRROR-7"
      title: "Care persistence + counterfactual empathic activation: love/cooperation as long-horizon coupling (MECH-052, MECH-127)"
      phase: 5
      status: blocked
      severity: high
      owner_exq: null
      unblocks_claims: [MECH-052, MECH-127, INV-029]
      depends_on: ["mirror_modelling_other_self_v5:MIRROR-4", "mirror_modelling_other_self_v5:MIRROR-6"]
      cross_plan_link: ["self_model_v4:SELF-7"]
      blocking_on: "Long-horizon care (MECH-052) and counterfactual cooperative activation (MECH-127) both require multi-step planning over ANOTHER agent's future state -- the MECH-163 hippocampal planner -- plus the harm-equivalence channel (MIRROR-4) and the INV-064 maturational gate (self_model_v4:SELF-7) confirming self-stability precedes social depth."
      readiness_gate:
        - "MECH-163 multi-step hippocampal planning (V3-completion gate): INV-029 'sharing joys and sorrows' / love-as-long-horizon-care requires planning trajectories that affect another agent's z_harm_a + benefit accumulation over time -- structurally inaccessible to 1-step greedy"
        - "MECH-052 (prolactin-analogue care-investment persistence): coupling persists across episodes/absence -- the stability that makes care a disposition, not a momentary resonance; recalibrated in sleep"
        - "MECH-127 (counterfactual other-cost activation): when the direct task-reward pathway is degraded, modelling anticipated cost to an ABSENT other substitutes as activation -- requires pre-encounter OTHER_SELFLIKE tagging (MIRROR-1) + a mirror that runs counterfactually (MIRROR-2)"
        - "self_model_v4:SELF-7 / INV-064 maturational gate: a stable self must precede this social depth (DEV-NEED-021)"
      last_updated: 2026-06-10
      completion_note: "The apex of the tier: mirror coupling becomes a long-horizon DISPOSITION (MECH-052 care persistence) and can ACTIVATE behaviour counterfactually even with the other absent (MECH-127), grounding INV-029 love-as-coherence-bias. This is the deepest social node and the natural bridge to V6 (cooperative coordination precedes shared language). Gated on the full planner + a stable self; design-only today."
---
# Mirror Modelling: Others Modelled by Reusing the Self-Model -- V5 Forward Roadmap

**Registered:** 2026-06-10
**Generation:** v5 (SOCIAL tier; forward roadmap; excluded from the V3 closure %)
**Status:** roadmap
**Scope:** sequence the mirror-modelling / Theory-of-Mind substrate -- the
user-named "other-attribution which models others as the self" -- from
otherness inference through self-model reuse, precision-coupling, the empathy
veto, the gain-calibration window, affective broadcast, and long-horizon care,
pinning for each step the V4-tier and V3-completion prerequisites that must land
first.

This is the **V5 (SOCIAL mind)** tier of the three-tier partition (V4 =
individual mind, V5 = social, V6 = linguistic). It sits on the ARC-059 /
DEV-NEED-021 spine: **self -> objects -> OTHERS -> language**. Otherness
inference is not a free-standing capability -- it REQUIRES object-permanence
(so an other persists as a trackable entity through occlusion) and a stable
self (so there is a self-model to mirror FROM). Both are V4. Every node here
therefore links back to a V4 sibling plan node, plus the shared **MECH-163**
multi-step hippocampal planning gate -- the V3-completion item that is the
V4-social entry gate (it stays v3; it is NOT flagged).

It is a *forward roadmap*, not a closure map: V5 has no experiments yet, so
nodes carry no `owner_exq` and the drift checker stays dormant. The value is the
**readiness gates** -- for each social step, exactly which V4 self/object work
and which V3-completion item must land before the V5 substrate step is honest to
build.

---

## One-line framing

> REE does NOT build a separate model of the other. It REUSES the self
> generative model (ARC-010) -- same shared L-space, reduced precision-coupling,
> no interoceptive closure -- to SIMULATE the other. The work of this tier is
> not a second self; it is the COUPLING APPARATUS: who counts as an other
> (MECH-031/032), how strongly their predicted state is coupled to selection
> (ARC-010 signed coupling, MECH-051), when predicted other-harm vetoes
> (INV-005, MECH-036), what keeps gain inside its window (the three failure
> modes), how affect is broadcast back (MECH-041), and how coupling becomes a
> long-horizon disposition (MECH-052, MECH-127, INV-029). All of it presupposes
> a stable self to mirror from (V4) and an other that persists as an object
> (V4).

---

## The mirror-modelling sequence (nodes mapped to claims)

| Node | Step | Claim | Phase leaning | The prerequisite gate |
|---|---|---|---|---|
| MIRROR-1 | otherness inference / OTHER_SELFLIKE tag | MECH-031, MECH-032 | V5 (entry) | OBJ-5 others-as-object slot (needs OBJ-2 + OBJ-3) |
| MIRROR-2 | reuse self-model to simulate other | ARC-010 | V5 (heart) | self_model_v4:SELF-1 stateful self; MECH-163 planner |
| MIRROR-3 | precision-weighted signed coupling | ARC-010, MECH-051 | V5 | MIRROR-2 mirror live; ARC-012 no-cost-term constraint |
| MIRROR-4 | empathy veto / harm-equivalence | INV-005, MECH-036 | V5 | MIRROR-3 coupling live |
| MIRROR-5 | gain-calibration window (3 failure modes) | MECH-032/036 + NEWCLAIM | V5 | MIRROR-3 + MIRROR-4 (sweep gain) |
| MIRROR-6 | affective expression as mode-broadcast | MECH-041 | V5 | ARC-047 SocialGridWorld scent fields; reciprocal mirror |
| MIRROR-7 | care persistence + counterfactual activation | MECH-052, MECH-127, INV-029 | V5 (apex) | MECH-163 planner; SELF-7 maturational gate |

---

## Phase reassignment: the social cluster is V5, not V4

Several claims this plan builds on are mislabelled or unlabelled for the
three-tier partition:

- **ARC-047 (SocialGridWorld harness)** and **ARC-083 (others-as-object slot)**
  are explicitly `implementation_phase: v4` in claims.yaml. Both are
  intrinsically SOCIAL / multi-agent: ARC-047's entire subject is the
  multi-agent test harness for ARC-010 mirror modelling; ARC-083's subject is
  per-other-agent object-file slots. They belong in the V5 SOCIAL tier and are
  reported in `generation_flags[]` (current v4 -> recommended v5). ARC-083's
  *prerequisites* (object-permanence PILLAR 1, self-stability PILLAR 2) stay
  V4 -- only the others-as-object endpoint is social.
- **The mirror-modelling mechanism cluster** (MECH-031, MECH-032, MECH-036,
  MECH-041, MECH-051, MECH-052, MECH-127) carries **no `implementation_phase`
  field at all** today. Every one is intrinsically social / relational /
  ethical and belongs to V5. They are NOT flagged in `generation_flags[]`
  (which requires a current_phase: v4 to report) -- the orchestrator should
  STAMP these unphased social mechanisms `implementation_phase: v5` when it
  reconciles this plan. They are listed in `scope_claims` so the linkage is
  explicit.
- **MECH-163 is NOT flagged.** It is the V3 dual-system / multi-step planning
  completion gate and stays `v3`; this plan treats it as the V4-social entry
  prerequisite, not as social work itself.
- **ARC-010 / INV-005** stay where they are: ARC-010 is an
  architectural_commitment (substrate_coherence; never in V3 closure), and
  INV-005 is a universal invariant. Neither needs a phase reassignment; they
  are the spine the V5 mechanisms hang off.

---

## What this plan deliberately does NOT pull into V3 (or V4)

- **No substrate code, no experiments, no claim promotions.** Registering this
  roadmap changes no V3 behaviour and adds no V4 work. The first real V5
  substrate step (otherness inference on a token-keyed other-object slot) is
  gated behind the entire V4 self/object stack and must not enter V3 closure.
- **The self-model and object-file are NOT re-litigated here.** A stable self
  (self_model_v4:SELF-1) and a persisting other-object (object_representation_v4:
  OBJ-2/OBJ-5) are *prerequisites*, owned by the V4 sibling plans. This plan
  consumes them; it does not duplicate them. The architectural bet of the tier
  is precisely that the other-model IS the self-model under a coupling transform.
- **MECH-051's sleep-recalibration loop is cross-cutting, not owned here.**
  Coupling is recalibrated during offline sleep (social.md); that loop lives in
  the sleep substrate plan. This plan owns the coupling DIAL, not its sleep
  recalibration.
- **V6 language is out of scope.** MECH-041 affective broadcast and MECH-127
  cooperative coordination are the *pre-linguistic* bridge; symbolic language
  (the arcuate-fasciculus / MECH-038 line) is the V6 tier and is not pulled
  forward here.

---

## Proposed new claim (V5)

One genuine capability gap surfaced, motivating a single new claim:

- **`mirror_gain_homeostasis`** (suggested generation v5, MECH family) --
  REE owns the coupling DIAL (ARC-010 signed coupling, MECH-051 relational
  modulation) and the failure-mode TAXONOMY in prose (low gain = psychopathy,
  high gain = empathic overwhelm, miscalibrated = burnout), but NO registered
  claim asserts that mirror-coupling gain must be **homeostatically regulated**
  -- held inside an operating window. The three failure modes are precisely the
  boundaries of that window. This is a falsifiable prediction (the three
  pathologies should be reachable by sweeping a single gain parameter) and is
  the substrate for the clinical mapping. Wired under MIRROR-5; depends on
  MECH-032/036 and the coupling apparatus (ARC-010/MECH-051). Returned in
  `proposed_claims[]` as a prose-only stub; the orchestrator assigns the real ID
  and replaces the `MECH-404` placeholder in MIRROR-5
  `unblocks_claims`.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/social.md](../../docs/architecture/social.md) | ARC-010 mirror modelling, coupling, otherness inference, failure modes, MECH-031/032/036/041/051/052/127 |
| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) DEV-NEED-021 | otherness inference REQUIRES object-permanence + self-stability (the V4 prerequisites) |
| claims.yaml ARC-059 | three-stage developmental ordering (self -> objects -> others); ARC-010 is the stage-3 (V4/V5) substrate |
| claims.yaml ARC-010 / INV-005 | the spine: mirror modelling + harm-via-mirror (universal invariant) |
| claims.yaml ARC-047 / ARC-083 | SocialGridWorld harness + others-as-object slot (flagged v4 -> v5) |
| evidence/planning/object_representation_v4_plan.md (OBJ-5) | others-as-object slot -- the V4 object-side prerequisite this plan consumes |
| evidence/planning/self_model_v4_plan.md (SELF-1, SELF-7) | the stable self this plan mirrors from; INV-064 maturational gate |

---

## Decision log

- **2026-06-10** -- Plan registered as the FIRST V5 (SOCIAL tier) forward-roadmap,
  sibling to `object_representation_v4` (OBJ-5 others-as-object) and
  `self_model_v4` (SELF-1 stable self, SELF-7 maturational gate). Seven nodes
  seeded along the mirror-modelling sequence: otherness inference (MECH-031/032)
  -> self-model reuse (ARC-010) -> signed coupling (ARC-010/MECH-051) ->
  empathy veto + harm-equivalence (INV-005/MECH-036) -> gain-calibration window
  (3 failure modes) -> affective broadcast (MECH-041) -> care persistence +
  counterfactual activation (MECH-052/MECH-127/INV-029). Every node gated on a
  V4 self/object prerequisite plus the shared MECH-163 V3-completion planner
  gate. `generation: v5` set so the V3 closure % is unaffected. No claims.yaml
  edits.
- **2026-06-10** -- Flagged ARC-047 + ARC-083 v4 -> v5 (intrinsically social).
  Noted the unphased mirror-modelling mechanism cluster (MECH-031/032/036/041/
  051/052/127) for an orchestrator `implementation_phase: v5` stamp -- not
  reportable via `generation_flags[]` (no current_phase: v4). MECH-163 left v3
  (V3-completion gate, not social work). One new claim proposed:
  `mirror_gain_homeostasis` (the gain-window regulator the failure-mode
  taxonomy implies but no claim asserts).
