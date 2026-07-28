# REE_assembly orphaned stash triage

**Triaged:** 2026-07-28T07:58Z (session `ree-assembly-stash-triage-f58f4c`, worktree `dazzling-taussig-f58f4c`)
**Repo:** `/Users/dgolden/REE_Working/REE_assembly`
**Trunk at triage time:** `origin/master` = `9ff5065cc6` -> `333629312a` (phase3-heartbeats writer moved it mid-triage; all blob comparisons below were taken against `9ff5065cc6`, and the writer only touches `runner_heartbeats/`)
**Entries triaged:** 7 (4 labelled `autostash`, 2 `runner-prepull-untracked`, 1 `gov-cycle-regen-wip-angry-ardinghelli`)

Companion to [`ree_v3_orphaned_autostash_triage.md`](./ree_v3_orphaned_autostash_triage.md), which
established the method. **Read that one first** -- this document assumes it.

---

## The defect being triaged

A concurrent `git pull --rebase --autostash` stashes a session's uncommitted work. When the pop
fails, the content stays in the stash list and **no error reaches the session that owned it** --
`git status` simply shows the files unmodified, so the work reads as silently vanished. On
`REE_assembly` the writer is the runner heartbeat (`ree-v3/runner_remote_control.py:push_heartbeat`),
which pulls against `REE_assembly` every minute.

These 7 entries were surfaced by the **first run** of `scripts/audit_stashes.py` (REE_Working
`4cc9cb9c35`, built 2026-07-28) -- the session-facing audit recommended as fix (b) at the end of the
ree-v3 triage. Nothing had surfaced them before; the oldest was **6.2 days** old.

---

## Headline: this is a DIFFERENT population from the ree-v3 one

The five ree-v3 entries were all **session substrate work** -- someone's in-progress `ree_core/`
change, caught mid-edit. Not one of the seven here is that. They fall into two classes, and neither
is lost work:

1. **Governance/indexer regen output (5 entries, ~1050-1190 files each).** Derived artifacts --
   per-experiment `INDEX.md`, `claim_evidence.v1.json`, `pending_review.md`, the planning
   registries, the docs stubs. All regenerable from committed inputs by
   `evidence/experiments/scripts/build_experiment_indexes.py` + `scripts/governance.sh`.
2. **Runner-side evidence writes (2 entries, 1 and 6 files).** A freshly-written manifest / run
   pack that the runner stashed before pulling. Both are byte-identical or a strict subset of what
   is on trunk today.

The practical consequence is that the *shape* of a REE_assembly stash entry is a strong prior on
its verdict, in a way the ree-v3 shapes were not. A four-figure file count on this repo means
"someone ran the governance cycle", not "someone was writing code".

---

## Verdicts

| # | Date (local) | Stash SHA | Shape | Verdict | Action |
|---|---|---|---|---|---|
| 0 | 2026-07-27 15:21 | `95b7594f49` | governance regen, 1186 files | SUPERSEDED (regenerable) + **stale-content skew** | DROPPED (pass 2) |
| 1 | 2026-07-27 15:20 | `07a5621a02` | near-duplicate of #0, 1186 files | SUPERSEDED (regenerable) + **stale-content skew** | DROPPED (pass 2) |
| 2 | 2026-07-26 08:58 | `4a081fbd57` | governance regen, 1130 files | SUPERSEDED (regenerable) | DROPPED (pass 2) |
| 3 | 2026-07-26 08:58 | `455475f8b2` | 1 untracked V3-EXQ-823 manifest | **ALREADY-LANDED (proven)** | **DROPPED (pass 1)** |
| 4 | 2026-07-26 00:56 | `995de28f5b` | governance regen 1120 + 20 untracked | SUPERSEDED (regenerable); **all 20 untracked verified on trunk** | DROPPED (pass 2) |
| 5 | 2026-07-22 04:00 | `370ca49bb5` | `graceful_timeout.py` + V3-EXQ-790 run pack | **ALREADY-LANDED (proven)** | **DROPPED (pass 1)** |
| 6 | 2026-07-22 03:56 | `8f92e7b559` | governance regen, 1063 files | SUPERSEDED (regenerable) | DROPPED (pass 2) |

**No entry is GENUINELY-ORPHANED.** Nothing needs restoring. Two residual content differences exist
and are recorded under "What is genuinely NOT on trunk" below; neither is work, and neither is
worth a restore.

Grades, same as the ree-v3 triage:

- **proven** -- blob identity, or a semantic (key-for-key) JSON identity, or trunk is a strict
  superset. Mechanical, no argument required.
