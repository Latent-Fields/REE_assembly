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

## Residual gap -- **CLOSED 2026-07-30 (working-tree half 17:34Z, stash half 18:09Z)**

~~Unchanged from the working-tree half: `runner_git_health.py`'s `FLEET` dict still has no
`DLAPTOP-4` entry, so **the Mac is graded only by manual one-offs like this pair of
documents.**~~ With all four boxes now swept, the series is complete as a point-in-time
exercise.

`DLAPTOP-4` is now a first-class `runner_git_health.py` target, probed in-process
(session `elastic-merkle-e0cca8`, chip `chip-20260730-githealth-local-mac-target`) -- so
the **working-tree** half of this pair is repeatable: `runner_git_health.py --host mac`.

~~**Read the split carefully, because the two halves closed unequally.**~~ **The stash half
is now closed too, 2026-07-30T18:09Z** (session `quirky-mayer-ee5ad2`, chip
`chip-20260730-mac-autostash-content-grading`). `runner_git_health.py` still only reports
the stash COUNT -- that part is unchanged and is a pointer, not a grade -- but
**`scripts/audit_stashes.py` now grades each entry's CONTENT**, so a session no longer has
to hand-triage an orphan to find out whether it holds unlanded work.

Every entry carries a `grade:` line: **CONTAINED / NOT CONTAINED / HAND-AUTHORED /
UNGRADEABLE**, computed by identifier-set containment against origin. It is on by default
(`--no-grade` opts out), never mutates anything, and still exits 0. The design and its
rationale live in the `CONTAINMENT GRADING` block of the script; the pins are
`scripts/test_audit_stashes_containment.py` (27 tests, time-independent, real `git stash`
in a tempdir).

**This document's own method is what it automates**, and the three archive tags above are
its end-to-end validation: replayed through the grader, all three come back **CONTAINED**
in ~1s each, with `n_identical == 0` -- i.e. the verdict is reached *despite* total byte
divergence, which is the case a byte comparison gets exactly backwards.

**Building it against these real entries found four false-positive classes that grading by
this document's table alone would have produced.** Recording them because the table above
reads as more settled than it is. **A fifth was found the same day by triaging the tool's
own first finding, and it is written up below** -- the count is a running tally, not a
closed list:

1. **IGW item `id` is not an identifier.** The table grades item ids and reports 0 absent --
   true only because the grading ran the SAME DAY. Ids are dated slot labels
   (`IGW-20260729-001`), regenerated wholesale each tick, so a day later **all 241** read as
   absent in all three entries. `stable_hash` is the content identity and produced zero
   misses. Grade on `stable_hash` only.
2. **An IGW `stable_hash` absence is advisory, not load-bearing.** One day on, 5 items had
   completed and dropped out. Treating that as NOT CONTAINED would redden every
   `REE_assembly` entry older than a day. Arm fingerprints are deliberately kept
   load-bearing -- a dropped fingerprint is a lost reusable arm.
3. **A run can be dropped from `claim_evidence.v1.json` while its pack sits on origin.**
   Grading run ids only against the registries reported **1021** spurious absences on the
   2026-07-27 tags, all of them V1/V2-era runs with complete packs on origin. The reference
   set now includes origin's `runs/<run_id>/` directory names and `review_tracker.json`.
4. **The run-id token shape missed a whole generation.** The V1/V2 form
   (`2026-02-13T224000Z_commit-dual-error-channels_seed11`) matched nothing, so that
   generation was invisible to the sweep.

~~**One real strand surfaced, and it is NOT from this document's three entries.**~~
**TRIAGED 2026-07-30T18:23Z (session `relaxed-montalcini-eb02e1`, chip
`chip-20260730-exq825-stranded-stash-runs`): NOT a strand. It is false-positive class 5,
and the grader has been taught it.** Nothing was ever lost and nothing needed recovering.

The 2026-07-27 archive tags (`stash-archive/20260727-07a5621a` and `-95b7594f`) do carry
`claim_evidence` entries for two V3-EXQ-825 runs --
`v3_exq_825_mech245_generative_dominance_deafferentation_20260726T151207Z_v3` and
`...T151439Z_v3` -- that appear nowhere on `origin/master`. **They are `--dry-run` smokes,
and their absence is the INTENDED end state.** Both were produced on `DLAPTOP-5.local` with
`dry_run: true`, 1 seed (`eval_seeds: [0]`) and truncated windows (`t0=8`, `t1=6` against
the real run's `50`/`30`), which is exactly the smoke the queue entry's own note
pre-declares: *"--dry-run smoke PASS (crash-free, writes manifest+sentinel; FAIL outcome
expected under truncated smoke windows)"*. Both graded FAIL / `weakens`.

