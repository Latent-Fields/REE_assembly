# Claim Synthesis -- ARC-065 GAP-A channel -> committed-action CONVERSION cluster

**Generated:** 2026-06-16T19:58:00Z
**Skill:** /claim-synthesis (proposal-first; nothing lands in claims.yaml without per-child user approval)
**Nominated cluster (direct):** ARC-065 GAP-A channel->committed-action conversion
**Trigger:** `failure_autopsy_V3-EXQ-569h_2026-06-16` Section 7 + 9 (user-confirmed 2026-06-16: "Amend + surface /claim-synthesis"), the 7th autopsy in the lineage and the 1st FAIL *after* the conversion config was identified (V3-EXQ-684a PASS).
**Status:** RESOLVED 2026-06-17 -- **RETIRED UNREGISTERED (correct refusal).** V3-EXQ-569i LANDED **PASS**/supports (committed-action entropy C_R1B strict-above BOTH matched-noise AND proposer, non-degenerate; governance cycle 2026-06-17, user-adjudicated). Per this doc's own pre-registered rubric (Section 6 / the bullet below: "If V3-EXQ-569i PASSes ... this child is not registered"), the conversion CLOSED -- it was substrate iteration, not claim-granularity debt. The proposed finer committed-diversity-GAIN child is **NOT registered** (the anti-proliferation rail's correct-refusal branch). ARC-065 substrate_ceiling LIFTED -> standard, pending_retest cleared. No claims.yaml / claims.json edit performed (proposal retired). [Prior state: PROPOSAL -- HELD pending V3-EXQ-569i, user-adjudicated 2026-06-16, see Section 6.]

> **DECISION (2026-06-16, user via AskUserQuestion): HOLD registration until V3-EXQ-569i (top_k shortlist conversion falsifier) returns.** The cluster cleared the granularity-debt bar (borderline; Section 2.1), but the last untested conversion architecture (top_k within-shortlist arbitration) is being queued now and is genuinely discriminating. Per the user's own framing -- "the amend discriminates the two readings: PASS = iteration closed, FAIL = granularity-debt confirmed" -- we let 569i resolve first.
> - **If V3-EXQ-569i PASSes** (committed entropy strict-above BOTH controls >= 2/3, proposer-already-diverse regime): the conversion closed -- it WAS substrate iteration after all; this child is **not** registered (the proposal is retired as a correct refusal).
> - **If V3-EXQ-569i FAILs** (third conversion architecture, after global-rescale @ 569h 1/3 and margin-shortlist @ 684 0/3): the granularity-debt reading is confirmed -- **re-run /claim-synthesis to register the Section 5.2 child** (this doc preserves the full decomposition; registration is then cheap).
> Resume primitive: watch V3-EXQ-569i in the coordinator DB / `pending_review.md`; route its review back here.

---

## 1. The cluster (Steps 1-2)

Seven autopsies circle one surface -- whether an upstream representational distinction that ARC-065's diversity pathway generates reaches and diversifies the **committed action**:

| # | Run(s) | Date | Self-route / verdict | Link in the chain |
|---|---|---|---|---|
| 1 | 569c | 05-30 | C1 calibration-miss FAIL, C3 +2.4x over matched-noise -> **supports** | floor set against wrong (training-only) magnitude |
| 2 | 569e | 05-31 | INSTRUMENTATION_FAILURE (E2 multi-step rollout overflow 1e16+) | SD-056 iterated-rollout numerical instability |
| 3 | 614e | 06-07 | candidate-pool collapse pre-fix | all K candidates -> identical z_world; class-uniform pool |
| 4 | 643 | 06-06 | dead gate (`active_frac=0.0`) | float32 catastrophic cancellation (scores ~1e32) |
| 5 | 569f / 661 / 654a | 06-10 | range present, readout bit-identical -> **non_contributory** (cluster) | range exists in representation but **un-routed** to the modulatory bias |
| 6 | 569g | 06-14 | REACH solved (route 0.18, 3/3), CONVERSION fails 1/3 | additive authority @ gain 0.5 subdominant to F-dominated primary |
| 7 | **569h** | 06-16 | REACH amplified (0.31, 3/3) on the 684a gain=2.0 config, CONVERSION fails 1/3 | **SHIFT, not GAIN** -- wins only the collapse seed |

