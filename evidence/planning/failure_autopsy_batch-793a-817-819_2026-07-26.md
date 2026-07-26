# Failure Autopsy — Batch: V3-EXQ-793a / 817 / 819 (2026-07-26)

Generated: `2026-07-26T11:32:51Z` · scope: batch · status: confirmed (user-adjudicated 2026-07-26)

## Scope

Five FAILs sat in `pending_review.md` on 2026-07-26. **816 + 820 already carry a
confirmed cluster autopsy** (`failure_autopsy_816-820-policy-decomposition-cluster_2026-07-26`,
routed to the 816b/816c GOV-FANOUT-1 portfolio) and only linger in `pending_review`
because `/failure-autopsy` does not mark runs reviewed — that is governance's loop.
**No flagged/vacuous diagnostic PASSes exist** (the only unclaimed PASS, V3-EXQ-823, is a
clean `supports` consumer run). Genuine autopsy debt = the three distinct targets below.

All three ran to completion (FAIL); all carry a complete always-core recording payload
(`substrate_hash`, `config`, `seeds`, `machine_class`, `elapsed_seconds`) — **no recording
gap**.

**Cross-cutting meta-observation** (not a formal single-claim cluster): two of the three
(817, 819) are cases where the run's own self-route/precondition label **misnames the cause**.
In both, the substrate *was* trained; the real fault is an ineffective training **objective**
(817) or a mis-calibrated non-vacuity **gate** (819) — the canonical "the self-route is a
hypothesis, not a verdict" pattern (V3-EXQ-642).

---

## Target 1 — V3-EXQ-793a · SD-049 · decisive robustness FAIL

**Run:** `v3_exq_793a_sd049_arm2_competence_repower_20260724T123828Z_v3` · ree-cloud-4 ·
~37.7 h / 24 curriculum cells · seeds 42–47 · non_degenerate **True**.

### Facts
Repowers 793 exactly per the 793 autopsy's repair pathway: n=3→6 seeds, and `guard_pass`
made **load-bearing** via a new `C_JOINT_ROBUST` gate. The 2×2 (curriculum × density):

| Arm | d3_clears | guard_pass_frac |
|---|---|---|
| A00 base/OFF | false (reproduces 693a ceiling, mean contact 0.0195 < 0.02) | 5/6 |
| A10 amended/OFF | true | 5/6 |
| A01 base/ON | true | 3/6 (0.5) |
| **A11 amended/ON (joint)** | **true** (d1=1.0, d2=1.0) | **3/6 (0.5)** |

The sole load-bearing criterion **`C_JOINT_ROBUST` FAILED**: A11 `guard_pass_frac = 0.5`
(3/6 seeds) vs the `MIN_FRACTION = 2/3` floor — short by one seed. The three guard failures
(seeds 43/44/47) are the low-baseline seeds whose `z_goal_norm_at_contact_peak` sits just
under the 0.4 gate (0.372 / 0.360 / 0.391). The four informational criteria all passed
non-degenerately.

### Four-layer diagnosis
| Layer | Status |
|---|---|
| Claim alignment | intact — decisive for the narrow lever-robustness question; **does not lift SD-049's park** (foraging-competence prerequisite, separate `/implement-substrate` route) |
| Biological reference | partial — goal-latching at contact (z_goal norm) under-develops on hard seeds |
| Prerequisites | present |
| Implementation | complete — did exactly what the 793 autopsy asked |
| Environment | adequate |
| Measurement | adequate — `C_JOINT_ROBUST` discriminated cleanly; the earlier arm-level `d3_clears` that hid per-seed guard failures is now fixed |
| Scale | adequate — n=6 sufficient to detect the fragility |

### Re-derive brake — DOES NOT FIRE
SD-049 carries **4 prior confirmed `substrate_ceiling` autopsies** (514l, 538a, 693, 693a),
past the threshold of 2. But under **R3 only `substrate_ceiling` readings count**, and this
reading is **`standard`** (a decisive, non-degenerate robustness FAIL). The brake does not
fire; this autopsy answers a *different* (lever-robustness) question, not the parked ceiling.

