# chip-strandedwt class: worker scratch has no declared home -- root-cause pass

**Status: DECIDED 2026-09-20T10:16Z (user: build option B, the attested `.scratch/` design) -- BUILT, REE_Working `b5baac013` on origin/master.**
Build note: the GOV-HELDOUT-1 re-check against the final wording caught one over-claim in section 4 -- row 5 (nested worktree under the scratch dir) would still have chipped under the staged text, because a ree-v3 checkout (~2730 files) exceeds the fail-closed 500-entry walk cap; contract rule 6a therefore also tells the worker to `git worktree remove` a nested throwaway worktree before attesting. The `_scratch/` blind spot (2g) was NOT built. The body below is unchanged from the staged version.

- Written: 2026-09-20T10:04:13Z, `/metaworker-learning`, session `ml-strandedwt-scratch-contract-20260920`
- Work chip: `chip-20260920-ml-strandedwt-worker-scratch-contract-rootcause`
- Routed by: user decision 2026-09-20T09:36Z on `chip-20260920-ml-strandedwt-worker-scratch-in-worktree-root`
- Nothing is changed by this document. No script, skill, brief or CLAUDE.md text was edited.

## 1. Recurrence is genuine (Step 1)

`TASK_CHIPS.json` on the Mac main checkout, 2026-09-20T10:00Z: **113** `chip-strandedwt-*`
chips (74 Aug, 39 Sep; 104 done, 7 withdrawn, 2 open). Threshold is 2.

Every chip's `UNCOMMITTED PATHS` block was parsed (archived prompts read through
`chip_ledger.archived_field`) and each flagged path classified by shape:

| Flagged-path shape | Aug | Sep | What fixed / explains it |
|---|---|---|---|
| harness files only (`.headless_contract.md`, `.session_uuid`, `.launch.sh`, ...) | 40 | 5 | detector exemptions `ede1b6700` (08-27), `d82e75808` (08-30), `6a19e21e9` (09-03) |
| harness + root file / tracked tree | 5 | 0 | same |
| registry files (`TASK_CHIPS.json` / `TASK_CLAIMS.json`), alone or with a root file | 5 | 8 | `_registry_rows_subsumed` (08-30); 2 of the Sep ones were TRUE positives |
| skill-sync residue | 0 | 2 | false positive, separate class |
| tracked-tree modification (` M scripts/...`) | 4 | 0 | **the confirmed real-loss shape (2026-08-15)** |
| **worker-made root files** | 15 | 7 | **nothing -- this document** |
| **worker-made scratch-like directory** (`scratch/`, `.scratch/`, `scratch_<id>/`, `wip/`) | 5 | 17 | **nothing -- this document** |

So the two prior learning fixes did what they claimed: the harness-file class fell from
45 to 5. What is left, and growing, is **worker-made scratch: 20 in Aug, 24 of 39 in Sep
(62%)**. It is one root cause, not the one the earlier fixes addressed.

## 2. Measured mechanism

**(a) No text anywhere tells a dispatched worker where scratch goes.** Checked:
`scripts/dispatch_remote_launch.py` (carries no brief prose at all; sets cwd = worktree
root, L565), `scripts/dispatch_campaigns.py` `render_science_brief` (L877) and
`render_bundle_brief` (L1028), and the HEADLESS WORKER CONTRACT in
`.claude/skills/metaworker-dispatch/SKILL.md` (L1626-1834). The words scratch / tmp / probe
appear in none of the brief renderers. Contract rule 6 says where DURABLE artifacts go
(tracked path, committed and pushed) and that the worktree "is scratch space that something
will eventually remove" -- it never says where throwaway files go.

**(b) The only placement rule a worker can find points INTO the worktree.** CLAUDE.md
"Python": never `/tmp`; "put scratch scripts under the current worktree". A worker whose cwd
is the worktree root complies by writing there. The raising Healer's hypothesis is confirmed.

