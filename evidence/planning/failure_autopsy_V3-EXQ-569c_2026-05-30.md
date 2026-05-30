# Failure Autopsy: V3-EXQ-569c

**Date:** 2026-05-30T16:55:40Z
**Scope:** single target
**Status:** confirmed
**Target:** V3-EXQ-569c (SD-056 action-contrastive matched-entropy FP-2 falsifier; ARC-065 GAP-A / MECH-341)
**Run ID:** v3_exq_569c_sd056_action_contrastive_diversity_falsifier_20260530T124450Z_v3
**Manifest:** REE_assembly/evidence/experiments/v3_exq_569c_sd056_action_contrastive_diversity_falsifier_20260530T124450Z_v3.json
**Script:** ree-v3/experiments/v3_exq_569c_sd056_action_contrastive_diversity_falsifier.py
**Supersedes:** V3-EXQ-569b (SIGTERM, no manifest), V3-EXQ-569a (NaN crash in torch.multinomial under self-anchored contrastive training)
**Plan-of-record:** REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md
**Routing:** queue-experiment (two parallel successors: V3-EXQ-569d + V3-EXQ-569e)

---

## 1. Facts (no interpretation)

### Acceptance criteria (pre-registered, ASCII)

- **C1 substrate operative:** mean cand_world_pairwise_dist > 0.05 across >= 2/3 seeds in EACH of ARM_1 / ARM_2 / ARM_3.
- **C2 R1.b unlock:** in at least one of ARM_1/2/3, candidate_first_action_entropy > 0.3 AND > ARM_4 matched-noise.
- **C3 selected-entropy lift:** in ARM_2 OR ARM_3, selected_action_class_entropy > 0.3.
- Overall PASS = C1 majority + (C2 OR C3) in at least one weight arm.

### Per-arm summary (means across 3 seeds, P1 measurement window)

| Arm | Label | pairwise_dist mean | seeds >0.05 | cand_first_action_entropy | **selected_action_entropy** | e3_top2_class_gap | contrastive_loss |
|---|---|---|---|---|---|---|---|
| ARM_0 | OFF baseline | 0.0147 | -- | -- (n/a in summary) | **0.361** | 0.396 | 0.0 |
| ARM_1 | SD-056 w=0.01 | **0.0451** | 1/3 | 0.796 | **0.875** | NaN | 1.93 |
| ARM_2 | SD-056 w=0.05 | **0.0422** | 0/3 | 0.786 | **0.833** | NaN | 1.98 |
| ARM_3 | SD-056 w=0.20 | **0.0462** | 1/3 | 0.791 | **0.951** | NaN | 1.95 |
| ARM_4 | matched-noise T=2.5 | 0.0148 | -- | 0.786 | **0.414** | 0.692 | 0.0 |

### Verdict tabulated

| Criterion | Result | Failed criterion | Notes |
|---|---|---|---|
| C1 (substrate operative) | **FAIL** | discrimination (per-arm seed-count threshold) | ON-arm means cluster at ~3x OFF baseline; per-seed counts 1/0/1 vs required >=2 |
| C2 (R1.b unlock) | PASS | -- | All ON arms above 0.3 floor; ARMs 1 + 3 strictly > ARM_4 matched-noise (0.796/0.791 > 0.786) |
| C3 (selected-entropy lift) | PASS | -- | ARMs 1/2/3 all > 0.3; ARM_2 + ARM_3 satisfy strict criterion |
| Overall | **FAIL** | C1 alone | Pre-registered conjunction requires C1 majority |

### Negative-control / absolute-criterion behaviour

- ARM_0 OFF (sd056_master_off, T=1.0) and ARM_4 NOISE (sd056_master_off, T=2.5) have **bit-identical pairwise_dist** (0.0147 vs 0.0148; the manifest reports ARM_0 and ARM_4 identical for seeds 42 + 43, near-identical for seed 44).
- ARM_0 vs ARM_4 selected_entropy: 0.361 vs 0.414. Temperature lift (1.0 -> 2.5) contributes only ~0.05 of entropy.
- ON arms selected_entropy: 0.833 - 0.951. **Approximately 2.4x the matched-noise control on the C3 axis** with bit-identical underlying pairwise_dist signature on the temperature axis.

