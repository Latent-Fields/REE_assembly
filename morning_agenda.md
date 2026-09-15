# Morning Agenda — 2026-09-15

Generated: 2026-09-15T04:23:50Z

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `orchestrate: 2026-09-15 02:03Z (30-min loop)` (`orchestrate-20260915-0203`, age 2.5h);
> `igw log backlog staleness warning` (`eloquent-jepsen-5f6242`, age 2.3h). The Governance Agenda,
> Experiments Awaiting Review, and granularity/category audit sections below reflect the **last**
> pipeline run (pending_review 2026-09-15T01:21Z; recommendations 2026-09-14T23:44Z), not today's
> state. Re-run `/morning-digest` manually once sessions are clear to refresh them. Note that
> V3-EXQ-1039 and V3-EXQ-1040 landed **after** that pipeline run, so they are not yet listed in
> `pending_review.md`.

> **ACTION — staged-deletion skew in the shared `REE_assembly` checkout.** `git status` shows
> `D ` (staged) plus `??` for
> `evidence/experiments/v3_exq_1040_sd077_centered_super_ordinal_cue_key_20260915T021006Z_v3.json`,
> the SD-077 PASS below. A bare `git commit` in that checkout would delete this manifest from
> HEAD. The copy on disk is **not** byte-identical to HEAD (it is pretty-printed; HEAD holds the
> compact phase3 copy from `31511e3a8a2`), so this run did not touch it. The index-only fix
> (`git -C REE_assembly reset -q -- <path>`) leaves the working tree untouched, but confirm first
> that no live session intends the on-disk version.

---

## Headlines — Positive Results & Live Decisions

These results came in after the last digest (2026-09-14T04:26Z):

- **V3-EXQ-1040 — SD-077 centered super-ordinal cue key — PASS** (evidence, `supports`)
  - **Moves:** SD-077 (candidate). Centering the cue key restores goal-anchor differentiation.
    The raw key collapses to 1 anchor on every seed. The centered key gives 85/37/60 anchors, a
    minimum delta of 36 against a margin of 4, so C1 passes on 3/3 seeds. The cue-geometry spread
    check (C3) passes on 2/3. Premise R1 holds: the common-mode ratio is at least 0.996.
  - **Makes live / unblocks:** the first experimental support for SD-077. That makes the
    promote-or-hold question for SD-077, and for the MECH-189 super-ordinal anchor pathway it
    fixes, a live `/governance` item.
  - **Gate on acting:** it is not yet in `pending_review` (landed after the pipeline run). C3 is
    marginal (seed 43 frac-below delta 0.31 < 0.5). The skew above must be cleared so the manifest
    is not lost.
- **V3-EXQ-1037 — SD-075 phasic-EMA episode continuity — PASS** (evidence, `supports`, already reviewed at governance-20260915)
  - **Moves:** SD-075 (candidate). Every warmed cell reaches an informative converged event rate
    (min 0.0256, bar 0.0167, ceiling 0.0333).
  - **Gate on acting:** governance flagged it as a dose result, not warmup causality. The
    criterion is absolute, and one unwarmed control cell (0.0238) also clears the bar.
- **V3-EXQ-1026 — MECH-423 sleep-integrated E2 consolidation — PASS** (diagnostic, `supports`, autopsied + confirmed)
  - **Moves:** MECH-423 (provisional). C1–C4 all pass. The E2 delta is entirely in the
    SELF-forward head.
  - **Makes live / gates:** `E2.world_forward` moved by exactly 0 and has no trainer on any sleep
    path, so **INV-063 leg B stays blocked**. The live decision is whether to build a
    world-forward sleep trainer.
- **V3-EXQ-1012a — MECH-439 E3 commensurability operator — PASS** (diagnostic, pending autopsy)
  - **Moves:** MECH-439 / `behavioral_diversity_isolation:GAP-I` (F-dominance). Operator selection
    changes the outcome in both regimes: flip rate 0.82 fed (bar 0.21) and 0.72 starved (bar 0.48),
    with 4/4 seeds above the floor each.
  - **Gate on acting:** a diagnostic PASS needs a confirmed `/failure-autopsy` before it drives GAP-I.
