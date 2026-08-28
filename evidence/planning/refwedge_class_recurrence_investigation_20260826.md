# Ref-convergence wedge class: why it still recurs (2026-08-28)

**Status: root-cause investigation. Diagnosis + proposals only. NOTHING in `scripts/` was
modified by this session, no live wedge was cleared, no lease taken, no ref moved.**

Chip: `chip-20260826-refwedge-class-recurrence-investigation`.
Session: `refwedge-class-investigation-20260828` (Remote Control, `DLAPTOP`).
Measured on `DLAPTOP`, `/Users/dgolden/REE_Working` (umbrella), `master`, 2026-08-28T05:39Z
-> 07:10Z, against a **live, uncleared wedge** (`first_refused_at` 2026-08-27T22:11:20Z).
Load average during the session was 27-29; that is context for timings, not a cause.

Continues `umbrella_ref_convergence_wedge_recurrence_20260818.md` (route C). That document's
**section 5 follow-on item 1** -- "commit bookkeeping writes onto `origin/<branch>`'s tip
rather than local HEAD, so the shared checkout never diverges" -- was built
(`--to-remote-tip`, ree-v3-adjacent `fce23fe5`, 2026-08-18T21:32Z) and made the default for
both ledger writers on 2026-08-23. **This investigation's central finding is that it is
gated off in exactly the state it was built to prevent.**

---

## 0. Summary

| the chip's hypothesis | verdict |
|---|---|
| Throwaway-worktree pushes leave the shared ref behind | **Confirmed** -- by design; `retry_push_via_worktree` never moves the shared ref |
| The ahead-count grows while wedged | **Confirmed** -- measured live, `[ahead 7] -> [ahead 10]` in ~60 s |
| "each subsequent commit joins an ever-harder-to-prove ahead set" | **REFUTED** -- new orphans are route-B provable *by construction*; unproven count was flat at 4 across that growth |
| The wedge is self-feeding | **Confirmed, different mechanism** -- see §3, the latch |
| The prior fixes did not work | **REFUTED** -- route C cut the rate ~7-12x, after which it went flat |
| `DLAPTOP` has a higher recurrence rate | **Refuted on frequency; confirmed on detection and repair latency** (§5) |

The one-sentence root cause: **a wedge is a LATCH.** Being ahead disables `--to-remote-tip`,
the mode that would stop the checkout going further ahead; going further ahead keeps the
latch set. The ahead-count is not what makes a wedge permanent -- an unprovable commit is --
but the latch is what makes the wedge *grow*, freeze the tree, and require out-of-band
operator work every time.

---

## 1. Evidence base

Three independent, read-only sources.

1. **The live wedge.** Audited with `ref_convergence.py --audit`, which is read-only by
   construction ("It reports; it never converges and never acknowledges anything"), plus
   direct `git cat-file` reads of the object store. Left exactly as found, as evidence,
   with the Orchestrator's agreement.
2. **The `chip-refwedge-*` population in `TASK_CHIPS.json`** -- the durable, machine-written
   occurrence log produced by `hygiene_routine_tick.py` source 10. 27 chips, of which 23
   are episode-resolved (§4.1).
3. **`~/Library/Logs/ree_hygiene_tick.launchd.log`** on `DLAPTOP`, carrying verbatim output
   of the writer calls that minted the poison; plus a verbatim transcript excerpt supplied
   on request by the sibling session `rc-bashgate-dec5b42b`, for the one poison commit whose
   generating command was not in that log.

---

## 2. The live wedge, decomposed

`ref_convergence.py --repo REE_Working --branch master --audit`, 2026-08-28T05:40Z:

