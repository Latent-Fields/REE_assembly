# Failure Autopsy: V3-EXQ-632 (MECH-230 z_goal structured-latent discriminative pair)

- **Generated (UTC):** 2026-06-03T16:41:47Z
- **Scope:** single (with load-bearing cross-reference to the foraging-competence substrate-ceiling cluster: V3-EXQ-603e/626a/622, V3-EXQ-514l, and the V3-EXQ-634 nursery readiness diagnostic)
- **Status:** confirmed (interactive gate answered 2026-06-03)
- **Target:** `v3_exq_632_mech230_zgoal_structured_latent_discriminative_20260603T071913Z_v3` (queue_id V3-EXQ-632)
- **Claim:** MECH-230 (z_goal structured latent goal representation, status provisional, conf=0.814, implementation_phase v3)
- **Outcome:** FAIL, author-stamped `does_not_support`
- **Machine:** ree-cloud-1

This is a **FAIL** (ran to completion, scientific criteria not met), correctly routed to `/failure-autopsy` rather than `/diagnose-errors`.

---

## 1. Facts reconstruction (no interpretation)

Phased discriminative pair on CausalGridWorldV2. P0 (150 ep): encoder/E1/E2/resource-proximity warmup (no z_goal seeding). P1 (100 ep, frozen encoder + heads): measure `z_goal_norm` after resource-contact events. Two conditions on matched shared seeds [42, 7, 13]:

- **GOAL_STRUCTURED**: `z_goal_enabled=True`, `drive_weight=2.0` (SD-012 active).
- **GOAL_ABLATED**: `z_goal_enabled=False` -> `goal_state` is None -> `update_z_goal` early-returns -> no attractor can form.

z_goal seeding fires only in the measurement phase, on `transition_type == "resource"`, using the raw post-step `harm_signal` as benefit magnitude (the documented EXQ-328 measurement-bug fix).

### Criterion table

| Criterion | Threshold | seed 42 | seed 7 | seed 13 | seeds pass | Pass? |
|---|---|---|---|---|---|---|
| C1 structured at contact t0 | > 0.1, >= 2/3 | **3.0115** | 0.0 | 0.0 | 1/3 | FAIL |
| C2 persists at t50 | > 0.05, >= 2/3 | 3.0115 | 0.0 | 0.0 | 1/3 | FAIL |
| **C3 ablated absent (negative control)** | < 0.05, >= 2/3 | 0.0 | 0.0 | 0.0 | **3/3** | **PASS** |
| delta (structured - ablated) at t0 | > 0.05, >= 2/3 | 3.0115 | 0.0 | 0.0 | 1/3 | FAIL |

### Per-condition contact counts (the decisive fact)

| seed | condition | num_contact_events | z_goal_norm @ contact | run_pass |
|---|---|---|---|---|
| 42 | GOAL_STRUCTURED | **6** | **3.0115** (flat across t0/t10/t25/t50) | true |
| 42 | GOAL_ABLATED | 6 | 0.0 | true |
| 7 | GOAL_STRUCTURED | **0** | 0.0 | false |
| 7 | GOAL_ABLATED | 0 | 0.0 | true |
| 13 | GOAL_STRUCTURED | **0** | 0.0 | false |
| 13 | GOAL_ABLATED | 0 | 0.0 | true |

**Failed criterion: discrimination** (C1/C2/delta). The **negative control C3 passes 3/3**. "Negative control passes, discrimination fails" is the substrate-ceiling fingerprint. The proximate cause is unambiguous in the per-seed data: only seed 42 made resource contact (6 events); seeds 7 and 13 made **zero** contact, so z_goal never had benefit input to seed on.

---

## 2. Claim-layer mapping

