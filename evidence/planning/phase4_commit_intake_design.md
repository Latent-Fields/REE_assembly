# PHASE-4 design: hub-serialised commit intake for the remaining coordination files

**Status:** DESIGN (2026-08-28). First slice ALREADY SHIPPED the same day this
doc was written: the WORKSPACE_STATE.md append intake (`ree-v3` `7bef34181b`
server-side, `REE_Working` `b7da7e54` client-side) -- see section 2.2, and
treat that slice as the reference implementation for everything append-shaped
here. Parent plan: `task_claim_chip_coordinator_migration_plan.md` (the
PHASE-4 frontmatter node points here; its sections 4, 5.2.6/5.2.7 D1-D15 and
9 are the conventions this doc follows). Authored by session
`responsibility-epistemic-hygiene-d6f9d3` after the PHASE-4 go-ahead was
relayed from session `elated-nobel-914234` (user-directed, 2026-08-28).

**The payoff this stays aimed at (user-stated):** once writes serialise
through the hub, the defensive apparatus built for concurrent git -- the
Concurrency Rules bulk of root CLAUDE.md, the commit/ref/push guard hooks,
the claim/wedge boilerplate in skills -- can be retired or drastically
shrunk, directly reducing per-session and per-turn context burn. Section 8
is the ledger that makes that payoff concrete and auditable per file.

---

## 1. Problem shape

PHASE-2 moved the two claim/chip registries' AUTHORITY to the hub. Every
other shared coordination file is still written by direct, independent,
per-machine git commits, and therefore still exposed to the whole
Concurrency Rules incident catalogue (pathspec races, HEAD/worktree skew,
ref-move discard, rebase-lock contention, read-modify-write contamination,
silent truncation). One serialising writer per file removes that entire
failure class *for that file* -- the registry cutover has now proven the
pattern in production, and removed ~73% of the commit traffic, which is why
PHASE-4 was sequenced after it.

Two write shapes cover everything left (parent plan PHASE-4 node):

- **Append-shaped**: WORKSPACE_STATE.md entries, RECOMMENDATION_LOG.jsonl,
  igw_routine_log.md. A client submits ONE new item; nothing existing is
  ever edited. These serialise trivially and need no CAS.
- **Whole-file editorial**: claims.yaml, hypothesis_space_registry.v1.json,
  substrate_queue.json, review_tracker.json, igw ledgers. A client submits
  a full replacement produced by real editorial judgement. These need
  CAS-at-the-hub: an intent carries the base ref it was edited from, and a
  rejected intent returns the CURRENT content for a clean client rebase --
  replacing today's push-reject/rebase wedge with a loud, structured retry.

## 2. What exists to build on

### 2.1 Proven machinery (do not reinvent)

- `task_claim_chip_git_writer.py`: the one-git-writer tick (ingest ->
  render -> byte-compare -> commit-on-state-change -> push-retry), the
  `last_rendered_json` 3-way-merge base (ingest-authority fix, `ree-v3`
  `ce50a937b9`), and the dedicated writer clone convention.
- `coordinator_transport.py`: the client transport contract -- never
  raises, every failure degrades to the unchanged git path, per-verb typed
  wrappers, scope gates (`scope_ok()` env-level + `in_scope()` per-caller),
  namespaced mode flag (D13), per-cutover suppression flags.
- The PHASE-2 endpoint conventions: verdict passthrough, 409-is-a-verdict,
  machine-token-is-not-the-actor (D6), client-supplied timestamps (D12).

### 2.2 The shipped WS-append slice IS the append-shaped template

`POST /workspace_state/append` + `workspace_state_entries` spool +
`render_workspace_state()` in the registry materializer tick. Properties
every future append-shaped route must copy:

1. **Append-only surface**: no edit/delete verb exists at all.
2. **No ingest**: the file's git copy stays authoritative for everything
   already in it; the DB holds only the not-yet-materialized tail. The
   ingest-authority clobber class cannot arise because there is no ingest.
3. **Splice, never re-render**: the materializer inserts pending items at
   the structural insertion point, byte-preserving all existing content --
   it never reconstructs a prose/JSON file it did not fully model.
4. **Guards on every write path**: conservation (remove the splice,
   recover the original byte-for-byte), exact-size, entry-count. This file
   has three confirmed silent-truncation incidents; the guards are why the
   materializer can be trusted with it.
