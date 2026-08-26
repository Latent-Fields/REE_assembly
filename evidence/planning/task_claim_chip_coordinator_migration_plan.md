---
closure_plan:
  id: task_claim_chip_coordinator_migration
  generation: process
  title: "TASK_CLAIMS/TASK_CHIPS Coordinator Migration (single-writer cutover)"
  registered: 2026-08-26
  last_updated: 2026-08-26
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
      status: in-progress
      severity: load-bearing
      last_updated: 2026-08-26
      note: >
        STARTED 2026-08-26 (session dazzling-jackson-efb9e9). Established:
        the contention surface is small (only the Mac + ree-cloud-5 write
        TASK_CLAIMS.json/TASK_CHIPS.json today; ree-cloud-1..4 never touch
        them). NOT YET DONE: live verification of ree-cloud-5's WireGuard
        mesh membership (see section 6.1 -- the 2026-06-11 mesh doc predates
        ree-cloud-5's 2026-08-11 discovery, so it is very likely NOT a peer
        yet); the coordinator schema/endpoint spec (section 5.2) is a design
        sketch only, not reviewed against ree-v3/coordinator/schema.sql or
        db.py by someone who will actually implement it; the degrade-path
        (coordinator/mesh unreachable) behavior is specified in section 5.3
        but not yet validated against the Mac's documented WireGuard-flakiness
        history (reference_wireguard_mesh memory).
    - id: PHASE-1
      title: "Shadow: coordinator mirrors TASK_CLAIMS/TASK_CHIPS state read-only; git stays authoritative"
      status: not-started
      severity: high
      last_updated: 2026-08-26
      note: >
        Mirrors ree-v3 sync_daemon.py's own PHASE 1 (shadow) design: read-only
        reconciliation against git-authoritative state, no write path, "no
        autostash, no rebase -- structurally incapable of the failure class
        this whole migration exists to remove" (quoting sync_daemon.py's own
        docstring on itself). Exit criterion: N days of the coordinator's
        mirrored claim/chip state matching git HEAD with zero drift.
    - id: PHASE-2
      title: "Claim-authority cutover: task_claim.py/chip_ledger.py call the coordinator; git becomes state-change materialization"
      status: not-started
      severity: high
      last_updated: 2026-08-26
      note: >
        Mirrors ree-v3's SYNC_MODE=coordinator (claim cutover): the DB becomes
        the claim/chip authority; git remains the transport/audit trail, one
        writer thread committing on state-change only (mirrors
        phase3_heartbeat_writer's commit-on-state-change discipline, NOT the
        retired 30-min liveness tick -- see root CLAUDE.md's explicit warning
        against reintroducing that). The existing git-mutate-and-commit path
        in task_claim.py/chip_ledger.py becomes the FALLBACK mode for when the
        coordinator/mesh is unreachable, not the default.
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

**Status:** DESIGN STAGE (v0.1, 2026-08-26). PHASE-0 started; nothing landed yet. No code has been written, no coordinator schema change made, no WireGuard mesh change made. This doc is the resume primitive across sessions -- read it before touching anything named in the phase table above.

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

## 5. Architecture design (sketch -- needs implementation-level review before Phase 1 starts)

### 5.1 Who writes today (the actual contention surface)

Only two real git clients write `TASK_CLAIMS.json`/`TASK_CHIPS.json` today: the Mac (interactive sessions + worktrees) and `ree-cloud-5` (the metaworker dispatcher, ~123 worktrees per `reference_cloud_workers` memory). `ree-cloud-1..4` never touch these files -- they are experiment-only runners mediated entirely by the coordinator already. This is good news for feasibility: the write-side fan-in is small.

### 5.2 Schema + endpoint shape (draft -- not reviewed against `schema.sql`/`db.py` yet)

