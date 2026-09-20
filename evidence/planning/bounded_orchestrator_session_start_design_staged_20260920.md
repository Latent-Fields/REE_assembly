# Bounded on-demand Orchestrator, zero-token keepalive, and the /workset session-start row

**Status: AWAITING USER REVIEW** -- design and staging only. Nothing here is built.
Staged 2026-09-20T11:39:53Z by `eloquent-jepsen-5f6242` via `/metaworker-learning`.
Source chip: `chip-20260920-ml-bounded-orchestrator-session-start-row`.
Decision chip: `chip-20260920-bounded-orchestrator-build-decision` (kind: decision -- the user's to answer).

User direction (2026-09-20, to the Orchestrator session `orchestrate-20260919-2125` after it landed):
make the Orchestrator an ON-DEMAND session that is BOUNDED FROM THE BEGINNING, with its start
prompt served from a distinct, non-task entry on `/workset`; unattended ticks become a cheap
script, not a Claude session and not the Dispatcher.

---

## 0. Summary and recommendation

The long-lived Orchestrator couples three things that do not belong together: **liveness** (the
lease is only renewed while one conversation keeps turning), **state** (which worker is where,
which decisions were already raised, the tick helper) and **judgment** (curation, the decision
lane). Only the third needs a Claude session. The design separates them:

| Concern | Today | Proposed |
|---|---|---|
| Judgment (curate, ask, route answers) | one ever-growing conversation | a bounded session, started on demand from a generated prompt |
| Liveness (lease, trigger) | that conversation's 30-min `/loop` | a zero-token gate on each worker box, live only inside a user-granted **authorisation window** |
| Dispatch of approved work | a `claude -p` Dispatcher cycle, ~117k tokens before anything launches | a scripted lane launcher built from scripts that already exist (section 4d); the Dispatcher session kept only for what needs judgment |
| State | conversation memory + a per-session scratchpad | durable records the start prompt is generated from |

Recommended build order: **start-row first** (section 8, option C), keepalive second. The start
row is the low-risk half, it removes the measured cost on its own, and the keepalive reverses a
standing user decision so it deserves its own yes.

---

## 1. Recurrence (skill Step 1) -- two genuine occurrences, one root cause

- Occurrence 1: `orchestrate-20260918-1840-cloud4`, user window 2026-09-18T19:10Z..2026-09-19T09:10Z
  (`WORKSPACE_STATE.md` entry stamped 2026-09-19T09:27:59Z).
- Occurrence 2: `orchestrate-20260919-2125`, 2026-09-19T21:25Z..2026-09-20T11:02Z
  (`WORKSPACE_STATE.md` entry stamped 2026-09-20T11:04:18Z).

Same root cause, not merely the same symptom: both lost lease continuity and paid cold re-reads
because lease renewal and run state lived inside one conversation's turn cadence.

### 1a. The figures in the chip are NOT in any durable record -- so they were re-measured

The chip cites 17% -> 83% context growth, a 2-hour `AskUserQuestion` wait, a Mac sleep
03:55Z-09:30Z and 600-800k cold re-reads. A search of `WORKSPACE_STATE.md`, both metaworker
skills and `evidence/planning/` finds **none of those figures**; each run's durable artifact is
one paragraph. That absence is itself evidence for section 5. The figures were therefore
re-measured from the session's own transcript usage records
(`~/.claude/projects/-Users-dgolden-REE-Working/b081618a-d13b-48ac-a091-db90dcf1eb5c.jsonl`,
1089 assistant turns, 2026-09-14T23:22Z..2026-09-20T11:30Z -- it is ONE conversation resumed
across every orchestrator cycle since 2026-09-14, not two):

- Context: 328k after the 2026-09-18 compaction -> 813k at 2026-09-20T10:10Z, peak **887k**
  (consistent with the "83% of 1M" report). It had already reached 810k once before, on
  2026-09-18T18:12Z.
- **14 idle gaps over 1 hour; 13 of them forced a cold cache rebuild** (`cache_creation` of
  351k..761k tokens on the next turn, `cache_read` collapsing to ~37-49k). Summed: about
  **7.5M tokens of cache writes caused by nothing but idleness.** Gaps in the two evidence runs:
  2.1h, 1.3h, 2.3h, 4.3h, 7.3h, 1.1h, 2.6h, 5.6h.
- The 5.6h gap is 2026-09-20T03:55Z -> 09:29Z. `pmset -g log` shows `Clamshell Sleep` from
  04:22 local (03:22Z): the lid was closed. Rebuild on wake: 733k tokens.
- Mean `cache_read` per turn across the transcript: ~463k. A fresh session sits near 150k.

---

## 2. Measurements made for this design (2026-09-20, read-only)

1. **Hub -> worker boxes.** From the hub (`ree@91.98.130.117`): TCP 22 is OPEN to both worker
   public IPs (91.99.68.94, 46.224.127.182), but `ssh -o BatchMode=yes` returns
   `Permission denied (publickey,password)` -- the hub's `~/.ssh/` holds no private key at all
   (`authorized_keys`, `known_hosts` only). The workers are not WireGuard-routable from the hub
   by the addresses tried (10.8.0.4/.5: no route). `claude` is not installed on the hub.
   **So the hub cannot trigger a worker today without a new keypair being provisioned on it.**
2. **Mac launchd.** 22 `com.ree.*` agents exist, so the pattern is established -- but the
   2026-09-20 lapse was a clamshell sleep, and launchd jobs do not run through that. A Mac-hosted
   keepalive fails in exactly the overnight case that motivated it.
3. **Worker boxes themselves.** `ree-cloud-4` and `ree-cloud-5`: up 12 days; each has
   `~/.ree_coordinator_client.json`, reaches the coordinator (`/health` 200), runs
   `dispatcher_control.py check --box $(hostname)` correctly (both read STOP, exit 3, right now),
   and already carries systemd timers (`ree-metaworker-healer`, `ree-hygienetick`,
   `ree-metaworker-autosync`, `ree-git-sync-repair`). `ree-metaworker.service` is `Type=oneshot`
   and its wrapper (`/usr/local/bin/ree_metaworker_dispatch.sh`, 722 lines) already performs the
   coordination-plane pause check before spending a `claude` invocation.
4. **Campaign launches already record the worker address.** `dispatch_campaigns.py`
   `build_launch()` (:1425-1429) stores `box`, `session_uuid`, `worktree`, `at`, `launched_by`.
   Item (4) of the brief is therefore narrower than it looked (section 5).
5. **The /workset page is `REE_assembly/workset.html`, not `explorer.html`.** Its stamp is
   `<!-- WORKSET_VERSION: 2026-08-20.3 -->` (line 2). The chip's "EXPLORER_VERSION bump" is the
   wrong stamp for this change; see section 9.

---

## 3. Item (1)+(2): the session-start row

### 3a. Facts that shape it (chip_ledger.py / serve.py / workset.html)

- `VALID_KIND = ("work", "decision", "report")` at `scripts/chip_ledger.py:633`, enforced only
  by argparse `choices=`. The coordinator stores `kind` as unconstrained TEXT
  (`ree-v3/coordinator/schema.sql:217`; no CHECK anywhere) and never inspects it. **Adding a
  kind needs no schema or endpoint change.**
- Every dispatch-facing consumer is a POSITIVE `== "work"` test
  (`dispatch_candidate_order.py:979`, `dispatch_campaigns.py:797`,
  `check_dispatch_fleet_health.py:1210`, `pause_pressure.py:488/642`), so a new kind is
  non-dispatchable and non-bundleable by construction -- the same property `report` relies on
  (`chip_ledger.py:394-400`). No exclusion list to extend.
- Three TALLIES are positive tests too and would silently omit the kind:
  `dispatch_preexit_check.py:249-250`, `serve.py:7371-7374` (`/api/fleet/summary`), and the
  `pc-kind-filter` dropdown in `workset.html:558-563` (which already lacks `report`).
  `dispatch_campaigns.py:797`'s refusal string names only decision/report. `mcp_server.py:644`
  hardcodes the kind list in help text.
- `amend-prompt` (`chip_ledger.py:4369-4452`) rewrites `prompt` in place, requires the literal
  `[chip_ref: <ref>]` marker, no-ops when unchanged, and appends the WHOLE previous prompt to
  `prompt_history`. There is no verb that rewrites `title`/`tldr`.
- `archive` only strips fat fields from TERMINAL chips (`select_archivable`, :4713-4739). An
  always-open row is never archived, so **its `prompt_history` grows without bound.**
- `copyChipPrompt()` (`workset.html:999-1035`) always prepends a `chip_ledger.py claim`
  preamble. A standing row must NOT tell its reader to claim it.

### 3b. Options for where the prompt lives

| | Option | For | Against |
|---|---|---|---|
| R1 | Stored row, rewritten by each landing session via `amend-prompt` | exactly the brief's wording; history kept | stale the moment a session dies without landing -- the case the brief says must work; every rewrite stores a full prior prompt in a never-archived row (the ledger already reached 20 MB once) |
| R2 | No ledger row; `serve.py` computes the prompt at request time | never stale | no durable identity, no history of the bounds the user agreed to, nothing for `/api/chips` consumers to see |
| **R3** | **Hybrid (recommended): a standing `kind: session_start` row per role holds the STABLE part -- role, bounds, landing step -- amended rarely with history; `serve.py` composes `row.prompt + live-state block` at copy time** | never stale (state is never stored); history covers what matters (policy changes); `prompt_history` grows per policy change, not per session | two pieces instead of one; the composed text is not what the ledger stores, so the panel must say so |

Recommendation: **R3.** "Rewritten in place with history" applies to the policy text; the state
block is generated, which is the only way a dead session still leaves a current prompt.

One row per role, fixed refs: `session-start-orchestrator` first; `session-start-healer` and
others only when asked for. `status` stays `open` forever. It is recorded once with
`record --kind session_start` and never claimed.

### 3c. The live-state block (generated; every source is already durable)

| Line in the prompt | Source |
|---|---|
| open `kind: decision` chips, oldest first, with `last_raised_at` | coordinator `/chip/list` (fallback `TASK_CHIPS.json`) |
| launched campaign entries with box + worktree + session uuid | `scripts/dispatch_campaigns.json` `launches[]` |
| parked workers and their question | `.worker_parked.json` via the launch address (section 5) |
| open lane entries, their `target_box` and `expires_at` | `dispatch_campaigns.py list --live --json` |
| lease state per box; authorisation window and what remains of it | `dispatcher_control.py status`, window record (section 4) |
| queue depth vs floor | `check_experiment_queue_floor.py --json` (read-only, fails open) |
| pause holder, if any | `coordination_plane.is_coordination_plane_paused()` |
| last WORKSPACE_STATE entry from an `orchestrate-*` session | `WORKSPACE_STATE.md` head |

**"Needs you" count** = open decision chips never raised or last raised > 24h ago (Step 3c's
existing cadence) + parked workers whose question needs a human + lane entries expiring within
6h with no authorisation window + an expired window that still has open lane entries. Shown as
a badge on the panel header; zero means "no reason to start a session".

New endpoint `GET /api/session_start?role=orchestrator` -> `{role, chip_ref, policy_prompt,
state_block, needs_you, generated_at}`. The generator lives in `scripts/session_start_prompt.py`
(testable without serve.py; also runnable from a terminal, which covers a dead serve.py).

### 3d. The panel

A `<details id="session-starts">` block ABOVE "Pending chips" in `workset.html`, following the
existing pattern (markup -> `loadSessionStarts()` -> `renderSessionStarts()`), one card per
role: needs-you badge, the state block rendered readably, and a **Copy start prompt** BUTTON
(reusing `copyText`/`markCopied`) that copies the composed text with NO claim preamble.
`renderChips()` filters `kind === 'session_start'` out of the pending list so the row never
looks like a task. Add `report` and `session_start` handling to the three tallies in 3a.

---

## 4. Item (3): the keepalive

### 4a. This re-opens a decided question, and says so

`metaworker-orchestrate/SKILL.md:960-963`: the lease-aware-timer tradeoff "was already asked and
answered once (2026-08-27); don't re-propose the same tradeoff without new evidence that manual
triggering has become a real bottleneck." **The evidence in section 1a is that new evidence:**
manual triggering now means a Claude session turning every 30 minutes at a 463k-token mean
context for 14 hours, 13 idleness-forced rebuilds totalling ~7.5M tokens, and two lease lapses
(one on a human wait, one on a closed lid) during windows the user had explicitly asked to keep
open. On 2026-08-27 the alternative to a timer was a person typing a command; today it is the
most expensive session in the estate. The tradeoff that was decided is not the one now on the
table. The user may still decline it (section 8, option C or D).

### 4b. What made 2026-08-23 a runaway, and the four properties that prevent a repeat

The runaway (~513 ticks/day, ~117k-token floor each, a weekly budget in under two days) had
three ingredients: a trigger with no human grant behind it, a candidate list that was never
empty (`hygiene_tick` regenerates continuously), and no expiry. The keepalive must have none:

1. **Authorisation window -- a human grant with an expiry.** A new record (section 4e) written
   only by an attended session on the user's explicit instruction: `granted_by`, `granted_at`,
   `expires_at`, `boxes`, `max_cycles_per_box`, the user's words in `note`. Clamped (proposed:
   16h; both evidence runs were ~14h). **Silence still stops the fleet** -- the property
   `dispatcher_control.py:14-22` exists for -- at window granularity: nobody can extend a
   window but a session in front of the user. Worst-case unattended bill is bounded by
   `max_cycles x per-cycle floor + the approved lane entries`, and is stated at grant time.
