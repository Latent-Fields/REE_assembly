# Weekly Dispatch - ree-v2

Generated: `2026-02-21T16:30:51.150927Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-v2`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`
- Architecture epoch: `ree_hybrid_guardrails_v1`
- Epoch start (UTC): `2026-02-15T15:31:31Z`
- Epoch policy source: `evidence/planning/planning_criteria.v1.yaml`

## Proposals

| proposal_id | claim_id | priority | experiment_type | dispatch_mode | decision_deadline_utc | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXP-0023` | `MECH-060` | `high` | `commit_dual_error_channels` | `discriminative_pair` | `2026-02-24T16:23:03.753684Z` | Run a decision-grade contamination ablation pair for MECH-060 (strict write-locus separation vs mixed-channel relaxation). | Run exactly one contamination-focused discriminative pair: strict commit-boundary write-locus guards vs explicit mixed-channel relaxation.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register contamination thresholds and attribution-reliability pass/fail criteria before execution, then report deltas.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; Package outputs as decision-grade comparison by `2026-02-24T16:23:03.753684Z`; explicitly score outcomes `retain_ree\|hybridize\|adopt_jepa_structure\|retire_ree_claim`. |
| `EXP-0024` | `MECH-058` | `high` | `jepa_anchor_ablation` | `discriminative_pair` | `2026-02-24T16:23:03.753684Z` | Run a decision-grade MECH-058 rate-separation pair on shared JEPA substrate (strong asymmetry vs relaxed asymmetry). | Run exactly one rate-separation discriminative pair: shared JEPA substrate with strong fast/slow asymmetry vs relaxed asymmetry.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register drift/collapse thresholds and attribution-preservation pass/fail criteria before execution, then report deltas.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; Package outputs as decision-grade comparison by `2026-02-24T16:23:03.753684Z`; explicitly score outcomes `retain_ree\|hybridize\|adopt_jepa_structure\|retire_ree_claim`. |
| `EXP-0025` | `Q-017` | `high` | `control_axis_ablation` | `discriminative_pair` | `n/a` | Run an adjudication-focused Q-017 pair (full orthogonal control axes vs minimal subset) with explicit regime-separation scoring. | Run exactly one control-axis discriminative pair: full orthogonal axis set vs reduced axis subset.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register regime-separation thresholds before execution, then report deltas.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; Explicitly report adjudication impact for outcomes `retain_ree\|hybridize\|adopt_jepa_structure\|retire_ree_claim`. |
| `EXP-0026` | `MECH-062` | `high` | `tri_loop_arbitration_policy` | `discriminative_pair` | `n/a` | Run a tri-loop arbitration policy pair for MECH-062 (baseline vs disinhibitory sweep check) to lock a best-performing gate policy. | Run exactly one arbitration-policy discriminative pair: baseline tri-loop arbitration vs disinhibitory sweep check policy.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register cross-gate conflict-resolution thresholds before execution, then report deltas.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0027` | `Q-016` | `high` | `tri_loop_arbitration_policy` | `discriminative_pair` | `n/a` | Run an explicit Q-016 arbitration bake-off (baseline vs disinhibitory sweep check) and score coupling-collapse risk. | Run exactly one arbitration-policy discriminative pair: baseline tri-loop arbitration vs disinhibitory sweep check policy.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register cross-gate conflict-resolution thresholds before execution, then report deltas.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-v2`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0023` / `MECH-060` / `commit_dual_error_channels` (mode=discriminative_pair; deadline=2026-02-24T16:23:03.753684Z; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim)
- `EXP-0024` / `MECH-058` / `jepa_anchor_ablation` (mode=discriminative_pair; deadline=2026-02-24T16:23:03.753684Z; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim)
- `EXP-0025` / `Q-017` / `control_axis_ablation` (mode=discriminative_pair; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim)
- `EXP-0026` / `MECH-062` / `tri_loop_arbitration_policy` (mode=discriminative_pair)
- `EXP-0027` / `Q-016` / `tri_loop_arbitration_policy` (mode=discriminative_pair)

Contract to follow exactly:
- `evidence/experiments/INTERFACE_CONTRACT.md`

Epoch tagging requirements:
- Stamp every new run `manifest.json` with `"architecture_epoch": "ree_hybrid_guardrails_v1"`.
- Keep `timestamp_utc` aligned with the current epoch window (`>= 2026-02-15T15:31:31Z`).

Acceptance checks per proposal:
- Use discriminative pairs (primary vs explicit ablation/control), not broad profile sweeps.
- Use matched shared seeds across pair conditions and pre-register thresholds before execution.
- At least 2 additional runs with distinct seeds unless stricter pair checks are specified in proposal acceptance checks.
- Experiment Pack validates against v1 schema.
- Each emitted manifest includes `architecture_epoch=ree_hybrid_guardrails_v1`.
- Result links to claim_ids_tested and updates matrix direction counts.

Output required:
- concise run table: run_id, seed, status, key metrics, evidence_direction
- list of generated run pack paths
```
