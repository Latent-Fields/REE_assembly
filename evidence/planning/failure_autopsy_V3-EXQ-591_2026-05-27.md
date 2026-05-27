# Failure autopsy — V3-EXQ-591 (ARC-046 curriculum-vs-flat)

- Run ID: `v3_exq_591_isef005_curriculum_vs_flat_20260526T184231Z_v3`
- Queue ID: V3-EXQ-591
- Claim tagged: ARC-046 (architectural_commitment, status candidate, conf 0.0)
- Outcome: FAIL · evidence_direction = `does_not_support` (overridden in this autopsy → `non_contributory`)
- Purpose: evidence
- Plan node: `infant_substrate:GAP-14` (status in-progress; unblocks DEV-NEED-008, ARC-046)
- Diagnosed: 2026-05-27 (session `failure-autopsy-V3-EXQ-591-20260527T052341Z`)

## 1. Facts (no interpretation)

Setup: 3 arms × 5 seeds (42–46) × 2000 episodes × 200 steps on CausalGridWorldV2 (size=12).

- ARM_0_ctrl_a — flat, all infant env features ON (harm_gradient_enabled=True scale=0.30, transient_benefit_enabled=True, microhabitat_enabled=True), novelty_bonus_weight=0.7.
- ARM_1_ctrl_b — flat, all infant env features OFF, novelty_bonus_weight=0.5.
- ARM_2_curriculum — 4-phase `InfantCurriculumScheduler`, novelty starts 0.5.

Gate criteria (`infant_substrate_expansion.md` §8): C1 z_goal_norm > 0.4 · C2 rolling-100-ep H_pos > 0.65·ln(144) ≈ 3.23 · C3 residue_coverage_pct > 0.15 · C4 action-zone entropy + KL · C5 harm/benefit ratio ∈ [0.2, 5.0] · C6 post-sleep z_goal retention > 0.85 · C7 traj cosine > 0.3.

PASS criterion: ARM_2 ≥ 6/7 in ≥ 4/5 seeds AND (ARM_0 OR ARM_1) ≤ 4/7 in ≥ 3/5 seeds.

Observed (all 15 runs):

| Arm | per-seed n_criteria_passing | which criterion passes | final z_goal_norm | final residue_cov | rolling H_pos mean | curriculum_final_phase |
|---|---|---|---|---|---|---|
| ARM_0_ctrl_a | 1, 1, 1, 1, 1 | only C3 | 8.5e-08 / 0 / 1.5e-15 / 0 / 9.4e-07 | 1.0 all seeds | 0.43 / 0.32 / 0.97 / 0.03 / 1.08 | n/a |
| ARM_1_ctrl_b | 1, 1, 1, 1, 1 | only C3 | 0 / 0 / 5.4e-08 / 0 / 1.1e-10 | 1.0 all seeds | 0.38 / 0.28 / 0.99 / 0.11 / 1.00 | n/a |
| ARM_2_curriculum | 1, 1, 1, 1, 1 | only C3 | 0 / 0 / 5.4e-08 / 0 / 1.1e-10 | 1.0 all seeds | 0.38 / 0.28 / 0.99 / 0.11 / 1.00 | **0** (every seed) |