2. **Lane-gated triggering.** Trigger only when `dispatch_campaigns.py list --live` holds an
   open entry whose `target_box` admits this box. Since 2026-09-16 a cloud cycle's candidate set
   IS the curated lane, so the "never-empty candidate list" ingredient is already gone; the gate
   makes the empty case cost zero tokens instead of one 117k cycle. Lane entries exist only
   because the user approved them (both evidence runs: campaigns put to the user via
   `AskUserQuestion`).
3. **Never while paused**, never while a cycle is already running on the box, never past
   `max_cycles_per_box`, never when `dispatch_usage_cooldown.py` says the box's account is cold.
4. **Zero tokens when it declines -- and zero dispatch tokens when it acts** (section 4d). The
   gate is shell + python. It is not a Claude session and not the Dispatcher.

**What it cannot do:** read the plan allowance. `get_usage` is in-app only, so Step 0a's
85/95% bands stay with attended sessions. Consequences, stated rather than hidden: a window
must be granted only after a Step 0a reading, the grant records that reading, and the default
clamp drops (proposed: 6h) when the reading was >= 70% -- an unattended window cannot see itself
cross 85%. The per-box reactive cooldown remains the only in-window brake on exhaustion.

### 4c. Where it runs -- options, with the measurements from section 2

| | Host | Works today? | Against |
|---|---|---|---|
| K1 | Mac launchd, ssh out (the existing tick helper, scheduled) | yes -- every path exists | stops with the lid (measured 2026-09-20); that is one of the two lapses it is meant to fix |
| K2 | Hub timer, ssh to workers | **no** -- no key on the hub (measured) | needs a new credential on the box that is meant to be dedicated to the coordination plane; widens the hub's blast radius |
| **K3** | **A systemd timer ON each worker box, running a local gate (recommended)** | yes -- boxes have the coordinator client, the lease check, the pause check and the timer infrastructure | a box the scaler has powered off cannot wake itself (no worse than K1, where the ssh also fails); needs the window readable from the box (4e) |

