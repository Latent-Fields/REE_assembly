# Failure Autopsy -- V3-EXQ-654d (arc_062 GAP-B rule-apprehension behavioural falsifier)

**generated_utc:** 2026-06-16T19:50:40Z
**scope:** single (5th in the 654 -> 654a -> 654b -> 654c -> 654d lineage; substrate-maturation recurrence, NOT claim-granularity debt -- user-adjudicated 2026-06-15, re-confirmed 2026-06-16)
**status:** confirmed (interactive gate cleared 2026-06-16)
**run_id:** v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3
**queue_id:** V3-EXQ-654d (supersedes V3-EXQ-654c)
**claim_ids (tagged):** MECH-309, ARC-062 (substrate actually exercised = **ARC-063** `CandidateRuleField`)
**outcome:** FAIL / non_contributory; self-route `substrate_not_ready_requeue`
**machine:** ree-cloud-2
**routing (confirmed):** implement-substrate -- **amend `crf-availability-maintenance`** at the CRF locus (fault 2 maintenance-vs-theta gate + fault 1 CRF context-key separation + frac_active readiness gate), **ungated from GAP-A**. NO claim demotion.
**predecessors:** `failure_autopsy_V3-EXQ-654_2026-06-09`, `failure_autopsy_569f-661-654a_2026-06-10`, `failure_autopsy_V3-EXQ-654b_2026-06-11`, `failure_autopsy_V3-EXQ-654c_2026-06-15`

---

## Summary

654d is the 5th consecutive failure on the **same** readiness precondition C1c
(`arm_on_rule_field_differentiated_and_matured`), `crf_frac_active = 0.0` again.
But it carries the **load-bearing disambiguation** the 654c autopsy could not make,
because 654d (a) ARMED the GAP-A de-collapse lever (ARM_STD_G2, validated by
V3-EXQ-684a) on both arms, and (b) finally **recorded the discriminator**
(`crf_mean_n_matched`) the 654c autopsy flagged as missing.

The result: **the GAP-A conversion de-collapse was the wrong lever for this gate.**
ARM_STD_G2 de-collapses the **E3 selection-authority channel** (the GAP-A / 569h /
684a fix). It does **not** touch the **CRF rule-mint/match context key**. So even
though the E3-channel divergence cleared the floor on 2/3 seeds
(`consumed_summary_pairwise_dist` 0.055 / 0.080 on seeds 42 / 44), the CRF still
matched **7-8 rules per tick** (`crf_mean_n_matched` 7.08 / 7.29 / 8.70) -- *higher*
than 654c's >=3 regime -- and **gated every one out**. The 654c route ("re-queue 654d
only after GAP-A context de-collapse") **conflated two distinct loci**; 654d proves
they are independent.

Root cause is the **two coupled CRF-locus faults the 654c autopsy already named,
both still un-amended** (substrate source bit-identical to 654c):

1. **CRF context-key collapse (fault 1, at the CRF locus -- NOT the E3 channel).**
   The 16 minted rules' `context_tag`s are mutually within `context_match_threshold`
   (cosine >= 0.5), so 7-8 of them co-match the current per-tick context ->
   `n_matched` inflates. ARM_STD_G2 de-collapses the per-candidate E3 summaries, a
   *different vector and use* than the single per-tick CRF match context, so the CRF
   match crowding is unaffected (indeed worse than 654c).
2. **Maintenance floor sits below the crowded-match theta (fault 2, pure gate
   calibration).** `gate_and_select` marks a rule active iff
   `availability >= theta = mature_tolerance_floor(0.15) + mature_tolerance_conflict_gain(0.25) * (n_matched-1)`.
   Maintenance holds availability at `maintenance_floor = 0.45`. With `n_matched ~= 7`,
   `theta ~= 1.65 >> 0.45` -> **every matched rule gated out -> frac_active = 0.0.**
   This calibration is **fully independent of GAP-A** -- it is a CRF gate property.

