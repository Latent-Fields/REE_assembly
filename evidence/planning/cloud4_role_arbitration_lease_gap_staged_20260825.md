**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry).**

# ree-cloud-4 role arbitration vs. the 2026-08-25 Dispatcher/Healer lease split

Written 2026-08-25T20:15Z by session `cloud4-runner-failsafe`
(chip-20260823-cloud4-runner-failsafe), while investigating the second
firing of the ree-runner failsafe on ree-cloud-4.

## What was fixed already (this session, landed on REE_Working master 1d1f2374)

`scripts/ree_runner_failsafe.py` used `systemctl is-active ree-metaworker.timer`
as a proxy for "the metaworker healthily owns the box". That proxy went
permanently, silently false when the resident Dispatcher timers were retired
fleet-wide (2026-08-23, made the permanent standing state 2026-08-25 by the
Dispatcher/Healer role split -- `check_metaworker_timer_state.py`'s
self-probe on ree-cloud-5 reports `RETIRED`, `retired_at=2026-08-23T09:55:45Z`).
Confirmed live: this made the failsafe's `not timer_active` branch fire
unconditionally, so every runner-down state read as "restart" regardless of
whether `metaworker_role_verdict.py`'s actual arbitration wanted the runner
stopped -- the exact contention bug the failsafe's own negative control
exists to prevent.

Fix landed: the failsafe now calls `metaworker_role_verdict.decide()`
directly against the live queue (`role_should_run()`), the same authority the
Dispatcher wrapper consults, instead of proxying via whichever cadence
mechanism happens to be ticking. Tests: 20, all passing
(`scripts/test_ree_runner_failsafe.py`).

## The gap this does NOT close (this doc's subject)

The failsafe is a 15-minute-latency **backstop**. The **primary** mechanism
that is supposed to keep ree-runner's ownership current is
`ree-metaworker-dispatch.sh`'s "Dual-role arbitration (ree-cloud-4)" block,
which calls `metaworker_role_verdict.py` and issues
`sudo systemctl start/stop ree-runner` every cycle.

Before 2026-08-25 that wrapper ran on a **resident systemd timer**
(`ree-metaworker.timer`, every 5-30min), so role arbitration was
re-evaluated on a steady cadence regardless of anything else.

