# Failure autopsy -- V3-EXQ-1090 (v3_exq_1090_mech449_endogenous_safety_veto_validation_20260925T221242Z_v3)

- Generated: `2026-09-26T10:19:36Z` | Status: **confirmed** (2026-09-26T10:43:53Z, user at /failure-autopsy Step 8 interactive gate (session failure-autopsy-20260926-batch7))
- Batch: failure-autopsy-20260926-batch7 (V3-EXQ-1105a/1067/1106/1107/1099/1104/1090)
- Claims: MECH-449
- bears_on: EVB-1409, substrate_queue:f_dominance_conversion_ceiling, substrate_queue:MECH-279, GFLAG-0508
- Recommendation ledger: rec-20260926-614b94c8, rec-20260926-ae63c5b8
- Dry-run gate: scripts/check_dry_run_citations.py run over all 7 2026-09-25 diagnostic run_ids of this batch: 0 dry, 7 clean.

## 1. Self-route and failed criterion

Self-route `endogenous_veto_fires_candidate_specificity_unmeasured`; failed criterion: **discrimination**.

Does the self-route hold? the label traces, but the reading underneath it changes: the ON-arm agent never varies its executed action (see facts.behaviour), so neither the veto's firing nor its specificity has any behavioural consequence in this run

## 2. Facts (re-measured from the flat manifest and driver)

