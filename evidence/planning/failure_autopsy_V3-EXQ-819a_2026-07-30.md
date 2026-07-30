# Failure Autopsy — V3-EXQ-819a (MECH-457/INV-088 zworld trained-vs-random gatefix)

**Generated:** 2026-07-30T06:44:02Z · **Scope:** single · **Status:** confirmed
**Session:** strange-noyce-c116b8 (chip `chip-20260730-autopsy-819a`, spawned by the 2026-07-29/30 `/governance` cycle)

**Trigger.** `run_id v3_exq_819a_mech457_inv088_zworld_trained_vs_random_gatefix_20260727T005012Z_v3` is a `diagnostic` PASS whose self-route (`zworld_prediction_training_confers_advantage`) drives a governance-relevant action — resolving the R4/D12 instrument-validity leg of the `competence_floor` hypothesis-space question — but carried no confirmed or in-flight autopsy. Per CLAUDE.md's Failure-autopsy boundary rule and governance SKILL.md Step 1.5a / "Diagnostics are not exempt from adjudication", a decision-routing diagnostic PASS may not be trusted inline without one, even though `pending_review.md`'s "Diagnostic adjudication required" table did not flag it (all `preconditions[]` were `met: true`, so no `precondition_unmet`/`vacuous_pass` flag fired).

**Dry-run check:** `check_dry_run_citations.py v3_exq_819a_..._v3 V3-EXQ-819a` → `0 dry cited, 1 clean`. Not a smoke.

---

## 1. Facts reconstructed