**(c) Workers already want a scratch directory and each invents its own.** Of the 24
September worker-scratch findings, 17 are directory-shaped: `scratch_<id>/` x7, `scratch/` x5,
`.scratch/` x5 (one worktree also used `wip/`); bare worktree root x7
(`b1..b8.py`, `mk2..mk7.py`, `.append_q.py` ..., `smoke2.log`, `check.out`,
`decision_prompt.txt`). Roughly 70% pick a directory unprompted. The contract gap is a
missing NAME, not a missing instinct.

**(d) The finding fires on a worker that closed cleanly.** For all nine chip-dispatched
September instances the worker's own chip was resolved `done` 6.0-6.5 h before the strand
chip was raised -- i.e. exactly `STRANDED_MIN_IDLE_HOURS` after a clean close. The detector
is not catching workers that died; it is catching workers that finished and left their
probes behind, which nothing told them not to do.

**(e) The scratch was scratch.** Adjudicated September scratch instances (Healer notes):
every one was "worthless / findings already landed" or a "rescue" of content that was not
owed to master. The one that looked like a real rescue is not: for
`chip-20260910-gflag0246-exq900-flat-benefit-autopsy` the Healer committed `.scratch/`
drafts to a `claude/*` branch as "NOT landed to master", but the worker had landed the
finals 7 h earlier (REE_assembly `22d1bf1564`). Checked here line-for-line: both rescued
drafts (304 and 267 lines) have **zero** lines absent from the landed
`failure_autopsy_V3-EXQ-900_2026-09-14.md` / `redteam_failure_autopsy_...md`. Three
auto-resolved instances (exq-1023, mech465, exq-1026) carry no verdict and are excluded.
Two root-level findings docs (`EXQ1056_FINDINGS.md` 4.6 KB, `redteam_findings.md` 15 KB)
were rescued to branches and NOT checked against master here -- they are the closest thing
to real work in the sample, and they were in the ROOT, not in a scratch directory.

**(f) The detector sees a directory as one undecidable line.** `_worktree_uncommitted_entries`
runs `git status --porcelain -z` with no `-uall`, so `scratch/` is one `??` entry;
`_path_content_is_elsewhere` returns `None` for a directory, so it is always kept;
`_is_metaworker_scratch` is an exact whole-string filename match with no directory support.

**(g) LATENT BLIND SPOT, found in passing.** The umbrella `.gitignore` already ignores
`/_scratch/` (`b77077b6c`, 2026-09-08, for the main checkout's session scratch). The
detector does not pass `--ignored`, so a worker that happens to name its directory
`_scratch/` is **invisible** to the stranded-work source today. One Mac worktree
(`igw-233-...`) has such a directory; the cloud boxes were not reachable by hostname from
this session and are unmeasured. This matters for the design: "use the existing gitignored
directory" is the obvious cheap fix and it is the wrong one (section 3, option D).

## 3. Options

| | Contract change | Detector change | Blind spot |
|---|---|---|---|
| **A** | name `.scratch/`; delete it as the last act of a clean close | none | none -- but a headless worker runs an irreversible `rm -rf`, and a deliverable mis-filed in scratch is destroyed rather than flagged |
| **B (recommended)** | name `.scratch/`; at clean close write an attestation file into it | drop `?? .scratch/` **only if** the attestation exists and nothing in the directory is newer than it | only a false attestation by a worker that also closed cleanly |
| **C** | name `.scratch/` | exempt the directory unconditionally | a worker that dies before landing, with its draft in scratch, is never surfaced -- the 2026-08-15 shape, relocated |
| **D** | tell workers to use gitignored `_scratch/` | none | same as C, and already silently true today (2g) |

### Option B, concretely

**Contract** -- one new rule in the HEADLESS WORKER CONTRACT
(`.claude/skills/metaworker-dispatch/SKILL.md`, mirrored to `.agents/skills/`), and one
sentence pointing at it in `render_science_brief` and `render_bundle_brief`:

> SCRATCH. Every throwaway file you create -- probe scripts, patch helpers, smoke logs,
> draft prompts, nested throwaway worktrees -- goes under `.scratch/` in your worktree root,
> and nowhere else in the worktree. Never `/tmp`. A deliverable (findings doc, autopsy,
> design note, anything a later session would want) is NEVER scratch: it goes to its tracked
> path, committed and pushed, under rule 6. As the LAST act of a clean close, after you have
> verified every deliverable on origin, write `.scratch/SCRATCH_DISPOSABLE` containing one
> line per deliverable (`<repo> <sha> <path>`). Do not write it if anything is unlanded, and
> do not write anything into `.scratch/` after it.

**CLAUDE.md "Python"** -- "under the current worktree" gains "(`.scratch/` for a dispatched
headless worker -- see the HEADLESS WORKER CONTRACT)". The `/tmp` prohibition and the
stdlib-name rule are unchanged and still apply inside `.scratch/` (a `.scratch/json.py`
shadows `json` for anything run from that directory).

