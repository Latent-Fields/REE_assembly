# IGW "~64 minute reap deadline": refuted at source; the real loss mechanisms named

**Date:** 2026-09-03T06:04:38Z
**Session:** quirky-williams-4db531 (chip-20260903-igw-lease-reaps-near-complete-work)
**Status:** investigation complete; read-only. No IGW lease/timeout value was changed.
**Scope note:** per standing user feedback the `/metaworker-orchestrate` session owns lease and
orchestration mechanics. Recommendations below are ROUTED, not applied.

---

## Headline

**There is no ~64-minute reap deadline. The hypothesis is refuted at source.** The ~64 min
figure is a **measurement artifact of the hourly IGW tick**: `reaped_at` is written by the tick
that *notices* a dead PID, not by anything that kills one. Any spawn that dies at any point
during its first hour is stamped `reaped_at ~= assigned_at + ~61 min`.

The chip's underlying concern — that near-complete `/queue-experiment` work was stranded and
only recovered by luck — **is real and confirmed**. But its cause is not a deadline, and a
lease change would not have prevented it. Two different mechanisms are responsible, named in
section 3.

---

## 1. The deadline constant, and where it lives

`scripts/igw_routine_tick.py`:

| constant | line | value | what it actually governs |
|---|---|---|---|
| `INFLIGHT_TIMEOUT_HOURS` | 194 | 6 | self-audit staleness reporting only |
| `LEDGER_REAP_HOURS` | 195 | 24 | `stale_timeout` for a spawn whose PID is **still alive** |
| `COOLDOWN_HOURS` | 217 | 48 | per-stable-hash respawn suppression |

**No constant is anywhere near one hour.** `reap_ledger()` (line 2288) is PID-liveness-based:

```python
if pid and not pid_alive(pid):        # <- the path all three entries took
    ... status = "completed_resumable" | "spawn_failed_no_session"
elif age_h > LEDGER_REAP_HOURS:       # <- 24h, only for a LIVE pid
    ... status = "stale_timeout"
```

All three cited entries carry `status: "completed_resumable"` — *PID gone, session JSONL
present*. The reaper **detected** an exit it did not cause. `spawn_claude()` (line 3094) passes
no `timeout` and no `--max-turns`, and detaches with `start_new_session=True`; nothing in the
tick can kill a spawn.

**The clustering is the tick cadence.** `~/Library/LaunchAgents/com.ree.igwroutine.plist` sets
`StartInterval = 3600`.

## 2. The proof: actual death times vs. recorded reap times

Process death time recovered from `claude.log` mtime:

| entry | assigned | **actual death** | **real lifetime** | `reaped_at` | detection lag |
|---|---|---|---|---|---|
| IGW-20260901-233 | 21:42:45Z | 21:59:09Z | **16m24s** | 22:47:01Z | 47m52s |
| IGW-20260902-239 | 13:57:52Z | 14:46:12Z | **48m20s** | 15:01:31Z | 15m19s |

Real lifetimes differ by 3x. Only the *detection* clusters. Across the whole ledger:

- **tick-derived** `reaped_at` (n=80): **median 61.3 min**
- **self-reported** `completed_at` (n=70): median 36.5 min, range 2.5 min – 4.7 days

Three independent confirmations that no deadline is killing work:

1. **31 `USEFUL_LANDED` entries are tick-derived**, range 47.6–760.9 min. A deadline that
   killed work at ~64 min cannot produce 31 *successes* at and beyond that mark.
2. **The `DUPLICATE` bucket is the cleanest proof**: n=5, range **60.9–61.4 min**. `DUPLICATE`
   means "found nothing to do" — it resolves in minutes. All five nonetheless read ~61 min.
   That spread is only explicable as quantization.
3. A self-reported `/queue-experiment` success ran **94.0 min** — straight through the
   supposed deadline.

**Correction to the chip's figure:** IGW-239 died ~16 min after its green smoke (14:29:54Z →
14:46:12Z), not ~32 min. The 32 was computed against `reaped_at`, i.e. against the artifact.

## 3. What actually killed the two traceable sessions

Two distinct mechanisms; neither is a timeout.

**(a) Account spend limit — IGW-233, died at 16m24s.** Its `claude.log` ends:

> `You've hit your monthly spend limit ... your session limit resets 12:20am (Europe/Dublin)`

The dispatcher cannot distinguish this from "the agent finished". It is recorded as
`completed_resumable` / `NO_OP`, indistinguishable from a session with nothing to do.

**(b) Print-mode turn ended while blocked on a long background job — IGW-239, died at 48m20s.**
No limit message anywhere in its log. Its final output is a *summary* narrating work still in
flight:

> "The commit is running its `pre-commit` contract-lint suite in a cold throwaway worktree
> (~15 min so far) — not wedged."

The agent narrated its in-flight state as a final answer, and `claude -p` exited. Everything
except the commit + queue append + coordinator POST was done. This is the confirmed-harm case:
recovered by hand on 2026-09-03 and landed unmodified as ree-v3 `c55d45cbe8` (V3-EXQ-977).