- **superseded (regenerable)** -- trunk has moved past the stash, and the residual is entirely
  derived-artifact output whose generator is named and whose inputs are on trunk. Strong, but it
  is an *argument*, so these were reported and left rather than dropped on a judgement call.

---

## Method

Same three tests as the ree-v3 triage (blob identity -> hunk containment -> symbol containment),
plus **three additions** this population needed. Record them; they are the reusable part.

4. **Derived-vs-source classification.** Before any containment test, ask *who writes this file*.
   `grep -rl "<basename>" scripts/*.py evidence/experiments/scripts/*.py docs/*.py`. A file with a
   named generator and committed inputs cannot be "lost" -- the containment tests are the wrong
   question for it. This is what collapses a 1186-file entry to a ~17-85 file real question.
   Established generators found here:

   | Artifact | Generator |
   |---|---|
   | `evidence/experiments/*/INDEX.md`, `*/experiment.md` (AUTO-DESIGN-IMPLICATIONS block), `claim_evidence.v1.json`, `conflicts.md`, `TODOs.md`, `promotion_demotion_recommendations.md`, `pending_review.md`, `arm_fingerprint_index.json`, `evidence_backlog.v1.json`, `experiment_proposals.v1.json`, `architecture_gap_register.v1.json` | `evidence/experiments/scripts/build_experiment_indexes.py` |
   | `evidence/GOVERNANCE_STATE.md`, `docs/REE_overview.md`, `docs/index.md` | `scripts/generate_status_stubs.py` |
   | `docs/closure_dashboard.md` | `scripts/generate_closure_snapshot.py` |
   | `docs/*.md` nav frontmatter | `docs/apply_nav_frontmatter.py` |
   | `evidence/planning/inter_governance_workset.{md,v1.json}` | `scripts/generate_inter_governance_workset.py` |

5. **Direction test (base vs stash vs origin).** For a suspected source file, compare all three
   blobs and then search the path's own history on `origin/master` for the stash blob:

   ```bash
   git rev-parse '<stash>^1:<path>'  # base HEAD at stash time
   git rev-parse '<stash>:<path>'    # what the working tree held
   git rev-parse 'origin/master:<path>'
   for c in $(git rev-list --max-count=40 origin/master -- '<path>'); do
     [ "$(git rev-parse "$c:<path>")" = "$STASH_BLOB" ] && echo "historical: $c"
   done
   ```

   `base == origin` **and** the stash blob found in history is the decisive signature of the
   `M ` HEAD/worktree skew documented in `CLAUDE.md`: the working tree was carrying pre-adoption
   content, and the autostash captured that staleness *as if it were an edit*. **Restoring such an
   entry would revert trunk.** This is the inverse of the failure the triage is looking for, and
   the blob-history search is the only thing that tells them apart.

6. **Line-superset test, for append-only files.** Blob identity and hunk containment both say
   nothing useful about a log or a `.jsonl` series. Use
   `comm -23 <(git show '<stash>:<path>' | sort -u) <(git show 'origin/master:<path>' | sort -u)`
   and read the count of lines present in the stash and absent from trunk. This is what found the
   two genuinely-unlanded log lines recorded below.

**Do not use the blob-history search on derived artifacts.** Every regen embeds a fresh
`Generated:` timestamp, so the blob is unique by construction and the test returns "never seen on
origin" for *everything*, which reads as total loss and means nothing. That false alarm is why
test 4 has to run first.

Two mechanical traps that cost real time and will recur:

- **`git diff` here has no `--pathspec-from-file`** (this git build), and 1100 paths overflow the
  argument list silently -- `git diff` prints its usage to stderr and an *empty* diff to stdout, so
  a naive `grep -c` on it reports **0 differences** and looks like a clean result. Chunk the paths
  (150 at a time) and check the diff is non-empty.
- **zsh eats `$s:evidence/...`** as the `:e` (extension) history modifier. Always write
  `"${s}:evidence/..."`.

---

## Per-entry evidence

### `370ca49bb5` -- 2026-07-22 04:00 -- `runner-prepull-untracked` -- ALREADY-LANDED (proven) -- DROPPED

The one entry whose shape suggested live session work (6 files, `+1215/-117`, including a `.py`),
and therefore the one triaged first. It is not session work.

- `graceful_timeout.py`: stash blob `9cc5f0b9e6` == `origin/master` blob == current worktree blob.
  **Byte-identical.** Landed as `b5bef97728` "graceful_timeout: re-vendor from canonical (bounded
  post-SIGKILL drain)".
- The three V3-EXQ-790 run-pack files (`manifest.json`, `metrics.json`, `summary.md`) show as `D`
  in `git stash show`. That is **not a deletion of work** -- it is the `D ` HEAD/worktree skew:
  the files were in HEAD, absent from index and disk. All three are present on `origin/master`.
