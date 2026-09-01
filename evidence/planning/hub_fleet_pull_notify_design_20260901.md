**Status: DESIGN WRITTEN, IMPLEMENTATION NOT RECOMMENDED -- see Section 5.**

# Hub -> fleet pull-notify: design and recommendation

`chip-20260901-hub-fleet-pull-notify`. USER-DECIDED 2026-09-01 (RECOMMENDATION_LOG header
"Fleet sync") alongside `chip-20260901-fleet-autosync-repair` (separate chip, **done** --
see Section 1). This doc is the design the brief asked for; it also does the re-scoping the
brief explicitly invited if the sibling fix already closes most of the gap. It does.

---

## 1. What changed under this chip while it was being designed

The sibling chip landed and deployed (verified on origin, `ree-v3` `72b4226`, and on-box on
`ree-cloud-4`/`ree-cloud-5`) **before** this design was written:

1. `ree-metaworker-dispatch.sh`'s own autosync now uses `safe_adopt_ref.py` instead of
   `git pull --ff-only`. The old `--ff-only` refused **permanently** once a box held any local
   commit origin lacked -- "the normal residue of every `ree_commit.py` cherry-pick push retry",
   per the wrapper's own comment -- measured at 45% (`ree-cloud-5`) / 22% (`ree-cloud-4`)
   failure rates. That is fixed.
2. A new `ree-metaworker-autosync.timer` (10-minute cadence, `OnBootSec=2min`,
   `RandomizedDelaySec=60`) pulls the **umbrella `REE_Working`** checkout independent of dispatch
   cadence, lease state, or pause locks. This closes the specific incident that motivated both
   chips: `ree-cloud-4` sat 305 commits behind for 2+ days because the only thing that pulled
   `REE_Working` was a dispatch cycle, and the dispatch cycle itself was silently refusing to run
   because it was reading a stale copy of `TASK_CLAIMS.json` holding a pause lock origin had
   already cleared -- the staleness was preventing the only mechanism that would have corrected it.

So the two things this pull-notify chip was implicitly reacting to -- a checkout that could drift
unboundedly, and a broken pull that made drift permanent -- are already closed by a fix that
landed in the same push. What's left for this chip to evaluate is narrower: **given those two
fixes, is a hub-initiated notification still worth building**, and if so, in what form.

---

## 2. Measured facts (verified live on `ree-cloud-5`, this session, 2026-09-01)

### 2a. Hub -> worker SSH is not an established path, and building one has a real cost

- WireGuard is hub-and-spoke: this worker's `wg0` config has exactly **one** peer (the hub,
  `10.8.0.1/32`). Workers do not peer with each other over WG; only the hub is universally
  reachable.
- `ping 10.8.0.1` and `curl http://10.8.0.1:8787/` both succeed from this worker (401 without a
  bearer token, i.e. reachable and authenticating) -- the **worker -> hub** HTTP path used by
  the coordinator client is confirmed live.
- This worker's `sshd` listens on `0.0.0.0:22` (including the WG interface) with 2
  `authorized_keys` entries: one unlabelled (the operator/Mac key used by every documented
  `ssh ree@<worker-ip>` invocation in `metaworker-orchestrate`/`metaworker-repair` SKILL.md and
  `coordinator/deploy/*.sh`), and one labelled `ree@ree-cloud-4-metaworker` (cloud-4's
  orchestrator role reaching into cloud-5 -- a worker-to-worker key for the metaworker system,
  not a hub key).
- Grepping every SSH invocation in `coordinator/deploy/*.sh`, `*.md`, and the metaworker skills
  turns up **zero** hub-initiated SSH. Every one is operator-or-orchestrator -> worker, always by
  public IP, never by the hub over WG. `FLEET_CHECKLIST.md`'s own host table only ever lists
  "Public SSH" as a column for reaching a box, never a box reaching the hub or reaching each other.
