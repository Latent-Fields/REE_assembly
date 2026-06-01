# Goal-pipeline developmental-window diagnostic — design-analysis memo

**Date:** 2026-06-01T08:15Z
**Session:** developmental-window-followup-20260601T081500Z (persists in-conversation memo from session failure-autopsy-v3-exq-622-20260601T075501Z)
**Purpose:** Design-of-record for the next /queue-experiment session. Diagnostic that dissociates drive-floor anneal vs hazard introduction vs writer-freeze axes as candidate causes of V3-EXQ-622 S1+ z_goal collapse, and finally enables dACC so consumer readout is measurable for the first time in this cohort.
**Status:** PRE-REGISTERED; the chip-spawned /queue-experiment session executes against this memo.

---

## Verdict (summary; full reasoning preserved in the parent session transcript)

The evidence supports one strong claim: **z_goal can form when the goal pipeline is trained on a goal-only env with high drive_floor and bridge + conjunction substrates enabled (V3-EXQ-622 S0, 3/3 seeds, z_goal_peak 0.28–0.44), and it does not persist when drive_floor anneals 0.9→0.2 together with mild hazard introduction (V3-EXQ-622 S1, collapse 1–6 orders of magnitude, 3/3 seeds).** Goal-directed *behaviour* is NOT shown anywhere in this cohort: dACC was unconfigured in both 621a and 622; the "consumer readout = 0" reading is a measurement-OFF artefact. The developmental-windowing hypothesis (writer-freeze + protected consolidation) is plausible but premature; the 622 S1 confound (drive anneal AND hazard introduction together) leaves the proximal cause unidentified. The minimal decisive move is a single 4-arm diagnostic that dissociates the axes and tests writer-freeze rescue, with dACC enabled to test consumer readout for the first time.

## Critical reading of the prior cohort

| Metric | V3-EXQ-621a (12 cells) | V3-EXQ-622 (3 seeds × S0-S3) |
|---|---|---|
| `z_goal_peak_max` | **0.0 in every cell** | S0: 0.281 / 0.439 / 0.342; S1: 0.108 / 0.326 / 0.112; S2: 0.003 / 0.026 / 0.132; S3: ~0 |
| `bridge_cue_fires` | 0 everywhere | S0: 17.5 / 4.6 / 14.0; S1: 20.8 / 4.5 / 9.7; S2: 3.8 / 0.07 / 2.8 |
| `dacc_bias_nonzero` | 0 everywhere | 0 everywhere |
| `approach_commit_rate` | ARM_2 seeds 42,44 + ARM_3 seed 42: 1.0; else 0.0 | S0/S1/S2: 0.0; S3: 1.0 in 2/3 seeds (criterion `>=0.01` trivially satisfied at z_goal in [1e-14, 1e-3]) |

Configuration deltas explaining the formation difference: 621a's scheduler **freezes** the goal pipeline during P0 (`use_mech295_liking_bridge=False`, `use_mech307_conjunction=False`). 622 has the goal pipeline ON from agent build and calls `update_z_goal()` every step. Neither script sets `use_dacc=True`. 621a's "PASS" came via C1 cells-complete + C3 approach_commit lift in ARM_2 — but with `z_goal_peak_max=0.0` everywhere in 621a, the C3 route is NOT z_goal-driven (almost certainly approach to the SD-054 reef refuge or another salient feature).

At 622 S1, `bridge_cue_fires` is preserved or higher than S0 while z_goal collapses by 1–6 orders of magnitude. The collapse mechanism is **downstream of the bridge cue write** — most likely SD-012's `effective_benefit = benefit_exposure * (1 + drive_weight * drive_trace)` ramping from ~3x at drive=1.0 to ~1.0 at drive=0.005, combined with `drive_ema_alpha=1.0` (instantaneous) leaving no sustained trace.

## Hypothesis ranking

| H | Description | Status |
|---|---|---|
| H1 | Drive-coupled gain collapse on still-firing cue input | **Best supported** by 622 (bridge_cue preserved while z_goal collapses) |
| H2 | Representation decay overwhelming maintenance under risk transition | Plausible, not isolable from H1 in 622 |
| H3 | Overwrite by competing risk/harm representation | Weak; z_goal collapses to ~1e-14 not to a different vector |
| H4 | Consumer readout failure | **Untested** (dACC unconfigured) |
| H5 | Missing consolidation phase | Speculative; the autopsy's sustained-drive EMA recalibration is the V3-conservative form |
| H6 | Approach_commit independent of z_goal | **Confirmed** at S3 (criterion-trivial) |