Recommendation: **K3**, with the lease itself carrying the window so no renewal is needed at
all. `ree-metaworker-keepalive.timer` (every 20 min) -> `scripts/metaworker_keepalive_gate.py`:

```
window valid for this box?            no -> exit 0 (silent)
dispatcher_control check --box        STOP by explicit request -> exit 0
coordination plane paused?            yes -> exit 0
usage cooldown active?                yes -> exit 0
ree-metaworker.service active?        yes -> exit 0
live lane entry admits this box?      no -> exit 0
cycles_this_window < max_cycles?      no -> exit 0, log CAP-REACHED once
otherwise                             launch the next approved lane entry (section 4d); count it
```

Always exit 0; every decline is one log line. It must reconcile with, not add to, the existing
timer story: `check_metaworker_timer_state.py`, `dispatcher_pauses.json`,
`account-handover` Step 2c and `ree-v3/coordinator/deploy/ree-metaworker.timer` still describe
the retired 5-minute timer as live (metaworker-dispatch/SKILL.md:9-10 and `cloud_workers.md:31`
too). The build includes correcting those, or the fleet ends up with three accounts of what
starts a cycle.

An explicit `dispatcher_control.py stop` still wins over an open window, so an attended session
(or the user) can end a window early with the existing verb.

### 4d. Dispatch itself should get cheaper, not just the Orchestrator (user direction, 2026-09-20 mid-session)

