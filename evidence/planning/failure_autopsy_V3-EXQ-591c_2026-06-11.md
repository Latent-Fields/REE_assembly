# Failure Autopsy — V3-EXQ-591c

**Generated:** 2026-06-11T00:23:46Z
**Scope:** single
**Status:** confirmed (user-adjudicated)
**Target:** `v3_exq_591c_isef005_curriculum_phase_advance_readiness_diversity_20260610T225515Z_v3`
**Predecessor autopsy:** `failure_autopsy_V3-EXQ-591b_2026-06-10`

---

## Verdict in one line

Claim-free, contributory, **not a falsification**. Arming the exploration-diversity stack
at landed-default magnitudes does **not** rescue the worst-case early-collapse seed — the
ARC-065 exploration substrate is load-bearing but under-powered at default strength. Routing:
**Q-043 magnitude sweep first** (`/queue-experiment`), substrate evidence **amended to ARC-065**,
seed-45 gate brittleness flagged as an **ARC-046** follow-on.

---

## 1. Facts (no interpretation)

- **Manifest:** outcome FAIL, `experiment_purpose: diagnostic`, `claim_ids: []`,
  `evidence_direction: does_not_support`, `architecture_epoch: ree_hybrid_guardrails_v1`.
- **Design:** Phase 0->1 reachability under the diversity stack ARMED — MECH-313 noise-floor
  (`noise_floor_alpha=0.1`) + MECH-314 curiosity (`curiosity_weight=0.05`) ON at landed
  defaults; SP-CEM main-path default-on. 5 seeds (42-46), 160 ep, 200 steps/ep, grid 12,
  `phase_0to1_threshold=0.993963`, `h_pos_frac_of_max=0.20` (the 2026-05-31 recalibration
  from 0.70). InfantCurriculumScheduler arm.
- **Precondition (gate validity):** `early_policy_produces_nontrivial_h_pos` — measured
  `max_h_pos=2.4849` vs floor 0.2 → **MET**. The FAIL is a real verdict, not a non-moving artifact.

| seed | final phase | advanced @ ep | genuine exploration | h_pos_mean | h_pos_max | eligible>=thr |
|------|-------------|---------------|---------------------|-----------|-----------|---------------|
| 42 | 1 | 104 | yes | 0.5621 | 1.8384 | 7 |
| 43 | 1 | 114 | yes | 0.3226 | 1.3118 | 6 |
| 44 | 1 | 100 | yes | 0.8424 | 2.4849 | 36 |
| 45 | 1 | 142 | **no** | 0.1404 | 1.4530 | 2 |
| 46 | **0** | — | **no** | **0.0375** | 0.6899 | 0 |

- **Failed criteria:** C1_all_reach_phase1 (load-bearing) = **false** (4/5; seed 46 stuck at
  Phase 0). C_all_advanced_genuinely_explored (non-vacuity) = **false** (seed 45 advanced
  without genuine exploration). Self-route label:
  `phase01_collapse_persists_under_diversity_needs_gate_change`.

## 2. Two distinct signals

1. **Seed-46 collapse persists (load-bearing).** Seed 46 has `h_pos_mean=0.0375` here with
   the diversity stack **ON** — *identical* to the 591b value with the stack **OFF**. Arming
   MECH-313 + MECH-314 at landed-default magnitudes does not move the worst-case seed off a
   near-stationary attractor. The collapse is reproducible and magnitude-robust across the
   arming toggle.
2. **Seed-45 gate permissiveness (new vs 591b).** Seed 45 reached Phase 1 with a near-stationary
   policy (`h_pos_mean=0.140 < 0.2`) that fluked the threshold on only 2 eligible episodes. The
   single-episode-crossing Phase 0->1 gate criterion is too permissive.

## 3. Claim-layer mapping

`claim_ids: []` — no claim is weighted. This is substrate instrumentation for the
InfantCurriculumScheduler (ARC-046) Phase-0 gate and the ARC-065 exploration-diversity
substrate. **No claim can be demoted or promoted by this run.** The constructive content is
about substrate strength, not claim truth.

## 4. Biological-reference triage

- **Closest mechanism:** early developmental motor exploration / infant motor babbling driven
  by intrinsic motivation (dopaminergic novelty, LC-NE tonic arousal, frontopolar exploration).
- **Formal-definition import?** Partly — MECH-314 curiosity is an EFE / information-gain analog;
  MECH-313 is an LC-NE / SAC-max-entropy analog. Biologically motivated, but the **as-landed
  default magnitudes** are too weak to reproduce the strong, active intrinsic drive of real
  early development for the collapse-prone seed.
