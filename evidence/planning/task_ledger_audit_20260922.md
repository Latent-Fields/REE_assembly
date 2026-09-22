# Durable task ledger audit -- 2026-09-22

Generated 2026-09-22T19:17:09Z by session `ledger-audit-20260922`.
Subject: the 165 `open` chips in `TASK_CHIPS.json` (4,142 rows total: 3,241 done, 736 withdrawn).
Read-only audit. No chip was resolved, withdrawn or amended by this pass -- every disposition
below is a **recommendation** with the evidence that supports it.

---

## 0. The headline number is not a backlog

| Window | Spawned | Resolved | Net |
|---|---:|---:|---:|
| 2026-09-08 .. 2026-09-22 (15 d) | 994 | 958 | **+36** |

Throughput is ~66 chips/day and the ledger is **roughly in balance**. 112 of the 165 open chips
are under 7 days old; only 2 are over 30 days. So "165 open" is about 2.5 days of inflow, not an
accumulated graveyard, and only 1 open chip is claimed-but-unresolved
(`chip-20260922-matched-capacity-definition`, claimed today).

**Therefore: reducing the ledger means reducing INFLOW OF NON-ACTIONABLE CHIPS, not sweeping old
ones.** Section 4 names the three inflow sources worth closing.

Open chips by origin: `spawn_task` 69, `headless` 53, **`proposal_tick` 33**, `hygiene_tick` 6, `igw_tick` 4.

---

## 1. SCIENCE SIDE -- no longer needs to be done

### 1a. The entire `proposal_tick` bucket: 32 of 33 are non-actionable today (VERIFIED)

Joined by `claim_id` (per the recorded join rule -- the `NNNN` in the chip ref is **not** a
`proposal_id`), each paced chip's claim was checked against `claims.yaml` and
`experiment_proposals.v1.json`:

| Disposition of the claim's EXP proposal | Chips |
|---|---:|
| `blocked_substrate`, with an explicit `release_condition` already recorded | 19 |
| `executed` (the experiment has already been run) | 2 |
| `skipped` | 1 |
| no `EXP-` proposal exists at all (LIT-only or none) | 4 |
| still `proposed` and genuinely open | **1** |

The one survivor is `chip-proposal-exp-0707-paced` (INV-022, EXP-0658) -- and even that is gated,
because `chip-20260909-mech004-signalmap-lit-findings` is holding a correction to INV-022's
collinearity failure signature (Haber's ascending spiral makes the signature fire on correct
behaviour). **No paced chip is queueable today.**

**Sub-bucket A -- withdraw outright, the claim type can never carry an experiment (11 chips).**
`0597 0603 0605 0607 0657 0669 0675 0677 0679 0681 0683`
Claims EXT-003/006/007/008, IMPL-008/016/019/023/025/026/027. Every one is
`external_failure_mode`, `implementation_note` or `reference_note`; **every one has no
`what_would_answer` at all**; and six carry a registry release_condition that says so in terms --
*"reference document -- no experiment is defined for it; do not mint"*, *"Do NOT re-offer ARC-120
as an experiment proposal"*, *"NOT RELEASED BY ANY SUBSTRATE BUILD"*. EXT-003 and EXT-007 already
have `executed` proposals. These cannot become GREEN by any amount of substrate work.

**Sub-bucket B -- withdraw as duplicate trackers (19 chips).**
`0494 0501 0515 0557 0560 0758 0760 0763 0798 0800 0804 0806 0810 0815 0822 0827 0845 0874 1222`
The proposal registry already holds the block *and* a machine-readable `release_condition` for
each, and it **re-derives every governance cycle**. The chip does not. This is the exact shape
CLAUDE.md already forbids: *"a chip is a second, staler tracker of an item that already has an
owner."* Withdraw pointing at the `release_condition`.

**Note, so the wrong reason is not re-cited:** four of these (0804/0810/0822/0827 =
MECH-023/028/038/042) carry a 2026-09-16 RED reading *"has NO what_would_answer"*. **That RED is
now stale** -- all four have a falsifier today (P4 tranche 1 landed it). They remain blocked, but
on substrate, not on a missing falsifier.

**Caveat on this whole section:** `blocked_substrate` set only in `manual_proposals.v1.json` is
reverted by the next regen. The code defect behind that was closed 2026-09-07
(`chip-20260907-proposal-status-revert-regen`, done). Spot-check one row after the next
`/governance` regen before trusting the durability of the status.

### 1b. Three IGW chips whose assignment already completed (VERIFIED)

