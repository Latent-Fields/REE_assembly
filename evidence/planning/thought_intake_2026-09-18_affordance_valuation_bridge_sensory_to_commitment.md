# Thought intake -- affordance-and-valuation bridge (z_world -> commitment)

- **Date processed:** 2026-09-22
- **Raw thought:** `docs/thoughts/2026-09-18_affordance_valuation_bridge_sensory_to_commitment.md` (329 lines, dated 2026-09-18)
- **Session:** `compassionate-pike-fe9174` (umbrella worktree, Mac)
- **Skill:** `/thought-ingestion`
- **Registered this pass:** ARC-149, MECH-575, MECH-576, MECH-577
- **Architecture home:** `docs/architecture/affordance_valuation_bridge.md`

---

## 1. The proposal, tightly stated

The thought asserts that REE is missing a named intermediate object between the world
model and the commitment boundary, and proposes this decomposition:

```text
observation
  -> z_world / E1-E2
  -> affordance-and-action geometry
  -> competing approach / avoidance / investigation tendencies
  -> E3 / commitment boundary
  -> motor policy / action
```

The intermediate object is, verbatim:

> **an affordance field: a dynamically selected geometry of presently reachable actions and
> their predicted consequences.**

constructed as `A_t = F(z_world, z_self, C, K)` where `z_self` is body/needs/capabilities/
commitments, `C` is control state (precision, mode, urgency, uncertainty, inhibition) and `K`
is commitments plus learned relational regularities. `A_t` is explicitly **not** a chosen
action, **not** a motor-primitive library, and **not** an action-value table -- the thought is
emphatic that a value table can rank actions but cannot retain the structured relation
`current world/body state -> feasible action trajectory -> predicted changed world/body/other state`.

Its compact formulation:

> The path from sensory input to motor output should be modelled as a changing geometry of
> reachable, affectively and socially consequence-bearing possibilities. Parietal-like
> processing supplies action-conditioned affordance structure; orbitofrontal-like dynamics
> preserve and contest rival action tendencies; E3 decides which tendency gains jurisdiction
> to become committed behaviour, while later cognition can reconstruct and interrogate the
> ethical grounds of that organisation.

The thought is self-limiting about its own status: *"This does not yet justify a new mechanism
claim. It does suggest a small set of sharply testable questions."* That caution is honoured
here as `status: candidate` + `epistemic_category: substrate_conditional` + explicit
"DO NOT build in V3" notes, **not** by withholding registration (per the standing 2026-06-09
correction recorded in the skill).

---

## 2. What is new vs. existing REE claims

Novelty table. Eight threads; four registered, four already owned.

