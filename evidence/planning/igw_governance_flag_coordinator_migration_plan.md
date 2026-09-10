closure_plan:
  id: igw_governance_flag_coordinator_migration
  generation: process
  title: "IGW ledger / IGW workset / governance-flag: coordinator migration (design only)"
  registered: 2026-09-10
  last_updated: 2026-09-10
  owner: machinery
  status: design-only -- NOTHING IN THIS DOCUMENT HAS BEEN BUILT BY THIS SESSION
  summary: >
    Move the three highest-volume Mac-local git writers in REE_assembly
    (igw-ledger 793/30d, governance-flag 266/30d, igw-workset 226/30d)
    off per-machine git commits and behind the Phase 3 coordinator, so
    that the coordinator ack IS the durable write and GitHub becomes the
    materialization/fallback path, not the live check every session reads.
    Answers the measured diagnosis in
    scratchpad/divergence_diagnosis.md (35.5% of observations diverged,
    ~4.1 episodes/day, ~0.7 multi-hour wedges/day, 25.4% of wall-clock
    ahead of origin, ~45 orphans/hour once wedged).
    generation: process -> infra/tooling lane; owns no scientific claims,
    segmented out of the V3 closure %.
  scope_claims: []
  sibling_plans:
    - REE_assembly/evidence/planning/task_claim_chip_coordinator_migration_plan.md   # PRECEDENT / parent
    - REE_assembly/evidence/planning/phase4_commit_intake_design.md                  # the intake mechanism this reuses

# =========================================================================== #
# 0. THE HEADLINE FINDING, BEFORE ANY DESIGN                                  #
# =========================================================================== #
#
# TWO OF THE THREE WRITERS ARE ALREADY MIGRATED. The precedent plan's PHASE-4
# node already built, deployed and activated the exact mechanism for them:
#
#   * /Users/dgolden/REE_Working/scripts/igw_routine_tick.py:576 `_CAS_ROUTED_PATHS`
#     already routes igw_routine_ledger.json, igw_assignments.json,
#     inter_governance_workset.v1.json, inter_governance_workset.md and
#     experiment_proposals.v1.json through POST /intent/replace.
#   * /Users/dgolden/REE_Working/ree-v3/coordinator/git_intent.py:113 `ROUTING`
#     carries the identical server-side allowlist.
#   * /Users/dgolden/REE_Working/scripts/coordinator_transport.py:899-954 already
#     exposes the four per-file suppress predicates
#     (suppress_igw_ledger_git_write / _assignments_ / _workset_ / _proposals_)
#     and :863 suppress_igw_log_git_write for the append route.
#   * igw_routine_log.md has its OWN append-shaped route -- POST /igw_log/append
#     (ree-v3/coordinator/app.py:533, db.py:2197 submit_igw_log_entry) -- because
#     it is append-only and must never be rendered from a DB dump.
#   * The hub-side clone + env var were the missing piece; ACTIVATED
#     2026-09-07T08:43:57Z per the precedent plan's PHASE-4 node.
#
# So for igw-ledger and igw-workset this is NOT a build. It is a SOAK
# EVALUATION AND A FIVE-LINE CONFIG EDIT, and the soak window's own stated
# evaluation date is TODAY: "evaluate against section 7 no earlier than
# 2026-09-10T08:44Z, then flip the three suppress predicates
# (chip-20260907-igw-intent-soak-eval-flag-flip)."
#
# Measured confirmation that the dual-write soak is already working, from
# `git log` on REE_assembly (Mac-authored, per day):
#
#   igw-workset local commits/day, Mac:
#     08-11..09-07: 5, 8, 5, 20, 10, ... (5-20/day, mean ~7.5)
#     09-08: 0    09-09: 0    09-10: 1
#
#   igw-ledger local commits/day, Mac:
#     09-07: 41   09-08: 19   09-09: 24   09-10: 9   (UNCHANGED in shape)
#
# The workset collapsed to ~zero the day after activation, because its
# commit path has a materiality gate against HEAD (`_head_blob`) and the hub
# now lands the identical content first, so the client has nothing to commit.
# The ledger did not collapse, because the tick rewrites it with a fresh
# timestamp every run and therefore always differs from HEAD. That asymmetry
# is the single most useful measurement in this document: it says the intake
# WORKS end to end, and it says the remaining igw-ledger traffic is removed
# only by arming the suppress flag, not by the intake existing.
#
# GROUND TRUTH, read 2026-09-10, ~/.ree_coordinator_client.json on the Mac:
#     mode=coordinator, url=http://10.8.0.1:8787, scope_root=/Users/dgolden/REE_Working
#     suppress_git_write: true                        (registries -- PHASE-2, armed)
#     workspace_state_suppress_git_write: true        (PHASE-4 WS, armed)
#     recommendation_log_suppress_git_write: true     (PHASE-4 RECLOG, armed)
#     -- NO igw_ledger_/igw_assignments_/igw_workset_/igw_proposals_/igw_log_
#        suppress key is present. All five default false. This is the dual-write
#        soak state, exactly as the PHASE-4 node says.
#
# governance-flag is the ONLY one of the three that is a genuine build. It has
# ZERO coordinator wiring: `grep -n "coordinator\|intent" scripts/governance_flag.py`
# returns nothing.

# =========================================================================== #
# 1. PER-WRITER ANALYSIS (what it writes, rate, readers, read-path verdict)    #
# =========================================================================== #

## 1.1 igw-ledger -- scripts/igw_routine_tick.py

  WRITES (three files, one nominal commit, already split into two by DP-3):
    CAS-routed subset (igw_routine_tick.py:892 `cas_rel`):
      REE_assembly/evidence/planning/igw_routine_ledger.json   361 KB
      REE_assembly/evidence/planning/igw_assignments.json      394 KB
    Append-routed subset (`log_rel`):
      REE_assembly/evidence/planning/igw_routine_log.md        797 KB, APPEND-ONLY

  RATE: 793 Mac commits/30d (~26/day), plus 89 from the Hub against the same
  files. Recent: 41/19/24/9 on 09-07..09-10. Bursty around ticks; a `igw-log:`
  prefix appears separately when the DP-3 split fires.

  READERS (all read the git working tree; none read the coordinator):
    scripts/audit_stale_claims.py, scripts/dispatch_preexit_check.py,
    scripts/index_lock_watch.sh, scripts/igw_routine_tick.py itself,
    the metaworker-dispatch and inter-governance-brief skills.

  DOES THE READ PATH NEED TO MOVE? **No.** The materializer renders into the
  same git paths on the same cadence; every reader keeps working unchanged.
  This is the precedent's own shape (TASK_CLAIMS.json is still a git file that
  everything reads; only the WRITE moved). ONE consequence must be enforced:
  after the flip these three files join TASK_CLAIMS/TASK_CHIPS in the
  "never hand-edit, anywhere" class, because the next render overwrites a
  git-side edit. The precedent enforces that with a blocking PreToolUse hook
  (scripts/protect_task_claims_hand_edit.py); this design extends that hook's
  path list rather than adding a second hook.

  SUITABILITY VERDICT: **GOOD, and already 90% done.** Pure coordination
  bookkeeping, machine-regenerated, no editorial judgement, 17% twin rate.
  Remaining work is evaluation + config, not code.

  CAVEAT THAT MUST NOT BE LOST: igw_routine_log.md is NOT part of the CAS
  route and must not be. See 1.4.

