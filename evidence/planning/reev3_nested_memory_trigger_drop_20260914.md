# `ree-v3/CLAUDE.md` nested_memory injection drop: diagnosis (2026-09-14)

**Run:** 2026-09-14T23:31Z, Mac (canonical DLAPTOP), session `eloquent-jepsen-5f6242`,
chip `chip-20260914-reev3-nested-memory-trigger-drop`. Read-only diagnosis over
`~/.claude/projects/*REE-Working*/*.jsonl` (1,761 transcripts) plus the installed Claude Code
2.1.269 binary. Answers owed item (2) of `context_budget_restructure_plan.md` section 7.4.

Classification: `mystery (known data)` -> **resolved**. No new data was needed; the data was
being read under the wrong frame.

## Verdict

**The harness did not change its trigger. The split did.** Claude Code skips a `nested_memory`
attachment for any CLAUDE.md that is already in the session's `readFileState`, and a successful
`Read` of that file puts it there. Before the split, `ree-v3/CLAUDE.md` (1.4 MB) was too large to
`Read`. The Read failed, the file was never registered, and the harness injected it. After the
split (62-74 KB) the same `Read` succeeds, so the harness correctly declines to inject a second copy.

The ree-v3 instructions **still reach these sessions**. They now arrive as a `Read` tool result,
not as a `nested_memory` attachment. The section 7.2 count of "1 of 166 injected" is a channel
count, not a count of sessions that loaded the instructions.

## (a) Harness trigger: unchanged

- **Code, 2.1.269** (installed binary): the nested-memory emitter does
  `if (loadedNestedMemoryPaths[path]) continue; if (!readFileState.has(path)) { push nested_memory ... }`.
  The Read tool pushes the read path onto `nestedMemoryAttachmentTriggers` only **after** it has
  `readFileState.set(...)`, and that set covers partial (`offset`/`limit`) views too. A Read that
  throws on the size limit reaches neither.
- **Control (same versions):** main-checkout sessions whose first REE_assembly access was a Read
  of a non-CLAUDE.md file got `REE_assembly/CLAUDE.md` injected in **25/26 PRE and 7/7 POST**. The
  POST sessions ran 2.1.260, 2.1.266 and 2.1.270.
- **Version is not the discriminator.** Pre-split injections span 2.1.237-2.1.260. The first
  post-split suppression (2026-09-08) ran on 2.1.260, the same version that produced injections
  on 09-05, 09-06 and 09-07.
- **Suppression already operated before the split:** `f4fdc52f` (2026-09-04, 2.1.258) read
  `ree-v3/CLAUDE.md` with `limit: 120`. The Read succeeded and **no injection** followed, even
  though the session then read `docs/ree-v3-spec.md` three times.
- **Changelog** (`anthropics/claude-code` CHANGELOG.md, which covers 2.1.257-2.1.271): no entry
  touches nested CLAUDE.md loading or read dedup. The only CLAUDE.md entries are 2.1.268 (managed
  `claudeMd` approval dialog) and 2.1.269 (`omitClaudeMd` for subagents), and neither applies.

## Mechanism, per session (main checkout, cwd `/Users/dgolden/REE_Working`)

