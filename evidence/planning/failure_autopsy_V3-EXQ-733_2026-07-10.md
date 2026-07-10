# Failure Autopsy — V3-EXQ-733 (rebinding-under-perturbation functional test, MECH-456)

- **Generated (UTC):** 2026-07-10T20:23:01Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated interactive gate 2026-07-10)
- **Run:** `v3_exq_733_rebinding_functional_ground_truth_20260710T130132Z_v3`
- **Queue id:** V3-EXQ-733 · **Claim:** MECH-456 (entities.rebinding_under_perturbation; candidate / v3_pending / substrate_conditional)
- **Outcome:** FAIL / self-stamped `evidence_direction=non_contributory`, label `substrate_not_ready_requeue`
- **Machine:** ree-cloud-2
- **Flagged by:** 2026-07-10 governance cycle (session brave-ishizaka-fa60b4)

## 1. Facts (ran to completion; 6/6 seeds, no errors)

The self-route is **correct**: the pre-registered readiness gate is genuinely unmet, so the run is `non_contributory` (NOT a rebinding verdict, NOT weighted in confidence/conflict scoring). This is not a mis-self-route of the V3-EXQ-642 kind — the substrate (learned cross_stream_binder) *did* train and converge; what is thin is the number of ground-truth overtake events available to the measurement.

Readiness preconditions (per `interpretation.preconditions`):

| Precondition | measured | threshold | met |
|---|---|---|---|
| learned_binder_converged (worst loss_ema) | 3.381 | 3.535 | **yes** |
| region_coverage_adequate (min P0 region visits) | 34 | 10 | **yes** |
| overtake_events_adequate (min P1 overtakes/seed) | **2** | **20** | **NO** |

Per-seed overtakes / P1 steps / readiness:

| seed | n_overtakes | n_p1_steps | steps/ep (÷25) | seed_ready | DV1 | DV2 (latency gap) |
|---|---|---|---|---|---|---|
| 42 | 26 | 744 | ~30 | **True** | ✓ (0.806 vs 0.232, m=0.574) | ✓ (17.7−4.6 = 13.1) |
| 43 | 2 | 241 | ~10 | False | ✓ | ✗ (−3.0; 2 events only) |
| 44 | 15 | 1029 | ~41 | False | ✓ | ✓ (9.5) |
| 45 | 14 | 417 | ~17 | False | ✓ | ✓ (13.5) |
| 46 | 13 | 349 | ~14 | False | ✓ | ✓ (17.0) |
| 47 | 11 | 701 | ~28 | False | ✓ | ✓ (16.5) |

**DV1 passed 6/6; DV2 passed 5/6.** Both DV criteria (`dv1_pass`, `dv2_pass`, `both_pass`) are `True` in the manifest — the *only* thing preventing `functional_rebinding_supported` is `all_ready=False` (the overtake quorum). On the one fully-ready seed (42) both DVs pass strongly and well clear their pre-registered margins. **This is encouraging for MECH-456, not refuting.**

## 2. Root cause of the unmet gate (decisive finding)

`CausalGridWorldV2.step` sets `done = self.agent_health <= 0.0 or self.steps >= 500` (`ree_core/environment/causal_grid_world.py:2528`). The experiment caps each episode at `STEPS_PER_EPISODE = 120` (< 500), so **within an episode `done` can only fire from agent death (health ≤ 0).** The observed average steps/episode (~10–41 vs the 120 cap) therefore mean the agent is **dying to hazards in ~10–40 steps**. Short episodes → few within-episode region-boundary crossings → thin overtakes → readiness quorum unmet.

Why is the agent dying? `_make_agent` builds a **cold, un-onboarded** agent (full SP-CEM + harm-stream + z_goal stack, but no staged survival pre-training) and drops it into the deliberately-lethal SD-054 reef-bipartite env (`hazard_food_attraction=0.7` forces the agent toward hazards to forage). This is the *exact* env whose lethality motivated the `scaffolded_sd054_onboarding` curriculum — which is **already BUILT + VALIDATED** (P1 survival 3/3; V3-EXQ-603m/603n). 733 simply did not use it.