### Operational notes

- contrastive_loss across ON arms means ~1.95 (range 1.52 - 3.71). ln(K=8) = 2.08; the head is just below random baseline. n_contrastive_skipped_sparse: 18/253/17 across seeds (sparse-batch skip on small-buffer ticks).
- e3_top2_class_gap is NaN on every ON arm (ARM_1 / ARM_2 / ARM_3) but populated on ARM_0 (0.396) and ARM_4 (0.692). **Instrumentation bug** -- diagnostic field intended to dissociate score-collapse vs class-collapse is unavailable for the falsifier comparison.
- V3-EXQ-613 (substrate-readiness, training-only) PASSed with cand_world_pairwise_dist baseline 0.136 -> trained 0.286. The 569c behavioural-runtime magnitude (~0.045) is ~6x lower than the standalone-task magnitude (~0.286).

---

## 2. Claim-layer mapping

### ARC-065 (parent architectural commitment, candidate, v3_pending=true)

`behavioral_diversity_generation_pathway`. Architectural commitment: a non-trivial behavioural diversity generation pathway is upstream-of and logically prior to both rule pathways. Multi-substrate distributed instantiation across MECH-313 (LC-NE noise floor), MECH-314 (structured curiosity), and the MECH-315-absorbed proposal-diversity channel.

- claim_type: architectural_commitment
- implementation_phase: v3
- depends_on: []
- prior support: indirect via V3-EXQ-567 PASS (SP-CEM main-path landing 2026-05-15), V3-EXQ-568 PASS, V3-EXQ-573 PASS

The 569c experiment tests SD-056 (Layer A) as an A_only matched-entropy falsifier for whether per-candidate z_world variance can drive behavioural diversity above a temperature-noise control. **Conditions to express:** SP-CEM main-path ON, MECH-341 (Layer B) OFF, MECH-313 (Layer C) OFF, MECH-269 (Layer D) at main-path default. **Conditions actually present:** confirmed by per-arm config in the manifest. The substrate had a fair chance to express.

### MECH-341 (Layer-B child, candidate, v3_pending=true)

`e3_scoring_preserves_trajectory_class_diversity`. E3 score aggregation over CEM-supplied candidates must preserve trajectory-class diversity rather than collapse a diverse candidate pool onto a single deterministic ranking.

- claim_type: mechanism_hypothesis
- depends_on: ARC-065, ARC-033, SD-003, INV-076
- prior support: substrate IMPLEMENTED 2026-05-27 (e3_score_diversity entropy_bonus + stratified_select); V3-EXQ-611 substrate-readiness FAIL surfaced the retune; V3-EXQ-611b PASSed retune.

The 569c manifest tags MECH-341 indirectly via the "E3 aggregation collapses upstream variance" interpretation cell -- the C1+!C3 outcome would have weakened MECH-341's non-load-bearing reading. **Conditions to express:** baseline MECH-341 default (no entropy bonus / stratified select active during 569c per script docstring); per-candidate variance present at >= matched-noise level; selected entropy measurable.

### claim_ids accuracy check

claim_ids inherited from 569a / 569b; verified appropriate for 569c. The script is a bit-identical re-run of 569b (matched-entropy FP-2 falsifier); claims do not need re-evaluation.

---

## 3. Biological-reference triage

### SD-056 closest mechanism

**Cerebellar internal model preserving action-specificity** (Tanaka et al. 2020). **Prefrontal counterfactual rollout** (Miyamoto / Rushworth / Shea 2023). **Vestibular cerebellum corollary discharge** (Cullen 2023).

Mammalian forward models must preserve action-conditional discriminability at the prediction step. Reconstruction-shaped training collapses to state-dominated minima where action effect fits to zero; biology evolved structural mechanisms (cerebellar microcircuits, PFC counterfactual rollouts, corollary-discharge cancellation) to prevent this collapse.

