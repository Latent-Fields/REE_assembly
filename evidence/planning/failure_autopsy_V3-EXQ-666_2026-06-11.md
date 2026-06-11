# Failure Autopsy -- V3-EXQ-666 (ARC-063 CRF mature-pool substrate-readiness diagnostic)

- **Generated (UTC):** 2026-06-11T07:06:49Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated at Step 8)
- **Run:** `v3_exq_666_arc063_crf_mature_pool_readiness_20260611T063849Z_v3` (machine ree-cloud-2)
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `experiment_purpose: diagnostic` / `claim_ids: []`
- **Self-route:** `mature_dynamics_insufficient_at_behavioural_runtime -> /failure-autopsy (NOT a requeue)`
- **Validates:** the 2026-06-11 ARC-063 CandidateRuleField amend routed by `failure_autopsy_V3-EXQ-654b_2026-06-11`

This skill is analysis + hand-off only. It does NOT edit claims.yaml, manifests, review_tracker, substrate_queue, or evidence_direction. Governance applies the recommendations interactively.

---

## 1. Scope

Single-target autopsy of a claim-free substrate-readiness diagnostic. EXQ-666 tests whether the 2026-06-11 ARC-063 amend (two opt-in flags) lets the CandidateRuleField hold a **differentiated, persistent >=2-rule pool** at behavioural runtime. It does NOT validate or weaken MECH-309 / ARC-062 / ARC-063 (all stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate). It gates the 654c GAP-B behavioural re-run (MECH-309 / ARC-062 committed-class entropy falsifier), which stays blocked until a CRF-readiness PASS lands.

The self-route is trustworthy (not a `precondition_unmet` / `vacuous_pass` masquerade):

- **Non-vacuity MET** -- every (arm x seed) cell minted >=2 rules (min_n_minted_all_cells=2). The field engaged; a below-gate reading is fix-insufficiency, not field-not-engaged. So this is a FAIL routed to autopsy, NOT a `substrate_not_ready_requeue`.
- **Discrimination MET** -- ARM_0_OFF reproduces the legacy 654b churn signature (`criteria_non_degenerate.readiness_gate_discriminates_vs_arm0_off = true`), so the env is not non-discriminating.

---

## 2. Facts (reconstruction, no interpretation)

**Readiness gate:** `crf_max_pairwise_rule_dist > 0.1` (DIFFERENTIATION: pool holds >=2 differing rules) **AND** `crf_frac_active >= 0.30` (PERSISTENCE/ACTIVITY: a matched rule clears its availability threshold theta on >=30% of steps). 3 arms x 3 seeds (42/43/44).

| Arm | crf_max_pairwise_rule_dist | crf_frac_active | minting | gate cleared |
|---|---|---|---|---|
| ARM_0_OFF (legacy, raw z_world ctx) | 0.0 | ~0.125 | 117-151 minted, ~all retired (1 active slot) | 0/3 -- **654b churn signature reproduced** |
| ARM_1_MATURE (mature dynamics, raw z_world ctx) | 0.0 | ~0.066 | only **2** minted, 1 active | 0/3 -- **load-bearing criterion FAILED** |
| ARM_2_MATURE_E2CTX (mature + e2_world_forward ctx) | **~1.71** | **0.016** | 10-17 **distinct** rules (n_slots_minted 10-16) | 0/3 |

Per-arm summary metrics (manifest `arm_summary`):
- ARM_0_OFF: n_gate_cleared 0/3, mean_frac_active 0.1247, mean_max_pairwise_rule_dist 0.0
- ARM_1_MATURE: n_gate_cleared 0/3, mean_frac_active 0.0661, mean_max_pairwise_rule_dist 0.0
- ARM_2_MATURE_E2CTX: n_gate_cleared 0/3, mean_frac_active 0.0160, mean_max_pairwise_rule_dist 1.708
- readiness_met_arm1_mature=false; discrimination_met_arm0_off_does_not_mature=true; e2ctx_met_arm2=false; non_vacuity_met_all_cells_minted=true.

**Which criterion failed:** the load-bearing one (ARM_1_MATURE clears readiness gate) = FALSE. The non-load-bearing positive control (ARM_0_OFF reproduces 654b) = TRUE. The non-load-bearing e2ctx criterion = FALSE.

Note: the unit smoke in the implement-substrate session (forced two-regime activation harness, cos-0.7 hazard negatives) reported `legacy n_present=1/dist=0.0/READY=False -> mature n_present=2/dist=1.49/READY=True`. That hand-fed 2-context harness PASSed where the behavioural-runtime context distribution (~2000-3900 contrastive steps) FAILs. The smoke is a poor proxy for runtime; 666 is the correct instrument and it did its job.

---

## 3. The load-bearing finding: differentiation and persistence are in TENSION at runtime

