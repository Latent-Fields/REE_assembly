# Fleet commit-sequencing redesign -- stop generating housekeeping, 2026-08-29

Session `wedge-clear-20260829`. Written immediately after the full-fleet wedge
clearance of 2026-08-29 (all six checkouts across DLAPTOP / hub / ree-cloud-4 /
ree-cloud-5 audited per-commit, stranded content landed, refs converged, zero
loss). This document is the durable capture the user asked for: what generated
the load, and the redesign that removes the generators rather than adding a
fix-on-fix.

## 1. The measured problem

- **1,496 chips recorded in the 14 days to 2026-08-29.** At least 50% are
  named coordination-housekeeping classes (prefix families): metaworkergc 286,
  queuefloor 226, strandedwt 69, staleclaim 52, statusregress 40, refwedge 33,
  stash/scriptscorpus/hookgating/unlandedwt/classifierblock/fleetstash 46.
  The `other` 744 also contains date-prefixed housekeeping (e.g.
  `chip-20260829-mac-checkout-push-backlog`), so 50% is a floor.
- **The same wedge episode minted >= 5 chips** (refwedge x2 handoffs,
  escalated-decision, push-backlog, healer follow-ons) because episodic chip
  refs carry `since-<timestamp>` suffixes -- every re-observation of a
  continuing episode mints a fresh ref that evades chip_ref dedup by design.
- **The wedges themselves were 100% recoverable bookkeeping.** Today's
  per-commit audit found not one commit of scientific content at risk; every
  stranded commit was WORKSPACE_STATE appends, igw ledger ticks, chip
  resolves, recommendation-log lines, dispatcher lease commands, or telemetry.

## 2. Root-cause taxonomy (each confirmed today, not hypothesised)

**R1 -- residual git-as-IPC on coordinator-mode boxes.** Since the 2026-08-28
cutover the two registries are coordinator-owned, but sessions and ticks still
LOCAL-COMMIT: WORKSPACE_STATE.md appends, dispatcher_control.json lease
commands, RECOMMENDATION_LOG.jsonl, metaworker_dispatch_budget_log.json /
cooldown ticks, worktree_session_registry regen (umbrella); igw ledger/workset
and steward ledger (REE_assembly). Meanwhile origin advances every ~2 minutes
(phase2b materializer, heartbeats, phase3 writers). Any local commit that
cannot push within one materializer interval is racing.

**R2 -- push-retry gives up exactly when it is needed.** `ree_commit.py`'s
push-retry correctly refuses to rebase when the shared tree is dirty (the
REE_assembly steward ledger's uncommitted append kept the tree dirty for
hours) or when the rebase conflicts on a hot file. Until today NO box had the
union merge driver installed -- designed 2026-08-19
(`docs/plans/union_merge_driver_design_20260819.md`, BUILD recommendation),
verified capable of resolving 97.9% of reconstructed registry conflicts with
zero mis-merges, and never deployed anywhere. WORKSPACE_STATE.md, the single
largest conflict source (29 of 34 historical conflicted merges), is outside
the driver's scope pending the S5.4 decision.

**R3 -- the chip-resolve double-write defect.** On a coordinator-mode box,
`chip_ledger.cmd_resolve`'s coordinator write SUCCEEDS (byte-identical
status/resolved_at/note in the DB and in the materialized origin file), but
`verify_resolve_coordinator_ack()` reports problems and the code falls through
to a redundant local git commit -- which then strands on a checkout that
cannot push, growing the wedge, which spawns more chips. 13 `chips: resolve`
commits reached origin this way since the cutover; today's audit found 5 more
stranded (4 Mac + 1 cloud-4), every one byte-identical to what the
coordinator had already durably recorded. The cloud-5 instance
(resolved_at 9s apart on the two sides) is the same defect hit by two boxes'
hygiene ticks resolving the same chip concurrently.

**R4 -- once wedged, convergence is correctly impossible without an audit.**
`ref_convergence` route A cannot patch-id-prove whole-file JSON rewrites, and
an append re-landed under a fresh timestamp (the lit-pull session re-appended
its WORKSPACE_STATE entry with a new stamp) has no matching patch-id either.
The refusal is right; the cost is that every wedge becomes multi-chip operator
work. The read-only `reconcile_wedge_content.py --check` wiring (2026-08-19
user decision) means nothing repairs even the provably-safe bookkeeping
classes automatically.

