**Status: DESIGN PROPOSED -- templates built, not yet installed on any box**

# Fleet-wide GC/stranded-work scanning gap: findings and design

Follow-on to `chip-20260826-cloud4-worktree-graveyard-audit-needed` (motivating finding: 63
unswept worktrees on `ree-cloud-4`). This is the fleet-wide-gap investigation the user chose
over a one-off triage (see that chip's `resolution_note`). Session:
`chip-20260826-fleet-wide-gc-scanning-gap`.

**Explicitly out of scope** (per the chip's own instruction): triaging or GC'ing the two
worktree graveyards this investigation confirms are live right now (63 worktrees on
`ree-cloud-4`, 92 on the Mac). Both are already tracked by their own chips
(`chip-20260826-cloud4-worktree-graveyard-audit-needed`, done, and
`chip-20260826-worktree-graveyard-triage-and-gc`, open) and stay deferred, human-supervised
work. This doc's job is the detection gap only.

---

## 1. Summary

`hygiene_routine_tick.py`'s GC/stranded-work sources (6, 6b, 12, 15) are not "Mac-only" in
the sense their host codebase implies (hardcoded Mac paths) -- a `/Users/dgolden -> /home/ree`
symlink shim on every provisioned Linux box already makes the Mac-spelled `REE_WORKING`
constant resolve correctly everywhere, and I confirmed that shim live on `ree-cloud-5`. The
real gap is **invocation**, not path resolution: the tick only ever *runs* on boxes that have
(a) a full umbrella checkout at all, and (b) something that periodically launches it there. Of
the five cloud boxes, only two -- `ree-cloud-4` and `ree-cloud-5` -- satisfy (a) at all
(verified below); the other three physically cannot accumulate `.claude/worktrees/metaworker-*`
state and are out of scope for this fix. Of those two, only `ree-cloud-5` currently gets (b),
and only *intermittently*, as a side effect of dispatch cycles that are themselves now
lease-gated rather than running on a fixed cadence. `ree-cloud-4`'s own dispatch timer was
retired on 2026-08-25 as part of the Dispatcher/Healer/Orchestrator role split, and nothing
replaced it as a trigger for the hygiene tick specifically -- so `ree-cloud-4` has had **zero**
periodic hygiene-tick coverage since that date, which lines up with its 63-worktree graveyard's
own `no owner since 2026-08-20` finding.

The fix does not touch `hygiene_routine_tick.py` itself. Every source already degrades safely
when its subject is absent on the box that runs it (verified for the two genuinely
Mac-artifact-dependent sources, see Section 4), and cross-box chip correctness is already
handled by the existing `origin_host` stamping / `_MACHINE_LOCAL_RESOLVE_PREFIXES` machinery
(see Section 5). What's missing is purely infrastructural: `ree-cloud-4` and `ree-cloud-5` each
need the same thing the Mac got on 2026-08-25 -- a dedicated periodic timer that runs
`hygiene_routine_tick.py --push` on a fixed cadence, decoupled from dispatch/lease state, for
exactly the reason the Mac's tick was decoupled from the old metaworker-dispatch cadence in the
first place (see `com.ree.hygienetick.plist`'s own header). I built the version-controlled
templates for that (systemd timer/service pair + install script, Section 6) but did not install
them -- this session has no ssh reach to `ree-cloud-4`, and installing a new timer on live
dispatch boxes deserves its own deliberate, verified follow-on rather than a blind push from
here. Removal of any worktree stays exactly as human-supervised as it already was; nothing in
this design changes that.

---

## 2. What the GC/stranded-work sources actually check (recap, not a re-design)

Read from `scripts/hygiene_routine_tick.py`'s own module docstring (points 6, 6b, 12, 15) and
the functions themselves:

| Source | Function | What it detects | Auto-removes? |
|---|---|---|---|
| 6 | `_metaworker_worktree_gc_findings` (~L1821) | A `metaworker-*` worktree whose chip is `done`/`withdrawn`, no live process (`lsof -a -d cwd`), clean `git status --porcelain`, and no unpushed commits on its branch | Never -- names the removal command, a human/agent runs it |
| 6b | `_metaworker_worktree_gc_batch_findings` (~L2262) | Batches source 6's candidates into at most one dispatchable "GC sweep" chip per tick | Never |
| 12 | `_stranded_worktree_findings` (~L3988) | A `metaworker-*` worktree holding **uncommitted** work (no commit, stash, or reflog entry anywhere) whose owning session looks dead (no lsof cwd, no fresh chip claim, idle past `STRANDED_MIN_IDLE_HOURS`) | Never -- report only, an auto-commit of another session's in-flight edit is the read-modify-write hazard CLAUDE.md documents |
| 15 | `_removed_worktree_live_worker_findings` (~L5159) | A worktree directory that's been deleted from disk while a process still has its cwd inside it | N/A -- there's nothing to remove, this is a "did we just lose work" alarm |

All four are read-only detectors over: the local filesystem (`WORKTREES_DIR`), `lsof`, `git`,
and the fleet-shared, git-tracked `TASK_CHIPS.json`. None of them read a Mac-local gitignored
log file. This matters for Section 4.

---

## 3. The path-shim check (ruling out the obvious hypothesis first)

`hygiene_routine_tick.py` hardcodes:

```python
REE_WORKING = Path("/Users/dgolden/REE_Working")
WORKTREES_DIR = REE_WORKING / ".claude" / "worktrees"
```

The natural hypothesis is "this only works on the Mac because the path is hardcoded to a Mac
home directory." That's the documented rationale for why chip **prompts** are written in
Mac-absolute form (`metaworker-dispatch/SKILL.md`'s "Cross-host absolute paths" section) -- but
it is not why the *tick's own scan* is under-covered. Verified live on this box (`ree-cloud-5`):

```
$ readlink -f /Users/dgolden/REE_Working
/home/ree/REE_Working
$ ls -la /Users
lrwxrwxrwx  1 root root  9 Aug  2 22:01 dgolden -> /home/ree
```

Every provisioned Linux box carries this `/Users/dgolden -> /home/ree` symlink (installed at
provisioning time -- see `metaworker-dispatch/SKILL.md`'s "the shim" section, which documents
it as deliberate and load-bearing for verbatim brief rendering). So `WORKTREES_DIR.iterdir()`
run on `ree-cloud-4` or `ree-cloud-5` already resolves to that box's own
`/home/ree/REE_Working/.claude/worktrees/`, not the Mac's. **If the script were invoked on
`ree-cloud-4` today, it would correctly scan `ree-cloud-4`'s own worktrees.** The gap is that
nothing invokes it there, not that it would resolve to the wrong place if something did.

`ree-cloud-1` (hub), `ree-cloud-2`, `ree-cloud-3` do not carry this shim and don't need to --
see Section 5.

---

## 4. Confirming the tick fails safe, not loud, on genuinely Mac-only sources

Two sources (18 `_scripts_corpus_findings`, 21 `_git_sync_repair_findings`) read gitignored,
genuinely-Mac-produced files under `logs/`. If those sources errored on a box where the file is
absent, running the unmodified tick on `ree-cloud-4` would be unsafe (one bad source could sink
the whole tick, since `run_tick()` calls all ~21 sources unconditionally in one function with no
per-source isolation visible at the call sites). Checked `_scripts_corpus_findings`
(`hygiene_routine_tick.py` ~L5978):

```python
try:
    st = results_path.stat()
except OSError:
    return [], {"scan_ok": False, "failed": 0,
                "reason": "no results file at %s -- com.ree.scriptscorpus "
                          "has not run here yet, or this is not the box "
                          "that runs it" % results_path}
```

Returns cleanly with `scan_ok: False` and a reason string -- no exception, no findings, no chip.
`_git_sync_repair_findings` follows the identical pattern (own module docstring: "Fails OPEN").
So **running `hygiene_routine_tick.py --push` unmodified on `ree-cloud-4` today would already
work correctly**: the worktree-lifecycle sources (6/6b/12/15) and every other per-box or
fleet-shared source (1-4, 8-14, 17) would run for real, and the two genuinely-Mac-artifact
sources (18, 21) would harmlessly report "not this box" and mint nothing. **No code change to
`hygiene_routine_tick.py` is required for this fix** -- the gap is entirely in what triggers the
script, not what the script does once triggered.

---

## 5. Fleet topology: which boxes can even accumulate this class of debris

Scoping this correctly matters -- CLAUDE.md's Narrow Edits Only rule applies as much to design
scope as to code edits. Verified against `scripts/audit_stashes.py`'s own `REMOTE_FLEET` table
and its docstring (`ree-cloud-4`/`ree-cloud-5` confirmed 2026-08-19 to be the only two cloud
boxes carrying a full umbrella checkout with `scripts/`; `ree-cloud-1` verified by direct ssh to
hold `REE_assembly`/`ree-v3` as **plain directories with no umbrella checkout at that root at
all** -- not a git repo, no `scripts/`; `ree-cloud-2`/`ree-cloud-3` are architecturally identical
pure experiment runners, not individually re-verified but nothing provisions an umbrella
checkout on them either):

| Box | Umbrella checkout? | `.claude/worktrees/` possible? | In scope for this fix |
|---|---|---|---|
| Mac (`DLAPTOP`) | yes | yes | already fixed (`com.ree.hygienetick`, 2026-08-25) |
| `ree-cloud-5` | yes | yes | **yes** -- gets it intermittently via dispatch, needs guaranteed cadence |
| `ree-cloud-4` | yes | yes | **yes** -- gets it not at all since dispatch retired 2026-08-25 |
| `ree-cloud-1` (hub) | no | no | out of scope -- can never have a `metaworker-*` worktree |
| `ree-cloud-2` | no | no | out of scope, same reason |
| `ree-cloud-3` | no | no | out of scope, same reason |

So "fleet-wide" for this specific gap means exactly three boxes total (Mac + 2 cloud), not five.
Building scanning infrastructure for `ree-cloud-1/2/3` would be effort spent on boxes that
structurally cannot produce the finding this fix exists to catch.

---

## 6. Evidence the gap is live, not theoretical

Two independent worktree graveyards exist in `TASK_CHIPS.json` right now, confirmed disjoint by
filesystem (per `chip-20260826-cloud4-worktree-graveyard-audit-needed`'s own tldr: "Not a
duplicate of the Mac's 92-worktree chip -- disjoint filesystems"):

- **`ree-cloud-4`: 63 worktrees**, "0 live, 1 parked, 22 look GC-safe, 24 hold unlanded commits,
  17 real-dirty ... no owner since 2026-08-20." (`chip-20260826-cloud4-worktree-graveyard-audit-needed`,
  now `done` -- that chip's job was raising this decision, not doing the triage.)
- **Mac: 92 worktrees**, "50 holding commits not on origin/master ... 6 are LIVE."
  (`chip-20260826-worktree-graveyard-triage-and-gc`, still `open`.)

The Mac number is the more striking data point for this design doc specifically: **even the one
box that has always had hygiene-tick coverage still has a 92-worktree backlog**, because
detection-and-report was never the bottleneck there -- human-supervised triage capacity is. That
is a separate, already-tracked problem (Section 8 makes this explicit) and this design does
nothing to speed up triage; it only makes sure `ree-cloud-4` starts generating the same kind of
report the Mac already does, instead of silently accumulating for six days between manual
sweeps.

---

## 7. Why "give it a timer" is the right shape, not a workaround

`com.ree.hygienetick.plist`'s own header already argues this, almost verbatim, for the Mac:
before 2026-08-25 the tick rode the `metaworker-dispatch` cycle's cadence; when that cadence
stopped being unconditional (dispatch became lease-gated behind an interactive Orchestrator),
the tick silently stopped too, and a dry run two days later found 12 unreported findings queued
up. **The identical failure mode reproduced on `ree-cloud-4`**, for the identical reason -- its
dispatch timer was the tick's only trigger, that timer was retired the same day for the same
reason (the Dispatcher/Healer/Orchestrator split), and nothing replaced it as a hygiene-tick
trigger. The fix that worked for the Mac -- decouple the tick's cadence from dispatch entirely,
give it its own timer -- generalizes directly.

**The plist's own "DO NOT install on cloud workers" line does not actually cover this case**,
and it's worth stating precisely why, since this doc is proposing to do exactly what that line
says not to do. Reading it closely, it gives two reasons:

1. "They cannot read the Mac-local verdict files" -- true, and it's why sources 18/21 will
   simply no-op there (Section 4). It is not true of sources 1-4, 6, 6b, 8-15, 17, which are
   either per-box-local (the worktree/lsof/git checks) or fleet-shared (`TASK_CHIPS.json`,
   `TASK_CLAIMS.json`). The line is correct for a subset of sources and was written as if it
   covered all of them.
2. "A second writer of `TASK_CHIPS.json` buys nothing but contention" -- also true in the
   specific case it was written for (a *second Mac-timer-equivalent* reading the *same*
   Mac-local files and re-deriving the *same* findings), and not true for a box whose local
   state (its own worktree directory) is invisible to every other writer. `chip_ledger`'s
   compare-and-swap is already the load-bearing mechanism for concurrent writers across this
   whole system (CLAUDE.md's arbitration section, and in practice: `ree-cloud-4` and
   `ree-cloud-5` already both write `TASK_CHIPS.json` concurrently whenever both hold a
   dispatch lease). Adding a third/fourth periodic writer is not a new class of risk.

So this is not "installing the Mac timer on the cloud despite its own warning" -- it's
installing a differently-scoped timer (a systemd equivalent, running the same script, on boxes
the warning's own reasoning doesn't actually cover) while leaving the warning's *correct* half
(don't expect it to see Mac-local verdict files) intact, because nothing in this design asks it
to.

---

## 8. What's built now vs. deferred as follow-on

**Built, version-controlled, NOT installed anywhere** (see the three new files under
`scripts/` alongside this doc's commit):

- `scripts/ree-hygienetick.service` -- systemd oneshot unit, runs
  `hygiene_routine_tick.py --push` as the `ree` user from `/home/ree/REE_Working`.
- `scripts/ree-hygienetick.timer` -- fires the service every 900s (matching the Mac's own
  cadence and its own stated duty-cycle reasoning), `Persistent=true` so a missed tick while the
  box was off still fires once on next boot rather than waiting a full period.
- `scripts/install_hygienetick_timer_cloud.sh` -- install script mirroring
  `install_hygienetick_timer.sh`'s own structure and guard style, but inverted: refuses on
  Darwin, and refuses on any host whose `canonical_machine_name()` isn't `ree-cloud-4` or
  `ree-cloud-5` (Section 5's scope table, enforced mechanically rather than left to whoever runs
  it to remember).

**Deliberately not done in this session, raised as follow-on instead** (chipped per CLAUDE.md's
default -- this is not `/governance` or `/failure-autopsy` work, so it gets a chip, not an inline
action):

- **Actually installing the timer on `ree-cloud-4` and `ree-cloud-5`.** This session has no ssh
  reach to `ree-cloud-4` (confirmed by the same routing/auth gap `metaworker-repair/SKILL.md`
  documents for the Healer's own reach into the Mac -- the reachability model for this fleet is
  asymmetric and not something to route around from here), and installing a new systemd timer on
  two live dispatch boxes is an infrastructure change that deserves a real verification pass
  (does the unit start, does it fire, does a real tick complete and push) from a session that can
  actually reach the target box -- not a blind push from a design session. Raised as
  `chip-20260826-install-cloud-hygienetick-timer` (`kind: work`).
- **A `--sources`/subset-selection CLI flag on `hygiene_routine_tick.py`.** Considered and not
  built: Section 4 confirms every source already no-ops safely when its subject is absent, so
  this would only save a handful of fast local file-stat calls per tick -- not required for
  correctness, and adding it risks the exact over-generalization CLAUDE.md's held-out-check rule
  warns about (a flag invites "only run sources 6/6b/12/15," which would silently also drop the
  per-box-local sources 8-15/17 this fix should equally extend, since none of *those* depend on
  Mac-only data either). Worth reconsidering only if a real cadence/CPU cost measurement on
  `ree-cloud-4` ever shows the full tick is too slow there -- no evidence of that today.

---

## 9. Guardrails this design does not change

- **No new auto-removal logic anywhere.** Sources 6/6b/12/15 remain report-only; this design
  adds nothing to `hygiene_routine_tick.py`'s own removal posture. A GC-candidate chip still
  only ever names the command; a human or an agent session still has to run it. This is the
  Healer's own established stance (`metaworker-repair/SKILL.md`'s "Worktree GC / stranded work"
  row: "Report-only by design") and this doc does not propose touching it.
- **The two existing graveyards stay exactly as deferred as they already are.** Installing the
  cloud timer will, once done, start raising fresh GC-candidate / stranded-work chips for
  `ree-cloud-4`'s 63 worktrees going forward -- it does not retroactively triage the backlog
  that's already there, and Section 6 already names the two chips that own that backlog.
- **Scope stays at three boxes** (Section 5). If `ree-cloud-1/2/3` are ever provisioned with a
  full umbrella checkout for some other reason, this design's scope table is the place to revisit
  -- do not assume it then.

---

## 10. Residual uncertainty, stated rather than papered over

- **`ree-cloud-5`'s current dispatch-timer state was not directly verifiable from this session.**
  `check_metaworker_timer_state.py`'s output in a same-day `WORKSPACE_STATE.md` entry reported
  `ree-cloud-4 RETIRED as designed` (a direct local check, since that Healer cycle ran *from*
  `ree-cloud-4`) alongside `ree-cloud-5 SSH-AUTH-GAP (known/expected)` -- i.e. it could not be
  checked remotely from `ree-cloud-4` that cycle, for the same routing/auth reasons
  `metaworker-repair/SKILL.md` documents for reach into the Mac. A separate `WORKSPACE_STATE.md`
  entry the same day mentions "`ree-cloud-4` and `ree-cloud-5` both hold valid run leases (139
  min) granted," which is consistent with dispatch (and therefore Step 2's hygiene invocation)
  still firing periodically on `ree-cloud-5` whenever a lease is held, rather than having been
  retired outright the way `ree-cloud-4`'s was. Either way the fix in Section 8 is correct: a
  lease-conditional trigger is strictly less reliable than a dedicated timer, so giving
  `ree-cloud-5` its own timer closes the gap regardless of which of these two states is
  currently true there. Whoever installs the timer (the follow-on chip) should confirm this
  directly via `systemctl status ree-metaworker.timer` on `ree-cloud-5` before assuming either
  answer.
- **Cadence choice (900s) is carried over from the Mac's own reasoning, not independently
  measured for `ree-cloud-4`/`ree-cloud-5`.** The Mac's plist header cites a 52s measured tick
  duration there; this design doc does not have an equivalent measurement for either cloud box
  (no ssh reach). The install follow-on should measure one real tick's wall-clock time on the
  target box before treating 900s as validated rather than merely carried over.

---

## 11. Installation follow-on results (2026-08-26, `chip-20260826-install-cloud-hygienetick-timer`)

**`ree-cloud-5`: installed and verified, both open items resolved.**

- Measured wall-clock of one real `hygiene_routine_tick.py --push` tick on `ree-cloud-5`:
  **~80s** (`time` output: `real 1m20.242s`). 900s leaves an ~11x margin -- comfortable, no
  `OnUnitActiveSec` change needed. (A second tick, triggered by the timer itself moments after
  install, completed in ~66s -- consistent with the manual measurement.)
- Section 10's open question, resolved directly: `systemctl status ree-metaworker.timer` on
  `ree-cloud-5` shows `Loaded: loaded (...; disabled; ...)` / `Active: inactive (dead)`. The old
  dispatch timer is **disabled outright**, the same as `ree-cloud-4`'s -- not lease-conditional.
  (`ree-metaworker-healer.timer` is separately active, but that is the new Healer role, not the
  old dispatch cycle, and does not invoke `hygiene_routine_tick.py`.) So the dedicated timer
  installed here was not merely defense-in-depth against an intermittent trigger -- on
  `ree-cloud-5`, as on `ree-cloud-4`, it is now the *only* trigger.
- `scripts/install_hygienetick_timer_cloud.sh` ran clean (`canonical_machine_name` resolved to
  `ree-cloud-5`, unit files copied, `daemon-reload` + `enable --now`). `systemctl list-timers`
  confirms `ree-hygienetick.timer` enabled, next fire scheduled 900s after the first, and the
  triggered `ree-hygienetick.service` exited `status=0/SUCCESS` producing a real chip
  (`chip-queuefloor-ree-cloud-5-since-2026-08-26t21-15-08z`) -- the confirmation this chip's
  Step 4 asked for.

**`ree-cloud-4`: NOT installed -- confirmed unreachable, not merely untried.** This is the same
asymmetric SSH-reach gap `metaworker-repair/SKILL.md` documents for the Healer's reach into the
Mac, now measured for the `ree-cloud-5` -> `ree-cloud-4` leg specifically rather than assumed by
analogy:

- Direct `ssh ree@91.99.68.94` (the fleet's own recorded IP for `ree-cloud-4`, from
  `dispatch_remote_launch.py`'s `DEFAULT_SSH_HOSTS`) from `ree-cloud-5`: `Permission denied
  (publickey,password)`. The host key matches a prior connection (known to `known_hosts`), so
  this is an authorization gap, not a routing/network one at this hop.
- `scripts/check_metaworker_wrapper_deploy.py --json`, run from `ree-cloud-5`, independently
  confirms the same: `"machine": "ree-cloud-4", "status": "UNREACHABLE", "detail": "ree@
  91.99.68.94: Permission denied (publickey,password)."` -- this is the tool's own documented
  non-finding stance (`UNREACHABLE ... NOT a finding`), included here only as independent
  confirmation, not as a new discovery.
- Routed through the hub instead (`ree-cloud-5` -> `ree-cloud-1` -> `ree-cloud-4`, both by public
  IP `91.99.68.94` and by the hub's own WireGuard peer `10.8.0.14`): same `Permission denied
  (publickey,password)` in both cases. So the hub's key is not authorized on `ree-cloud-4`
  either -- this is not a `ree-cloud-5`-specific gap that routing through another box works
  around.
- Per `metaworker-repair/SKILL.md`'s framing of the equivalent Mac case: "Both are the user's
  decisions, not gaps to route around." No `authorized_keys`/WireGuard change was attempted here
  for the same reason. Raised as a `kind: decision` chip
  (`chip-20260826-cloud4-hygienetick-ssh-unreachable`) rather than guessed around, per the
  headless-worker contract.
- **Once reach exists** (whether via a human running it directly, or a future session with a
  working route), the remaining work is exactly Section 8's three steps, unchanged: `bash
  /home/ree/REE_Working/scripts/install_hygienetick_timer_cloud.sh`, then `time
  /usr/bin/python3 /home/ree/REE_Working/scripts/hygiene_routine_tick.py --push` to check the
  900s margin holds there too (worktree count and therefore GC-scan cost may differ from
  `ree-cloud-5`'s), then confirm one real chip or clean tick via `journalctl -u ree-hygienetick`.
