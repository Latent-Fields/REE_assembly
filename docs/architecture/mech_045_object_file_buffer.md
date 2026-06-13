---
title: MECH-045 -- Token-Instance Object-File / Entity-Persistence Buffer (Substrate Design Memo)
parent: "Attention, Binding & Objects"
grandparent: Architecture
nav_order: 5
---

# MECH-045 -- Token-Instance Object-File / Entity-Persistence Buffer (Substrate Design Memo)

**Claim Type:** mechanism_hypothesis (substrate design)
**Claims served:** MECH-045 (object-file-like persistence), ARC-006 (entities are sparse, persistent, bindable structures)
**Status of substrate:** IMPLEMENTED 2026-06-09 (v1, behind no-op-default `use_object_file_buffer`; `ree-v3/ree_core/entities/object_file_buffer.py` + `REEAgent.update_object_file_buffer`; ree-v3 commit b00c83d). Was DORMANT (design-only) when this memo was written. Validation experiment **V3-EXQ-658** queued (the EVB-0293/EXP-0117 re-queue); `substrate_queue.ready` stays FALSE until it clears the Section 6 gates at full scale. MECH-045/ARC-006 NOT yet promoted (governance applies after the run).
**Scope band:** V4 / late-V3 substrate enrichment. **OFF the GAP-7 closure critical path.**
**Registered:** 2026-06-09
**Author context:** Unblock memo for the `/queue-experiment` Step-2.5 readiness gate (2026-06-09) that marked proposal **EVB-0293 / EXP-0117** `status=blocked_substrate`. This memo + the biology lit-pull are deliverable 1; the sibling `/implement-substrate` chip (gated on this memo) writes the `ree_core` code.

> **Guardrail (read first).** This is a **design memo + literature** only. It edits
> NO `claims.yaml`, queues NO experiment, writes NO `ree_core` code, and makes NO
> governance promotion/demotion decision. It frames the substrate as **V4 /
> late-V3** per [ARC-080](arc_080_object_representation_primitive.md) Pillar 1, and
> nothing here is to be pulled into V3 closure (`goal_pipeline:GAP-7`,
> `scaffolded_sd054_onboarding`, SD-057 resource-bound behaviour). The `ree_core`
> module and the experiment described below are **proposals for a future chip**, not
> landed artefacts.

---

## 0. The gap in one paragraph

MECH-045 requires a buffer that **binds features across time AND motion**, keyed by an
entity **TOKEN INSTANCE** -- an identity that survives the entity moving to a new cell --
**without symbolic/type labels**, **attention-gated**, with **precision-weighted
continuity constraints**. REE-v3 has two *live* per-item stores that look adjacent but
test different claims, and one *dormant* design layer that is the real home:

| Store | Key | What it is | Why it is NOT MECH-045 |
|---|---|---|---|
| SD-057 `IncentiveTokenBank` (`ree-v3/ree_core/goal.py:163`) | resource **TYPE tag** k (1..n, SD-049) | per-type incentive value + detached `z_resource` clone | TYPE-keyed: "all apples are the same." `z_object[k]` is a *category* identity, location-invariant, not a token followed through motion. |
| SD-039 / MECH-292 ghost-goal bank (`ree-v3/ree_core/hippocampal/anchor_set.py`) | spatial **ANCHOR** | per-anchor `z_goal_snapshot` + wanting/arousal, dual-trace | ANCHOR-keyed: persistence of a *motivational value at a place*. No cross-motion re-identification; queries by wanting rank, not "where is object X now." |
| ARC-006 / MECH-045 object-file buffer (this memo) | entity **TOKEN** | features bound across time+motion, label-free, attention-gated | **Does not exist in code.** This is the missing primitive. |

This is the **type-vs-token-vs-anchor fork** ARC-080 calls "the first design fork."
A persistence-vs-ablation probe of MECH-045 against the two live stores would be
**vacuous** -- neither can re-identify a moved entity, so neither can fail the test in
the way that would falsify or confirm MECH-045. Hence `blocked_substrate`. This memo
resolves the fork (Section 3) and specifies the token store that closes it (Section 4).