## 1.2 igw-workset -- the inter-governance workset regen (same script)

  WRITES:
    REE_assembly/evidence/planning/inter_governance_workset.v1.json   479 KB
    REE_assembly/evidence/planning/inter_governance_workset.md        ~297 KB

  RATE: 226 Mac commits/30d, but see 0 above -- ALREADY ~0/day since
  2026-09-07. The Hub writes it too (58/30d), independently, on its own cadence.

  READERS: REE_assembly/serve.py (the /workset panel),
  scripts/igw_routine_tick.py, scripts/audit_stashes.py,
  scripts/check_dispatch_scripts_freshness.py, and two skills.

  DOES THE READ PATH NEED TO MOVE? **No**, same reasoning. serve.py reading a
  hub-materialized file is indistinguishable from serve.py reading a
  Mac-materialized one.

  SUITABILITY VERDICT: **BEST OF THE THREE, by a wide margin.** Not because of
  commit volume (it is the smallest of the three) but because of commit SHAPE.
  A 479 KB whole-file regeneration rewritten 100% per commit
  (measured on 71e6394c30: 1471 insertions / 1471 deletions across 2 files) by
  TWO machines on independent cadences is permanently unprovable by every route
  ref_convergence.py has: no two whole-file regenerations of the same logical
  state share a patch-id (defeats route A), and derived output never carries a
  `-x` backref (defeats route B). Every such commit that reaches the local
  branch is a guaranteed permanent orphan. Migrating it removes an entire
  *class* of unprovable commit, not merely a count of commits. It also collapses
  the two-machine independent-regeneration problem (diagnosis root cause 4) to
  one writer.

  Ranking by commit volume put this third. Ranking by suitability puts it first.

