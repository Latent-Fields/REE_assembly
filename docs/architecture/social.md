---
nav_exclude: true
---

# Social Cognition (Self/Other)

**Claim Type:** architectural_commitment
**Scope:** Social cognition via mirror modelling, coupling, and otherness inference
**Depends On:** INV-005 (harm via mirror modelling), ARC-004 (L-space), ARC-006 (entities and binding)
**Status:** stable
**Claim ID:** ARC-010, ARC-047, MECH-159, MECH-190
<a id="arc-010"></a>

---

> **Elaborates Section 5 (Social Extension: Self/Other) of `REE_CORE.md`.**

## Social Cognition (REE)

This folder specifies **social cognition mechanisms** in the Reflective-Ethical Engine (REE).

Social cognition in REE is grounded in:
- reuse of the self generative model,
- precision-weighted coupling to others,
- and persistence of harm via moral residue.

It precedes language and enables empathy, coordination,
and ethical generalisation without symbolic rules.

**Subsystem abstract (core claims):** ARC‑010 anchors mirror modelling and coupling. MECH‑031 and MECH‑036 define
fast empathy routing and veto thresholds, and MECH‑041 adds affective expression as a mode‑broadcast channel for
social prediction load reduction. Supporting context includes MECH‑032 (high‑recall OTHER_SELFLIKE), MECH‑051
(relational topology modulation), MECH‑052 (care persistence), and ARC‑009/ARC‑006.

Source: `docs/processed/legacy_tree/architecture/social/README.md`

---

## Mirror Modelling

### Definition
Mirror modelling is the reuse of the **self generative model**
to simulate other agents, with reduced coupling and without interoceptive closure.

It enables:
- prediction of others' behaviour,
- empathy as predicted self-like degradation,
- generalisation of harm without explicit moral rules.

### Mechanism
- Same latent variables as self-model (shared L-space)
- Lower precision gains (alpha_k reduced)
- No direct interoceptive error correction
- Coupling strength modulates empathic resonance

### Harm Equivalence Principle
Predicted degradation in a mirrored other-model
is treated as homologous to degradation of the self,
discounted by coupling strength.

### Role in Ethics
Mirror modelling is the primary pathway by which:
- harm-to-other contributes to ethical consequence and residue (legacy \(M(\zeta)\) proxy)
- moral residue R forms without direct self-harm

Note: legacy sources use the ethical cost term M. Current canonical framing removes the explicit cost term while retaining residue and mirror modelling (see `docs/architecture/e3.md`).

### Signed viability coupling (clarification)
Canonical social coupling should remain **signed**, not harm-only:

- predicted other-benefit and predicted other-harm both influence selection/ranking,
- harm channels retain stronger veto/interrupt authority under catastrophic/high-certainty conditions (`MECH-036`),
- benefit channels provide approach/repair pressure without becoming a standalone objective function.

This keeps REE aligned with INV-001/ARC-012 (no explicit moral reward module) while avoiding a purely aversive social
model.

### Failure Modes
- Low gain: psychopathy / callousness
- Excessive gain: empathic overwhelm / paralysis
- Miscalibrated gain: burnout, moral injury

Source: `docs/processed/legacy_tree/architecture/social/mirror_modelling.md`

---

## Social Coupling

Social coupling determines how strongly mirrored models influence selection.

### Coupling Factors
- Structural similarity
- Temporal synchrony
- History of interaction
- Language-mediated trust signals

### Coupling Effects
- Scales signed other-impact contribution (harm and benefit)
- Modulates ethical consequence and residue (legacy \(M\) proxy)
- Affects residue accumulation

### Dynamics
Coupling is:
- context-dependent,
- history-sensitive,
- recalibrated during offline sleep.

This allows empathy without global collapse.

Source: `docs/processed/legacy_tree/architecture/social/social_coupling.md`

---

## Otherness Inference

REE distinguishes self from other via coupling structure.

### Self
- Tight action–prediction coupling
- Interoceptive and proprioceptive closure
- High precision on internal error signals

### Other
- Structural similarity to self-model
- Loose coupling
- No interoceptive closure

Otherness is inferred when an entity:
- behaves coherently,
- predicts similarly to self,
- but does not respond to self action commands.

This avoids symbolic identity assignment.

Source: `docs/processed/legacy_tree/architecture/social/otherness_inference.md`

---

<a id="mech-031"></a>
## Derived Social Tags and Empathy Coupling (MECH-031)