Added on the user's instruction while this was being staged: "the way things are dispatched
should end up some way that is better and more efficient than current methods ... it may use
some or all of older retired or current methods."

The gate in 4c, as first drafted, ends by starting `ree-metaworker.service` -- a `claude -p`
Dispatcher cycle that pays a **~117k-token fleet-state floor before it launches anything**
(`metaworker-orchestrate/SKILL.md:333`; the resident form of this cost was measured at ~59M
tokens/day). Since 2026-09-16 that floor buys almost nothing on the lane path: a campaign entry
is ALREADY curated, bundled, targeted at a box, given a model and a brief, pre-flighted (science
lane) and approved by the user. The judgment was paid for once, in the attended session. What
remains is mechanical, and **every mechanical step already exists as a tested script**:

| Dispatch-cycle step | Already a script |
|---|---|
| is the plane paused | `coordination_plane.py`; re-checked inside `dispatch_remote_launch.py` |
| may this box run | `dispatcher_control.py check` |
| budget / runaway brake | `dispatch_budget_gate.py` |
| account exhausted | `dispatch_usage_cooldown.py` |
| in-flight cap (`REE_DISPATCH_MAX_INFLIGHT`) | `count_inflight_workers.py` |
| candidate order, lane first | `dispatch_candidate_order.py` (campaign mode) |
| duplicate / invalidator triage | `dispatch_triage.py` |
| compose the brief | `dispatch_campaigns.py brief` (+ the HEADLESS WORKER CONTRACT, today inline in `metaworker-dispatch/SKILL.md` ~:1485 -- to be lifted into one file both paths read) |
| claim members, worktree, hooks, launch detached, record box + worktree + session uuid | `chip_ledger.py claim`, `dispatch_remote_launch.py --campaign-id ... --box local` |
| was the launch dead on arrival | `check_worker_launch.py` |