**R5 -- episodic chip minting has no recurrence collapse.** Hygiene/healer
ticks mint a fresh `since-<ts>` chip per observation of a CONTINUING episode,
and mint per-instance chips (226 queuefloor, 286 metaworkergc) for conditions
that are really one standing process each. Chips measure observations, not
problems, so the ledger fills at observation rate.

## 3. Done today (no decision needed)

- Full fleet wedge clearance, per-commit content audit, zero loss:
  Mac umbrella (17 ahead) + REE_assembly (23 ahead) + cloud-4 umbrella
  (1 ahead + uncommitted WORKSPACE_STATE 9-entry-loss repair, landed
  `6bcdb482`) + cloud-5 umbrella/assembly (2+4 ahead) all converged level
  with origin; hub verified clean; detached worktree reattached.
- **Union merge driver installed on all three umbrella checkouts that exist
  (DLAPTOP, ree-cloud-4, ree-cloud-5)** per S5.3 of the design doc.
  Interpreter paths verified real on each box.

## 4. Proposed redesign (raised with the user 2026-08-29)

**W1 -- kill the R3 double-write (smallest, highest leverage).** On a box
where `coordinator_suppression_armed()` and `coordinator_resolve` returned
ok/ok_unchanged, an unverifiable ack must NOT fall through to a git write for
materializer-owned files: the materializer will overwrite that commit within
minutes anyway, so the fallback provides zero durability and nonzero wedge
growth. Replace the fallthrough with: re-verify against the coordinator's
copy (not the not-yet-rendered origin) and, only on a PROVEN missing row,
take the git path. Fix the ack-verifier's false-positive class at the same
time (concurrent duplicate resolves from two boxes' ticks must classify as
ok_unchanged, not hollow).

