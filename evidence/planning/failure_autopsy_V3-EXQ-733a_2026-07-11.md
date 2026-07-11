# Failure Autopsy — V3-EXQ-733a (rebinding portfolio, MECH-456) — CLUSTER

- **Generated (UTC):** 2026-07-11T22:00:37Z
- **Scope:** cluster (2 legs of the V3-EXQ-733a GOV-FANOUT-1 portfolio)
- **Status:** confirmed (user-adjudicated interactive gate 2026-07-11)
- **Runs:**
  - P-A: `v3_exq_733a_rebinding_pA_survival_onboarded_20260711T100753Z_v3` (queue `V3-EXQ-733a-a`, machine ree-cloud-1)
  - P-B: `v3_exq_733a_rebinding_pB_directed_traversal_20260711T095846Z_v3` (queue `V3-EXQ-733a-b`, machine ree-cloud-2)
- **Claim:** MECH-456 (`entities.rebinding_under_perturbation`; candidate / v3_pending / substrate_conditional)
- **Both:** FAIL / self-stamped `evidence_direction=non_contributory` / `non_degenerate=True`, label `substrate_not_ready_requeue`
- **Recurrence context:** this 2-leg portfolio was the redesign PRESCRIBED by `failure_autopsy_V3-EXQ-733_2026-07-10` to fix that run's readiness-gate-unmet failure (cold agent dying in the lethal SD-054 env starved within-episode overtakes). Both prescribed legs again fail the readiness gate. **2nd MECH-456 non_contributory readiness autopsy → re-derive brake fires.**

---

## 1. Facts (both legs ran to completion; 6/6 seeds, no errors)

Neither is a mis-self-route of the V3-EXQ-642 kind (untrained-substrate masquerading as a ceiling). The self-routes are correct — the pre-registered readiness gate is genuinely unmet on both — but the two legs fail the gate for **structurally different reasons**, and one of them (P-B) passes every *mechanism* criterion.

### Leg P-A — survival-onboarded (training-regime axis), K=4 (G_PARTITION=2)

The only change vs V3-EXQ-733: the agent is survival-onboarded (`scaffolded_sd054_onboarding`, the validated 603m/603n recipe) before the functional test. The binder is still trained fresh in the test's own P0.

| Readiness precondition | measured | threshold | met |
|---|---|---|---|
| learned_binder_converged (worst loss_ema) | **4.159** | 3.535 | **NO** |
| region_coverage_adequate (min P0 region visits) | 13 | 10 | yes |
| overtake_events_adequate (min P1 overtakes/seed) | **14** | **20** | **NO** |

- **Survival onboarding worked as designed:** episodes now run the full ~200 steps (`onboard_p0_mean_episode_length=200`, all 6 onboard gates passed). The 733 cold-death cause is *gone*.
- **But overtakes stayed thin (min 14 < 20) — P-A's declared NULL fired.** Survival was not the (only) overtake lever.
- **Binder non-convergence on 2/6 seeds** (42, 43 sit at *exactly* the chance floor 4.1589 — the binder learned nothing discriminative). Seeds 44–47 converged (loss ~3.25–3.39).
- Region visits are grossly concentrated: seed 42 `[1563, 1926, 23, 13]`, seed 43 `[1457, 1915, 19, 23]` — the agent lives in 2 of the 4 regions.
- **DV1** true on 3/6 (44 misses at margin 0.02 < 0.10); **DV2** true on 4/6.

**Root:** a *competent* onboarded forager exploits the resource-rich reef band and stays put → (a) few region-boundary crossings ⇒ thin overtakes; (b) two regions get ~13–23 visits ⇒ thin, ill-defined prototypes ⇒ the binder collapses to the dominant regions and stalls at the chance floor. **Survival competence is antagonistic to the traversal this readout needs.** Fixing survival made overtake-generation *worse-conditioned*, not better.

### Leg P-B — directed-traversal teleport (test-bed / environment axis), K=16 (G_PARTITION=4)

The agent is the cold V3-EXQ-733 agent verbatim (no onboarding); only the test-bed changes: softened survival (`hazard_harm=0`), finer lattice (K=16), and a scripted teleport tour every `TRAVERSE_PERIOD=8` steps that persists across P0 and P1.

| Readiness precondition | measured | threshold | met |
|---|---|---|---|
| learned_binder_converged (worst loss_ema) | 3.235 | 3.535 | yes |
| region_coverage_adequate (min P0 region visits) | **9** | **10** | **NO** |
| overtake_events_adequate (min P1 overtakes/seed) | 62 | 20 | yes |

