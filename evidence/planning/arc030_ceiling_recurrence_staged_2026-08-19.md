# ARC-030 "ceiling-may-have-lifted" -- third recurrence, re-confirmed NOT queueable

**Status: AWAITING USER REVIEW.**

Session: `metaworker-chip-20260816-arc030-ceiling-lifted-retest` (headless, DLAPTOP)
Chip: `chip-20260816-arc030-ceiling-lifted-retest`
Date: 2026-08-19T07:24Z

## Verdict

**DID NOT QUEUE the ARC-030 discriminative retest.** The ceiling has lifted only
PARTIALLY: MECH-307 (the substrate the audit keys on) is implemented and genuinely
reachable, but ARC-030's own mandatory G0 non-degeneracy precondition still FAILS,
and its blocker is no longer MECH-307.

This is a **re-confirmation, not a fresh investigation**. `chip-20260812-arc030-ceiling-lifted-retest`
reached the identical conclusion on 2026-08-14 (`chip-20260813-queueexp-arc030-retest`
was withdrawn as a duplicate of it). This session re-verified every load-bearing fact
against current state and found **nothing changed**.

## Evidence re-verified 2026-08-19

| Check | Result |
|---|---|
| `experiment_queue.json` ARC-030 entries | none (queue holds 0 items) |
| `task_claim.py check` on the queue | no overlapping active claim |
| ARC-030 `pending_retest_after_substrate` | still `true`; `status: candidate` |
| Newest ARC-030-tagged manifest | `v3_exq_899_...20260808T214833Z_v3` -- no new evidence since 2026-08-08 |
| `check_substrate_ceiling_audit.py` | still lists `[lifted] ARC-030 -- unblocking substrate MECH-307 implemented` |
| SD-010 (ARC-030 `depends_on`) | `status: implemented` -- not the blocker |
| MECH-457 (the real blocker thread) | still `candidate` / `v3_pending`, unmoved |

### Why the retest is still readiness-blocked

ARC-030's `what_would_answer` makes the COMBINED-vs-NOGO_ONLY discriminative pair
conditional on a **MANDATORY non-degeneracy precondition**: FULL-arm
`resource_visit_rate` must beat RANDOM by >= 0.05 on >= 2/3 seeds. That gate is what
V3-EXQ-899 measured, twice, and it failed both times:

- `v3_exq_899_..._20260808T153148Z_v3` -- FAIL, `evidence_direction: non_contributory`
- `v3_exq_899_..._20260808T214833Z_v3` -- FAIL, `evidence_direction: non_contributory`
  - `g0_on_pass = 0.0`, `g0_off_pass = 0.0`
  - `mech307_perturbs_baseline = 0.0` -- ON vs OFF are indistinguishable
    (`resource_visit_rate` 0.00401 ON vs 0.00390 OFF), while RANDOM scores 0.01164.
    The FULL arm forages **below** a random policy.
  - Both readiness *preconditions* were MET (`reached_p2_frac_seeds = 1.0`,
    `p2_window_live_frac_seeds = 0.667`), so this is a real failure of the gate,
    not a dead measurement window.

The run's own interpretation: *"MECH-307 reachability alone does not restore the G0
gate ... do NOT force through to the discriminative retest."*

Queueing the retest now would return `substrate_not_ready_requeue` and burn a queue
letter for no information.

### The blocker has been re-pointed, but not recorded on the claim

899's self-route (to substrate stub `scaffolded-curriculum-hazard-rebalance`) was
**superseded**. That stub's own diagnosis chip
(`chip-20260808-igw200-scaffolded-curriculum-hazard-rebalance`) found no substrate
change warranted -- z_goal survives every hazard stage and enters P2 at ~0.52; the C6
washout was a driver-side measurement artefact, fixed by V3-EXQ-866c. Its
`substrate_queue` entry now reads
`diagnosis_done_NO_SUBSTRATE_CHANGE_WARRANTED_2026-08-08`.

`failure_autopsy_V3-EXQ-866a-G0_2026-08-08` reclassified the true root as the
**MECH-457 competence-floor phenomenon** (approach-before-avoidance ordering,
V3-EXQ-728/769), reclassified `competence_implementation_gap` -- *not* a
substrate_ceiling -- with routing "no new build; cross-ref MECH-457 H1/H2/H3
portfolio". The matching `substrate_queue` entry ("Competent unsupervised explorer
for the action-learning competence floor (MECH-457)") is
`blocked_pending_discrimination`, `ready: false`.

So ARC-030 is blocked on MECH-457, while `claims.yaml` still records its gate as
MECH-307.

## Recommended governance action (NOT applied by this session)

The chip forbade this session from touching ARC-030's status or
`pending_retest_after_substrate`, and the disposition below is likewise governance's
call. It is staged here rather than applied.

**The audit will re-flag ARC-030 every cycle until this is recorded.** This chip is
the third instance of the same mechanically-generated finding (2026-08-12,
2026-08-13, 2026-08-16), each costing a full worker investigation to reach the same
answer. `chip-20260812`'s resolution note predicted exactly this recurrence.

`check_substrate_ceiling_audit.py` already has the purpose-built mechanism:
`ceiling_decision: deferred` plus a `ceiling_routing_note` moves a claim into the
`parked` bucket (23 claims already sit there) so it stops surfacing as ACTIONABLE
without losing the owed retest.

Suggested, for governance to accept/revise/reject:

1. Set `ceiling_decision: deferred` on ARC-030 with a `ceiling_routing_note` naming
   MECH-457 (competence floor) as the operative blocker, not MECH-307.
2. Leave `pending_retest_after_substrate: true` -- the retest is genuinely still
   owed; only its blocker is re-pointed.
3. Append the V3-EXQ-899 FAIL result to ARC-030's `evidence_quality_note`, which
   currently stops at the 2026-08-08 "readiness chipped" line and does not record
   that the readiness gate then ran twice and failed.
4. Re-queue the ARC-030 discriminative retest only after the MECH-457 competence-floor
   thread delivers a FULL arm that clears RANDOM on the G0 statistic.

Note that (1) is a claims-field change only; it does not weaken or resolve ARC-030,
and the claim remains `candidate` with its retest owed.