The amend treated "differentiated" and "persistent" as jointly solvable by one set of gate/credit/retire knobs. 666 decomposes the gate into its two sub-properties and shows they trade off against each other under the current availability scheme:

- **Differentiation is delivered ONLY by the e2_world_forward context.** ARM_1 (raw z_world) is too self-similar -- the mint-block (`mature_mint_block_threshold` 0.8) collapses minting to ~2 rules, dist 0.0. ARM_2 (e2_world_forward) mints 10-16 *distinct* rules, dist 1.71. This **confirms and strengthens** the 654b-autopsy dependency hypothesis (ARC-065 GAP-A: raw z_world spread too low to mint distinct rules). The e2ctx routing is necessary *and* sufficient for differentiation.
- **But more differentiation WORSENS activity.** Once context is well-differentiated, each rule matches only a narrow slice of contexts, so its `availability` EMA never accumulates above theta between sparse matches (and decays in between) -> it rarely counts as "active". ARM_2 has the WORST frac_active (0.016). Both mature arms fail persistence; ARM_1 (no differentiation) also fails it (0.066).

`crf_frac_active = _n_active_steps / _step`, where `_n_active_steps` increments on any tick where a matched rule's `availability >= theta = tolerance_floor + gain * n_competing_matched`. The conflict-gate retune (`mature_tolerance_floor` 0.15 / `mature_tolerance_conflict_gain` 0.25 -> theta(1)=0.40, theta(2)=0.65, theta(3)=0.90 < 1.0) -- the 654b-diagnosed fix -- lowered theta, but the binding constraint in the *differentiated* regime is not theta. It is that per-rule availability does not accumulate under sparse matching: a narrowly-tuned rule sees its context rarely, accrues availability slowly when matched, and decays (`mature_availability_decay` 0.001/tick) over the long gaps. So even theta(1)=0.40 is rarely cleared.

**Conclusion:** the amend is half-right. It solves differentiation (via e2ctx) but introduces/worsens a persistence collapse. The next constraint is **availability MAINTENANCE under sparse per-rule matching** -- a maintenance problem, not a gating problem.

---

## 4. Biological-reference triage

- **Closest mechanism:** PFC rule / task-set cell representations -- prefrontal cells that encode the currently-active rule and maintain it across the trial (Wallis, Anderson & Miller 2001; Mante et al. 2013 context-dependent computation; Frank 2006, already cited in the CRF source for the tolerance-gate). The CRF is a faithful **biological-mechanism translation** of this class, NOT a formal-definition import (no Pearl / Shannon / optimal-control formalism is being instantiated).
- **Existence proof for the class:** brains plainly maintain multiple concurrently-differentiated task rules. So the default reading of the FAIL is a translation/calibration gap, not a falsification of the rule-apprehension claims.
- **Missing-dependency signature:** the differentiation<->persistence tension maps onto a *real* biological design constraint. Narrowly-tuned (highly selective) rule cells fire on a small fraction of inputs, so their maintenance cannot rely on input-driven re-activation alone -- biology supplies **sustained-activity / recurrent-attractor maintenance** (Goldman-Rakic delay-period persistent activity; Wang recurrent-attractor working memory), or **activity-silent synaptic maintenance** (Stokes 2013; Lundqvist 2016 gamma-burst reactivation). The CRF accrues availability ONLY on match and decays otherwise -- it has the *symbol* of a rule cell but not the *maintenance* functional role. That is the discovered gap.
- **Lit status:** no `targeted_review` entry exists for CRF persistence / PFC rule-cell sustained activity. Per the user's Step-8 judgment, the maintenance mechanism must be grounded in biology BEFORE it is specified in substrate. A live fork the lit-pull must resolve: is rule maintenance **persistent-firing** (-> a sustained-activity term that holds availability across context-absent ticks) or **activity-silent / synaptic** (-> the `frac_active` "active fraction" framing is itself biologically questionable; rules can be silently maintained and reactivated, which would change the readiness readout, not just the credit dynamics)? This fork directly shapes whether the substrate fix is a maintenance term or a redefinition of "active".

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free) | Informs MECH-309 / ARC-062 / ARC-063 readiness only; all stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate. Substrate STILL not ready. |
| Biological reference | clear | PFC rule/task-set cells; mechanism translation not formal import. Differentiation<->persistence tension maps to a real design constraint (selective cells need sustained-activity / activity-silent maintenance). Default reading = calibration/completeness gap. |
| Developmental / dependency prerequisites | dependency strengthened | e2_world_forward context CONFIRMED necessary for differentiation (raw z_world insufficient; ARC-065 GAP-A). |
| Implementation completeness | partial | Differentiation works (ARM_2); persistence/maintenance does not. The match-triggered-EMA availability scheme lacks a maintenance term. |
| Environment adequacy | adequate | 654b hazard env discriminates (ARM_0 reproduces churn; criteria_non_degenerate true). |
| Measurement adequacy | adequate | The gate did its job -- it decomposed the failure into differentiation vs persistence. (The unit smoke was a poor runtime proxy; 666 is the right instrument.) Open lit question: whether "active fraction" is the right persistence readout if maintenance is activity-silent. |
| Integration adequacy | partially coupled | Context-source (e2_world_forward) integration works for minting; availability-accounting interacts badly with the retire/decay dynamics once rules are differentiated. |
| Scale / capacity | adequate | ~2000-3900 contrastive steps; minting clearly happens; budget is not the limiter. |

