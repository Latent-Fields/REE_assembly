# Hobby Operator Playbook (REE-v2)

Purpose: keep progress structured for spare-time work with explicit weekly decisions.

Audience: single-operator workflow using a constrained local machine (currently `MacBook Air M2 2022`).

---

## Weekly Checklist

1. Monday (planning + placement)
- Review pending experiments for this cycle.
- Run resource estimator and mark each run `local` or `remote`.
- Set this week target workload hours.

2. Tuesday to Wednesday (execution)
- Run local smoke checks and schema/hook validation.
- Launch remote jobs for heavy profiles.
- Track blocked local sessions (thermal/runtime/OOM).

3. Thursday (handoff + ingest prep)
- Prepare weekly handoff packet using:
  - `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
- Confirm CI gate status and run-pack inventory completeness.

4. Friday (review + next cycle decision)
- Record rolling 3-month cloud spend.
- Update local compute recommendation (`hold_cloud_only|upgrade_low|upgrade_mid|upgrade_high`).
- Capture blockers and next cycle focus.

---

## Hobby-Mode Local Hardware Decision Policy

Default state:

- `hold_cloud_only`

Runtime placement baseline for this hobby setup:

- offload to remote if estimated per-run runtime `> 360 minutes (6 hours)`
- offload to remote if estimated batch runtime `> 360 minutes (6 hours)`
- offload to remote for multi-seed qualification sweeps (`>2 seeds/condition`)

Upgrade triggers:

1. `upgrade_low`
- local friction is increasing, and
- rolling 3-month cloud spend is below `EUR 80/month`.

2. `upgrade_mid`
- rolling 3-month cloud spend is `>= EUR 100/month`, or
- blocked local sessions exceed `2/week` for 3 consecutive weeks.

3. `upgrade_high`
- rolling 3-month cloud spend is `>= EUR 250/month` for 3 consecutive months, and
- active qualification workload is `>10 hours/week`.

If unclear, remain at `hold_cloud_only` and reassess next week.

---

## Required Records

Keep the following updated each cycle:

- `docs/ops/local_compute_options.md` (in `ree-v2`)
- weekly handoff `Local Compute Options Watch` section
- short rationale for any change in recommendation status
