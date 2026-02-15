# Local Cadence Automation (Weekly)

Purpose: run cross-repo handoff pull/ingest and outbound dispatch generation on a local schedule.

This guide assumes `REE_assembly` is at:

- `/Users/dgolden/Documents/GitHub/REE_assembly`

and cadence config:

- `evidence/planning/cadence_automation.v1.json`

---

## Scripts

- Handoff sync/import:
  - `python3 evidence/planning/scripts/sync_weekly_handoffs.py`
- Dispatch generation:
  - `python3 evidence/planning/scripts/emit_weekly_dispatches.py`
- Structure review dossiers:
  - `python3 evidence/planning/scripts/build_structure_review_dossiers.py`
- Connectome pull queue:
  - `python3 evidence/planning/scripts/build_connectome_literature_pull.py`
- Adjudication cascade application:
  - `python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied`
- Task inbox sync:
  - `python3 evidence/planning/scripts/sync_task_inbox.py`

---

## Recommended Weekday Commands

Run from `REE_assembly` root.

### Monday (ree-v2 handoff pull)

```bash
python3 evidence/planning/scripts/sync_weekly_handoffs.py --day MONDAY
```

### Tuesday (ree-experiments-lab handoff pull)

```bash
python3 evidence/planning/scripts/sync_weekly_handoffs.py --day TUESDAY
```

### Wednesday (ree-v1-minimal handoff pull)

```bash
python3 evidence/planning/scripts/sync_weekly_handoffs.py --day WEDNESDAY
```

### Thursday (full ingest + governance)

```bash
python3 evidence/planning/scripts/sync_weekly_handoffs.py \
  --full-run \
  --run-ingestion
```

Then generate structure dossiers (human decision packet):

```bash
python3 evidence/planning/scripts/build_structure_review_dossiers.py
```

Then generate connectome literature pull queue:

```bash
python3 evidence/planning/scripts/build_connectome_literature_pull.py
```

Then apply adjudication cascade (if any `applied` model-adjudication decisions exist):

```bash
python3 evidence/planning/scripts/apply_adjudication_cascade.py --decision-statuses applied
```

Note: `run_governance_cycle.py` now executes this step automatically unless `--skip-adjudication-cascade` is used.
It also runs task inbox sync automatically unless `--skip-task-inbox-sync` is used.
Checked (`- [x]`) task lines are removed from inbox automatically during sync.

### Friday (dispatch bundle generation for next week)

```bash
python3 evidence/planning/scripts/emit_weekly_dispatches.py
```

---

## Dry-Run Safety

Use these before turning on schedule:

```bash
python3 evidence/planning/scripts/sync_weekly_handoffs.py --day MONDAY --dry-run --skip-git-pull
python3 evidence/planning/scripts/emit_weekly_dispatches.py --date 2026-02-14
```

---

## launchd Example (macOS)

Create one plist per weekday trigger. Example command payloads:

- Monday:
  - `python3 .../sync_weekly_handoffs.py --day MONDAY`
- Tuesday:
  - `python3 .../sync_weekly_handoffs.py --day TUESDAY`
- Wednesday:
  - `python3 .../sync_weekly_handoffs.py --day WEDNESDAY`
- Thursday:
  - `python3 .../sync_weekly_handoffs.py --full-run --run-ingestion`
- Friday:
  - `python3 .../emit_weekly_dispatches.py`

Set `WorkingDirectory` to:

- `/Users/dgolden/Documents/GitHub/REE_assembly`

and log output to a local file for monitoring.

---

## cron Alternative

Example (Europe/Dublin local machine clock):

```cron
# Monday 09:00
0 9 * * 1 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/sync_weekly_handoffs.py --day MONDAY
# Tuesday 09:00
0 9 * * 2 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/sync_weekly_handoffs.py --day TUESDAY
# Wednesday 09:00
0 9 * * 3 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/sync_weekly_handoffs.py --day WEDNESDAY
# Thursday 10:00
0 10 * * 4 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/sync_weekly_handoffs.py --full-run --run-ingestion
# Friday 10:00
0 10 * * 5 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/emit_weekly_dispatches.py
```

---

## Outputs

- Handoff sync reports:
  - `evidence/planning/handoff_sync_reports/*.json`
- Weekly dispatch bundles:
  - `evidence/planning/outbound_dispatches/<YYYY-MM-DD>/*.md`
  - `evidence/planning/outbound_dispatches/<YYYY-MM-DD>/dispatch_report.json`
- Adjudication cascade outputs:
  - `evidence/decisions/adjudication_cascade_state.v1.json`
  - `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`

## Persistent Unfinished Items

Use:

- `evidence/planning/manual_carryover_items.v1.json`

Any item with `status != done` is automatically merged into each newly generated governance agenda so unfinished
manual items persist across weekly and full-run cycles.

Fast capture helper:

```bash
python3 evidence/planning/scripts/capture_carryover_item.py add --summary "Follow up X" --priority high
python3 evidence/planning/scripts/capture_carryover_item.py list --open-only
python3 evidence/planning/scripts/capture_carryover_item.py done --item-id MCI-0002
```

Checklist inbox helper:

```bash
python3 evidence/planning/scripts/sync_task_inbox.py --dry-run
python3 evidence/planning/scripts/sync_task_inbox.py
```
