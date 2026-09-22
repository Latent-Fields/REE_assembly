# Campaign curation proposal -- 2026-09-22

**THIS IS A PROPOSAL. It requires Orchestrator ratification before any part of it is acted on.**

Nothing in this document has been claimed, recorded as a campaign, dispatched, or started.
No `dispatch_campaigns.py add` was called. No `chip_ledger.py claim`, `resolve`, `spawn_task`
or `dismiss_task` was called. The producing session was read-only apart from this one file.

| | |
|---|---|
| Produced | 2026-09-22T09:00:10Z |
| Producing session | `curation-proposal-20260922` (TASK_CLAIMS claim opened 2026-09-22T08:54:46Z, resource = this file only) |
| Method | Step 1b of `.claude/skills/metaworker-orchestrate/SKILL.md` (four lanes, bundle by shared CLASS **or** shared SUBJECT RESOURCE, cap ~6) |
| Scope | every OPEN chip in the coordinator ledger at read time |
| Curation act | **NOT performed** -- recording a campaign belongs to the Orchestrator |

---

## 0. The two numbers Step 1b requires -- and the finding in them

Read from the coordinator (`GET /chip/list`), which is authoritative; the git file lags.

| Metric | Value |
|---|---|
| **OPEN chips right now** | **174** |
| **Chips RECORDED in the last 7 days** (`spawned_at` >= 2026-09-15) | **553** |
| Chips RESOLVED in the last 7 days (`resolved_at`) | **501** (396 `done`, 105 `withdrawn`) |
| **Net over the window** | **+52 -- the ledger is a NET SOURCE, not a sink** |

**Stated plainly, as Step 1b requires: curation is currently failing its stated purpose.**
Over the trailing week the fleet recorded 52 more chips than it resolved. That is not a
close call and it is not noise -- it is about one extra open chip every three hours,
sustained. Per Step 1b's own instruction ("If they trend UP across a week of curation, the
curation is failing its purpose; raise that as a decision chip rather than curating harder"),
**this belongs in the decision lane at the next attended cycle, not in a bigger curation pass.**

Two structural contributors, both visible in the age histogram and both worth naming before
anyone proposes "curate harder":

1. **The paced proposal generator is the single largest producer of open chips.** 38 of the
   174 open chips (22%) are `chip-proposal-exp-NNNN-paced`, auto-paced back into the workset
   from the 2026-09-01 `proposal_tick` backlog. Each one is a genuine SCIENCE item that must
   be dispatched individually and cannot be bundled, so the lane that is *forbidden* from
   bundling is also the lane being refilled automatically. This is an intake-rate question,
   not a curation question.
2. **Auto-detector chips re-fire by generation.** Four `chip-daemondrift-*` are at generations
   3, 3, 4 and 7; the queue-floor report chip is at generation 13. Their own prompts say the
   recurrence count means the symptom fixes are not holding and route them to
   `/metaworker-learning` instead of another instance fix. Re-dispatching these individually
   is exactly the loop Step 1b exists to stop.

Age distribution of the 174 open chips (days since `spawned_at`):

| Age | 0-1d | 2-4d | 5-7d | 8-14d | 15-40d |
|---|---|---|---|---|---|
| Count | 35 | 75 | 25 | 24 | 15 |

---

## 1. Lane totals

| Lane | Count | Note |
|---|---|---|
| SCIENCE (dispatch first, individually, never bundled) | 96 | 38 paced proposals + 58 substrate / queue / lit / claim-synthesis items |
| CAMPAIGN-BUNDLE | 32 | 7 proposed bundles, all <= 6 members |
| HOLD | 25 | every one carries a reason AND a review cadence (section 4) |
| ABSORBED | 19 | 4 already landed; 15 owned by a named workstream (section 5) |
| TELEMETRY (`kind: report` / standing row -- never dispatched, never bundled) | 2 | `chip-queuefloor-fleet-g13`, `session-start-orchestrator` |
| **Total** | **174** | every open chip is in exactly one lane |

---

## 2. STALE-PREMISE FLAGS -- do not bundle these, and do not dispatch them as written

Flagged separately per the curation brief. A bundle built on a stale premise wastes a whole
session, so these are surfaced rather than laned into work.

### 2.1 Four chips whose work has ALREADY LANDED (verified this session, at `origin/main`)

These should be **resolved `done` by the Orchestrator**, not dispatched. Each was verified
against `origin/main`, not inferred:

| Chip | Evidence it is done |
|---|---|
| `chip-20260922-trunk-red-pinned-corpus-lints` | All three named lints are green on `ree-v3 origin/main`. Its three children landed as `9d10fce` (frozen-z_goal family pin 33->34), `de2e276` (r0z pin held at 150), `293349a` (dsp pin held at 0). The parent chip is fully covered. |
| `chip-20260922-exq541d-precondition-recomputability` | `ree-v3 de2e276` -- the 541d firing was adjudicated a FALSE POSITIVE and `_nan_drop_subsets()` narrows branch (e); pin held at 150 with an identical fired set. |
| `chip-20260922-exq1066-dryrun-keyed-point` | `ree-v3 293349a` -- `SEEDS`/`COMMIT_WINDOW` numeric coincidence adjudicated a false positive; precondition (5) narrowed to axis-derived operands; pin held at 0. |
| `chip-20260919-mech018-trunk-red-flag-registry-and-substrate-index` | Both contracts named in its own STOP-CHECK now pass at `origin/main` (`HEAD == origin/main == 293349a`, `tests/` clean): `tests/contracts/test_from_dims_flag_reachability.py` **23 passed**, `tests/docs_integrity/test_wi1_substrate_split_index_integrity.py` **5 passed**. Note the chip's STOP-CHECK also quotes the second file at the wrong path (`tests/contracts/...` -- it actually lives under `tests/docs_integrity/`), so a worker following it literally would have got `file or directory not found` and could have read that as an error rather than as "already green". |

