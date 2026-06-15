# Failure Autopsy -- V3-EXQ-654c (arc_062 GAP-B rule-apprehension falsifier)

**generated_utc:** 2026-06-15T16:08:09Z
**scope:** single (4th in the 654 -> 654a -> 654b -> 654c lineage; substrate-maturation recurrence, NOT claim-granularity debt -- user-adjudicated 2026-06-15)
**status:** confirmed (interactive gate cleared 2026-06-15)
**run_id:** v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3
**queue_id:** V3-EXQ-654c (supersedes V3-EXQ-654b)
**claim_ids (tagged):** MECH-309, ARC-062 (substrate actually exercised = **ARC-063** `CandidateRuleField`)
**outcome:** FAIL / non_contributory; self-route `substrate_not_ready_requeue`
**machine:** ree-cloud-1
**routing (confirmed):** implement-substrate -- **amend `crf-availability-maintenance`** (BOTH faults) + flip ready True->False + frac_ACTIVE readiness gate; 654d re-queue **gated on GAP-A context de-collapse**. NO claim demotion.
**predecessors:** `failure_autopsy_V3-EXQ-654_2026-06-09`, `failure_autopsy_569f-661-654a_2026-06-10`, `failure_autopsy_V3-EXQ-654b_2026-06-11`

---

## Summary

654c is the 4th consecutive failure on the **same** readiness precondition C1c
(`arm_on_rule_field_differentiated_and_matured`), but with a **new, inverted
signature** that is the load-bearing finding. The 666c maintenance amend (which
654b recommended) **succeeded at fixing the retire-churn**: `crf_max_pairwise_rule_dist`
went 0.0 -> **1.711** and minting collapsed from hundreds to a stable **12-16**, so
the CandidateRuleField now holds >=2 differentiated, persistent rules. But
`crf_frac_active` collapsed from ~0.13 (654/654a/654b) to **exactly 0.0** -- the
matured pool **never activates**. The blocker marched one stage downstream: from
"the pool never matures" (654b) to "the matured pool never fires through the gate"
(654c).

Root cause is **two coupled faults**, both code-grounded:

1. **GAP-A monostrategy collapse reached the CRF context channel.**
   `crf_context_from_e2_world_forward=True` keys rule mint/match off
   `e2_world_forward`, but that summary is itself collapsed
   (`consumed_summary_pairwise_dist = 0.0089`, below the 0.05 GAP-A floor). Under a
   collapsed context the differentiated rules' `context_tag`s all co-match the same
   context (cosine >> the 0.5 `context_match_threshold`), so `n_matched` inflates.
2. **Maintenance floor sits below the crowded-match theta.** `gate_and_select`
   marks a rule active iff `availability >= theta = 0.15 + 0.25*(n_matched-1)`.
   Maintenance holds availability at `maintenance_floor = 0.45`, deliberately tuned
   (code comment, `candidate_rule_field.py:181-183`) to clear the **2-way** match
   (theta=0.40). The collapsed context forces **>=3** rules to co-match -> theta >=
   0.65 > 0.45 -> **every matched rule is gated out -> frac_active = 0.0.**

The 666c PASS that marked this substrate `ready=True` measured the **wrong
statistic**: its load-bearing criterion is `ARM_2_MAINTENANCE_clears_frac_MAINTAINED_gate`
-- availability **hold**, not gate **firing**. 654c proves **maintained != active**:
the conflict gate sits between availability and activation, and the readiness probe
never exercised it under collapsed context. This is the V3-EXQ-642-class trap (a
PASS validated a different precondition than the falsifier requires). 654b's
recommendation #3 -- a readiness gate on `crf_frac_active >= 0.30` -- was **not**
implemented (666c gated `frac_maintained` instead), so that readiness debt is unpaid.

**Strategic link:** the C1c collapse traces to the **same** GAP-A /
behavioral-diversity-isolation monostrategy collapse that blocks the 569g/682
committed-action conversion ceiling. A CRF-only amend is therefore **necessary but
not sufficient**: 654d can still fail C1c until GAP-A context de-collapse resolves.
This is why the confirmed route gates 654d behind GAP-A.

