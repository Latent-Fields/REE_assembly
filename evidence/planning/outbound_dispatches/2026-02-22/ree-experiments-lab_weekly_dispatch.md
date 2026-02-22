# Weekly Dispatch - ree-experiments-lab

Generated: `2026-02-22T16:07:31.965256Z`

## Context

- Source: `evidence/planning/experiment_proposals.v1.json`
- Target repo: `ree-experiments-lab`
- Contract reference: `evidence/experiments/INTERFACE_CONTRACT.md`
- Architecture epoch: `ree_hybrid_guardrails_v1`
- Epoch start (UTC): `2026-02-15T15:31:31Z`
- Epoch policy source: `evidence/planning/planning_criteria.v1.yaml`

## Proposals

| proposal_id | claim_id | priority | experiment_type | dispatch_mode | decision_deadline_utc | objective | acceptance_checks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXP-0001` | `MECH-061` | `high` | `claim_probe_mech_061` | `discriminative_pair` | `2026-02-25T16:07:31.471252Z` | Generate decision-grade discriminative evidence for MECH-061 before governance deadline. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; Package outputs as decision-grade comparison by `2026-02-25T16:07:31.471252Z`; explicitly score outcomes `retain_ree\|hybridize\|adopt_jepa_structure\|retire_ree_claim`. |
| `EXP-0002` | `MECH-057` | `high` | `claim_probe_mech_057` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for MECH-057 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; If conflicting behaviors persist, split the claim into atomic subclaims before requesting another broad rerun. |
| `EXP-0003` | `Q-013` | `high` | `claim_probe_q_013` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-013 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; If conflicting behaviors persist, split the claim into atomic subclaims before requesting another broad rerun. |
| `EXP-0004` | `Q-014` | `high` | `claim_probe_q_014` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-014 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; If conflicting behaviors persist, split the claim into atomic subclaims before requesting another broad rerun. |
| `EXP-0005` | `ARC-003` | `high` | `claim_probe_arc_003` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for ARC-003 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0006` | `Q-012` | `high` | `claim_probe_q_012` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-012 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts.; If conflicting behaviors persist, split the claim into atomic subclaims before requesting another broad rerun. |
| `EXP-0007` | `Q-001` | `high` | `claim_probe_q_001` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-001 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |
| `EXP-0008` | `Q-002` | `high` | `claim_probe_q_002` | `discriminative_pair` | `n/a` | Run a discriminative support-vs-ablation pair for Q-002 with matched seeds and pre-registered thresholds. | Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.; Use at least 2 matched seeds shared across both pair conditions.; Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.; Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.; Experiment Pack validates against v1 schema.; Result links to claim_ids_tested and updates matrix direction counts. |

## Copy/Paste Prompt

```md
You are Codex operating in `ree-experiments-lab`.

Goal: execute this week's approved proposals and emit contract-compliant Experiment Packs.

Required work items:
- `EXP-0001` / `MECH-061` / `claim_probe_mech_061` (mode=discriminative_pair; deadline=2026-02-25T16:07:31.471252Z; required_outcomes=retain_ree|hybridize|adopt_jepa_structure|retire_ree_claim)
- `EXP-0002` / `MECH-057` / `claim_probe_mech_057` (mode=discriminative_pair)
- `EXP-0003` / `Q-013` / `claim_probe_q_013` (mode=discriminative_pair)
- `EXP-0004` / `Q-014` / `claim_probe_q_014` (mode=discriminative_pair)
- `EXP-0005` / `ARC-003` / `claim_probe_arc_003` (mode=discriminative_pair)
- `EXP-0006` / `Q-012` / `claim_probe_q_012` (mode=discriminative_pair)
- `EXP-0007` / `Q-001` / `claim_probe_q_001` (mode=discriminative_pair)
- `EXP-0008` / `Q-002` / `claim_probe_q_002` (mode=discriminative_pair)

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