**Detector** -- `scripts/hygiene_routine_tick.py`: a new predicate next to
`_is_metaworker_scratch`, used only by `_stranded_worktree_findings` (NOT by
`_git_worktree_is_dirty` / GC, whose exemption semantics are different and documented as
such at L2147):

- entry path is exactly `.scratch/` (untracked directory), and
- `.scratch/SCRATCH_DISPOSABLE` exists, and
- no file under `.scratch/` has an mtime newer than the attestation (reuse
  `_newest_mtime`'s capped walk; cap exceeded or any stat error -> NOT exempt, fail toward
  flagging).

Meta counter `scratch_attested` beside `registry_subsumed`. Tests in
`StrandedWorktreeFindingsTest` using the existing `_real_git_wt()` pattern: attested-and-quiet
is dropped; unattested is kept; attested-then-written-after is kept; a root-level file beside
an attested `.scratch/` still strands; `scratch/` (wrong name) is kept. `.scratch/` must NOT
be added to `.gitignore` -- that would convert B into C.

**Not proposed:** any change to `METAWORKER_SCRATCH_FILES`, `batch_worktree_gc.py`, or the
`/session-land` scratch trio. GC of a worktree holding `.scratch/` stays refused-by-dirty and
is offered through source 6 as today.

## 4. Held-out check (GOV-HELDOUT-1)

The rule was written from today's six-chip batch (`metaworker-science-20260918-*`,
ree-cloud-5). Held-out = every other adjudicated worker-scratch instance since 2026-09-11.
"NEW" assumes the worker follows the contract; section 5 says what happens when it does not.

| # | Instance (box) | Shape | Worker closed cleanly? | Healer verdict | OLD | NEW (B) | Option C | Differs? / right? |
|---|---|---|---|---|---|---|---|---|
| 1 | exp-0893 (cloud-5) | `scratch/` 10 calib probes | yes, 6.0 h prior | worthless, findings landed `5cd2882` | chip | no chip | no chip | yes / right |
| 2 | exq900 autopsy (cloud-4) | `.scratch/` drafts | yes, 6.1 h prior | "rescued" -- drafts identical to landed finals (2e) | chip + wasted rescue | no chip | no chip | yes / right |
| 3 | exq-861i autopsy (cloud-5) | `.scratch/` draft copies | yes | redundant, final landed `a2692377f0` | chip | no chip | no chip | yes / right |
| 4 | arc029-p1p3 (cloud-5) | `scratch_arc029/` | STOP-to-decision | worthless, finding landed `963678ef22` | chip | no chip | no chip | yes / right |
| 5 | mech018 build (cloud-4) | `scratch_mech018/` incl. nested worktree `wt3/` | yes | worthless, 5 ree-v3 commits on origin | chip | no chip | no chip | yes / right |
| 6 | inv063 ladder (cloud-4) | `scratch/` probe + sentinels | yes | worthless, conclusions in `973bed43` | chip | no chip | no chip | yes / right |
| 7 | exp-1069 (cloud-5) | root `smoke_out.txt` + ` M TASK_CHIPS.json` | yes | smoke log worthless | chip | **chip** (registry path still kept) | chip | no -- degenerate, not counted |
| 8 | 2026-08-15 real loss (cloud-5) | ` M scripts/*.py` tracked | no (died) | TRUE positive | chip | chip | chip | no -- regression control, right |
| 9 | exp-0841 / exp-0457 (cloud-5, 09-03) | ` M TASK_CHIPS.json` local-only closure | yes | TRUE positive | chip | chip | chip | no -- regression control, right |
| 10 | hypothetical: #2's worker dies BEFORE landing | `.scratch/` drafts, no attestation | no | would be real work | chip | **chip** | **no chip -- LOSS** | B vs C differ; B right, C wrong |