- Teleport decoupled P1 overtake-generation from survival: **overtakes 62–808/seed**; **binder converged 6/6**.
- **`dv1_pass=True` (6/6), `dv2_pass=True` (6/6), `both_pass=True`.** The binder tracks the true competitor ~3–6× above the region-label-shuffle control (`alignment_real` 0.16–0.44 vs `alignment_shuffle` ~0.06), and ON re-acquires **8–14 steps faster** than the FROZEN arm over the shared trajectory — on **every** seed. **This is the strongest affirmative rebinding signal to date.**
- **Sole blocker: `all_ready=False` because P0 region coverage min 9 < 10 — one region, one seed (43).**

**Root:** seed 43 *starved* in P0. `hazard_harm=0` removes contact death but energy/starvation death still fires (`done = health<=0`), and the teleport is a pure position read that does **not** advance/refill health — so it repositions the agent but cannot stop the episode ending. Seed 43's total P0 experience was ~545 step-visits vs ~4600 on seed 42 (8× thinner); on the finer K=16 lattice (3×3 cells/region) the agent drifts out of the teleported region within 1–2 moves, so the fixed absolute floor of 10 is **granularity-blind** and the thinnest region (9 visits) dips under it.

---

## 2. Adjudication — why does readiness recur on BOTH axes?

The user's question: is it P0 binder non-convergence, thin region coverage, or insufficient overtake generation? **Answer: all three, and they are one thing.** Both legs' failing readiness signals — P-A overtakes, P-A binder-convergence, P-B P0-coverage — trace to a single locus:

> **Every readiness measure remains coupled to the agent's foraging survival / spatial distribution, and competent foraging concentrates coverage.** Wherever the test-bed *forcibly decouples* a measure from foraging (P-B's P1 teleport → 62–808 overtakes, DV1/DV2 6/6), that measure clears cleanly. Wherever it doesn't (P-A overtakes; P-A binder prototypes; P-B's P0 prototype-build) it fails.

This is **not** the same failure mode recurring (733 was cold-death; P-A survival is fixed and it *still* fails, for a different reason — foraging concentration), and it is **not** N independent bugs. It is **one structural property of the test-bed**, expressed through whichever readiness channel is left survival-coupled.

**Two readings, and the cluster forces the choice:**