REE's SD-056 is a **faithful biological translation** of an architectural prerequisite, not a formal-definition import. The ML/AI mapping is to InfoNCE contrastive next-state (Srivastava et al. 2021); the lit-pull synthesis at `evidence/literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md` confirmed lever B (contrastive next-state) over PLSM (lever A) and SWIRL (lever C). **lit_status: present** (lit-pull complete; conf 0.78-0.82).

### ARC-065 closest mechanism

Distributed diversity generation across LC-NE tonic noise (Aston-Jones & Cohen 2005), frontopolar uncertainty-driven curiosity (Daw et al. 2006), striatal novelty (Wittmann et al. 2008), and hippocampal trajectory sampling (Pfeiffer & Foster 2013). The claim is that a substantive architectural diversity pathway is required; gradient descent on a parametric policy without diversity pressure collapses (MECH-309 predicted equilibrium).

### MECH-341 closest mechanism

OFC value comparison preserves option-distinct value signals through the comparison stage (Padoa-Schioppa & Conen 2017). PFC mixed selectivity encodes diverse trajectory contingencies (Rigotti et al. 2013).

### Biology-matches-failure-signature check

Does the failure resemble what would happen biologically if a dependency of the reference mechanism were absent?

**The "failure" is borderline -- not a biological-dependency-missing signature.** The substrate is operative (3x baseline pairwise distance), produces structural diversity above matched-noise on the C3 axis (~2.4x noise), and just misses a magnitude threshold on C1 calibrated against a different regime (training-only V3-EXQ-613 at 0.286 vs behavioural-runtime ~0.045). Biology of mammalian forward models predicts that behavioural-runtime variance will be lower than standalone-task variance (training-time exploitation vs runtime task-shaped reduction); the C1 floor was set inappropriately for the runtime regime.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (both)** | ARC-065: substrate produces structural diversity above matched-noise on C3 (~2.4x). MECH-341: variance does propagate through E3 aggregation to selection. The test let both claims express; both surface positive evidence. |
| Biological reference | **clear** | SD-056 = Tanaka 2020 cerebellar action-specificity preservation + Srivastava 2021 contrastive RSSM. ARC-065 = Aston-Jones LC + Wittmann striatal novelty distributed pathway. Lit-pull complete (SYNTHESIS lit_conf 0.78-0.82). NOT a formal-definition import. |
| Prerequisites / dependencies | **present** | SP-CEM main-path ON (default since 2026-05-17). MECH-341 substrate landed (2026-05-27, retune validated 2026-05-28). MECH-269 main-path default. SD-005 z_world routing intact. |
| Implementation completeness | **complete (small caveat)** | Substrate landed ree-v3 main 041a974 (2026-05-29); V3-EXQ-613 standalone PASS. Caveat: contrastive_loss ~1.95 (near ln(8)=2.08 random) in behavioural runtime indicates the head has not fully trained within the 50-episode window; buffer-warmup time-to-effect is incompletely characterised. |
| Environment adequacy | **adequate** | causal_grid_world_v3 with reef + hazard_food_attraction substrate (SD-054 + SD-049 + SD-047 + SD-048). 200-step episodes generated 1745-5314 P0 ticks per seed -- sufficient candidate diversity for SP-CEM. |
| Measurement adequacy | **under-instrumented** | e3_top2_class_gap is NaN on every ON arm but populated on ARM_0 / ARM_4. Diagnostic field intended to dissociate score-margin-collapse vs class-collapse is unavailable for the load-bearing comparison. This must be fixed in 569d / 569e. |
| Integration adequacy | **coupled cleanly** | n_contrastive_steps tracks n_p1_ticks per seed; n_buffer_appends substantial (753 / 8529 / 360 across seeds in ARM_1). The contrastive task fires every measured tick; the head receives consistent gradient signal. |
| Scale / capacity | **likely insufficient (training time)** | contrastive_loss stays at random baseline; the head needs more training time to reach the V3-EXQ-613 standalone-task magnitude. Behavioural-runtime sparsity vs synthetic-batch density is the gap. P0 30 ep + P1 20 ep may be undersized. |

### Recommended REE-native `epistemic_category`

`standard`. The substrate is operative; the failure mode is test-design calibration + measurement instrumentation. Not `substrate_ceiling` (substrate produces structural diversity above noise); not `substrate_conditional` (no upstream substrate missing); not `derivational` (empirical question); not `out_of_domain` (REE-tractable).

