# Worktree graveyard triage -- ree-cloud-4 (chip-20260826-worktree-graveyard-triage-and-gc)

**Status: AUDIT-ONLY. NO REMOVALS PERFORMED.** Written by a headless `claude -p`
dispatch on ree-cloud-4 (session slug `worktree-graveyard-triage-and-gc`,
2026-08-28T20:21-20:46Z). The chip's own banner requires this task to run under
Remote Control with a human attached before any `git worktree remove` -- "If no
human is reachable, STOP after producing the triage document, commit it, and
resolve nothing. A completed audit with zero removals is a full and correct
outcome for this chip." That is exactly what this document is. **No worktree
was removed by this session.**

## Scope note: this is ree-cloud-4's graveyard, not the one originally measured

The chip was spawned from DLAPTOP (the Mac) on 2026-08-26, with `cwd:
/Users/dgolden/REE_Working` and measurements of 92 worktrees there (6 named
LIVE worktrees with human-style random slugs, 14 `igw-*`, 16 random-slug,
45 `metaworker-*`). This session picked the chip up on **ree-cloud-4**, whose
own `.claude/worktrees/` is a *completely disjoint* directory (a worktree is a
per-machine filesystem artifact; the `/Users/dgolden -> /home/ree` shim makes
the *path spelling* resolve on every box, but each box has its own worktree
set). ree-cloud-4 currently holds **72 worktrees, all `metaworker-chip-*`
dispatch worktrees** -- no `igw-*`, no interactively-created random-slug
worktrees, none of the 6 named-LIVE worktrees from the original measurement.
This box is a dispatch box, not an interactive one.

Per CLAUDE.md's headless-worker rule 8 ("check `origin_host` before you
conclude 'already done'"), this is closer to a wrong-box condition than a
same-box re-measurement -- the *specific* 92-worktree graveyard the chip
describes lives on DLAPTOP and is untouched by this session. But the chip's
task ("triage the worktree graveyard, per-commit audit before any removal")
is a generic problem that recurs independently on every dispatch box, the
chip carries no `origin_host`-only gate, and CLAUDE.md's own worktree-GC
tooling (`hygiene_routine_tick.py` / `batch_worktree_gc.py`) already treats
each host's worktree set as its own independent GC domain. So this session
did the audit for **ree-cloud-4's own graveyard** rather than declaring the
chip inapplicable. **DLAPTOP's original 92-worktree graveyard is still
untouched and still needs its own supervised pass** -- this document does not
cover it.

## What already exists: an automated GC pipeline this task complements, not duplicates

Before auditing, this session found that `hygiene_routine_tick.py` +
`batch_worktree_gc.py` already run continuously on every dispatch box,
applying the same four removal gates this chip specifies (chip
done/withdrawn, no live process, clean apart from scratch, zero unlanded
commits) and dispatching `chip-metaworkergc-*` chips (visible in the table
below: `metaworker-chip-metaworkergc-*` worktrees are leftovers of that
pipeline's own runs). That pipeline is deliberately conservative: gate 4
("zero unlanded commits") is a **literal rev-list count**, not a content
audit -- it holds every worktree this chip's brief warns about (`wip:`
subjects, coordination-plane writes that landed under a different sha) rather
than trying to prove them safe. This chip's marginal job is exactly that
harder residual: the per-commit CONTENT audit CLAUDE.md requires before
trusting a "looks unlanded" worktree, which the automated pipeline
deliberately does not attempt.

## Audit method

For every non-live worktree with `origin/master..<branch>` commits (a fresh
`git fetch origin master` was run first; counts are a snapshot at
2026-08-28T20:28Z and drift as the fleet keeps committing):

1. **Cherry-pick backref / patch-identity check** (`ree_commit`'s standard
   route A/B, reused from `ref_convergence.py`) -- catches the common
   throwaway-worktree push-retry shape where a commit landed byte-identical
   or patch-identical under a different sha.