- **Missing-dependency signature?** Yes. The persistent collapse resembles what happens when
  intrinsic exploratory drive is too weak relative to a strong early attractor (a behavioral
  collapse / learned-helplessness shape). In biology the fix is *stronger active exploration*,
  which maps onto the magnitude lever (Q-043) and, if that fails, active Phase-0 shaping —
  **not** a lower competency-advance bar.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | not applicable (claim-free) | substrate-readiness diagnostic; no claim weighted |
| Biological reference | partial | active intrinsic drive; default passive noise+curiosity under-powered |
| Prerequisites / dependency | present but underpowered | MECH-313 + MECH-314 landed & main-path; gap is magnitude not module |
| Implementation completeness | partial | symbol-of-mechanism present; functional role (guarantee Phase-0 escape) unmet at default strength |
| Environment adequacy | adequate | standard 12x12 nursery; seeds 42-44 explore freely |
| Measurement adequacy | under-instrumented | single-episode-crossing gate admits a non-exploring seed (seed 45) — ARC-046 K-of-N/EMA follow-on |
| Integration adequacy | not applicable | — |
| Scale / capacity | adequate | seed 46 stays collapsed across full 160-ep budget — genuine, not under-training |

**Recommended epistemic_category:** `not_applicable_claim_free_diagnostic`.

## 6. Learning extracted

1. Arming MECH-313 + MECH-314 at **landed default magnitudes** does NOT rescue the worst-case
   collapse seed (seed 46: 0.0375 stack-off in 591b *and* stack-on in 591c). The default-magnitude
   ARC-065 substrate is insufficient for the collapse-prone seed tail — positive evidence that
   ARC-065's exploration substrate is load-bearing for curriculum Phase-0 escape.
2. New second signal: seed 45 advanced without genuine exploration → the single-episode-crossing
   Phase 0->1 gate is too permissive (independent ARC-046 gate-robustness follow-on).
3. Converges with / strengthens 591b: the residual collapse is an UPSTREAM exploration-diversity
   **strength** gap (ARC-065 / behavioral_diversity_isolation lineage) surfaced by the gate, not
   a gate-threshold defect. Lowering the threshold is explicitly NOT the route.
4. The fix forks cheaply: the **Q-043 magnitude sweep** discriminates "substrate needs stronger
   default config" from "substrate needs an active Phase-0 exploration-shaping mechanism" before
   any expensive new substrate is committed.

## 7. Repair pathway (user-confirmed)

- **Primary — `/queue-experiment`: Q-043 magnitude sweep.** Scale `noise_floor_alpha` (0.1) and
  `curiosity_weight` (0.05) above landed defaults; pre-register whether seed 46 escapes Phase 0.
  PASS (rescued) → substrate needs stronger default magnitudes (config-only); FAIL (still
  collapses) → active Phase-0 exploration-shaping substrate required. No gate-threshold change.
- **Secondary — substrate_queue `amend` on ARC-065.** Append the 591b+591c default-magnitude
  insufficiency `failure_record` so the substrate's evidence trail is complete; resolution forks
  on the Q-043 result.
- **Note — ARC-046 gate-robustness follow-on** for the seed-45 brittleness (K-of-N / EMA crossing
  criterion replaces the single-episode crossing).

## 8. Draft `evidence_quality_note` for governance

> V3-EXQ-591c (claim-free curriculum Phase 0->1 reachability diagnostic; diversity stack ARMED
> — MECH-313 noise-floor + MECH-314 curiosity at landed defaults, SP-CEM main-path). FAIL: C1
> (all 5 seeds reach Phase 1) 4/5 — seed 46 never escaped Phase 0 (h_pos_mean 0.0375, identical
> to 591b stack-OFF), so arming the diversity stack at landed-default magnitudes does NOT rescue
> the worst-case early-collapse seed. Reproducible, magnitude-robust across the arming toggle →
> ARC-065's exploration-diversity substrate is load-bearing but under-powered at default
> magnitudes (converges with + strengthens failure_autopsy_V3-EXQ-591b_2026-06-10). Second,
> independent signal: seed 45 advanced to Phase 1 without genuine exploration (h_pos_mean 0.140
> < 0.2, 2 crossings) → single-episode-crossing Phase 0->1 gate (ARC-046) too permissive (K-of-N
> / EMA follow-on). NOT a claim falsification (claim-free) and NOT a gate-threshold defect;
> lowering the threshold is explicitly NOT the route. Pre-registered next lever is the Q-043
> magnitude sweep (scale noise_floor_alpha + curiosity_weight above defaults) BEFORE any active
> exploration-shaping substrate work.

## 9. Routing

`routing: queue-experiment` (Q-043 magnitude sweep) + substrate_queue `amend` on ARC-065 +
ARC-046 gate-robustness note. Governance applies; this skill produced the diagnosis only.