- `PASS` · `experiment_purpose: diagnostic` · `ree-worker-1` (cloud hub) · `linux-x86_64-py3.10-torch2.12.0+cpu` · 46080.2s wall clock (~12.8h) · seeds 42–47 (6 seeds, up from 819's 3) · `non_degenerate: true` · `recording_schema: rec/v1` · `dry_run: false`.
- **Supersession**: 819a supersedes V3-EXQ-819. 819 was itself adjudicated `measurement_test_design_defect` in `failure_autopsy_batch-793a-817-819_2026-07-26.md` target 3 (user-confirmed): its `post_bc_install_took` gate scored on the WORST seed, so a single near-miss (seed 43: 0.9 vs 1.0 floor) vacated the whole trained arm even though the router's own `install_took_strict_majority` predicate read an asymmetric-install ADVANTAGE from the same data — the gate and the router disagreed on identical numbers. 819a's three declared fixes (all measurement, substrate/science unchanged): (1) `post_bc_install_took` now scores the STRICT-MAJORITY install fraction (>0.5), identical to the router's own predicate, so gate and router cannot disagree; (2) `advantage_abs_floor` 1.0 → 0.3, rescaled to the observed 0.35–2.4 res/ep near-floor band; (3) seeds 3 → 6.
- **Manipulation**: SD-070 P0a encoder warmup (`zworld_p0_episodes=60` trained arm vs `0` random-projection control), encoder DETACHED (`cotrain_encoder=False`) post-warmup so only the *initial content* of the representation differs between arms; everything else identical (BC warmstart 300 ep, on-budget RL 3000 ep, actor-critic hidden 128, D3 hazard-free rung).
- **Readiness anchors** (all `met: true`): `local_view_greedy_d3` 47.73 (floor 1.0), `greedy_oracle_d3` 57.79 (floor 1.0), `zworld_world_encoder_trained` (trained arm's own P0a warmup moved `split_encoder.world_encoder`, max|delta| 0.275, gating on the TRAINED arm only — the control is deliberately frozen).
- **Per-arm gate**: `zworld_trained` GREEN (all 5 preconditions met, `post_bc_install_fraction=0.833` > 0.5). `zworld_random_proj` RED on `post_bc_install_took` (`fraction=0.167` < 0.5) — this does **not** vacate the green arm (per-arm gate design, citing `failure_autopsy_V3-EXQ-785_2026-07-19` §2a/8: a red arm is unscored, not a refutation). `any_green: true`, `non_degenerate: true` at top level, `degeneracy_reason` confirms "PARTIAL non-vacuity... Arm(s) zworld_trained passed the gate in full and ARE scored".
- **Load-bearing criterion** `C_zworld_training_confers_competence_advantage` (discrimination): passed. Per-seed paired AUC delta (trained − random), effect margin = max(0.3 abs, 0.15 rel) = 0.3: seed 42 +0.792, 43 +0.565, 44 −0.031, 45 +1.515, 46 +0.665, 47 +0.246. 4/6 seeds clear the margin (42, 43, 45, 46) — strict majority. `n_seeds_harm=0`. Mean paired AUC delta +0.626, mean peak delta +1.067, mean terminal delta +1.10.
- `criteria_non_degenerate` all true for the load-bearing criterion; `headline.advantage_confirmed: true`; `training_advantage_transient/harms_competence/pathway_dispensable` all false.
- **Recording provenance**: `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, full `config`, explicit `seeds` list all present (recording standard §3b satisfied) — see §5 for one caveat on `substrate_stable_across_run`.

---

## 2. Claim-layer mapping

**MECH-457** (`action_learning_as_first_class_actor_critic_substrate`) — `candidate/v3_pending`, `implementation_phase: v3`. Decomposed 2026-07-22 into MECH-475/MECH-476 children; MECH-457 retained as narrowed umbrella. `depends_on`: SD-056, MECH-229, MECH-459, MECH-460, MECH-461. This run is **not** a direct test of the actor-critic-substrate claim content — it is an instrument-validity check on the z_world representation used across the broader `competence_floor` question's legs, several of which bear on MECH-457.

**INV-088** (`world_goal_evaluator_bounded_by_z_world_differentiation`) — `candidate`, `invariant_type: emergent` (from ARC-001/003/019), `pending_substrate_reconfirmation: true`. `depends_on`: INV-064, ARC-001, ARC-003, ARC-019.

**Manifest's own routing intent** (stated in `notes`): "DIAGNOSTIC (excluded from scoring); PROMOTES/DEMOTES NOTHING... MECH-457 stays candidate/v3_pending; INV-088 unchanged." This run's job is R4 of the `competence_floor` question (D12): "does a prediction-trained z_world confer any competence advantage over a random projection of the same dimensionality?" — an instrument-validity re-check triggered because V3-EXQ-780 found every prior z_world arm across the whole campaign ran a **frozen random projection** rather than a genuinely prediction-trained one (the encoder-training capability, SD-070's `zworld_p0` warmup, did not exist as working code until `ree-v3 b523b9c70a`).

**Governance action this run actually routes**: not a claims.yaml write (correctly — the run is `scoring_excluded: diagnostic_probe`), but resolution of hypothesis `H-zworld-trained-instrument` in the `competence_floor` question of `hypothesis_space_registry.v1.json` (already pre-registered 2026-07-26, `adjudicating_runs: [V3-EXQ-819, V3-EXQ-819a]`, state `alive` pending this run). See §6.

**Indexer note (resolved, not a bug):** `claim_evidence.v1.json` stamps both claim entries `evidence_direction: "supports"`, `adjudication: "verified"`, `confidence: 0.75` — which looks inconsistent against the manifest's own top-level `evidence_direction: "unknown"`. Traced to `build_experiment_indexes.py:2474-2477`: when a run's `evidence_direction` is `"unknown"` and no `evidence_direction_note` is present (`direction_explicitly_set = bool(manifest.get("evidence_direction_note"))`), the indexer defaults `inferred_direction` to `"supports"` for any PASS. This is the documented generic fallback for evidence runs that omitted a direction, not a defect specific to 819a — and it is inert here: `scoring_excluded: "diagnostic_probe"` already keeps this run out of the actual confidence/conflict aggregate for both claims, so the cosmetic "supports" label in the index does not risk a false promotion. Minor hygiene recommendation (non-blocking): future R4-class instrument-validity diagnostics could set an explicit `evidence_direction_note` (e.g. "diagnostic instrument-validity check, not claim evidence") to suppress the default and make the index entry self-explaining, but no action is owed on this run.

---

## 3. Biological-reference triage

Closest reference mechanism: predictive/structured sensory representation learning (predictive coding — Rao & Ballard 1999; hierarchical prediction-error minimization in visual cortex) shaping downstream competence, vs. an untrained/random projection of the same dimensionality. This is a **formal-instrumentation check**, not a direct test of a specific REE mechanism against a named biological analog — its purpose is to confirm the measuring apparatus (a trained z_world encoder) actually differs functionally from a broken one (frozen random projection), before trusting any of the sixteen prior campaign legs that used it. The qualitative direction confirmed (a representation shaped by prediction training supports better downstream competence than a random projection of equal dimensionality) is biologically unsurprising and uncontroversial — structured, learned sensory representations reliably outperform random ones for downstream behavior in both biological and ML systems. `lit_status`: not separately pulled for this instrument-validity check; not needed — this is not a novel biological claim, it is confirming SD-070's engineering worked as intended.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | The run tests exactly what it was designed to test (trained vs. frozen-random z_world), and does not weigh directly on MECH-457/INV-088's content — it is scoring-excluded by design. |
| Biological reference | clear | Structured/trained representations beating random projections for downstream competence is well-established; not a novel or contested biological claim. |
| Developmental / dependency prerequisites | present | SD-070 (`sd_zworld_warmup_optimizer_group`) BUILT (`ree-v3 b523b9c70a`) + VALIDATED (`REE_assembly 25a69fcd4c`, 2026-07-22) before this run — the exact substrate the 780/781/782 cluster autopsy identified as owed. |
| Implementation completeness | complete | Both arms ran the full detached-encoder protocol; the trained arm's encoder demonstrably moved (`world_encoder_max_abs_delta` 0.275, 6/6 seeds `encoder_trained_strict_majority: true`); the 819 gate/router disagreement is reconciled in this iteration. |
| Environment adequacy | adequate | D3 hazard-free rung; both anchors (`local_view_greedy`, `greedy_oracle`) clear the 1.0 floor by a wide margin, confirming the env is solvable and the floor is meaningful. |
| Measurement adequacy | adequate, with one unresolved-but-low-severity caveat | The trajectory DV (AUC over BC-install + every-250-episode probe, 12 readings in the worst cell) is the right shape for a "succeeded then decayed" check per the recording standard. Caveat: `substrate_stable_across_run: false` — see §5. Does not change the routing recommendation. |
| Integration adequacy | isolated | A controlled two-arm instrument comparison (not an integration test of a claim mechanism with the rest of the substrate). |
| Scale / capacity | adequate | 6 seeds (up from 819's 3) gives a firmer strict-majority read; 3000-episode on-budget RL + 300-episode BC warmstart matches the reference build (128-wide, 3x budget, detached) explicitly distinguished from the 769-falsified 256/5x build. |

**Dominant diagnosis**: none required — this is a **confirmed positive instrument-validity result**, not a FAIL needing a repair pathway. Recommended `epistemic_category`: **`standard`** (a clean confirming result; not `substrate_ceiling`, not a measurement/test-design defect — that defect was already fixed by 819a itself relative to its 819 predecessor).

---

## 5. Substrate-stability check (flagged, investigated, resolved to low-severity)

**Finding**: top-level `substrate_stable_across_run: false`. `substrate_stability_detail.distinct_cell_substrate_hashes` shows exactly **two** hashes across the run's cells: `20cc7323...` (used by `local_view_greedy`, `greedy_oracle`, `random_walk`, and — critically — the **trained** arm `zworld_trained`, all 6 seeds, `substrate_n_files=159`) and `97780328...` (used by the **control** arm `zworld_random_proj`, all 6 seeds, `substrate_n_files=158`). The 12.8-hour wall-clock run spanned a git-tree change on the runner (`ree-worker-1`) between the trained-arm cells and the control-arm cells.

**Precedent**: this is the same *shape* as `failure_autopsy_V3-EXQ-782_2026-07-20`, a confirmed FALSE POSITIVE where `_SUBSTRATE_GLOBS` (`ree_core/**/*.py`, `experiments/_harness.py`, `experiments/_metrics.py`, `experiments/_lib/**/*.py`) was wider than the driver's actual import closure, so an unrelated co-resident commit moved the whole-tree hash without touching anything the run executed.

**Investigation performed** (not a full closure-restricted recompute, which 782's autopsy did and which this one did not): searched `ree-v3` origin history for commits landing between the two resolution timestamps (`2026-07-26T12:02:14Z` and `2026-07-26T13:01:33Z`, i.e. the 819a run's own start window). Four commits landed in that window: three `phase3-queue: snapshot` commits (touch only `experiment_queue.json`, coordination data, not in `_SUBSTRATE_GLOBS`) and one (`200040c`, 12:46:50Z) adding V3-EXQ-817a's own new driver script — but that file is `experiments/v3_exq_817a_*.py`, which is **not** covered by `_SUBSTRATE_GLOBS` either (the globs cover `ree_core/**`, `experiments/_lib/**`, `_harness.py`, `_metrics.py` — not bare `experiments/*.py` driver files). No commit touching `ree_core/**` or `experiments/_lib/**` was found in the pushed origin history for this window. The observed `n_files` delta (159→158, a *decrease*) is also not explained by any of these four commits (none delete a substrate-glob file), so the root cause is not fully identified — most likely an unpushed/runner-local state (an autostash cycle, or a file resolved mid-write) rather than a landed commit, per the class of hazard CLAUDE.md already documents for the runner heartbeat's `git pull --rebase --autostash`.

**Assessment**: LOW severity, not fully closure-verified, but does not change the routing recommendation, for two independent reasons: (a) the shape matches a confirmed false-positive precedent and no evidence of a substantively relevant code change was found in the searched window; (b) even in the worst case, the affected arm is the **control** (`zworld_random_proj`), whose role is to establish "what happens with an untrained representation" — a benign unrelated code delta on the control side would not manufacture the *decisive, hypothesis-predicted direction* of the trained-vs-random contrast (a 0.626 mean paired AUC delta in the direction the SD-070 warmup was built to produce), since the delta is measured relative to the trained arm's own within-run-stable substrate. Recorded honestly rather than silently cleared: **flagging `dry_run_checked`-style provenance discipline is satisfied, but a full closure-restricted fingerprint recompute (782's method) was NOT performed here** — if this leg's `confirmed` status is later contested, that recompute is the next concrete step, not a blind re-run.

**Reuse consequence**: the manifest's own `reuse_mint.reuse_eligible: true` for `zworld_random_proj` will be correctly refused by `arm_reuse.py`'s consumer-side check (`manifest.get("substrate_stable_across_run") is False` → stale, `_is_arm_stale`-equivalent) regardless of the driver's optimistic stamp — no action needed; this is already-built machinery (per its own docstring: "over-refusal is the correct failure direction here").

---

## 6. Precautionary cross-check: does this reopen H-rep?

`H-zworld-trained-instrument`'s own description asks: "does this re-validate whether the representation-axis eliminations (H-rep, 747/749) hold now that the encoder actually trains?" — since V3-EXQ-780 found *every* prior z_world arm in the campaign ran a frozen random projection, and `H-rep` ("representation insufficient") was eliminated 2026-07-13 partly on the strength of "the z_world/dense-teacher control clears the task" (registry `resolution.basis`).

**Traced the actual control**: `H-rep`'s elimination (`V3-EXQ-747`/`749`) draws its z_world reference from **V3-EXQ-748** ("`ac_zworld_bc` — raw-view BC clears while z_world BC does not => z_world is action-inadequate", cited in `v3_exq_749_...py:287-288`). Read `v3_exq_748_mech457_hexplore_reward_density_actor_critic.py` directly: it sets `cotrain_encoder: True` (lines 101, 381) — an older, **actively-jointly-training** mechanism, structurally distinct from the `zworld_p0` **detached** P0a-warmup-then-frozen mechanism that V3-EXQ-780 diagnosed as broken (819a's own caveat corroborates: "the historical 32.72 z_world+BC band (748) ran cotrain=True"). The 780 defect is specific to the newer, detached-encoder experimental family (769+ era) that 819a itself belongs to; it does not implicate 748's cotrained encoder.

**Conclusion**: `H-rep` is **not** confounded by the frozen-random-projection defect and its `eliminated` state stands unchanged — this autopsy does not recommend reopening it via the registry (reopening an already-`eliminated` leg without a genuine new adjudicating run would itself violate the frozen-ledger invariants).

**User-directed precaution (Step 8 gate, 2026-07-30)**: despite the above finding, the user asked that H-rep be flagged for a precautionary re-derivation given how central the frozen-instrument confound has been across this whole question. Recorded as a routing item in §7 — a low-priority `/queue-experiment` spike re-running 748's dense-teacher/z_world-BC arm under the now-validated `zworld_p0`-trained encoder (i.e., a modernized 748-equivalent), to directly (not just structurally) confirm H-rep's elimination survives contact with the proven-working instrument. This is precautionary, not because the structural argument above is in doubt.

---

## 7. Learning extracted and repair pathway

**Learning**:
1. The 819→819a gate/router reconciliation worked: this run is `non_degenerate: true` with no adjudication flag, confirming the fix.
2. Prediction-trained z_world confers a real, decisive competence advantage over a frozen random projection of the same dimensionality (`H-zworld-trained-instrument` → `confirmed`). The campaign's prior z_world legs that used the *pre-780* frozen-random-projection instrument (769-era `zworld_p0` family) are now re-interpretable against a substrate that can actually express the representation-quality axis — but that re-interpretation is a separate, future task, not performed here.
3. `H-rep`'s 2026-07-13 elimination draws on a structurally different (cotrained, not detached-frozen) z_world instrument and is unaffected by the 780 defect — checked directly against the driver script, not inferred.
4. One unresolved measurement-provenance caveat (substrate-hash drift within a single 12.8h run) is recorded for future closure-restricted verification if ever contested; it does not block this leg's resolution.

**Diagnosis classification** (work-graph debt vocabulary): this is not a `complicated (buildable)`, `complex (probe-gated)`, or `aleatoric (irreducible)` item — it's a confirmed positive result. The one open item (§6 precaution) is `complex (probe-gated) / puzzle (known rules)` — a cheap, well-posed spike, not a build and not a reframe.

**Routing**:
- **Primary**: resolve `H-zworld-trained-instrument` in `hypothesis_space_registry.v1.json` (Step 9b, Mode B) to `confirmed`. No `claims.yaml` write — MECH-457/INV-088 status is unchanged, matching the manifest's own declared intent.
- **Secondary (chippable, per user direction)**: `/queue-experiment` — a low-priority precautionary spike re-running V3-EXQ-748's dense-teacher/z_world-BC arm under the validated `zworld_p0`-trained encoder, to directly reconfirm `H-rep`'s elimination against the now-proven instrument. Not a re-derive-brake case (H-rep is not currently contested) — framed as confirmatory hardening, not a re-test of a live discrimination.
- No `/implement-substrate`, `/lit-pull`, or `/claim-synthesis` routing needed. No re-derive brake (this is not a `substrate_ceiling`/`non_contributory` reading). No granularity-debt trigger (claim alignment reads `intact`, not `weakened`).

**Draft `evidence_quality_note` (informational only — this run is `scoring_excluded`, so governance need not append it to either claim, but it is drafted per the skill template in case a future re-interpretation pass wants the context):**

> V3-EXQ-819a (2026-07-27, confirmed autopsy 2026-07-30) is an instrument-validity diagnostic, not direct claim evidence (`scoring_excluded: diagnostic_probe`): it confirms a prediction-trained z_world beats a frozen random projection on installed foraging competence (paired AUC delta +0.626, 4/6 seeds clear a 0.3 margin, non-degenerate). This resolves the `H-zworld-trained-instrument` hypothesis-space leg but promotes/demotes nothing on MECH-457/INV-088; the campaign's pre-780 z_world legs (run on the broken frozen-projection instrument) remain flagged for separate re-interpretation, not retroactively reweighted here.

---

---

## 8. Step 9b — ledger delta

Resolved `H-zworld-trained-instrument` (`competence_floor` question) from `alive` → `confirmed` (Mode B: `resolving_runs: [V3-EXQ-819a]`, `evidence_direction: supports`, `epistemic_category: standard`, `control_passed: true`, `non_degenerate: true`, `met_elimination_bar: false` per the state-mapping table for a `supports`+control-passed leg, `resolved_utc: 2026-07-27T00:50:12Z` = the run's own manifest timestamp). No new hypotheses pre-registered this cycle (the leg was already pre-registered 2026-07-26 from `failure_autopsy_batch-793a-817-819_2026-07-26.json`). `initial_frozen_count` unchanged (20).

`build_hypothesis_space.py`: `build=80.0% (104/130) surviving=35/46 at registration (35/64 incl. +18 fan-out) ready=7/14`.

`check_hypothesis_space_integrity.py`: 1 flag, 23 advisory (labelled fan-out, pre-existing), 16 git-witnessed, 1 fan-out-recurrence overlay (pre-existing, `competence_floor` — routing-only, not this autopsy's action). The one flag — **(a) un-backed surviving-count drop**, "surviving fell by 1 but resolved_out did not rise" — is the expected, correct shape of a `confirmed` resolution (not an elimination): a `confirmed` leg legitimately leaves the `alive`/surviving set without counting as an eliminated `resolved_out`. The registry already carries 15 other `confirmed`-state hypotheses produced the same way; this is not a defect introduced by this edit. No action owed.

The pre-existing fan-out-recurrence overlay on `competence_floor` (5 labelled portfolios, N≥3) is unrelated to this leg's resolution — it was already present before this edit and is routing-only per GOV-FROZEN-1 (re-pose the operationalization before opening a 6th portfolio; promotes/demotes nothing). Not actioned here; noted for the next `/governance` walk.

---

*Adjudicated by session `strange-noyce-c116b8` (chip `chip-20260730-autopsy-819a`). Inputs: `evidence/experiments/v3_exq_819a_mech457_inv088_zworld_trained_vs_random_gatefix_20260727T005012Z_v3.json`; `evidence/experiments/claim_evidence.v1.json`; `evidence/experiments/scripts/build_experiment_indexes.py`; `docs/claims/claims.yaml` (MECH-457, INV-088); `evidence/planning/hypothesis_space_registry.v1.json` (`competence_floor`); `evidence/planning/failure_autopsy_V3-EXQ-782_2026-07-20.md`; `evidence/planning/failure_autopsy_batch-793a-817-819_2026-07-26.md`; `ree-v3/experiments/_lib/arm_reuse.py`, `arm_fingerprint.py`; `ree-v3/experiments/v3_exq_747_mech457_hrep_rawview_actor_critic.py`, `v3_exq_749_mech457_hrep_x_hexplore_rawview_dense_actor_critic.py`, `v3_exq_748_mech457_hexplore_reward_density_actor_critic.py`; `ree-v3` git log 2026-07-26T10:00–15:00Z. User scientific judgment confirmed the routing at the Step 8 gate, 2026-07-30, with the H-rep precaution added per user direction.*