Dominant reading: H1 + H6 jointly explain the data. H4 and H5 are open.

## Diagnostic design

**4 arms × 3 seeds × P0(formation)+P1(transition)+P2(measurement).** New EXQ number (next available, likely V3-EXQ-630+). `experiment_purpose=diagnostic`, `claim_ids=[]` (substrate-readiness, not evidence-weighting), `supersedes=null`.

| Arm | P0 (≥30 ep) | P1 (≥30 ep) | P2 (≥30 ep) | dACC | Purpose |
|---|---|---|---|---|---|
| **ARM_A_FORMATION_ONLY** | drive_floor=0.9, no hazard, full goal pipeline (use_mech295=True, use_mech307=True) | continue P0 config | continue P0 config | `use_dacc=True` | Baselines dACC readout when z_goal non-trivial AND stable; regression guard on 622 S0 PASS |
| **ARM_B_DRIVE_ANNEAL_ONLY** | identical to ARM_A | drive_floor 0.9→0.2 anneal, **no hazard introduction** | constant drive_floor=0.2 | `use_dacc=True` | Isolates drive-anneal axis (H1 test) |
| **ARM_C_HAZARD_ONLY** | identical to ARM_A | constant drive_floor=0.9, **hazard_food_attraction 0→0.7 anneal** | constant drive_floor=0.9 + hazard | `use_dacc=True` | Isolates hazard-introduction axis |
| **ARM_D_WRITER_FROZEN_DURING_TRANSITION** | identical to ARM_A | **freeze use_mech295 + use_mech307 to False during P1**, anneal drive AND hazard | unfreeze at P2 start; measure under target config | `use_dacc=True` | Tests Option A (writer-freeze windowing) — does freezing across the transition protect z_goal state from collapse? |

**Deliberately NOT included:** S2 (gradual harm) and S3 (full SD-054 arbitration). Those are V3-EXQ-603d's job. Keep this experiment scoped to formation-vs-persistence-vs-windowing.

## Pre-registered metrics

