# Failure Autopsy -- V3-EXQ-047m (MECH-095 TPJ agency-routing CORRECTED retest on SD-047)

- **Generated (UTC):** 2026-07-11T21:38:53Z
- **Scope:** single (load-bearing signal is the RECURRENCE with V3-EXQ-047l)
- **Status:** confirmed (interactive gate answered)
- **Target:** run_id `v3_exq_047m_mech095_agency_routing_sd047_20260711T195846Z_v3`, queue_id `V3-EXQ-047m`, machine `ree-cloud-2`
- **Claim:** MECH-095 (`tpj.agency_detection_comparator`) -- candidate / substrate_ceiling / pending_retest_after_substrate
- **Verdict adjudicated:** FAIL (3/5), self-stamped `non_degenerate: true`, `evidence_direction: mixed`, decision `ceiling_confirmed_route_autopsy`.
- **Autopsy verdict:** **non_contributory -- SECOND operationalisation degeneracy** (training-label saturation). NOT a valid `substrate_ceiling` hit; NOT a claim falsification. `n_ceiling_hits` STAYS 0. **Re-derive brake FIRES** (2nd non-informative read for MECH-095, threshold 2). Route to a **test-bed redesign** (`/implement-substrate`); **REFUSE a third 047 letter.**

---

## 1. Facts (from manifest -- no interpretation)

Pre-registered criteria (identical to the EXQ-047k PASS / 047l):

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world_routed > 0.55 | **FAIL** | 0.492 |
| C2: recall improvement (routed - baseline) > 0.04 | **FAIL** | -0.302 |
| C3: action_dissoc_mean > -0.05 | PASS | -0.002 (std 0.032) |
| C4: n_contact_probe (min) >= 20 | PASS | 97 |
| C5: no fatal errors | PASS | -- |

Load-bearing observations:

- **Probe partition is non-degenerate this time** (the 047m fix worked): `n_no_contact_min = 8 >= PROBE_NEG_FLOOR 5`, `non_degenerate: true`. The eval contrast was real -- unlike 047l's empty negative class.
- **Routing HURTS recall.** ROUTED contact_recall_world 0.492 vs BASELINE 0.795 -> recall_improvement **-0.302**. C1 and C2 (the two discrimination criteria) both FAIL, load-bearing.
- **Secondary, non-degenerate:** action-dissociation collapsed BASELINE +0.140 -> ROUTED -0.002 (z_world became as action-predictive as z_self under routing) -- a *stronger* replication of the same claim-orthogonal side-effect flagged in the 047l autopsy.
- **Seed heterogeneity is a degeneracy tell, not a clean ceiling.** ROUTED contact_recall_world per seed: 0.562 / 0.545 / **0.111** / 0.750. Seed 123 is catastrophic (world 0.111 while self 1.000) -- the routing head *inverted* the self/world axis for that seed. This variance is a signature of an unstable training signal, not a uniform substrate ceiling.
- Routing head active: mean_routing_loss 0.0046. SD-047 active: env_ev_ticks ~4405-4484 per cell.
- Failed criterion type: **discrimination** (C1/C2).

## 2. Claim-layer mapping

MECH-095: `mechanism_hypothesis`, status `candidate`, `epistemic_category: substrate_ceiling`, `pending_retest_after_substrate: true`, `depends_on: [SD-005, MECH-069, ARC-021]`. Lit strong (lit_conf ~0.907: Blakemore 2002, Gu 2008, Pitcher & Ungerleider 2021, Rolls 2023). GOV-CEIL-1 floored active->candidate on 2026-07-11 with `n_ceiling_hits=0`, mapping SD-047 as the enrichment owner. 047l (1st retest) was non_contributory (empty eval negative class); 047m is the corrected successor. `claim_ids` accuracy: correct (MECH-095 only).

**Did the experiment test the claim under conditions where it could express itself? No** -- for a *different* reason than 047l. 047l never populated the eval contrast; 047m populates the eval contrast but the **training** contrast is degenerate (Section 3). The comparator was invalidly *trained*, so the claim is neither supported nor weakened.