```
audit of master vs origin/master -- 10 ahead, 6 proven, 4 unproven
    PROVEN   385bbb6adc  cherry-picked upstream (-x backref)  chips: claim chip-20260827-precommit-cache-...
    PROVEN   dacbf3e80b  cherry-picked upstream (-x backref)  chips: claim chip-20260826-refwedge-...
    PROVEN   bf66c139e1  cherry-picked upstream (-x backref)  chips: claim chip-20260827-chipledger-...
    PROVEN   434e262be3  cherry-picked upstream (-x backref)  claim: open refwedge-class-investigation-...
    PROVEN   5e9ae04cde  cherry-picked upstream (-x backref)  claim: open rc-chipledger-lockfailopen-...
    PROVEN   a3a89678f5  cherry-picked upstream (-x backref)  claim: open rc-bashgate-dec5b42b
    UNPROVEN 092d21fb87  chips: claim chip-20260827-bashcommandgate-nongit-overfire
    UNPROVEN d0d35e5f95  chips: archive resolved-chip fields into chip_archive/2026-08.json
    UNPROVEN ef4e34ea31  chips: record chip-queuefloor-dlaptop-since-2026-08-27t18-50-30z
    UNPROVEN f34963462f  chips: record chip-gitsyncverdict-dlaptop-ree-working

  1 unproven commit(s) touch non-registry paths ... d0d35e5f95  chip_archive/2026-08.json
  Registry items NOT present upstream (1):
      TASK_CHIPS.json :: item ('chip-20260827-bashcommandgate-nongit-overfire',): tip value not present upstream
```

Persisted wedge state at the same moment:

```json
{"ahead_count": 10, "first_refused_at": "2026-08-27T22:11:20Z",
 "last_refused_at": "2026-08-28T05:40:14Z", "refusal_count": 9,
 "unproven_count": 4,
 "unproven_shas": ["092d21fb87","d0d35e5f95","ef4e34ea31","f34963462f"]}
```

### 2.1 The ahead set does NOT get harder to prove

At 05:39:05Z the banner read `4 refusal(s), now 4 ahead`, 3 unproven. Sixty seconds later,
after four Remote Control sessions opened their claims (this session's own two writes among
them), it read **10 ahead, 4 unproven**. Six new orphans arrived and **all six were
immediately provable**.

This is not luck. A successful push-retry writes `(cherry picked from commit <sha>)` into the
twin it pushes -- `git cherry-pick -x` on the clean path, and the structural re-apply path
writes the identical trailer by hand (`ree_commit.py:3325`) -- so route B covers every such
orphan *by construction*.

**So the chip's "ever-harder-to-prove ahead set" describes a set that empirically does not
get harder to prove.** What grows with the ahead-count is the *cost* of the wedge: a frozen
working tree, a longer list a human must audit per-commit before `--allow-discard`, and a
rising probability of a genuine cherry-pick conflict (which is itself a poison generator).

### 2.2 One poison commit denies proof to several innocent ones

Only **1** of the 4 unproven commits holds content genuinely absent from origin
(`092d21fb87`). The other 3 are collateral of `_apply_route_c`:

```python
for sha, author, subject in unproven:
    if not touches_only_registries(repo, sha):
        # One non-registry unproven commit refuses the move anyway, so there
        # is nothing to gain by scanning registries. Bail before the cost.
        return proven, unproven
```

`d0d35e5f95` touches `chip_archive/2026-08.json`, which is not in `REGISTRY_SPECS`. The bail
therefore fires, and `ef4e34ea31` / `f34963462f` -- registry-only, net effect fully upstream
-- are reported unproven purely as collateral.

That reasoning is correct for the **move** (refused either way) and wrong for the **report**:
`--audit` exists precisely because `CLAUDE.md` mandates a per-commit content audit before any
`--allow-discard`, and here it inflates that list **4x** (4 reported, 1 real).

---

## 3. THE LATCH -- the actual self-feeding mechanism

`--to-remote-tip` lands a commit on `origin/<branch>` **without ever moving the shared
checkout's local ref**. Its own docstring states the consequence plainly:

> "This function removes the wedge class outright for its caller's paths by never creating
> the divergence in the first place: `new_sha` never becomes `refs/heads/<branch>`, so there
> is nothing for a later convergence pass to prove OR to wedge on."

It is fully plumbed through **both** poison-generating writers (`chip_ledger.py`,
`task_claim.py`) and, since 2026-08-23
(`chip-20260823-remotetip-flip-ledger-writer-defaults`, user-authorised), it is the
**default**. And then:

```python
# chip_ledger.remote_tip_is_default  /  task_claim.remote_tip_is_default
if args.to_remote_tip and _local_branch_is_ahead():
    args.to_remote_tip = False
```

**The wedge-eliminating mode resolves OFF the moment the branch is ahead -- which is the
definition of a wedged checkout.** So:

```
wedged  ->  branch is ahead  ->  remote-tip gated OFF  ->  ordinary branch push
        ->  rejected (non-fast-forward)  ->  push-retry via throwaway worktree
        ->  +1 orphan, shared ref not moved  ->  branch is (still, more) ahead  ->  ...
```

