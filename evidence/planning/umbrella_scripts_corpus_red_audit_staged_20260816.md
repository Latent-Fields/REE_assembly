# Umbrella `scripts/` test corpus: trunk-red audit

Staged 2026-08-16T12:51:07Z. Box `ree-cloud-5` (linux, `/opt/local/bin/python3`).
Chip `chip-20260816-trunk-red-igwreap-govflag`.
Session `metaworker-chip-20260816-trunk-red-igwreap-govflag`.

All measurements below were taken against **unmodified throwaway worktrees of
`origin/master`** (`git worktree add --detach`), never a local tree.

---

## 1. Headline finding: nothing runs this corpus, and it has been red for a while

`REE_Working/scripts/` holds **100 `test_*.py` files** (~1800 tests). There is
**no runner, no CI workflow, and no documented invocation for any of them.**

- `scripts/remote_pytest.sh` is `ree-v3`-only. Its default test roots are
  `tests/`, `coordinator/`, `dispatch/` and three named files -- **all resolved
  inside `ree-v3`**. The umbrella repo is not among them, and the wrapper
  rsyncs a `ree-v3`-shaped tree.
- The `PreToolUse` commit guards in `.claude/settings.json` run
  `ree-v3/validate_queue.py` and `ree-v3/scripts/precommit_contracts.sh` --
  again `ree-v3` only. **No hook, gate or timer executes `REE_Working/scripts/test_*.py`.**
- Consequence: these tests are run only when a session happens to run the one
  file it is editing. Two of the four red files below were not in any chip and
  had gone unnoticed.

This is the more valuable finding than either individual fix, and it is the
reason both clusters could sit red indefinitely.

### Full corpus state on clean `origin/master`

96 of 100 files green. Four red:

| file | state | verdict | owner |
|---|---|---|---|
| `test_governance_flag_stale_id.py` | `FAILED (failures=5)` | **(a) real defect** | fixed here, `1ab439a7` |
| `test_igw_routine_tick_reap.py` | `FAILED (failures=5)` | **(c) stale fixture** | claimed by `metaworker-chip-20260815-igwgc-skiplogic-tests-red-on-trunk` -- diagnosis handed over, NOT edited |
| `test_audit_stale_claims_shared_basenames.py` | `FAILED (errors=1)` | uncharacterised | **no chip existed** |
| `test_audit_stashes.py` | `FAILED (failures=2)` | uncharacterised | **no chip existed** |

Seven further files produce no `unittest` summary line
(`test_audit_retest_staleness.py`, `test_check_deferral_exit.py`,
`test_fleet_pause_commit_idiom.py`, `test_fleet_pause_targets.py`,
`test_reaper_helpers.py`, `test_remote_pytest_detect.py`,
`test_remote_pytest_liveness_patterns.py`). All were run individually and all
**exit 0** -- they are pytest-format or bespoke pass/fail scripts, not reds. Any
future corpus runner must not treat a missing `Ran N tests` line as failure.

---

## 2. Cluster B -- `test_governance_flag_stale_id.py`: verdict **(a), a real defect**

### Mechanism

`ree_commit.py`'s `ID_FIELDS` is a hardcoded allowlist of primary-key field
names. It had no entry for `governance_flags.v1.json`, whose items are keyed by
**`flag_id`**. Those items carry **no other `ID_FIELD` at all**: `claim_ids` is a
LIST so `_scalar_field` rejects it, and every remaining key (`flag_type`,
`summary`, `raised_by_session`, `raised_at`, `status`, `resolved_at`,
`resolution_note`) is free text or a timestamp.

Measured against the live 37-item registry:

```
usable ID_FIELDS: []
flag_id scalar+unique: True True
```

So `_index_maps` returned `None` for the `items` list, and
`verify_cherry_pick_faithful` could only conservatively **REFUSE**:

```
ree_commit: cherry-pick faithfulness CANNOT BE PROVEN for
  evidence/planning/governance_flags.v1.json (list 'items') -- no field uniquely
  identifies entries across all versions, so a transplant cannot be ruled out.
  Refusing to push; the commit stays local for a human to reconcile.
```

### Why this is a real defect, not conservative-by-design

The refusal strands **every `governance_flag.py raise` made from a
behind-origin checkout** -- which is the one case the whole stale-id minting
path exists to serve. Sequence: push rejected -> `retry_push_via_worktree`
cherry-picks cleanly -> twin refused as unprovable -> flag committed locally,
never reaching origin, exit 1.

This is the identical failure mode the module's own comment already documents
for `TASK_CHIPS.json` -- "without them the verifier can only conservatively
REFUSE on TASK_CHIPS.json (safe but strands every concurrent chip commit)".
`task_id`/`chip_ref` were added for exactly this reason; `flag_id` was simply
missed when the flags registry was created.

### The second half: a DUPLICATED `flag_id` must stay keyable

Adding `flag_id` fixed 3 of 5. The remaining two --
`test_raise_reports_a_duplicate_that_already_exists_on_origin` and
`test_old_minting_lands_a_duplicate_flag_id_on_origin` -- both deliberately
construct a registry in which `flag_id` is **duplicated**, so `flag_id` alone is
non-unique and `_index_maps` refuses again.

That duplicated state is **not** a corrupt registry to be refused. It is
precisely the state `governance_flag.py`'s duplicate REPORT path exists to
surface (a peer's id landing upstream between the fetch and the pushed
cherry-pick), and it must stay **report-only** -- both tests assert exit 0
explicitly, because re-running the raise would append a THIRD item. Refusing
there converts a report into a hard exit-1 that strands the commit.

