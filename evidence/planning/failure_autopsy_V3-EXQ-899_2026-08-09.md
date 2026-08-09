# Failure Autopsy — V3-EXQ-899 (ARC-030/MECH-307 G0-readiness diagnostic)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09; presented as part of a 9-target/8-group batch, low-controversy — no reclassification of a filed direction)

## 1. Facts

Manifest `v3_exq_899_arc030_mech307_g0_readiness_20260808T214833Z_v3` (queue_id V3-EXQ-899). Real run (`dry_run` unset, `substrate_hash` present, `elapsed_seconds=19872`, `substrate_commit=da85559c2b`, dirty=false). `experiment_purpose: diagnostic`, manifest `claim_ids: []` (readiness gate; `gates_claims: [ARC-030, Q-021, INV-034]` informationally). `readiness_check_of: V3-EXQ-866a`.

Fourth run in the chain diagnosing why the "G0" foraging-competence readiness gate blocks retesting ARC-030/Q-021/INV-034 (866 -> 866a -> 866c -> 899). Design: single-variable MECH-307 A/B (`use_mech307_conjunction=True/False`) plus a RANDOM reference arm, on 866a's exact FULL `scaffolded_sd054_onboarding` config, 3 seeds.

Readiness gate:

| Item | Frac seeds | Pass |
|---|---|---|
| P1 curriculum_reached_p2 | 1.00 | True |
| P2 p2_window_admits_contact | 0.67 | True |
| **G0_ON (load-bearing)** | 0.00 | **False** |
| G0_OFF (reproduction, non-gating) | 0.00 | **False** |

Preconditions genuinely met (measurement is takeable, `g0_non_degenerate=1.0`). MECH-307 A/B: `d_resource_visit_rate_mean(ON-OFF) = 0.0001`, `mech307_perturbs_baseline = False` — OFF fails G0 just as badly as ON. **MECH-307 reachability is ruled out as the G0 fix.**

Secondary finding: 899's non-gating z_goal readout reuses 866a's stale decay-only P2-mean method, not 866c's same-day-corrected contact-gated peak — a recording-debt note for reuse of this harness, not something affecting the load-bearing G0 verdict (which is `resource_visit_rate`-based).

Dry-run check: clean (`check_dry_run_citations.py`, 0 dry cited).

## 2. Claim-layer mapping

G0 is a pre-registered non-degeneracy precondition gating ARC-030/Q-021/INV-034, not itself a discrimination test of them (confirmed against claims.yaml: Q-021's `what_would_answer` states the G0-equivalent precondition verbatim; INV-034 cross-references Q-021's gate and states a FAIL there is "a competence-floor failure, not evidence against INV-034/Q-021"). Both claims' `live_status.evidence` already cites `failure_autopsy_V3-EXQ-866c_2026-08-08`, `non_contributory/competence_implementation_gap`. 899 extends, does not change, that reading.

ARC-030 itself is not claim-tagged on 866/866a/866c/899 in the autopsy corpus (`granularity_debt_cluster.py ARC-030` shows only unrelated pre-2026-05 runs) — a minor bookkeeping note for governance, not a substantive gap; ARC-030's own decisive test (COMBINED-vs-NOGO_ONLY ablation) is a later, different experiment than this readiness gate.

## 3. Biological-reference triage

No new lit search warranted. The observed phenotype (near-total harm avoidance + near-zero foraging below RANDOM + collapsed near-deterministic policy, entropy ~0) matches the ontogenetic **approach-before-avoidance** ordering already load-bearing for the MECH-457 competence-floor cluster (Debiec & Sullivan 2016; Opendak 2025; Clements 2022; Brunelli 2007; Muller 2018) — active-avoidance systems are quiescent early in altricial-mammal development, appetitive approach is bootstrapped first. The claim's own reference (D1/D2 Go/NoGo BG pathways, Bariselli 2018; wanting/liking, Barch & Dowd 2010) remains untested — the run never reaches that discrimination layer.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (untested, 4th time) | G0 precondition unmet a 4th occurrence; INV-034/Q-021's own mechanism still never fairly exercised |
| Biological reference | clear, unchanged | approach-before-avoidance ordering matches the observed phenotype; claim's own reference untested |
| Dependency prerequisites | missing, cross-claim, reconfirmed | same gap the MECH-457 GOV-FANOUT-1 portfolio targets — but that portfolio's qid (`competence_floor`) is CLOSED to further fan-out as of 2026-08-08 |
| Implementation completeness | MECH-307 wiring confirmed fixed; effect near-zero | plausibly downstream-of-the-floor: MECH-307's anticipatory-conjunction precondition rarely fires when the policy has already collapsed to near-zero foraging |
| Environment adequacy | adequate | RANDOM clears the P2 window-contact floor on 2/3 seeds |
| Measurement adequacy | partially degraded (non-gating diagnostics only) | 899's z_goal non-gating readout uses the stale 866a-style method, not 866c's corrected peak; does not affect the load-bearing G0 result |
| Integration adequacy | isolated, confounded | MECH-307's interaction with the goal/foraging pathway cannot be assessed while G0 blocks foraging contact |
| Scale / capacity | likely insufficient, per the MECH-457 cluster's own read | deficit is the action-learning competence floor, not training budget |