| thread in the thought | existing REE coverage | verdict |
|---|---|---|
| **A necessary intermediate action-conditioned representation** between `z_world` and policy | ARC-002 (E2 is the fast forward predictor of affordances) -- a predictor, not a structured object downstream machinery consumes. ARC-129 (consumed present is an affordance-conditioned forward-displaced prediction) -- says the conditioning exists, never that it is itself represented. MECH-125 constrains how E3 *scores*, not what it is *given*. | **adjacent-but-distinct -> registered narrowly as ARC-149**, carrying a separability falsifier (a direct `z_world -> policy` map at matched capacity reproducing the full phenotype withdraws it) |
| **The field has metric/geometric structure** -- neighbouring trajectories in neighbouring regions; lawful deformation under single-factor interventions while world identity stays stable | MECH-151 already calls the target an "action-affordance **manifold**" but asserts only a *bias vector* over it. MECH-528 presupposes addressable "affordance regions" and says what self-state uncertainty does to them. ARC-080/ARC-082 bind afforded actions to object-files -- token-indexed, not geometric. | **adjacent-but-distinct -> registered narrowly as MECH-575**. MECH-151 could hold in full while MECH-575 is false; MECH-528 and MECH-575 are partners but neither entails the other |
| **Rival tendencies alternate temporally** before commitment rather than summing; dwell-time / switching-rate statistics separate deliberation from flicker and perseveration | MECH-140 (soft-competitive disinhibition, not WTA) is about the *shape* of competition and is compatible with concurrent co-activation -- it is MECH-576's **primary falsifier**, not its owner. MECH-488's `gap_norm` is exactly the instantaneous scalar compression the thought predicts is insufficient. MECH-487 is *post-rejection* retention. SD-033e/MECH-264 hold parallel counterfactual values -- concurrent, not alternating. MECH-483 supplies the orient/survey tendency state. | **adjacent-but-distinct -> registered narrowly as MECH-576** |
| **Phase-shared + phase-exclusive sensorimotor subspaces**, overlap varying along the path | MECH-561 (phase as address) is the nearest, and the distinction is load-bearing: MECH-561's phase is an **endogenous cyclic** coordinate indexing an inter-engine communication subspace, and it is `implementation_phase: v3`. The thought's phase is a **task/processing** phase (orienting/rollout/preparation/execution), non-cyclic, a property of where the organism is in an action. | **adjacent-but-distinct -> registered narrowly as MECH-577**, with an explicit warning that a V3 MECH-561 result is not evidence about MECH-577 |
| **Commitment is a jurisdiction change** -- one path acquires privileged ability to alter body and world, retaining an interrupt/rebranch route | MECH-090 (beta gating of E3 -> action propagation), MECH-342 (release of an elevated latch when readiness degrades mid-commitment), MECH-138 (cancel-window-open flag). ARC-145 supplies the jurisdiction vocabulary for the inter-engine *information* case. | **already owned -> cross-ref only.** The thought contributes unifying language, not new falsifiable content |
| **The structured proposal object** (trajectory + consequences + confidence + provenance + affective exposure + reconstructible grounds + dominance) | Union of MECH-487 (provenance-tagged candidate retention: identity plus trajectory/value sketch, not a transient scalar), MECH-035 (vector valence, ranked without scalar collapse), MECH-125 (multi-constraint viability), ARC-115 (non-collapsible confidence readouts), MECH-530 (non-oracular output typing) | **already owned -> cross-ref only** |
| **Ethics begins as affectively/socially organised consequence and is cognitively reconstructed later**; E3 as umpire, not cold veto | ARC-094 (no empathy module / no empathy scalar), MECH-405 (fast-empathy stream binding), MECH-127 (counterfactual other-cost-aversion as a *motivational* surrogate, i.e. entering before selection, which is the thought's "not an afterthought" requirement), MECH-485 (predicted-harm triage), INV-084 (kindness is not constraint compliance), MECH-125. **And most directly MECH-569.** | **already owned -> cross-ref only.** See the convergence note below |
| **"Local success without organismal benefit"** failure mode | The thought's own cited parent `2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`, registered as GOV-JURIS-1 / GOV-ECOL-1 / GOV-HOTHER-1 / GOV-DELETE-1 / Q-108 | **already owned -> cross-ref only** |

### The convergence worth naming

**MECH-569 was registered on 2026-09-18 -- the same day this thought was written -- from a
completely unrelated route**: the `ree-lit-pull-am-b` scheduled literature pull for ARC-089 /
ARC-094, via the raw thought `2026-09-18_fast_empathy_bootstraps_cognitive_empathy.md`. It
asserts that the fast affective route is the developmental scaffold from which the slower
mentalizing route differentiates.

This thought's ethics section independently arrives at the same shape and applies it to
ethical grounds specifically: *"what later becomes ethical thought begins as affectively and
socially organised consequence... This later reconstruction is crucial; it is not the origin
of ethical relevance."* Two routes, same day, same structure. That is an extraction success,
not a registration gap -- and it is the kind of corroboration the registry exists to make
visible.

---

## 3. Key formulations (verbatim)

> It is not merely a motor primitive library. Skills supply the possible primitives; the
> affordance field says which primitive or sequence is currently viable, available, relevant,
> and consequential from this body-state in this world-state.

> The important object is a **field**, not a list. Similar trajectories should occupy related
> regions; blocked or costly trajectories should be visibly deformed or down-weighted;
> changing a resource, threat, bodily capability, or social constraint should alter the
> reachable geometry.

> This makes the present not a point but a temporally displaced, action-indexed surface. The
> organism has already partly entered a future through its set of reachable next states,
> without yet being committed to one.

> A policy can become dominant because it is better supported, more stable, more precise,
> compatible with constraints, or survives longer under counterfactual scrutiny. That differs
> from simply being assigned the largest instantaneous score.

> alternation between tendencies may be a normal precommitment regime, not necessarily
> indecision or failure. The relevant question is when alternation becomes productive
> deliberation, and when it becomes pathological flicker, perseveration, or unsafe delay.

> The shared structure preserves continuity: the action remains about the same world, body and
> other agents. Phase-specific structure permits different computations: exploration requires
> preserving alternatives; execution requires suppressing many alternatives in favour of
> robust control and rapid feedback.

> So E3 should not be framed as a cold ethical veto that adds morality after value. It is the
> umpire of affectively shaped, socially consequential trajectories.

> A good result is not merely better reward. It is that the representation's geometry predicts
> **which trajectories have become reachable or unavailable**, and why.

---

## 4. Affected existing claims

**Cross-referenced (`depends_on` wiring only -- nothing amended).** No existing claim's
`status`, `confidence`, `epistemic_category` or evidence record was touched by this pass.

- ARC-149 -> ARC-002, ARC-082, ARC-129, MECH-125, MECH-151, MECH-528, SD-044, ARC-145
- MECH-575 -> ARC-149, MECH-151, MECH-528, ARC-082, ARC-080
- MECH-576 -> ARC-149, MECH-140, MECH-483, MECH-487, MECH-488, MECH-432, SD-033e
- MECH-577 -> ARC-149, MECH-561, ARC-145, MECH-575

**Explicitly distinguished-from, and the distinction is load-bearing in each case:**

- **MECH-140 vs MECH-576** -- MECH-140 is MECH-576's primary falsifier, deliberately. If
  concurrent soft-competitive arbitration reproduces commitment outcomes and latencies at
  matched capacity, MECH-576 is refuted. Wiring it as a dependency without saying this would
  invite a future session to read MECH-140 as *support*.
- **MECH-561 vs MECH-577** -- different senses of "phase" (endogenous cyclic vs task
  phase), different implementation phases (v3 vs v4). A V3 phase-as-address result must not
  be read as support for MECH-577.
- **MECH-151 vs MECH-575** -- a bias vector over a manifold is not a claim about the
  manifold's geometry.
- **ARC-145 vs ARC-149** -- jurisdiction over inter-engine *information* routing vs the
  content of what E3 arbitrates over.

---

## 5. Candidate claims -- REGISTERED this pass

All four: `status: candidate`, `epistemic_category: substrate_conditional`,
`implementation_phase: v4`, `version_relevance: v4_v5`, `registered_utc: 2026-09-22`,
`location: docs/architecture/affordance_valuation_bridge.md#<id>`.

| id | type | subject | one-line |
|---|---|---|---|
| **ARC-149** | architectural_commitment | `architecture.affordance_valuation_bridge` | An intermediate, action-conditioned representation between the world model and E3 is architecturally necessary; a direct `z_world -> policy` map reproducing the full phenotype (not just reward) withdraws the commitment |
| **MECH-575** | mechanism_hypothesis | `representation.action_conditioned_affordance_geometry` | That representation is a field with metric structure that deforms lawfully under single-factor interventions while world identity stays decodable; a pure re-ranking of a fixed candidate set refutes it (thought's assay A) |
| **MECH-576** | mechanism_hypothesis | `commitment.precommitment_tendency_alternation` | Rival tendencies alternate as discrete states before commitment rather than summing, and dwell/switch statistics separate deliberation from flicker and perseveration (thought's assay C) |
| **MECH-577** | mechanism_hypothesis | `representation.sensorimotor_phase_subspace_gradient` | The sensorimotor path carries shared world-anchored plus phase-exclusive dimensions with varying overlap; falsified from both directions (fully shared, or fully serial) (thought's assay B) |

Each carries a pre-registered falsifier in its `title` and an explicit **DO NOT build in V3 /
DO NOT queue an experiment** caveat in its `notes`. Per the skill, **no `what_would_answer`
was drafted** -- that is `/thought-digestion`'s job.

---

## 6. Next steps

1. **Version-routing decision is OWED to `/governance`.** The raw thought says "V3 assays
   first; richer social consequences are later-tier work". All four claims are registered
   `v4` / `v4_v5` per the ingestion default because none is cleanly and cheaply testable on
   substrate that exists in V3 today. **This disagreement is deliberate and flagged, not
   resolved.** MECH-577 is the most likely candidate for a V3 re-route given MECH-561 sits at
   `implementation_phase: v3`.
2. **Assay D was not registered as a claim.** The thought's ethical-arbitration test (two
   paths, one locally advantageous and harmful to another agent; compare scalar action value
   / late veto only / annotated affordance field plus E3 arbitration) is an *experiment
   design*, not a claim. It is a plausible `/queue-experiment` candidate once ARC-149 has a
   substrate, and is recorded here so it is not lost. Do not queue it now -- there is nothing
   to run it against.
3. **Literature is unverified as REE evidence, deliberately.** The Diomedi et al. (Commun
   Biol) and Starkweather et al. (Nat Neurosci) 2026 papers were read only as the thought
   reports them; neither was independently pulled, and per `feedback_lit_exp_decoupled`
   neither strengthens any REE claim's confidence. A `/lit-pull` against MECH-576 and
   MECH-577 would be a reasonable follow-on but is **not** a prerequisite for anything here.
4. **Deliberately left unregistered:** the four "already owned" threads in section 2. If a
   future session believes any of them is genuinely uncovered, the burden is to say which of
   the cited claims fails to cover it -- not to re-register.

---

## 7. Digestion drafts

**None produced this pass.** Per the skill, ingestion stops at `candidate` and does not draft
`what_would_answer`. The four claims are live input to the next `/thought-digestion` run.