5. **Durability ordering**: an entry flips to materialized only once its
   text provably reached git (push succeeded, or it was found already
   present); the flip is one-way, so rotation can never be undone by the
   writer (no resurrection).
6. **Dual-write soak built in**: `client_git_write=1` entries are never
   spliced, only watched for -- so the soak phase needs no shadow mode,
   the production path IS the shadow (see section 7).

## 3. Intent model: typed-per-file beats a generic byte-intake

**Decision: no generic "commit these bytes to this path" endpoint.** Every
routed file gets either a typed append verb (`/workspace_state/append`
style) or the one generic CAS verb below. Reasons: a generic byte-intake
cannot validate anything (the queue validator, claims.yaml schema, JSON
well-formedness all live server-side only if the endpoint knows what the
file IS); and an endpoint that accepts arbitrary paths is an arbitrary-
write primitive on the hub -- the blast radius the bearer token then
carries is the whole repo, not a file.

### 3.1 Append intents (typed, one endpoint per file)

`POST /workspace_state/append` (shipped), then per-file siblings as routed
(`/recommendation_log/append`, `/igw_log/append`, ...). Each endpoint owns
its file's dedup/idempotency semantics (WS: identical `(ts, text)`;
RECOMMENDATION_LOG: the jsonl record's own identity fields) and its
formatting convention, byte-identical to the incumbent client tool's.

### 3.2 Whole-file CAS intents (one generic verb, allowlisted paths)

```
POST /intent/replace
  {repo, path, base_sha, content, message, session_id}
-> 200 {verdict: "applied", commit}
-> 409 {verdict: "base_moved", current_sha, current_content}
-> 400 {verdict: "not_routed" | "validation_failed", detail}
```

- `path` must be on the server-side routing allowlist (section 5); any
  other path is `not_routed`, always.
- `base_sha` is the origin commit the client's edit was computed FROM. The
  hub applies intents ONE AT A TIME per repo: fetch, verify the file at
  origin tip still matches `base_sha`'s version (file-content compare, not
  commit equality -- an unrelated commit to another file must not bounce
  the intent), write, validate (per-path validator hook: yaml parse +
  schema for claims.yaml, `check_hypothesis_space_integrity` for the
  registry, plain json parse otherwise), commit, push.
- On `base_moved` the client re-edits from `current_content` and resubmits.
  This is the structured replacement for today's silent-adoption hazard --
  see DP-1.
- Size guard: same spirit as the WS guards -- a replacement that shrinks
  the file by more than a per-path threshold is refused with a distinct
  verdict (`suspicious_shrink`) requiring an explicit `allow_shrink` field
  the CLI only sets when the operator asked for a deliberate prune.

## 4. The client lever: `ree_commit.py` coordinator branch

The reason PHASE-4 adoption can be zero-churn: every call site already
routes through `ree_commit.py`. Add a transport-first branch mirroring
`task_claim.py`'s PHASE-2b blocks:

- Consult the routing table (section 5) with the commit's declared path
  set. **Only a commit whose ENTIRE path set is routed goes via the
  intake** (DP-3); a mixed or unrouted set takes the git path unchanged,
  with a NOTE naming which paths kept it on git.
- Per-path shape: append-shaped paths are NOT routed through ree_commit at
  all (their dedicated tools own them -- append_workspace_state_entry.py
  already has its own branch); ree_commit's branch carries only the CAS
  shape, one `/intent/replace` per path, all-or-nothing per commit.
- Ack allowlist, conservative: only `applied` suppresses the local git
  write. `base_moved` surfaces the returned current content to the caller
  (for tooling that can rebase, e.g. a registry append helper) or degrades
  to git with a warning. Every other outcome (unreachable, 4xx/5xx,
  not_routed) degrades to the byte-identical git path.

**Which `ree_commit.py` guarantees move hub-side, and which become moot,
for routed commits:**

| guarantee today | under the intake |
|---|---|
| private-index pathspec-race defence | moot -- content is sent per declared path; nothing else CAN ride along, by construction (the sweep class dies at the client) |
| per-item delta summary (sweep detection) | client-side pre-post: computed against `base_sha`'s content, so it reports exactly what the intent changes -- stronger, not weaker |
| compare-and-swap push + retry-on-reject + rebase lock | moot -- the hub is the one committer; CAS-at-the-hub replaces it |
| pre-push intent records (`pre-push.local` check) | moot per routed path (section 8) |
| HEAD/worktree-skew check | unchanged -- it protects local checkouts, which still exist |

