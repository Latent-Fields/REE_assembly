# Failure Autopsy -- V3-EXQ-610c (INV-074 crystallization necessity)

- **Generated (UTC):** 2026-06-03T06:51:53Z
- **Scope:** single (with explicit lineage note -- 7th member of the crystallization-arm non_contributory family)
- **Status:** confirmed (interactive gate; user-approved routing 2026-06-03)
- **Skill:** /failure-autopsy
- **Run:** `v3_exq_610c_inv074_crystallization_necessity_20260602T191404Z_v3`
- **Queue id:** V3-EXQ-610c (supersedes V3-EXQ-610b)
- **Machine:** ree-cloud-2
- **Claims tested:** INV-074 (primary; universal invariant), MECH-334, MECH-333
- **experiment_purpose:** evidence
- **Manifest evidence_direction (as found):** `unknown` (untriaged -- the diagnosis this autopsy supplies)

---

## 1. Facts -- reconstruction (no interpretation)

Two-arm discriminative experiment, 3 matched seeds (42/43/44), 2500 episodes/arm,
4-phase infant curriculum, Phase-3 WITH the IGW-20260601-023 destabilising-pressure
substrate (SD-047 multi_source_dynamics + SD-048 interoceptive_noise + accelerated
env_drift). Primary observable: Shannon entropy of the selected-action distribution
over the last 50 episodes of Phase 2 (peak window) and Phase 3 (post-closure +
pressure).

Action space = 5 (CausalGridWorldV2.ACTIONS = up/down/left/right/stay); `ln 5 = 1.609`
nats is the maximum entropy.

Pre-registered acceptance:

| Criterion | Rule | Result | Value |
|---|---|---|---|
| D1 crystallization preserves diversity | ARM_1.p3 - ARM_0.p3 >= +0.10 | **FAIL** | -0.0130 (crystallized arm marginally LOWER) |
| D2 control shows collapse | ARM_0.p2 - ARM_0.p3 >= +0.10 | **FAIL** | +0.0465 (weak, below floor) |
| D3 sanity both diverse at p2 | both p2 > 0.4 | PASS | 1.1200 / 1.1200 |
| Verdict | D1 AND D2 AND D3 | **FAIL** | -- |

Per-arm per-seed (p2 -> p3 entropy):

| Seed | ARM_0 control p2 | ARM_0 p3 | ARM_1 test p2 | ARM_1 p3 |
|---|---|---|---|---|
| 42 | 1.0908 | 0.9718 (-0.119) | 1.0908 | 0.9332 |
| 43 | 0.9581 | 0.9922 (+0.034) | 0.9581 | 0.9786 |
| 44 | 1.3110 | 1.2566 (-0.054) | 1.3110 | 1.2699 |

Observations:
- Phase-2 entropies are **byte-identical** between ARM_0 and ARM_1 per seed -- the
  two arms are bit-identical up to the Phase-3 entry where crystallization fires.
- All six runs sit at 0.66-0.81 of max entropy (1.06-1.31 nats / 1.609 max) =
  **near-uniform action distribution** -- no monostrategy in either arm.
- D2 "collapse" is weak and seed-dependent: only seed 42 clears the 0.10 floor;
  the mean +0.0465 is dominated by one seed.
- D1 is essentially zero / marginally negative in every seed: crystallization did
  not preserve more diversity than control in any seed.
- Mean reward -1.03 to -1.14 across all six runs: the agent never learned a
  competent harm-avoiding / benefit-seeking policy.

---

## 2. The load-bearing finding: crystallization is a behavioral no-op in this harness

Reading `ree-v3/experiments/v3_exq_610c_inv074_crystallization_necessity.py`, three
instrumentation gaps make D1/D2 **non-discriminative by construction**:

1. **The policy is never trained.** Lines 575-585 sketch a REINFORCE-like update,
   build `policy_loss_t` with `requires_grad=False`, and end in
   `pass  # Omit policy training in this substrate diagnostic`. Grep confirms
   `policy_optimizer.step()` is **never called** anywhere in the training loop
   (only `aux_optimizer`, `e2_wf_optimizer`, `harm_eval_optimizer`, `e1_optimizer`
   step). The `gated_policy` parameters sit at initialisation in BOTH arms.

