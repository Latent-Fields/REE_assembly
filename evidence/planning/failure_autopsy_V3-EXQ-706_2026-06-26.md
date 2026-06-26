# Failure Autopsy -- V3-EXQ-706 (MECH-314 curiosity-conversion, double-gated; pre-registered terminal of the 705 lineage)

- **Generated (UTC):** 2026-06-26T04:46:05Z
- **Scope:** single target (705 lineage); convergent-endpoint context shared with V3-EXQ-700c (see Section 9)
- **Status:** confirmed (user-adjudicated 2026-06-26 -- hold/reconsider -> 706b validity re-test)
- **Claim tagged:** MECH-314 (structured-curiosity conversion; candidate)
- **Outcome:** FAIL -- self-routed `conversion_ceiling_persists_despite_double_gating` -- evidence_direction `non_contributory`
- **Machine:** ree-cloud-3
- **Run:** `v3_exq_706_mech314_curiosity_conversion_double_gated_20260626T015604Z_v3`
- **Supersedes:** V3-EXQ-705b

---

## 1. Facts -- reconstruction (no interpretation)

706 is the **brake-EXEMPT double-gated re-test** the confirmed `failure_autopsy_V3-EXQ-705b_2026-06-25` pre-registered: 705b ran with only the MECH-448 demotion gate; the autopsy's correction was that the conversion needs the BUILT MECH-449 Go/No-Go eligibility constitution composed with it. 706 turns BOTH on (`use_f_eligibility_demotion=True` AND `use_go_nogo_constitution=True`) plus an active staleness/perseveration No-Go so the second gate genuinely fires, with MECH-314 curiosity the SOLE modulatory channel arbitrating the within-eligible argmin.

3 arms x 3 seeds, phased P0/P1, reef-bipartite foraging, GAP-A `e2_world_forward` divergent pool, adaptive floor ON. Arms: ARM_CURIOSITY (w=0.25) / ARM_FONLY (w=0, double-gated F-only control) / ARM_NOISE (w=0, flat-hot temperature 2.5).

### Readiness -- all 5 legs MET (manifest)

| leg | metric | measured | floor | met |
|---|---|---|---|---|
| A | GAP-A pool divergence (cand_world_pairwise_dist) | 0.0768 | 0.02 | yes |
| B | curiosity_bias_range at non-saturation arm (w=0.25) | 0.00278 | 0.0001 | yes (590c confound fixed) |
| C | f_eligibility demotion excluded_count | 22.69 | >0 | yes |
| D | rolled-out z_world magnitude bounded | 0.200 | < 1e6 | yes |
| E | **Go/No-Go n_soft_applied (gate non-degeneracy)** | **7.05** | >0 | yes |

### Load-bearing criterion -- FAILED

`mech314_committed_diversity_lift_over_double_gated_f_only_and_noise` (non-degenerate per `criteria_non_degenerate`): **passed = false**.

Per-arm committed-class entropy (mean): ARM_CURIOSITY **1.013** / ARM_FONLY **0.970** / ARM_NOISE **0.970**. Lift over F-only on the margin (0.05): **1/3** seeds; strict-above-noise: 2/3 seeds. PASS required >=2/3 on BOTH.

### Failed criterion type

Discrimination (the lift criterion), but with two **validity gaps** surfaced on deeper inspection (Section 5) that demote this from a clean terminal ceiling to a not-yet-fair test.

---

## 2. Per-seed reconstruction (the scrutiny the "hold/reconsider" decision called for)

| seed | ARM_CURIOSITY | ARM_FONLY | ARM_NOISE | lift (CUR-FONLY) | P1 ticks (CUR / FONLY) |
|---|---|---|---|---|---|
| 42 | 1.398 | 1.387 | 1.387 | +0.012 | 3997 / 3967 |
| 43 | 0.693 | 0.699 | 0.699 | -0.006 | 5400 / 5400 |
| 44 | 0.947 | 0.826 | 0.826 | **+0.121** | **545 / 344** |

Two facts the aggregate hides:

1. **The matched-noise control is degenerate.** ARM_NOISE (temperature 2.5) is **byte-identical to ARM_FONLY** (temperature 1.0) on all three seeds -- same entropy, same committed-class counts. Raising softmax temperature changed nothing, because committed-class entropy is decoupled from temperature by the eligibility constitution. This is the **exact MECH-313 temperature-decoupling the 700b autopsy diagnosed**, recurring on the curiosity test. The C1 "strict-above-noise" leg is therefore vacuous (though it is NOT the binding failure -- the noise==F-only equality made it the easier leg, 2/3).
2. **The only "passing" seed is the least-sampled.** The single seed clearing the margin (44, +0.121) ran ~545/344 P1 ticks vs ~4000-5400 for seeds 42/43, so its entropy estimate is noisy and its committed-class counts are small ({0:318, 2:149, 4:78}). The two WELL-sampled seeds (42, 43) are flat/negative.