Fix: add `raised_by_session` / `raised_at` to `TIE_BREAK_FIELDS`, so
`(flag_id, raised_by_session)` separates the two -- exactly as
`(session_id, claimed_at)` already does for `TASK_CLAIMS.json`. Singles are
tried before pairs, so a healthy registry still keys on `flag_id` alone and the
pair is reached only when the duplicate is genuinely present.

### Landed

`REE_Working` `1ab439a7` on `origin/master` (`scripts/ree_commit.py`, one file).
`test_governance_flag_stale_id.py`: **11/11 OK**.

**Regression evidence.** The full 100-file corpus was run on clean
`origin/master` and on the patched tree, and the two result sets diffed. The
**only** substantive difference across ~1800 tests is
`test_governance_flag_stale_id.py :: FAILED (failures=5)` -> `OK`; everything
else differs only in timing jitter. Specifically re-verified green after the
change: `test_ree_commit_push_retry.py` (19, the file that pins this identity
machinery), `test_ref_convergence.py` (71), `test_governance_flag.py`,
`test_governance_flag_foreign_drop.py`, `test_governance_flag_push_default.py`,
`test_task_claim_foreign_drop.py`, `test_chip_ledger_push_default.py`.

---

## 3. Cluster A -- `WorktreeGcSkipLogic`: verdict **(c), stale fixture**. NOT edited.

**Contention, handled per CLAUDE.md "Conflict resolution".**
`task_claim.py open` returned exit 3: `metaworker-chip-20260815-igwgc-skiplogic-tests-red-on-trunk`
(claimed 2026-08-16T10:18:53Z, not stale) owns `scripts/test_igw_routine_tick_reap.py`
with task "Repair WorktreeGcSkipLogic fixtures broken by the 2026-08-15
classify_untracked change". This session **is not the owner and did not edit
that file**; it re-opened a narrowed claim on the uncontended resources only.
What follows is the handover the losing-session rule asks for.

### The fixture, not the code, is what broke

The 2026-08-15 `classify_untracked` change is **behaving exactly as designed and
documented**. `classify_untracked` "fails CLOSED: on any git error the error
string is returned as an artifact, so the worktree is kept rather than swept on
an unreadable state."

`WorktreeGcSkipLogic.setUp` states its own shortcut in its docstring: *"git is
stubbed via monkeypatched `worktree_unpushed_commits` / `worktree_tracked_changes`
so these run without a real worktree repo"*. The 2026-08-15 change added a
**third** git-touching dependency -- `worktree_skip_reason` -> `classify_untracked`
-> `_untracked_paths`, which really shells out to git -- and the fixture does not
stub it. In a bare `tempfile.mkdtemp` directory that call returns rc=128, the
fail-closed path returns the git error string *as an artifact name*, and the
worktree is pinned. The raw error then leaks into the reason string:

```
AssertionError: 'un-pushed' not found in
'1 untracked artifact(s) e.g. <git-rc=128: fatal: not a git repository (or any of the pare'
```

This masks the real keep-reason in all 5 tests in the class.

### Prescription (proven, one line, changes no assertion)

`_mk_wt` writes exactly `IGW_START_HERE.md` and `claude.log` -- which are
**exactly** `IGW_SCRATCH_FILES = frozenset({"IGW_START_HERE.md", "claude.log"})`,
i.e. the disposable set. So making the fixture dir a real git repo classifies
both as disposable and every one of the 5 tests passes **unchanged**. Verified
directly, without editing the owner's file:

```
REAL git repo fixture   -> ''                                    # removable, as asserted
NON-repo fixture (test) -> '1 untracked artifact(s) e.g. <git-rc=128: fatal: not a git...'
```

So: add `subprocess.run(["git","init","-q","-b","master",str(d)], check=True)`
to `_mk_wt`. This re-pins the **new** rule rather than the old one, which is
what CLAUDE.md requires ("If the tests are stale, they still need re-pinning to
the NEW rule, not deleting").

### One genuine sub-finding for the owner

The fail-closed branch returns the **raw multi-line git error as an artifact
name**, which is then truncated mid-word into the keep-reason
(`...(or any of the pare`). Defensible (it is a keep-reason for a human to
read, and keeping is the safe direction), but it makes the reason string
actively misleading -- it says "untracked artifact" when the truth is "could not
read git state". Worth a one-line distinct message. Not a correctness bug, and
**not** why the tests fail.

---

## 4. Recommended follow-on

1. **A runner for this corpus.** 100 files with no invocation path is the root
   cause of everything above. Note the 7 non-`unittest` files: gate on exit
   status, not on a `Ran N tests` line.
2. `test_audit_stale_claims_shared_basenames.py` -- `KeyError: 'attributable'`
   in `test_proposals_resource_entry_is_never_attributable`; a test reading a
   key the producer no longer emits. Needs its own diagnosis (a) vs (c).
3. `test_audit_stashes.py` -- 2 failures, and the file's own fixture self-guard
   is one of them (*"Guard the fixture itself: if the pop stopped conflicting,
   the rest is vacuous"*): the autostash pop no longer conflicts, so the fixture
   strands 1 stash entry instead of 2. Smells environment-dependent (git
   version) -- candidate (b), i.e. should skip with a stated reason rather than
   fail.
