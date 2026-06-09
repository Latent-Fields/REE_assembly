# Failure Autopsy — V3-EXQ-654 (arc_062 GAP-B behavioural falsifier)

- **generated_utc:** 2026-06-09T17:31:34Z
- **scope:** single (cluster-context note below)
- **status:** confirmed (interactive gate cleared 2026-06-09)
- **run_id:** v3_exq_654_arc062_gapb_rule_apprehension_behavioural_falsifier_20260609T081844Z_v3
- **queue_id:** V3-EXQ-654
- **claim_ids:** MECH-309, ARC-062
- **experiment_purpose:** evidence
- **outcome:** FAIL / non_contributory
- **manifest self-route:** `substrate_not_ready_requeue` (indexer adjudication: `precondition_unmet`)
- **machine:** ree-cloud-2

## 1. Scope

V3-EXQ-654 is the GAP-B behavioural falsifier for MECH-309 ("trainers weight rules
they do not invent") and its ARC-062 weak-reading instantiation. Single-variable
contrast: **ARM_OFF** (`use_candidate_rule_field=False`, legacy collapsed
delta/world EMA rule_state) vs **ARM_ON** (`use_candidate_rule_field=True`, the
ARC-063 CandidateRuleField's differentiated `crf_source` feeding SD-033a
LateralPFCAnalog), both on the matched 649 GAP-A / 643a authority / SD-056 /
SP-CEM / MECH-341 stack with the SD-033a bias head un-zeroed
(`lateral_pfc_train_rule_bias_head=True`) and e2 trained online in P0.

**PRIMARY DV** = paired-by-seed committed-class entropy lift (ARM_ON > ARM_OFF).
**Self-route adjudicated:** the run FAILed on the **C1c readiness precondition**
(`arm_on_rule_field_differentiated`), not on the C2 falsifier DV — so this is
**not** a falsification of either claim.

This is the adjudication the manifest was waiting for: the `substrate_not_ready_requeue`
self-route is a hypothesis, and the autopsy confirms its direction while
identifying the precise substrate cause.

## 2. Facts (no interpretation)

Pre-registered acceptance criteria (`acceptance_criteria` block):

| Criterion | Value | Pass |
|---|---|---|
| C1a class axis exercisable (both arms) | n_off=3, n_on=3 | ✅ |
| C1b GAP-A consumed-summary divergence (both arms) | n_off=2, n_on=2 | ✅ |
| C1b bounded (< 1e6) | max 0.1126 | ✅ |
| **C1c ARM_ON rule field differentiated** | **n_on_differentiated = 0/3** | **❌** |
| C2 committed-class lift (load-bearing) | n_lift_seeds = 0/3 | ❌ (never reached — C1 gated) |

C1c detail (the failed precondition):
- `crf_frac_active_ge_floor` (fraction of P1 ticks the field fired a non-zero
  rule_state): **0.116 / 0.123 / 0.115** across ARM_ON seeds 42/43/44, vs the
  **0.30 floor**. The field is mostly inert.
- `crf_max_pairwise_rule_dist` = **0.0** on every ARM_ON seed (never ≥2 rules
  active simultaneously).
- `crf_n_minted_total` = 131 / 408 / 145 (minting fires plentifully).

C2 numbers (confirm zero behavioural reach even though C2 wasn't the gate):
- committed-class entropy mean: ARM_OFF 0.900018, ARM_ON 0.906556.
- paired lifts by seed: {42: 0.0, 43: −0.030338, 44: +0.049953}.
- **Seed-42 ARM_ON committed_class_counts are byte-identical to ARM_OFF**
  ({0:127, 1:649, 2:134, 3:627, 4:32}, entropy 1.224698).
- lateral_pfc bias |mean|: ARM_OFF 0.071846 vs ARM_ON 0.064645 (secondary control);
  on seed-42 specifically 0.099945 (OFF) vs 0.099989 (ON) — a 0.00004 difference.

Secondary negative control (within-class-representative entropy): ARM_OFF 1.631 vs
ARM_ON 1.595 — ~null as designed (the rule bias is class-keyed; confirms the bias
cannot move within-class selection).

## 3. Root cause — three compounding degeneracies (code-grounded)

### (a) Per-episode wipe → the live rule pool never matures
`agent.reset()` calls `candidate_rule_field.reset()` unconditionally
(`ree_core/agent.py:1908-1909`); `CandidateRuleField.reset()`
(`candidate_rule_field.py:371`) clears `self._rules`, `self._recurrence`, and
`self._step` every episode. P1 episodes are short (~26 ticks: 1569 P1 ticks / 60
episodes for seed 42; episodes terminate early on `done`). `_maybe_mint`
(`candidate_rule_field.py:198`) only mints after `mint_recurrence_threshold` (3)
recurrences of the same `(context_bucket, action_object)` **within one episode**,
because the recurrence counter is wiped at the boundary. `crf_n_minted_total`
131–408 is *cumulative across all 60 episodes* but the live pool is re-cold-started
every episode, so it rarely holds even one differentiated rule when `get_state()`
is read. This is why both `frac_active` (0.12) and `max_pairwise_rule_dist` (0.0)
collapse.

### (b) Conflict-scaled tolerance gate forbids ≥2-rule co-activation
`gate_and_select` (`candidate_rule_field.py:250`): `theta = tolerance_floor(0.3) +
tolerance_conflict_gain(1.0) * n_competing_matched`. The instant ≥2 rules match the
same context, `theta ≥ 1.3` while availability is capped at 1.0 → **both are locked
out**. So the field can never hold ≥2 active rules simultaneously →
`max_pairwise_rule_dist = 0.0` and `active_rule_state` returns near-zero. (This is
partly by design: the field's intended regime is single-rule-active with
across-tick variation, which is why C1c keys on `frac_active`, not `max_pairwise`.
But combined with (a) it means the field essentially never emits a live rule_state.)

### (c) Propagation washout — differentiated rule_state ≈ legacy bias even when live
On seed-42 the field fired 131 mints + 11.6% active, yet committed_class_counts are
byte-identical to ARM_OFF and lateral_pfc bias differs by 0.00004. The
`crf_source` → `lateral_pfc.compute_bias` path produced a per-candidate bias
indistinguishable from the legacy collapsed source. The `rule_bias_head` is
un-zeroed but **untrained in this run** (P1 is a frozen-encoder measurement window
with no E3-coupled bias-head optimizer), so a near-zero-norm rule_state maps through
a random head to a near-legacy bias. This is the `FAIL_C1_holds_C2_fails` grid
branch's open question — *"does propagation require a TRAINED bias head?"* —
surfacing even under a C1c-fail.

## 4. Claim-layer mapping — does not falsify either layer

The experiment never let MECH-309 / ARC-062 express themselves: the rule-creator's
output never reached the committed-selection argmin at the required liveness. An
immature-substrate cold-start gated the falsifier. **V3-EXQ-639 PASS**
(substrate-readiness, `norm_diff_across_contexts=0.806`, 2 distinct mints,
conflict-sensitive gate) is the existence proof that the CandidateRuleField *can*
emit a differentiated rule_state when its pool is allowed to mature — confirming the
substrate is sound and 654's per-episode cold-start is the cause, not a structural
absence of the mechanism.

## 5. Biological-reference triage

- **Closest mechanism:** non-Bayesian PFC rule-creator. Rule-coding units that
  abstract over instances (Bongard & Nieder 2010 PNAS; Miller & Cohen 2001).
  Conflict-graded availability gate (Frank 2006 STN threshold).
- **Dependency the failure resembles being absent:** biological PFC/BG rule
  (task-set) learning **accumulates across many experiences and is not reset
  between trials** (Collins & Frank 2014 task-set; Mansouri rule-selective
  persistence). The per-episode wipe of `_rules` + `_recurrence` is a translation
  failure: the V3 field cold-starts every episode, denying the cross-experience
  consolidation that lets a rule population mature. The FAIL matches the
  "missing-dependency signature" — a **discovered prerequisite (cross-episode rule
  consolidation), not a falsification**.
- **Formal-import check:** the mechanism is biologically grounded (not a formal
  definition import); no `/lit-pull` commission is the primary output. Biology is
  load-bearing in the *correct* direction here: it predicts the per-episode wipe is
  wrong.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C2 never fairly tested; C1c gated it out |
| Biological reference | clear; missing-dependency signature | cross-episode rule consolidation absent (per-episode wipe) |
| Developmental / dependency prerequisites | **missing / immature** | field cold-started every ~26-tick episode; never matures a live differentiated pool |
| Implementation completeness | partial | bias_head un-zeroed but untrained → propagation washout (seed-42 byte-identical) |
| Environment adequacy | adequate | SD-054 bipartite reef/forage substrate is the intended falsifier env |
| Measurement adequacy | adequate-but-incomplete | C1c tests `frac_active` only; does not test rule_state→bias non-vacuity (the seed-42 washout it missed) |
| Integration adequacy | partially coupled | field → lateral_pfc → E3 wired, but the field is inert and its live output washes out |
| Scale / capacity | likely insufficient at behavioural horizon | short episodes + recurrence-threshold mint + per-episode wipe starve the pool |

**Recommended epistemic_category:** `substrate_ceiling` (precondition_unmet flavour —
substrate immaturity, not a representational ceiling).
**Recommended evidence_direction:** `non_contributory` (unchanged).
**pending_retest_after_substrate:** true. **Do NOT weaken MECH-309 / ARC-062.**

## 7. Cluster-context note (not an independent cluster)

654 shares the *committed-action no-lift* shape with the 604a / 624a / 614d / 614e
convergent cluster (all "modulatory/diversity channel reaches E3 but does not move
the committed argmin") and the 543 lineage (gated-policy collapse). But 654's
**proximate** failure is a distinct, newly-surfaced mode: the CandidateRuleField
never reaches a live differentiated state because of per-episode cold-start. The
643a modulatory-bias-selection-authority gate (proven operative) is enabled in this
run, so authority is not the bottleneck here — the bottleneck is upstream of
authority, in the rule-creator's own maturation. Treat as single-target;
cross-reference the cluster as shared structural property only.

## 8. Learning extracted

1. **New dependency discovered:** the CandidateRuleField needs cross-episode rule
   persistence to mature a differentiated pool at behavioural-runtime episode
   lengths. The per-episode `reset()` wipe is the load-bearing immaturity.
2. **Bias-head propagation is a second latent precondition** the C1c gate does not
   test: even a live field produced a bias == legacy (seed-42). A trained bias head
   (or a bias-non-vacuity gate) is required so a future C1-pass is not itself
   vacuous.
3. **The conflict gate (`conflict_gain=1.0`) forbids ≥2-rule co-activation**, so
   `max_pairwise_rule_dist` is structurally 0 and differentiation lives in the
   across-tick single-rule sequence — `frac_active` is the correct binding
   readiness, confirming C1c's design.

## 9. Repair pathway (user-confirmed at the interactive gate)

**PRIMARY route — `implement-substrate` (substrate amend first):** add a
no-op-default cross-episode rule-persistence flag to the ARC-063 CandidateRuleField
so `_rules` / `_recurrence` are not cleared on `agent.reset()` (the biologically
faithful fix — PFC rule learning is not reset per trial). Bit-identical OFF;
default preserves current per-episode-reset behaviour. This lets the field
accumulate a live, differentiated pool across the P1 measurement episodes so
`crf_frac_active` can clear the 0.30 floor.

**SECONDARY (test-design, folded into the 654a re-queue) — `queue-experiment`:**
on the persistent-field substrate, queue 654a with
(i) a **trained-bias-head P1 arm** (E3-coupled optimizer on
`lateral_pfc.bias_head_parameters()`, GAP-D wiring already landed 2026-05-17) so
the differentiated rule_state can actually move committed-class selection; and
(ii) a **propagation non-vacuity precondition** (ARM_ON lateral_pfc bias must differ
from ARM_OFF by a margin on firing ticks) so a future C1-pass cannot be vacuous;
keep the committed-class entropy PRIMARY DV.

**Recommended `evidence_quality_note` (governance to write — do not write here):**
> V3-EXQ-654 (arc_062 GAP-B falsifier, MECH-309/ARC-062) FAIL non_contributory,
> self-route substrate_not_ready_requeue (precondition_unmet). C1c
> arm_on_rule_field_differentiated FAILED: ARM_ON CandidateRuleField fired a
> non-zero rule_state on only ~12% of P1 ticks (frac_active 0.116/0.123/0.115 vs
> 0.30 floor); max_pairwise_rule_dist 0.0 all seeds; seed-42 committed-class
> byte-identical to ARM_OFF. Code-grounded cause (failure_autopsy_V3-EXQ-654_2026-06-09):
> agent.reset()→candidate_rule_field.reset() wipes the rule pool + recurrence
> counters every ~26-tick episode, so the field never matures a live differentiated
> pool (cumulative n_minted 131-408 but live pool cold-started each episode);
> compounded by the conflict gate forbidding >=2-rule co-activation and an untrained
> bias head washing out the live rule_state (propagation gap). NOT a falsification —
> the falsifier never ran. V3-EXQ-639 PASS proves the field CAN differentiate when
> its pool matures. Route: implement-substrate (cross-episode rule-persistence flag
> on ARC-063 CandidateRuleField) then re-queue 654a with a trained-bias-head P1 arm
> + bias-non-vacuity precondition. MECH-309/ARC-062 stay candidate / v3_pending /
> pending_retest_after_substrate; do NOT weaken.

## 10. Routing

- **routing:** implement-substrate (PRIMARY) + queue-experiment (654a, SECONDARY,
  gated on the substrate amend).
- **recommended_substrate_queue_entry.action:** amend (ARC-062 GAP-B substrate
  track; implementation target is the ARC-063 CandidateRuleField module).
- governance applies the writes; this autopsy is analysis + handoff only.
