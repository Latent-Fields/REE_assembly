# Ingress-gated chip routing gap (chip-20260826-ingress-gated-chip-routing-gap)

**Status:** investigated, one low-risk mitigation shipped, one architecture
question raised as a decision chip rather than decided unilaterally.
**Date:** 2026-08-26. **Box:** ree-cloud-5.

## The symptom

`chip-20260814-queue-causal-sleep-matched-arm` (`urgency: true`) sat `open`
and unclaimed in `TASK_CHIPS.json` for **12 days** despite dozens of
`metaworker-dispatch` cycles on `ree-cloud-4` and `ree-cloud-5` running
against it. Every cycle correctly logged `WITHHELD ... condition 4
(INGRESS-INCAPABLE)` and moved on — no cycle ever mishandled it. Two more
chips, `chip-20260825-mech492-falsifier-queue` and
`chip-20260825-e1-rollout-horizon-sweep-probe`, were withheld the same way
from their very first eligible dispatch cycle, with no other action ever
taken.

**The individual withholds are correct.** The gap is structural: nothing
in the system ever converts "correctly withheld" into "actually dispatched
somewhere that can finish it."

## What condition 4 actually does (and doesn't)

`.claude/skills/metaworker-dispatch/SKILL.md` Step 4 condition 4 (and the
near-identical Step 3.5 IGW host-capability gate) checks, once per dispatch
cycle, whether *this box* can complete a coordinator-ingress deliverable
(`/queue-experiment`'s `POST /queue/add`, gated on
`REE_assembly/coordinator.env` carrying `COORDINATOR_URL` +
`COORDINATOR_LOCAL_TOKEN`). On `ree-cloud-4`/`ree-cloud-5` — which have no
such file — it correctly withholds: leaves the chip open, unclaimed, and
unassigned, and logs one `WITHHELD` line. The design says explicitly: *"the
item is left `ready` and unassigned, so the interactive Mac dispatcher
(INGRESS-CAPABLE) picks it up through the same Step 4 pool and finishes it
end to end."*

That sentence is the load-bearing assumption, and it does not hold in
practice.

## Root cause: the hand-off target is not reliably running

1. **The Mac dispatcher is intentionally not resident/scheduled.** Per the
   skill's own "Intended invocation" and "Why the resident role has to be a
   live session" sections, the Mac runs `metaworker-dispatch` only when a
   human starts it (single invocation or `/loop metaworker-dispatch`) — a
   deliberate choice, because the resident role needs to call
   `PushNotification` and hold real conversational presence, which a bare
   cron job cannot do. There is no mechanism that ages, escalates, or
   otherwise notifies anyone when an ingress-gated chip has been waiting for
   days with the Mac dispatcher not running.

2. **Cloud dispatchers structurally cannot hand off to the Mac.**
   `dispatch_remote_launch.py --box <ree-cloud-N|local>` already supports
   launching a worker on a *different* box, but `--box local` only runs
   locally where the script itself is invoked (`run_on()`: `if box ==
   "local": return run(["/bin/bash", "-lc", cmd], ...)` — no SSH at all).
   No cloud box holds an authorised key to the Mac's `sshd`
   (`dispatch_tier_select.py`'s own docstring, confirmed 2026-08-25: the
   Mac's `sshd` is reachable over WireGuard but no cloud key is
   authorised in it). So even a dispatcher that *wanted* to hand this chip
   to the Mac has no channel to do so.

