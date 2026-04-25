# Synthetic Evidence Audit

**Prepared:** 2026-02-26
**Reason:** ree-v2 and ree-experiments-lab archived as synthetic scaffolding only. All PASS/FAIL results they produced are unreliable as evidence for REE claims.
**Revalidation update:** 2026-04-25

---

## Summary

All experimental runs in `evidence/experiments/` that originated from `ree-v2` or `ree-experiments-lab` are **synthetic parametric data**, not genuine measurements. This audit catalogs which claims are affected and what genuine re-experimentation is required.

The old run directories are retained for auditability, but governance must not treat the old
synthetic rows as active evidence. Current scoring uses epoch applicability
(`epoch_start_utc = 2026-02-27T00:00:00Z`) plus `docs/claims/scoring_exclusions.json`.
Rows from the pre-cutover JEPA/synthetic experiment families should appear only as
`stale_epoch` or explicit `invalid_run`/`superseded` audit rows.

**Valid substrates at time of original audit:** `ree-v1-minimal` only.
**Current valid substrates:** genuine post-cutover V2/V3 evidence tagged with
`architecture_epoch: ree_hybrid_guardrails_v1`, plus retained genuine V1/V2 rows.
**Genuine experiments completed as of original audit (3 total):**

| experiment | claim | result |
|---|---|---|
| `consolidation_ablation` | CSH-1 (consolidation improves multi-hop reasoning) | **PASS** |
| `training_run` | Harm reduction under training | **IMPROVED** (harm 1.0→0.675) |
| `control_plane_precision_separation` | MECH-059 (confidence channel separate from PE) | **PASS** (2026-02-26, EVB-0037) |

## 2026-04-25 Revalidation Status

| claim | current status | revalidation disposition |
|---|---|---|
| MECH-056 | provisional | Revalidated for current scoring by `20260314T220919_residue_trajectory_placement_v2` (PASS/supports). Old `trajectory_integrity` rows are stale_epoch audit rows. |
| MECH-057a | provisional | Not fully revalidated. V2 support remains, but V3 EXQ-139 and EXQ-203 are substrate/proxy-limited and explicitly excluded. Needs a genuine V3 action-sequence substrate test. |
| MECH-057b | candidate | Not revalidated. Zero counted genuine experimental evidence. Needs first V3 hippocampal trajectory-promotion test after substrate support exists. |
| MECH-058 | retired | Do not revalidate as JEPA/anchor or learning-rate separation. Retired/superseded by MECH-069; obsolete timescale probes are excluded from scoring. |
| MECH-059 | active | Revalidated by counted precision-separation PASS (`20260314T202143_control_plane_precision_separation_v2`). Old `jepa_uncertainty_channels` rows are stale_epoch audit rows. |
| MECH-060 | provisional | Revalidated by counted write-locus PASS (`20260314T235933_write_locus_contamination_v2`). Old `commit_dual_error_channels` rows are stale_epoch audit rows. |
| MECH-061 | active | Revalidated by counted commit-boundary PASS (`20260315T024049_commitment_boundary_validation_v2`). |
| Q-012 | candidate | Synthetic rows no longer count. EXQ-152 is superseded/excluded; EXQ-193 is the counted mixed V3 result and supports the REE-vs-predictive gap but not the no-learning floor criterion. |
| Q-013 | legacy/retired | JEPA integration was decoupled 2026-03-29. V3-EXQ-153 is excluded as post-retirement external-substrate proxy evidence; MECH-059 owns the REE-native precision-routing question. |
| Q-014 | legacy/retired | JEPA-specific question retired. V3-EXQ-154 is superseded; the REE-native blind-spot concern moved to MECH-128 and SD-008. |

---

## Archived / Synthetic Sources

| Repo | Status | Evidence quality |
|---|---|---|
| `ree-v2` | Archived 2026-02-26 — not the canonical substrate | Parametric synthetic — all results invalid |
| `ree-experiments-lab` | Archived 2026-02-26 — synthetic scaffolding only | Synthetic parametric — all results invalid |

---

## Experiment Types with Synthetic-Only Evidence (need genuine re-run)

These experiment types exist in `evidence/experiments/` but all runs originated from synthetic sources:

| experiment type | primary claim | current claim status | synthetic run count |
|---|---|---|---|
| `claim_probe_arc_003` | ARC-003 | active (architectural) | 7 |
| `claim_probe_arc_007` | ARC-007 | active (architectural) | 12 |
| `claim_probe_mech_033` | MECH-033 | candidate | 10 |
| `claim_probe_mech_040` | MECH-040 | active | 9 |
| `claim_probe_mech_046` | MECH-046 | active | 9 |
| `claim_probe_mech_056` | MECH-056 | candidate | 42 |
| `claim_probe_mech_057` | MECH-057 | candidate | 10 |
| `claim_probe_mech_058` | MECH-058 | candidate | 30 |
| `claim_probe_mech_059` | MECH-059 | active | 38 |
| `claim_probe_mech_060` | MECH-060 | candidate | 30 |
| `claim_probe_mech_061` | MECH-061 | active | 8 |
| `claim_probe_mech_062` | MECH-062 | stable | 44 |
| `claim_probe_mech_063` | MECH-063 | active | 2 |
| `claim_probe_q_001` | Q-001 | active (open question) | 11 |
| `claim_probe_q_002` | Q-002 | active (open question) | 11 |
| `claim_probe_q_003` | Q-003 | active (open question) | 11 |
| `claim_probe_q_004` | Q-004 | active (open question) | 11 |
| `claim_probe_q_005` | Q-005 | active (open question) | 11 |
| `claim_probe_q_006` | Q-006 | active (open question) | 1 |
| `claim_probe_q_007` | Q-007 | active (open question) | 12 |
| `claim_probe_q_008` | Q-008 | legacy | 12 |
| `claim_probe_q_009` | Q-009 | legacy | 12 |
| `claim_probe_q_010` | Q-010 | legacy | 11 |
| `claim_probe_q_012` | Q-012 | candidate | 8 |
| `claim_probe_q_013` | Q-013 | active | 11 |
| `claim_probe_q_014` | Q-014 | active | 11 |
| `claim_probe_q_015` | Q-015 | active | 9 |
| `claim_probe_q_017` | Q-017 | active | 30 |
| `commit_dual_error_channels` | MECH-060 | candidate | 137 total (ree-v2: 92, lab: 25, v1-min: 20 — all invalid; v1-min runs used ree-v2 qualification harness) |
| `control_axis_ablation` | ARC-005 / MECH-062 | stable | 88 total |
| `jepa_anchor_ablation` | MECH-058 | candidate | 126 total (all synthetic) |
| `jepa_uncertainty_channels` | MECH-059 | active | 126 total (all synthetic) |
| `trajectory_integrity` | MECH-056 | candidate | 121 total (all synthetic) |
| `tri_loop_arbitration_policy` | MECH-062 | stable | 113 total |

> **Note on "ree-v1-minimal" labelled runs:** Run IDs ending in `_toyenv_internal_minimal` were generated by the `ree-v2-qualification-harness` runner using `toy_env_runner.v1+internal_minimal`, with `source_repo.name: "ree-v2"`. These are NOT genuine ree-v1-minimal experiments despite the name. Confirmed via manifest inspection (e.g. `commit_dual_error_channels/runs/2026-02-21T151442Z_.../manifest.json`).

---

## Impact Assessment by Claim Category

### Safe — Status not determined by experiments

These claims were set to their current status based on **architectural reasoning and design docs**, not experimental evidence. Synthetic evidence adds supplementary data but did not determine the status.

| category | count | rationale |
|---|---|---|
| INV-001 through INV-017 (invariants) | 17 | Purely architectural. No experiments. |
| ARC-001, 002, 004, 005, 009-015 | 11 | Architectural commitments. |
| IMPL-001, 002, 003, 005, 010-014, 017-018 | 8 | Implementation notes. |
| Q-001 through Q-007 | 7 | Open questions — `active` means "this question is open and being tracked." Status is valid regardless of evidence quality. |

### Architectural adjudications — Valid despite synthetic evidence

These claims were adjudicated with outcomes of `retain_ree` or `hybridize`. The adjudication direction is a **strategic architectural decision** (which path to pursue), not an empirical finding. Synthetic evidence may have influenced confidence percentages but did not reverse the directional choice. Status is maintained.

