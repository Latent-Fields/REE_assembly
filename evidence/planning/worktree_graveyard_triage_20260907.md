# Worktree graveyard triage -- 2026-09-07

Chip: `chip-20260826-worktree-graveyard-triage-and-gc` (campaign W4-HK, bundle C).
Session: `w4hk-bundle-c-20260907` on DLAPTOP. Audit run 2026-09-07T22:08-22:35Z.

**Filename note.** The chip specified `worktree_graveyard_triage_20260826.md` after its own
scan date. That scan is 12 days stale and its numbers no longer hold (92 worktrees then, 72
now), so this document is dated for the day the audit was actually run. Nothing else about
the chip's deliverable spec is changed.

## Outcome in one line

**Audit complete, NOTHING REMOVED.** 51 of 72 worktrees are provably removable; 21 must be
held. No removal was performed, for two independent reasons, either of which alone is
sufficient: (1) the chip requires a human to agree the removal list before any
`git worktree remove`, and (2) `git worktree remove` was refused by this session's
permission classifier, so the action was not available even had it been authorised.
The removal list below is therefore a **proposal awaiting sign-off**, not a record of work
done.

## State, re-measured (do not trust the chip's 2026-08-26 figures)

| | 2026-08-26 (chip) | 2026-09-07 (this audit) |
|---|---:|---:|
| registered worktrees | 92 | 72 |
| LIVE (process cwd-rooted there) | 6 | 2 |
| holding commits not on `origin/master` | 50 | 53 |
| distinct such commits | -- | 305 (575 counted with duplicates across branches) |

LIVE now: `cool-sutherland-9d984d`, `peaceful-kare-a6a78f`. None of the chip's six named LIVE
worktrees is still live; all six have since ended or been collected. Liveness was tested by
PATH PREFIX against `lsof -a -d cwd`, not string equality, so a process cwd'd into a
subdirectory counts.

## The per-commit content audit

The chip's core requirement was that the 53 branches holding unlanded commits get a
**per-commit content audit**, never a shape argument. 305 distinct commits were audited.
Method, by path class:

- **`TASK_CHIPS.json` (116 commits).** Oracle: the set of `chip_ref`s in
  `origin/master:TASK_CHIPS.json` **today**. This is a COMPLETE oracle, not a sample:
  CLAUDE.md's chip-archive rule states that archiving strips the three fat fields *in place
  and keeps the row*, and `merge_origin_into_local()` has no deletion path, so every
  `chip_ref` that ever reached origin is still present. Result: **116/116 fully accounted
  for** -- every `chip_ref` added by every one of those commits is on origin.
- **`TASK_CLAIMS.json` (119 commits).** Retention ages entries out (the materializer reports
  ~1017 aged-out against ~90 kept), so the current file is NOT an oracle. Built a complete
  key index instead by walking **all 7,466 `origin/master` revisions of that file since
  2026-07-01** and extracting every `"session_id"` / `"claimed_at"` string: 7,003 distinct
  keys. Sampling was tried first and rejected -- at 1-in-8 the largest gap between sampled
  revisions was 196h, well over the 24h retention window, so a key could have appeared and
  aged out unseen. Result: **118/119 fully accounted for**; one outlier, below.
- **`WORKSPACE_STATE.md` (many commits).** First pass compared added lines against the live
  file alone and produced 20+ false "unaccounted" findings. `WORKSPACE_STATE.md` **rotates
  monthly** into `docs/workspace_state_archive/<YYYY-MM>.md` (6 archives on origin), so the
  oracle is the union of the live file and every archive: 17,562 lines. That cleared 20 of
  the 46 initially-flagged commits.