**Disambiguation (the new finding vs 654c):** 654c could only *infer* "matched but
gated out" from the collapsed-context data. 654d **measures** it: `crf_mean_n_matched`
~7-8 with `crf_frac_active` 0.0, and `mean_prop_counterfactual_delta = 0.0` (zeroing
rule_state changes nothing -> the gated-out rule_state never reaches committed
action). The blocker is now **precisely localized to the CRF conflict gate**, and the
controlled experiment (GAP-A de-collapse armed, gate still locked) proves it is
**independent of the GAP-A selection-authority conversion**.

**Strategic correction:** the 654c gating decision ("gate 654d behind GAP-A") was
the right caution but the wrong dependency. The correct next step is to amend the
CRF gate **directly at its own locus** (couple maintained availability to the
per-tick `theta(n_matched)`, and/or cap `n_competing`, and/or sharpen
`context_match_threshold` so fewer rules spuriously co-match) and **not** re-gate the
next iteration on GAP-A.

---

## Facts (no interpretation)

Manifest: `v3_exq_654d_arc062_gapb_rule_apprehension_behavioural_falsifier_20260616T152753Z_v3.json`
(machine ree-cloud-2; seeds 42/43/44; 2 arms; p0=200 / p1=90 / p2=60 ep; 200 steps/ep;
`crf_persist=True`, `crf_mature_pool_dynamics=True`, `crf_context_from_e2_world_forward=True`,
`crf_availability_maintenance=True`, `maintenance_floor=0.45`, `maintenance_decay=0.0`;
ARM_STD_G2 armed on BOTH arms: `use_modulatory_selection_authority=True`,
`modulatory_authority_gain=2.0`, `modulatory_authority_normalize_basis="std"`,
`use_modulatory_channel_routing=True`, `modulatory_channel_route_source="cand_world_summary"`;
`lateral_pfc_train_rule_bias_head=True` trained in a frozen-encoder P1 REINFORCE window).

**C1 non-vacuity preconditions:**

| precondition | measured | threshold | met |
|---|---|---|---|
| committed-class axis exercisable (both arms) | 1.0 | 0.30 | yes |
| GAP-A consumed-summary divergence (both arms) | 2/3 seeds clear (ARM_ON 0.055 / 0.008 / 0.080) | 0.05 | **yes** (majority both arms; ARM_OFF n=2, ARM_ON n=2) |
| consumed-summary bounded (no 643a explosion) | 0.1396 max | 1e6 | yes |
| **C1c ARM_ON rule field differentiated AND matured** | **crf_frac_active 0.0** | **0.30** | **NO** |
| propagation non-vacuity (ARM_ON bias != ARM_OFF) | 0.0282 / 0.0165 / 0.0044; 3/3 seeds | 0.001 | yes |

**The discriminator (new in 654d -- the 654c-flagged instrument):**

| arm/seed | crf_n_minted | crf_max_pairwise_rule_dist | **crf_mean_n_matched** | crf_mean_n_active | **crf_frac_active** |
|---|---|---|---|---|---|
| ARM_ON 42 | 16 | 1.711 | **7.08** | 0.0 | **0.0** |
| ARM_ON 43 | 16 | 1.711 | **7.29** | 0.0 | **0.0** |
| ARM_ON 44 | 16 | 1.711 | **8.70** | 0.0 | **0.0** |

Rules ARE minted (16), ARE differentiated (max_pairwise_dist 1.711), ARE matching
(7-8 per tick) -- and EVERY ONE is gated out (n_active 0.0). `theta(n_matched=7) =
0.15 + 0.25*6 = 1.65 >> maintenance_floor 0.45`. The 654c "matched-but-gated-out"
reading is now directly measured, not inferred.

**Lineage (the load-bearing signal):**