MECH-230 (`docs/claims/claims.yaml`): "E3 maintains a structured latent goal representation (positive attractor in z_goal sub-space, measurable as z_goal_norm > 0) distinct from harm avoidance, enabling hippocampal terrain navigation toward goal states." mechanism_hypothesis, **provisional**, implementation_phase v3, depends_on SD-012/SD-015/SD-005/ARC-007/MECH-069/ARC-030. claim_ids on the manifest = [MECH-230] (single-claim; tag accurate -- the experiment directly measures z_goal latent structure under SD-012 drive vs ablation).

**Did the experiment test the claim under conditions where it could express itself?** On seed 42 (contact occurred): yes -- and the claim expressed itself cleanly (see Section 4). On seeds 7/13 (no contact): no -- z_goal cannot form a structured attractor with zero benefit input, so the claim was never under test on 2/3 seeds. The aggregate FAIL is therefore a measurement-of-a-prerequisite failure, not a falsification.

**Correction to MECH-230's recorded substrate gap (load-bearing).** The claim's `evidence_quality_note` (2026-04-17) states the blocker is the *E1-frontal -> hippocampal goal-projection* wiring: "z_goal_norm=0 cannot distinguish 'goal not structured' from 'goal not wired to hippocampal system'. No genuine evidential run is possible until the E1-frontal-to-hippocampal goal projection is implemented." **632 seed 42 contradicts this.** When contact occurs, z_goal forms a strong structured attractor (3.0115), persists byte-identically to t50, and is absent under ablation (0.0). z_goal structure forms fine post-contact; the projection wiring is not the operative blocker. The real prerequisite is **foraging-competence / benefit-contact** -- getting the agent to the resource at all. This is the same prerequisite the 603e/626a/622 cluster and 514l surfaced on different substrates.

---

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (on the fair seed) / unclear (aggregate) | seed 42 is a clean positive-discrimination result for MECH-230; aggregate FAIL is driven entirely by 2/3 seeds never reaching the resource, where the claim was never under test |
| Biological reference | clear | vmPFC/OFC incentive-value / goal-representation formation from reward-contact history (Berridge wanting/liking). Faithful translation, not a formal-definition import -- no biology divergence, no lit-pull warranted |
| Developmental / dependency prerequisites | missing | foraging/benefit-contact competence: 2/3 seeds make zero resource contact under the P0/P1 curriculum; SD-012/SD-015 wiring present and verified |
| Implementation completeness | complete | z_goal seeding correctly gated on `transition_type=="resource"` with the post-step benefit fix; GOAL_ABLATED negative control behaves exactly (goal_state None -> 0.0 every seed) |
| Environment adequacy | wrong pressures | the measurement env does not reliably deliver the agent to resources; without contact there is no benefit input to seed z_goal |
| Measurement adequacy | partial / under-instrumented | no foraging-contact-rate guard on the z_goal read -- a z_goal=0 cell cannot be distinguished from "agent never foraged" without the contact count (which here is the only thing that saved interpretability) |
| Integration adequacy | isolated | the goal stream is never integrated into behaviour on the non-foraging seeds because the policy never reaches the contact stage that drives it |
| Scale / capacity | adequate | P0=150 / P1=100 ep is not the binding constraint; seed 42 reached competence at this budget, seeds 7/13 did not -- a curriculum/substrate property, not a budget artifact |

**Recommended `epistemic_category`: `substrate_ceiling`** -- MECH-230 is V3-tractable in principle (seed 42 proves it) but the current substrate cannot reliably deliver the reward-contact the measurement requires across seeds. The correct response is substrate enrichment (foraging-competence), not more experiments on the existing substrate.

---

## 4. Biological-reference triage