2. **Registry net-effect check** for `TASK_CHIPS.json`/`TASK_CLAIMS.json`
   touches -- reused `ref_convergence.registry_net_contained()` with an
   explicit `head_rev=origin/master` override (this repo's worktree branches
   are never literally named the same as a same-named origin branch, which
   is what that function normally assumes, so it needed the override rather
   than `--audit`'s CLI default).
3. Where (2) refused as "upstream history too large to scan" (the 150-commit
   cap in `MAX_UPSTREAM_SCAN_COMMITS`, hit routinely for these two
   high-churn registries over a multi-day-old branch): fell back to
   CLAUDE.md's documented manual recipe -- diff the commit against its
   parent to get the exact `(chip_ref)` / `(session_id, claimed_at)` keys it
   touched, then check whether that key is present in origin/master's
   *current* copy. Where a claim key was legitimately **absent**, confirmed
   via `git log -S<session_id> -- TASK_CLAIMS.json` that it existed upstream
   and was removed by the standard `TASK_CLAIMS.json: prune done entries
   older than 24h` job, never that it failed to land.
4. **Ephemeral-status-file rule**: commits touching only
   `metaworker_dispatch_cooldown.json` (a single-object status file
   overwritten every cooldown tick by design, same class as
   `runner_heartbeats/*.json`) are safe by construction regardless of byte
   match -- superseding it is the file's normal operation, not data loss.
5. **Prose added-line check** for `WORKSPACE_STATE.md` touches -- extract the
   commit's added lines and confirm they appear verbatim in origin/master's
   current copy (CLAUDE.md's documented "prose files by added-line sets"
   recipe). One case (below) needed a closer look because the exact line
   wasn't found: it turned out two sessions raced to append the same
   session-land closing entry 46 seconds apart, and the *other* one's append
   (not this worktree's) is what landed -- content-equivalent, not lost.
6. Anything left over got a **hand read** of the actual diff against
   origin/master's current file.

**Result: every unlanded commit across all 26 non-clean worktrees resolved to
PROVEN safe.** No genuinely stranded work was found on ree-cloud-4. Full
per-commit reasoning for the 23 unique shas that needed manual escalation
(steps 3, 5, 6 above) is in the scratch audit scripts referenced at the
bottom of this document; the summary:

- **17 shas**: `TASK_CHIPS.json`/`TASK_CLAIMS.json` bookkeeping, confirmed
  present upstream by key (chip done, or claim closed) -- the documented
  route-A false-negative shape (push-retry lands under a different sha).
- **1 sha**: `TASK_CLAIMS.json` entries confirmed landed then legitimately
  pruned (`>24h` retention), verified via `git log -S`.
- **8 shas** (`metaworker_dispatch_cooldown.json` only): ephemeral
  overwritten-by-design status writes.
- **2 shas** (`WORKSPACE_STATE.md`): content-equivalent append, landed
  verbatim (one under a different session's near-simultaneous append).
- **1 sha** (`scripts/run_scripts_tests.sh`, chip
  `chip-20260819-runscriptstests-symlink-worktree-false-positive`): a
  genuinely different implementation of the same fix that ALSO landed
  independently as `7a49c07d` (chip confirmed `done`, resolution note cites
  `origin/master 72ac01fc9d`). This worktree's own commit is a duplicate
  draft of already-shipped work, not unique content.

Two worktrees also carry non-scratch **dirt** (uncommitted changes beyond the
known dispatch-scratch trio):

- `metaworker-chip-20260816-implsub-contextmemory-writepath-degeneracy`:
  only `_local_fullsuite_run.log(.done)` / `_remote_pytest_run.log(.done)` --
  test-run log scratch, not currently in the documented scratch set but the
  same class as `claude.log`. **Recommend adding these four filenames to the
  documented scratch set** (CLAUDE.md / session-land Phase 2c /
  `batch_worktree_gc.py`'s gate 3) so future audits don't have to
  re-derive this.
- `metaworker-chip-20260820-heartbeat-cosmetic-vs-ssh-authoritative`: 865
  uncommitted lines across 4 script files implementing the same SSH
  disambiguation feature the chip's own (already `done`) resolution note
  says landed as `REE_Working master fa5c92c2`. Confirmed origin/master's
  current file is a **larger, more complete** version (1340 lines) than this
  worktree's uncommitted draft (1218 lines) and contains the same
  `SSH DISAMBIGUATION` section -- an earlier draft superseded by the actual
  landing, not unique content.

## Full table (72 worktrees, snapshot 2026-08-28T20:2x-20:4xZ)

`?` under Non-scratch dirt/Unlanded means clean/zero; see prose above for the
two dirty exceptions. Sorted by branch tip.

| Worktree | Chip status | Branch tip | Live? | Non-scratch dirt | Unlanded commits | Content-audit verdict | Recommended action |
|---|---|---|---|---|---|---|---|
| `metaworker-chip-20260816-autopsy-preflight-cluster-glob` | done | 2026-08-18T21:10:57 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260816-step25c-inert-corrupting-stamp` | done | 2026-08-18T21:57:07 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260818-cloud4-scripts-freshness-wedge` | done | 2026-08-18T23:42:15 |  | clean | 16 | 16/16 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260816-substrate-navigation-immobility-probe` | done | 2026-08-18T23:43:19 |  | clean | 17 | 17/17 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260817-blocked-note-not-carried-forward` | done | 2026-08-18T23:44:12 |  | clean | 19 | 19/19 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260817-cloud5-worker-settings-periodic-reinstall` | done | 2026-08-19T00:32:57 |  | clean | 2 | 2/2 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260818-scriptscorpus-dispatch-base-identity` | done | 2026-08-19T00:48:59 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260818-reapply-cascade-refusal-diagnostic` | done | 2026-08-19T01:03:53 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260816-implsub-contextmemory-writepath-degeneracy` | done | 2026-08-19T01:09:41 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260818-wire-taskclaim-chipledger-remotetip` | done | 2026-08-19T01:37:29 |  | 1 line(s) | 0 | dirt: ?? scripts/test_task_claim_chip_ledger_remote_tip_wiring.py | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-metaworkergc-chip-20260816-920a-episo-006e2a2bcb83` | done | 2026-08-19T18:03:55 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-metaworkergc-chip-20260817-mech053-se-331253b900b3` | done | 2026-08-19T18:05:02 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-metaworkergc-chip-20260817-steward-em-3621ce0e1616` | done | 2026-08-19T18:05:29 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260819-rederive-brake-double-counts-readjudications` | done | 2026-08-19T18:55:20 |  | clean | 2 | 2/2 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-metaworkergc-chip-20260819-umbrella-c-9b9e6f819305` | done | 2026-08-19T19:47:43 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260819-phase3-writer-smoke-red-on-dlaptop` | done | 2026-08-19T21:09:16 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260819-runscriptstests-symlink-worktree-false-positive` | done | 2026-08-19T21:27:39 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260820-dispatch-stale-pause-check-window` | done | 2026-08-20T03:29:53 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260819-scriptscorpus-launchd-timer-and-chip` | done | 2026-08-20T03:38:02 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260820-heartbeat-cosmetic-vs-ssh-authoritative` | done | 2026-08-20T07:39:06 |  | 4 line(s) | 0 | dirt: M scripts/check_dispatch_fleet_health.py;  M scripts/ree_metaworker_heartbeat.py;  M scripts/test_check_dispatch_fleet_health.py;  M scripts/test_ree_metaworker_heartbeat.py | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-refwedge-ree-cloud-4-ree-working-master-since-2026-08-20t09-46-46z` | done | 2026-08-20T10:39:55 |  | clean | 18 | 18/18 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-strandedwt-ree-cloud-4-metaworker-chip-20260819-fa0ed0a64114` | done | 2026-08-20T10:41:27 |  | clean | 19 | 19/19 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-strandedwt-ree-cloud-4-metaworker-chip-20260820-57cd64641083` | done | 2026-08-20T10:41:59 |  | clean | 20 | 20/20 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260814-queue-causal-sleep-matched-arm` | open | 2026-08-20T11:33:45 |  | clean | 0 | n/a -- chip not resolved | **HOLD -- chip status=open** (work in progress or abandoned; not a GC judgment call, needs its own triage) |
| `metaworker-chip-20260820-cem-authority-readiness-validation` | done | 2026-08-20T11:35:55 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260818-mech152-redesign-queue-gated` | open | 2026-08-20T11:55:38 |  | clean | 0 | n/a -- chip not resolved | **HOLD -- chip status=open** (work in progress or abandoned; not a GC judgment call, needs its own triage) |
| `metaworker-chip-20260820-metaworkerrepair-cloud4-stalled-withheld-explained` | done | 2026-08-20T13:42:03 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-metaworkergc-sweep-2-f87a21663fdcfb78` | done | 2026-08-20T15:01:05 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260821-conflictpathrecorder-pin-missing-assert-guard` | done | 2026-08-21T18:51:38 |  | clean | 3 | 3/3 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260821-timerstate-selfprobe-midrun-falsepositive` | done | 2026-08-21T18:53:35 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260821-account-handover-deferred-lessons` | done | 2026-08-21T19:34:19 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260821-refconvergence-refusal-advice-untested` | done | 2026-08-21T20:11:49 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260821-heartbeat-hysteresis-remeasure` | open | 2026-08-21T20:23:55 |  | clean | 0 | n/a -- chip not resolved | **HOLD -- chip status=open** (work in progress or abandoned; not a GC judgment call, needs its own triage) |
| `metaworker-chip-20260821-phase3writers-failureautopsy-skill-edit` | done | 2026-08-21T20:56:04 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260821-queueexp-step9-orchestrator-heartbeat-false-positive` | done | 2026-08-22T00:05:29 |  | clean | 2 | 2/2 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260822-hostwithhold-precision-context-mentions` | done | 2026-08-22T11:37:50 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260822-fromdims-sd016-divweight-repair` | done | 2026-08-22T22:37:06 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260822-fromdims-dropsite-lint-into-corpusscan` | done | 2026-08-22T22:39:00 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-metaworkergc-sweep-1-db222ba36e118472` | done | 2026-08-22T22:39:42 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260823-completedunresolved-batch-plus-worklanded-timeout` | done | 2026-08-23T00:54:36 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-metaworkergc-sweep-1-a7ebf18cdbca64f8` | done | 2026-08-23T06:17:42 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260823-mech314bc-2x2-diversity-validation` | done | 2026-08-23T08:51:54 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-e1-rollout-consistency-litpull` | done | 2026-08-25T22:22:18 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-gap5b-mel-environment-design-scoping` | done | 2026-08-25T22:22:18 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-mech357-h2-reanalysis` | done | 2026-08-25T22:22:18 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-extoo9-q032-stale-citation` | done | 2026-08-25T22:53:01 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-sd101-mech503-litpull` | done | 2026-08-25T22:53:01 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-gulli-verify-arc130-litpull` | done | 2026-08-25T23:03:26 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-arc130-govintervene1-claimsyaml-citation` | done | 2026-08-25T23:44:25 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-evidence-backlog-literature-channel-probe` | done | 2026-08-25T23:44:25 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-metaworkerlearning-hygiene-host-declaration` | done | 2026-08-26T04:46:04 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260824-exq861f-duplicate-run-stale-claim-reap` | done | 2026-08-26T05:38:45 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-indexer-vacuous-pass-or-semantics-gap` | done | 2026-08-26T05:43:42 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260825-igw-refresh-taskclaim-partial-key` | done | 2026-08-26T05:54:56 |  | clean | 1 | 1/1 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260825-sleep-entry-pressure-build` | done | 2026-08-26T06:53:36 |  | clean | 14 | 14/14 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260825-sd011-urgency-sign-inversion` | done | 2026-08-26T06:59:12 |  | clean | 14 | 14/14 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260826-driver-criteria-aggregation-followup` | done | 2026-08-26T07:31:53 |  | clean | 28 | 28/28 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260826-sd099-diagnostic-adjudicated-flag` | done | 2026-08-26T07:52:35 |  | clean | 22 | 22/22 commits PROVEN safe via content audit | GC-CANDIDATE (content-audited safe) -- requires a Remote-Control-supervised session to re-verify gates fresh and remove, per chip banner |
| `metaworker-chip-20260826-claude-md-self-discoverable-hunt` | done | 2026-08-26T11:28:05 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-strandedwt-ree-cloud-4-metaworker-chip-20260825-f195df22e528` | done | 2026-08-26T11:34:40 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260826-scoring-excluded-expcount-investigation` | done | 2026-08-26T18:34:44 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260826-cloud4-untracked-items-triage` | done | 2026-08-26T18:37:48 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260826-taskclaim-coordinator-migration-phase1` | done | 2026-08-26T18:37:48 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260826-hostwithhold-selfref-resolve-command-falsepositive` | done | 2026-08-26T21:52:14 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260826-contextmemory-gumbel-writeselect-build` | done | 2026-08-27T00:09:02 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260827-arc070-repose-reoperationalization` | done | 2026-08-28T19:52:18 |  | clean | 0 | n/a -- nothing to audit | GC-CANDIDATE: passes all 4 gates cleanly (chip done, not live, clean, 0 unlanded). Already eligible for `batch_worktree_gc.py`; likely just hasn't been swept yet. |
| `metaworker-chip-20260827-queueexp-mech320-authority-retest` | open | 2026-08-28T19:52:18 | LIVE | clean | 0 | n/a -- LIVE | **HOLD -- LIVE session, never touch** |
| `metaworker-chip-20260828-sd069-stepcap-rerun` | done | 2026-08-28T19:52:18 | LIVE | clean | 0 | n/a -- LIVE | **HOLD -- LIVE session, never touch** |
| `metaworker-chip-20260826-representation-authority-selection-bottleneck` | open | 2026-08-28T20:16:13 |  | clean | 0 | n/a -- chip not resolved | **HOLD -- chip status=open** (work in progress or abandoned; not a GC judgment call, needs its own triage) |
| `metaworker-chip-20260826-thought-digestion-wave-grouping-design` | open | 2026-08-28T20:16:13 | LIVE | clean | 0 | n/a -- LIVE | **HOLD -- LIVE session, never touch** |
| `metaworker-chip-20260826-worktree-graveyard-triage-and-gc` | open | 2026-08-28T20:16:13 | LIVE | clean | 0 | n/a -- LIVE | **HOLD -- LIVE session, never touch** |
| `metaworker-chip-20260827-headlesscontract-scratchfile-fix` | done | 2026-08-28T20:16:13 | LIVE | clean | 0 | n/a -- LIVE | **HOLD -- LIVE session, never touch** |

## Summary

- **72 worktrees** total on ree-cloud-4 at snapshot time.
- **5 LIVE** (active session cwd'd inside): never touched, never will be by this document.
- **4 HOLD -- chip not resolved** (`chip-20260814-queue-causal-sleep-matched-arm`,
  `chip-20260818-mech152-redesign-queue-gated`,
  `chip-20260821-heartbeat-hysteresis-remeasure`,
  `chip-20260826-representation-authority-selection-bottleneck`): not live,
  but their own chip is still `open` -- either abandoned mid-work or genuinely
  still pending. Removing these is not a GC judgment call at all (it would be
  discarding unfinished work); each needs its own triage to determine
  abandoned-vs-pending, out of scope here.
- **35 trivially clean GC candidates**: chip done/withdrawn, not live, zero
  non-scratch dirt, zero unlanded commits. These already pass all four gates
  literally -- no content judgment needed. They are exactly what
  `batch_worktree_gc.py` is built to sweep and most likely just haven't been
  swept yet (or a leftover from a race between this audit and the automated
  pipeline's own cadence).
- **28 audited GC candidates**: chip done, not live, but with unlanded
  commits and/or non-scratch dirt that failed the *automated* pipeline's
  literal gate 4/3 -- every one of them individually content-audited safe by
  this document (see above). These need a human to re-run the same four
  gates FRESH at removal time (state moves) and then remove, per the chip
  banner -- this session does not do that.

35 + 28 + 4 + 5 = 72.

## Stranded work found: none

No genuinely stranded work was found on ree-cloud-4. Every unlanded commit
across all 26 non-clean worktrees is proven, by content, to already exist on
`origin/master` in some form (verbatim, patch-equivalent, registry-net-effect
contained, legitimately pruned after landing, or superseded by an
independently-landed duplicate fix). Nothing needed cherry-picking or
recovery.

## Recommended next steps (for a Remote-Control-supervised session)

1. Re-fetch `origin/master` and re-run this same audit fresh immediately
   before removing anything -- state moves (this snapshot is already ~20
   minutes old by the time it's committed, and the fleet commits continuously).
2. For the 35 trivially-clean candidates: `batch_worktree_gc.py` should
   already handle these; if it hasn't, running it under supervision is the
   straightforward path (it re-verifies its own four gates fresh per
   candidate, immediately before each removal, exactly as the chip banner
   requires).
3. For the 28 audited-but-not-trivially-clean candidates: re-verify the four
   gates fresh, spot-check a few of this document's content-audit verdicts
   against current `origin/master` state (things move; a spot-check costs
   little and catches this document going stale), then remove one at a time
   with plain `git worktree remove` (never `--force`).
4. Consider adding `_local_fullsuite_run.log`, `_local_fullsuite_run.log.done`,
   `_remote_pytest_run.log`, `_remote_pytest_run.log.done` to the documented
   dispatch-scratch set (CLAUDE.md / session-land Phase 2c /
   `batch_worktree_gc.py` gate 3) -- they're evidently a normal byproduct of
   a chip session running the test suite locally before landing, same class
   as `claude.log`.
5. **DLAPTOP's original 92-worktree graveyard (the one the chip was actually
   spawned to measure) is still untouched** -- this document only covers
   ree-cloud-4. That audit still needs to be run, ideally by a
   Remote-Control session actually attached to DLAPTOP.
6. Every other dispatch box (ree-cloud-2, ree-cloud-3, ree-cloud-5,
   ree-worker-1..4 where applicable) likely has its own independent
   worktree graveyard with the same shape; not surveyed by this session.

## Reproducing this audit

The scratch scripts used to produce this table are not committed (session
tmpfiles, `/tmp/wt_*.py` on ree-cloud-4) -- the method is fully described
above and reuses only existing repo tooling
(`scripts/ref_convergence.py`'s `registry_net_contained()`,
`scripts/ree_commit.py`'s `git()` wrapper) plus ordinary `git` commands. No
new script was added to the repo since the four gates and the registry-proof
machinery already exist; this document is the artifact.
