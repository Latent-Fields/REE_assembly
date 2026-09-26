# Failure autopsy -- V3-EXQ-1106 (v3_exq_1106_mech287b_stage0_lock_precondition_20260925T164510Z_v3)

- Generated: `2026-09-26T10:19:36Z` | Status: **confirmed** (2026-09-26T10:43:53Z, user at /failure-autopsy Step 8 interactive gate (session failure-autopsy-20260926-batch7))
- Batch: failure-autopsy-20260926-batch7 (V3-EXQ-1105a/1067/1106/1107/1099/1104/1090)
- Claims: MECH-287
- bears_on: chip-20260925-mech287-lock-dv-path-decision, GFLAG-0506, substrate_queue:staleness_within_episode_peak_tracker, GFLAG-0508
- Recommendation ledger: rec-20260926-614b94c8, rec-20260926-78ecb89a
- Dry-run gate: scripts/check_dry_run_citations.py run over all 7 2026-09-25 diagnostic run_ids of this batch: 0 dry, 7 clean.

## 1. Self-route and failed criterion

Self-route `path_built_not_reached_in_regime`; failed criterion: **absolute**.

Does the self-route hold? yes -- S0-3 counter is 0 on 3/3 seeds and is not pinned by alpha = 0 (the counter increments on drive > 0 independent of alpha, agent.py 6937-6959)

## 2. Facts (re-measured from the flat manifest and driver)

- **S0_1**: lock reproduces: freeze-active 1.0, lock persistence 1.0 on every cell
- **S0_2**: median lock ratio 1.74 -> alpha 1.0
- **S0_3**: drive-steps-while-frozen 0/0/0 in the reach arm; eval H events 0 in all 6 cells
- **predicted_before_run**: ree-v3/docs/substrate/MECH-287-pag-descending-release-option-b.md (same day): T3 half redundant (the boundary's dual-trace remap deactivates segment_id_old BEFORE the broadcast is applied, so a broadcast finds no active target); untrained 1097 D_BOTH_ON rollout gave 0 T3, 0 H. Driver F3: H suppressed while frozen under MECH-284.
- **regime**: a 100%-frozen eval is a regime in which the events the path reads (new boundaries, staleness) cannot accrue -- the agent does not move
- **decision_record_conflict**: chip-20260925-mech287-lock-dv-path-decision resolved 2026-09-25T08:00:53Z: 'USER DECISION 07:58Z (live): B -- build a substrate path ... then test on the lock DV'. GFLAG-0506 resolved 11:52:17Z as option (A) (re-anchor the DV on E3 commitment perseveration / avoid-mode monostrategy) via governance-20260925's bulk 'Accept all recs' over 86 flags (rec-20260925-deedce42), and claims.yaml MECH-287 now records option A 'rather than (B)'. The option-B build (ree-v3 aa14769, 14:46Z) and this Stage-0 run followed the 07:58Z decision. Two contradictory user decisions are on record. Refinement (red-team): GFLAG-0506 was raised 07:54Z; the B decision at 07:58Z lives only in the chip ledger (resolution note) with no RECOMMENDATION_LOG row, so the 11:29Z governance session re-decided a flag that was already stale.
- **staleness_leak**: open substrate entry staleness_within_episode_peak_tracker records MECH-284 staleness magnitude destroyed by leak before readout (1097 dry run: peak 0.43 vs post-loop 0.0) -- a further reason the H source may never fire
- **freeze_lock_context**: GFLAG-0508 (open): pre-fix freeze-gated runs walked UP when frozen; 1106 ran post-fix and shows the true lock (100% frozen).

## 3. Four-layer diagnosis

| Layer | Reading |
|---|---|
| claim_alignment | n/a -- Stage-0 precondition gate; tests no claim hypothesis. |
| biological_reference | partial -- PAG descending control of freezing and its release by contextual change (targeted_review_waking_v_s_invalidation). Biology releases freeze on new information; this substrate cannot generate new information while frozen. |
| prerequisites | present -- the lock exists (S0-1) at a bounded ratio (S0-2). |
| implementation | partial -- coupled but inert by DEFECT: the path reads a source that is structurally absent in the regime it targets (T3 neutralised by remap-before-broadcast ordering; H suppressed while frozen). |
| environment | partial -- total catatonic lock gives the path nothing to read. A self-referential regime: escape requires the events that the lock prevents. |
| measurement | adequate -- gate ticked, reach arm frozen, counter independent of alpha. |
| integration | coupled but inert -- missing link: no consumer-reachable source (no event reaches the path while frozen). |
| scale | adequate for a count criterion. |

**Failure location (GOV-FAILLOC-1):** mechanism partial, measures established, environment partial, REE failed: False. Net: MIXED (MECHANISM source-starved + ENVIRONMENT self-locking regime), not chargeable to REE.

## 4. Biological reference

PAG freeze with descending release on contextual change -- divergence: no movement-independent invalidation source; lit: partial.

## 5. Recommendations

- evidence_direction: `non_contributory`; epistemic_category: `standard`
- **MECH-287**: change `STANDS`; none -- stays candidate
- Substrate queue: ```{
 "action": "none",
 "note": "The option-B path stays default-OFF and inert. Whether anything more is built depends on which MECH-287 decision stands (B at 07:58Z vs A at 11:52Z)."
}```
- Re-derive brake: {'fired': False, 'threshold': 2, 'note': 'category standard; MECH-287 1 prior target (gflag0452-D1, standard)'}

## 6. Routing

**governance** -- USER DECISION at this gate (rec-20260926-78ecb89a): option A STANDS -- re-anchor MECH-287's lock DV on E3 commitment perseveration / avoid-mode monostrategy (EXQ-471 regime), as already recorded in claims.yaml and GFLAG-0506. The 07:58Z option-B chip resolution is superseded. The built option-B path (ree-v3 aa14769) stays parked default-OFF. Do NOT queue Stage 1. The active orchestrator claim orchestrate-20260924-breakthrough-c2 ('resume ... MECH-287b') should not resume MECH-287b work.


## 7. Hypothesis-space ledger (Step 9b)

No registered question names this run or its claims and no fan-out was emitted: nothing to register.

## 8. Learning extracted

- A release path that reads movement-generated events cannot release a lock that stops movement; the path needs a movement-independent source.
- The 0 was predicted in writing by the build doc before the run; Stage 0 confirmed it at full scale.
- Two user decisions on one chip contradict each other (07:58Z B vs 11:52Z A via bulk acceptance); a bulk flag-agenda acceptance can silently reverse a live decision.

## 9. Checks

- Step 7b pre-routing checks: {'C2': 'ACTED -- staleness_within_episode_peak_tracker (misleading; MECH-284 staleness leak destroys magnitude before readout) is a second candidate reason the H route is silent and is now named; pag_freeze_gate_phase_scoped_recommit_readout (corrupting) concerns cumulative-counter ratios this driver does not read (it snapshot-differences); MECH-288 and its BOCPD rail are upstream event sources, unchanged. No new entry.'}
- Step 7c red-team (Step 7c red-team run on fable (cross-model; drafter opus)): {'model': 'fable', 'verdict': 'CONFIRMED', 'applied': 'stale-flag refinement added', 'file': 'redteam_B.md'}

Granularity-debt recurrence trigger: does NOT fire (no target in any of this run's claim clusters reads `weakened` with structurally different signatures attributable to this run; this run's own claim_alignment is n/a / could-not-express).