---

## Facts (no interpretation)

Manifest: `v3_exq_654c_arc062_gapb_rule_apprehension_behavioural_falsifier_20260615T123848Z_v3.json`
(machine ree-cloud-1; seeds 42/43/44; 2 arms; p0=200 / p1=90 / p2=60 ep; 200 steps/ep;
`crf_persist=True`, `crf_mature_pool_dynamics=True`, `crf_context_from_e2_world_forward=True`,
`crf_availability_maintenance=True`, `maintenance_floor=0.45`, `maintenance_decay=0.0`;
`lateral_pfc_train_rule_bias_head=True` trained in a frozen-encoder P1 REINFORCE window).

**C1 non-vacuity preconditions:**

| precondition | measured | threshold | met |
|---|---|---|---|
| committed-class axis exercisable (both arms) | 1.0 | 0.30 | yes |
| GAP-A consumed-summary divergence (both arms) | 0.008926 spread | 0.05 | **manifest records met:true** (but ARM_ON seed-43 gapa_divergence=false; seed-42/44 true) |
| consumed-summary bounded (no 643a explosion) | 0.1469 | 1e6 | yes |
| **C1c ARM_ON rule field differentiated AND matured** | **crf_frac_active 0.0** | **0.30** | **NO** |
| propagation non-vacuity (ARM_ON bias != ARM_OFF) | 0.0384 | 0.001 | yes (2/3 seeds; seed-42 prop diff = 0.0) |

**Lineage (the load-bearing signal):**

| run | regime | crf_frac_active | crf_max_pairwise_rule_dist | crf_n_minted_total | crf_differentiated |
|---|---|---|---|---|---|
| V3-EXQ-654 | per-episode wipe | ~0.12 | 0.0 | 131-408 | false |
| V3-EXQ-654a | crf_persist | 0.137 | 0.0 | 268/549/220 | false |
| V3-EXQ-654b | crf_persist + 240 ep | 0.130 | 0.0 | 452/1014/419 | false |
| **V3-EXQ-654c** | **+ 666c maint. levers** | **0.0** | **1.711** | **16/12/15** | **false** |

Per-seed 654c ARM_ON: `crf_mean_n_active` 0.0 all three; `crf_frac_active_ge_floor`
0.0 all three; `crf_max_pairwise_rule_dist` 1.711484 all three; `crf_n_minted_total`
16/12/15. Note seed-42 ARM_ON is byte-identical to ARM_OFF (committed_class_entropy
1.377154, bias 0.10000001, prop diff 0.0) -- the 654 seed-42 propagation washout
recurs on that one seed, though propagation is non-vacuous on seeds 43/44.

**C2 (moot -- C1 gates it):** committed-class entropy ARM_OFF 0.893128 vs ARM_ON
0.92258; paired lifts by seed {42: 0.0, 43: +0.0208, 44: +0.0676}; 1/3 seeds positive
(<2/3 needed). Not scored.

**Failed criterion class:** readiness (C1c maturation/activation precondition),
which self-routes requeue and correctly does NOT score against MECH-309/ARC-062.

**Discriminator NOT recorded:** the script reads `crf_n_active_last` from
`get_state()` but not `crf_n_matched_last` (which the CRF *does* track,
`candidate_rule_field.py:647`). So the manifest cannot directly prove "matched but
gated out" vs "never matched". The collapsed-context data (spread 0.0089, max_pairwise
1.71 -> rules present and differentiated) makes high-`n_matched` gate-lockout the
consistent reading; the amend must surface `crf_n_matched` to confirm.

---

## Claim-layer map

- **MECH-309** (mechanism_hypothesis, candidate, `substrate_ceiling`, v3_pending) and
  **ARC-062** (architectural_commitment, candidate, `substrate_ceiling`, v3_pending)
  both carry promote/demote suppression by construction. non_contributory is safe.
- **ARC-063** (the strong-reading distributed CandidateRule field) is the
  implementation actually exercised by `use_candidate_rule_field=True` in ARM_ON.
  654c's tags do not include ARC-063 but, because the result is non_contributory, no
  mis-weighting occurs.
