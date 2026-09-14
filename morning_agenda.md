# Morning Agenda — 2026-09-14

Generated: 2026-09-14T04:26:56Z

Tier 1 full run: `governance.sh` ran to completion (exit 0, 6m36s). No live claims at start. The
last digest was 2026-09-11 (Friday). The two days since were Saturday and Sunday, and the cron
(`7 5 * * 1-5`) doesn't fire on weekends, so no runs were missed.

---

## THE ONE THING TODAY: the fleet has been idle for ~48h and nothing is set to refill it

The queue has been **empty since the 2026-09-12 snapshot**. The last result reached the coordinator
at **2026-09-12T04:53Z** (V3-EXQ-1023). I checked the coordinator DB directly over ssh: it has
**0 pending / 0 claimed**. The fleet-idle watcher agrees (`status: OK`, `idle_risk: true`,
`claimable_backlog: 0` against a threshold of 3, snapshot `2026-09-14T03:42:14Z`, so it's fresh).
`ready_sd_validation_candidates` is **empty** across 82 ready SDs (`excluded_validation_already_ran: 39`,
`excluded_no_queueable_validation: 39`). Re-queuing an old validation won't refill this. It needs
new `/queue-experiment` designs.

**Friday's refill leads both came back negative:**

- `chip-20260910-recover-stranded-exq-1018-1003` is **done, and both scripts were refused**. Neither
  was queued (REE_assembly `b0d0a1a887`,
  `evidence/planning/exq1026_mech005_nu_path_authority_refusal_20260911.md`). The two scripts are
  still untracked in `ree-v3/experiments/`.
- `chip-20260910-merge-paced-proposal-triage` is **done: 0 GREEN / 1 AMBER / 7 RED**. None of the 8
  paced proposals can be built right now.
- `chip-20260910-curated-pause-window-g6` staged an agenda at
  `evidence/planning/curated_pause_window_agenda_20260911.md` (`9785847013`). **It is a proposal only.
  The halt was not carried out and is waiting for your review.** While that is undecided, chip
  over-production is the reason this digest **spawned no new chips** (see Blocked Items).

**The best candidates for new designs come from this weekend's results.** V3-EXQ-1023 says the
first SD-106 build **does not close** the observation->z_world gap (below). V3-EXQ-1025 gives
MECH-349 its first indexed evidence (below). V3-EXQ-964a narrows MECH-482: the readout
differentiates, but the committed action never changes.

---

## Headlines — Positive Results & Live Decisions

These are new results since the 2026-09-11 digest (the prior agenda already covered 1019 and 1020).
One positive, plus one decision-relevant negative that sits on the v3 binding constraint.

- **V3-EXQ-1025 — `mech349_crf_churn_retirement` — PASS** (evidence, `supports`, `ree-worker-3`, 2026-09-11T18:11Z)
  - **Moves:** **MECH-349** (CandidateRule mint, ARC-063 CREATE face). This is the first
    experimental entry the indexer has credited to MECH-349: `claim_evidence` now reads exp=1,
    exp_conf **0.77**, where GFLAG-0198 recorded zero entries. Churn is **selective, not a
    treadmill**. Extinct regularities are retired (C2 5/5 cells) while still-recurring ones keep
    their slots, with zero persistent retirements or re-mints (C1 5/5). The same substrate *does*
    produce the 666c treadmill at a higher dose, so the negative is not vacuous. MECH-349
    FALSIFYING(3) does not occur.
  - **Makes live:** the pipeline now puts **MECH-349 on the Governance Agenda as `pending_user`**
    (`hold_pending_v3_substrate`). Whether the V3-pending hold still fits a claim that now has
    direct V3 evidence is a real decision, not a routine re-accept.
  - **Before acting:** it's a single run and hasn't been reviewed. Take it through the normal
    `/governance` walk. It is a claim-tagged PASS, so no autopsy is needed.

- **V3-EXQ-1023 — `sd106_bottleneck_preservation_validation` — FAIL** (diagnostic, `ree-cloud-2`, 2026-09-12T04:53Z). *This isn't a positive. It's here because it changes what to do next on the most important node in v3.*
  - **Result:** SD-106 (scale-normalised reconstruction plus a zero-init linear bypass at the
    observation->z_world encoder) reaches consumer agreement of **0.719 mean / 0.699 min**. The
    OFF arm reaches 0.668 and the PCA-32 anchor 0.869. **0 of 3 seeds clear the 0.85 parity bar.**
    All five preconditions were met: the raw-field instrument ceiling was 0.974, the PCA anchor
    cleared on 3/3, the bypass trained off zero, the encoder trained in P0, and the latent did not
    collapse. So this is a readable null, not a broken instrument. SD-106 moves the latent a
    little (+0.05) and doesn't come close to PCA parity at the same width.
  - **Bears on:** `zworld_adequacy:ZW-1` (assembling, `awaiting: SD-106`). This is the v3 binding-constraint
    interface, and most of the remaining closure work chains through it (ZW-1
    `unblocks_claims`: INV-088, MECH-457, SD-015, ARC-030, MECH-117, ARC-065). The built form of SD-106 doesn't close it, so ZW-1's
    `assembly_status` and the SD-106 design need another look.
  - **Before acting:** this is **diagnostic, so a confirmed `/failure-autopsy` is required** before
    anything is applied from its self-route (`sd106_below_pca32_parity`).

---

## Decisions Waiting on You (6)

6 decision(s) recorded as awaiting your answer, oldest first. These do NOT block any session -- they are recorded requests, so nothing is stalled while they sit. Answer any of them with the command in its block, or reopen the asking session.

### MECH-074d -- waiting 37d

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

### MECH-316 -- waiting 30d

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

### MECH-317 -- waiting 30d

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

### MECH-314a -- waiting 30d

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

### MECH-091 -- waiting 30d

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

### MECH-122 -- waiting 29d

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

- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0). The coordinator DB has 0 pending and 0 claimed.
- **ALERT: the queue is empty** (fewer than 3). It has been empty since 2026-09-12, and the fleet has had no work for ~48h.
- Fleet-idle watcher: `status: OK`, idle_risk=**true**, claimable backlog=0 (threshold 3),
  snapshot 2026-09-14T03:42:14Z. `ready_sd_validation_candidates` is **empty**
  (82 ready SDs; 39 validations already ran, 39 have no queueable validation, 4 excluded as known churn), so
  **refill needs a new `/queue-experiment` design, not a re-queue**.