2. **`crystallize()` freezes never-trained heads.** At Phase-3 entry (ARM_1 only)
   `gated_policy.crystallize()` sets `requires_grad=False` on head_0/head_1/
   discriminator and adds a zero-init plastic expansion channel (output bit-identical
   at the transition instant). The policy optimizer is rebuilt to target
   `expansion_parameters()` (line 636) but is **never stepped**. So the expansion
   channel stays at its zero-output init -> post-crystallization gated_policy output
   is bit-identical to pre-crystallization.

3. **`ewc_penalty()` is never added to any loss.** Only `snapshot_ewc_anchor()`
   fires (MECH-334 anchor capture); the EWC penalty term that would write-protect
   the diversity distribution is never called. `residue_ewc_lambda=0.1` is set but
   inert.

Consequence: INV-074's predicted mechanism -- *gradient-driven winner-take-all
monostrategy collapse of a learned policy, which a time-bounded plasticity
asymmetry must precede* -- **is never instantiated**. With no policy learning there
is no WTA dynamic; with no WTA the control cannot collapse (D2 has nothing to
measure), and a no-op crystallization cannot preserve anything (D1 has nothing to
measure). The near-uniform entropy in both arms is an untrained-policy /
SP-CEM-diverse-candidate distribution that neither the Phase-3 env pressure nor the
weight-freeze can move.

The marginally-LOWER D1 (crystallized arm slightly below control) and the weak,
single-seed D2 are pure noise around two near-identical near-uniform distributions,
exactly as the no-op reading predicts.

---

## 3. Why this supersedes the 610b "env ceiling" diagnosis

610b (same harness) was read by 2026-06-01 governance as "CausalGridWorldV2 supplies
no post-Phase-3 destabilising pressure (env/test-bed ceiling)" and routed to a
substrate_queue amend (`test_bed_enrichment_crystallization_necessity`, priority 3),
implemented as IGW-20260601-023 (SD-047 + SD-048 + accelerated drift in
InfantCurriculumScheduler Phase 3). 610c ran **with** that pressure and D2 STILL
failed (control still did not collapse).

This run is the evidence that the env-ceiling hypothesis was insufficient: **the
substrate fix targeted the wrong layer.** Env pressure cannot induce policy collapse
when the policy is never trained. The actual blocker is upstream of the environment,
at the experiment harness (no policy training) -- a measurement / test-design defect,
not a substrate ceiling for this run.

---

## 4. Claim-layer mapping

INV-074 (universal invariant, candidate, conf via exp indirect, lit_conf 0.82,
epistemic_category=substrate_ceiling, pending_retest_after_substrate=true): asserts
that a model-building agent whose scoring is dominated by a high-variance predictive
pathway converges to monostrategy under Hebbian-equivalent learning unless a
time-bounded plasticity asymmetry lets diversity circuits establish competitive
weight before WTA closes the option space. The claim is a statement about *learned*
policies. The experiment did not test it under conditions where it could express
itself (no learning -> no WTA). **Claim alignment: intact -- no pressure on INV-074.**

MECH-333 (critical-period open phase; v3_pending, implementation_phase v3) and
MECH-334 (critical-period closure / crystallization; v3_pending, EWC write-protect
IMPLEMENTED 2026-05-17): both depend on a functional differentiated policy that the
crystallize()/EWC machinery can act on. Neither was exercised (heads frozen-at-init;
EWC penalty never applied). Both remain candidate, untouched.

`claim_ids` accuracy: the trio is correctly tagged for what the experiment *intends*
to test; the run simply does not deliver interpretable signal for any of them, so
all three resolve to non_contributory (not per-claim split).

---

## 5. Biological-reference triage