- **Did the experiment test the claims under conditions where they could express
  themselves?** No. The rule-creator's differentiated rule_state never reached an
  active state, so the GAP-B falsifier (does a differentiated, matured rule_state add
  committed-class diversity?) could not run. C1 correctly blocked scoring. An
  implementation/dependency gap, not a falsification.

---

## Biological-reference triage

- **Closest mechanism:** non-Bayesian PFC/BG **task-set rule-creator** -- rule-coding
  units abstracting over instances (Bongard & Nieder 2010; Miller & Cohen 2001);
  conflict-graded "hold-your-horses" availability threshold (Frank 2006; Cavanagh
  2011); rule-selective persistence (Mansouri; Collins & Frank 2014 task-set
  accumulates across experiences, not reset per trial).
- **Faithful translation, not a formal-definition import.** No `/lit-pull`
  commission is the primary output; the biology is load-bearing in the *correct*
  direction (it predicted the per-episode wipe was wrong -- 654; and predicts a
  maintained set of differentiated rules should be *selectable*, not gated out).
- **Does the failure resemble a missing dependency of the reference mechanism?** Yes
  -- two of them: (i) a *context representation* with enough cross-state separation
  for distinct rules to key to distinct contexts (the GAP-A collapse denies this);
  (ii) an *availability/conflict gate* calibrated so a maintained, differentiated
  rule set can actually win selection rather than mutually crowding each other out.
  Both are discovered prerequisites of the reference mechanism, **not**
  falsifications of MECH-309/ARC-062.

---

## Mechanism (from `ree-v3/ree_core/policy/candidate_rule_field.py`)

- **`gate_and_select` (l.386-431):** `matched = [r : cosine(context, r.context_tag)
  >= context_match_threshold(0.5)]`; for each matched `r`, active iff
  `r.availability >= theta = theta_floor + theta_gain * (n_matched-1)`. Under
  `mature_pool_dynamics` (654c) `theta_floor=0.15`, `theta_gain=0.25`:
  theta(n_matched=1)=0.15, theta(2)=0.40, theta(3)=0.65, theta(4)=0.90.
- **Maintenance (l.202-204, l.358-369, l.486-501):** `availability_maintenance=True`
  holds a differentiated rule's availability at `maintenance_floor=0.45`
  (`maintenance_decay=0.0`). Code comment l.181-183: 0.45 was chosen to be "above the
  mature 2-way-match theta" (0.40) -- i.e. tuned to the **single-competitor** case.
- **The interaction that produces frac_active=0.0:** collapsed `e2_world_forward`
  context (spread 0.0089) -> rule `context_tag`s mutually similar AND all match the
  current context (cosine >> 0.5) -> `n_matched` >= 3 -> theta >= 0.65 > 0.45
  maintenance -> no rule clears the gate -> `crf_n_active_last = 0` every P2 tick.
  The maintenance floor lives in the dead zone between the 2-way (0.40) and 3-way
  (0.65) match theta, and context collapse forces the >=3-way regime.
- **Why the churn fix is real progress:** `mature_pool_dynamics` (slower
  `mature_availability_decay=0.001`, absolute `mature_retire_floor=0.05`, asymmetric
  negative credit) + `crf_persist` stop the retire-churn that emptied the pool in
  654/654a/654b. The pool now holds >=2 differentiated rules (`max_pairwise_dist`
  1.71). The 654b conflict-gate recalibration (mature theta pair) is also correct --
  it just isn't sufficient once context collapse forces the >=3-way match.

---

## Adjudication of the self-route