- Owed successors: none. Every Owner-EXQ on an in-flight, blocked or stale plan node
  (V3-EXQ-910b, -938, -445h, -964a) **has already run** (Step 7c check (b): manifests present).
- Phantom Owner-EXQ ids: none found.

---

## Experiments Awaiting Review (3 indexed / 0 runner-only)

### V3-EXQ-1025 — `mech349_crf_churn_retirement` — PASS
- **Claims tested:** MECH-349 (status: candidate; indexed exp confidence 0.77; prior evidence: 0 indexed entries before this run, so this is the first)
- **Key metrics:** C1 persistent regimes hold their slot 5/5 cells (worst cell 0 retired+re-minted persistent); C2 extinct regimes retired 5/5 (worst cell 6 retired); C3 live population distinct in tag space 5/5 (non-load-bearing)
- **Classification:** evidence (`supports`)
- **Governance impact if confirmed:** it would give MECH-349 its first direct V3 experimental support. That bears on whether its `hold_pending_v3_substrate` recommendation (now `pending_user`) still applies.

### V3-EXQ-1023 — `sd106_bottleneck_preservation_validation` — FAIL
- **Claims tested:** SD-106 (status: implemented; the claim itself says "NO EXPERIMENTAL EVIDENCE YET"; no indexed entries)
- **Key metrics:** SD-106 consumer agreement 0.719 mean / 0.699 min vs OFF 0.668 and PCA-32 anchor 0.869; parity bar 0.85, 0/3 seeds clear it; all 5 preconditions met; participation ratio worst 8.13 (not collapsed)
- **Classification:** diagnostic. **Needs a confirmed `/failure-autopsy`** (self-route `sd106_below_pca32_parity`)
- **Governance impact if confirmed:** the first measured evidence that SD-106 *as built* does not bring observation->z_world up to PCA parity. Bears directly on `zworld_adequacy:ZW-1` (assembling, awaiting SD-106).

