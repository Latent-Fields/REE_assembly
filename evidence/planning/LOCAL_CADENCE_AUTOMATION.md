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
  --repos ree-v2 ree-experiments-lab ree-v1-minimal \
  --run-ingestion
```

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
  - `python3 .../sync_weekly_handoffs.py --repos ree-v2 ree-experiments-lab ree-v1-minimal --run-ingestion`
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
0 10 * * 4 cd /Users/dgolden/Documents/GitHub/REE_assembly && python3 evidence/planning/scripts/sync_weekly_handoffs.py --repos ree-v2 ree-experiments-lab ree-v1-minimal --run-ingestion
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
