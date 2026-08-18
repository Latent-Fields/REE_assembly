# ree-cloud-5 REE_assembly `master` ref-wedge -- content audit and resolution

**Status: RESOLVED 2026-08-18T10:46Z. The checkout is converged
(`ref_convergence.py --check` exits 0, "no refusal state; converging normally").
No operator action outstanding.** Two follow-ups are noted in section 7 for a human to
weigh; neither blocks anything.

- Session: `metaworker-chip-refwedge-ree-cloud-5-ree-assembly-master-since-2026-08-18t05-20-27z`
- Chip: `chip-refwedge-ree-cloud-5-ree-assembly-master-since-2026-08-18t05-20-27z`
- Box: `ree-cloud-5` -- checkout `/home/ree/REE_Working/REE_assembly`
- Audited and resolved: 2026-08-18T10:20Z - 10:47Z
- Worked example followed: `evidence/planning/cloud5_stale_scripts_wedge_staged_20260814.md` sections 5-6

## 1. The wedge

`scripts/ref_convergence.py` had been refusing to converge `master` onto `origin/master`
since 2026-08-18T05:20:27Z. **The refusal was correct and was not relaxed.** No heuristic
third proof route was added (`ref_convergence.py`'s docstring explains why reverse-apply
was designed and deliberately not shipped). The refusal was cleared by doing the operator
work it exists to demand -- a per-commit content audit, then an explicitly acknowledged
adoption -- not by weakening the predicate.

At audit start: `[ahead 269, behind 215]`, 56 proven upstream, **213 unproven**.
By the time of the move it had drifted to `[ahead 272, behind 216]` -- the drift is
entirely `phase3-heartbeats:` ticks (section 3), which is why this could never clear by
waiting.

This was the **third** wedge of this shape on this box: `backup/refwedge-20260815-master`
and `backup/refwedge-20260816-master` are the prior two. It recurs -- see section 7.

## 2. Audit method

`ref_convergence.py --audit` (route C per-item content audit), then a **per-commit content
audit** of every distinct path group. Per CLAUDE.md, a `--allow-discard` acknowledgement
must rest on a content audit, never on a shape argument about which file a commit touches --
the 2026-08-15 measurement found 45% of route-A refusals were genuinely stranded.

The 213 unproven commits touch exactly three path groups:

| n | path | verdict |
|---|------|---------|
| 210 | `evidence/experiments/runner_heartbeats/ree-cloud-5.json` | safe to discard (section 3) |
| 2 | `evidence/planning/governance_flags.v1.json` | safe to discard -- net-zero pair (section 4) |
| 1 | `evidence/planning/substrate_queue.json` | **partial true positive -- RECOVERED AND LANDED** (section 5) |

## 3. Group A -- 210 `phase3-heartbeats: orchestrator tick ree-cloud-5` commits

Each touches **only** `evidence/experiments/runner_heartbeats/ree-cloud-5.json`
(verified by `git show --name-only` across all 210). The file is a flat 15-key JSON object
of current-state fields, fully overwritten on each tick by
`/home/ree/REE_Working/scripts/ree_metaworker_heartbeat.py` -- there is no accumulating
array, so no intermediate value is uniquely held by history.

Content check, local tip vs origin tip at audit time:

- local  `cycles_completed: 2796`, `last_tick_utc: 2026-08-18T10:20:08Z`
- origin `cycles_completed: 2580`, `last_tick_utc: 2026-08-17T13:21:07Z`

Origin was ~21h stale **because** this checkout was wedged and could not push. This is the
same derived-materialisation class CLAUDE.md describes for the phase3 queue writer: the
authoritative state is the live orchestrator, the git file is a materialisation, and the
next tick (cadence ~3-6 min, measured) rewrites it. Adopting origin therefore **fixed**
the staleness rather than causing it -- confirmed after the move, with the writer committing
normally again. Nothing durable was lost.

## 4. Group B -- GFLAG-0038 pair (net zero)

- `760825bb4a` (2026-08-18T05:20:47Z) `governance-flag: resolved GFLAG-0038`
- `30c8ae16a1` (2026-08-18T05:22:00Z) `Revert "governance-flag: resolved GFLAG-0038"`