## 5. Per-file routing table (initial; the server-side allowlist)

| file | shape | route | notes |
|---|---|---|---|
| `TASK_CLAIMS.json` / `TASK_CHIPS.json` | registry | DONE (PHASE-2) | typed verbs + materializer |
| `WORKSPACE_STATE.md` | append | DONE (this slice) | awaiting coordinator restart + soak + flag flip |
| `RECOMMENDATION_LOG.jsonl` | append | next append slice | jsonl append is the trivial case; typed endpoint |
| `evidence/planning/igw_routine_log.md` | append | later append slice | same splice pattern as WS |
| `docs/claims/claims.yaml` | editorial | CAS `/intent/replace` | THE COMMIT MOVES, NOT THE JUDGEMENT (parent plan section 4); yaml-parse + schema validation server-side; see DP-1 |
| `evidence/planning/hypothesis_space_registry.v1.json` | editorial | CAS | integrity checker as server-side validator |
| `evidence/planning/substrate_queue.json` | editorial | CAS | |
| `evidence/planning/igw_routine_ledger.json` / `igw_assignments.json` | editorial (tick-rewritten) | CAS, submitted by `igw_routine_tick` itself | the tick becomes an intake client; its `_ree_commit()` helper is the single call site |
| `evidence/experiments/review_tracker.json` | editorial (two append-ish arrays) | CAS first; consider a typed `/review/mark` verb if 409 churn is high | |
| `ree-v3/experiment_queue.json` | DB-authoritative | **typed queue endpoints ONLY -- option C settled, see section 6** | |
| `dispatcher_control.json` | control commands (lease grant/stop) | typed endpoints + DB state; git render stays as the DEGRADED FALLBACK dispatchers read when the hub is unreachable | added 2026-08-29 (fleet_commit_sequencing_redesign W3 fold-in): a STOP command stranded on DLAPTOP while the cloud dispatchers it addressed could not see it; emergency stop must survive a hub outage, hence the retained git fallback + documented direct-ssh stop |
| `metaworker_dispatch_budget_log.json` / `metaworker_dispatch_cooldown.json` | append (tick telemetry) | typed append endpoints, same template as WS/RECOMMENDATION_LOG | added 2026-08-29: the cloud-4 healer identified the budget-tick writer local-committing while wedged as the wedge-grower |
| work-repo code, experiment scripts, docs, evidence run packs | -- | stays git-direct | code plane has its own defence (integration branches); results already flow through the phase3 spool |

## 6. Option C settled: `experiment_queue.json` gets typed verbs, never file intents

The queue is already DB-authoritative (Phase 3): the git file is a
MATERIALISATION. A file-replacement intent for it would invert authority --
the hub would be asked to commit a file whose content the DB is about to
re-derive, and the queue writer's conflict recovery (`reset --hard` +
re-materialise) would legitimately destroy the intent's commit. So: client
queue edits go through typed endpoints (`/queue/add` exists; add
`/queue/amend` and `/queue/remove` with the same validation
`validate_queue.py` does client-side today, moved server-side), and
`/intent/replace` REFUSES the queue path with `not_routed` forever. This
is DP-8 as a settled rule, not an open question.

## 7. Rollout: shadow-first, per file, with windowed soak criteria

Per routed file, in order, each gated on the previous:

1. **Endpoint live** (for WS: pending on the next authorised coordinator
   restart -- the endpoint 404s until then and clients degrade to git, so
   deploy order is free).
2. **Dual-write soak.** Append shape: client POSTs with
   `client_git_write=true` and still git-writes; the materializer watches
   and marks carried entries. CAS shape: client POSTs the intent with a
   `shadow: true` field -- the hub records and CAS-checks it but does NOT
   commit; the client git-writes as today. Soak evidence = recorded
   intents whose CAS check matched what git then received.
3. **Soak exit criteria -- WINDOWED, with a total-ticks clause** (the
   PHASE-1 detector incident is the cautionary tale: a stalled timer must
   never read as a clean soak). For WS concretely: over a window of >= 3
   days, (a) materializer ticks observed in the window >= 0.9 * expected
   (2-min cadence), (b) zero guard fires, (c) zero duplicate entries in
   the file (grep by `(ts, text)` pair), (d) every `awaiting_client` entry
   marked carried within 10 minutes of its session's git push, (e) zero
   entries stuck pending > 24h. CAS analog: zero shadow intents whose CAS
   verdict disagreed with what git actually received.
