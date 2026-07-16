# Failure Autopsy (CLUSTER) — V3-EXQ-767 (SD-025) + V3-EXQ-768 (ARC-057)

- **Generated (UTC):** 2026-07-16T17:42:12Z
- **Scope:** cluster (2 diagnostic PASSes sharing one failure shape)
- **Status:** confirmed
- **Skill:** `/failure-autopsy` (diagnostic adjudication)
- **Trigger:** governance cycle 2026-07-16c aborted at Step 1.5 pre-flight — both PASSes flagged `vacuous_pass`; under the diagnostic adjudication gate their PASS cannot drive an SD-025 / ARC-057 governance action until this autopsy lands.
- **Analysis + handoff only.** No edits to `claims.yaml` / manifests / `review_tracker.json` / `substrate_queue.json`. SD-025 and ARC-057 stay `candidate`; a later `/governance` consumes this artifact.

---

## 1. Targets

| | V3-EXQ-767 | V3-EXQ-768 |
|---|---|---|
| run_id | `v3_exq_767_sd025_curiosity_drive_selection_bias_20260716T073159Z_v3` | `v3_exq_768_arc057_da_curiosity_interaction_spike_20260716T155307Z_v3` |
| claim | SD-025 (`hippocampal_module.curiosity_drive`) | ARC-057 (SD-024 × SD-025 approach-emergence interaction) |
| purpose | diagnostic, 8 seeds | diagnostic, 8 seeds |
| machine | DLAPTOP-4 (Mac, darwin-arm64-py3.13) | ree-worker-1 (cloud, linux-x86_64-py3.10) |
| outcome (self-routed) | PASS / `supports` | PASS / `supports` |
| flagged load-bearing crit | `L1a_pref_A_on = 1.0` on all 8 seeds | `C2_both_on_approaches = 1.0` on all 8 seeds |
| script's own guard | `pref_on_varies_across_seeds = False` → **`non_degenerate: false`** | `pref_both_on_varies_across_seeds = False` → **`non_degenerate: false`** |
| **adjudication (this autopsy)** | **vacuous** | **vacuous** |

Both `substrate_hash` present (`f92a600c…`), full `config` + explicit `seeds` recorded — **no recording gap**; the recording standard's always-core is satisfied.

---

## 2. Facts — the shared failure shape

Both scripts share the **identical selection instrument** `_pref_dense` (767 lines 220-250; 768 lines 279-304):

> For each of `N_TRIALS = 32` counterbalanced trials, build `K = 16` candidate trajectories (half → dense region, half → sparse), score each with `hip._score_trajectory` (the exact CEM elite-selection path), and count the fraction whose **`argmin(score)`** heads to the dense region. Averaged over an A-dense and a B-dense field (cancels the harm-terrain geometry).

The per-candidate continuous `scores` list is computed at run time (`scores.append(...)`) but **the function returns only the binary argmin fraction — the continuous margin is discarded.**

**Why it saturates.** `_score_trajectory` = harm-residue terrain (empty here → ≈ 0) + curiosity term `-w · mean(density · (1 − familiarity))`. Density at the dense region vs sparse:

- 767: ≈ **84 vs 9** (curiosity_weight 1.0) → per-trial score gap ≈ 75
- 768: ≈ **28 vs 10** (curiosity_weight 1.5) → gap ≈ 18-20

The curiosity contribution dwarfs the near-zero terrain score and any candidate jitter, so `argmin` picks a dense candidate on **every** trial, **every** seed → `pref_dense = 1.0` exactly, **zero cross-seed variance**. The OFF / single-drive controls (curiosity_weight 0) score on the empty terrain → **exactly 0.5** (chance) after counterbalancing.

### Per-target detail

**767 (SD-025):** essentially every load-bearing quantity is constant — L1a = 1.0, L1b propagation_delta = 0.5, L1c weight_indep_delta = 0.0, L2a antipersev_delta = 0.5. The only varying quantity, `pref_a_fresh` (0.19–0.88), does **not** enter a load-bearing pass as variance. → **strongest vacuity case.**