| Chip | IGW ledger status | Outcome | Reaped |
|---|---|---|---|
| `chip-igw-246-literature-proposal-for-mech-042` | `completed_resumable` | USEFUL_LANDED | 2026-09-18 |
| `chip-igw-244-literature-proposal-for-mech-078` | `completed_resumable` | NO_OP | 2026-09-20 |
| `chip-igw-241-proposal-for-mech-078` | `completed_resumable` | NO_OP | 2026-09-20 |

Resolve `--status done`. (`chip-igw-216-substrate-ready-sd-pp-1` is genuinely `staged` and
awaiting human assent -- see 3d.)

### 1c. Two whose stated symptom has cleared

- **`chip-20260915-mech542-543-register-rows`** -- stated symptom was *"the traceability gate now
  exits 1 every run"*. Ran it: `check_backward_traceability.py` reports **OK, exit 0**
  (98 developmental claims, 17 exempt). MECH-542/543 carry no `developmental_need` field and are
  `implementation_phase: v4`, so the gate does not require rows for them. Verify how it went green
  (fix vs. field removal), then withdraw.
- **`chip-20260910-merge-substrate-queue-mint-batch`** -- the registry-write half is done:
  MECH-493, MECH-494, MECH-495 and MECH-354 all have `substrate_queue.json` entries. The residual
  is only the z_world overlap check, which belongs to the z_world campaign (3c).

**Withdraw/close candidates on the science side: 11 + 19 + 3 + 2 = 35 chips (21% of the open ledger).**

---

## 2. SCIENCE SIDE -- important or blocking

### 2a. The experiment queue is empty and the fleet is idle (VERIFIED)

`origin/main:experiment_queue.json` depth = **1**, and that one item (`V3-EXQ-1067`) is already
`claimed`. Every worker has nothing to pick up.
Owning chips: `chip-20260918-queue-refill-empty` and `chip-queuefloor-fleet-g13`.
The `-g13` suffix is load-bearing: this is **generation 13** of the same class, re-fired 12 times.
Its own text says to route it to `/metaworker-learning` for a root-cause pass rather than
re-fixing the instance. The root cause is visible in this audit: the proposal pipeline's only
candidate generator (`proposal_tick`) is producing chips of which 32/33 are unqueueable.

### 2b. The residue field is the convergent blocker, and nothing owns building it

`GFLAG-0344` (raised 2026-09-18, **still open**, claims MECH-105/005/024/023) records **thirteen
consecutive experiment refusals**, the last three converging on one organ:

- `RBFLayer.add_residue` is a **32-slot ring buffer** while harm fires on 62.5% of steps -- 895
  harm events into 32 slots is 28 wraps in 720 steps, so a divergent harm history *relocates*
  trained centres rather than adding to them;
- `kernel_bandwidth = 1.0` against a visited z_world manifold whose **max pairwise distance is
  0.1249**, leaving the field spatially near-uniform;
- MECH-105's completion signal is a sigmoid *of* residue cost, so its unreachable 0.75 threshold
  (achievable range is `(0, 0.5]`) is a scaling bug on the same quantity.

The flag said there was no substrate_queue entry for residue-field geometry. **That has since been
corrected** -- five entries now exist:
`residue-field-geometry-ring-bandwidth-neural-gating`, `residue-field-ring-capacity`,
`residue-field-kernel-resolution`, `residue-cost-untrained-neural-field`,
`residue-completion-signal-threshold-unreachable`.
**All five are `proposed_REGISTRATION_ONLY_not_a_build_authorisation`, `ready: false`.**

So the organ is registered, diagnosed, and **not authorised to build**, while experiment designs
against it keep being refused. This is the highest-leverage decision on the ledger and it is a
**user call, not a chip**: authorise a residue-field geometry build, or accept that the claims
resting on it stay blocked.

GFLAG-0344 also proposes a cheap curation-time check that would have caught 2 of 3 refusals in a
minute with no run: *does the DV's producer have an achievable range that crosses its consumer's
threshold?* The nearest open chip is `chip-20260922-preflight-a2-presence-vs-liveness`
("instantiated is not armed") -- fold it in there rather than minting a separate gate.

### 2c. Nineteen substrate entries are built but never validated

`substrate_queue.json` holds **19 entries at `implemented_pending_validation`**. Each owes exactly
one validation run. This is the answer to 2a: the queue is empty while nineteen ready-to-write
runs sit unwritten.