| claim | adjudication outcome | rationale |
|---|---|---|
| MECH-059 | retain_ree | Keep REE's precision/confidence channel. Valid: JEPA decoupled. |
| MECH-061 | retain_ree | Keep REE's commitment boundary token approach. Valid: JEPA decoupled. |
| Q-013 | hybridize | Stochastic uncertainty calibration as REE design direction. Valid. |
| Q-014 | hybridize | Ethical relevance blind spot — REE-native implementation intended. Valid. |
| Q-015 | retain_ree | Commitment boundary minimal contract. Valid. |
| Q-017 | hybridize | Control plane axis set as REE design direction. Valid. |
| ARC-003 | retain_ree | E3 trajectory commitment. Valid. |
| ARC-007 | hybridize | Hippocampal path memory. Valid. |

**Critical caveat:** While the adjudication DIRECTIONS are valid, the **mechanistic predictions** (i.e., whether the chosen approach actually performs as intended) cannot be confirmed without genuine ree-v1-minimal experiments.

### Candidates with contaminated evidence — Need genuine experiments

These claims are already `candidate` status (correctly not promoted) but their adjudication confidence scores are unreliable due to synthetic evidence. Prior experimental data in their experiment type directories should be treated as indicative only.

| claim | subject | confidence (synthetic) | genuine experiment needed |
|---|---|---|---|
| MECH-056 | residue.trajectory_first_placement | 0.766 (synthetic) | `claim_probe_mech_056` on ree-v1-minimal |
| MECH-057 | uncertainty.jepa_pe_routing | 0.525 (synthetic) | `claim_probe_mech_057` on ree-v1-minimal |
| MECH-058 | latent_stack.e1_e2_timescale_separation | 0.725 (synthetic) | `claim_probe_mech_058` on ree-v1-minimal |
| MECH-060 | commitment.dual_error_channels_pre_post_commit | 0.733 (synthetic) | `commit_dual_error_channels` on ree-v1-minimal |
| Q-012 | latent_predictive_models.control_completion_falsifiability | 0.503 (synthetic) | `claim_probe_q_012` on ree-v1-minimal |

---

## Evidence Re-Validation Roadmap

The original roadmap below is kept for audit history. As of 2026-04-25, P1 items
MECH-059, MECH-060, and MECH-061 have counted genuine support. The active blockers
are MECH-057a (faithful V3 action-sequence test), MECH-057b (first V3 trajectory
promotion test), and Q-012 (corrected REE-vs-predictive follow-up that also beats
the no-learning floor). MECH-058 should not be re-run under its old JEPA/anchor
framing because the claim is retired and superseded by MECH-069.

Priority order from the original 2026-02-26 audit:

### P1 — Highest priority (mechanistic predictions for active claims)

1. **MECH-059 mechanistic validation**: Does REE's precision/confidence channel actually separate from PE? Design a probe that measures confidence channel independence on ree-v1-minimal.
2. **MECH-060 / commit_dual_error_channels**: Design and run pre/post-commit dual error routing experiment in ree-v1-minimal. MECH-060 is `pending_design` — design must precede experiment.
3. **MECH-061 mechanistic validation**: Does REE's commitment boundary token reclassification work as predicted?

### P2 — Candidate promotion blockers

4. **MECH-056 / trajectory_integrity**: Residue placed at trajectory positions. Needs genuine rollout experiment.
5. **MECH-058 / old anchor-ablation framing** (historical only): no active rerun; claim retired and superseded by MECH-069.
6. **MECH-057 split**: MECH-057a needs faithful action-sequence testing; MECH-057b needs first V3 hippocampal trajectory-promotion test.

### P3 — Open question validation

7. **Q-013 through Q-017**: Validate hybridize decisions with genuine ree-v1-minimal experiments once P1/P2 mechanisms are in place.
8. **Q-001 through Q-007** (astrocyte/entity binding questions): These remain open — design experiments once ree-v1-minimal has astrocyte stack.

---

## What This Does NOT Change

- **Claim statuses are maintained.** No demotions are needed: status transitions were based on architectural decisions, not experimental PASS/FAIL counts.
- **Architecture documents remain valid.** The design decisions in `docs/architecture/` stand.
- **Decision log entries stand.** Decisions were architectural, not empirical.
- **Only confidence scores are unreliable.** The confidence numbers in `claim_evidence.v1.json` based on synthetic runs should be treated as rough indicators, not validated measurements.