- The flat manifest `v3_exq_790_..._20260722T021558Z_v3.json` appears twice (tracked-`M` and
  untracked in `^3`), the signature of index-lacking + worktree-present. The untracked disk copy
  (`a77d307`, 43543 B) and trunk's (`e9de7c2`, 35624 B) are **key-for-key identical JSON** --
  `python -m json.tool --sort-keys` on both yields a zero-length diff. The byte difference is
  serialization indentation only.
- **Coupled set (remedy (a2)) intact.** `graceful_timeout.py` is a vendored module whose canonical
  copy and pinned contract (`tests/contracts/test_graceful_timeout_lockfile.py`) live in `ree-v3`.
  Nothing in this stash touches the contract, and the vendored body is byte-identical to trunk, so
  there is no half-landed pair. (One incidental drift found, unrelated to the stash -- see
  "Incidental findings".)

### `455475f8b2` -- 2026-07-26 08:58 -- `runner-prepull-untracked` -- ALREADY-LANDED (proven) -- DROPPED

One untracked file: `evidence/experiments/v3_exq_823_sd079_ghost_goal_retrieval_consumer_20260726T075327Z_v3.json`.

- Present on `origin/master`. Semantic diff stash -> trunk is a **single added key on trunk's
  side**: `"queue_id": "V3-EXQ-823"`. Trunk is a strict superset; the stash holds the runner's
  pre-annotation copy.

### `995de28f5b` -- 2026-07-26 00:56 -- `gov-cycle-regen-wip-angry-ardinghelli` -- SUPERSEDED -- left in place

The entry flagged as highest-risk in the chip brief, because it carries **20 untracked evidence run
packs** which would not be regenerable if the underlying runs' manifests had never landed. They all
landed. Every one of the 20 paths exists on `origin/master`:

| Result | Count | Paths |
|---|---|---|
| byte-identical | 12 | all 6 `experiment.md`; the full 3-file run packs for `v3_exq_817_..._20260725T204837Z_v3` and `v3_exq_821_..._20260725T222252Z_v3` |
| trunk is richer | 2 | `v3_exq_817_...json` (trunk adds `"queue_id": "V3-EXQ-817"`); `v3_exq_821_...json` (trunk has `evidence_direction: non_contributory` + adjudication note where the stash has `unknown` -- i.e. trunk carries the 2026-07-25 `/governance` adjudication the stash predates) |
| timestamp-only | 6 | the per-experiment `INDEX.md` for 806/807/817/818/820/821 -- sole difference is the `Generated:` line |

Nothing absent. The tracked 1120-file part is governance regen output, handled below.

### `95b7594f49` + `07a5621a02` -- 2026-07-27 15:21 / 15:20 -- SUPERSEDED + stale-content skew -- left in place

Two autostashes one minute apart with identical `+55231/-125542` stats, off different bases
(`9dd23d96ed` / `99c0c5ef93`, both `igw-ledger: update`). **Not exact duplicates:** their trees
differ by exactly 4 files -- the V3-EXQ-826a `20260727T141840Z_v3` run pack, present in the later
one. All 4 are byte-identical to `origin/master`.

The `-125542` deletion count is the interesting part, and it is **not work being deleted**. Every
source file in the entry has `base blob == origin blob` while the stash holds an **older version
already in trunk's history**:

| Path | Stash blob is the version from |
|---|---|
| `scripts/generate_status_stubs.py` | `d4034d75c5` 2026-07-26 "Redesign public REE homepage" |
| `docs/_includes/head_custom.html` | `d4034d75c5` 2026-07-26 |
| `docs/apply_nav_frontmatter.py` | `77511a3f55` 2026-07-15 |
| `.github/ISSUE_TEMPLATE/replication_attempt.yml` | `efd7a4d7ab` 2026-06-15 |
| `docs/contribute.html` | `134e5c179f` 2026-06-20 |
| `docs/architecture/overview.md` | `1eecf2a901` 2026-05-19 |
| `docs/glossary.md` | `f190c41c2c` 2026-04-26 |

This is the `M ` skew variant: the shared Mac working tree was carrying months-stale copies of the
`docs/` cluster while HEAD had current ones, and the autostash captured that as an edit. **The skew
has since been repaired** -- all seven paths' current worktree blobs equal `origin/master` today.
Applying either entry would revert trunk's public-site work by up to three months.

### `4a081fbd57` -- 2026-07-26 08:58 -- SUPERSEDED -- left in place

