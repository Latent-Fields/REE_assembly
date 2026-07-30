# Stranded-manifest grade -- DLAPTOP-4 (the Mac), 2026-07-30

**Graded:** 2026-07-30T07:26Z -- 07:29Z, session `great-hopper-1d7b24`
(chip `chip-20260730-dlaptop4-untracked-grade`)
**Source:** `DLAPTOP-4.local`, `/Users/dgolden/REE_Working/REE_assembly` @ `origin/master`
`a6ca2a5762` and `/Users/dgolden/REE_Working/ree-v3` @ `origin/main` `3f5af1f`.

Third box in the series after [`README.md`](README.md) (ree-cloud-3, 2026-07-29) and
[`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) (ree-cloud-2 +
the V3-EXQ-614 find on ree-cloud-4). The cloud-2 write-up says in as many words
"the lesson to carry to `ree-cloud-4` / `DLAPTOP-4`"; cloud-4 was covered the same day,
this closes the Mac.

**Nothing was recovered, because there was nothing to recover.** No files were moved,
copied, deleted or reverted. The checkout was read-only throughout -- ~13 concurrent
Claude sessions had live uncommitted work in it.

---

## Headline: CLEAN -- zero stranded run manifests on the Mac

| Surface | Result |
|---|---|
| `REE_assembly` main checkout, untracked vs `origin/master` | **0 findings** (0 untracked) |
| `ree-v3` main checkout, untracked vs `origin/main` | **0 findings** (1 untracked, a note) |
| 8 worktrees of both repos (5 x REE_assembly, 3 x ree-v3) | **0 findings** |
| 47 **gitignored** files in `REE_assembly` (grader-blind, see below) | **0 run manifests** |
| 40 `_runner_signals/*.json`, graded by derived run id | **40/40 present on origin** |

**The 2026-05-30-sweep hypothesis is FALSIFIED for this box.** Both previously known
stranded manifests were `.bak.20260530` files, i.e. residue of one sweep, and the chip
raised the possibility that the same sweep touched the Mac. A direct filesystem sweep
(`find -name '*.bak*'`, which does not depend on git's view) found the only
`.bak.20260530` files on this machine to be the **already-recovered** ones sitting in
this very directory, plus two identical copies visible through
`REE_assembly/.claude/worktrees/{fervent-benz-b5cbaa,compassionate-curie-c75e63}` --
which are worktree checkouts of those same now-tracked files, not independent residue.
The Mac carries no sweep residue.

### Method

Reused the existing grader rather than writing a new one, per the chip. `UNTRACKED_PY`
was extracted from `REE_assembly/scripts/runner_git_health.py` and run directly:

```bash
/opt/local/bin/python3 -c "import sys;sys.path.insert(0,'/Users/dgolden/REE_Working/REE_assembly/scripts');import runner_git_health as m;print(m.UNTRACKED_PY)" > /tmp/grader.py
/opt/local/bin/python3 /tmp/grader.py /Users/dgolden/REE_Working REE_assembly:origin/master ree-v3:origin/main
```

Both repos were `git fetch`ed first. Worktrees were graded by importing `grade_repo`
from the same extracted source and pointing it at each `git worktree list` path.

### The one `ree-v3` note is live work, not a strand

`experiments/v3_exq_748a_mech457_hrep_zworldp0_rederivation.py` is untracked and absent
from `origin/main`. It is owned by active claim `quirky-mayer-ee5ad2`
("queue-experiment: V3-EXQ-748a", opened 2026-07-30T06:54:47Z) -- an in-flight
`/queue-experiment` session, correctly a `no_counterpart_other` note and not a finding.

---

## Three things worth carrying forward to `runner_git_health.py`

The grade came back clean, so the durable value of this exercise is in what the grading
exposed about the grader itself. All three are Mac-observed but none is Mac-specific.

### 1. A transient false positive appeared and self-resolved within minutes

The first run produced exactly one `REE_assembly` finding:
`evidence/experiments/_dry_v3_exq_748a_mech457_hrep_zworldp0_rederivation_20260730T072554Z_v3.json`
(`outcome=FAIL`, `elapsed_seconds=17.4`). Its timestamp was ~30 seconds before the run.
It was the **dry-run output of the live V3-EXQ-748a smoke test** above, and it was gone
by the next grade, which returned `untracked: 0`.

This is the chip's "expect more noise than a worker" caution playing out exactly, with a
useful addition: the noise was **self-clearing**, and an `_dry_`-prefixed manifest with a
sub-20-second `elapsed_seconds` is cheap to recognise. A future local grade should
re-run once before acting on any finding whose timestamp is minutes old.

### 2. `*.bak` is gitignored in `REE_assembly`, so the grader is blind to plain-`.bak` files

`REE_assembly/.gitignore:13` is `*.bak`. The grader selects candidates from
`git status --porcelain -uall`, taking only `?? ` entries -- and git reports ignored
files as `!! `, never `?? `. So **any plain-`.bak` file is invisible to it in this repo.**

The blind spot is narrower than it first looks, and that is the reassuring part: the
glob `*.bak` matches only names *ending* in `.bak`, so `foo.json.bak.20260530` does
**not** match it and the actual stranded class stays visible -- which is why the
cloud-2 and cloud-4 finds worked. Graded by hand here, the full ignored set is 47 files
and contains **no run manifests**: 28 `.DS_Store`, 7 cache dirs
(`__pycache__` / `.pytest_cache`), `.claude/`, `runner.log`, `coordinator.env`,
`coordinator_shadow.log`, `scratch/`, three local reports, plus
`evidence/planning/experiment_proposals.v1.json.bak` -- the one plain-`.bak` file, and
not a manifest (keys are `generated_at_utc` / `items` / `schema_version` /
`source_backlog`; no `run_id`, no `outcome`).

Suggested hardening: grade `--ignored=matching` as a separate, lower-severity bucket
rather than leaving the class unexamined.

### 3. `_runner_signals/*.json` would fire as ~40 false findings on any box where it is not gitignored

`evidence/experiments/_runner_signals/` holds 40 files on the Mac, each carrying **both**
`run_id` and `outcome` -- which is precisely the grader's test for "this is a run
manifest". They are not manifests; they are runner exit signals that *point at* one
(`manifest_path`, `exit_reason`, `pid`, `queue_id`, `script`).

Here they are inert because `.gitignore` hides them. But the grader's `BYDESIGN` list
covers `_per_tick.jsonl`, `runner_status/`, `runner_commands/` and `runner_heartbeats/`
and **not** `_runner_signals/`. On any box where that directory is untracked rather than
ignored, the probe would emit up to `MAX_FINDINGS` (25) findings and a `truncated` tail,
all spurious -- exactly the "probe that false-positives on ordinary runner churn gets
ignored" failure its own module docstring warns about. **Suggested fix: add
`(^|/)_runner_signals/` to `BYDESIGN`.**

Graded here anyway, as the most direct available check on this machine's runner history:

- **Grade by the `run_id` field and you learn nothing** -- it is present in the schema but
  **empty in 36 of 40** signals. A first pass scored those 36 as "not on origin", which
  was measuring an absent key rather than a stranded run. Derive the run id from the
  `manifest_path` basename instead.
- Graded that way, **40 of 40 resolve to a run id present on `origin/master`** (checked
  against both flat `<run_id>.json` and pack `.../runs/<run_id>/manifest.json`: 1959 flat
  and 2666 pack ids on origin). Zero stranded.
- Coverage runs 2026-06-03 through 2026-07-30T01:06Z (V3-EXQ-798a), so this is an
  independent confirmation across the Mac's recent runner history and not just a
  point-in-time working-tree snapshot.
- One signal, `V3-EXQ-461c`, has `manifest_path` pointing at a file no longer on disk
  while its run id **is** on origin -- the run landed and the local copy was later
  cleaned. Correct behaviour, not a loss.

---

## Residual gap (not closed by this exercise)

`runner_git_health.py`'s `FLEET` dict still contains only `ree-cloud-1..4`. **The Mac has
no entry, so it is still not graded on any automated pass** -- this document is a manual
one-off. Adding a local target would need the probe to handle a non-ssh, non-`REE_Working_runner`
path layout, which is a real change rather than a dict entry, and was out of scope for a
grade-only chip. Anyone re-triaging the Mac should start from this file rather than from
scratch.

Not examined here (different chip, different tool): the Mac's **git stash list**. Stash
containment is `scripts/audit_stashes.py`; the cloud-2 write-up's central point is that
stash grading and working-tree grading are different checks, and this exercise is the
working-tree half only.