This is 4 of the 6 chips I would otherwise have bundled as a trunk-RED campaign. **The
already-landed check was worth more than the bundling**, exactly as the brief predicted.

### 2.2 One chip whose premise was re-diagnosed two days later, by a second chip

- `chip-20260920-worktree-edit-guard-workrepo-false-twin` asks to **stop the guard firing** on
  work-repo paths.
- `chip-20260922-worktree-guard-false-twin-message` (raised 2 days later, on the same file and
  the same two lines) measured it and concluded the **firing is correct and deliberate** --
  the `os.path.isdir(twin_parent)` clause exists so a `Write` creating a NEW file in a shared
  dir fires -- and that only the **message** at line ~220 is false.

Verified at `origin/master` this session: line 206 is
`if not (os.path.exists(twin) or os.path.isdir(twin_parent)):` and line 220 is the
unconditional `"The same file exists in your own worktree at:"` string. **The newer diagnosis
is the correct one; the 09-20 framing is superseded.** They are bundled together in B2 below
*with the newer chip named as authoritative*, because dispatching the older one as written
would remove a deliberate clause.

### 2.3 One chip whose premise was probably cleared by this morning's hub restart -- UNVERIFIED

`chip-daemondrift-ree-cloud-1-ree-coordinator-g3` (raised 2026-09-20T10:30Z, "1.0d stale").
The resolution note on `chip-20260918-decision-hub-restart-id-collision` records that at
**2026-09-22T06:41:02Z** `ree-coordinator` was restarted on `ree-cloud-1` (PID 3667893 ->
392535) and the hub's `ree-v3` was fast-forwarded `65806e0b` -> `bfad374196`. I confirmed
locally that `bfad374196` is an ancestor of `origin/main` and only 3 commits behind it, so
the hub's code is current as of ~2h ago.

**I could not verify the daemon's live state**: `ssh ree-cloud-1` failed with
`Could not resolve hostname` -- the WireGuard tunnel is down on this box. So this is a
*likely-stale* premise, not a proven one. The two sibling chips
(`ree-sync-daemon-g4`, `ree-explorer-g7`) were NOT restarted by that note, though their code
on disk moved with the fast-forward. **The Orchestrator should re-check all three with the
tunnel up before doing anything with them.** All four daemon-drift chips are laned HOLD.

### 2.4 One premise that has gone stale in the *helpful* direction

`chip-20260918-mech204-f1-substrate-queue-amend` says it is "blocked by a live governance
claim on 2026-09-18" (`task_claim.py open` exited 3 against the `governance-20260918` pause
claim). **There is no governance claim active now** -- `task_claim.py list --status active`
returns 6 claims and none is a `governance-*` lock. That blocker is gone; the chip is
dispatchable. Laned SCIENCE.

### 2.5 A stranded artefact found while checking a bundle -- worth the Orchestrator's attention

