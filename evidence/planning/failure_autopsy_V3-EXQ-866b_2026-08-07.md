# Failure Autopsy: V3-EXQ-866b (SD-059 / MECH-358 substrate regression check)

Generated: `2026-08-07T20:04:51Z`
Status: **confirmed**
Scope: single
Trigger: `experiment_purpose: "diagnostic"` PASS with no confirmed adjudication (2026-08-07 policy: every diagnostic result, PASS or FAIL, needs a confirmed autopsy — not only flagged ones).

## 1. Dry-run gate

`scripts/check_dry_run_citations.py v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3` → 0 dry, 1 clean. Confirmed real run (`dry_run` key absent from manifest but full-budget arithmetic — 3 seeds × full curriculum episode counts — is present throughout; no truncation signature).

## 2. Facts

**Run**: `v3_exq_866b_603q_substrate_regression_check_20260803T192405Z_v3`, queue_id `V3-EXQ-866b`, `experiment_purpose: diagnostic`, `claim_ids: [SD-059, MECH-358]` (tagged for discoverability only — `evidence_direction: non_contributory` throughout, `scoring_excluded: "diagnostic_probe"` in the index; this run cannot move either claim's confidence by design).

**What it checks**: a byte-identical re-run of V3-EXQ-603q's `ARM_BASE_IA_ONLY` config (config parity already verified line-by-line in the 866a autopsy) on seeds 42/43/44, through the same 5-stage curriculum, checking whether the current substrate still reproduces 603q's `base_mean_survival=37.725`. It exists solely because **V3-EXQ-866a** (INV-034/Q-021 goal-maintenance test, ported onto the same scaffolded curriculum) failed its own G0 gate and showed Stage-H survival ~7x below 603q's reference plus a z_goal collapse (Stage-0 peak ~0.5 → P2 mean 0.12) — and 866a's confirmed autopsy could find no config difference to explain the gap, so it routed exactly this diagnostic: "re-run 603q's own script fresh, unmodified, to isolate substrate drift from one-off seed variance without touching the INV-034/Q-021 design."

**Decision rule** (from the driver): `readiness_met` (curriculum reaches Stage-H on ≥2/3 seeds AND Stage-0 z_goal forms on ≥2/3 seeds) → then `reproduces` iff `base_mean_survival >= 0.5 * 37.725 = 18.8625`.

**Result**: readiness met (all three preconditions `met: true` — curriculum_reached_hazard_stage 1.0, stage0_forced_feed_lights_zgoal_on_base 0.667 exactly at the 2/3 boundary, survival_measured_non_starved 1.0). `base_mean_survival = 33.9`, ratio vs reference `0.8986` — comfortably clears the 18.86 floor (in fact within ~10% of the reference itself). → PASS, label `substrate_reproduces_603q_reference`.

**Per-seed detail** (the load-bearing statistic is arm-mean, not per-seed): seed 42 = 29.1 (per-seed gate: fail), seed 43 = 20.45 (fail), seed 44 = 52.15 (pass). Only 1/3 seeds individually clears its own Stage-H gate (`g_h_frac=0.333`) — but 603q's own per-seed reference spread was similarly wide (67.6/9.1/36.4), so this is consistent with the task's known seed-variance, not new information.

**z_goal trajectory** (secondary DV, non-gating): mean holds at ~0.41–0.47 across all curriculum stages on all three seeds — it does **not** reproduce 866a's decay pattern (Stage-0 peak ~0.5 → P2 0.12) at all.

**Harm-landscape localization diagnostic** (non-gating): `per_seed_harm_eval_range = [0.470, 0.295, 0.115]`, `harm_landscape_discriminative_frac = 1.0` — all three seeds produced a non-flat, discriminative harm-eval landscape, unlike the flat ~0.002 signature of the older 603i defect.

**Substrate-hash provenance** (found while reading the manifest, not flagged by the indexer): all three seeds' process-snapshot hashes agreed with each other at seed-cell start (`bb755658…`), but the top-level manifest's `substrate_hash` (`8e275408…`, matching `substrate_commit.commit = c4247794…`) was taken ~2h26m later at manifest-write time and **disagrees** with the seed-cells' own snapshot. `substrate_stable_across_run: false` is self-reported in the manifest. `elapsed_seconds` is absent from the manifest (cannot independently corroborate the gap from that field, though the two recorded UTC timestamps — 16:58:16Z snapshot vs 19:24:05Z manifest-write — give the same ~2.5h figure).

**Recording**: always-core fields present (`recording_schema`, `substrate_hash`, `substrate_commit`, `machine=ree-worker-3`, `machine_class=linux-x86_64-py3.10-torch2.12.0+cpu` — matching 603q's required cloud machine-class per the driver's own machine-class caveat, `config`, `seeds=[42,43,44]`). `elapsed_seconds` absent.

## 3. Claim-layer map

SD-059 (escape-affordance-bridge architecture) and MECH-358 (its instantiating mechanism) are tagged on this run for discoverability only — the manifest's own `evidence_direction_per_claim` is `non_contributory` for both, and the claim-evidence index structurally excludes this run from scoring (`scoring_excluded: "diagnostic_probe"`, `confidence: 0.0`). A byte-identical config re-run of 603q cannot itself generate new evidence about SD-059/MECH-358 — it can only certify whether the *substrate* underlying 603q's original PASS is still stable. Both claims currently carry exactly one genuine experimental entry (603q itself, `genuine_exp_count: 1` for each), `pending_retest_after_substrate: false` (cleared 2026-06-17 by 603q). This run does not change that picture either way.

**Cross-claim note**: SD-058's own `evidence_quality_note` already characterizes 866b as having "reconfirmed" SD-059/MECH-358's 603q evidence — but SD-059's and MECH-358's own notes have not been updated to mention 866b at all. That inconsistency is exactly what a confirmed autopsy is supposed to gate before governance writes anything; this autopsy is that gate.

## 4. Biological-reference triage

Not applicable in the usual sense — this is a pure substrate-integrity check (does the current `ree_core` tree reproduce a prior numeric result), not a test of a biological mechanism. SD-059/MECH-358's own biological grounding (Moscarello & LeDoux 2013 ilPFC relief/safety pathway; Martinez-Rivera et al. 2018 PL/IL→BLA/ventral-striatum tracing) is unaffected by this run either way.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (non_contributory by design) | Tagged for discoverability only; cannot move SD-059/MECH-358 confidence |
| Biological reference | n/a | Substrate-integrity check, not a mechanism test |
| Developmental / dependency prerequisites | present | Same scaffolded curriculum already validated (V3-EXQ-514o contact-rate ceiling cleared) |
| Implementation completeness | complete | Byte-identical config re-run, verified line-by-line against 603q |
| Environment adequacy | adequate | Same 5-stage curriculum, same seeds |
| Measurement adequacy | **partial** | Substrate-hash provenance disagrees between seed-cell-start snapshot and manifest-write time (2.5h apart) — the run's own purpose is verifying stability, and its own provenance chain shows instability |
| Integration adequacy | n/a | Single-arm check |
| Scale / capacity | adequate | Arm-mean statistic clears the pre-registered floor comfortably; per-seed spread matches the reference's own spread |

## 6. Learning extracted

1. **The numeric "reproduces 603q" verdict is sound and should be accepted** — the load-bearing statistic (33.9 vs an 18.86 floor, ratio 0.90 of the reference) clears comfortably, and per-seed variance is consistent with 603q's own spread rather than novel.
2. **The substrate-hash drift is a genuine recording/provenance gap, not a science finding.** A run whose entire purpose is confirming substrate stability recorded two disagreeing hashes for what "the substrate" was during its own execution. This does not invalidate the survival numbers (all three seeds' own process snapshots agreed with each other), but it means the top-level `substrate_hash` field cannot currently be trusted to describe what actually ran on a multi-hour shared-hub-checkout run. **Recommend a scripts/tooling fix**: capture (or additionally record) the substrate hash at seed-cell completion time, not only at manifest-write time, for any diagnostic whose verdict depends on substrate identity.
3. **866a's own "harness-specific decay" explanation is now unsupported.** 866a's routing assumed its ~7x survival shortfall and z_goal collapse (peak 0.5 → 0.12) were explained by something specific to 866a's own harness (not a real regression) — but 866b's byte-identical re-run of 603q's actual config shows z_goal *holding steady* (~0.41–0.47) rather than collapsing. Since 866b's survival number does independently confirm the substrate is stable, the "substrate stable" conclusion stands — but *why 866a specifically diverged* (both in survival magnitude and z_goal trajectory shape) from both 603q and 866b remains genuinely unexplained. This is a `mystery (known data)`, not a `puzzle` — the data (866a's numbers, 866b's numbers) already exist; the frame ("harness-specific") that 866a's autopsy used to explain the gap no longer fits. Not blocking: 866a's own scientific question (INV-034/Q-021) already moved forward under its own routing. Flagged here so it is available if INV-034/Q-021 work resumes and needs to explain what actually happened in 866a.

## 7. Repair pathway / routing

- **Recommended `epistemic_category`**: `standard` (self-contained instrument-health check; does not touch SD-059/MECH-358 scoring).
- **Recommended `evidence_direction`**: unchanged — `non_contributory` (by design, both claims).
- **Recommended `recommended_substrate_queue_entry.action`**: `none`. This is not a substrate gap — it is a recording/provenance gap in the diagnostic harness itself, not in `ree_core`.
- **Routing**: infrastructure/tooling finding, not a claim-level action. Recommend flagging for a scripts fix (capture substrate hash at seed-cell completion, not only manifest-write time) via a spawned follow-on task — not itself `/failure-autopsy` or `/governance` work, so per CLAUDE.md's chip-everything-else rule this should be chipped rather than reported-and-dropped.
- **Draft `evidence_quality_note` addendum for SD-059 and MECH-358** (both identical): *"[2026-08-07 governance: V3-EXQ-866b (confirmed autopsy, failure_autopsy_V3-EXQ-866b_2026-08-07) re-confirms 603q's substrate-reproduction: base_mean_survival=33.9 vs reference 37.725 (ratio 0.90), clears the 0.5x floor. Non_contributory by design (byte-identical config re-run; scoring_excluded='diagnostic_probe'), does not change confidence or pending_retest_after_substrate. Note: the run's own substrate-hash provenance disagreed between seed-cell-start and manifest-write time (~2.5h apart) — treated as a recording-harness gap, not grounds to distrust this run's own internally-consistent per-seed numbers.]"*

## 8. User confirmation (Step 8 gate)

User selected: **"Accept as clean, flag hash drift as recording gap"** — treat the survival-reproduction verdict as valid; record the hash-drift as a provenance/recording gap for a future fix; separately note that 866a's "harness-specific decay" explanation is now unsupported by 866b's own z_goal data, reopening (as an unexplained mystery, not a blocking issue) what actually explains 866a's shortfall.