**Recommended `epistemic_category`:** unchanged. ARC-062 / MECH-309 stay `substrate_ceiling`; this diagnostic is `non_contributory` and weights nothing in governance.

---

## 6. Learning extracted

1. **e2_world_forward context is a confirmed prerequisite for CRF differentiation** -- raw z_world context is too self-similar (mint-block collapses the pool to ~2 rules). Adopt e2ctx as the mature-regime differentiation default.
2. **Differentiation and persistence are in tension** under the current match-triggered-EMA availability scheme: solving differentiation (via e2ctx) worsens activity, because narrowly-tuned rules match sparsely and their availability never accumulates above theta.
3. **The next binding constraint is availability MAINTENANCE under sparse matching** (a PFC sustained-activity / activity-silent analog), not the conflict-gate theta. The 654b theta retune was necessary but addressed the wrong constraint for the differentiated regime.
4. **Ground the maintenance mechanism in biology first** (user judgment) -- the persistent-firing vs activity-silent fork determines whether the fix is a sustained-activity term or a redefinition of the "active fraction" readout.

---

## 7. Repair pathway (user-confirmed at Step 8)

**Primary route: `/lit-pull`** -- commission a `targeted_review` on PFC rule/task-set-cell persistence and maintenance (persistent delay-period activity vs activity-silent/synaptic maintenance; how selective rule cells are maintained across input-absent epochs). Resolve the persistent-firing vs activity-silent fork. This blocks the substrate fix.

**Downstream (gated on the lit verdict): `/implement-substrate`, action = CREATE a new substrate_queue entry** for the CRF availability-maintenance / sustained-activity gap (the user chose a NEW entry over amending the existing ARC-062 entry, to keep the maintenance gap distinct from ARC-062's differentiation/gating work). The implementation, informed by the lit-pull, should: (a) make e2_world_forward the mature-regime differentiation default; (b) add availability maintenance so differentiated rules reach frac_active >= 0.30 (the exact mechanism -- sustained-activity term holding availability across context-absent ticks, OR an activity-silent reactivation readout -- to be set by the lit verdict); (c) re-validate with a 666-successor CRF-readiness diagnostic BEFORE the 654c GAP-B behavioural re-run.

**Not recommended:** demotion (claim-free; biology supports the class), requeue of 666 as-is (the field engaged; re-running unchanged returns the same answer). The 654c GAP-B behavioural re-run STAYS gated/blocked.

**Draft `evidence_quality_note` for governance to write (against ARC-062 / MECH-309 / ARC-063, or the new substrate entry's failure record):**

> V3-EXQ-666 (claim-free CRF mature-pool readiness diagnostic, non_contributory) decomposed the 654b non-maturation: the e2_world_forward context delivers differentiation (ARM_2 crf_max_pairwise_rule_dist 1.71, 10-16 distinct rules) but per-rule availability does not accumulate under sparse matching, so crf_frac_active collapses (ARM_2 0.016, worse than legacy 0.125). The CRF lacks a maintenance mechanism analogous to PFC sustained-activity; the conflict-gate theta retune addressed the wrong constraint for the differentiated regime. Substrate STILL not ready. Routed: lit-pull on PFC rule-cell persistence (persistent-firing vs activity-silent) -> new substrate_queue entry (CRF availability maintenance) -> 666-successor re-validation before the 654c GAP-B behavioural falsifier (which stays gated). MECH-309 / ARC-062 / ARC-063 stay candidate / substrate_ceiling / v3_pending / pending_retest_after_substrate (unchanged by this non_contributory diagnostic).

---

## 8. Hand-off summary

- **Failed criterion:** discrimination/load-bearing (ARM_1_MATURE clears readiness gate = false).
- **Dominant diagnosis layer:** implementation completeness (missing availability-maintenance mechanism) + strengthened dependency (e2_world_forward context).
- **Biological-reference verdict:** clear existence proof; mechanism translation, not formal import; calibration/completeness gap, not falsification.
- **Routing:** lit-pull (primary, blocking) -> implement-substrate action=create (gated on lit verdict) -> 666-successor re-validation. No demotion, no requeue.
- **Gated downstream:** 654c GAP-B behavioural re-run (MECH-309 / ARC-062) stays blocked.
