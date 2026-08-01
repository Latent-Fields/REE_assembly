# Project Insights — 2026-08-01

Generated: 2026-08-01T10:44:08Z

---

## Experiment Health

- **Total runs:** 227 (PASS: 77 | FAIL: 150 | ERROR: 0 | error rate: 0.0%) — window: last 30 days
  (2026-07-02T05:25Z .. 2026-08-01T07:34Z), source: coordinator DB. 6 unexplained phantom
  completions (no evidence on disk) are not folded into the numerator; treating every one as a
  crash gives an upper bound — **error rate: 0.0%–2.6% (0 recorded ERROR / 227 classified; 6
  phantom completions unclassified)**.
- **Last ERROR recorded fleet-wide:** 2026-06-11T21:18:10Z (per-machine `runner_status/` split;
  the synthetic ERROR-record path only went live 2026-06-17, so counts before that date
  understate the true historical rate — the live 30-day window above is unaffected).
- **High-iteration experiments** (3+ lettered iterations) — 52 base EXQ numbers cleared the
  threshold out of 363 tracked in the manifest corpus. Top 20 by iteration count:
  - EXQ-603 — 18 iterations — claims: MECH-260, MECH-313, MECH-358, Q-045, SD-059 — last: PASS
  - EXQ-460 — 15 iterations — claims: ARC-108, MECH-090, MECH-260, MECH-261, MECH-342, MECH-445,
    MECH-446, SD-034 — last: PASS
  - EXQ-485 — 14 iterations — claims: MECH-261, MECH-263, SD-033b — last: FAIL
  - EXQ-543 — 12 iterations — claims: ARC-062, INV-074, MECH-309, MECH-334, SD-029 — last: FAIL
  - EXQ-418 — 11 iterations — claims: SD-016, SD-017 — last: FAIL
  - EXQ-514 — 11 iterations — claims: MECH-229, MECH-230, MECH-436, SD-015, SD-049 — last: PASS
  - EXQ-689 — 10 iterations — claims: ARC-107, MECH-439, MECH-448, MECH-449 — last: FAIL
  - EXQ-654 — 10 iterations — claims: ARC-062, MECH-309 — last: FAIL
  - EXQ-569 — 8 iterations — claims: ARC-065, MECH-341 — last: PASS
  - EXQ-445 — 7 iterations — claims: (none tagged) — last: weakens
  - EXQ-610 — 7 iterations — claims: INV-074, MECH-313, MECH-333, MECH-334, MECH-341 — last: FAIL
  - EXQ-680 — 6 iterations — claims: MECH-423 — last: PASS
  - EXQ-614 — 6 iterations — claims: ARC-065, MECH-341 — last: FAIL
  - EXQ-468 — 5 iterations — claims: MECH-090, MECH-268, SD-034 — last: FAIL
  - EXQ-591 — 5 iterations — claims: (none tagged) — last: PASS
  - EXQ-625 — 5 iterations — claims: (none tagged) — last: FAIL
  - EXQ-700 — 5 iterations — claims: ARC-108, MECH-439, MECH-450 — last: FAIL
  - EXQ-836 — 5 iterations — claims: MECH-476 — last: FAIL
  - EXQ-517 — 5 iterations — claims: MECH-302 — last: PASS
  - EXQ-733 — 4 iterations — claims: MECH-456 — last: PASS

  Note: "last outcome: FAIL" here is a raw letter-count fact, not a stalled-chain claim — see the
  liveness-gated section below; several of these (543, 610, 614, 468, 689) are live, actively-owned
  campaign legs (MECH-341, ARC-062/MECH-309, SD-034 clusters), not dead ends.

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries): **none in the 30-day window** —
  ERROR count is 0/227 for the period, so there is no ERROR-based trouble-spot signal to report.
  (Historically the last fleet-wide ERROR was 2026-06-11, well outside this window.)