INV-074's closest reference is **ocular-dominance critical-period plasticity**:
during the open window E/I balance enables competitive plasticity; after closure
(PNN/Lynx1/NgR1) configurations lock. Monocular deprivation is the direct analog of
monostrategy capture when the window never closes around the competing pathway
(Hubel & Wiesel 1970; Fagiolini & Hensch 2000; Clothiaux/Bear/Cooper 1991 BCM;
Achille/Rovere/Soatto 2019 critical periods in ANNs; Kirkpatrick 2017 EWC). Lit pull
already completed 2026-05-17 (4 subagents, lit_conf 0.82).

The biology is an existence proof for the **class** of mechanism: time-bounded
plasticity asymmetry IS necessary for diversity persistence in developing brains.
The reference mechanism has two non-negotiable preconditions: (a) a competitive
learning dynamic that WOULD collapse without closure, and (b) the closure mechanism
actually operating. This harness instantiates **neither**. The FAIL therefore matches
"what would happen if a known prerequisite were absent" -- a discovered/confirmed
prerequisite (a learned WTA-prone policy), NOT a falsification.

`is_formal_import`: no -- INV-074 is a biology-faithful translation, not a
formal-definition import. Demotion is off the table (universal invariant, biology
supportive, claim not under fair test). No new lit-pull warranted.

---

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | claim never allowed to express; no pressure on INV-074/333/334 |
| Biological reference | clear | OD-plasticity / BCM / critical-period-in-ANNs; existence proof for the class; lit already pulled |
| Developmental / dependency prerequisites | missing | requires a trained, WTA-prone policy; harness omits policy training |
| Implementation completeness | stub | symbol of crystallization present (`crystallize()` fires) but not its functional role -- frozen heads never trained, expansion never stepped, EWC penalty never applied |
| Environment adequacy | adequate-but-irrelevant | IGW-023 Phase-3 pressure landed; not the blocker for this run |
| Measurement adequacy | misleading | D1/D2 measure an untrained near-uniform action distribution that crystallization cannot move |
| Integration adequacy | n/a | -- |
| Scale / capacity | n/a | -- |

**Recommended run-level epistemic_category: `measurement_test_design_defect`** (the
harness omits policy training + crystallization exercise; the run is a non-test).
This is sharper than the claim-level `substrate_ceiling`, which is RETAINED on the
claims for the deeper retest story (see Section 8).

---

## 7. Lineage / convergent shape

This is the **7th** non_contributory crystallization-arm result for the
INV-074/MECH-333/MECH-334 trio:

| Run | Why non_contributory |
|---|---|
| 543h | gated policy inert (cross-machine common attractor); crystallize froze a collapsed policy |
| 543i | byte-identical runs landed opposite basins; basin selection nondeterministic |
| 543k | (lineage member) heads never differentiated |
| 543l | all diff-ON gated arms inert at escalated floor; heads never separated |
| 610a | control did not collapse (no env pressure) |
| 610b | control did not collapse (no env pressure); routed to test_bed_enrichment substrate |
| **610c** | **control did not collapse + crystallization a behavioral no-op -- policy never trained** |

**One structural property, not seven independent bugs:** across every variation
(env pressure present/absent, heads differentiated/inert, policy frozen/trained-in-
intent) **a functional, trained, WTA-prone policy has never actually been placed
under the crystallization mechanism.** The 543 sub-lineage failed because the heads
never *differentiated*; the 610 sub-lineage failed because (610a/b) the env supplied
no collapse pressure and (610c) the policy is never *trained at all*. The
crystallization-necessity claim has not yet been falsifiably tested.

---

## 8. Learning extracted + repair pathway

Learning:
- The 610-lineage env-ceiling diagnosis (610a/b) was incomplete; the env substrate
  fix (IGW-023) did not unblock the test because the blocker is harness-level.
- The crystallization machinery (`crystallize()` + EWC) is wired and contract-tested
  but is **behaviorally inert in any harness that does not train the policy and add
  the EWC penalty term to the loss**. A future evidence-grade run MUST step
  `expansion_parameters()` post-crystallization and add `residue_field.ewc_penalty()`
  to the loss, on top of a real policy-learning signal.
- A negative-control sanity (D3) passing while every discrimination criterion fails
  is, again, the substrate/test-design fingerprint -- here driven by the harness, not
  the substrate.