Confirmed live: every one of this session's own commits printed
`push-retry 1/3: pushed via throwaway worktree (shared checkout untouched)` -- the gated-off
branch-push path -- not the remote-tip path.

### 3.1 The gate's justification is sound for a TRANSIENT ahead and false for a WEDGED one

The gate is not a mistake; it was added deliberately after a plain flip was reverted, and its
docstring gives the reason:

> "`--to-remote-tip` does not push a branch -- it cherry-picks THIS call's own commit onto
> origin in a throwaway worktree -- so with an unconditional default there is no carrier and
> a withheld close is STRANDED PERMANENTLY... The arrangement SELF-HEALS: a consecutive write
> whose cherry-pick conflicts falls back to local landing (leaving the branch ahead by one),
> and the next write therefore takes the branch-push path and lands both."

Every clause of that is correct **when the ahead-ness is transient**: the ordinary branch push
pushes `<sha>:<branch>`, which carries ancestors, so the withheld commit gets a free ride.

On a **wedged** checkout the carrier does not exist. The next ordinary branch push is
guaranteed to be rejected -- that is what "wedged" means -- so it carries nothing, and control
passes to the push-retry, which transplants **only this call's own commit**. The self-heal
step "the next write lands both" never executes. The gate is paying a real cost (re-arming
the latch on every write, forever) for a benefit that is unavailable in that state.

### 3.2 A related consequence, worth stating separately

The same "the push-retry transplants only THIS commit's diff" fact explains why locally-kept
content never escapes. This session's own `chip_ledger claim` printed:

> `KEPT this box's unpushed change to chip-20260827-bashcommandgate-nongit-overfire (origin
> has not seen it -- it is NOT visible to any other host until the push lands)`

and its commit did carry that value in its tree. It still did not reach origin, because by
then the value lived in the commit's **base**, not its **diff**, and the 3-way merge against
an origin that lacks it resolves it away. **"Kept locally" and "will reach origin" are
unrelated properties, and only the first is true.** Verified: `claimed_by` for that chip is
`None` across **all 115** origin `TASK_CHIPS.json` commits since 2026-08-27T20:00Z, and no
`-x` backref naming `092d21fb87...` exists anywhere on origin.

---

## 4. The poison taxonomy

The latch explains growth. Poison explains *permanence*: `ref_convergence` refuses while any
one ahead commit is unprovable, correctly and by design. Four generator classes, each with
live evidence.

### P1 -- the no-op churn commit

`chip_ledger._mutate_and_commit_locked` **always** writes and **always** commits, whether or
not `apply_fn` changed anything:

```python
note = apply_fn(data)          # may be a pure "already recorded -- not appending again"
...
atomic_write_text(CHIPS_PATH, text)
print(note)
try:
    commit(commit_message, push, bot, to_remote_tip=to_remote_tip)
```

`load_chips_for_mutation` first rebases/merges origin into the local file, so a
**semantically empty** call still produces a changed file, hence a commit whose entire
content is the rebase product. Verbatim, `DLAPTOP` tick log, 2026-08-28:

```
chip_ref chip-gitsyncverdict-dlaptop-ree-working already recorded (origin=hygiene_tick) -- not appending again

NOT RETRYING: ree_commit.py exited 1 AFTER creating commit f34963462f.
```

Measured content of `f34963462f`, item-by-item against its parent:

| | |
|---|---|
| items | 1932 -> **1925** |
| added | none |
| **removed** | **7 chips, every one minted by `ree-cloud-4` / `ree-cloud-5`** |
| changed | `chip-20260827-cloud4metaworker-orchestrator-stalled-222min-cycle758`: `status` `withdrawn -> open`, `resolved_at` set -> `None` |
| **intended item-level delta** | **none -- the command recorded nothing** |

That is the **regression direction** of the read-modify-write sweep (root `CLAUDE.md`,
background A-05) happening live, under a `chips: record` message, from a command that
recorded nothing. The next call, `ef4e34ea31`, is its mirror image (1925 -> 1932, restoring
all 7, re-resolving the one) and names the mechanism in its own log line:

```
1 origin terminal resolution(s) protected from a stale snapshot
  KEPT origin's resolved status for chip-...-222min-cycle758 (the working tree held a
  stale pre-resolution snapshot -- resolution is monotone, so it cannot be a real edit)
```