- **Stalled chains** (FAIL with no successor queued) — liveness check executed per the skill's
  mandatory 4-leg procedure. Candidate pool: 78 chains whose most-recent lettered iteration ended
  FAIL, deduplicated to 34 unique claim_ids and screened to those last touched >3 weeks ago (the
  remainder are too recent to plausibly be "stalled" rather than "mid-cycle"). Legs checked for
  all 34: TASK_CLAIMS.json (incl. `done`), autopsy-file content grep, successor-manifest grep
  under any EXQ number, and `git log --since="7 days ago"`.
  - 33 of 34 claims had at least one autopsy-file hit (4–117 files each) — adjudicated, not
    stalled.
  - The one claim with zero autopsy/TASK_CLAIMS hits, **ARC-038**, is not stalled either: its
    claims.yaml entry documents the FAIL (EXQ-355a) as reclassified `non_contributory` (a
    write-gating-propagation artifact, not real evidence against the claim) and explicitly gates
    retest on **MECH-261** (`pending_retest_after_substrate`).
  - **None — all candidate chains have an owner, an autopsy, or a documented substrate-gate
    reason.** No claim survives the liveness check as genuinely stalled this cycle.

---

## Substrate Bottlenecks

- **Ready SDs** (`ready: true` in `substrate_queue.json`, not yet `implemented`) — 18 entries:
  SD-047, SD-048, INF-ENV-002, INF-ENV-004, MECH-341, MECH-090, `scaffolded_sd054_onboarding`,
  `test_bed_enrichment_crystallization_necessity`, `modulatory-bias-selection-authority`,
  `crf-availability-maintenance`, `sd_actor_critic_action_learning`,
  `agency_comparator_testbed_sd047`, `rebinding-harness-p0-coverage-decoupling`, SD-074,
  SD-PROBE-WARMUP, `sd_zworld_warmup_optimizer_group`, SD-MEL-PRODUCER,
  MECH324-REACQ-WINDOW-GATING-DECOUPLE. Caveat: `implementation_status` is a sparse free-text
  field on this file — several of these (e.g. MECH-341, MECH-090) carry substantial amend history
  in other free-text fields (`status`, `amend_note_*`) this pass did not fully parse, so treat
  "18" as an upper bound on genuinely unbuilt-and-ready work, not a precise count.
- **Blocked SDs** (`depends_on_unresolved` non-empty): 38 entries. Notable: SD-033 family
  (SD-033b/c/d/e all block on MECH-261, plus ARC-035/MECH-116/151/152/235 variously), SD-083
  (blocked on its own missing `/failure-autopsy` adjudication for V3-EXQ-829), `v4_loop_segregation`
  (blocked on ARC-109/MECH-452/451 sequencing).
- **SDs with failure records** (experiments failed because missing), by count: `scaffolded_sd054_onboarding`
  28, `f_dominance_conversion_ceiling` 26, `modulatory-bias-selection-authority` 15, ARC-062 11,
  MECH-256 10, `v4_loop_segregation` 10, SD-049-PHASE-2 9, ARC-065 8, `commitment-closure-control-plane` 7,
  SD-037 6, `mech457_competence_bootstrap_explorer` 6.

Cross-reference with Step 2: the ARC-062/MECH-309 pair (EXQ-543, EXQ-654 chains, 11 failure
records) and the MECH-341 cluster (EXQ-610, EXQ-614, EXQ-569, 5–8 failure records) are both
high-iteration AND high-failure-record — but both are liveness-confirmed live campaigns (autopsy
counts in the dozens), not missing-substrate bottlenecks in the naive sense.

---

## Governance State

- Claims pending V3 substrate (`v3_pending: true`): 228
- Pending promotion/demotion decisions: **0** — all 169 rows in the current Decision Queue
  (`evidence/experiments/promotion_demotion_recommendations.md`, regenerated 2026-08-01T10:09Z)
  show `decision_status: applied`. The 2026-07-30/31 governance cycles cleared the backlog that
  existed earlier in the window.
- Evidence superseded (rework): 72 manifests carry `evidence_direction: "superseded"`.