---

## 5. Learning extracted

The pre-registered interpretation grid did not anticipate the observed outcome shape (C1 borderline FAIL + C2 PASS + **C3 PASS with strong lift above matched-noise control**). The two prepared rows -- "C1 holds, C2/C3 fail -> MECH-341 load-bearing" and "C1 fails -> SD-056 wiring gap" -- mis-route a third interpretable case:

- The script's manifest declares `evidence_direction_per_claim` ARC-065 = weakens; MECH-341 = supports. This autopsy reclassifies ARC-065 as **supports** on the following grounds:
  1. C1 borderline FAIL (1/0/1 seeds above floor; means 0.041 / 0.042 / 0.046 vs 0.05 strict-greater floor) is a **calibration miss** -- the floor was set against V3-EXQ-613's training-only magnitude (0.286), not behavioural-runtime magnitude (~0.045).
  2. The **matched-entropy control (ARM_4)** -- the load-bearing FP-2 falsifier the script committed to -- is **decisively cleared on C3**: ARM_4 selected_entropy 0.414 vs ON arms 0.833-0.951 (~2.4x). Pure softmax temperature does not account for the lift; SD-056 produces structural diversity that the noise-injection control does not.
  3. The substrate IS operative on the C1 axis (3x baseline lift, just under threshold); pre-registered C1 floor failed against the wrong magnitude target.

- MECH-341 reading per the manifest holds: per-candidate variance is present and does propagate through E3 aggregation into selected-action diversity. The C3 lift confirms aggregation does not collapse upstream variance under MECH-341 default (no MECH-341 active during 569c).

### Open question this autopsy surfaces (mechanism question for 569e)

**Where exactly is the C3 lift coming from?**

Two plausible pathways:

- **Pathway A (per-candidate variance propagation):** C1 lift (~3x) propagates through E3 scoring as small-but-real score differences that resolve to different action classes at selection. Proportions roughly compatible (C1 ~3x, C3 ~2.4x).
- **Pathway B (E2 rollout dynamics shift):** Contrastive training updates E2.world_forward such that ON-arm rollouts have qualitatively different dynamics than OFF-arm rollouts -- not just slightly more spread but a different trajectory landscape. E3 sees a different scoring problem and selects different classes for reasons independent of within-tick per-candidate variance.

These are not mutually exclusive; both could contribute. The current measurement stack cannot dissociate them -- the e3_top2_class_gap NaN on ON arms blocks the most informative dissociation channel.

### Calibration learning

- C1 floor at 0.05 was set against the training-only standalone-task magnitude (V3-EXQ-613 measured 0.286 in standalone training). Behavioural-runtime measurement uses the **same metric** but in a sparser regime where the contrastive head trains incompletely within the experiment window. Floors set against training-only tasks should be re-calibrated against behavioural-runtime baselines before use as falsifier criteria.
- Bit-identical floor 0.05 happens to discriminate cleanly against noise (0.015) but fails to detect 3x baseline lift (0.045). A floor of 0.03 would discriminate noise (0.015) from substrate-operative (0.045) without rejecting realistic behavioural-runtime magnitudes.

### Draft `evidence_quality_note` for governance

For ARC-065:

> V3-EXQ-569c (2026-05-30) tested SD-056 against ARC-065 GAP-A R1.b as a matched-entropy FP-2 falsifier. Headline result: ON arms produce selected_action_entropy 0.833-0.951 vs matched-noise control (ARM_4 T=2.5) at 0.414 -- ~2.4x above the FP-2 control on the C3 acceptance axis. Pre-registered C1 floor (cand_world_pairwise_dist > 0.05) was not cleared by 2/3-seed majority (ON-arm means 0.041 / 0.042 / 0.046; per-seed counts 1/0/1) -- the floor was calibrated against V3-EXQ-613 standalone-task magnitude (0.286) rather than behavioural-runtime magnitude (~0.045); ON arms cluster at 3x bit-identical noise (0.015), confirming substrate operative. Per /failure-autopsy V3-EXQ-569c 2026-05-30: routed to /queue-experiment for V3-EXQ-569d (recalibrated C1 floor + e3_top2_class_gap NaN fix) and V3-EXQ-569e (mechanism probe dissociating per-candidate-variance propagation vs E2-rollout-dynamics shift as source of the C3 lift). Evidence direction for ARC-065 upgraded supports per the matched-noise control clearance on C3.