| run | regime | crf_frac_active | crf_n_matched | crf_max_pairwise_rule_dist | crf_n_minted |
|---|---|---|---|---|---|
| V3-EXQ-654 | per-episode wipe | ~0.12 | (unrecorded) | 0.0 | 131-408 |
| V3-EXQ-654a | crf_persist | 0.137 | (unrecorded) | 0.0 | 268/549/220 |
| V3-EXQ-654b | crf_persist + 240 ep | 0.130 | (unrecorded) | 0.0 | 452/1014/419 |
| V3-EXQ-654c | + 666c maint. levers | 0.0 | (unrecorded; inferred >=3) | 1.711 | 16/12/15 |
| **V3-EXQ-654d** | **+ ARM_STD_G2 GAP-A de-collapse** | **0.0** | **7.1/7.3/8.7 (measured)** | **1.711** | **16/16/16** |

**C2 (moot -- C1 gates it):** committed-class entropy ARM_OFF 1.026737 vs ARM_ON
1.022444; paired lifts by seed {42: -0.0196, 43: +0.0040, 44: +0.0027}; 0/3 seeds
above the 0.05 margin. Not scored.

**Within-arm rule_state counterfactual:** `mean_prop_counterfactual_delta = 0.0` on
all three ARM_ON seeds (C1d_within_arm_on_rule_state_counterfactual_nonzero = false).
The C1d propagation pass (0.028) comes from OTHER matched-stack differences between
ARM_ON and ARM_OFF, NOT from rule_state -- because rule_state is gated out (frac_active
0.0) it contributes nothing to committed action. This corroborates the gate-lockout:
the controlling failure is firmly C1c.

**Failed criterion class:** readiness (C1c maturation/activation precondition), which
self-routes requeue and correctly does NOT score against MECH-309/ARC-062.

---

## Claim-layer map

- **MECH-309** (mechanism_hypothesis, candidate, `substrate_ceiling`, v3_pending) and
  **ARC-062** (architectural_commitment, candidate, `phase_1_implemented_evidence_gated`,
  v3_pending) both carry promote/demote suppression by construction. non_contributory
  is safe.
- **ARC-063** (the strong-reading distributed CandidateRule field) is the
  implementation actually exercised by `use_candidate_rule_field=True` in ARM_ON.
  654d's tags do not include ARC-063 but, because the result is non_contributory, no
  mis-weighting occurs.
- **Did the experiment test the claims under conditions where they could express
  themselves?** No. The matured, differentiated rule_state matched (7-8/tick) but was
  gated out before it could reach committed action, so the GAP-B falsifier (does a
  differentiated, matured rule_state add committed-class diversity?) could not run. C1
  correctly blocked scoring. An implementation/dependency gap at the CRF conflict gate,
  not a falsification.

---

## Biological-reference triage

- **Closest mechanism:** non-Bayesian PFC/BG **task-set rule-creator** -- rule-coding
  units abstracting over instances (Bongard & Nieder 2010; Miller & Cohen 2001);
  conflict-graded "hold-your-horses" availability threshold (Frank 2006; Cavanagh
  2011); rule-selective persistence (Mansouri; Collins & Frank 2014).
- **Faithful translation, not a formal-definition import.** No `/lit-pull` commission
  is warranted; the biology is load-bearing in the *correct* direction (a maintained
  set of differentiated rules should be **selectable**, not gated out by mutual
  crowding).
- **Does the failure resemble a missing dependency of the reference mechanism?** Yes,
  and 654d sharpens which one. The conflict gate exists biologically to suppress
  *competing* rules so a *winner* emerges; in the REE implementation the gate's theta
  grows linearly with `n_matched` while maintenance holds availability at a fixed
  floor, so under many co-matching rules the gate suppresses **all** of them rather
  than electing one. That is an **availability/conflict-gate calibration gap** -- a
  discovered prerequisite (a maintained, differentiated rule set must be able to *win*
  selection under realistic match-crowding), **not** a falsification of
  MECH-309/ARC-062.

---