---

## Literature Coverage

- Priority-1 backlog items still open: **none** — the 3 open literature-flagged items (Q-086,
  Q-087, Q-088) are all `priority: low`; the one `priority: medium` item (Q-019) is `covered`.
- Total open literature items: 3 (Q-086, Q-087, Q-088)
- Covered in recent sessions: 5 `targeted_review_*` entries landed in the last 4 days
  (connectome/MECH-204, MECH-457 consolidation, MECH-457 baseline-informativeness, Q-085,
  SD-082), plus a MECH-324 connectome review 4 days prior — a healthy, active cadence, not a
  backlog.

---

## Human-Intervention Patterns

Derived from the WORKSPACE_STATE.md tail (last 200 lines, ~42 dated entries, spanning
2026-07-20 to 2026-08-01):

- Session-type mix in the tail: governance (41 mentions), queue-experiment (19),
  implement-substrate (15), failure-autopsy (12), lit-pull (7), claim-synthesis (3),
  session-land (3), morning-digest (1), diagnose-errors (1). Governance dominates because it is
  the nexus skill that surfaces and routes the most follow-on work (per this repo's own
  session-land convention).
- Explicit user-adjudication / pause points: 9 entries reference a user confirmation, adjudication,
  or explicit user instruction (e.g. the 2026-07-19 split-vs-eliminate call on the MECH-457
  competence-retention leg, the 2026-07-22 objective-misspecification cluster adjudication) — this
  is the recurring low-friction-but-not-zero pattern: `/failure-autopsy` runs mostly headless but
  regularly reaches a genuine judgment call at its Step-8 gate that only a human can close.
  Claim-synthesis in the same window shows 2 of 3 mentions being outright Step-3 gate refusals
  (MECH-440, MECH-204) rather than pass-throughs — a recurring stop point worth noting, though the
  same-window sample is small.
- `NOT LANDED:` markers: 3 in the tail — none aged past the same session's own close, i.e. no
  standing abandoned side-branch surfaced in this window.
- Low-friction headless tasks: lit-pull (7 of 7 mentions read as completions, no dispute
  language) and the routine `/governance` apply cycles once a collision window clears (the one
  governance-abort in the tail, 2026-07-20T09:57Z, self-resolved within the same session once two
  colliding sessions closed — see the Concurrency friction rate in `dual_insights_report.md` for
  the detailed count).

---

## Recommendations

Every candidate below was run through the four-gate check (liveness, correct target, not already
applied, not brake-refused) before being written. Re-checked `git log --since="1 hour ago"`
immediately before this section — only `igw-ledger: update` commits landed, nothing that changes
an autopsy routing.

1. **No substrate-build recommendation this cycle.** The two highest-failure-record SD entries
   (`scaffolded_sd054_onboarding` 28, `f_dominance_conversion_ceiling` 26) are both live,
   multi-hypothesis campaigns already tracked in `hypothesis_space_registry.v1.json` with alive
   hypotheses and active fanout — not missing-substrate gaps a single build would close. Naming
   either here would duplicate the campaign's own internal routing rather than add information.
2. **8 pending_review items await adjudication** (2 PASS to close out, 6 FAIL): V3-EXQ-841
   (MECH-163/Q-085), V3-EXQ-845 (MECH-180), V3-EXQ-836a/836d (MECH-476), V3-EXQ-850 (MECH-204/SD-076,
   flagged as a diagnostic self-route needing adjudication), V3-EXQ-844 (MECH-321), plus
   V3-EXQ-846 (ARC-005) and V3-EXQ-849 (Q-081) awaiting PASS close-out. A TASK_CLAIMS entry
   (`elastic-merkle-e0cca8`) already owns the FAIL side as of 2026-08-01T10:11Z — this is in
   progress, not unowned, so no separate chip is needed.
3. **Literature backlog is not actionable** — all 3 open items are `priority: low`; no
   recommendation to accelerate lit-pull this cycle.
