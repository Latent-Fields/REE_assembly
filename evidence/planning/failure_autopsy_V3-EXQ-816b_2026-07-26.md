# Failure Autopsy: V3-EXQ-816b (P-A env-harshening leg)

**Generated:** 2026-07-26T14:37:45Z
**Status:** confirmed (user-confirmed 2026-07-26, inline under governance session `optimistic-ellis-4357c6`)
**Scope:** single (GOV-FANOUT-1 P-A leg of the `policy_decomposition_discrimination` question)

## Facts

- Run: `v3_exq_816b_mech321_policy_decomposition_harshened_env_20260726T123216Z_v3`
- `experiment_purpose: diagnostic`, `claim_ids: []`, `bears_on: [ARC-070, MECH-321]`
- Outcome: FAIL. Load-bearing criterion `C_LOWVS_harshened_env_produces_low_vs` failed: worst-cell `low_vs_steps=0` vs floor 5 (same shape as V3-EXQ-816/820).
- Harshening applied: `env_drift_interval=3`, `world_rule_shift_enabled=True`, `world_rule_shift_interval=24`, `world_rule_shift_depth=1`. Seeds: [11, 23, 47, 71, 97].
- The disambiguating readout this run exists to record: `off_pe_mean_worst = 0.0086` vs `PE_ELEVATED_FLOOR = 0.01` → `pe_elevated = false`. Forward-PE moved from the 816/820 baseline (~0.005) toward the floor but did not cross it.
- Readiness preconditions (`vs_tracking_live`, `off_forward_pe_varies`, `off_forward_pe_bounded`) all met — this is a clean, correctly-instrumented negative, not a broken/starved run like 816/820 were.
- `C_SECONDARY_lowvs_forward_pe_reduced` is degenerate (`non_degenerate: false`) — no low-V_s states existed to test it.

## Self-route verdict

Self-route label `env_still_underdrives_uncertainty` **matches the data**. The experiment's own pre-declared null-reading guide anticipated exactly this branch: "low-V_s absent AND forward-PE NOT elevated → the harshening was insufficient... H-env not refuted, just not yet confirmed." Contrast with 817/819 in the same governance cycle, where the self-route label was a misnomer for what the data actually showed.

## Claim-layer mapping

ARC-070 (`policy.decomposition_on_prediction_failure`) and MECH-321 (`policy.decomposition_via_event_segmenter`) are both `candidate` / `v3_pending`. This run is diagnostic (`claim_ids: []`) and bears on both without weighting them — no change to their status is implied.

## Biological-reference triage

Closest mechanism: PE-driven event segmentation (Zacks 2007) on imagined continuation, with chunk-size bounds (Sakai 2003). Unchanged from the 816/820 autopsy — this run adds a dose-response datapoint, not a new divergence. `lit_status: present`.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested) | R1 trigger still not behaviourally exercised |
| Biological reference | clear | PE-driven event segmentation; unchanged |
| Prerequisites | present | forward model + region-V_s tracking + (new) full distributional recording |
| Implementation | complete | harshening + expanded recording both worked as designed |
| Environment | insufficient magnitude, right axis | PE moved 0.005→0.0086, short of the 0.01 floor |
| Measurement | adequate, improved | full per-cell region-V_s + forward-PE distributions now recorded (closes 816's gap) |
| Integration | isolated | unchanged |
| Scale | adequate | 5 seeds sufficient to establish the dose-insufficient finding cleanly |

## Recommended disposition

- `epistemic_category`: `standard` (both claims)
- `evidence_direction`: `non_contributory` (both claims) — bears_on only, no weight change
- `recommended_substrate_queue_entry.action`: `none`
- `re_derive_brake`: not fired (0 confirmed substrate_ceiling autopsies for either claim; this reading is `standard`)
- `routing`: **queue-experiment** — a further environment-axis letter with a stronger harshening dose (e.g. `world_rule_shift_depth` 1→2 and/or `env_drift_interval`→1), rather than pivoting directly to the P-B measurement-comparator probe (which presupposes PE is already elevated to be informative)

## Hypothesis-space ledger (Step 9b, Mode B resolve)

Resolves the leg `H-env-underdrives-uncertainty` under question `policy_decomposition_discrimination` (pre-registered by `failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26.json`). Result is informative-but-non-eliminating: does not meet the elimination bar (dose insufficient, direction correct) — hypothesis **stays alive** pending a stronger-dose retest.

## Learning extracted

1. Harshening via `env_drift_interval→3` + `world_rule_shift` (interval 24, depth 1) moves forward-PE in the right direction but does not cross the 0.01 discrimination floor — a dose problem, not a wrong-lever problem.
2. The 816/820 recording gap (only the derived `low_vs_steps` count, not the underlying distributions) is now closed for future legs on this ladder.
3. PE reaching ~86% of the floor on the first harshening attempt suggests one more dose step is the efficient next move before spending on the P-B probe.
4. First pure-diagnostic autopsy hit on the `policy_decomposition_discrimination` bears_on token (GOV-DIAG-1 count: 1 of 3) — not a recurrence concern.

## Routing (user-confirmed 2026-07-26)

Queue-experiment a next letter (environment axis, stronger dose) continuing the same hypothesis before running the already-pre-registered P-B probe. Not a substrate gap; not a ceiling; not a re-derive-brake circle.