**A longer lease would not have saved either.** (a) is a billing boundary; (b) is a session that
*voluntarily ended its turn*. Raising a timeout that is not firing changes nothing.

## 4. Per-lane fit: the budget is not binding

`/queue-experiment` successes, self-reported duration: **median 20.5 min**, with many under
15 min. That is an order of magnitude *below* the supposed 64-min budget, and several successes
exceed it outright. Successful runs are **not** bunched just under an hour — the signature a
binding deadline would leave.

**Conclusion: the `/queue-experiment` lane is not being set up to fail by a time budget.** The
mandatory gates (substrate-readiness, empirical probe, code review, smoke test, adversarial
red-team) fit comfortably in the observed distribution. The elevated NO_OP rate is caused by
(a) and (b) above plus the classifier defect in section 6 — not by a budget.

## 5. Orphan residue: signature real, currently empty, detector already exists

Signature: TASK_CLAIMS entry still `active` reserving an EXQ slot + an **untracked** driver in
`ree-v3/experiments/` + no queue entry and no git history ever adding one.

**`scripts/audit_unqueued_experiment_scripts.py` already detects this** — it is tested
(`scripts/test_audit_unqueued_experiment_scripts.py`), exposed as an MCP tool
(`mcp_server.py:846`), and **wired to nothing**. Its own docstring says so: "NOT a hook, NOT a
commit gate ... invoked by hand or from a periodic tick". The chip's guess — that wiring the
existing audit is the whole fix — is correct, with one refinement.

**The refinement matters.** Run as-is it reports **146 findings** (harness helpers without a
leading underscore, old onboarding smokes, long-dead drafts) — far too noisy to chip. But
intersect with *untracked* and it collapses to **2**:

| file | verdict |
|---|---|
| `v3_exq_822e_sd082_...py` | known-deliberate; design refuted by its own red-team |
| `v3_exq_951a_mech320_...py` | **false positive** — a pilot that *ran*; its refutation is recorded in an active claim and absorbed by V3-EXQ-951c (queued and landed, `e5b5b84`) |

**So there is currently zero live orphan residue.** The one confirmed instance (977) has been
recovered. `v3_exq_977` has left the untracked set, independently confirming that landing.

Tracked-vs-untracked is the load-bearing distinction and the audit does not currently make it:
an **untracked** orphan exists nowhere but one disk and dies with a worktree GC (IGW-245's
worktree was GC'd 2 seconds after reap, taking its `claude.log` with it); a **tracked** orphan is
safe in git and is merely backlog.

## 6. Adjacent, separate defect — noted, not re-derived

The AUTO outcome classifier misfiles work *after the fact*: IGW-239's `/lit-pull` sibling for
ARC-120 was recorded `NO_OP` by AUTO and hand-corrected to `USEFUL_LANDED`, because AUTO looks
for a queue/experiment landing or a worktree-branch commit and a `/lit-pull` lands neither — its
output is a work-repo commit on `REE_assembly` master. **This is a different bug** (misclassify
after completion) from anything in this note (nothing kills sessions early). Kept separate
deliberately.

---

## Recommendations — routed to `/metaworker-orchestrate`, not applied

1. **Do not change any IGW lease or timeout value.** No deadline is firing. Raising
   `LEDGER_REAP_HOURS` or adding a per-lane budget would be a fix to a non-existent defect.
2. **Stop `reaped_at` masquerading as a death time.** Record the observed exit time (e.g.
   `claude.log` mtime) as a distinct field, or mark `reaped_at` explicitly as detection-time.
   This artifact produced a plausible, precise, and entirely wrong hypothesis that survived into
   a dispatched chip. Cheap, and it is what makes every future duration read honestly.
3. **Detect the spend-limit exit as its own outcome.** `_classify_outcome` should scan
   `claude.log` for the limit string and emit e.g. `NO_OP_SPEND_LIMIT`. A billing stop currently
   looks identical to an agent with nothing to do, so the fleet cannot see it happening.
4. **Wire `audit_unqueued_experiment_scripts.py` into `hygiene_routine_tick.py`**, gated on
   `untracked AND unqueued` (146 → 2 today). This is in-chip-scope and the residue's only
   detector. Suggest an explicit skip-list note for the deliberate `822e` case.
5. **Worth a look, out of scope here:** the print-mode turn ending while a background job is in
   flight (mechanism (b)) is the one that actually destroyed an hour of good work. Guidance to
   headless briefs to *block on* rather than narrate a long-running commit would address the
   cause directly.

**Hygiene item spotted in passing:** the claim
`metaworker-chip-20260901-mech320-dv-headroom-and-vt-floor` has been `active` since
2026-09-01T20:28:45Z (>24h stale) while holding
`ree-v3/experiments/v3_exq_951a_...py`. `audit_stale_claims.py` territory, not this chip's.
