# Failure Autopsy -- V3-EXQ-654b (arc_062 GAP-B rule-apprehension falsifier)

**Date:** 2026-06-11T00:14:09Z
**Scope:** single (capstone of the 654 -> 654a -> 654b lineage)
**Status:** confirmed (user-adjudicated 2026-06-11)
**Claims under test (tagged):** MECH-309, ARC-062 (substrate actually exercised: **ARC-063** `CandidateRuleField`)
**Outcome:** FAIL / non_contributory; self-route `substrate_not_ready_requeue`
**Routing (confirmed):** implement-substrate -- **amend ARC-063 `CandidateRuleField`** gate/credit/retire dynamics. NO claim demotion.
**Substrate owner (confirmed):** the **ARC-062** `substrate_queue.json` entry (hosts the ARC-063 CRF amend lineage), NOT `modulatory-bias-selection-authority`.
**Predecessors:** `failure_autopsy_V3-EXQ-654_2026-06-09`, `failure_autopsy_569f-661-654a_2026-06-10`

---

## Summary

V3-EXQ-654b is the third iteration of the GAP-B behavioural falsifier and the
third consecutive failure on the **same** readiness precondition: C1c
`arm_on_rule_field_differentiated_and_matured`. Across 654 (per-episode wipe),
654a (`crf_persist=True`), and 654b (`crf_persist` + a 2.4x longer 240-ep
maturation window), `crf_frac_active` is **pinned at ~0.12-0.14** and
`crf_max_pairwise_rule_dist` is **exactly 0.0** every cell. The maturation-budget
reading (reading B of the 569f/661/654a cluster) is therefore **exhausted, not
unexplored**: more budget and cross-episode persistence move the maturation
metric by nothing.

