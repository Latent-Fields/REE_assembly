# Chip status regression (git `70f6849fab`) -- root cause, repair record, residual decisions

**Written:** 2026-09-19T10:17:12Z by session `eloquent-jepsen-5f6242`
(chip `chip-20260918-chip-status-regression-restore-and-rootcause`).
**Status:** root cause CONFIRMED on the hub; data REPAIRED and verified against the hub DB; recurrence path
CLOSED in code (ree-v3 `0ddac64` on origin/main, see "Fix"). Two items are left as user decisions (section 6).

Supersedes the mechanism paragraph of `metaworker_learning_outstanding_classes_staged_20260918.md` section P3,
which named the right code branch "from code, NOT confirmed on the hub" and listed the stale source only as a
candidate. That session (`ml-build-a-20260918`) landed the terminal/archived guard (ree-v3 `7f51dff`) and
re-resolved the open rows at 2026-09-18T18:40Z. This document adds the hub evidence, the full blast radius
(wider than the 22 rows), the remaining repairs, and the fix for the source itself.

## 1. Mechanism (confirmed)

The writer was **not** the hub materializer, a degraded client git push, a DB import, or the status-plane
projector. It was the **PHASE-1 shadow-sync timer** (`ree-task-claim-chip-shadow-sync.timer`, every 10 min),
which was left running after the 2026-08-28 cutover and still upserts into the now-authoritative tables.

Hub journal (`journalctl -u ree-task-claim-chip-shadow-sync.service`, UTC):

```
2026-09-18T12:52:35 WARN git fetch/resolve failed for repo_path='/home/ree/REE_Working_shadow_mirror_readonly'
                    ref='origin/master': TimeoutExpired([... 'fetch', '--quiet', 'origin'], 30)
2026-09-18T12:52:35 ref=origin/master-stale-local claims: git=140 db=1951 new=0 updated=133 orphan=12
                    | chips: git=1707 db=3875 new=0 updated=1183 orphan=2169 | diverged=1
```

Chain of events:

1. One `git fetch` hit its 30 s timeout (the registry writer's own fetch timed out two minutes later at
   12:54:36Z, so this was a network/GitHub blip, not a fault in either service).
2. `load_source_documents()` fell back to `_load_local_json()`: the **working-tree** copy in the mirror clone.
3. That module only ever runs `fetch` / `rev-parse` / `show` -- it never checks anything out -- so the mirror's
   working tree is frozen at the commit it was provisioned from: `HEAD 6099facd 2026-08-26T20:23:02Z`,
   file mtime `Aug 26 20:24`, `master...origin/master [behind 6923]`, 1707 chips.
4. `reconcile_chips()` upserted those 1707 three-week-old rows. For any row whose DB entry equalled its last
   render base (the steady state), `upsert_chip` took Case B, "only git moved -> adopt git", which had no
   guard. 1183 rows were overwritten.
5. The next healthy registry-writer tick (12:55:44Z) rendered the damaged DB faithfully as `70f6849fab`.

The Healer's correlation ("exactly the oldest resolved rows", first resolved_at 2026-08-26T20:26:57Z) is
explained exactly: the 22 rows are the chips that were still open when the mirror was cloned at 20:23Z.

It is the only `stale-local` tick in the hub's retained journal. Can it recur: **yes, on any fetch failure**,
until the fix below is on the hub's checkout (the service is a oneshot, so it loads new code on its next tick;
no restart is involved).

## 2. Blast radius (pre-image: hub backup `coordinator-5.db`, 2026-09-18T03:41Z, vs live DB)

- `task_claims`: 0 of the snapshot's 140 keys differ pre -> now. No claim damage.
- `chip_ledger`: 1183 rows rewritten.
  - 1178 lost `archived` and regained inline fat fields. Self-healed: the 2026-09-19 04:30 archive run
    re-stripped 1377 rows (content is intact in `chip_archive/`).
  - **22** went done/withdrawn -> open (the reported set).
  - **6 more rows, not previously reported**, regressed without a status change:
    - `chip-20260814-queue-causal-sleep-matched-arm` and `chip-20260818-mech152-redesign-queue-gated`
      (both OPEN): prompt reverted, **dropping the Orchestrator's `PRE-FLIGHT VERDICT: RED` prefix** that
      keeps a queue session from being spent on an experiment gated by a corrupting substrate defect; claim
      notes reverted; the first also regained a phantom 2026-08-26 claim.
    - `chip-20260826-representation-authority-selection-bottleneck` and
      `chip-20260826-thought-digestion-wave-grouping-design` (both OPEN): regained phantom 2026-08-26 claims
      (`session-6d235fb7`, `session-ee03a1d4`), which makes an open chip undispatchable.
    - `chip-20260819-cloud5-hcloud-readonly-token` and `chip-20260826-ingress-dispatch-architecture-decision`
      (done): lost their `handoff_pending` trackers (two user-owed manual steps dropped off the handoff audit).

## 3. Repair record (ledger verbs only; every write verified by reading the hub back)

