# Object-Representation Thread — Coherence / Design-Review Synthesis

**Type:** intake / synthesis (planning memo — NOT a claim, NOT a substrate spec)
**Date:** 2026-06-04
**Trigger:** SD-057 (`drive.object_bound_incentive_salience`) landed 2026-06-04. The goal
stream now binds benefit to OBJECT IDENTITY (SD-049 per-type tag), keeps a per-object
incentive token with a stored `z_object` embedding, seeds `z_goal` from the most-wanted
object's embedding, and has a cue-recall path + object-discriminative dACC readout.
User observation: *"the idea of objects has now begun to be part of functioning."*
User named four planned object capabilities: **(1) object permanence, (2) self as a
special object, (3) objects as tools, (4) others as special objects** — and asked whether
claims / lit / design / developmental-plans / current state are coordinated to support an
object-representation layer with clean insertion points, **without distracting from V3
closure.**

**Status of this memo:** SYNTHESIS + RECOMMENDATIONS for user decision. No claims
registered, no `claims.yaml` edit, no substrate code, no experiments queued. The proposed
ARC spine below is a PROPOSAL only.

> **HARD CONSTRAINT honoured.** Nothing here touches or reprioritises the V3-closure
> critical path. `goal_pipeline:GAP-7`'s remaining deliverable — the GAP-2-gated L9
> wanting≠liking behavioural retest (owned by `scaffolded_sd054_onboarding`) — is
> untouched. SD-057's resource-bound object-identity stays exactly as-is for V3. Almost
> everything below is V4-leaning or cross-cutting; the V3/V4 boundary is kept explicit in
> §4.

---

## 1. Current-state map — where object-ness already exists

The substrate already contains object-related machinery, but it sits in **three
disconnected lineages plus two V4 pillars**, none of which reference each other through a
shared representational spine.

### 1.1 Capability → existing fragments → what's missing