---

## 1. Biology grounding (biology-before-formal-definitions)

Per the project rule, the biology pull precedes the formal substrate. This memo's pull
lives at `evidence/literature/targeted_review_mech_045_object_file/` (5 entries,
2026-06-09) and complements the two ARC-080 pulls of 2026-06-04
(`targeted_review_object_files_feature_binding` = L1, `targeted_review_object_permanence`
= L2). Together they put MECH-045's `literature_confidence` at 0.866 over 15 entries.

The five new entries map onto the four properties MECH-045 names:

| Property MECH-045 requires | Biological / computational grounding | Source |
|---|---|---|
| **Per-object buffer, features bound across time AND motion** | The **object-file** construct itself. Object-specific preview benefit; linkage carried by shared *relative position in a moving frame*, not by features -- binding follows the object through motion. | Kahneman, Treisman & Gibbs 1992 (Cognitive Psychology) -- *supports*, 0.82 |
| **Token KEY, label-free (no type label)** | **Visual indexes / FINSTs**: a preconceptual pointer that individuates and tracks ~4-5 objects *without encoding their identities*. The cleanest statement of "no symbolic label." MOT is the behavioural test of tracking-through-motion. | Pylyshyn 2001 (Cognition) -- *supports*, 0.78 |
| **Persistence across time (outlives perceptual contact)** | **Object-trace cells** in lateral entorhinal cortex (LEC, the "what/content" stream): fire at the location where an object *used to be* after removal -- persistence-through-absence at the single-cell level. | Tsao, Moser & Moser 2013 (Current Biology) -- *supports*, 0.72 |
| **Objects as a first-class coded entity (ARC-006)** | **Object-vector cells** in medial entorhinal cortex (MEC, "where"): dedicated machinery coding objects as reference points -- but *object-generically* (the where/anchor axis), a cautionary case for the fork. | Hoydal, Moser & Moser 2019 (Nature) -- *mixed*, 0.66 |
| **The concrete update rule (KEY mechanism, computational)** | **Data association** (DeepSORT): predict -> motion-gate -> appearance-match -> birth/death assigns persistent, label-free track ids across occlusion; combine spatiotemporal continuity with a feature embedding. | Wojke, Bewley & Paulus 2017 (IEEE ICIP) -- *supports*, 0.70 |

**Two load-bearing biological facts for the design:**

1. **What and where are separable channels.** LEC object-trace cells (identity/content,
   persistence) and MEC object-vector cells (spatial relation) are *distinct cell
   populations in distinct regions*. This licenses a token buffer that **holds features**
   (the what) and **consumes an anchor channel** (the where) rather than conflating them
   -- and it tells us the SD-039 anchor bank is the *where* half of a system whose *what*
   half is missing.

2. **Identity is carried by continuity, not by features.** The object-file benefit, FINST
   tracking, and DeepSORT's motion gate all key on *spatiotemporal continuity*. This is
   the property the TYPE-keyed `IncentiveTokenBank` (which is *defined* to be
   location-invariant) structurally cannot have. The token KEY must be a continuity
   association, not a feature classifier.

**The honest adverse finding (Hoydal 2019, *mixed*).** The brain's best-characterised
object cell type (object-vector) is *object-generic* -- it codes "an object is here
relative to me," not "this is object #7 again." It is evidence for ARC-006 (objects are
coded) but a *warning* for MECH-045: the obvious neural template is the wrong axis. The
token-instance property is genuinely harder than the object-vector literature delivers,
which is consistent with REE finding it a real (not incidental) gap.

---

## 2. What MECH-045 must do (functional contract)

From the claim text + ARC-006 design constraints, the buffer must:

- **C1 -- Token KEY.** Assign and maintain a per-entity token id by spatiotemporal-
  continuity data-association over `z_world` features, with **no type label**. The token
  survives the entity moving to a new cell (cross-motion re-identification).
- **C2 -- Per-token feature buffer.** Hold a running, bound feature representation per
  token (the "file"): an EMA/precision-weighted estimate of the entity's `z_world`-local
  features, updated on each re-observation.
- **C3 -- Persistence through absence.** Keep a token (and its features) alive for a
  bounded number of ticks when the entity is occluded / out of view, then evict
  (track death) -- the object-trace-cell + DeepSORT track-management property.
- **C4 -- Attention-gating.** Binding/update is gated by precision/attention state, not a
  feedforward merge (ARC-006 explicit constraint). Tokens compete for a bounded buffer
  (the FINST ~4-5 capacity analogue); attention selects which entities get a file.
- **C5 -- Precision-weighted continuity.** The continuity (association) decision and the
  feature update are weighted by precision -- high-precision observations bind more
  strongly; low-precision (uncertain) observations update less, and a low-confidence
  association can *defer* rather than force a (mis)match.

**Non-goals (explicitly out of scope for this substrate):** value/incentive (that is
SD-057's job, downstream), goal-snapshot motivational persistence (SD-039's job),
object *type/schema* formation (MECH-278, bypassed in V3), self/other object slots
(ARC-081/083, V4). MECH-045 is the **representational substrate** the others consume.

---

## 3. Resolving the type-vs-token-vs-anchor fork

ARC-080 states any unified object primitive must decide whether the unit is a **type, a
token, or an anchor**, and that this is the first fork. This memo resolves it as follows:

**The three are not competitors; they are three projections of one entity, and REE
already has two of them. The token buffer is the missing third, and it is the SPINE the
other two should hang off.**

```
                    ENTITY (this fish, here, now, an apple)
                        |
   ┌────────────────────┼─────────────────────┐
   │ TYPE projection     │ TOKEN projection      │ ANCHOR projection
   │ "what kind"         │ "which one"           │ "where (remembered)"
   │ SD-057              │ MECH-045 (THIS MEMO)   │ SD-039
   │ IncentiveTokenBank  │ ObjectFileBuffer       │ ghost-goal bank
   │ key = resource tag  │ key = continuity token │ key = spatial anchor
   │ location-INVARIANT  │ motion-TRACKED         │ place-BOUND
   │ LIVE                │ DORMANT (build this)   │ LIVE
   └────────────────────┴─────────────────────┘
```

**Why token is the spine, not a fourth peer:** the type tag answers "what kind is the
thing I am tracking" and the anchor answers "where did the thing I was tracking go" --
*both presuppose a tracked thing.* The token IS the tracked thing. So the resolution is:

- **Build the token buffer as the primary entity index.** Its key is the only one with
  cross-motion identity, so it is the natural carrier of "this entity" across the system.
