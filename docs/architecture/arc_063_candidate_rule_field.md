# ARC-063: policy.rule_apprehension_layer (V3-tractable distributed CandidateRule field)

**Claim ID:** ARC-063
**Subject:** policy.rule_apprehension_layer.strong_reading
**Status:** PENDING (V3-tractable design; design-only — no code yet)
**Registered:** 2026-06-04 (design doc; ARC-063 claim registered 2026-05-08, brought V4→V3 2026-05-18)
**Depends on:** SD-033a (LateralPFCAnalog rule_state consumer — the GAP-B target), ARC-062 (gated-policy top-down population source), ARC-064 (bottom-up rule discovery population source), MECH-288 (event segmenter — context boundaries), MECH-269/MECH-292 (hippocampal anchor / rollout substrate), SD-049 (per-type identity tags — a context-tag source)
**Blocks:** arc_062_rule_apprehension:GAP-B (the canonical closure), MECH-309 promotion, MECH-318 retire-vs-promote gate, the GAP-7/object-discretisation and language threads (downstream)

Lit grounding (pulled 2026-06-04, A+B+C top-up):
`evidence/literature/targeted_review_tolerance_gated_rule_availability` (A),
`targeted_review_rule_level_credit_assignment` (B),
`targeted_review_candidate_rule_field_representation` (C),
plus `targeted_review_arc_062_rule_apprehension`, `targeted_review_arc_064_bottom_up_rule_discovery`,
`targeted_review_mech_318_rule_state_abstraction`, `targeted_review_socially_scaffolded_rule_population`,
and the embedded 2026-05-04 tolerance-gated intake in `docs/architecture/rule_apprehension_layer.md`.

---

## Problem

`arc_062_rule_apprehension:GAP-B` is blocked on a substrate that does not exist: a **non-Bayesian rule-creator** — a mechanism that *populates differentiated rule_state* into SD-033a, "not just trainable bias heads."

MECH-309's logical-necessity claim: **trainers weight rules they do not invent.** Without a mechanism that *creates* candidate rules, gradient descent on a parametric policy collapses to the single smoothest regime good-enough across the whole state space. The 543 lineage demonstrated this empirically and exhaustively:
- ARC-062 weak-reading (two scoring heads + context discriminator) collapsed to inert across one-hot head inputs (543f/g), differential heads (543i), mode_separation_floor 0.5 + P1 aux 0.3 (543l, all four diff-ON arms 3/3 inert), and crystallization (543h).
- V3-EXQ-598b isolated the cause: the bias-head *wiring* is correct (C1 frozen-silent PASS, C2 trainable-nonzero PASS) but **the upstream rule_state inputs collapse** (C3 trainable-not-monomodal FAIL: ARM_0 `[0.10, 0.06, 0.0]` vs ARM_1 `[0.10, 0.03, 0.0]`).

The deep reason: **gradient descent weights; it does not mint.** Two scalar heads sharing a return gradient have an inert equilibrium (head_0 == head_1) that is a flat attractor; differentiation is a rare lucky-basin escape. The fix is not more pressure on the heads — it is a *structural* mechanism that mints distinct candidate rules by a non-gradient event, after which gradient/credit only *weights* them. This is ARC-063.

## Core idea: mint-then-weight, over a subspace-partitioned field