Repair pathway -- **/queue-experiment redesign -> V3-EXQ-610d** (same scientific
question, implementation fix -> alphabetic suffix; user-confirmed 2026-06-03):
1. Train the policy with a real advantage / REINFORCE update so winner-take-all
   monostrategy can emerge in the ARM_0 control (the precondition D2 measures).
2. Step `gated_policy.expansion_parameters()` post-crystallization and add
   `residue_field.ewc_penalty()` to the Phase-3 loss so MECH-333 (plasticity
   injection) and MECH-334 (EWC write-protect) are actually exercised in ARM_1.
3. Pre-register the substrate-ceiling fork: **if the trained-policy control STILL
   does not collapse** (SP-CEM main-path + MECH-313 noise floor + MECH-260 dACC +
   MECH-341 E3-score-diversity keeping entropy near-uniform), that is NOT a result
   against INV-074 -- it is positive evidence that the diversity-preservation
   machinery is robust enough that crystallization is unnecessary in this substrate,
   and should *strengthen* MECH-341/MECH-313 rather than weaken INV-074. This is the
   standing substrate-ceiling question the 543/610 lineage has been circling; it can
   only be reached once the harness actually trains the policy.

NOT implement-substrate: the env substrate (test_bed_enrichment) already landed and
is not the blocker; the new gap is harness-level. NOT lit-pull: biology clear,
already pulled 2026-05-17. NOT demotion: universal invariant, biology supportive,
claim not under fair test.

---

## 9. Recommended writes for /governance (do NOT apply here)

- **Manifest** `v3_exq_610c_inv074_crystallization_necessity_20260602T191404Z_v3`
  (flat + nested `runs/.../manifest.json`):
  - `evidence_direction: non_contributory` (all three claims; the run yields no
    interpretable signal for any of them)
  - `epistemic_category: measurement_test_design_defect`
  - `evidence_direction_note`: see recommended text below.
- **claims.yaml** INV-074 / MECH-333 / MECH-334: append the dated note below; retain
  `pending_retest_after_substrate=true`; retain claim-level
  `epistemic_category=substrate_ceiling`; NO confidence / flag / promotion change; NO
  de-weight (INV-074 not falsified).
- **review_tracker.json**: mark `v3_exq_610c_..._20260602T191404Z_v3` reviewed.

Recommended `evidence_quality_note` text (verbatim for governance to write):

> [2026-06-03 governance: V3-EXQ-610c non_contributory + measurement_test_design_defect
> (confirmed failure_autopsy_V3-EXQ-610c_2026-06-03)]: V3-EXQ-610c (crystallization-
> necessity retest, supersedes 610b) FAILed D1 (-0.013) and D2 (+0.047, below the 0.10
> floor) with both arms near-uniform (entropy 1.06-1.12 of 1.609 max). Root cause is
> HARNESS-level, not env-level: the experiment never trains the gated policy
> (`policy_optimizer.step()` is never called; REINFORCE is explicitly `pass`ed at lines
> 575-585), `crystallize()` freezes never-trained heads and the expansion optimizer is
> rebuilt but never stepped, and `ewc_penalty()` is never added to any loss. So
> crystallization is a behavioral no-op and INV-074's predicted winner-take-all
> monostrategy collapse is never instantiated -- D1/D2 are non-discriminative by
> construction. This supersedes the 610a/b env-ceiling reading (IGW-023 Phase-3 pressure
> landed and did not help because env pressure cannot collapse an untrained policy).
> 7th non_contributory crystallization-arm result (543h/i/k/l + 610a/b/c): one
> structural property -- a functional, trained, WTA-prone policy has never been placed
> under the crystallization mechanism. INV-074 (universal invariant, lit_conf 0.82) not
> weakened, no claim falsified; pending_retest_after_substrate retained;
> epistemic_category substrate_ceiling unchanged. Routed to /queue-experiment redesign
> V3-EXQ-610d: train the policy, step expansion_parameters + add ewc_penalty, with a
> pre-registered substrate-ceiling fork (a trained-policy control that still does not
> collapse strengthens MECH-341/MECH-313, not weakens INV-074).
