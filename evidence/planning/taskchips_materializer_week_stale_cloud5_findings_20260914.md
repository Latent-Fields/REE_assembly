**Status: REVIEWED 2026-09-16 (user) -- staleness self-check landed REE_Working 6264f356a (2026-09-14).**

# TASK_CHIPS.json "week stale on cloud5" -- root-cause findings (2026-09-14)

Chip: `chip-20260914-taskchips-materializer-week-stale-cloud5`
Investigating session: headless worker on `ree-cloud-5`, worktree
`metaworker-chip-20260914-taskchips-materializer-week-stale-cloud5`, 2026-09-14T14:38Z-15:0xZ.

## Reported symptom (from the chip's own body)

> On ree-cloud-5 at cycle 3920 (2026-09-14T10:3x), the committed TASK_CHIPS.json's newest
> chip spawned_at is 2026-09-06T18:09:28Z, while `chip_ledger.py list --live` shows 114+ open
> work chips spawned through 2026-09-14, none of which exist in the local file.

## What did NOT turn out to be true (ruled out with evidence)

1. **The hub materializer is not broken.** `ree-v3/coordinator/task_claim_chip_git_writer.py`
   (author `REE Automation (Hub)`) has committed `phase2b-registry: materialize TASK_CHIPS.json`
   continuously and reliably the entire week, roughly every 2-4 minutes, with content that
   genuinely advances each time (verified via `git show <sha>:TASK_CHIPS.json` at ten separate
   points across 2026-09-05 through 2026-09-14 -- the max `spawned_at` inside the committed blob
   tracked "now minus 5-40 minutes" throughout, never stuck).