**Claim Type:** mechanism_hypothesis  
**Scope:** Derived social tags and control-plane coupling for fast empathy  
**Depends On:** ARC-010, ARC-005, ARC-017, ARC-015, ARC-006, INV-005  
**Status:** provisional  
**Claim ID:** MECH-031

---

## Agency and Other-Selflike Detection (Derived Streams)

REE can extend social cognition without a new subsystem by adding **derived** tags over WORLD:

- `AGENCY`: detects interveners vs passive dynamics (goal-directed intervention, error-correction, boundary maintenance).
- `OTHER_SELFLIKE`: probability that an agent runs a self/world separation and self-impact loop.

These are inference tags, not perceptual primitives. They reuse the same self/world/impact machinery, rather than
introducing a separate social-cognition module.

Prerequisite: reliable **object persistence/binding** is required to mark an entity as `OTHER_SELFLIKE`, otherwise
agency cues cannot be attributed to a stable target (see `entities_and_binding.md`).

Calibration note: `OTHER_SELFLIKE` should be biased toward **high recall** (tolerating false positives) rather than
high precision. Early false positives are historically normal and less harmful than false negatives, which block
empathy coupling and ethical generalisation. Calibration can tighten over development.

<a id="mech-032"></a>
## OTHER_SELFLIKE High-Recall Bias (MECH-032)

**Claim Type:** mechanism_hypothesis  
**Scope:** Bias `OTHER_SELFLIKE` toward recall to avoid empathy false negatives  
**Depends On:** MECH-031, ARC-010  
**Status:** provisional  
**Claim ID:** MECH-032

<a id="mech-036"></a>
## Other-Harm Veto Threshold (MECH-036)

**Claim Type:** mechanism_hypothesis  
**Scope:** When inferred other-harm should veto vs influence ranking  
**Depends On:** MECH-031, ARC-005, INV-005  
**Status:** provisional  
**Claim ID:** MECH-036

Other-harm should trigger a hard veto only under high-certainty, catastrophic, or irreversible outcomes. In most
ambiguous or tradeoff-heavy contexts, other-harm should influence ranking rather than veto selection. Control-plane
coupling parameters (`lambda_empathy`, `v_other_veto`) set and adapt this threshold.

Open question Q‑009 addresses whether care‑investment weights should be allowed to override veto thresholds in
exceptional contexts.

---

<a id="mech-041"></a>
## Affective Expression as Mode Broadcast (MECH-041)

**Claim Type:** mechanism_hypothesis  
**Scope:** Pre‑verbal affective displays as control‑plane regime signals for social prediction load reduction  
**Depends On:** ARC-010, ARC-005, ARC-016, MECH-039  
**Status:** provisional  
**Claim ID:** MECH-041

Affective expression can be treated as a **low‑latency broadcast** of control‑plane regime to other agents.
Rather than encoding rich propositional content, these displays expose coarse **mode‑level state** (arousal, readiness,
valence bias, veto sensitivity), allowing social partners to reduce predictive load and coordination cost before language.

Neuroanatomical observations (e.g., cranial‑nerve afferent/efferent loops with brainstem proximity) suggest that
fast, embodied signaling channels could exist, but REE treats this as a functional design hypothesis rather than an
anatomical requirement.

Evidence anchors: P40–P43.

**Evidence summary:** Facial motor control (CN VII), facial afferent processing (CN V), and the clinical dissociation
between emotional vs volitional facial pathways collectively support a **fast, embodied expression channel** that is
partly separable from deliberative control. This is consistent with a low‑latency broadcast of control‑plane regime to
social partners without invoking propositional content.

**Safety note (functional):** Affective expression can also be treated as a **safety mechanism**: it exposes deep control
states that should not be hidden, and extreme expression can modulate behavior by **reducing exploration** (e.g., sensory
interference) or **triggering assistance** (e.g., distress calls). These are treated as functional hypotheses, not
anatomical claims.

---

<a id="mech-051"></a>
## Oxytocin/Vasopressin as Relational Topology Modulators (MECH-051)

**Claim Type:** mechanism_hypothesis  
**Scope:** Dynamic self–other boundary geometry and mode‑prior shaping  
**Depends On:** ARC-010, ARC-005, ARC-006  
**Status:** candidate  
**Claim ID:** MECH-051

REE should represent **relational distance** between self and other agents as a continuous control‑plane variable
\(R_{\text{self},j}\in[0,1]\), where 0 is fully self‑like and 1 is fully external/adversarial. This is a structural
geometry, not an emotion.