- **Wire the two live stores to consume the token, not replace it** (the "missing wiring"
  ARC-080 flags). Concretely (proposed, for the `/implement-substrate` chip):
  - **IncentiveTokenBank (TYPE -> TOKEN):** today `bank.update(k, benefit, z_resource)`
    keys incentive on type tag `k`. The token buffer lets a *token* carry an optional
    `type_hint` (the SD-049 tag observed when the token was last in a resource cell). The
    incentive bank can then be queried per-token ("how much do I want *this* object")
    while still aggregating to type for revaluation. **Backward-compatible:** when the
    token buffer is OFF, the bank behaves bit-identically (type-only).
  - **Ghost-goal bank (ANCHOR -> TOKEN):** today `AnchorGoalPayload` snapshots `z_goal` at
    a spatial anchor. The token buffer supplies an optional `token_id` field on the
    payload, so an inactive anchor can record *which token* it last held -- upgrading the
    bank from "value persisted at a place" toward "object X was last seen here" (ARC-080
    Pillar 1's stated generalisation). **This is wiring, not a rewrite:** the anchor bank
    keeps its anchor key; it gains a token cross-reference.

**What this resolution explicitly does NOT do:** it does not merge the three stores into
one object, does not change SD-057's resource-bound V3 behaviour, and does not put any of
the wiring on the V3 critical path. The wiring fields are **proposed optional additions**
the implement chip would add behind no-op-default flags; v1 of the token buffer can land
**standalone** (no wiring) and be validated in isolation (Section 5), exactly as SD-039's
substrate landed before its population layer.

---

## 4. Proposed ree-v3 module

**Proposed path:** `ree-v3/ree_core/entities/object_file_buffer.py` (new package
`ree_core/entities/`).

**Shape:** a stateful, **NON-TRAINABLE** module (like `IncentiveTokenBank`): pure
dict/tensor state + an association rule. No `nn.Module`, no trainable parameters, so **no
phased training** for v1 -- it consumes `z_world` (already trained) and produces token
assignments. (A learned association *metric* is the upgrade path, not v1 -- mirroring how
SD-057's learned-affordance-embedding is explicitly deferred.)

### 4.1 State

```
ObjectFileBuffer:
  _tokens: dict[int, ObjectFile]          # token_id -> file
  _next_id: int
  _tick: int

ObjectFile (dataclass):
  token_id: int
  z_features: Tensor [world_dim]          # C2 per-token bound feature buffer (EMA)
  last_pos: Tensor [2]                    # last observed (row,col) -- continuity gate only
  precision: float                        # C5 running confidence of this track
  last_seen_tick: int                     # C3 persistence / eviction clock
  hits: int                               # n re-observations (track maturity)
  type_hint: Optional[int] = None         # SD-049 tag if last seen in a resource cell (wiring)
```

### 4.2 The update loop (one call per waking tick)

`update(observations, attention, precision) -> dict[entity_slot -> token_id]`, where
`observations` is the set of currently-perceived candidate entities (each a `z_world`-
local feature vector + grid position; see the detector dependency note below).

```
1. PREDICT       For each live token, predicted_pos = last_pos (v1 zero-order;
                 a velocity term is the v2 upgrade -- DeepSORT's Kalman step).
2. GATE (C1,C5)  Cost(token, obs) = w_motion * d_pos(predicted_pos, obs.pos)
                                   + w_feat   * d_cos(token.z_features, obs.z)
                 Gate out pairs whose motion distance exceeds a continuity radius
                 (Mahalanobis-style; here a fixed cell radius) OR whose precision-
                 weighted feature distance exceeds a threshold. The gate is what
                 makes identity continuity-based, not nearest-cell-based.
3. MATCH (C4)    Solve the gated assignment (greedy by ascending cost for v1;
                 Hungarian is the v2 upgrade). Attention caps the number of
                 simultaneously-maintained tokens to `max_tokens` (~the FINST 4-5):
                 when over capacity, lowest-precision / least-recently-seen tokens
                 lose their slot.
4. UPDATE (C2,C5) For each matched (token, obs):
                   alpha = base_alpha * precision_of(obs)            # precision-weighted
                   token.z_features <- (1-alpha)*z_features + alpha*obs.z
                   token.precision  <- ema(token.precision, match_confidence)
                   token.last_pos = obs.pos; token.last_seen_tick = tick; token.hits += 1
                   token.type_hint = obs.resource_tag if obs in resource cell else hint
5. BIRTH         Unmatched observations with sufficient attention/salience open a NEW
                 token (assign _next_id). Low-salience unmatched obs are ignored (C4).
6. DEATH (C3)    Tokens unseen for > persist_ttl ticks are evicted. Until then they
                 persist (occlusion tolerance) and remain queryable -- the object-trace-
                 cell / persistence-through-absence property.
```

**MECH-094 guardrail (mandatory).** The buffer updates **only on the waking stream**.
During simulation / replay / sleep it must be a no-op (no token births, no feature
writes) -- a moved-imagined-object must not rewrite the waking object-file. This mirrors
SD-039's `simulation_mode=True` skip and SD-057's waking-only bank.

### 4.3 Config (all no-op defaults; bit-identical OFF)

| Param | Default | Purpose |
|---|---|---|
| `use_object_file_buffer` | `False` | master switch (bit-identical OFF) |
| `obf_max_tokens` | `5` | attention capacity cap (FINST analogue, C4) |
| `obf_continuity_radius` | `2.0` | motion gate radius in cells (C1) |
| `obf_w_motion` / `obf_w_feat` | `1.0` / `1.0` | association cost weights |
| `obf_feature_alpha` | `0.3` | base feature EMA rate (scaled by precision, C2/C5) |
| `obf_persist_ttl` | `8` | ticks a token survives unseen before eviction (C3) |
| `obf_min_birth_salience` | `0.0` | attention floor to open a new token (C4) |
| `obf_use_precision_weighting` | `True` | C5 on/off |

### 4.4 The detector dependency (named, not hidden)

DeepSORT assumes an external detector proposing candidate entities each frame; REE has
none. **v1 resolves this by using the substrate REE already has:** the SD-049 per-type
resource-field views (`resource_field_view_<name>`) and the grid's discrete object/hazard
cells supply candidate entity positions + their local `z_world` slice. This restricts v1
to entities the env already exposes as cells (resources, hazards, the agent) -- which is
exactly the set the persistence experiment needs. A learned figure-ground proposer is a
later, separate concern (it overlaps MECH-278 object-schema formation, which is V4). **The
memo states this limit rather than assuming it away.**

---

## 5. Feasibility against the known V3 discriminative ceilings

Two findings in the object-representation thread bear directly on whether this buffer can
work at the current substrate.

### 5.1 The z_world dim=32 discriminative ceiling

**Finding (2026-06-06 cluster autopsy, encoded in `ree-v3/ree_core/utils/config.py:156`):**
"the 2026-06-06 cluster autopsy established z_world at dim=32 lacks discriminative
granularity"; `E2WorldForward` *hard-asserts* `world_dim >= 128`. Default `world_dim = 32`.

**Why this bites THIS buffer specifically.** The token KEY's feature term (`d_cos` in the
gate, step 2) is a re-identification metric over `z_world`. This is exactly DeepSORT's
appearance term -- and the Wojke 2017 entry's headline failure signature is that *if the
appearance descriptor is not discriminative enough, association degenerates to
motion-only*, which is the **location-collapse vacuity mode**: the buffer would track
"whatever was in the nearest cell last tick" and pass a naive persistence test **without
ever re-identifying a moved entity**. At `world_dim=32`, the same autopsy that blocks
`E2WorldForward` predicts the feature term will be too weak to disambiguate two
same-type entities by appearance.

**Verdict: the token buffer is FEASIBLE to build at dim=32 but NOT validatable at dim=32.**
Precisely:
- The *mechanism* (the association loop, persistence, attention-gating) runs at any
  `world_dim` -- it is just dict bookkeeping over `z_world`.
- The *discriminative* claim (re-identify a *moved, same-type* entity by continuity+feature
  rather than by nearest-cell) requires the feature term to carry instance-level signal.
  At `world_dim=32` this is at or below the established granularity floor.

**Therefore the experiment (Section 6) MUST run at `world_dim >= 128`** (the same floor
`E2WorldForward` already asserts), and the readiness precondition must *prove* the feature
term is non-degenerate before scoring persistence (so a motion-only pass cannot masquerade
as token tracking). This is the single most important design constraint in this memo. A
v1 that ships and is only ever tested at dim=32 would produce a **vacuous pass** -- the
exact `feedback_diagnostic_self_route_is_hypothesis` failure mode (a PASS that is vacuous
because a precondition was unmet).

### 5.2 The 641a "bound-representation prerequisite absent" finding

**Finding (V3-EXQ-641a, `..._20260606T092011Z_v3`, FAIL / non_contributory diagnostic):**
the coherence-non-reducibility probe (is cross-stream phase-alignment coherence
irreducible to single-stream E?) did not establish a non-reducible bound register;
`evidence_direction_note` routes `specificity_unproven` and warns against
"structural-analogy-no-mechanism." The object-representation thread reads this as
"bound-representation prerequisite absent."

**Relevance to MECH-045.** 641a asked whether REE *already has* an emergent bound
representation arising from cross-stream coherence. The answer (FAIL) is consistent with
the framing of THIS memo: REE does **not** have an emergent token-bound register, which is
*why* MECH-045 must be **built as an explicit substrate** rather than read out of existing
coherence. 641a is therefore not a blocker for this memo -- it is corroboration that the
explicit buffer is the right move (you cannot read a token out of coherence that is not
there; you must maintain it explicitly via data-association). The caution 641a carries
forward is methodological: **do not claim the buffer delivers binding by structural
analogy to object files; prove it delivers cross-motion re-identification behaviourally**
(Section 6 non-vacuity gate).

### 5.3 Feasibility summary

| Question | Answer |
|---|---|
| Can the buffer be *implemented* on V3 as-is? | **Yes** -- non-trainable bookkeeping over `z_world`; bit-identical OFF. |
| Can MECH-045's discriminative claim be *validated* at `world_dim=32`? | **No** -- feature term below the established granularity floor; risks a vacuous motion-only pass. |
| What substrate change is required to validate? | Run the experiment at **`world_dim >= 128`** (already the `E2WorldForward` floor) + a non-degeneracy precondition on the feature term. |
| Does 641a block this? | **No** -- it corroborates that an *explicit* buffer is needed (no emergent bound register exists to read out). |

---

## 6. Pre-specified discriminative experiment (for the post-implementation re-queue of EVB-0293 / EXP-0117)

**Do NOT queue this now.** It is pre-registered here so that, once the
`/implement-substrate` chip lands the buffer, the re-queued EVB-0293 cannot pass or fail
vacuously.

- **run_id:** ends `_v3` (e.g. `v3_exq_NNN_mech045_object_file_persistence_<ts>_v3`).
- **architecture_epoch:** `ree_hybrid_guardrails_v1`.
- **claim_ids:** `["MECH-045"]` (ARC-006 bears-on, not co-tagged -- ARC-006 is a
  substrate_coherence commitment, exempt from exp gating; tagging it would contaminate per
  the `claim_ids` accuracy rule).
- **purpose:** evidence (discriminative_pair).
- **substrate:** `world_dim = 128` (Section 5.1), `use_object_file_buffer` toggled per arm.

### 6.1 Design: matched-seed, ablation vs intact

Seeds `[42,43,44]` (matched across arms). Environment seeds an entity that **moves to a
new cell** between observations, with a **same-type distractor** present (so features
alone cannot disambiguate -- the MOT "identical objects" structure forcing continuity to
carry identity).

| Arm | `use_object_file_buffer` | Identity wiring | Tests |
|---|---|---|---|
| **INTACT** | True | token id from data-association | Can the buffer re-identify the moved entity? |
| **ABLATION-OFF** | False | none | Baseline: no buffer -> no persistence (floor). |
| **ABLATION-SHUFFLE** | True | token ids **shuffled** each tick before readout | Kills identity continuity while keeping the buffer "on" -> isolates that it is the *identity*, not mere buffer presence, that carries persistence. |

### 6.2 Readiness preconditions (non-vacuity gates -- ALL must pass before scoring)

Per `feedback_diagnostic_self_route_is_hypothesis` and the 641a methodological caution:

- **G0 -- buffer populated.** INTACT arm maintains >= 1 live token for the target entity
  on >= 2/3 seeds (else the buffer never engaged -> `substrate_not_ready_requeue`).
- **G1 -- feature term non-degenerate (the dim=32 guard).** The feature distance `d_cos`
  between the target and the same-type distractor must exceed a floor
  (`d_cos_target_distractor >= 0.1`) -- i.e. `z_world` at this `world_dim` actually
  separates the two instances. If it does not, the experiment cannot test token tracking
  (only motion), and self-routes `substrate_not_ready_requeue` (NOT a MECH-045 failure).
- **G2 -- the entity actually moved.** The target's cell at re-observation differs from
  its cell at first observation on every scored trial (else "persistence" is vacuously
  satisfied by a stationary object = the location-collapse mode).

### 6.3 Pre-registered discriminators (scored only if G0-G2 pass)

- **C1 -- re-identification (PRIMARY).** Fraction of trials where the INTACT buffer assigns
  the **same token id** to the entity before and after its move, *and* that token is the
  target (not the distractor): `reid_frac_INTACT >= 0.6`.
- **C2 -- ablation contrast.** `reid_frac_INTACT > reid_frac_SHUFFLE + 0.3` AND
  `reid_frac_INTACT > reid_frac_OFF` (OFF has no token, so its reid_frac is 0 by
  construction; SHUFFLE is the load-bearing control -- it shows the *identity*, not the
  buffer's presence, carries the effect).
- **C3 -- feature persistence.** The token's `z_features` after the entity is briefly
  occluded remains closer to the target's true features than to the distractor's
  (`persisted_feature_match`), on >= 2/3 seeds -- the object-trace-cell property.

**Interpretation grid:**

| Outcome | Reading | Next action |
|---|---|---|
| G0-G2 pass, C1+C2+C3 pass | Token buffer delivers cross-motion re-identification -> MECH-045 *supports* | Governance: consider MECH-045 promotion candidate->provisional retest |
| G0-G2 pass, C1 fail or C2 fail | Buffer present but identity not continuity-carried (motion-only / collapse) -> MECH-045 *weakens* | `/failure-autopsy`: association metric too weak even at dim=128, or gate mis-tuned |
| G1 fail | `z_world` non-discriminative at this dim -> precondition unmet, NOT a verdict | `substrate_not_ready_requeue` at higher `world_dim`; do NOT weaken MECH-045 |
| G0 or G2 fail | Buffer didn't engage / entity didn't move -> test invalid | `substrate_not_ready_requeue`; fix harness |

This grid makes the eventual run **symmetric** (a PASS clears the gate only with G1
non-degeneracy proven; a FAIL weakens only when the precondition that would excuse it is
ruled out) -- closing the under-adjudicated PASS-clears-gate hole flagged in
`feedback_diagnostic_self_route_is_hypothesis`.

---

## 7. Proposed substrate_queue.json entry (for governance to mint -- NOT committed here)

The following is a **candidate** entry for `REE_assembly/evidence/planning/substrate_queue.json`.
This memo does **not** write it; governance mints substrate-queue entries.

```json
{
  "sd_id": "mech-045-object-file-buffer",
  "title": "Token-instance object-file / entity-persistence buffer: spatiotemporal-continuity data-association over z_world assigning label-free per-entity token ids with attention-gated, precision-weighted feature buffers (ARC-006/MECH-045; the missing TOKEN store of the ARC-080 type/token/anchor triad)",
  "status": "pending_implementation",
  "ready": false,
  "design_doc": "docs/architecture/mech_045_object_file_buffer.md",
  "scope_band": "v4_or_late_v3",
  "off_critical_path": true,
  "depends_on_unresolved": [
    "world_dim >= 128 substrate (z_world dim=32 discriminative ceiling, config.py:156; E2WorldForward floor)",
    "candidate-entity proposal from SD-049 resource-field views + grid object/hazard cells (detector dependency, Section 4.4)"
  ],
  "unblocks_claims": [
    "MECH-045",
    "ARC-006",
    "ARC-080 Pillar 1 (object permanence; ghost-goal-bank token generalisation)"
  ],
  "wiring_targets": [
    "SD-057 IncentiveTokenBank (TYPE -> per-token type_hint, backward-compatible)",
    "SD-039 AnchorGoalPayload (ANCHOR -> optional token_id cross-reference)"
  ],
  "proposed_module": "ree-v3/ree_core/entities/object_file_buffer.py",
  "validation_experiment": "pre-registered in design_doc Section 6 (INTACT vs ABLATION-OFF vs ABLATION-SHUFFLE; G0-G2 non-vacuity gates incl. dim=32 feature-degeneracy guard; re-queues EVB-0293/EXP-0117)",
  "no_op_default": "use_object_file_buffer=False, bit-identical OFF; non-trainable (no phased training for v1)",
  "mech_094": "waking-stream only; no-op under simulation_mode/replay/sleep",
  "notes": "Resolves the ARC-080 type-vs-token-vs-anchor fork: token is the spine, the two live stores wire to consume it. v1 lands standalone (no wiring required) and is validatable in isolation. EVB-0293 stays blocked_substrate until this lands AND the dim>=128 substrate is available."
}
```

---

## 8. What this memo unblocks, and what it does not

**Unblocks:** once the `/implement-substrate` chip lands the module (behind no-op flags)
and the `world_dim >= 128` substrate is available, EVB-0293 / EXP-0117 can be re-queued
with the Section 6 design and pass the Step-2.5 readiness gate non-vacuously.

**Does NOT unblock / out of scope:** SD-057 V3 resource-bound behaviour (unchanged),
GAP-7 closure (untouched), MECH-278 object-schema formation (V4, separate), the
self/other object-file slots ARC-081/083 (V4, separate), and any promotion of MECH-045 /
ARC-006 (governance decision, gated on the experiment actually running).

**Sequencing reminder (ARC-080 §5.1):** this is Pillar-1 (permanence) substrate work --
V3-straddle / V4, **must NOT enter V3 closure.**

---

## Related Claims (IDs)

- MECH-045 (object-file-like persistence -- this substrate's home claim)
- ARC-006 (entities are sparse, persistent, bindable structures), MECH-044 (hippocampal relational binding), MECH-050 (functional locality)
- ARC-080 (object-representation umbrella; type-vs-token-vs-anchor fork), ARC-081/082/083 (pillars; downstream consumers, V4)
- SD-057 / MECH-344-348 (IncentiveTokenBank -- TYPE store; proposed wiring target)
- SD-039 / MECH-292 / MECH-293 (ghost-goal bank -- ANCHOR store; proposed wiring target)
- MECH-278 (object definition / schema -- V4, bypassed in V3), ARC-059 (developmental ordering)
- INV-002 (coherence includes temporal binding), MECH-094 (waking-vs-simulation write gate)

## References / Source

- Biology lit-pull: `evidence/literature/targeted_review_mech_045_object_file/` (5 entries, 2026-06-09) + ARC-080 pulls `targeted_review_object_files_feature_binding` (L1), `targeted_review_object_permanence` (L2), both 2026-06-04.
- [`entities_and_binding.md`](entities_and_binding.md) (ARC-006 / MECH-045), [`arc_080_object_representation_primitive.md`](arc_080_object_representation_primitive.md) (umbrella + fork), [`sd_057_object_bound_incentive_salience.md`](sd_057_object_bound_incentive_salience.md) (TYPE store), [`sd_039_anchor_goal_payload.md`](sd_039_anchor_goal_payload.md) (ANCHOR store).
- `docs/thoughts/2026-02-10_object_file_persistence.md` (original source fragment).
- z_world ceiling: `ree-v3/ree_core/utils/config.py:156` (world_dim>=128 / E2WorldForward floor). 641a: `evidence/experiments/v3_exq_641a_coherence_ablation_nonreducibility_20260606T092011Z_v3.json`.
- Blocked proposal: `evidence/planning/experiment_proposals.v1.json` EVB-0293 / EXP-0117 (`status: blocked_substrate`, 2026-06-09).