4. **Flag flip**, one file at a time (`workspace_state_suppress_git_write`
   is the WS lever; each route gets its own, deliberately NOT the registry
   `suppress_git_write` flag).
5. **Rollback** = unset the flag. The git path is permanent fallback
   (parent plan 5.3) -- it is today's code, not new code, and stays
   exercised by every degraded call.

## 8. Decommission payoff ledger

"Retire" almost always means "shrink to a fallback appendix", not delete --
the git path remains the degrade route (DP-2), so its doctrine must stay
findable, just not resident in every session's context. Per file/route:

| once routed + flipped | retires / shrinks |
|---|---|
| registries (done) | already taken by the PHASE-3 rewrite (REE_Working `7914a203`): exposed-files listing, re-read rule, arbitration re-scoped |
| WORKSPACE_STATE.md | its exposed-files row; the append-tool-vs-Edit doctrine shrinks to "use the tool" (tool now routes); `append_workspace_state_entry.py` stays as the fallback writer with its guards |
| claims.yaml | the heartbeat-autostash skip doctrine for `docs/claims/`; the claim-before-editing-claims.yaml choreography shrinks (the CAS verdict replaces it as the mechanical gate); high-contention row shrinks |
| planning ledgers / registry / substrate_queue | `evidence/planning/` exposed-files rows; the igw-ledger read-modify-write caveat |
| ree_commit routed paths generally | `pre-push.local` intent-record checks per routed path; the pathspec-race and read-modify-write CLAUDE.md sections compress to a fallback appendix; `ref_convergence`/`safe_adopt_ref` remain (they protect local refs, which still exist) but fire far less |
| NOT retired by any of this | ref-move guard and skew checks (local checkouts persist); code-plane rules; archive origin-verification gates (DP-7); clinical-hours machinery (already removed separately 2026-08-28) |

The end-state CLAUDE.md rewrite is PHASE-3's job with this table as input;
do not start deleting doctrine per-slice -- one pass once the routing table
is substantially live, per the parent plan's PHASE-3 node.

## 9. Design problems (honest, 5.2.6 style)

- **DP-1 -- claims.yaml: CAS moves the COMMIT, and ALSO fixes the read
  point, but not the judgement.** Today's read-modify-write contamination
  comes from editing the WORKING TREE copy (which carries other sessions'
  uncommitted edits). An intake client must edit FROM `base_sha`'s content
  as served by origin/the hub, never from the shared working tree -- that
  is the actual mechanical fix for silent adoption, and the CLI branch
  must enforce it (refuse to submit an intent whose base was a
  working-tree read). What CAS cannot do is validate editorial quality;
  governance-only-edits discipline for claims.yaml is untouched.
- **DP-2 -- hub-unreachable UX (Mac tunnel bounce).** Fallback is the git
  path, so a tunnel blackout degrades to today's behaviour, silently
  correct but re-exposed to the old hazards for its duration. Consequence:
  no routed file's git-path tooling may ever be deleted (only shrunk), and
  the transport's degrade message must name the file-specific fallback
  hazard so a session knows it is back in the old world.
- **DP-3 -- mixed-path commits.** A `ree_commit.py` call naming a routed
  and an unrouted path in one commit must NOT be silently split (two
  commits with different durability stories under one message). Whole
  set routed -> intake; else git, with a NOTE.
- **DP-4 -- WS dual-write identity.** During the soak the same entry
  exists as a DB row and a client git append; the exact-substring
  presence check is the dedup. A client that mutates its entry text
  between POST and git write would produce a stranded `awaiting_client`
  row -- accepted (the tool has no such path; monitoring catches it via
  criterion 3d/3e).
- **DP-5 -- rotation/retention interplay generalises.** Any append route
  whose file gets rotated needs the WS one-way materialized flip; any
  whose DB spool outlives the file's retention needs D14-style render
  retention. Check per route at design time, not after.
