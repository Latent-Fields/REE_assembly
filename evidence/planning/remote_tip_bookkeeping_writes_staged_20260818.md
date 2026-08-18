**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any registry). The CODE it describes (`scripts/ree_commit.py`'s new `--to-remote-tip` mode) has been landed on `master` -- it is fully opt-in and inert unless a caller explicitly passes the new flag, so no existing writer's behavior changed. What is under review here is the SEPARATE, larger decision of whether/when to wire `task_claim.py` / `chip_ledger.py` to actually pass it, which this document deliberately does NOT do.**

# Committing bookkeeping writes onto origin/<branch> tip (2026-08-18)

Chip: `chip-20260818-bookkeeping-writes-onto-origin-tip`, follow-on from
`chip-20260818-dispatch-registry-commit-rate-wedges-umbrella` (route C,
`REE_Working` `b5cb4153`) and
[`umbrella_ref_convergence_wedge_recurrence_20260818.md`](umbrella_ref_convergence_wedge_recurrence_20260818.md)
section 4, which named this as "the only candidate that removes the wedge
class outright" and deliberately did not attempt it ("this session could not
validate a change of that blast radius").

## 1. What this is

`scripts/ree_commit.py` gained a new opt-in CLI flag, `--to-remote-tip`
(requires `--push`; mutually exclusive with `--retry-push-on-reject`), and a
new function `land_at_remote_tip()`. When passed, the commit ree_commit.py
builds is **never given a ref** -- it is not `update-ref`'d onto the shared
checkout's local branch at all -- and is landed on `origin/<branch>`
primarily via the SAME already-hardened throwaway-worktree cherry-pick
machinery `--retry-push-on-reject` already uses as a rejection fallback
(`_push_one_commit_via_worktree`: `cherry-pick -x`, faithfulness
verification, structural per-entry re-apply on a line-level conflict,
bounded retry). Here it is the PRIMARY path, not only a fallback.

**On success:** the shared checkout's local branch ref is byte-identical
before and after the call. There is no local-ahead commit, so there is
nothing for `ref_convergence.py` to ever need to prove and nothing for it to
wedge on. The wedge CLASS (permanently-unprovable ahead commit) cannot arise
from a write landed this way.

**On any failure** (a genuine semantic conflict the structural re-apply
cannot resolve, or the rebase lock cannot be acquired within its timeout, or
retries are exhausted): falls back to EXACTLY today's pre-existing
behavior -- `update-ref refs/heads/<branch> new_sha old_head` (the same
compare-and-swap `main()` always used) -- so the commit becomes ordinary
local HEAD, exactly as if `--to-remote-tip` had never been passed. The
failure case is a strict no-op relative to today; only the success case
changes.

Verified live (real git repos, not just unit tests): a two-writer scenario
where `box` is behind `origin` and both sides append disjoint entries to the
same JSON registry lands cleanly on origin via structural re-apply, with
`box`'s `refs/heads/master` provably unchanged (`git rev-parse` before/after
identical) and `git status --porcelain` showing only the caller's own
pre-existing on-disk write. A genuine same-entry conflict (both sides
resolve the same claim differently) correctly falls back to local landing,
exit code 1, matching `--retry-push-on-reject`'s existing "commit is safe
locally" contract exactly.

## 2. Feasibility against ree_commit.py's actual contract (task point 1)