- **readiness**: 3/5 ON seeds meet the harm-range precondition (exactly at threshold). Seed 43 decayed through P1 (0.0205 -> 0.0161); seed 47's harm head is constant (range 0.0, prox_corr NaN) at both checkpoints despite the most training (4,464 steps).
- **C1**: 3/3 veto applied (331 / 27 / 614)
- **C2**: fire rate 0.033 / 0.006 / 0.052 (ceiling 0.25)
- **C4**: control fire rate 0.0 on 5/5
- **C3**: qualifying mixed ticks 0 / 13 / 1 (need 5 on 2 seeds). On seeds 42 and 46 the veto fires on WHOLE ticks (21/21 and 32/33 fired ticks are all-candidate): within-tick predicted-harm spread median 0.00025 and 0.00005, 80-400x below the 0.02 minimum veto excursion. Seed 45 (spread 0.018) gives 13 mixed ticks, mean gt proximity difference +0.0065. Seed 45's gt_paired_diff_harm_mean is -0.0136 (opposite sign to prox +0.0065); C3 scores prox only (driver :703).
- **lives**: ON-arm eval lives are bimodal: 3-6 steps or the full 200
- **recording**: per-tick rows truncated at 600 and carry ground truth only on mixed ticks, so a tick-level specificity re-score is not possible from the manifest
- **behaviour**: tick_rows[*].executed_action (int(act.argmax()) of select_action's output, driver :465-467) is 0 on 3,000/3,000 ARM_HARM_ON rows across all 5 seeds; the untrained-head control varies (seed 42 control: actions 0-4). use_pag_freeze_gate=True. The process loaded code at start (~2026-09-24 21:30Z), BEFORE 1fc881692d (freeze no-op 0=UP -> STAY, 2026-09-25 09:33Z); the manifest's commit 07b5fe688d (which contains the fix) was resolved at manifest-write time and is not the code that ran. Leading reading: the harm-trained agent is freeze-locked and every tick executes the pre-fix freeze no-op UP -- the same lock as V3-EXQ-1106 (100% frozen) and V3-EXQ-1107 (post-fix STAY, 6-step deaths). Lives are bimodal (3-6 or 200 steps), consistent with walking UP into a hazard or pinning against the wall. GFLAG-0508 names 1090 as straddling the fix.
- **all_fired_path**: on all-fired ticks e3_selector.py:2440-2450 executes the strongest-F vetoed candidate anyway (selected_vetoed true, envelope 1) -- the veto is an inert alarm, not a tick-wide stop

## 3. Four-layer diagnosis

| Layer | Reading |
|---|---|
| claim_alignment | could not express -- the producer fires, is calibrated (C2) and silent on a flat head (C4), but the ON-arm agent's executed action never varies, so the safety No-Go cannot shape behaviour in this run. |
| biological_reference | partial -- BG No-Go opponency (Kravitz 2010; Mink 1996), filed under targeted_review_connectome_mech_439/ARC107_GROUNDING_SYNTHESIS. No source grounds a running-z harm veto specifically. |
| prerequisites | partial -- the harm head is discriminative across REAL states on 3/5 seeds but nearly flat across the CANDIDATES within a tick on 2 of those 3. Upstream candidate homogeneity (the MECH-439 / f_dominance_conversion_ceiling lineage) or harm-head resolution over predicted states. |
| implementation | complete -- the producer computes as specified (contract test present). |
| environment | inadequate -- a freeze-locked (or action-monostrategic) harm-trained agent; see facts.behaviour. |
| measurement | under-instrumented -- C3 can only be read on mixed ticks, which a near-homogeneous candidate set rarely produces; ground truth is not recorded on whole-tick fires, so a tick-level specificity reading is impossible after the fact. |
| integration | coupled but inert by STARVED UPSTREAM -- the veto's output reaches selection, but the executed action is fixed downstream (freeze override / monostrategy), so there is nothing for it to change. |
| scale | readiness is fragile: exactly 3/5 at threshold, with one collapsed head. |

**Failure location (GOV-FAILLOC-1):** mechanism established, measures not_established, environment not_established, REE failed: False. Net: ENVIRONMENT/harness (freeze-locked or monostrategic ON-arm agent) + MEASURES (candidate-level criterion unreadable; no action-diversity precondition), not chargeable to REE.

## 4. Biological reference

indirect-pathway No-Go opponency (Kravitz 2010) -- divergence: running-z veto over an abstract candidate set; lit: partial.

## 5. Recommendations

- evidence_direction: `non_contributory`; epistemic_category: `standard`
- Draft evidence_quality_note: [2026-09-26 failure_autopsy_V3-EXQ-1090] Endogenous safety producer validation FAIL endogenous_veto_fires_candidate_specificity_unmeasured: fires on 3/3 scored seeds (C1), calibrated (fire rate <=0.052, C2), silent on the untrained-head control (0.0 on 5/5, C4). Specificity (C3) unmeasured AND behaviourally moot: the ON-arm executed action is 0 on 3,000/3,000 recorded ticks (freeze gate on, pre-STAY-fix code) so the veto cannot change behaviour; on all-fired ticks the strongest-F vetoed candidate executes anyway. EVB-1409 release condition (b) NOT met. Diagnostic, non_contributory; status unchanged.
- **MECH-449**: change `append the drafted evidence_quality_note; stamp this artifact`; none -- stays provisional
- Substrate queue: ```{
 "action": "none",
 "note": "the producer is not defective; the upstream candidate-homogeneity question already lives in f_dominance_conversion_ceiling"
}```
- Re-derive brake: {'fired': False, 'threshold': 2, 'note': 'category standard; MECH-449 0 ceiling hits'}

## 6. Routing

**implement-substrate** -- Blocked on the freeze-lock finding (GFLAG-0508; V3-EXQ-1107 artifact, MECH-279 amend): no 1090a until the harm-trained agent behaves. Then 1090a (same question -> letter) with an action-diversity precondition, gate-off freeze or a recalibrated freeze threshold, per-tick ground truth on every tick (untruncated), and 8 ON seeds.


Spawned follow-on: {'chip_ref': 'chip-20260926-pag-freeze-lock-confirmer', 'task_id': 'task_ad36ff97', 'why': 'user overrode the autopsy-does-not-chip-its-own-routing rule for this item at the gate (rec-20260926-ae63c5b8) because queued freeze-gated runs may be burning compute'}

## 7. Hypothesis-space ledger (Step 9b)

No registered question names this run or its claims and no fan-out was emitted: nothing to register.

## 8. Learning extracted

- A selection-layer veto validated on an agent whose executed action never varies validates arithmetic only; require an action-diversity precondition.
- Record ground truth on every tick (including whole-tick fires) so tick-level specificity can be re-scored.
- The 866b harm regime is less robust at 5 seeds than its 3/3 suggested: readiness landed exactly at threshold with one collapsed head.
- Long runs resolve substrate identity at manifest-write time and mislabel the code that ran (same defect as 1067).

## 9. Checks

- Step 7b pre-routing checks: no fires
- Step 7c red-team (Step 7c red-team run on fable (cross-model; drafter opus)): {'model': 'fable', 'verdict': 'CONTESTED', 'applied': "executed action constant -> veto behaviourally inert; 'tick-wide stop' withdrawn (inert alarm); harm-sign discrepancy on seed 45 stated; 1090a needs action-diversity precondition; routed behind the freeze-lock finding", 'file': 'redteam_A.md'}

Granularity-debt recurrence trigger: does NOT fire (no target in any of this run's claim clusters reads `weakened` with structurally different signatures attributable to this run; this run's own claim_alignment is n/a / could-not-express).