The IGW-239 session (stale claim, 72h) left
`ree-v3/experiments/v3_exq_1062_mech055_affect_channel_separation_diagnostic.py` **untracked
(`??`) in the shared `ree-v3` main checkout**, and `V3-EXQ-1062` does not appear in
`origin/main`'s `experiment_queue.json`. Two consequences: (a) 72 hours of work is stranded
and unreferenced; (b) several corpus-lint contracts **scan `experiments/` on disk**, so this
untracked file silently participates in any corpus verdict run from the main checkout. That
is the exact hazard `chip-20260922-trunk-red-pinned-corpus-lints` warns about in its own
STOP-CHECK ("the shared ree-v3 main checkout always carries other sessions' uncommitted and
untracked experiment scripts ... its verdict is INADMISSIBLE in both directions"). This is
the reason B7 is proposed as the first bundle to run.

---

## 3. Proposed CAMPAIGN-BUNDLEs

Seven bundles, 32 members, none over 6. Every bundle states **one** justification -- class
**or** subject resource, never both -- as the ratified rule requires.

Every `task_claim.py check` below was **run in this session** at ~2026-09-22T08:58Z, read-only.
All seven came back clean. There are **no live campaigns** in `dispatch_campaigns.json` right
now (29 entries, all `resolved` / `expired` / `withdrawn` / `launched`-and-expired), so no
proposed member is already inside another live campaign.

---

### B7. IGW stalled auto-spawn sessions 239 + 246 -- **RUN THIS ONE FIRST**

- **Justification: shared SUBJECT RESOURCE** -- the two stalled IGW sessions `IGW-20260919-239`
  and `IGW-20260918-246` and the TASK_CLAIMS rows they left behind.
- **Members (4):**
  - `chip-staleclaim-igw-239-mech055-exq-1062-20260919T013240Z`
  - `chip-igw-239-proposal-for-mech-055`
  - `chip-staleclaim-igw-246-literature-proposal-fo-20260918T230957Z`
  - `chip-igw-246-literature-proposal-for-mech-050`
- **Resource union (`--resources`):**
  `ree-v3/experiments/v3_exq_1062_mech055_affect_channel_separation_diagnostic.py`
  `ree-v3/experiment_queue.json`
  `REE_assembly/evidence/literature/targeted_review_connectome_mech_050`
- **`task_claim.py check` (run now):** **exit 0, with three NOTEs -- not a refusal.** Verbatim:
  - `igw-246-literature-proposal-for-mech-050` (2026-09-18T23:09:57Z) also names
    `REE_assembly/evidence/literature/targeted_review_connectome_mech_050` -- *scope overlap only*
    (a directory resource, so not arbitrated);
  - `igw-239-mech055-exq-1062` (2026-09-19T01:32:40Z) also names the 1062 driver -- **stale
    (older than 6h)**, so excluded from arbitration;
  - `eloquent-jepsen-5f6242` (2026-09-21T04:49:02Z) also names `ree-v3/experiment_queue.json`
    -- **stale (older than 6h)**; task = "Diagnose V3-EXQ-1066 runner ERROR and re-queue a
    lettered fix". This is a **third** rival the bundle would meet and was not in my original
    read of the ledger.

  So `check` does not stop this bundle -- but two of the three rivals ARE its subjects, and
  both are classified bucket `U_undetermined` by `audit_stale_claims.py` (explicitly *not*
  auto-closable). **Treat all three as stale rivals to be adjudicated, not raced.** The
  `eloquent-jepsen` one is not in this bundle's scope and should be reported to the user
  rather than cleared by this session.
- **Already-landed check, per member:**
  - `chip-igw-246-literature-proposal-for-mech-050` -- **WORK LANDED**: `REE_assembly 6491ae5c7ba`
    ("lit-pull MECH-050 (IGW-246, EVB-1410): 5 entries on functional locality vs columnar
    geometry"). The claim was never closed. This is a textbook **landed-unclosed** row.
  - `chip-staleclaim-igw-246-...` -- resolves with the above.
  - `chip-igw-239-proposal-for-mech-055` -- **WORK NOT LANDED**: `V3-EXQ-1062` absent from
    `origin/main:experiment_queue.json`; the driver is untracked in the shared checkout
    (section 2.5). Needs a judgement call: land it, or archive it and withdraw.
  - `chip-staleclaim-igw-239-...` -- resolves with the above.
- **Fit:** **Sonnet, ~45 min** for the 246 half (close a landed-unclosed claim with
  `--from-commit 6491ae5c7ba`). The 239 half needs **Opus judgement**: deciding whether a
  72h-old untracked experiment driver is landed, re-run, or abandoned is an evidence call, not
  a bookkeeping one. Recommend splitting, or running the whole bundle on Opus.
- **Unsafe right now?** Two stale-but-`active` rival claims, by construction. Nothing else.

---

### B1. Phase-4 routed-path writer compliance

- **Justification: shared CLASS** -- findings of `scripts/audit_routed_path_writers.py`; one
  plan of record (`REE_assembly/evidence/planning/phase4_routing_compliance_20260918.md`).
- **Members (4):**
  - `chip-routedwriter-umbrella-task-claims-json`
  - `chip-routedwriter-ree-assembly-igw-assignments-json`
  - `chip-routedwriter-ree-assembly-inter-governance-workset-v1-json`
  - `chip-routedwriter-ree-assembly-inter-governance-workset-md`
- **Deliberately EXCLUDED:** `chip-routedwriter-umbrella-workspace-state-md`. Its unrouted
  writer is `scripts/rotate_workspace_state.py`, a whole-file rotation against an append-only
  endpoint -- and the chip's own text says such a writer "needs the verb built first ... chip
  that instead of forcing a call site". That verb is `chip-20260918-phase4-ws-rotation-verb`,
  a member of B5. So this chip is **ABSORBED by B5**, not a B1 member. Dispatching it here
  would have produced a forced call site against a verb that does not exist.
- **Resource union (`--resources`):**
  `scripts/prune_task_claims_done.py` `scripts/session_startup_checklist.py`
  `REE_assembly/scripts/igw_assignments_lib.py` `REE_assembly/serve.py`
  `REE_assembly/scripts/generate_inter_governance_workset.py`
  `REE_assembly/scripts/assembly_coordinator.py`
- **`task_claim.py check` (run now):** clean -- "no active claim overlaps" all six. No rival,
  live or stale.
- **Already-landed check:** **none landed.** I re-ran `audit_routed_path_writers.py` read-only
  this session (2026-09-22T08:58:44Z, 240 files scanned): it reports exactly these 5 routed
  paths still failing, with exactly the writer/line lists the chips quote. Nothing has moved.
- **Fit:** **Sonnet, ~45 min/item.** Each item is "read the named lines, decide real writer vs
  false positive, and if real add a gated call site through `assembly_coordinator.py`". The
  chips themselves say a finding is a shortlist and false positives are expected, so
  "verified false positive, resolved with a record" is a valid per-item outcome.
- **Unsafe right now?** One caution to carry into the brief: `REE_assembly/serve.py` is the
  live Explorer server. A call-site change there should be landed with `serve.py` restarted
  afterwards, and the brief should say so.

---

### B2. `worktree_edit_guard.py` false-twin advisory

- **Justification: shared SUBJECT RESOURCE** -- `scripts/worktree_edit_guard.py`.
- **Members (2):**
  - `chip-20260922-worktree-guard-false-twin-message` -- **authoritative framing**
  - `chip-20260920-worktree-edit-guard-workrepo-false-twin` -- superseded framing, see 2.2
- **Resource union:** `scripts/worktree_edit_guard.py` `scripts/test_worktree_edit_guard.py`
  `CLAUDE.md`
- **`task_claim.py check` (run now):** clean, no rival.
- **Already-landed check:** **not landed.** At `origin/master`, line 206 still reads
  `if not (os.path.exists(twin) or os.path.isdir(twin_parent)):` and line 220 still carries the
  unconditional `"The same file exists in your own worktree at:"` message.
- **Fit:** **Sonnet, well under 45 min** -- make the message conditional on which clause
  matched, plus a test. Two chips, one fix; the second resolves `done` with the same sha.
- **Unsafe right now?** `CLAUDE.md` is in the resource union because point 5b of the
  "Worktree / Chipped Sessions" section describes this guard's behaviour. **If the wording of
  that section changes, GOV-HELDOUT-1 applies** (3 held-out cases where old and new wording
  differ). The brief must say so. Prefer changing only the script's message and leaving
  `CLAUDE.md` alone, which keeps this a pure Sonnet item.

---

### B3. substrate-queue gate correctness

- **Justification: shared SUBJECT RESOURCE** -- `REE_assembly/evidence/planning/substrate_queue.json`
  and the gate that reads it.
- **Members (4):**
  - `chip-20260917-substrate-paths-unmatched-prefix` (7 `substrate_paths` across 4 entries whose
    leading segment can never match a driver import -- those entries protect nothing)
  - `chip-20260917-substrate-path-gate-closed-test-divergence` (forward half tightened
    2026-09-16, backward half not)
  - `chip-20260918-proposaltick-substrate-filter-inert` (pre-filter measured 0/3 and 0/11)
  - `chip-sqdrift-sd-086` (SD-086 reads `pending_implementation` but `resolved_build_chip` says
    it landed)
- **Resource union:** `REE_assembly/evidence/planning/substrate_queue.json`
  `REE_assembly/scripts/proposal_tick.py` `REE_assembly/scripts/substrate_path_gate.py`
- **`task_claim.py check` (run now):** clean, no rival.
- **Already-landed check:** not landed -- no commit in `REE_assembly origin/master` since
  2026-09-17 touches the path gate or these `substrate_paths`. **Caveat, stated honestly:** I
  verified this from the commit log, not by re-running the gate, because re-running
  `proposal_tick` is a write. The dispatched session must re-verify per item.
- **Fit:** **Sonnet for the three code items; the 4th (`chip-sqdrift-sd-086`) needs a
  judgement call** on which of two disagreeing records is true, so it may hand back.
- **Unsafe right now?** `substrate_queue.json` is an **exposed whole-file read-modify-write
  target** (CLAUDE.md, Exposed files). The brief must carry the narrow-structural-append rule
  and the `ree_commit.py` per-item delta check. Also: `chip-20260918-proposaltick-substrate-filter-inert`
  changes what `proposal_tick` emits, and `proposal_tick` is what produces the 38 paced
  proposal chips -- so this item has **intake-rate consequences for section 0's finding**, and
  should be sequenced knowingly rather than as routine housekeeping.

---

### B4. Test-gate measurement hygiene

- **Justification: shared CLASS** -- defects in the instruments that produce test verdicts
  (not in the code under test).
- **Members (6):**
  - `chip-20260919-provenance-pin-test-claim-session-link` (umbrella corpus red: missing
    `pin_scripts_dir()`)
  - `chip-20260918-scriptscorpus-verdict-id-collision` (33/35 corpus files pin the canonical
    `scripts/` dir, so a worktree run exercised the old copy)
  - `chip-20260916-scriptscorpus-item-e-recheck-after-0919` (re-count clean runs after 09-19)
  - `chip-20260918-corpusscan-perworker-xdist-floor` (session-scoped fixture re-paid per xdist
    worker, ~2 min x4)
  - `chip-20260917-test-suite-baseline-stale` (CLAUDE.md + routing doc quote a 6-week-old
    baseline; suite has grown ~73%)
  - `chip-maconlypin-dlaptop-test-burned-queue-entry-detector` (Mac-local pin red)
- **Resource union:** `scripts/run_scripts_tests.sh` `scripts/test_claim_session_link.py`
  `ree-v3/tests/conftest.py` `ree-v3/tests/contracts/test_burned_queue_entry_detector.py`
  `docs/reference/ree-v3-test-suite-routing.md` `CLAUDE.md`
- **`task_claim.py check` (run now):** clean, no rival.
- **Already-landed check, per member:**
  - `provenance-pin-test-claim-session-link` -- **NOT landed**: `grep pin_scripts_dir
    scripts/test_claim_session_link.py` returns nothing.
  - `scriptscorpus-verdict-id-collision` -- **NOT landed**; the guard commit it refers to
    (`50cb64874`) is in, but the corpus verdict from the main checkout has not been recorded.
  - `scriptscorpus-item-e-recheck` -- **not landed**, and the 2026-09-19 run it waits on has
    now happened, so it is due.
  - `corpusscan-perworker-xdist-floor` -- **not landed**.
  - `test-suite-baseline-stale` -- **not landed**: `CLAUDE.md` still quotes
    "~13m12s / ~3558-test idle-hub baseline", while the 2026-09-19 hub run measured
    **6411 tests** (3 failed / 6408 passed). The stale figure is real and is ~80% low.
  - `burned-queue-entry-detector` -- **NOT landed, and still RED**. I ran it: `1 failed,
    10 passed, 15 subtests passed`; `test_c7_signal_stays_small_and_the_lost_set_is_pinned`
    asserts `21 not less than or equal to 20`.
- **Fit:** **Sonnet for five; the sixth needs escalation.** The burned-queue cap is guarded by
  its own docstring: *"Raising it is a real decision about what this assertion is for; do not
  do it merely to get to green."* A worker must adjudicate the 21st finding (genuine burn vs
  false positive) and, if genuine, **stop and raise a `kind: decision` chip** about the cap
  rather than bumping it. The brief must say this in those words.
- **Unsafe right now?** `CLAUDE.md` is in the union for the baseline figure. Correcting a
  *measured number* is not a standing-rule change, so GOV-HELDOUT-1 does not fire -- but the
  brief should say that explicitly so the worker does not either skip the edit or over-apply
  the gate. Also: any new baseline must be measured on a **verified-idle** box per
  `docs/reference/ree-v3-test-suite-routing.md`, not taken from a contended run.

---

### B5. Coordinator-side routing verbs

- **Justification: shared SUBJECT RESOURCE** -- the coordinator's write surface
  (`ree-v3/coordinator/`) and the clients that must route through it.
- **Members (6):**
  - `chip-20260918-phase4-chip-archive-verb` (build the archive verb `cmd_archive` should route to)
  - `chip-20260918-phase4-ws-rotation-verb` (build the rotation verb; **absorbs**
    `chip-routedwriter-umbrella-workspace-state-md`)
  - `chip-20260918-intent-log-read-endpoint` (read-only `GET /intent/log`)
  - `chip-20260919-refwedge-f4-handoff-coordinator-transport` (F4 of the user-approved D2 set)
  - `chip-20260916-chipledger-claim-history-previous-host` (record `previous_claimed_host`)
  - `chip-20260910-gflag-phase2a-coordinator-shadow` (governance_flag shadow -- the last big
    local git writer driving REE_assembly divergence)
- **Resource union:** `ree-v3/coordinator/` `scripts/chip_ledger.py`
  `scripts/rotate_workspace_state.py` `scripts/coordinator_transport.py`
- **`task_claim.py check` (run now):** clean, no rival.
- **Already-landed check:** none landed. `chip-20260919-refwedge-f4-...` states F1/F2/F3/F5
  landed in its own session and F4 was chipped precisely because it needs a coordinator change
  plus a hub deploy.
- **Fit:** **NOT a Sonnet bundle. Opus, and probably not as a single 45-min/item run.**
  Reasons, stated so the Orchestrator can disagree with evidence rather than vibes:
  1. Every item needs a **hub deploy** to take effect, and the hub is the sole git writer for
     the coordination-data plane. A half-deployed verb wedges the writers.
  2. `ree-v3/coordinator/` is executable-code plane -- CLAUDE.md's Git Policy says a
     multi-session or half-landing-hazardous change there belongs on a short-lived
     `integration/<slug>` branch with the full contract suite + `coordinator/phase3_preflight.py`
     as the merge gate, run on a cloud worker.
  3. `chip-20260910-gflag-phase2a-coordinator-shadow` explicitly needs a *different* route from
     the other migrated files because compare-and-swap cannot allocate flag ids -- that is a
     design question, not an implementation.
  **Recommendation: do not dispatch B5 as a bundle. Ratify it as a named workstream** with an
  `integration/` branch, or split the one genuinely safe read-only item
  (`chip-20260918-intent-log-read-endpoint`, a GET endpoint) out on its own.
- **Unsafe right now?** The WireGuard tunnel to `ree-cloud-1` is down from this box
  (`ssh: Could not resolve hostname ree-cloud-1`). **Nothing in B5 can be deployed or verified
  until that is restored.** That alone makes B5 unsafe to launch this cycle.

---

### B6. Audit/detector script defects

- **Justification: shared CLASS** -- a hygiene or intake detector that mis-measures, where
  the fix is in the detector, not in what it watches.
- **Members (6):**
  - `chip-20260918-disk-space-audit-gap` (nothing in the fleet watches free disk; below ~2GB
    the Bash tool dies in every session on the box)
  - `chip-20260922-unqueued-auditor-banner-screen-v2` (auditor cannot see DO-NOT-QUEUE banners;
    that gap let V3-EXQ-1066 burn 48 min of cloud compute)
  - `chip-20260917-enablement-audit-row-splitting` (one multi-line ssh error counted as three
    rows; defect written down 15 days ago)
  - `chip-20260921-phase-leak-check-at-thought-intake` (13 of 18 commits behind 35 phase leaks
    were thought-intake registrations; add the check at intake)
  - `chip-20260922-convergence-intake-schema-drift` (validator already rejects two
    REE_convergence intakes: an `evidence_status` outside the enum + two stray keys)
  - `chip-20260920-indexer-adjudication-applies-false` (indexer stamps a false
    `precondition_unmet` on `applies:false`; hit V3-EXQ-1069)
- **Resource union:** `scripts/dev-doctor.sh` `scripts/audit_unqueued_experiment_scripts.py`
  `REE_assembly/scripts/mitigation_enablement_audit.py`
  `REE_assembly/docs/thoughts/scripts/` `REE_convergence/handoff/`
  `REE_assembly/scripts/build_experiment_indexes.py`
- **`task_claim.py check` (run now):** clean on the three checked paths
  (`dev-doctor.sh`, `audit_unqueued_experiment_scripts.py`, `mitigation_enablement_audit.py`);
  **the Orchestrator should re-run `check` on the full six-path union before recording**, since
  the last three were derived from chip text rather than from a declared `--resources` line.
- **Already-landed check:** none landed. The two 2026-09-22 members are hours old; the other
  four have no touching commit in their repo's log.
- **Fit:** **Sonnet, ~45 min/item**, with one exception:
  `chip-20260920-indexer-adjudication-applies-false` touches
  `build_experiment_indexes.py`, i.e. **evidence index regeneration**. CLAUDE.md's *Narrow
  Edits Only* rule applies in full (snapshot `git status --porcelain` before any regen; back
  out only paths that were CLEAN before). Consider moving that one item out of the bundle.
- **Unsafe right now?** Nothing blocking. Note only that the members span three repos
  (umbrella, `REE_assembly`, `REE_convergence`), so per-item landing must name the right
  `--repo` each time.

---

## 4. HOLD lane -- 25 chips, each with a reason AND a cadence

A hold with neither is the stale-claim problem one level up, so both are stated for every row.

### 4a. Gated on another piece of work (5)

| Chip | Reason | Review cadence |
|---|---|---|
| `chip-20260814-queue-causal-sleep-matched-arm` | needs sleep cadence T + DV set from `chip-20260812-exq920-...-retrospective` | when the 920 retrospective lands. **39 days old** -- if that chip is already resolved or withdrawn, this is orphaned and should be re-laned or withdrawn next cycle |
| `chip-20260818-mech152-redesign-queue-gated` | Step 2.5c corrupting gate on the open ContextMemory addressing-degeneracy entry (GFLAG-0044) | next governance cycle that touches GFLAG-0044 |
| `chip-20260902-r5-per-repo-divergence-threshold-gated` | deliberately deferred until R4's puller changes the distribution it would sample | when R4 lands |
| `chip-20260919-mech561-release-after-1043a` | gated on V3-EXQ-1043a; the 1043b successor is itself still being queued | when V3-EXQ-1043b reports |
| `chip-20260920-p0-readiness-gate-incremental` | carries a coupled ask ("propose the matching red-team rule") that is a standing-rule change requiring GOV-HELDOUT-1 | next cycle; **split the gate build from the rule change before dispatching** |

### 4b. Time-gated re-measurements (5)

| Chip | Reason | Review cadence |
|---|---|---|
| `chip-20260911-remeasure-retry-default-flip` | 7-day readback of the 2026-09-11 push-retry default flip | **due now** -- promote to a bundle next cycle |
| `chip-20260915-token-split-remeasure-b2` | one week after the 2026-09-14/15 reword landed | **due today (2026-09-22)** -- promote next cycle |
| `chip-20260914-token-split-read-channel-count` | the measuring instrument miscounts Read-channel loads; must be fixed before the re-measure is meaningful | review **together with** the row above -- these two are a coupled pair and must not be dispatched separately |
| `chip-20260920-strandedwt-scratch-remeasure-after-1004` | design says not before 2026-10-04 | 2026-10-04 |
| `chip-20260920-autopull-fossil-reconcile-7day-readback` | 7-day readback of a 2026-09-20 change | 2026-09-27 |

### 4c. Decision-shaped, belongs in Step 3b not in a worker (4)

| Chip | Reason | Review cadence |
|---|---|---|
| `chip-20260915-mech027-status-token` | "decide and record" a substrate status token | raise as `AskUserQuestion` next attended cycle |
| `chip-20260917-reconciler-nondict-entry-wedge` | crash-vs-skip on a non-dict registry entry is a policy call on the 2-minute materializer tick | next attended cycle |
| `chip-20260920-strandedwt-underscore-scratch-blindspot-decision` | its own text says "measure, ask the user, build only on yes" | next attended cycle |
| `chip-20260922-account-status-desktop-app-surface-gap` | touches account/credential surfaces; detection is automatable, remediation is user-only | next attended cycle |

### 4d. User-attached Remote-Control sessions -- not dispatchable (2)

| Chip | Reason | Review cadence |
|---|---|---|
| `chip-20260826-representation-authority-selection-bottleneck` | an ongoing research session the user attaches to directly; a headless worker cannot do what it is for | offer to the user at the next attended cycle |
| `chip-20260826-thought-digestion-wave-grouping-design` | same shape, design rather than research | offer to the user at the next attended cycle |

### 4e. Recurrence-flagged auto-detectors -- route to `/metaworker-learning`, not to an instance fix (4)

All four carry the same self-instruction in their own prompt text and are Mac-only
(`THIS CHIP MUST RUN ON DLAPTOP`).

| Chip | Reason | Review cadence |
|---|---|---|
| `chip-daemondrift-ree-cloud-1-ree-coordinator-g3` | gen 3; premise **likely cleared** by the 2026-09-22T06:41Z restart (section 2.3) but UNVERIFIED -- tunnel down | verify with the tunnel up, this cycle |
| `chip-daemondrift-ree-cloud-1-ree-sync-daemon-g4` | gen 4; not restarted by that note, though its code moved with the fast-forward | verify with the tunnel up, then `/metaworker-learning` |
| `chip-daemondrift-ree-cloud-1-ree-explorer-g7` | **gen 7** -- six prior resolutions did not hold; the strongest root-cause signal in the ledger | `/metaworker-learning`, next pass |
| `chip-daemondrift-dlaptop-mac-runner-g3` | gen 3; and the Mac runner is **deliberately off**, so "drift" on it may be expected rather than a fault | `/metaworker-learning`, next pass -- check the deliberately-off premise first |

### 4f. IGW auto-spawn trackers, self-resolving (3)

`chip-igw-241-proposal-for-mech-078`, `chip-igw-244-literature-proposal-for-mech-078`,
`chip-igw-246-literature-proposal-for-mech-042`. **Reason:** each is an auto-spawned headless
IGW session tracker whose own tldr says "No action needed unless it stalls or errors"; none
has a stale claim against it. **Cadence:** review when a `chip-staleclaim-*` fires for its
claim, or at 72h, whichever comes first -- which is exactly how 239 and 246-mech-050 surfaced
into B7.

### 4g. Scoping-first (1)

`chip-20260908-compute-ledger-v2`. **Reason:** building a new durable ledger with a persistent
state surface is a design decision, not a ~45-min housekeeping item. **Cadence:** raise as a
scoping question at the next attended cycle.

### 4h. Standing-rule edit, no bundle class (1)

`chip-20260916-campaign-gc-skill-docs`. **Reason:** it edits the GC-gate wording in TWO
`SKILL.md` files (`session-land` Phase 2c gate 1, `metaworker-dispatch` Step 4c), which is a
standing-rule change -- **GOV-HELDOUT-1 applies** (>= 3 held-out cases where old and new
wording give DIFFERENT answers, and the outcome recorded on the edit). It shares a class with
no other open chip, so bundling it would be bundling by vibes. **Cadence:** next cycle -- it is
a good single Opus item, not a Sonnet bundle member.

---

## 5. ABSORBED lane -- 19 chips

### 5a. Already landed (4)

See section 2.1 for the evidence. These should be **resolved `done`** by the Orchestrator,
citing the shas given there, rather than dispatched:
`chip-20260922-trunk-red-pinned-corpus-lints`,
`chip-20260922-exq541d-precondition-recomputability`,
`chip-20260922-exq1066-dryrun-keyed-point`,
`chip-20260919-mech018-trunk-red-flag-registry-and-substrate-index`.

### 5b. Absorbed by another open chip (1)

`chip-routedwriter-umbrella-workspace-state-md` -> `chip-20260918-phase4-ws-rotation-verb` (B5).

### 5c. `/governance` work -- report inline, never chip (6)

Per CLAUDE.md's chip-scope rule, the governance cycle re-derives its own worklist each pass,
so a chip here is a second and staler tracker for an item that already has an owner:

`chip-20260909-govapply1-unresolvable-35-manifests`,
`chip-20260914-q081-exq865-governance-disposition`,
`chip-20260911-e1-rollout-closure-owner`,
`chip-20260915-mech542-543-register-rows`,
`chip-20260910-gflag0245-runpack-metrics-heal`,
`chip-20260917-shp4-bearson-provenance-join`.

**Note the direction of this call.** These are laned ABSORBED because the *work-type* is
governance, not because a governance session raised them. The four-revision scope history of
that rule is why the distinction matters: a `/queue-experiment` re-run surfaced by a
governance session is still queue-experiment work and stays SCIENCE. Nothing in section 3 or
section 6 was moved here on session-type grounds.

### 5d. Metaworker / Orchestrator workstreams (8)

`chip-20260920-red-verdict-second-pass-triage` (this *is* Step 1b at another grain -- 48 chips
carrying RED pre-flight verdicts, 43 distinct claims, ~35 with no owner; it belongs to the
Orchestrator, not to a dispatched worker),
`chip-metaworkergc-sweep-26-f9d35493b94b2e0f`,
`chip-20260909-cloud3-autostash-gc-triage`,
`chip-20260920-cloud5-coordinator-token-inline-unit`,
`chip-20260901-dispatch-bg-wait-ceiling-kills-fanout`,
`chip-20260919-fleethealth-declared-stopped-but-dispatching`,
`chip-20260920-dispatch-lane-launcher-build`,
`chip-20260920-cycle-trigger-story-reconcile`.

These are leases, wrappers, box infra and dispatch mechanics -- the Orchestrator's own
territory. Naming them here is the report; none should be spun out as an independent worker.

---

## 6. SCIENCE lane -- 97 chips, dispatched individually, never bundled

Not enumerated in full here (the ledger is the list). The shape, for ratification:

| Sub-population | Count | Note |
|---|---|---|
| `chip-proposal-exp-NNNN-paced` | 38 | auto-paced `/queue-experiment` proposals from the 2026-09-01 `proposal_tick` backlog; substrate readiness is explicitly NOT pre-checked, so "not buildable yet" is a valid per-item outcome |
| `/implement-substrate` builds | ~23 | MECH-035/039/037/065/468/157/003/330/002/213/206, SD-032a, z_world channels, etc. |
| `/queue-experiment` (non-paced) | ~19 | MECH-465 conjunct-3 and P2 LLRR, MECH-043 sweep, MECH-428 alpha sweep, SD-024 redesign, V3-EXQ-1043b, SD-036 matrix, queue refill, etc. |
| `/claim-synthesis` | 4 | MECH-349 reframe, language-cluster text repair, MECH-064 principle-vs-mechanism, P4 falsifier tranche 2 |
| `/lit-pull` | 3 | ARC-099 Michel 2023 full text, ARC-103 symbolic-inference harm, Butola published methods |
| spikes / probes | ~9 | ARC-046 reachability, INV-109 endpoint hash, Q-081 telemetry audit, P3-R5 separability, etc. |

**Two things the Orchestrator should know before dispatching from this lane.**

1. **`dispatch_campaigns.py add --lane science` requires a recorded pre-flight and refuses RED
   outright.** 97 science chips is far more pre-flight than one cycle can pay for. The 1d-iii
   pre-flight is a ~220k-token read-only Sonnet pass; the W5-S2a counter-case is ~535k tokens
   and zero runs for skipping it. **Ratify a per-cycle science budget rather than trying to
   lane all 97.**
2. **The pre-flight backlog is already a known problem.**
   `chip-20260920-red-verdict-second-pass-triage` (laned ABSORBED, 5d) records 48 chips
   carrying a RED verdict across 43 distinct claims, of which only 8 are named in any
   `substrate_queue` `unblocks_claims`. That is ~35 claims with nobody moving them toward
   GREEN. Dispatching more science without working that backlog re-creates it.
3. **`chip-20260918-mech204-f1-substrate-queue-amend` is newly unblocked** (section 2.4) and is
   cheap -- a registry amend whose only blocker was a governance pause claim that has since
   closed. Good first science item if a cheap one is wanted.

---

## 7. What I would run first, and why

**B7 (IGW stalled sessions 239 + 246).**

Not because it is the biggest -- it is the smallest -- but because it is the only bundle whose
cost is **rising while it waits**, and the only one that is currently contaminating other
verdicts:

- Two `active` TASK_CLAIMS rows are 72h stale and classified `U_undetermined`, i.e. explicitly
  not auto-closable. Every future `task_claim.py check` against those paths returns exit 3 to
  somebody.
- One of the two (246) is a **landed-unclosed** row: the work is on `origin/master`
  (`REE_assembly 6491ae5c7ba`) and only the closure is missing. That half is minutes of work.
- The other (239) left an **untracked experiment driver in the shared `ree-v3` checkout**
  (section 2.5), and corpus-lint contracts scan `experiments/` on disk. So this stranded file
  is silently inside the denominator of any corpus verdict run from the main checkout --
  including the verdicts B4 exists to fix. Clearing B7 before B4 makes B4's measurements
  admissible.

Second: **B1 (routed-writer)** -- clean claim check, no rival, re-verified against a live
read-only audit run this session, genuinely Sonnet-sized, and the one bundle where I am
confident nothing has moved underneath it.

**Do not run B5 this cycle.** Every item needs a hub deploy and the WireGuard tunnel to
`ree-cloud-1` is down from this box.

---

## 8. Honest limits of this read

- **The tunnel was down.** `ssh ree-cloud-1` failed to resolve, so no daemon, service or hub
  state was verified directly. Sections 2.3 and B5 depend on that and say so.
- **Already-landed checks are per-member and evidence-bearing where I could run them** (B1 via
  a live audit run; B2 via `git show origin/master:`; B4 via two actual pytest runs and a
  `grep`; 2.1 via two pytest runs and three commit reads). For **B3** I checked the commit log
  only, because re-running `proposal_tick` is a write. Every dispatched session must still run
  its own START-TIME STOP-CHECK; the bundle-level check is additive, never a replacement (the
  2026-07-28 84-second triple-claim is why).
- **B6's resource union is partly derived from chip prose**, not from declared `--resources`
  lines. Re-run `task_claim.py check` on the full six-path union before recording it.
- **Lane assignment for ~10 chips is a judgement call**, chiefly on the governance-work
  boundary (5c) and on whether registry-mint chips are substrate work or housekeeping. Those
  are the rows to argue with first.

---

*Produced read-only by session `curation-proposal-20260922`. Ratification, recording and
dispatch belong to the Orchestrator.*