- `z_goal_norm_median_last_window` (P1 final 10 ep + P2)
- `z_goal_norm_peak_max` (per phase)
- `bridge_cue_fires_per_episode_mean` (per phase)
- **`dacc_bias_nonzero_steps_per_episode_mean`** (per phase) — the NEW measurement
- `approach_commit_rate` AND **`approach_commit_at_high_z_goal_rate`** (conditional on `z_goal_norm > 0.05` at commit tick — replaces 622's criterion-trivial S3 metric)
- `mean_episode_length` (survival check)

## Pre-registered acceptance criteria

- **C1 (formation regression guard):** ARM_A `z_goal_median_last_window >= 0.05` on ≥2/3 seeds. FAIL = substrate regressed since 622 → /diagnose-errors.
- **C2 (drive-axis isolation):** ARM_B `z_goal_median_last_window < 0.05` on ≥2/3 seeds AND ARM_B z_goal_norm at P1 end < 0.5 × ARM_A. PASS = drive-anneal alone is sufficient to collapse z_goal.
- **C3 (hazard-axis isolation):** ARM_C `z_goal_median_last_window < 0.05` on ≥2/3 seeds. PASS = hazard introduction alone is sufficient.
- **C4 (writer-freeze rescue):** ARM_D `z_goal_median_last_window` AT P2 START ≥ 0.5 × ARM_A. PASS = freezing the writer across the transition preserves z_goal state (Option A is the load-bearing fix).
- **C5 (consumer readout under non-trivial z_goal):** in the arm with highest z_goal during P2 (ARM_A or ARM_D), `dacc_bias_nonzero_steps_per_episode_mean ≥ 1.0` on ≥2/3 seeds. PASS = consumer reads z_goal; FAIL = readout failure is a separate gap.

## Interpretation grid (4 rows)

| C2 | C3 | C4 | C5 | Reading | Routing |
|----|----|----|----|---------|---------|
| PASS | FAIL | (any) | PASS | drive-anneal alone collapses z_goal; consumer reads fine | /implement-substrate AMEND on `scaffolded_sd054_onboarding` (Option D + sustained-drive EMA at low drive_floor) — conservative path |
| FAIL | PASS | (any) | PASS | hazard alone collapses z_goal; competing-representation or attention-partition mechanism implicated | /implement-substrate AMEND with risk introduction decoupled in time from drive anneal |
| PASS | PASS | PASS | (any) | both axes contribute AND writer-freeze rescues — Option A confirmed | /implement-substrate AMEND adding writer-freeze P1 sub-phase; bounded, single-purpose, no new closure node |
| (any) | (any) | (any) | FAIL | non-trivial z_goal does not reach dACC | /failure-autopsy on dACC readout chain (E3 score_bias composition, dACC sub-weights); substrate work may be needed |

## What this diagnostic deliberately does NOT do

- Does not vary writer-freeze as a candidate substrate amendment — it tests the hypothesis. Substrate amend shape is decided by /implement-substrate IF C4 PASSes.
- Does not change the closure-map structure. Updates `goal_pipeline:GAP-4` resume_condition with the dissociation finding and annotates `behavioral_diversity_isolation:GAP-C` prereq (2).
- Does not promote/demote any claim. `claim_ids=[]`.
- Does not run S2/S3 — those are V3-EXQ-603d.

## Closure / governance impact

- `goal_pipeline:GAP-4` — resume_condition update only; status unchanged.
- `behavioral_diversity_isolation:GAP-C` prereq (2) — annotation acknowledging that 621a's substrate-readiness PASS did not establish z_goal formation in default config; this diagnostic refines the substrate's behavioural-runtime profile.
- No new closure node. No parallel closure map.
- Does NOT determine V3 closure for Q-045 / MECH-313 / MECH-260. Those remain gated on V3-EXQ-603d behavioural cluster validation under a substrate that has cleared this diagnostic.

## Risks of overfitting / complexity debt

| Risk | Mitigation |
|---|---|
| Premature windowing substrate (R1) | Diagnostic-first discipline; substrate amend only IF C4 PASSes |
| Closure-map inflation (R2) | Update existing GAP-4 / GAP-C resume_conditions in place; no new node |
| Over-claiming downstream consumption (R3) | C5 explicitly tests this; do not assert dACC readout works/fails without it |
| Multi-knob anneal coupling (R4) | If C2 PASSes, the /implement-substrate amend session dissociates `drive_floor` vs `min_drive_to_fire` vs `z_beta_threshold` axes separately |
| Developmental-stage philosophy generalising to other substrates (R5) | Keep windowing scoped to the goal substrate; do not extend to z_world / z_self / z_harm / z_resource / z_beta in V3 |

## Adjacent long-horizon territory (NOT in scope)

The user has separately flagged the **ACh / PV-interneuron / state-dependent plasticity window** territory as long-horizon V4-or-late-V3 substrate work. That framing is captured in `REE_assembly/docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md` and project memory. The current diagnostic is NOT a probe into that territory; it is the minimum-scope discriminative test for the immediate goal-pipeline question. If the diagnostic eventually leads to a windowing substrate, that substrate would be the V3-conservative form (scheduler-driven flag toggles + sustained-drive EMA); the neuromodulator-gated state-conditional form is V4 work and should not be conflated.

## References

- [failure_autopsy_V3-EXQ-622_2026-06-01.md](failure_autopsy_V3-EXQ-622_2026-06-01.md) — parent autopsy artifact
- [sd_054_scaffolded_onboarding_substrate_design.md](sd_054_scaffolded_onboarding_substrate_design.md) — current substrate-of-record
- [goal_pipeline_plan.md](goal_pipeline_plan.md) — closure node GAP-4
- [behavioral_diversity_isolation_plan.md](behavioral_diversity_isolation_plan.md) — closure node GAP-C
- [z_goal_collapse_triage_2026-05-31.md](z_goal_collapse_triage_2026-05-31.md) — ownership re-attachment that named the substrate
- 621a manifest: `evidence/experiments/v3_exq_621a_scaffolded_sd054_onboarding_substrate_readiness_20260531T230932Z_v3.json`
- 622 manifest: `evidence/experiments/v3_exq_622_goal_stream_staged_sd054_20260531T223804Z_v3.json`
- [../docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md](../../docs/thoughts/2026-06-01_plasticity_window_neuromodulators.md) — adjacent long-horizon territory (NOT this experiment's scope)