So the recommended end state is a **scripted lane launcher**, `scripts/dispatch_lane_launch.py`:
the box-side gate, on a pass, runs that chain and launches the WORKER directly. No Dispatcher
session sits between an approved entry and the worker that does it.

How it uses older, retired and current methods together:

- **Retired, reused:** the resident timer cadence (retired 2026-08-23/25). It was dangerous
  because each tick was a 117k-token session with a never-empty candidate list and no human
  grant. A tick that costs zero tokens, fires only inside a window, and launches only
  user-approved entries keeps the one thing the timer was good at -- nothing sits idle for 4.5h
  waiting for someone to type `systemctl start` (2026-08-27).
- **Current, kept as is:** the lease and its fail-closed evaluation, the campaign/science lanes
  and their approval step, the budget gate, the cooldown, the in-flight cap, the pause, the
  launch shape, `worker_message.py` for routing answers back.
- **Current, demoted:** the `claude -p` Dispatcher cycle. It stays available for what still needs
  judgment -- urgent chips outside the lane, and triage of an uncurated ledger -- run attended
  or by explicit trigger, not as the path every approved entry must pass through.
- **Older, kept:** Step 1d supervised subagents from the Mac session remain the cheapest path
  when the work fits on the Mac.

Rough size of the saving, from the two evidence runs: a 30-minute trigger on two boxes for 14h is
up to ~56 Dispatcher cycles, ~6.5M tokens of floor per run, before any worker does anything.
The scripted path spends none of it. Per launched entry the saving is one 117k floor plus the
minutes the cycle takes to derive state it then discards.

What this must NOT lose, and how: the Dispatcher's per-cycle STOP-CHECK reading is replaced by
the worker's own STOP-CHECK (every chip carries one) plus `dispatch_triage.py`; the DOA
classification stays via `check_worker_launch.py`; a launcher refusal of any kind leaves the
entry open and adds to the needs-you count rather than retrying in a loop. H5 (2026-08-23)
becomes this script's first regression test: no window -> no launch; empty lane -> no launch;
cap reached -> no launch.

Held-out note: no historical case exercises a scripted lane launch, so this rests on the
inventory above, not on history. It should ship behind the window with `max_cycles_per_box`
low for the first runs, and the Dispatcher cycle remains the fallback if it misbehaves.

### 4e. Window record and lease authority