## 1.3 governance-flag -- scripts/governance_flag.py raise / resolve

  WRITES: REE_assembly/evidence/planning/governance_flags.v1.json  683 KB
          (single file; REGISTRY_REL at governance_flag.py:158)

  RATE: 266 Mac commits/30d (~9/day) but HEAVILY BURSTY -- 36 on 09-09 (the
  108-flag governance session), 16 on 09-08, 1 on 09-10. **37.6% twin rate,
  the highest measured of any writer in the repo.**

  READERS: scripts/audit_retest_staleness.py, scripts/governance_flag.py list,
  the /governance skill.

  DOES THE READ PATH NEED TO MOVE? **PARTIALLY -- and this is the one place in
  this design where a read genuinely must move.** `next_flag_id()` mints the
  next GFLAG id **from origin, not the working tree** -- a fix landed 2026-08-14
  after chip-20260814-gflag-stale-id-collision produced two items sharing
  GFLAG-0028 (repaired by hand as REE_assembly c0b00acac2). That read is an
  ID-ALLOCATION read, and under a hub intake it must move to the hub or the
  same collision returns in a new costume (see 1.3.1).

  SUITABILITY VERDICT: **GOOD candidate for migration, BAD candidate for the
  route the other two use.** Stated plainly because the diagnosis ranked by
  commit volume and volume is the wrong axis here:

    * As a CAS /intent/replace path (what igw uses): **BAD.** CAS validates that
      the base you edited from is still current; it does not allocate ids. A
      client that mints GFLAG-0035 from origin, loses the CAS race to another
      client that also minted GFLAG-0035, and retries, re-mints on the new base
      and succeeds -- fine. But a client on a DEGRADED path (hub unreachable)
      mints from origin and commits locally, and the wedge re-appears exactly as
      in 2026-08-14. Worse, the 108-flag burst shape means 108 sequential CAS
      submissions against a 683 KB file, each racing the others, on one session.
      CAS turns a wedge into a rejection storm.
    * As a TYPED-VERB path (what TASK_CLAIMS/TASK_CHIPS use -- the PHASE-2
      pattern): **GOOD, and the correct answer.** `raise` and `resolve` are
      exactly the shape of `open`/`close`: two mutating verbs, server-side
      arbitration, an id the server allocates, a DB row per flag, a materializer
      rendering the file. The 37.6% twin rate is the strongest possible argument
      for moving it; the shape argument says move it to the PHASE-2 lane, not
      the PHASE-4 lane.

  ### 1.3.1 Two properties that MUST survive the migration

    (a) **No amend verb.** governance_flag.py has `raise`, `resolve`, `list`
        and nothing else. Do not add one server-side. The precedent's chip
        surface grew `amend_chip_prompt` / `amend_chip_note` and each one became
        a verb with no suppression allowlist entry, i.e. a permanent
        degraded-path writer. A new verb here would re-open the git path this
        design is closing. If a flag's text is wrong, `resolve --status
        superseded` and raise a new one -- which is the existing discipline.
    (b) **Append-only with supersession-not-deletion.** `foreign_delta()`
        already treats ANY removal from `data["items"]` as having "no innocent
        explanation" and refuses the write (governance_flag.py docstring, ported
        from task_claim.py's 2026-08-10 fix). The server-side db layer must
        carry the same invariant as a hard constraint: no DELETE, ever, on the
        flags table; `resolve` mutates `status`/`resolution_note` in place. And
        the materializer must have NO retention rule. This is the single
        sharpest divergence from the precedent -- see section 5.2.

## 1.4 igw_routine_log.md -- the append-only file, called out separately

  It is not one of the three named writers but it is inside one of them, and it
  is the constraint most likely to be lost.

  EVIDENCE THAT IT IS NOT REGENERABLE: on 2026-09-09 two repair commits landed
  on this checkout -- "igw-log: land the 3 stranded igw-236 log lines" (07:55)
  and "igw-log: recover 16 stranded tick log lines (04:09Z-08:41Z 2026-09-09)"
  (10:02). Nineteen lines had to be recovered by hand because nothing else in
  the system held them. Today's heal confirmed the same thing from the other
  direction: of the twelve ahead-commits, igw_routine_log.md content was the
  only genuinely stranded content.

  DESIGN CONSEQUENCE, non-negotiable: **it keeps its own append-shaped route
  and its own flag.** POST /igw_log/append + `igw_log_entries` spool
  (db.py:2178) + splice-only materialization -- exactly the WORKSPACE_STATE.md
  template, which is splice-only for exactly this reason. It must NEVER be
  added to `_CAS_ROUTED_PATHS` / `git_intent.ROUTING`, because /intent/replace
  submits whole-file content: a client that regenerated the file from a DB view
  and submitted it as a replacement could drop appended lines and the CAS would
  happily accept it (the base matched; the content is just shorter). The
  existing 0.5-fraction shrink guard in git_intent.py:81 would catch a
  catastrophic truncation, not the loss of nineteen lines.

  ADDITIONAL GUARD THIS DESIGN ADDS (see PHASE-1C): a **monotonic line-count
  conservation gate** on the materializer -- a render whose output has fewer
  lines than the file it is replacing, or whose first N lines are not a prefix
  of the previous content, is refused and reported, never committed. This is
  the append-only analogue of D14's retention ownership, and it is what makes
  "a materializer that renders from a DB cannot lose appended lines" a
  mechanical fact rather than a promise.

# =========================================================================== #
# 2. SCHEMA + ENDPOINT SKETCH                                                  #
# =========================================================================== #

## 2.1 igw-ledger + igw-workset -- NOTHING NEW. Reuse verbatim.

  Endpoint:   POST /intent/replace          (ree-v3/coordinator/git_intent.py)
  Body:       {repo, path, base_sha, content, message, session_id, shadow?}
  Verdicts:   applied | noop | cas_stale (returns current content for rebase)
              | not_routed | repo_not_configured | invalid
  Spool:      git_intent_log (id, path, repo, base_sha, verdict, ts, session_id,
              machine, applied_ref)
  Client:     igw_routine_tick.py `_coordinator_submit_cas()` (:687)
  Flags:      igw_ledger_suppress_git_write, igw_assignments_suppress_git_write,
              igw_workset_suppress_git_write, igw_proposals_suppress_git_write

  The ONLY schema change this design proposes for the igw lane is one column,
  and it is for the log route, not the CAS route:

  ALTER TABLE igw_log_entries ADD COLUMN rendered_line_count INTEGER;
      -- the conservation-gate baseline of 1.4 / PHASE-1C. Written by the
      -- materializer once a render provably reached git, the same discipline
      -- as last_rendered_json on task_claims/chip_ledger (precedent (i)).

## 2.2 igw_routine_log.md -- NOTHING NEW either.

  Endpoint:   POST /igw_log/append          (app.py:533)
              GET  /igw_log/pending          (app.py:1107)
  Body:       {line, session_id, client_git_write}
  Table:      igw_log_entries(entry_id, line, session_id, client_git_write,
              submitted_at, materialized_at, ref)   -- db.py:2178
  Client:     igw_routine_tick.py `_coordinator_submit_igw_log()` (:1057)
  Flag:       igw_log_suppress_git_write

## 2.3 governance-flag -- the genuine build, PHASE-2 shaped

  Table (ree-v3/coordinator/db.py), mirroring task_claims/chip_ledger exactly:

    CREATE TABLE governance_flags (
      flag_id        TEXT PRIMARY KEY,        -- 'GFLAG-0035', SERVER-ALLOCATED
      seq            INTEGER NOT NULL,        -- monotonic allocator, UNIQUE
      status         TEXT NOT NULL,           -- open | resolved | superseded
      flag_type      TEXT NOT NULL,
      summary        TEXT NOT NULL,
      claim_ids      TEXT NOT NULL,           -- JSON array
      raised_by_session TEXT,
      raised_at      TEXT NOT NULL,
      resolved_at    TEXT,
      resolution_note TEXT,
      entry_json     TEXT NOT NULL,           -- LOSSLESS, stored VERBATIM (D15)
      last_rendered_json TEXT,                -- 3-way-merge render base
      machine        TEXT, host TEXT          -- D9 attribution split
    );
    -- HARD INVARIANT: no DELETE statement may reference this table. Enforced
    -- by a contract test that greps the module, the negative-control shape the
    -- precedent used for `no archive verb exists` (D7).

  Endpoints (dispatch-table entries in app.py, matching /task_claim/*):

    POST /governance_flag/raise
      body:    {claim_ids[], flag_type, summary, raised_by_session, machine}
      returns: {verdict: ok, flag_id: "GFLAG-0035", entry: {...}}
      NOTE: the id is ALLOCATED SERVER-SIDE inside the same BEGIN IMMEDIATE
      as the insert. This is the fix for chip-20260814-gflag-stale-id-collision
      at its root: no client ever proposes an id, so no two clients can
      propose the same one.
      verdicts: ok | idempotent (same session+summary within the window)

    POST /governance_flag/resolve
      body:    {flag_id, resolution_note, status in (resolved, superseded),
                resolved_by_session}
      returns: {verdict: ok | already_resolved | not_found | ambiguous}
      Mutates in place. Never deletes. `superseded` is a first-class status,
      not a soft delete.

    POST /governance_flag/raise_batch      -- REQUIRED, not optional
      body:    {items: [ ...raise bodies... ]}   (cap ~200)
      returns: {verdict: ok, flag_ids: [...], per_item: [...]}
      WHY: the 09-09 burst was 108 flags from one session. 108 sequential
      single-verb POSTs is 108 arbitration rounds and 108 render ticks' worth
      of churn; one batch is one BEGIN IMMEDIATE and one commit. The precedent
      did not need this because claims arrive one per session; flags do not.
      Same for /governance_flag/resolve_batch (the "resolve 50 flags" and
      "resolve 26 decision-docket flags" commits in today's ahead-range are
      literally this shape).

    GET  /governance_flag/list?status=open   -- read surface for the CLI's
      `list` verb and for audit_retest_staleness.py IF it ever wants the
      fresher view. Not required for cutover: the git file stays readable.

  Materializer: ree-v3/coordinator/governance_flag_git_writer.py, OR (preferred)
    a new render function inside the EXISTING task_claim_chip_git_writer.py tick.
    Preferred, per DP-6: one writer process per repo. Two timers pushing
    REE_assembly would race each other, and REE_assembly already has the phase3
    sync_daemon writers in it. Render rules:
      * from entry_json VERBATIM (D15 byte-equality; a field-by-field rebuild
        from typed columns is NOT sufficient and must not be attempted)
      * `_carry_unmodelled()` equivalent, running BEFORE any field-strip, so
        an unmodelled key added to the file by a future CLI change is not
        silently dropped (the precedent found this bug in its own code:
        `handoff_pending` on 198 of 1920 chips)
      * source-order faithful, ascending `seq`
      * **NO RETENTION. NO PRUNE. NO AGE-OUT.** see 5.2.
      * commit on state-change only

  Client: scripts/governance_flag.py grows `coordinator_raise()` /
    `coordinator_resolve()` behind `enabled() and in_scope(ROOT)` (DP-10),
    per-verb ack allowlists, and a `governance_flag_suppress_git_write` flag.
    `next_flag_id()` becomes DEAD on the coordinator path (the ack carries the
    id) and is RETAINED unchanged for the degraded path.

# =========================================================================== #
# 3. PHASED NODE LIST                                                          #
# =========================================================================== #
  nodes:

    - id: PHASE-0
      title: "Prerequisites: confirm the igw intake is live and healthy; settle the governance_flag schema"
      status: mostly-satisfied-by-precedent
      severity: load-bearing
      last_updated: 2026-09-10
      note: >
        Three of four prerequisites are already discharged by the precedent
        plan's PHASE-4 node and verified read-only by this session:
        (a) WireGuard/mesh coverage for the Mac -- discharged 2026-08-26,
        unchanged; (b) the hub REE_assembly intent clone
        /home/ree/REE_Working_intent_ree_assembly and
        COORDINATOR_INTENT_REPO_REE_ASSEMBLY -- prepared and ACTIVATED
        2026-09-07T08:43:57Z; (c) the client-side route table and all five
        suppress predicates -- landed 2026-09-01.
        NOT discharged: (d) the governance_flag schema/endpoint decision
        above (section 2.3), specifically the typed-verb-not-CAS call, the
        server-side id allocation, the batch verbs and the no-retention rule.
      exit_criterion: >
        A single read-only health probe returns green on all four:
        `GET /igw_log/pending` answers 200; `git_intent_log` shows
        verdict=applied (not repo_not_configured) for all five routed paths
        within the last 24h; ~/.ree_coordinator_client.json parses and its
        scope_root matches the operating root; and section 2.3 is reviewed
        and accepted by the user as the governance_flag shape.
      rollback: >
        None required -- this node changes nothing. If (d) is rejected,
        PHASE-2* do not start; PHASE-1* are independent and proceed anyway.

    - id: PHASE-1A
      title: "Soak evaluation of the igw dual-write window (2026-09-07T08:44Z -> now)"
      status: DUE NOW -- the stated evaluation date is 2026-09-10T08:44Z
      severity: high
      last_updated: 2026-09-10
      note: >
        The precedent's PHASE-4 node registers this as
        chip-20260907-igw-intent-soak-eval-flag-flip and names section 7 of
        phase4_commit_intake_design.md as the criteria. Apply the CAS analogue:
        "zero shadow intents whose CAS verdict disagreed with what git actually
        received", plus the windowed total-ticks clause -- the PHASE-1 detector
        incident is the standing cautionary tale that a stalled timer must never
        read as a clean soak.
        Independent corroborating evidence this session already measured:
        Mac igw-workset local commits went 5-20/day for the four weeks before
        activation, then 0 / 0 / 1 on 09-08 / 09-09 / 09-10. That is the intake
        landing content first and the client's materiality gate correctly
        no-opping. It is a strong positive signal and it is NOT a substitute for
        the section-7 checklist.
      exit_criterion: >
        Over a window >= 3 days ending no earlier than 2026-09-10T08:44Z:
        (a) materializer ticks observed >= 0.9 * expected at the 2-min cadence;
        (b) zero guard fires in the writer journal;
        (c) for every git_intent_log row with verdict=applied on the five routed
            paths, origin/master's content at applied_ref byte-matches the
            submitted content;
        (d) zero rows with verdict=repo_not_configured since 08:43:57Z
            (this is the specific 2026-09-07 regression -- 218 silent failures);
        (e) zero igw_log_entries rows pending > 24h, AND the count of
            igw_routine_log.md lines on origin is monotonically non-decreasing
            across the window.
      rollback: >
        N/A (read-only evaluation). A failed criterion does not roll anything
        back; it blocks PHASE-1B and re-opens the chip with the failing letter.

    - id: PHASE-1B
      title: "Flag flip: arm the three CAS suppress predicates for ledger, assignments, workset"
      status: not-started (gated on PHASE-1A)
      severity: high
      last_updated: 2026-09-10
      note: >
        Add to ~/.ree_coordinator_client.json on the Mac ONLY (the Hub keeps
        writing directly; it is the materializer's own box and its writes are
        not the source of this checkout's divergence):
          "igw_ledger_suppress_git_write": true,
          "igw_assignments_suppress_git_write": true,
          "igw_workset_suppress_git_write": true
        Do NOT arm igw_proposals_suppress_git_write in this node -- 2 commits in
        the window is too little traffic to have soaked anything. Give it its
        own node later or leave it dual-writing indefinitely; it costs nothing.
        Do NOT arm igw_log_suppress_git_write here. That is PHASE-1C and it is
        separate on purpose.
        One flag at a time, per the precedent's rollout rule, with >= 6h between
        each -- ledger first (highest volume, clearest signal), assignments
        second, workset third (it is already effectively silent, so it proves
        the least).
      exit_criterion: >
        48h after the third flag: zero Mac-authored `igw-ledger:` or
        `igw-workset:` commits in REE_assembly's local reflog; every ledger and
        assignments state change visible on origin/master within 2 render ticks
        of the tick that produced it; the tick prints
        "coordinator-acknowledged (commit <sha>); git write suppressed" for
        every routed path; and `ref_convergence.py --audit` no longer lists any
        igw-prefixed commit in the ahead-range.
      rollback: >
        Remove the key(s) from ~/.ree_coordinator_client.json. That is the whole
        procedure. The git path is TODAY'S CODE, permanently retained (parent
        plan 5.3 / DP-2), not new code, and it is exercised on every degraded
        call, so the rollback target is continuously proven. Recovery of
        anything the hub holds but git does not: the next tick after the
        rollback rewrites the files from live state and commits them normally.

    - id: PHASE-1C
      title: "igw_routine_log.md: append-only conservation gate, THEN arm igw_log_suppress_git_write"
      status: not-started (gated on PHASE-1B + one new server-side guard)
      severity: load-bearing
      last_updated: 2026-09-10
      note: >
        Sequenced last and alone because this is the one file in the igw lane
        whose content is not regenerable. Nineteen lines had to be hand-recovered
        on 2026-09-09 ("igw-log: land the 3 stranded igw-236 log lines",
        "igw-log: recover 16 stranded tick log lines"). Before the flag is armed,
        the materializer gains the conservation gate of section 1.4:
          * splice-only append; the renderer NEVER emits a whole-file body
          * refuse-and-report if the rendered output's line count is lower than
            the previous rendered line count (rendered_line_count column, 2.1)
          * refuse-and-report if the previous content is not a strict PREFIX of
            the new content
          * on refusal: no commit, loud journal line, and the pending rows stay
            pending (they are never marked materialized on a refused render)
        Contract tests required before the flip, mirroring the precedent's
        13-contract materializer suite: round-trip byte-equality, a render that
        would drop a line is REFUSED not committed, a concurrent git-path append
        during the flip window survives, trailing-newline tolerance.
      exit_criterion: >
        72h after arming: `git log --follow` on igw_routine_log.md shows the
        line count monotonically non-decreasing at every commit; zero refusals
        in the writer journal; zero igw_log_entries rows pending > 10 min;
        and a deliberate negative-control probe (submit a render that drops a
        line, in check mode) is REFUSED.
      rollback: >
        Remove igw_log_suppress_git_write. Then, because this file is
        append-only and the hub's spool may hold lines git does not:
        `GET /igw_log/pending`, take every row with materialized_at IS NULL,
        and append them to the file in submitted_at order via the ordinary
        append path, one commit, message "igw-log: recover N rows from the
        coordinator spool after rollback". This procedure is the same one the
        2026-09-09 hand-recovery performed, and it is why /igw_log/pending
        exists.

    - id: PHASE-2A
      title: "governance_flag: shadow -- coordinator mirrors the flag registry read-only; git stays authoritative"
      status: not-started (gated on PHASE-0(d))
      severity: high
      last_updated: 2026-09-10
      note: >
        Mirror the precedent's PHASE-1 exactly. Build governance_flags table +
        an ingest that upserts from origin's governance_flags.v1.json on the
        existing writer tick, plus GET /governance_flag/drift. NO mutating
        route exists in this node, and a contract test PINS that -- the
        precedent wrote that pin deliberately so that adding the routes later
        would be a reviewed inversion of a test rather than a quiet addition,
        and it worked.
        The CLI is untouched in this node. Nothing in the fleet calls anything.
      exit_criterion: >
        GET /governance_flag/drift reports diverged_ticks=0 over a window
        >= 3 days with tick coverage >= 0.9 * expected; the DB's item count and
        every item's flag_id/status match origin's file exactly at every tick;
        the "no mutating route exists" pin is green.
      rollback: >
        Stop and disable the ingest leg. Nothing else reads it. Zero client
        impact -- no client is configured to call anything in this node.

    - id: PHASE-2B
      title: "governance_flag: mutating verbs + server-side id allocation + materializer, all default-OFF"
      status: not-started
      severity: high
      last_updated: 2026-09-10
      note: >
        Build /governance_flag/raise, /resolve, /raise_batch, /resolve_batch,
        each taking BEGIN IMMEDIATE BEFORE its guard SELECT (the same primitive
        try_claim uses). Build the render into the EXISTING
        task_claim_chip_git_writer.py tick (DP-6: one writer process per repo).
        Deploy the materializer in REGISTRY_WRITER_MODE=check first -- renders,
        byte-compares against origin, reports, never writes. That check-mode
        soak is the deployment soak; it is what caught the precedent's key
        problems before they could write anything.
        Client branch lands DEFAULT OFF behind
        `enabled() and in_scope(ROOT)`; with the flag on but suppression off,
        the client asks the coordinator AND STILL WRITES GIT. State that plainly
        here because it is the thing a later session is most likely to
        misremember: what moves in this node is the ID ALLOCATION AND
        ARBITRATION, not the storage.
        The local file-based checks (foreign_delta, the removal refusal,
        next_flag_id) are NOT removed, weakened or skipped. They run first,
        unchanged. A check that can only ADD refusals cannot regress today's
        behaviour.
      exit_criterion: >
        Check-mode soak >= 3 days with byte-equality on every tick (a first
        commit that is a whole-file reformat is a FAILURE, not a cosmetic
        issue -- D15); full contract suite green including the no-DELETE
        negative control and an unmodelled-key round-trip; a live canary flag
        raised through the endpoint renders correctly and is never resurrected
        or downgraded across >= 2 ticks.
      rollback: >
        Set the client mode flag off (it defaults off; this is the no-op case)
        and set REGISTRY_WRITER_MODE=check on the writer. The render stops
        writing within one tick. No file state to unwind -- check mode never
        wrote.

    - id: PHASE-2C
      title: "governance_flag cutover: arm governance_flag_suppress_git_write on the Mac"
      status: not-started
      severity: high
      last_updated: 2026-09-10
      note: >
        Per-verb ack allowlist, degrading byte-identically to the git path on
        EVERY other outcome (transport down, HTTP error, ambiguous, not_found,
        409). Verbs with no mirror are never suppressed -- and there are none to
        add, because this design deliberately ships no amend verb (1.3.1a).
        Requires a separate human go-live confirmation, per the precedent.
        Simultaneously: extend scripts/protect_task_claims_hand_edit.py's path
        list to cover governance_flags.v1.json and the three igw files, so a
        hand edit is blocked rather than silently overwritten by the next render.
      exit_criterion: >
        7 days: zero Mac-authored `governance-flag:` commits; every raise/resolve
        prints "coordinator-acknowledged; git write suppressed"; zero duplicate
        flag_ids in the rendered file (the 2026-08-14 failure mode, now
        structurally impossible); a full governance cycle's flag burst
        (>= 20 flags) lands through raise_batch in one render tick.
      rollback: >
        Remove governance_flag_suppress_git_write. The CLI's own git path,
        including next_flag_id()'s origin-mint, is retained unchanged and
        resumes on the next call. If the DB holds flags git does not: the
        materializer's next write-mode tick renders them; if the writer is also
        being rolled back, dump the DB rows to the file via a one-shot render
        and land it with ree_commit.py.

    - id: PHASE-3
      title: "Retention, monitoring, decommission, and residual measurement"
      status: not-started
      severity: medium
      last_updated: 2026-09-10
      note: >
        (a) RETENTION: state the per-file rule EXPLICITLY, once, here, because
        getting it wrong is how the precedent's D14 nearly inflated
        TASK_CLAIMS.json 3.6x:
            igw_routine_ledger.json / igw_assignments.json -- render exactly what
              the tick's CAS content said. No render-side retention; the tick
              already owns pruning and this design does not take that ownership.
            inter_governance_workset.v1.json / .md -- same.
            igw_routine_log.md -- APPEND-ONLY, no retention, ever, conservation
              gate as PHASE-1C.
            governance_flags.v1.json -- APPEND-ONLY, supersession not deletion.
              NO RETENTION RULE AT ALL. Explicitly NOT the precedent's D14
              done>24h age-out. See 5.2.
        (b) MONITORING: extend the existing drift-log reader rather than adding
        a second monitor; add the git_intent_log verdict histogram to the
        morning digest (the 2026-09-07 lesson: 218 consecutive HTTP 500s were
        invisible for five days because nobody was reading the verdict).
        (c) DECOMMISSION: per the precedent's payoff-ledger discipline -- shrink,
        never delete. The `evidence/planning/` exposed-files rows and the
        igw-ledger read-modify-write caveat in CLAUDE.md's Concurrency Rules
        compress to a fallback appendix. `ref_convergence.py` /
        `safe_adopt_ref.py` STAY -- local refs still exist, they just fire far
        less often.
        (d) RESIDUAL MEASUREMENT: re-run the diagnosis's episode analysis over a
        14-day post-cutover window and publish the actual numbers against
        section 7's predictions. If the prediction is wrong, this node says so.
      exit_criterion: >
        A 14-day post-cutover measurement published as an addendum to
        scratchpad/divergence_diagnosis.md's methodology, reporting observed
        divergence share, episode rate, wedge rate and time-ahead, compared
        against the predicted ~15-18%, ~2/day, ~0.35/day, ~12-15%.
      rollback: >
        N/A -- monitoring and documentation. A decommission step that turns out
        premature is reverted by restoring the CLAUDE.md section from git, which
        is why the rule is "shrink to a fallback appendix", not "delete".

# =========================================================================== #
# 4. THE DEGRADE PATH, PER WRITER, CONCRETELY                                  #
# =========================================================================== #

The rule, stated once in the precedent's own words and unchanged here:
**the coordinator ack IS the durable write, with GitHub as the materialization
/ fallback path.** A box with no ~/.ree_coordinator_client.json, an unreachable
hub, or a verb with no coordinator mirror takes the degraded git path -- local
write + commit + push, bot-authored, pushes by default -- and it does so
LOUDLY.

  igw ledger / assignments / workset:
    Trigger: coordinator_transport.enabled() false, in_scope() false, socket
    error, HTTP != 200, verdict in {not_routed, repo_not_configured, invalid},
    or CAS stale after the client's one rebase attempt.
    Behaviour: `_coordinator_submit_cas()` returns 'degraded'; the tick's
    existing `_ree_commit(...)` runs exactly as it does today.
    Loudness: the transport already prints the SERVER VERDICT, not just
    "returned HTTP 500" -- that fix landed 2026-09-07 precisely because the
    generic message hid 218 failures for five days. The tick line must name the
    file and say "git path -- this checkout can now orphan".
    DP-3 preserved: the CAS subset and the log subset are committed by two
    separate _ree_commit calls, never one, so a mixed outcome never produces
    one commit with two durability stories.

  igw_routine_log.md:
    Trigger: same set, plus a refused conservation gate.
    Behaviour: `_coordinator_submit_igw_log()` returns non-'suppressed'; the
    line is appended locally and committed with the `igw-log:` prefix.
    Loudness: same. AND: because this file is the one that strands, the degrade
    line must additionally print the pending count from /igw_log/pending when
    reachable, so an operator can see the backlog forming rather than discover
    it three days later as sixteen missing lines.
    Note the asymmetry that makes this safe: on the append route, degrading
    produces a DUPLICATE line at worst (dedup is the exact-substring presence
    check, DP-4), never a LOST one. Duplicates are recoverable; losses are not.
    Bias every ambiguous case toward the duplicate.

  governance-flag:
    Trigger: same set, plus verdicts {not_found, ambiguous, already_resolved}
    on resolve.
    Behaviour: `next_flag_id()` mints from origin as it does today,
    `mutate_and_commit()` runs with foreign_delta + the removal refusal intact,
    ree_commit.py commits and pushes.
    Loudness: the degrade line must name the SPECIFIC re-exposed hazard, per
    DP-2 -- "degraded: flag id minted locally from origin; a concurrent raise on
    another box can collide (chip-20260814-gflag-stale-id-collision)". That is
    a real, previously-confirmed hazard and a session that is back in the old
    world deserves to be told which old world it is in.
    Explicitly NOT degraded-suppressed: there is no amend verb to worry about,
    and `resolve --status superseded` degrades identically to `resolve
    --status resolved`, so supersession is never lost on the fallback path.

# =========================================================================== #
# 5. WHAT COULD GO WRONG -- drawn from the precedent's own incident record     #
# =========================================================================== #

## 5.1 The hollow-ack regression (precedent PHASE-2 item (i), ree-v3 ce50a937b9)

  WHAT HAPPENED: the materializer's ingest-before-render adopted git
  unconditionally (the PHASE-1 "git wins" upsert semantics carried forward), so
  any DB-side mutation on a row that git still rendered in its OLD state was
  REVERTED within one tick. Every suppressed close was hollow: the client
  printed "coordinator-acknowledged; git write suppressed", the ack was real,
  and the state change evaporated. Fixed with a 3-way merge against a recorded
  render base (last_rendered_json, written only once a render PROVABLY reached
  git: push succeeded, or the file already byte-matched the render), with a
  terminal guard so done/withdrawn is never downgraded.

  HOW THIS DESIGN AVOIDS REPEATING IT:
    (a) The igw CAS route is structurally immune. /intent/replace has no ingest
        leg at all -- the client supplies base_sha and full content, and the hub
        commits onto that base. There is no "adopt git" direction to get wrong.
        This is a real reason to prefer the CAS route where it fits, and it is
        why PHASE-1B carries far less risk than PHASE-2C.
    (b) The igw_log append route is structurally immune for the same reason:
        splice-only, no ingest, no reconciliation.
    (c) governance_flag is NOT immune -- it is the same DB-authoritative,
        ingest-and-render shape as task_claims. So PHASE-2A/2B MUST reuse the
        3-way merge machinery that already exists (last_rendered_json + the
        base-comparison merge rule) rather than writing a second ingest. The
        merge rule transfers unchanged: git==base -> preserve the DB
        (the suppressed-mutation case); DB==base -> adopt git (the fallback
        self-healing direction); base NULL or both moved -> terminal guard
        (resolved/superseded is never downgraded to open), else adopt git.
    (d) PHASE-2C's exit criterion includes a LIVE CANARY that survives >= 2
        ticks, because that is exactly the probe that caught the precedent's
        hollow ack (canary claim ingest-clobber-livecheck-20260828). A cutover
        that only checks "the ack came back 200" is checking the thing that was
        already true when it was broken.

## 5.2 The materializer ownership-boundary move (precedent D14)

  WHAT HAPPENED: the DB mirror is a SUPERSET of the file, because the file had
  been pruned repeatedly and the DB remembered everything. A naive DB->JSON dump
  would have resurrected every claim ever pruned and inflated TASK_CLAIMS.json
  ~3.6x. The precedent's answer was to move retention ownership INTO the
  materializer -- render-time age-out of done>24h -- which absorbed
  prune_task_claims_done.py's job entirely. That was correct there. It was also
  an OWNERSHIP BOUNDARY MOVE performed as a side effect of building a renderer,
  and the plan itself flags it as "the single most important constraint on
  PHASE-2b and it is not visible from the schema".

  HOW THIS DESIGN AVOIDS REPEATING IT: by refusing the move, explicitly, per
  file, in PHASE-3(a), and by making the refusal a contract test rather than a
  paragraph.
    * governance_flags.v1.json is APPEND-ONLY WITH SUPERSESSION-NOT-DELETION.
      It has never been pruned. Its DB mirror will therefore NOT be a superset
      of the file, and there is no retention problem to solve. Do not solve it
      anyway. A `resolved` flag from three months ago is the evidence trail that
      audit_retest_staleness.py walks; ageing it out at render time would delete
      history that no other store holds. Required contract:
      `test_governance_flag_render_has_no_retention` -- render a DB with a flag
      resolved 400 days ago and assert it appears in the output.
    * igw_routine_ledger.json / igw_assignments.json: the TICK owns pruning
      today and keeps owning it. The renderer emits what the CAS content said,
      full stop. A renderer that "helpfully" ages out completed assignments is
      taking ownership of a policy that lives in igw_routine_tick.py, and the
      two will drift.
    * igw_routine_log.md: no retention, ever, plus the PHASE-1C conservation
      gate, which is precisely a mechanical prohibition on the renderer ever
      taking retention ownership by accident.

  THE GENERAL RULE THIS DESIGN ADOPTS: **a materializer renders; it does not
  decide what deserves to exist.** Where a retention policy is genuinely needed,
  it is a separate, named, tested node -- never a property of a render function.

## 5.3 Three more, specific to this migration

  * **The silent-500 shape (2026-09-07).** 218 intents answered
    repo_not_configured for five days and every one degraded to git, silently,
    because the client printed only "returned HTTP 500". Already fixed in the
    transport. This design's PHASE-1A exit criterion (d) tests for exactly this
    verdict, and PHASE-3(b) puts the verdict histogram in the morning digest, so
    the next instance is caught in hours rather than days.
  * **Transport scope leak (DP-10, 2026-08-28).** A plain test run on a
    suppression-armed box leaked 21 fixture chips into the production DB, because
    fixtures redirect the FILE, not the transport. governance_flag.py has a large
    existing test suite (test_governance_flag.py, _foreign_drop, _stale_id,
    _push_default, _atomic_write) that writes real registries. Every one of them
    must be unroutable by construction (isolated config path) BEFORE PHASE-2B
    lands, not after.
  * **The batch verb as a new failure mode.** raise_batch is required (1.3.1 /
    2.3) but a partially-applied batch is worse than no batch: 60 flags in, 48
    refused, and the session cannot tell which. It must be all-or-nothing inside
    one BEGIN IMMEDIATE, returning either every flag_id or a single refusal with
    the offending index. A per-item verdict array is for reporting, not for
    partial success.

# =========================================================================== #
# 6. THE TWO PROHIBITED FIXES -- accepted, with one argued exception           #
# =========================================================================== #

## 6.1 Another local push-retry loop: REJECTED, no reservation.

  The diagnosis is decisive and this design has nothing to add: the pushes
  SUCCEED. 115 successful `update by push` reflog events on 09-09 alone.
  retry_push_via_worktree already retries 3x with a rebase lock and it works --
  it lands the content. What fails is the ref move afterwards, and
  `_converge_after_push` fails OPEN by design because durability is already
  achieved by then. Adding retry attacks a step that is not failing, and each
  retry that lands a twin manufactures one more orphan. No.

## 6.2 Adding inter_governance_workset.v1.json to REGISTRY_SPECS: REJECTED --
##     but here is the argued exception the prohibition should not swallow.

  On the workset itself, rejected without reservation, and for a reason the
  diagnosis does not state: **after PHASE-1B the workset stops being a local
  commit at all.** Route C exists to adjudicate whether a local commit's items
  are contained upstream. A file with zero local commits produces zero such
  questions. A REGISTRY_SPECS entry for it would be dead code within days of
  the flip, while permanently raising MAX_UPSTREAM_SCAN_COMMITS pressure on a
  479 KB file -- against a cap whose own comment warns that an over-long scan
  "MANUFACTURES the divergence it is trying to prove away". Building convergence
  machinery around an artifact whose whole purpose in this plan is to stop
  being a git commit is the definition of against the grain.

  THE EXCEPTION, argued explicitly rather than slipped in:
  **governance_flags.v1.json is a legitimate candidate for a time-boxed
  REGISTRY_SPECS entry, and the argument for it is not the same argument.**
    * The workset is unmigrateable-by-route-C AND about to disappear.
      governance_flags.v1.json is about to disappear too -- but on a MUCH longer
      timeline: PHASE-2A/2B/2C is a real build with two soaks and a go-live
      confirmation, realistically 3-6 weeks, against PHASE-1B's config edit.
      That is 3-6 weeks at ~9 commits/day with a 37.6% twin rate: roughly
      250-550 more commits, of which ~100-200 become orphan twins. This design
      is otherwise asking the checkout to absorb all of them.
    * It is the RIGHT SHAPE for route C in a way the workset is not: a JSON
      registry with an `items` list, each item carrying a stable unique
      `flag_id` -- structurally identical to the TASK_CHIPS.json spec that route
      C was built for (`RegistrySpec("json", "chips", ("chip_ref",))`). The
      analogous spec is `RegistrySpec("json", "items", ("flag_id",))`.
      The file is append-only with no deletion, which is exactly the property
      route C's net-item-containment test needs to be sound: a ref move can only
      be shown to "drop" an item that was genuinely added locally.
    * It is a stopgap, and it must carry its own sunset: the REGISTRY_SPECS
      entry is REMOVED as part of PHASE-2C, in the same commit that arms
      governance_flag_suppress_git_write. Registered as a node condition, not a
      hope.
    * The honest counterargument, stated because it may win: this is still
      building convergence machinery for a file scheduled for removal, it costs
      a scan-budget increase on a 683 KB file, and if PHASE-2 slips the entry
      outlives its box. **Recommendation: do it ONLY if PHASE-2A has not started
      within 7 days of this design being accepted.** If PHASE-2 is moving, the
      stopgap is not worth its own review cost. If PHASE-2 is not moving, 100-200
      avoidable orphans is a real price to pay for tidiness.
  This is a recommendation, not a decision. The prohibition stands unless the
  7-day condition fires.

## 6.3 Two with-the-grain fixes this design does NOT own, but depends on

  Both are from the diagnosis section 7.4, both are cheap, and neither is
  blocked by anything here. This design's residual estimate in section 7
  ASSUMES the first one happens; if it does not, the residual is worse.
    * Make the manual escape hatch use `-x`. Zero backrefs on today's twins
      against a 9.9% baseline is the recurrence engine (root cause 3).
    * Surface the fail-open. ree_ref_convergence_wedge.json recorded 9 refusals
      over 11.5h and nothing read it until the digest degraded.

# =========================================================================== #
# 7. DOES THIS STOP THE ORPHAN GENERATION, OR ONLY REDUCE IT?                  #
# =========================================================================== #

**It reduces it. It does not eliminate it. Concretely: local automated commit
volume on this checkout falls ~77%, but TOTAL local commit volume falls ~52%,
and the residual wedge rate is roughly half of today's -- not zero.**

## 7.1 The 77% figure is true and it is also misleading

  The diagnosis states: 1285 of the Mac's 1660 automated local commits = 77%.
  Correct. But the denominator that matters for divergence is not
  Mac-automated commits, it is ALL commits on this checkout, because every one
  of them is a push attempt that can be non-fast-forwarded:

    local writers, 30d:  Mac automated 1660  +  nooarche interactive 817  = 2477
    migrated by this design:                                                1285
    residual:                                                               1192

    1285 / 1660 = 77%   <- the diagnosis's figure, of the automated subset
    1285 / 2477 = 52%   <- the figure that predicts divergence behaviour

  So: ~83 local commits/day becomes ~40/day. Not ~10/day.

## 7.2 What that does to each measured quantity

  Orphan generation is per-non-fast-forward-push, and origin's advance rate is
  set by Cloud + Hub (~92/day) and is UNCHANGED by this migration -- indeed the
  hub materializer now lands the migrated content there instead, so origin
  advances at least as fast. The probability that any given local push is
  non-fast-forward is therefore roughly unchanged; what falls is the NUMBER of
  local pushes. So each quantity scales with local push rate, ~0.48x:

    | quantity (diagnosis, measured)      | today   | predicted post-cutover |
    |-------------------------------------|---------|------------------------|
    | local commits/day                   | 83      | ~40                    |
    | divergence episodes/day             | 4.1     | ~2.0                   |
    | multi-hour wedges/day               | 0.7     | ~0.35                  |
    | share of observations diverged      | 35.5%   | ~15-18%                |
    | wall-clock ahead                    | 25.4%   | ~12-15%                |
    | in-wedge amplification              | ~45/h   | ~21/h                  |

  The ~45 orphans/hour figure specifically: it is an amplification RATE, one
  orphan per push attempt once wedged, measured on ree-cloud-5. It is not a
  constant of nature -- it is the local push rate during a burst. Halve the push
  rate and you halve the amplification. **A wedge on this box after cutover
  still fills at ~21 orphans/hour. It fills more slowly. It does not stop.**

## 7.3 The residual, named specifically

  Test it against today's actual ahead-range, which is the only fully-decomposed
  sample the diagnosis has (12 commits, 4 unproven). Apply this migration
  retroactively and ask what would still refuse:

    43f6e5713e  igw-workset regen              UNPROVEN -> **REMOVED by PHASE-1B**
    c8116c399b  governance: apply 26 flags     UNPROVEN -> **STILL THERE**
                  blockers: claim_evidence.v1.json, substrate_status_snapshot.json,
                  pending_review.md -- governance REGEN output, prefix `governance:`,
                  NOT one of the three writers, not in scope here
    26708abc22  lit-pull ARC-055/056           UNPROVEN -> **STILL THERE**
                  blockers: claim_evidence.v1.json (a 261-line reordering),
                  INDEX.md ordering -- interactive research content
    853e336bbb  docs: replay-dependent         UNPROVEN -> **STILL THERE**
                  151 genuinely local-only prose lines. MUST stay in git. The
                  converger refusing it is the system working correctly.

  **Migrating all three writers removes exactly ONE of today's four unproven
  commits. The all-or-nothing gate would still refuse today's range.** That is
  the honest headline and it should not be softened: the diagnosis's root cause
  2 -- "one unprovable commit holds the other eleven hostage" -- is NOT fixed by
  this design.

  The three residual sources, in order of size:
    1. **The governance regen plane** (`governance:` prefix, ~74 commits/30d
       across nooarche and automation, writing claim_evidence.v1.json,
       substrate_status_snapshot.json, hypothesis_space_registry.v1.json,
       pending_review.md). These are whole-file regenerated registries -- the
       SAME shape as the workset, the same permanent-unprovability, and they are
       2 of today's 4 blockers. They are the obvious PHASE-4 successor route
       (phase4_commit_intake_design.md section 5 already lists
       hypothesis_space_registry.v1.json and substrate_queue.json in its full
       table, deliberately unrouted). **If the goal is to stop orphan generation
       rather than halve it, this is the next node, and it is not in this plan.**
    2. **The interactive prose plane** (~27 commits/day, nooarche). This MUST
       NOT migrate. It is authored research content; git is the correct store;
       it needs review, history and blame. It is also the class that produced
       today's single TRUE negative. Any design that "eliminates" divergence by
       migrating this is destroying the thing the converger exists to protect.
       This residual is permanent and correct.
    3. **Hand cherry-picks without `-x`** (root cause 3). Not fixed here; fixed
       by 6.3's one-line change. If it is not fixed, every future manual wedge
       escape re-seeds the next wedge and the numbers in 7.2 degrade.

## 7.4 What this design DOES eliminate outright

  Two things, and they are worth having:
    * **The whole-file-regenerated-JSON class disappears from the local commit
      stream for the igw files.** That is the class no convergence route can
      ever prove. Every such commit that reaches the local branch is a permanent
      orphan by construction. Removing it is not a rate reduction; it is
      removing a category. (The governance-regen registries remain in that
      category -- see 7.3.1.)
    * **The two-machine independent-regeneration problem for the workset.** Mac
      and Hub both regenerate a 479 KB derived artifact on independent cadences
      today; after cutover there is one writer. Root cause 4 is closed for these
      files.

## 7.5 The one-sentence answer

  Migrating igw-ledger, igw-workset and governance-flag cuts local commit volume
  ~52%, roughly halves episode rate, wedge rate, time-ahead and in-wedge
  amplification (~45 -> ~21 orphans/hour), and permanently removes one class of
  unprovable commit -- but it removes only one of today's four unproven blockers
  and does not fix the all-or-nothing gate, so **wedges will still form, about
  half as often, and the residual is dominated by the governance regen plane,
  which is the next migration, not this one.**
