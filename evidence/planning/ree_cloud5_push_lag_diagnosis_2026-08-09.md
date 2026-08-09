# ree-cloud-5 shared-checkout push lag — diagnosis

**Date:** 2026-08-09
**Chip:** `chip-20260809-cloud5-reeassembly-push-lag`
**Box:** `ree-cloud-5`, shared checkout `/home/ree/REE_Working/REE_assembly`
**Status:** DIAGNOSIS ONLY. Nothing was rebased, reset, ref-moved, or discarded on the
shared checkout. No fix applied — see "Recommended fix" for the follow-on.

## Verdict, up front

The chip asked whether this is **(a) benign by design** or **(b) a real gap where session
work can sit unpushed indefinitely**. The answer is **both, split cleanly by repo**:

- **`REE_assembly` — (a) benign for durability.** No session work is or was stranded.
  Every one of the 9 real-work commits in the ahead-set has a **patch-equivalent already on
  `origin/master`**, and every real-work *file path* is **byte-identical** to origin. The
  local copies are orphan duplicates left behind by the sanctioned
  cherry-pick-in-a-throwaway-worktree landing pattern, which changes the SHA by
  construction. The remaining 18 local-only commits are 15 derived heartbeat ticks plus a
  raise/raise/drop governance-flag triple that nets to zero.
- **`REE_Working` (umbrella) — (b)-shaped, and this is the part worth acting on.** The
  umbrella's coordination ledger (`TASK_CHIPS.json`, `TASK_CLAIMS.json`) is *not* derived
  and *not* landed by any throwaway-worktree pattern. It currently has local-only commits,
  and the dispatcher's own `git pull --ff-only` is failing as a direct result.

**The ahead-count is NOT simply "expected on this box."** It is a stuck state with a
specific, removable cause, and it self-clears whenever that cause is absent.

## Measured state (2026-08-09T09:2x–09:3xZ)

```
REE_assembly   master...origin/master [ahead 27, behind 25]   5 dirty (all ` M`, tracked)
REE_Working    master...origin/master [ahead  5, behind 15]
```

`git cherry -v origin/master master` on `REE_assembly` — `-` = equivalent change already
on origin, `+` = genuinely local-only:

| bucket | count | disposition |
|---|---|---|
| `-` real session work (lit-pull ×3, failure-autopsy 9b, GOV-CAT-1 ×2, indexer tests, governance-flag ×2) | 9 | **already on origin** under different SHAs |
| `+` `phase3-heartbeats: orchestrator tick ree-cloud-5` | 15 | derived; regenerated every tick |
| `+` governance-flag raise/raise/drop triple | 3 | nets to zero; `governance_flags.v1.json` byte-matches origin |

Confirmed byte-identical to `origin/master`: `scripts/check_epistemic_category_completeness.py`,
`scripts/governance.sh`, `evidence/planning/epistemic_category_enum_backlog.v1.json`,
`evidence/planning/governance_flags.v1.json`, `evidence/literature/INDEX.md`.

The only content local-has-and-origin-lacks outside heartbeats is **7 lines**, and all 7 are
*stale older versions* of lines origin has since changed (e.g. an un-bumped
`<!-- FISHTANK_VIZ_VERSION: 2026-06-10.2 -->`). That is local being **behind**, not local
holding unique work.

## Root cause

A single deterministic mechanism, with direct log evidence:

1. `ree_metaworker_heartbeat.py` commits via `ree_commit.py --push`.
2. The push is rejected `non-fast-forward` — because the checkout is **behind** origin.
3. `retry_push_after_rebase()` (`scripts/ree_metaworker_heartbeat.py:109`) runs
   `git pull --rebase origin master` to clear the behind-ness.
4. **That pull fails immediately** — `error: cannot pull with rebase: You have unstaged
   changes.` — because the shared checkout carries other work's tracked modifications.
5. It aborts and gives up on attempt 1 (correctly: it refuses to force anything).
6. The local commit stays. The next tick stacks another on top. The box never becomes
   un-behind, so **every subsequent push from that checkout is rejected too** — including
   real session work.

The retry is not broken; its precondition is simply never met. Over the whole dispatch log:

```
182 give-ups, 100% with the identical cause "cannot pull with rebase: You have unstaged changes"
  0 ever reached attempt 2/3 or 3/3
 85 successes — all on ticks where the tree happened to be clean
```

Daily split shows a sharp regime change:

| date | success | fail | success rate |
|---|---|---|---|
| 2026-08-03 | 7 | 0 | 100% |
| 2026-08-04 | 9 | 0 | 100% |
| 2026-08-05 | 12 | 0 | 100% |
| 2026-08-06 | 9 | 0 | 100% |
| 2026-08-07 | 24 | 1 | 96% |
| **2026-08-08** | **14** | **166** | **8%** |
| 2026-08-09 | 10 | 16 | 38% |

### What is actually pinning it right now

Five tracked ` M` files, all stuck since **07:12:12Z**:

```
evidence/experiments/v3_exq_{241a,241b,614,673,707c}_*/INDEX.md
```

