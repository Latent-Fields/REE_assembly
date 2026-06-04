# Planning Memo: Grounding a Future REE Language Faculty in the Emerging Discretisation Substrate (LLM Engineering as Mined Counsel)

**Date:** 2026-06-04
**Type:** Long-horizon architecture-coherence / convergence-intake review (planning memo only)
**Status:** EXPLORATORY DESIGN. NO claims registered, NO substrate code, NO experiments queued. Surfaced for user decision.
**Target horizon:** **V5** (user-confirmed 2026-06-04: "ready to come back to in V5"). This is later than V4 (= social systems / "sharing joys and sorrows"). Resume primitive: revisit this memo at the start of V5 scoping; check the §5.4 V3 prerequisites have closed and that the V4 social layer (which the language faculty's internal<->external map depends on) is in place before building any of the proposed spine.
**Author session:** language-system-llm-mining-review-20260604T1539Z (TASK_CLAIMS)
**Sibling session (coordinate, do not duplicate):** object-representation-thread-design-review-20260604T1539Z -> `evidence/planning/object_representation_thread_2026-06-04.md`

---

## 0. HARD CONSTRAINT (read first)

This is **V4+/language-system long-horizon work**. It must **not touch or reprioritise the active V3-closure critical path** (goal_pipeline:GAP-7 L9 retest, goal_pipeline:GAP-2 foraging-competence / `scaffolded_sd054_onboarding`, behavioral_diversity GAP-A/B/C, etc.). Everything below is capture-and-design. The proposed claim spine is a PROPOSAL; it is not registered and must not enter `claims.yaml` or any experiment queue without an explicit, separate user decision gated well after V3 closure.

---

## 1. Trigger and the load-bearing distinction

On 2026-06-04 we landed **SD-057 object-bound incentive salience** (`ree-v3/ree_core/goal.py` `IncentiveTokenBank`, MECH-344/345/346): a per-object incentive layer that mints a per-resource-type **"token"** holding a cached value + a stored `z_object` identity embedding. The user observed that "tokenisation" is also a core LLM feature, and that LLMs likely share features with REE's eventual language system, so LLM design could be mined for it.

**The pun is not the thread.** A REE incentive *token* (`goal.py:163` — a per-object cached value + identity embedding keyed by an integer type tag) and an LLM *token* (a discrete sub-word vocabulary unit produced by BPE/byte-level tokenisation) share the *word* but are different constructs. Building the review on that lexical overlap would be a category error.

**The genuine shared thread, one level up, is:**

> **Discretisation of continuous experience into addressable, typed, reusable units — a grounded vocabulary of discrete symbols — plus a sequence model over those units.**

That is precisely what a language faculty needs and what LLMs are the most mature *engineering* instance of. The whole review is framed on this **discretisation / vocabulary / sequence bridge**. Where the incentive-token/LLM-token analogy is *superficial* vs *load-bearing* is flagged explicitly in §3.6.

**Relationship to existing REE language work.** REE already carries a (largely early / legacy) **language-as-coordination** layer — `INV-003` (language emerges as functional self-representation), `ARC-009` (language as symbolic mediation/coordination layer), `MECH-010..MECH-015` (emergence/learning/institutions/failure-modes/signalling/trust), and the more recent Steve-the-dog bridge `ARC-048` + `MECH-191/192/193` + `INV-057` (language as high-bandwidth externalisation of pre-existing functional states), plus `docs/architecture/language.md`, `docs/architecture/play_mode.md`, and `docs/thoughts/2026-02-09_language.md`. **None of those address the discretisation/vocabulary/sequence substrate** — they answer *why* language emerges (coordination, compression, externalisation of functional state) and *what social preconditions* it has (joint attention, signal legibility), not *what grounded discrete units it is built from* or *what sequence machinery operates over them*. This memo is the **substrate-side complement** to that existing emergence-side layer. The two must be reconciled at registration time (see §5.3), not duplicated.

---

## 2. STEP 1 — REE's current discretisation / symbol / sequence substrate

REE has, almost incidentally, accreted a substantial amount of machinery that turns the continuous experience stream into discrete, typed, addressable, reusable units and operates over sequences of them. The table audits each. Columns:

- **(a) vocabulary** — does it provide a finite/growing set of distinct typed units?
- **(b) grounded** — are the units anchored to experience latents (`z_world`/`z_self`/`z_harm`/`z_resource`/`z_goal`/sensory)?
- **(c) sequence** — does it compose or sequence the units?

| # | Substrate (claim) | File (verified) | (a) vocab | (b) grounded | (c) seq | What the mechanism actually is |
|---|---|---|---|---|---|---|
| 1 | **SD-049** multi-resource per-type identity tags | `ree-v3/ree_core/environment/causal_grid_world.py` | **Yes** — integer type tags `1..n` (`_resource_type_grid`, `resource_type_at_agent`), per-type proximity field views | **Yes** — env-side; each tag indexes a qualitatively distinct resource type (food/water/novelty) | No | The discrete *type alphabet*. A small, fixed, typed vocabulary of object kinds, each with its own drive axis. The most language-like primitive REE has: a finite set of discrete categories over experience. |
| 2 | **SD-049 Phase-2 / SD-015** identity-aware `z_resource` encoder + classifier head | `ree-v3/ree_core/latent/stack.py` (`ResourceEncoder`, `identity_logits`) | Partial — the classifier head **maps continuous `z_resource` -> discrete type logits** (the grounding<->symbol map) | **Yes** — `z_resource` is the object-type latent (location-invariant "what") | No | The **grounding-to-symbol bridge for objects**: a learned map from a continuous identity embedding to a discrete category. This is the closest existing thing to "lexicalisation" — continuous percept -> discrete label. |
| 3 | **SD-057 / MECH-345** per-object incentive token bank (`z_object`) | `ree-v3/ree_core/goal.py:163` `IncentiveTokenBank` | **Yes** — `dict: tag k -> (base_value[k], z_object[k])`; addressable by integer tag; minted on contact (L2), looked up by L4 pointer `(k*, z_object[k*], wanting[k*])` | **Yes** — `z_object[k]` is the stored `z_resource` identity embedding | No | A **growing, addressable store of grounded entries keyed by discrete identity**. Structurally this *is* a tiny learned-by-experience vocabulary table: discrete key -> (value, embedding). The trigger for this memo; see §3.6 for where the token analogy is load-bearing vs superficial. |
| 4 | **ARC-006** entities as sparse, persistent, bindable structures | `docs/architecture/entities_and_binding.md` (design); object-file thread | Partial — entities are addressable persistent slots | Yes (design intent) | No | The **object-file / entity-persistence** commitment. Discrete persistent referents — the precondition for a noun-like unit that survives occlusion/respawn. Coordinated with the sibling object-representation memo. |
| 5 | **MECH-288** event segmenter (`BoundaryEvent`) | `ree-v3/ree_core/hippocampal/event_segmenter.py:43` | **Yes** — emits monotonic `outer.inner` **segment IDs** at detected boundaries; two-scale (PE-threshold fast on `z_world+z_self`; BOCPD-Gaussian slow on `z_goal`) | **Yes** — boundaries fire on prediction error in grounded latents | **Yes** | **Discretisation of the experience *stream* into discrete, nested, addressable events.** This is the temporal-segmentation analog of tokenisation: it chunks a continuous signal into discrete, hierarchically-IDed units. The single most important existing substrate for the language bridge — it already turns continuous time into a sequence of discrete typed segments. |
| 6 | **MECH-269 anchor sets** (scale, segment_id, stream_mixture) | `ree-v3/ree_core/hippocampal/anchor_set.py` | **Yes** — keyed addressable anchors (`AnchorKey`), dual-trace (active/inactive) | **Yes** — `z_world` + per-stream V_s | Partial — anchors are the nodes a sequence is built over | Discrete, keyed, persistent memory units (Bouton dual-trace). A *symbol table over places/regions* the hippocampus addresses. |
| 7 | **SD-039 / MECH-292 / MECH-293** ghost-goal bank (per-anchor goal snapshots) | `ree-v3/ree_core/hippocampal/ghost_goal_bank.py:149`; `anchor_set.py` `AnchorGoalPayload` | **Yes** — per-anchor `goal_payload` (`z_goal_snapshot`, wanting, arousal); ranked, queryable by cosine match | **Yes** — `z_goal` snapshots | Partial — ghost-seeded trajectory proposals are sequences | Addressable stored *goal* units with a retrieval-by-content cue (cf. `MECH-339` composite cue + outshining). A content-addressable memory of discrete motivational referents — directly analogous to cue-addressed retrieval in a vocabulary. |
| 8 | **SD-004** E2 action-object space O | `ree-v3/ree_core/predictors/e2_fast.py` (`action_object`); `ree-v3/ree_core/hippocampal/module.py` | Partial — `o_t` is a *compressed* world-effect space, lower-dim than `z_world`; not yet a discrete codebook | **Yes** — `o_t = E2.action_object(z_world, a)` encodes world-effects | **Yes** — hippocampus proposes **sequences** in O, decodes to action sequences | The **action-object space** the hippocampus navigates *instead of* raw `z_world`. A semantically-grounded compressed space — the natural place a *verb-like / affordance* codebook would attach. Currently continuous; a quantiser over O would yield a discrete affordance vocabulary. |
| 9 | **MECH-291 / MECH-293 / ARC-018 / ARC-032** hippocampal sequence generation | `ree-v3/ree_core/hippocampal/module.py` (`propose_trajectories`, `_propose_ghost_seeded`); `MECH-290` backward sweep | n/a (operates over units) | **Yes** — sequences over grounded action-objects / anchors | **Yes** — **this is REE's existing sequence model**: CEM trajectory proposal + replay (waking/quiescent), goal-biased, one generator across waking + offline (Muessig 2019 framing) | **REE already has a sequence generator over grounded units.** It is *not* a transformer; it is a CEM-refined, residue-shaped, replay-capable proposer over action-object space. This is the substrate any "sequence model over the vocabulary" should *reuse / extend*, not replace (see §3.3). |
| 10 | **ARC-063 / MECH-349-352** CandidateRule field | `ree-v3/ree_core/policy/candidate_rule_field.py:100` `CandidateRule` | **Yes** — minted **rule slots** on recurring `(context-bucket -> action-object)` regularities; pinned-distinct subspace directions (Weber 2023); availability/eligibility/context-tag | **Yes** — context_tag in `z_world`; action-object grounded | Partial — rules are context->action-object production units | A **non-Bayesian creator that mints discrete reusable units (rules) from recurring regularities** and combines the active ones into a differentiated state. Architecturally this is *grammar-adjacent*: discrete production rules minted by frequency over grounded antecedents. Landed today (2026-06-04) for GAP-B; mechanically the most "compositional" substrate REE has. |
| — | latent codebook / VQ-VAE-style quantisation | (searched: none) | — | — | — | **REE has NO explicit vector-quantisation / learned discrete codebook anywhere.** The discreteness it has is either (i) env-side type tags (SD-049), (ii) dict-keyed banks (SD-057, ghost-goal), (iii) PE-driven event boundaries (MECH-288), or (iv) minted rule slots (ARC-063). There is no continuous-latent -> discrete-code quantiser. This is the single clearest *engineering gap* a VQ-style mechanism could fill (see §3.2). |

### 1.1 Reading of the table

REE's discretisation substrate is **strong on grounding, partial on vocabulary, weak-but-present on sequence, and absent on a unified codebook**:

- **Grounding is everywhere** — every discrete unit REE has is anchored to an experience latent. This is REE's structural advantage over LLMs and the whole point of the philosophy (Axiom II signal regularity; §4.3). REE does not have the symbol-grounding problem *for the units it already has* because they were never ungrounded to begin with.
- **Vocabulary exists in fragments** — SD-049 type tags, SD-057 token bank, MECH-288 segment IDs, ARC-063 rule slots, ghost-goal entries are each a *local* addressable typed vocabulary, but they are **not unified, not compositional across each other, and not externalisable as symbols**. There is no single "lexicon" object; there are five disjoint addressable stores.
- **A sequence model already exists** (MECH-291/293 hippocampal generator) — and crucially it is **not** a transformer and **should not** be replaced by one (§3.3).
- **The missing keystone** is a *general* learned discretisation of a continuous latent into a reusable, compositional code — and the *mapping layer* between internal grounded units and external (communicable) symbols.

---

## 3. STEP 2-3 — Language-faculty requirements, gaps, and mined LLM counsel

### 3.0 Layer-7 framing (ENGINEERING COUNSEL, NOT ARCHITECTURAL AUTHORITY)

REE is neuroscience/philosophy-grounded, not RL/LLM-derived. LLM engineering is mined here as **counsel on solved sub-problems**, never as theoretical framing to import wholesale. For each mined technique below: what engineering problem it solves, and how the REE adaptation must differ. REE's anti-over-engineering norm holds throughout (encoders are 2-3 layer MLPs; do **not** import ImageNet/LLM-scale complexity).

### 3.1 What a REE language faculty needs (requirements)

A language faculty grounded in REE's ontology requires:

1. **Symbol grounding** — external symbols must bottom out in `z_world`/`z_self`/`z_harm`/`z_resource`/`z_goal`/functional-state latents. REE *largely has this already* for its internal units (table §2); language reuses it. (ARC-048's "functional states as referents" is the existing claim.)
2. **A compositional vocabulary** — a unified, reusable, growing set of discrete grounded units that can be *combined*. REE has fragments (§1.1) but no unified lexicon and no general composition operator across them.
3. **Sequence prediction/generation over the vocabulary** — REE *has* a sequence generator (MECH-291/293) over action-objects; a language faculty needs an analogous generator over *symbol* units, ideally the **same** generator extended.
4. **Internal<->external mapping** — the bidirectional map between an internal grounded representation and an external (emitted/perceived) symbol. This is the genuine new organ. ARC-048/MECH-191 already frame *why* (externalisation of functional state for coordination); the substrate is unbuilt.
5. **Self-supervised learning signal** — a training signal for the vocabulary + sequence model. REE has a native one (E1/E2 prediction error) that is *better grounded* than next-token prediction (§3.4).

### 3.2 Requirements -> gaps (what REE partially meets vs genuine gaps)

| Requirement | REE status | Gap |
|---|---|---|
| Symbol grounding | **Met (for internal units).** SD-049/SD-015 classifier, SD-057 z_object, MECH-288 grounded boundaries. | The gap is not grounding — it is grounding *of external symbols*, i.e. wiring step 4. |
| Compositional vocabulary | **Partial.** Five disjoint addressable stores. No unified lexicon; no general quantiser (no VQ); no composition operator. | A **general discretisation layer** over a chosen latent (e.g. action-object space O or z_world) producing a reusable code, + a composition mechanism. ARC-063 rule-field is the nearest compositional primitive. |
| Sequence model over units | **Met-and-reusable.** MECH-291/293 hippocampal generator; MECH-288 already sequences events. | Extend the existing generator to symbol units; do **not** add a parallel transformer stack. |
| Internal<->external mapping | **Absent.** | The genuine new organ: an emit/perceive map between internal units and communicable symbols. (ARC-048 frames the *function*; no substrate.) |
| Self-supervised signal | **Met (native).** E1/E2 PE channels; MECH-288 boundaries are themselves PE-driven. | Decide how a symbol-sequence prediction signal relates to E1/E2 PE (§3.4); not a missing capability, a design choice. |

### 3.3 LLM-mining: sequence models — contrast, do NOT default to transformer

**Engineering problem transformers solve:** long-range dependency modelling over discrete token sequences with parallelisable training and content-based (attention) addressing.

**REE adaptation / how it must differ:** REE *already has a sequence substrate* — the hippocampal generator (MECH-291/293): CEM-refined, residue-shaped, goal-biased, replay-capable, and crucially **one generator shared across waking and offline modes** (the Muessig-2019 framing already in the codebase). It is biologically motivated and grounded. **Defaulting to "use a transformer" would be importing LLM theoretical framing wholesale — the prohibited move.** What is genuinely mineable:
- **Content-based addressing** (attention's core idea) already has a REE analog: the ghost-goal bank's cue-addressed retrieval (`MECH-339` composite cue + outshining) and anchor `query_by_goal_match`. The mined lesson is *the value of content-addressable retrieval over a stored vocabulary*, which REE independently arrived at — not the transformer's specific QKV machinery.
- **Positional / hierarchical structure**: MECH-288's nested `outer.inner` segment IDs already encode hierarchical sequence position grounded in PE, which is *more* principled than learned positional embeddings.
- **Verdict:** the REE sequence model for language should be the **extended hippocampal generator over a symbol/affordance code**, with content-addressable retrieval (already present), not a transformer. Transformers are counsel on *what problems a sequence model must solve* (long-range dependency, addressing), not the architecture to adopt.

### 3.4 LLM-mining: next-token prediction as self-supervision vs REE's PE channels

**Engineering problem it solves:** a dense, label-free training signal that forces a model to represent the statistics of the sequence — the entire basis of LLM pretraining.

**REE adaptation:** REE's **E1/E2 prediction-error channels are the native equivalent and are better grounded** — they predict *grounded latent continuations under action*, not surface symbol co-occurrence. MECH-288 boundaries are *themselves* PE events. The mined lesson is the *power of next-element prediction as a self-supervised objective*, which REE already exploits at the latent level. The design choice (not gap): a symbol-sequence-prediction signal should be **derived from / consistent with** E1/E2 PE rather than a parallel surface-statistics objective — otherwise REE would grow an ungrounded language model bolted onto a grounded core (exactly the failure mode INV-003 was written to forbid: "language emerges as functional self-representation, not a bolt-on"). The philosophy's anti-correspondence stance (§4.3) reinforces this: meaning is predictive adequacy, not symbol-symbol statistics.

### 3.5 LLM-mining: vocabulary construction (BPE / wordpiece / byte-level / VQ-VAE)

**Engineering problem these solve:** turning a continuous or open-ended input into a finite, reusable, discrete vocabulary that a sequence model can operate over efficiently.

**REE adaptation per scheme:**
- **Text BPE / wordpiece / byte-level** solve discretisation *of already-discrete text*. **Superficially relevant to REE** — REE's input is continuous grounded experience, not a byte stream. "Tokenisation of grounded experience" in REE would mean: chunk the continuous experience stream into reusable units. REE *already does the temporal-chunking half* via MECH-288 (event segmentation). What it lacks is the *unit-content quantisation* half.
- **VQ-VAE / learned discrete codebooks** are **the genuinely load-bearing analog** — closer to REE than text BPE. A VQ codebook maps a *continuous latent* to a nearest discrete code-vector, learned end-to-end, with a small (256-1024) codebook. This is *exactly* the missing keystone in §1.1: a general continuous-latent -> reusable-discrete-code map. The natural REE attachment point is **action-object space O (SD-004)** — quantising `o_t` would yield a discrete *affordance/verb* vocabulary grounded in world-effects — or **`z_resource`** (SD-015), where SD-049's classifier head is already a soft version. **Caveat (anti-over-engineering):** a VQ-VAE in vision/audio is large; REE's encoders are 2-3 layer MLPs. A REE codebook should be *small* (tens of codes, matching SD-049's handful of types and ARC-063's 16 rule slots), learned with the existing PE signal, not a heavyweight separate VQ training run.
- **Verdict:** VQ-style quantisation is the most mineable single technique; BPE/byte-level is mostly a category mismatch (REE's "tokenisation" is event segmentation, already done). The codebook must be small and grounded, attached to O or z_resource, trained on existing PE.

### 3.6 The incentive-token / LLM-token analogy: where superficial vs load-bearing

| Aspect | Superficial (do not build on) | Load-bearing (genuine) |
|---|---|---|
| The word "token" | SD-057 incentive token vs LLM sub-word token share only the name; one is (value, embedding) keyed by object identity, the other is a vocabulary index. | — |
| **Addressable keyed store** | — | SD-057's `dict: tag -> (value, embedding)` *is* structurally an embedding table / learned vocabulary keyed by discrete identity. The LLM lesson — *a discrete-keyed table of learned embeddings is a powerful, composable primitive* — transfers. |
| **Minting by experience** | — | SD-057 mints tokens on contact; ARC-063 mints rules on recurrence. This *growing-vocabulary-from-experience* pattern is exactly what a grounded lexicon needs and is the opposite of LLMs' fixed pre-trained vocabulary — a place REE is *ahead* conceptually. |
| Sequence over tokens | LLM tokens feed a transformer. | REE's units feed the hippocampal generator. The *sequence-over-discrete-units* idea is shared; the machinery is not. |

**Bottom line of §3:** the load-bearing mined techniques are (1) VQ-style small grounded codebook (fills the §1.1 keystone gap), (2) discrete-keyed embedding-table-as-vocabulary (SD-057 already instantiates the pattern), (3) content-addressable retrieval over the vocabulary (REE already has it). The rejected imports are: transformer-by-default, next-token surface-statistics as a parallel objective, text-BPE, and LLM-scale model sizing.

---

## 4. STEP 4 — Biology before formal definitions (recommended lit pulls)

Per the project rule (`feedback_biology_before_formal_definitions`: commission biology *before* registering any SD/MECH that instantiates a formal concept — canonical failures SD-003, SD-010/011), **no LLM formalism should be registered before the biology anchor is pulled.** Recommended lit pulls (recommend only — do not run unless trivial), each tagged with the proposed claim it would ground:

1. **Statistical learning / word segmentation** — Saffran et al. 1996 (8-month-old transitional-probability word segmentation); Aslin/Newport. *Grounds:* the discretisation-of-the-stream claim — segmentation of a continuous signal into reusable units by transitional statistics. Directly validates MECH-288-as-language-substrate and any proposed lexicalisation claim. **(Highest priority — it is the bridge from MECH-288 to language.)**
2. **The symbol grounding problem** — Harnad 1990; Barsalou perceptual symbol systems. *Grounds:* the internal<->external mapping claim and the framing that REE's units are grounded-by-construction. Connects to the philosophy paper (§4.3).
3. **Dual-stream language model** — Hickok & Poeppel 2007 (dorsal "how"/sensorimotor vs ventral "what"/comprehension streams); Broca/Wernicke functional anatomy. *Grounds:* a proposed ARC-level architecture split (a production/sequencing stream vs a comprehension/grounding stream) — and tells us whether the emit/perceive map should be one organ or two. Note REE already has a "dorsal-like" sequencing substrate (hippocampal generator) and "ventral-like" grounding (z_resource/z_object).
4. **Predictive processing in language** — Pickering & Garrod 2013 (prediction-by-production in dialogue); Lupyan. *Grounds:* the §3.4 design choice that the language sequence signal derive from E1/E2 PE rather than a parallel objective. Confirms the prediction-error framing is biologically right for language, not just for perception.
5. **Gesture / protolanguage / emotional-prosody continuity** — already partly pulled for ARC-048 (Filippi 2016 emotional prosody as language precursor; Fournier 2026 cross-species vocal emotion). *Grounds:* the pre-linguistic-to-linguistic bridge (ARC-048) connection to the discretisation thread — how graded externalised signals (whine/yelp, MECH-191) become discrete symbols.
6. **Infant word learning / fast mapping** — Carey & Bartlett fast mapping; Markman constraints; cross-situational word learning (Yu & Smith). *Grounds:* the mint-by-experience pattern (SD-057/ARC-063) extended to symbol acquisition — how a single grounded unit gets a label from sparse exposure.
7. **Arcuate fasciculus / sequence-to-motor** — note existing `docs/thoughts/2026-02-09_arcuate_fasciculus_language_nudges.md` (MECH-017: arcuate-like sequence-to-motor channel). *Grounds:* the internal<->external *production* map (how a planned symbol sequence reaches an output channel) — REE-internal prior art to reconcile.

### 4.3 Philosophy foundation (Synthese paper) — bearing on symbol grounding

`/Users/dgolden/Documents/GitHub/Philosophy/Synthese_submission/ree_minds_machines_DRAFT.md` **does not address language or symbol grounding in classical (Harnad) terms**, but it bears on *meaning* in a way that constrains the whole faculty:

- **Axiom II (Signal Regularity):** "Signals arise from a structured and persistent process such that prediction across time is possible." -> meaning arises from *structured signal regularity*, not arbitrary symbol-world mapping. This is the philosophical license for §3.4 (PE-derived language signal) and for the whole grounded-vocabulary stance.
- **§6 Temporal Coherence Without Ground Truth:** REE "rejects privileged latent world states"; trajectories persist by *temporal survivability*, not truth. -> A REE symbol's meaning is its *predictive/functional adequacy*, not correspondence. This is an explicitly **enactivist, anti-representational** grounding (§10.4) — closer to Wittgenstein-use / coordination than to reference.
- **Implication for the faculty:** symbols are tools for coordination-preserving prediction, not truth-carriers. This *aligns with ARC-009/INV-003* (language as coordination/functional self-representation) and means the proposed faculty should ground meaning in **functional persistence + coordination**, not in a symbol-referent correspondence table. Harnad's grounding is *necessary but not sufficient* in REE's frame — grounding must be to *viable predictive engagement*, not to sensorimotor invariants alone.

---

## 5. STEP 5 — Homes, insertion points, proposed claim spine, sequencing

### 5.1 Homes

- **LLM-mining intake** belongs in **REE_convergence** (the established intake/translation workspace for external frameworks — JEPA, MuZero, DNC, Dreamer, ...). A stub is created at `REE_convergence/sources/llm-language-systems/README.md` (see §6), cross-linked to this memo. A *full* 7-file intake (`source.yaml`, `claims.md`, `ree_map.md`, ...) is **not** created — that is premature before the user decides to pursue the faculty; the stub records the scope and the discretisation-bridge framing so a full intake can be spun up on decision.
- **The design memo** (this file) lives in `REE_assembly/evidence/planning/` alongside the existing `thought_intake_*` / `literature_synthesis_*` files.

### 5.2 Logged candidate insertion points (REE substrate)

Where a language/vocabulary layer would attach (LOGGED, not built):

1. **A small grounded codebook over action-object space O** (`e2_fast.py action_object`) — quantise `o_t` into a discrete *affordance/verb* vocabulary. Reuses SD-004; trained on existing E2 PE. The single highest-value insertion point (fills the §1.1 keystone).
2. **A symbol layer reading the SD-057 token bank + SD-049 type tags + ARC-006 entities** — unify the existing disjoint addressable stores into a single *noun-like* lexicon. No new grounding needed; a unification/indexing layer over what exists.
3. **Sequence reuse: extend the hippocampal generator** (MECH-291/293 `propose_trajectories` / `_propose_ghost_seeded`) to propose *symbol* sequences, with content-addressable retrieval (ghost-goal bank / MECH-339 pattern). Do **not** add a transformer.
4. **MECH-288 segment IDs as the temporal-chunking primitive** — the language stream's "where do units begin/end" is already answered by the event segmenter. A lexicalisation layer consumes BoundaryEvents.
5. **Internal<->external map** — the genuinely new organ; attaches downstream of (1)+(2), upstream of an output channel (cf. arcuate MECH-017). Frames onto ARC-048's externalisation channel.

### 5.3 Proposed claim spine (PROPOSALS ONLY — NOT registered)

A candidate ARC-level spine for the language faculty, **explicitly subordinate to and reconciled with** the existing `INV-003`/`ARC-009`/`ARC-048` layer (which it complements on the substrate side):

- **ARC-LANG-α (proposed):** *A REE language faculty is built on a unified grounded discrete vocabulary + the existing hippocampal sequence generator, not a separate language model.* (Reconciles with INV-003 "not a bolt-on"; this is its substrate-level restatement.)
  - **child Q-claim:** Should the vocabulary be a learned VQ-style codebook over O, an index over existing stores (SD-049/SD-057/ARC-006), or both? (Decided by the §4 lit pulls + a substrate readiness probe — *after* V3.)
  - **child MECH (proposed):** *grounded lexicalisation* — continuous latent (O or z_resource) -> small discrete code via VQ, trained on E1/E2 PE. Grounds on Saffran statistical learning + VQ-VAE counsel.
  - **child MECH (proposed):** *event-segmented unit boundaries* — language units inherit boundaries from MECH-288. Grounds on word-segmentation lit.
  - **child MECH (proposed):** *internal<->external symbol map* — the emit/perceive organ. Grounds on Hickok & Poeppel dual-stream + arcuate MECH-017.
  - **child MECH (proposed):** *PE-derived sequence-prediction signal* — symbol-sequence learning derives from E1/E2 PE, not surface statistics. Grounds on Pickering & Garrod + philosophy Axiom II.
- **Reconciliation note:** ARC-009 (symbolic mediation), ARC-048 (externalisation channel), MECH-191/192/193 (signal legibility), INV-057 (cross-species legibility) are the *emergence/coordination* face; ARC-LANG-α is the *substrate/discretisation* face. At registration they must be cross-linked, not duplicated — the existing claims answer "why/when language", the proposed spine answers "from what units / on what machinery".

### 5.4 Developmental sequencing (V5 target; what must NOT enter V3)

- **This is V5 work** (user-confirmed 2026-06-04) — exploratory, gated **well after V3 closure** and after the V4 social layer. V4 (social systems / "sharing joys and sorrows", multi-agent z_self_j) is itself a prerequisite: the internal<->external symbol map (the new organ in §3.2/§5.2) presupposes a represented *other* to communicate with, which is V4 territory. So the dependency chain is **V3 closure -> V4 social -> V5 language faculty.**
- **V3 prerequisites** (must be done first, on the existing critical path — not advanced by this work): goal_pipeline:GAP-2 foraging competence + GAP-7 L9 wanting/liking dissociation (so the object vocabulary is behaviourally real); behavioral_diversity closure (so the sequence generator produces diverse non-monostrategic sequences — a degenerate generator cannot support compositional language); SD-049 Phase-2 identity-recovery validation (V3-EXQ-514 — so the grounding-to-symbol map is proven before a vocabulary is built on it); ARC-063 GAP-B behavioural validation (so the rule/composition primitive is real).
- **What must NOT enter V3:** no codebook/quantiser, no symbol layer, no internal/external map, no language sequence objective, no claim registration. The V3/V4 boundary doc (`ree-v3/CLAUDE.md`, V4 scope = social systems "sharing joys and sorrows") already places language-grade multi-agent communication in V4; this memo is consistent with that and adds the substrate-side detail.
- **Earliest sensible first step (V5):** the *lexicalisation* MECH alone — a small grounded codebook over O or z_resource, validated as a substrate-readiness probe (identity recovery + reuse), with NO external symbols yet. Everything else sequences after.

---

## 6. STEP 6 — Deliverables and recommendations

- **This memo** — `REE_assembly/evidence/planning/language_system_llm_mining_2026-06-04.md`.
- **Convergence intake stub** — `REE_convergence/sources/llm-language-systems/README.md` (created; lightweight, cross-linked; records the discretisation-bridge framing + which LLM techniques are load-bearing vs rejected; flags that a full 7-file intake is deferred pending user decision).
- **No claims registered, no claims.yaml edit, no substrate code, no experiments queued.**

### Recommendations to the user (for decision)

1. **Accept the framing** that the REE-LLM bridge is *discretisation/vocabulary/sequence*, not the token pun. (Confirm or redirect.)
2. **Commission the §4 biology lit pulls** (priority: Saffran statistical learning, then symbol grounding, then Hickok & Poeppel) — these are cheap, biology-first, and are the gate before any formal claim. Could be done *during* V3 (literature work does not touch the V3 critical path) so the design is ready when V4 opens.
3. **Coordinate with the object-representation sibling memo** (`object_representation_thread_2026-06-04.md`) — the discrete-typed-objects -> vocabulary -> symbols -> language arc is one continuous thread; the object memo owns the object/entity end, this memo owns the language end. Register a shared ARC spine, not two.
4. **Defer everything substrate-side to V5** (per the V3 -> V4 social -> V5 language chain in §5.4), gated on the §5.4 V3 prerequisites and the V4 social layer. The earliest build is the grounded codebook over O.
5. **Reconcile, do not duplicate, the existing INV-003/ARC-009/ARC-048 language layer** when (if) the spine is registered.

---

## Appendix — verification notes

All §2 file/line references were read directly this session (`goal.py:163` IncentiveTokenBank; `event_segmenter.py:43` BoundaryEvent; `ghost_goal_bank.py:149`; `candidate_rule_field.py:100`; `module.py` SD-004 action-object space; `e2_fast.py action_object`). The "no VQ/codebook anywhere" finding is from a negative grep over `ree-v3/ree_core/` for `codebook|quantiz|quantis|vocab|discret` (matches were config flags / comments, not a quantiser). Claim titles/status confirmed against `docs/claims/claims.yaml`. Philosophy passages per the Synthese draft (`§6`, `§10.4`, Axiom II) located this session. Existing language layer (INV-003/ARC-009/MECH-010-015/ARC-048/MECH-191-193/INV-057, `docs/architecture/language.md`, `play_mode.md`) confirmed present in `claims.yaml` + docs.