`git diff 760825bb4a^ 30c8ae16a1 -- evidence/planning/governance_flags.v1.json` is **empty**.
The authoring box reverted its own commit 73 seconds later -- consistent with the known
`ree_commit.py` `ID_FIELDS` defect on `governance_flags.v1.json` (tracked as
`chip-20260816-reecommit-idfields-registry-keys`), which makes the push refuse from a
behind-origin checkout.

The underlying work is verified present on origin: `a843ee6ebb`
(`failure-autopsy: MECH-321/ARC-070 Step 9b Mode-B ...`) is an ancestor of `origin/master`,
and both `evidence/planning/failure_autopsy_mech321-hypothesis-legs-modeb_2026-08-18.{md,json}`
are on origin. Origin also already showed GFLAG-0038 `status: resolved` (governance cycle
2026-08-16T20:15:21Z, `cranky-driscoll-126a36`), whereas **local tip showed it `open`** --
so adopting origin was a strict improvement here, not a loss.

**Residual worth a human's attention (not blocking):** origin's `resolution_note` is the
*ratification* note ("Chipped as chip-20260816-mech321-hypothesis-legs-mode-b"), written
before the work was done. The *applied* note -- recording that the Mode-B pass actually
landed as `a843ee6ebb`, with the ledger delta and the GFLAG-0040 residual -- never reached
origin anywhere. The flag reads as routed-but-not-yet-done when in fact it is done.
Re-applying it is blocked by the same `ID_FIELDS` defect above.

## 5. Group C -- `b6cfbfaed3` substrate_queue (partial true positive) -- RECOVERED

`b6cfbfaed3` `substrate_queue: correct stale mech357-avoidance-efficacy-eligibility-trace-imbalance status`.

Per-item content audit against origin for `sd_id: mech357-avoidance-efficacy-eligibility-trace-imbalance`:

- **Already upstream**: `status: implemented` + `implementation_status: implemented` -- landed
  independently via `019a1120a1` (Mac governance cycle 2026-08-16). This is the load-bearing
  content (it stops the IGW generator re-offering already-built work).