As of the 2026-08-25 Dispatcher/Healer role split
(ree-v3 `4597a4e1`, `8202bd7b`; commit message: "the roles were split on
2026-08-25"):

- The resident Dispatcher timer is **permanently retired**. The Dispatcher
  (`ree-metaworker-dispatch.sh`, which is where the dual-role arbitration
  code lives) now runs **only** while an Orchestrator session holds a run
  lease in `dispatcher_control.json` (`.claude/skills/metaworker-orchestrate/
  SKILL.md` Step 1: `dispatcher_control.py grant --box <box> --lease-hours 2`,
  clamped to `REE_DISPATCH_LEASE_MAX_HOURS` (6), renewed every Orchestrator
  cycle).
- A new resident, unleased **Healer** (`ree-metaworker-healer.sh`,
  `ree-metaworker-healer.timer`, hourly, confirmed installed and active on
  ree-cloud-5) runs `/metaworker-repair` -- but by design **never dispatches
  `kind:work`** and, confirmed by reading both the wrapper script and the
  skill (`grep -c "role_verdict\|ree-runner\|dual-role" .claude/skills/
  metaworker-repair/SKILL.md` = 0 hits), **never touches
  `metaworker_role_verdict.py` or `ree-runner` at all.**
- `metaworker-orchestrate/SKILL.md` Step 1's example, and its only worked
  example, grants a lease to `ree-cloud-5`. Nothing in that skill grants a
  standing/recurring lease to `ree-cloud-4` specifically, and nothing
  requires one.

**The consequence:** once `metaworker_role_verdict.py` decides ree-cloud-4's
runner should be stopped (state=`dispatching`, no surge, box holds no claim),
nothing re-evaluates that decision -- and therefore nothing can reverse it
even once a real surge later arrives -- unless an Orchestrator session
happens to grant cloud-4 a lease for some other reason. There is currently no
guarantee that ever happens. This matches the observed symptom exactly:
`ree-cloud-4-metaworker.json`'s own orchestrator heartbeat has been stale
since `2026-08-23T09:59:36Z` (health=`stalled`, "12 consecutive cycle(s)...
no dispatch and no live worker"), i.e. cloud-4's own Dispatcher cycles
stopped around the same time the resident timer was retired, and have not
resumed since -- while cloud-5 (this box) took over as the fleet's resident
orchestrator/dispatcher (cycle 3804 as of this writing, healthy).

The ree-runner failsafe (15-min, self-contained, always resident, unleased --
confirmed via its own separate `ree-runner-failsafe.timer`) is what actually
caught and corrected this, twice now (2026-08-20, non-issue -- see that
chip's resolution note; 2026-08-23, this issue). It is a safety net, not a
substitute for the primary mechanism running.

## Two remediation options (needs a human/Orchestrator decision, not made here)

**Option A -- give ree-cloud-4 a standing/auto-renewed Dispatcher lease.**
Simplest to describe: whichever process now plays the "resident Orchestrator"
role on ree-cloud-5 (currently: this box's own resident dispatch, per its
healthy heartbeat) also periodically grants ree-cloud-4 a lease, purely so
its Dispatcher cycle -- and therefore its role-arbitration block -- keeps
running on a steady cadence. Cost: reintroduces close to the original
per-cycle token floor for cloud-4 specifically (the ~117k-token context load
the whole split was built to eliminate), UNLESS the lease is granted but the
Dispatcher's own `dispatch_preexit_check.py` / idle-skip logic is trusted to
make an idle cycle cheap -- worth checking whether that pre-exit check
happens BEFORE or AFTER the dual-role arbitration block runs (if before, an
idle cycle might skip the claude launch AND the role check together, which
would silently reopen this exact gap; if after, it is cheap and safe). This
needs the actual wrapper's Step ordering re-examined, not assumed.

**Option B -- move role arbitration into the resident Healer.** Add the
`metaworker_role_verdict.py` check + `sudo systemctl start/stop ree-runner`
calls to `ree-metaworker-healer.sh`, alongside its other repair-only checks,
gated the same way the Dispatcher's block is (`REE_DUAL_ROLE=1`, presumably
only ever set on cloud-4's healer unit). This is "plumbing", matching the
Healer's own stated charter ("must stay healthy whether or not anyone is
dispatching"), and role arbitration itself never spends the token budget on
new work (it is plain systemctl/python, no `claude` invocation) -- consistent
with why the Healer is allowed to be resident and unleased in the first
place. Cost: the Healer would need read access to `ree-v3/experiment_queue.json`
(already does, indirectly, via its repair skill) and `sudo -n systemctl
start/stop ree-runner` sudoers privilege it may not currently have (the
Dispatcher's service unit presumably already has this on cloud-4; needs
confirming whether the Healer's service unit does too). This is the
structurally cleaner fix (role arbitration is inherently "does the box's
role match reality right now", a resident-cadence question, not a
lease-gated-dispatch question) but was not implemented in this session
because: (a) it requires editing `ree-metaworker-healer.sh`, a live
production deploy script this session has no claim on and did not verify is
even installed on ree-cloud-4 yet (cannot SSH there -- confirmed cross-fleet
key-provisioning gap, `check_dispatch_fleet_health.py`'s documented
`SSH-AUTH-GAP`); (b) it changes which systemd unit holds privileged
`sudo -n systemctl` access, a real security-surface tradeoff worth a second
opinion; (c) it cannot be end-to-end verified without deploying to cloud-4,
which this session cannot do.

**This session's recommendation, weakly held:** Option B, because it matches
the actual shape of the problem (role arbitration is inherently a resident
concern, not dispatch work) and because Option A's token-cost interaction
with `dispatch_preexit_check.py` needs verification before it can be trusted
not to silently reopen the same gap it's meant to close. But this is a
genuine design tradeoff a human or the session that built the 2026-08-25
split should weigh in on, not something to land unilaterally from an
investigation session that cannot test either change against the actual box.

## Evidence trail

- `check_metaworker_timer_state.py --json` (run from ree-cloud-5, 2026-08-25T20:02Z):
  `ree-cloud-5` timer `RETIRED` (retired_at 2026-08-23T09:55:45Z, self-probe);
  `ree-cloud-4` `SSH-AUTH-GAP` (cannot confirm cloud-4's own timer state
  directly -- see below).
- `REE_assembly/evidence/experiments/runner_heartbeats/ree-cloud-4-metaworker.json`:
  `last_tick_utc: 2026-08-23T09:59:36Z`, `health: stalled`, `no_dispatch_streak: 12`.
- `ree-v3` git log: `4597a4e1` ("deploy: resident Healer units for the
  metaworker role split"), `8202bd7b` ("healer units: fix PATH and auth"),
  both dated 2026-08-25.
- `ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh` header comment:
  "Reference copy... Run: systemd timer, every 30 minutes, 5min until
  2026-08-24" and the "resident timers are now retired" language inside the
  script's own lease-follows-demand section.
- `.claude/skills/metaworker-orchestrate/SKILL.md` Step 1: only example is
  `--box ree-cloud-5`; no cloud-4 mention anywhere in that skill file
  (grepped for "cloud-4", 0 hits).
- `.claude/skills/metaworker-repair/SKILL.md`: 0 hits for
  "role_verdict|ree-runner|dual-role|dual role".
- Cross-fleet SSH: `ree-cloud-5 -> ree-cloud-4` and `hub -> ree-cloud-4` both
  `Permission denied (publickey,password)`; WireGuard handshake to cloud-4
  (10.8.0.14) fresh (16s old when checked), so the box is up -- this is the
  documented `SSH-AUTH-GAP` (`check_dispatch_fleet_health.py` module
  docstring), not evidence cloud-4 is down. This is why cloud-4's own
  `journalctl`/`~/ree_metaworker_dispatch.log` could not be inspected
  directly from this session.

## What was NOT done in this session, and why

- Did not touch `ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh`:
  claimed by a concurrent session (`metaworker-healer-cycle-
  20260825T172414Z-wrapper`, "repair: land stranded wrapper-deploy comment
  fix") at the time this investigation started.
- Did not touch `ree-metaworker-healer.sh` or `metaworker-orchestrate/
  SKILL.md`: no claim conflict, but implementing Option B or A without the
  ability to test against ree-cloud-4 (SSH-AUTH-GAP) or verify the Healer's
  sudoers/PATH setup on that box felt like the wrong risk to take
  unilaterally in a headless investigation session, versus surfacing the
  choice clearly.