- **V3-EXQ-1028 / 1029 — SD-082 learning-signal and selection-authority diagnostics — PASS** (1029 reviewed; 1028 pending autopsy)
  - 1028 label `c2_noisy__c3_sign_null`: the learning signal is present but noisy (2 exhausted, 0
    persistent seeds). 1029 label `H_selection_authority_bounded_supported_magnitude_test_underpowered`.
    Read with 1027 FAIL (`H_replay_rule_state_mismatch_not_supported`), SD-082 now has three
    discriminating readings in a day. Decision: which hypothesis branch to pursue next.

Two PASS outcomes route **negatively**. They are not positives, but they change the next action:
- **V3-EXQ-1039 — MECH-428/INV-086 waypoint-field consumer drive signal:** `training_signal_does_not_convert_h1_not_supported`.
  Shaped and demo arms reach 0/5 seeds (0.2–0.27 visits/ep against an oracle's 11.6). Paired with
  1030 FAIL (z_world lift null, `precondition_unmet`), the waypoint field is not decodable from
  z_world and its training signal does not convert.
- **V3-EXQ-861i — INV-050/MECH-180:** confirms that mover `6293b23` (MECH-091 phase_reset)
  reproduces the recorded behaviour under the full protocol. This is attribution, not support.

---

## Decisions waiting on you

6 decision(s) recorded as awaiting your answer, oldest first. These do NOT block any session -- they are recorded requests, so nothing is stalled while they sit. Answer any of them with the command in its block, or reopen the asking session.

### MECH-074d -- waiting 38d

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

### MECH-316 -- waiting 31d

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

### MECH-317 -- waiting 31d

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

### MECH-314a -- waiting 31d

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

### MECH-091 -- waiting 31d

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

### MECH-122 -- waiting 30d

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

---

## Queue Status
- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0). 1 claimed/running: V3-EXQ-935a.
- **ALERT: Queue low. 0 claimable experiments** (threshold 3).
- Fleet-idle watcher: status OK, idle_risk=**true**, claimable backlog=0 (threshold 3), snapshot
  2026-09-15T03:58:00Z. Its only validation candidate is SD-106 -> V3-EXQ-1023, but **1023
  already ran** (manifest `v3_exq_1023_sd106_bottleneck_preservation_validation_20260912T045319Z_v3.json`),
  and the follow-on chip `chip-20260915-sd106-step-budget-diagnostic` is already open.
  `excluded_validation_already_ran` = 39. **Refilling the queue needs a fresh `/queue-experiment`
  design; a re-queue won't do.**
- Fleet git health: ree-cloud-1 hub OK; ree-cloud-4 OK; ree-cloud-3 REE_assembly **GC-BLOCKED**
  (`gc.log` present, automatic gc disabled); ree-cloud-2 UNREACHABLE (ssh timeout; it posted a
  result at 02:53Z, so check `hcloud server list` before assuming a fault); DLAPTOP REE_assembly
  **SKEW** (the 1040 staged deletion flagged above). No WEDGED checkouts.
- No owed successors: every Owner-EXQ on an in-flight or stale plan node (964a, 445h, 910b, 938)
  already has a manifest.

---

## Experiments Awaiting Review (5 indexed / 0 runner-only) — as of pending_review 01:21Z

### V3-EXQ-1030 — MECH-428/INV-086 waypoint-field z_world decodability — FAIL
- **Claims tested:** INV-086 (candidate, no evidence rows), MECH-428 (candidate, overall 0.74; exp 0 / lit 3)
- **Key metrics:** C1 z_world lift null not met (per-seed lift −0.03..+0.12, 1/5 positive); C0 raw positive control met (raw lift 0.21–0.42 on 5/5)
- **Classification:** diagnostic, `precondition_unmet` (`zworld_probe_extracts_known_signal`), self-route `substrate_not_ready_requeue`, direction non_contributory
- **Governance impact if confirmed:** none on confidence. Routes to `/failure-autopsy`, and pairs with 1039's negative reading.

### V3-EXQ-1038 — ARC-131 coalition endogenous recruitment rate probe — PASS
- **Claims tested:** ARC-131 (candidate, overall 0.80; exp 0 / lit 6)
- **Key metrics:** C0 readiness control fires 1.0/1.0 (guaranteed-fire positive control)
- **Classification:** diagnostic, label `endogenous_recruitment_engaged_at_default_threshold`, non_contributory
- **Governance impact if confirmed:** readiness only. Confirms the trigger is live, so an ARC-131 evidence experiment becomes designable.

