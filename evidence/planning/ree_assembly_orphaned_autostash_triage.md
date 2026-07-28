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
| 0 | 2026-07-27 15:21 | `95b7594f49` | governance regen, 1186 files | SUPERSEDED (regenerable) + **stale-content skew** | left in place |
| 1 | 2026-07-27 15:20 | `07a5621a02` | near-duplicate of #0, 1186 files | SUPERSEDED (regenerable) + **stale-content skew** | left in place |
| 2 | 2026-07-26 08:58 | `4a081fbd57` | governance regen, 1130 files | SUPERSEDED (regenerable) | left in place |
| 3 | 2026-07-26 08:58 | `455475f8b2` | 1 untracked V3-EXQ-823 manifest | **ALREADY-LANDED (proven)** | **DROPPED** |
| 4 | 2026-07-26 00:56 | `995de28f5b` | governance regen 1120 + 20 untracked | SUPERSEDED (regenerable); **all 20 untracked verified on trunk** | left in place |
| 5 | 2026-07-22 04:00 | `370ca49bb5` | `graceful_timeout.py` + V3-EXQ-790 run pack | **ALREADY-LANDED (proven)** | **DROPPED** |
| 6 | 2026-07-22 03:56 | `8f92e7b559` | governance regen, 1063 files | SUPERSEDED (regenerable) | left in place |

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

**Two dropped, five left in place. The stash list went 7 -> 5.**

The two-pass split from the ree-v3 triage is preserved deliberately:

1. **Dropped without asking -- mechanically proven contained:**
   - `370ca49bb57e7b574e5d1e5b7800cd46a9ed3b39` (6 files; `graceful_timeout.py` byte-identical to
     trunk, run pack present, manifest key-for-key identical)
   - `455475f8b2a349874887eb91336c92570193ef73` (1 untracked manifest; trunk is a strict superset)
2. **Left in place, reported, awaiting the owner's call -- the five regen entries.** Their verdict
   rests on the derived-artifact argument (test 4) plus the stale-content direction test (test 5).
   Both are strong, and the `95b`/`07a` pair is arguably *safer* to drop than the two that were
   dropped, since applying them would actively damage trunk. But it is still an argument, so it is
   the owner's decision:
   - `95b7594f495c91f17f34a857a1323e8d5a08fa82`
   - `07a5621a02b2a47173977e071fe8dc341578ca38`
   - `4a081fbd5776846bdc80d974f6781a0870f776dc`
   - `995de28f5bde53affa5a75348e8d02cabf522f25`
   - `8f92e7b5596a7d39f9c1ef4dfce28eb292bcda59`

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
that a tag exists: `stash-archive/20260722-370ca49b` still lists its 5 tracked files + 1 untracked,
and `stash-archive/20260726-455475f8` still lists its 1 untracked file.

Tags keep the commits reachable so `git gc` cannot prune them. Recover with
`git stash apply stash-archive/<tag>` or `git show <tag>:<path>`. **Local-only and never pushed** --
verified `git ls-remote --tags origin 'stash-archive/*'` = 0. **Do not bulk-delete these tags;**
deleting them is the one action that would actually destroy the content.

---

## Incidental findings (reported, not actioned)

1. **`graceful_timeout.py` vendor drift.** The module's own banner states that the three copies
   (`ree-v3/graceful_timeout.py` canonical, `REE_assembly/graceful_timeout.py`,
   `REE_Working/scripts/graceful_timeout.py`) are byte-identical and "`shasum` over all three must
   match". They do not: `REE_assembly`'s copy (`9cc5f0b9e6`) is missing the 23-line
   VENDORED COPY banner that `ree-v3`'s canonical copy (`6b05cc02bd`) carries. **The module body
   below the banner is identical** -- the drift is documentation only, so there is no functional
   divergence, but the banner's own `shasum` check is currently false. Not fixed here (out of
   scope); worth a one-line re-vendor.

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
  harmful only if a regen is ever committed *from* such a stash. `complicated (buildable)` fix if
  anyone wants it: have `scripts/governance.sh` open a `TASK_CLAIMS` entry covering `evidence/` for
  its duration, which the existing skip already honours.