- **Conclusion:** a hub -> worker SSH push channel does not exist today and would need: a new
  keypair generated on the hub, that public key added to `authorized_keys` on every current and
  future worker, and (per the brief's own constraint 1) careful thought about what it's allowed
  to run once installed. That is a new standing inbound attack surface on every worker, for a
  hub that currently has **no** inbound capability onto any of them. Constraint 2 in the brief
  already prefers avoiding exactly this; the measurement confirms there's no existing precedent
  to build on, so it would be built from scratch.

### 2b. The coordinator already has a channel that doesn't require any of that

Workers already `POST /heartbeat` and `POST /status` to the hub during any active experiment
(`coordinator_client.report_heartbeat` / `report_status`, `ree-v3/coordinator_client.py:154,180`).
The handler (`coordinator/app.py:1226`, `:1253`) currently acks with a bare `{"ok": True}`. Riding
a "here's the current known HEAD sha for the repos I write to" field on that existing ack costs no
new port, no new credential, and no new direction of trust -- the worker is still the one
initiating the connection, same as every other coordinator call. This is the mechanism the brief's
constraint 2 points at ("workers ASK for it on an existing call"), and it is concretely available:
`upsert_heartbeat` already runs inside the hub process that also runs the phase3 writers, which
know their own last-committed sha the moment they commit it.

### 2c. The residual staleness window, now that the sibling fix has landed, is already small relative to the thing that actually consumes it

| Population | What bounds its git staleness today | Bound |
|---|---|---|
| `REE_Working` (umbrella), any state (idle, paused, powered-on-idle) | `ree-metaworker-autosync.timer` (new, this chip's sibling) | ~10 min (+ up to 60s jitter) |
| `ree-v3` / `REE_assembly`, box actively running an experiment with `--auto-sync` | `experiment_runner.py`'s own `_background_sync` thread, `_sync_pull_tick` every 60s (`experiment_runner.py:4221`, wait interval literal `60`) | ~60s |
| `ree-v3` / `REE_assembly`, box NOT running an experiment | `ree-git-sync-repair.timer` (existing, unrelated to either chip) | 30 min (`OnBootSec=10min`, `OnUnitActiveSec=30min`) |
| `ree-v3` / `REE_assembly` / `REE_Working`, top of a dispatch cycle | dispatch wrapper's own pull (now `safe_adopt_ref`-based, per sibling chip) | at most 30 min (dispatch cadence) |

And the cadence of the thing that actually *acts* on a fresh checkout:

| Consumer | Cadence | Gated by git freshness, or independently paced? |
|---|---|---|
| `ree-metaworker.timer` (dispatch -- claims chips, starts work) | 30 min, **user-directed** (reduced from 5 min on 2026-08-24 specifically for cost) | Independently paced. A perfectly fresh checkout does not make dispatch run any sooner than the timer fires. |
| `ree-metaworker-healer.timer` | 1 hour | Same -- independently paced, and deliberately coarse ("every avoided tick is a ~117k-token context floor not paid"). |
| Active experiment's own substrate code | Should **not** move mid-run at all -- that's what the `integration/<slug>` staging-branch convention in `CLAUDE.md` exists to prevent. Fast git sync mid-experiment is not a goal. | N/A by design. |
| A live interactive orchestrator/operator session | Human-paced, and already reaches boxes directly over SSH (2a) when it needs something faster than any timer. | N/A -- doesn't wait on any of these timers at all. |

The pattern across every row: **nothing in the fleet currently waits on git latency as its
bottleneck.** The dispatcher is deliberately paced at 30 minutes regardless of how fresh the
checkout is; the healer at an hour; an active experiment already syncs at 60s and should not sync
substrate any faster than that; a human operator already has a faster path (direct SSH) than
anything git-based. A hub-push notification would shave the *idle-box* bound from ~10 min (already
small) toward near-zero, but that idle-box bound is not gating anything downstream of it today.

---

## 3. What "hub commits" actually means, concretely

The brief's frame -- "let the hub tell workers to pull when it commits" -- bundles several
distinct writers under one verb. Worth being precise, since a notify design would need to pick
which of these it covers:

- `phase3_git_writer` (`phase3:` results), `phase3_queue_writer` (`phase3-queue:`),
  `phase3_heartbeat_writer` (`phase3-heartbeats:`) -- `REE_assembly`/`ree-v3` coordination-data
  commits. **Already superseded as a latency concern**: results/queue/heartbeats are all
  DB-authoritative and read live via the coordinator API (`/shadow/status`, the queue snapshot in
  the DB) by anything that actually needs current data now -- the git materialisation exists for
  the git-history record and git-fallback readers, not as the primary read path. Per
  `CLAUDE.md`'s Coordinator section, this is explicit: "DO NOT read intra-run progress from
  `runner_heartbeats/*.json` ... on `origin/master` and assume it is current ... Use the live
  sources instead."
- `task_claim_chip_git_writer` -- renders `TASK_CLAIMS.json`/`TASK_CHIPS.json` from the DB, 2-min
  timer. Same shape: the DB is authoritative and `task_claim.py`/`chip_ledger.py` read/write it
  live over the coordinator API on a coordinator-mode box; the git file is the durable/fallback
  copy, not the hot path.
- `ree-assembly-git-writer` -- not otherwise detailed in this session; same coordination-data
  shape as the above by naming convention.
- Executable code changes (`ree_core/`, `coordinator/`, `scripts/`) landed by a human/agent
  session and pushed directly (not via a writer). **This is the one category where staleness has
  a real correctness cost** -- a worker running an old copy of, say, `ree_commit.py` after a bug
  fix lands could re-hit the bug for as long as it stays stale. This is exactly what Section 2c's
  bounds (10 min umbrella / 60s-or-30min work-repos) already cover, and it's the one category
  where the periodic-pull fix (sibling chip) is doing real work.

So the "hub commits" event that would matter for a notify design is narrower than the brief's
framing suggests: coordination-data writer commits are already latency-irrelevant (DB-primary),
leaving only human/agent-authored code and doc pushes -- which land at operator-driven, not
high-frequency, rate, and are already covered to within ~10 min / ~60s by the fixes above.

---

## 4. If it were built anyway: the low-cost design

Stated for completeness and as a starting point if a concrete pain point emerges later (see
Section 5's re-open condition), not as something built in this session.

**Mechanism:** piggyback on `/heartbeat` and `/status` acks (2b), never a new channel.

1. Hub-side: each phase3/materializer writer already knows the sha it just committed to origin
   for its own repo. Cache the three latest known origin HEAD shas (`REE_Working`,
   `ree-v3`/`main`, `REE_assembly`/`master`) in a small in-memory dict on the coordinator process,
   updated by each writer's post-commit hook (or read cheaply via `git rev-parse` against the
   hub's own checkouts -- sub-5ms, no DB migration needed for a first cut).
2. `app.py`'s `/heartbeat` and `/status` handlers add one small object to the existing 200
   response: `{"repo_heads": {"REE_Working": "<sha>", "ree-v3": "<sha>", "REE_assembly": "<sha>"}}`.
3. Worker-side: `coordinator_client.report_heartbeat`'s caller compares the returned shas against
   its own local `HEAD` for each repo. If behind AND at least `N` seconds have elapsed since its
   last opportunistic pull (a simple rate limit, e.g. 60s -- must not turn every heartbeat into a
   git operation), kick off `safe_adopt_ref.py` for that repo in the background, exactly the
   mechanism the sibling chip already standardised on (never `--ff-only`, never `--force`,
   `--allow-discard` never auto-passed).
4. **Never load-bearing, per constraint 3**: this only ever *shortens* the wait before the
   existing periodic pull (autosync timer / git-sync-repair timer / background sync thread) would
   have run anyway. A box that never heartbeats (no active experiment, e.g. idle dispatcher-only)
   gets zero benefit from this and falls through entirely to the periodic timers -- which is
   correct per constraint 4 (a notify that assumes a live listener silently no-ops for a
   powered-off or non-heartbeating box; the timers are what actually cover that case,
   unconditionally).

**What this explicitly does NOT protect**, stated per the brief's own requirement:
- Boxes that are powered off, or powered on but not currently heartbeating (idle
  dispatcher/healer-only boxes -- the majority of fleet-time) get no benefit; they still rely
  entirely on the periodic timers, at their existing bounds.
- It does not shorten the dispatch (30 min) or healer (1 h) cadence -- those are paced
  independently of git freshness (Section 2c) and this design does not touch them.
- It does not add any new inbound trust to a worker (2b is worker-initiated, same as today); it
  does add a small amount of hub-side state (the cached shas) and a small amount of worker-side
  logic (the rate-limited opportunistic pull) that would need its own tests, in the same spirit as
  the sibling chip's `safe_adopt_ref`-based fix.
- A dropped or delayed heartbeat costs nothing beyond falling back to the periodic bound --
  by construction, since the notify is read-only piggyback data on a call the worker was already
  making for an unrelated reason.

**Estimated cost to build:** small (one coordinator response field, one client-side compare +
rate-limited call, tests for both) but not zero, and it touches `app.py`'s hot request path and
`coordinator_client.py`'s shared caller -- both used by every worker on every heartbeat, so a bug
here has fleet-wide blast radius the way any coordinator-hot-path change does.

---

## 5. Recommendation: do not build this now

The brief invited exactly this outcome ("if the worker-side fixes already hold the fleet current,
this one's value drops and its scope should be re-argued rather than built by default"). That's
where the evidence points:

- The concrete incident behind both chips (a checkout that could drift unboundedly, made
  unrecoverable by `--ff-only`) is fully closed by the sibling chip, which is already deployed and
  verified on both metaworker boxes.
- Every remaining staleness bound (Section 2c) is already smaller than the cadence of whatever
  would consume a fresher checkout -- the dispatcher and healer are paced independently of git
  freshness by deliberate user decision (cost, not correctness), and an active experiment already
  syncs substrate every 60 seconds by a completely separate, pre-existing mechanism.
- The one channel that would let a hub-push design avoid new attack surface (2b, the heartbeat
  ack) only reaches boxes that are already heartbeating -- i.e., already running experiments,
  which are already the best-covered population (60s bound). It provides the least value exactly
  where it's cheapest to build, and no value at all for the population (idle dispatcher-only
  boxes) where the original incident actually happened -- that population is covered by the
  sibling chip's timer instead, not by anything this chip could add.
- Building the alternative that *would* reach idle/dispatcher-only boxes (a real hub -> worker
  push) means standing up SSH access the fleet does not have today, which the brief's own
  constraint 2 already disfavours, for a latency win (removing the ~10-minute bound) that nothing
  downstream is currently gated on.

**Re-open condition, stated concretely so this isn't a permanent no:** if a specific consumer is
later found to need sub-10-minute propagation of a hub commit to an idle/non-heartbeating worker
-- e.g., a safety-critical script fix that must not wait even one autosync cycle, or a dispatch
cadence that gets re-tightened below 10 minutes and starts actually racing the autosync timer --
revisit Section 4's design with that consumer named explicitly. Until then, the periodic bounds
already in place (10 min umbrella / 60s active-experiment / 30 min idle work-repos) are the
answer, and they exist because of the sibling chip, not this one.

---

## 6. Scope note on the sibling-chip overlap

`task_claim.py open` for this session flagged a scope overlap with the (by-then-closed)
`metaworker-chip-20260901-fleet-autosync-repair` claim on
`ree-v3/coordinator/deploy/ree-metaworker-dispatch.sh` -- expected, not arbitrated (a directory
resource, and the rival claim was already closed by the time this note printed). No files from
that chip's scope were touched here; this design only reads them for the measurements in Section 1
and 2c.

No code was deployed to the hub or to any worker by this session. Nothing in Section 4's design
was implemented -- it is documented as a starting point only, per the recommendation in Section 5.