**Four of these are `severity: corrupting`, which means they are live `/queue-experiment` Step 2.5c
STOP-GATES** -- `implemented_pending_validation` counts as OPEN for that gate (SKILL.md:426):

| Entry | Status | Claims it blocks |
|---|---|---|
| `contextmemory-write-path-addressing-degeneracy` | impl_pending_validation | SD-017, ARC-045, MECH-166, MECH-152, **ARC-021** |
| `sd_blocked_agency_mismatch_floor_calibration` | impl_pending_validation (ready=true) | MECH-353, SD-029, MECH-112, SD-011, SD-019b |
| `SD-082` | impl_pending_validation | SD-078 |
| `MECH-320` | (none), ready=false | ARC-066 |

**The ContextMemory one is the most costly.** Three open chips are gated on it
(`chip-20260814-queue-causal-sleep-matched-arm`, `chip-20260818-mech152-redesign-queue-gated`,
`chip-20260911-arc021-h2-contextmemory-inplace-write`), plus MECH-067's EXP-0812 release
condition (`chip-proposal-exp-0845-paced`). Their 2026-09-14 REDs say the defect is *"confirmed
still open"* and cite GFLAG-0044 as unresolved -- **both readings are now out of date**:
GFLAG-0044 was resolved 2026-08-21, and the entry has moved
`pending_implementation` -> `implemented_pending_validation`. **The build has landed. What is owed
is a validation run, and nobody owns it.** One run releases five claims and four chips.

### 2d. V3-EXQ-1043b is the single gate on five claims

`chip-20260922-exq1043b-prereg-rank-coprimary` records the finding: 1043b gates MECH-538,
MECH-539, MECH-561, MECH-562 and (via a sequencing precondition) MECH-540. Whatever its readiness
gate decides, it decides for all five. Three chips sit on this one run -- see 3e.

### 2e. Two decisions that only the user can make (do not let these age)

- `chip-decision-20260922-inv069-behaviour-channel` -- the AMBER pilot PASSED, but INV-069's WWA
  names DR-10, which is inert without a z_self->viability mapping the substrate does not have.
  Which z_self->behaviour channel should the test use?
- `chip-20260922-inv023-dv-ceiling-decision` -- INV-023's primary calibration DV is pinned by a
  symmetric EMA that erases the arm A/B timing difference by construction; the other two DVs were
  never instrumented. Which DV carries the falsifier?

Both are `kind: decision`. They block a run each and cannot be resolved by a worker.

---

## 3. SCIENCE SIDE -- merge into campaigns

Six campaigns absorb 28 chips. Each has a single natural first move.

### 3a. "Validate what we already built" (11 chips)
The 19 `implemented_pending_validation` entries, worked as one queue-filling campaign. Members:
`gflag0119-963-lineage-validation-retest` (sd_phasic_burst_decay; AMBER confirms no 963c driver
exists), `sd024-standing-density-redesign` (SD-024), `sd061-mech343-q056-proposal-entropy-upstream-leg`
(SD-061), `mech204-f1-substrate-queue-amend` + `mech204-new-waking-drift-source` (MECH-204),
`igw-216-substrate-ready-sd-pp-1` + `mech043-precision-sweep` (SD-PP-1),
`inv063-lega-dv-reregistration` (e2-world-forward-sleep-trainer),
`sd032a-operating-mode-no-consumer` (mode-governance-engagement), `mech027-status-token`
(dv-dynamic-range-precondition-class), `queue-refill-empty`.
**First move: this campaign IS the queue refill.** It converts 2a from "invent new experiments"
into "write the runs already owed".
**Verified live:** MECH-204's entry still has `substrate_paths: None`, so the
`mech204-f1-substrate-queue-amend` chip has not been discharged.

### 3b. ContextMemory corrupting gate (4 chips)
`chip-20260814`, `chip-20260818`, `chip-20260911-arc021-h2`, `chip-proposal-exp-0845-paced`.
**First move: queue the validation run** for
`contextmemory-write-path-addressing-degeneracy`. Do not re-run the pre-flights first -- their
stated gate reasoning is stale (2c).

### 3c. z_world binding constraint (5 chips)
`chip-20260908-w5-s1-zworld-front` is already the campaign. Fold in
`zworld-exogenous-event-channel`, `gflag0228-zresource-zworld-planning-fusion`,
`e1-rollout-closure-owner`, `zworld-separation-quantified-join`, plus the residual z_world overlap
check from `merge-substrate-queue-mint-batch`. This is the recorded V3 binding constraint
(observation -> z_world -> E1/E2), so it should not be worked as five unrelated tickets.

