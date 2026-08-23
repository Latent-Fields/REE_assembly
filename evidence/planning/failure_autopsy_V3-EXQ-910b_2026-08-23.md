# Failure Autopsy: V3-EXQ-910b (MECH-489 valence-gating retest, override-tick counter)

**Generated:** 2026-08-23T20:31:37Z
**Scope:** single
**Status:** confirmed (user adopt at Step 8, 2026-08-23T20:31:37Z)
**Target:** V3-EXQ-910b (PASS, `experiment_purpose: diagnostic`, `claim_ids: [MECH-489]`, supersedes V3-EXQ-910a)
**Predecessors (read in full):** `failure_autopsy_V3-EXQ-910_2026-08-10`, `failure_autopsy_V3-EXQ-910a_2026-08-11`

This is a diagnostic PASS. The self-route `orienting_valence_gating_non_degenerate` is a hypothesis, not a verdict.

**Dry-run gate:** clean (`check_dry_run_citations.py` on run_id + V3-EXQ-910b: 1 clean). Manifest `dry_run` absent. Lint `dry_run_unreachable_criterion` does not name this driver. Dry reduction (1 seed, 2 eval episodes) is not cited.
**Recording provenance:** `validate_recording.py --paths` OK. `recording_schema: rec/v1`, `substrate_hash: 421d91d62cbb9785...`, `machine: ree-worker-1` / `linux-x86_64-py3.10-torch2.12.0+cpu`, `elapsed_seconds: 102477`, `seeds: [0,1,2]`. `z_goal_stream.writer_defect: false` (`writer_calls: 152429`). `substrate_stable_across_run: false` is process-snapshot drift over a ~28h run; per-cell hashes agree.

## Facts (recomputed from manifest cells)

2-arm ablation (`orienting_off` / `orienting_on`), seeds `[0,1,2]`, EVAL_EPISODES=48 on the reused 906b observational eval. Scored arm is ON only. OFF is a structural negative control (`use_defensive_orienting=False` forces `n_override_ticks==0`).

Corrected readout (sentinel tap: count decision AT the override tick, synchronously):

| | ON pooled | OFF pooled |
|---|---|---|
| `n_select_calls` | 67198 | 69377 |
| `n_fresh_orienting_ticks` | 11025 | 0 |
| `n_latched_ticks` | 56173 | 69377 |
| `n_trigger_ticks` | 24 | 0 |
| `n_override_ticks` | **21** | **0** |
| `decision_counts` | approach=**19**, withdraw=**2**, resume=**0** | all 0 |
| unclassified | 0 | 0 |

Same-run legacy per-env-step readout (the 910-lineage defect, ON arm): `n_overrides_latched=125`, `decision_counts_latched_sum=684`. Realized inflation: overrides `125/21 = 5.952...`, decisions `684/21 = 32.571...`.

Per-seed ON override ticks / decisions:

| seed | overrides | approach | withdraw | resume | excite chan_std | dread chan_std |
|---|---|---|---|---|---|---|
| 0 | 4 | 4 | 0 | 0 | 4.20 | 0.11 |
| 1 | 2 | 2 | 0 | 0 | 0.87 | 0.06 |
| 2 | 15 | 13 | 2 | 0 | 22650 | 505 |

Seed 2 holds 15/21 overrides (71%) and both withdraws. Seeds 0+1 together are 6/6 approach and would miss `MIN_OVERRIDE_TICKS=10`.

Preconditions (ON arm): fresh ticks 11025 >= 100; latched 56173 >= 1; override ticks 21 >= 10. All met.

Criteria (recomputed; the driver builds `criteria[]` locally but does not emit it into the returned manifest dict):

- **C1** `C_decision_counts_bounded_by_override_ticks`: coded as `sum(decision_counts)==n_override_ticks AND unclassified==0`. The sum is an identity of the tap (denominator and numerator increment in one `if`). Discriminating cells: **unclassified=0** and the **legacy contrast**. Passes.
- **C2** `C_decision_alignment_non_degenerate`: `>=2` of 3 classes nonzero. 19/2/0 -> 2 classes. Passes the pre-registered bar. Does not test valence-tracking.

Context-only (NOT pass criteria; latched log, deliberately uncorrected so comparable to 910/910a): event_trigger_alignment limb 2/608=0.33%, hazard 2/576=0.35%, rule-shift 2/268=0.75%. Trigger-alignment falsifying signature #1 is not re-litigated.

Manifest self-route: `orienting_valence_gating_non_degenerate`. Manifest `evidence_direction: supports`. Executed `substrate_commit: 273191797c`; `775eb55` (2026-08-20 window-expiry amend) is an ancestor.