**W2 -- extend coordinator ownership to WORKSPACE_STATE.md (phase 2c).**
Sessions POST closing entries; the hub materializer renders the file the way
it already renders the registries; `append_workspace_state_entry.py` becomes
the client the way task_claim/chip_ledger did. Removes the #1 conflict file
from every rebase and removes the whole-file read-modify-write truncation
class (4 confirmed incidents) structurally. Consistent with the migration
plan's direction; the memory `reference-phase2b-materializer-ownership-
boundary` records WORKSPACE_STATE as the known residual.

**W3 -- move the dispatcher control plane off git-as-IPC.** dispatcher lease
grant/stop commands, budget-tick and cooldown appends become coordinator
endpoints + DB state (rendered to git for visibility if wanted). Today a
lease STOP command sat stranded on the Mac while the cloud dispatchers it
addressed could not see it -- git-as-IPC failing exactly the way Phase 3
found for the experiment plane. The healer independently flagged the
budget-tick writer as the wedge-grower on cloud-4.

**W4 -- wire `reconcile_wedge_content.py --repair` for the allowlisted
bookkeeping classes only** (TASK_CLAIMS/TASK_CHIPS/WORKSPACE_STATE), keeping
--check-only behaviour for everything else. This reverses the narrow half of
the 2026-08-19 check-only decision; W1-W3 shrink what it would ever need to
touch, so its blast radius shrinks with them. Anything outside the allowlist
still refuses to a human, unchanged.

**W5 -- recurrence-class collapse in chip minting.** An episodic finding
(refwedge, queuefloor, gc-candidate, staleclaim...) updates ONE standing chip
per (class, subject) with an episode counter instead of minting
`since-<ts>` instances; crossing N episodes escalates that standing chip to a
root-cause route (/metaworker-learning) instead of re-dispatching another
symptom fix. This is the "economical review" layer: the ledger then measures
problems, not observations. (`chip-20260828-metaworkerlearning-refwedge-
rechip-gap` already names the refwedge instance of this gap.)

## 5. Sequencing

W1 alone stops the active bleeding; it is a scoped code fix with tests.
W5 stops the ledger noise and is independent. W2/W3 are the structural
completion of the coordinator migration and should follow the same
shadow-first pattern as phase 2b (endpoint + suppressed client + materializer,
git path retained as degraded fallback). W4 lands last, once W1-W3 have
shrunk its surface. Each workstream gets its own chip; none of them should be
absorbed into "while I'm here" fixes -- that pattern is what this document
exists to end.

## 6. Absorption check against the durable chip ledger (user-requested, 2026-08-29)

All 43 open chips on origin were checked against W1-W5. Absorptions below mean
"this chip becomes a named work item of that workstream, withdrawn as a
standalone dispatch when the workstream's owner picks it up" -- not silent
withdrawal now.

**Absorbed into W1 (registry write-path correctness):**
`chip-20260828-chipledger-amendurgency-postcommit-selfverify`,
`chip-20260828-cutover-durability-review` (becomes W1's adversarial test
plan), `chip-20260828-chipledger-failopen-loss-fix`,
`chip-20260828-chipledger-noop-record-committed-destructive-delete`,
`chip-statusregress-f5f80d8d7d`, `chip-statusregress-e9142d4036`
(materializer render regressions -- same write-path family),
`chip-20260829-staleclaim-absent-path-stale-file-gap`,
`chip-20260829-auditstaleclaims-virtual-slot-resource`.

**Absorbed into W2 -- and W2 itself collapses into an EXISTING chip:**
`chip-20260828-phase4-ws-soak-eval-flag-flip` reveals the WORKSPACE_STATE
coordinator endpoint + dual-write soak is ALREADY BUILT and waiting on its
>=3-day soak evaluation. W2 is therefore not new design work: it is
executing that chip (evaluate section-7 criteria, flip suppression).
`chip-20260829-wsappend-guard-blind-to-preexisting-loss` is interim
hardening that the flip obsoletes -- do it only if the soak eval fails.

**Absorbed into W4:** `chip-20260828-chiparchive-uncovered-by-every-proof-route`
(proof-route coverage is exactly W4's precondition).

**Absorbed into W5 (recurrence collapse):**
`chip-20260829-queuefloor-kindreport-hysteresis` (already specifies W5 for
the queuefloor class -- kind=report, non-dispatchable, hysteresis),
`chip-20260828-metaworkerlearning-refwedge-rechip-gap`,
`chip-20260829-metaworkerlearning-hookgating-recurrence`,
`chip-20260829-repr-authority-selfcontinuation-loop` (the completion-
predicate requirement below comes from it),
`chip-20260829-sessionland-phase4-resolves-foreign-claimed-chip`,
`chip-20260904-refwedge-r1-rate-cost-remeasure` (becomes the plan's own
outcome measurement).

**Discharged or part-discharged by today's clearance:**
`chip-20260828-reecloud4-behind-divergent-manifests` -- the 117-commit lag
half is discharged (cloud-4 REE_assembly fast-forwarded level today); the
divergent-manifest half remains (an untracked flat manifest for v3_exq_603s
sits on cloud-4, not on origin) and should be re-scoped to just that.
`chip-strandedwt-ree-cloud-5-...repr-authority...` / `chip-unlandedwt-ree-cloud-4-...`
remain real but shrink to single-worktree audits.

**NOT absorbed -- science and standalone infra, the ledger's intended
content (17):** sleep matched-arm, MECH-152 redesign, MECH-320 retest,
INV-050 MEL env, MECH-482 accumulator, evidence-ladder dirsweep,
capability-contract vocab, repr-authority research thread, thought-digestion
wave grouping, UA claustrum scan, heartbeat hysteresis remeasure, bashgate
quote defect, stash-fleet test de-flake, skill archaeology, step5c registry
producer rule, IGW-236, scripts-corpus RED sweep -- plus
`chip-20260829-queue-three-stranded-exq-drivers`, which is the single most
urgent item on the board: the experiment queue is STARVED (depth 1) while
three finished, smoke-tested drivers (956/957/958) sit unqueued -- the
direct scientific cost of the coordination noise this plan removes.

## 7. Red-team findings (user-requested), and the plan revisions they force

**RT1 -- W1 as first drafted inverts fail-safety. REVISED.** Deleting the
git fallback on an unverifiable ack assumes acks are never hollow; the
2026-08-28 amend incident was a GENUINE hollow ack that silently dropped a
completion note. Revised W1: (a) fix the verifier's false-positive class
(concurrent duplicate resolve from two boxes' ticks must classify
ok_unchanged); (b) keep the fallback, but land it on the REMOTE TIP
(chip_ledger already has `to_remote_tip`) via throwaway worktree so a
fallback commit can never strand on a wedged local ref; (c) verify-on-origin
doctrine unchanged.

**RT2 -- W2 was about to duplicate an existing build.** Caught in section 6:
the endpoint and soak exist; the work is the evaluation + flip, owned by the
existing phase4 chip. A redesign that re-specifies already-built work is
itself the fix-on-fix pattern; this document defers to the built thing.

**RT3 -- W3 makes the hub a SPOF for the emergency dispatcher STOP.** A
stop command must reach a box whose coordinator link is down -- today's git
path, for all its faults, is transport-independent of the hub. Revision:
coordinator becomes primary, git file stays as the degraded fallback (read
by dispatchers when the hub is unreachable), and the runbook documents
direct ssh stop. Same shadow-first shape as every other cutover here.

**RT4 -- W4 (auto-repair) can mask W1-W3 regressions.** A symptom cleaner
that silently lands stranded bookkeeping hides the very generator telemetry
the redesign needs. Revision: --repair logs every repair to a counter the
morning digest surfaces, with an alert threshold (>N repairs/day = a
generator regressed; raise a class chip, not more repairs). Non-allowlisted
paths keep refusing to a human, unchanged. This flip reverses a deliberate
2026-08-19 user decision and lands ONLY with explicit user ratification.

**RT5 -- W5's standing chips risk becoming permanent furniture.** The
repr-authority chain (9 self-continuations, empty notes, no done-condition)
is the demonstrated failure mode of standing work without a completion
predicate. Revision: every standing class chip carries (a) a done-condition
("class rate < X/week for Y weeks"), (b) episodes appended INTO the chip
(forensic detail preserved -- the since-<ts> chips' one virtue), (c) the
>=N-episodes escalation to /metaworker-learning.

**RT6 -- rollout window.** The wedge class stays live until W1-W2 land
(demonstrated: a fresh chips:resolve fallback commit stranded DURING this
session's own closeout). Interim regime, verified working today: union
driver auto-merges registry rebases (observed resolving a TASK_CHIPS
conflict unaided); WORKSPACE_STATE remains the one manual conflict until
the W2 flip -- which argues for executing the phase4 soak-eval chip FIRST.

**Revised sequencing:** W2-flip (existing chip, mostly evaluation) ->
W1 (verifier fix + to_remote_tip fallback) -> W5 -> W3 -> W4 last, behind
its telemetry. Queue-starvation chip (956/957/958) is orthogonal and should
dispatch immediately regardless.

## 8. Review outcome + FINAL plan of record (user review, 2026-08-29)

Reviewed interactively with the user 2026-08-29. Ratifications and amendments:

**Ratified.** W4 (reconciler --repair for the three allowlisted files,
telemetry-gated, LAST in sequence) -- explicit user yes, reversing the
2026-08-19 check-only decision. The bundling rule for campaign dispatch
(below) -- user: "the bundling feels right."

**Execution mode -- run-through under halt.** The user has HALTED metaworker
orchestration and chip dispatch for the duration. The plan executes as ONE
directed campaign (this umbrella session + directly-run scoped sessions),
each workstream landing and resolving as it completes -- no dispatched chips,
no waiting on the machinery the plan modifies. The machinery RESTARTS only
after W5b/c lands, so the orchestrator comes back up already running the
curation policy instead of the behaviour this plan retires. The standing
"leave metaworker orchestration to the orchestrator session" rule is
consciously set aside here by direct user instruction for this campaign.

**Corpus signals folded in** (relayed from the /insights session's 803-session
2026-06-24..08-29 usage report; its prescriptions were mostly behind current
practice and are discounted -- only the frequency/pattern data is used):
(1) wedging confirmed as a top-3 corpus friction class -- independent
corroboration of section 1's ranking by a second measurement method;
(2) mid-task session death (usage limits / sleep) stranding open claims with
unwritten deliverables, >=6 sessions -- becomes W6; (3) duplicate-dispatch
races caught by STOP-CHECK only AFTER exploration cost, >=4 sessions --
becomes the pre-dispatch landed-check in W5b; (4) built-but-not-enabled
mitigations as a recurring class (the union driver's ten uninstalled days are
the poster child) -- becomes W7. Its two anti-doctrine proposals (blocking
Edit/Write PreToolUse hook; default worktree-isolated landing) are rejected
per the 2026-08-15 hook incident and trunk-first policy.

**New/restructured workstreams:**

- **W6 -- incremental landing + resumable state (PRECONDITION for W5b).**
  Skill-text changes: land deliverables as produced rather than batching at
  close; on limit-approach write a resumable-state note; campaign briefs
  require per-item resolve-as-you-go (today's clearance session is the
  worked example). Standing-rule edits get the GOV-HELDOUT-1 held-out check.
- **W5 restructured:** **W5a** minting collapse (one standing chip per
  (class, subject), episode counter, episodes appended INTO the chip,
  completion predicate, >=N episodes escalates to /metaworker-learning).
  **W5b** orchestrator curation pass: each cycle, classify the open ledger
  into science-dispatch / campaign-bundle / hold-with-reason /
  absorbed-into-workstream; run ownership + already-landed checks ONCE per
  bundle BEFORE dispatch. **Bundling rule (ratified):** bundle only within a
  class or shared subject resource; cap campaign size; the campaign session
  may re-scope or hand back items. A hold carries a stated reason + review
  cadence. The curator must be a NET CHIP SINK -- open-chip count and
  chips/week are its success metrics and are tracked. **W5c**
  science-priority scheduling: science chips always dispatch first;
  housekeeping dispatches only as campaigns under a budget cap; a starved
  experiment queue preempts housekeeping dispatch entirely.
- **W7 -- mitigation-enablement audit.** Fleet-wide, read-only: enumerate
  built guards/drivers/hooks/flags and verify installed+armed state per box
  (the audit_worktree_skills pattern generalised). Can run at any point in
  the sequence; also the natural later home for W4's repair-rate telemetry.

**FINAL SEQUENCE (run-through order):**
W0 queue rearm (V3-EXQ-956/957/958 via /queue-experiment -- science first;
runners/scaler are independent of the halted chip machinery) ->
W2-flip -> W1 -> W6 -> W5a -> W5b -> W5c -> W3 -> W7 (or earlier, any idle
moment) -> W4 -> restart orchestration + dispatch.

**Restart criteria:** all of -- W5b/c landed (curation live in the orchestrate
skill); W1 verified (no new chips:resolve fallback commits over an
observation window); W7 first audit green or its findings chipped; wedge
check clean (ref_convergence quiet on all boxes).

## 9. Reconciliation with the other plans on this surface (user-requested verification, 2026-08-29)

Surveyed before final acceptance: `phase4_commit_intake_design.md` (2026-08-28,
user-ratified; parent `task_claim_chip_coordinator_migration_plan.md`),
`docs/plans/union_merge_driver_design_20260819.md`,
`docs/plans/coordination_db_offline_write_path_20260819.md`,
`docs/plans/fleet_telemetry_consolidation_20260821.md`,
`queue_authoring_contention_and_id_collision_20260829.md`,
`refwedge_class_recurrence_investigation_20260826.md`.

**Verdict: fold the commit-mechanics workstreams INTO phase-4; this document
remains the campaign umbrella.** Phase-4 is the plan of record for how git
commits happen (hub-serialised intake, per-file routing table, section-8
decommission ledger whose stated payoff -- retire the concurrency defensive
apparatus -- is this plan's own goal). Specifically:

- **W2-flip** = phase-4 sequencing steps 1-2, unchanged (already its plan).
- **W1** re-homed as a phase-4 **hardening slice before further slices**:
  the ack-verify pattern it fixes is inherited by every future endpoint.
- **W3** re-homed as two new rows in phase-4's section 5 routing table
  (dispatcher_control.json; budget/cooldown tick appends), with the
  degraded git fallback requirement carried over from RT3 -- which also
  discharges the surviving requirement of the 2026-08-19 offline-write
  scoping doc (its hub-SPOF argument against registry DB-authority was
  overtaken by the PHASE-2b cutover; its unreachable-hub requirement lives
  on in every fallback clause).
- **Union merge driver plan**: absorbed -- installed fleet-wide 2026-08-29;
  remains the interim mitigation while the phase-4 table goes live; W7
  audits its installed state thereafter.
- **Queue-authoring contention doc**: already landed (EXQ ID reservation),
  sits on phase-4's option-C line; no fold needed.
- **Telemetry consolidation + refwedge recurrence investigation**: adjacent
  scope (liveness inference; recurrence measurement) -- cross-referenced,
  not folded. The refwedge investigation's measurements feed W5a's class
  definitions.

**Amended run-through (both goals, one sweep):** W0 queue rearm ->
W1 (phase-4 hardening slice) -> W2-flip (phase-4 steps 1-2) ->
RECOMMENDATION_LOG slice (phase-4 step 3, smallest, strands confirmed today)
-> W6 -> W5a -> W5b -> W5c -> igw-tick intake client (phase-4 step 5) +
dispatcher-family rows (folded W3) -> W7 -> W4 -> restart machinery.
Remaining phase-4 slices (claims.yaml CAS, review_tracker, typed queue
verbs) run AFTER restart, dispatched through the new W5b curation pass --
deliberately, as its first live test. Phase-4's section 10 carries the
mirror of this note.