Two opponent analogues modulate this topology:

- **Oxytocin‑analogue:** reduces relational distance for selected agents under safe affiliative signals, increasing
  bonding‑mode priors and shared‑trajectory weighting.
- **Vasopressin‑analogue:** increases boundary rigidity under sustained threat or norm violation, sharpening group
  differentiation and defensive mode priors.

Relational distance directly scales harm weighting and coupling strength in trajectory evaluation. It also conditions
mode priors (bonding vs defensive) before deep E3 evaluation.

These are **control‑plane weights**, not explicit ethical cost terms. They modulate coupling and harm weighting inside
the existing commitment and residue architecture rather than introducing a separate moral objective.

---

<a id="mech-052"></a>
## Prolactin as Care‑Investment Persistence (MECH-052)

**Claim Type:** mechanism_hypothesis  
**Scope:** Sustained caregiving orientation and care‑weight persistence  
**Depends On:** ARC-010, MECH-051, MECH-048  
**Status:** candidate  
**Claim ID:** MECH-052

REE should include a **care‑investment weight** \(C_j\) for each agent \(j\), representing sustained willingness to
absorb cost on their behalf. A prolactin‑analogue increases the persistence of \(C_j\), stabilising caregiving modes
even when immediate reward is low or costs are asymmetric.

Care weight should scale how strongly predicted harm to \(j\) influences trajectory evaluation, separate from
relational distance. Oxytocin lowers distance; prolactin sustains care; μ‑style stability overlays reduce rapid
oscillation once care is established.

Operational clarification: \(C_j\) should scale signed other-impact routing (benefit and harm) rather than only the
harm channel, while catastrophic other-harm veto behavior remains governed by `MECH-036`.

Care weights are **control‑plane priorities**, not standalone ethical objectives. They bias selection and learning
within the existing commitment/residue framework.

---

<a id="mech-127"></a>
## Counterfactual Other-Cost-Aversion as Motivational Surrogate (MECH-127)

**Claim Type:** mechanism_hypothesis
**Scope:** Counterfactual empathic activation substituting for a degraded direct motivation pathway
**Depends On:** MECH-031, MECH-032, INV-005, INV-028, INV-034
**Status:** candidate
**Claim ID:** MECH-127

When an agent's direct task-motivation pathway is degraded (deficit state), modeling the
*anticipated* cost to another agent -- other-cost-aversion -- can substitute as an activation
mechanism, producing cooperative task-engagement even when the other agent is absent and no
direct task reward signal is available.

**Key structural distinction from MECH-031:**
MECH-031 describes empathy *modulating* behavior via OTHER_SELFLIKE tagging and control-plane
coupling -- modulation of an existing pathway. MECH-127 describes empathy *replacing* a degraded
pathway -- it is a **bypass**, not a modulation. The distress-at-their-struggle response provides
motivational energy the direct pathway cannot supply.

**The activation is counterfactual:** the other agent need not be present or actually struggling.
The anticipation of what *would* happen to them *if* they took on the burden is sufficient to
activate the mechanism. This implies OTHER_SELFLIKE tagging must function pre-encounter (supporting
MECH-032 high-recall bias) and that forward simulation (E2/E3 lookahead) underlies the projection.

**Mechanism steps:**
1. Direct motivation pathway degraded (agent in deficit state)
2. Counterfactual projection: model what would happen to Agent B if B took on the task
3. Affective response to that model: distress-at-B's-struggle activates via shadow bundle
4. Distress-response provides motivational energy the direct pathway cannot
5. Behavioral output: task engagement / cooperation -- identical to direct-pathway output
6. Cooperative uplift: actual burden-sharing reduces cost, positive feedback loop

**Multiagent implication:** this mechanism can produce *more* cooperative output under degraded
conditions than predicted by n=1 (direct-pathway) analysis. This is the motivating case for
ARC-034 (ethics testing must span nth-order dynamics).

**Motivating observation:** first-person report, 2026-03-24. Formal basis:
`docs/thoughts/2026-02-09_empathy.md` (MECH-031/032 infrastructure) provides the shadow bundle
and control-plane coupling that MECH-127 recruits. See also:
`evidence/planning/thought_intake_2026-03-24_empathy_multiagent_ethics.md`.

---

## Fast Empathy via Shadow Bundles

When `OTHER_SELFLIKE` is high, REE can instantiate a shadow bundle of inferred streams for an agent `j`:

- `HOMEOSTASIS_j`, `HARM_j`, `BENEFIT_j`, `SELF_IMPACT_j`, optionally `TEMPORAL_COHERENCE_j`.

These are estimated viability variables, not direct interoception. The control plane can couple them into pruning and
ranking via a small set of knobs:

- `lambda_empathy`: other-to-self coupling strength.
- `g_social`: social attention gain for `OTHER_SELFLIKE` agents.
- `alpha_other`: precision assigned to inferred other-states.
- `v_other_veto`: whether other-harm can trigger veto/interrupt vs only affect ranking.
- Optional `AFFILIATION`: stabilises coupling based on history/kinship.

This yields fast empathy as **routing + weighting**, not a new moral module.

---

<a id="mech-159"></a>
## Intergenerational Moral Progress (MECH-159)

**Claim Type:** mechanism_hypothesis
**Scope:** Moral progress as a multi-generational property, not single-agent optimisation
**Depends On:** INV-043 (caregiver requirement), ARC-019 (staged curriculum), ARC-010 (social cognition)
**Status:** candidate
**Claim ID:** MECH-159

Moral progress in REE is hypothesised to be **intergenerational rather than individual**.
A single agent cannot achieve its own moral maximum within a lifetime because:

1. **Childhood plasticity** enables world-model formation, belief formation, and love-internalisation
   — but a child cannot take full responsibility (E3 not online).
2. **Adulthood stability** enables responsibility and ethical action — but reduces world-model
   plasticity, limiting how much the adult can revise foundational beliefs.
3. Therefore, each generation must improve the **developmental starting conditions** for the
   next — caregiving, modelling of love, scaffolded responsibility — so that the next
   generation begins from a higher ethical baseline.

**Implications:**

- REE agents may have an ethical *obligation* to participate in raising next-generation agents
  as part of their own ethical development. Parenthood/caregiving is not external to ethics —
  it is part of the ethics of shared existence (INV-042).
- Simulated or single-machine testing cannot test this hypothesis — it requires multi-generation
  multi-agent infrastructure.
- Civilisational ethics, cultural transmission, and institutional design are all
  expressions of this mechanism at scale.

**Relationship to MECH-052 (care persistence):** MECH-052 describes the sustained
caregiving orientation within a single agent. MECH-159 describes the population-level
consequence of that mechanism applied across generations — care persistence propagates
ethical baselines forward in time.

Source: `docs/thoughts/2026-04-01_Caregivers_childhood_moral_development.md`

---

---

<a id="arc-047"></a>
## Social Scent Harness — SocialGridWorld (ARC-047)

**Claim Type:** architectural_commitment
**Scope:** Minimal multi-agent substrate for empirical testing of social cognition claims
**Depends On:** ARC-010, MECH-041, MECH-031, MECH-036, MECH-127, IMPL-019
**Status:** candidate
**Claim ID:** ARC-047
**Implementation phase:** v4

> **Registered 2026-04-06.** Current social claims (ARC-010, MECH-031/036/041/051/052/127)
> have no empirical substrate. SocialGridWorld is the minimal environment to generate evidence.

### Architecture

**Base:** Extend CausalGridWorld to SocialGridWorld — N REE agent instances + optional
predator entity in a shared grid.

**Predator entity:** autonomous agent with random walk + drift toward nearest agent.
Contact with agent triggers a harm event (z_harm_s spike, residue accumulation).
Not trainable — purely environmental pressure.

### Scent Channels (7 per other-agent)

Each agent's observation includes seven additional channels from other agents, delivered as
Gaussian gradient fields (same format as existing hazard_field_view / resource_field_view):

| Channel | Source signal | Emission type |
|---------|--------------|---------------|
| `wanting_scent_field[25]` | Other's z_goal norm | Automatic, continuous |
| `seeking_scent_field[25]` | Other's novelty/arousal state | Automatic, continuous |
| `alarm_scent_field[25]` | Other's hazard-contact event | Automatic, spike on event |
| `harm_stress_field[25]` | Other's z_harm_a norm | Automatic, continuous |
| `direction_cue_field[25]` | Other's trajectory direction | Automatic, continuous |
| `celebration_scent_field[25]` | Other's benefit-contact event | Automatic, spike on event |
| `defense_scent_field[25]` | Other's voluntary defense action | Voluntary discrete action |

Scent emission is **semi-involuntary** for all channels except defense, implementing
MECH-041 affective expression as mode broadcast. Each channel decays with distance
(Gaussian kernel) and persists for N steps before decaying.