These are **uncommitted `build_experiment_indexes.py` regen output** — derived, not session
work. The change is a run-timestamp normalisation (`20260408T190019Z` ->
`2026-04-08T19:00:19Z`) that is **already committed on origin for the rest of the corpus**
(e.g. `v3_exq_904_*/INDEX.md` carries the ISO form). So these 5 are the residue of a
normalisation applied everywhere else and never landed here.

**Untracked files do not cause this** — `git pull --rebase` only refuses on tracked
unstaged changes. That is why the dispatcher's long-running `dirty=1 ahead=0` baseline
converged fine while `dirty=5` (tracked) does not.

### The correlation, from the dispatcher's own log

```
dirty=1     ahead=0                 <- steady state, converges
dirty=1219  ahead=1  -> 98          <- 2026-08-08 governance-regen episode, monotonic climb
dirty=1     ahead=0                 <- dirt cleared, drained to zero on its own
dirty=5     ahead=27 behind=25      <- now
```

Sustained *tracked* dirt produces monotonic ahead-growth; a clean tree drains it to 0
without intervention. The mechanism is recurrent, not a one-off — it previously reached
**ahead=98**.

## Two consequences beyond the lag itself

1. **The dispatcher's health check reports `OK` throughout.**
   `audit_coordination_plane_dirt.py` flags only above a `DIRTY_COUNT_FLOOR = 150` (tuned to
   detect the ~1050–1190-file governance-regen shape). Every cycle logged
   `OK REE_assembly 5 dirty file(s), below the 150-file governance-regen floor (ahead N, behind M)`
   while `N` climbed 15 -> 27. **The threshold that matters for convergence is 1 tracked
   file, not 150.** The audit already computes and prints `ahead`/`behind` — it just does
   not use them in its verdict.

2. **The dispatcher is running stale code.** `ree_metaworker_dispatch.sh` starts each cycle
   with `git pull --ff-only origin master` on the umbrella, which now refuses because the
   umbrella is ahead. Logged **868** times, and continuously in recent cycles:
   ```
   [2026-08-09T09:19:10Z] autosync: FAILED (git pull --ff-only) -- continuing this cycle on existing code
   ```
   This re-arms precisely the failure the autosync was built to prevent — the script's own
   comment cites "47 cycles (~4h) on a since-fixed heartbeat-commit bug before anyone
   noticed". A push-lag on the umbrella therefore **blocks the box from picking up fixes**,
   including a fix to this very problem.

## It also manufactures false signals

This is the confirmed cause of the same morning's `substrate_queue` write-back drift false
positive (`chip-20260809-sqdrift-stale-checkout-fp`): a detector read a working-tree file 24
commits behind and reported drift on an entry that had been correct upstream for 35 minutes,
costing a full headless-worker dispatch. That detector has since been fixed to corroborate
against the remote-tracking ref (`REE_Working` `31461e9b33`). **Any other tool on this box
that reads a working-tree file and reasons about freshness has the same exposure and has not
been audited.**

## Recommended fix (NOT applied here)

Ordered by value. Note the chip's own steer is right: this is **not** a change to how
sessions land.

1. **Do not use `--autostash`.** It would "fix" step 4 and is explicitly rejected — CLAUDE.md
   documents autostash silently sweeping live sessions' uncommitted work into orphaned
   stashes. The whole point of the current code backing off is that it refuses to touch
   other work.
2. **Push via a throwaway worktree instead of rebasing the shared checkout.** The heartbeat
   commit touches only `runner_heartbeats/<machine>.json`, which no other writer touches.
   Cherry-picking it onto `origin/master` in a detached worktree and pushing from there is
   the pattern CLAUDE.md already sanctions for exactly this situation (pushing around a
   dirty shared checkout), is clean by construction, and cannot be blocked by shared-tree
   dirt. The shared checkout stays ahead with orphan copies — which is already the norm and
   is provably harmless (see Verdict).
3. **Make the health check fire on the condition that actually matters.** Have
   `audit_coordination_plane_dirt.py` flag `ahead > 0 AND tracked-dirty > 0` (or ahead
   growing across N cycles) as a distinct verdict from the 150-file regen shape. It already
   has both numbers in hand. Today the box can sit non-convergent for 38+ hours under a
   green light.
4. **Land the 5 stuck `INDEX.md` files.** Deliberately left alone here: they are another
   process's regen leftovers, and this codebase's standing posture is detect-and-report,
   never force through. But they are derived and reproducible, and landing (or discarding)
   them returns `REE_assembly` to the umbrella's self-draining behaviour immediately.

## Method note

Everything above is read-only measurement on the live box: `git cherry` for patch-id
equivalence, two-dot/three-dot diffs for content, `git show origin/master:<path>` for
byte-comparison, and `~/ree_metaworker_dispatch.log` for the failure counts. `git pull
--rebase` was deliberately **not** run to test the hypothesis — on the off-chance the tree
were clean at that instant it would have rebased the shared checkout, which the chip
forbids.