---

## 3. Claim-layer mapping

MECH-314 asserts the structured-curiosity channel adds committed-action-class diversity. 706 was intended as the first fully-fair test under BOTH composed eligibility gates. The readiness legs all passed and the Go/No-Go gate genuinely fired (legE 7.05). **But the load-bearing comparison was not validly instrumented:** its noise leg used a degenerate temperature control, and its margin verdict turned on a single under-sampled seed. So 706 does not cleanly establish a fair ceiling. MECH-314 is **not falsified** (the well-sampled seeds being flat is suggestive of a ceiling, but the test has a measurement-validity gap). MECH-314 stays `candidate`, unweakened, `pending_retest_after_substrate`. The self-route `non_contributory` is SOUND; its LABEL (`...persists_despite_double_gating` = pre-registered TERMINAL) is **corrected** to "re-test for validity" (the self-route is a hypothesis, not a verdict -- the readiness legs all passed mechanically but the C1 noise control and seed budget were not fair).

---

## 4. Biological-reference triage

Closest reference: frontopolar / rostrolateral-PFC uncertainty-driven curiosity (the behavioural-diversity generation pathway, ARC-065). Curiosity in real brains drives *exploration*; the *conversion* of that drive into committed-action-class diversity is gated downstream by segregated BG loops (and the Go/No-Go eligibility constitution, MECH-449). The 706 result is consistent with the conversion being gated upstream of the single selection face, but the test cannot yet decide it (degenerate null + seed imbalance). Biological reference: **clear**; not a falsification.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | MECH-314 not falsified; well-sampled seeds flat is suggestive but not validly established |
| Biological reference | clear | curiosity drives exploration; conversion gated by segregated BG loops + Go/No-Go |
| Prerequisites | present + composed | BOTH eligibility gates genuinely active (demotion excluded 22.7; Go/No-Go suppressed 7.05) |
| Implementation | complete (for what was armed) | demotion + adaptive floor + Go/No-Go correct; curiosity channel correct |
| Environment | adequate | GAP-A divergent pool 3/3 |
| Measurement | **ROOT** | (a) matched-noise control degenerate (ARM_NOISE==ARM_FONLY, temperature-decoupled -- the 700-lineage null shape); (b) severe per-seed P1-budget imbalance (~545 vs ~5400) so the one "passing" seed is the noisiest |
| Integration | double-gated | both selection-face eligibility gates composed -- but the validity gaps block a clean read |
| Scale | imbalanced | total budget adequate but per-seed termination rates wildly unequal -> noisy per-seed verdict |

**Dominant diagnosis:** measurement / test-validity ROOT (degenerate noise control + seed-budget imbalance). Recommended `epistemic_category`: NO CHANGE (MECH-314 stays as-is). Recommended `evidence_direction`: `non_contributory`, `pending_retest_after_substrate`.

---

## 6. Re-derive brake -- NOT FIRED (brake-lock recorded)

Mechanically the brake would fire on a CLEAN ceiling (this would be the 7th MECH-314 substrate_ceiling/non_contributory autopsy; 705b was the pre-registered 6th brake-lock trigger). **It does NOT fire here**: 706 is not the fair-and-still-ceilinged terminal test it self-reported as -- the matched-noise control is degenerate and the margin verdict turns on an under-sampled seed. By the same logic that exempted V3-EXQ-705 (not 705b), an invalid-precondition / not-yet-fair self-route does not fire the brake.

**Brake-lock recorded:** the NEXT MECH-314 result with a VALID non-temperature noise control AND balanced per-seed budget that still shows no curiosity conversion FIRES the brake and routes to V4 ARC-110 loop-segregation with no further V3 letters. 706b is the one validity-fixed letter the lock permits.

---

## 7. Learning extracted + routing (user-adjudicated 2026-06-26: 706b validity re-test)

**Learning:**
1. A temperature/flat-hot noise control is degenerate for a committed-class-entropy DV -- it is byte-identical to the F-only arm because the eligibility constitution decouples temperature from committed-class diversity (the same MECH-313 lesson the 700 lineage learned). A valid curiosity-conversion null must be a same-layer / non-temperature perturbation.
2. Episodes terminate at very different rates per seed on this substrate (545 vs 5400 P1 ticks), so a fixed episode budget yields a wildly imbalanced per-seed tick budget; the verdict must be on a balanced (or tick-capped) budget, else the noisiest seed dominates the margin test.

