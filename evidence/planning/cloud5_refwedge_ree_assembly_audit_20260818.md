# ree-cloud-5 REE_assembly `master` ref-wedge -- content audit and partial resolution

**Status: AWAITING OPERATOR ACTION -- the audit is complete and the one genuinely-stranded
piece of content has been recovered and landed, but the ref move itself is BLOCKED (see
section 6). The checkout remains wedged.**

- Session: `metaworker-chip-refwedge-ree-cloud-5-ree-assembly-master-since-2026-08-18t05-20-27z`
- Chip: `chip-refwedge-ree-cloud-5-ree-assembly-master-since-2026-08-18t05-20-27z`
- Box: `ree-cloud-5` -- checkout `/home/ree/REE_Working/REE_assembly`
- Audited: 2026-08-18T10:20Z - 10:37Z
- Worked example followed: `evidence/planning/cloud5_stale_scripts_wedge_staged_20260814.md` sections 5-6

## 1. The wedge

`scripts/ref_convergence.py` has been refusing to converge `master` onto `origin/master`
since 2026-08-18T05:20:27Z. **The refusal is correct and was not relaxed.** No heuristic
third proof route was added (`ref_convergence.py`'s docstring explains why reverse-apply
was designed and deliberately not shipped).

At audit start: `[ahead 269, behind 215]`, 56 proven upstream, **213 unproven**.
By the end of the session it had drifted to `[ahead 272, behind 216]` -- the drift is
entirely `phase3-heartbeats:` ticks (see section 3), which is why this cannot be cleared
by waiting.

This is the **third** wedge of this shape on this box: `backup/refwedge-20260815-master`
and `backup/refwedge-20260816-master` are the prior two. It recurs.

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

Content check, local tip vs origin tip:

- local  `cycles_completed: 2796`, `last_tick_utc: 2026-08-18T10:20:08Z`
- origin `cycles_completed: 2580`, `last_tick_utc: 2026-08-17T13:21:07Z`

Origin is ~21h stale **because** this checkout is wedged and cannot push. This is the same
derived-materialisation class CLAUDE.md describes for the phase3 queue writer: the
authoritative state is the live orchestrator, the git file is a materialisation, and the
next tick (cadence ~3-6 min, measured) rewrites it. Adopting origin therefore **fixes**
the staleness rather than causing it. Nothing durable is lost.

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
are on origin. Origin also already shows GFLAG-0038 `status: resolved` (governance cycle
2026-08-16T20:15:21Z, `cranky-driscoll-126a36`), whereas **local tip shows it `open`** --
so adopting origin is a strict improvement here, not a loss.

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
cherry-pick" mechanism the chip describes, and why nothing will ever prove this commit.

**Resolution:** applied as a narrow structural insert instead of a conflicting cherry-pick.
`implementation_note` added alongside origin's `implementation_note_update` -- both keys are
established convention in this file (30 vs 19 occurrences) and
`scripts/backfill_failure_record_run_role.py` reads both. Round-trip verified byte-exact
(`indent=2, ensure_ascii=True`), diff is **one line**.

**Landed on `origin/master` as `5c2078903c`.**

## 6. What remains -- OPERATOR ACTION REQUIRED

The audit is complete. Every commit in the ahead range has been content-audited and is
either already upstream, net-zero, derived telemetry regenerated on the next tick, or
(for the single true positive) recovered and landed. **The ref move is the only step left**,
and it is **blocked by the Claude Code auto-mode classifier** on this headless box: the
identical command passes with `--dry-run` and is refused without it. This is a permission
boundary, not a tooling defect and not a safety finding -- it was not worked around.

Dry-run confirmed clean immediately before the block:

```
safe_adopt_ref: dry run -- would move refs/heads/master from f5b44d3afa to 5c2078903c (origin/master)
```

Run this on a box (or under a permission mode) that permits the move:

```bash
R=/home/ree/REE_Working/REE_assembly
git -C "$R" branch "backup/pre-refconverge-$(date -u +%Y%m%dT%H%M%SZ)" master   # backup first
git -C "$R" rev-list origin/master..master > /tmp/discard_shas.txt
/opt/local/bin/python3 /home/ree/REE_Working/scripts/safe_adopt_ref.py \
  --repo REE_assembly --branch master --allow-discard $(cat /tmp/discard_shas.txt)
```

The list must be regenerated **immediately** before the move: the heartbeat writer adds a
commit every ~3-6 minutes, and `safe_adopt_ref.py` independently recomputes the discard set
and exits 3 on anything unacknowledged. That refusal is the backstop working -- just
regenerate and re-run. Re-running is safe and idempotent.

Confirm with:

```bash
/opt/local/bin/python3 /home/ree/REE_Working/scripts/ref_convergence.py --repo REE_assembly --check
# exit 0 = clear, 4 = still wedged
```

**Backup:** `backup/pre-refconverge-20260818T102515Z` -> `56dccd4e1e` (local to `ree-cloud-5`;
`enforce-single-branch.yml` deletes non-default branches on push, so it cannot be pushed).
Commits after that point are heartbeat ticks only, and `git reflog show master` recovers them.

## 7. Why this matters, and why it recurs

While wedged, the checkout cannot adopt origin, so its tracked tree -- `scripts/`, skills,
contracts -- is **frozen**, and every guard landed on origin since the strand is silently
undeployed on the box that runs headless chip sessions. That is the 2026-08-14 `ree-cloud-5`
outage shape.

Two structural contributors, both already tracked, neither fixed here:

1. `ree_commit.py`'s cherry-pick faithfulness gate cannot key `governance_flags.v1.json`
   (no `ID_FIELDS` member is present-and-scalar on a flag entry), so governance-flag pushes
   from this box refuse and the commits strand locally --
   `chip-20260816-reecommit-idfields-registry-keys`.
2. The `phase3-heartbeats:` writer commits every ~3-6 min against a checkout that cannot
   push, so the ahead count grows ~10-20/hour indefinitely. It is harmless content but it
   makes every convergence attempt a moving target and inflates the discard list. Worth
   considering whether the orchestrator heartbeat should short-circuit its commit while its
   own checkout is known-wedged.