Add `dispatcher_control.py window grant|revoke|status`, stored beside the leases in
`dispatcher_control.json` under `"windows"` (same fail-closed evaluation: missing, malformed or
expired means no window) and dual-written to the coordinator exactly as leases are.
`should_run()` becomes: explicit stop -> STOP; valid lease -> RUN; **valid window naming this
box -> RUN**; else STOP. Nothing renews anything on a timer, so there is no renewal to lapse
while the Mac sleeps -- the two lapses in section 1 cannot recur inside a window.

`grant` without a window keeps today's meaning (a <=6h lease held by an attended session) for
short attended cycles. `claim_advisory` learns that a window is a legitimate authority, which
also retires the recurring "lease outlives claim" finding (2026-08-26, 2026-08-29).

---

## 5. Item (4): conversation-only state -> durable records

| State that lived only in the conversation | Where it goes | Size of change |
|---|---|---|
| which worker sits in which worktree on which box | **already recorded** for campaign launches (`launches[]`). Gap: Step 1d subagent runs and any launch that bypasses `record-launch`. Make `record-launch` mandatory in Step 1d-i/ii and have the generator flag a `launched` entry with an empty `launches[]`. | small |
| which decisions were already raised, and when | `last_raised_at` + `raise_count` on the decision chip, via a new `chip_ledger.py amend-raised --chip-ref` (coordinator-mirrored like `amend-urgency`). Step 3c's "this session's own conversation history is the de-dup signal" is replaced by this field -- that sentence is the single strongest dependency on a long conversation in the skill. | medium (new verb + coordinator passthrough; `entry_json` needs no schema change) |
| the tick helper (`orch_tick.sh` in a per-session scratchpad, session id hardcoded) | `scripts/orchestrator_tick.py` with tests (`scripts/test_orchestrator_tick.py`, injected-data pattern): claim check, pause holders, lease/window status, Mac load publish, queue floor, campaigns gc + list, open decision chips from the coordinator, queue on origin, per-box liveness. `--no-trigger` default; triggering only with `--trigger` from an attended session. Shares its readers with `session_start_prompt.py`. | medium |
| context figures, waits, lapses | not stored per tick. The window record's `cycles` counter and the gate's log are the unattended trail; a session's own landing note carries the rest. | none |

`dispatch_tier_select.py publish` writes `mac_dispatch_load.json` (local, uncommitted). It stays
a Mac-side step of an attended session; a sleeping Mac reading as ineligible is already the
designed behaviour.

---

## 6. Item (5): the bounds the start prompt carries, and the hand-off

Carried verbatim in the policy half of the row, so a change to any of them is an `amend-prompt`
with history:

1. **Session cap.** Stop taking new work at the FIRST of: 12 cycles, ~400k context, or 5h wall.
   5h is deliberate: a claim older than 6h reads as stale, and the orchestrator's own claim has
   tripped the stale-claim auditor repeatedly (section 7, H3). Above the cap the session lands;
   it does not compact and continue.
2. **Authorisation window.** The session may grant or extend a window ONLY on the user's
   explicit instruction in that session, after a Step 0a reading, and must state the worst-case
   spend. It never extends a window on its own judgment.
3. **Usage bands.** Step 0a unchanged, run first and before any window grant.
4. **Idle rule.** Waiting on the user for more than ~50 minutes is a reason to LAND, not to
   wait: the next turn would pay a full rebuild anyway (section 1a), a fresh session is cheaper
   than the resumed one, and the needs-you badge is what calls the user back.
5. **Landing step.** Record `last_raised_at` for everything raised; confirm every launch has a
   `launches[]` row; write the resumable WORKSPACE_STATE entry; `amend-prompt` the row ONLY if a
   bound or the role text changed; then `/session-land`.

### The hand-off must not drop the claim or the leases

The 2026-09-17 damage was two acts fused into "close": `dispatcher_control.py stop` took the
boxes out of RUN and `task_claim.py close` dropped the claim that authorised renewal, leaving
`science-20260917-arc029-p1p3` (23h TTL, REFUSED-PAUSED at the time) owned by nobody. Under this
design they separate:

- **The fleet's authority is the window, not the session's claim.** Landing a bounded session
  closes that session's claim and nothing else. It issues `stop` only if the user asked to end
  the window. A lane entry left behind while the plane is paused is picked up by the box-side
  gate when the pause clears, inside the window -- the 2026-09-17 entry would have had an owner.