**768 (ARC-057):** the super-additive *interaction* survives —
- single-drive arms at chance: `sd024_on = 0.5` (flat), `sd025_on ≈ 0.45` (varies 0.33–0.61 across seeds)
- `C1 interaction contrast` = `pref_both_on − (pref_sd024_on + pref_sd025_on − pref_both_off)` = `1.0 − pref_sd025_on` → **varies across seeds and passes** (`interaction_varies_across_seeds = True`)
- C3 (sd025-alone at chance), C4 (weight-zeroing persistence), C7 (value non-discriminating) pass.

Only the **absolute-level** load-bearing gate `C2` (both_on ≥ 0.6) saturates. So 768 carries more surviving structure than 767 — but its flagged criterion is still a zero-variance load-bearing gate.

---

## 3. Claim-layer mapping

- **SD-025** — `design_decision`, `subject: hippocampal_module.curiosity_drive`, **status candidate**, `depends_on: SD-024, SD-004, ARC-057, MECH-111, INV-051`.
- **ARC-057** — `architectural_commitment`, `subject: hippocampus.curiosity_approach_emergence`, **status candidate**, `depends_on: MECH-232, ARC-007, SD-004`.

Did the test let the claim express itself? **Yes for the mechanism, no for the gate.** Both drives genuinely move selection off the null (OFF = 0.5 → ON/both-ON = 1.0; a null selection rule gives 0.5, cleanly shown by the controls). But the load-bearing gate is a saturated binary that carries no graded/effect-size information, so it cannot *clear* on evidence. Neither claim is falsified; neither may promote on these runs. Tags are accurate (not inherited from a predecessor).

---

## 4. Biological-reference triage

| | closest mechanism | formal import? | divergence |
|---|---|---|---|
| SD-025 | curiosity / novelty-seeking drive biasing hippocampal trajectory selection toward representationally richer regions, discounted by a waking-only familiarity EMA | **no** — faithful drive instantiation | none — this is a measurement-operationalization defect, not a biology divergence |
| ARC-057 | conjunctive approach from DA-mediated representational expansion (VTA→hippocampus, verified in 766a) × curiosity drive; AND-gate, no explicit valence gradient | **no** — faithful conjunctive-interaction instantiation | none |

Lit status **present** (SD-024 leg grounded in Retailleau & Morris 2018 / Lisman & Grace 2005 / Wittmann 2005 per the 766a autopsy). No `/lit-pull` commission owed.

---

## 5. Four-layer diagnosis (dominant layer bolded)

| Layer | 767 | 768 |
|---|---|---|
| Claim alignment | intact (not falsified; propagation real) | intact (super-additive shape real) |
| Biological reference | clear | clear |
| Prerequisites | present (SD-024 verified 766a) | present (766a + 767 prereqs ran) |
| Implementation | complete (drive works; readout mis-operationalized) | complete (interaction works; same readout) |
| Environment | adequate | adequate (env-free Test B) |
| **Measurement** | **under-instrumented / misleading — binary argmin proportion saturates to 1.0, zero variance; all load-bearing crits ~constant** | **under-instrumented for C2 — same saturation; interaction C1 survives, absolute-level C2 does not** |
| Integration | n/a | coupled (conjunction is the test; works but saturates) |
| Scale | adequate (8 seeds; metric, not sample) | adequate |

**Recommended `epistemic_category`: `measurement_degeneracy`** — explicitly **NOT `substrate_ceiling`** (the SD-024/SD-025 substrate works; 766a verified SD-024). **Recommended `evidence_direction`: `inconclusive`** (promotes/demotes nothing).

---

## 6. Cluster pattern

