# Committed conflict markers in igw_routine_log.md: durable fix (metaworker-learning)

**Status: APPROVED 2026-09-26 (rec-20260926-bce5797e, F1+F2) and BUILT** -- REE_Working `a3e4a53e57`. F3 not built (not chosen).

- **Session:** `mwlearn-20260926-1044`, 2026-09-26
- **Chip:** `chip-20260924-learning-igwlog-conflictmarker-rootcause-v2`
- **Decision of record:** `chip-20260924-decision-igwlog-conflictmarker-recurrence-learning-route`, option A: find the root cause and/or add a TARGETED committed-content check. A blanket clean-tree scan is ruled out.
- **Companion chip:** `chip-20260923-igwlog-conflict-markers`
- **Current state:** neither `origin/master` nor the local worktree has markers in this file. Instance 2 was already stripped at `d9f64a28831`.

## 1. Occurrences: two, one root cause

| # | Introducing commit (origin) | Local original | Committer | Time (Z) | Marker labels | Removed by |
|---|---|---|---|---|---|---|
| 1 | `54f9e1a60de` "igw-ledger: update" | cherry-pick of `4019aea644` | REE Automation (Mac) | 2026-09-17 21:31 | `<<<<<<< Updated upstream` / (empty) / `=======` / `complete igw-243-...` / `>>>>>>> Stashed changes` | `6e84a89a307` |
| 2 | `36fe7849d35` "igw-ledger: update" | cherry-pick of `f7ef74a2f3` | REE Automation (Mac) | 2026-09-23 15:32 | same shape, carrying `complete IGW-20260923-228` | `d9f64a28831` |

The labels `Updated upstream` / `Stashed changes` are what `git stash apply` writes. The two IGW JSON ledgers have never had markers. In all of REE_assembly since 2026-01 the only other marker event is a retired `runner_heartbeats` JSON on 2026-05-07.

## 2. Mechanism

Confirmed from the reflog, the archived stashes (`stash-archive/20260918-2af9a119b5b` and `stash-archive/20260923-f86316d3d85`) and a local repro on git 2.51.2.

**The chips' premise is corrected here.** The stash pop does not happen inside `igw_routine_tick.py`'s commit path. The tick *creates the precondition* and later *commits the damage*. The stash and pop come from a separate bare `git pull --rebase --autostash` in the Mac's shared REE_assembly checkout.

Incident 2, step by step (incident 1 is identical):

1. **14:34:52Z.** `cmd_complete` appends `auto-defer`. `save_ledger` → `commit_ledger_files` then lands the log via `ree_commit.py --push --to-remote-tip`. By design that path does not move the local ref, so origin now has the line and local HEAD is stale.
2. **14:35:24Z.** `cmd_complete` appends the `complete ...` line **after** `save_ledger` (`scripts/igw_routine_tick.py:5883-5885`). The worktree is now origin plus one trailing line, sitting on a stale HEAD.
3. **14:37:28-42Z.** A bare `pull --rebase --autostash` runs. It stashes both lines against the stale HEAD, fast-forwards to origin (which already has the `auto-defer` line), and re-applies the stash. That is an add/add conflict. git factors out the common line, leaving *upstream = empty, stash = [complete]*, which is exactly the committed block.
   - Repro: a worktree equal to origin plus one trailing line gives this block and `UU`.
   - Control: a worktree byte-identical to origin gives "Applied autostash." cleanly.
4. **15:25-15:31Z.** The next tick appends lines on top of the marked file. `ree_commit.build_private_index` hashes the file from disk into a private index. It has no marker check and never consults the shared index's unmerged entries, so the markers are committed and pushed.

**Who ran the pull.** Strongly indicated, not proven:
- The reflog argv is a bare `pull --rebase --autostash` with no remote argument. That matches `ree-v3/experiment_runner.py:git_pull` (the auto-sync tick and startup), not `land_governance.sh` (which pulls with `origin master`).
- The 09-17 stash also held two runner-produced manifests.
- The Mac runner was set to stop after its current experiment on 09-22T18:10Z, so it was plausibly still alive on 09-23.
- Whatever the caller, **any** bare autostash pull reproduces the bug while the precondition exists. So the durable fix removes the precondition.

**Why nothing noticed:** `audit_shared_checkout_conflicts.py` scans only files git reports dirty, by design. A committed file is clean.

## 3. Proposed fix

**F1: remove the precondition (root cause, narrow). File: `scripts/igw_routine_tick.py`.** Never leave log lines unlanded after a landing.