### 3d. Residue-field organ (6 chips)
`chip-proposal-exp-0860-paced` (MECH-105), `0862` (MECH-107), `0804` (MECH-023), `0806` (MECH-024),
`sd024-standing-density-redesign`, `mech268-closure-cadence-dose`.
**First move is not an experiment**: it is the build authorisation in 2b. Until that is answered,
all six stay refused.

### 3e. V3-EXQ-1043b (3 chips -- one is a duplicate)
`chip-20260920-exq1043b-mech537-random-subspace-reference` (AMBER, 09-20 design) and
`chip-20260922-exq1043b-prereg-rank-coprimary` (09-22, carries the USER RULING and says it is
*"an ADDITION to the option-E pre-registration this chip already carries"*) **are the same run**.
Withdraw the 09-20 chip into the 09-22 one. `chip-20260919-mech561-release-after-1043a` is the
downstream release check and sequences after it.

### 3f. P4 falsifier authoring (4 chips)
`p4-falsifier-authoring-tranche2`, `experiment-backlog-claims-without-falsifiers` (4 claims -- a
strict subset), `matched-capacity-definition` (defines a term several falsifiers depend on),
`digest-apply-backlog17-and-doctrine-claims` (128 drafted `what_would_answer` conditions sitting
unreviewed).
**Measured scope:** 166 of 910 experiment-eligible claims (mechanism_hypothesis / architectural
commitment / invariant / design_decision) still have **no `what_would_answer`** -- 120 of them
mechanism hypotheses. The 128 drafted conditions are the largest single tranche available; apply
them before authoring more by hand.

### 3g. MECH-465 / EXP-0590 (2 chips)
`chip-20260909-mech465-conjunct3-queue` (RED -- EXP-0590 still `gated`, the offline P2-floor
derivation failed twice) and `chip-20260914-mech465-p2-llrr-probe-queue` (the probe that adds the
missing per-tick urgency recording). **Sequence: probe first, then the conjunct-3 queue.** Working
them independently is what produced the two failed derivations.

---

## 4. ASSEMBLY MACHINERY SIDE -- reducing total ledger volume

### 4a. Three inflow sources, in order of volume

1. **`proposal_tick`'s substrate pre-filter is inert.** This is the single biggest lever: it mints
   the 33 paced chips (20% of the open ledger) of which 32 are non-actionable. Already chipped as
   `chip-20260918-proposaltick-substrate-filter-inert`, which records the measurement: *"0 of 3 on
   claims a triage had already proved have no substrate, and 0 of 11 REDs in a later batch."*
   **Promote this above every other machinery item.** A filter that screened on claim_type alone
   (`implementation_note` / `reference_note` / `external_failure_mode` with no
   `what_would_answer`) would have stopped 11 of today's 33 with a one-line predicate.
2. **Nothing resolves an IGW chip when the IGW ledger reaps its assignment.** 3 of the 4 open IGW
   chips are stale for exactly this reason (1b). A reconciler that closes chips whose
   `igw_routine_ledger.json` entry reads `completed`/`completed_resumable` is small and permanent.
3. **Recurrence chips re-fire forever.** `queuefloor-fleet-g13` (gen 13),
   `daemondrift-ree-cloud-1-ree-explorer-g7` (gen 7), `daemondrift-dlaptop-mac-runner-g3` (gen 3),
   `crossdispatch-fleet`. **All four already say in their own text to route to
   `/metaworker-learning` instead of re-fixing the instance.** That is one learning session, not
   four fixes. Note for the mac-runner one: the Mac runner is *deliberately* off, so a code-drift
   detector firing on it repeatedly is likely a detector-scope defect, not drift.

### 4b. Merge groups on the machinery side (24 chips -> 7 sessions)

