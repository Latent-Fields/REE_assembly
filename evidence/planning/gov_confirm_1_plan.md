---
closure_plan:
  id: gov_confirm_1
  # generation: process -- infrastructure/governance tooling lane, not V3
  # substrate science. Owns no scientific claims (it only surfaces OTHER claims'
  # confirmers), so it is segmented out of the V3 closure % and rendered on the
  # shared `process` tab alongside arm_reuse_fingerprint + convergence intake.
  generation: process
  title: "GOV-CONFIRM-1 Evidence-Confirmer Detector (generative complement to the IGW workset)"
  registered: 2026-07-14
  last_updated: 2026-07-14
  scope_claims: [GOV-CONFIRM-1]
  sibling_plans: [ree_ai_design_critique_plan.md]
  nodes:
    - id: "gov_confirm_1:P0"
      title: "Plan-of-record + register GOV-CONFIRM-1 governance_rule claim"
      phase: 0
      status: done
      severity: high
      owner_exq: null
      last_updated: 2026-07-14
      completion_note: "This doc + GOV-CONFIRM-1 registered in claims.yaml (candidate/governance_rule, warn-only, PROMOTES/DEMOTES NOTHING). Motivating incident: 2026-07-14 a 634-candidate subagent scan was required to surface 5 buildable, wall-independent representation/functional-signature confirmers (MECH-304/288/303/284/287) that the existing consume-only IGW workset never surfaced because no `proposed` entry had been hand-authored for them. The detector closes that discovery gap."
    - id: "gov_confirm_1:P1"
      title: "Shadow detector -- derive-only `evidence_confirmer` lane in generate_inter_governance_workset.py; output-only, NOT wired to autospawn"
      phase: 1
      status: done
      severity: high
      owner_exq: null
      last_updated: 2026-07-14
      completion_note: "DONE. Added `_evidence_confirmer_candidates` + `_claim_lit_conf` + `_claims_implemented_in_substrate` helpers and the `evidence_confirmer` lane to generate_inter_governance_workset.py. REUSES the existing predicates (exp_evidence / _TESTABLE_CLAIM_STATUSES / _EPI_SUPPRESS_PROPOSAL / _is_deferred_beyond_v3 / _retest_blockers) + a lit_conf floor (0.6) + the built-substrate gate (claim-id tagged in ree-v3/ree_core -- the honest proxy, since neither `location` nor `assembly_state` distinguishes built from unbuilt). v3_pending RELAXED under the built-substrate guard (user decision 2026-07-14): v3_pending means 'held until V3 experiments provide evidence' and a confirmer on built substrate IS that evidence. Surfaces 32 confirmers incl. all 5 motivating claims (MECH-304/288/303/284/287; ranks 3-22). P1-SAFE / output-only: gated by CONFIRMER_AUTOSPAWN_ENABLED=False -> status 'surfaced' (not 'ready'), which the external auto-spawn routine and check_workset_drift both skip. VERIFIED: additive (non-confirmer items byte-identical with/without the lane), py_compile OK, test_igw_spawned_task_autorelease 3/3, check_workset_drift ready_items_flagged=0."
    - id: "gov_confirm_1:P2"
      title: "Wire the confirmer lane to the hourly IGW autospawn at strictly LOW priority"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      last_updated: 2026-07-14
      next: "routing=implement-substrate (REE_assembly tooling)"
      resume_condition: "ONLY after P1 shadow output is verified clean (user-approved). Wire the `evidence_confirmer` lane into the autospawn eligibility gate at a priority strictly BELOW the wall-campaign lanes, so confirmers run as background fill and never compete with the live front. User directive 2026-07-14: eventual scope = low-priority autospawn (not surface-only)."
---

# GOV-CONFIRM-1 -- Evidence-Confirmer Detector (Plan of Record)

**Created:** 2026-07-14 &nbsp;|&nbsp; **Status:** P0 + **P1 done** (detector + shadow lane landed, output-only); P2 (low-priority autospawn wiring) pending.

## The gap (why this exists)

The inter-governance workset (`scripts/generate_inter_governance_workset.py`) + the hourly
IGW auto-spawn routine can *complete* an experiment confirmer, **but only if a
`status: proposed` entry was hand-authored for it first.** `_proposed_experiments()`
(line 684) is **consume-only**: it re-surfaces pre-authored proposals and applies a stack
of *exclusion* filters (drop `v3_pending`, drop substrate-blocked, drop already-evidenced,
drop V4+). There is **no generative path** that scans `claims.yaml` and *authors* a
confirmer for a thin-evidence candidate whose substrate is already built.