**Routing: `/queue-experiment` V3-EXQ-706b (validity-fixed re-test; brake-exempt).**
- Equalise per-seed P1 measurement budget (tick-cap or balanced-episode termination) so no single under-sampled seed dominates the margin verdict.
- Replace the degenerate temperature noise control with a VALID non-temperature control (a same-layer perturbation, mirroring the 700-lineage same-layer-null direction; magnitude-matched to the curiosity channel's realised bias range -- avoid the 700c overshoot).
- Keep the double-gated design (demotion + Go/No-Go both ON, curiosity sole modulatory channel, GAP-A pool, adaptive floor, committed-action-class entropy DV).
- `claim_ids=[MECH-314]`; `experiment_purpose=evidence`; PROMOTES NOTHING.
- Pre-register 706b as **terminal for the validity question**: a valid, seed-balanced double-gated test that still shows no curiosity conversion escalates to V4 ARC-110 (no more V3 letters) -- this trips the brake-lock.

**`recommended_substrate_queue_entry.action = amend`** (target `v4_loop_segregation`) -- additive bookkeeping ONLY: (a) record 706 as a `failure_record` / `metric_trajectory` data point to preserve the convergent-endpoint signal (Section 9); (b) add `MECH-314` to the entry's `unblocks_claims` (currently `[MECH-439, ARC-108, MECH-450, ARC-110]`) since the curiosity-conversion lineage now also routes to loop-segregation as its escalation. This does NOT change the entry's `ready=false` / gated status and does NOT force the build; the immediate routing is the 706b re-test. No new substrate is required for 706b (MECH-449 is built+validated 689g; the fix is to the experiment's null + seed budget).

**Demotion threshold NOT reached.** MECH-314 stays candidate, unweakened, `pending_retest_after_substrate`.

---

## 8. Draft `evidence_quality_note` (for governance to write -- do not write here)

> V3-EXQ-706 (MECH-314 curiosity-conversion DOUBLE-GATED: MECH-448 demotion + the BUILT MECH-449 Go/No-Go both ON, curiosity sole modulatory channel; supersedes V3-EXQ-705b) FAIL / non_contributory. All 5 readiness legs met (GAP-A pool divergent 0.077; demotion excluded 22.69; Go/No-Go genuinely suppressed 7.05) and the load-bearing committed-class-entropy lift over the double-gated F-only control failed (1/3 seeds at margin 0.05; CUR 1.013 ~ FONLY 0.970 ~ NOISE 0.970). Autopsy 2026-06-26 (the manifest's pre-registered TERMINAL label is corrected to re-test): two validity gaps -- (1) the matched-noise control is degenerate (ARM_NOISE temperature 2.5 byte-identical to ARM_FONLY on all seeds; committed-class entropy is temperature-decoupled by the eligibility constitution, the 700-lineage MECH-313 null shape), and (2) severe per-seed P1-budget imbalance (~545 vs ~5400 ticks) means the one seed clearing the margin (44, +0.121) is the noisiest while the two well-sampled seeds (42/43) are flat/negative. non_contributory; MECH-314 UNWEAKENED (well-sampled seeds flat is suggestive of a ceiling but not validly established). Re-derive brake NOT fired (not-yet-fair test, not a clean ceiling); brake-LOCK recorded (next valid seed-balanced non-temperature-nulled no-lift fires it -> V4 ARC-110, no more V3 letters). Routing: /queue-experiment 706b with equal per-seed budget + a valid non-temperature (same-layer) noise control (brake-exempt validity fix); recommended_substrate_queue_entry amend = additive trajectory record + add MECH-314 to unblocks_claims on the gated v4_loop_segregation entry (does not un-gate). No promotion/demotion; pending_retest_after_substrate.

---

## 9. Convergent endpoint (cross-claim signal -- user-directed to record)

V3-EXQ-706 (curiosity-conversion lineage; MECH-314) and V3-EXQ-700c (settling-conversion lineage; MECH-439/ARC-108/MECH-450) -- autopsied the same session -- both ultimately point to **V4 ARC-110 loop-segregation** as the escalation, reached from structurally different mechanisms. They are NOT a cluster by failure shape (706 = degenerate temperature null + seed-imbalance; 700c = magnitude-mismatched same-layer null), but they share a **measurement lesson that IS the convergent signal**:

> On the V3 single foraging arena, neither conversion test could furnish a VALID committed-class null. 706's temperature null was byte-identical-inert (ARM_NOISE == ARM_FONLY); 700b's temperature null was decoupled-inert; 700c's same-layer null was magnitude-mismatched (41x). The committed-class-entropy DV is decoupled from temperature/scale-mismatched perturbations by the F-bounded eligibility constitution -- a valid null must be a same-layer, magnitude-matched perturbation, and even that is hard to calibrate on one arena.

This independently strengthens the 700b "single arena is the binding constraint" argument: it now holds across BOTH the curiosity and settling conversion routes. Each lineage gets ONE validity-fixed V3 letter (706b / 700d) before the V4 jump; if either's validly-nulled, seed-balanced re-test still shows no conversion, that is the decisive escalation to ARC-110. Recorded as a `failure_record` trajectory point + a `MECH-314` `unblocks_claims` addition on the gated `v4_loop_segregation` substrate entry (additive; does not un-gate).