| Merge into one session | Chips | Why |
|---|---|---|
| **Substrate-path gate** | `substrate-paths-unmatched-prefix`, `substrate-path-gate-closed-test-divergence` | Same gate, forward and backward halves. **Verified:** 6 paths across 3 entries still carry a `ree-v3/` prefix that can never match, so those entries silently protect nothing. |
| **Burned-ID machinery** | `validate-queue-burned-id-guard-inert` (URGENT), `maconlypin-...-test_burned_queue_entry_detector` | **Both verified.** The guard reads `REE_assembly/evidence/experiments/runner_status/`, which **does not exist at either configured path** -- inert, returns zero IDs silently. The contract test is red at `21 not <= 20` on a noise cap whose docstring says raising it is a real decision, not a route to green. Same subject; one session, but the cap needs a user call. |
| **Negative instruments reporting green on nothing** | `validate-experiments-unreadable-path-green`, `unqueued-auditor-banner-screen-v2`, `preflight-a2-presence-vs-liveness`, `proposaltick-substrate-filter-inert` | All four are the documented "nothing found must not read the same as the search broke" failure. One pass applying the standard remedy (cannot-determine category / canary / printed denominator) is cheaper and more consistent than four. |
| **Phase-4 routing completion** | `phase4-chip-archive-verb`, `phase4-ws-rotation-verb`, `routedwriter-umbrella-workspace-state-md`, `igwbrief-workset-commit-route`, `refwedge-f4-handoff-coordinator-transport`, `intent-log-read-endpoint` | Same migration; the last is the measurement that tells you when the others are done. |
| **Scripts-corpus health** | `scriptscorpus-item-e-recheck-after-0919`, `scriptscorpus-verdict-id-collision`, `corpusscan-perworker-xdist-floor`, `provenance-pin-test-claim-session-link` | All require a main-checkout corpus run; one run answers all four. |
| **Token-split measurement** | `token-split-read-channel-count`, `token-split-remeasure-b2` | **Strict ordering** -- the Read-channel count must land first or the re-measure reports a false frequency collapse. |
| **Dispatch/worktree hygiene** | `campaign-gc-skill-docs`, `cycle-trigger-story-reconcile`, `metaworkergc-sweep-26`, `strandedwt-underscore-scratch-blindspot-decision` | All documentation/GC of the same dispatch surface. `dev-doctor` currently reports 40 agent worktrees, 3 with detached HEAD, and several `metaworker-chip-2026-08-*` worktrees still present -- the GC sweep chip is still warranted, though its "26" count is stale. |

### 4c. Date-gated -- leave alone, they are not stale

| Chip | Not before |
|---|---|
| `strandedwt-scratch-remeasure-after-1004` | 2026-10-04 |
| `autopull-fossil-reconcile-7day-readback` | ~2026-09-27 |
| `red-verdict-second-pass-triage` | 2026-09-25 (allowance reset) |
| `mech204-new-waking-drift-source` | 2026-09-25 (allowance reset) |
| `scriptscorpus-item-e-recheck-after-0919` | **due now** |
| `token-split-remeasure-b2` | **due now** |

### 4d. One standing row -- never resolve
`session-start-orchestrator` is marked *"standing row -- not a task"*. It should be excluded from
any ledger-count or sweep tooling so it stops being re-counted as open work.

### 4e. Stale pre-flight verdicts are themselves a ledger cost

33 open chips carry a RED or AMBER pre-flight verdict. At least six are now demonstrably stale
(four "no what_would_answer" REDs where the falsifier now exists; two ContextMemory REDs citing a
resolved flag and a superseded substrate status). A RED verdict is dated evidence, not a durable
property, and `chip-20260920-red-verdict-second-pass-triage` is the chip that exists to re-walk
them -- it is correctly held to 2026-09-25. **Recommend it re-check verdict freshness against
live state, not just route each RED**, since a third of them may have moved.

---

## 5. Recommended dispositions, counted

| Action | Science | Machinery | Total |
|---|---:|---:|---:|
| Withdraw / resolve now | 35 | 0 | **35** |
| Merge into 6 science campaigns | 28 | -- | **28** |
| Merge into 7 machinery sessions | -- | 24 | **24** |
| Date-gated, leave | 4 | 2 | **6** |
| Standing row, exclude from counts | -- | 1 | **1** |
| Decisions owed by the user | 2 (+1 in 2b) | 1 (burn cap) | **4** |
| Remaining as individual work | ~50 | ~17 | ~67 |

Acting on rows 1-3 takes the open ledger from **165 to roughly 80 tracked items across 13
campaigns/sessions plus ~67 singletons**, with no work lost -- every withdrawal points at a
release condition or a completed record that already re-derives.

## 6. The three things that are genuinely blocking

1. **The experiment queue is empty** (depth 1, claimed) while **19 substrate entries are built and
   unvalidated**. The validation campaign (3a) is the refill.
2. **The residue-field organ is diagnosed, registered, and not authorised to build** -- 13
   consecutive experiment refusals converge on it (2b). This needs a user decision, not a chip.
3. **The ContextMemory corrupting STOP-GATE is releasable and nobody owns the release** -- one
   validation run clears five claims and four chips (2c/3b), and the chips' own stated reasons for
   staying blocked are out of date.
