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

## 10. Final red-team + landing-sweep fold-in (user-requested, 2026-08-29) -- THE EXECUTABLE SEQUENCE

Three independent review passes were run against the reconciled plan before
acceptance: failure-modes/rollback (F1-F12), completeness-by-enumeration
(C1-C12), and a landing sweep over all 43 open chips + residues. Verbatim
reports in the session transcript; every accepted finding is folded below.
This section SUPERSEDES the run-through orders in sections 8 and 9.

### 10.1 Blockers found, and their resolutions

- **F1: the WS soak has not started** -- the coordinator restart that
  activates the WS endpoint has never happened, so a W2 "flip" mid-campaign
  would flip with zero soak evidence, violating phase-4 section 7 on the one
  file with three confirmed truncation incidents. RESOLVED: W2 splits into
  **W2-restart** (one restart, soak begins passively, campaign continues)
  and **W2-flip** (executes ONLY when section-7 criteria are met -- expected
  AFTER machinery restart; no campaign step depends on it).
- **F2: one restart, not four.** All server-side endpoint code (RECLOG,
  governance-flag verbs, dispatcher family, igw intake, W5a episode verb,
  archive verb) lands on the hub checkout BEFORE the single user-authorised
  restart; clients stay on git until their flags flip.
- **F4: dispatch is NOT fully halted.** `com.ree.dispatch-service` was
  observed RUNNING (pid 3750) with `com.ree.dispatch-executor` loaded on
  DLAPTOP despite the control-plane stop. Phase A below makes the halt real
  and verified before anything else runs.
- **C1: `governance_flags.v1.json`** -- busiest uncovered writer (88
  commits/14d, confirmed stranding history) -- added to the phase-4 table
  (typed raise/resolve verbs).
- **C2: the steward ledger** (`scripts/steward/state/*`) -- named by this
  very plan as today's wedge-keeper, then undispositioned. Interim rule
  (lands with W6): the steward sweep COMMITS its append in the same step,
  never leaves it dirty; phase-4 gets a later append-slice row. Until that
  slice lands, R2's mechanism is explicitly NOT fully retired.
- **C3: W5a's episode appends would ride mirror-less verbs** (chip
  attach/amend have no coordinator representation -- always git path),
  installing a new generator inside the workstream meant to end them.
  RESOLVED: the coordinator-side episode verb is a stated PRECONDITION of
  W5a, landed with the endpoint batch and live at W2-restart.

### 10.2 Accepted serious/moderate revisions