**Consequence (the motivating incident, 2026-07-14):** finding buildable evidence
confirmers required a bespoke 634-candidate subagent scan. It surfaced five claims that are
`candidate`, high `lit_conf`, **zero** experimental evidence, substrate **built**, and NOT
wall-bound -- and every one of them already *passes* the workset's exclusion filters. They
were invisible only because no human remembered to author a proposal. These are exactly the
**"non-urgent but important evidence confirmers"** that should be discovered and completed
by the machinery, not by hand.

## The rule (GOV-CONFIRM-1)

A **generative** complement to the workset: scan `candidate`/`provisional` claims and emit a
low-priority `evidence_confirmer` lane for each claim that is
**confirmable-but-uncofirmed** -- built substrate, thin/zero experimental evidence, decent
literature support, not wall-bound, not already covered -- so the IGW autospawn completes
them as background fill. Warn-only routing standard; **PROMOTES/DEMOTES NOTHING.** The one
piece that needs judgment -- scoping a confirming **dependent variable that is buildable
now** (a representation-level / functional-signature DV, self-routing
`substrate_not_ready_requeue` if only a wall-bound behavioural DV exists) -- stays in the
per-item `/queue-experiment` pass, where the code review + smoke test already live. The
detector owns *discovery*, not design.

> **Durability note:** the rule does NOT hard-encode "the competence wall." The wall is the
> current *reason* the buildable confirmers are the representation-level ones; the durable
> core is "surface confirmable-but-unconfirmed candidates as low-priority background
> experiments." Wall-bound behavioural confirmers are already filtered by the reused
> substrate-block / epistemic-category predicates, and any that slip through self-route
> vacuous at `/queue-experiment`.

## Detector design (P1) -- reuses predicates that already exist

The generator already computes every predicate needed; the lane just applies them
*generatively* over the full claim set instead of only over pre-authored proposals:

| Selection criterion | Existing helper to reuse |
|---|---|
| `status in {candidate, provisional}` + not `v3_pending` + testable `epistemic_category` | `_claim_v3_testable()` |
| not already evidenced (`exp_conf ~ 0`) | `_claims_with_experimental_evidence()` |
| not substrate-blocked (the wall / substrate_queue gate) | `_retest_blockers()` |
| not V4/V5-only | `_is_deferred_beyond_v3()` |
| worth confirming (`lit_conf >= 0.6`) | `claim_evidence.v1.json` |
| substrate actually built (noise gate) | claim `location` field resolves to an existing `ree-v3/ree_core/*` file |

The `location`-exists + `lit_conf` gates are the **noise filter** that takes the raw
candidate set (~153 in the 2026-07-14 scan) down to a short high-signal list (the ~5 known
confirmers + peers). Output is a distinct `evidence_confirmer` lane, each item naming the
claim id, its `location`, `lit_conf`, and a note instructing the `/queue-experiment` pass to
scope a wall-independent representation/functional-signature DV.

**P1 acceptance:** one shadow run surfaces a short high-signal set (includes
MECH-304/288/303/284/287) and is **bit-identical** to the prior workset for every
non-confirmer item (additive lane only).

## Autospawn wiring (P2) -- low priority, background fill

After the P1 shadow output is verified clean, wire the `evidence_confirmer` lane into the
hourly autospawn eligibility at a priority **strictly below** the wall-campaign lanes, so
confirmers run only as background fill and never compete with the live front. (User
directive 2026-07-14: eventual scope = low-priority autospawn.)

## Cross-references

- Consume-only path this complements: `scripts/generate_inter_governance_workset.py`
  `_proposed_experiments()` + the IGW auto-spawn routine.
- Sibling governance rules (same warn-only / promotes-nothing shape): GOV-CEIL-1 (ceiling
  exhaustion, detection), GOV-DIAG-1 (diagnostic recurrence, detection), GOV-FANOUT-1
  (bottleneck fan-out, response), GOV-REUSE-1 (reanalysis-first, consumer). GOV-CONFIRM-1 is
  the **generative-discovery** member of that family.
- First-application seed set (2026-07-14 subagent scan): MECH-304, MECH-288, MECH-287,
  MECH-303, MECH-284 (chips spawned this session); borderline MECH-271 (substrate
  unconfirmed), MECH-292 (scope-risky).