### V3-EXQ-1012a — MECH-439 E3 commensurability selection-level regime validation — PASS
- **Claims tested:** MECH-439 (candidate, overall 0.80; exp 0 / lit 7)
- **Key metrics:** flip rate fed 0.82 (bar 0.21), starved 0.72 (bar 0.48); 4/4 seeds each; 0 self-check failures
- **Classification:** diagnostic
- **Governance impact if confirmed:** would give the F-dominance root (GAP-I) its first positive experimental reading.

### V3-EXQ-1028 — SD-082 learning signal, extended budget — PASS
- **Claims tested:** SD-082 (candidate_substrate_landed, overall 0.83; exp 0 / lit 8)
- **Key metrics:** C1 gradient present 5/5 (worst median grad norm 0.0106); C2 windowed persistence noisy 3/3 (2 exhausted, 0 persistent)
- **Classification:** diagnostic, label `c2_noisy__c3_sign_null`, direction unknown
- **Governance impact if confirmed:** narrows SD-082's failure to a noisy learning signal. The sign test is null.

### V3-EXQ-1036 — EXT-002 stage-2 revisit-rate DV calibration — PASS (unclaimed baseline)
- **Claims tested:** none (bears on EXT-002/ARC-013)
- **Key metrics:** 3 non-degenerate seeds; decline_rate_gap mean −0.00043, range 0.00129; A1 control range 0.00128
- **Classification:** baseline calibration. It banks the statistic a future C1 bar should be derived from. Mark the manifest stem as discussed.

---

## Errors to Diagnose (0)

The coordinator DB shows 2 ERRORs in the last 30 days (1.7%, 2/118). Both already have lettered
successors: V3-EXQ-944a -> 944b ran 2026-08-25, and V3-EXQ-591g -> 591h ran 2026-09-03. Nothing is outstanding.

---

## Governance Agenda (6 pending_user recommendations)

- **ARC-069** (candidate) — **hold** (`hold_pending_v3_substrate`) — exp 0 / lit 3, overall 0.80
- **ARC-075** (candidate) — **hold** (`hold_pending_v3_substrate`) — exp 0 / lit 4, overall 0.79
- **ARC-076** (candidate) — **hold** (`hold_pending_v3_substrate`) — exp 0 / lit 3, overall 0.53 (speculative)
- **MECH-012** (candidate) — **hold** (`hold_candidate_resolve_conflict`) — exp 0 / lit 6, overall 0.63
- **MECH-013** (candidate) — **hold** (`hold_candidate_resolve_conflict`) — exp 0 / lit 6, overall 0.67
- **MECH-349** (candidate) — **hold** (`hold_pending_v3_substrate`) — exp 1 PASS (V3-EXQ-1025) / lit 0, overall 0.77 (novel_discovery). One PASS already exists, so check whether the substrate hold is still accurate.

**Granularity-debt recurrence (GOV-GRAN-1):** no P0 dropped handoffs. The audit lists 50 P1
unflagged-recurrence claims for discrimination. No chips were spawned. The largest:
- **INV-050**: 13 hits / 9 signatures, alignment unclear=8 intact=4 n/a=1. No weakened readings, so it is likely measurement debt (the 861 cluster).
- **MECH-180**: 12 hits / 8 signatures, unclear=8 intact=2 n/a=1 other=1. No weakened readings; likely measurement debt.
- **SD-082**: 8 hits / 6 signatures, unclear=8. No weakened readings; this is the current discrimination campaign (1027–1029).
- **SD-078**: 7 / 6, unclear=7. No weakened readings.
- **MECH-075**: 7 / 5, intact=5 other=2. No weakened readings.
- **MECH-111**: 5 / 3, other=4 **weakened=1**. The weakened reading makes this a real coarse-claim candidate.
- **Q-034**: 6 / 2, **weakened=3** other=3. Coarse-claim candidate.
- **INV-054**: 4 / 2, **weakened=2**. Coarse-claim candidate.
- Also carrying weakened readings: ARC-018 (2/2), ARC-038 (3/1), SD-005 (3/1).

**Epistemic-category completeness (GOV-CAT-1):** clean. missing_category 0, invalid_category 0
(673 historical excluded); 10 legacy-schema warns, 2 claimless-missing, 0 malformed markers.

---

## Active Plans Heartbeat (18 plans; 13 non-done)

