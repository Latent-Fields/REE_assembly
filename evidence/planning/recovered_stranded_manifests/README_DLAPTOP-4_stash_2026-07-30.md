# Orphaned-autostash grade -- DLAPTOP-4 (the Mac), 2026-07-30

**Graded:** 2026-07-30T07:40Z -- 07:52Z, session `nostalgic-yalow-da4b15`
(chip `chip-20260730-dlaptop4-stash-triage`)
**Source:** `DLAPTOP-4.local`, `/Users/dgolden/REE_Working/REE_assembly` @ `origin/master`
`6d9b22668a` and `/Users/dgolden/REE_Working/ree-v3` @ `origin/main` `37012de11e`.

**This is the STASH half of the Mac's triage.** The working-tree half is
[`README_DLAPTOP-4_2026-07-30.md`](README_DLAPTOP-4_2026-07-30.md) (session
`great-hopper-1d7b24`, earlier the same morning), whose closing section names exactly this
gap: *"Not examined here (different chip, different tool): the Mac's git stash list."*
Read the two together -- the cloud-2 write-up's central point is that stash grading and
working-tree grading are different checks, and neither substitutes for the other.

Fourth and last box in the series: [`README.md`](README.md) (ree-cloud-3),
[`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) (ree-cloud-2 + the
V3-EXQ-614 find), [`README_ree-cloud-4_2026-07-30.md`](README_ree-cloud-4_2026-07-30.md).

**Nothing was recovered, because nothing was stranded.** No file was moved, copied,
created, deleted or reverted in either checkout. The only mutation was three
`git stash drop`s, each preceded by an archive tag and by positive proof of containment.

---

## Headline: CLEAN -- all 3 autostash entries fully contained on `origin/master`

| Surface | Result |
|---|---|
| `REE_assembly` stash list | **3 entries, all `autostash`, all contained** -> archived + dropped |
| `ree-v3` stash list | **0 entries** |
| `REE_assembly` untracked (`??`) | **0** |
| `ree-v3` untracked (`??`) | **1**, live claimed work -- a note, not a finding |
| Untracked component of any stash (`stash@{N}^3`) | **none exists on any of the 3** |
| `count-objects` garbage / `gc.log` | 0 garbage, no `gc.log`, both repos |

`scripts/audit_stashes.py` now reports both repos clean.

| slot | stash SHA | taken | files | archive tag (local-only) |
|---|---|---|---|---|
| `stash@{0}` | `b534f1e7f3` | 2026-07-29 23:38:38 +0100 | 1128 | `stash-archive/20260730-b534f1e7f3` |
| `stash@{1}` | `cd7c3c881f` | 2026-07-29 21:56:26 +0100 | 2 | `stash-archive/20260730-cd7c3c881f` |
| `stash@{2}` | `29e8334256` | 2026-07-29 20:39:51 +0100 | 1131 | `stash-archive/20260730-29e8334256` |

All three tags verified to resolve with a readable tree **after** the drops. The stash
reflog is now empty, so those tags are the only thing keeping the commits reachable --
do not delete them without re-grading.

---

## The Mac's fault class really is different, and it changes what "clean" means

The chip's framing is right and worth preserving. The three cloud workers' orphans were
`runner-prepull-untracked` -- residue of `_prepull_stash_blocking_untracked()` when a
`git pull` failed all three retries. The Mac's are `autostash`, taken by the runner
heartbeat's `git pull --rebase --autostash` against `REE_assembly`, which is the class
that silently orphans **a live session's uncommitted work** with no error reaching the
owning session.

So the question here was not "is this completed-run evidence that never reached origin?"
but "is this a session's work that was swept out from under it?" The answer is a
qualified no, and the qualification is the interesting part:

**All three stashes ARE swept session work -- and all three are derive-only regen output.**
Every path across all 1131 of them is a generated artifact. There is no substrate code, no
`*_plan.md`, no experiment script, no hand-authored planning prose, and no run manifest:

- **1113 x** `evidence/experiments/*/INDEX.md` (per-experiment index rebuild)
- `evidence/experiments/{INDEX.md, claim_evidence.v1.json, conflicts.md, TODOs.md,`
  `promotion_demotion_recommendations.md, pending_review.md, arm_fingerprint_index.json,`
  `substrate_status_snapshot.json}`
- `evidence/decisions/decision_state.v1.json`
- `evidence/planning/{INDEX.md, ARCHITECTURE_GAP_REGISTER.md, architecture_gap_register.v1.json,`
  `evidence_backlog.v1.json, experiment_proposals.v1.json, experiment_proposals_index.v1.json,`
  `inter_governance_workset.md, inter_governance_workset.v1.json}`

i.e. two interrupted `governance.sh` / `build_experiment_indexes.py` regens (the 1128- and
1131-file entries) and one `igw_routine_tick.py` tick (the 2-file entry). That is what the
governance pipeline being **derive-only** buys: a swept regen costs a re-run, not
information. Had any of these carried a `_plan.md` edit or a substrate change, the correct
action would have been to surface it to the user unpopped, not to drop it.

## Containment grading: identifier sets, not bytes

Byte comparison is useless on this content -- **1131 of 1131 paths differ from
`origin/master`** in every stash, because a regen moves timestamps, counts and ordering on
every file it touches. Grading on that would have reported 100% loss. The method's
"compare parsed JSON, not bytes" caution generalises here to *compare identifier sets*:

| identifier set | origin | `stash@{2}` | `stash@{1}` | `stash@{0}` | absent on origin |
|---|---|---|---|---|---|
| `claim_evidence.v1.json` run ids | 3643 | 3631 | 3626 | 3637 | **0 / 0 / 0** |
| `arm_fingerprint_index.json` keys | 2201 | 2087 | 1991 | 2111 | **0 / 0 / 0** |
| `evidence/experiments/` experiment dirs | 1147 | 1143 | 1143 | 1145 | **0 / 0 / 0** |
| IGW workset item ids | 246 | 243 | 243 | 243 | **0 / 0 / 0** |
| IGW workset `stable_hash` | 243 | 240 | 240 | 240 | **0 / 0 / 0** |
| `decision_state.v1.json` nested items | 274 | 271 | 271 | 271 | -- |

`origin/master` is a **strict superset in every dimension**, and leads on every count. A
later regen (the one whose output is in the working tree as ~1135 live ` M` files right
now) supersedes all three again.

Aggregate token sweep over every path of every stash, for
`v3_exq_*` / `V3-EXQ-*` / `v2_exq_*` / `v1_exq_*`, cross-checked against `origin/master`'s
version of the same paths: **exactly one** token appeared to be absent, and it was a false
positive worth recording (below).

### The one apparent find -- `V3-EXQ-836b` -- and why it is not one

`V3-EXQ-836b` appears in `stash@{2}` and `stash@{1}` but not in `origin/master`'s copy of
those files. It is present in the workset **header**, not in an item:

```
- Live EXQs: V3-EXQ-687a, V3-EXQ-798a, V3-EXQ-833, V3-EXQ-836b
```

That is a *transient snapshot of what was running when the IGW tick fired* (20:39Z and
21:56Z on 2026-07-29). 836b finished, so it is correctly absent from the current workset.
Its evidence is complete on `origin/master` -- flat manifest, run pack
(`runs/v3_exq_836b_..._20260729T210911Z_v3/{manifest.json,summary.md}`), `experiment.md`,
`INDEX.md`, `claim_evidence.v1.json`, `review_tracker.json`, `claims.yaml`, and both a
`failure_autopsy_v3-exq-836b_2026-07-29` pair and the MECH-476/MECH-475 cluster autopsy.
Nothing to recover.

**Generalisable caution:** an ephemeral "currently live" telemetry field inside an
otherwise-derived artifact will read as absent-on-origin the moment the thing it names
stops being live. Grade a token hit by asking *where in the file it sits* before treating
it as content. The same shape will recur on any future stash carrying an IGW workset.

### `V3-EXQ-592b` was specifically looked for. It is not here.

The chip flags 592b as the known-unrecoverable DLAPTOP-4 run from the 2026-05-30 cluster
(siblings 490h and 614 were recovered from cloud workers on 2026-07-30). A `592b` substring
search does hit 3 times in `arm_fingerprint_index.json` -- **all three are coincidental
substrings inside SHA-256 arm fingerprints** (`...7d8e253f2f592b1384fe7dac`, etc.), and all
three are byte-identical in the stashes and on origin. There is no 592b manifest, run pack,
or fingerprint entry in any stash. 592b remains unrecovered; the Mac's stash list is not
where it is.

This is the second independent falsification of the 2026-05-30-sweep-touched-the-Mac
hypothesis, after the working-tree half's `find -name '*.bak*'` pass.

---

## The `ree-v3` untracked file is live work -- deliberately untouched

`ree-v3/coordinator/deploy/runner-prestart-pull.sh` (5371 bytes, `Jul 30 08:49` local, i.e.
~1 minute before it was graded) is untracked, absent from `origin/main`, and absent from
all `ree-v3` history. On a worker that signature would be a finding. Here it is
**in-flight work**, owned by active claim `friendly-antonelli-b0f414` (opened
2026-07-30T07:45:37Z, resources `ree-v3/experiment_runner.py` + `ree-v3/coordinator/deploy`,
task: *"Close the cold-boot stale-code window: refresh ree-v3 before ree-runner.service
loads experiment_runner.py"*). Its own header documents the 2026-07-30T06:51Z / 07:35Z
incident it closes. Left strictly alone; **not** copied into this directory, which would
have duplicated a live session's work under a recovery filename.

This mirrors the working-tree half's V3-EXQ-748a note. On the Mac the discriminator between
"strand" and "live work" is `TASK_CLAIMS.json`, not the git state -- both look identical to
a grader. Check the claims file before grading any Mac untracked file as a finding.

## Procedure notes

- **Archive-tag-first, by SHA, in one pass** -- all three SHAs resolved and tagged before
  anything else ran. Dropping then re-resolved the live stash list on **every** iteration
  and re-verified `stash@{N} == expected SHA` plus the presence of the archive tag before
  each `drop`. With 18 concurrent sessions on this box, `stash@{N}` is racy in a way that
  a fixed list of slot numbers is not safe against.
- **`zsh` does not word-split unquoted parameters.** A `for x in $LIST` drop loop ran
  exactly once, on the whole string, and correctly refused (`not in live stash list`)
  rather than dropping something unintended. Enumerate literals, or use an array.
- **Never `git checkout -- .` and never a blanket restore here.** The tree carried ~1135
  live ` M` files (another session's in-flight regen) throughout.
- **Per-file `git show` does not scale to 1131 x 2 paths** -- it timed out at 2 minutes.
  `git diff --name-only <stash> origin/master -- <paths>` for the differ-set and
  `git grep -h -o -E <pattern> <rev> -- <paths>` for tokens both run in-process and
  complete in seconds.

## Residual gap

Unchanged from the working-tree half: `runner_git_health.py`'s `FLEET` dict still has no
`DLAPTOP-4` entry, so **the Mac is graded only by manual one-offs like this pair of
documents.** With all four boxes now swept, the series is complete as a point-in-time
exercise; nothing automated will notice the next Mac autostash orphan. The heartbeat's
claim-aware skip (`evidence/` + `docs/claims/`) is the preventive control, and it is
adoption-dependent -- it only fires when the session registered its claim *before* opening
the file.
