# Umbrella `REE_Working` stash triage -- `7538603043` (2026-08-25)

**Repo:** `/home/ree/REE_Working` (umbrella, ree-cloud-5)
**Entry:** `stash@{0}` -> `7538603043ed29abe95a91f32e349aceb4879040`, taken 2026-08-25 19:55 (local)
**Stash message:** `On master: orchestrator-cleared-2026-08-25: TASK_CHIPS mods + untracked dispatcher_control.json, all content confirmed already on origin`
**Archive tag:** `stash-archive/20260825-75386030` (local-only, per the established convention)
**Triaged:** 2026-08-25T20:39:14Z, session `chip-fleetstash-ree-cloud-5-ree-working-7538603043` (chip `chip-fleetstash-ree-cloud-5-ree-working-7538603043`)
**Trunk at triage time:** `origin/master` (fetched 2026-08-25T20:34Z)

---

## Verdict: **ALREADY-LANDED (superseded / regenerable-lease)** -- nothing orphaned, nothing to restore

`audit_stashes.py` graded this **HAND-AUTHORED CONTENT** because both paths (`TASK_CHIPS.json`,
`dispatcher_control.json`) fall outside its derive-only allowlist. Per the precedent in
`umbrella_stash_triage_20260812_93c95300.md`, that grade is a pointer for a human to READ the
entry, not an automatic finding of loss. Both paths have now been read and content-verified
against `origin/master` individually.

**The stash's own message already stated the correct conclusion** ("all content confirmed
already on origin") -- this triage independently re-derives and confirms it rather than taking
the message on trust, per CLAUDE.md's warning against reasoning from shape/self-report alone.

---

## Per-path grading

### 1. `TASK_CHIPS.json` -- 4 hunks, +38/-12

The stash's own diff (`git diff 'stash@{0}^' 'stash@{0}' -- TASK_CHIPS.json`) touches exactly
four chip records:

| # | task_id / chip_ref | Change | Verified against `origin/master` today |
|---|---|---|---|
| 1 | `task_4425e586` / `chip-20260823-invalid-epistemic-category-mech321` | `claimed_by` DLAPTOP spawn_task -> `a7772dd9-dc40-4426-819d-abdfaac1af1a` @ ree-cloud-5 | **PROVEN** -- byte-identical `claimed_by`/`claimed_at`/`claimed_host` on origin now |
| 2 | (unnamed in narrow diff context; identified via wide-context diff) `chip-20260823-cloud4-runner-failsafe` | `claimed_by` null -> `e852c86d-4251-4ee2-99de-db4a7c24001d` @ ree-cloud-5 | **SUPERSEDED** -- chip has since resolved: `status: "done"`, `claimed_by: null` on origin. The claim captured here was an intermediate in-progress state of the *same* chip's lifecycle; the chip's terminal state (completed, unclaimed) is what's on trunk now. Nothing lost -- the work this claim represented was finished. |
| 3 | `task_637350c7` / `chip-20260824-mech142-ach-gating-falsifier-scope` | `claimed_by` DLAPTOP spawn_task -> `3bf1a68f-690a-48d9-9694-69ecb45e12f3` @ ree-cloud-5 | **PROVEN** -- byte-identical `claimed_by`/`claimed_at`/`claimed_host` on origin now |
| 4 | `task_4c6627a7` / `chip-20260825-gap5b-mel-environment-design-scoping` (new record, +26 lines) | New chip appended | **PROVEN** -- full record (task_id, chip_ref, title, tldr, prompt including the `[chip_ref: ...]` marker, cwd, origin_host, spawned_at, status, claimed_by/at/host) byte-identical on origin now |

3 of 4 changes are byte-exact verbatim present on `origin/master` right now (stronger than
"superseded" -- this is blob/hunk-level containment, test 2/4 strength in the reference method).
The 4th is a claim-state snapshot of a chip that has since completed and cleared its own claim
on trunk -- the same object, advanced forward through its own normal lifecycle, not diverged
from it. This is not a same-shape-therefore-safe assumption (CLAUDE.md's warning about
TASK_CHIPS/TASK_CLAIMS bookkeeping): every one of the four changed records was individually
read and its current origin state individually confirmed, per commit content, not per file
shape.

### 2. `dispatcher_control.json` -- untracked at stash time, 1 file, whole-file lease snapshot

At stash time (19:55) this file was **untracked** -- it did not yet exist in git. Since then:

- `d41798bd` "dispatcher_control.json: add to git tracking -- was never committed, so
  Orchestrator lease grants never reached any Dispatcher box" added it to tracking.
- `6c055953` and `b8fcd552` "dispatcher_control.json: renew lease" landed two subsequent
  renewals, both from the same requester (`insights-7fd98a`, the Orchestrator session) as the
  stash's own snapshot.

The stash's copy (`expires_at: 2026-08-25T21:34:28Z`, `requested_at: 19:34:28Z`) is a strict
temporal predecessor of the tracked, current lease
(`expires_at: 2026-08-25T22:20:12Z`, `requested_at: 20:20:12Z`) -- same dispatcher
(`ree-cloud-5`), same requester, same shape, later renewal. This is a live lease file the
Orchestrator overwrites every cycle by design (see the file's own `_comment` block); the
stash holds a stale snapshot of mutable coordination state that has been legitimately
superseded by later renewals, exactly analogous to the `runner_heartbeats/*` /
`experiment_queue.json` "DB-authoritative snapshot, superseded by re-run" reasoning used
throughout `ree_v3_orphaned_autostash_triage.md`.

---

## Why this was not an `autostash`

The stash message (`On master: orchestrator-cleared-2026-08-25: ...`) indicates this was
**hand-taken**, not the runner's silent `autostash` defect the sibling triage doc's coverage
gap describes. The message's own wording ("orchestrator-cleared") and content (chip-claim
reassignments consistent with the Orchestrator's dispatch bookkeeping, plus its own lease file)
both point to the same session (`insights-7fd98a`) having parked its working tree deliberately
mid-cycle, then having its work land through normal commits shortly after -- which is exactly
what the per-path grading above confirms.

---

## Actions taken

1. Archive-tagged `stash-archive/20260825-75386030` -> `7538603043ed29abe95a91f32e349aceb4879040`,
   and verified both paths (`TASK_CHIPS.json`, and `dispatcher_control.json` via the tag's
   untracked-files parent, `^3`) resolve through the tag **before** touching the entry.
2. Re-verified `stash@{0}` still resolved to `7538603043` immediately before dropping.
3. Dropped `stash@{0}`.
4. Re-verified after the drop that both paths still resolve through the tag.

`git stash list` in `REE_Working` on ree-cloud-5 is now empty.

**Residual, stated rather than papered over:** the archive tag is **local-only** by the
established convention (see `ree_v3_orphaned_autostash_triage.md` "Why LOCAL-ONLY"), so the
sole surviving copy of this exact stash commit object lives in this box's (`ree-cloud-5`)
local `.git`. The underlying *content*, per the grading above, is independently present on
`origin/master` regardless -- the tag is a redundant packaging, not the only copy of any work,
consistent with reason 1 in that section.

## Coverage note

`audit_stashes.py`'s grade is deliberately conservative and cannot be read as a finding on its
own -- a HAND-AUTHORED grade means "no automated test applies, a human (or an equivalent,
fully-worked content audit) must read it." In this case a content audit of all five changed
records/fields across both paths found every one contained, superseded by the same entity's
own forward progress, or superseded by a later legitimate renewal from the same source. The
grade did its job: it stopped an automated drop of a coordination-plane bookkeeping stash
without individual verification, and that verification, once done, confirmed the stash's own
self-reported conclusion.