`final_harm_benefit_ratio = -1.0` and `final_traj_cosine = -1.0` in every seed (the script's "no data observable" sentinel). `post_sleep_retention = -1.0` in every seed (the C6 retention path is only entered when `final_z_goal_norm > 0.1`, which never occurs).

**Per-seed ARM_1 and ARM_2 rolling_h_pos_mean are byte-identical** (e.g. seed 42 → 0.38474135175975177 in both). Because `InfantCurriculumScheduler` never left Phase 0, and Phase-0 env config is the same minimal set ARM_1 uses.

Failed-criterion class: **negative-control passes (C3 saturates trivially), every discrimination criterion fails across every arm.** This is the substrate-ceiling fingerprint.

## 2. Why the curriculum stayed in Phase 0

`InfantCurriculumScheduler` Phase 0 → 1 transition requires (a) episode ≥ 100 and (b) the latest `h_pos` argument ≥ `H_POS_FRAC_OF_MAX * ln(grid²) = 0.70 * ln(144) ≈ 3.48`.

Observed rolling-mean H_pos ranges across 2000 episodes per seed: 0.03 – 1.08. The advancement gate is **never** approached in any seed. The scheduler is structurally stuck.

The effective experiment is therefore ARM_0 (full features) vs ARM_1 ≡ ARM_2 (no features). Both null in identical ways.

## 3. Claim-layer map (ARC-046)

```
ARC-046: "The infant stage requires a hazard protection mechanism that permits
sensorially salient harm exposure without catastrophic residue saturation."
claim_type: architectural_commitment
status: candidate · confidence: 0.0
depends_on: INV-055, ARC-019, ARC-013, SD-010, SD-011
```

Did the experiment let the claim express itself? **No.** ARC-046 asserts that `residue_scale_factor ≈ 0.1` + reduced `hazard_magnitude` during infancy delivers harm geography without destroying the substrate. To discriminate "phased residue accumulation via curriculum" from "flat parameter baselines" the test needs at least one arm to **develop a non-trivial z_goal trajectory** and at least one arm to **exhibit measurably different residue dynamics**. Neither happened. z_goal ≈ 0 in every arm; residue_cov saturates to 1.0 in every arm.

`claim_ids = [ARC-046]` is the right tag for what the experiment was *designed* to test, but the actually-measured signal does not weigh on ARC-046 in either direction.

## 4. Biological-reference triage

ARC-046 is a developmental-protection claim. Mammalian / primate / human anchors:

- Myelination, NMDA-subunit, and PFC-maturation time courses give a long infant window of plasticity with attenuated long-term consolidation.
- Attachment-buffered nociception (Hofer / Sullivan literature; SD-011 / SD-035 cluster): caregiver presence dampens C-fibre amplitude into central registers, producing exactly the "educative but non-destructive" exposure ARC-046 names.
- INV-043 caregiver-function "imperfect protection: allow harm-learning without destruction" is the surrounding architectural commitment.

ARC-046's mechanism (low `residue_scale_factor` + reduced `hazard_magnitude`) is a **faithful biological translation**, not a formal-definition import. No lit-pull commission required. The mechanism class has a working existence proof; the implementation has not been shown not to work.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Test did not let ARC-046 express itself; substrate too coarse and training regime did not produce z_goal in any arm |
| Biological reference | clear | Developmental hazard protection is well-anchored; mechanism is faithful translation, not formal import |
| Prerequisites | **missing** | Depends on goal-pipeline substrate that does not produce non-trivial z_goal in default config (V3-EXQ-540 series, V3-EXQ-603 series) |
| Implementation completeness | partial | `InfantCurriculumScheduler` Phase 0 → 1 advancement gate (H_pos ≥ 3.48) is structurally unreachable under current training regime |
| Environment adequacy | inadequate for discrimination | All 3 arms produced indistinguishable z_goal / H_pos / harm_benefit; cannot discriminate phased vs flat residue accumulation |
| Measurement adequacy | under-instrumented | C5 / C6 / C7 emit –1.0 sentinels in every seed of every arm; 3 of 4 advisory criteria carry no information |
| Integration adequacy | isolated | Modules work in isolation; training regime / default config does not engage the goal-pipeline substrate needed for the curriculum advantage to be measurable |
| Scale / capacity | likely insufficient | Same training-regime gap V3-EXQ-603b autopsy flagged: random-policy 2000-episode training with default novelty / drive / no MECH-307 / no MECH-295 / no SD-049 does not develop z_goal |

Recommended `epistemic_category`: **`substrate_ceiling`**.

## 6. Cluster pattern (load-bearing)

V3-EXQ-591 is the fourth distinct expression in 30 days of one structural property. None of these is an independent bug; they share a single upstream blocker — the V3 substrate at default config under standard random-policy training across 2000 episodes does not produce non-trivial z_goal, behavioural diversity, or action-class differentiation.

| Run | Claim layer | Negative-control / absolute criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-540a/b/c/e | MECH-307, MECH-295 | bridge instantiates and wires | `conj_fire_rate = 0` across all arms | Default config values sit above achievable substrate ceiling. Default-value recalibration landed 2026-05-12; V3-EXQ-540e validation pending. |
| V3-EXQ-603 / 603b | Q-045, MECH-313, MECH-260 | scripts complete | 2 of 3 seeds die at 350–475 steps; effective N=1 | Training-regime measurement_gap — needs P0 (E1+E2 warmup) + P1 (consolidation) per the 603b autopsy. V3-EXQ-603c routed via /queue-experiment 2026-05-27. |
| V3-EXQ-590a | MECH-314 (Goldilocks novelty weight) | wiring intact | per-candidate signal = 0 across all weights | `goldilocks_weight=0.1` is an artefact: MECH-111 broadcast branch is argmin-invariant; MECH-314a per-candidate signal is structurally zero under E2 z_world per-candidate collapse. |
| **V3-EXQ-591** | **ARC-046** | **C3 residue saturation (trivial)** | **6 of 7 criteria fail every arm; curriculum stuck Phase 0** | **z_goal collapses to ≈ 0; curriculum advancement gate unreachable.** |

Two readings are live: (a) test-design ceiling (these are four independent test-design errors masked as substrate failures), (b) substrate enrichment required (the substrate at default config genuinely doesn't produce z_goal). The convergent shape across four structurally-different claims with four different downstream consumers strongly favours **(b)** — this is one structural property, not four independent test-design errors. The recommended planning decision is to treat substrate fix as the unblocker for all four; behavioural validation experiments resume once the substrate produces non-trivial z_goal in default config.

## 7. Learning extracted

- The InfantCurriculumScheduler's Phase 0 → 1 advancement gate (`H_pos ≥ 0.70·ln(144) ≈ 3.48`) is **structurally unreachable** under current training. Observed rolling-mean H_pos saturates at ~1.08 with random-policy stepping over 2000 episodes. This is a Phase-1 test-design error orthogonal to the substrate question: even with a perfectly working goal-pipeline substrate, ARM_2 would still stay in Phase 0 unless either the threshold or the gating signal is changed.
- C3 (`residue_cov > 0.15`) is **degenerate as a discrimination criterion** in the current substrate. It saturates to 1.0 trivially regardless of arm, regardless of whether the agent ever forms goal-directed behaviour. It cannot contribute to PASS/FAIL discrimination.
- C5/C6/C7 carry **no information** at all in any arm because their preconditions are never met (harm_benefit_ratio sentinel −1.0 from `coverage_telemetry`; C6 retention path gated on `final_z_goal_norm > 0.1` which is never true; C7 traj_cosine sentinel from env when traj_telemetry has no committed segments).
- The full 7-criterion gate currently has only **3 criteria that could discriminate** (C1, C2, C4). All three depend on z_goal or H_pos developing — which only happens once the upstream goal-pipeline substrate produces signal.

## 8. Routing (user-confirmed)

User selected: cluster-absorb + curriculum-gate fix (recommended); single failure_autopsy with cluster section (recommended).

- ARC-046 is **untouched**. This FAIL does not weigh on the claim in either direction.
- `evidence_direction_per_claim["ARC-046"]` overridden to **`non_contributory`**.
- `pending_retest_after_substrate = true`.
- Recommended `epistemic_category` for the indexer: **`substrate_ceiling`**.

Three substrate prerequisites must clear before V3-EXQ-591b is queued. Two are already routed via in-flight substrate work; one is new:

1. **MECH-307 default-value recalibration validated** — V3-EXQ-540e on the queue, awaiting full run; not blocking here.
2. **Goal-pipeline training regime produces non-trivial z_goal in default config** — V3-EXQ-603c routed 2026-05-27 (P0 / P1 phased training per the 603b autopsy); not blocking here.
3. **NEW: InfantCurriculumScheduler Phase 0 → 1 exit signal tuned to achievable signal magnitudes** — recommended `/implement-substrate` target. Two options: (a) lower the H_pos fraction-of-max threshold from 0.70 to a value the substrate can actually reach (probe data implies ~0.20 of max ≈ 0.99 is reachable; ~0.30 ≈ 1.49 may be the right break-point); (b) replace the H_pos gate with a z_goal-norm-based gate or a residue-coverage progression gate. Choice between (a) and (b) wants a brief substrate probe before commitment.

Once (1)–(3) clear, queue V3-EXQ-591b via `/queue-experiment`. The 7-criterion gate may also need partial revision: C3 is trivially saturating and C5/C6/C7 are sentinel-emitting; the gate should be rebuilt against criteria that have non-degenerate variance.

## 9. Draft `evidence_quality_note` (governance applies, not this skill)

> 2026-05-27 (V3-EXQ-591 failure_autopsy): Substrate-uniform FAIL — all 3 arms hit only 1/7 gate criteria across all 5 seeds (only C3 residue_cov, which saturates to 1.0 trivially in every arm). Curriculum scheduler stuck in Phase 0 across all 5 seeds (advancement gate `H_pos ≥ 0.70·ln(144) ≈ 3.48` vs observed rolling-mean H_pos 0.03–1.08). z_goal collapses to ~1e-7 in every arm. C5 harm/benefit ratio, C6 post-sleep retention, C7 traj cosine all return −1.0 "no data" sentinels in every seed of every arm (3 of 4 advisory criteria carry no information). ARM_1 and ARM_2 produce per-seed-identical rolling H_pos because Phase-0 env config ≡ ARM_1 minimal config. Convergent shape with V3-EXQ-540a/b/c/e (MECH-307 / MECH-295 default-value recalibration), V3-EXQ-603 / 603b (training-regime measurement_gap), V3-EXQ-590a (Goldilocks novelty no-op) — one structural property across four structurally-different claims. evidence_direction overridden to non_contributory; pending_retest_after_substrate=true. Does NOT weaken ARC-046. Retest gated on (a) MECH-307 default-value recalibration validated (V3-EXQ-540e PASS), (b) goal-pipeline training regime producing non-trivial z_goal in default config (V3-EXQ-603c P0/P1 phased training), (c) InfantCurriculumScheduler Phase 0 → 1 advancement signal tuned to achievable H_pos magnitudes OR replaced with a z_goal-norm-based / residue-progression-based exit gate.