2. **`origin/master`'s committed history was never 8 days stale.** A `git log --grep
   "phase2b-registry" -- TASK_CHIPS.json` walk (initially misread as showing a gap -- it was just
   an un-truncated 605-line list, not a real gap) in fact shows continuous commits touching that
   path every few minutes throughout the week, matching (1).
3. **`ree-cloud-5` is not without a sync mechanism.** Two independent layers exist:
   - `ree-metaworker-autosync.timer`/`.service` (systemd, every 10 min, `OnBootSec=2min`),
     `ExecStart=/usr/local/bin/ree_metaworker_autosync.sh`, source
     `ree-v3/coordinator/deploy/ree-metaworker-autosync.sh`.
   - `ree-metaworker-dispatch.sh` (systemd timer, every 5 min) also runs the same
     `safe_adopt_ref.py --repo /Users/dgolden/REE_Working --branch master` sync at the top of
     every dispatch cycle, before invoking `claude -p`.
   Both were added 2026-09-01 (chip-20260901-fleet-autosync-repair) specifically because
   `ree-git-sync-repair.timer`'s cloud-worker repo list only ever covered `REE_assembly`/`ree-v3`,
   never the umbrella `REE_Working` checkout -- this was the actual historical gap, and it was
   closed two weeks before this chip was filed.
4. **The scripts named in the chip's step 3 genuinely have no `--live` mode** -- confirmed
   absent in `scripts/dispatch_candidate_order.py`, `scripts/check_substrate_directive.py`,
   `scripts/check_host_withhold.py`, `scripts/check_remote_control_required.py` (all read only
   `--path`, defaulting to `ROOT / "TASK_CHIPS.json"` with `ROOT` defaulting to
   `/Users/dgolden/REE_Working`, no HTTP import anywhere). `chip_ledger.py list --live` is the
   only script in the family that supports it. This part of the original chip's suspicion is
   correct as stated, but see "Recommended fix" below for why it's a mitigation, not the root
   cause fix.

## What DID happen: a confirmed 26.8-hour autosync outage, 2026-09-06 -> 2026-09-07

`~/ree_metaworker_autosync.log` on ree-cloud-5 (goes back to 2026-09-01, ~11k lines) shows:

- Last successful sync before the gap: `[2026-09-06T18:10:42Z] autosync: ok (29b312635)`.
- Next log line of any kind: `[2026-09-07T21:00:14Z] safe_adopt_ref: master moved
  29b3126358 -> 7c0cbf9c81 (adopted origin/master)` -- a **26.8-hour silence**, confirmed two
  ways: (a) the raw log line-gap above, (b) an independent walk of this box's `git reflog show
  master` which found the same gap as the single largest (26.8h) in the whole 13-day window.
- `systemctl status ree-metaworker-autosync.timer` independently reports `Active: active
  (waiting) since Mon 2026-09-07 20:57:31 UTC` -- i.e. the **timer unit itself was
  (re)started at 2026-09-07T20:57:31Z**, ~3 minutes before the first post-gap sync completed.
  This means the systemd unit was not merely failing silently during the gap -- it was not
  running at all, then got (re)installed/restarted.
- Log volume by day corroborates the same window: ~270 lines/day is the steady-state baseline
  (2 lines per successful cycle x ~135 cycles/day); 2026-09-06 has only 202 and 2026-09-07 has
  only 36, then every day from 09-08 onward is back to ~270-272.
- **This timing match is exact.** The chip's reported frozen value, `2026-09-06T18:09:28Z`, is
  74 seconds before the log's last successful sync at `2026-09-06T18:10:42Z` -- consistent with
  that sync having captured whatever chip the hub had most recently materialized at that moment.

**After 2026-09-07T21:00, the mechanism was healthy for the rest of the week** -- confirmed by
both the steady ~270/day log volume and by direct content checks (`git show <sha>:TASK_CHIPS.json`
as-of ten timestamps between 2026-09-08 and 2026-09-14, all showing max `spawned_at` within
~5-40 minutes of "now" at each checked point, including as-of 2026-09-14T10:30Z -- the exact
window the reporting session says it observed the staleness).

## The unresolved gap in this account

Given (a) the outage was real but only 26.8 hours, and (b) the mechanism was demonstrably
healthy again by the time the reporting session ran (cycle 3920, ~10:30Z), **the reporting
session's own read must have come from something that did not re-acquire fresh state after the
outage ended** -- not from the umbrella checkout's committed content, which was fine by then.
The most likely candidate, not confirmed with direct evidence (the reporting session's own
process/PID could not be inspected retroactively): a `claude -p` dispatch cycle or the
long-running Orchestrator process that was itself alive across the outage window and never
re-read `TASK_CHIPS.json` from disk after its own start/last-refresh, continuing to operate on
an in-memory or otherwise-cached view taken at or before 2026-09-06T18:10:42Z until cycle 3920.
`ree-metaworker-dispatch.sh`'s own header documents exactly this class of hazard from a prior
incident (2026-08-03, "this box ran 47 cycles (~4h) on a since-fixed heartbeat-commit bug ...
no mechanism to pick the fix up short of a manual pull") -- the autosync-before-every-cycle
design was the fix for THAT case (a stale binary/script), but does not obviously cover a
process that is itself long-lived and never restarts to pick up the resync.

This session did not have a way to inspect a now-gone process's state to confirm this
hypothesis further; it is offered as the most evidence-consistent explanation, not a proven
mechanism.

## Relationship to the DLAPTOP wedge chips

`chip-20260914-dlaptop-reeworking-wedge-metaworkerlearning-referral` and the
`chip-refwedge-dlaptop-ree-working-master-g4`/`g5` generations describe a **mechanistically
different** failure (DLAPTOP's `safe_adopt_ref.py` actively REFUSING for 16h+ because of local
unpushed commits -- an ongoing, still-open wedge needing a per-commit audit) from this one (a
transient ~27h service outage on ree-cloud-5 that self-recovered, followed by an apparently
stuck long-lived consumer). They share the same **category** -- a checkout or a process
serving stale local coordination-plane reads without any visible error -- which is exactly the
recurring pattern class the `checkoutdiverged-dlaptop-...-g3/g4/g5` chips have already
flagged for a `/metaworker-learning` root-cause pass rather than one-off re-fixes. This
session did not fold its own findings into that chip (does not own it, and the chip's `kind:
decision` is for a human to actually run the pass); leaving this doc as the pointer for
whoever does.

## Recommended fix (not implemented by this session -- see follow-on chip)

The concrete, narrowly-scoped mitigation: give `dispatch_candidate_order.py` (and ideally the
`ree-metaworker-dispatch.sh` wrapper, before it even invokes `claude -p`) a **staleness
self-check** -- compare `TASK_CHIPS.json`'s max `spawned_at` against wall-clock "now" and WARN
(or refuse to dispatch) if the gap exceeds a threshold (e.g. 2h, well above the 10-minute
autosync cadence plus normal jitter). This is a better-targeted fix than the chip's suggested
`--live` HTTP fallback: the root cause here was never "the script can't reach the API," it was
"nothing detected that the read was stale," so a self-check that fires BEFORE a dispatch cycle
silently acts on week-old data is the fix that actually closes this specific hole. A `--live`
escape hatch (mirroring `chip_ledger.py list --live`) is still a reasonable secondary/manual
fallback for a human diagnosing a live wedge, and is not mutually exclusive with the
self-check.

Filed as a separate `kind: work` chip rather than implemented here, since it touches a script
every dispatch cycle on every cloud box depends on and deserves its own review/test pass rather
than being folded into a root-cause investigation session.