- **Closest mechanism:** vmPFC/OFC structured goal/incentive-value representation that forms from reward-contact history; `benefit_exposure` at a resource contact is the consummatory-contact analog feeding `GoalState.update` (SD-012 drive amplification). z_goal is the structured positive attractor MECH-230 asserts.
- **Faithful translation, not a formal import.** This is not a Pearl/Shannon/optimal-control import; it is a direct biological translation. Biology divergence is therefore not in play, and no `/lit-pull` is warranted (lit_conf already 0.831 / 11 entries).
- **Does the failure match a known-dependency-absent signature?** Yes, exactly. Goal representations require reward-contact history to form (Berridge; Dickinson & Balleine outcome re-experience). An agent that never contacts the resource has no substrate from which a structured goal attractor can develop -- which is precisely what seeds 7/13 show, and what seed 42 (the agent that *did* forage) refutes as a claim-level problem. **The FAIL is a discovered/confirmed prerequisite, and seed 42 is positive evidence for the mechanism**, not a falsification.

---

## 5. Cluster cross-reference (load-bearing)

632 is the latest instance of **one structural property**, not an independent bug. The shared shape across structurally-different claims and substrates is the load-bearing signal:

| Experiment | Claim(s) | Negative-control / absolute | Discrimination | Read |
|---|---|---|---|---|
| 603e | Q-045/MECH-313/MECH-260 | wiring/contract pass | z_goal=0 all 15 cells | foraging-competence + benefit-starvation; effective N=1 |
| 626a | (diagnostic) | P0 positive control | z_goal forms 1/3 seeds (foraging seed only) | same prerequisite |
| 514l | MECH-229/230/SD-015/SD-049 | C0..C4 wiring pass | C2c/C5/C6 fail (~0.2% consumption) | same foraging-competence ceiling |
| **632** | **MECH-230** | **C3 ablation 3/3 pass** | **C1/C2/delta 1/3 (2 seeds zero-contact)** | **same: z_goal forms when contact occurs (seed 42=3.011), absent when it does not** |
| 634 (readiness) | (diagnostic, claim_ids=[]) | Stage-0 forced-feed z_goal=0.454 pass | P1 survival / P2 contact=0 / P2 z_goal fail | **nursery fix landed but NOT yet validated**: forced-feed lights z_goal, ecological foraging still fails |

**Structural property:** REE-v3 agents cannot reliably forage competently enough to make ecological resource contact, so any claim whose measurement requires post-contact latent structure (z_goal formation, wanting/liking dissociation) cannot be discriminatively tested at N>1. The two live readings -- (a) substrate-enrichment needed vs (b) test-design ceiling -- both point at the same planning decision: land and validate the foraging-competence substrate before re-issuing these measurements. 632 is informative *toward (a)*: seed 42 shows the downstream mechanism is sound, so the gap is upstream (getting to the resource), not in z_goal formation.

634 is the critical adjacent context: the `scaffolded_sd054_onboarding` nursery/feeding amend (ree-v3 e718bf4 + developmental-window amend) IS landed and its forced-feed Stage-0 positive control passes, but its runtime readiness gates (P1 survival, P2 contact, P2 z_goal) still fail. The substrate fix that would unblock 632 is implemented_pending_validation, not yet ready.

---

## 6. Learning extracted

1. **MECH-230's mechanism is sound when the prerequisite is met.** Seed 42 (6 contacts) produced a structured z_goal attractor of 3.011 that persisted to t50 and was absent under ablation -- clean discrimination. This is positive evidence for the claim, surfaced only because the script recorded `num_contact_events`.
2. **The recorded substrate gap is wrong.** MECH-230's evidence_quality_note attributes the blocker to the E1-frontal -> hippocampal goal-projection wiring; 632 shows z_goal structure forms fine post-contact. The operative prerequisite is foraging-competence / benefit-contact. Governance should correct the recorded gap (recommended note text below).
3. **Same foraging-competence ceiling as 603e/626a/622 and 514l.** One structural property across MECH-229/230/313/260/Q-045 -- the z_goal / goal-pipeline measurement family is uniformly blocked upstream of the claims by the agent's inability to reach resources.
4. **The substrate fix is landed but unvalidated (634).** Forced-feed Stage-0 lights z_goal; ecological P1/P2 foraging still fails. 632's retest is gated on the nursery substrate reaching readiness.
5. **Measurement gap worth porting forward:** the contact-rate guard that made 632 interpretable (without `num_contact_events` this FAIL would read as plain z_goal=0) should be a standard readout on every z_goal-formation measurement. The scaffolded_sd054_onboarding amend already added a P2 contact-rate readout; the 632 successor should adopt it.