## Claim-layer map

**MECH-489** (candidate, `mechanism_hypothesis`, `epistemic_category: standard`, `pending_retest_after_substrate: true`, `live_status.evidence.from: failure_autopsy_V3-EXQ-910a_2026-08-11`, mixed). Compound five-component chain. This run is scoped to Components 4/5 (valence-gated decision) only, as 910/910a already required.

Did the experiment test the valence sub-claim under conditions where it could express itself?

- **Instrument (the owed 910a retest):** yes. The driver-half logging defect is measured on real data (legacy contrast + unclassified=0). `pending_retest_after_substrate` was waiting on that driver half -- it can now go false.
- **Valence-gating as "tracks event valence":** no. C2's bar is a two-class floor. Per-override event class was not recorded. The 2 withdraws that clear C2 sit in one numerically wild seed.

Trigger/identification (Components 1-3) was not tested; 910/910a's fairly-hit falsifying signature #1 still stands. identification_confidence-as-decay-tracker (910a) is not re-opened.

Not out-of-domain: the claim's own `what_would_answer` names this lineage's confirming/falsifying signatures. The run is a diagnostic shakeout of the instrument, matching the 2026-08-21 note that diagnostic purpose is retained for this lineage.

## Biological-reference triage

Closest mechanism: Sokolov orienting-reflex arrest-and-release; post-identification valence-gated approach/withdraw (defense cascade). Not a formal-definition import.

Lit status: **present** -- `targeted_review_connectome_mech_489/` (5 entries) and `targeted_review_sd_099/` (4 entries). No `/lit-pull`.

Divergence (unchanged from 910a): `identification_confidence` is a decay-tracker, not epistemic identification. This run does not re-test that. The 90% approach histogram is compatible with this ecology's residue_surprise peaking on resource/boundary events (910 MEASURES finding) once the structural withdraw pin is gone -- untested here because per-override event class was not recorded.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Instrument test was fair and passed. C2's bar is too weak to confirm the valence-gating sub-claim. Trigger sub-claim not in scope and still stands as fairly falsified. |
| Biological reference | partial | Sokolov arrest/release still sound; Component 3 narrative overclaim from 910a unchanged; lit present. |
| Prerequisites | present | All three ON-arm readiness preconditions cleared with margin. |
| Implementation | partial | Scale fix + window-expiry amend are in the executed tree. identification_confidence still a decay-tracker. Valence comparison now produces a mix, not a pin. |
| Environment | adequate | Overrides exist at shipped defaults given EVAL=48. Trigger still does not concentrate on injected hazards (context-only; not scored). |
| Measurement | partial | Override-tick counter is now trustworthy (C1 discriminating cells). C2 cannot test valence-tracking. `criteria[]` not emitted (recording gap, recomputed). |
| Integration | partial | Gate, arrest, override, and decision arithmetic all fire. Orient/identify step still absent (910a). |
| Scale | adequate | 21 genuine override ticks >= 10 floor. Concentration in seed 2 is a robustness caveat, not a sample-size miss at the pooled bar. |

**Failure-location (GOV-FAILLOC-1):** MECHANISM partial (valence mix exists, tracking unshown) + MEASURES partial (C1 adequate, C2 weak bar) + ENVIRONMENT not established as the cause of this PASS. **Net: MIXED.** REE FAILED is not reached.

## Cluster / lineage

Not a new cluster. Single-target retest of 910a's owed instrument repair. 910 and 910a remain confirmed mixed FAILs on their own runs (R2: latest adjudication per run_id; this file does not re-stamp those runs).

Read-across, not adjudicated: V3-EXQ-946 (unclaimed diagnostic PASS, ContextMemory write-address) is a separate pending autopsy. V3-EXQ-861g/861h already covered by the confirmed 861g-861h MECH-180 cluster. MECH-395/482/483 were not tested.

## Learning extracted

1. Driver-half validation is **unclassified=0** plus the same-run legacy contrast (125 vs 21 overrides, 5.95x; 684 vs 21 decisions, 32.57x). The 21==21 sum is an identity of counting in one if-block and cannot fail the inflation defect. Close the **910a** `failure_record` only.
2. C2's pre-registered bar (>=2 nonzero classes) is not a valence-tracking test. 19/2/0 clears it. Resume is 0/21. Both withdraws are in seed 2 (15/21 overrides; extreme excite/dread). Seeds 0+1 are 6/6 approach.
3. Sign flip vs 910/910a (100% withdraw -> 90% approach) is the informative histogram result: the structural withdraw pin is gone. Compatible with (a) z-score fix + this ecology's surprise composition and/or (b) longer eval letting decision MADs leave `scale_floor`. Unmeasured here.
4. Trigger-alignment context-only numbers remain near-zero. Falsifying signature #1 still stands.
5. Recording gap: driver `criteria[]` is computed and dropped from the returned dict. Not a measurement gap.
6. OFF-arm zero is forced by construction and was correctly scoped out of scoring.