## Mechanism (from `ree-v3/ree_core/policy/candidate_rule_field.py`, unchanged since 654c)

- **`gate_and_select` (l.392-427):** `matched = [r : cosine(context, r.context_tag)
  >= context_match_threshold(0.5)]`; for each matched `r`, active iff
  `r.availability >= theta = theta_floor + theta_gain * (n_matched-1)`. Mature pool:
  `mature_tolerance_floor=0.15`, `mature_tolerance_conflict_gain=0.25` ->
  theta(1)=0.15, theta(2)=0.40, theta(3)=0.65, **theta(7)=1.65, theta(8)=1.90**.
- **Maintenance (l.203, l.365-369):** `maintenance_floor=0.45` holds a differentiated
  rule's availability (`maintenance_decay=0.0`). Tuned (code comment l.181-183) to
  clear the **2-way** match (theta=0.40), i.e. the single-competitor case.
- **The interaction that produces frac_active=0.0:** the 16 minted rules' context_tags
  are mutually similar (cosine >= 0.5) -> 7-8 co-match the per-tick context ->
  `n_matched ~= 7` -> theta ~= 1.65 > 0.45 maintenance -> no rule clears the gate ->
  `crf_n_active_last = 0` every P2 tick. The maintenance floor lives permanently in
  the dead zone for any `n_matched >= 3`.
- **Why ARM_STD_G2 did not help:** `modulatory_channel_route_source="cand_world_summary"`
  and the std-basis authority gain act at **E3.select** on the per-candidate summaries
  -- the GAP-A *selection-authority* conversion channel. The CRF context that
  `gate_and_select` matches against is the single per-tick `e2_world_forward` context
  fed to mint/match; de-collapsing the cross-candidate E3 spread does not separate the
  minted rules' context_tags. Two distinct loci.

---

## Adjudication of the self-route

`substrate_not_ready_requeue` is **not vacuous** -- the C1c precondition was genuinely
unmet (the CRF really did not activate; 7-8 rules matched and all gated out). But the
**action the label implies** -- a budget/maturation requeue -- is wrong (the canonical
V3-EXQ-642 trap). The cause is the **two coupled CRF-locus faults the 654c autopsy
already named** (context-key crowding + maintenance/conflict-gate calibration), both
**still un-amended** (substrate source bit-identical to 654c). 654d's controlled
addition (ARM_STD_G2) proves these faults are **independent of the GAP-A selection
conversion**. The correct route is the CRF-substrate amend at its own locus -- NOT a
654e budget requeue, and NOT another GAP-A-gated wait.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C2 never fairly tested; C1c gated it out (5th time) |
| Biological reference | clear; one sharpened missing-dependency signature | a maintained, differentiated rule set must be SELECTABLE under match-crowding; the conflict gate suppresses all instead of electing one |
| Developmental / dependency prerequisites | **present at the GAP-A locus, missing at the CRF locus** | ARM_STD_G2 de-collapsed the E3 channel (2/3 seeds) but the CRF context_tag separation + gate calibration are unaddressed |
| Implementation completeness | partial | pool mints + differentiates + matches (real progress); the activation gate locks the matched pool out |
| Environment adequacy | adequate | SD-054 bipartite reef/forage falsifier env is intended |
| Measurement adequacy | **adequate now** | 654d added `crf_mean_n_matched` -- the discriminator 654c lacked; "matched but gated out" is now measured |
| Integration adequacy | partially coupled | field -> lateral_pfc -> E3 wired; field matures + matches but its output is gated out before committed action (prop_counterfactual_delta 0.0) |
| Scale / capacity | adequate | not a budget problem; activation is a gate calibration, not a budget, failure |

**Recommended epistemic_category:** `substrate_ceiling` (precondition_unmet flavour --
CRF conflict-gate calibration under match-crowding, not a representational ceiling).
**Recommended evidence_direction:** `non_contributory` (unchanged).
**pending_retest_after_substrate:** true. **Do NOT weaken MECH-309 / ARC-062 / ARC-063.**