- **No window open** -> landing leaves the boxes STOP-by-expiry exactly as today; nothing is
  orphaned that a fresh session's start prompt does not list (open lane entries and their
  `expires_at` are in the state block, and count toward needs-you when close to expiry).
- So `/session-land` becomes correct for an Orchestrator session, and Step 6 splits into
  "6a end the window (only when the user says)" and "6b land this session (every session)".

---

## 7. Item (6): skill changes and the held-out check (GOV-HELDOUT-1)

### 7a. What changes in `.claude/skills/metaworker-orchestrate/SKILL.md` (mirrored to `.agents/skills/`)

- Header: the role is on-demand and bounded; started from `/workset` -> Session starts.
- New "Bounds" section (section 6 above), placed before Step 0a.
- Step 1: grant a short lease for an attended cycle, or a window on explicit instruction;
  remove "renew it on every cycle" for the window case.
- Step 1c: the manual ssh trigger stays for attended cycles; the 2026-08-27 paragraph is
  amended to record that it was revisited on 2026-09-20 with the evidence in section 1a, and
  what the user chose.
- Step 3c: replace "this session's own conversation history is the de-dup signal" with
  `last_raised_at`.
- Step 0a item 4 ("Do NOT `/session-land` yourself"): rewritten per section 6. Note that its
  "see the long-lived-loop rule above" is a **dangling reference today** -- the rule exists only
  in the user's memory note, not in the skill.
- Step 6: split into 6a/6b.
- **Memory:** `feedback_orchestrate_is_a_long_lived_loop.md` must be rewritten when this ships
  (its "never /session-land" instruction becomes wrong), and
  `feedback_leave_metaworker_orchestration_to_orchestrator.md` re-read against the window
  model. Until the build lands, both notes remain correct and must not be edited.
- Also touched: `metaworker-dispatch/SKILL.md:9-10` (stale resident-timer text),
  `account-handover` Step 2c, `docs/reference/` timer descriptions, `CLAUDE.md` only where it
  lists chip kinds.

### 7b. Held-out check

Old wording = long-lived loop, lease renewed per conversation turn, manual trigger, conversation
as state, never `/session-land`. New = sections 3-6. Cases the design was NOT written from
(the two runs in section 1 and the 2026-09-17 landing damage are excluded as motivating):

