---
closure_plan:
  id: task_claim_chip_coordinator_migration
  generation: process
  title: "TASK_CLAIMS/TASK_CHIPS Coordinator Migration (single-writer cutover)"
  registered: 2026-08-26
  last_updated: 2026-09-06
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
      status: done
      severity: high
      last_updated: 2026-09-06
      note: >
        CLOSED 2026-09-06 (session cutover-closeout-20260906). The soak
        PASSED under the RESTATED criterion (user decision 2026-09-01, see
        section 3): zero PERSISTENT divergence plus the tick-coverage clause.
        Measured 2026-09-01: 143 ticks/24h, 16 diverged, every one an orphan
        that self-healed within one reconcile cadence (26/26 identities,
        orphan age median 56s / max 100s), 0 content mismatches. Re-measured
        2026-09-06T20:55Z: 143 ticks/24h, 5 diverged, 0 content mismatches,
        0 persistent. The log now has a PROGRAMMATIC reader (durability
        review finding C.8): hygiene_routine_tick.py source 28
        (_drift_log_findings) reads GET /task_claim/drift over the last 24h
        every tick and chips only on a persistent orphan, a content
        mismatch, or a stalled detector -- the old "zero diverged ticks"
        wording is retired below as unmeetable, not merely unmet.

        SOAK EVIDENCE INVALIDATED AND THE DETECTOR FIXED, 2026-08-28 (session
        coordinator-migration-phase2b). The zero-drift record this node
        previously reported was real but SHORT, and everything after it was a
        FALSE POSITIVE. Found while judging the soak for a cutover go/no-go
        that the user had asked for -- not by any test or alarm.

        MEASURED: GET /task_claim/drift showed 64 of 200 ticks diverged.
        Clean from 2026-08-26T20:25:22Z, then diverged CONTINUOUSLY from
        2026-08-27T19:03:25Z onward. Cause: `scripts/prune_task_claims_done.py`
        commit b6907cce removed 127 `done` entries from TASK_CLAIMS.json at
        19:02:07Z, and the next shadow-sync tick 78 SECONDS LATER went
        diverged and never recovered. All 50 reported claim_orphans were
        verified individually: every one was present in git with status
        `done` immediately before that prune and absent after. ZERO
        unexplained. chip_orphans stayed 0 throughout.

        ROOT CAUSE: `db.reconcile_task_claims` treated any DB key absent from
        git as an orphan, and its own docstring justified that with
        "TASK_CLAIMS.json entries are never deleted (root CLAUDE.md)". THAT
        PREMISE IS FALSE. `prune_task_claims_done.py` deletes done entries
        older than 24h and runs at EVERY `/session-land` close (Phase 2b) --
        routine, documented and correct. The mirror never deletes (also
        correct), so every pruned entry became a permanent orphan.

        WHY THIS WAS WORSE THAN A NOISY METRIC, and the reason it is recorded
        at this length: (1) the exit criterion as written ("N days of
        diverged_ticks staying at 0") became UNMEETABLE -- one routine prune
        arms it forever, and the only reason ~22.6h of clean history existed
        at all is that no prune happened to land in that window; and (2) a
        REAL divergence would then have hidden behind an already-raised flag.
        The detector was not merely wrong, it was saturated.

        FIXED (ree-v3, same session): orphans are now split on the pruner's
        own predicate -- `done` + absent from git = RETIRED (expected,
        counted, reported in n_claims_retired and detail.claim_retired, never
        raises diverged); `active` + absent = ORPHAN (real drift, and the
        direction that actually loses work). Chips deliberately stay STRICT
        and are NOT given the same softening: chips are never deleted
        (archiving strips fields and keeps the row, D5; merge_origin_into_local
        has no deletion path), so a missing chip has no benign explanation.
        `task_claim_chip_drift_summary` also gained an optional `since=` window
        -- the cumulative totals permanently carry these 64 rows, which are not
        wrong and must not be deleted, so the criterion had to become windowed
        rather than absolute.

        DEPLOYED AND VERIFIED LIVE 2026-08-28T06:16:02Z (ree-v3 cacb5cb103,
        already on the hub's checkout; the shadow-sync timer runs a fresh
        process each tick, so NO coordinator restart was needed for the fix
        itself). The tick immediately after deploy read
        `diverged=0, n_claims_orphan=0, n_claims_retired=162, n_chips_orphan=0`
        against `diverged=1, n_claims_orphan=162` on the tick three minutes
        earlier -- same mirror, same git state, correct classification. The
        additive migration applied on that tick's own `connect()`.

        **THE SOAK CLOCK RESTARTS AT 2026-08-28T06:16:02Z.** Nothing before
        that instant is admissible evidence: the pre-19:03Z window was clean
        but only ~22.6h long, and everything after it was measured by a
        detector now known to be wrong.

        ONE CAVEAT ON READING IT: `GET /task_claim/drift?since=` needs a
        coordinator restart to become available, because `app.py`/`db.py` are
        loaded by the long-running service. The fix itself does not. Until
        someone restarts it, read the window straight from
        `task_claim_chip_drift_log` over SSH -- the rows are identical, only
        the convenience of the HTTP filter is pending.

        THE EXIT CRITERION IS THEREFORE RESTATED, and this is the operative
        version: `GET /task_claim/drift?since=<T-24h>` must report
        `window.diverged_ticks == 0` AND a `window.total_ticks` consistent
        with the 10-minute cadence (~144/day). The second clause is not
        decoration -- zero diverged out of two ticks is not evidence of
        anything, and without it a STALLED TIMER reads as a clean soak.

        Prior (retained for history; its zero-drift claim is superseded by the
        measurement above):
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
      status: done
      severity: high
      last_updated: 2026-09-06
      note: >
        LIVE SINCE 2026-08-28 and CLOSED 2026-09-06 (session
        cutover-closeout-20260906). Client git-write suppression is armed on
        the Mac, ree-cloud-4 and ree-cloud-5 (~/.ree_coordinator_client.json
        suppress_git_write=true); the hub materializer runs
        REGISTRY_WRITER_MODE=write on a 2-min timer (verified live 2026-09-06);
        every open/close/record/resolve in the fleet prints
        "coordinator-acknowledged; git write suppressed". The last
        unverified suppressed verb was closed 2026-09-06: `renew` now
        verifies its ack (verify_renew_coordinator_ack, durability review
        finding C.7) exactly as close/amend do, falling through to the git
        path on a hollow or mismatched ack. The durability review of
        2026-08-28 (coordinator_cutover_durability_review_20260828.md)
        returned HOLDS / no rollback. The git fallback path stays PERMANENT
        (section 5.3) and is exercised whenever the hub is unreachable.
        Everything below this paragraph is the build record and predates
        the go-live.

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

        PHASE-2b BUILT AND DEPLOYED IN CHECK MODE 2026-08-28 (session
        coordinator-phase2b-takeover-20260828, user-directed takeover).
        ree-v3 af4dcea1e9 + a trailing-newline-tolerance follow-up:
        * coordinator/task_claim_chip_git_writer.py -- the DB->git
          materializer. One tick = ingest origin (closes the
          fallback-commit race), render both registries from the lossless
          entry_json blobs (D14 retention at render: done>24h aged out,
          absorbing prune_task_claims_done.py's job; chips never dropped
          per D5; source-order-faithful; metadata carried over), byte-
          compare, and in write mode commit+push on state change only.
        * db.py: entry_json now stored VERBATIM (was sort_keys=True, which
          defeated _claim_entry_json's carefully-mirrored client key order
          and made D15 byte-equality impossible). Reconciler overwrites
          blobs from git every tick, so pre-change rows self-healed on the
          first post-land tick (one-tick n_updated blip; diverged counts
          only orphans, unaffected).
        * deploy/ree-task-claim-chip-git-writer.{service,timer}: installed
          and ENABLED on the hub 2026-08-28T07:28Z, 2-min cadence,
          REGISTRY_WRITER_MODE=check (renders + compares + reports, never
          writes -- the deployment soak). First live ticks: chips
          match=True (1974/1974 byte-identical against origin), claims
          mismatch ONLY in the expected direction (+0 added, -2 aged-out
          done entries the render correctly prunes).
        * 13 new contracts (test_task_claim_chip_git_writer.py): round-trip
          byte-equality incl unmodelled keys + odd key order, retention,
          fallback-race survival, coordinator-row canonical key order,
          state-change-only commits, check-mode-never-writes, source-order
          fidelity, trailing-newline tolerance. 131 existing task_claim/
          chip coordinator tests green, zero regressions.

        (c) CLIENT GIT-WRITE SUPPRESSION: BUILT AND LANDED 2026-08-28
        (REE_Working 3f6cfa5dd7, committed 13:33:50Z, session
        coordinator-suppression-20260828). task_claim.py + chip_ledger.py
        gain coordinator_suppression_armed() (transport enabled AND
        coordinator_transport.suppress_git_write()); each verb with a
        coordinator transport skips its local write+commit+push ONLY on
        its own per-verb ack allowlist -- open: ok/idempotent; close:
        ok/already_closed; chip record: ok/idempotent; chip
        claim/resolve/unclaim: ok -- and degrades byte-identically to the
        git path on EVERY other outcome (transport down, HTTP error,
        ambiguous, not_found, ref_collision, terminal_conflict). Verbs
        with no transport (amend/renew/dedupe on claims; attach,
        amend-prompt, declare/verify-handoff, archive on chips) are never
        suppressed, nor is a resolve carrying a confirmer verdict or
        --handoff-pending (no DB representation). Durability contract in
        both docstrings: the coordinator 200 IS the ack; origin-reach
        checks apply only to the fallback. Open's post-suppression
        contention re-read of the GIT file is retained (catches rivals on
        degraded git-path boxes; additive-refusal only). 29 new contracts
        (scripts/test_task_claim_git_suppression.py) + 15 affected suites
        re-run green (264 tests, incl. both coordinator-branch pin
        suites and the remote-tip wedge-gate suite).

        STILL OPEN, and the ACTUAL CUTOVER still waits on all of it:
        (a) soak evidence -- TWO soaks: the PHASE-1 windowed drift
        criterion (section 10 item 3) AND the materializer check-mode soak
        (journalctl -u ree-task-claim-chip-git-writer: chips_match=True
        and claims_delta never showing +added is the healthy signature;
        still clean as of 2026-08-28T13:19Z);
        (b) a separate human go-live confirmation; (d) client env wiring
        (mode flag + URL + token) for the THREE machines that write these
        files: the Mac (interactive sessions + launchd ticks), ree-cloud-5
        (the metaworker dispatcher), and ree-cloud-4 (the resident
        metaworker-dispatch box -- its dispatched headless chip sessions
        open/close claims when it is in that mode; user-confirmed
        2026-08-28). All three verified reachable to 10.8.0.1:8787 with
        tokens already in the coordinator roster. The
        ~/.ree_coordinator_client.json config file (coordinator_transport
        0d3dcc94b8) is the per-machine switch on each -- add
        "suppress_git_write": true to arm the (c) branch at flip time.
        (e) DEPLOYMENT of the endpoints IS DONE -- see below.

        POST-CUTOVER FOLLOW-ONS registered from user direction 2026-08-28
        (recorded here so the flip does not read as the finish line):
        (f) MCP TIDY -- scripts/mcp_server.py wraps these CLIs, so it
        inherits suppression for free, but its tool descriptions still
        narrate the git-write semantics; update them to describe the
        coordinator-ack semantics once the flip lands, and consider
        direct-coordinator read tools (check/list) that skip subprocess
        overhead entirely.
        (g) CHIP-LEDGER END-STATE AUDIT -- once the new system is
        established, sweep TASK_CHIPS.json's OPEN chips and update /
        withdraw / re-point every task whose premise the migration
        changed (git-wedge machinery chips, hook-gating chips,
        commit-race chips, and any chip whose prompt hardcodes the
        pre-cutover write path). User-directed 2026-08-28; do it as its
        own session with a claim on TASK_CHIPS.json.
        (h) FRICTION-REDUCTION PROPOSAL -- a consolidated
        github-process-friction proposal (what PHASE-4 absorbs, what
        CLAUDE.md/hook machinery it retires, what stays) was requested by
        the user 2026-08-28 and is delivered in the takeover session's
        report; PHASE-3/PHASE-4 nodes are its plan-side anchors.

        INGEST AUTHORITY (3-WAY MERGE) + REMAINING VERB MIRRORS: BUILT,
        DEPLOYED AND LIVE-VERIFIED 2026-08-28 (session
        coordinator-ingest-clobber-fix-20260828, the takeover handoff's
        continuation):
        (i) INGEST-CLOBBER FIX (ree-v3 ce50a937b9). The materializer's
        ingest-before-render adopted git unconditionally (upsert_*'s
        PHASE-1 "git wins" semantics), so any DB-side close/resolve on a
        row git still rendered active/open was reverted within one tick
        -- the defect that made every suppressed close hollow. Fixed
        with a 3-way merge against a recorded render base
        (last_rendered_json on task_claims + chip_ledger, written by the
        writer once a render PROVABLY reached git: push succeeded, or
        the file already byte-matched the render). Merge rule:
        git==base -> preserve the DB (the suppressed-mutation case);
        DB==base -> adopt git (the fallback self-healing direction,
        kept); base NULL (pre-migration) or both moved -> terminal
        guard (done / done|withdrawn never downgraded to active/open),
        else adopt git. Auto-migrating (connect() ALTERs), deployed by
        hub `git pull` alone, both ingest callers covered (materializer
        + shadow-sync). 12 new contracts
        (coordinator/test_registry_ingest_authority.py); 150-test
        registry suite green on Mac and hub. LIVE-VERIFIED: canary
        claim ingest-clobber-livecheck-20260828 + chip
        chip-20260828-ingest-clobber-livecheck were opened/recorded
        suppressed, rendered active/open into git, then closed/withdrawn
        DB-side at 15:25Z -- both SURVIVED 2+ write-mode ticks and
        render done/withdrawn on origin/master;
        probe-hollow-ack-20260828 also renders done.
        (j) REGISTRY REPAIR SWEEP: the whole 2026-08-28 interim-protocol
        repair list verified already repaired in the DB (every listed
        claim done, incl. both coordinator-phase2b-takeover rows; all
        listed chips done/withdrawn); renders match, nothing re-applied.
        (k) renew/amend/dedupe COORDINATOR MIRRORS (REE_Working
        c8738b2f: task_claim.py + coordinator_transport.py). Same
        conservative allowlist + degrade-to-git pattern as open/close;
        renew passes the CLI's own new stamp so a mirror-only box
        re-keys identically on both sides; renew's DB re-key now
        TOMBSTONE-CLOSES the old stamp instead of deleting it (a
        deleted key cannot survive ingest -- it would resurrect as the
        active phantom; a done "renewed: ..." row is preserved by the
        merge and ages out of the render in 24h); dedupe is an accepted
        no-op (composite PK; the render collapses file-level
        duplicates). 15 new suppression contracts + a stale-git
        re-ingest tombstone contract.
        (l) chip_ledger SCOPE GATE + RESOLVE FALLBACK (same commit;
        chip chip-20260828-chipledger-coordinator-scope-and-resolve-
        fallback resolved). coordinator_enabled() gains the
        in_scope(ROOT) leg -- without it a re-rooted corpus run posted
        chip-20260809-guard-test into the PRODUCTION DB (withdrawn with
        an explanatory note); cmd_resolve falls back to
        coordinator_transport.fetch_chip() on a local miss (the
        suppressed-record lag window) and refuses up-front when
        suppression is not armed. Both coordinator-branch pin suites
        repaired to supply their own transport config (the machine
        config's scope_root was correctly disarming them).
        KNOWN RESIDUE: a fully-degraded box (no transport at all) doing
        a git-path renew still leaves its old-stamp DB row active until
        the next ingest/render resurrects it into git -- converges as
        boxes arm; the mirrors close it everywhere the transport
        reaches. Follow-ons (f)/(g) plus PHASE-3 shrink and the PHASE-4
        endpoint are chipped:
        chip-20260828-phase3-claudemd-registry-doctrine-shrink,
        chip-20260828-phase4-workspace-state-append-endpoint,
        chip-20260828-mcp-tidy-coordinator-ack,
        chip-20260828-taskchips-endstate-audit.

        DEPLOYED 2026-08-27, shortly after the build landed: the user
        authorised the coordinator restart and the orchestrator session
        (insights-7fd98a) performed it. `ree-coordinator.service` now serves
        the PHASE-2 route table -- `/task_claim/*` and `/chip/*` answer 401
        to an unauthenticated probe rather than 404, which is the correct
        signal that the routes EXIST and are bearer-gated. phase3 writer
        traffic resumed cleanly within seconds, no disruption, same as the
        PHASE-1 restart on 2026-08-27T07:52:01Z.

        So the endpoints are now REACHABLE, not merely landed on origin.
        This does NOT change the cutover status in any way: the client flag
        `TASK_CLAIM_COORDINATION_MODE` still defaults to `git`, so nothing
        in the fleet calls these endpoints, and (a)/(b)/(c) above are all
        still open. A reachable endpoint that no client is configured to
        call is exactly the intended state for this phase -- it means the
        soak and the go-live decision are the only things left gating the
        flip, rather than an undeployed server being a hidden fifth
        prerequisite.

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
    - id: PHASE-4
      title: "Hub-serialised commit intake for the REMAINING coordination files (WORKSPACE_STATE.md, claims.yaml, ledgers): clients submit intents, the hub is the one committer"
      status: in-progress
      severity: high
      last_updated: 2026-09-06
      note: >
        STATUS 2026-09-06: the intake is LIVE for every file it was built
        for so far -- WORKSPACE_STATE.md (workspace_state_suppress_git_write
        on the Mac 2026-08-28, cloud-4/5 2026-09-01; unmaterialized rows 0
        on 2026-09-06), RECOMMENDATION_LOG.jsonl (flag flipped fleet-wide
        2026-09-06, hub DB 132/133 materialized at check time), the three
        IGW ledger files via POST /intent/replace (2026-09-01), and the
        retired heartbeat/status/command git telemetry (runbook R1-R7
        complete 2026-09-06). Not yet started: a claims.yaml intake, if one
        is ever wanted -- the governance cycle still commits claims.yaml
        directly under its pause claim, and nothing here assumes otherwise.
        The record below is the activation and soak history.

        ACTIVATED + SOAKING 2026-08-28T18:26Z: the user authorised the
        coordinator restart; /workspace_state/append and /pending answer 200.
        End-to-end dual-write verified live within minutes: entry_id 1
        (client_git_write=1) POSTed by the canonical append tool, git-appended
        and pushed (REE_Working 986203eefc), and marked materialized by the
        writer's next tick ~60s later. The umbrella shared checkout was also
        reconverged to origin/master in the process (5 stranded
        recommendation: commits content-audited and cherry-picked, 9
        proven-false-negative shas acknowledged via safe_adopt_ref) -- the
        stale canonical scripts/ had been silently keeping the coordinator
        branch inert. Soak evaluation + flag flip:
        chip-20260828-phase4-ws-soak-eval-flag-flip.
        SOAK EVAL RUN 1, 2026-08-28T22:39Z (chip
        chip-20260828-phase4-ws-soak-eval-flag-flip): RE-SCOPED, not flipped.
        Soak window start = first coordinator restart after ree-v3
        7bef34181b landed (commit committer date 18:05:16Z), confirmed via
        `systemctl show ree-coordinator -p ExecMainStartTimestamp` =
        2026-08-28T18:26:17Z. At eval time (22:39Z) the window was only
        ~4h13m old -- well short of section 7's >=3 day windowed-soak
        requirement -- so the flag was NOT flipped; this run is a
        progress-so-far snapshot only, re-run needed no earlier than
        2026-08-31T18:26Z. Progress against the section-7 criteria over the
        partial window: (a) tick coverage 125/126.5 expected ticks (~98.8%)
        on ree-task-claim-chip-git-writer, comfortably >= 0.9; (b) zero
        "GUARD=" lines in the writer journal for the window; (c) zero
        duplicate or missing file-matches among the 19 entries the
        coordinator DB marked materialized (structural check: each DB
        (ts, text) pair found exactly once in origin/master's
        WORKSPACE_STATE.md). ANOMALY FOUND, relevant to (d): entry_id=4
        (ts 2026-08-28T19:28:15Z, DLAPTOP-4.local, the /account-handover
        close note) has sat in `awaiting_client` continuously since
        submission -- still not marked carried/materialized as of this
        eval, ~3h11m later, well past section 7(d)'s 10-minute expectation
        (though short of (e)'s 24h stuck-pending threshold). Root cause
        found on inspection, not yet fully diagnosed: the DB's stored
        `text` for entry_id=4 carries a duplicate leading
        "2026-08-28T19:27:56Z -- " timestamp prefix that is byte-for-byte
        ABSENT from the header actually spliced into origin/master's
        WORKSPACE_STATE.md (file line begins "## 2026-08-28T19:28:15Z --
        /account-handover: switched Claude account..." with no duplicated
        prefix), so the materializer's exact-substring (ts, text) match
        can never find it and it will strand forever, not just past 10
        minutes. append_workspace_state_entry.py's perform_append() calls
        _coordinator_submit() and format_entry() with the identical `text`
        variable in one invocation, so a single call cannot produce this
        divergence -- either two separate append invocations were involved
        for this entry (one whose git-written text differs from what
        reached the coordinator) or the file was touched by another path
        after the POST. This is exactly the DP-4 "stranded awaiting_client
        row from a client that mutates its entry text between POST and git
        write" shape that section 9/DP-4 asserted "the tool has no such
        path" for -- that assumption needs re-checking before the next full
        soak evaluation closes criterion (d); the eventual re-run should
        also confirm whether entry_id=4 ever resolves or needs a manual
        DB-side reap. Nothing else in this run is actionable: TASK_CLAIMS
        arbitration and the /workspace_state/pending endpoint (currently
        n_pending=1, n_awaiting_client=1, matching entry_id=4) were both
        confirmed live and responsive. VERDICT: flag
        workspace_state_suppress_git_write left OFF (absent) in
        ~/.ree_coordinator_client.json on the Mac; not checked on
        ree-cloud-5 since the flip did not proceed. Next eval should re-run
        the full section-7 (a)-(e) checklist over the >=3-day window and
        resolve the entry_id=4 anomaly first.
        FIRST SLICE SHIPPED + DESIGN DOC WRITTEN 2026-08-28 (session
        responsibility-epistemic-hygiene-d6f9d3). The WORKSPACE_STATE.md
        append intake is BUILT, TESTED and DEPLOYED: server ree-v3
        7bef34181b (POST /workspace_state/append + GET
        /workspace_state/pending, workspace_state_entries spool,
        render_workspace_state splice-only materialization in the
        registry writer tick with conservation/size/entry-count guards,
        21 new contracts; full coordinator suite 767 passed on the hub),
        client REE_Working b7da7e54 (coordinator-first branch in
        append_workspace_state_entry.py + append_workspace_state /
        suppress_workspace_state_git_write in coordinator_transport.py --
        a SEPARATE cutover flag from the registry suppression, default
        OFF = dual-write soak; 8 new contracts). Hub writer confirmed
        ticking the new code live ("ws: pending=0 ... committed=False").
        ACTIVATION IS ONE PENDING STEP: the running coordinator daemon
        predates the commit, so the endpoints 404 until the next
        USER-AUTHORISED restart (clients degrade to git on exactly that,
        so nothing is waiting unsafely). The full-scope design the
        withdrawn chip carried is now written:
        evidence/planning/phase4_commit_intake_design.md -- intent model
        (typed appends + one allowlisted CAS verb, no generic
        byte-intake), ree_commit.py client lever with the
        guarantees-moved table, per-file routing table, option C SETTLED
        (queue = typed verbs only, file intents refused), hub-writer
        serialisation (DP-6), scope-gating as hard requirement (DP-10,
        coordinating with the cool-sutherland corpus sweep), windowed
        soak criteria incl. total-ticks clause, decommission payoff
        ledger, 11 design problems, and slice sequencing (next:
        restart -> WS soak -> flag flip -> RECOMMENDATION_LOG append ->
        ree_commit CAS branch for claims.yaml). Resume from that doc's
        section 10.
        Prior (unchanged): USER GO-AHEAD 2026-08-28 (session elated-nobel-914234): build PHASE-4.
        Work began the same hour -- session responsibility-epistemic-hygiene-d6f9d3
        is building the WORKSPACE_STATE append-endpoint slice (TASK_CLAIMS
        17:32Z). A full-scope design-doc chip
        (chip-20260828-phase4-commit-intake-design) was spawned and withdrawn
        minutes later on discovering that live session; the design brief was
        messaged to it directly instead: intent schema + CAS semantics, the
        ree_commit.py coordinator-branch client lever, per-file routing table,
        the experiment-queue option-C decision, hub-writer serialisation,
        transport scope-gating (the 2026-08-28 fixture-leak lesson), windowed
        soak criteria with a total-ticks clause, and the decommission /
        context-burn payoff ledger.
        USER-DIRECTED PRIORITY (2026-08-28): the second half of the
        strategic picture. PHASE-2 moves the two claim/chip registries'
        AUTHORITY to the hub; PHASE-4 generalises the WRITE PATH -- a hub
        commit-intake service where a client POSTs an intent (paths +
        content or structural append + message + base ref for CAS) and
        the hub applies intents ONE AT A TIME onto origin tip, commits,
        pushes. One serialising writer removes the entire concurrent-git
        failure class (pathspec races, ref wedges, rebase locks,
        read-modify-write sweeps) for every file routed through it, not
        just the two registries. Append-shaped files (WORKSPACE_STATE
        entries, RECOMMENDATION_LOG.jsonl, igw ledgers) serialise
        trivially; whole-file editorial files (claims.yaml) use
        CAS-at-the-hub -- a rejected intent returns the current content
        for a fast client rebase, which replaces today's wedge with a
        clean retry. NOT STARTED and deliberately sequenced AFTER the
        PHASE-2 cutover ships: the cutover both proves the hub-writer
        pattern in production and removes 73% of the commit traffic,
        which shrinks PHASE-4's blast radius. Design doc first; section 4
        of this plan ("do not assume the mechanism trivially extends")
        still applies to claims.yaml content semantics -- PHASE-4 moves
        the COMMIT, not the editorial judgement.
        THE PAYOFF THE USER NAMES, recorded so scope stays aimed at it:
        once writes serialise through the hub, the defensive apparatus
        built for concurrent git -- the Concurrency Rules bulk of root
        CLAUDE.md, the commit/ref/push guard hooks, the claim/wedge
        boilerplate in skills and .claude config -- can be retired or
        drastically shrunk (PHASE-3's rewrite, now with a much larger
        surface), directly reducing per-session and per-turn context
        burn.
    - id: PHASE-3
      title: "Harden: monitoring, CLAUDE.md rewrite to reflect the new default, decommission what is safe to decommission"
      status: in-progress
      severity: medium
      last_updated: 2026-09-06
      note: >
        STATUS 2026-09-06: monitoring hardening DONE (C.8 drift-log reader,
        hygiene source 28; C.7 renew ack check; coordinator DB backup timer
        on the hub, R6, daily since 2026-09-01 with a 7-day rotation).
        Decommissioning DONE: the hub runner is retired (D.7, 2026-08-30) and
        the heartbeat-retirement runbook R1-R7 is complete (2026-09-06;
        frozen runner_heartbeats/ runner_status/ runner_commands/ removed
        from REE_assembly master in 6320b7f3fa). THE ONE REMAINING ITEM is
        the doctrine/skill-text shrink for the retired telemetry paths --
        chip-20260901-doctrine-shrink-retired-telemetry, unblocked by R7 and
        still open: CLAUDE.md (umbrella + ree-v3), twelve skills mirrored to
        .agents/skills/, and the retired-mode-only tests, with the
        GOV-HELDOUT-1 check before any standing-rule rewording. When that
        lands, flip this node to done.

        CLAUDE.md REWRITE LANDED 2026-08-28 (REE_Working 7914a203, session
        elated-nobel-914234, chip
        chip-20260828-phase3-claudemd-registry-doctrine-shrink): new
        "coordinator-authoritative (cutover 2026-08-28)" section at the top of
        Concurrency Rules; TASK_CLAIMS/TASK_CHIPS removed from the exposed-files
        list and the shared-files re-read rule; arbitration re-stated as a lock
        on coordinator-mode boxes (best-effort on the git fallback only);
        open/close/dedupe/chip-record semantics conditioned on transport;
        GOV-HELDOUT-1 run on 4 non-degenerate cases, all pass. Fallback doctrine
        retained per this node, only conditioned. Settings-hook audit: the ONLY
        registry-specific client hook (protect_task_claims_hand_edit.py) is
        KEPT -- hand-edits are more wrong post-cutover, not less. Same commit
        also removed the clinical-hours guard entirely (separate, explicit user
        decision 2026-08-28 -- not a PHASE-3 decommission; recorded here because
        it shared the commit). Found + contained live post-cutover defect: a
        plain test_hygiene_routine_tick.py run on a suppression-armed box leaked
        all 21 fixture chips into the production DB (fixtures redirect the chips
        FILE but not the transport); chips withdrawn same hour, test file now
        pins TASK_CLAIM_COORDINATION_MODE=git at import; corpus-wide sweep for
        the same shape chipped. REMAINING for PHASE-3: monitoring hardening,
        skill-text sweep for stale registry-write narration ((f)/(g) in the
        PHASE-2 node), and any further decommissioning -- most of the standing
        doctrine shrink is deliberately deferred to PHASE-4's larger surface.
        Prior (unchanged): Only after PHASE-2 has run in production long enough to trust it.
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

**Status:** PHASE-2a BUILT + DEPLOYED; SOAK RESTARTED ON A FIXED DETECTOR (v0.7, 2026-08-28). **The PHASE-1 soak evidence was invalidated on 2026-08-28**: 64 of 200 ticks had been reporting drift since 2026-08-27T19:03Z, every one a false positive caused by `prune_task_claims_done.py` legitimately removing `done` entries the mirror never deletes. The detector now separates RETIRED (pruned, expected) from ORPHAN (real loss), and the exit criterion is restated as a WINDOWED check because the cumulative counter can never return to zero. See the PHASE-1 node for the measurement and section 10 item 3 for the operative criterion. **PHASE-2a (the coordinator-first transport, DEFAULT OFF) is built, tested and landed** -- 11 mutating endpoints on `ree-v3` `528ce44fc5`, a new `scripts/coordinator_transport.py`, flag-gated branches in `task_claim.py`/`chip_ledger.py`, 110 new tests green, the full 707-test coordinator suite unregressed and all 43 existing `task_claim`/`chip_ledger` umbrella test files green with the flag off. Server on `ree-v3` `origin/main`, client on `REE_Working` `origin/master` (`ed1bcf7869`). The endpoints were DEPLOYED to the running hub on 2026-08-27 (restart authorised by the user) and now answer 401 rather than 404 -- reachable, not merely landed. Nothing in the fleet calls them regardless: `TASK_CLAIM_COORDINATION_MODE` defaults to `git`. See the PHASE-2 frontmatter node and section 10. **PHASE-0 is CLOSED** (all three prerequisites verified live -- see section 6). **PHASE-1 is DEPLOYED and SOAKING, and `ree-coordinator.service` has now been RESTARTED (2026-08-27T07:52:01Z) so `/task_claim/*` and `/chip/*` are LIVE**: the shadow-mirror schema, reconciler and read-only endpoints (landed on `ree-v3` `main` `f385e8bb24`) are installed on the coordinator hub, the shadow-sync timer has been running at its documented 10-minute cadence since 2026-08-26T20:26:52Z, and the restart (session `metaworker-chip-20260827-coordinator-phase1-restart-soak-start`) confirmed zero disruption to the phase3 writer plane and exposed the FULL pre-restart drift history via `GET /task_claim/drift` (`total_ticks: 70, diverged_ticks: 0` at restart time -- nothing was lost by deferring the restart). Soak evidence is now readable live via the API; no more `journalctl` workaround needed (see the PHASE-1 frontmatter node for full detail). No WireGuard mesh change has been made (none was needed, see section 6.1). This doc is the resume primitive across sessions -- read it before touching anything named in the phase table above.

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

**Soak exit criterion -- RESTATED 2026-09-01 (user decision), recorded here
because the wording that used to live in section 10 was unmeetable by
construction, for the second time in this plan's history.** The mirror is
judged over a 24h window of `GET /task_claim/drift?since=<24h-ago>`, and it
PASSES when BOTH hold: (1) **zero PERSISTENT divergence** -- no orphan
identity (a `(session_id, claimed_at)` claim key or a `chip_ref`) appears in
two or more diverged ticks, and no diverged tick reports a content mismatch
(`n_*_new` / `n_*_updated` > 0); (2) `window.total_ticks` is consistent with
the 10-minute cadence (~144/day -- a stalled detector must never read as a
clean soak). Sub-cadence orphans are ingest lag (measured 2026-09-01: orphan
age median 56 s, max 100 s, 26/26 self-healed) and are explicitly NOT a
failure; requiring `diverged_ticks == 0` was requiring that no fleet write
land in any pre-ingest window all day. This criterion is what
`hygiene_routine_tick.py` source 28 now enforces mechanically.

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

#### 5.2.7 PHASE-2b design problems (found 2026-08-28, before writing the writer)

- **D14 -- THE MIRROR IS A SUPERSET OF THE FILE, so the materializer must own RETENTION. A naive DB->JSON dump would resurrect every claim ever pruned.** This is the single most important constraint on PHASE-2b and it is not visible from the schema.

  Measured live on the hub, 2026-08-28: `task_claims` holds **228** rows while `TASK_CLAIMS.json` on `origin/master` holds **63** -- the mirror carries **165 extra**, one for every entry `prune_task_claims_done.py` has ever removed. The reconciler never deletes (correct, and deliberately so), while the file is pruned of `done` entries older than 24h at every `/session-land` close. `chip_ledger` by contrast matches exactly (1967 = 1967), consistent with chips never being deleted (D5) -- so this asymmetry is claims-only.

  A materializer that emits every row would therefore inflate `TASK_CLAIMS.json` by ~3.6x and silently undo every prune ever performed. Nothing in the schema, the endpoint list or section 5.2.4 hints at this; it is only visible by counting.

  **Resolution: apply the retention rule at RENDER time, statelessly** -- emit `status='active'`, plus `status='done'` whose `closed_at` (falling back to `claimed_at`) is within `COORDINATOR_TASK_CLAIM_RETAIN_HOURS` (24, matching the pruner). Verified against live data the same day: that rule keeps **61** of the 228 rows against git's 63, with **0 rule-only** (it never resurrects anything git dropped) and 2 git-only -- both `done` and closed more than 24h ago, i.e. entries git is still carrying only because no session has run the pruner since. The rule is a strict subset of the file, lagging in the SAFE direction.

  Two consequences worth stating before anyone builds this:
  1. **The materializer absorbs `prune_task_claims_done.py`'s job.** Pruning stops being an event a session performs and becomes a property of what gets rendered. That removes the prune commits entirely -- and, note, removes the very writes that produced the D-series false positive fixed on 2026-08-28.
  2. **A stateless rule was preferred over a `pruned_at` column** deliberately: there is no retention state to drift out of sync with the file, and the render is idempotent. The cost is that the boundary moves with the wall clock, so entries age out between ticks and produce a genuine content change. That is a real commit with a real diff, NOT the forced periodic "liveness tick" root `CLAUDE.md` forbids reintroducing -- the distinction being that this one only fires when the rendered content actually differs.

- **D15 -- byte-equality is the acceptance test, and the format forbids shortcuts.** Both files are written as `json.dumps(data, indent=2) + "\n"` with **no `sort_keys`**, so key order is whatever the writing script's in-memory dict had, and row order is append order. The top-level key orders even differ between the two files (`claims, schema_version, stale_after_hours` vs `schema_version, chips`). The materializer must reproduce all of that exactly or its first commit is a whole-file reformat -- which would be indistinguishable from a corruption in review and would collide with every concurrent writer. The lossless `entry_json` column (5.2.1) is what makes this achievable; a field-by-field reconstruction from the typed columns is not sufficient and must not be attempted.

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

**As of 2026-09-06 the cutover is complete for TASK_CLAIMS.json /
TASK_CHIPS.json and every PHASE-4 file built so far.** PHASE-0, PHASE-1 and
PHASE-2 are `done` in the frontmatter above; PHASE-3 and PHASE-4 are
`in-progress` with exactly one open item between them. Read the frontmatter
nodes for the record; this section is only the pointer.

**What is live (verified against the hub, the clients and origin on
2026-09-06):**

- Client suppression armed on the Mac, ree-cloud-4 and ree-cloud-5 for
  claims, chips, WORKSPACE_STATE.md and RECOMMENDATION_LOG.jsonl
  (`~/.ree_coordinator_client.json`); the hub materializer in
  `REGISTRY_WRITER_MODE=write` on a 2-min timer; the shadow-sync drift
  detector on a 10-min timer, now read every hygiene tick (source 28).
- Every suppressed verb verifies its ack before trusting suppression
  (`open`/`close`/`amend`/`dedupe`, and `renew` since 2026-09-06).
- Coordinator DB backed up daily on the hub (7-day rotation); the hub runner
  retired; git heartbeat/status/command telemetry retired and its frozen
  directories removed from REE_assembly master.
- The git fallback path is PERMANENT and byte-identical to the pre-cutover
  behaviour whenever the hub is unreachable (section 5.3). Do not remove it.

**The one open item:** the doctrine/skill-text shrink for the retired
telemetry paths -- `chip-20260901-doctrine-shrink-retired-telemetry`
(umbrella + ree-v3 CLAUDE.md, twelve skills mirrored to `.agents/skills/`,
retired-mode-only tests). It needs the GOV-HELDOUT-1 held-out check before
any standing-rule rewording lands, and it is what flips PHASE-3 to `done`.

**How to check health by hand, if the hygiene tick is not running:**

```bash
curl -s -H "Authorization: Bearer $TOK" \
  "http://10.8.0.1:8787/task_claim/drift?since=<ISO-24h-ago>&limit=200"
```

and apply the section 3 criterion (persistent divergence, content mismatch,
tick coverage). `ref_convergence.py --check` and a `rev-list --left-right
--count origin/<b>...HEAD` per checkout cover the client side.

**What a resuming session must NOT do:** re-derive as open work anything the
frontmatter marks done (the earlier text of this section listed the client
suppression branch and the writer-mode flip as pending for a week after they
went live); flip any client back to `git` mode without a hub-side reason; or
remove the git fallback code path.

Update the frontmatter `nodes` status/note for whichever phase you touch, in the same commit as your actual work, so the next session does not have to re-read this whole document to find out what changed.
