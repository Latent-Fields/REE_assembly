---
closure_plan:
  id: task_claim_chip_coordinator_migration
  generation: process
  title: "TASK_CLAIMS/TASK_CHIPS Coordinator Migration (single-writer cutover)"
  registered: 2026-08-26
  last_updated: 2026-08-27
  owner: machinery
  summary: >
    Move TASK_CLAIMS.json/TASK_CHIPS.json claim+chip coordination off
    per-machine git commits onto the Phase 3 coordinator (ree-cloud-1),
    mirroring the shadow-first cutover already used for
    experiment_queue.json/results/heartbeats. GitHub becomes the
    materialization/fallback path, not the live check every session reads.
    generation: process -> infra/tooling lane; owns no scientific claims,
    segmented out of the V3 closure %.
  scope_claims: []
  sibling_plans: []
  nodes:
    - id: PHASE-0
      title: "Prerequisites + design finalization (WireGuard coverage audit, schema/endpoint spec, degrade-path spec)"
      status: done
      severity: load-bearing
      last_updated: 2026-08-26
      note: >
        CLOSED 2026-08-26 (session
        metaworker-chip-20260826-taskclaim-coordinator-migration-phase0), all
        three prerequisites verified live, no blockers. 6.1 WireGuard:
        ree-cloud-5 was ALREADY a peer (10.8.0.15/32, persisted in wg0.conf,
        bidirectional with PersistentKeepalive) -- the prior assumption that it
        was very likely NOT a peer was WRONG; verified end-to-end with ping
        (0% loss) and a coordinator /health 200 from cloud-5 over the mesh. No
        mesh change was made. 6.2 Mac tunnel: both launchd agents loaded and
        healthy, latest digest reads bounces_24h=0 / keepalive=HOLDING, so the
        literal precondition is met -- BUT the full 75-digest record is 33%
        FLAPPING (8 flapping days in the last 30, most recent 2026-08-22, and 5
        occasions where recovers < bounces), so the point-check as written is a
        weak predicate and section 6.2 now recommends restating it as a trailing
        rate criterion before PHASE-2. This does NOT gate PHASE-1, which is
        read-only and does not depend on the Mac's tunnel. 6.3 schema/endpoint:
        section 5.2 rewritten from a sketch into implementation-ready DDL +
        endpoint signatures against a full read of schema.sql/db.py/app.py, with
        all field and uniqueness assumptions checked against the live JSON files;
        11 design problems recorded in 5.2.6, of which D1 (path-namespace
        collision with the existing experiment /claim endpoints), D2 (resources
        MUST be an indexed child table or the migration buys no correctness at
        all), D3 (dedupe has no atomic equivalent and needs none under a
        composite PK) and D7 (chip archive stays git-side -- its gate is an
        origin fact) change the design as sketched.
    - id: PHASE-1
      title: "Shadow: coordinator mirrors TASK_CLAIMS/TASK_CHIPS state read-only; git stays authoritative"
      status: soaking
      severity: high
      last_updated: 2026-08-27
      note: >
        COORDINATOR RESTARTED 2026-08-27T07:52:01Z (session
        metaworker-chip-20260827-coordinator-phase1-restart-soak-start, chip
        chip-20260827-coordinator-phase1-restart-soak-start). SSH to the hub
        (ree-cloud-1, ree@91.98.130.117) confirmed the pre-restart state
        exactly as the prior node text described: `ree-coordinator.service`
        had been running since 2026-08-26T04:47:44Z (~27h), while
        `app.py` on disk carried the PHASE-1 routes since 2026-08-26T19:00Z
        -- so `/task_claim/list` and `/chip/list` 404'd with a verified-valid
        bearer token (confirmed via `/shadow/status` -> 200 with the same
        token) while `/health` still answered normally. Before restarting,
        confirmed the shadow-sync timer was healthy (11h of ticks since
        enable, most recent tick 5 min prior, diverged=0 on every visible
        tick) and that phase3 writer commits were still landing normally on
        `origin/master` -- i.e. the restart was not being used to paper over
        an already-broken soak.

        `sudo systemctl restart ree-coordinator.service` executed cleanly
        (ActiveEnterTimestamp confirms 2026-08-27T07:52:01Z). Post-restart
        verification, all live: `/health` -> `{"ok": true, "mode":
        "coordinator"}`; `/task_claim/list` -> 200 with real claim data;
        `/chip/list` -> 200; `/task_claim/drift` -> 200 with the FULL
        backfilled history the shadow-sync timer had been accumulating all
        along (`total_ticks: 70, diverged_ticks: 0` at restart time, i.e.
        zero drift across the entire ~11.4h the timer had been running
        pre-restart -- nothing was lost by waiting, exactly as the prior
        node predicted). `journalctl -u ree-coordinator.service` post-restart
        shows normal `POST /heartbeat` (200) traffic resuming from cloud-2/
        cloud-4/the hub itself within seconds, plus a `POST /claim` and a
        `GET /commands` both 200. `/writer-health` confirms all three phase3
        writers (git_writer, queue_writer, heartbeat_writer) show
        `last_error: null` and a `last_tick_at` seconds-old at check time,
        `spool_pending: 0` -- the restart caused no observable disruption to
        the writer plane it shares the box with.

        **THE SOAK CLOCK NOW EFFECTIVELY STARTS RETROACTIVELY FROM THE TIMER
        ENABLE, NOT FROM THIS RESTART**: because the shadow-sync timer and
        drift-log table were already running and recording ticks the whole
        time (per the PHASE-1 node's prior text), the moment the routes
        became reachable they immediately reported the full pre-restart
        history rather than starting from zero. `GET /task_claim/drift`
        (`total_ticks`/`diverged_ticks`) is now the live, API-reachable exit
        -criterion measurement -- no more `journalctl` workaround needed.
        Exit criterion (still N days of `diverged_ticks` staying at 0,
        unchanged from the original design) is NOT yet met: only ~11.4h of
        history exists as of this restart, well short of any reasonable N.
        This session's task ends here, per its own brief -- it does not
        redefine N, does not start PHASE-2, and does not add any write path.
        The only remaining PHASE-1 work is elapsed time: continue polling
        `GET /task_claim/drift` (or `journalctl -u
        ree-task-claim-chip-shadow-sync`) periodically until N days of
        zero-drift history accumulates, then bring that evidence to a human
        for the PHASE-2 go/no-go decision (which additionally needs the
        section 6.2 Mac-tunnel rate-criterion question resolved -- still
        open, unchanged by this session).

        Prior (unchanged, retained for history):
        SOAK STARTED 2026-08-26T20:26:52Z (session
        metaworker-chip-20260826-coordinator-migration-phase1-deploy, chip
        chip-20260826-coordinator-migration-phase1-deploy). Deployed to the
        coordinator hub (ree-cloud-1 / ree-worker-1, 91.98.130.117): cloned a
        read-only umbrella checkout to
        /home/ree/REE_Working_shadow_mirror_readonly (--no-checkout +
        `checkout master`, origin https://github.com/Latent-Fields/REE_Working.git),
        installed deploy/ree-task-claim-chip-shadow-sync.{service,timer}
        verbatim (matched byte-for-byte against origin/main via `diff`
        before install -- no edits needed, TASK_CLAIM_CHIP_REPO_PATH already
        pointed at the exact path used) to /etc/systemd/system/, and
        `systemctl enable --now` the timer. `systemctl list-timers` confirms
        the 10-minute OnUnitActiveSec cadence is armed (next tick
        2026-08-26T20:36:52Z at enable time).

        ZERO-DRIFT VERIFIED via two manual `systemctl start` ticks before
        enabling the timer (byte-identical invocation to what the timer
        itself runs) -- first tick populated the mirror from empty
        (claims: git=142 db=141 new=141, chips: git=1707 db=1706 new=1706,
        diverged=0), second tick back-to-back showed new=0 updated=0
        orphan=0 diverged=0 on both tables, i.e. genuine convergence, not
        just an empty-DB false positive. The git=142/db=141 (and
        git=1707/db=1706) gap is NOT drift -- `task_claim_chip_shadow_sync`
        reports diverged=0 for both -- and is explained by section
        5.2.2/D3's composite-PK dedup: TASK_CLAIMS.json currently carries
        one confirmed exact-duplicate (session_id, claimed_at) pair (see
        this session's own `task_claim.py open` output, which surfaced it
        independently and unprompted), and TASK_CHIPS.json likely carries
        an analogous chip_ref collapse (chip_ledger.py's own `dedupe`/HEAL
        logic hit several `chip-queuefloor-since-initial`-style duplicates
        during this same session, unrelated file but same failure class).
        Neither file was edited to remove the duplicate -- out of scope for
        this chip -- so the count gap will persist until a future dedupe
        pass, without affecting diverged=0.

        `GET /task_claim/drift` is NOT YET REACHABLE: on-disk `app.py`
        (mtime 2026-08-26T19:00:27Z, from the ree-v3 f385e8bb24 pull already
        present on the hub) has the new /task_claim/* and /chip/* routes,
        but the live `ree-coordinator.service` process has been running
        since 2026-08-26T04:47:44Z -- 14h before that code landed on disk --
        so it is still serving the pre-PHASE-1 route table and 404s on
        those paths. Per this node's own prior text and the plan's HARD
        STOP framing ("reloading ree-coordinator.service... left for a
        human to do with eyes on it, not something this session
        self-authorized mid-run"), this session deliberately did NOT
        restart the live production coordinator -- it is a shared,
        always-on service the whole experiment fleet depends on for
        claim/heartbeat traffic, and the plan doc pre-decided that decision
        belongs to a human. Soak verification therefore continues via
        `journalctl -u ree-task-claim-chip-shadow-sync -f` on the hub until
        a human restarts the coordinator (a fast, low-risk restart --
        Type=simple + Restart=always, same pattern as every other phase3
        writer -- but still a live-infra action this session was not
        chartered to take unilaterally); the drift-log table
        (task_claim_chip_drift_log) is already being written every tick
        regardless, so `GET /task_claim/drift` will have full backfilled
        history the moment the coordinator picks up the new routes.

        PHASE-2 explicitly NOT started, per the chip's own hard-stop
        instruction and this node's pre-existing text -- no claim-authority
        cutover, no write path added, task_claim.py/chip_ledger.py
        untouched.

        Prior (unchanged, retained for history):
        BUILT 2026-08-26 (session
        metaworker-chip-20260826-taskclaim-coordinator-migration-phase1,
        ree-v3 f385e8bb24, pushed to origin/main). Added task_claims/
        task_claim_resources/chip_ledger/task_claim_chip_drift_log tables
        (schema.sql + an additive db.py migration guarded by the existing
        PRAGMA table_info convention) and task_claim_chip_shadow_sync.py, a
        read-only reconciler modeled directly on sync_daemon.py's own PHASE-1
        design: it only ever runs `git fetch` / `git rev-parse` / `git show`
        against the REE_Working umbrella repo (a DIFFERENT repo from this
        one) -- no autostash, no rebase, no commit, no push, and no code path
        anywhere in it can mutate that repo's working tree or advance its
        branch. Verified live against the real 144-claim/1697-chip files in
        3.7s with zero drift, and a dedicated test
        (test_reconcile_never_dirties_the_source_working_tree) pins the
        structural-incapability property rather than just asserting it in
        prose. Added three READ-ONLY observability endpoints (GET
        /task_claim/list, /task_claim/check, /chip/list, /task_claim/drift)
        -- no mutating /task_claim/* or /chip/* endpoint exists, and a test
        (test_no_mutating_task_claim_or_chip_post_route_exists) pins that
        every such POST still 404s. task_claim.py/chip_ledger.py are
        UNCHANGED -- nothing anywhere reads from or writes to this mirror
        yet. 646 coordinator/ tests pass (was 645 + a real bug this work
        surfaced: db.connect() never set PRAGMA foreign_keys=ON, so the new
        ON DELETE CASCADE silently did not enforce outside init_db()'s
        one-off executescript connection -- fixed, and every pre-existing
        table has no FK so nothing else changed behaviourally).

        NOT YET LIVE-INSTALLED ANYWHERE, deliberately: the coordinator hub
        (ree-cloud-1) has no git clone of the REE_Working umbrella repo today
        (confirmed live via SSH) -- only ree-v3/REE_assembly/etc, a different
        repo. Provisioning a new read-only clone on shared production infra
        and reloading ree-coordinator.service to pick up the schema
        migration are left for a human to do with eyes on it, not something
        this session self-authorized mid-run. The systemd timer/service
        template (deploy/ree-task-claim-chip-shadow-sync.{service,timer},
        10-minute cadence) is committed and documents exactly what a human
        runs to start the soak, including the clone-provisioning step.

        HOW TO CHECK SOAK STATUS, once installed: `journalctl -u
        ree-task-claim-chip-shadow-sync -f` on the hub, or `GET
        /task_claim/drift` on the coordinator (same bearer-token auth as
        every other endpoint) for total_ticks/diverged_ticks/recent rows
        without SSH. The exit criterion (frontmatter summary, unchanged): N
        days of diverged_ticks staying at 0.

        Exit criterion (unchanged): N days of the coordinator's mirrored
        claim/chip state matching git HEAD with zero drift, once the timer
        is actually running. status is `built-not-soaking`, not `done` --
        the soak has not started because the timer has not been installed.
        PHASE-2 (claim-authority cutover) is explicitly NOT started and NOT
        chipped by this session -- see the plan's HARD STOP note; that
        remains a human-initiated follow-up once the soak window has
        actually elapsed cleanly.
    - id: PHASE-2
      title: "Claim-authority cutover: task_claim.py/chip_ledger.py call the coordinator; git becomes state-change materialization"
      status: in-progress
      severity: high
      last_updated: 2026-08-27
      note: >
        Mirrors ree-v3's SYNC_MODE=coordinator (claim cutover): the DB becomes
        the claim/chip authority; git remains the transport/audit trail, one
        writer thread committing on state-change only (mirrors
        phase3_heartbeat_writer's commit-on-state-change discipline, NOT the
        retired 30-min liveness tick -- see root CLAUDE.md's explicit warning
        against reintroducing that). The existing git-mutate-and-commit path
        in task_claim.py/chip_ledger.py becomes the FALLBACK mode for when the
        coordinator/mesh is unreachable, not the default.

        PHASE-2a BUILT AND LANDED 2026-08-27 (session
        coordinator-migration-phase2-build, chip
        chip-20260827-coordinator-migration-phase2-build). The flag is
        DEFAULT OFF and nothing in the fleet reaches any of it.

        WHAT LANDED -- ree-v3 528ce44fc5 + a follow-up (server, on
        origin/main) and REE_Working ed1bcf7869 (client, on origin/master):
        * ree-v3/coordinator/db.py: 11 mutating verbs, each taking BEGIN
          IMMEDIATE BEFORE its guard SELECT (the same primitive try_claim
          already uses for experiment claims). Claims: try_open_task_claim /
          close_task_claim / renew_task_claim / amend_task_claim /
          dedupe_task_claim (accepted no-op per D3). Chips: record_chip /
          try_claim_chip / unclaim_chip / resolve_chip / attach_chip /
          amend_chip_prompt.
        * ree-v3/coordinator/app.py: the 11 matching POST endpoints under
          /task_claim/* and /chip/* (D1), as a dispatch table rather than 11
          more arms in do_POST. 409 = a legitimate VERDICT a client branches
          on; 400 malformed; 404 unknown key.
        * scripts/coordinator_transport.py (NEW): the client transport. Hard
          no-op unless TASK_CLAIM_COORDINATION_MODE=coordinator AND a URL and
          token are configured. Every failure returns None = "carry on with
          git".
        * scripts/task_claim.py: coordinator branch on `open` (arbitration,
          can stop the session on CONTENTION_EXIT) and `close` (mirror only,
          never stops).
        * scripts/chip_ledger.py: coordinator branch on `claim` (the mutex --
          the only chip verb allowed to stop the session), plus `record`,
          `resolve` and `unclaim` as mirrors.

        THE SCOPE OF "COORDINATOR-FIRST" IN THIS PHASE, stated plainly
        because it is the thing a later session is most likely to
        misremember: with the flag ON, the client asks the coordinator AND
        STILL WRITES GIT. It does not stop writing git. The DB->git
        materializer (the analogue of sync_daemon's phase3_*_writer family)
        DOES NOT EXIST for these two files, so a claim living only in the DB
        would be invisible to audit_stale_claims.py,
        prune_task_claims_done.py, serve.py's /workset panel,
        audit_orphan_chips.py, every chip_ledger.py list, and every session
        on every other machine. What moves to the coordinator here is the
        ARBITRATION AUTHORITY -- the verdict, not the storage. This mirrors
        ree-v3's own Phase 2 exactly ("git remains the queue worklist/
        transport; the DB becomes the claim authority"). Suppressing the
        client git write is PHASE-2b and needs the materializer first.

        The local file-based arbitration is NOT removed, weakened, or
        skipped. It still runs FIRST, unchanged, and still refuses on its
        own terms; the coordinator adds a second, stricter opinion. Two
        consequences worth stating: a check that can only ADD refusals
        cannot regress today's behaviour, and running the local check first
        means a local refusal never leaves an orphan claim row in the DB
        that git never learns about.

        ONE REAL BUG FOUND IN THIS SESSION'S OWN CODE, worth recording
        because it defeats the promise 5.2.1 makes: the entry_json rebuild
        emitted only the MODELLED columns, so any field the schema does not
        model was silently dropped by a coordinator mutation. `handoff_pending`
        is the live case -- no column, set by chip_ledger.py's `resolve
        --handoff-pending` / `declare-handoff`, and present on **198 of 1920
        chips** in the real TASK_CHIPS.json (measured 2026-08-27). A chip
        claimed or resolved through the coordinator would have lost it with no
        error anywhere. Fixed by `_carry_unmodelled()`, which fills only keys
        the rebuild does not produce, so the columns still win. Ordering is
        load-bearing and the first attempt got it wrong: it must run BEFORE the
        archived-field pop, or it resurrects a stripped `prompt` out of a stale
        blob -- the archive-undo D5 forbids. Caught by
        test_archived_fields_are_absent_not_null_in_entry_json, which is the
        argument for having written that test.

        TESTED -- 110 new tests, all green, no regressions:
        * ree-v3/coordinator/test_task_claim_chip_mutations.py (57): the db
          layer. Two headline concurrency tests on REAL threads and REAL
          sqlite -- 3 sessions racing one claim resource produce exactly 1
          owner and 2 told (the 2026-07-28 shape), 4 sessions racing one chip
          claim produce exactly 1 winner (the 2026-08-09 shape). Plus
          negative controls that no verb touches git and that no archive verb
          exists (D7).
        * ree-v3/coordinator/test_task_claim_chip_mutation_endpoints.py (4):
          HTTP wiring end to end. Its own server and DB, because sharing
          PHASE-1's fixture polluted that file's list assertions.
        * test_task_claim_chip_endpoints.py: PHASE-1's
          "no mutating route exists" pin is INVERTED, not deleted -- it said
          such a change had to be deliberate and reviewed, and this is that
          change. It now pins the routes exist, that an empty body is a 400
          rather than a 404, and that /chip/archive still 404s.
        * scripts/test_coordinator_transport.py (22): default-off, and the
          fallback exercised against REAL sockets -- closed port, unresolvable
          host, a server that accepts and never answers (the WireGuard
          blackhole shape, which is NOT the same as connection refused), a
          500, a non-JSON error body, and a 200 with an unparseable body.
        * scripts/test_task_claim_coordinator_branch.py (15) and
          scripts/test_chip_ledger_coordinator_branch.py (14): the flag-off
          assertions run against a LIVE, ANSWERING coordinator whose request
          log must stay empty -- so "no call was made" is a measurement, not
          an inference. The headline flag-on tests are the ones where the
          LOCAL file shows no rival at all and the coordinator refuses anyway,
          which is the whole correctness argument in one assertion.
        * Full ree-v3 coordinator suite after the change: 707 passed + 172
          subtests, zero regressions.
        * Full existing umbrella suites with the flag OFF -- all 43
          test_task_claim_*.py + test_chip_ledger_*.py files: 43/43 green.
          The parallel run (jobs=7) initially reported
          test_task_claim_amend_renew_orphan_guard.py red and
          test_task_claim_mutation_lock.py timed out at the 600s per-file
          limit; both pass solo (461s and 137s respectively) on the same dirty
          tree. Both do real git pushes to file remotes and are slow enough
          that 7-way parallelism plus concurrent test runs pushed them over.
          Neither touches a code path this work changed.

        STILL OPEN, and the ACTUAL CUTOVER still waits on all of it:
        (a) soak evidence (N days of GET /task_claim/drift showing
        diverged_ticks=0); (b) a separate human go-live confirmation;
        (c) PHASE-2b, the DB->git materializer, before the client git write
        can be suppressed; (d) deployment -- the endpoints are on origin/main
        but ree-coordinator.service on the hub has not been restarted to pick
        them up, so /task_claim/open et al still 404 in production, exactly
        as PHASE-1's routes did before its own restart. Nothing depends on
        them, so this is not urgent, but a future session should not read
        "landed" as "reachable".

        Prior (unchanged, retained for history):
        BUILD STARTED 2026-08-27 (user go-ahead, decoupled from the soak):
        the soak (PHASE-1's remaining exit criterion) only validates the
        shadow mirror before anything DEPENDS on it -- it says nothing about
        whether the cutover code is ready. So implementation work starts now,
        in parallel with the soak's remaining ~1 day, gated behind a
        default-OFF flag so today's git-only behavior is completely
        unchanged until an explicit separate go-live decision flips it. The
        ACTUAL CUTOVER (flipping the default so task_claim.py/chip_ledger.py
        call the coordinator first) still waits on: (a) soak evidence (N
        days of GET /task_claim/drift showing diverged_ticks=0), and (b) a
        separate go-live confirmation. Building/testing does not.
    - id: PHASE-3
      title: "Harden: monitoring, CLAUDE.md rewrite to reflect the new default, decommission what is safe to decommission"
      status: not-started
      severity: medium
      last_updated: 2026-08-26
      note: >
        Only after PHASE-2 has run in production long enough to trust it.
        Update root CLAUDE.md's Concurrency Rules section to describe the new
        default transport (many of today's documented hazards -- pathspec
        races, ref-move skew, rebase-lock contention, read-modify-write
        contamination -- stop applying to TASK_CLAIMS.json/TASK_CHIPS.json
        specifically once there is only ever one git-writer for them; they
        keep applying to claims.yaml/WORKSPACE_STATE.md/experiment_queue.json
        as before). Do not remove the git-fallback code path -- it stays
        permanent, mirroring the runner's own retained legacy git-claim
        fallback under Phase 3 experiment coordination.
---
# TASK_CLAIMS / TASK_CHIPS Coordinator Migration Plan

**Status:** SOAKING + PHASE-2a BUILT (v0.6, 2026-08-27). **PHASE-2a (the coordinator-first transport, DEFAULT OFF) is built, tested and landed** -- 11 mutating endpoints on `ree-v3` `528ce44fc5`, a new `scripts/coordinator_transport.py`, flag-gated branches in `task_claim.py`/`chip_ledger.py`, 110 new tests green, the full 707-test coordinator suite unregressed and all 43 existing `task_claim`/`chip_ledger` umbrella test files green with the flag off. Server on `ree-v3` `origin/main`, client on `REE_Working` `origin/master` (`ed1bcf7869`). Nothing in the fleet reaches any of it: `TASK_CLAIM_COORDINATION_MODE` defaults to `git` and the endpoints are not yet deployed to the running hub. See the PHASE-2 frontmatter node and section 10. **PHASE-0 is CLOSED** (all three prerequisites verified live -- see section 6). **PHASE-1 is DEPLOYED and SOAKING, and `ree-coordinator.service` has now been RESTARTED (2026-08-27T07:52:01Z) so `/task_claim/*` and `/chip/*` are LIVE**: the shadow-mirror schema, reconciler and read-only endpoints (landed on `ree-v3` `main` `f385e8bb24`) are installed on the coordinator hub, the shadow-sync timer has been running at its documented 10-minute cadence since 2026-08-26T20:26:52Z, and the restart (session `metaworker-chip-20260827-coordinator-phase1-restart-soak-start`) confirmed zero disruption to the phase3 writer plane and exposed the FULL pre-restart drift history via `GET /task_claim/drift` (`total_ticks: 70, diverged_ticks: 0` at restart time -- nothing was lost by deferring the restart). Soak evidence is now readable live via the API; no more `journalctl` workaround needed (see the PHASE-1 frontmatter node for full detail). No WireGuard mesh change has been made (none was needed, see section 6.1). This doc is the resume primitive across sessions -- read it before touching anything named in the phase table above.

**Closes:** the same "no single enforcement chokepoint" class of gap the Phase 3 coordinator closed for `experiment_queue.json`/results/heartbeats (see `ree-v3/coordinator/PHASE3_CUTOVER.md`), applied to `TASK_CLAIMS.json` + `TASK_CHIPS.json` -- the two coordination files still edited by direct, independent, per-machine git commits, and therefore still exposed to the whole "Concurrency Rules" incident catalogue in root `CLAUDE.md` (pathspec races, HEAD/worktree skew, ref-move discard, rebase-lock contention, read-modify-write contamination, chip-ledger merge-origin-into-local dances).

**Owns:** designing and staging a coordinator-backed claim/chip service that `task_claim.py`/`chip_ledger.py` talk to over the network (via the existing WireGuard mesh) instead of mutating a local git clone directly, with git/GitHub demoted to a state-change materialization + fallback transport.

**Does NOT own:** `claims.yaml`, `WORKSPACE_STATE.md`, `experiment_queue.json` (already coordinator-authoritative for claims), or any work-repo (`ree-v3`/`REE_assembly`) code-plane contention. See section 4 (Scope) for why each is excluded.

**This is a multi-session effort, likely spanning weeks given the phased, shadow-first discipline this doc deliberately imposes** (see section 3 and `feedback_infra_shadow_first` memory: reversible, minimal-deps, one step at a time). The phase table in the frontmatter above is the cross-session resume primitive -- update `status`/`last_updated`/`note` on the relevant node every session that touches this, the same convention `pack_writer_single_writer_migration_plan.md` and `sleep_substrate_plan.md` use.

---

## 1. The problem

`TASK_CLAIMS.json` and `TASK_CHIPS.json` are shared, git-tracked, whole-file JSON registries mutated by every Claude session that opens/closes a task claim or records/resolves a chip -- via `task_claim.py`/`chip_ledger.py`, which each do a local read-modify-write, commit, and push against the shared GitHub remote. Every machine that runs a Claude session against this codebase is an independent git client racing every other one on the same file.

Root `CLAUDE.md`'s "Concurrency Rules" section is, by page count, dominated by defenses built for exactly this failure class: the pathspec-commit race (A-01/A-02), HEAD/worktree skew after a ref move (A-07 through A-11), a bare ref-move silently discarding local commits (A-17 through A-22), read-modify-write contamination (A-04, A-05), the chip ledger's merge-origin-into-local dance, `safe_adopt_ref.py`, `ref_convergence.py`, the mkdir-based rebase lock (A-62), and more. All of that machinery makes concurrent git writes to these two files *safe*. None of it makes them *uncontended* -- sessions still queue behind each other's pushes, still hit "REVERTED: N committed foreign claim entries would be REGRESSED" self-verify refusals under load, and still burn multiple fetch-rebase-retry cycles to land one claim.

**This is not a hypothetical.** While drafting this very document (2026-08-26, session `dazzling-jackson-efb9e9`), `task_claim.py open` on a brand-new, non-conflicting resource path failed 3 consecutive attempts with exactly that self-verify refusal, because a concurrent `/metaworker-orchestrate` session on the same machine (`DLAPTOP`) was mid-flight closing several unrelated claims/chips in the shared main checkout at the same time. No repair was needed -- it was live, legitimate, in-progress work, not skew -- but diagnosing "is this real contention or a stale-skew bug" cost real time and very nearly led to an incorrect manual "repair" of someone else's in-flight commit. That diagnostic cost is the recurring tax this migration is meant to remove.

## 2. Prior art: the Phase 3 coordinator already solved this once

`ree-v3/coordinator/` (live since 2026-05-29, per root `CLAUDE.md` "Coordinator (Phase 3)") is the *same* problem, already solved, for a *different* set of files: `experiment_queue.json`, result manifests, `runner_heartbeats/*.json` + `runner_status/*.json`. The hub (`ree-cloud-1`, always-on -- the cloud-scaler's `HUB_NAME` skip means it is never powered off) runs a coordinator service (`app.py` + `db.py`, SQLite-backed) reachable over the WireGuard mesh at `10.8.0.1:8787`. Producers (experiment runners on every worker) `POST` to the coordinator's HTTP API; they never `git commit` these paths themselves. A single writer thread (`sync_daemon.py`'s `phase3_*_writer` family) is the only process that ever materializes DB state to git, committing on state-change only (the 30-minute forced liveness tick was deliberately retired -- root `CLAUDE.md` explicitly forbids reintroducing it, see the "Coordinator (Phase 3)" section, "Operator gotchas").

The rollout that got there was itself staged and multi-session, exactly the discipline this doc borrows:

- **Phase 1 (shadow):** `sync_daemon.py` reconciles a DB mirror against git-authoritative state, read-only, no write path -- "structurally incapable of the failure class the whole project exists to remove" (the module's own docstring).
- **Phase 2 (coordinator/claim cutover, `SYNC_MODE=coordinator`):** git remains the queue worklist/transport; the DB becomes the **claim authority** (workers `POST /claim`; `try_claim`'s `BEGIN IMMEDIATE` closes the read-then-write race a git-based mutex cannot).
- **Phase 3 (authoritative):** the coordinator becomes the sole git writer for these paths, guarded behind `SYNC_MODE=authoritative` + `--i-understand-phase3` until proven out.

Root `CLAUDE.md`'s "Multi-Machine Experiment Coordination" section explicitly documents that the legacy git-based claim mutex is *still present in the runner code as a fallback* even after the coordinator became authoritative -- git did not disappear, it was demoted. That demotion -- **coordinator is the live check; git is the fallback, not the general check** -- is precisely the shape requested for this migration.

## 3. Decision (2026-08-26, proposed -- not yet user-ratified as a build): reuse the same coordinator, same phased discipline

**Do not stand up a second service.** Add `task_claims` and `chip_ledger` tables to the *existing* coordinator DB on `ree-cloud-1` and extend `app.py` with new endpoints, rather than building a parallel piece of infrastructure. This keeps one coordinator, one DB, one always-on box to reason about.

**Follow the same three-phase shadow-first cutover** the queue used (section 2), not a hard cutover -- every session in the fleet depends on `task_claim.py`/`chip_ledger.py` working, so this is exactly the kind of infra change `feedback_infra_shadow_first` (memory) says must be reversible and staged.

**Server-side atomic claim-check-and-write is a strict correctness improvement, not just a contention reduction.** Root `CLAUDE.md`'s own "Conflict resolution" section admits arbitration today is "best-effort, not a lock": two sessions can each read `TASK_CLAIMS.json` clean and both write, which is exactly the confirmed 2026-07-28 three-session collision on `runner_remote_control.py`. A single DB transaction (the same `BEGIN IMMEDIATE` primitive `db.py` already uses for experiment claims) removes the read-then-write gap across machines entirely -- there is no longer a window for two different machines to land in, only one DB transaction ordering to reason about.

## 4. Scope

**In scope:** `TASK_CLAIMS.json` and `TASK_CHIPS.json` only. Both are structured, mostly-append records with a small, stable per-entry schema (session_id/claimed_at/task/resources/status/... for claims; chip_ref/task_id/title/tldr/prompt/status/claimed_by/... for chips) -- the same shape as the queue entries the Phase 3 coordinator already models.

**Explicitly out of scope, and why:**
- **`claims.yaml`** and **`WORKSPACE_STATE.md`** are prose documents authored by governance/session-closing sessions with real editorial content, not pure coordination bookkeeping. They do not obviously fit a DB-table model the same way a claim/chip record does. Treat as a separate, later question if this migration succeeds -- do not assume the mechanism trivially extends.
- **`experiment_queue.json`** is already coordinator-authoritative (Phase 2/3, section 2). Nothing to do here.
- **Work-repo (`ree-v3`/`REE_assembly`) code-plane contention** already has its own, different, already-adequate defense (`integration/<slug>` staging branches, per-file claim discipline in root `CLAUDE.md` "Why trunk-only"). Out of scope.

## 5. Architecture design (5.2 REVIEWED and implementation-ready as of 2026-08-26; 5.1/5.3 unchanged)

### 5.1 Who writes today (the actual contention surface)

Only two real git clients write `TASK_CLAIMS.json`/`TASK_CHIPS.json` today: the Mac (interactive sessions + worktrees) and `ree-cloud-5` (the metaworker dispatcher, ~123 worktrees per `reference_cloud_workers` memory). `ree-cloud-1..4` never touch these files -- they are experiment-only runners mediated entirely by the coordinator already. This is good news for feasibility: the write-side fan-in is small.

### 5.2 Schema + endpoint design (REVIEWED against `schema.sql` + `db.py`, 2026-08-26)

**Status: implementation-ready.** This section was a sketch until 2026-08-26; it has now been written against a full read of `ree-v3/coordinator/schema.sql` (155 lines), `db.py` (1296) and `app.py` (975), and every field/uniqueness assumption below was verified against the **live** `TASK_CLAIMS.json` (154 entries) and `TASK_CHIPS.json` (1692 entries) rather than inferred. Where the earlier sketch was wrong, it is corrected rather than softened -- see "Design problems found" at the end, which is the part a Phase-1 implementer should read first.

#### 5.2.1 Conventions inherited from the existing schema

The two tables below deliberately copy four patterns already load-bearing in `schema.sql`, so nothing new has to be reasoned about:

- **A lossless `entry_json` column** on every row, mirroring `experiments.item_json`. Materialization back to the JSON files reads this, so a field this schema does not model explicitly still round-trips. This is what makes the migration safe against every existing consumer (`audit_stale_claims.py`, `prune_task_claims_done.py`, `chip_ledger.py list`, `serve.py`'s `/workset` panel, `audit_orphan_chips.py`, `substrate_queue_writeback_drift.py`).
- **`updated_at TEXT NOT NULL`** on every row, ISO-8601 UTC via `db.utcnow()`.
- **Additive-only migrations** in a `_migrate_*(conn)` function called from `connect()`, guarded by a `PRAGMA table_info` column check -- never a table rebuild. Existing rows keep NULL.
- **ASCII-only** in all returned strings and log lines.

#### 5.2.2 `task_claims` -- exact DDL

```sql
-- One row per TASK_CLAIMS.json claims[] entry.
-- PK is COMPOSITE and must stay that way: CLAUDE.md states the claim key is
-- (session_id, claimed_at), and `close --claimed-at` exists precisely because
-- session_id alone is ambiguous. Verified on the live file 2026-08-26:
-- 0 duplicate (session_id, claimed_at) pairs, but 8 session_ids own more than
-- one claim -- so a session_id-only PK would silently collapse real rows.
CREATE TABLE IF NOT EXISTS task_claims (
    session_id                   TEXT NOT NULL,
    claimed_at                   TEXT NOT NULL,   -- ISO-8601 UTC, second half of the key
    session_label                TEXT NOT NULL DEFAULT '',
    task                         TEXT NOT NULL DEFAULT '',
    status                       TEXT NOT NULL DEFAULT 'active',  -- active|done
    closed_at                    TEXT,            -- committer date of the landing commit
    completion_note              TEXT,
    completion_note_history_json TEXT,            -- JSON array, append-only; see 5.2.5
    spawned_by                   TEXT,            -- present on 2/154 live entries
    entry_json                   TEXT NOT NULL,   -- full original entry, lossless
    updated_at                   TEXT NOT NULL,
    PRIMARY KEY (session_id, claimed_at)
);
CREATE INDEX IF NOT EXISTS idx_task_claims_status ON task_claims(status);

-- `resources` is a LIST and gets a child table, NOT a JSON column. This is the
-- single most important schema decision in this document -- see design problem
-- D2. Cheap: 372 rows total across all 154 live claims, 200 distinct paths.
CREATE TABLE IF NOT EXISTS task_claim_resources (
    session_id  TEXT NOT NULL,
    claimed_at  TEXT NOT NULL,
    resource    TEXT NOT NULL,           -- repo-relative path, verbatim
    PRIMARY KEY (session_id, claimed_at, resource),
    FOREIGN KEY (session_id, claimed_at)
        REFERENCES task_claims(session_id, claimed_at) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_task_claim_resources_resource
    ON task_claim_resources(resource);
```

#### 5.2.3 `chip_ledger` -- exact DDL

```sql
-- One row per TASK_CHIPS.json chips[] entry. PK = chip_ref (verified unique
-- across all 1692 live entries). task_id CANNOT be the PK: it is NULL on
-- 1043/1692 rows (a chip only gets one if spawn_task actually minted it), so
-- it is a nullable column with a PARTIAL unique index instead -- 649 non-null
-- values, 0 duplicates.
CREATE TABLE IF NOT EXISTS chip_ledger (
    chip_ref                     TEXT PRIMARY KEY,
    task_id                      TEXT,
    session_id                   TEXT NOT NULL,
    session_label                TEXT NOT NULL DEFAULT '',
    title                        TEXT NOT NULL DEFAULT '',
    tldr                         TEXT NOT NULL DEFAULT '',
    prompt                       TEXT,           -- NULL once archived (see D5)
    cwd                          TEXT NOT NULL DEFAULT '',
    origin                       TEXT,           -- spawn_task|headless|hygiene_tick|igw_tick|proposal_tick
    kind                         TEXT,           -- work|decision|report
    urgency                      INTEGER NOT NULL DEFAULT 0,   -- bool
    spawned_at                   TEXT NOT NULL,
    origin_host                  TEXT,           -- canonical_machine_name()
    origin_host_raw              TEXT,           -- as reported; audit only (see D6)
    status                       TEXT NOT NULL DEFAULT 'open',  -- open|done|withdrawn
    claimed_by                   TEXT,
    claimed_at                   TEXT,
    claim_note                   TEXT,
    claimed_host                 TEXT,           -- canonical
    claimed_host_raw             TEXT,           -- as reported; audit only
    resolved_at                  TEXT,
    resolved_by_session_id       TEXT,
    resolution_note              TEXT,           -- NULL once archived (see D5)
    resolution_note_auto         INTEGER NOT NULL DEFAULT 0,   -- bool
    attached_by_session_id       TEXT,
    attached_at                  TEXT,
    archived_json                TEXT,           -- {file, month, fields[], at}
    prompt_history_json          TEXT,           -- JSON array
    urgency_history_json         TEXT,           -- JSON array
    resolution_note_history_json TEXT,           -- JSON array
    confirmer_verdict_json       TEXT,           -- JSON object
    entry_json                   TEXT NOT NULL,
    updated_at                   TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_chip_ledger_task_id
    ON chip_ledger(task_id) WHERE task_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_chip_ledger_status  ON chip_ledger(status);
CREATE INDEX IF NOT EXISTS idx_chip_ledger_claimed ON chip_ledger(status, claimed_by);
CREATE INDEX IF NOT EXISTS idx_chip_ledger_spawned ON chip_ledger(status, spawned_at);
```

File-level metadata (`schema_version`, and `TASK_CLAIMS.json`'s `stale_after_hours: 6`) is **not** a column -- it is regenerated by the materializer from coordinator config constants (`COORDINATOR_TASK_CLAIM_STALE_HOURS`, defaulting to 6 to match today's file).

#### 5.2.4 The atomic write -- `try_open_task_claim`, mirroring `try_claim`

This is where the migration earns its correctness claim (section 3). Today's arbitration is, in CLAUDE.md's own words, "best-effort, not a lock": `task_claim.py open` reads `TASK_CLAIMS.json`, checks for a rival, then writes -- and two sessions on two machines can both pass the check. The DB version closes that window with the *same* primitive `try_claim` already uses:

```python
def try_open_task_claim(conn, session_id, session_label, task, resources,
                        allow_overlap=False, spawned_by=None,
                        stale_hours=TASK_CLAIM_STALE_HOURS_DEFAULT, now=None):
    """Atomic claim-open with resource arbitration. Returns
    (verdict, payload) where verdict is one of:
      'ok'            -- claim written, caller owns every named resource
      'idempotent'    -- this session already holds an active claim; nothing written
      'owned_by_other'-- a live rival owns >=1 named FILE resource; nothing written
      'error'
    payload carries the owner rows so the CLI can render today's exit-3 text.

    Atomicity: BEGIN IMMEDIATE takes the write lock BEFORE the rival SELECT,
    so no other request -- on any machine -- can interleave between the
    arbitration check and the INSERT. This is the read-then-write gap that
    the git implementation structurally cannot close, and it is why the
    2026-07-28 three-session collision on runner_remote_control.py (three
    claims inside 84 seconds, two implementations live in one working tree)
    cannot recur under this path.

    `now` is injected for testability, matching db.py's existing convention
    (_is_stale, machine_departed, lifecycle_state all take an explicit now).
    """
    now = now or utcnow()
    try:
        conn.execute("BEGIN IMMEDIATE")
        # Preserve today's documented idempotency: `open` is idempotent per
        # session-id and silently no-ops on a re-run. Without this the
        # server-assigned claimed_at would mint a SECOND row every retry.
        existing = conn.execute(
            "SELECT claimed_at FROM task_claims "
            "WHERE session_id=? AND status='active'", (session_id,)
        ).fetchone()
        if existing is not None:
            conn.execute("ROLLBACK")
            return ("idempotent", {"claimed_at": existing["claimed_at"]})

        rivals = []
        if not allow_overlap and resources:
            # Scope claims are NOT arbitrated -- a verdict fires only on an
            # exact match of a FILE-shaped resource. governance.sh holds
            # REE_assembly/evidence/ for a whole regen and fails open;
            # arbitrating it would stop every evidence session. Directory
            # overlaps are reported as a NOTE by the caller, never a refusal.
            files = [r for r in resources if not r.endswith("/")]
            if files:
                q = ",".join("?" * len(files))
                rivals = conn.execute(
                    "SELECT c.session_id, c.claimed_at, c.session_label, "
                    "       c.task, r.resource "
                    "FROM task_claim_resources r "
                    "JOIN task_claims c ON c.session_id=r.session_id "
                    "                  AND c.claimed_at=r.claimed_at "
                    "WHERE r.resource IN (%s) AND c.status='active'" % q,
                    files,
                ).fetchall()
                # Stale rivals (older than stale_hours) are excluded, matching
                # task_claim.py's existing arbitration.
                rivals = [r for r in rivals
                          if not _is_stale(r["claimed_at"], stale_hours, now)]
        if rivals:
            conn.execute("ROLLBACK")
            return ("owned_by_other", {"rivals": [dict(r) for r in rivals]})

        conn.execute(
            "INSERT INTO task_claims (session_id, claimed_at, session_label, "
            " task, status, spawned_by, entry_json, updated_at) "
            "VALUES (?,?,?,?, 'active', ?, ?, ?)",
            (session_id, now, session_label, task, spawned_by,
             json.dumps({...}, sort_keys=True), now),
        )
        conn.executemany(
            "INSERT OR IGNORE INTO task_claim_resources "
            "(session_id, claimed_at, resource) VALUES (?,?,?)",
            [(session_id, now, r) for r in resources],
        )
        conn.execute("COMMIT")
        return ("ok", {"claimed_at": now})
    except sqlite3.Error:
        try:
            conn.execute("ROLLBACK")
        except sqlite3.Error:
            pass
        return ("error", {})
```

Every other mutating verb follows the identical `BEGIN IMMEDIATE` / SELECT-guard / conditional-UPDATE / `COMMIT` skeleton already used by `try_claim`, `release_claim` and `ack_command` -- most are simpler, because they address one row by primary key. `close`, `renew`, `amend` guard on `(session_id, claimed_at)` and refuse rather than guess when `claimed_at` is omitted and the session owns more than one row (today's documented `close --claimed-at` behaviour, including printing the candidate stamps).

#### 5.2.5 Endpoints -- exact signatures

All are bearer-authenticated exactly like every existing endpoint (`self._authed()`), return `application/json` via `self._send(code, obj)`, and accept an optional gzip body via `self._json_body()`. `409` is used for a refusal that is a legitimate verdict (a rival owns the resource); `400` for a malformed request; `404` for an unknown key.

| Verb | Method + path | Request body | Response |
|---|---|---|---|
| open | `POST /task_claim/open` | `{session_id, session_label, task, resources[], allow_overlap?, spawned_by?}` | `200 {verdict:"ok"\|"idempotent", claimed_at}` / `409 {verdict:"owned_by_other", rivals:[{session_id, claimed_at, session_label, task, resource}], notes:[...]}` |
| close | `POST /task_claim/close` | `{session_id, claimed_at?, closed_at, completion_note, not_landed?}` | `200 {ok:true}` / `409 {error:"ambiguous", candidates:[{claimed_at, task}]}` / `404` |
| check | `GET /task_claim/check?resource=A&resource=B` | -- | `200 {owned:false}` / `200 {owned:true, rivals:[...]}` |
| renew | `POST /task_claim/renew` | `{session_id, claimed_at?}` | `200 {ok:true, claimed_at}` |
| amend | `POST /task_claim/amend` | `{session_id, claimed_at?, completion_note, reason?}` | `200 {ok:true}` (pushes prior text onto `completion_note_history_json`) |
| dedupe | `POST /task_claim/dedupe` | `{session_id, claimed_at?}` | `200 {removed:0, note:"not applicable under PK"}` -- see D3 |
| list | `GET /task_claim/list?status=active` | -- | `200 {claims:[...], stale_after_hours:6}` |
| record | `POST /chip/record` | full chip entry (`chip_ref` required; `prompt` MUST contain `[chip_ref: <ref>]`) | `200 {ok:true}` / `400 {error:"prompt missing chip_ref marker"}` |
| claim | `POST /chip/claim` | `{chip_ref, claimed_by, claimed_host, note?, stale_after_hours?}` | `200 {ok:true}` / `409 {error:"already claimed", claimed_by, claimed_at}` |
| unclaim | `POST /chip/unclaim` | `{chip_ref, note?}` | `200 {ok:true}` |
| resolve | `POST /chip/resolve` | `{chip_ref?, task_id?, status:"done"\|"withdrawn", note, resolved_by_session_id}` | `200 {ok:true, changed:bool}` -- `changed:false` when already at that status (today's silent no-op, now *reported*; see D11) |
| attach | `POST /chip/attach` | `{chip_ref, task_id, attached_by_session_id}` | `200 {ok:true}` |
| amend-prompt | `POST /chip/amend-prompt` | `{chip_ref, prompt, reason}` | `200 {ok:true}` / `400` if marker missing |
| list | `GET /chip/list?status=open&origin=...&limit=...` | -- | `200 {chips:[...]}` |
| archive | -- | -- | **stays git-side; see D7** |

Client-side, `task_claim.py`/`chip_ledger.py` keep their exact CLI surface and gain one transport branch each (coordinator first, git on failure -- section 5.3).

#### 5.2.6 Design problems found

These are the review's actual output. D1-D3 and D7 change the design; the rest are constraints an implementer would otherwise discover the hard way.

- **D1 -- the sketch's `/claim/open` path was wrong and must not be used.** `/claim` and `/claim/release` are already taken by the **experiment** claim endpoints (`app.py` lines 471, 543) and mean something entirely different. Namespacing new verbs under `/claim/*` would put two unrelated claim systems in one path prefix. Corrected above to `/task_claim/*` and `/chip/*`.
- **D2 -- `resources` must be a child table, not a JSON column, and this is the whole correctness argument.** A JSON blob can only be arbitrated by loading every active claim and scanning in Python -- which is exactly today's best-effort check, reimplemented server-side, and would leave the migration with no correctness gain at all over git. Only an indexed `task_claim_resources` row makes the rival test a single indexed SELECT *inside* the `BEGIN IMMEDIATE` transaction. This is the difference between "the same race, faster" and "the race is gone".
- **D3 -- `dedupe` has no atomic equivalent, and does not need one.** It is a whole-file operation that removes entries byte-identical to another entry. Under a `(session_id, claimed_at)` primary key the duplicate class it cleans up **cannot be created** -- the second INSERT fails. The 2026-08-18 byte-identical-duplicate incident is prevented at the source rather than repaired after the fact. Keep the verb as an accepted no-op returning `{"removed": 0}` so existing call sites and tests do not break; do not port its logic.
- **D4 -- `task_id` cannot be an identifier.** NULL on 1043/1692 live rows. `chip_ref` is the only always-present unique key; `resolve` accepting `--task-id` must resolve through the partial unique index and 404 cleanly on a NULL-task_id chip.
- **D5 -- archiving must strip FIELDS and keep the ROW, and the DB makes this easy to get wrong.** CLAUDE.md is emphatic that `merge_origin_into_local()` has no deletion path and that teaching it tombstones would be a mistake. A DB tempts an implementer to `DELETE` archived rows. It must instead set `prompt=NULL, resolution_note=NULL, archived_json=...` and keep the row, so the materialized JSON keeps the identity/status/timestamp fields and `chip_ledger.archived_field()` readers continue to work unchanged.
- **D6 -- the bearer token identifies a MACHINE; claims and chips are per-SESSION.** `auth_machine()` maps a token to a machine label, but `session_id` is the actor here and must come from the body. Follow the existing `machine_raw` vs `_canon(machine)` split exactly (`app.py` `/claim`): store the canonical host for logic, keep the raw reported host for audit. `origin_host`/`claimed_host` must go through `machine_identity.canonical_machine_name()` -- never a raw compare, per CLAUDE.md's DLAPTOP note.
- **D7 -- `chip archive` does NOT move to the coordinator in Phase 2.** Its correctness gate is that the archive file has actually reached **origin** (`cmd_archive` fetches and verifies at `origin_ref()` before stripping, after the 2026-08-19 first-run failure). That gate is inherently a git fact and has no DB equivalent. Leave `archive` as a git-side operation reading the materialized file; revisit only in Phase 3.
- **D8 -- `open`'s idempotency is load-bearing and is easy to lose.** Today `open` is idempotent per `session_id`. If the server assigns `claimed_at = now`, a naive INSERT mints a *new* row on every retry -- and retries are common, since the current git path fails and retries under contention. The active-claim pre-check in `try_open_task_claim` above is not optional.
- **D9 -- history fields stay JSON columns, deliberately, unlike `resources`.** `completion_note_history`, `prompt_history`, `urgency_history`, `resolution_note_history` are append-only audit lists that nothing queries *across* rows (62, 22, 5 and 1 live occurrences respectively). A child table would add four joins to buy nothing. The asymmetry with D2 is intentional and is justified by whether anything arbitrates on the field.
- **D10 -- `check` must be a GET.** It is the START-TIME predicate a chip STOP-CHECK carries and it writes nothing; making it a POST invites an implementer to log or mutate on it.
- **D11 -- `resolve` on an already-resolved chip is currently a SILENT no-op**, which is exactly the trap the headless worker contract warns about (`resolve --status open` losing a note). The endpoint should return `{"changed": false}` explicitly so the CLI can say so, rather than reporting success indistinguishable from a real transition.
- **D12 (added 2026-08-27 during the PHASE-2 build) -- `claimed_at` is CLIENT-SUPPLIED, not server-stamped. This CHANGES 5.2.4 as written above.** The sketch has `try_open_task_claim` stamp `claimed_at = now` server-side, and that is wrong for as long as the client is still performing its own git write -- which, per the PHASE-2a scope note in section 10, is the whole of this phase. A server stamp and a client stamp differ by the network round trip, so the DB row and the JSON entry would carry **different halves of the `(session_id, claimed_at)` primary key**, and the PHASE-1 reconciler would report that as drift on every tick, forever. Implemented as: the client sends the stamp it is about to write to git, and the server falls back to its own `now` only when the field is absent (which keeps the sketch's signature valid for any caller that does not have a stamp of its own). The same applies to a chip claim's `claimed_at`. Pinned by `test_the_clients_own_claimed_at_is_what_is_sent` in `scripts/test_task_claim_coordinator_branch.py` and `test_claim_calls_the_coordinator_and_still_writes_git` in `scripts/test_chip_ledger_coordinator_branch.py`.
- **D13 (added 2026-08-27) -- the client flag MUST NOT be `COORDINATION_MODE`.** The obvious implementation reuses ree-v3's existing `coordinator_client.py` env contract wholesale, since this module is otherwise modelled on it. That would have been an incident: `COORDINATION_MODE=coordinator` is **already set in production** on every cloud worker's `ree-runner.service` for the EXPERIMENT plane, so reusing the name would have flipped claim/chip transport across the fleet the moment the code landed -- a silent default flip, which is precisely what the phase forbids. The mode variable is therefore namespaced (`TASK_CLAIM_COORDINATION_MODE`, default `git`) while the CONNECTION settings (`_URL`, `_TOKEN`, `_TIMEOUT`) do fall back to the experiment-plane names, so a box already configured for the coordinator needs only the mode flag. Pinned by `test_the_experiment_plane_flag_does_NOT_enable_this` in `scripts/test_coordinator_transport.py`.

### 5.3 Fallback / degrade path (must be first-class, not an afterthought)

When the coordinator or the WireGuard mesh is unreachable, `task_claim.py`/`chip_ledger.py` fall back to **today's existing local git-mutate-and-commit path**, unchanged. This is not new code to write -- it is the *current* implementation, kept exactly as-is and demoted to a fallback branch. This matters for a specific, documented reason (section 6.2): the Mac's WireGuard tunnel has a real flakiness history (stale-handshake blackouts, `reference_wireguard_mesh` memory), and today that does not matter for claims/chips because the Mac talks to GitHub directly. Once the coordinator is authoritative, the Mac's own session productivity becomes dependent on that tunnel being up -- so "coordinator unreachable" must be a well-exercised path from day one, not a rare edge case discovered later.

## 6. Prerequisites (PHASE-0 -- must close before Phase 1 starts)

### 6.1 WireGuard mesh coverage for `ree-cloud-5`

The mesh, as last documented (`reference_wireguard_mesh` memory, 2026-06-11), has four peers: the hub (`10.8.0.1`), the Mac's GUI tunnel (`10.8.0.11`), and cloud workers 2/3/4 (`10.8.0.12/13/14`). **`ree-cloud-5` was discovered on 2026-08-11 -- after that mesh documentation -- and is not a confirmed peer.** Given `ree-cloud-5` is one of exactly two machines that write these files today (section 5.1), this is a hard prerequisite, not a nice-to-have. Verify live with `sudo wg show` on the hub before assuming either way; adding a peer is documented as a single non-disruptive command (`sudo wg set wg0 peer <pub> allowed-ips 10.8.0.X/32` + append a `[Peer]` block to `wg0.conf`, no interface restart).

**RESOLVED 2026-08-26 -- verified live, no change required. The assumption above was wrong.**

`ree-cloud-5` **is already a WireGuard peer** and has been configured as one at some point before this audit. Measured directly on the hub (`sudo wg show` + `/etc/wireguard/wg0.conf`):

- Peer `lfhMcbKT0c09vfe7bZqD4lWvLnl3x5m062Ci2pLKuXI=`, `allowed ips 10.8.0.15/32`, latest handshake **1 minute** old at time of check.
- Persisted in `/etc/wireguard/wg0.conf` under the comment `# ree-cloud-5 (Phase H metaworker-dispatch box)` -- so it survives an interface restart. It is not a live-only `wg set` that would evaporate.
- **Bidirectional**, which the prerequisite as written did not actually ask about but which is what matters: from `ree-cloud-5`, `sudo wg show` lists the hub (`qp3fuadZ8...`, `10.8.0.1/32`) as its peer with `persistent keepalive: every 25 seconds`.

End-to-end verification from `ree-cloud-5`, not inferred from config:

```
$ ping -c 3 10.8.0.1     -> 3 packets transmitted, 3 received, 0% packet loss
                            rtt min/avg/max = 0.768/0.996/1.427 ms
$ curl http://10.8.0.1:8787/health
                         -> HTTP 200 in 2.0 ms
                            {"ok": true, "mode": "coordinator"}
```

So the coordinator is **already reachable over the mesh from the metaworker box**, which is the actual thing this prerequisite exists to establish. No peer was added and no config was edited.

**Current mesh (measured, supersedes the 2026-06-11 four-peer doc):** `10.8.0.1` hub, `10.8.0.11` Mac GUI tunnel, `10.8.0.12` ree-cloud-2, `10.8.0.13` ree-cloud-3, `10.8.0.14` ree-cloud-4, `10.8.0.15` ree-cloud-5, `10.8.0.20` an iPhone peer (added 2026-06-23). Next free /32 for a future box is `10.8.0.16`.

One incidental observation, not a blocker for this migration: `ree-cloud-3`'s handshake was **5h57m** stale at check time. That is the expected signature of a scaler-powered-off experiment worker, not a fault, and `ree-cloud-3` writes neither `TASK_CLAIMS.json` nor `TASK_CHIPS.json` (section 5.1), so it is outside this migration's contention surface either way.

### 6.2 Mac WireGuard tunnel reliability audit

The Mac's tunnel has a documented history of "Connected but not routing" blackouts, mitigated by a `PersistentKeepalive` fix + a launchd watchdog (`com.ree.wgwatchdog`) + a daily health digest (`com.ree.wghealthdigest`) -- all detailed in `reference_wireguard_mesh` memory. Before Phase 2 makes the Mac's claim/chip traffic depend on this tunnel, confirm the watchdog is still installed and the health digest still reads `bounces_24h=0` (keepalive holding). If it is not, fix that first -- it is a precondition for the whole migration, not a Phase-2-time surprise.

**AUDITED 2026-08-26 on the Mac itself (`DLAPTOP`). The literal precondition is MET, but the precondition as written is a weak predicate -- read the second half of this.**

What was verified:

- Both launchd agents are **loaded and healthy**: `launchctl list` shows `com.ree.wgwatchdog` and `com.ree.wghealthdigest`, both with last exit status `0`. Plists present in `~/Library/LaunchAgents/`.
- The most recent digest (`~/Library/Logs/ree_wg_health.log`, `2026-08-26T11:44:16Z`) reads `hub reachable; watchdog=active; 24h: bounces=0 recovers=0 warns=0 offline_skips=0; keepalive=HOLDING`. **`bounces_24h=0`, exactly what 6.2 asks for.**
- Independently corroborated from the hub side: the Mac's peer (`10.8.0.11`) showed a **41-second-old** handshake during the 6.1 check.

**The finding that matters, which a point-check would have missed.** The full log is 75 digests spanning 2026-06-11 to 2026-08-26, and it is **50 HOLDING / 25 FLAPPING -- 33% of days show at least one bounce**. Eight of those flapping days fall in the last 30, the most recent on 2026-08-22 (4 days before this audit). On five occasions `recovers < bounces` (e.g. `2026-08-20T18:49Z bounces=4 recovers=1 warns=3`), meaning the watchdog did **not** fully recover every bounce it saw.

Nothing here is a regression -- there are **zero** `hub unreachable` digests and **zero** `watchdog=inactive` digests across the entire 75-day record, so the tunnel has never been recorded fully down and the mitigation is working as designed. But the consequence for this plan is concrete: **"the digest reads `bounces_24h=0` today" is close to a coin flip about tomorrow**, and 6.2's phrasing invites a future session to run it once, see green, and treat the Mac's tunnel as settled.

**Recommended restatement of this prerequisite for Phase 2** (not applied to the criterion above, since changing a gate is not this node's call): replace the point check with a rate criterion measured over a trailing window -- e.g. *no unrecovered bounce (`recovers < bounces`) in the trailing 14 days*, which the current record would **fail** (2026-08-20). Whichever form is chosen, it should be a rate, not a snapshot.

**This does not block PHASE-0 or PHASE-1**, and deliberately so: Phase 1 is a read-only shadow mirror with no write path (see the PHASE-1 node), so nothing about it depends on the Mac's tunnel being up. The flakiness is a **PHASE-2 gate**, where section 5.3's git-fallback path stops being a nicety and becomes the thing that keeps the Mac productive on a bounce. Carried forward as such rather than passed silently.

**REVISED 2026-08-27 (user decision): this is NOT a PHASE-2 pre-gate. It is deferred to POST-cutover monitoring.** Originally proposed as a trailing-window rate check (e.g. no unrecovered bounce in the trailing 14 days) that PHASE-2 would have to pass *before* cutover. The user's explicit call: the current git-coordination system's day-to-day cost (ref-wedges, read-modify-write races, hook false-positives -- see the same day's session for direct, repeated examples) is actively overwhelming project progress *right now*, and that cost outweighs the marginal risk this pre-gate was hedging against. Two things make deferring it to monitoring rather than dropping it a sound trade, not a corner cut:

1. Section 5.3's git-fallback path is *already* designed as first-class, well-exercised infrastructure ("not a rare edge case discovered later") -- a tunnel bounce during PHASE-2 degrades the Mac to exactly today's git-mutate-and-commit behavior, not to a hard failure. The pre-gate was hedging against a *rough UX during a bounce*, not against data loss or a stuck session.
2. Nothing about the rate-criterion IDEA is wrong or discarded -- only its position in the sequence changes. Track it live post-cutover (the same `bounces_24h`/`recovers`-vs-`bounces` digest fields already emit) rather than requiring N clean days observed *before* PHASE-2 can start. If real degraded-UX pain shows up post-cutover, that is the signal to revisit -- not a multi-day wait beforehand for a failure mode section 5.3 is already built to absorb.

Held-out note (GOV-HELDOUT-1 spirit, not the full discipline -- this is a one-off user call, not a standing rule edit): this reverses the plan's own prior stance ("changing a gate is not this node's call") specifically because the call is now coming from the user directly, which is the one thing that section explicitly deferred to.

### 6.3 Schema/endpoint review

Section 5.2 is a sketch written without reading `ree-v3/coordinator/schema.sql` or `db.py` in implementation-level detail. Before writing any code, a session should read both, confirm the `try_claim`-style atomic-transaction pattern generalizes cleanly to a claim/chip shape (vs. the experiment-claim shape it was built for), and update this section with the actual table/endpoint design.

**DONE 2026-08-26.** Section 5.2 has been rewritten against a full read of `schema.sql`, `db.py` and `app.py`, with every field and uniqueness assumption checked against the live `TASK_CLAIMS.json`/`TASK_CHIPS.json` rather than inferred. The `try_claim` pattern **does** generalize cleanly -- `BEGIN IMMEDIATE` + a guarded SELECT + a conditional write is the right shape for every mutating verb here -- but it only delivers the correctness gain if `resources` is an indexed child table (design problem D2). Eleven design problems are recorded in 5.2.6; D1, D2, D3 and D7 change the design as sketched.

## 7. Phased rollout

See the frontmatter `nodes` table at the top of this file for the authoritative, resumable phase list (PHASE-0 through PHASE-3) with live status. Do not re-derive the phase list from this prose section -- update the frontmatter node instead, the same convention every other multi-session plan doc in this directory uses.

## 8. Open questions (not yet decided)

- **Which machine hosts the new tables/endpoints:** the existing hub (`ree-cloud-1`) is the natural choice (already always-on, already the coordinator), but confirm nothing about claim/chip traffic volume or latency argues for a different box.
- **Degrade UX:** when `task_claim.py open` falls back to git because the coordinator is unreachable, should it warn the user inline, or fail silently identical to today's behavior? Leaning toward an explicit warning, since a session should know it's on the weaker-arbitration path.
- **Whether `claims.yaml`/`WORKSPACE_STATE.md` ever get folded in:** deliberately deferred (section 4). Revisit only after PHASE-2 is stable in production for TASK_CLAIMS/TASK_CHIPS.

## 9. Risks (carried forward from the initial design conversation, 2026-08-26)

- **New single point of failure.** Every session everywhere becomes dependent on the coordinator + mesh for claim/chip coordination, where today each machine can (imperfectly) act independently. Mitigated by the git-fallback path (section 5.3) and by the hub already being the fleet's highest-uptime box, but this is a real trade, not a free win.
- **File-transfer variants that ship whole files are a trap.** An earlier version of this proposal considered raw `rsync`/`scp` of the whole JSON file between machines. Rejected: that reintroduces the exact read-modify-write contamination hazard root `CLAUDE.md`'s "Concurrency Rules" section exists to prevent -- worse than git, since `rsync` has no compare-and-swap at all. Any transport must ship discrete intents (an HTTP call, or at minimum a small append-only intent record), never a whole-file sync.
- **This is a transport-layer change to two heavily-tested scripts** (`task_claim.py`, `chip_ledger.py`), not a wrapper -- it touches the push-by-default, bot-authorship, close/dedupe/amend plumbing documented at length in root `CLAUDE.md`. Treat it with the same care those scripts' existing test suites imply (`test_task_claim_*.py`, `test_chip_ledger_*.py`, dozens of files each).

## 10. Where to resume

**PHASE-0 is closed (2026-08-26).** Sections 6.1, 6.2 and 6.3 all carry live-verified answers, not carried-forward memory claims.

**PHASE-1 is now soaking with `/task_claim/*` and `/chip/*` LIVE (coordinator
restarted 2026-08-27T07:52:01Z, session
metaworker-chip-20260827-coordinator-phase1-restart-soak-start).** The
read-only clone, systemd timer, zero-drift verification, and now the
coordinator restart itself are all done -- see the PHASE-1 frontmatter node
for full detail. The exit criterion (N days of `diverged_ticks` staying at
0) is now directly measurable via `GET /task_claim/drift`
(`total_ticks`/`diverged_ticks`), no `journalctl` workaround required. As of
the restart, only ~11.4h of zero-drift history exists -- well short of any
reasonable N. **The only remaining PHASE-1 work is elapsed time**: no code,
no infra, no config change is pending. A future session (or a human) should
periodically check `GET /task_claim/drift` (or `journalctl -u
ree-task-claim-chip-shadow-sync`) until N days of clean history has
accumulated, then bring that evidence forward for the PHASE-2 go/no-go
decision. (Section 6.2's Mac-tunnel rate-criterion is no longer a
prerequisite here -- see the 2026-08-27 revision at the end of section 6.2:
deferred to post-cutover monitoring by explicit user decision.)

Two things PHASE-1 must NOT do, unchanged from the original plan and still
true of the code as built and now the live routes: it must not add any write
path back to git (that is PHASE-2, and it is explicitly not user-ratified as
a build -- see section 3), and it must not treat section 6.2's green digest
as settling the Mac's tunnel (see the rate-criterion recommendation there,
which is a PHASE-2 gate). Neither happened -- verified by
test_reconcile_never_dirties_the_source_working_tree and
test_no_mutating_task_claim_or_chip_post_route_exists in
ree-v3/coordinator/ (unchanged by this session, since it touched
infrastructure, not code), and the Mac's tunnel was not touched.

**PHASE-2a is BUILT (2026-08-27) and is where a resuming session picks up.**
The sentence that used to stand here -- "Do not start PHASE-2 from this
state" -- was written before the user's explicit 2026-08-27 go-ahead to
DECOUPLE the build from the soak. That decision is narrow and is worth
restating precisely, because the reasoning is what makes it safe: the soak
validates that the shadow mirror does not drift **before anything depends on
it**, which says nothing whatever about whether the transport code is
correct. So building and testing proceed in parallel; what still waits on the
soak is FLIPPING THE DEFAULT, and only that.

Read the PHASE-2 frontmatter node for exactly what landed and what is tested.
The four things still open, in the order a resuming session should think about
them:

1. **PHASE-2b -- the DB->git materializer.** The largest remaining piece, and
   the one that gates suppressing the client's own git write. Model it on
   `sync_daemon.py`'s `phase3_heartbeat_writer`: commit on STATE-CHANGE ONLY.
   Root `CLAUDE.md` explicitly forbids reintroducing a forced periodic
   liveness tick (it was the dominant source of `REE_assembly` history bloat
   and was deliberately retired), and this writer would be writing to the
   umbrella repo, whose trunk is already ~60-77% machine-written coordination
   data.
2. **Deployment.** The endpoints are on `ree-v3` `origin/main` but
   `ree-coordinator.service` on the hub has not been restarted to pick them
   up, so `POST /task_claim/open` still 404s in production -- exactly the
   state PHASE-1's own routes were in between 2026-08-26T19:00Z and the
   2026-08-27T07:52Z restart. Nothing depends on them, so this is not urgent;
   the point is that **"landed" must not be read as "reachable"**. Restarting
   the live coordinator remains a human-with-eyes-on action, per this doc's
   own standing framing.
3. **Soak evidence.** Unchanged: N days of `GET /task_claim/drift` showing
   `diverged_ticks: 0`.
4. **The go-live decision itself**, which is a human's and is separate from
   all three above.

**What a resuming session must NOT do:** flip
`TASK_CLAIM_COORDINATION_MODE` to `coordinator` anywhere -- not in
`.claude/settings.json`, not in a systemd unit, not as a default in
`coordinator_transport.py` -- and must not remove the git path. Section 5.3
and the PHASE-3 node both say the git path stays permanently, mirroring the
runner's own retained legacy git-claim fallback.

Update the frontmatter `nodes` status/note for whichever phase you touch, in the same commit as your actual work, so the next session does not have to re-read this whole document to find out what changed.