Both exited 1 and both are now permanent poison. The faithfulness verifier almost certainly
did its job on the first: a commit whose net effect is deleting 7 entries origin holds is
exactly what `verify_cherry_pick_faithful`'s Case-2 collateral multiset check must refuse.
**So the guard converts a would-be data corruption into a permanent convergence poison** --
the right trade at the instant it is made, and the wrong outcome overall, because the commit
should never have been minted.

**Census (negative result, and it is informative).** Scanning the last **400** origin/master
`TASK_CHIPS.json` commits (2026-08-27T04:23Z -> 2026-08-28T05:44Z), parsing every distinct
blob: **0 zero-item-delta commits and 0 item-count-shrink commits.** Origin's history is
clean of this shape -- precisely because these commits are the ones that fail to push. **The
poison population is unobservable from origin**, exists only as local-only orphans on wedged
boxes, and is destroyed by the `--allow-discard` that clears the wedge. That is a large part
of why this class has been hard to characterise across eleven days.

### P2 -- a non-registry path in the ahead range

`chip_archive/<YYYY-MM>.json` is written daily by `chip_ledger.py archive` (launchd
`com.ree.chiparchive`, 04:30 local). It is a whole-file JSON registry with more than one
producing box, and it is in **neither** `REGISTRY_SPECS` nor any route-C-eligible shape.
Today's run (`d0d35e5f95`) failed to push and is now the commit that denies route C to the
entire range (§2.2).

It cannot be added to `REGISTRY_SPECS` as written: its `chips` member is a **dict keyed by
`chip_ref`** (486 entries), not the array-of-item-dicts that `RegistrySpec`'s
`array_key`/`key_fields` contract assumes. Covering it needs either a new `kind` in
`_load_registry` or a change to the archive file's shape.

Note the layer mismatch. `cmd_archive`'s gate ("refusing is cheap and self-correcting -- the
archive commit is already made, so the next daily run re-verifies and proceeds once the push
lands") is right **at the archive layer** and wrong at the convergence layer: each failed
attempt leaves one more unprovable orphan, and on a wedged box the attempt can fail daily.

### P3 -- the deliberate non-fatal no-push branch

`092d21fb87`, the only commit here holding genuinely stranded content, came from this
documented, intentional branch. Verbatim, supplied by the session that ran it
(`rc-bashgate-dec5b42b`, 2026-08-28T05:39:23Z):

```
  CONTINUING (exit 0): the push was on BY DEFAULT, not requested.
  The entry is committed locally, which is what this command
  did before pushing became the default -- so this is not a
  regression, but the content is NOT on origin and no later
  session will carry it there (see push_is_default()).
  Pass --push to make this fatal instead.
```

`chip_ledger.py` states the consequence exactly right, including *"no later session will
carry it there"* (§3.2 explains the mechanism). What is missing is the other half: the branch
announces a permanent strand and **nothing records that fact anywhere durable.**

### P4 -- the amplifier (cost, not poison)

Every ordinary coordination write on a wedged box adds one route-B-provable orphan. It does
not impede convergence. It does: freeze the working tree, so guards landed on origin are
silently undeployed (the `cloud5_stale_scripts_wedge_staged_20260814.md` failure); lengthen
the per-commit audit a human must perform; and raise the chance of a real cherry-pick
conflict, which is itself a P-class generator. This is the class the latch (§3) drives.

---

## 5. Rate: before/after, and the confound that has to be stated first

### 5.1 The detector's sensitivity changed on the same day as the fix

The `chip-refwedge-*` population **cannot** support a naive before/after split across
2026-08-18. Any such split measures the detector.

* `1b6f7813`, **2026-08-18T03:17:16Z** -- "hygiene_tick: episode-qualify the refwedge
  chip_ref so a RECURRING wedge can be chipped". Before it, `cmd_record`'s chip_ref dedup
  collapsed every later wedge on the same `(host, repo, branch)` triple into the first one's
  chip: **at most one chip per triple, ever.**
* `c559183b` + `b5cb4153`, **2026-08-18T08:49:30Z** -- route C.

Five and a half hours apart, same day. Of the 27 `chip-refwedge-*` chips, only the **23**
carrying a `-since-<episode>` slug are episode-resolved; the other 4 predate `1b6f7813` and
each stands for an unknown number of episodes. **The "23 occurrences" figure in the chip is
exactly this episode-qualified set -- i.e. it is already the post-detector-fix population,
and must not be read as "23 failures of the fix".**