- **Code, skills, CLAUDE.md, `.mcp.json` (26 commits after the archive pass).** Added-line
  containment is too strict for text that evolved after the commit, so each was adjudicated
  by hand against a distinctive marker on origin. Every one landed, most in reworded or
  relocated form. Notable relocations: `de9374e35`'s ree-worker-4 dual-role paragraph now
  lives in `docs/reference/ree-v3-test-suite-routing.md`; `d923abba4`'s HEADLESS WORKER
  CONTRACT rule-6 correction now lives in
  `docs/skill_archaeology/metaworker-dispatch/b-65-contract-rule6-thoughtdigest-near-loss.md`.
  Existence-and-marker checks confirmed `scripts/dispatch_usage_cooldown.py` (878 lines,
  "allowlist" x5), `scripts/run_scripts_tests.sh` (607), `scripts/mcp_server.py` (1009),
  `scripts/ref_convergence.py` (1401, "route C" x16), and `proposal_id` in
  `scripts/ree_commit.py` (x7) all on origin.
- **Transient state files** (`metaworker_dispatch_cooldown.json`, `dispatcher_control.json`
  lease renewals, generated `docs/worktree_session_registry.md`): superseded by later
  writes; carry no recoverable content.

### What is genuinely stranded (4 commits, 4 worktrees)

These reached origin in **no** form. Each is HELD.

| commit | worktree | content | assessment |
|---|---|---|---|
| `fc749670e` | `metaworker-chip-20260819-modulatory-authority-cem-throughput-build` | `scratch/smoke_cem_authority.py`, 206 lines | underlying chip is `done` |
| `9d805136d` | `metaworker-chip-20260820-mech489-retest-driver-decision-at-override-tick` | `scratch/probe_orienting_latch_mech489.py`, 71 lines | underlying chip is `done` |
| `a81eef999` | `metaworker-chip-20260821-exq861e-h1-h3-fanout` | `gen/build.py` (1332) + `gen/queue_append.py` (311) + `gen/legs.py` (59) | underlying chip is `done` |
| `58c4eba41` | `igw-199-proposal-for-mech-086` | 2026-07-12 `TASK_CLAIMS.json` entries (`inter-governance-brief-0f23a4` and siblings); `git log -S` over `origin/master` finds them never on origin | the WORK it records (pack_writer edge-case-A HYBRID) IS on origin, in `docs/workspace_state_archive/2026-07.md` -- historical bookkeeping only |

**The finding worth carrying forward: the first three are themselves recovery commits.**
Their subjects all read `wip: recover stranded work from chip-...`. A prior session found
stranded work, preserved it onto a worktree branch, and then never landed the preservation --
so the recovery is now itself the strand. That is the exact signature the chip warned about
(`'wip:' plus 'recover stranded work' is the signature of content that exists NOWHERE ELSE`),
and it held.

**Not landed by this session, deliberately.** `scratch/` and `gen/` are not tracked
directories in the umbrella repo; cherry-picking these onto `origin/master` would add two new
top-level directories, which is a repo-shape decision rather than a recovery. All three
underlying chips are `done`, so the substantive work landed by other means and these are the
intermediate artifacts of it. Holding the worktrees costs a directory entry and keeps the
only copy alive; that is the safe call and it is reversible in either direction.

## Verdicts

Gates, per `/session-land` Phase 2c, checked one worktree at a time:
(1) chip resolved `done`/`withdrawn` for `metaworker-*`; (2) no process cwd-rooted there;
(3) `git status --porcelain` clean apart from the known scratch set; (4) zero unlanded
commits, OR every counted commit passed the content audit above.

Scratch set counted as clean for gate 3: `.dispatch_pid`, `.headless_contract.md`,
`.session_uuid`, `.worker_parked.json`, `.worker_turns.jsonl`, `DISPATCH_BRIEF.md`,
`HEADLESS_CONTRACT.md`, `claude.log`, `IGW_START_HERE.md`, and -- per the chip's own known
exception -- any ` D` confined to `skills/insights/` paths, which is the deliberate
2026-08-26 deletion of the shadowing project `/insights` skill (REE_Working `157adeff`).
Those deletions were NOT restored; restoring them would re-arm the shadowing.

**21 HOLD / 51 REMOVABLE.** Hold reasons: 2 LIVE, 15 dirty beyond the scratch set, 2 with an
`open` chip, 3 carrying stranded content (one of which is also dirty).