- **Already upstream, and richer**: origin carries `implementation_note_update`,
  `implemented_utc`, `implemented_session`. Origin's note additionally carries a caveat the
  stranded note lacks ("NOT yet verified ... do not mark the failure_record resolved from
  this status flip alone"). **Origin is authoritative where the two differ.**
- **Genuinely NOT upstream**: the additive `implementation_note` field -- three incidental
  provenance breadcrumbs (the `mech357_n_freeze_noop` counter name; chip refs
  `chip-20260816-igw219-mech357-avoidance-efficacy-implement` and
  `chip-20260816-frozen-zgoal-family-935-drift`; the IGW-20260816-215 staleness rationale).

A `git cherry-pick -x b6cfbfaed3` onto `origin/master` **conflicts** -- origin had already
changed the same two status lines. This is exactly the "stranded by a conflicting push-retry
cherry-pick" mechanism the chip describes, and why nothing would ever have proven this commit.

**Resolution:** applied as a narrow structural insert instead of a conflicting cherry-pick.
`implementation_note` added alongside origin's `implementation_note_update` -- both keys are
established convention in this file (30 vs 19 occurrences) and
`scripts/backfill_failure_record_run_role.py` reads both. Round-trip verified byte-exact
(`indent=2, ensure_ascii=True`), diff is **one line**.

**Landed on `origin/master` as `5c2078903c`.**

## 6. The move, and the skew repair that followed

With every ahead commit content-audited, the adoption was performed with an explicit
acknowledgement of the full discard set, so `safe_adopt_ref.py`'s independent recomputation
stayed the gate:

```bash
git -C "$R" rev-list origin/master..master > /tmp/discard_shas.txt
/opt/local/bin/python3 /home/ree/REE_Working/scripts/safe_adopt_ref.py \
  --repo REE_assembly --branch master --allow-discard $(cat /tmp/discard_shas.txt)
```

Backup taken first: `backup/pre-refconverge-20260818T102515Z` -> `56dccd4e1e` (local to
`ree-cloud-5`; `enforce-single-branch.yml` deletes non-default branches on push, so it
cannot be pushed). `git reflog show master` recovers the discarded range.

**The move succeeded but its built-in skew repair was cut off partway** (the invocation hit
a 2-minute tool timeout while materialising a 216-commit adoption). The ref had already
moved -- `master == origin/master` -- so the residue was a half-finished repair, which is
precisely the state CLAUDE.md's HEAD/worktree-skew section is written for. It was completed
by hand, reading the status **codes** rather than a dirty-file count:

- **29 `M ` staged reverts** -- each verified byte-identical to the pre-move HEAD
  (`fe53d6fba7`) before touching it, per the rule that an `M ` restore is *not*
  unconditionally safe. All 29 matched -> stale adoption lag, nothing local to lose ->
  restored with `git checkout HEAD -- <paths>`. Never `git checkout -- .`.
- **2 `A ` staged re-adds** -- the deletion-direction analogue, and the one variant the
  documented detector does not name.
  `evidence/literature/neuro_pe_habenula_da/entries/2026-02-13_habenula_da_signed_pe_review/`
  was **deliberately deleted upstream** by `734a9eab1a` ("governance 2026-08-16: remove
  placeholder habenula/DA literature entry (GFLAG-0031)"); index and worktree still held it,
  so adopting the deletion surfaced it as a staged addition -- a staged revert of an upstream
  *deletion*. Both files verified byte-identical to pre-move HEAD, then removed with
  `git rm -f`, adopting the governance decision.
- **1 `MM`** (`scripts/steward/state/steward_ledger.jsonl`) -- staged revert *plus* an
  unstaged edit on top. Content check against pre-move HEAD **differed**, i.e. a live
  session's uncommitted work. **Not restored** -- `git checkout HEAD --` would have destroyed
  it. Only the staged revert was cleared, index-only: `git reset -q -- <path>`.
- **1 ` M`** (`evidence/planning/cloud5_stale_scripts_wedge_staged_20260814.md`, held under
  an active claim by `metaworker-chip-20260814-cloud5-stale-scripts-disabled-orphan-guard-b`)
  -- another session's live work, deliberately untouched.

Final state: `## master...origin/master` with no ahead/behind, and the working tree carrying
only the two ` M` files that belonged to other sessions before this session started.

**Confirmation:**

```
$ /opt/local/bin/python3 scripts/ref_convergence.py --repo REE_assembly --check
ref_convergence --check: /home/ree/REE_Working/REE_assembly -- no refusal state; converging normally
EXIT=0
```

The tracked tree is current again -- `scripts/`, skills and contracts are at origin, so
guards landed since the strand are deployed on this box rather than silently frozen.

## 7. Why it recurs -- three observations, none fixed here

While wedged, the checkout cannot adopt origin, so its tracked tree -- `scripts/`, skills,
contracts -- is **frozen**, and every guard landed on origin since the strand is silently
undeployed on the box that runs headless chip sessions. That is the 2026-08-14 `ree-cloud-5`
outage shape. This box has now wedged three times in four days, so the mechanism matters
more than this instance:

1. `ree_commit.py`'s cherry-pick faithfulness gate cannot key `governance_flags.v1.json`
   (no `ID_FIELDS` member is present-and-scalar on a flag entry), so governance-flag pushes
   from this box refuse and the commits strand locally --
   `chip-20260816-reecommit-idfields-registry-keys`. This is what produced the group-B pair
   and, one revert later, the unprovable strand that pinned the whole ref.
2. The `phase3-heartbeats:` writer commits every ~3-6 min against a checkout that cannot
   push, so the ahead count grows ~10-20/hour indefinitely. The content is harmless, but it
   makes every convergence attempt a moving target, inflates the discard list, and buries the
   two or three commits that actually need auditing under 210 that do not. Worth considering
   whether the orchestrator heartbeat should short-circuit its commit while its own checkout
   is known-wedged (`ref_convergence.py --check` already answers that question cheaply, and
   is already the routine-tick entry point).
3. `safe_adopt_ref.py`'s post-move skew repair is not restartable and leaves no marker that
   it was interrupted. On a large adoption it can exceed a caller's timeout; the ref has
   moved by then, so the operation *looks* done while a half-repaired index sits armed with
   staged reverts that a bare `git commit` would land. The repair is idempotent in effect, so
   simply re-running `safe_adopt_ref.py` finishes it -- worth saying somewhere a session will
   read before hand-rolling the repair, as this one did.