The only window with uniform sensitivity is **2026-08-18T03:17Z onward**.

### 5.2 Rates inside that window

| window | n | span | episodes/day |
|---|---|---|---|
| pre-route-C (08-18 03:17Z -> 08:49Z) | 5 | 0.23 d | **21.7** |
| post-route-C (08-18 08:49Z -> 08-28 05:40Z) | 18 | 9.87 d | **1.82** |
| post `reconcile_wedge_content` fix (08-19 02:10Z ->) | 16 | 9.15 d | 1.75 |
| post `857f9ff7` registry-aware advice (08-21 19:34Z ->) | 12 | 6.42 d | 1.87 |
| last 5 days | 9 | 5.24 d | 1.72 |

Normalised by fleet write volume (origin/master commits/day), which removes the "quiet fleet"
confound -- 2026-08-24 saw only **45** origin commits, and accounts for most of the apparent
08-22 -> 08-25 lull:

* pre-route-C: ~5 episodes per ~250 origin commits ~= **20 per 1000 commits**
* 2026-08-19 .. 08-27: 16 episodes per 5,643 origin commits ~= **2.8 per 1000 commits**

**Route C bought a 7-12x reduction depending on normalisation, and nothing since has moved
the rate at all.** The pre-fix sample is short (5.5 h, n=5) and that caveat is real; the
intra-day pattern on 2026-08-18 itself is consistent with it (5 episodes in the first 5.5 h,
2 in the remaining 18.5 h).

**Note what the flat post-08-23 segment means given §3.** The remote-tip default flip landed
2026-08-23 and the rate did not move -- which is exactly what the latch predicts: the mode is
disabled in every state where it would have helped.

Correct reading of "the rate hasn't gone to zero": **the fixes worked, and the class now sits
on a stable floor of ~1.8 episodes/day fleet-wide, set by the poison arrival rate of §4.**
Nothing shipped since 2026-08-18 addresses P1, P2 or P3, and the one thing that addresses P4
is latched off.

### 5.3 Per-box: the `DLAPTOP` sub-hypothesis

| box / checkout | episodes | median detect lag | median dur | mean dur | max dur |
|---|---|---|---|---|---|
| `dlaptop` / `REE_Working` | 10 | **55.9 min** | 2.08 h | **4.77 h** | **14.0 h** |
| `ree-cloud-5` / `REE_Working` | 8 | 11.4 min | 1.90 h | 2.42 h | 6.5 h |
| `ree-cloud-5` / `REE_assembly` | 2 | (pooled above) | | | |
| `ree-cloud-4` / `REE_Working` | 3 | 14.6 min | 1.11 h | 1.25 h | 2.1 h |

**Frequency: refuted.** `DLAPTOP`'s single checkout wedged 10 times; `ree-cloud-5`'s
`REE_Working` checkout wedged 8. That gap does not survive normalisation by write volume, and
the chip's proposed explanation (long idle gaps between interactive bursts letting other
writers accumulate) predicts a *frequency* effect that is not present.

**Latency: confirmed, and the larger effect.** ~4-5x slower to detect, ~2-4x slower to clear.
The live episode is the extreme case: 7.5 h old at time of writing with **no
`chip-refwedge-...-since-2026-08-27t22-11-20z` chip in the ledger at all.**

The cause is in the tick log, and it is not idleness. `DLAPTOP`'s hygiene tick runs on
schedule (`com.ree.hygienetick`, `StartInterval` 900) and **correctly detects the wedge** --
`ref_convergence_wedge: {'scan_ok': True, 'scanned': 7, 'wedged': 1}` -- and then **every
chip it tries to mint fails**:

```
  ERROR chip-staleclaim-insights-7fd98a-20260827T052925Z                    -- SystemExit(1)
  ERROR chip-ledgerint-claimskew-chip-20260827-capability-contract-preflight -- SystemExit(1)
  ERROR chip-refwedge-dlaptop-ree-working-master-since-2026-08-27t07-25-32z  -- SystemExit(1)
  ERROR chip-strandedwt-dlaptop-metaworker-chip-20260820-31c0b573571a        -- SystemExit(1)
  ERROR chip-wtremoved-dlaptop-dazzling-jackson-efb9e9                       -- SystemExit(2)
  ERROR chip-scriptscorpus-dlaptop-sweep-14-8220a4d6ba1cc18e                 -- SystemExit(1)
  ERROR chip-unlandedwt-dlaptop-metaworker-chip-20260814-92a2d0fc78d3        -- SystemExit(1)
  ERROR chip-gitsyncverdict-dlaptop-ree-working                              -- SystemExit(1)
  ERROR chip-queuefloor-dlaptop-since-2026-08-27t18-50-30z                   -- SystemExit(1)
```