## 3. Root cause -- dispositive: the env_events fold now saturates the TRAINING label

The routing-head training label (047m line 343-346, KEPT from 047l by design):

```python
is_world = 1.0 if (prev_ttype in WORLD_CAUSED or prev_env_events > 0) else 0.0
```

`multi_source_n_env_events` is a per-step counter incremented by env hazards + transient appear/disappear + **background drift moves** (causal_grid_world.py:2303, 2324-2326). With `N_DRIFT_SOURCES=2` random-walking **every step** (line 2326), `env_events > 0` fires on essentially every step. Arithmetic from this manifest: episodes die at ~11 steps (`done = agent_health <= 0`, causal_grid_world.py:2528; probe records ~110 steps / 20 double-stepped episodes), so training is ~400 x ~11 ~= 4800 steps and `env_ev_ticks` ~4470 -> **`env_events > 0` on ~93%+ of training steps**. Therefore **`is_world` ~= constant 1.0**: the routing head almost never sees a self-caused (`is_world=0`) example.

**Consequence.** A comparator trained on a near-constant-positive label cannot learn a self-vs-world discrimination -- there is no contrast to carve. Its BCE gradient into z_world is a degenerate, homogenizing pressure that:
1. does NOT isolate world-causation (no negative class to separate from), and
2. **actively corrupts** the contact structure z_world already acquires from E1+E2 (BASELINE 0.795 -> ROUTED 0.492), and injects generic action/transition structure (action-dissoc collapse 0.140 -> 0.000).

**This is the SAME env_events-fold disease as 047l, moved from the EVAL probe to the TRAINING label.** 047l over-applied the fold into the *probe* partition (empty negative eval class -> vacuous 0.0). 047m correctly reverted the *probe* partition to 047k's `CONTACT_SET`, but the identical fold in the *training* label saturates the routing head's supervision. The 047m non-degeneracy guard checks only `n_no_contact` in the **probe** -- it does **not** check training-label balance -- so `non_degenerate: true` is a **FALSE CLEAR** of validity. The eval contrast was validated; the training contrast was not.

**Proof by contrast with the 047k PASS:** 047k ran on the THIN env, where `is_world` = `prev_ttype in WORLD_CAUSED` had a genuine self/world contrast (agent_caused vs env_caused hazards), and PASSed 5/5 (recall 0.796). The saturation is specific to SD-047 @ intensity 1.0, where world-caused change is so pervasive that "is this change world-caused?" is trivially yes.

## 4. Why this is NOT a substrate_ceiling hit -- three independent reasons

