---
title: ARC-080 -- Object Identity as a Cross-Cutting Representational Primitive
parent: "Attention, Binding & Objects"
grandparent: Architecture
nav_order: 1
status: candidate
status_asof: 2026-09-01
status_claim: ARC-080
---

# ARC-080 -- Object Identity as a Cross-Cutting Representational Primitive

**Claim Type:** architectural_commitment (thin umbrella / coherence map)
**Scope:** Object identity as one representational primitive underlying permanence, self-as-object, tools/affordances, and others-as-object
**Status:** candidate (`v3_pending: false`, `implementation_phase: v4`) -- v3_pending cleared 2026-09-01 (GOV-V4CUT-1 F4, GFLAG-0104); see the claims.yaml UPDATE note
**Claim ID:** ARC-080
<a id="arc-080"></a>
**Depends On:** ARC-006 (object-file / binding substrate), MECH-278 (object definition), ARC-059 (developmental ordering), SD-015 / SD-049 / SD-057 (live identity latent)
**Registered:** 2026-06-04
**Source memo:** [`evidence/planning/object_representation_thread_2026-06-04.md`](../../evidence/planning/object_representation_thread_2026-06-04.md) (the full brief -- this doc is the "Option A" spine adopted by the user 2026-06-04)

> **This is documentation + governance only.** ARC-080 introduces NO substrate
> code, NO experiments, and changes NO V3 behaviour. It is a *coherence map*: it
> names objects as a single cross-cutting primitive and gives the scattered
> object-related fragments a registered parent (via `depends_on`) so future pillar
> work slots in cleanly instead of drifting into a fourth blind per-item store.
> It does **not** promote anything. The V3-closure critical path
> (`goal_pipeline:GAP-7`, `scaffolded_sd054_onboarding`, SD-057's resource-bound
> behaviour) is untouched.

---

## 1. Why this umbrella exists

SD-057 (`drive.object_bound_incentive_salience`) landed 2026-06-04. The goal
stream now binds benefit to OBJECT IDENTITY (SD-049 per-type tag), keeps a
per-object incentive token with a stored `z_object` embedding, and seeds `z_goal`
from the most-wanted object's embedding. The user's observation -- *"the idea of
objects has now begun to be part of functioning"* -- is accurate, but the object
machinery sits in **three disconnected lineages** with no shared representational
spine, and the user named four planned capabilities (permanence, self-as-object,
tools, others-as-object) that need clean insertion points without distracting
from V3 closure.

ARC-080 is the spine. Its job is to assert that an object is a **token-bound
identity representation that persists across time and perceptual gaps**, to
generalise `z_object`/`z_resource` into an object-file/binding layer, and to
record that the four capabilities are **specialisations of one primitive**, not
four separate mechanisms.

---

## 2. Current-state map -- the three disconnected lineages

Object-ness already exists in the substrate, but the lineages do not reference
each other through any shared spine.

### Lineage A -- DORMANT representational layer

ARC-006 ("entities are sparse, persistent, bindable structures", `provisional`) +
MECH-044 (hippocampal relational binding, `provisional`) + MECH-045
("object-file-like buffers provide minimal entity persistence across time",
`provisional`). Files: [`entities_and_binding.md`](entities_and_binding.md);
`docs/thoughts/2026-02-10_object_file_persistence.md`.

- **State:** NOT in ree-v3 code (design-only, legacy 2026-02-10 source). The
  entire layer is orphaned. Until the 2026-06-04 L1/L2 lit pulls there was **no
  biology lit-pull at all** (sources were internal thoughts + DANIEL_README).
- `entities_and_binding.md`'s Status Note already flags "relationship to social
  cognition (self/other modeling)" as unspecified -- it gestures at
  self/other-as-object but was never connected.

### Lineage B -- DEVELOPMENTAL-ORDERING layer (with the object DEFINITION)