Governance regen, 1130 files. 1088 are per-experiment `INDEX.md`. The 42 non-`INDEX.md` residuals
are all derived (`claim_evidence.v1.json`, the drift reports, the planning registries, the docs
stubs, `contributors/contributions.json`) plus 4 `runner_heartbeats/*.json` -- machine-written
telemetry rewritten every tick by the `phase3-heartbeats:` writer.

### `8f92e7b559` -- 2026-07-22 03:56 -- SUPERSEDED -- left in place

Governance regen, 1063 files, 1046 of them `INDEX.md`. The single hand-authored residual is
`docs/architecture/sd_077_centered_super_ordinal_cue_key.md`, and **its change is on trunk**: the
stash's entire edit vs its base is a 2-line frontmatter update
(`status: candidate/v3_pending -> candidate`, `status_asof: 2026-07-21 -> 2026-07-22`).
`origin/master` carries `status: candidate` plus a `status_asof` of 2026-07-24 and a 45-line
section ("The sweep this motivated -- run 2026-07-22, TWO more consumers found") that the stash
predates. Trunk contains the stash's change and is far ahead of it.

### The regen bulk, common to all five

Verified once, applies to every regen entry:

- **`INDEX.md` (1046-1105 files each): the only per-file difference is the `Generated:` timestamp**,
  plus 162-168 table rows in the top-level `evidence/experiments/INDEX.md` that trunk has since
  re-sorted or replaced with newer run ids (trunk carries 171-248 rows the stash lacks -- i.e.
  trunk is ahead in both directions of churn, as expected of a rebuilt index).
- **`experiment.md`** diffs sit entirely inside `<!-- AUTO-DESIGN-IMPLICATIONS:START -->` blocks.
- **Planning registries** carry no orphaned ids. Id-level superset test on
  `decision_state.v1.json`, `arm_fingerprint_index.json`, `governance_agenda.v1.json`,
  `hypothesis_space.v1.json`: **0 ids in any stash absent from trunk**. `evidence_backlog.v1.json`
  and `experiment_proposals.v1.json` reference 5-20 `claim_id`s trunk no longer lists (`ARC-045`,
  `MECH-124`, `MECH-166`, `Q-017`, `SD-048`, `ARC-016`) -- these are backlog/proposal *rows for
  claims that have since been serviced*, dropped by the regenerator, not lost input.
- **`inter_governance_workset.v1.json`** is regenerated whole each day with date-stamped ids, so
  each stash naturally holds its own day's set (`20260722`/`20260725`/`20260726`/`20260727`).
  Consume-only; not accumulated.
- **`hypothesis_space_timeseries.v1.jsonl`** keeps one row per `date`. The two rows flagged as
  stash-only (`2026-07-25T23:35:44Z`, `2026-07-26T05:15:35Z`) were each replaced later the same day
  by trunk's row for that date (`23:57:08Z`, `15:39:43Z`). Supersession by design.

---

## What is genuinely NOT on trunk

Two residuals, both recorded for completeness. Neither is work; neither justifies a restore.

1. **Two IGW skip-log lines** (`8f92e7b559`, `evidence/planning/igw_routine_log.md`):
   ```
   2026-07-22T01:11:34Z skip IGW-20260722-206: no fresh runner heartbeat (experiment-lane item would just sit in queue)
   2026-07-22T02:11:52Z skip IGW-20260722-206: no fresh runner heartbeat (experiment-lane item would just sit in queue)
   ```
   Machine-written operational log lines recording two *skipped* ticks. No scientific content. The
   other three regen entries' copies of this log are proper subsets of trunk's.

2. **The IGW workset on trunk is a day stale.** `origin/master`'s
   `inter_governance_workset.v1.json` holds the **`20260726`** set (657 items). Stash `95b7594f49`
   holds a `20260727` regen (611 items) that never landed. Regenerable --
   `python3 scripts/generate_inter_governance_workset.py` -- so this is a staleness observation,
   not a loss. Worth knowing before reading the workset as current.

---

## Actions taken

**All seven dropped. The REE_assembly stash list is now EMPTY.** Every one was archive-tagged
first, so no content was destroyed.

Dropped in two passes, deliberately -- preserving the split established by the ree-v3 triage:

1. **Pass 1, no permission needed -- mechanically proven contained:**
   - `370ca49bb57e7b574e5d1e5b7800cd46a9ed3b39` (6 files; `graceful_timeout.py` byte-identical to
     trunk, run pack present, manifest key-for-key identical)
   - `455475f8b2a349874887eb91336c92570193ef73` (1 untracked manifest; trunk is a strict superset)