1. **Training-label saturation (Section 3):** the comparator was never validly trained. A ceiling test requires the mechanism to have been validly exercised; it was not.
2. **Wrong experiment.** The pre-registered SD-047 validation (`docs/architecture/sd_047_multi_source_dynamics.md`, "Validation experiment") is a **4-arm intensity sweep** (ARM_0 OFF -> ARM_1 0.25x -> ARM_2 1.0x -> ARM_3 4.0x), keyed on ARM_0-vs-ARM_2, designed to observe Asai (2016) non-monotonicity and to route the Woo/Spelke (2023) falsifier. The doc explicitly warns a **binary** test is "under-specified -- a flat ON-vs-OFF result would be ambiguous between 'SD-047 works' and 'SD-047 overshot calibration.'" 047m is a binary comparator-ON-vs-ABLATED at fixed intensity 1.0 -- the wrong contrast axis, and the Asai "overshot" branch (too much env noise overwhelms the agent's self-signal, slope flattens) is exactly what the label saturation instantiates and is unexcluded.
3. **Baseline already succeeds (0.795).** z_world encodes contact well WITHOUT the comparator -> the substrate is not representation-ceiling-limited for the target signal. The failure is corruption of an already-good representation, not an absent signal. A genuine substrate ceiling would look like routed ~= baseline ~= chance, not baseline-succeeds / routing-hurts.

## 5. Biological-reference triage

Closest reference: TPJ as an agency-detection comparator (self- vs other-caused change against a textured causal background). Lit already strong (lit_conf ~0.907) -> **no `/lit-pull` commission owed.** The failure is not a missing biological dependency and not a biology divergence from a formal import -- it is a test-bed/operationalisation artifact.

**Load-bearing redesign input (not a falsification):** MECH-095's own notes (claims.yaml:6830-6847) describe a **read-out** comparator -- compare *efference-copy-predicted* z_self change against *observed* z_self change; divergence attributes to z_world. The 047-lineage instead operationalises it as an **auxiliary BCE head that reshapes z_world by gradient** to predict a world-vs-self label. That is plausibly the wrong functional translation: it makes the comparator a representation-shaping pressure competing with E1+E2 (hence routing degrades an already-good z_world), rather than a query-time read-out that leaves the representation intact. This should inform the test-bed redesign; it is a hypothesis, not a verdict.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | comparator invalidly trained; neither supports nor weakens |
| Biological reference | clear | TPJ read-out comparator; the auxiliary-BCE-head translation is a candidate divergence (redesign input, not falsification) |
| Prerequisites | present | SD-005 split-latent active; SD-047 landed + active |
| Implementation | **partial (dominant, training side)** | routing head active but trained on a saturated label (is_world ~const 1) -> degenerate supervision; the guard validated only the probe, not the training contrast |
| Environment | **wrong pressure at this intensity** | SD-047 @ intensity 1.0 makes world-caused change ~ubiquitous -> the self-vs-world contrast the comparator needs collapses; pre-registered fix is the intensity SWEEP, not a single point |
| Measurement | adequate (this time) | probe partition non-degenerate (n_no_contact_min 8 >= 5); the eval contrast is real -- the failure is upstream in training |
| Integration | isolated | single-mechanism probe; n/a |
| Scale | adequate | 97-110 contacts x 4 seeds |

**Dominant layers:** implementation-completeness (training-label saturation) + environment-adequacy (intensity 1.0 collapses the self/world contrast; binary != the pre-registered sweep). **Recommended `epistemic_category` for the run: `measurement_degeneracy` / operationalisation degeneracy** -- explicitly **not** `substrate_ceiling`. MECH-095's claim-level `epistemic_category` stays `substrate_ceiling`; `n_ceiling_hits` stays 0.

## 7. Recurrence pattern (047l + 047m) -- the load-bearing signal

| Experiment | Where the env_events fold degenerated | Guard status | Read |
|---|---|---|---|
| 047l | EVAL probe partition (`is_contact` folded env_events>0) -> empty negative eval class | no probe guard | non_contributory (probe never exercised) |
| 047m | TRAINING label (`is_world` folds env_events>0) -> is_world ~const 1 | probe guard added (fixed eval) but NO training-label guard | non_contributory (comparator never validly trained) |

**Structural property, not two independent bugs:** the `env_events>0` additive fold is degenerate at intensity 1.0 *wherever applied*, because SD-047's drift sources make env_events fire on ~every step. Fixing it in one place (the probe) exposed it in the other (the training label). **Two non-valid reads on the same operationalisation implicate the OPERATIONALISATION, not the substrate** -- exactly the escalation the 047l autopsy and the claims.yaml RE-DERIVE-BRAKE ESCALATION FLAG (6918-6921) pre-registered.

## 8. Re-derive brake (MOVE-3) -- FIRES

- Prior `substrate_ceiling`/`non_contributory` failure_autopsy_*.json tagging MECH-095: **1** (`failure_autopsy_V3-EXQ-047l_2026-07-11`).
- This autopsy is the **2nd** non_contributory read for MECH-095. Threshold = 2 -> **brake FIRES.**
- **Refused:** a third 047 letter (047n) that re-tests the same claim against the same substrate at the same intensity. A same-question lettered re-pose is exactly the loop the brake exists to stop.
- **Route:** `/implement-substrate` -> build a valid **agency-comparator test-bed** on SD-047 (substrate_queue `create`; see Section 9). SD-047 the *substrate* is already built and correct -- the missing upstream is the **test-bed + a non-saturating comparator operationalisation**, which is `complicated (buildable)`.
- A redesign that tests a *different* mechanism (new EXQ number, different claim_ids) or a commitment-free read remains allowed; another 047 letter does not.

## 9. Learning extracted + repair pathway

Learning:
- **Training-label saturation discovered:** the env_events additive fold that makes ROUTED != BASELINE on SD-047 also makes `is_world` ~constant 1 at intensity 1.0, degenerating the comparator's supervision. A non-degeneracy guard must check the **training-label balance**, not only the probe partition.
- **Binary-at-fixed-intensity != the pre-registered SD-047 validation.** The owed test is the 4-arm intensity sweep (Asai non-monotonicity + Woo/Spelke branch), never run.
- **Operationalisation candidate divergence:** auxiliary-BCE-head-reshaping-z_world vs a query-time read-out comparator (biology favours the latter).
- Two non-valid reads (047l probe, 047m training) => the 047-on-SD-047 operationalisation is the fault, not the substrate.

**Node classification (work_graph_debt_vocabulary):** the residual is `complex (probe-gated) / mystery (known data)` at the top level -- we already have the data (two degenerate reads) telling us the *frame* (binary @ intensity 1.0 + saturating fold) is wrong; more same-frame runs will not settle it, so reframe. The reframe itself -- build the pre-registered sweep test-bed + a non-saturating comparator -- is `complicated (buildable)`.

**Routing: `/implement-substrate`** via a substrate_queue `create` entry (governance materialises it). Refuse `/queue-experiment` for a same-claim 047 letter (brake). The test-bed spec:
1. **Non-saturating routing-label / comparator operationalisation.** Either (a) restrict the training label to `prev_ttype in WORLD_CAUSED` (drop the env_events fold) and instead make SD-047's env-caused events *set* a transition_type so the label carries a real self/world contrast, or (b) reoperationalise MECH-095 as a query-time read-out comparator (efference-copy-predicted vs observed z_self change) that does not reshape z_world by gradient. Add a **training-label non-degeneracy guard** (require both classes populated above a floor per cell) mirroring the probe guard.
2. **The pre-registered 4-arm intensity sweep** (ARM_0 OFF / ARM_1 0.25x / ARM_2 1.0x / ARM_3 4.0x), keyed to ARM_0-vs-ARM_2, so the Asai non-monotonicity and the Woo/Spelke falsifier branch are both testable per the sd_047 interpretation grid.
3. Report BASELINE + ROUTED contact_recall and action_dissoc at every arm (the routing-hurts / action-dissoc-collapse signals are the diagnostics).

**GOV-FANOUT-1:** the open question after redesign is a genuine *discrimination* (H1 operationalisation-fault vs H2 Woo/Spelke V4-bound vs H3 Asai calibration-overshoot), but the discrimination is **realized inside the test-bed** (the intensity sweep IS the portfolio across the calibration axis, and a corrected operationalisation is the axis for H1). Per GOV-FANOUT-1's "exempt: routes to one unambiguous build," the immediate routing is the single test-bed build, NOT sequential 047 letters. The fanout_recommendation is recorded to inform what the test-bed must contrast, not to spawn separate probes.

**pending_retest_after_substrate:** **keep true, RE-POINT the blocker.** SD-047-the-substrate is built (that condition is satisfied), but the retest has been attempted twice and both were non-valid. The claim is *retest-blocked-on-testbed*, not retest-resolved. Governance should re-point the flag's referent from "SD-047 implementation" (done) to the new substrate_queue test-bed entry. The ceiling audit should move MECH-095 off `ceiling_may_have_lifted` to `ceiling-retest-blocked-on-testbed`. `n_ceiling_hits` stays 0.

Not a ceiling hit, not demotion, not lit-pull, not a 3rd 047 letter.

## 10. Interactive gate -- resolved

User confirmed (2026-07-11):
- **Ledger reading:** 2nd operationalisation degeneracy -> `non_contributory`; `n_ceiling_hits` STAYS 0; MECH-095 stays candidate / substrate_ceiling / pending_retest_after_substrate. Re-derive brake FIRES.
- **Routing:** `/implement-substrate` test-bed redesign (substrate_queue `create`); **keep + re-point** `pending_retest_after_substrate`; refuse a 3rd 047 letter.

## 11. Draft `evidence_quality_note` (for `/governance` to write -- NOT written by this skill)

> V3-EXQ-047m (2026-07-11, SD-047 @ intensity 1.0, 4 seeds, ree-cloud-2) is the CORRECTED successor to 047l. Its probe-partition fix worked (non_degenerate=true, n_no_contact_min=8 >= floor 5) so the EVAL contrast was real, and it FAILed 3/5 with routing HURTING recall (ROUTED 0.492 vs BASELINE 0.795, improvement -0.302). But this is NON_CONTRIBUTORY -- a SECOND operationalisation degeneracy, NOT a substrate_ceiling confirmation and NOT a weakens. Root cause: the identical env_events fold that saturated 047l's PROBE now saturates the TRAINING label. `is_world = 1 if (prev_ttype in WORLD_CAUSED or env_events>0)`, and at intensity 1.0 the 2 background-drift sources fire env_events>0 on ~93%+ of steps (env_ev_ticks ~4470 of ~4800; episodes die ~11 steps), so is_world ~= constant 1 -- the routing head never sees a self-caused negative and cannot learn the discrimination; instead it homogenizes z_world, degrading an already-good BASELINE contact encoding (0.795) and collapsing action-dissociation (BASELINE +0.140 -> ROUTED -0.002; seed 123 catastrophic: world 0.111 / self 1.000). The 047m guard validated only the PROBE partition, not the training-label balance, so non_degenerate=true is a FALSE CLEAR of validity. Three independent reasons this is not a valid ceiling hit: (1) comparator invalidly trained (saturated label); (2) 047m is a binary comparator-ON-vs-ABLATED at fixed intensity 1.0, NOT the pre-registered 4-arm SD-047 intensity sweep (sd_047 doc warns a binary test cannot distinguish 'SD-047 works' from 'SD-047 overshot calibration' -- the Asai overshoot branch is exactly the label saturation and is unexcluded); (3) the BASELINE succeeds at 0.795, so the substrate carries the contact signal -- the failure is corruption of a good representation, not an absent one. n_ceiling_hits STAYS 0. RE-DERIVE BRAKE FIRES (2nd non_contributory MECH-095 read, threshold 2): route to a test-bed redesign, REFUSE a third 047 letter. The convergent 047l(probe)+047m(training) shape implicates the OPERATIONALISATION (the env_events fold is degenerate at intensity 1.0 wherever applied), not the substrate. Load-bearing redesign input: MECH-095's notes describe a query-time read-out comparator (efference-copy-predicted vs observed z_self), but the 047-lineage operationalises it as an auxiliary BCE head reshaping z_world by gradient -- plausibly the wrong functional translation. Substrate_queue: CREATE an agency-comparator test-bed entry (non-saturating training label / read-out reoperationalisation + a training-label non-degeneracy guard + the pre-registered 4-arm intensity sweep). pending_retest_after_substrate stays true but RE-POINTED from 'SD-047 build' (done) to that test-bed; ceiling audit moves MECH-095 off 'ceiling_may_have_lifted' to 'ceiling-retest-blocked-on-testbed'. MECH-095 stays candidate / substrate_ceiling / pending_retest_after_substrate; this consumption PROMOTES/DEMOTES NOTHING.

Governance actions implied (this skill does not apply them):
- Set `evidence_direction: non_contributory` + note on the 047m manifest (flat + runs/ pack); rebuild indexes; mark reviewed in review_tracker.json; regenerate pending_review to confirm 0 pending for 047m.
- MECH-095: append the note above; **no status/category change**; keep `n_ceiling_hits=0`; keep `pending_retest_after_substrate: true` but re-point its blocker to the new substrate_queue test-bed entry.
- substrate_queue: `create` the agency-comparator test-bed entry (Section 9 / JSON artifact).
- Ceiling audit: MECH-095 `ceiling_may_have_lifted` -> `ceiling-retest-blocked-on-testbed`.
