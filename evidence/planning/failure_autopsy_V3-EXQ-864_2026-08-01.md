# Failure Autopsy: V3-EXQ-864 (SD-076 WCI/RV trajectory crossover diagnostic)

- **Generated:** 2026-08-01T21:50:27Z
- **Scope:** single
- **Status:** confirmed
- **Run ID:** `v3_exq_864_sd076_wci_rv_trajectory_crossover_diagnostic_20260801T195304Z_v3`
- **Queue ID:** V3-EXQ-864 (removed from queue on completion)
- **Claim(s):** SD-076 (also bears on MECH-204's EVB-0454 decision context)
- **Fanout source:** `failure_autopsy_V3-EXQ-860_2026-08-01.json` (this run is the directly-commissioned follow-up)
- **dry_run_checked:** true (`scripts/check_dry_run_citations.py` — 0 dry cited, clean; a separate `--dry-run` manual smoke signal file exists at 20260801T190217Z but is not the scored run)
- **Machine:** ree-worker-3, `linux-x86_64-py3.10-torch2.12.0+cpu`
- **Recording provenance:** full always-core present in the flat manifest (`recording_schema`, `elapsed_seconds: 654.6`, `config`, `seeds: [0,1]`); the nested runs-pack lacks these fields (thin-pack, advisory-only).

## 1. Facts

**Why this run exists.** V3-EXQ-860's confirmed autopsy found `inflation_lowers_rv` (the SD-076 readiness criterion comparing the inflated/asymmetric-EMA `_running_variance` path against its symmetric-EMA counterfactual) flipped **wrong-signed** at 5x longer episodes (`STEPS_PER_EP=1000` vs the 200 used in 850/853): LO -2.76e-4, HI -1.46e-4 against a +1e-4 threshold, having been small-positive-but-sub-threshold at shorter episodes. 860's autopsy explicitly recommended chipping a follow-up diagnostic to instrument the trajectory (not just the end-of-episode value) rather than let it block the SD-076/MECH-204 EVB-0454 decision. V3-EXQ-864 is that follow-up: a cheap (`N_TRAIN_EPS=8` vs 860's 30), 2-arm × 3-step-count × 2-seed sweep of `steps_per_ep` in `{200, 500, 1000}`, instrumenting `diff_final = wci_symmetric_rv_ref_final - rv_final_after_training` across the sweep to bracket where (if anywhere) the sign flips.

**Result.** PASS, `interpretation.label = "wci_rv_trajectory_characterized_no_crossover_in_range"`. All 18 readiness preconditions (6 cells × 3 preconditions: `rv_live`, `f1_recalib_engaged`, `trajectory_non_degenerate`) met. C0 `trajectory_data_usable` (load-bearing) passed. C1 `crossover_bracketed_in_swept_range` (non-load-bearing, descriptive) failed for both arms — `diff_final_by_steps` reads **bit-identical** across all three swept values in both arms and both seeds (e.g. ARM_INFL_LO: -0.008332025904674908 at 200, 500, AND 1000 steps_per_ep), `sign_sequence: [negative, negative, negative]`, `crossover_bracket_steps_per_ep: null`.

**Root cause (code-verified, not inferred).** `_run_cell()` (`ree-v3/experiments/v3_exq_864_...py:371-487`) correctly threads `steps_per_ep` into the training-tick loop bound (`for t in range(steps_per_ep)`, line 403) and the trajectory-sampling interval (`interval = _sample_interval(steps_per_ep)`, line 373). But line 423-424 breaks the loop early on `if result.done: break`. `CausalGridWorldV3`'s own `done` condition (`ree_core/environment/causal_grid_world.py:2892`) is `agent_health <= 0.0 or self.steps >= 500` — independent of the experiment's `steps_per_ep` argument. The per-seed trajectory data confirms episodes terminated far short of even the 200-step floor: `global_tick` reached only ~62-88 across 8 episodes (roughly 8-11 ticks/episode on average), well below all three swept values. Because `env.reset()`/seeding is identical across the three `steps_per_ep` values for a given (arm, seed) cell, and the `range(steps_per_ep)` loop bound never actually binds (the environment's own termination always fires first), the realized episode content — and hence `rv_final`, `wci_symmetric_rv_ref_after_training`, `diff_final`, `recalib_cycles_fired` — is identical regardless of the nominal `steps_per_ep` configured. Only the trajectory-**sampling** cadence (`interval` = 5/12/25, hence `trajectory_n_samples` and the last-sampled `global_tick`) differs between the three sweep points, because `interval` scales with `steps_per_ep` even though the underlying episode never reaches it — confirmed by `trajectory_non_degenerate`'s measured values genuinely varying by step count (LO: 0.0815/0.0655/0.0493) while every value derived from the *final* post-episode state does not.

**Consequence: the sweep never varied real exposure.** `crossover_bracket_steps_per_ep: null` is not evidence that no crossover exists in the range 200-1000 — the driver never actually tested three different exposure levels, only one (governed entirely by the environment's own 500-step/death cap), sampled three different ways. The "characterized, no crossover in range" label is uninformative on the question it was built to answer. **V3-EXQ-860's wrong-signed `inflation_lowers_rv` puzzle remains genuinely unresolved.**

**Deadline discrepancy found in passing.** `experiment_proposals.v1.json`'s EVB-0454 entry (`items[6]`) states `decision_deadline_utc: "2026-08-04T21:09:57.681848Z"`. Every other reference to this deadline — MECH-204/SD-076's `claims.yaml` notes, V3-EXQ-860's autopsy, and V3-EXQ-864's own driver docstring — cites `2026-08-03T20:50:36Z`. These are two different timestamps (roughly 24h apart) for what should be one decision deadline. `experiment_proposals.v1.json` is the source-of-truth schema for `decision_deadline_utc` per the EXQ versioning/decision-tracking convention; recommend governance correct the `2026-08-03T20:50:36Z` citations to match `experiment_proposals.v1.json`'s `2026-08-04T21:09:57Z`, or investigate which is actually authoritative before the next EVB-0454-adjacent write.

## 2. Claim-layer mapping

**SD-076** (`docs/claims/claims.yaml`): design_decision, status `candidate`, `implementation_phase: v3`, `epistemic_category: standard`, `depends_on: [ARC-016]`. Mechanism (implemented, `ree-v3/CLAUDE.md` SD-076 entry): asymmetric EMA in `E3TrajectorySelector.update_running_variance` — error improvements incorporated at `alpha*(1+asym)`, worsenings at `alpha*(1-asym)`, settling `rv` below the true error mean (directional overconfidence, biological basis: optimism/positive-outcome bias in waking belief updating). Headroom-repaired 2026-07-22 after a floor-saturation defect (absolute floor 0.01 sat 1.8x above the real operating point ~0.0054, clamping `rv_final` to exactly 0.01 across all arms) — replaced with a relative floor, pinned by 17 contracts.

**MECH-204**: mechanism_hypothesis, status `candidate`, `implementation_phase: v3`. `depends_on` chain includes SD-076 as its drift source. The 2026-08-01 GOV-FANOUT-1 synthesis note on both claims (predates V3-EXQ-860/864, not yet updated by either) records the three-way H1(alive, partial)/H2(weakens itself)/H3(weakened by lit-pull) residual uncertainty and explicitly states V3-EXQ-860 "was not requeued this session given the tight timeline" — now superseded by 860 having run and being confirmed-autopsied, and by 864 having run as its follow-up.

**Prior evidence tally on SD-076 (granularity-debt cluster check, `scripts/granularity_debt_cluster.py SD-076`, re-run today):** 5 targets — V3-EXQ-794 (`non_contributory/competence_implementation_gap`, untested-both), V3-EXQ-850/H1 (`inconclusive/measurement_test_design_defect`, excluded-diagnostic), V3-EXQ-853/H2 (`weakens/measurement_test_design_defect`, excluded-diagnostic), V3-EXQ-860/H2 (`weakens/measurement_test_design_defect`, excluded-diagnostic), a 794a cluster entry. No target reads `weakened` (all diagnostic-excluded or untested) — granularity-debt trigger correctly does not fire. Zero `substrate_ceiling` hits — re-derive brake nowhere near threshold.

## 3. Biological-reference triage

Not load-bearing for this run. SD-076's biological grounding (optimism/positive-outcome bias in waking belief updating) and MECH-204's REM-serotonin-gate grounding are addressed by the separate H3 lit-pull (`evidence/literature/targeted_review_sd_076/`, 8 entries: Sharot2011, Garrett2018, Rollwage2020, Ni2023, Jones2006, Baranski2007/1994, Boardman2024; `evidence/literature/targeted_review_rem_precision_recalibration_timing/`, 6 entries) already complete and unaffected by this run's finding. This autopsy's core move is methodological (instrumentation design), not biological.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (diagnostic, correctly excluded from claim scoring) | this run tests neither SD-076 nor MECH-204 directly; it instruments a puzzle from a prior diagnostic |
| Biological reference | not applicable | see above |
| Developmental/dependency prerequisites | present | `rv_live`, `f1_recalib_engaged` both pass on all 6 cells; SD-076 mechanism itself is IMPLEMENTED |
| Implementation completeness | complete for the intended design, but the design has a latent flaw | `steps_per_ep` is correctly threaded through the code; the environment's own termination condition was not accounted for |
| Environment adequacy | inadequate for this diagnostic's purpose | `CausalGridWorldV3`'s 500-step/death cap silently overrides the driver's exposure-length manipulation |
| Measurement adequacy | misleading | `diff_final` and related end-of-episode metrics correctly measure the substrate state, but that state was never actually varied by the swept parameter |
| Integration adequacy | isolated | the driver's episode loop and the environment's termination logic were not co-designed |
| Scale/capacity | not the limiting factor | N=8 episodes is a legitimate reduced-cost diagnostic scale; the defect is orthogonal to sample size |

## 5. Learning extracted

1. **Recurring pattern, third instance:** a driver's nominal sweep parameter fails to actually vary the measured quantity because of an unaccounted environment-level constraint — structurally the same class of defect as V3-EXQ-845's write-count confound and V3-EXQ-794's floor-saturation defect, this time an environment termination condition silently overriding an experiment-level exposure parameter. Worth naming as a project-level lesson: any driver that sweeps an exposure/duration parameter against `CausalGridWorldV2/V3` must explicitly check whether the environment's own `done` condition (health floor or internal step cap) binds before the swept parameter does.
2. **Measurement gap, not a claim finding.** The wrong-signed `inflation_lowers_rv` puzzle from V3-EXQ-860 remains open. This diagnostic did not resolve it because it never tested the intended manipulation.
3. **Deadline discrepancy found:** `experiment_proposals.v1.json` EVB-0454 (`2026-08-04T21:09:57Z`) disagrees with claims.yaml/autopsy/driver citations (`2026-08-03T20:50:36Z`) by ~24h. Flagged for governance correction.

## 6. Repair pathway

**Routing: `/queue-experiment`** — a redesign of the crossover-bracketing diagnostic that decouples `steps_per_ep` from episode termination, e.g. (a) disable agent-death termination for this diagnostic's arms, or (b) raise `CausalGridWorldV3`'s internal step cap above the swept range for this run only, or (c) measure exposure in realized ticks rather than nominal `steps_per_ep` and re-derive the sweep points from that. **Non-blocking**: per V3-EXQ-860's own autopsy, this puzzle was explicitly not gating the EVB-0454 decision; this redesign inherits that same non-blocking status. **Also route to governance**: correct the EVB-0454 deadline citation discrepancy.

**Draft `evidence_quality_note`** — none owed on SD-076/MECH-204 directly; this run is `claim_ids: [SD-076]` for provenance/traceability but the finding is a diagnostic-instrumentation defect, not claim evidence. Recommend `evidence_direction: non_contributory` (replacing the self-routed `unknown`) with a note: *"V3-EXQ-864 (2026-08-01, autopsy-confirmed): diagnostic instrumenting V3-EXQ-860's wrong-signed inflation_lowers_rv puzzle across a steps_per_ep sweep. The sweep did not actually vary real exposure — CausalGridWorldV3's own episode-termination condition (health floor / internal 500-step cap) fires before any of the three swept step counts (200/500/1000) bind, so diff_final and related end-of-episode metrics are bit-identical across the sweep. The 'no crossover in range' finding is uninformative; the puzzle remains open. Non-blocking for EVB-0454 (per V3-EXQ-860's autopsy). Routed /queue-experiment for a redesign that decouples steps_per_ep from environment-level termination."*

## 7. Re-derive brake / granularity-debt / hypothesis-space

- Re-derive brake: not fired (0 substrate_ceiling hits for SD-076/MECH-204 under R1-R3).
- Granularity-debt trigger: not fired (no target reads `weakened`).
- Fan-out recommendation: not applicable — this run is itself the fan-out-commissioned follow-up to V3-EXQ-860's puzzle, and did not itself discriminate between live hypotheses (its diagnostic failed to execute its design, not merely to find a null result).
- Hypothesis-space ledger (Step 9b): SD-076/MECH-204's GOV-FANOUT-1 H1/H2/H3 portfolio predates the hypothesis-space registry's current usage in this session's autopsy chain; not re-registered here to avoid a second producer writing inconsistent legs mid-portfolio. Left for a future autopsy or governance pass with the full portfolio in view.

## 8. User gate (Step 8)

Presented alongside V3-EXQ-861 via AskUserQuestion. **Confirmed disposition:** `measurement_test_design_defect`, non-blocking, exactly as proposed. Routed `/queue-experiment` for a redesign; EVB-0454's puzzle from 860 stays open and non-blocking. Deadline "discrepancy" noted for governance correction at Step 4/apply.

## 9. Addendum (2026-08-01T21:50:27Z, added at governance apply, non-mutating): the deadline is not a fixed value

What Section 1 called a "~24h discrepancy" between the 2026-08-03T20:50:36Z figure cited across claims.yaml/prior autopsies/this driver's docstring and `experiment_proposals.v1.json`'s 2026-08-04T21:09:57Z is **not a discrepancy between two fixed deadlines** — it is root-caused (via `evidence/experiments/scripts/build_experiment_indexes.py:5107-5111`) to `decision_deadline_utc` being **computed**, not frozen: `generated_at_dt + timedelta(hours=mandatory_decision_deadline_hours)` (`mandatory_decision_deadline_hours=72`), recomputed on **every** governance regeneration for as long as the underlying conflict stays unresolved. So the field perpetually reads "~3 days from whenever governance last ran," not a commitment set once. Every cited timestamp (including this artifact's Section 1) was a snapshot of that rolling value at the moment it was read, not evidence of drift between two authoritative sources. Corrected in claims.yaml (SD-076 + MECH-204 evidence_quality_note) at governance apply. Worth a design review — a deadline that re-arms itself every cycle can never be missed — flagged rather than fixed unilaterally in this pass.