2. **Pass 2, on explicit user authorisation** (2026-07-28: *"They do sound to be a risk just
   sitting there. They should not be easily reincorporated and rewinding of our precious repos"*)
   -- the five regen entries, whose verdict rests on the derived-artifact argument (test 4) plus
   the stale-content direction test (test 5) rather than on blob identity:
   - `95b7594f495c91f17f34a857a1323e8d5a08fa82` (1186 files)
   - `07a5621a02b2a47173977e071fe8dc341578ca38` (1186 files)
   - `4a081fbd5776846bdc80d974f6781a0870f776dc` (1130 files)
   - `995de28f5bde53affa5a75348e8d02cabf522f25` (1120 tracked + 20 untracked)
   - `8f92e7b5596a7d39f9c1ef4dfce28eb292bcda59` (1063 files)

**The two-pass split is the point, not bureaucracy -- and note the ordering is NOT by risk.** Pass 2
contains the entries that are arguably the *most* dangerous to leave in place: `95b`/`07a` hold
months-stale `docs/` content, so a future reader who sees "1186 files, N days old" and applies one
would revert trunk. They still went in pass 2 because their verdict is an *argument* (derived +
direction-tested), not a blob comparison, and that distinction -- not the size of the hazard -- is
what decides whether a session may act alone. Preserve it if this triage is repeated.

Nothing was restored, and nothing should be. Every entry is behind trunk.

**All seven were archive-tagged before anything was dropped**, local-only, following the convention
from the 2026-07-18 fleet clear. `REE_assembly` now carries 63 such tags (56 pre-existing + these 7):

```
stash-archive/20260727-95b7594f  -> 95b7594f495c91f17f34a857a1323e8d5a08fa82   (1186 files)
stash-archive/20260727-07a5621a  -> 07a5621a02b2a47173977e071fe8dc341578ca38   (1186 files)
stash-archive/20260726-4a081fbd  -> 4a081fbd5776846bdc80d974f6781a0870f776dc   (1130 files)
stash-archive/20260726-455475f8  -> 455475f8b2a349874887eb91336c92570193ef73   (1 untracked)
stash-archive/20260726-995de28f  -> 995de28f5bde53affa5a75348e8d02cabf522f25   (1120 + 20 untracked)
stash-archive/20260722-370ca49b  -> 370ca49bb57e7b574e5d1e5b7800cd46a9ed3b39   (5 tracked + 1 untracked)
stash-archive/20260722-8f92e7b5  -> 8f92e7b5596a7d39f9c1ef4dfce28eb292bcda59   (1063 files)
```

Content was re-verified **through the tags after the drops** (`git stash show --name-only <tag>`,
`git ls-tree -r --name-only <tag>^3`), which is the check that proves survival rather than merely
that a tag exists. Post-drop file counts match the pre-drop counts exactly:

| tag | tracked | untracked |
|---|---|---|
| `stash-archive/20260727-95b7594f` | 1186 | 0 |
| `stash-archive/20260727-07a5621a` | 1186 | 0 |
| `stash-archive/20260726-4a081fbd` | 1130 | 0 |
| `stash-archive/20260726-995de28f` | 1120 | 20 |
| `stash-archive/20260726-455475f8` | 0 | 1 |
| `stash-archive/20260722-370ca49b` | 5 | 1 |
| `stash-archive/20260722-8f92e7b5` | 1063 | 0 |

Blob-level readability was spot-checked too, not just the file lists:
`git show stash-archive/20260727-95b7594f:docs/glossary.md` still returns the 2026-04-26 content.

Tags keep the commits reachable so `git gc` cannot prune them. Recover with
`git stash apply stash-archive/<tag>` or `git show <tag>:<path>`. **Local-only and never pushed** --
verified `git ls-remote --tags origin 'stash-archive/*'` = 0. **Do not bulk-delete these tags;**
deleting them is the one action that would actually destroy the content.

---

## Incidental findings (reported, not actioned)

1. **`graceful_timeout.py` vendor drift. FIXED 2026-07-28 -- landed as ree-v3 `d21d880014`**
   (session `dazzling-dubinsky-dec79b`). The module's own banner states that the three copies
   (`ree-v3/graceful_timeout.py` canonical, `REE_assembly/graceful_timeout.py`,
   `REE_Working/scripts/graceful_timeout.py`) are byte-identical and "`shasum` over all three must
   match". They did not. **The module body below the banner was identical** (sha `5a8eb4a3a0`), so
   the drift was documentation only and there was no functional divergence -- but the banner's own
   `shasum` check was false.

   **Correction to what this item originally said, because the direction was backwards and the
   inverted version was acted on.** This entry read "`REE_assembly`'s copy (`9cc5f0b9e6`) is
   missing the 23-line VENDORED COPY banner that `ree-v3`'s canonical copy (`6b05cc02bd`)
   carries". It is the other way round: **the two VENDORED copies carried the banner and the
   CANONICAL copy did not.** The banner was authored at vendoring time (`REE_assembly`
   `478b7879e5`, umbrella `8816015`) and written into the copies only; it was never back-added to
   `ree-v3`, which had never carried it in any of that file's three commits (`eb6979b`,
   `b0a6dd8`, `7b3c5d0`). The `diff` evidence quoted here was consistent with the truth and not
   with the prose -- `diff <copy> <canonical>` = `3,25d2` means the *copy* holds lines 3-25 --
   but the prose won, and the follow-up task was written as "bring both stale copies
   byte-identical to the canonical; do NOT edit the canonical", which executed literally would
   have **deleted** the banner from both copies.

   That failure mode is worth naming: byte-identity is a symmetric target, so a convergence task
   is only well-specified once you say *which* content survives. Here the destructive direction
   satisfied the stated success criterion (`shasum` matches) while destroying the entire point of
   the fix -- the banner is the only place the sync convention is written down, and stripping it
   would have removed it from precisely the file the banner exists to point future editors AT.

   **Fix applied: the banner was added to the canonical copy** (23 insertions, 0 deletions,
   docstring only; module body untouched). All three now hash `9cc5f0b9e6` on their respective
   `origin` refs, so the banner's `shasum` assertion is true for the first time.
   `tests/contracts/test_graceful_timeout_lockfile.py` green (8 passed). The banner's path list
   was re-verified: those three are the only `graceful_timeout.py` files in `REE_Working`, and the
   named consumers are the real importers (`REE_assembly/serve.py:63`,
   `scripts/igw_routine_tick.py:110`) -- every other mention in either repo is a comment.

