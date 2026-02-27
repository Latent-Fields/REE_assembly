# Governance State

Generated: `2026-02-27`
Maintained: manually, updated after each governance cycle or major corpus change.

This file provides an honest snapshot of the current evidence corpus state so that
governance tooling and human reviewers can make correctly-calibrated decisions.

---

## Synthetic Evidence Contamination

All experiments conducted before 2026-02-26 used synthetic substrates:

- **ree-v2** (`_toyenv_internal_minimal` run_id suffix) — archived 2026-02-26
- **ree-experiments-lab** — archived 2026-02-26

These substrates generated plausible-looking statistical outputs but did not involve
the actual REE agent architecture. Their confidence scores, conflict ratios, and
direction counts in `claim_evidence.v1.json` are **unreliable as architecture evidence**.

The `promotion_demotion_recommendations.md` file now flags claims with zero genuine runs
with `⚠️ Synthetic data flag` and overrides the statistical recommendation with
`collect_genuine_evidence`. Do not promote or demote these claims based on the existing
confidence scores.

---

## Genuine Evidence Corpus (as of 2026-02-27)

The only valid experimental substrate is **ree-v1-minimal** (run_id suffix: `_ree_v1_minimal`).

### Completed Genuine Experiments

| EXQ | EVB | Claim(s) | Experiment | Result | Completed |
|-----|-----|----------|-----------|--------|-----------|
| EXQ-000 | EVB-0037 | MECH-059 | Control Plane Precision Separation | **PASS** | 2026-02-26T16:13Z |
| EXQ-001 | EVB-0039 | MECH-056 | Residue Trajectory Placement | **PASS** | 2026-02-26T20:52Z |
| EXQ-002 | EVB-0040 | MECH-058 | E1/E2 Timescale Ablation | **FAIL** (substrate resolution) | 2026-02-26T21:37Z |
| EXQ-003 | EVB-0041 | MECH-061 | Commitment Boundary Token Reclassification | **PASS** | 2026-02-26T22:24Z |
| EXQ-004 | EVB-0042 | MECH-057 | Control Completion Requirement | **FAIL** (informative baseline) | 2026-02-26T23:24Z |

### Genuine Run Counts per Claim

| Claim | Genuine Runs | Synthetic Runs | Reliable? |
|-------|-------------|----------------|-----------|
| MECH-056 | 2 | 163 | Partially — genuine PASS dominates |
| MECH-057 | 2 | 12 | Partially — genuine FAIL informative |
| MECH-058 | 2 | 156 | Partially — genuine FAIL (substrate limit) |
| MECH-059 | 2 | 164 | Partially — genuine PASS dominates |
| MECH-061 | 2 | 10 | Partially — genuine PASS dominates |
| All other claims | 0 | varies | **Unreliable — all synthetic** |

Claims with 2 genuine runs have directionally meaningful signal but remain statistically
thin. The overall_confidence figures in `claim_evidence.v1.json` are dominated by the
larger synthetic entry counts and should be treated with caution.

---

## Claims with Reliable Status Changes (from Genuine Evidence)

| Claim | Previous Status | New Status | Basis |
|-------|----------------|------------|-------|
| MECH-059 | candidate | **active** (adjudicated) | EXQ-000 PASS + architecture decision retain_ree |
| MECH-056 | candidate | **provisional** | EXQ-001 PASS — residue placement confirmed |
| MECH-061 | candidate | **active** (adjudicated) | EXQ-003 PASS + commitment boundary confirmed |
| MECH-058 | candidate | candidate (unchanged) | EXQ-002 FAIL — substrate resolution issue |
| MECH-057 | candidate | candidate (unchanged) | EXQ-004 FAIL — informative baseline, redesign needed |

---

## Pending Genuine Experimentation

| EXQ | EVB | Claim(s) | Status | Notes |
|-----|-----|----------|--------|-------|
| EXQ-005 | EVB-0043 | MECH-060, MECH-067 | `needs_script` | Write-locus contamination ablation (FULL / CONTAMINATED_DURABLE / CONTAMINATED_RESIDUE). Script at `ree-v1-minimal/experiments/write_locus_contamination.py`. ~22.5 min estimated. |

---

## Governance Pipeline Health

### `build_experiment_indexes.py` Modes

| Mode | When to use | What it writes |
|------|-------------|----------------|
| `python3 build_experiment_indexes.py --index-only` | After ingesting new experiment results | `claim_evidence.v1.json`, `INDEX.md`, `TODOs.md`, `decision_state.md` |
| `python3 build_experiment_indexes.py` | After full governance review | All of the above + `evidence_backlog.v1.json`, `experiment_proposals.v1.json`, `architecture_gap_register.v1.json`, `promotion_demotion_recommendations.md`, `conflicts_report.md` |

**Use `--index-only` immediately after experiment ingestion** to update the evidence matrix
without regenerating the backlog or overwriting manually-maintained planning artefacts.

Reserve the full rebuild for explicit governance review sessions.

### Backlog Stability

`evidence_backlog.v1.json` is regenerated from scratch on each full build. EVB IDs are
positional — IDs shift if the sort order changes. Do not reference EVB IDs in persistent
cross-repo documents; use claim_ids instead.

Items with `pinned: true` are preserved across regeneration. Items from the ree-v1-minimal
`experiment_queue.json` (EVB-0039 through EVB-0043) are not in the auto-generated backlog
— they live in the experimental substrate repo and are tracked via `runner_status.json`.

### Promotion/Demotion Recommendations Reliability

| Recommendation type | Reliability |
|--------------------|-------------|
| `collect_genuine_evidence` (⚠️ synthetic flag) | **High** — derived from run_id patterns, not statistics |
| Recommendations for MECH-056/057/058/059/061 | **Medium** — genuine results exist but statistics still polluted by synthetic entries |
| All other recommendations (Q-*, ARC-*, IMPL-*, etc.) | **Low** — based entirely on synthetic evidence; do not act without genuine runs |

---

## Pending Governance Decisions

| Claim | Decision | Status | Notes |
|-------|----------|--------|-------|
| Q-012 | demote_to_candidate | `pending_user` | Recommendation changed from prior `retain_ree`; needs fresh review |
| MECH-040 | collect_genuine_evidence | `pending_user` | Demotion recommendation was stale (synthetic data); wait for genuine run |
| MECH-046 | collect_genuine_evidence | `pending_user` | Same as MECH-040 |
| Q-015 | hold | `pending_user` | Prior demotion recommendation superseded by MECH-061 PASS (EXQ-003) |

---

## Architecture Epoch Registry

| Epoch ID | Description | Start UTC | Source Repo |
|----------|-------------|-----------|-------------|
| `ree_hybrid_guardrails_v1` | Current planning epoch (all post-adjudication entries) | 2026-02-15T15:31Z | N/A (planning criteria) |
| `ree_v1_minimal_genuine_v1` | Genuine ree-v1-minimal experiment results | 2026-02-26T00:00Z | ree-v1-minimal |

The build scanner reads `architecture_epoch` from `manifest.architecture_epoch` (top level)
or falls back to `current_architecture_epoch` from planning_criteria. Genuine EXQ manifests
now store `architecture_epoch: ree_v1_minimal_genuine_v1` at the top level (fixed 2026-02-27).
The contamination filter in `_genuine_run_count()` also accepts the `_ree_v1_minimal` run_id
suffix as a fallback for resilience.