MECH-278 ("an object is the stable bundle of features that behave causally
together under interventional perturbation") + MECH-276 (scientist-agent) +
MECH-277 (action-space discovery / self-as-object) + ARC-059 (3-stage
self->objects->others ordering). Files: `claims.yaml`,
[`developmental_needs_register.md`](developmental_needs_register.md)
DEV-NEED-033.

- **State:** `candidate`, `v3_pending`; not validated end-to-end. MECH-278
  explicitly notes V3's `z_world` is engineered pre-split -- an **"architectural
  shortcut past stage 2"**. The object DEFINITION exists but is *bypassed* in V3.

### Lineage C -- LIVE resource-bound identity latent

SD-015 `z_resource` (learned, location-invariant embedding) -> SD-049 per-type
identity tag + classifier head + per-axis drive -> SD-057 `IncentiveTokenBank`
(`z_object` = detached `z_resource` clone + revaluable `base_value`); plus
MECH-262 (`z_resource`/`z_world` re-convergence at hippocampal planning) and
MECH-344..348. Files: `ree-v3/ree_core/latent/stack.py` (ResourceEncoder),
`ree-v3/ree_core/goal.py` (IncentiveTokenBank);
[`sd_015_z_resource_encoder.md`](sd_015_z_resource_encoder.md),
[`sd_049_multi_resource_heterogeneity.md`](sd_049_multi_resource_heterogeneity.md),
[`sd_057_object_bound_incentive_salience.md`](sd_057_object_bound_incentive_salience.md).

- **State:** LIVE, default-OFF flags. But identity is keyed on the SD-049
  **resource type** (~3 categories: food/water/novelty) and coupled to the
  drive/goal axis. It is **not a general object** -- SD-057 itself says "a learned
  affordance embedding is the upgrade path, not v1" -- and it cites **neither**
  ARC-006/MECH-045 **nor** MECH-278.

### The coherence gap

So "objects have begun to be part of functioning" is true -- but on a single
resource-bound spur, disconnected from the representational layer sketched four
months earlier (ARC-006) and from the developmental claim that already enumerates
the four pillars (ARC-059). **There is no spine connecting them.** That is the gap
ARC-080 fills.

---

## 3. The three overlapping per-item stores (the anti-duplication payload)

Three per-item stores already exist, with three different keys, **none citing the
canonical object-file layer**:

| Store | Key | Payload | Lifecycle | Claim |
|---|---|---|---|---|
| `IncentiveTokenBank` (SD-057) | resource **type tag** (k) | `base_value` + `z_object` (detached `z_resource`) | concurrent, drive-revaluable, waking | MECH-344/345/346 |
| `AnchorGoalPayload` / ghost bank (SD-039/MECH-292) | spatial **anchor** | `z_goal_snapshot` + wanting + arousal | inactive-anchor retrospective store | SD-039 / MECH-292 / MECH-293 |
| Object-file buffer (ARC-006/MECH-045) | entity **token** | features bound across time | attention-gated persistence | MECH-045 (dormant) |

SD-057's doc cleanly distinguishes itself from the ghost bank ("inactive-anchor
store" vs "concurrent per-object-type store") -- good. But none of the three cite
ARC-006/MECH-045, the supposed canonical object-file layer. **Risk:** a fourth
per-item store gets built for permanence or tools without anyone noticing three
already exist with overlapping intent. The cross-references added alongside this
doc (see §6) make the three stores acknowledge each other to prevent exactly that.

### "Object" currently means at least three things

1. a **type / category** -- SD-049 tag; `z_resource` is location-invariant, so it
   is a *type*;
2. a **spatial anchor** -- the hippocampal anchor in the ghost bank;
3. a **feature-bundle token entity** -- MECH-278 / ARC-006.

Biology separates these: object-files are **token-instance** ("*this* apple,
tracked through occlusion") distinct from category ("apples"). **REE's live work
is at the TYPE level.** True object permanence -- and tools, self-as-object, and
others-as-object -- need **token-instance** tracking. This is a genuine
representational gap, not just a missing flag. Any unified object primitive must
decide whether the unit is a **type, a token, or an anchor** -- and that
type-vs-token-vs-anchor choice is the **first design fork** for any future
substrate step.

> **OBJ-1 RESOLUTION (2026-06-14, IGW plan-reconcile `object_representation_v4:OBJ-1`; user decision).**
> The fork is resolved **not** by electing one of {type, token, anchor} as the
> primitive that subsumes the other two, but by making the **coordination itself
> the primitive**: an object is a **binding that holds three distinct coordinate
> facets** -- a TYPE/category readout (SD-015/SD-049, `z_resource`), a SPATIAL
> ANCHOR (SD-039/MECH-292/293 ghost bank), and a TOKEN-INSTANCE individuation
> (ARC-006/MECH-044/MECH-045 object-file) -- none of which reduces to another. The
> object-file is the structure that keeps the facets **coregistered**; the
> primitive is the coregistration, not any one facet crowned. This fits the binding
> literature already on file: a **slot** addresses the token (which object;
> Pylyshyn FINST / Locatello slot-attention), **synchrony** binds the features that
> cohere now (Fries / Singer / von der Malsburg), and von der Malsburg's
> **superposition catastrophe** is exactly *why* the facets must be kept
> distinct-but-bound rather than collapsed. The V3 diagnostics that bottomed out on
> a missing bound representation (V3-EXQ-641a coherence-non-reducibility =
> "bound-representation prerequisite absent"; `z_world` dim=32 discriminative
> ceiling) are the experimental pull toward this same coregistration substrate.
> **Consequence:** OBJ-2 is no longer "pick token over type" but **"build the
> coregistration structure that binds the three facets"**; `z_object` becomes the
> *type-readout of* a coordinate object-file rather than a free-standing type tag;
> SD-039's anchor store is now wired into ARC-080 `depends_on` as the anchor facet.
> The remaining open sub-fork -- token-vs-type **individuation strength** within the
> bound token facet -- is deferred to the first OBJ-2 build step. Design commitment
> only: `implementation_phase: v4` / `v3_pending`, off the V3-closure critical path;
> no substrate built, no V3 behaviour changed.

### Where a unified object representation would live

A coherent layer generalises `z_object`/`z_resource` out of the resource silo
into an **object-file / binding layer** that:

- keys on an **entity token** (not only a resource type tag),
- stores an **identity embedding** (generalised `z_object`) + a
  **persistence/state buffer** (the out-of-view continuation), and
- is **consumed by**: (i) the incentive bank (SD-057, drive/goal axis),
  (ii) hippocampal anchors + planning (MECH-262 / SD-039), (iii) the self-model
  slot (z_self, V4), (iv) the social other-slots (z_self_j, V4), and (v) the
  affordance/action map (SD-016, tools).

ARC-006/MECH-044/MECH-045 is the natural home -- but it needs reactivation, a
biology grounding (the 2026-06-04 L1/L2 pulls), and explicit wiring to the live
`z_resource` lineage and to MECH-278's object definition. **This is a V4 /
late-V3 substrate task, not part of this umbrella.**

---

## 4. The four pillars (specialisations of the one primitive)

```
ARC-080  object identity = cross-cutting representational primitive
  ├─ representational substrate ........ ARC-006 / MECH-044 / MECH-045 (reactivate + ground)
  ├─ object definition ................. MECH-278 (causal feature bundle under intervention)
  ├─ developmental ordering ............ ARC-059 (self -> objects -> others)
  ├─ live identity latent .............. SD-015 -> SD-049 -> SD-057 (generalise z_object)
  │
  ├─ PILLAR 1  permanence .............. NEW future child (token persistence through occlusion);
  │                                      reactivate MECH-045; generalise the SD-039/MECH-292/293
  │                                      ghost-goal bank from goal-snapshot to object-token. [V3-straddle/V4]
  │                                      -- UNREGISTERED (future child; not minted by this umbrella)
  ├─ PILLAR 2  self-as-object .......... ARC-081 -- z_self as a privileged object-file slot
  │                                      (DR-10..DR-14, MECH-214/MECH-215, INV-064). [begins V3, cutover V4]
  ├─ PILLAR 3  tools / affordances ..... ARC-082 -- object->action binding; ground SD-016
  │                                      cue_action_proj (UNGROUNDED -- V3-EXQ-449 0.0 grad; EXP-0155). [V3 substrate / V4 grounding]
  └─ PILLAR 4  others-as-object ........ ARC-083 -- other-agent object-file slots (z_self_j, z_harm_a_j);
                                         ARC-010 / ARC-047. [V4]
```

> **Registered children (2026-06-04):** Pillars 2/3/4 are now registered as thin
> `architectural_commitment` children of ARC-080 -- **ARC-081** (self-as-object),
> **ARC-082** (tools/affordances), **ARC-083** (others-as-object) -- each a
> coherence-map child that adds *only* the "X-as-object-file-slot" framing + the
> V3-begin/V4-cutover boundary (see §5.1), wiring `depends_on` to the pillar's
> existing claims rather than restating their mechanism. **Pillar 1 (permanence)
> remains an unregistered future child** -- the umbrella documents it but does not
> mint a claim for it (the token-instance permanence substrate is the first real
> V4/late-V3 step, not a doc-spine entry).

### Pillar 1 -- object permanence

| | |
|---|---|
| **Existing fragment** | SD-039 dual-trace `AnchorGoalPayload`; MECH-292 ranked ghost-goal bank; MECH-293 ghost-goal probe search (Bouton dual-trace). LIVE. |
| **What it actually delivers** | Per-anchor goal-VALUE snapshots that persist when not perceived -- a *motivational*-persistence primitive, NOT object permanence. Keyed by spatial anchor; payload is `z_goal_snapshot` + wanting; queries by *wanting rank*, not "where is object X now." |
| **What's missing** | Token-instance tracking through occlusion. |
| **Insertion point** | NEW future child (token persistence through occlusion): reactivate MECH-045; generalise the ghost-goal bank from goal-snapshot to object-token. Documented here as a future child; NOT registered as a separate claim by this umbrella. [V3-straddle / V4] |

### Pillar 2 -- self as a special object

| | |
|---|---|
| **Existing fragment** | z_self (SD-005 self/world split; SD-030 E2 self-forward-model, V4-deferred); DR-10..DR-14 self-model integration audit; MECH-214 (goal must be E1-representable); MECH-215 (self-model prerequisite for agentive prediction); INV-064 (maturational-sequence necessity). |
| **What it actually delivers** | z_self is a body-state latent (proprioceptive/interoceptive; single MLP + EMA) -- **not a self-OBJECT slot.** |
| **What's missing** | DR-10 (not in E3 scoring), DR-11 (no z_goal_self domain), DR-12 (E2 PE not modulating E3 confidence), DR-13 (no temporal depth/recurrence), DR-14 (env doesn't dissociate proxy from hedonic). All V4. |
| **Registered child** | **ARC-081** (self-as-object-file-slot). `depends_on` ARC-080 + SD-005/SD-003/MECH-277/ARC-059/ARC-074 (V3 beginning) + MECH-214/MECH-215/INV-064/SD-030 (V4 cutover). |
| **Boundary** | **Begins V3, cutover V4.** The self *begins* in V3 -- z_self body latent (SD-005), self-attribution (SD-003), action-space discovery / self-as-object stage 1 (MECH-277, ARC-059 stage 1), reward-free babbling Phase 0 (ARC-074). The object-file **cutover** -- z_self promoted to a privileged self-OBJECT slot -- is V4 (DR-10..DR-14 audit, MECH-214/215, INV-064, SD-030). See §5.1. |
| **Insertion point** | z_self as a privileged object-file slot, gated by the DR-10..14 self-model integration audit + MECH-163 multi-step planning. [V4 cutover; V3 beginning already live] |

### Pillar 3 -- objects as tools / affordances

| | |
|---|---|
| **Existing fragment** | SD-016 `cue_action_proj` (affordance bias for E2), `cue_terrain_proj`, `world_query_proj`. |
| **What it actually delivers** | `cue_terrain_proj` works (E3 precision). `cue_action_proj` is inert: V3-EXQ-449 found 0.0 gradient (non-differentiable CEM blocks the path; signal vanishes before E3.select). EXP-0155 queued to instrument. |
| **What's missing** | A grounded object->action pathway. |
| **Registered child** | **ARC-082** (tools-object-action-binding). `depends_on` ARC-080 + SD-016 + SD-055 (differentiable-CEM grounding track; SD-055 was re-registered 2026-06-04 after a 2026-05-15 auto-sync conflict had silently dropped its `claims.yaml` entry). |
| **Boundary** | **V3 substrate exists but ungrounded; grounding straddles V3; full binding V4.** SD-016 `cue_action_proj` is in V3 code but inert (V3-EXQ-449 0.0 gradient). Grounding it (EXP-0155 + SD-055 differentiable-CEM) is its own track and can begin in the V3 era; folding afforded actions into a token-keyed object-file slot is V4. See §5.1. |
| **Insertion point** | object->action binding; ground SD-016 `cue_action_proj` (its own existing track via EXP-0155 / differentiable-CEM SD-055); fold into the object->action axis once the object-file exists. [V3 substrate / V4 grounding] |

### Pillar 4 -- others as special objects

| | |
|---|---|
| **Existing fragment** | ARC-010 mirror modelling (`stable`); ARC-047 SocialGridWorld scent harness (`candidate`, v4); MECH-031/032/036/041 (derived social tags, empathy coupling, other-harm veto, affective broadcast); MECH-051/052/127/159/190. |
| **What it actually delivers** | Design-only. |
| **What's missing** | Each other-agent j needs its own `z_self_j`, `z_harm_a_j`, drive, commitment chain -- an "other-as-object" slot. |
| **Registered child** | **ARC-083** (others-as-object-file-slot). `depends_on` ARC-080 + ARC-010/ARC-047 + MECH-163 (gate) + ARC-081 (self-stability prereq) + SD-039 (partial-permanence prereq). |
| **Boundary** | **V4.** Design-only today; gated on MECH-163 multi-step planning. Per DEV-NEED-021, prerequisites are object-permanence (Pillar 1, partial via SD-039) + self-stability (Pillar 2 / ARC-081). See §5.1. |
| **Insertion point** | other-agent object-file slots; ARC-010 / ARC-047. Gated on MECH-163 (multi-step hippocampal planning) and on Pillars 1+2 (per DEV-NEED-021: otherness inference REQUIRES object persistence + self-stability). [V4] |

### The ordering is load-bearing

`developmental_needs_register.md` already encodes the thread, but as *ordering*,
not representation:

- **DEV-NEED-033** ↔ ARC-059: the self->objects->others ordering (the user's
  pillars 2 -> (implicit object) -> 4).
- **DEV-NEED-021:** "otherness inference *after* self-stability" lists **object
  persistence** as a prerequisite for other-modelling. So the register already
  treats object permanence as load-bearing for the social pillar -- but the
  permanence substrate it presupposes (a true object-file persistence buffer)
  does not exist; only the goal-snapshot ghost bank does.

```
self-as-object (MECH-277) --> objects-as-patterns (MECH-278) --> others-as-object (ARC-010, V4)   [ARC-059]

object-file / persistence primitive (ARC-006 reactivated, generalised z_object)
      ├─ temporal axis  -> PILLAR 1 permanence
      ├─ action axis    -> PILLAR 3 tools / affordances (SD-016)
      └─ special slots  -> PILLAR 2 self + PILLAR 4 other   [both V4]

DEV-NEED-021: otherness REQUIRES object persistence + self-stability
  => PILLAR 1 + PILLAR 2 are prerequisites for PILLAR 4
```

---

## 5. V3 / V4 sequencing -- what must NOT enter V3 closure

| Capability | V3/V4 | State | On V3-closure critical path? |
|---|---|---|---|
| Object-identity IN GOALS (SD-057) | **V3** | LANDED (resource-bound) | The L9 retest is -- but it is owned by `scaffolded_sd054_onboarding` and untouched here |
| Permanence -- motivational (ghost-goal bank) | **V3** | LANDED (goal-snapshot, partial) | No |
| Permanence -- object token through occlusion | **V3-straddle / V4** | NOT built | **No -- must NOT enter V3 closure** |
| Object-schema formation (MECH-278) | **V4** | BYPASSED in V3 (engineered z_world) | No |
| Tools / affordances (SD-016, ARC-082) | **V3 substrate / V4-grounding** | LIVE but UNGROUNDED (EXP-0155 gate) | No -- separate existing track |
| Self-as-object (z_self, DR-10..14, ARC-081) | **begins V3, cutover V4** | V3 beginning live (z_self/SD-005, SD-003, MECH-277, ARC-074); V4 self-OBJECT slot latent only | No |
| Others-as-object (ARC-010/047, ARC-083) | **V4** | design only | No |

### 5.1 Per-pillar V3-begin / V4-cutover boundary

The four pillars are **not** cleanly V3-vs-V4. Each has a V3 BEGINNING and a V4
CUTOVER at which it becomes a **token-keyed object-file slot** under ARC-080. This
is the central distinction the registered children (ARC-081/082/083) encode:

| Pillar | Registered child | V3 BEGINNING (already live / in progress) | V4 CUTOVER (-> object-file slot) | On V3-closure critical path? |
|---|---|---|---|---|
| **1 -- permanence** | *(unregistered future child)* | Motivational persistence: SD-039 dual-trace ghost-goal bank, MECH-292/293 (goal-VALUE snapshots that persist when unperceived) | Token-instance persistence through occlusion: reactivate MECH-045; generalise the ghost bank from goal-snapshot to object-token | No -- must NOT enter V3 closure |
| **2 -- self-as-object** | **ARC-081** | z_self self/world split (SD-005); self-attribution (SD-003); action-space discovery / self-as-object stage 1 (MECH-277, ARC-059 stage 1); reward-free babbling Phase 0 (ARC-074). *"The idea of a self that acts" has begun.* | z_self promoted to a privileged self-OBJECT slot: DR-10..DR-14 self-model integration audit, MECH-214 (goal E1-representability), MECH-215 (self-model prerequisite), INV-064 (maturational sequence), SD-030 (E2 self-forward-model). Gated on MECH-163. | No |
| **3 -- tools/affordances** | **ARC-082** | SD-016 `cue_action_proj` exists in V3 code but is UNGROUNDED (V3-EXQ-449 0.0 gradient; non-differentiable CEM severs the path). *Grounding straddles V3* on its own track: EXP-0155 instrumentation + SD-055 differentiable-CEM. | Full object->action binding: afforded actions keyed to a token-instance object-file slot, once the generalised object-file exists. | No -- separate existing track |
| **4 -- others-as-object** | **ARC-083** | *(none -- design-only)*; mirror-modelling claim ARC-010 is `stable` but unimplemented as an other-slot. | Per other-agent j: own `z_self_j`, `z_harm_a_j`, drive, commitment chain (ARC-010 / ARC-047). Gated on MECH-163 + (per DEV-NEED-021) on Pillar 1 permanence + Pillar 2 self-stability. | No |

**The boundary in one line:** *the beginning of each pillar is V3 (or partial-V3);
the object-file-slot cutover is V4.* Self is the clearest case -- it is NOT flatly
V4: the self **begins in V3**, and only the privileged-object-file-slot cutover is
V4. Registering ARC-081/082/083 changes no V3 behaviour and pulls nothing into V3
closure; the cutovers are V4 / late-V3 substrate enrichment.

**Proposed ordering (post-V3, nothing pulled forward):**

1. **Spine + grounding (doc-only, V3-safe):** this umbrella + the L1/L2 lit pulls
   (in progress 2026-06-04). Zero code. The only piece that can happen during the
   V3 era -- it touches no substrate and no critical-path file.
2. **Generalise `z_object`** from type-tag to token-keyed object-file (the first
   real substrate step) -- **V4 / late-V3 substrate enrichment.**
3. **PILLAR 1 permanence** (token persistence through occlusion) on top of the
   generalised object-file; reuses/extends the ghost-goal bank.
4. **PILLAR 3 tools** -- ground SD-016 (its own EXP-0155 / SD-055 track); fold
   into the object->action axis once the object-file exists.
5. **PILLAR 2 self-as-object** -- V4, gated by the DR-10..14 audit + MECH-163.
6. **PILLAR 4 others-as-object** -- V4, gated on MECH-163 and on Pillars 1+2 per
   DEV-NEED-021.

**Explicitly excluded from V3 closure:** no generalisation of
`z_object`/`IncentiveTokenBank` beyond resource types as part of GAP-7; no new
permanence / object-file substrate; no SD-016 grounding work; no self/other-object
work bundled into the L9 wanting≠liking retest. SD-057 stays resource-bound for
V3.

---

## 6. Biology grounding (biology-before-formal-definitions)

Per the project rule, biology lit pulls are commissioned **before** any new
object-file / permanence / self / other claim. ARC-006/MECH-044/MECH-045 had **no
biology lit-pull at all** at the time this umbrella was registered -- that gap is
being closed concurrently:

| # | Pull | Anchors | Grounds | Status |
|---|---|---|---|---|
| L1 | Object files & feature binding | Kahneman/Treisman/Gibbs 1992 (object files); Treisman & Gelade 1980 (FIT) | ARC-006, MECH-044, MECH-045; generalised `z_object` | **ACTIVE 2026-06-04** (`litpull-object-files-feature-binding`) |
| L2 | Object permanence (token-instance, occlusion) | Piaget A-not-B; Baillargeon violation-of-expectation; Spelke core-knowledge; Kellman & Spelke 1983 | PILLAR 1; token-vs-type gap | **ACTIVE 2026-06-04** (`litpull-object-permanence`) |
| L3 | Affordances / objects-as-tools | Gibson 1979; Rizzolatti/Murata canonical neurons; Khetarpal et al. (affordances in RL) | PILLAR 3; SD-016 grounding | pending (when Pillar 3 scheduled) |
| L4 | Self-as-object / minimal self | Gallagher minimal vs narrative self; de Vignemont body schema; Botvinick & Cohen rubber-hand; Blanke bodily self | PILLAR 2 / **ARC-081**; z_self-as-object | pending (V4) -- RECOMMENDED next |
| L5 | Theory of mind / others-as-agents | Woodward 1998 (infant goal attribution); Gergely & Csibra (teleological stance / natural pedagogy); Baron-Cohen ToMM; Premack & Woodruff | PILLAR 4 / **ARC-083**; ARC-010 / ARC-047 | pending (V4) -- RECOMMENDED next |

> **Recommendation (NOT auto-run -- for user approval).** With Pillars 2 and 4 now
> registered (ARC-081, ARC-083), the next two biology groundings are **L4
> (self-as-object / body-as-object: Gallagher minimal self, Botvinick & Cohen
> rubber-hand, de Vignemont body schema)** for ARC-081 and **L5 (theory of mind:
> Woodward 1998 infant goal attribution, Gergely & Csibra teleological stance /
> natural pedagogy, Baron-Cohen ToMM)** for ARC-083. These are recommendations to
> commission when Pillars 2/4 are scheduled, per `biology_before_formal_definitions`
> -- they are deliberately **not** run as part of this doc-only registration.

**Until L1 lands, treat ARC-006's biology grounding as IN PROGRESS** -- the
umbrella is registered now (doc-spine is V3-safe and the fragments were already
drifting), with this dependency flagged in the ARC-080 claim's
`biology_grounding_note`.

---

## 7. Cross-references added alongside this doc

To stop a fourth per-item store being built blind, the three existing stores now
acknowledge each other and this umbrella:

- [`entities_and_binding.md`](entities_and_binding.md) (ARC-006 / MECH-045) --
  points at the live SD-057 `IncentiveTokenBank`, the SD-039 ghost-goal bank, and
  this umbrella.
- [`sd_057_object_bound_incentive_salience.md`](sd_057_object_bound_incentive_salience.md)
  -- noted as one of three per-item stores under ARC-080; links to ARC-006.
- [`sd_039_anchor_goal_payload.md`](sd_039_anchor_goal_payload.md) -- same.
- [`developmental_needs_register.md`](developmental_needs_register.md) --
  cross-ref near DEV-NEED-021 / DEV-NEED-033.

---

## Related Claims (IDs)

- ARC-080 (this umbrella)
- ARC-081 (PILLAR 2 child -- self-as-object-file-slot), ARC-082 (PILLAR 3 child -- tools/object-action-binding), ARC-083 (PILLAR 4 child -- others-as-object-file-slot)
- ARC-006, MECH-044, MECH-045, MECH-050 (representational substrate)
- MECH-278, MECH-276, MECH-277, ARC-059 (object definition + developmental ordering)
- SD-015, SD-049, SD-057, MECH-262, MECH-344..348 (live identity latent)
- SD-039, MECH-292, MECH-293 (Pillar 1 partial -- ghost-goal bank)
- SD-016 (Pillar 3 -- tools/affordances, ungrounded)
- z_self / SD-005 / SD-030 / DR-10..DR-14 / MECH-214 / MECH-215 / INV-064 (Pillar 2 -- self, V4)
- ARC-010, ARC-047, MECH-031/032/036/041 (Pillar 4 -- others, V4)

## References / Source

- [`evidence/planning/object_representation_thread_2026-06-04.md`](../../evidence/planning/object_representation_thread_2026-06-04.md) -- the full synthesis brief and the Option-A proposal this doc instantiates.
</content>
</invoke>