### V3-EXQ-964a — `mech482_epistemic_deficit_multitarget_readiness` — FAIL
- **Claims tested:** MECH-482 (status: candidate; no indexed entries; the 2026-08-30 governance note records that V3-EXQ-964's C2 was structurally unsatisfiable)
- **Key metrics:** C1 multitarget regime reached (14 vs ≥2) ✓; C2 readout differentiates (0.0044 > 0) ✓; **C3 downstream consumer can diverge = 0.0** ✗ (load-bearing); C4 instrument control bit-identical ✓
- **Classification:** diagnostic, `evidence_direction: mixed`. **Needs a confirmed `/failure-autopsy`** (self-route `readout_differentiates_but_never_changes_committed_action`)
- **Supersedes:** V3-EXQ-964. It fixes the structurally unsatisfiable C2, which now passes. The failure has moved to C3.
- **Governance impact if confirmed:** the 964→964a successor worked. The remaining gap is that no consumer acts on the epistemic_deficit readout. It owns `orienting_epistemic_deficit_v3:ORNT-2`, which ORNT-3 and ORNT-4 depend on.

---

## Errors to Diagnose (0)

There are 2 ERRORs in the last 30 days (coordinator DB, rate 1.8%, 2/109). **Both already have successors**:
- V3-EXQ-944a (ERROR 2026-08-22, ree-cloud-3) → V3-EXQ-944b ran 2026-08-25
- V3-EXQ-591g (ERROR 2026-09-02, ree-cloud-2) → V3-EXQ-591h ran 2026-09-03

---

## Governance Agenda (4 recommendations)

- **MECH-349** (candidate) — Recommendation: **hold** (`hold_pending_v3_substrate`)
  - Evidence: 1 experimental (V3-EXQ-1025, supports), 0 literature
  - Current confidence: 0.77 (exp)
  - *New this cycle, because of V3-EXQ-1025. See Headlines.*
- **MECH-012** (candidate) — Recommendation: **hold** (`hold_candidate_resolve_conflict`)
  - Evidence: 0 experimental, 6 literature
  - Current confidence: 0.63 (lit)
- **MECH-013** (candidate) — Recommendation: **hold** (`hold_candidate_resolve_conflict`)
  - Evidence: 0 experimental, 6 literature
  - Current confidence: 0.67 (lit)
- **ARC-069** (candidate) — Recommendation: **hold** (`hold_pending_v3_substrate`)
  - Evidence: 0 experimental, 3 literature
  - Current confidence: 0.80 (lit)

The 2026-09-11 cycle accepted 10 holds. The four above are what is still `pending_user`.

**Granularity-debt recurrence (GOV-GRAN-1):** **P0 `dropped_handoff`: 0, which is clean.** No chip needed.
P1 `unflagged_recurrence`: **50 claims**, the same set as 2026-09-11. Only **6** have any `weakened`
alignment, which is what makes granularity debt more likely than measurement debt. These need a human
to decide between a coarse claim and a substrate campaign; no action has been taken:
- **Q-034** — 6 hits, alignment weakened=3 other=3
- **SD-005** — 3 hits, alignment weakened=3
- **ARC-038** — 3 hits, alignment weakened=3
- **INV-054** — 4 hits, alignment weakened=2 other=2
- **MECH-111** — 5 hits, alignment other=4 weakened=1
- **ARC-018** — 2 hits, alignment unclear=1 weakened=1

The other 44 have no `weakened` alignment and are probably measurement or implementation debt. The largest are INV-050 (12 hits, unclear=8 intact=4), MECH-180 (11), MECH-058 (13, legacy V2 bridge runs), SD-078 (7, all unclear), MECH-075 (7, intact=5) and SD-082 (6, all unclear).

**Epistemic-category completeness (GOV-CAT-1):** **clean.** `missing_category: 0`,
`invalid_category: 0`, `malformed_markers: 0`. P1 only: 10 `unkeyed_schema` and 2
`claimless_missing`. Baseline holds at 673 excluded instances. **Do not regenerate that snapshot.**

---

## Active Plans Heartbeat (13 non-done v3 plans of 18)

Source: `closure_status.md` (regenerated this run) plus per-node `last_updated` from each plan's
frontmatter. Stale = not done, deferred or assembling, with `last_updated` more than 7 days before
2026-09-14. Overall closure is **72.3%**: 64 done, 34 remaining, 11 assembling, 10 deferred.

| Plan | Phases in-flight | Blocked | Paused | Assembling | Stale rows | Last decision |
|---|---|---|---|---|---|---|
| arc_062_rule_apprehension | 3 | 3 | 0 | 0 | 6 | 2026-07-29 |
| behavioral_diversity_isolation | 3 | 1 | 0 | 1 | 4 | (no decision log) |
| orienting_epistemic_deficit_v3 | 4 | 1 | 0 | 0 | 4 | 2026-08-22 |
| self_attribution | 0 | 4 | 0 | 0 | 4 | 2026-08-18 |
| global_workspace_jlens | 2 | 2 | 0 | 0 | 3 | (no decision log) |
| sd_037_axis_b_sustained_threat_curriculum | 0 | 3 | 0 | 1 | 3 | (no decision log) |
| infant_substrate | 1 | 1 | 0 | 0 | 2 | 2026-05-21 |
| commitment_closure | 2 | 0 | 0 | 1 | 1 | 2026-09-08 |
| mech357_avoidance_efficacy | 1 | 0 | 0 | 0 | 1 | 2026-08-13 |
| policy_decomposition_trigger | 0 | 1 | 0 | 0 | 1 | 2026-08-18 |
| sleep_substrate | 0 | 1 | 0 | 0 | 1 | 2026-08-14 |
| zworld_adequacy | 0 | 1 | 0 | 1 | 0 | 2026-09-11 |
| conversion_ceiling_campaign | 0 | 0 | 0 | 7 | 0 | (no decision log) |

"Blocked" counts `blocked`, `blocked_pending_substrate` and `upstream_blocked` together. The
per-status split is in `closure_status.md`.

**Stale rows (30), with each Owner-EXQ status from Step 7c:**

- **arc_062_rule_apprehension:** GAP-B (09-01), GAP-H (07-20), GAP-I (06-23), GAP-I-absorption (09-01), GAP-J (05-17), GAP-K (06-19). No owner_exq.
- **behavioral_diversity_isolation:** GAP-B (08-01), GAP-C (07-10), GAP-G (08-18), GAP-I (09-02). No owner_exq.
- **orienting_epistemic_deficit_v3:** ORNT-1 (08-13), ORNT-3 (08-13), ORNT-4 (08-13), ORNT-6 (08-25): Owner-EXQ V3-EXQ-910b, **ran** 2026-08-22 and was confirmed-autopsied. The row isn't reconciled yet. ORNT-2 isn't stale (09-11), but its owner V3-EXQ-964a **ran and FAILed 2026-09-11**. See Awaiting Review.
- **self_attribution:** GAP-1 (08-18): Owner-EXQ V3-EXQ-445h, **ran**. GAP-2 (08-18, owner TBD), GAP-3 (06-25, owner TBD), GAP-6 (09-04).
- **global_workspace_jlens:** A (07-10), B (07-09), MECH-191 (07-09). GATE-B isn't stale (09-08).
- **sd_037_axis_b:** P2, P3, P4 (all 06-05). This is a depends_on chain behind P1b.
- **infant_substrate:** GAP-13 (07-20), GAP-14 (09-03).
- **commitment_closure:** GAP-4-battery (08-21).
- **mech357_avoidance_efficacy:** BUILD (08-29).
- **policy_decomposition_trigger:** REPOSE (08-21): Owner-EXQ V3-EXQ-938, **ran**, and its autopsy was applied 2026-08-21.
- **sleep_substrate:** GAP-2 (08-13).

No stale row has an owed Owner-EXQ. Every stale row is waiting on a substrate or an upstream
dependency, or its owner already ran and the row hasn't been reconciled.

**Ran — may need /failure-autopsy:**
- V3-EXQ-964a (plan orienting_epistemic_deficit_v3, row ORNT-2): ran 2026-09-11, FAIL/mixed, no confirmed autopsy yet.

**PLAN STALING** (no decision logged in >14 days while rows are in flight):
- arc_062_rule_apprehension: no decisions since 2026-07-29; 3 rows in flight.
- orienting_epistemic_deficit_v3: no decisions since 2026-08-22; 4 rows in flight.
- infant_substrate: no decisions since 2026-05-21; 1 row in flight.
- mech357_avoidance_efficacy: no decisions since 2026-08-13; 1 row in flight.
- behavioral_diversity_isolation, global_workspace_jlens: no `## Decision log` section at all; 3 and 2 rows in flight.

---

## Literature Pull Candidates (Top 5)

All 481 backlog items needing literature are priority `medium` (or `low`), so there's no ranking
signal. These are the first 5 `open` items in backlog order. Each has **0 experimental and 0
literature** entries. Existing-entry counts come from `record.json` `claim_ids_tested`.

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | ARC-075 | Infant curriculum must implement plasticity-magnitude asymmetry (suppress F during MECH-333 window), not only temporal scheduling | medium | 0 |
| 2 | ARC-076 | Developmental commitment-loop calibration window with critical-period lock (two-layer temperament/personality) | medium | 0 |
| 3 | ARC-079 | Goal persistence as a gated control op; disengagement is the ungated default | medium | 0 |
| 4 | ARC-084 | Typed signed cognifold coupling (competition as a first-class generative mode) | medium | 0 |
| 5 | ARC-089 | Substrate-independent cognifold primitives | medium | 0 |

---

## Stale Claims (3 active > 6h)

- Buckets: A(auto-closable) 0 | B(vendor-sync) 0 | C(no-trace) 1 | D(dirty-unproven) 1 | U(undetermined) 1
- **[D]** `codex-showcase-build-20260911-exq1021` (62h): queue-experiment: V3-EXQ-1021. `experiments/v3_exq_1021_survive_recover_resume_showcase.py` and `experiments/showcase_replay.html` are dirty (untracked) and can't be proven complete. **Don't commit or revert them.** V3-EXQ-1021 is **not** in the queue.
- **[U]** `codex-showcase-build-20260911` (62h): REE showcase implementation. It's directory-scoped (`ree-v3/experiments/`, `ree-v3/docs/experiments/`), so landing can't be attributed.
  - warn: shared/directory resource is dirty, likely another live session: ree-v3/experiments/
- **[C]** `orchestrate-20260913-1643` (11.6h): orchestrate 2026-09-13. Nothing landed and nothing is dirty; that pattern can't separate an abandoned claim from a wrong-direction one. It's already chipped as `chip-staleclaim-orchestrate-20260913-1643-20260913T164610Z` (open).
- Also: `governance-sh-DLAPTOP-4` (this run's governance lock) is **`done` locally but still `active` on origin**. `governance.sh` printed `failed to close TASK_CLAIMS claim`, because the close committed only to the diverged umbrella checkout (see Blocked Items). Bucket G auto-reaps it after 2h, so no manual action is needed.

---

## Fleet Git Health

- DLAPTOP, ree-cloud-1 (hub) and ree-cloud-4: REE_assembly and ree-v3 both **OK**, with 0 stranded manifests.
- ree-cloud-2 and ree-cloud-3: **UNREACHABLE** over ssh. With 0 queue demand they're most likely powered off by the scaler, which isn't a fault.

---

## Serve.py Status
- **NOT RUNNING** on port 8000. Start it with: `cd /Users/dgolden/REE_Working/REE_assembly && /opt/local/bin/python3 serve.py &`

---

## Blocked Items

- **The Mac's WireGuard tunnel is down.** This Mac has no `10.8.0.x` address, and 10.8.0.1 doesn't
  answer ping. On the hub, `ree-coordinator` and `wg-quick` are both `active`, and ssh to the
  public IP works. Because of this, every coordinator-routed helper on this Mac (`task_claim.py`,
  `chip_ledger.py`) is using the **degraded git path**. This session's claim was opened that way
  (umbrella `465889f900`, pushed through a throwaway worktree). Bringing the tunnel back up is a
  local network action for you; it needs your password.
- **The umbrella `REE_Working` checkout has diverged** (`master` ahead 10 / behind 15 at start). This
  is already chipped as `chip-checkoutdiverged-dlaptop-ree-working-master-g5` and
  `chip-refwedge-dlaptop-ree-working-master-g3` (both open), so I didn't touch it here. It's why the
  governance lock close above didn't reach origin.
- **No chips were spawned by this digest.** The follow-on it would raise is either
  `/governance` or `/failure-autopsy` work, which gets reported rather than chipped (964a and 1023
  autopsies, the 1025 review, 4 pending_user holds), or it is already chipped (the umbrella wedge,
  the stale orchestrate claim). The rest is queue-refill design, where the curated pause window
  (`chip-20260910-curated-pause-window-g6`, waiting for your review) is the open decision on chip
  over-production. There are 122 open chips in the ledger.