| Experiment | Claim | Negative control (absolute) | Flagged load-bearing crit | Non-saturated companions | Read |
|---|---|---|---|---|---|
| V3-EXQ-767 | SD-025 | OFF = 0.5 exactly | L1a = 1.0 (0 var) | L1b/L1c/L2a all ~constant | metric saturates; mechanism real |
| V3-EXQ-768 | ARC-057 | both_off / sd024-alone = 0.5 | C2 = 1.0 (0 var) | **C1 interaction varies + passes**, C3/C4/C7 pass | metric saturates; interaction real |

**This is ONE structural property, not two independent bugs.** The shared `_pref_dense` binary-argmin selection instrument has no headroom under a dominant curiosity term, so the load-bearing gate saturates to exactly 1.0 and loses all cross-seed variance / effect-size information — while the continuous CEM score-margin that *would* carry that information is computed at run time and thrown away.

**Two live readings — they converge:**
1. *Ceiling-effect on a real mechanism* (metric-saturation): mechanism genuine, binary metric has no headroom.
2. *Degenerate binary test*: the argmin proportion saturates for any nonzero curiosity weight, so the PASS carries no graded evidence.

Both force the **same action** — re-operationalize the load-bearing selection statistic onto a continuous, variance-bearing form before either PASS can move governance. Resolving (1) vs (2) is not required to route. (The clean negative controls + non-saturated companion criteria favour reading 1.)

---

## 7. Learning + repair pathway

**Debt token:** `mystery (known data)` — we already have the data (per-seed density gaps `r1_density_gap` vary 58-80; the continuous per-candidate `scores`); the **frame (binary pref threshold) is wrong**. Reframe the readout — do **not** gather more runs, do **not** build substrate.

**Routing: `/queue-experiment` re-operationalization — alphabetic suffix `767a` / `768a`** (same scientific question, corrected instrument):

- Replace the saturating binary `pref_dense` load-bearing gate with the **continuous CEM score-margin** `mean(sparse_score − dense_score)` per trial, aggregated across seeds (user-selected). It is variance-bearing (the density gaps already vary 58-80 across seeds), reflects drive magnitude, and is **already computed internally** in `_pref_dense` — only discarded.
- Keep the clean OFF / single-drive controls, the counterbalancing, the equal-mass value isolation (768), and the weight-zeroing persistence check (767 L1c / 768 C4).
- **Recommend fixing the saturation at the shared `experiments/_lib` selection-instrument level** so the 766-lineage of SD-024/SD-025 CEM-selection diagnostics does not reproduce it.

**Not** demotion (mechanism not falsified). **Not** substrate build (`recommended_substrate_queue_entry.action = none`). **Re-derive brake: NOT fired** — 0 prior `substrate_ceiling`/`non_contributory` autopsies for either claim; and this reading is `measurement_degeneracy`, not a ceiling. **Granularity-debt trigger: not fired** — first autopsy on each claim.

### Draft `evidence_quality_note` (for `/governance` to write — do not write here)

- **SD-025 / V3-EXQ-767** — see `targets[0].recommended_evidence_quality_note` in the JSON.
- **ARC-057 / V3-EXQ-768** — see `targets[1].recommended_evidence_quality_note` in the JSON.

---

## 8. Routing summary for `/governance`

| Target | Adjudication | evidence_direction | epistemic_category | Route | Claim status |
|---|---|---|---|---|---|
| V3-EXQ-767 (SD-025) | vacuous | inconclusive | measurement_degeneracy | `/queue-experiment` 767a (CEM score-margin gate) | stays candidate |
| V3-EXQ-768 (ARC-057) | vacuous | inconclusive | measurement_degeneracy | `/queue-experiment` 768a (CEM score-margin gate) | stays candidate |

Neither PASS clears its gate; do **not** action SD-025 / ARC-057 on the current runs. Both re-queue with the continuous selection statistic; recommend a shared `_lib`-level fix.

*User scientific judgment (Step 8 gate, 2026-07-16): confirmed both targets held vacuous pending re-operationalization; confirmed CEM score-margin as the re-operationalized load-bearing gate.*