---

## 7. Disposition (user-confirmed 2026-06-03)

- **Evidence direction:** `non_contributory` (override the author-stamped `does_not_support`). The aggregate FAIL is a foraging-competence substrate-ceiling, not falsification; on the one fair seed the mechanism worked.
- **epistemic_category:** `substrate_ceiling`.
- **pending_retest_after_substrate:** true (on MECH-230).
- **narrow_supports_flag:** **true.** MECH-230 is provisional (conf=0.814) but its experimental backing is thin: `genuine_exp_count=2` = exactly 1 PASS / 1 FAIL (the FAIL is 632 itself), exp_conf=0.599, quadrant `plausible_unproven`. Reclassifying 632 weakens -> non_contributory leaves MECH-230 resting on a **single experimental support**. non_contributory is the honest call (the FAIL was never a fair test), but it does **not** manufacture closure -- MECH-230 returns to "awaiting a fair experimental test under the foraging-competence substrate," not "confirmed." Flag so governance does not read the reclassification as conflict-resolution.
- **MECH-230 stays provisional / v3_pending** -- no promotion, no demotion. The substrate-ceiling note + pending_retest flag is the governance signal.

### Recommended `evidence_quality_note` (exact text for governance to write)

> [2026-06-03 failure autopsy V3-EXQ-632] FAIL re-read as **non_contributory / substrate_ceiling**, NOT does_not_support. Discriminative pair on z_goal structured-latent formation: negative control C3 (ablated absent) PASSED 3/3, but C1/C2/delta failed because 2/3 seeds (7, 13) made ZERO resource contact (num_contact_events=0) so z_goal never had benefit input to seed on. The one seed that foraged (42, 6 contacts) produced a clean positive result: z_goal_norm=3.0115 at contact, persisting byte-identically to t50, absent under ablation (0.0) -- a structured z_goal attractor distinct from harm avoidance, exactly as MECH-230 asserts. This CORRECTS the prior recorded substrate gap: the blocker is NOT the E1-frontal -> hippocampal goal-projection wiring (z_goal structure forms fine post-contact) but foraging-competence / benefit-contact upstream. Convergent with the 603e/626a/622 cluster and 514l (same foraging-competence ceiling across the z_goal / wanting-liking family). MECH-230 stays provisional/v3_pending, pending_retest_after_substrate; the remaining experimental support is narrow (1 PASS after this reclassification) so non_contributory does NOT resolve the claim -- it returns it to awaiting a fair test on the foraging-competence substrate. Routing: implement-substrate AMEND on scaffolded_sd054_onboarding (add MECH-230 to unblocks_claims + 632 failure_record). The substrate fix is landed (ree-v3 e718bf4 + developmental-window amend) but its runtime readiness gates failed on V3-EXQ-634 (Stage-0 forced-feed lights z_goal, P1 survival / P2 contact still fail), so the 632 retest is gated on the nursery substrate reaching readiness.

---

## 8. Routing (user-confirmed)

**implement-substrate AMEND** on the existing `scaffolded_sd054_onboarding` substrate_queue entry (status `amend_developmental_window_implemented_pending_validation`, ready=false, priority 1). Add MECH-230 to `unblocks_claims` and append a 632 `failure_record`. The gap is already articulated and the substrate is already queued; do not create a duplicate entry. The retest (a MECH-230-tagged re-issue of 632 with a contact-rate guard) is queued via `/queue-experiment` only after a full-scale substrate-readiness run confirms the foraging gates.

`/governance` applies the recommended writes. This autopsy is analysis + handoff only -- no edits to claims.yaml, manifests, evidence_direction, review_tracker, or substrate_queue.