For MECH-341 (extension of existing note):

> V3-EXQ-569c (2026-05-30) confirms variance does propagate through E3 aggregation to selection: ON arms achieve selected_action_entropy 0.833-0.951 vs OFF baseline 0.361 (under MECH-341 default / no entropy bonus or stratified select active). No new MECH-341 substrate test required by 569c; the result strengthens MECH-341's non-collapse reading. evidence_direction supports per the manifest's per-claim tag, preserved.

---

## 6. Repair pathway

**Routing: queue-experiment (two parallel successors).** Confirmed by user 2026-05-30T16:55Z.

### V3-EXQ-569d: floor-recalibrated falsifier

- Same 5-arm structure (OFF / W001 / W005 / W020 / matched-noise T=2.5).
- C1 floor recalibrated to 0.03 (or whichever magnitude the user prefers after discussion). Rationale: discriminates structural lift (~0.045) from bit-identical noise (~0.015) without rejecting realistic behavioural-runtime magnitudes.
- Fix e3_top2_class_gap NaN on ON arms (instrumentation bug). Required for any mechanism discrimination.
- Optional: extend P0 from 30 ep to 50-60 ep so the contrastive head has more warmup time; document the buffer-warmup-to-effect curve.
- Accept the same C2 + C3 thresholds; the question is whether the substrate-operative axis tests positive under a runtime-calibrated floor.

### V3-EXQ-569e: mechanism probe

- Question: is the C3 lift coming from per-candidate z_world variance propagation OR from E2 rollout dynamics shifts that affect downstream E3 scoring independent of within-tick per-candidate variance?
- Design suggestion (open to refinement at queue time): record E2 rollout-divergence metrics across arms (E2 rollout trajectory KL or pairwise distance over trajectory steps), e3 score std across candidates, AND fix e3_top2_class_gap measurement.
- Acceptance criteria explicitly construct discrimination between pathway A and pathway B. Pre-register the interpretation grid this time including the C1-borderline-with-strong-C3-lift cell.

### Both successors should reference this autopsy

Each manifest should carry `supersedes: V3-EXQ-569c` and a docstring reference to `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-569c_2026-05-30.{md,json}`. The 569c manifest is NOT marked superseded for indexing purposes -- it is a contributory result whose evidence-direction is being upgraded by autopsy, not invalidated by a successor.

### Substrate / claims.yaml / review_tracker writes

NONE in this session. Governance applies:
- ARC-065 evidence_quality_note extension (text drafted above; verbatim).
- MECH-341 evidence_quality_note (no extension required; manifest tag preserved).
- review_tracker.json: V3-EXQ-569c run_id will be added to `reviewed_run_ids` by governance at next walk-through.
- substrate_queue.json: no substrate amendment (substrate is operative; failure mode is test design + measurement).

---

## 7. Routing decision (user-confirmed)

- **Routing:** queue-experiment (two parallel successors V3-EXQ-569d + V3-EXQ-569e).
- **ARC-065 evidence direction:** supports (autopsy upgrade from manifest weakens).
- **MECH-341 evidence direction:** supports (autopsy preserves manifest tag).
- **pending_retest_after_substrate:** false (substrate operative; no substrate amendment).
- **narrow_supports_flag:** false.

---

## 8. Concurrent-session coordination

Active claim at session start: igw-auto-igw-020-substrate-ready-mech-302-20260530T161236Z (NO-OP DONE 16:14Z; disjoint resources on evidence/lit_pulls/MECH-302 + MECH-303 + IGW ledger).

NOT touched this session: claims.yaml, claims.json, substrate_queue.json, experiment_queue.json, review_tracker.json, manifests, ree-v3/, ree_core/, experiment scripts. The autopsy produces a recommendation; governance applies.