**Chain of custody, end to end.** `de0c34a3cb` (2026-07-26) committed both smokes' packs to
`master`; `cb7298c1c4` (2026-07-28) made the pack converter and the indexer refuse smokes
and **deleted this pair outright, packs AND flat manifests**, its message naming the same
two runs as confirmed MECH-245 contamination; `5189800eea` regenerated the index the same
morning, dropping 22 dry-run entries and moving MECH-245 `fail_runs` 2 -> 0 and
`experimental_confidence` 0.571 -> 0.771. The stash tags were taken 2026-07-27, i.e.
*between* the two -- which is the entire reason they still hold content `master` has since
correctly purged.

**V3-EXQ-825 itself ran once and PASSED.** The coordinator DB (authoritative; the manifest
scan is structurally blind here) holds exactly one `results` row for the queue id -- `PASS`,
received `2026-07-26T15:21:04Z`, committed `15:23:25Z` -- and the `experiments` row is
`status=completed`, `removal_reason=PASS`. That is run
`...T152102Z_v3`, executed on `ree-worker-3` (`linux-x86_64`), and it is on `origin/master`
with a full `runs/<run_id>/` pack. **Neither stranded id has a DB row at all**, so this is
also not a phantom completion -- a phantom is a DB `completed` row with no
manifest; here it is the mirror image, manifests with no DB row, because a `--dry-run` never
reports a result to the coordinator.

**Class 5: a deliberately-purged artifact reads as an absence.** The grader asks "is this
identifier on origin", which cannot distinguish *lost* from *correctly deleted* -- so it
reported the fix as the loss. `scripts/audit_stashes.py` now suppresses any run id the
entry's own tree marks `dry_run: true` at `evidence/experiments/_dry_<run_id>.json`, in
**both** the struct pass and the token sweep, and prints a `dry-run smoke (absence is
intended)` line rather than dropping it silently. Replaying the two tags now yields **0**
run-level findings (the 3 residual are arm fingerprints, deliberately load-bearing), in the
same ~1.2s.

**The sweep is now CLOSED, not merely this case.** Replaying **all 66** `stash-archive/*`
tags in `REE_assembly` after the fix gives **0 run-level absences across the whole set** (8
dry-run suppressions, all of them the 4+4 on these two tags; the only remaining `missing`
entries anywhere are arm fingerprints). So the answer to "is any experimental evidence
stranded in the stash archive" is **no**, and that is now a measured statement over every
tag rather than an inference from three of them. Re-measure after adding tags; the replay is
~1.2s per tag.

Two things that fix got wrong first and are now pinned:

- **Probe the entry's TREE, not its changed-path list.** A stash entry lists only what it
  MODIFIED, and here the `_dry_` manifests were already committed at the stash's base and
  untouched by it -- present in `git ls-tree` of the entry, absent from `entry_files`. The
  first implementation scanned the changed paths and suppressed nothing at all.
- **Never trust the `_dry_` filename alone.** The blob must actually say `dry_run: true`.
  This matters because of the coupling `cb7298c1c4` flagged: the flat manifest is the ONLY
  carrier of the flag, since the pack it produced has no `dry_run` field.

Pins: `scripts/test_audit_stashes_containment.py` (35 tests, was 27), including both traps
above, a negative control where a `_dry_`-named file with `dry_run: false` suppresses
nothing, and one asserting an arm fingerprint is never suppressed.

**What has NOT changed:** which identifiers matter is still a per-artifact judgement, and
the classifier is a deliberately minimal **allowlist** of the current governance regen.
Replaying the older tags (2026-06-17 .. 2026-07-09) grades them HAND-AUTHORED on
superseded-era derived paths -- the safe direction, and the same replays correctly surfaced
genuinely hand-authored content (`build_experiment_indexes.py`,
`docs/architecture/effort_dissociation_env.md`) in those same entries. Extending the
allowlist requires naming the generator that writes the path.

Two things from this document DID land in the probe, both from the section above on the
`ree-v3` untracked file:

- **`TASK_CLAIMS.json` is the discriminator, not git state.** An untracked path covered by
  an ACTIVE claim now grades as a note naming the owning session. This document's
  `runner-prestart-pull.sh` -- untracked, absent from `origin/main`, absent from all
  history, and live work under claim `friendly-antonelli-b0f414` -- is the selftest's
  worked case.
- **Never `git checkout -- .` on this tree.** The probe is strictly read-only, and its
  stranded-manifest ACTION block now says so explicitly for the multi-session box.

The heartbeat's claim-aware skip (`evidence/` + `docs/claims/`) remains the preventive
control, and it is adoption-dependent -- it only fires when the session registered its
claim *before* opening the file.