2. **`REE_assembly`'s working tree carried months-stale `docs/` content.** The `95b`/`07a`
   evidence shows the shared Mac checkout holding `docs/glossary.md` from 2026-04-26 and
   `docs/architecture/overview.md` from 2026-05-19 as recently as 2026-07-27. That skew is repaired
   now, but it went undetected for ~3 months, and `git status` was its only visible symptom -- the
   exact failure mode CLAUDE.md documents under "HEAD/worktree skew". A periodic
   `git status --porcelain | grep -vE '^ M'` check would have caught it.

3. **The `M ` currently on `evidence/planning/igw_routine_log.md` is NOT skew.** Checked during
   triage: the index holds one line more than HEAD (`2026-07-28T07:22:49Z no eligible item...`),
   i.e. a live forward append by the IGW routine tick. Left alone.

---

## Does the ree-v3 coverage gap apply here?

Partly, and differently.

- **The claim-aware skip already exists for `REE_assembly`** and is the fix the ree-v3 triage
  proposed generalising. `runner_remote_control._active_claim_on_evidence_dir()` skips the
  heartbeat push when an active `TASK_CLAIMS.json` claim covers `evidence/` or `docs/claims/`.
  **It did not prevent any of these seven**, for a reason worth stating plainly: the five regen
  entries were produced by governance runs, and the two runner entries by the runner's own
  evidence writes. A claim-aware skip protects a *session's* uncommitted work from the runner; it
  does nothing about a long-running regen that rewrites 1100 files over several minutes with no
  claim open, and nothing about the runner stashing its own output.

- **The audit (fix (b)) is what actually worked.** `scripts/audit_stashes.py` found all seven on
  its first run, including entries that had sat 6.2 days. That is the load-bearing mitigation on
  this repo, and it should stay in the session-start and `/session-land` sweeps.