## Repair pathway

- `complicated (buildable)` -- close the 910a driver-half item on `SD-ORIENTING-DECISION-SCALE` (`action: amend`, `resolves_prior_failure_record` for the 910a run only). Leave the original 910 item OPEN (target still requires valence-tracking).
- Do **not** queue 910c (same two criteria). A later experiment that tags each override tick with concurrent event class vs decision is a **new** scientific question (new EXQ number), not a letter.
- Granularity-debt trigger **fires as a surface-at-governance signal**, not as this session's primary routing: 2 prior `weakened` targets (910 trigger, 910a measurement) plus this mixed PASS. The remaining split is Components 1-3 fairly falsified vs Components 4-5 instrument-valid but weakly tested. `/claim-synthesis` of the compound claim is for the next `/governance` walk to chip after ratification.

**Re-derive brake:** does not fire. R1-R3 ceiling hits for MECH-489 = 0 (910 and 910a both `standard`; this autopsy also `standard`). Same-question re-queue is still refused because the owed validation has run.

## Step 7b / 7c

**7b:** `fire_count: 0`. C5 inapplicable (no sibling `.md` at check time).

**7c:** CONTESTED ([red-team](a66d7d20-484c-427a-9b35-9ab816a8077e)). Both contests adopted before the gate:

1. Drop original 910 `failure_record` from `resolves_prior_failure_record`.
2. Lead the 910a close-out with unclassified=0 + inflation contrast, not the tautological sum.

Licensed as adopted: mixed direction, `pending_retest_after_substrate: false`, refuse 910c, implement-substrate amend closing **only** the 910a item.

## Routing (confirmed)

**`implement-substrate`** -- amend `SD-ORIENTING-DECISION-SCALE`: resolve the 910a driver-half `failure_record`; leave the 910 valence-tracking item open; do not change `severity`/`substrate_paths`. Flip MECH-489 `pending_retest_after_substrate` true -> false. Append the evidence_quality_note below. Status stays candidate. `epistemic_category` stays `standard`. Manifest self-route `supports` is not to be applied as a clean supports.

Not spawned as a chip from this artifact.

## Draft `evidence_quality_note` (governance should write)

> 2026-08-23 (failure_autopsy_V3-EXQ-910b_2026-08-23): V3-EXQ-910b is a diagnostic PASS whose self-route orienting_valence_gating_non_degenerate must not be applied as a clean supports. C1 (instrument): unclassified=0 and same-run legacy contrast 125 vs 21 overrides (5.95x) / 684 vs 21 decisions (32.57x); the sum identity 21==21 is true by construction of the tap and is not the discriminating test. OFF-arm structural control is 0 overrides by construction. This discharges the DRIVER half of SD-ORIENTING-DECISION-SCALE (the 910a logging defect). Flip THAT failure_record only to resolved and set pending_retest_after_substrate false -- the substrate/driver blockers this flag was waiting on have both now been measured. Leave the original 910 failure_record OPEN: its target still requires a mix that tracks event valence, which C2 does not test. C2 (valence): 19 approach / 2 withdraw / 0 resume clears the pre-registered >=2-class bar, and the structural 100% withdraw pin of 910/910a is gone as a histogram. That is NOT a demonstration that the decision tracks event valence: resume is still 0/21; the 2 withdraws are entirely in ON-arm seed 2 (which also holds 15/21 overrides and an extreme excite/dread chan_std); seeds 0 and 1 are 6/6 approach. Trigger-alignment (context-only, not a criterion) remains near-zero (0.33/0.35/0.75% on the three injected event types) -- 910/910a's falsifying signature #1 is not re-litigated and still stands. Do NOT queue another same-question lettered iteration. Optional later work is a NEW scientific question (per-override event class vs decision), not 910c. Status stays candidate. epistemic_category stays standard. Re-derive brake: 0 ceiling hits. Granularity-debt: 2 prior weakened targets (910 trigger, 910a measurement) plus this mixed PASS -- surface /claim-synthesis of the compound five-component claim at the governance walk; not routed as this session's primary action.

## Step 9b

Skipped. No existing `qid` for MECH-489 / SD-099 / orienting in `hypothesis_space_registry.v1.json`. No `fanout_recommendation`. No growth-restriction to surface.