## 5. Re-derive brake (R1-R3)

Ran the counting recipe for Q-021/INV-034. `865a`'s original `substrate_ceiling` reading was superseded (R2) by `866a-G0`'s `competence_implementation_gap`; under R3 only `substrate_ceiling` counts. **Current ceiling-hit count = 0.** Stamping this target `competence_implementation_gap` keeps the count at 0. **Brake does not fire.**

## 6. Learning extracted

1. MECH-307 reachability (from_dims wiring fix, 2026-08-07) is ruled out as the G0 fix — single-variable A/B on the exact 866a config shows near-zero effect, and OFF fails G0 identically to ON.
2. Fourth occurrence of the identical G0 failure shape (866/866a/866c/899), matching the independent MECH-457 competence-floor cluster's own "avoidance without approach" signature.
3. MECH-307's near-zero measured effect is plausibly confounded by the floor itself — integration cannot be assessed until foraging competence clears.
4. 899's non-gating z_goal readout uses a stale method; a recording-debt note for any future reuse of this harness, not a finding against G0 itself.
5. The MECH-457 `competence_floor` hypothesis-space qid is closed to further fan-out (2026-08-08) — a 5th confirmatory instance here should not be grown onto it.

## 7. Routing (confirmed)

**Routing: governance-note-only.** No new `/queue-experiment` or `/implement-substrate` action from this specific run. `recommended_substrate_queue_entry.action: amend` — `target_sd_id: mech457_competence_bootstrap_explorer` (existing entry, `status: blocked_pending_discrimination`), append a `failure_record_entry` for this run strengthening the read that the floor generalizes across harnesses with MECH-307 ruled out as a confound. `scaffolded-curriculum-hazard-rebalance` stays closed (no substrate change warranted there per 866c).

**Step 9b:** no pre-registered hypothesis anywhere references this run or MECH-307, and no qid currently lists claims [INV-034, Q-021, ARC-030]. Per the growth_restriction escape clause, the correct disposition is either a *new*, independently-registered qid for this claim line, or a governance-note-only cross-reference (no ledger write) — deliberately not grown onto the closed `competence_floor` qid. Given this run's routing is governance-note-only (not itself opening a new discrimination campaign), **Step 9b registration is deferred** rather than minted in this pass; a future session opening a dedicated hypothesis-space question for the INV-034/Q-021/ARC-030 G0 line should do so explicitly, not as a byproduct of this autopsy.

## 8. Evidence quality note (for governance to apply)

> [2026-08-09 failure-autopsy, V3-EXQ-899, readiness_check_of V3-EXQ-866a]: G0 non-degeneracy gate FAILED a fourth time (866/866a/866c/899), reconfirming the competence_implementation_gap already diagnosed by failure_autopsy_V3-EXQ-866a-G0_2026-08-08. 899's own contribution: MECH-307 (previously unreachable via from_dims, fixed 2026-08-07) is now confirmed genuinely wired and exercised, but its A/B (FULL_M307_ON vs FULL_M307_OFF, single-variable, same seeds/harness) shows near-zero effect on G0 (d_resource_visit_rate=0.0001, mech307_perturbs_baseline=False) — MECH-307 reachability is RULED OUT as the fix for this gate. The remaining driver is the same shape already load-bearing for the MECH-457 competence-floor cluster (avoidance learned without approach; near-zero policy entropy; forages below random). That cluster's own discrimination qid (competence_floor) is CLOSED TO FURTHER FAN-OUT as of 2026-08-08 (all axis families resolved) — a fifth confirmatory instance does not license a new portfolio leg there. No new /queue-experiment or /implement-substrate action from this run; awaiting mech457_competence_bootstrap_explorer (substrate_queue, blocked_pending_discrimination) OR a fresh, independently-registered hypothesis-space qid for the INV-034/Q-021/ARC-030 G0 line specifically. pending_retest_after_substrate stays true.