- **New, `REE_assembly`-specific gap:** a governance-cycle regen has no claim and no crash
  protection. If the runner heartbeat pulls mid-regen, the entire half-written derived-artifact set
  is stashed. Here that was harmless because the regen is idempotent -- rerun it. It becomes
  harmful only if a regen is ever committed *from* such a stash. `complicated (buildable)` fix:
  have `scripts/governance.sh` open a `TASK_CLAIMS` entry covering `evidence/` for its duration,
  which the existing skip already honours.

  **CLOSED 2026-07-28 -- landed on `origin/master` as `49d5c87922`** (session
  `gracious-snyder-aa4b35`; supersedes the IN FLIGHT note previously here, which said the file was
  still uncommitted). `scripts/governance.sh` now opens a `TASK_CLAIMS` entry over
  `REE_assembly/evidence/` (session_id `governance-sh-<host>`) as Step 0-pre and releases it from
  an exit trap on **every** path. Both subtleties that make it non-trivial are handled:

  - The `REE_assembly` heartbeat guard has **no `max_age_hours`**, so a leftover `active` entry
    gates the heartbeat push *indefinitely* -- hence `trap` on `EXIT` (covers `set -e` aborts, the
    Step 4b/9c blocking gates, any explicit exit) plus `INT`/`TERM`, which re-raise so the caller
    still sees the correct 128+N status.
  - The held-flag is armed **before** the `open` call, because `task_claim.py` writes the entry to
    disk and only then commits it, so a SIGINT inside that window leaves an `active` entry already
    gating the heartbeat while `open` exits non-zero. This was not theoretical -- it was **observed
    while testing the guard** (SIGINT during the open's git commit orphaned exactly such an entry).
    The close is therefore guarded on what is actually on disk rather than on the in-memory flag,
    which additionally **self-heals a leftover claim from a SIGKILLed earlier run** (the next run's
    `open` adopts it and the trap releases it -- verified).

  Verified against the real script: the claim is active mid-run and the heartbeat guard fires on
  that entry **alone** (checked in isolation, so other sessions' `evidence/` claims cannot make the
  check pass spuriously); the entry is closed with `closed_at` + `completion_note` on SIGINT
  (exit -2), SIGTERM (-15), a non-zero exit (7, status correctly propagated) and exit 0.

  **Residual hole -- CLOSED 2026-07-28 on the nudge side; the guard bound is deliberately NOT
  taken in the flat form, and the remaining piece is blocked.** `SIGKILL` / power loss still
  leaves an `active` entry, and because the `REE_assembly` guard is unbounded that entry gates the
  heartbeat push until a human clears it. The machine-obvious `governance-sh-<host>` session_id is
  what makes such an entry recognisable in the meantime.

  **The obvious follow-on -- bounding the guard with a `max_age_hours`, as
  `_active_claim_on_ree_v3_code` already does -- is only half a fix, and the missing half is the
  important one.** A bound converts a LOUD failure (the heartbeat visibly stops pushing) into a
  QUIET one: the heartbeat silently resumes, the protection has lapsed, nobody is told, and if a
  regen genuinely is still running the original autostash hazard returns unannounced. That is the
  same trade this document's own findings warn against -- cf. CLAUDE.md on the `M ` staged-revert
  skew being "the quieter and therefore worse one", and GOV-CAT-1, which exists because a verdict
  that was never *recorded* is invisible to the machinery built to act on it.

  It is worse than a hypothetical, because **nothing reports a stale `active` claim today at all.**
  `TASK_CLAIMS.json` declares `stale_after_hours: 6`, but the only consumer is
  `scripts/igw_routine_tick.py` (IGW auto-spawned claims); `scripts/prune_task_claims_done.py`
  states in its own docstring that it "Keeps all active claims" and warns only about `done` entries
  missing `closed_at` / `completion_note`. Measured 2026-07-28T18:05Z: **2 of 6 active claims were
  already past the 6h threshold (12.1h and 10.9h) with nothing anywhere surfacing them.**

  So the follow-on is *aging-out must produce a nudge*, on a **session-facing** surface --
  `prune_task_claims_done.py` (already advisory, already run at every `/session-land`) and the
  Session Startup Protocol -- **not** runner stdout, which is precisely how
  `experiment_runner._warn_on_stash_bloat()` failed (threshold 20 against a 5-entry incident,
  printed where no session sees it). The actionable content for an aged-out `governance-sh-*` entry
  is: *a regen was killed mid-write, so its half-written set may be sitting in a stash -- run
  `scripts/audit_stashes.py` and rerun the regen.* That makes the claim's own aging the trigger for
  the audit that is the load-bearing mitigation on this repo, closing the loop.

  Note the asymmetry when deciding whether to auto-reap. CLAUDE.md requires user confirmation
  before clearing a stale claim, because a heartbeat-stale session may still be RUNNING locally --
  that rule governs human/session claims and must stand. A `governance-sh-<host>` entry is
  different in kind: a regen takes minutes, so an hours-old one is definitionally abandoned, no
  human owns it, and the next `governance.sh` on that host already adopts and releases it. Those
  are safe to reap; session claims are not. It is therefore worth weighing whether to bound the
  guard at all, versus keeping the wedge loud and auto-reaping only the machine-owned entries.

  ### Resolution (2026-07-28, session `quirky-sinoussi-b9a180`)

  **The fork above was resolved AGAINST the flat bound, on measured evidence rather than
  preference.** The proposal was to bound the `REE_assembly` guard at the 6h `stale_after_hours`
  threshold, as `_active_claim_on_ree_v3_code` already does. Checked against the live file at the
  moment of writing, that bound would have de-protected **both** stale entries -- 12.3h
  `dazzling-dubinsky-dec79b` and 11.1h `zealous-merkle-f5dfc8` -- and **both were holding real
  uncommitted work in the shared `ree-v3` checkout at that instant** (325 modified lines across
  `runner_remote_control.py` + `experiment_runner.py`, plus one untracked contract test). A flat
  6h bound is therefore not a conservative simplification; on the day it was proposed it would
  have removed live protection from live work. The 6h figure answers "might a human still be
  working?" and the honest answer for this workspace is routinely yes.

  **What was taken instead -- a SHAPE-AWARE bound.** The two claim shapes get opposite treatment,
  keyed on the one property that actually distinguishes them:

  * **`governance-sh-*` locks are bounded tightly** (`GOVERNANCE_REAP_HOURS = 2.0`). A regen is a
    minutes-long derive-only pipeline, so 2h is ~an order of magnitude above any live run -- no
    running regen is reaped even on a loaded machine -- while a killed one stops wedging the
    heartbeat the same working day. This is the only shape the residual hole is actually about.
  * **Session claims stay UNBOUNDED.** The wedge stays loud for exactly the case where a silent
    lapse would be dangerous, preserving CLAUDE.md's confirm-before-clearing rule and the standing
    memory `feedback_heartbeat_stale_not_abandoned`.

  So the quiet-failure trade the section above warns against is never taken: the only claim that
  can now age out of the guard is one that is abandoned by construction.

  **And the aging-out is not silent, which was the actual requirement.**
  `scripts/prune_task_claims_done.py` (REE_Working, + `scripts/test_prune_task_claims_stale_active.py`,
  15 tests) now:

  * **reaps** `governance-sh-*` locks past the same `GOVERNANCE_REAP_HOURS`, writing a
    `completion_note` that records it was reaped as stale, by what, and that the regen did NOT
    complete -- and **announces it** with the two follow-up actions: `scripts/audit_stashes.py`
    (the load-bearing detector) and a rerun of the idempotent regen. The claim's own aging is thus
    the trigger for the stash audit, which is the loop this thread wanted closed;
  * **reports, and never closes,** stale session claims and undatable ones, each with the remedy
    that fits it.

  One threshold with one meaning: the age at which the guard would stop honouring a governance
  lock is the same age at which the pruner reaps and announces it, on the session-facing surface
  (`/session-land` housekeeping, Session Startup Protocol step 3) rather than runner stdout -- the
  `_warn_on_stash_bloat()` failure mode. Exit 0 always; it must never block a close. The reap is
  safe against a racing regen for a second reason too: `gov_claim_close` is guarded on
  `gov_claim_is_active`, so a reaped entry makes the exit trap a clean no-op.

  A negative control found a real gap during implementation rather than by inspection: under
  `--no-reap` a stale governance lock was reported by neither path, reproducing the exact silence
  this work exists to remove. It is now its own reported bucket.

  **STILL OPEN -- the guard-side half is blocked, not skipped.** Applying the shape-aware bound
  means editing `ree-v3/runner_remote_control.py`, and every line it must touch
  (`_active_claim_on_paths`, `_claim_age_hours`, `_active_claim_on_evidence_dir`'s docstring)
  exists **only as session `zealous-merkle-f5dfc8`'s uncommitted working-tree change** -- none of
  it is on `origin/main`. Committing that file would land ~176 lines of another session's
  in-flight work under a foreign message (CLAUDE.md read-modify-write contamination) *and* break
  its coupled set (CLAUDE.md remedy (a2)): `_active_claim_on_ree_v3_code` would land on trunk
  without its caller in `experiment_runner.py` or its new untracked contract test
  `tests/contracts/test_ree_v3_pull_claim_guard.py`. Deferred deliberately. The change to make,
  once that session lands:

  ```python
  # in _active_claim_on_paths: bound only the machine-owned locks
  _GOVERNANCE_LOCK_PREFIX = "governance-sh-"
  _GOVERNANCE_CLAIM_MAX_AGE_HOURS = 2.0   # keep in sync with
  # REE_Working/scripts/prune_task_claims_done.py GOVERNANCE_REAP_HOURS
  ```

  applied per-entry (a `governance-sh-*` entry past that age does not gate; every other entry is
  unbounded exactly as today), plus a rewrite of `_active_claim_on_evidence_dir`'s docstring,
  which currently states the 2026-07-28 generalisation kept "no age bound ... on purpose, so
  REE_assembly behaviour is bit-identical" -- that deliberate decision is what this narrows, and
  the docstring must say so rather than be silently contradicted.

  The sibling ree-v3 gap -- fix (a) of the ree-v3 triage, extending the claim-aware skip to the
  ree-v3 pull itself, which is what produced all five of *that* repo's entries -- is the same
  in-flight session `zealous-merkle-f5dfc8`.