### Receiving Scents

The receiving agent interprets scent channels via ARC-010 mirror modelling:
- MECH-031 OTHER_SELFLIKE inference tags the source as another agent
- MECH-127 counterfactual other-cost operates on the inferred other-state from scent inputs
- MECH-036 other-harm veto triggers when harm_stress_field is high for a tagged other-agent

### Tests Enabled

1. **Cooperative defense** (MECH-190): co-emission of defense scent under predator threat
2. **Defense of others**: defense emission when others' harm_stress_field is high but self is safe
3. **Goal helping**: response to wanting_scent by moving toward resources + direction cue
4. **Self-maintenance**: balancing energy drain from defense with self-resource replenishment
5. **Kin-weighting**: relational distance (MECH-051) modulating defense threshold for others

### Testing Order (IMPL-019)

Per IMPL-019 self-first ordering: SocialGridWorld experiments are introduced only after
self-viability, control-plane stability, and E3 commitment reliability are confirmed in
single-agent CausalGridWorld. Early experiments can use one trained agent + one scripted
partner before full multi-agent training.

---

<a id="mech-190"></a>
## Defense Scent Coalitions (MECH-190)

**Claim Type:** mechanism_hypothesis
**Scope:** Cooperative predator defense via additive scent pressure without language
**Depends On:** ARC-047, MECH-041, MECH-036, MECH-031, MECH-051
**Status:** candidate
**Claim ID:** MECH-190

> **Registered 2026-04-06.** First predicted multi-agent cooperative behavior in SocialGridWorld.

**Mechanics:** each agent has a discrete action bit `emit_defense` at energy cost
`defense_cost`. When emitted, a `defense_scent` Gaussian field centers on the agent.
Predator avoidance: `P(avoid) = min(1.0, sum(defense_scent at predator position) * avoidance_scale)`.
Additive structure: two agents co-emitting → double deterrence at half per-agent cost.

**Predicted behavioral sequence:**
1. **Individual defense** — emit when predator within personal threat radius
2. **Early coalition** — emit when others' alarm_scent spikes (MECH-041 coordination signal), even if predator is not immediately proximate
3. **Altruistic defense** — emit when another agent's harm_stress_field is high, even when self is not threatened (requires MECH-036 other-harm routing + MECH-127 counterfactual evaluation)

Stage 3 provides the first empirical test of MECH-127 in a multi-agent setting.
Relational distance (MECH-051) should modulate the threshold for altruistic defense.

**Why this emerges before goal-cooperation:** defense signal structure is simpler (binary
spike + harm coupling) and benefit is immediate; goal-helping requires sustained goal-state
inference across multiple steps.

---

## Open Questions

<a id="q-009"></a>
**Q-009 — Care weights vs other‑harm veto (legacy)**  
This question is resolved by a bounded override policy: catastrophic high-certainty irreversible other-harm remains a
hard veto; non-catastrophic override is allowed only under necessity, imminence, proportionality, and explainability
gates, with mandatory post-commit accountability logging.
Resolution note: `docs/conflicts/resolutions/2026-02-18_care-override-vs-other-harm-veto.md`

## Related Claims (IDs)

- ARC-010
- ARC-009
- ARC-006
- ARC-004
- INV-005
- MECH-031
- MECH-032
- MECH-036
- MECH-041
- MECH-051
- MECH-052
- MECH-127
- ARC-034
- Q-009
- INV-043 (Caregiver requirement -- developmental_curriculum.md)
- MECH-158 ("Love exists but not for me" failure mode)
- MECH-159 (Intergenerational moral progress)
- ARC-047 (Social scent harness -- SocialGridWorld)
- MECH-190 (Defense scent coalitions)

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/social/README.md`
- `docs/processed/legacy_tree/architecture/social/mirror_modelling.md`
- `docs/processed/legacy_tree/architecture/social/social_coupling.md`
- `docs/processed/legacy_tree/architecture/social/otherness_inference.md`
- `docs/thoughts/2026-02-09_empathy.md`
- `docs/thoughts/2026-04-01_Caregivers_childhood_moral_development.md`
- `docs/thoughts/2026-02-09_other_harm_gating.md`
- `docs/thoughts/2026-02-11_oxytocin_vasopressin.md`
- `docs/thoughts/2026-02-11_prolactin.md`
- `docs/thoughts/2026-02-25_task_loop_extraction_and_latent_field_ethics.md`