- In `cmd_complete`, move the final `append_log(... complete ...)` **above** `save_ledger(...)`.
- Make the same change in `cmd_disposition`, where `append_log` follows `save_ledger` (around line 5745).
- The `cmd_tick` skip paths (paused, generator-failed, pending_review) append without landing. Add a log-only flush in `main()` for every subcommand before `fossil_reconcile_at_tick_end`: `_ree_commit(["evidence/planning/igw_routine_log.md"], ..., no_local_fallback=True)`. `ree_commit` already no-ops when nothing changed.
- Run `fossil_reconcile_at_tick_end` after `complete`, `disposition`, `launch` and `gc` too, not only after `tick`. That reconciles the byte-identical-to-origin fossil F1 leaves behind, so the local ref stops lagging.
- **Effect:** after any subcommand the log in the worktree equals origin, so an autostash pull re-applies cleanly (proven by the repro control).
- **Blast radius:** this one file, plus one no-op subprocess per invocation.
- **Residual:** two concurrent igw processes can still interleave appends between the two landings.
- **Tests:** follow `scripts/test_igw_routine_tick_complete_target.py`, which patches `tick.LOG_MD` and `tick.commit_ledger_files`. Assert that no `append_log` follows the last commit call in `cmd_complete` / `cmd_disposition`. Confirm the test FAILS on the current ordering.

**F2: targeted guard for this ledger. File: `commit_ledger_files` (around line 1031).**

- Before `_ree_commit(log_existing, ...)`, check `LOG_MD` for a column-0 marker block (at least one `<<<<<<< ` line and one `>>>>>>> ` line, reusing the regexes at `audit_shared_checkout_conflicts.py:200-202`). Also check `git ls-files -u -- evidence/planning/igw_routine_log.md`.
- On a hit: **refuse to land the log**, print `[igw-tick] REFUSING to land igw_routine_log.md: conflict markers at lines N..M`, and raise a `governance_flag.py` entry. Keep appending locally, so no lines are lost.
- **Blast radius:** one file, and no false-positive surface, because this log never legitimately contains column-0 markers.
- This is the "targeted committed-content check" option A allowed. It prevents rather than detects after the fact.

**Not proposed now (for your decision):**

- **F3: a guard across the whole of `ree_commit.py`.** It would refuse a declared path that is `UU` in the shared index, or whose blob gains a column-0 marker block HEAD lacked, skipping ``` fences in `.md`. It would also catch the WORKSPACE_STATE merge-residue commits (umbrella `d2abe729f` and `038288881`, both caught by the held-out check below).
  - Its blast radius is every coordination writer.
  - A refusal blocks every later append to that file until someone resolves it by hand.
  - A naive version has a proven false positive: `f9e271170`, a design doc with fenced example blocks.
  - Recommend it as its own chip, scoped fence-aware or UU-only, not bundled here.
- **Removing `--autostash` from the runner's `git_pull` on REE_assembly**, or skipping the pull when the log is ` M`. The runner is currently disabled, and F1 makes the pull safe anyway. Revisit if F1 lands and a third instance appears.
- **Flipping `igw_log_suppress_git_write` so the hub writer owns the log.** This is a PHASE-4 cutover, larger in scope.

## 4. Held-out check (GOV-HELDOUT-1)

**F1 and F2: no non-degenerate held-out case exists.** The only committed markers this file has ever carried are the two motivating incidents. The WORKSPACE_STATE cases have a different trigger: merge residue in a file that is not an IGW ledger, which F1 and F2 never touch. **F1 and F2 therefore ship explicitly scoped to this incident class, not as a general rule.** That is acceptable here because both are narrow code changes to one writer, not a standing rule or a skill edit.

**F3 (not proposed now):** three non-degenerate cases, and the check caught an over-broad draft.

| Case | Old | F3 | Correct? |
|---|---|---|---|
| Umbrella `d2abe729f` (2026-08-23): WORKSPACE_STATE append swept `<<<<<<< HEAD` merge markers | committed | refuses | yes |
| Umbrella `038288881` (2026-08-25): same path, two blocks | committed | refuses | yes |
| Umbrella `f9e271170` (2026-08-19): design doc with 3 legitimate column-0 example blocks | committed | naive version refuses (**wrong**); fence-aware or UU-only version passes | only the fence-aware or UU-only form |

**Cost counterweight:** F1 adds a no-op commit subprocess per tick invocation. F2 adds one file read per landing.

## 5. Open questions

1. When marked commit 2 was made, was the shared index still `UU`? `--to-remote-tip` may skip `refresh_shared_index`. The answer decides whether a UU-only F3 would actually have fired.
2. `land_governance.sh:66` runs the same kind of autostash pull. Since F1 removes the precondition for this file only, that pull stays a hazard for any other file a writer appends to after its landing.
3. The docstring at `igw_routine_tick.py:824` still names the retired runner-heartbeat autostash. Fix it with F1.
