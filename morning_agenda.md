# Morning Agenda — 2026-09-20

Generated: 2026-09-20T10:35:55Z

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `V3-EXQ-541d option C+D: survivable regime + rv falsifier` (`metaworker-science-20260920-mech204-541d-cd`, age `0.9`h);
> `ARC-029 V3-EXQ-1070a tick-budget repair` (`metaworker-science-20260920-arc029-1070a`, age `0.9`h);
> `queue-experiment: INV-063 four-arm intake ladder` (`metaworker-science-20260920-inv063-ladder`, age `0.9`h);
> `queue-experiment: V3-EXQ-1071` (`metaworker-science-20260920-inv063-ladder-exq-1071`, age `0.8`h);
> `queue-experiment: V3-EXQ-1070a` (`metaworker-science-20260920-arc029-exq-1070a`, age `0.8`h);
> `V3-EXQ-1068 noise-floor gate + queue` (`metaworker-science-20260920-sd036-obs3-noisefloor`, age `0.8`h);
> `clear four stale staged files in the Mac umbrella checkout` (`umbrella-index-fossils-20260920`, age `0.8`h).
> The Governance Agenda, Experiments Awaiting Review, and granularity/category audit sections below reflect the **last** pipeline run, not
> today's state. Re-run `/morning-digest` manually once sessions are clear to refresh them.
>
> **Mitigating fact, stated so the banner is not read as worse than it is:** the derived artifacts on disk are in fact
> **minutes old** — `pending_review.md` generated `2026-09-20T10:25:34Z`, `promotion_demotion_recommendations.md`
> `2026-09-20T10:24:06Z`, `closure_status.md` `2026-09-20T01:14:27Z` — because another process regenerated them just
> before this run. The Tier-2 skip is a *policy* skip (a concurrent session might hold `claims.yaml` half-edited), not
> evidence that these numbers are stale. Treat the governance rows as fresh-but-unverified.

---

## Headlines — Positive Results & Live Decisions

Four positives landed since the last digest (2026-09-18T05:10Z). Two are clean; two are PASSes the indexer
has flagged as untrustworthy and they are listed here because they move a live design decision, not because
they score.