Corroborating substrate-side data (not autopsies, but same surface): **V3-EXQ-684** ran the *margin* shortlist-then-modulate variant -> converted **0/3** (committed entropy 0.337 < proposer 0.549; the margin cutoff admitted ~7/8 candidates = a near-whole state-stable set whose argmin collapsed to the channel's global favourite).

---

## 2. Discrimination gate (Step 3 -- the load-bearing filter)

Classify each FAIL; only the residue is granularity debt.

**EXCLUDED (the other three causes -- the metabolized links):**

- **569c** -> became **supports** (calibration miss; floor recalibrated 0.05->0.03 in 569d PASS). Not a FAIL signature.
- **569e** -> **implementation pathology** (numerical instability), amended via /implement-substrate. Not granularity debt.
- **614e, 643** -> **substrate-not-ready** (candidate-pool collapse; float32 cancellation dead-gate). Each was a distinct broken link subsequently fixed. Enrichment, not a missing claim.
- **654a** -> **precondition-unmet** (`substrate_not_ready_requeue`; CRF maturation `frac_active 0.137 < 0.30`). Correctly never scored as a falsifier.
- **569f / 661** -> genuine non-degenerate negatives, but the diagnosed cause (range present but **un-routed**) was **solved** by the route-range amend (569g/569h preconditions held 3/3). Metabolized.

**SURVIVING -- genuine, non-degenerate, substrate-ready FAIL signatures circling ARC-065 GAP-A conversion:**

1. **569g** -- REACH solved (in-arm route_range 0.18, 3/3 seeds, mechanism active in the scored arm), CONVERSION fails (committed entropy strict-above controls 1/3). `non_degenerate=true`. Signature: *additive authority at gain 0.5 is subdominant to the F-dominated primary (F = 88-89% of E3 score variance, V3-EXQ-571)*.
2. **569h** -- REACH amplified (route_range 0.31, 3/3) on the **684a-identified** gain=2.0 std-basis config, CONVERSION still fails 1/3. `non_degenerate=true`; both non-vacuity preconditions held 3/3. Signature: *even at the identified gain, the config delivers a committed-argmax SHIFT (beats legacy, 684a) but no diversity GAIN over an already-diverse proposer -- it rescues only the collapse seed (43)*.
3. (corroborating, substrate-side) **684 margin-shortlist** -- a *third distinct* conversion architecture (within-shortlist arbitration, margin variant) converting **0/3**.

These are **structurally distinct** signatures (additive-subdominant -> shift-not-gain -> shortlist-collapse-to-global-favourite), all non-degenerate, all substrate-ready (the mechanism was active where the DV was scored), all circling the **same** claim. **>= 2 distinct genuine non-degenerate substrate-ready signatures -> the cluster CLEARS the granularity-debt bar.**

### 2.1 The honest caveat (why this is borderline, and why 569g said the opposite)

This gate-clear is **borderline and deliberately user-pre-authorized**, for three reasons the skill requires me to surface:

- **The machine-readable exclude fires.** ARC-065 carries `epistemic_category: substrate_ceiling` -- the auto-detector's cheap first-pass EXCLUDE signal ("substrate too coarse / enrichment-in-progress, not undetected granularity debt"). It *also* fires every backstop exclude: registered children (MECH-313/314a-c), a recent `modulatory-bias-selection-authority` substrate_queue amend (2026-06-16), and an in-progress closure GAP (`behavioral_diversity_isolation:GAP-A`) that owns the cluster. On an **auto-detected** worklist ARC-065 would be excluded as already-metabolized. This is a **direct nomination** from a confirmed autopsy, which is the only reason it is on the table.
- **569g explicitly adjudicated "substrate iteration, NOT granularity debt"** -- "ARC-065 is one architectural commitment; each amend fixed the next isolated link." That reading was correct *through* 569g.
- **What re-opens it (569h's specific contribution):** 569h is the **first FAIL after the conversion config was identified** (684a PASS, `conversion_mechanism_identified`). The substrate-iteration thesis made a falsifiable prediction -- *once the conversion config is identified and armed, the properly-armed falsifier clears*. It did not. And the failure signature **evolved** (REACH-solved -> SHIFT-not-GAIN) rather than repeating. Two of three conversion architectures have now failed post-identification (gain-rescale @ 569h 1/3; margin-shortlist @ 684 0/3). A coarse claim whose substrate enrichment keeps moving the gap down one link without ever closing it -- now even past *identification* -- is the granularity-debt fingerprint: ARC-065's broad "diversity-generation pathway" commitment **does not name** the finer mechanism that keeps failing.

**Conclusion:** PROCEED to a single, narrowly-scoped child, but as a **proposal the user adjudicates against the still-pending top_k falsifier** (Section 6). This is not a demotion and not premature proliferation -- the child is born testable and its first falsifier (V3-EXQ-569i) is already being built.

---

## 3. The common thread (Step 4)

> Every surviving failure shares this: the modulatory selection authority can **reach** the committed-action argmax and **shift** it, but cannot convert that reach into a committed-action **diversity GAIN over an already-diverse proposer**, because it operates as a gain-rescaled additive/normalized bias on the **global** argmax against an F-dominated primary (F = 88-89% of E3 score variance).

ARC-065 asserts diversity **generation** (a source exists). The route-range substrate solved **reach** (the source gets to the authority). Neither names the **conversion** function -- turning reached range into committed-action diversity -- as a *separable* mechanism with its own gating variable (F-dominance) and its own required architecture (within-shortlist arbitration, not global-argmax rescaling). That is the missing chunk of cognition the registry has not named.

---

## 4. Lit grounding (Step 5)

**No new /lit-pull commissioned** (consistent with the 569g and 569h biological triages, both user-confirmed). Rationale:

- **Not a formal-definition import.** The conversion coupling is an engineering instantiation of a known biological dependency -- a BG-like / cortico-striatal committed-action selection gate applying DA-modulated **gain/contrast** to convert small representational differences into a discrete choice, competing against a forward-model-dominated primary value. The "biology before formal definitions" rule (Pearl/Shannon/control-theory imports) does not bite here.
- **Generation side already grounded:** `evidence/literature/targeted_review_arc_065_behavioral_diversity_generation` (LC-NE tonic, frontopolar curiosity, striatal novelty, hippocampal trajectory sampling; R1 = both-channels-needed).
- **Conversion side is biology-consistent, not a divergence:** the failure shape (a selection gate's gain sub-dominant to a strong upstream sampler; the gate shifts choice at near-ties but cannot reweight the committed distribution toward diversity when the sampler is already diverse) **matches a missing-BG-dependency signature**. Within-shortlist (near-tie) arbitration is, in fact, *closer* to the basal ganglia's actual architecture (direct/indirect-pathway gating of a near-tie cortical competition) than the global-argmax additive rescale that has now failed twice -- so the proposed child is biology-*supported*, not a formal speculation.

If the user prefers belt-and-suspenders, the optional micro-pull would be **"basal-ganglia near-tie / within-shortlist action arbitration; gain-vs-structure in committed selection against a strong cortical prior"** -- but the autopsy position (engineering gap, not lit-adjudicable) is that it is not warranted. **Defaulting to no new pull.**

---

## 5. Proposed decomposition (Step 6)

### 5.1 ARC-065's fate: **retained-and-narrowed (umbrella)**

ARC-065 stays the architectural slot for diversity **GENERATION** (the source). It is **coarse, not wrong**: status **provisional**, `epistemic_category: substrate_ceiling`, `pending_retest_after_substrate: true` -- all **unchanged**. **No demotion.** The 569c/569f C1 PASSes (the source demonstrably exists) remain its positive evidence. The decomposition adds a child that names the **conversion** function ARC-065 currently leaves implicit at the GAP-A surface; ARC-065 becomes the umbrella over {generation (itself + MECH-313/314), conversion (new child)}. The **reach** function is *not* promoted to a claim -- it is solved and substrate-tracked (route-range amend); naming it would be proliferation.

### 5.2 Candidate child claim (ONE)

| Field | Value |
|---|---|
| **Proposed id** | next free MECH at registration time (check max + recent `git log`; ~MECH-360-range) |
| **claim_type** | `mechanism_hypothesis` |
| **subject** | `ethics_engine_3.committed_action_diversity_gain_via_within_shortlist_arbitration` |
| **status** | `candidate` |
| **epistemic_category** | `substrate_conditional` (the discriminating substrate -- within-shortlist/top-k arbitration -- is queued but not yet validated; keeps promote/demote suppressed until it lands) |
| **implementation_phase** | `v3` |
| **depends_on** | `[ARC-065, MECH-341]` (parent generation pathway; MECH-341 supplies the *preserved* scoring-layer diversity this mechanism must *convert*) |
| **polarity** | `asserts` |

**One-line claim:**
> Committed-action diversity **GAIN** over an already-diverse proposer is a mechanism **distinct** from diversity GENERATION (the ARC-065 source) and from channel REACH (route-range to the E3 selection authority). A gain-rescaled additive/normalized modulatory bias applied to the **global** argmax -- even at the V3-EXQ-684a-identified gain (2.0, std-basis) -- produces a committed-argmax **SHIFT** but no net diversity GAIN against an F-dominated primary (F = 88-89% of E3 score variance, V3-EXQ-571); converting reach into committed-action diversity requires **within-shortlist (near-tie) arbitration** -- F filters to a small rotating near-tie candidate set, the modulatory channel arbitrates *within* it -- so the structured channel is load-bearing without having to out-magnitude F.

**Draft `what_would_answer`:**
> A **within-shortlist arbitration** run (F filters to a near-tie / top-k set; the modulatory channel arbitrates within it) on the STD_G2 conversion substrate, in a 569-lineage matched-entropy falsifier with an in-arm route-range non-vacuity gate **and a verified-lifting noise control**: committed-action entropy strict-above **BOTH** a (diverse) proposer baseline AND the (lifting) matched-noise control on **>= 2/3 seeds, in the regime where the proposer is already diverse** (not only the collapse seed). **PASS** confirms within-shortlist arbitration converts reach into a committed-diversity GAIN -- the mechanism is real and global-argmax rescaling was the wrong instantiation. **FAIL across both global-rescale (exhausted: 684a/569h 1/3) and within-shortlist arbitration (684 margin 0/3; top_k V3-EXQ-569i pending)** confirms committed-action diversity GAIN is not achievable by the modulatory channel against an F-dominated primary at the current substrate granularity -- escalating to a deeper E3-primary rebalancing (reduce F dominance) or to V4.

**First falsifier already in flight:** **V3-EXQ-569i** (top_k shortlist conversion falsifier), being authored/queued now by the active `implement-substrate-gapa-shortlist-topk` session. The child is therefore born **on a test path**, not added to the untested believed tail. The 684 margin-shortlist 0/3 is already a data point against the naive variant.

**Cluster evidence motivating the child:** 569g (additive-subdominant, 1/3), 569h (shift-not-gain at identified gain, 1/3), 684 (margin-shortlist collapse, 0/3) -- three structurally distinct conversion architectures, none producing a GAIN.

### 5.3 Shared-child wiring (cross-reference)

The autopsy notes the conversion bottleneck is **shared** across channels; the child becomes their common downstream:

- **MECH-341** (E3 score-diversity preservation) -- *scoring-layer* preservation is established (ratified 2026-06-14); its committed-action **CONVERSION** (the 614e/660 byte-identical committed-class entropy) is exactly this child. Wire as upstream (`depends_on` includes MECH-341).
- **ARC-062 / MECH-309** (rule-field channel) -- same reach->commit conversion ceiling (654a/654b/654d). Add a `depends_on` / xref note so their GAP-B conversion failures bear on this child once their own substrate (CRF maturation) clears.
- **MECH-294** (theta co-binding coherence channel) -- same (661). Xref.

These are **cross-references, not new children** -- one shared conversion mechanism, named once.

### 5.4 What this proposal explicitly does NOT do

- No demotion or status change to ARC-065, MECH-341, ARC-062, MECH-309, MECH-294.
- No `claims.yaml` / `claims.json` edit until per-child user approval.
- No second child for "reach" (solved, substrate-tracked).
- No new lit-pull (Section 4).
- No touch to `behavioral_diversity_isolation_plan.md` / `substrate_queue.json` / `modulatory_bias_selection_authority.md` (held by the active top_k session).

---

## 6. The decision for the user (Step 7)

The cluster clears the granularity-debt bar, but the call is genuinely **borderline** (Section 2.1) and the child's first falsifier (V3-EXQ-569i, top_k) is being built **right now**. Two defensible paths:

- **(A) Register the child now** (`substrate_conditional`, wired under ARC-065, falsifier = 569i). Pro: names the recurring nameless mechanism before another round; the child is immediately on a test path (569i + the 684 margin 0/3 prior); makes ARC-065 a true umbrella. Con: if 569i (top_k) PASSes, the conversion closes and the child is shown almost immediately -- registering one cycle early.
- **(B) Hold registration until V3-EXQ-569i returns.** Pro: maximally conservative; lets the last untested conversion architecture discriminate first (the user's own 2026-06-16 framing -- "the amend discriminates the two readings -- PASS = iteration closed, FAIL = granularity-debt confirmed"). Con: if 569i FAILs, we re-run /claim-synthesis to land the same child a round later.

Both honour the discipline. Recommendation flagged in the response.

---

## 7. Hand-off

- On approval (path A): register the child into `claims.yaml` (`candidate` / `substrate_conditional`, with `what_would_answer` + `depends_on` + an architecture-doc stub), wire the ARC-065 umbrella + MECH-341/ARC-062/MECH-309/MECH-294 xrefs, run `python scripts/build_claims_json.py`, pathspec-commit, push `HEAD:master`.
- Either path: the child's test is V3-EXQ-569i (top_k), already in flight; this skill does not run it.
- WORKSPACE_STATE.md Recent Work line on close.