---

## Lineage / recurrence read (5th autopsy on this target)

Per the granularity-debt recurrence hook, this is the 5th separate autopsy circling
the same C1c precondition. **User-adjudicated read (re-confirmed 2026-06-16):
substrate-maturation recurrence, NOT claim-granularity debt.** 654d *strengthens*
this read rather than weakening it: (a) the claims are well-defined and have **never
been tested** (C1 gated every iteration), so they are not "coarse claims circled by
structurally-different falsifications"; (b) the blocker has marched one
well-localised stage downstream each time (cold-start washout -> retire-churn ->
activation-gate-under-collapse -> **now: activation-gate calibration, isolated and
measured, independent of GAP-A**); (c) 654d obtained the discriminator
(`crf_mean_n_matched`) that converts the prior inference into measurement. No
`/claim-synthesis` decomposition is warranted. The honest strategic caveat -- 5
iterations and the falsifier still has not run -- is now addressed by amending the
CRF gate **directly at its own locus**, rather than iterating an upstream proxy
(per-episode budget; GAP-A conversion) again.

---

## Learning extracted

1. **The GAP-A conversion de-collapse and the CRF context-key collapse are two
   distinct loci.** ARM_STD_G2 (modulatory selection authority at E3.select, std
   basis, gain 2.0, channel routing on `cand_world_summary`) de-collapses the
   per-candidate E3 selection channel; it does NOT separate the CRF minted rules'
   `context_tag`s. The 654c gating decision ("gate 654d behind GAP-A") conflated them.
   654d's controlled test (GAP-A armed, gate still locked, n_matched HIGHER) is the
   disambiguation.
2. **maintained != active, now measured.** Holding a differentiated rule's
   availability at 0.45 does not make it fire when 7-8 rules co-match: theta(7)=1.65.
   The conflict gate suppresses the entire maintained pool rather than electing a
   winner. `crf_mean_n_matched` 7-8 + `crf_frac_active` 0.0 is the direct evidence the
   654c autopsy asked for.
3. **Fault 2 is a pure CRF gate calibration, independent of GAP-A.** Coupling
   maintained availability to the per-tick `theta(n_matched)` (maintain at
   `max(maintenance_floor, theta(n_matched)+eps)`), and/or capping `n_competing` in
   theta, and/or sharpening `context_match_threshold` so fewer rules spuriously
   co-match, can be done and validated without any GAP-A dependency.
4. **The 666c churn fix continues to hold.** `max_pairwise_dist` 1.711 and stable
   16-rule minting across all seeds -- the retire-churn / per-episode-wipe lineage is
   resolved. The remaining work is the conflict gate + the context-key separation, not
   pool maturation.

---

## Repair pathway (user-confirmed at the interactive gate, 2026-06-16)

**Route: implement-substrate -- amend `crf-availability-maintenance` at the CRF locus,
UNGATED from GAP-A.** NO 654e budget requeue; NO claim demotion; NO re-gating on GAP-A.
The amend should:

1. **Recalibrate maintenance vs the conflict gate (fault 2 -- pure CRF gate
   calibration, the now-confirmed sole independent blocker):** make a maintained,
   differentiated rule clear the gate under realistic match-crowding -- couple the
   maintained availability to the *actual* per-tick `theta(n_matched)` (maintain at
   `max(maintenance_floor, theta(n_matched)+eps)`), and/or cap `n_competing` in theta,
   and/or sharpen `context_match_threshold` so fewer rules spuriously co-match. Raising
   `maintenance_floor` alone is insufficient (it cannot track a growing `n_matched`).
2. **De-collapse the CRF context KEY at the CRF locus (fault 1 -- distinct from the
   GAP-A E3 channel):** separate the minted rules' `context_tag`s so a small
   differentiated pool does not all co-match one per-tick context. This is NOT the
   ARM_STD_G2 / E3 conversion lever (654d proved that does not reach the CRF match
   context); it is a CRF-internal context-representation / mint-key fix.