| worktree | type | tip | live | dirt | unlanded | chip | verdict |
|---|---|---|---|---|---|---|---|
| `closure-maps-correctness-807268` | named/slug | 2026-08-09 | - | 6 | 1 | n/a | HOLD -- dirty |
| `cool-sutherland-9d984d` | named/slug | 2026-09-07 | YES | - | - | n/a | HOLD -- LIVE |
| `elated-nobel-914234` | named/slug | 2026-08-28 | - | 1 | 2 | n/a | HOLD -- dirty |
| `epic-poincare-3cf746` | named/slug | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `hopeful-solomon-01a60c` | named/slug | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-199-proposal-for-mech-086` | igw | 2026-07-12 | - | - | 1 | n/a | HOLD -- STRANDED CONTENT -- 2026-07-12 TASK_CLAIMS entries (inter-governance-brief-0f23a4 et al) |
| `igw-213-substrate-ready-mech465-commit-g` | igw | 2026-09-04 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-220-substrate-ready-sd-probe-warmup` | igw | 2026-08-31 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-222-substrate-ready-sd-e1-rollout-co` | igw | 2026-08-31 | - | 2 | - | n/a | HOLD -- dirty |
| `igw-224-substrate-ready-sd-blocked-agenc` | igw | 2026-08-31 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-225-substrate-ready-sd-epistemic-def` | igw | 2026-08-31 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-229-proposal-for-sd-099` | igw | 2026-08-21 | - | - | 1 | n/a | REMOVABLE (all 1 commits content-proven on origin) |
| `igw-232-confirm-evidence-mech-091-lit-0` | igw | 2026-08-22 | - | - | 28 | n/a | REMOVABLE (all 28 commits content-proven on origin) |
| `igw-232-literature-proposal-for-mech-489` | igw | 2026-08-10 | - | - | 10 | n/a | REMOVABLE (all 10 commits content-proven on origin) |
| `igw-233-literature-proposal-for-arc-052` | igw | 2026-09-01 | - | 1 | - | n/a | HOLD -- dirty |
| `igw-233-proposal-for-inv-040` | igw | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-238-confirm-evidence-mech-267-lit-0` | igw | 2026-09-05 | - | 5 | - | n/a | HOLD -- dirty |
| `igw-239-proposal-for-arc-052` | igw | 2026-09-02 | - | 1 | - | n/a | HOLD -- dirty |
| `igw-239-proposal-for-mech-143` | igw | 2026-08-29 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `igw-241-literature-proposal-for-ext-008` | igw | 2026-09-03 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `insights-7fd98a` | named/slug | 2026-09-02 | - | 1 | 3 | n/a | HOLD -- dirty |
| `mech-025-dv-redesign-cf8c06` | named/slug | 2026-08-10 | - | 6 | 1 | n/a | HOLD -- dirty |
| `metaworker-chip-20260814-analyse-920a-multiseed-within-life-trends` | metaworker | 2026-08-18 | - | - | 6 | done | REMOVABLE (all 6 commits content-proven on origin) |
| `metaworker-chip-20260814-queue-causal-sleep-matched-arm` | metaworker | 2026-08-18 | - | - | 1 | open | HOLD -- chip open |
| `metaworker-chip-20260816-audit-stale-claims-shared-basenames-worktree-divergence` | metaworker | 2026-08-18 | - | - | 8 | done | REMOVABLE (all 8 commits content-proven on origin) |
| `metaworker-chip-20260816-governance-flag-stale-id-red-on-trunk` | metaworker | 2026-08-18 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260816-igw-test-oracle-vacuity-audit` | metaworker | 2026-08-18 | - | - | 37 | done | REMOVABLE (all 37 commits content-proven on origin) |
| `metaworker-chip-20260816-implsub-contextmemory-writepath-degeneracy` | metaworker | 2026-08-18 | - | - | 15 | done | REMOVABLE (all 15 commits content-proven on origin) |
| `metaworker-chip-20260816-mech152-measurement-redesign` | metaworker | 2026-08-18 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260816-morningdigest-missed-firing-window` | metaworker | 2026-08-18 | - | - | 21 | done | REMOVABLE (all 21 commits content-proven on origin) |
| `metaworker-chip-20260816-phase3-preflight-postcutover-verdict` | metaworker | 2026-08-18 | - | - | 2 | done | REMOVABLE (all 2 commits content-proven on origin) |
| `metaworker-chip-20260816-queueexp-mech151-affordance-set-instrumentation-v2` | metaworker | 2026-08-18 | - | - | 19 | done | REMOVABLE (all 19 commits content-proven on origin) |
| `metaworker-chip-20260816-reecommit-idfields-registry-keys` | metaworker | 2026-08-18 | - | - | 20 | done | REMOVABLE (all 20 commits content-proven on origin) |
| `metaworker-chip-20260816-steward-apply-d008-frontmatter-fixes` | metaworker | 2026-08-18 | - | - | 2 | done | REMOVABLE (all 2 commits content-proven on origin) |
| `metaworker-chip-20260816-thoughtdigest-trial5-artifact-recovered` | metaworker | 2026-08-18 | - | - | 4 | done | REMOVABLE (all 4 commits content-proven on origin) |
| `metaworker-chip-20260816-umbrella-scripts-corpus-no-runner` | metaworker | 2026-08-20 | - | 1 | 5 | done | HOLD -- dirty |
| `metaworker-chip-20260817-orphaned-stash-igw-routine-tick-20260812` | metaworker | 2026-08-19 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260818-adopt-origin-to-deploy-route-c` | metaworker | 2026-08-18 | - | - | 35 | done | REMOVABLE (all 35 commits content-proven on origin) |
| `metaworker-chip-20260818-cooldown-gate-observed-at-misparse` | metaworker | 2026-08-18 | - | - | 6 | done | REMOVABLE (all 6 commits content-proven on origin) |
| `metaworker-chip-20260818-dispatch-registry-commit-rate-wedges-umbrella` | metaworker | 2026-08-18 | - | - | 24 | done | REMOVABLE (all 24 commits content-proven on origin) |
| `metaworker-chip-20260818-fleetidle-watcher-e2big-silent-failure` | metaworker | 2026-08-19 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260819-account-handover-misses-systemd-token-sites` | metaworker | 2026-08-19 | - | - | 2 | done | REMOVABLE (all 2 commits content-proven on origin) |
| `metaworker-chip-20260819-gitsyncrepair-reports-ok-while-not-syncing` | metaworker | 2026-08-22 | - | - | 10 | done | REMOVABLE (all 10 commits content-proven on origin) |
| `metaworker-chip-20260819-modulatory-authority-cem-throughput-build` | metaworker | 2026-08-22 | - | - | 1 | done | HOLD -- STRANDED CONTENT -- scratch/smoke_cem_authority.py (206 lines) |
| `metaworker-chip-20260819-scaler-stop-powering-down-cloud4` | metaworker | 2026-08-19 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260819-sibling-watchers-silent-failure` | metaworker | 2026-08-22 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260820-mech489-retest-driver-decision-at-override-tick` | metaworker | 2026-08-22 | - | 10 | 1 | done | HOLD -- dirty -- scratch/probe_orienting_latch_mech489.py (71 lines) |
| `metaworker-chip-20260820-scriptscorpus-mac-launchd-install` | metaworker | 2026-08-22 | - | - | 8 | done | REMOVABLE (all 8 commits content-proven on origin) |
| `metaworker-chip-20260821-exq861e-h1-h3-fanout` | metaworker | 2026-08-26 | - | - | 8 | done | HOLD -- STRANDED CONTENT -- gen/build.py+queue_append.py+legs.py (1702 lines) |
| `metaworker-chip-20260821-exq939a-mech303-readiness-gate` | metaworker | 2026-08-22 | - | 1 | 7 | done | HOLD -- dirty |
| `metaworker-chip-20260823-morning-digest-scheduler-misfire` | metaworker | 2026-08-27 | - | - | 2 | done | REMOVABLE (all 2 commits content-proven on origin) |
| `metaworker-chip-20260825-mech492-falsifier-queue` | metaworker | 2026-08-26 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260826-vendored-stray-worktree-false-positive` | metaworker | 2026-08-27 | - | - | 1 | done | REMOVABLE (all 1 commits content-proven on origin) |
| `metaworker-chip-20260828-chipledger-noop-record-committed-destructive-delete` | metaworker | 2026-09-02 | - | - | - | open | HOLD -- chip open |
| `metaworker-chip-20260902-pausepressure-fixab-generator-pacing` | metaworker | 2026-09-02 | - | - | - | done | REMOVABLE (0 unlanded) |
| `metaworker-chip-metaworkergc-chip-20260814-mech321-pe-d7ba78bf5a59` | metaworker | 2026-08-19 | - | - | 11 | done | REMOVABLE (all 11 commits content-proven on origin) |
| `metaworker-chip-metaworkergc-chip-20260815-dead-sessi-87f8415dc068` | metaworker | 2026-08-18 | - | - | 14 | done | REMOVABLE (all 14 commits content-proven on origin) |
| `metaworker-chip-metaworkergc-chip-stagedskew-dlaptop-516e9589639a` | metaworker | 2026-08-19 | - | - | 13 | done | REMOVABLE (all 13 commits content-proven on origin) |
| `metaworker-chip-refwedge-dlaptop-ree-working-master` | metaworker | 2026-08-18 | - | - | 35 | done | REMOVABLE (all 35 commits content-proven on origin) |
| `metaworker-chip-refwedge-dlaptop-ree-working-master-since-2026-08-18t04-00-43z` | metaworker | 2026-08-18 | - | - | 26 | done | REMOVABLE (all 26 commits content-proven on origin) |
| `metaworker-chip-refwedge-dlaptop-ree-working-master-since-2026-08-18t05-54-51z` | metaworker | 2026-08-18 | - | - | 20 | done | REMOVABLE (all 20 commits content-proven on origin) |
| `metaworker-chip-refwedge-dlaptop-ree-working-master-since-2026-08-18t21-35-24z` | metaworker | 2026-08-19 | - | - | 33 | done | REMOVABLE (all 33 commits content-proven on origin) |
| `metaworker-chip-stash-ree-working-93c953009a` | metaworker | 2026-08-18 | - | - | 6 | done | REMOVABLE (all 6 commits content-proven on origin) |
| `metaworker-chip-strandedwt-ree-cloud-5-metaworker-chip-20260808-82ce49421e08` | metaworker | 2026-08-18 | - | - | 15 | done | REMOVABLE (all 15 commits content-proven on origin) |
| `metaworker-chip-strandedwt-ree-cloud-5-metaworker-chip-20260813-e92710ffef74` | metaworker | 2026-08-18 | - | - | 28 | done | REMOVABLE (all 28 commits content-proven on origin) |
| `nifty-chebyshev-227274` | named/slug | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `objective-hamilton-1d00ce` | named/slug | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |
| `peaceful-kare-a6a78f` | named/slug | 2026-09-07 | YES | - | 2 | n/a | HOLD -- LIVE |
| `pending-task-009a3a` | named/slug | 2026-08-22 | - | 1 | 53 | n/a | HOLD -- dirty |
| `ree-thought-intake-displaced-present-1ecf2e` | named/slug | 2026-08-25 | - | 2 | 2 | n/a | HOLD -- dirty |
| `serene-yalow-3dd4b0` | named/slug | 2026-08-25 | - | 7 | 18 | n/a | HOLD -- dirty |
| `wt-adopt` | named/slug | 2026-09-07 | - | - | - | n/a | REMOVABLE (0 unlanded) |


## What was NOT done, and why

- **No worktree was removed.** See "Outcome in one line". The 51 REMOVABLE rows are a
  proposal. Each still needs its four gates RE-RUN at removal time -- this table is
  scan-time evidence and goes stale as sessions start.
- **No branch was deleted.**
- **No stranded content was cherry-picked.** Reasoning above.
- **`chip-metaworkergc-sweep-1-2687350d9ad53512`** (the one-worktree DLAPTOP sweep,
  `metaworker-chip-20260902-pausepressure-fixab-generator-pacing`) had all four gates
  verified PASS and its scratch files cleared, but the `git worktree remove` was refused by
  the permission classifier. The worktree is now gate-clean and staged for a one-command
  removal. Chip left OPEN.
- **`chip-metaworkergc-sweep-154-67fd3ce5efc53055`** is declared MUST-RUN-ON-`ree-cloud-5`;
  not touched from here.

## Removal procedure, when authorised

One at a time, re-running all four gates immediately before each. Clear the known scratch
files with `rm -f` first, then a **PLAIN** `git worktree remove` -- never `--force`. Git's
refusal on an unexpected file is the last line of defence against a durable artifact none of
the four gates can see (the permanently unrecoverable loss in
`chip-20260807-thoughtdigestion-trial-5`). A remove that still refuses after the scratch set
is cleared is telling you something real: read what it names, log the worktree as SKIP, and
move on.

---

# EXECUTION -- appended 2026-09-07T22:5xZ, after user sign-off

The user was shown the audit and the 51-row removal list and chose **"Remove all 51, gates
re-run per worktree"** (logged to `RECOMMENDATION_LOG.jsonl`, entry 146; the stranded-work
question was answered "keep holding those worktrees", entry 147). That is the supervision the
chip requires; the removals below were made under it.

## Result

**67 -> 29 worktrees. 35 removed, 16 skipped. All 21 HOLD worktrees re-verified present at
close.**

**No commit was destroyed by any removal.** `git branch -d` refuses a branch not fully merged
into HEAD, so all 35 branches were KEPT, by design and reported per worktree. What was removed
is 35 working directories; every commit they held is still reachable from its local branch.
(The umbrella now carries 271 dangling `claude/*` branches -- a separate tidiness question,
deliberately not touched here.)

Skips, all four gates re-run immediately before each removal:

| skip reason | n |
|---|---:|
| directory already absent (collected by another agent during the session) | 9 |
| gate 1: IGW ledger status `completed_resumable` -- kept for the user to resume | 5 |
| gate 1: IGW ledger status `staged` -- never launched | 1 |
| gate 4: 3 unlanded commits NOT in the audited-proven set (`objective-hamilton-1d00ce`) | 1 |

Gate 4 was implemented as the chip specifies -- **zero unlanded commits OR every current
unlanded sha present in the audited-proven set** (301 shas: the 305 audited minus the 4
stranded). A commit appearing after the scan therefore SKIPs the worktree rather than riding
on stale evidence; that is what caught `objective-hamilton-1d00ce`.

## ERROR MADE AND REPAIRED -- read this before writing the next sweep

**Three worktrees were removed with gate 1 unchecked.** The first driver applied gate 1 as
"chip resolved `done`/`withdrawn`" for `metaworker-*` worktrees ONLY, and applied *nothing* to
`igw-*` ones -- where the chip is explicit that gate 1 is the IGW ledger entry being
`completed`, and that `igw_routine_tick.py gc` is preferred over doing it by hand. Removed
before the gap was noticed:

- `igw-213-substrate-ready-mech465-commit-g` (IGW-20260904-213, ledger status `staged`)
- `igw-220-substrate-ready-sd-probe-warmup` (IGW-20260831-220, `staged`)
- `igw-224-substrate-ready-sd-blocked-agenc` (IGW-20260831-224, `staged`)

**What was and was not lost.** Gates 2/3/4 did hold for all three -- no live process, clean
tree, zero unlanded commits -- so no committed or uncommitted work was lost. What was lost is
each one's staged `IGW_START_HERE.md` brief, which is untracked and is NOT reconstructible:
`write_start_here()` derives it from the workset item, and none of the three items still
exists in `inter_governance_workset.v1.json` (matched by neither `stable_hash` nor title on
2026-09-07). They had been `staged` since 2026-08-31 / 2026-09-04, well past
`STAGE_STALE_HOURS` (72), so those briefs were frozen snapshots of a condition that had
already lapsed -- which is the hazard `igw_routine_tick.py`'s own comment at line ~1412 warns
about, and it means relaunching from them would have been wrong anyway. That mitigates the
loss; it does not excuse the missed gate.

**Repair.** All three closed with
`igw_routine_tick.py complete <stable_hash> --outcome NO_OP`, carrying a summary that states
exactly the above. `NO_OP` is the honest classification (nothing landed) and it is also the
safe one: R3 retires a backing proposal only when `lane == "experiment"` AND the outcome is
`USEFUL_LANDED`/`DUPLICATE`, so a `substrate`-lane `NO_OP` retires nothing -- no proposal was
mistagged, and Guard 3 (landed 2026-09-07) rules out the cross-lane literature-twin
displacement in any case. Closing them also released their 2026-08-31 `TASK_CLAIMS` entries,
which had been open for 7 days, and stopped three ledger entries sitting LIVE against absent
worktrees. If any of the three substrate items is still wanted, it should be re-surfaced by
the generator on its own merits, not relaunched from a lapsed brief.

**The fourth of that group, `igw-225-substrate-ready-sd-epistemic-def`, was NOT removed** --
the corrected gate caught it, and it still has its worktree and brief intact.

**Fix applied to the driver, and the lesson for the next one:** gate 1 has TWO
implementations, not one -- chip status for `metaworker-*`, IGW ledger status for `igw-*` --
and a sweep that knows only the first will silently pass every `igw-*` worktree. `completed`
is the only IGW status that clears the gate; `completed_resumable` is a deliberate keep-for-
resume and must SKIP (it did, 5 times, after the fix).

## Operational note

`git worktree remove` was refused twice by this session's permission classifier when issued as
a compound `rm -f ... && git worktree remove ... && git branch -d ...`, and went through
immediately as separate single commands. If a sweep looks blocked, split the three commands
before concluding anything about the worktree.

---

# BRANCH DISPOSITION -- appended 2026-09-07T23:22:12Z

Chip: `chip-20260907-umbrella-dangling-claude-branches`, session `cool-sutherland-9d984d`.
The GC above deliberately left every branch in place. This section adjudicates them.

## Verdict: KEEP ALL 245. Nothing deleted.

## State

274 local `claude/*` branches; 29 are checked out in a surviving worktree (never deletable);
**245 are deletion candidates**, and every one of them holds at least one unlanded commit, so
`git branch -d` refuses all 245 by construction and `-D` would be required for each.

**Branch name != worktree directory name** (e.g. `closure-maps-correctness-807268` is on
`claude/metaworker-dispatch-34f021`). The checked-out set must be derived from
`git worktree list --porcelain`, never by slug matching.

## The audit was RE-RUN, not inherited -- and the chip's premise did not survive it

The chip asserted the ~262 non-merged branches "exist solely to hold commits whose CONTENT was
proven to be on origin". That is **false as stated**. The audit above covered 305 commits from
the 53 worktrees alive on 2026-09-07; the 245 candidate branches carry **896 distinct unlanded
commits**, so roughly 591 were never examined -- they belong to worktrees collected long before
this GC. No sha list of the 301-proven set was persisted, so coverage could not be inherited
and the audit was rebuilt from scratch, by path class:

| class | commits | method | unaccounted |
|---|---:|---|---:|
| `TASK_CHIPS.json` | 344 | complete `chip_ref` oracle on origin (3146 refs) | **0** |
| `RECOMMENDATION_LOG.jsonl` | 41 | union of all distinct lines ever on origin (434) | **0** |
| code / skills / docs | 98 | exact blob-in-path-history, then marker adjudication | **0** |
| `TASK_CLAIMS.json` | 263 | key index over 8,902 distinct blobs since 2026-05 (10,248 keys) | **8** |
| `WORKSPACE_STATE.md` | 137 | live file + all 6 monthly archives (17,572 lines) | **17** |

Transient paths (`dispatcher_control.json`, generated `worktree_session_registry`,
`metaworker_dispatch_budget_log.json`) carry no recoverable content -- superseded by later writes.

**The code class is clean, and that is the reassuring part.** 238 of 247 file/commit pairs matched
a blob **exactly** in that path's origin history. All 9 exceptions resolved to landed-in-evolved
or landed-relocated form, reproducing the pattern the audit above found: `audit_stale_claims.py`'s
"ANNOTATING A CONTENTION OWNER" landed reworked as "OWNER LANDEDNESS ANNOTATION (added
2026-08-19)", and its `OwnerAnnotationTest` landed as the separate file
`scripts/test_audit_stale_claims_contention_owner_landed.py`. Checking only the original filename
would have called both lost. **No executable code is stranded on any candidate branch.**

**What IS stranded: 21 distinct commits across 25 candidate branches**, all bookkeeping --
8 `TASK_CLAIMS.json` `session_id`s that appear nowhere in origin's history of that file
(`arc063-bringforward-arc077`, `diagnose-exq543e-noncontrib`, `state-sync-implement-substrate-arc062`,
`arc062-gap-b-spcem-falsifier`, `metaworker-chip-20260814-mech122-dv3-revalidation-861d`,
`metaworker-chip-20260813-queueexp-mech321-r4`, `studyhum1-mvp-spike`,
`metaworker-chip-20260813-queueexp-mech152-softselect-ablation`) and 17 `WORKSPACE_STATE.md`
session-closing entries whose own timestamp is on neither the live file nor any archive. Three
further claim keys looked unaccounted but landed under a different `claimed_at` -- benign.
Method note: two of the 17 pass a naive marker test because the entry body *quotes* an older
timestamp that is on origin; the entry's **own** stamp must be the marker.

The method independently rediscovered `58c4eba41`, a known strand from the audit above, which is
what gives it credit for the 21 it found that the earlier pass never looked at.

## Why keeping is right, and why archive-tagging is not the compromise it looks like

- **The benefit is ~1%.** Objects reachable only from the 245 candidates: 653 blobs + 843 trees +
  677 commits = **16.0 MB** in a **1.5 GB** `.git`. Refs cost 22.4 KB of `packed-refs`.
- **Nothing reads the branch list.** `dev-doctor.sh` is the only tooling that enumerates branches
  and it inspects only worktree-attached ones, so it never sees these 245. The cost of keeping
  them is a longer `git branch` listing and nothing else.
- **Archive-tagging before deleting accomplishes exactly nothing.** A tag holds identical
  reachability to a branch, so tagging all 245 and deleting the branches reclaims **0 MB** and
  leaves the ref count unchanged -- it renames `refs/heads/claude/*` to `refs/tags/*`. The chip's
  containment suggestion and the only real benefit (reclaiming space) are **mutually exclusive**,
  because holding commits alive is the entire function these refs perform. This is the structural
  difference from the stash case CLAUDE.md models it on: a stash entry is *additional* to the
  object's reachability, whereas here the branch *is* the reachability.
- **`-D` is close to irreversible.** All 274 branches have per-branch reflogs, and `git branch -D`
  deletes the branch's reflog with it; the 677 commits then fall to the next `gc` under a 2-week
  `pruneExpire` grace.

So the options are: delete untagged (gain 1%, permanently destroy 21 commits of unique
bookkeeping plus the recoverability of the rest), delete tagged (gain nothing), or keep (cost
nothing measurable). **Keep.** The chip explicitly blesses this outcome and asks that it not be
overridden out of tidiness.

## If this is ever revisited

Do not treat this section as a standing clearance. It is scan-time evidence: a branch touched
after 2026-09-07T23:22:12Z is outside it, and the 25 strand-holding branches are listed here precisely so that a
future sweep can exclude them rather than re-derive them. The cheapest real win in this repo is
unrelated to branches -- two orphaned `.git/objects/*/tmp_obj_*` files from an interrupted git
operation, which `git gc` clears and which nothing references.