The concern going in: `build_private_index()` seeds its private index from
**local HEAD's tree**, then overlays only the declared paths from disk. If
local HEAD is behind origin (the routine state -- "two dispatchers write the
same origin"), does building on local HEAD produce a commit whose OTHER
(undeclared) paths are stale relative to origin?

**This does not matter, and no change to `build_private_index` was needed.**
The commit's diff relative to its own parent (`old_head`) only ever touches
the DECLARED paths (everything else is copied through unchanged from
`old_head`'s tree). When that diff is cherry-picked onto origin's current
tip, cherry-pick only replays the touched paths' hunks -- the "stale" content
for undeclared paths in the constructed tree is never part of the diff being
applied, so it is irrelevant. `_commit_touches_only()` (used by the existing
retry path) formalizes exactly this invariant; `land_at_remote_tip()` relies
on the same "touches only its declared paths by construction" property
without needing to re-check it (there is no ref for a rival process to move
in between, unlike the existing check's reason for re-verifying `HEAD`).

**Which callers could safely opt in, mechanically:** any caller committing to
a single, JSON-registry-shaped file with a working, unique per-entry key that
`_verify_keyed_merge_faithful`'s `_index_maps`/`_entry_delta` machinery can
resolve -- because that machinery is what makes the primary-path cherry-pick
SAFE against silently landing on the wrong entry (a "transplant") rather than
merely usually-correct. Concretely:

* **`task_claim.py`** (`TASK_CLAIMS.json`, keyed by `(session_id,
  claimed_at)`) and **`chip_ledger.py`** (`TASK_CHIPS.json`, keyed by
  `chip_ref`) -- both single-file writers of exactly the registries route C
  and the faithfulness-verification machinery already understand. Mechanically
  safe candidates.
* **NOT safe today:** `governance_flag.py` (`governance_flags.v1.json` --
  CLAUDE.md already documents `ID_FIELDS` has no working key for this
  registry, tracked separately as `chip-20260816-reecommit-idfields-registry-keys`)
  and `confirmer_verdict.py` (`experiment_proposals.v1.json` -- `claim_id` is
  declared but duplicated). For these, a real conflict cannot be proven
  faithful and `land_at_remote_tip()` would fall back to local landing every
  time a conflict occurs -- not unsafe (the fallback is the same "commit is
  safe locally" outcome the callers already handle), just not yet delivering
  the benefit. Fix the keying gap first.
* **Not evaluated, out of scope here:** `record_recommendation_outcome.py`
  (JSONL, not covered by route C's registry allowlist per
  `umbrella_ref_convergence_wedge_recurrence_20260818.md` section 9),
  `hygiene_routine_tick.py`, `igw_routine_tick.py` (multiple registries,
  more surface area than this session reviewed).

## 3. The read-modify-write contamination hazard (task point 2)

CLAUDE.md's "Read-modify-write contamination" section: a whole-file
read-modify-write reads the WORKING TREE, which can carry another session's
uncommitted edit, and a naive re-read-and-commit silently adopts it.

**This mechanism is unchanged by `--to-remote-tip`, and cannot be fixed by
anything in `ree_commit.py`.** `ree_commit.py` never reads or writes
application data itself -- it hashes whatever the CALLER already wrote to
disk before invoking it. The contamination happens strictly before
`ree_commit.py` runs, in the caller's own read-modify-write. Whichever mode
lands the result, it lands whatever was on disk.

**What DOES change: the disk file stays "live" (dirty, ' M') for longer
under `--to-remote-tip`, which widens the window during which the NEXT
caller's read-modify-write can pick up content that is not yet reflected in
local HEAD.** Concretely: today, a successful write immediately advances
local HEAD to include the new content, so the next caller's `build vs local
HEAD` comparison and its own disk read agree. Under `--to-remote-tip`, local
HEAD never advances for these paths, so disk can be arbitrarily far ahead of
local HEAD (bounded only by how often something else pulls). This does NOT
create data loss or silent corruption -- any read-modify-write that lands via
the SAME primary cherry-pick path is still checked by
`verify_cherry_pick_faithful`'s keyed proof (which compares by VALUE at each
identity key, so a "diff computed against a stale base" that happens to
re-describe an already-upstream entry is not itself wrong -- see section 4)
-- but it does mean local HEAD is a weaker source of truth for these specific
paths for longer, which is the documented trade-off in section 5 below, not
a new failure mode.

**A genuinely new question this raised, and answered by tracing the exact
mechanics:** could a stale-base diff (the artifact's documented "bundling"
shape -- a session's diff computed against local HEAD accidentally
re-describes an entry that already reached origin via a DIFFERENT session's
commit) get cherry-picked onto a tip that already has that entry and
DUPLICATE it? Verified this cannot happen silently: `verify_cherry_pick_faithful`
requires, for any file both sides touched, a KEYED semantic proof (every id
the box's diff "added": `M[id] == B[id]`; every id it did not touch:
`M[id] == A[id]`) rather than trusting the raw line-based merge result. A
value-identical re-description of an already-upstream entry satisfies this
trivially (same value, wherever it came from); if the underlying line-based
merge actually produced a duplicate key, the keyed indexing this check
performs would find the file un-keyable (duplicate key) and REFUSE (fatal ->
falls back to local landing) rather than silently push a corrupted file. This
was verified by re-reading `_verify_keyed_merge_faithful`/`_index_maps`
rather than assumed; no test in this session's suite specifically drives a
"stale-base re-description" case through the primary path (a real one would
need a 3-writer fixture), which is worth naming as a residual gap rather than
claiming full coverage.

## 4. Opt-in scoping (task point 3)

`--to-remote-tip` is a new CLI flag on `ree_commit.py`, defaulting to
**off**. No existing caller (`task_claim.py`, `chip_ledger.py`,
`governance_flag.py`, `confirmer_verdict.py`, `record_recommendation_outcome.py`,
`hygiene_routine_tick.py`, `igw_routine_tick.py`, or any manual invocation)
was changed. `git diff --stat scripts/task_claim.py scripts/chip_ledger.py`
against this session's changes is empty -- verified, not assumed. The
`RemoteTipNegativeControlTest` class in the test file below specifically
pins that a caller NOT passing the flag is byte-for-byte unaffected (local
HEAD still advances immediately on success, exactly as before this mode
existed).

**Deliberately not done in this session: wiring `task_claim.py` /
`chip_ledger.py` to pass the flag, even behind their OWN opt-in flag.**
Reason, found by tracing the caller contract rather than assumed: see
section 6.

## 5. Safety properties (task point 4) -- none relaxed

* No force-push anywhere in the new path (verified by reading
  `_push_one_commit_via_worktree` -- unchanged, reused as-is).
* No bare `update-ref` to a remote-derived value. The ONLY `update-ref` call
  in the new code (`land_at_remote_tip`'s fallback) is a compare-and-swap
  against `old_head` -- the exact same shape and exact same safety property
  as `main()`'s existing normal-path CAS. Pinned by
  `test_fallback_never_force_pushes_or_touches_origin`.
* `--allow-discard` / `safe_adopt_ref.py` are not invoked anywhere in this
  path -- there is no local-ahead state for either to reconcile, since the
  whole point is that no local-ahead state is ever created.
* `ref_convergence.py` is not invoked either, for the same reason.
* The documented trade-off, stated rather than hidden: on success, the
  touched paths sit as an ordinary unstaged ' M' modification in the shared
  checkout until something else next fast-forwards local HEAD past this
  push (a plain pull, `/session-land` housekeeping, or a later ordinary
  commit to the repo). This is the SAME shape CLAUDE.md documents as
  "someone may have it open" and explicitly warns never to blindly
  `git checkout -- ` away. The content is not at risk (durably on origin
  under a different, twin sha) but a careless narrow checkout of that one
  path on the shared checkout would revert the local working copy to
  pre-push content -- confusing, not lossy. Not solved here; recorded so a
  future caller-side integration weighs it explicitly.

## 6. The caller-wiring blocker found by tracing the contract (why not wired here)

`task_claim.py`'s `ree_commit_once()` determines whether a commit landed, and
which sha to read the committed content back from, by comparing
`head_sha(repo)` **before and after** the subprocess call -- it does not
parse `ree_commit.py`'s stdout at all today. `verify_landed()` then re-reads
the committed claim at exactly that returned sha (`claims_at_rev(sha)`) to
self-check that the write landed correctly.

Under `--to-remote-tip`, on SUCCESS local HEAD does not move, so
`before == after`, and `ree_commit_once()` would return the OLD (pre-write)
sha -- `verify_landed()`'s local-side self-check would then read the file
WITHOUT this session's own entry and report a false "SELF-CHECK FAILED",
even though the write correctly landed on origin (the separate
origin-side check in `verify_landed()` would correctly see it). This is a
real, traced contract break, not a hypothetical: `land_at_remote_tip()`
prints the created sha on its own machine-parseable line
(`ree_commit: to-remote-tip sha=<40-char-sha>`) specifically so a future
caller-side fix can capture it directly instead of relying on
before/after HEAD diffing, but `ree_commit_once()` does not do that
capture today.

**This is exactly the kind of check GOV-HELDOUT-1 asks for** (CLAUDE.md
General Rules): it directly shaped this session's scope decision -- not
wiring `task_claim.py`/`chip_ledger.py` to the new flag -- rather than being
retrofitted after the fact.

**What wiring would require, precisely, for a future session:**
1. `ree_commit_once()` gains a mode where, when the new flag is used, it
   captures stdout (currently uncaptured -- inherited straight to the
   terminal) and parses the `to-remote-tip sha=` line for the sha to return,
   instead of `head_sha()` before/after diffing.
2. `verify_landed()`'s contract (fails open, reads at the returned sha) is
   otherwise unaffected -- it just needs the correct sha handed to it.
3. `CommitLandedLocally`'s detection (`before and after and after != before`)
   needs a parallel path for the fallback case, where local HEAD DOES move
   (exactly as it does today) -- that part of the contract is unchanged and
   does not need new code, only needs to be exercised correctly alongside
   (1).
4. This touches `task_claim.py`'s and `chip_ledger.py`'s existing, extensive
   test suites (`test_task_claim_postcommit_selfverify.py`,
   `test_task_claim_retry_duplicate_commits.py`,
   `test_chip_ledger_push_wedge_revert.py`, and others) -- a real, separate
   testing pass, not a drive-by addition.

## 7. Tests (task point 5)

`scripts/test_ree_commit_remote_tip.py`, 12 tests, real git repos in a
tempdir (origin + two clones), time-independent, ASCII-only:

* `RemoteTipHappyPathTest` (5): local branch ref byte-identical before/after
  on success with a non-fast-forward push; working tree/index left exactly
  as the caller set them; no leaked worktree / no detached HEAD; the
  machine-parseable sha line, and the object is readable even though
  unreferenced; the "already on origin" idempotent no-op path.
* `RemoteTipFallbackTest` (3): a genuine semantic conflict falls back to
  local landing (exit 1, matching the pre-existing "commit is safe locally"
  contract exactly) and never touches origin; rebase-lock contention falls
  back immediately without waiting or touching the working tree.
* `RemoteTipCliValidationTest` (2): `--to-remote-tip` without `--push` dies
  before building anything; `--to-remote-tip` with `--retry-push-on-reject`
  dies (mutually exclusive).
* `RemoteTipNegativeControlTest` (2) -- **the load-bearing negative
  controls**: a caller NOT passing `--to-remote-tip` still advances local
  HEAD immediately on a plain push (unchanged default behavior); and a
  differential control proving the PRE-EXISTING wedge-prone MECHANISM is
  still present when `--to-remote-tip` is not requested (with
  `REE_COMMIT_NO_CONVERGE=1` to observe the raw divergence
  `--retry-push-on-reject` creates before the separate, best-effort
  `_converge_after_push()` reconciles it) -- this is the specific mechanism
  `--to-remote-tip` exists to avoid ever creating, and it must still occur
  when the new flag is not passed.

All 12 pass. All pre-existing `scripts/test_ree_commit_*.py` files (13
files, ~140 tests total) pass unchanged, run individually. `git diff --stat`
confirms `task_claim.py`/`chip_ledger.py` are untouched, so their own
extensive test suites are unaffected by construction and were not
separately re-run in full (see the honesty note in section 9).

## 8. Held-out check (GOV-HELDOUT-1)

**Only 2 independently-dated historical cases were found where OLD and NEW
give different verdicts, not 3 -- reported honestly per the rule's own
instruction ("if you cannot find 3, that is itself the finding").**

**Differing:**

1. **The 07:28Z wedge measurement itself** (this chip's own motivating
   artifact, `umbrella_ref_convergence_wedge_recurrence_20260818.md`
   section 1-3): 26 ahead commits, 17 unproven, all `chip_ledger.py`/
   `task_claim.py` bookkeeping. OLD requires route C (a large, separate
   reconciliation mechanism) to reduce -- not eliminate -- this. Under NEW,
   had these writes used `--to-remote-tip`, none would have created a local
   commit at all, so there is nothing to later find unproven. NEW gives the
   correct call (no wedge).
2. **The 2026-08-14 self-sustaining orphan-growth incident**
   (`retry_push_via_worktree`'s own docstring, `ree-cloud-5`, `[ahead 34]`
   at 02:30Z -> `[ahead 104]` at 04:06Z, ~45 orphans/hour): OLD's mechanism
   (advance local ref, THEN discover the push is rejected, THEN cherry-pick
   a twin) is what makes the residual self-sustaining -- once ahead by one,
   every subsequent push repeats the pattern. NEW never advances local ref
   on success, so the growth cannot start from writes using this mode.

**Search for a third, genuinely independent case came up empty.** Every
other documented incident of this specific failure class in CLAUDE.md and
the linked artifacts (the "5c05ebc9" bundling example, the 2026-08-15
`ree-cloud-5` measurement, the `chip-20260814-*` reconciliation chips) traces
back to the same short cluster of write-ups from 2026-08-14 through
2026-08-18 -- i.e. the same incident family this chip is itself a follow-on
of, not an independent historical source. Per the rule, this is the finding:
**this change is validated against a narrow, recent incident cluster, not
against the broader historical record**, and should be read accordingly.

**One negative control (degenerate, kept for completeness):** the 2026-08-08
detached-HEAD rebase-race incident (`_acquire_rebase_lock`'s docstring) is
NOT a differing case -- `land_at_remote_tip()` reuses the identical lock
(`_acquire_rebase_lock`/`_release_rebase_lock`) around the identical
worktree-mutating operations, so OLD and NEW are equally protected against
it. This bounds the change: the new primary path does not bypass any
existing concurrency protection.

**A separate, non-incident-based check that materially shaped scope** (noted
here because it is exactly the kind of check this discipline is meant to
encourage, even though it is not one of the >=3 required cases): tracing
`task_claim.py`'s `verify_landed()`/`ree_commit_once()` contract (section 6)
surfaced a real incompatibility that a naive "just pass --to-remote-tip
through" wiring would have silently broken (a false self-check failure on
every successful write). This is why callers are NOT wired in this session.

## 9. Honesty notes on verification limits

* This session did not run the full ~115-file / ~2500-test `scripts/`
  corpus via `run_scripts_tests.sh` (documented ~8 minutes at `--jobs 7`).
  Given the change's footprint is a single file (`ree_commit.py`, purely
  additive: one new function, one new CLI flag, one new early-validation
  branch) with zero lines changed in any other file, and all 13
  `test_ree_commit_*.py` files (existing + new, ~150 tests) pass
  individually, this was judged sufficient for the actual footprint of the
  change. This is a narrower verification than the full-corpus run CLAUDE.md
  asks for before landing under `scripts/`, stated plainly rather than
  implied.
* No test in this session drives a genuine 3-writer "stale-base
  re-description" scenario through the PRIMARY (not fallback) cherry-pick
  path end-to-end (see section 3's residual-gap note). The keyed-proof
  reasoning was verified by reading the existing, already-tested
  `_verify_keyed_merge_faithful` code rather than by a new fixture
  specifically for this shape.
* This document's own existence is not evidence the underlying practice
  (staging risky infrastructure changes for review before wiring callers)
  works -- consistent with GOV-HELDOUT-1's self-reference caution.

## 10. Recommendation

* **Land the core mechanism now** (already done, on `master`): it is
  opt-in, tested, and provably inert for every existing caller.
* **Do not wire `task_claim.py` / `chip_ledger.py` to pass
  `--to-remote-tip` without first fixing the `ree_commit_once()` /
  `verify_landed()` sha-tracking contract** (section 6) and re-running
  their existing test suites. This is real, separate, scoped work -- not a
  rubber stamp on top of what is here.
* Once wired (even behind a further caller-side opt-in flag, not a
  default), the natural next step is a soak period on manual/low-stakes
  invocations before considering flipping either script's DEFAULT --
  consistent with "opt-in per caller, never a global default flip" in the
  original brief.
* Follow-on, not attempted: fix `governance_flag.py`'s / `confirmer_verdict.py`'s
  registry keying (already tracked as `chip-20260816-reecommit-idfields-registry-keys`)
  before considering `--to-remote-tip` for those callers.