## 3. Claim-layer mapping

MECH-456 (`claims.yaml:24359`): mechanism_hypothesis, `entities.rebinding_under_perturbation`, status `candidate`, `epistemic_category: substrate_conditional`, `v3_pending: true`, registered 2026-07-10 (salvaged from `failure_autopsy_V3-EXQ-725a_2026-07-10`). `depends_on`: ARC-006, INV-002, MECH-045, MECH-269, MECH-270. `what_would_answer` requires BOTH (1) rebinding tracks the true competitor above a shuffle control AND (2) a graded, non-saturating behavioural consequence vs a frozen arm. V3-EXQ-733 is the claim-tagged functional test that operationalises exactly (1)=DV1 and (2)=DV2.

Did the test let the claim express itself? **On the ready seed, yes** — and the answer there was affirmative on both conditions. The failure is upstream of the claim: the test-bed under-generated the overtake events the measurement needs. This must **not** demote MECH-456; MECH-456 stays candidate/v3_pending regardless (V3-pending gate) with no supporting evidence yet weighted.

`claim_ids` accuracy: correct (single tag MECH-456; `bears_on_not_tagged` = MECH-269, MECH-270, ARC-006, MECH-045, INV-002 — appropriate, untagged).

## 4. Biological-reference triage

MECH-456's grounding is object-file updating (Kahneman/Treisman/Gibbs), serial-dependence hysteresis (Manassi & Whitney), PE-driven perceptual switching (Weilnhammer; Cole ACC), latent-cause inference (Gershman) — an E(τ)/stability grounding, explicitly **not** a formal-import (the coherence-C(τ) import was settled NO-CLAIM by V3-EXQ-725a and is excluded from MECH-456). So no `/lit-pull` commission is owed; biology divergence is not the issue here. The failure is a translation/test-bed adequacy gap, not a formal-import mechanism error.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (partial) | DV1 6/6, DV2 5/6 — binder tracks truth AND confers a graded advantage wherever overtakes occurred. |
| Biological reference | clear | non-formal-import; not the fault locus. |
| Developmental / dependency prerequisites | present but un-invoked | validated survival onboarding (`scaffolded_sd054_onboarding`) exists but is not used → cold agent dies. |
| Implementation completeness | complete | binder converged; harness-level measurement; `ree_core` unmodified. |
| Environment adequacy | wrong pressures for this readout | SD-054 env kills a cold agent before it traverses regions; overtake generation is entangled with foraging survival. |
| Measurement adequacy | partial | 20-overtake/seed floor mismatched to an env that ends episodes in ~10–40 steps. |
| Integration adequacy | isolated | binder works alone; the test-bed can't feed it enough overtakes. |
| Scale / capacity | adequate | P0 convergence + region coverage both met. |

**Recommended `epistemic_category`: `substrate_ceiling`** (survival/navigation-competence flavour) — with the load-bearing qualifier that the blocking substrate is **already built and validated**, so the repair is a re-queue over the existing scaffold, **not** a new deep-substrate build and **not** the exhausted conversion-ceiling park.

## 6. Adjudication of the competing reads

- **(A) pure power/coverage — REJECTED as sufficient.** On the dying seeds the yield is ~0.08–0.5 overtakes/episode; more episodes won't efficiently reach 20/seed and would treat the symptom, not the early-death cause.
- **(B) co-blocked on the conversion ceiling (literal) — REJECTED as the repair route.** B correctly reads thin overtakes as a *competence* symptom, but the deep substrate it points at — `f_dominance_conversion_ceiling` and `v4_loop_segregation` — is **exhausted, `ready=False`, "PROMOTES_NOTHING," V3-closure-required**. Parking MECH-456 there stalls it indefinitely, and is unwarranted because (a) the binder demonstrably works and (b) the survival substrate needed to *generate* overtakes is already validated.
- **CONFIRMED read:** a **training-regime + test-design gap over an already-built survival substrate.** The cold agent died before it could traverse regions; the fix is a re-queued redesign that restores episode survival and/or decouples overtake generation from foraging competence.