### Routing — **governance (record finding; NO re-queue)** [user-confirmed]
Record the decisive finding. The design implication — a future **693b must address the
z_goal-at-contact guard fragility on hard seeds** before receiving this config as a robust
hand-off — is noted but **not queued now** (queuing another SD-049 letter risks circling the
ceiling; SD-049's real park is the foraging scaffold). `epistemic_category: standard`,
`evidence_direction: inconclusive`.

---

## Target 2 — V3-EXQ-817 · SD-080 / SD-004 · self-route is a MISNOMER

**Run:** `v3_exq_817_sd080_consequence_grounding_falsifier_20260725T204837Z_v3` · Mac ·
seeds 0–4 · non_degenerate **False** · self-route `substrate_not_ready_requeue`.

### Facts — the substrate WAS trained
Three arms: ARM_0 (frozen head baseline = the SD-080 defect), ARM_1 (consequence-grounded:
train `action_object_head` to predict `z_world` delta with a frozen encoder), ARM_2 (shuffled
control). The **grounding gate failed** — both ARM_1 readiness preconditions:

- `arm1_ao_state_dependence_acquired` (M5 r² **0.98247** vs ceil 0.95, direction upper — r²
  did not drop enough) → **not met**
- `arm1_ao_consequence_structure_acquired` (M6 within-pair spearman **0.08490** vs floor 0.15
  — did not rise enough) → **not met**

**But the head demonstrably trained**: ARM_1 `M0_action_object_head_param_delta_l2_from_frozen`
≈ **1.3–1.47** (0.0 is the ARM_0/frozen value), grounding loss converged ~0.02 → ~1e-5. So
`substrate_not_ready` is a **misnomer** — the substrate trained; the **delta-prediction
objective was ineffective** at inducing state-dependent, consequence-structured geometry.
M6 has high inter-seed variance (0.011 / 0.251 / 0.088 across seeds 0/1/2 — seed-1 *cleared*
the floor). `grounding_took=false` blocked the behavioural (load-bearing) discrimination, so
the falsifier could not run → **non_contributory** for both claims.

### ⚠ Factual error in SD-080's existing note (flagged for governance) [user-confirmed]
SD-080's `evidence_quality_note` (`docs/claims/claims.yaml` ~line 51015) states
*"did not move the AO head (delta_l2_from_frozen = 0.0), so ARM_1 collapsed onto ARM_0"* —
the manifest **contradicts** this (Δ ≈ 1.3–1.47; 0.0 is ARM_0). Governance should correct the
note to say the head trained but the objective did not move the M5/M6 representational DVs.

### Four-layer diagnosis
| Layer | Status |
|---|---|
| Claim alignment | SD-080 intact (frozen-random-projection defect already **confirmed by V3-EXQ-809**; 817 does not re-test it); SD-004 intact/untested (gate blocked the behavioural read) |
| Biological reference | partial — SD-004 specifies O as a *learned* consequence-structured compression |
| Prerequisites | **missing** — a consequence-grounding training objective that actually induces the geometry (SD-080's whole point) |
| Implementation | partial — objective built and trained the head, but ineffective |
| Measurement | under-instrumented / mis-calibrated — M5/M6 absolute thresholds vs high seed variance |

### Routing — **queue-experiment 817a** [user-confirmed]
Re-queue **817a** with a **stronger/different grounding objective** (e.g. a contrastive
consequence loss) **and recalibrated M5≤0.95 / M6≥0.15 thresholds** given the seed variance.
SD-080's defect stays confirmed (via 809); 817 adds no direction.
`epistemic_category: competence_implementation_gap` (secondary
`measurement_test_design_defect`), `evidence_direction: non_contributory` (both).

---

## Target 3 — V3-EXQ-819 · MECH-457 / INV-088 · flagged `precondition_unmet`

**Run:** `v3_exq_819_mech457_inv088_zworld_trained_vs_random_20260726T005930Z_v3` · cloud ·
seeds 42/43/44 · non_degenerate **False** · self-route `zworld_advantage_grid_nondiscriminative`
· adjudication `precondition_unmet`.

### Facts — the "not ready" is a misnomer, and the gate contradicts the router
The flagged precondition **`post_bc_install_took`** is met=false on **both** arms under the
**worst-seed** rule (min post-BC foraging competence vs the 1.0 floor): trained **0.9** (worst
seed 43), random **0.4**. That set `non_degenerate=false`, which vacated the run.

**But the z_world encoder DID train** (3/3 seeds, `world_encoder_max_abs_delta` 0.277–0.333) —
the V3-EXQ-780 *frozen random projection* fault is **fixed** (upstream substrate
`sd_zworld_warmup_optimizer_group`, ree-v3 `b523b9c70a`, validated 25a69fcd4c). The failing
precondition is a competence floor, **not** an encoder-training check.

**Internal contradiction (the load-bearing finding):** the routing predicate
`advantage_confirmed` uses **strict-majority** install (trained 2/3 → True, random 0/3 →
False) → asymmetric install → `advantage_confirmed = **true**` (and `headline.advantage_confirmed`
IS true). The **worst-seed non-vacuity gate vacated a run the strict-majority router would
have PASSed**, on a single seed-43 0.1 near-miss (0.9 vs 1.0). The precondition's own docstring
declares it *"NON-vacating per-arm"*, yet the aggregate gate vacated both arms.

Anchors were reachable (local_view_greedy D3 **48.05**, greedy_oracle **57.2**, all 3 seeds
supra-floor) — the env is provably floor-achievable; the z_world arms simply forage near-floor
(~2% of ceiling) within a solvable env.

### Four-layer diagnosis
| Layer | Status |
|---|---|
| Claim alignment | MECH-457 untested (vacated); INV-088 untested (precondition blocked; governance-downstream) |
| Prerequisites | present — encoder now trains (780 fault fixed) |
| Implementation | complete for the encoder; **defective for the non-vacuity gate** (contradicts the strict-majority router and its own per-arm-non-vacating docstring) |
| Environment | adequate — anchors reachable |
| Measurement | **test_design_defect** — the load-bearing paired-advantage DV never scored; gate and router disagree on the same data |
| Scale | under-powered for a worst-seed rule (n=3; one seed vacates the run); the 1.0 effect margin is large vs the 0.35–2.4 competence range |

### Weak (unscored) directional signal
A prediction-trained z_world lifts installed competence only from AUC **0.46 → 0.90** (mean
paired advantage **+0.442**, **0/3** seeds over the 1.0 margin; still ~2% of the achievable
ceiling) — mild, non-load-bearing support for MECH-457's thesis that encoder quality alone
does not confer competent action. Recorded, not read as confirming.

### Re-derive brake — DOES NOT FIRE
Under **R3 only `substrate_ceiling` readings count**; MECH-457 and INV-088 each have **0**
ceiling autopsies (the whole MECH-457 campaign is `competence_implementation_gap` /
`measurement_test_design_defect`). The queue note's "brake released (MECH-457 count 8)" refers
to the *old* non_contributory-disjunct convention, superseded by R3. This 819a routing is a
**test-design fix**, not a same-question ceiling re-pose — it does not circle.

### Routing — **queue-experiment 819a** [user-confirmed]
`measurement_test_design_defect` → **819a** reconciling the worst-seed non-vacuity gate with
the strict-majority routing predicate (per-arm non-vacating as the docstring intends, or
strict-majority), and reconsider the 1.0 worst-seed floor + 1.0 effect margin against the
near-floor competence range. `evidence_direction: non_contributory` (both).

### Hypothesis-space ledger (Step 9b)
Pre-registered the **competence_floor R4 instrument-validity** leg
(`H-zworld-trained-instrument`, axis `instrumentation`) as **`alive`** — 819 attempted it but
the non-vacuity gate vacated the run, so it awaits a scored 819a. Recorded as **labelled
fan-out growth** (invariant 3a): pre-registration precedes adjudication, git-witnessed by this
artifact, original denominator preserved. **Not circling** — the leg re-tests whether the
representation-axis eliminations (H-rep, 747/749) hold now that the encoder actually trains
(780 proved those legs used a frozen random projection); it is instrument-validity, not the
dead H-rep leg renamed.

---

## Consolidated routing summary

| Target | Claims | Category | Direction | Routing |
|---|---|---|---|---|
| 793a | SD-049 | standard | inconclusive | governance — record finding, no re-queue |
| 817 | SD-080, SD-004 | competence_implementation_gap (+ measurement_test_design_defect) | non_contributory | queue-experiment **817a** + correct SD-080 note |
| 819 | MECH-457, INV-088 | measurement_test_design_defect | non_contributory | queue-experiment **819a** (reconcile gate) |

**Governance follow-on:** correct the SD-080 `evidence_quality_note` (Δ=0.0 error); write the
three `evidence_quality_note`s above; mark the three runs reviewed. **Chip follow-on:** 817a
and 819a are `/queue-experiment` work (chippable); the 693b guard-fragility consideration is a
future design note, not queued now.