`substrate_not_ready_requeue` is **not vacuous** -- the C1c precondition was
genuinely unmet (the CRF really did not activate). But the **action the label
implies** -- a budget/maturation requeue -- is wrong (the canonical V3-EXQ-642 trap).
The cause is **two coupled substrate faults** (context collapse reaching the CRF +
maintenance-floor/conflict-gate calibration under crowded matches), plus a
**readiness-probe gap** (666c gated `frac_maintained`, not `frac_active`). The
correct route is a CRF-substrate amend addressing both faults and a frac_ACTIVE
readiness gate -- NOT a 654d budget requeue, and NOT a CRF-only amend that leaves the
GAP-A context collapse in place.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C2 never fairly tested; C1c gated it out (4th time) |
| Biological reference | clear; two missing-dependency signatures | (i) separable context representation; (ii) selectable maintained rule set |
| Developmental / dependency prerequisites | **missing** | GAP-A context de-collapse is an unresolved upstream dependency feeding the CRF context key |
| Implementation completeness | partial | maintenance fills + differentiates the pool (real progress) but the activation gate locks it out under collapsed context |
| Environment adequacy | adequate | SD-054 bipartite reef/forage falsifier env is intended |
| Measurement adequacy | **under-instrumented** | script records `crf_n_active` but not `crf_n_matched`; 666c readiness gated `frac_maintained` not `frac_active` |
| Integration adequacy | partially coupled | field -> lateral_pfc -> E3 wired; field now matures but its output is gated out; GAP-A collapse couples in via the context key |
| Scale / capacity | adequate | not a budget problem (the maturation metric moved; activation is a gate, not a budget, failure) |

**Recommended epistemic_category:** `substrate_ceiling` (precondition_unmet flavour --
activation-gate + context-collapse interaction, not a representational ceiling).
**Recommended evidence_direction:** `non_contributory` (unchanged).
**pending_retest_after_substrate:** true. **Do NOT weaken MECH-309 / ARC-062 / ARC-063.**

---

## Lineage / recurrence read (4th autopsy on this target)

Per the granularity-debt recurrence hook, this is the 4th separate autopsy circling
the same C1c precondition -- a recurrence signal that was put to the user at the
interactive gate. **User-adjudicated read: substrate-maturation recurrence, NOT
claim-granularity debt.** The recurrence lives in the ARC-063 implementation layer,
not in a coarse MECH-309/ARC-062 claim: (a) the claims are well-defined and have
**never been tested** (C1 gated every iteration), so they are not "coarse claims
circled by structurally-different falsifications"; (b) each fix provably advances a
real substrate metric and the blocker marches downstream by one well-localised stage
each time (cold-start washout -> retire-churn -> activation-gate-under-collapse). No
`/claim-synthesis` decomposition is warranted. The honest strategic caveat -- 4
iterations and the falsifier still has not run -- is addressed by **gating 654d
behind GAP-A** rather than iterating the CRF in isolation again.

---

## Learning extracted

1. **maintained != active.** Holding a differentiated rule's *availability* (666c
   frac_maintained) does not make it *fire*: the conflict gate sits between
   availability and activation, and under crowded (context-collapsed) matches the
   maintenance floor is below the gate theta. A readiness probe that gates
   `frac_maintained` over-states readiness for a falsifier that needs `frac_active`.
2. **The GAP-A monostrategy collapse reaches the CRF context channel.**
   `crf_context_from_e2_world_forward` was intended to escape the raw-z_world collapse
   654b flagged, but `e2_world_forward` is itself collapsed (spread 0.0089). The same
   collapse that gates the 569g/682 committed-action conversion also crowds the CRF
   matches -- one upstream cause, two downstream blockers.
3. **The 666c churn fix is genuine.** `max_pairwise_dist` 0.0 -> 1.71 and stable
   12-16 minting show the retire-churn / per-episode-wipe lineage is resolved. The
   remaining work is the activation gate + the context key, not pool maturation.
4. **Instrument the discriminator.** `crf_n_matched_last` is already tracked in the
   CRF but unread by the script; recording it (plus the theta-vs-availability margin
   on matched ticks) will distinguish "never matched" from "matched but gated out" in
   the next run.

---

## Repair pathway (user-confirmed at the interactive gate)

**Route: implement-substrate -- amend `crf-availability-maintenance` (BOTH faults).**
NO 654d budget requeue; NO claim demotion. The amend should:

1. **De-collapse the CRF context key (fault 1 / GAP-A in the rule channel):** sharpen
   or per-candidate-separate the `e2_world_forward` context feeding CRF mint/match so
   a small differentiated pool does not all co-match one collapsed context (mirror the
   ARC-065 / GAP-A diversity fix into the CRF mint/match keys). Acknowledge this is the
   **same** behavioral-diversity-isolation:GAP-A collapse (569g/682); the CRF amend may
   be necessary-but-not-sufficient until GAP-A resolves.
2. **Recalibrate maintenance vs conflict gate (fault 2):** make a maintained,
   differentiated rule clear the gate under realistic match-crowding -- e.g. couple the
   maintained availability to the *actual* per-tick `theta(n_matched)` (maintain at
   `max(maintenance_floor, theta(n_matched)+eps)`), and/or cap `n_competing` in theta,
   and/or sharpen `context_match_threshold` so fewer spurious co-matches inflate
   `n_matched`. Raising `maintenance_floor` alone is insufficient (it cannot track a
   growing `n_matched`).
3. **Upgrade the readiness gate (probe debt -- 654b rec #3, still unpaid):** assert
   `crf_frac_active >= 0.30` (gate-firing rate) AND record the `crf_n_matched`
   distribution -- NOT `frac_maintained` -- before any GAP-B falsifier is scored. Flip
   the `crf-availability-maintenance` substrate entry from `validated / ready=True`
   back to **not-ready** until `frac_active` is demonstrated.
4. **Gate the 654d re-queue on GAP-A context de-collapse**, not on a CRF-only amend.

**Substrate owner:** the `crf-availability-maintenance` `substrate_queue.json` entry
(amend target; ARC-063 `CandidateRuleField` is the module), under the ARC-062 umbrella.
`unblocks_claims` already lists MECH-309 / ARC-062 / ARC-063.

### Draft `evidence_quality_note` (governance writes; this skill does not)

> V3-EXQ-654c (arc_062 GAP-B behavioural falsifier, MECH-309/ARC-062; implementation
> under test = ARC-063 CandidateRuleField) FAILed C1c
> `arm_on_rule_field_differentiated_and_matured` (crf_frac_active = 0.0 < 0.30) for the
> 4th consecutive iteration -- but with an INVERTED signature: the 666c maintenance
> amend fixed the retire-churn (crf_max_pairwise_rule_dist 0.0 -> 1.711, minting
> stabilised at 12-16), so the pool now holds >=2 differentiated rules, yet activation
> collapsed to exactly 0.0. Code-grounded cause
> (failure_autopsy_V3-EXQ-654c_2026-06-15), two coupled faults: (1) the GAP-A
> monostrategy collapse reached the CRF context key (crf_context_from_e2_world_forward;
> consumed_summary spread 0.0089 < 0.05 floor) -> differentiated rules all co-match one
> collapsed context -> n_matched inflates; (2) gate_and_select theta = 0.15 +
> 0.25*(n_matched-1) climbs above the maintenance_floor 0.45 once >=3 rules co-match ->
> every matched rule gated out. The 666c PASS that marked the substrate ready=True
> measured frac_MAINTAINED (availability hold), not frac_ACTIVE (gate firing) --
> maintained != active. non_contributory (C1 gated scoring; no claim weight). Route:
> implement-substrate amend crf-availability-maintenance for BOTH faults (de-collapse the
> CRF context key per the ARC-065/GAP-A fix; couple maintenance to theta(n_matched)) +
> a frac_ACTIVE readiness gate; flip crf-availability-maintenance ready True->False;
> re-queue 654d only after GAP-A context de-collapse. pending_retest_after_substrate.
> NO demotion -- the claims were never tested. Substrate-maturation recurrence, not
> claim-granularity debt (user-adjudicated 2026-06-15).

---

## Routing

- **routing:** implement-substrate (amend `crf-availability-maintenance`, BOTH faults
  + frac_ACTIVE readiness gate + flip ready->not-ready); 654d re-queue gated on GAP-A
  context de-collapse.
- **recommended_substrate_queue_entry.action:** amend (target = `crf-availability-maintenance`).
- governance applies the writes; this autopsy is analysis + handoff only.