## 7. Learning extracted

- The MECH-456 functional readout is currently **entangled** with foraging-survival competence: overtakes (ground-truth region crossings) can only accrue while the agent stays alive and navigates. A cold agent in the SD-054 env dies in ~10–40 steps, starving the measurement — the binder mechanism is not at fault.
- The binder tracks ground-truth and confers a graded re-acquisition advantage on every seed that produced enough overtake events (DV1 6/6, DV2 5/6) — MECH-456's `what_would_answer` is affirmatively met on the ready seed; the block is purely the seed-quorum.
- A functional test that rides on agent navigation to generate its own ground-truth events must either (a) equip the agent with the validated survival onboarding or (b) decouple event generation from the floored competence — otherwise the readiness gate, not the mechanism, decides the outcome.

## 8. Routing (user-confirmed)

`/queue-experiment` **redesign V3-EXQ-733a** (same scientific question → letter suffix, `supersedes: V3-EXQ-733`), fanned out into a **2-leg portfolio** (each leg faithfully tests MECH-456's `what_would_answer`; each declares its null):

- **Leg P-A (training-regime axis):** run the functional test on a **survival-onboarded** agent — adopt the validated `scaffolded_sd054_onboarding` curriculum so P1 episodes survive long enough to accrue ≥20 overtakes/seed on ≥4/6 seeds. Null: even survival-onboarded, overtakes stay < 20/seed → survival is not the (only) lever.
- **Leg P-B (test-bed / environment axis):** generate region-crossings **independent of foraging survival** — directed reset spawns across regions, and/or a finer lattice (larger `G_PARTITION`) to raise boundary-crossings per unit movement, and/or softened survival pressure (lower `hazard_harm` / fewer hazards) so the agent survives to traverse. Isolates the binder readout from the navigation-competence confound. Null: with overtakes guaranteed, DV1/DV2 fail to clear on ≥4/6 → the seed-42 signal was not general.

`evidence_direction` stays **non_contributory**; `pending_retest = True`. **No new `substrate_queue` entry owed** (`action: none`) — the survival substrate already exists and is validated; the dependency is recorded in the draft `evidence_quality_note` below. Re-derive brake: **not fired** (first `substrate_ceiling`/`non_contributory` autopsy tagging MECH-456). MECH-456 remains candidate / v3_pending.

### Draft `evidence_quality_note` (for /governance to write on MECH-456 — do not write here)

> V3-EXQ-733 (functional rebinding test) FAILed on the pre-registered readiness quorum only (min overtakes/seed 2 vs 20; only seed 42 reached the floor) → `non_contributory`, not a rebinding verdict. Root cause (autopsy 2026-07-10): a cold, un-onboarded agent dies to hazards in ~10–40 steps (`done=health<=0`, episodes capped at 120<500) in the lethal SD-054 reef env, starving within-episode ground-truth overtakes. The binder itself passed DV1 6/6 and DV2 5/6, both strongly on the one ready seed — encouraging for MECH-456. Re-queued as V3-EXQ-733a (2-leg portfolio: P-A survival-onboarded agent via validated `scaffolded_sd054_onboarding`; P-B directed-traversal test-bed decoupling overtakes from foraging survival). pending_retest. NOT co-blocked on the exhausted `f_dominance_conversion_ceiling` / `v4_loop_segregation` substrate; the survival substrate needed here is already built + validated.

## 9. Handoff

Next: `/queue-experiment` for V3-EXQ-733a (2-leg portfolio above). A follow-up `/governance` run consumes this artifact (writes the `evidence_quality_note`, marks V3-EXQ-733 reviewed as `non_contributory`, no promotion/demotion of MECH-456).