| # | Case | Old gives | New gives | Differ? Right call? |
|---|---|---|---|---|
| H1 | `orchestrate-20260915-0203` (WORKSPACE_STATE 2026-09-15T17:42:28Z): "wall time 01:45Z-17:41Z because each decision waited on the user; dispatchers STOP throughout, no lease" | one session held 16h; transcript shows a 4.1h and a 9.9h gap that day, rebuilds of 362k and 441k | idle rule lands the session; the badge calls the user back; a fresh ~150k session answers the next decision | **Differ. Right** -- same decisions made, ~800k of rebuild avoided. Tests the bound and the row, not the keepalive (no lease was involved). |
| H2 | `orchestrate-20260913-1643` (2026-09-14T21:49:58Z): "user-requested 8h dispatch window ... leased 10:30-18:30Z with a 30-min trigger loop ... dispatchers explicitly STOPPED at 21:48Z" | a Claude `/loop` turned ~16 times to hold an 8h window (longer than the 6h lease clamp, so renewal was mandatory); the boxes ran 3h18m past the window the user asked for until someone stopped them | one `window grant --hours 8`; the gate triggers at zero tokens; the window ends itself at 18:30Z | **Differ. Right** -- this is the authorisation window, already requested by the user in those words, built ad hoc out of the most expensive primitive available. The over-run is the clearest single point in favour. |
| H3 | The Orchestrator's own claim tripping the stale-claim auditor: `chip-staleclaim-orchestrate-20260911-0330-*`, `chip-staleclaim-orchestrate-20260915-0203`, `chip-staleclaim-orchestrate-20260918-gc` (classified `L_orchestrator_live`), plus `chip-20260829-metaworkerlearning-staleclaim-orchestrator-lease-recurrence` | a claim held past 6h by design; each trip mints a chip someone must read and withdraw | a 5h session cap means the claim never goes stale | **Differ. Right.** Also what fixes the bound at 5h rather than "whenever context is full". |
| H4 | 2026-08-27, both boxes idle ~4.5h with valid leases (Step 1c's own motivating case) | idle until the next manual trigger | the gate triggers -- but only if a user-approved lane entry exists, and in 2026-08 the lane did not exist (pre-2026-09-16 the candidate set was the whole chip ledger) | **Partial.** Differs only given the lane. It also shows why this was NOT safe to build on 2026-08-27: without lane-gating it would have been a bounded 2026-08-23. Not counted. |
| H5 | 2026-08-23 runaway | today's lease model already stops it | no window -> no trigger | **Degenerate** (old and new agree). Kept as the regression test the build must carry, not as evidence. |
| H6 | `orchestrate-20260918-1812`: single cycle, loop stopped, lease left to lapse at 20:15Z | lapses | lapses (no window) | **Degenerate.** |
| H7 | `orchestrate-20260916-1305` / `-2250`: hand-written mid-run resumable notes | works when the session remembers to write one | generated; nothing to remember | differs in mechanism, not in outcome on these two cases. Not counted. |

**Result: 3 non-degenerate cases (H1, H2, H3), each giving the right call; the check passes,
narrowly.** What the check caught: H4 forced property 2 (lane-gating) to be stated as a
precondition rather than an optimisation, and H3 set the session cap. What it did not find: any
historical case exercising K3 specifically (a box-side gate) -- H2 supports a window, not a
host. **The K3 choice rests on the section 2 measurements, not on held-out history**, and the
first unattended window should be short and watched.

Counterweight: this check cost two research subagents (~540k subagent tokens) plus the
transcript measurement. It was worth it here because the change reverses two standing rules;
it would not be for a smaller edit.

---

## 8. Build options (the decision chip asks the user to choose one)

| | Option | Builds | Rough size | Risk |
|---|---|---|---|---|
| A | **Full** | everything in sections 3-7, including the scripted lane launcher (4d) | 4-5 sessions; `integration/` not needed (umbrella `scripts/` + REE_assembly page + box-side unit; the only ree-v3 touch is the coordinator window dual-write, which can follow) | highest: reverses the 2026-08-27 decision and the never-land rule in one step |
| B | **Keepalive-script-first** | window record + K3 gate + scripted lane launcher (4d) + tests + timer-story reconciliation; Orchestrator stays long-lived meanwhile | 3 sessions | fixes the lapses and the ~117k-per-cycle dispatch floor, not the Orchestrator's context cost; ships the riskier half first and alone |
| **C** | **Start-row-first (recommended)** | `session_start` kind, generator, endpoint, panel, `last_raised_at`, `orchestrator_tick.py` + tests, the bounds and hand-off rewrite for ATTENDED cycles. No window, no box-side timer: leases stay session-held and lapse when a bounded session lands | 2-3 sessions | low: nothing unattended is added. Removes the measured context cost immediately. Leaves overnight continuity AND the dispatch-floor saving (4d) unsolved until the keepalive is approved separately, with real start-row experience behind that decision |
| D | **Hold** | nothing; keep this doc | 0 | the next long run repeats section 1a (~7.5M rebuild tokens per five days at current use) |

Under C the skill's "never `/session-land`" rule is relaxed only as far as: a bounded session
lands, and its leases lapse by expiry as they do today when a session ends (H6). Under A or B
the window model in section 6 applies in full.

## 9. Operational notes for whoever builds it

- The page change is in `REE_assembly/workset.html`: bump **`WORKSET_VERSION`** (line 2). Only
  bump `EXPLORER_VERSION` if `explorer.html` itself changes (it need not). **`serve.py` must be
  restarted** for the new endpoint. Neither has been done.
- `scripts/` changes: run `scripts/run_scripts_tests.sh` from the MAIN checkout before landing.
- Box-side unit files go through a scripted installer (the `install_worker_claude_settings.py`
  pattern), not hand-copies, and are NOT to be installed on the hub.
- Incidental, not part of this design: `systemctl cat ree-metaworker.service` on `ree-cloud-5`
  prints a coordinator bearer token from an `Environment=` line (ree-cloud-4 uses an
  `EnvironmentFile` instead). Worth moving into `/etc/ree/*.env`.
- A coordination-plane pause (`failure-autopsy-20260920-1022-pause`) was active while this was
  staged; the box-side probes above were read-only.