| What | By | How |
|---|---|---|
| 17 of 22 re-resolved | `ml-build-a-20260918`, 2026-09-18T18:40Z | `chip_ledger.py resolve` |
| 5 of 22 re-resolved independently | proposal_tick / hygiene auto-resolve / metaworker-learning | their own paths |
| 20 rows: true original resolution facts | this session | `amend-note` (the 18:40Z restore notes recorded a truncated `orig resolved_at=05Z` and dropped resolved_by / claim fields; the 4270-char note of `chip-20260826-worktree-graveyard-triage-and-gc` had been lost outright and is back verbatim) |
| 2 prompts (RED verdicts) | this session | `amend-prompt`, pre-image verbatim |
| 3 phantom claims + 4 claim notes | this session | `unclaim --note <pre-image claim_note>` (mech152: momentary claim + unclaim, the only verb route to a claim note on an unclaimed chip) |
| 2 `handoff_pending` trackers | this session | `declare-handoff --since <original>` (no coordinator mirror: degraded git path; as-pushed commits `52d53f915`, `cdab7aed3` each change exactly one field of one row) |

Not restorable through any verb, and left as-is: `resolved_at` on the 22 rows now reads 2026-09-18 (the
original is in the amended note); `prompt_history` on the two re-prompted chips lost its intermediate
2026-08-23..09-14 amendment records (one extra "stale prompt" entry instead); `declared_by` on the two handoff
trackers is now this session. Two rows ended in a different terminal status than before, each by a legitimate
later actor, left alone: `chip-20260826-refwedge-class-persists-post-fix` (withdrawn -> done) and
`chip-proposal-exp-0590` (done -> withdrawn by proposal_tick, "gated").

No chip was skipped for being live-claimed: none of the 28 rows carried a claim newer than the incident.

## 4. Fix (ree-v3 `coordinator/`)

1. `task_claim_chip_shadow_sync.py`: **the working-tree fallback is removed.** A failed fetch/resolve now
   skips the tick (exit 1, nothing ingested, no drift row). A skipped tick costs nothing: the registry writer
   ingests origin every 2 min on its own fetch. This is the root-cause fix; `7f51dff` is not sufficient on its
   own, because the 6 extra rows in section 2 carry no terminal or archived signature a row-level guard can
   test. The new test `test_fetch_failure_never_ingests_the_frozen_working_tree` reproduces that shape and
   fails against `7f51dff`.
2. `db.py` `upsert_task_claim`: the done -> not-done guard is hoisted above the adopt-git branch, the mirror of
   `7f51dff`'s chip change (proposed in the 2026-09-18 design doc, not built then). Claims escaped damage this
   time; a reopened claim would re-arm arbitration against the current legitimate holder. Test `t3c` fails on
   the old code.

Scope note: the claim guard blocks a done -> active transition arriving by git. No verb produces one (a re-open
is a new `(session_id, claimed_at)` row), so nothing legitimate is newly refused. The chip-side equivalent in
`7f51dff` does newly refuse a git-path `resolve --status open` (e.g. `0b395755f`); that trade-off was recorded
in the 2026-09-18 design doc and is unchanged here.

## 5. Why the guards are not the whole answer

Case B in `upsert_chip` / `upsert_task_claim` infers "git is NEWER than the DB" from "git differs from the
render base and the DB equals it". That inference is only sound if the git content read is at least as new as
the base. A working-tree file three weeks old violates it grossly; an `origin/master` sha fetched a few seconds
before the registry writer pushes a newer render violates it slightly. The second is a narrow race between the
two timers (shadow-sync fetches outside its `BEGIN IMMEDIATE`), it would revert only what changed in that
window, and no occurrence has been observed -- it is stated here so the next statusregress investigation does
not have to rediscover it.

## 6. Decisions left for the user

1. **Retire `ree-task-claim-chip-shadow-sync.timer` on the hub?** `complicated (buildable)`. PHASE-1 closed
   2026-09-06; the registry writer ingests the same origin content every 2 min, so the shadow tick's ingest is
   redundant, and it is the only remaining source of the section-5 race. Its one unique product is the drift
   log (`/shadow/status` drift summary). Recommended: disable the timer, or keep it but make the tick
   log-only (compare, do not upsert). A hub systemd change is not a session's to make.
2. **The frozen mirror working tree** (`/home/ree/REE_Working_shadow_mirror_readonly`, 9 MB of 2026-08-26
   registry files) is now unread by any code path. Harmless once the fix is pulled; deleting the two files
   would make the old failure impossible even under a rollback.

## 7. Evidence index

- Hub journal lines quoted in section 1; `systemctl cat ree-task-claim-chip-shadow-sync.service`
  (`TASK_CLAIM_CHIP_REPO_PATH=/home/ree/REE_Working_shadow_mirror_readonly`).
- Pre-image: `/home/ree/backups/coordinator-5.db` (2026-09-18T03:41:36Z, integrity ok). Rotates out ~2026-09-25;
  the row-level pre-images that mattered are now in the amended notes and in `git show 70f6849fab^:TASK_CHIPS.json`.
- Git shape of `70f6849fab`: 1183 rows changed, 22 terminal -> open, 1178 `archived` dropped, 1 row added;
  hub-authored, empty body (an ordinary materializer render of an already-damaged DB).