- **SD-098 (read-time rerank) — evidence — PASS / `supports`** (`sd098_ghost_goal_readtime_rerank_20260918T182337Z_v3`)
  - **Moves:** SD-098 — first experimental support for half (i): read-time re-classification reinstates old goal
    anchors with **no write** (C3 byte-identical anchor-pool fingerprint across probes, 1.0/1.0).
  - **Why it is a real positive:** the A-B-A reversal makes the recency/cue-displacement account predict the
    *opposite* sign. Group A is older than B, so recency can only see A lose rank; A was reinstated
    (C2 measured 0.477 vs threshold 0.10, 11 positive seeds).
  - **Gate on acting:** scope is half (i) only. Half (ii) — the matched stored-node-type comparison arm — is
    **not built by user decision (2026-09-17: do not build SD-097's typed topology)**. C1 (rank inversions) is
    recorded, non-gating, and flagged degenerate. So this supports the claim's first half and closes nothing.

- **V3-EXQ-1058 — SD-071 consolidation-readout instrument validity — evidence — PASS / `supports`**
  - **Moves:** SD-071 (`candidate`, exp_conf 0.772, 1 entry, 0 fail_runs, quadrant `novel_discovery`) — the
    NREM and SWS consolidation readouts are validated as content-contingent instruments; all three criteria
    non-degenerate.
  - **Makes live:** downstream sleep-consolidation readouts (`sleep_substrate` plan) can now be read as
    instruments rather than argued about.
  - **Gate on acting — read this before quoting the PASS.** The manifest records its own two-way ambiguity:
    `ceiling_inside_ci95 == false` PASSES C1 both when the CI sits *below* the ceiling (the content-contingent
    reading SD-071 asserts) and when it sits *above* it (the **confounded** reading that refutes it). The
    pre-registered C1 cannot separate them; the side is recorded per leg. A second recorded caveat: C3's
    content-scale ladder is a **sigma-reparameterisation of the injected arm's own damage curve**, not an
    independent content-tracking probe. Actionable, but not as a clean instrument certificate.

- **V3-EXQ-1060 — MECH-423 E2 world-forward sleep trainer — diagnostic — PASS / `supports`**
  - **Moves:** MECH-423 (`provisional`, exp_conf 0.629 / lit 0.821, quadrant `confirmed_established`) — the E2
    world-forward sleep trainer is **LIVE**: cross-module consolidation metrics merge, E2 world is touched under
    the interleaved schedule, world-head delta positive ON, and the OFF arm is **bit-identical** (clean negative
    control). All six criteria non-degenerate, plain AND, real waking rollout via `_e1_tick` (179 world-replay
    pairs vs a floor of 17).
  - **Makes live / unblocks:** the cognifold super-additivity thread (MECH-423) now has a working substrate to
    measure on, and the INV-063 sleep-dependency ladder has its trainer.
  - **Gate on acting:** none mechanical — but it is a `diagnostic`, so it needs a confirmed `/failure-autopsy`
    before governance applies anything from it.

- **V3-EXQ-1063 + V3-EXQ-1069 — INV-063 — diagnostic — PASS / `non_contributory`, BOTH FLAGGED**
  - Listed here under the 723 rule (a `non_contributory` result that still changes the next action), **not** as
    evidence. They score nothing and must not be quoted as INV-063 support.
  - **1063** (`legb_dv_converged_base_infonce_positive_mse_not`) is flagged **`vacuous_pass`** — the overall PASS
    rests on a degenerate criterion. The substantive content is the split it names: leg-B DV converged on base
    InfoNCE positive but **not** MSE.
  - **1069** (`inv063_p1_intake_ladder_gradeable`) is flagged **`precondition_unmet`** AND carries a
    **DEAD z_goal stream** (`writer_defect: true`, 16800 ticks, **0** writer calls — `REEAgent.update_z_goal`
    never ran, so every z_goal consumer silently no-opped for the whole run). Judge it only on criteria that do
    not read z_goal.
  - **Decision it makes live:** three metaworker sessions are queueing the INV-063 four-arm intake ladder
    (V3-EXQ-1071) **right now**. 1069's z_goal writer defect is exactly the class of harness bug that would
    invalidate that ladder if it is inherited. Worth checking 1071's driver calls `update_z_goal` before it runs.

---

## Decisions Waiting on You (7)

## Decisions waiting on you

7 decision(s) recorded as awaiting your answer, oldest first. These do NOT block any session -- they are recorded requests, so nothing is stalled while they sit. Answer any of them with the command in its block, or reopen the asking session.

### MECH-074d -- waiting 43d

**Question:** Demotion review: provisional -> candidate (conflict_ratio 0.667)

**Recommendation:** demote_to_candidate

**Context:** (source: evidence/experiments/promotion_demotion_recommendations.md)

- decision_id: `(legacy row -- no decision_id)`
- asked by: `governance`
- status: `discussing`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-074d \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-316 -- waiting 36d

**Question:** Orphan V3 claim: owning node arc_062_rule_apprehension:GAP-I-absorption is deferred

**Recommendation:** undefer_owning_node

**Context:** D-002 orphan-V3-claim adjudication (chip-20260815-orphan-v3-claims-adjudicate). Claim reads as live V3 in the registry but its ONLY owning closure node is `deferred`, which generate_closure_snapshot.py DEFERRED_STATUSES excludes from the V3 progress denominator: not done, not remaining, not visible as a gap. Plan-frontmatter note applied; node status change PROPOSED not applied (outside session au ...

- decision_id: `(legacy row -- no decision_id)`
- asked by: `orphan-v3-claims-adjudicate-6f88bd`
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-316 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-317 -- waiting 36d

**Question:** Orphan V3 claim: owning node arc_062_rule_apprehension:GAP-I-absorption is deferred

**Recommendation:** undefer_owning_node

**Context:** D-002 orphan-V3-claim adjudication (chip-20260815-orphan-v3-claims-adjudicate). Claim reads as live V3 in the registry but its ONLY owning closure node is `deferred`, which generate_closure_snapshot.py DEFERRED_STATUSES excludes from the V3 progress denominator: not done, not remaining, not visible as a gap. Plan-frontmatter note applied; node status change PROPOSED not applied (outside session au ...

- decision_id: `(legacy row -- no decision_id)`
- asked by: `orphan-v3-claims-adjudicate-6f88bd`
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-317 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-314a -- waiting 36d

**Question:** Orphan V3 claim: owning node behavioral_diversity_isolation:GAP-G is deferred

**Recommendation:** undefer_owning_node

**Context:** D-002 orphan-V3-claim adjudication (chip-20260815-orphan-v3-claims-adjudicate). Claim reads as live V3 in the registry but its ONLY owning closure node is `deferred`, which generate_closure_snapshot.py DEFERRED_STATUSES excludes from the V3 progress denominator: not done, not remaining, not visible as a gap. Plan-frontmatter note applied; node status change PROPOSED not applied (outside session au ...

- decision_id: `(legacy row -- no decision_id)`
- asked by: `orphan-v3-claims-adjudicate-6f88bd`
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-314a \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-091 -- waiting 36d

**Question:** Orphan V3 claim: owning node commitment_closure:GAP-7 is deferred

**Recommendation:** decide_blocker_generation_then_route

**Context:** D-002 orphan-V3-claim adjudication (chip-20260815-orphan-v3-claims-adjudicate). Claim reads as live V3 in the registry but its ONLY owning closure node is `deferred`, which generate_closure_snapshot.py DEFERRED_STATUSES excludes from the V3 progress denominator: not done, not remaining, not visible as a gap. Plan-frontmatter note applied; node status change PROPOSED not applied (outside session au ...

- decision_id: `(legacy row -- no decision_id)`
- asked by: `orphan-v3-claims-adjudicate-6f88bd`
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-091 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-122 -- waiting 35d

**Question:** Demotion review: provisional -> candidate

**Recommendation:** demote_to_candidate

**Context:** (source: evidence/experiments/promotion_demotion_recommendations.md)

- decision_id: `(legacy row -- no decision_id)`
- asked by: `governance-cycle-2026-08-16`
- status: `discussing`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --claim-id MECH-122 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

_No session is waiting on this one -- answering it above is all that is needed._

### MECH-037 -- waiting 40h

**Question:** MECH-037: demote provisional -> candidate? The pipeline recommends demote_to_candidate (epistemic_category standard, exp_entries 0, lit_entries 5, directions supports 2 / weakens 1 / mixed 2, conflict_ratio 0.667 -- a literature-only conflict, which per the 2026-09-03 EXT-003 ruling is non-gating). Alternative: hold as provisional. No experimental evidence exists either way.

**Recommendation:** demote_to_candidate (pipeline); governance session left it undecided for lack of context on why it was promoted

**Context:** governance-20260918 walk; the same-day pattern on 2026-09-17 demoted MECH-019 and MECH-152 (lit-only conflict_ratio 0.667, exp_entries 0) with the user's reaffirmation, so a consistent ruling would demote; needs the user's call.

- decision_id: `dec-20260918T190425-MECH-037`
- asked by: `dgolden` (session `governance-20260918`)
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --decision-id dec-20260918T190425-MECH-037 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

**Or reopen the session that asked:**

```bash
# session 'governance-20260918' not in the worktree registry (ended, or a non-Mac box)
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/sync_worktree_session_registry.py --why
```

---

## Queue Status

- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0). One item `claimed`: **V3-EXQ-1067**, claimed by
  `DLAPTOP` at `2026-09-20T02:07:22Z`.
- **ALERT: QUEUE EMPTY.** Zero pending items against a low-water mark of 3. The fleet has nothing unclaimed to
  pick up. This is the third occurrence in the recent record (queue was also empty ~48h on 2026-09-14).
- **Refill IS in flight — do not double-queue.** Four sessions opened `queue-experiment` claims ~0.8–0.9h ago and
  are landing **V3-EXQ-1068** (SD-036 observable-3 noise-floor gate), **V3-EXQ-1070a** (ARC-029 tick-budget
  repair), **V3-EXQ-1071** (INV-063 four-arm intake ladder) and a V3-EXQ-541d option C+D arm. Check
  `experiment_queue.json` before queueing anything new this morning.
- **Check V3-EXQ-1067's claim.** It has been `claimed` by `DLAPTOP` for **8.5h**. Per standing policy the Mac
  runner is deliberately off, so a live Mac claim of that age is worth a look — but *absence of telemetry is not
  abandonment* (`feedback_heartbeat_stale_not_abandoned`), and `COORDINATOR_STALE_HOURS` is 6 for exactly this
  reason. **Do not clear it on the age alone** — a duplicate run is worse than a slow recovery. Verify the Mac is
  or is not running it first.
- **Fleet-idle watcher:** `status: OK`, snapshot `2026-09-20T09:43:22Z` (43 min old — fresh). **`idle_risk: true`**,
  claimable backlog **0** vs threshold 3 — the watcher independently confirms the starvation above.
  - Ready-SD validation candidates: **1** — `SD-106` (leverage 6) → `V3-EXQ-1023`.
  - Exclusion tallies: 39 excluded because validation already ran, 43 with no queueable validation, 4 known churn,
    0 already queued. So the candidate pool is nearly exhausted: **refill needs fresh `/queue-experiment` design
    work, not re-queues.**
  - Caveat on the one candidate: **V3-EXQ-1065 just ran on SD-106/MECH-566 last night (FAIL / `mixed`,
    `recoverability_indeterminate__mech566_conditioning_falsified`)**. Read that result before treating
    V3-EXQ-1023 as a clean next step.
- **Owed successors: none.** All four plan `owner_exq` ids on non-done nodes (V3-EXQ-1047, 445h, 910b, 938) fail
  Step 7c check (b) — every one has a landed manifest, so none is owed. Two plan rows carry a literal `TBD`
  rather than an id and are not cross-checkable.
- **Phantom Owner-EXQ ids: none.** No candidate id reached check (d).
- **Declared never-minted ids: none surfaced this run.**

---

## Experiments Awaiting Review (10 indexed / 0 runner-only)

`pending_review.md` generated `2026-09-20T10:25:34Z` — 4 PASS, 6 FAIL, 0 runner-only, 0 ERROR manifests.
**7 of the 10 are diagnostics with no confirmed autopsy**, so most of this list routes to `/failure-autopsy`
rather than to a verify-and-close.

### V3-EXQ-1058 — SD-071 consolidation-readout instrument validity — evidence — PASS
- **Claims tested:** SD-071 (`candidate`, exp_conf 0.772, 1 entry / 0 fail_runs, quadrant `novel_discovery`)
- **Key metrics:** C1 nrem CI95 [0.1438, 0.1451] mean 0.1445, ceiling outside CI on both legs; C2 both legs'
  denominators supra-floor on all seeds; C3 sws ladder spread > 0.01 all seeds. All three non-degenerate.
- **Classification:** evidence
- **Governance impact if confirmed:** would give SD-071 its instrument-validity leg — but see the two-way C1
  ambiguity and the C3 sigma-reparameterisation caveats in Headlines before treating it as settled.

### V3-EXQ-1060 — MECH-423 E2 world-forward sleep trainer — diagnostic — PASS
- **Claims tested:** MECH-423 (`provisional`, exp 0.629 / lit 0.821, 7 entries, quadrant `confirmed_established`)
- **Key metrics:** C1–C6 all pass, all non-degenerate; OFF arm bit-identical; 179 world-replay pairs (floor 17).
- **Classification:** diagnostic — **needs a confirmed `/failure-autopsy` before governance applies anything.**

### V3-EXQ-1063 — INV-063 leg-B DV direction — diagnostic — PASS — **`vacuous_pass`**
- **Claims tested:** INV-063 (`candidate`, exp_conf 0.0 / lit 0.684, quadrant `plausible_unproven`)
- **Self-route:** `legb_dv_converged_base_infonce_positive_mse_not`; `evidence_direction: non_contributory`
- **Classification:** diagnostic — adjudicate via `/failure-autopsy`. The label must not drive a governance action.

### V3-EXQ-1069 — INV-063 P1 gate (798a P0) — diagnostic — PASS — **`precondition_unmet` + DEAD z_goal**
- **Claims tested:** INV-063
- **Key metrics:** 16800 ticks, **z_goal writer_calls = 0**, active_frac 0.000, GoalState `live`.
- **Classification:** diagnostic. Two independent flags. Judge only on criteria that do not read z_goal.

### V3-EXQ-1057 / V3-EXQ-1057a — MECH-017 reality-consolidation replay additive budget — evidence — FAIL
- **Claims tested:** MECH-017 (`candidate`, exp 0.473 / lit 0.74, 6 entries, 1 fail_run)
- **Degeneracy:** both flagged `non_degenerate: false` — 1057 on
  `additive_arm_retains_replay_gain`, 1057a on `additive_arm_retains_recency_benefit_d2`.
  `evidence_direction: inconclusive`, self-route `substrate_not_ready_requeue`.
- **Route:** `/failure-autopsy` (evidence-purpose degenerates are not caught by `_compute_adjudication`;
  **do not verify-and-close**).

### V3-EXQ-1039a — INV-086 / MECH-428 waypoint-field consumer drive-signal absorption — diagnostic — FAIL
- **Claims tested:** INV-086, MECH-428 (both `candidate`, exp_conf 0.0)
- **Supersedes:** V3-EXQ-1039. Flagged `precondition_unmet`; `evidence_direction: unknown`.

### V3-EXQ-1043a — MECH-537 communication-subspace permutation null — diagnostic — FAIL
- **Claims tested:** MECH-537 (`candidate`, exp_conf 0.0 / lit 0.772)
- Flagged `precondition_unmet`; `non_contributory`.

### V3-EXQ-1065 — SD-106 subspace overlap / MECH-566 recondition — diagnostic — FAIL — `mixed`
- **Claims tested:** SD-106 (`implemented`), MECH-566 (`candidate`, **`v3_pending: true`**)
- **Self-route:** `recoverability_indeterminate__mech566_conditioning_falsified` — MECH-566's conditioning is
  falsified while recoverability stays indeterminate.
- **Why it matters beyond its own row:** SD-106 is the substrate the `zworld_adequacy:ZW-1` assembly-frontier node
  is `awaiting` (assembly_status `queued`, `revisit_after 2026-10-15`), and SD-106 is also the fleet-idle
  watcher's only ready validation candidate. This result is upstream of both.

### V3-EXQ-1070 — ARC-029 env operating-point feasibility — diagnostic — FAIL
- **Claims tested:** ARC-029 (`candidate`, exp_conf 0.125 / lit 0.784, 1 fail_run)
- **Unmet precondition:** `training_tick_budget_equalised` measured **3.959** against a threshold of **2.0**.
- **Already being repaired:** `metaworker-science-20260920-arc029-1070a` holds a live claim for the tick-budget
  repair and V3-EXQ-1070a is being queued. No action needed here.

---

## Errors to Diagnose (0)

- **None outstanding.** `pending_review.md` lists 0 runner-only and 0 ERROR manifests.
- Fleet ERROR rate (coordinator DB, last 30 days, `2026-08-22 .. 2026-09-20`): **1.6%** — 2 ERROR against
  68 PASS / 57 FAIL over 127 classified runs. 0 phantom completions, 0 operator cancellations, 0 bookkeeping gaps.
  Both ERRORs are already metabolized (nothing surfaced for `/diagnose-errors`).
- Per-machine run counts in window: ree-cloud-2 59, ree-worker-3 32, ree-cloud-4 17, ree-worker-1 9,
  DLAPTOP-4.local 9, ree-cloud-3 1.

---

## Fleet Git Health

Active ssh probe (`runner_git_health.py`) — **all probed checkouts structurally clean.**

| machine | REE_assembly | ree-v3 |
|---|---|---|
| DLAPTOP-4 (local) | OK | OK |
| ree-cloud-1 (hub) | OK | OK |
| ree-cloud-2 (worker) | UNREACHABLE (ssh timeout) | — |
| ree-cloud-3 (worker) | UNREACHABLE (ssh timeout) | — |
| ree-cloud-4 (worker) | OK | OK |

`UNREACHABLE` is **not** a fault — cloud-2/3 are routinely powered off; `hcloud server list` is the authority on
power state. Note ree-cloud-2 ran 59 experiments in the last 30 days (most recent `2026-09-20T04:26:54Z`), so it
was up a few hours ago. Untracked grading: 34 untracked paths graded against origin, **0 stranded run manifests**,
0 same-run_id-different-content, 0 stranded literature entries.

---

## Governance Agenda (5 pending_user recommendations)

| claim | status | decision needed | recommendation |
|---|---|---|---|
| `MECH-037` | `provisional` | Demotion review: provisional -> candidate | `demote_to_candidate` |
| `MECH-050` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` |
| `MECH-055` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` |
| `MECH-065` | `candidate` | Conflict resolution before promotion | `hold_candidate_resolve_conflict` |
| `MECH-561` | `candidate` | Hold — V3 substrate required before evidence | `hold_pending_v3_substrate` |

MECH-037 is also the one **non-legacy** row in the Decisions-Waiting block above
(`dec-20260918T190425-MECH-037`, asking session `governance-20260918`).

**Granularity-debt recurrence (GOV-GRAN-1):** `dropped_handoff` **0** — no dropped `/claim-synthesis` handoff,
nothing chipped. `unflagged_recurrence` **51** (of 217 claims with hits; 79 excluded as metabolized).
**List-only — a human must discriminate coarse-claim vs coherent substrate campaign before any of these routes.**

The count alone is the weak signal; the alignment distribution is what leans the discrimination. **Only 6 of the
51 carry any `weakened` alignment at all** — those are the ones where the granularity reading is actually live:

- `Q-034` — 6 hits / 2 signatures, alignment weakened=3 other=3 — **weakened present**
- `MECH-111` — 5 hits / 3 sigs, other=4 weakened=1 — **weakened present**
- `INV-054` — 4 hits / 2 sigs, other=2 weakened=2 — **weakened present**
- `ARC-038` — 3 hits / 1 sig, weakened=3 — **weakened present, and uniformly so**
- `SD-005` — 3 hits / 1 sig, weakened=3 — **weakened present, and uniformly so**
- `ARC-018` — 2 hits / 2 sigs, unclear=1 weakened=1 — **weakened present**

The largest-count rows are, by contrast, **not** granularity debt on this reading — no `weakened` anywhere:

- `INV-050` — 13 hits / 9 sigs, unclear=8 intact=4 n/a=1: no weakened, likely measurement debt
- `MECH-180` — 12 hits / 8 sigs, unclear=8 intact=2 n/a=1 other=1: no weakened, likely measurement debt
- `SD-082` — 9 hits / 6 sigs, unclear=9: no weakened, likely measurement debt
- `SD-078` — 7 hits / 6 sigs, unclear=7: no weakened, likely measurement debt
- `MECH-075` — 7 hits / 5 sigs, intact=5 other=2: no weakened, alignment largely intact
- `MECH-058` / `MECH-059` — 13 / 12 hits but **1 signature each** (bridge_v2 corpus, unclear throughout): high
  count, single failure mode — the classic false-positive shape the pre-2026-07-22 trigger over-fired on.

**Epistemic-category completeness (GOV-CAT-1): clean.** `missing_category` **0**, `invalid_category` **0**,
`malformed_markers` **0**. Legacy warns only: 10 `unkeyed_schema` (singular `claim_id` targets) + 2
`claimless_missing`. Neither can corrupt a count; list-only, no chip. (673 `invalid_baselined` + 1
`invalid_metabolized` are the excluded historical backlog — **do not regenerate the snapshot to clear them.**)

---

## Active Plans Heartbeat (18 plans with closure frontmatter; 13 non-done)

Overall v3 closure: **72.3%** weighted across 98 non-deferred nodes. Remaining **34**; assembly frontier **11**
(separate axis, not a backlog); deferred 10; done 64.

| Plan | In-flight | Blocked | Assembling | Progress | Last updated |
|---|---|---|---|---|---|
| `conversion_ceiling_campaign_plan` | 0 | 0 | 7 | 0% | 2026-07-10 |
| `global_workspace_jlens_plan` | 0 | 2 (+2 open) | 0 | 5% | 2026-09-08 |
| `policy_decomposition_trigger_plan` | 0 | 1 | 0 | 10% | 2026-08-21 |
| `zworld_adequacy_plan` | 0 | 1 (upstream) | 1 | 10% | 2026-09-18 |
| `sd_037_axis_b_sustained_threat_curriculum_plan` | 0 | 3 | 1 | 10% | 2026-06-23 |
| `self_attribution_plan` | 0 | 4 | 0 | 28% | 2026-09-04 |
| `orienting_epistemic_deficit_v3_plan` | 2 | 1 (+2 open) | 0 | 32% | 2026-09-17 |
| `mech357_avoidance_efficacy_plan` | 0 (1 partial) | 0 | 0 | 50% | 2026-08-29 |
| `arc_062_rule_apprehension_plan` | 2 | 1 (+2 blocked_pending_substrate) | 0 | 56% | 2026-09-01 |
| `behavioral_diversity_isolation_plan` | 2 | 1 | 1 | 71% | 2026-09-16 |
| `commitment_closure_plan` | 2 | 0 | 1 | 88% | 2026-09-16 |
| `sleep_substrate_plan` | 0 | 1 (upstream) | 0 | 91% | 2026-08-14 |
| `infant_substrate_plan` | 1 | 1 (pending substrate) | 0 | 91% | 2026-09-16 |
| *(5 plans at 100%: `arc_005_control_plane_routing`, `goal_pipeline`, `mech303_safety_threshold`, `sd033_governance`, `sd_037_axis_a`)* | — | — | — | 100% | — |

**Stale rows: 0. Drifted nodes: 0.** Per `closure_drift.md` (the maintained, date-aware check — not reimplemented
here), both the `Drifted nodes` and `Stale since last update` sections are empty, and every collapsed node's
stored `live` head matches its projection (0 of 99).

**Honest caveat on that zero.** Many remaining rows carry an old calendar `last_updated` — `sd_037_axis_b:P2/P3/P4`
at 2026-06-05, `arc_062_rule_apprehension:GAP-J` at 2026-05-17, `global_workspace_jlens:A/B` at 2026-07-09/10.
The drift report reports 0 because its stale predicate is *evidence-relative* (a later-lettered sibling reached
terminal state, or a confirmed autopsy post-dates the node), not calendar-relative. Those rows are old because
nothing has happened to them, which is the correct reading — they are all `blocked` on an upstream node.

**Suppressed (legitimately non-terminal) — 4, listed for audit, not drift:**

- `orienting_epistemic_deficit_v3:ORNT-2` — `in_progress`, owner V3-EXQ-1047 — `manifest_evidence_direction=non_contributory`
- `orienting_epistemic_deficit_v3:ORNT-6` — `in_progress`, owner V3-EXQ-910b — `case_3_self_tag`
- `policy_decomposition_trigger:REPOSE` — `blocked`, owner V3-EXQ-938 — `manifest_evidence_direction=non_contributory`
- `self_attribution:GAP-1` — `blocked`, owner V3-EXQ-445h — `case_3_self_tag`

**All four ran (manifests confirmed on disk) — none is owed.** See Queue Status.

**Assembly frontier — 11 nodes, resting, 0 `revisit_due`.** The one node with a date, `zworld_adequacy:ZW-1`
(awaiting SD-106, assembly_status `queued`), is due `2026-10-15` — not yet. The 7-node
`conversion_ceiling_campaign` plan is entirely assembling, which is why it reads 0% and is **not** a stalled
backlog.

**PLAN STALING (no decision-log entry in >14 days *and* rows in-flight):** none identified — the plans with
in-flight rows (`orienting_epistemic_deficit_v3` 2026-09-17, `behavioral_diversity_isolation` 2026-09-16,
`commitment_closure` 2026-09-16, `infant_substrate` 2026-09-16) were all touched within the last 4 days.
`arc_062_rule_apprehension` (2 in-flight, last updated 2026-09-01, 19 days) is the one borderline case — worth
a look, not yet a flag.

---

## Literature Pull Candidates (Top 5)

All `high`-priority backlog rows (115) need **experimental** evidence, not literature. The literature lane is
469 open rows, all `medium`. Top 5 by backlog order, each checked authoritatively via `claim_ids_tested` in
`record.json` (not directory-name globbing):

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | ARC-101 | Language bootstraps from a grounded social ecology, not from grammar | medium | 0 |
| 2 | ARC-102 | Two distinct abstraction levels not to be conflated (substrate vs …) | medium | 0 |
| 3 | ARC-103 | Symbolic inference subordinate to embodied harm sensing (V6 inference) | medium | 0 |
| 4 | ARC-104 | Language-cannot-override-harm guard (language-input level) | medium | 0 |
| 5 | ARC-105 | granularity_matched_goal_hierarchy | medium | 0 |

**Note:** ARC-101–104 are language-cluster claims. The standing position on that cluster is *block the
experimental lane, leave the literature lane proposed* — so these are legitimately lit-pullable even though no
V3 language channel exists.

---

## Stale Claims (3 active > 6h)

- Buckets: A(auto-closable) 0 | B(vendor-sync) 0 | C(no-trace) 0 | D(dirty-unproven) 1 | U(undetermined) 1 | L(orchestrator-live) 1
- **[U]** `igw-246-literature-proposal-for-mech-050` (35.4h) — *IGW-246 MECH-050 lit-pull* — directory-scoped, so
  git cannot evidence landing either way.
  - warn: `directory-scoped (not attributable): REE_assembly/evidence/literature/targeted_review_connectome_mech_050`
  - warn: **`path does not exist: REE_assembly/evidence/experiments/indexes`** — the claim's premise is missing.
- **[D]** `igw-239-mech055-exq-1062` (33.0h) — *queue-experiment: V3-EXQ-1062* — dirty, completeness **not**
  provable. **Report, never action: do not commit it and do not revert it.**
  - warn: `virtual ID-slot reservation (not attributable): ree-v3/experiment_queue.json/V3-EXQ-1062`
  - warn: `directory-scoped: ree-v3/experiments/`; `shared/directory resource is dirty, likely another live session`
- **[L]** `orchestrate-20260919-2125` (13.2h) — *orchestrate: open-ended 30-min loop from 2026-09-19T21:25Z* —
  orchestrator-live bucket. **Leave it alone**: `/metaworker-orchestrate` is a long-lived loop and is never
  `/session-land`ed.
  - warn: `machine-local untracked scratch (not attributable): mac_dispatch_load.json`

Note both MECH-050 and MECH-055 also appear in the Governance Agenda above — the two stale IGW claims are the
in-flight work on exactly those two claims.

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 62795).

---

## Blocked Items

- **`governance.sh` skipped (Tier 2).** Seven active non-stale claims at generation time. See the banner — the
  derived artifacts happen to be minutes old anyway.
- **`WORKSPACE_STATE.md` append skipped**, per the Tier-2 rule: it is a whole-file read-modify-write and a
  concurrent session's uncommitted edits would be adopted and landed under this task's commit message. This
  agenda file is the run's record.
- **No agenda was produced on Friday 2026-09-19** (prior agenda: 2026-09-18). `GAP_DAYS = 2`, which is below the
  banner threshold, so this is a note rather than a MISSED-RUNS banner. Today's own 05:07 slot also did not
  produce a run — this digest was started manually at 10:26Z, ~5h19m past the slot, which the Check-1 guard had
  correctly refused as `STALE_SKIP`. Two consecutive weekday slots missing is the shape that precedes a real
  scheduler-side outage; **if tomorrow's 05:07 also misses, run diagnostic (d)**
  (`scripts/audit_scheduled_task_fires.py --task ree-morning-digest --scheduler-log --profiles`) before
  attributing it to sleep.
- **Queue is empty** — see Queue Status. Refill is in flight from four concurrent sessions; the ready-SD
  candidate pool is nearly exhausted (39 already-ran / 43 no-queueable-validation), so the next refill after
  those four will need fresh design work.
