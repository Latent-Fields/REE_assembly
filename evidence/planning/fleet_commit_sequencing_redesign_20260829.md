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