- New tables mirroring the JSON entry shapes byte-for-byte, so materialization back to `TASK_CLAIMS.json`/`TASK_CHIPS.json` stays compatible with every existing consumer (`audit_stale_claims.py`, `prune_task_claims_done.py`, `chip_ledger.py list`, `serve.py`'s `/workset` panel, the IGW ledger, the `spawn_task` first-action instruction, `/session-land`'s self-report check).
- Endpoints mirroring the CLI verbs 1:1, so `task_claim.py`/`chip_ledger.py` become thin HTTP clients with the exact same command surface: `/claim/open`, `/claim/close`, `/claim/check`, `/claim/renew`, `/claim/amend`, `/claim/dedupe`; `/chip/record`, `/chip/claim`, `/chip/unclaim`, `/chip/resolve`, `/chip/attach`, `/chip/amend-prompt`, `/chip/list`, `/chip/archive`.
- Materialization: one writer thread per file (or one shared, keyed by path), committing on state-change only -- explicitly NOT a timer tick (section 2's warning applies here too). Bot-authored by default, same as `task_claim.py`'s current `--bot` default, so clinical-hours stays clean without any new logic.

### 5.3 Fallback / degrade path (must be first-class, not an afterthought)

When the coordinator or the WireGuard mesh is unreachable, `task_claim.py`/`chip_ledger.py` fall back to **today's existing local git-mutate-and-commit path**, unchanged. This is not new code to write -- it is the *current* implementation, kept exactly as-is and demoted to a fallback branch. This matters for a specific, documented reason (section 6.2): the Mac's WireGuard tunnel has a real flakiness history (stale-handshake blackouts, `reference_wireguard_mesh` memory), and today that does not matter for claims/chips because the Mac talks to GitHub directly. Once the coordinator is authoritative, the Mac's own session productivity becomes dependent on that tunnel being up -- so "coordinator unreachable" must be a well-exercised path from day one, not a rare edge case discovered later.

## 6. Prerequisites (PHASE-0 -- must close before Phase 1 starts)

### 6.1 WireGuard mesh coverage for `ree-cloud-5`

The mesh, as last documented (`reference_wireguard_mesh` memory, 2026-06-11), has four peers: the hub (`10.8.0.1`), the Mac's GUI tunnel (`10.8.0.11`), and cloud workers 2/3/4 (`10.8.0.12/13/14`). **`ree-cloud-5` was discovered on 2026-08-11 -- after that mesh documentation -- and is not a confirmed peer.** Given `ree-cloud-5` is one of exactly two machines that write these files today (section 5.1), this is a hard prerequisite, not a nice-to-have. Verify live with `sudo wg show` on the hub before assuming either way; adding a peer is documented as a single non-disruptive command (`sudo wg set wg0 peer <pub> allowed-ips 10.8.0.X/32` + append a `[Peer]` block to `wg0.conf`, no interface restart).

### 6.2 Mac WireGuard tunnel reliability audit

The Mac's tunnel has a documented history of "Connected but not routing" blackouts, mitigated by a `PersistentKeepalive` fix + a launchd watchdog (`com.ree.wgwatchdog`) + a daily health digest (`com.ree.wghealthdigest`) -- all detailed in `reference_wireguard_mesh` memory. Before Phase 2 makes the Mac's claim/chip traffic depend on this tunnel, confirm the watchdog is still installed and the health digest still reads `bounces_24h=0` (keepalive holding). If it is not, fix that first -- it is a precondition for the whole migration, not a Phase-2-time surprise.

### 6.3 Schema/endpoint review

Section 5.2 is a sketch written without reading `ree-v3/coordinator/schema.sql` or `db.py` in implementation-level detail. Before writing any code, a session should read both, confirm the `try_claim`-style atomic-transaction pattern generalizes cleanly to a claim/chip shape (vs. the experiment-claim shape it was built for), and update this section with the actual table/endpoint design.

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

Read section 6 first (Prerequisites) -- nothing past PHASE-0 should start until 6.1 and 6.2 are closed with a live-verified answer (not carried forward from a stale memory doc, per root `CLAUDE.md`'s memory-freshness discipline). Then read section 5.3 (schema/endpoint review) before writing any coordinator code. Update the frontmatter `nodes` status/note for whichever phase you touch, in the same commit as your actual work, so the next session does not have to re-read this whole document to find out what changed.