The diagnosis relocates the blocker from "the CRF needs more maturation budget"
(the self-route's implied action) to **the ARC-063 `CandidateRuleField`
GATE/CREDIT/RETIRE dynamics never let a differentiated, persistently-active pool
of >=2 rules form**. This is upstream of, and distinct from, the
`modulatory-bias-selection-authority` route-range coupling that V3-EXQ-662
validated on 2026-06-10T13:27 -- 654b never produced a differentiated
`rule_state` for that routing to carry, so the 662 fix is irrelevant to this leg.

---

## Facts (no interpretation)

Manifest: `v3_exq_654b_arc062_gapb_rule_apprehension_behavioural_falsifier_20260610T200549Z_v3.json`
(machine ree-cloud-4; seeds 42/43/44; 2 arms; p0=150 / p1=90 / p2=60 ep; 200 steps/ep).

**C1 non-vacuity preconditions:**

| precondition | measured | threshold | met |
|---|---|---|---|
| committed-class axis exercisable (both arms) | 1.0 | 0.30 | yes |
| GAP-A consumed-summary divergence (both arms) | 0.0091 spread | 0.05 | yes (manifest records met:true; note seed-43 ARM_ON gapa_divergence=false) |
| consumed-summary bounded (no 643a explosion) | 0.184 | 1e6 | yes |
| **C1c ARM_ON rule field differentiated AND matured** | **crf_frac_active 0.130** | **0.30** | **NO** |
| propagation non-vacuity (ARM_ON bias != ARM_OFF) | 0.0122 | 0.001 | yes |

**Lineage (the load-bearing signal):**

| run | regime | crf_frac_active (best seed) | crf_max_pairwise_rule_dist | crf_n_minted_total | crf_differentiated |
|---|---|---|---|---|---|
| V3-EXQ-654 | per-episode wipe | ~0.12 | 0.0 | 131-408 | false |
| V3-EXQ-654a | `crf_persist=True` | 0.137 | 0.0 | 268/549/220 | false |
| **V3-EXQ-654b** | `crf_persist` + 240 ep | **0.130** | **0.0** | 452/1014/419 | false |

Per-seed 654b ARM_ON: crf_frac_active 42=0.112 / 43=0.127 / 44=0.130;
crf_max_pairwise_rule_dist 0.0 all three; crf_mean_n_active 0.11-0.13.

**C2 (moot -- C1 gates it):** committed-class entropy paired lift ARM_ON-vs-ARM_OFF
= 42:-0.025 / 43:-0.047 / 44:-0.124 (all negative; 0/3 seeds positive).
ARM_OFF mean committed-class entropy 1.000 vs ARM_ON 0.935.

**Failed criterion class:** readiness / negative-control (C1c maturation precondition),
which self-routes requeue and correctly does NOT score against MECH-309/ARC-062.

---

## Claim-layer map

- **MECH-309** (mechanism_hypothesis, candidate, `epistemic_category: substrate_ceiling`,
  v3_pending) and **ARC-062** (architectural_commitment, candidate, `substrate_ceiling`,
  v3_pending) both carry promote/demote suppression by construction. non_contributory
  is safe -- no false weight accrues.
- **ARC-063** (the strong-reading distributed CandidateRule field) is the implementation
  actually exercised by `use_candidate_rule_field=True` in ARM_ON. 654b's tags
  (MECH-309/ARC-062) do not include ARC-063, but because the result is non_contributory
  no mis-weighting occurs. The substrate to AMEND is ARC-063's `CandidateRuleField`.
- Did the experiment test the claims under conditions where they could express themselves?
  **No** -- the rule-creator never produced a differentiated rule_state, so the GAP-B
  falsifier (does a differentiated, matured rule_state add committed-class diversity?)
  could not run. C1 correctly blocked scoring.

---

## Biological-reference triage

Closest mechanism: BG/PFC **task-set rule learning** -- Collins & Frank 2014
(rule structure accumulates across experiences, not reset per trial), Frank 2006 /
Cavanagh 2011 (conflict-graded "hold your horses" availability threshold),
Mansouri (rule-selective persistence). Biology is an existence proof that a
non-Bayesian rule-creator maintains a **differentiated, persistent** set of
task-set rules. The CandidateRuleField is a faithful translation of this class,
not a formal-definition import.

The failure matches what happens biologically if the **maintenance/credit dynamics**
of such a field were mis-set so rules cannot co-persist: a single transient rule,
rapidly retired, never a differentiated set. That is a discovered
parameter/mechanism prerequisite of the reference mechanism, **not** a falsification
of MECH-309/ARC-062. Demotion is not reached: the claims were never tested under
conditions where they could express themselves.

---

## Mechanism (from `ree-v3/ree_core/policy/candidate_rule_field.py`)

`crf_max_pairwise_rule_dist = 0.0` (the diagnostic iterates rules **present** in
`self._rules`; distinct minted rules occupy distinct pinned subspace directions)
means **<=1 rule is present in the pool at any measured tick**, despite 452-1014
total mints. The pool churns: mint -> brief life -> retire -> re-mint, never
accumulating >=2.

Candidate drivers for the amend to recalibrate:

1. **Retire-churn (primary).** `availability` decays 0.5%/tick
   (`availability_decay=0.005`) and `credit()` drives availability toward 0 on
   negative outcomes (frequent in a hazard env); a rule drops below
   `_retire_floor = 0.5 * tolerance_floor = 0.15` before a second differentiated
   rule co-accumulates. `crf_persist` preserves the pool across episode boundaries
   but does nothing about within-run churn -- which is why 240 ep changed nothing.
2. **Mint-block under collapsed context (secondary).** `_maybe_mint` blocks a new
   rule whenever any existing rule's `context_tag` is within
   `context_match_threshold=0.5` cosine. Under the low cross-candidate z_world
   spread the 649/GAP-A finding documents, one rule "covers" the context space and
   suppresses differentiated mints. The CRF reads the agent's raw z_world context,
   so the SD-056 / e2_world_forward GAP-A fix that re-diversified the *other* bias
   channels does **not** reach it.
3. **Conflict-gate deadlock (latent).** `tolerance_floor=0.3` +
   `tolerance_conflict_gain=1.0` gives `theta = 0.3 + 1.0*n_competing`; with even
   one competing matched rule `theta = 1.3 > 1.0` max availability, so **>=2
   context-matched rules can never both be active**. This does not bite while the
   pool is empty (faults 1-2), but it would block differentiation the moment the
   pool filled -- so the amend must address it together with the churn.

The flat `crf_frac_active ~0.13` is the lone transient rule firing on ~13% of
ticks (not context-matched, or below the 0.3 availability gate, the rest of the time).

---

## Adjudication of the self-route

The `substrate_not_ready_requeue` label is **not vacuous**: the C1c precondition
was genuinely unmet (the CRF really did not mature). But the *action the label
implies* -- requeue with a longer maturation budget -- is **wrong**, the canonical
V3-EXQ-642 trap. The unmet precondition's cause is **mis-tuned CRF gate/credit/retire
dynamics**, not an untrained or under-budgeted substrate. Three escalating budgets
(per-episode wipe -> crf_persist -> crf_persist+240ep) leave frac_active flat and
the pool at <=1 present rule. The correct route is a CRF-substrate amend with a
CRF-readiness gate, not a 654c budget requeue.

---

## Lineage / mini-cluster read

The 569f/661/654a cluster (2026-06-10) grouped 654a with two routing-layer FAILs
under reading A ("upstream range present, committed action invariant -> route range
into the bias the authority rescales"; fixed by the 662-validated route-range amend).
654b **separates the 654 leg from that cluster**: 569f and 661 carried genuine
upstream cross-candidate range that the coupling flattened; the 654 leg never
produced upstream range at all (the CRF rule_state is undifferentiated, pool empty).
So the 654 leg's blocker is **CRF-internal differentiation/maturation**, upstream of
the routing the cluster fixed. The 654a/654b failure records currently filed on
`modulatory-bias-selection-authority` are mis-homed for this leg; they belong on the
ARC-062 entry (governance note below).

---

## Learning extracted

1. The CRF maturation problem is **not budget-bound**: frac_active is invariant
   (0.137 -> 0.130) across an already-2.4x longer window plus cross-episode
   persistence. The retire-churn empties the pool faster than differentiated rules
   accumulate, independent of how many ticks are available.
2. `crf_max_pairwise_rule_dist = 0.0` is the headline: the field never holds >=2
   rules present, so "differentiation" (distinct pinned directions) has no
   opportunity to express -- the symbol of the mechanism without its functional
   role.
3. The 662 route-range fix is necessary for the *other* bias channels but cannot
   help the 654 leg until the CRF first produces a differentiated rule_state to
   route. The two substrate threads are now cleanly separated.
4. The CRF reads raw z_world context for mint/match; under monostrategy-collapsed
   z_world spread, one rule covers everything -- the same GAP-A collapse, reaching
   a channel the GAP-A fix did not.

---

## Repair pathway (user-confirmed)

**Route: implement-substrate -- amend ARC-063 `CandidateRuleField`** (NOT a 654c
budget requeue; NO claim demotion). The amend should:

- Recalibrate the GATE/CREDIT/RETIRE parameters so a differentiated,
  persistently-active pool of >=2 rules can form and persist under the matched
  649/SD-056/SP-CEM/MECH-341 stack: at minimum reconsider `availability_decay`,
  `_retire_floor`, the negative-outcome credit rate, `context_match_threshold`, and
  the `tolerance_conflict_gain`/`tolerance_floor` pair (so `theta` is reachable for
  >=2 matched rules).
- Consider routing per-candidate / e2_world_forward context into the CRF's
  mint/match keys (mirroring the ARC-065 GAP-A fix) so the mint-block does not
  collapse under low raw-z_world spread.
- Add a **CRF-readiness gate** asserting `crf_max_pairwise_rule_dist > floor` AND
  `crf_frac_active >= 0.30` (V3-EXQ-639-style substrate-readiness) BEFORE any GAP-B
  behavioural falsifier (654c successor) is scored.

**Substrate owner:** the **ARC-062** `substrate_queue.json` entry (hosts the ARC-063
CRF amend lineage). Governance should append the 654b failure record there and may
re-home the misfiled 654a record from `modulatory-bias-selection-authority`.

**pending_retest_after_substrate: true.** The remaining "supports" for
MECH-309/ARC-062 are not affected (the claims were never tested; non_contributory).

### Draft `evidence_quality_note` (governance writes; this skill does not)

> V3-EXQ-654b (arc_062 GAP-B behavioural falsifier, MECH-309/ARC-062;
> implementation under test = ARC-063 CandidateRuleField) FAILed C1c
> `arm_on_rule_field_differentiated_and_matured` (crf_frac_active 0.130 < 0.30) for
> the third consecutive iteration. crf_frac_active is flat at ~0.13 across 654
> (per-episode wipe) / 654a (crf_persist) / 654b (crf_persist + 240 ep) and
> crf_max_pairwise_rule_dist is 0.0 every cell -- the CandidateRuleField never holds
> >=2 rules present, so the maturation-budget reading is exhausted. Diagnosis
> (failure_autopsy_V3-EXQ-654b_2026-06-11): CRF retire-churn + context-match
> mint-block under collapsed z_world spread + an unreachable conflict-gate theta
> prevent a differentiated persistent pool. non_contributory (C1 gated scoring; no
> claim weight). Route: amend ARC-063 CandidateRuleField gate/credit/retire dynamics
> + a CRF-readiness gate (crf_max_pairwise_rule_dist>floor AND frac_active>=0.30)
> before re-scoring GAP-B (654c successor). pending_retest_after_substrate. NO
> demotion -- the claims were never tested.

---

## Hand-off

- `/governance` consumes the companion JSON: append the 654b failure record to the
  ARC-062 substrate_queue entry, set the ARC-062 amend target = ARC-063
  CandidateRuleField, optionally re-home the 654a record, mark
  pending_retest_after_substrate. It is the only skill that writes
  claims.yaml / manifests / substrate_queue.
- `/implement-substrate` picks up the ARC-063 CandidateRuleField gate/credit/retire
  amend + CRF-readiness gate; `/queue-experiment` queues the 654c GAP-B successor
  only after a V3-EXQ-639-style CRF-readiness run clears.