Main-checkout sessions that Read or Edit a ree-v3 file with first turn >= 2026-08-20 (a wider
PRE window than section 7.2's 08-29 start, to enlarge n), split at 2026-09-07T20:50Z. Each is
classified by its first ree-v3 access:

| first ree-v3 access | PRE injected | POST injected |
|---|---|---|
| `Read ree-v3/CLAUDE.md` -> **ERR** (file too large) | **7/7** | -- (cannot occur post-split) |
| `Read ree-v3/CLAUDE.md` -> **ok** (whole or partial) | **0/1** (f4fdc52f) | **0/3** |
| Read of another ree-v3 file first | 8/9 | -- (0 sessions) |
| Edit/Write only, no Read | 2/5 | 0/2 |

**All five POST sessions are the `nightly-documentation-update` scheduled task.** The three
"ok" rows (2f8aafe4 09-08, 2e8b82c2 09-11, dd26d1a5 09-14) Read `ree-v3/CLAUDE.md` explicitly
near their start. The two Edit-only rows (7fe50f2f 09-12, c6b61741 09-13) never used Read on a
ree-v3 file. f4fdc52f is the same task too. Before the split, that task accounts for all 7
"ERR -> injected" rows (d17345ac, 4993fc5e, 3d172be3, a65da5e2, d4ca0dca, 1a0300a6, 5cd419eb).
It also accounts for 3 of the "other file first" rows (b6561b52, c0276565, f4189a29, which read
the spec before CLAUDE.md). **10 of the 17 PRE injections in this window were that one task.** In
section 7.2's own window (first turn >= 08-29), 6 of its 11 unique injected sessions were the
nightly task (12 with the 1a8f42c4/1cb0b5d4 fork duplicate). The POST denominator of 5 is
nightly-only. So the "12/17 -> 0/5" figure compares a mixed population with one nightly task
whose Read now succeeds. It is not a like-for-like trigger rate.

The one post-split `nested_memory` event (73,617 chars, 2026-09-10T19:30Z) is not a new session.
It comes from `1a8f42c4`, a session started 2026-09-02 and resumed on 09-10. That session was
re-injected when a Read of `experiments/v3_exq_1008_*.py` followed the resume. That fits resumption
starting with an empty `readFileState` (inferred, not traced in code). So in this window the "other file Read first" trigger still works
post-split (1/1).

## (b) Other channel: yes, the Read tool result, not `instructions`

- `instructions` attachments (261 sessions since 2026-09-02) carry only the umbrella or worktree
  `CLAUDE.md` and `MEMORY.md`. **0/261 carry `ree-v3/CLAUDE.md`.**
- The channel that replaced `nested_memory` is the session's own `Read`. The nightly task gets a
  first read (~33-38 KB serialized) and, in 2 of 3 runs, a paged re-read (27-44 KB). The measurement
  books this under **tool results**, not harness injections.

## (c) Session behaviour

- **The nightly task's explicit `Read ree-v3/CLAUDE.md` is the behaviour behind most of the drop.**
  Its effect changed because the Read now succeeds. The task prompt was not diffed; that is not needed to explain the change.
- **Bash is not a new substitute.** Among main-checkout sessions, 84/106 PRE and 57/74 POST touched
  ree-v3 only through Bash (79% vs 77%). Bash never triggers `nested_memory`, in either window.
- **Worktree share rose.** Main-checkout sessions were 106/201 PRE and 74/183 POST (53% -> 40%).
  Worktree sessions can never trigger: the emitter walks only directories under cwd, and
  `$BASE/ree-v3` is not under `.claude/worktrees/<slug>`. That is 7/7 uninjected in both windows.
- **Residual, stated rather than explained away:** main-checkout sessions that are not the
  nightly task and Read a non-CLAUDE.md ree-v3 file numbered 6 PRE, 5 of them injected. They were
  coordinator/infra work: 1d4c3901, af52458a, e0fd9306, 1a8f42c4, 5483fb9f, and uninjected
  12cdbd48, over 08-20..09-07 (~18 days, ~2.3/week). POST there were **0 such sessions** in ~7
  days. At the PRE rate ~2.3 would be expected, so p ~ 0.1: not significant. The only POST
  exercise of this path (1a8f42c4's 09-10 resume) did inject. This is session mix, not a trigger
  change.

## Consequence for WI-1

- **Section 7.4 under-credits WI-1.** Each POST nightly run avoided the 1.4 MB injection its
  pre-split twin carried, and kept only a ~35-80 KB Read result instead. That is roughly
  **~350 k tok/turn x 247 post-read turns ~ 0.09 B tokens** (chars/4), or about **+1 pp** on the
  realized ~3%. This is an estimate from turn counts, not an OLS refit.
- **WI-1's fleet frequency is set by two things.** One is main-checkout sessions that `Read`
  ree-v3 files. The other is whether they Read the CLAUDE.md itself first. Both are workflow
  properties, not harness properties. Worktree sessions get neither channel unless they Read
  `$BASE/ree-v3/CLAUDE.md` explicitly.
- **Any future injection-frequency metric must count both channels**: `nested_memory`
  attachments, and successful `Read` tool results of `ree-v3/CLAUDE.md`. Otherwise it will keep
  reporting this channel change as a frequency collapse.
- Owed item (3), the `ree-v3/CLAUDE.md` regrowth, now bites through the Read channel as well. The
  Read is paged, so regrowth also adds re-read turns.

## Method (reproducible)

Scratch scripts were not landed: `nm_scan.py`, `seq.py`, `probe2.py` in this session's scratchpad.
For each transcript the scan collects: the earliest timestamp; `cwd`; `version`; non-sidechain
`nested_memory` attachments (path, content length); and `Read`/`Edit`/`Write` tool uses paired
with their `tool_result` (`is_error`, size). A session is PRE or POST by its first timestamp
relative to 2026-09-07T20:50Z. Session files duplicated by fork or resume (1a8f42c4/1cb0b5d4) were
counted once in the prose. The binary check read strings around `nested_memory` and
`nestedMemoryAttachmentTriggers` in `~/.local/share/claude/versions/2.1.269`.