| Capability | Existing fragments (claim ids + files) | Lineage | Status in code | What's missing |
|---|---|---|---|---|
| **Object as identity latent (live)** | SD-015 `z_resource` (learned, location-invariant embedding); SD-049 per-type identity tag + identity-classifier head + per-axis drive; SD-057 `IncentiveTokenBank` (`z_object` = detached `z_resource` clone + revaluable `base_value`); MECH-262 (`z_resource`/`z_world` re-convergence at hippocampal planning); MECH-344/345/346/347/348. Files: `ree-v3/ree_core/latent/stack.py` (ResourceEncoder), `ree-v3/ree_core/goal.py` (IncentiveTokenBank), `sd_015/sd_049/sd_057_*.md` | **C — implemented identity-latent** | LIVE, default-OFF flags | Identity is keyed on the SD-049 **resource type** (≈3 categories: food/water/novelty) and coupled to the drive/goal axis. Not a general object; SD-057 itself says "a learned affordance embedding is the upgrade path, not v1." Does NOT cite ARC-006 / MECH-045 / MECH-278. |
| **Object-file / binding / persistence (representational)** | ARC-006 "Entities are sparse, persistent, bindable structures" (`provisional`); MECH-044 hippocampal relational binding (`provisional`); MECH-045 "object-file-like buffers provide minimal entity persistence across time" (`provisional`); MECH-050 functional locality. Files: `docs/architecture/entities_and_binding.md`, `docs/thoughts/2026-02-10_object_file_persistence.md` | **A — dormant representational** | NOT in ree-v3 code (design-only, legacy 2026-02-10 source) | The entire layer is orphaned. No biology lit-pull exists (sources are internal thoughts + DANIEL_README). `entities_and_binding.md` Status Note explicitly flags "relationship to social cognition (self/other modeling)" as unspecified — it already gestures at self/other-as-object but was never connected. |
| **Object as causally-coherent feature bundle (definition)** | MECH-278 "object-schema formation… an object is the stable bundle of features that behave causally together under interventional perturbation"; MECH-277 (action-space discovery / self-as-object); MECH-276 (scientist-agent); ARC-059 (3-stage ordering). Files: `claims.yaml`, `developmental_needs_register.md` DEV-NEED-033 | **B — developmental ordering** | `candidate`, `v3_pending`; NOT validated end-to-end | MECH-278 explicitly notes V3's `z_world` is engineered pre-split → **"architectural shortcut past stage 2"** (objects-as-patterns is *bypassed* in V3). The object DEFINITION exists but isn't operationalised. |
| **(1) Object permanence** | SD-039 dual-trace `AnchorGoalPayload`; MECH-292 ranked ghost-goal bank; MECH-293 ghost-goal probe search (Bouton dual-trace). Files: `ree-v3/ree_core/hippocampal/{anchor_set,ghost_goal_bank,module}.py`, `sd_039/mech_292/mech_293_*.md` | partial (D) | LIVE | Stores per-anchor **goal-value snapshots** that persist when not perceived — a *motivational*-persistence primitive, NOT object permanence. Keyed by spatial anchor, payload is `z_goal_snapshot`+wanting (not an object-identity code); queries by *wanting rank*, not "where is object X now." Missing: token-instance tracking through occlusion. |
| **(3) Objects as tools / affordances** | SD-016 `cue_action_proj` (affordance bias for E2), `cue_terrain_proj`, `world_query_proj`. Files: `ree-v3/ree_core/predictors/e1_deep.py`, `sd_016_frontal_cue_integration.md` | E | LIVE but **UNGROUNDED** | `cue_terrain_proj` works (E3 precision). `cue_action_proj` is inert: V3-EXQ-449 found 0.0 gradient (non-differentiable CEM blocks the path; signal vanishes before E3.select). EXP-0155 queued to instrument. No grounded object→action pathway exists. |
| **(2) Self as a special object** | z_self (SD-005 self/world split; SD-030 E2 self-forward-model V4-deferred); DR-10..DR-14 self-model integration audit; MECH-214 (goal must be E1-representable); MECH-215 (self-model prerequisite for agentive prediction); INV-064 (maturational-sequence necessity). Files: `ree-v3/ree_core/latent/stack.py`, `v4_spec.md` §V4-2, `ree-v3/CLAUDE.md` (self-model audit), `psychiatric_failure_modes.md`, `sd_030_e2_self_forward_model.md` | F (V4) | z_self LIVE as proprioceptive/interoceptive latent (single MLP + EMA) | z_self is a body-state latent, **not a self-OBJECT slot**. DR-10 (not in E3 scoring), DR-11 (no z_goal_self domain), DR-12 (E2 PE not modulating E3 confidence), DR-13 (no temporal depth/recurrence), DR-14 (env doesn't dissociate proxy from hedonic). All V4. |
| **(4) Others as special objects** | ARC-010 mirror modelling (`stable`); ARC-047 SocialGridWorld scent harness (`candidate`, v4); MECH-031/032/036/041 (derived social tags, empathy coupling, other-harm veto, affective broadcast); MECH-051/052/127/159/190. Files: `social.md`, `v4_spec.md` §V4-1 | G (V4) | design-only | Each other-agent j needs its own `z_self_j`, `z_harm_a_j`, drive, commitment chain — an "other-as-object" slot. Gated on MECH-163 (multi-step hippocampal planning) before V4 entry. |

### 1.2 The register already names the thread — but as ordering, not representation

`developmental_needs_register.md` already encodes:
- **DEV-NEED-033** ↔ ARC-059: the self→objects→others ordering (the user's pillars 2→(implicit object)→4).
- **DEV-NEED-021**: "Otherness inference *after* self-stability" — required substrate lists **object persistence** as a prerequisite for other-modelling. So the register *already treats object permanence as load-bearing for the social pillar*, but the permanence substrate it presupposes (a true object-file persistence buffer) does not exist — only the goal-snapshot ghost bank does.

---

## 2. Coherence assessment

### 2.1 Is there an ARC-level claim articulating OBJECTS as a representational primitive?

**No — and that is the gap.** What exists is:
- A **representational** primitive (ARC-006/MECH-044/MECH-045) that is *dormant* (provisional, design-only, no code, no biology).
- A **developmental ordering** primitive (ARC-059/MECH-277/278) that *names* self-as-object, objects-as-patterns, and others-as-object — but as a training-sequence claim, and with the object DEFINITION (MECH-278) explicitly bypassed in V3.
- A **live identity latent** (SD-015→049→057) that actually runs — but on the narrow resource/drive rail, having effectively reinvented a per-object store (`IncentiveTokenBank`, `z_object`) **without wiring to either the dormant object-file layer or MECH-278's object definition.**

So "objects have begun to be part of functioning" is accurate — but on a single resource-bound spur, disconnected from the representational layer that was sketched four months ago (ARC-006) and from the developmental claim that already enumerates the four pillars (ARC-059). There is no spine connecting them.

### 2.2 Duplication / conflict risk

**Three overlapping per-item stores, three different keys, none citing the canonical object-file layer:**

| Store | Key | Payload | Lifecycle | Claim |
|---|---|---|---|---|
| `IncentiveTokenBank` (SD-057) | resource **type tag** (k) | `base_value` + `z_object` (detached z_resource) | concurrent, drive-revaluable, waking | MECH-344/345/346 |
| `AnchorGoalPayload` / ghost bank (SD-039/MECH-292) | spatial **anchor** | `z_goal_snapshot` + wanting + arousal | inactive-anchor retrospective store | SD-039/MECH-292 |
| Object-file buffer (ARC-006/MECH-045) | entity **token** | features bound across time | attention-gated persistence | MECH-045 (dormant) |

SD-057's doc *does* cleanly distinguish itself from the ghost bank ("inactive-anchor store" vs "concurrent per-object-type store") — good. But **none of the three cite ARC-006/MECH-045**, the supposed canonical object-file layer. **Risk:** a fourth per-item store gets built for permanence or tools without anyone noticing three already exist with overlapping intent.

**"Object" currently means at least three different things:**
1. a **type/category** (SD-049 tag, `z_resource` is location-invariant → a *type*);
2. a **spatial anchor** (hippocampal anchor in the ghost bank);
3. a **feature-bundle token entity** (MECH-278 / ARC-006).

Biology separates these: object-files are **token-instance** ("*this* apple, tracked through occlusion") distinct from category ("apples"). REE's live work is at the **type** level. **True object permanence needs token-instance tracking — a genuine representational gap, not just a missing flag.** Any unified object primitive must decide whether the unit is a type, a token, or an anchor.

### 2.3 Where a unified object representation would need to live

A coherent layer would generalise `z_object`/`z_resource` out of the resource silo into an
**object-file / binding layer** that:
- keys on an **entity token** (not only a resource type tag),
- stores an **identity embedding** (generalised `z_object`) + a **persistence/state buffer** (the out-of-view continuation), and
- is **consumed by**: (i) the incentive bank (SD-057, drive/goal axis), (ii) hippocampal anchors + planning (MECH-262/SD-039), (iii) the self-model slot (z_self, V4), (iv) the social other-slots (z_self_j, V4), and (v) the affordance/action map (SD-016, tools).

ARC-006/MECH-044/MECH-045 is the natural home — but it needs reactivation, a biology
grounding, and explicit wiring to the live `z_resource` lineage and to MECH-278's object
definition. This is exactly the "consolidate the scattered fragments into a coherent layer
with clean insertion points" the user asked about.

---

## 3. Proposed ARC spine (PROPOSAL — not registered)

Two structural options; I recommend a thin umbrella (Option A) over a heavy rewrite.

**Option A (recommended) — a thin umbrella ARC naming objects as a primitive, pointing at
the existing pieces.** Register one new architectural_commitment, e.g.
`ARC-OBJ: object identity is a cross-cutting representational primitive`, whose body is a
**coherence map**, not new mechanism:

```
ARC-OBJ  (proposed, architectural_commitment)
  "An object is a token-bound identity representation that persists across time and
   perceptual gaps, generalising z_object/z_resource into an object-file/binding layer
   (ARC-006), defined by causal feature-coherence under intervention (MECH-278), consumed
   by drive/goal (SD-057), hippocampal planning (MECH-262), and the self/other special-
   object cases. The four object capabilities are specialisations of one primitive."

  ├─ representational substrate ........ ARC-006 / MECH-044 / MECH-045 (reactivate + ground)
  ├─ object definition ................. MECH-278 (causal feature bundle under intervention)
  ├─ developmental ordering ............ ARC-059 (self → objects → others)
  ├─ live identity latent .............. SD-015 → SD-049 → SD-057 (generalise z_object)
  │
  ├─ PILLAR 1  permanence .............. NEW child (token persistence through occlusion);
  │                                      reactivate MECH-045; generalise ghost-goal bank
  │                                      from goal-snapshot to object-token. [V3-straddle/V4]
  ├─ PILLAR 2  self-as-object .......... z_self as a privileged object-file slot
  │                                      (DR-10..14, MECH-214/215, INV-064). [V4]
  ├─ PILLAR 3  tools / affordances ..... object→action binding; ground SD-016
  │                                      cue_action_proj. [V3-substrate, ungrounded]
  └─ PILLAR 4  others-as-object ........ other-agent object-file slots (z_self_j, z_harm_a_j);
                                         ARC-010 / ARC-047. [V4]
```

Pros: minimal footprint, no rename of the live SD-015/049/057 lineage, makes the spine
machine-readable via `depends_on`, and gives each future pillar a registered parent so it
"slots in cleanly." Cons: ARC-006 is purely representational while the pillars mix
representation + development, so ARC-OBJ has to span both — acceptable for an umbrella.

**Option B — reactivate ARC-006 itself as the spine** (extend its scope from "entities are
bindable" to "objects are the cross-cutting primitive" and hang the pillars off it). Lighter
in claim count but overloads a `provisional` legacy claim and muddies its history. Not
recommended; prefer a fresh umbrella that *depends_on* ARC-006.

**Either way, the spine's job is documentation + insertion points, not new mechanism.** The
first concrete substrate step (whenever it comes, post-V3) is generalising `z_object` from a
type-tag store to a token-keyed object-file — which is a V4 / late-V3 substrate task, not
part of this memo.

---

## 4. Recommended literature pulls (biology before formal definitions)

Per the project rule (`feedback_biology_before_formal_definitions`): commission these
**before** registering any new object-file / permanence / self-as-object / other-as-object
claim. Note that ARC-006/MECH-044/MECH-045 currently have **no biology lit-pull at all**
(sources are internal 2026-02 thoughts) — that gap should be closed first if the spine is
adopted. Do **not** run these now; recommend for user approval.

| # | Pull topic | Key anchors | REE claims it would ground | Priority |
|---|---|---|---|---|
| L1 | **Object files & feature binding** | Kahneman, Treisman & Gibbs 1992 (object files / reviewing); Treisman & Gelade 1980 (FIT); Treisman binding problem | ARC-006, MECH-044, MECH-045; generalised `z_object` (Option A spine). **Foundational — pull first.** | High |
| L2 | **Object permanence** (token-instance, occlusion) | Piaget A-not-B; Baillargeon violation-of-expectation (drawbridge); Spelke core-knowledge object principles; Kellman & Spelke 1983 (perceptual completion) | PILLAR 1 permanence; distinguishes token-tracking from type (the §2.2 gap) | High |
| L3 | **Affordances / objects-as-tools** | Gibson 1979 (affordances); Rizzolatti/Murata canonical neurons (AIP); Khetarpal et al. (affordances in RL) | PILLAR 3; SD-016 grounding rationale | Medium |
| L4 | **Self-as-object / minimal self & body-as-object** | Gallagher minimal vs narrative self; Head & Holmes / de Vignemont (body schema); Botvinick & Cohen rubber-hand; Blanke bodily self | PILLAR 2; z_self-as-object; MECH-214/215 | Medium (V4) |
| L5 | **Theory of mind / others-as-agents** | Premack & Woodruff; Baron-Cohen ToMM; Woodward 1998 (infant goal attribution); Gergely & Csibra teleological stance / natural pedagogy (partly cited via ARC-077) | PILLAR 4; ARC-010 / ARC-047 / MECH-031 | Medium (V4) |

---

## 5. Developmental sequencing — V3 vs V4, with insertion points

### 5.1 Where each piece sits

| Capability | V3/V4 | State | On V3-closure critical path? |
|---|---|---|---|
| Object-identity IN GOALS (SD-057) | **V3** | LANDED (resource-bound) | The L9 retest is — but **that's owned elsewhere and untouched here** |
| Permanence — motivational (ghost-goal bank) | **V3** | LANDED (goal-snapshot, partial) | No |
| Permanence — object token through occlusion | **V3-straddle / V4** | NOT built | **No — must NOT enter V3 closure** |
| Object-schema formation (MECH-278, objects-as-patterns) | **V4** | BYPASSED in V3 (engineered z_world) | No |
| Tools / affordances (SD-016) | **V3 substrate / V4-grounding** | LIVE but UNGROUNDED (EXP-0155 gate) | No — separate existing track |
| Self-as-object (z_self, DR-10..14) | **V4** | latent only | No |
| Others-as-object (ARC-010/047) | **V4** | design only | No |

### 5.2 Dependency edges (the ordering is load-bearing)

```
self-as-object (MECH-277, action-space discovery)
      └─> objects-as-patterns (MECH-278, object-schema formation)
              └─> others-as-special-objects (ARC-010, V4)        [ARC-059 ordering]

object-file / persistence primitive (ARC-006 reactivated, generalised z_object)
      ├─ temporal axis  -> PILLAR 1 permanence
      ├─ action axis    -> PILLAR 3 tools / affordances (SD-016)
      └─ special slots  -> PILLAR 2 self  +  PILLAR 4 other   [both V4]

DEV-NEED-021 (register): otherness inference REQUIRES object persistence + self-stability
  => PILLAR 1 (permanence) and PILLAR 2 (self) are prerequisites for PILLAR 4 (others).
```

**Proposed ordering (post-V3, nothing pulled forward):**
1. **Spine + grounding (doc-only, V3-safe):** if adopted, register the Option-A umbrella as a coherence map and commission L1/L2 lit pulls. Zero code. This is the only piece that could happen during the V3 era because it touches no substrate and no critical-path file.
2. **Generalise `z_object`** from type-tag to token-keyed object-file (the first real substrate step) — **V4 / late-V3 substrate enrichment.**
3. **PILLAR 1 permanence** (token persistence through occlusion) on top of the generalised object-file; reuses/extends the ghost-goal bank.
4. **PILLAR 3 tools** — ground SD-016 (its own existing track via EXP-0155 / differentiable-CEM SD-055); fold into the object→action axis once the object-file exists.
5. **PILLAR 2 self-as-object** — V4, gated by the DR-10..14 self-model integration audit + MECH-163.
6. **PILLAR 4 others-as-object** — V4, gated on MECH-163 multi-step planning and on Pillars 1+2 per DEV-NEED-021.

### 5.3 What must NOT enter V3 closure (explicit)

- No generalisation of `z_object`/`IncentiveTokenBank` beyond resource types as part of GAP-7.
- No new permanence / object-file substrate, no SD-016 grounding work, no self/other-object work bundled into the L9 wanting≠liking retest.
- SD-057 stays resource-bound for V3. The object-representation thread is a **deliberate V4-leaning consolidation**; the only V3-era-safe action is the documentation spine in §3 (and only if the user wants it now).

---

## 6. Recommendation set (for user decision)

1. **Decide on the spine.** Adopt **Option A** (a thin `ARC-OBJ` umbrella as a coherence
   map with the four pillars as registered children) — recommended — or defer entirely to
   V4. The umbrella is doc-only and V3-safe; it is the cheapest way to stop the fragments
   drifting further and to give permanence/self/tools/others clean parents to slot into.
2. **If adopted, commission L1 + L2 lit pulls first** (object files; object permanence) —
   they ground both ARC-006 (which has *no* biology today) and the token-vs-type
   permanence gap. L3/L4/L5 follow when their pillars are scheduled.
3. **Connect the live lineage to the dormant layer in docs** regardless of the spine
   decision: add cross-references so SD-057/`IncentiveTokenBank`, SD-039/ghost-bank, and
   ARC-006/MECH-045 explicitly acknowledge each other as three per-item stores (prevents a
   fourth being built blind).
4. **Hold everything substrate-level for V4 / late-V3.** Do not touch V3 closure. The L9
   GAP-7 retest remains owned by `scaffolded_sd054_onboarding`.
5. **Note the genuine representational gap** for whenever the object-file work begins:
   REE's live object identity is **type-level**; true permanence/tools/self/other need
   **token-instance** object-files. That decision (type vs token vs anchor as the unit) is
   the first design fork.

---

## Appendix — file/claim index (for the next session)

- Live identity latent: `ree-v3/ree_core/latent/stack.py` (ResourceEncoder), `ree-v3/ree_core/goal.py` (IncentiveTokenBank); `docs/architecture/sd_015_z_resource_encoder.md`, `sd_049_multi_resource_heterogeneity.md`, `sd_057_object_bound_incentive_salience.md`. Claims SD-015, SD-049, SD-057, MECH-262, MECH-344..348.
- Dormant representational: `docs/architecture/entities_and_binding.md`; `docs/thoughts/2026-02-10_{object_file_persistence,hippocampal_relational_binding}.md`. Claims ARC-006, MECH-044, MECH-045, MECH-050.
- Developmental ordering / object definition: `claims.yaml` ARC-059, MECH-276/277/278; `developmental_needs_register.md` DEV-NEED-021, DEV-NEED-033.
- Permanence (partial): `ree-v3/ree_core/hippocampal/{anchor_set,ghost_goal_bank,module}.py`; `sd_039_anchor_goal_payload.md`, `mech_292/293_*.md`. Claims SD-039, MECH-292, MECH-293.
- Tools/affordances: `ree-v3/ree_core/predictors/e1_deep.py`; `sd_016_frontal_cue_integration.md`. Claim SD-016 (cue_action_proj UNGROUNDED — EXP-0155, V3-EXQ-449).
- Self-as-object (V4): `ree-v3/ree_core/latent/stack.py` (z_self); `v4_spec.md` §V4-2, `ree-v3/CLAUDE.md` self-model audit, `psychiatric_failure_modes.md`, `sd_030_e2_self_forward_model.md`. Claims MECH-214, MECH-215, INV-064, DR-10..DR-14, SD-005, SD-030.
- Others-as-object (V4): `social.md`, `v4_spec.md` §V4-1. Claims ARC-010, ARC-047, MECH-031/032/036/041/051/052/127/159/190.