3. **Keep the frac_ACTIVE readiness gate (654b rec #3 / 654c rec #3, still unpaid):**
   assert `crf_frac_active >= 0.30` (gate-firing rate) AND record the `crf_n_matched`
   distribution (already instrumented in 654d) before any GAP-B falsifier is scored.
   `crf-availability-maintenance` stays `ready=False` until `frac_active` is
   demonstrated.
4. **Re-queue the GAP-B falsifier (654e) on the CRF amend's frac_active readiness gate,
   NOT on GAP-A.** 654d proved GAP-A de-collapse is the wrong lever for this gate.

**Substrate owner:** the `crf-availability-maintenance` `substrate_queue.json` entry
(amend target; ARC-063 `CandidateRuleField` is the module), under the ARC-062 umbrella.
`unblocks_claims` already lists MECH-309 / ARC-062 / ARC-063. The entry is already
`ready=False` (flipped by 654c); this autopsy adds 654d's failure record and corrects
the re-queue dependency (CRF-locus frac_active gate, NOT GAP-A).

### Draft `evidence_quality_note` (governance writes; this skill does not)

> V3-EXQ-654d (arc_062 GAP-B behavioural falsifier, MECH-309/ARC-062; implementation
> under test = ARC-063 CandidateRuleField) FAILed C1c
> `arm_on_rule_field_differentiated_and_matured` (crf_frac_active = 0.0 < 0.30) for the
> 5th consecutive iteration. 654d ARMED the GAP-A de-collapse lever ARM_STD_G2
> (modulatory selection authority, std basis, gain 2.0, channel routing) on both arms
> AND recorded the discriminator (crf_mean_n_matched). Result
> (failure_autopsy_V3-EXQ-654d_2026-06-16): the GAP-A conversion de-collapse is the
> WRONG LEVER for this gate -- it de-collapses the E3 selection channel
> (consumed_summary spread cleared the 0.05 floor on 2/3 seeds) but NOT the CRF
> rule-match context key. The CRF matched 7-8 rules per tick (crf_mean_n_matched
> 7.08/7.29/8.70, HIGHER than 654c's >=3) and gated EVERY one out: gate_and_select
> theta = 0.15 + 0.25*(n_matched-1) ~= 1.65 >> maintenance_floor 0.45. mean_prop_
> counterfactual_delta = 0.0 confirms the gated-out rule_state never reaches committed
> action. The two CRF-locus faults the 654c autopsy named (context-key crowding +
> maintenance/conflict-gate calibration) remain un-amended (substrate bit-identical to
> 654c); 654d proves they are INDEPENDENT of the GAP-A selection conversion.
> non_contributory (C1 gated scoring; no claim weight). Route: implement-substrate amend
> crf-availability-maintenance at the CRF locus, UNGATED from GAP-A -- couple maintained
> availability to theta(n_matched) (fault 2, pure gate calibration), de-collapse the CRF
> mint/match context key (fault 1, distinct from the E3 channel), keep the frac_ACTIVE
> readiness gate; re-queue 654e on that gate, NOT on GAP-A. pending_retest_after_substrate.
> NO demotion -- the claims were never tested. Substrate-maturation recurrence, not
> claim-granularity debt (user-adjudicated 2026-06-15, re-confirmed 2026-06-16).

---

## Routing

- **routing:** implement-substrate (amend `crf-availability-maintenance` at the CRF
  locus: fault-2 maintenance-vs-theta gate calibration + fault-1 CRF context-key
  separation + frac_ACTIVE readiness gate; re-queue 654e on the CRF frac_active gate,
  UNGATED from GAP-A).
- **recommended_substrate_queue_entry.action:** amend (target = `crf-availability-maintenance`).
- governance applies the writes; this autopsy is analysis + handoff only.