- **(A) Test-bed operationalisation ceiling** — the harness incompletely decouples P0 prototype-building from survival, and its coverage floor is granularity-blind. **CONFIRMED** by P-B's clean DV1/DV2 6/6 (the mechanism works when the readout is decoupled) and by P-A's null (fixing survival the *other* way — onboarding — doesn't help, because foraging competence concentrates coverage).
- **(B) MECH-456 mechanism ceiling** — rebinding genuinely can't track the true competitor. **REFUTED** by P-B DV1 6/6, DV2 6/6.

Exactly as the re-derive-brake note anticipated: **a 2nd non_contributory readiness recurrence implicates the TEST-BED operationalisation, not the mechanism and not another same-shape re-queue.**

---

## 3. Claim-layer mapping

MECH-456 (`claims.yaml`): mechanism_hypothesis, `entities.rebinding_under_perturbation`, status `candidate`, `epistemic_category: substrate_conditional`, `v3_pending: true`. `depends_on`: ARC-006, INV-002, MECH-045, MECH-269, MECH-270. `what_would_answer` requires BOTH (1) rebinding tracks the true competitor above a shuffle control (=DV1) AND (2) a graded, non-saturating behavioural consequence vs a frozen arm (=DV2).

Did the test let the claim express itself? **On P-B, emphatically yes — and the answer was affirmative on both conditions, on all 6 seeds.** The block is a P0-coverage precondition upstream of the DVs, not the DVs themselves. This must **not** demote MECH-456; it stays candidate / v3_pending (V3-pending gate), both legs unweighted (`non_contributory`).

`claim_ids` accuracy: correct (single tag MECH-456 per leg; `bears_on_not_tagged` = MECH-269, MECH-270, ARC-006, MECH-045, INV-002 — appropriate, untagged).

**Interpretable signal before any non_contributory call (skill requirement):**
- P-A is `non_contributory` *for MECH-456* but **contributory for the test-bed question**: it *falsifies* survival-onboarding as the readiness lever (its null fired) and reveals the antagonism between foraging competence and traversal coverage.
- P-B is `non_contributory` *as stamped* but carries a **near-decision-flipping positive** for MECH-456 (DV1/DV2 6/6). Per the confirmed framing, this is recorded so the recurrence is not misread as mechanism failure; it is expected to convert to SUPPORT on the test-bed-fixed retest.

---

## 4. Biological-reference triage

MECH-456's grounding is object-file updating (Kahneman/Treisman/Gibbs), serial-dependence hysteresis (Manassi & Whitney), PE-driven perceptual switching (Weilnhammer; Cole ACC), latent-cause inference (Gershman) — an E(τ)/stability grounding, explicitly **not** a formal-import (the coherence-C(τ) import was settled NO-CLAIM by V3-EXQ-725a and is excluded from MECH-456). No `/lit-pull` commission is owed; biology divergence is not the fault locus. The failure is a test-bed operationalisation gap.

---

## 5. Four-layer diagnosis (cluster)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (P-B), untested (P-A) | P-B: DV1 6/6, DV2 6/6 — binder tracks truth AND confers a graded advantage. P-A: readout never reached (overtakes/binder starved). Neither weakens MECH-456. |
| Biological reference | clear | non-formal-import; not the fault locus. |
| Developmental / dependency prerequisites | present | survival onboarding + binder substrate both exist and work; the fault is not a missing dependency mechanism. |
| Implementation completeness | complete (`ree_core` unmodified) | binder converges wherever coverage is adequate; harness-level measurement. |
| Environment adequacy | wrong pressures for the P0 readout | competent foraging concentrates coverage (P-A); softened-but-not-removed starvation truncates P0 (P-B). |
| Measurement adequacy | **partial — the fault locus** | `MIN_REGION_VISITS_P0=10` is granularity-blind (calibrated for K=4, applied to K=16); P0 coverage is not guaranteed by construction the way P1 overtakes are. |
| Integration adequacy | isolated | the binder works alone; the test-bed under-feeds its P0 prototype-build on survival-coupled channels. |
| Scale / capacity | adequate | P-B P1 shows the design generates 62–808 overtakes trivially once decoupled. |

**Recommended `epistemic_category`: `substrate_ceiling`** (test-bed-operationalisation flavour) — with the load-bearing qualifier that the blocking "substrate" is the **functional harness**, and the repair is a bounded, buildable test-bed change over an otherwise-working mechanism, **not** a deep neural-substrate build and **not** a park on the exhausted conversion ceiling.

---

## 6. Cluster pattern

| Experiment | Claim | Negative-control / readiness anchor | Discrimination criteria (DV1/DV2) | Read |
|---|---|---|---|---|
| P-A survival-onboarded (K=4) | MECH-456 | binder non-convergent 2/6 (chance floor); overtakes min 14<20 | DV1 3/6, DV2 4/6 (readout starved) | survival-fixing does NOT lift the readout; foraging concentration is antagonistic → **null fired** |
| P-B directed-traversal (K=16) | MECH-456 | overtakes 62–808 ✓, binder 6/6 ✓; **P0 coverage min 9<10** ✗ | **DV1 6/6, DV2 6/6, both_pass=True** | mechanism PASSES; blocked only by a granularity-blind, survival-coupled P0-coverage floor |

**Verdict: one structural property, not two independent bugs.** The load-bearing signal is the *contrast within P-B*: the P1 channel, which the test-bed forcibly decoupled from survival, clears by a wide margin and the DVs pass 6/6; the P0 channel, left survival-coupled, fails by one visit on one starved seed. P-A independently confirms the same law from the other side — decoupling survival by making the agent *competent* backfires because competence concentrates coverage. The fault is the incomplete decoupling of readiness from survival in the harness; the MECH-456 mechanism is refuted as the fault locus.

---

## 7. Learning extracted

- **Survival onboarding is the wrong lever for this readout, and counterproductive.** A competent forager exploits the reef band and stays put — suppressing both region-boundary crossings (overtakes) and non-reef-region prototype coverage (binder convergence). Fixing survival made two readiness channels worse.
- **The test-bed decouples P1 but not P0.** The teleport guarantees P1 overtakes by construction but is a pure position read; it cannot stop starvation truncating P0 episodes, so P0 prototype accumulation stays survival-coupled. On unlucky/starved seeds, P0 coverage dips below a floor that is itself granularity-blind (calibrated for K=4, applied to K=16 where per-region dwell is far smaller).
- **The MECH-456 mechanism works.** Under guaranteed events (P-B P1), the binder tracks the true competitor 3–6× above the shuffle control and confers an 8–14-step graded re-acquisition advantage over a frozen arm, on all 6 seeds. `what_would_answer` is affirmatively met on the decoupled channel; only a survival-coupled readiness precondition prevents it being counted.
- **Recurrence rule validated:** the 2nd non_contributory readiness result on one claim, with *different* proximate causes, points at the test-bed operationalisation, not the mechanism. It ends the survival-lever line of attack.

---

## 8. Routing (user-confirmed)

**Re-derive brake: FIRED** (2nd MECH-456 `non_contributory` readiness autopsy; prior: `failure_autopsy_V3-EXQ-733_2026-07-10`).

- **REFUSED:** re-queuing the **P-A survival-onboarding axis.** Its null fired and it is counterproductive (foraging concentration). A 3rd survival-onboarding letter would circle the same non-result — the brake forbids it.
- **Route → `/implement-substrate` on the FUNCTIONAL HARNESS (test-bed) substrate** (`complicated (buildable)`; GOV-FANOUT-1 **exempt** — the discrimination is already done, this is one unambiguous build): decouple P0 prototype-coverage from survival the same way P-B decoupled P1 overtakes —
  1. accrue a guaranteed clean per-region prototype sample **at teleport-time** (read the region at the directed-respawn cell, before drift), so P0 coverage is deterministic by construction;
  2. prevent starvation-death from truncating P0 episodes during the directed tour (respawn/refill or ignore health-`done` in the scripted-tour P0);
  3. scale `MIN_REGION_VISITS_P0` to lattice granularity K (or count at teleport-time so the floor is trivially met).
- Then **ONE** re-run of the P-B directed-traversal design (new letter, e.g. **V3-EXQ-733b**, `supersedes: V3-EXQ-733a`), tagged MECH-456. **This is permitted and is not a same-ceiling loop:** P-B already cleared DV1/DV2 6/6; the re-run only lifts a granularity-blind, survival-coupled precondition so the demonstrated near-PASS is counted. (Consumer-half note: `/queue-experiment` Step 2.5 must recognise this as the brake-permitted retest-after-substrate, gated on the harness build landing — not the forbidden survival re-queue.)

`evidence_direction` stays **non_contributory** for both legs (unweighted). `pending_retest_after_substrate = True`. MECH-456 remains **candidate / v3_pending**; the `hold_pending_v3_substrate` decision applied by the 2026-07-11 governance cycle stands.

### Draft `evidence_quality_note` (for /governance to write on MECH-456 — do not write here)

> V3-EXQ-733a 2-leg portfolio (the redesign prescribed by the 733 autopsy) again FAILed the pre-registered readiness gate → both legs `non_contributory`, not a rebinding verdict. Cluster autopsy 2026-07-11: the two legs fail for different proximate reasons that resolve to ONE structural property — every readiness measure stays coupled to the agent's foraging survival, and competent foraging concentrates spatial coverage. P-A (survival-onboarded): survival was fixed but overtakes stayed thin (min 14<20, its null fired) and the binder stalled at chance on 2/6 seeds because a competent forager over-visits 2 of 4 regions and starves the others. P-B (directed-traversal teleport): the decoupled P1 channel PASSED every mechanism criterion — DV1 6/6, DV2 6/6, both_pass=True, binder converged 6/6, overtakes 62–808/seed; the binder tracked the true competitor 3–6× above the shuffle control and re-acquired 8–14 steps faster than a frozen arm on all 6 seeds (the strongest affirmative rebinding signal to date). P-B was blocked ONLY by a granularity-blind, survival-coupled P0-coverage floor (min 9<10 on one starved seed). Re-derive brake fired (2nd non_contributory readiness autopsy): the survival-onboarding axis is REFUSED; routed to a bounded functional-harness fix (guarantee P0 per-region prototype samples at teleport-time / prevent starvation-truncation of P0 / scale MIN_REGION_VISITS_P0 to K), then a single P-B re-run (V3-EXQ-733b) expected to convert the P-B near-pass to counted SUPPORT. MECH-456 stays candidate/v3_pending; NOT a mechanism ceiling (P-B refutes that reading) and NOT co-blocked on the exhausted conversion ceiling.

---

## 9. Handoff

- `/implement-substrate` on the harness test-bed fix (recommended_substrate_queue_entry, action `create`, in the JSON artifact).
- Then `/queue-experiment` for **V3-EXQ-733b** (single re-run of the P-B design; brake-permitted retest-after-substrate; do NOT re-queue the P-A survival axis).
- A follow-up `/governance` run consumes this artifact: writes the `evidence_quality_note`, marks both 733a legs reviewed as `non_contributory`, creates the substrate_queue entry, no promotion/demotion of MECH-456.