`ref_convergence.py`'s docstring justifies escalating from the tick rather than from inside
`converge()` on the grounds that "the tick runs outside the lock and pushes normally, and its
push demonstrably survives a wedged checkout." **On `DLAPTOP`, as of 2026-08-28, that
assertion is false: the wedge silences its own alarm.** That is the same shape --
loud-once-then-silent -- that `record_refusal`/`wedge_report` were built to fix, reappearing
one layer up.

Two of the nine failures (`chip-gitsyncverdict-...`, `chip-queuefloor-...`) are the P1 churn
commits of §4, so the failing mint path and the poison generator are **the same code path**.
Whether the underlying `SystemExit(1)` is the ledger mutation lock, the push-retry, or
something else is being investigated live by
`chip-20260827-chipledger-lockfailopen-sweep-investigation`; this report deliberately does
not duplicate that, and every finding above stands independently of its outcome.

---

## 6. Proposals

None relaxes `ref_convergence`'s refusal. None adds a proof route. Both remain correctly
rejected in the module's own docstring and are out of bounds per the chip.

### R1 (primary) -- gate remote-tip on "ahead **AND NOT wedged**", not on "ahead"

**Change.** In `chip_ledger.remote_tip_is_default` and `task_claim.remote_tip_is_default`,
replace `_local_branch_is_ahead()` with "ahead **and** the checkout is not wedged", reading
the verdict `ref_convergence` already computes and persists (`wedge_severity` -> `transient`
vs `wedged`; `--check` exits 4). Everything else -- the explicit-flag override, the no-push
downgrade, the fallback-to-local-CAS on any non-success -- unchanged.

**Why.** §3.1: the gate's carrier argument is true for a transiently-ahead checkout and false
for a wedged one, where the next branch push is guaranteed rejected and therefore carries
nothing. On a wedged checkout remote-tip is strictly better: it lands the content on origin
and creates no new orphan.

**Why it is safe.** The dangerous direction is using remote-tip when a withheld commit still
needs a carrier. That risk is *strictly smaller* under the new gate, because it only ever
turns remote-tip ON in a state where no carrier is coming. `_local_branch_is_ahead()`'s
fail-closed discipline should be preserved verbatim: any "cannot tell" (no upstream, git
error, unreadable wedge state) must resolve to today's behaviour.

**What it does and does not do.** It cuts P4 -- a wedged box stops manufacturing orphans, the
tree stops being frozen, `--allow-discard` lists stop growing. It does **not** clear a live
wedge and does **not** reduce the poison arrival rate; P1/P2/P3 are untouched. The rate of
*episodes* would not fall; the *cost and duration* of each should.

### R2 -- make `--audit` report the true poison set

**Change.** Keep `_apply_route_c`'s bail on the convergence path (a correct latency
optimisation inside `ree_commit`'s 30 s rebase lock) and **skip it under `--audit`**, which is
read-only, runs outside the lock, and has no latency budget.

**Why.** `--audit` exists because `CLAUDE.md` mandates a per-commit content audit before any
`--allow-discard`, and it currently over-reports by 4x on the live case, inflating exactly the
list a human must work through one commit at a time. It cannot cause a wrong move: the
non-registry commit still refuses.

### R3 -- do not mint a commit for a semantically empty ledger mutation

**Change.** In `chip_ledger._mutate_and_commit_locked`, when `apply_fn` leaves the item list
unchanged, write the merged file to disk and print the note as now, but **return without
committing**.

**Held-out outcome: FAILED the >=3 bar. Shipping this, if it ships, must be explicitly
incident-scoped** -- see §7.3. Kept in the list because P1 is real and measured, not because
the check passed.

### R4 -- `chip_archive/<YYYY-MM>.json` is an uncovered whole-file registry *(finding, not a proposal)*