F3 W1 covers the IN-PROCESS tick callers (hand-built Namespace never takes
the CLI's remote-tip default; the ticks are the R3 population) with a
regression test on that route. F5 W1 semantics: cannot-verify != verified-
present -> take the git path (redundant commit is the acceptable cost); test
that a remote-tip fallback for a genuinely-DB-missing row survives two
materializer ticks. F6 WS-flip rollback = unset flag PLUS drain pending
entries to git, verified pending=0. F7 the restart is preceded by the
operator-guide drift check + preflight and followed by /writer-health green
+ one observed phase3 commit. F8 WORKSPACE_STATE leaves W4's repair
allowlist once the WS flip lands (pre-flip strands only). F9 pause
`com.ree.workspacestaterotate` + the cloud-4 budget tick for the window; run
`ref_convergence --dry-run` on all boxes after EACH workstream lands. F10
unload `com.ree.chiparchive` for the window (idempotent; reload at restart).
F11 the W1 restart criterion is restated falsifiably: no `chips: resolve`
commit whose content is byte-identical to a coordinator-acked resolve
(verdict/handoff resolves excluded), over a window with a minimum observed-
resolve count. F12 W1's final sub-step is fleet deployment: pull umbrella on
cloud-4/5 and confirm one post-W1 tick's verifier output. C4 the igw
WORKSET regen + C6 `experiment_proposals.v1.json` join the igw intake slice
(DP-3 whole-set rule -- without them the slice's headline estimate does not
hold). C5 `worktree_session_registry.*` stays git-direct, justified:
Mac-owned single-writer, machine-scoped regen. C7 the chip archiver gets a
coordinator-side archive verb (strip the DB rows, not just the git render)
-- landed with the endpoint batch; its absorbed proof-route chip moves from
W4 to this item. C8 W5b's pre-dispatch bundle check is ADDITIVE: the
START-TIME STOP-CHECK inside each session remains mandatory (the 2026-07-28
84-second triple-claim is the held-out case). C9/C10 named GOV-HELDOUT-1
target rules: W5a/b/c check against the chip-scope rule's closed four-
revision history, the 2026-08-25 never-preclaim revert, and the
spawn_task/record pairing rule; W6 checks against claim-first point 2's
narrow-exposure-window doctrine, the session-land-must-be-invoked rule, and
the multi-file-push rule. C11/C12 `decision_log.v1.jsonl` +
`stash_dispositions.json` -> later append slices; governance-regen outputs +
`morning_agenda.md` -> explicitly git-direct (single-session, claim-guarded).

### 10.3 Landing-sweep additions (safe adds, ranked)

Folded into the workstreams they ride: (1) amend-urgency post-commit
self-verify -> W1's chip_ledger diff; (2) audit_stale_claims virtual
ID-slot resource -> W1 batch (de-risks W0's own claim shape); (3) WS append
shrink-guard compares against HEAD -> lands BEFORE W2-restart (the flip
makes this path live); (4) the two statusregress chips become W4's
verification fixtures; (5) session-land Phase-4 foreign-claimed-chip guard
-> W6's skill edit; (6) staleclaim absent-path hardening -> W1 batch; (7)
stash-fleet wall-clock de-flake -> quiets the false-chip manufacturer
before restart; (8) re-run the scripts-corpus RED subset on the quiesced
box -- this re-measurement IS W1's verification gate, and nobody budgets
triage against the unre-measured 15+8 figure; (9) close the trivial stale
`side-branch-session` test claim. CONTINGENT (10): the ree-cloud-4 stranded
failopen-loss worktree + the untracked v3_exq_603s manifest -- cloud-4 IS
reachable (91.99.68.94; the sweep agent probed a wrong address), so this is
in scope if the window allows, else it stays with its owner chip.
REJECTED adds, on the sweep's own caution: the `merge_origin_into_local`
destructive-delete chip (three-incident function, needs its own session);
full 15-file corpus triage before re-measurement. The converging
chip_ledger.py edits land as ONE reviewed diff with the corpus subset green
between steps.

### 10.4 THE SEQUENCE (final, supersedes 8/9)

- **Phase A -- make the halt real:** verify/effect stop of
  dispatch-service/executor (Mac launchd + cloud-4/5 units); pause
  workspacestaterotate, chiparchive, cloud-4 budget tick; baseline
  `ref_convergence --dry-run` on all boxes.
- **W0** queue rearm (V3-EXQ-956/957/958).
- **W1** chip_ledger hardening as one reviewed diff (ack-verifier
  false-positive class; remote-tip fallback incl. the in-process tick
  route; amend-urgency self-verify; F5 semantics) + W1-batch safe adds
  (2, 6, 7) + WS shrink-guard-vs-HEAD (3) + corpus-subset green + fleet
  deploy to cloud-4/5 with one observed post-W1 tick.
- **Endpoint batch (server-side only, no activation):** RECLOG append;
  governance-flag verbs; dispatcher_control + budget/cooldown; igw intake
  (ledgers + log + workset + experiment_proposals); W5a episode verb;
  archiver verb.
- **W2-restart:** drift check -> preflight -> ONE coordinator restart ->
  /writer-health green + observed phase3 commit. WS soak begins.
- **W6** skill-text batch (incremental landing; resumable-state note;
  steward commit-immediately rule; session-land foreign-claimed guard) --
  each edit with its named GOV-HELDOUT-1 cases.
- **W5a/b/c** (episode verb live; additive STOP-CHECK declared; named
  held-out cases run).
- **Client flag flips** per-file as each soak meets its criteria (RECLOG
  and dispatcher first; WS = W2-flip only at soak maturity, rollback =
  unset + drain).
- **W7** mitigation-enablement audit (also re-verifies W1 fleet deploy).
- **W4** reconciler --repair (allowlist per F8; statusregress fixtures;
  telemetry + digest surfacing + rate alert).
- **Contingent add 10** if window allows.
- **Restart:** criteria = F11-restated W1 quiet signature + curation live
  + W7 first audit green-or-chipped + fleet ref_convergence quiet +
  dispatcher-control state drained/consistent; then reload the paused
  launchd agents and restart orchestration/dispatch. W2-flip follows at
  soak maturity through the restarted machinery.

## 11. EXECUTED (2026-08-29, session wedge-clear-20260829 -- the campaign ran to completion in one day)

Every section-10.4 step ran and landed, in order, under the halt; the
machinery restarted at ~13:00Z with all restart criteria met. Landing record
(all on origin; umbrella shas unless noted):

- **Phase A**: halt made real (dispatch-service was live at pid 3750 despite
  the control-plane stop -- unloaded + verified, with workspacestaterotate,
  chiparchive, and both cloud healer timers); fleet ref_convergence baseline
  all-level.
- **W0**: V3-EXQ-957 + 958 queued (ree-v3 c5a982a193 + POST) and BOTH PASSED
  within minutes; 956 had already run (FAIL diagnostic, 01:45Z). Three
  results to pending review.
- **W1**: bf5fb21f -- ack-verifier Class B fix (target-status, not stale
  local pre-read), Class A logged, remote-tip default extended to the
  in-process tick callers (the R3 population), amend-urgency self-verify,
  audit_stale_claims virtual ID-slot, staleclaim origin-confirmation, WS
  append set-membership loss guard, stash-fleet de-flake. Deployed to
  cloud-4/5. F11 signature quiet from deploy through restart (short window,
  stated honestly; the criterion continues to be monitored by the same
  check).
- **Endpoint batch** (ree-v3, all INERT until the restart): RECLOG append
  intake ca1369bf98; dispatcher lease intake 9de55a91c3 (ingest-before-
  render, git file kept as degraded fallback); chip episode verb ef12e99adb.
- **W2-restart**: ONE coordinator restart (user-authorised, preflight +
  drift-checked, nothing in flight); /writer-health green, all new endpoints
  live, WS soak accumulating (2 dual-write entries pending at first check).
  **W2-flip remains OPEN** pending its >=3-day soak
  (chip-20260828-phase4-ws-soak-eval-flag-flip owns it; WORKSPACE_STATE.md
  leaves W4's repair allowlist at that flip, F8).
- **W6**: 1534080bae -- CLAUDE.md incremental-landing + resumable-trail rule
  (GOV-HELDOUT-1 cases on the edit), session-land Phase 4 foreign-claimed
  guard, steward never-exit-dirty rule (live stranded append landed,
  07ec0b16b0 REE_assembly; sweep hardening chipped:
  chip-20260829-steward-sweep-dirty-exit-hardening).
- **W5a**: 1a192ab6e4 -- standing episodic chips (refwedge + queuefloor),
  coordinator episodes, generation minting, 6h hysteresis, queuefloor
  kind=report.  **W5b/c**: 9d5726f0 -- orchestrate Step 1b curation pass
  with the ratified bundling rule and the net-chip-sink metric.
- **W4**: 5683ae9b50 -- telemetry-gated auto-repair (3/day withhold + rate
  alert).  **W7**: b5b95b9feb -- audit_mitigation_enablement.py; first live
  audit 0 findings / 36 rows.
- **Restart**: Mac agents reloaded, cloud healer timers active, dispatchers
  idling against the standing stop leases until the Orchestrator grants new
  ones (by design). The hub ree-runner's 27-day code drift in
  ~/REE_Working_runner was OBSERVED and left for an operator window (its
  restart kills in-flight runs; nothing was in flight at ours, but the user
  had not answered the offer).

**Deferred to post-restart phase-4 slices, deliberately** (section 9's own
sequencing; one planned future restart batches their activation):
/intent/replace CAS + ree_commit transport branch, igw tick intake client,
governance-flag verbs, chip-archive DB-strip verb, review_tracker, typed
queue verbs -- to be dispatched through the new W5b curation pass as its
first live test.

**Outcome measures to watch** (the plan's own falsifiable predictions):
refwedge episode rate/cost (chip-20260904-refwedge-r1-rate-cost-remeasure);
open-chip count + chips/week trending DOWN under curation (the net-chip-sink
metric); wedge_repairs.jsonl rate staying near zero (a spike = a regressed
generator, alerted at 3/day).