3. **`dispatch_tier_select.py` computes machine eligibility, not chip
   routing, and has no concept of ingress capability at all.** Read in
   full: `select()` returns which of `{local, ree-cloud-4, ree-cloud-5}`
   are eligible to dispatch *this round*, purely from budget stage,
   `metaworker_role_verdict` (cloud-4's experiment-priority call), and live
   reachability/load — the same global answer regardless of which chip is
   being considered. It is consumed once per cycle to gate whether the
   *box already running the cycle* should dispatch at all (and, since
   2026-08-18, to let that box additionally launch on another *eligible and
   reachable* box via `dispatch_remote_launch.py`). It never inspects a
   chip's deliverable, and `ree-cloud-1` (the hub) is not in its ladder
   (`LADDER_MACHINES = (LOCAL, CLOUD4, CLOUD5)`) at all. Condition 4 — chip-
   scoped, prompt-inspecting — is the only ingress-aware logic in the
   system, and it only ever answers "can *this* box finish it," never
   "who can."

4. **The hub (`ree-cloud-1`) is the one structurally-possible automatic
   target, and nothing points at it.** Confirmed live 2026-08-26 (SSH from
   `ree-cloud-5`, which already holds a key to the hub):
   - `ree-cloud-1` runs `ree-coordinator.service` + `ree-sync-daemon.service`
     and is reachable from both cloud dispatch boxes over the same SSH path
     `dispatch_remote_launch.py` already uses for cloud-4<->cloud-5.
   - It has **no** `ree-metaworker.timer`/`ree-metaworker.service` —
     `systemctl list-unit-files | grep -i ree` lists only the coordinator,
     sync-daemon, explorer, runner, and two housekeeping timers. No
     resident dispatcher has ever run there.
   - It has **no** `REE_assembly/coordinator.env` — only a
     `coordinator.env.example`. The coordinator itself is configured via
     `EnvironmentFile=/etc/ree-coordinator.env` (server-side), a different
     file than the client-side one condition 4's own check reads. So even
     if a dispatcher were installed there, the existing INGRESS-CAPABLE
     check (`[ -r "$ENV" ] && grep -qE '^COORDINATOR_URL=' ...` against
     `REE_assembly/coordinator.env`) would misclassify the hub as
     INGRESS-INCAPABLE too, without a separate fix.
   - The hub is also the one box every other section of `CLAUDE.md`
     deliberately keeps free of extra load: never a `remote_pytest.sh`
     target for throughput reasons, never touched by the cloud-scaler,
     no commit-guard installed. It is a 2 vCPU / 3 GB box running the
     coordination plane's single point of failure. Adding metaworker
     dispatch workers to it is a real capacity/reliability trade, not a
     free win.

## A compounding, separate finding (not this chip's root cause, but relevant)

`chip-20260814-queue-causal-sleep-matched-arm`'s history shows the hand-off
target failing even when it *did* eventually get a turn:

- **2026-08-18, `ree-cloud-5`:** a worker was actually dispatched (worktree
  `metaworker-chip-20260814-queue-causal-sleep-matched-arm` still exists,
  claim commit `1812da7b`). It could not complete the queue action anyway —
  it hit an unrelated mandatory `/queue-experiment` Step 2.5c `corrupting`
  stop (`contextmemory-write-path-addressing-degeneracy`, a genuine
  substrate defect) — but it handled that correctly: real design-doc work
  landed in `REE_assembly` `3a63239277`, and the chip was left `open` via
  `unclaim` with an explicit resume condition, noting *"Step 8.6 ... cannot
  be completed from ree-cloud-5 ... this must eventually be queued from the
  Mac."* That gating chip (`chip-20260816-implsub-contextmemory-writepath-
  degeneracy`) has since resolved `done`.
- **Some point before 2026-08-21, on the Mac:** a second attempt did run —
  `chip-unlandedwt-dlaptop-metaworker-chip-20260814-92a2d0fc78d3` (now
  `done`, i.e. the *GC/repair* of the stranded worktree is done) documents
  that the Mac worktree held commits `origin/master` cannot reach and "the
  worker died (or exited without landing) without landing this work." So
  the Mac dispatcher *did* eventually pick this chip up, and still failed
  to land it — for a different reason (crash/exit-without-landing) than the
  routing gap this investigation targets.

Net effect: the chip's substrate gate is now clear, but nobody has
re-attempted actually queuing it since. This is a second, independent gap
(worker reliability / crash-safety, not routing) worth a follow-up but out
of this chip's scope. Recommend a human (or the next Mac-side dispatch
cycle) re-check `chip-20260814-queue-causal-sleep-matched-arm`'s resume
condition and either re-dispatch it or queue it directly.

## Why option (a) from the brief, as literally stated, doesn't close the gap

The brief proposed teaching `dispatch_tier_select.py` to compute a
per-chip eligible set restricted to `{Mac, hub}` when a chip directs
`/queue-experiment`, mirroring condition 5's per-chip prompt inspection.
Doing only that would not help: `eligible` narrowed to `{local,
ree-cloud-1}` still has to be *actionable* by whichever box is running the
cycle, and per point 2 above, `ree-cloud-4`/`ree-cloud-5` cannot reach the
Mac at all, and `ree-cloud-1` is not wired as a launch target or a resident
dispatcher today. The narrowed eligible set would just report `tier: null`
with an eligible-but-unreachable machine in it — a more precise diagnosis,
not a fix. The real blocker is the launch-capability + hub-capacity
decision in point 4, not the eligibility computation.

## What was shipped now (low risk, no architecture decision required)

Added an **aging-escalation clause** to `.claude/skills/metaworker-dispatch/
SKILL.md` condition 4 (and a cross-reference at the Step 3.5 IGW gate),
mirrored to `.agents/skills/metaworker-dispatch/SKILL.md` per the dual-
skill-directory convention. It mechanizes what condition 6 already asks for
prose-only ("surface it to the user as an ageing item") and that prose
form has demonstrably not worked for condition 4's chips: once a chip has
been logged `WITHHELD ... condition 4` in 3+ separate cycles, or is 48h+
old and still in the ledger, the dispatcher raises **one** `kind: decision`
chip (deduped against an existing open one) naming the aged chip, so it
reaches the user through the same `PushNotification`/re-ask channel Step
5's Orchestrator already owns — instead of depending on someone reading a
dispatch log. It does not dispatch or mutate the original chip, and it
does not change condition 4's own withhold behaviour at all.

This does not require any resource/architecture trade-off and was safe to
ship without consent.

## What was NOT built, and why: raised as a decision chip instead

Closing the gap for real means either:

- **(a) install a resident dispatcher on the hub** (`ree-cloud-1`), the one
  box that is both SSH-reachable from the cloud fleet and genuinely
  INGRESS-CAPABLE — requires accepting shared load on the coordinator's own
  box, teaching `dispatch_tier_select.py`/`dispatch_remote_launch.py` about
  a fourth machine, and fixing the INGRESS-CAPABLE check to also recognise
  `/etc/ree-coordinator.env` (or "coordinator co-located"); or
- **(b) authorise a cloud-fleet SSH key on the Mac**, closing the
  `dispatch_remote_launch.py --box local` gap directly — a security
  decision `dispatch_tier_select.py`'s own docstring already says belongs
  to the user, not to a dispatcher; or
- **(c) make the Mac dispatcher resident/scheduled after all** — reverses
  an explicit, reasoned prior design decision (no live session -> no
  `PushNotification`, no conversational presence) and needs the same
  sign-off that decision got.

Each is a genuine resource/security trade-off with no clearly-dominant
option and no way to test it live from a headless cloud session. Per the
HEADLESS WORKER CONTRACT (rule 7: "contested dispositions, unresolvable
resource conflicts"), this was raised as a `kind: decision` chip rather
than decided here:

`chip-20260826-ingress-dispatch-architecture-decision`

citing this document, the three confirmed-aged chips, and the SSH/hub
facts confirmed live above.

## Evidence appendix

- Dispatch log counts on `ree-cloud-5` (`~/ree_metaworker_dispatch.log`,
  133617 lines spanning 2026-08-02 to 2026-08-26):
  - `chip-20260814-queue-causal-sleep-matched-arm`: 148 mentions, first at
    or before cycle-line 50048, still confirmed withheld/correctly-excluded
    as of the most recent cycle read (2026-08-26).
  - `chip-20260825-mech492-falsifier-queue`: 7 mentions, all `WITHHELD ...
    condition 4`, no worktree ever created.
  - `chip-20260825-e1-rollout-horizon-sweep-probe`: 4 mentions, same
    pattern, no worktree ever created.
  - Global: 2102 lines mention `INGRESS-INCAPABLE` in this log alone.
- `ree-cloud-1` (hub) checked live via SSH from `ree-cloud-5`:
  `systemctl list-unit-files | grep -i ree` -> `ree-coordinator.service`,
  `ree-explorer.service`, `ree-git-sync-repair.{service,timer}`,
  `ree-live-status.{service,timer}`, `ree-runner.service`,
  `ree-sync-daemon.service` — no `ree-metaworker.*`.
  `systemctl cat ree-coordinator.service` ->
  `EnvironmentFile=/etc/ree-coordinator.env`.
  `find .../REE_assembly -maxdepth 3 -iname "coordinator.env*"` ->
  `coordinator.env.example` only.
- `ree-cloud-4` was not independently checked (no SSH key from
  `ree-cloud-5` to `ree-cloud-4` — the same known cross-fleet key gap
  `dispatch_tier_select.py`'s docstring already documents); the brief's
  claim of "dozens of cycles on both boxes" is taken as given and is
  consistent with condition 4 applying identically on both (neither has
  `coordinator.env`).

## Human decision (2026-08-26, via chip-20260826-ingress-dispatch-architecture-decision)

**Decision: (b) Authorize cloud->Mac SSH.** The user chose to let cloud dispatchers
hand off ingress-gated work directly to the Mac via `dispatch_remote_launch.py --box local`,
rather than installing a resident dispatcher on the fragile hub, or reversing the
deliberate interactive-only Mac dispatch design.

**Status: PENDING the user's own manual step.** Adding an SSH public key to
`~/.ssh/authorized_keys` is a system/security-setting change the orchestrator is not
permitted to perform even with explicit authorization (see the safety boundary this
was flagged against). The orchestrator supplied the two cloud boxes' existing public
keys (`ree@ree-cloud-4-metaworker`, `ree-cloud-5-fleet-outbound`) and a `command=`
restriction option for scoping the grant down to `dispatch_remote_launch.py --box local`
only, rather than a bare unrestricted key. As of this cycle, reachability has not yet
been re-verified -- do not assume the key is in place; check `ssh -o BatchMode=yes ree@<mac-tailscale-or-wireguard-ip> true` (or equivalent) from a cloud box before relying on this path, and if reachable, wire `ree-cloud-4`/`ree-cloud-5` dispatch cycles to actually invoke `dispatch_remote_launch.py --box local` for ingress-gated candidates instead of leaving them WITHHELD.

**Follow-on chip needed once the key is confirmed in place:** wire condition 4's
WITHHELD branch to attempt a hand-off to the Mac via SSH when a chip is ingress-gated,
falling back to the existing WITHHELD-and-report behavior if the Mac is unreachable
or its own memory floor is exceeded (do not let a cloud dispatcher pile work onto an
already-constrained Mac blind to its load -- read `mac_dispatch_load.json` first).