Needs a dict-shaped `kind` in `_load_registry`, or a change to the archive file's shape. Both
have their own consumers (`chip_ledger.archived_field`, `audit_orphan_chips`,
`substrate_queue_writeback_drift`, `serve.py`'s `/api/chips/prompt`) and deserve their own
chip. Recording the gap is the deliverable here.

### R5 -- the implicit-push no-push branch strands content with nothing to recover it *(finding, not a proposal)*

Making `push_is_default()`'s non-fatal branch fatal is **not** proposed: its stated rationale
(not regressing against pre-2026-08-15 behaviour) is sound and this investigation found no
evidence against it. The gap is the other half -- the branch announces "no later session will
carry it there" and nothing records that anywhere durable. `reconcile_wedge_content.py` exists
for precisely this shape and is not wired to it. A separate, separately-reviewable change.

---

## 7. Held-out check (GOV-HELDOUT-1)

Per root `CLAUDE.md`: at least 3 historical cases the rule was **not** written from, where old
and new wording give **different** answers. Degenerate cases are excluded and named.

### 7.1 R1 -- "gate remote-tip on ahead AND NOT wedged"

Old = current code (remote-tip off whenever ahead). New = off only when ahead and not wedged.
They differ on any wedged checkout that then performed ledger writes. Four such cases, all
with **measured** ahead-counts recorded by someone other than this session:

1. **2026-08-23, `DLAPTOP` umbrella, `[ahead 20, behind 249]`** -- recorded in
   `remote_tip_is_default`'s own docstring, which adds "nearly every ahead commit audited in
   both was a `claim:` or `chips:` commit, i.e. produced by these two scripts." Old: every one
   of those 20 is an orphan. New: they land on origin's tip and no divergence is created.
   **Different.**
2. **2026-08-23, `ree-cloud-5` `REE_assembly`, `[ahead 19, behind 47]`** -- same source, same
   composition, a **different box and a different repo**, so it is not a restatement of case 1.
   **Different.**
3. **2026-08-27, `DLAPTOP` umbrella, `[ahead 19] -> [ahead 179]` over ~14.7 h** -- recorded in
   this chip's own prompt by the repairing session `elated-nobel-914234`. Old: ~160 orphans
   accumulate and a human audits 179 commits one at a time. New: the growth does not happen.
   **Different**, and it is the largest measured instance of the latch.
4. **2026-08-18T07:28Z, `DLAPTOP` umbrella, `[ahead 26, behind 67]`, 11 unproven** --
   `umbrella_ref_convergence_wedge_recurrence_20260818.md` §2: "All 26 ahead commits ... were
   `chip_ledger.py` ... or `task_claim.py` ... writes." 100% of the range is in scope.
   **Different.**

**Negative controls (degenerate -- excluded, kept because they bound the change):**

* **A transiently-ahead, non-wedged checkout.** Old and new agree by construction. This is the
  entire point: the carrier argument that justified the gate is preserved exactly where it
  holds. If a change ever made these two disagree, that change is wrong.
* **2026-08-15, `ree-cloud-5`, 15 of 33 unproven genuinely stranded**, including 50 of 53
  lines of a `WORKSPACE_STATE.md` block (prior doc §7). `WORKSPACE_STATE.md` is not written by
  either of these two scripts' remote-tip path, so R1 changes nothing about that range, and
  `ref_convergence` still refuses. R1 must not be read as touching that case.

**Outcome recorded per GOV-HELDOUT-1: the check was run, found 4 differing cases and 2
degenerate controls, and it did change the proposal** -- an earlier draft of this
investigation proposed R3 as the primary fix; running the check surfaced that R1 has broad
measured support and R3 does not, and they swapped places.

### 7.2 R2 -- "`--audit` should not inherit the convergence bail"

1. **2026-08-14, `ree-cloud-5`, 43 ahead** (`ref_convergence.py` docstring): 40 proven, 3 not.
   One of the 3, `6ea3df15`, is a `WORKSPACE_STATE.md` line -- **non-registry, and genuinely
   not on origin**. Another, `5c05ebc9`, is registry-only with its content fully on origin.
   Old reports both unproven; new leaves only `6ea3df15`. **Different.**
2. **2026-08-27, `DLAPTOP`, 179 ahead**: the repairing session reports that its first audit
   pass missed stranded content living in worktree-session closing `WORKSPACE_STATE.md`
   entries -- non-registry -- alongside registry commits it landed structurally. Old gives an
   undifferentiated 179-commit list; new separates the registry-net-contained majority from
   the residue that actually needed the hand audit. **Different.**
3. **2026-08-28, this episode** (motivating -- listed for completeness, **not counted**):
   4 reported, 1 real.

**Negative control (degenerate):** the **2026-08-18 26-commit backlog** route C was built on.
Its residual was 1 (`lit-pull-q093-20260818`) and every unproven commit was registry-only, so
no non-registry commit existed to trigger the bail. Old and new give the identical answer.
This case tests nothing and is not counted.

**Outcome: 2 differing held-out cases + 1 named degenerate control. Below the bar of 3.**
Per GOV-HELDOUT-1 that is itself the finding: **R2 ships (if it ships) as scoped to the
audit-reporting path on ranges that mix registry and non-registry orphans, not as a general
principle**, and it must not be read as licence to touch the convergence path's bail.

### 7.3 R3 -- "do not commit a semantically empty ledger mutation"

Old = commit whenever the on-disk file differs from HEAD. New = commit only on a non-empty
intended item delta.

* **Differing, held-out (1):** the incident in `chip_ledger.py`'s own docstring (~line 1266) --
  a `record` that "had already recorded its chip -- rebased onto origin, adopted origin's
  unclaimed copy, and committed the reversion of `claimed_by`/`claimed_at`/`claim_note` under
  the message `chips: record chip-proposal-exp-0532`, while that cycle's worker (pid 2838454)
  was still live", causing a **real double-dispatch**. Empty intended delta, so new suppresses
  the commit and the reversion. **Different.**
* **Degenerate (2), and they are the ones that matter:** `6f10f014` (2026-08-15) and
  `58d2532e` (2026-08-18, the A-05 case in root `CLAUDE.md`). Both are regression sweeps --
  and both have a **non-empty** intended delta (`added=1` and `added=2` respectively), so R3
  would not have prevented either. Verified directly against the object store this session.
* **Census:** 0 zero-item-delta commits in the last 400 origin `TASK_CHIPS.json` commits (§4
  P1), because this shape never reaches origin.

**Outcome: 1 differing case against 2 degenerate ones. FAILS the >=3 bar, and the two
degenerate cases actively show the rule is narrower than the problem it was drafted for.**
Per GOV-HELDOUT-1 this is the finding: **R3 is scoped to its motivating incident.** It should
either ship with that stated explicitly, or -- better -- be replaced by the broader rule the
degenerate cases point at: *commit only the intended item-level delta against origin's current
copy, never the whole merged file.* That broader rule is what `claim_rescue.rescue_and_land`
already does on the rescue path and what `--to-remote-tip` does structurally, i.e. R1 is the
already-built version of it. **Do not ship R3 as a general rule on the strength of this
check.**

---

## 8. What was deliberately not done

* The live `DLAPTOP` wedge was **left exactly as found**, uncleared, as evidence, with the
  Orchestrator's agreement. No `safe_adopt_ref`, no `--allow-discard`, no lease, no ref move.
* No change to `ref_convergence`'s refusal semantics is proposed and no third proof route is
  proposed -- both out of bounds per the chip, and both still correctly rejected in the
  module's own docstring.
* The `SystemExit(1)` chip-mint failures of §5.3 were not diagnosed further;
  `chip-20260827-chipledger-lockfailopen-sweep-investigation` is live on that question.
* R1-R5 are proposals and findings. **Nothing in `scripts/` was modified by this session.**

## 9. Recommended follow-on chips

1. **Implement R1** (`chip_ledger` + `task_claim` remote-tip gate: ahead **and not wedged**),
   with tests alongside `test_task_claim_close_orphan_guard.py::
   test_an_ahead_only_orphan_is_also_withheld_but_self_corrects`, which pins the behaviour the
   gate exists for and must stay green. Highest value of anything here.
2. **Implement R2** (`--audit` skips the route-C bail), scoped per §7.2.
3. **R4** -- cover or reshape `chip_archive/<YYYY-MM>.json`.
4. **R5** -- wire `push_is_default()`'s non-fatal strand announcement into
   `reconcile_wedge_content.py` so a stranded commit is recorded durably instead of only
   printed.
5. **Re-measure the episode rate ~7 days after R1 lands**, normalised per 1000 origin commits
   (§5.2 gives the baseline: **2.8 per 1000**). R1 predicts episode *rate* roughly unchanged
   and episode *cost* (mean ahead-count at clearing, mean duration) sharply down. That is a
   falsifiable prediction and should be recorded as one.