From `closure_status.md` (2026-09-14T23:46Z). Weighted progress is 72.3% across 98 nodes: 34
remaining, 11 assembling (exempt from staleness), 64 done.

| Plan | In-flight | Blocked | Paused | Assembling | Stale rows (>7d) | Last updated |
|---|---|---|---|---|---|---|
| conversion_ceiling_campaign | 0 | 0 | 0 | 7 | 0 | 2026-07-10 |
| global_workspace_jlens | 2 open | 2 | 0 | 0 | 3 | 2026-09-08 |
| policy_decomposition_trigger | 0 | 1 | 0 | 0 | 1 | 2026-08-21 |
| zworld_adequacy | 0 | 1 upstream_blocked | 0 | 1 | 0 | 2026-09-11 |
| sd_037_axis_b | 0 | 3 | 0 | 1 | 3 | 2026-06-23 |
| self_attribution | 0 | 4 | 0 | 0 | 4 | 2026-09-04 |
| orienting_epistemic_deficit_v3 | 4 | 1 | 0 | 0 | 4 | 2026-09-11 |
| mech357_avoidance_efficacy | 1 partial | 0 | 0 | 0 | 1 | 2026-08-29 |
| arc_062_rule_apprehension | 3 | 3 | 0 | 0 | 6 | 2026-09-01 |
| behavioral_diversity_isolation | 3 | 1 | 0 | 1 | 4 | 2026-09-02 |
| commitment_closure | 2 | 0 | 0 | 1 | 1 | 2026-09-08 |
| sleep_substrate | 0 | 1 upstream_blocked | 0 | 0 | 1 | 2026-08-14 |
| infant_substrate | 1 | 1 | 0 | 0 | 2 | 2026-09-04 |

Stale owner-EXQ status (Step 7c):
- `orienting_epistemic_deficit_v3:ORNT-2`: owner V3-EXQ-964a **ran, FAIL/non_contributory**, and is already autopsied (`failure_autopsy_V3-EXQ-964a_20260914`). Only the node row needs reconciling.
- `orienting_epistemic_deficit_v3:ORNT-6`: owner V3-EXQ-910b ran 2026-08-22 (PASS/supports) and is confirmed autopsied. The row has not been reconciled.
- `self_attribution:GAP-1`: owner V3-EXQ-445h ran 2026-05-08. The node is **gated** on the same upstream substrate gates as GAP-2.
- `policy_decomposition_trigger:REPOSE`: owner V3-EXQ-938 ran FAIL/non_contributory and was autopsied and applied 2026-08-21. The node is blocked pending a re-pose design.

**Ran — may need /failure-autopsy:** none. Both FAIL owners are already autopsied.

**PLAN STALING:** `sd_037_axis_b`: no update since 2026-06-23, with the P2–P4 chain blocked on
P1b. `arc_062_rule_apprehension`: GAP-J last updated 2026-05-17, GAP-K 2026-06-19, GAP-I
2026-06-23.

---

## Literature Pull Candidates (Top 5)

No high-priority backlog items need literature. There are 478 open or in-progress items that do
(all medium or low). The first five in backlog order:

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | ARC-079 | Unresolved goal persistence as a gated re-probe target | medium | 0 |
| 2 | ARC-082 | Tools/affordances as object->action binding (ARC-080 pillar 3) | medium (in_progress) | 0 |
| 3 | ARC-083 | Others-as-object token-keyed agents (ARC-080 pillar 4) | medium (in_progress) | 0 |
| 4 | ARC-084 | Typed signed cognifold coupling | medium | 0 |
| 5 | ARC-089 | Substrate-independent cognifold primitives | medium | 0 |

---

## Stale Claims (0 active > 6h)

Stale claims: none (clean steady state).

---

## Serve.py Status
- **NOT RUNNING** on port 8000. Start it with: `cd /Users/dgolden/REE_Working/REE_assembly && python serve.py &`

---

## Blocked Items
- `governance.sh` was skipped (Tier 2). Two live non-stale claims exist: `orchestrate-20260915-0203` and `eloquent-jepsen-5f6242`. Neither names a governance file.
- The staged-deletion skew on the V3-EXQ-1040 manifest in the shared REE_assembly checkout is not repaired; see the top of this agenda.
- ree-cloud-3 REE_assembly is GC-blocked (`gc.log`). Not repaired, since this skill only reports fleet state.