- **DP-6 -- one writer process per repo.** The umbrella intake rides the
  SAME tick as the registry materializer (shipped that way for WS): two
  timers pushing the same repo would race each other. For REE_assembly
  the intake writer must serialise with the phase3 sync_daemon writers
  that share `/home/ree/REE_Working/REE_assembly` -- either a dedicated
  clone plus push-retry (the phase3 writers already tolerate interleaved
  pushes; correctness is per-file CAS, not per-repo locking), or
  absorption into sync_daemon's own tick. Start with the dedicated clone
  (matches the registry-writer convention); absorb later only if push
  contention measures as a problem.
- **DP-7 -- origin-verification gates stay git-side.** `chip archive`'s
  "archive file reached origin" gate (D7) and any future archive/rotate
  operation keep their git-fact gates; the intake does not absorb them.
- **DP-8 -- authority inversion.** See section 6; `not_routed` for
  DB-authoritative materialisations, permanently.
- **DP-9 -- actor identity.** Intents record `session_id` (body) AND the
  token's machine (canonicalised) AND the raw reported host, exactly the
  D6 split. An intent's commit message carries the session attribution
  the way `task_claim.py` commits do today.
- **DP-10 -- transport scope-gating is a HARD requirement.** The
  2026-08-28 incident: a plain `test_hygiene_routine_tick.py` run on a
  suppression-armed box leaked 21 fixture chips into the production DB --
  fixtures redirect the FILE, not the transport. Every new client branch
  must sit behind `enabled() and in_scope(<operating root>)`, and
  fixtures must be unroutable by construction (isolated config path).
  A corpus-wide sweep for this shape is already in flight (session
  `cool-sutherland-9d984d`, chip
  `chip-20260828-corpus-coordinator-transport-leak-sweep`) -- new routes
  coordinate with it rather than duplicating it. The WS client branch
  shipped with both gates and an isolated-config test.
- **DP-11 -- the coordinator restart dependency.** New endpoints answer
  404 on a running daemon until it restarts; restarts are individually
  user-authorised (precedent: 2026-08-27, 2026-08-28). Design
  consequence: every client branch must treat 404-with-payload as
  degrade-to-git (the transport already does), so code can land freely
  and activation is a clean, separate, authorised event per deploy.

## 10. Sequencing (next slices, in order)

> **2026-08-29 reconciliation (session `wedge-clear-20260829`):** the
> fleet-wedge campaign plan
> (`fleet_commit_sequencing_redesign_20260829.md` section 9) folds its
> commit-mechanics workstreams INTO this document: its W2-flip IS steps 1-2
> below; its W1 (fix `verify_resolve_coordinator_ack`'s false-positive
> class + re-point the registry git fallback at the remote tip) is inserted
> as a **hardening slice BEFORE further slices** -- every new endpoint
> inherits the same ack-verify pattern, and the false positive is the
> confirmed generator of 13+ redundant `chips: resolve` fallback commits
> since the PHASE-2b cutover; its W3 is the two dispatcher-family rows added
> to the section 5 table. During the current machinery halt the campaign
> executes, under this doc's conventions, only the slices that kill the
> 2026-08-29 confirmed stranding generators: W1 hardening, steps 1-2 (WS
> flip), step 3 (RECOMMENDATION_LOG), step 5 (igw tick client -- would have
> prevented 18 of the 23 commits stranded on REE_assembly that day), plus
> the dispatcher rows. Steps 4, 6, 7 continue on this doc's own sequence
> after the machinery restarts, dispatched through the new curation pass.

1. **Coordinator restart** (user-authorised) -> WS endpoint live; WS
   dual-write soak begins passively (every closing session that uses the
   append tool participates).
2. **WS soak** against section 7's criteria; then flip
   `workspace_state_suppress_git_write` in the Mac + cloud-5 configs.
3. **RECOMMENDATION_LOG.jsonl append endpoint** -- smallest next slice,
   same template.
4. **`ree_commit.py` transport branch + `/intent/replace`** behind its own
   flag, claims.yaml first (shadow mode), with server-side validators.
5. **igw tick as intake client** for its two ledgers + log.
6. **review_tracker.json**; then judge whether a typed `/review/mark` verb
   is warranted by 409 churn.
7. **Typed queue amend/remove endpoints** (option C completion).
8. **PHASE-3 doctrine pass** using section 8's ledger, once the table is
   substantially live.

Each slice: claim-first, tests in `ree-v3/coordinator/` + scripts corpus,
full coordinator suite on a worker before landing, deploy = hub pull,
activation = authorised restart where the daemon is involved.