ARC-063 separates **creation** (a non-gradient, structural event that instantiates a new candidate rule) from **weighting** (gradient/credit that refines an existing rule's availability and embedding). MECH-309's "trainers weight rules they do not invent" becomes a literal architectural split.

```
                          ┌─────────────────── CandidateRuleField (NEW) ───────────────────┐
 context (z_world,        │  K slots, each = (rule_embedding, context_tag,                  │
   z_self, z_harm,        │                   availability a_k, eligibility e_k)            │
   SD-049 type)           │  subspace-partitioned: each rule a distinct direction          │
        │                 │  (Weber 2023) -- NOT competing scalar heads                     │
        ▼                 │                                                                 │
 ┌─ CREATE (mint) ─┐      │   ┌─ AVAILABILITY GATE (tolerance) ─┐   ┌─ SELECT (cue) ─┐       │
 │ bottom-up: a    │──────┼──►│ a_k clears a threshold that      │  │ current context │      │
 │ recurring       │ mint │   │ RISES with conflict / exceptions │  │ matched to      │      │
 │ (ctx→ao→outcome)│ slot │   │ (Cavanagh 2011, Frank 2006)      │  │ context_tag     │      │
 │ regularity      │      │   │ availability != selection        │  │ (Tulving;       │      │
 │ (ARC-064)       │      │   │ (Frank/O'Reilly 2001)            │  │ MECH-338)       │      │
 │ top-down:       │      │   └──────────────┬──────────────────┘  └────────┬───────┘       │
 │ ARC-062         │      │                  │ available ∧ context-matched rules            │
 │ discriminator   │      │                  ▼                                              │
 └─────────────────┘      │   DIFFERENTIATED rule_state = stack of active rule embeddings ──┼──► SD-033a
                          │   (resolves 598b: distinct vectors, not a collapsed scalar)     │   LateralPFCAnalog
                          │   CREDIT: outcome/PE updates a_k via eligibility e_k            │   .update(rule_state)
                          │   (Brzosko 2015 trace; Kovach 2012 recency)                     │   → bias_head → E3
                          └─────────────────────────────────────────────────────────────────┘
```

The architectural claim is that *differentiation is structural, not learned*: distinct rules exist because they were minted as distinct slots, occupying distinct subspace directions, so the rule_state handed to SD-033a is differentiated by construction — exactly what 598b found missing.

## The CandidateRule unit

Each of the field's `K` slots holds:
- `rule_embedding` — a vector in a rule latent space (dim `rule_dim`), the "what": the action-object bias / regularity the rule encodes. Minted from the context+action-object that generated it; refined by credit. Subspace-partitioned (Weber 2023) so rules stay separable.
- `context_tag` — the cue/state signature under which the rule was minted (z_world/z_self/z_harm summary + SD-049 type tag). The MECH-338 retrieval key.
- `availability a_k` ∈ [0,1] — accumulated support net of exceptions; the tolerance-gated quantity.
- `eligibility e_k` — a decaying trace marking the rule as creditable for recent outcomes (Brzosko/Yamaguchi).
- `minted_step`, `last_active_step` — bookkeeping for decay/retirement.

## The five faces

### 1. CREATE — the rule-creator (the GAP-B blocker; element: "in" face)
The non-Bayesian creator mints a new slot on a *structural* event, not by gradient:
- **Bottom-up (ARC-064, primary V3 source):** a regularity detector watches the `(context → action-object → outcome)` stream; when a regularity recurs above a detection threshold (and no existing rule's context_tag already covers it), it MINTS a new CandidateRule with that context_tag and an action-object-biased embedding. Grounded by Lee & Lee 2026 (subiculum forms behavioural-pattern schemas → mPFC rule-guided action) and the arc_064 review.
- **Top-down (ARC-062, secondary V3 source):** the existing gated-policy discriminator output seeds a candidate — now *feeding the field* rather than being the whole mechanism (this is why ARC-062 alone collapsed: it had no field to populate and no minting event, only two heads to train).

Minting is a discrete, non-gradient instantiation. This is the literal form of "trainers weight rules they do not invent": the creator invents (mints) slots; credit only weights them. **This is the single load-bearing fix for the 543/598b collapse.**

### 2. REPRESENT — subspace-partitioned field (element i; Wallis 2001, Weber 2023)
Rules are explicit, abstract representations (Wallis: PFC neurons encode abstract rules). The field holds them as a *population of distinct subspace directions* (Weber: mixed-selective subspace partitioning lets multiple codes coexist without interference). This is the architectural answer to *why two scalar heads collapsed but a field will not*: separability is structural (distinct minted directions), not an equilibrium the gradient must find.

### 3. GATE — tolerance-gated availability (element ii; Cavanagh 2011, Frank 2006, Frank/O'Reilly 2001)
A rule becomes AVAILABLE (eligible to bias E3 / enter the active rule_state) only when its `availability a_k` clears a threshold `θ` that **rises with conflict** — the number of competing context-matched rules and the accumulated exceptions. This is the "hold your horses" dynamic threshold (Frank 2006), frontally-set and BG/STN-implemented (Cavanagh 2011). Critically, AVAILABILITY (which rules enter the active set) is distinct from SELECTION/EXPRESSION (which action E3 picks among available rules' biases) — the Frank/O'Reilly 2001 BG-gates-WM-updating split. The gate keeps under-supported rules out of rule_state, so the agent samples before committing a rule.

### 4. SELECT — cue-driven context-bound retrieval (MECH-338; Tulving, Godden & Baddeley — GAP-L lit)
The current context is matched against each rule's `context_tag`; matching rules have their availability gate eased (context-dependent retrieval). This is the same context-cue retrieval motif as the SD-057 cue-recall bridge (a perceived cue retrieves a stored token) — ARC-063 retrieves a stored *rule* by context. Only context-matched, available rules enter rule_state.

### 5. OUTPUT + CREDIT — differentiated rule_state into SD-033a (resolves GAP-B; element iv)
The active set (available ∧ context-matched rules) is stacked into a **differentiated rule_state** — distinct subspace-partitioned vectors — and written into `LateralPFCAnalog.update(rule_state=...)`, then SD-033a's bias_head → E3 score_bias. This is exactly the "differentiated rule_state inputs to SD-033a" that 598b found collapse without a creator. **CREDIT (V3-minimal):** each rule active when an action was taken leaves an eligibility trace `e_k`; the subsequent outcome/PE updates `a_k` (raise on success, lower on exception), recency-weighted (Kovach 2012), via the Brzosko/Yamaguchi retroactive-eligibility mechanism. Rules whose availability decays below a floor are retired (dual-trace-preserved if the ghost-goal/anchor substrate is on).

## V3-tractable scope vs deferred

**In v1 (this design):** CREATE (bottom-up regularity-mint + top-down ARC-062 seed), REPRESENT (subspace field), GATE (tolerance availability), SELECT (cue/context retrieval), OUTPUT (differentiated rule_state → SD-033a), minimal CREDIT (eligibility-trace availability update). Reuses existing latents (no new trained encoder).

**Deferred to a V3 follow-on within ARC-063 (NOT in v1, but V3-tractable — not V4):**
- **Sleep-vs-waking refinement asymmetry** (element v) — **V3, not V4.** Sleep is V3 (rescoped from V4 on 2026-04-20; V4 is social-only), and the sleep cluster it needs is already implemented (MECH-272 routing gate, MECH-273 self-model writeback, MECH-285 replay sampler, SD-017 passes). The asymmetry is: waking does lightweight rule operations (mint / split / merge / availability credit — the v1 core); sleep does heavyweight rule-field operations (compress redundant rules, renormalise availability, consolidate/contextualise). This is a V3 follow-on (a `CandidateRuleField` sleep-pass invoked from the sleep loop), deferred out of the v1 core only to bound the first landing — NOT deferred to V4. MECH-094 applies (sleep writes carry the hypothesis-tag/mode-gate convention).
- **Full per-action evidence-trace records + moral-residue attribution** — v1 keeps only the eligibility→availability credit loop; the richer evidence record (rollouts generated/suppressed, harm, moral residue) and rule-field-level moral-residue attribution are a later phase (the moral-residue face is tied to the V4 strong-reading elaboration; the evidence-record enrichment itself is V3-tractable).
- **Learned affordance/identity embedding** for rule_embedding — v1 mints from existing z_world/z_self/z_resource + action-object; a learned rule encoder (which would need phased training) is the upgrade path.

**Genuinely V4-deferred (hard substrate gap):**
- **Social "in" face** (ARC-077/MECH-337) — requires a caregiver/teacher-agent substrate that does not exist in V3 (single-agent). Hard-gated; this is the only ARC-063 face that is V4 by substrate necessity rather than landing-order convenience.

## Config (all no-op defaults; bit-identical OFF)

| Param | Type | Default | Purpose | Class |
|---|---|---|---|---|
| `use_candidate_rule_field` | bool | False | master switch | REEConfig |
| `crf_n_slots` | int | 16 | K candidate-rule slots | CandidateRuleFieldConfig |
| `crf_rule_dim` | int | 16 | rule_embedding dim (matches SD-033a rule_dim) | " |
| `crf_mint_recurrence_threshold` | int | 3 | bottom-up: regularity recurrences before minting | " |
| `crf_tolerance_floor` | float | 0.3 | base availability threshold θ₀ | " |
| `crf_tolerance_conflict_gain` | float | 1.0 | how much θ rises per competing matched rule (Frank 2006) | " |
| `crf_availability_alpha` | float | 0.1 | credit EMA rate on a_k | " |
| `crf_availability_decay` | float | 0.005 | slow availability decay between activations | " |
| `crf_eligibility_window` | int | 20 | eligibility-trace steps (recency credit) | " |
| `crf_context_match_threshold` | float | 0.5 | cue→context_tag match floor for retrieval | " |
| `crf_seed_from_arc062` | bool | True | top-down population from the ARC-062 discriminator | " |

With `use_candidate_rule_field=False`, SD-033a's rule_state is sourced exactly as today (legacy), bit-identical.

## Insertion points (for the later implementation pass)

- **New module:** `ree_core/policy/candidate_rule_field.py` — `CandidateRuleField` + `CandidateRule` + `CandidateRuleFieldConfig` (pure-arithmetic + small buffers; no trained params in v1 → no phased training).
- **Bottom-up creator:** a regularity detector reading the `(context, action-object, outcome)` stream — can reuse the MECH-288 event-segmenter boundaries + the ResidueField / SD-049 type tags as the context signature.
- **`ree_core/pfc/lateral_pfc_analog.py` (SD-033a):** `update()` gains an optional `rule_state` source from the field (the differentiated stack) when `use_candidate_rule_field` — this is the GAP-B wiring.
- **`ree_core/agent.py`:** `sense()`/`select_action()` tick the field (mint on detected regularities, gate availability, match context cues, write rule_state, credit on outcome). Reuse the SD-057 cue-recall context-perception helper for the SELECT face.
- **`ree_core/utils/config.py`:** surface the flags.

## Proposed claim spine (PROPOSALS — NOT registered; register on implementation)
- **MECH-CRF-mint** (the non-Bayesian creator: regularity-detected minting of candidate-rule slots; bottom-up ARC-064 + top-down ARC-062 feed). The literal MECH-309 answer.
- **MECH-CRF-field** (subspace-partitioned distributed representation of K candidate rules; the anti-monomodal geometry — Weber/Wallis).
- **MECH-CRF-tolerance** (conflict-scaled dynamic availability gate; availability≠selection — Cavanagh/Frank).
- **MECH-CRF-credit** (eligibility-trace, recency-weighted availability update — Brzosko/Yamaguchi/Kovach).
- MECH-338 (cue-driven context-bound retrieval — already registered) is the SELECT face.
(L6 cue-recall / SD-057 is the affective-token analog; this is its rule-field sibling.)

## Validation (the falsifier the implementation must pass)

The failure record defines success. The substrate must **break the 543l/598b monomodal collapse**:
- **C1 (differentiated rule_state):** with the field ON, SD-033a receives a rule_state with ≥2 distinct active rule vectors (subspace separation above a floor) on ≥2/3 seeds — directly inverting 598b's C3 FAIL (`trainable_not_monomodal`).
- **C2 (minting fires):** the bottom-up creator mints ≥2 distinct context-tagged rules over a foraging/reef episode (a regularity-detected, non-gradient event).
- **C3 (tolerance gate works):** under-supported / high-conflict rules are held out of rule_state (availability < θ); the gate is conflict-sensitive (θ rises with competing matched rules).
- **C4 (downstream behavioural diversity):** the ARC-062 GAP-B falsifier (the multi-signature refuge/forage diversity criteria) re-run on the field-populated substrate produces ≥2/4 criteria — the behavioural pay-off that the rule-creator-absent substrate could not deliver.
Validation experiment queued via `/queue-experiment` after implementation; `experiment_purpose=diagnostic` for C1–C3 (substrate readiness), and the C4 ARC-062 falsifier re-run is the governance-weighting test for MECH-309/ARC-062.

## MECH-094 + phased training
v1 is pure-arithmetic + buffers (no trained parameters) → **no phased training**. The minting/credit/gate operations run on the waking stream; the field is ticked from `sense()`/`select_action()` (waking), so MECH-094 applies by call-site scoping (replay/simulation paths must not mint or credit — the field's tick carries a `simulation_mode` no-op guard, matching the SD-057 / regulator pattern). The learned-rule-embedding upgrade WOULD need P0/P1/P2.

## Open design questions (for the implementation session)
- **A1:** mint trigger granularity — per MECH-288 boundary event vs per recurring (context,action-object) tuple? (Lean: tuple-recurrence, with boundary events as context_tag delimiters.)
- **A2:** rule_embedding subspace allocation — fixed orthogonal init per slot vs learned-but-pinned (cf. ARC-062 differential-heads norm-pin that prevented collapse)? (Lean: pinned-distinct init, the Weber separability lesson.)
- **A3:** does tolerance gate availability OR rollout-eligibility (hippocampal preplay, element iii) OR both? (element iii hippocampal-rollout-eligibility is grounded but deferred to a v2 — v1 gates rule_state availability only; flag for the design session.)
- **A4:** retirement vs dual-trace preservation — reuse the MECH-292 ghost-anchor dual-trace for retired rules?

## Related claims
ARC-063 (this), MECH-309 (logical necessity — the creator is its answer), ARC-062 (weak-reading top-down source; exhausted alone), ARC-064 (bottom-up source), MECH-318 (rule_state abstraction; retire-vs-promote gate downstream), SD-033a (rule_state consumer — GAP-B target), MECH-338 (SELECT face), ARC-077/MECH-337 (social in-face, deferred), SD-057/MECH-347 (affective cue-recall sibling — same retrieval-by-context motif), MECH-288 (context boundaries), MECH-269/MECH-292 (anchor/rollout substrate), MECH-094 (call-site scoping).

## Amend — cross-episode rule persistence (V3-EXQ-654 GAP-B maturity, 2026-06-09)

**Status:** IMPLEMENTED 2026-06-09 (ree-v3 main). Routed by the confirmed `failure_autopsy_V3-EXQ-654_2026-06-09` (applied in the 2026-06-09 governance cycle; `substrate_queue.json` ARC-062 amend).

**Problem (discovered prerequisite, not a falsification).** The V3-EXQ-654 ARC-062 GAP-B behavioural falsifier (MECH-309/ARC-062) FAILed its **C1c readiness precondition** (`arm_on_rule_field_differentiated`) before its C2 falsifier DV could run: `agent.reset() → candidate_rule_field.reset()` (`agent.py:1908`) wiped `self._rules` + `self._recurrence` **every ~26-tick episode**, so the live pool cold-started each episode and never matured a differentiated rule pool (`crf_frac_active` 0.116/0.123/0.115 < 0.30 floor; `crf_max_pairwise_rule_dist` 0.0 all ARM_ON seeds; seed-42 ARM_ON committed-class byte-identical to ARM_OFF). The recurrence-threshold mint (≥3 within **one** episode) plus the per-episode wipe starve the pool at behavioural-runtime episode lengths despite cumulative `crf_n_minted` 131–408. Biology accumulates task-set rule structure **across** experiences and is **not** reset per trial (Collins & Frank 2014; Mansouri rule-selective persistence) — the per-episode wipe is a translation failure. V3-EXQ-639 PASS proves the field differentiates when its pool matures (this is design question **A4**'s near neighbour: the field must outlive the episode boundary).

**Fix (no-op-default; bit-identical OFF).** A new flag `persist_rules_across_episode_reset` on `CandidateRuleFieldConfig` (default `False`), surfaced as `REEConfig.crf_persist_rules_across_episode_reset` + `from_dims` passthrough and forwarded into the field config at the `agent.py` build site. When set, `CandidateRuleField.reset()` is a **no-op** — the live rule pool (`_rules`), recurrence counters (`_recurrence`), and the clock (`_step`, kept monotonic so `minted_step`/`last_active_step` stay ordered) **persist** across the per-episode `agent.reset()`. The `agent.reset()` call itself is unchanged; only the field's `reset()` semantics change. Default OFF reproduces the legacy per-episode wipe exactly (the credit/eligibility/decay math uses no step deltas, so a continuous clock is dynamics-neutral).

**Validation.** Substrate-level: contracts C9 (default-OFF bit-identical wipe), C10 (pool survives `reset()` + keeps maturing), C11 (`from_dims` + agent wiring) — 11/11 CRF contracts + 7/7 preflight PASS; full suite 959 pass (one pre-existing `control_vector` C4 flake, unrelated). The behavioural validation is **V3-EXQ-654a** (separate `/queue-experiment`, gated on this amend): single-variable ARM_OFF (`use_candidate_rule_field=False`) vs ARM_ON (differentiated `crf_source` with `crf_persist_rules_across_episode_reset=True`) GAP-B falsifier with a **trained-bias-head P1 arm** (GAP-D `rule_bias_head` trainability, landed 2026-05-17) + a **propagation non-vacuity precondition** (ARM_ON `lateral_pfc` bias must differ from ARM_OFF on firing ticks); committed-class entropy stays the PRIMARY DV. MECH-309/ARC-062 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate — **not** weakened; `claims.yaml`/governance untouched (substrate-only amend).

## Amend — mature-pool gate/credit/retire dynamics (V3-EXQ-654b GAP-B maturity, 2026-06-11)

**Status:** IMPLEMENTED 2026-06-11 (ree-v3 main). Routed by the confirmed `failure_autopsy_V3-EXQ-654b_2026-06-11` (the ARC-062 `substrate_queue.json` `recommended_substrate_queue_entry` hand-off; `amend_target_impl = ARC-063 CandidateRuleField`).

**Problem (the budget reading is exhausted).** The cross-episode persistence amend (2026-06-09) preserves the pool *across* episode boundaries but does nothing about *within-run churn*. V3-EXQ-654 (per-episode wipe), 654a (`crf_persist`), and 654b (`crf_persist` + a 2.4× longer 240-ep window) leave `crf_frac_active` **pinned at ~0.12–0.14** and `crf_max_pairwise_rule_dist` **exactly 0.0** every ARM_ON cell — the field never holds **≥2 rules present** despite 452–1014 cumulative mints. More budget and persistence move the maturation metric by nothing, so the blocker is the **GATE/CREDIT/RETIRE dynamics**, not budget. Three drivers (autopsy §Mechanism):
1. **Retire-churn (primary).** `availability_decay` (0.005) + negative-outcome credit drive availability below `_retire_floor` (0.5·`tolerance_floor` = 0.15) before a 2nd differentiated rule co-accumulates.
2. **Mint-block under collapsed context (secondary).** `context_match_threshold` (0.5) lets one rule "cover" the low-spread z_world context space and suppress differentiated mints; the CRF reads raw z_world, so the ARC-065 GAP-A fix that re-diversified the other bias channels does not reach it.
3. **Conflict-gate deadlock (latent).** `tolerance_floor` (0.3) + `tolerance_conflict_gain` (1.0) give θ ≥ 1.3 > 1.0 max availability whenever ≥2 rules match a context, so **≥2 matched rules can never both be active** — it bites the moment the pool fills.

**Fix (no-op-default; bit-identical OFF; new behaviour behind two flags).**

- **`crf_mature_pool_dynamics`** (`CandidateRuleFieldConfig.mature_pool_dynamics`, default `False`) routes a bundle of recalibrated knobs, all consulted *only* under the master flag (so OFF is bit-identical): conflict-gate pair `mature_tolerance_floor` 0.15 / `mature_tolerance_conflict_gain` 0.25 → θ(1)=0.40, θ(2)=0.65, θ(3)=0.90, all < 1.0 max availability (the deadlock fix); `mature_availability_decay` 0.001 (5× slower passive decay); `mature_retire_floor` 0.05 (absolute floor, decoupled from `tolerance_floor`); `mature_availability_alpha_negative` 0.02 (asymmetric — negative outcomes erode availability gently); `mature_mint_protection_ticks` 30 (a freshly minted rule is retirement-protected so a 2nd differentiated rule has time to co-accumulate — the direct "rule drops below floor before a 2nd co-accumulates" fix); `mature_mint_block_threshold` 0.8 (decoupled from the 0.5 retrieval threshold — a new differentiated mint is blocked only by a *very* similar existing rule).
- **`crf_context_from_e2_world_forward`** (`REEConfig`, default `False`) sources the CRF mint/match context from `e2.world_forward(z_world, prev_action_onehot)` (action-regime-separated, `no_grad`, falling back to raw z_world when prev-action is unset) instead of raw z_world — mirroring the ARC-065 GAP-A re-sourcing so the mint-block does not collapse under low raw-z_world spread. MECH-094 not implicated (waking read on a detached latent).

**CRF-readiness gate readout.** `get_state()` now emits `crf_frac_active` (fraction of ticks with ≥1 active rule) alongside `crf_max_pairwise_rule_dist`. The Step-8 readiness diagnostic asserts `crf_max_pairwise_rule_dist > floor AND crf_frac_active >= 0.30` — the gate that MUST clear before any GAP-B behavioural falsifier (654c successor) is scored.

**Validation.** Substrate-level: contracts C12 (mature default-OFF bit-identical + `crf_frac_active` readout), C13 (conflict-gate admits ≥2 matched rules — legacy θ=1.3 deadlocks, mature θ=0.40 admits both), C14 (the 654b inversion: legacy reproduces `crf_max_pairwise_rule_dist`=0.0 / 1 rule present / READY=False at the collapsed-z_world cos-0.7 regime, mature → ≥2 differentiated co-present rules / READY=True), C15 (mint-youth protection survives a below-floor fresh rule + asymmetric negative credit is gentler), C16 (`from_dims` + agent wiring of both flags, e2-context path executes) — **16/16 CRF contracts + 7/7 preflight PASS; full suite 1004 pass + 1 pre-existing `control_vector` C4 flake (confirmed failing on a clean tree, unrelated).** Activation smoke (two regimes at cos 0.7, frequent hazard negatives): legacy `n_present=1 / max_pairwise_dist=0.0 / READY=False` (the 654b signature) → mature `n_present=2 / max_pairwise_dist=1.49 / frac_active~0.99 / READY=True`. The CRF-readiness validation EXQ (claim-free diagnostic, mature + e2-context arms vs OFF, asserts the readiness gate) is the Step-8 follow-on; the 654c GAP-B behavioural re-run is a SEPARATE later `/queue-experiment` session gated on that readiness PASS. MECH-309/ARC-062/ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate — **not** weakened; `claims.yaml`/governance untouched (substrate-only amend).