Six non-degenerate cases (1-6), all given the right call by B; three controls unchanged.
Row 10 is constructed, not historical, and is labelled as such: no September worker died
with its only copy in a scratch directory, so **history cannot distinguish B from C** -- the
case for B over C rests on the mechanism, not on a measured loss. If that is judged too
thin, C is cheaper and would also have been right 6 of 6.

**Would it have prevented the last 10 instances?** The ten most recent worker-scratch chips
(09-19T02:48 to 09-20T08:00): six are directory-shaped (`scratch_1039a/`+`wip/`,
`scratch_mech018/`, `.scratch/`, `scratch/`, `scratch_541d/`, `scratch/`) and need only the
NAME to become attestable; four are root-spill (sd061 1 path, mech017 34 paths, sd071 24
paths, sd036 4 paths) and need the worker to change where it writes. Under full compliance
all ten disappear **except** sd061 and sd071, where a
findings doc in the root would -- correctly -- still strand until committed. That residual
is the rule working, not failing.

## 5. Honest counterweight

- **Prompt text is mitigation, not enforcement** (A-36). Nothing makes a worker use
  `.scratch/`. Non-compliance degrades to exactly today's behaviour (a chip), never to a
  hidden loss, which is the property that makes B safe to ship. Expect the class to shrink,
  not vanish; re-measure after ~2 weeks of dispatches before claiming it worked.
- The attestation is self-reported. A worker can write it wrongly. It is still strictly
  more information than a directory name.
- The science lane often ends in STOP-to-decision rather than a clean close (case 4). The
  rule must say a STOP counts as a close for attestation purposes once the decision chip is
  recorded and any findings doc is pushed; otherwise the science lane -- today's whole
  batch -- gets no benefit.
- The held-out check cost ~40 minutes and one subagent pass per side. It changed the design:
  the first draft was option C.
- 2(g) is a real but separate gap (a gitignored `_scratch/` hides work from the detector).
  It WIDENS what the detector reports, so it is not bundled here; it is named in the
  decision chip as an optional add-on.

## 6. Sweeping what is already stranded (question 4)

No new sweeper. Already-stranded scratch sits in worktrees that source 6's GC already
offers once the strand chip is resolved, and GC refuses a dirty tree without `--force` by
design. Rule for the Healer, unchanged but now stated: a path is provably scratch only if
(i) it has no git object AND its content is line-subsumed by a landed artifact, or (ii) its
own docstring/header declares it throwaway AND the deliverable it fed is on origin. Anything
else gets a branch commit + push, as today. Nested throwaway worktrees (`wt3/`) must be
removed with `git worktree remove` from their owning repo, not `rm -rf`, or they leave
dangling worktree metadata in `ree-v3`. Nothing is deleted on the strength of this document.

## 7. What a build would touch (after the decision chip is answered)

1. `.claude/skills/metaworker-dispatch/SKILL.md` + `.agents/skills/` mirror -- contract rule.
2. `scripts/dispatch_campaigns.py` -- one sentence in each of the two renderers;
   `test_dispatch_science_lane.py` pins brief wording and will need a matching assertion.
3. `.claude/skills/metaworker-orchestrate/SKILL.md` (+ mirror) L529-545 -- routes the same
   science brief to a Mac `Agent` subagent; same sentence.
4. `scripts/hygiene_routine_tick.py` + `scripts/test_hygiene_routine_tick.py` -- predicate,
   counter, five tests, failing test first.
5. `CLAUDE.md` "Python" -- the parenthetical.
6. `scripts/run_scripts_tests.sh --changed` from the MAIN checkout before landing.
