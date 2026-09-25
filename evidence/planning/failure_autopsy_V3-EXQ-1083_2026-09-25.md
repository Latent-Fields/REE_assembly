# Failure autopsy: V3-EXQ-1083 (SD-081 adaptive vs fixed allocation, model-uncertainty half)

- Run: `v3_exq_1083_sd081_adaptive_vs_fixed_allocation_20260924T172346Z_v3` (ree-cloud-2, 8 seeds, 6.4 h)
- Claim: SD-081 (design_decision, candidate). Purpose: evidence.
- Generated: 2026-09-25T01:41:28Z by orchc0925-autopsyA-1083 (orchestrate-20260924-1707 autopsy subagent A)
- Status: **confirmed**. Confirmed under the user's standing delegation via orchestrate-20260924-1707. The self-route is the driver's own pre-registered branch. Every number below re-derives from the manifest, and the routing changes no claim status or scope.
- Chip: chip-autopsy-v3-exq-1083

## 1. Dry-run gate and recording

- `check_dry_run_citations.py` covered the run_id and the queue_id: 0 dry, 2 clean. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- `validate_recording.py`: OK. The always-core is complete (substrate_hash `cb6e158c...`, commit `00210b562c` clean, config, seeds 0-7, machine, elapsed). `substrate_stable_across_run: false` is on-disk drift during the run (process_snapshot_drift). The per-cell hashes agree, so the running process used one substrate throughout.
- `dry_run_unreachable_criterion` lint: silent for this driver.

## 2. Facts

The design has five arms on one practised agent per seed, with bit-identical weights: adaptive (the SD-081 rule), fixed (w = this seed's adaptive mean), shuffled, habit_only and planned_only. There are two cells, familiar-intact and familiar-perturbed, where "perturbed" means seeded Gaussian noise on the E2 world_transition weights (relative sigma 2.0).

| Gate / criterion | Measured | Bar | Result |
|---|---|---|---|
| P1 pathways differ (worst seed) | 0.652 | >= 0.2 | met |
| P1b habit score range (worst tick) | 0.0037 | > 1e-6 | met |
| P2 arbitration live on familiarity (worst seed) | 1.0 | >= 0.95 | met |
| P4 perturbation reaches u_planned (seeds with AUC >= 0.7) | 6/8 = 0.75 | >= 2/3 | met |
| P7 seeds with reach data | 8 | >= 6 | met |
| **C1** w(intact) - w(perturbed), mean - SEM | 0.131 (mean 0.177, 7/8 +) | > 0.02 | **PASS** |
| **C2** DID of P(selected == planned argmin given disagreement), adaptive minus fixed, mean - SEM | 0.139 (mean 0.198, 7/8 +) | > 0.03 | **PASS** |
| **P5** single-path outcome separation, max cell of mean(planned_only - habit_only return) | **0.035** | >= 0.2 | **UNMET** |
| **C3** benefit over fixed | vacated (0 scored cells) | > 0.1 | FAIL (non-degenerate false) |
| C4 reach beyond shuffled (secondary) | 0.140 | > 0.03 | pass |

- Seed 2 is an outlier: u_planned 13-15 against 0.03-1.3 on other seeds, C1 0.033, C2 0.099. The 8-seed means are therefore not homogeneous.
- Seed 1 is the only negative seed on C1 and C2. Reach (selected == argmin(arbitrated)) is 0.606 on the worst seed (seed 2). That is below "reach complete", but it does not matter because C2 passed.
- **The agent is at a competence floor.** Mean episode return is -0.875 (planned_only) to -0.910 (habit_only), and all five arms fall within 0.035 of each other. Episodes end by death at about 55 of 120 steps. Benefit contacts are 0-1 per episode. The per-seed planned-minus-habit differences are mixed in sign (-0.15 to +0.24).
- Self-route: `reach_confirmed_benefit_untestable` -> non_contributory. This is the driver's pre-registered branch for "C1, C2 pass, P5 unmet".
- Expected vs observed: the driver expected C1 and C2 to show that the weight tracks model uncertainty and reaches selection (observed), and C3 to show benefit over the fixed mixture (not testable: the pure pathways do not differ in outcome).

## 3. Claim layer

SD-081 has 0 prior experimental entries and no epistemic_category. Its what_would_answer (2026-09-21 audit) says:
- CONFIRMING: uncertainty changes allocation and improves appropriate pathway recruitment beyond a fixed mixture, **with both pathways informative**. The DV includes benefit over fixed.
- FALSIFYING: with both scores non-degenerate, adaptive allocation has **no benefit** or **does not reach committed selection**. "The sigmoid formula alone is not supporting evidence." A failure under unmet preconditions is not evidence against the claim.

**Did the test let the claim express itself?** It did for reach. It did not for benefit. The "does not reach committed selection" arm of FALSIFYING is **not met**, because C2 shows reach beyond a matched fixed mixture. The "no benefit" arm is **untested**, because the precondition "both pathways informative" failed (P5). The familiarity half was out of scope by design (GFLAG-0454).

**What C1 and C2 actually establish.** u_planned is `E3._running_variance`, the EMA of E2's one-step world error. The manipulation injects noise into the same E2 weights, so C1 moving is close to guaranteed once P4 holds; the driver calls C1 necessary, not sufficient. C2 is the substantive result. The fixed arm sees the same perturbed candidate geometry, and its PA change is subtracted, so C2 isolates the allocation rule's effect on the committed pick. What C2 shows is **plumbing, not appropriate recruitment**: the planned argmin that the weight recruits is not itself outcome-informative on this substrate (section 4).

## 4. Biological reference

- Closest mechanism: reliability-based arbitration between a goal-directed controller and a habitual controller. The model-based side is dorsomedial striatum / OFC; the habitual side is dorsolateral striatum; vlPFC / frontopolar cortex arbitrates on reliability. References: Daw, Niv & Dayan 2005; Lee, Shimojo & O'Doherty 2014; Daw 2011. All are already on file under `targeted_review_connectome_mech_163`. lit_status: present.
- Dependencies in the brain: (i) a model-based controller whose predictions of action consequences are informative when its own prediction error is low; (ii) reliability estimated from each controller's own prediction errors; (iii) enough competence that the two controllers' choices lead to different outcomes.
- **The FAIL matches the signature of dependency (i) being absent.** Same-day evidence: GFLAG-0485, REE_assembly f300ebf64d plus the 2d848ca2d3 addenda.
  - E2 predicts the executed action's consequence at chance, even when trained.
  - E3's full-horizon J does not track true consequences (rho -0.18 to 0.01; the pick rate is at or below chance).
  - More than 98% of the across-candidate variance comes from rollout steps > 5.
  - The planned pathway is exactly that full-horizon J. Neither pathway is "informative", so arbitrating between them cannot buy benefit.
  - Regime match. The 811a lineage runs WORLD_DIM 32, and `warmup_train` trains the E2 world head with single-step MSE at about 14k updates. That is GFLAG-0485's BWF recipe, whose action-blindness showed no dose trend from 600 to 10000 updates. The regimes differ in grid size (10x10 vs 5x5), and here the benefit channel is on and the harm head is trained. So the GFLAG-0485 reading is **extrapolated** to this run, not re-measured.
- **In-run evidence consistent with it.** The 2.0 x mean|w| E2 noise raised return by **+0.154 for planned_only and +0.154 for habit_only**, identically; the other three arms moved by +0.17 to +0.20. If the full-horizon pathway carried E2-borne outcome information, wrecking E2 should hurt it differentially, and it does not.
- Translation note, not load-bearing: SD-081's habit pathway is a depth-2 read of the same scorer, not a cached model-free value (Dezfouli & Balleine 2013 is on file).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Reach leg expressed and passed; benefit leg could not express (P5 unmet) |
| Biological reference | partial | Arbitration biology is clear. The missing dependency is an outcome-informative model-based controller |
| Developmental / dependency prerequisites | missing | Outcome-informative planned pathway (GFLAG-0485 chain); familiarity input for the other half (GFLAG-0454) |
| Implementation completeness | complete | SD-081 is live (P2 1.0) and reaches the committed pick (C2) |
| Environment adequacy | partial | The pressure exists in the 10x10 grid, but at a 0-1 benefit-contact competence floor the death-censored return cannot tell the pathways apart |
| Measurement adequacy | adequate | P5 correctly vacated C3; C2 reads committed selection against a matched fixed control |
| Integration adequacy | coupled but inert (STARVED UPSTREAM) | The arbitration moves the pick, but the recruited ranking carries no outcome information. Implementation is not downgraded for this |
| Scale / capacity | unknown | 811a practice budget. Worker D found no dose trend in E2's action-blindness up to 10k head steps |

**Failure location (GOV-FAILLOC-1): MIXED (ENVIRONMENT / competence regime + missing upstream prerequisite). It is not chargeable to REE or to SD-081.** The benefit criterion was vacated, not failed, so there is no "REE failed" observation to classify.

## 6. Cluster

Single run. There are 0 prior autopsy targets tagging SD-081 (`granularity_debt_cluster.py SD-081`). Related open context is GFLAG-0454 (the familiarity half) and GFLAG-0485 (the E2/E3 chain), but no cluster.

## 7. Learning and routing

Learning extracted:
1. **Existing dependency strengthened (a positive-negative result).** Uncertainty arbitration can only show benefit when the model-based pathway is outcome-informative. 1083 reproduces SD-081's own CONFIRMING precondition as the binding constraint.
2. **Reach established.** The SD-081 weight tracks E2 model uncertainty and moves committed selection beyond a matched fixed mixture. This is the lineage's first committed-selection read; 811a's DV came from a different scorer.
3. **In-run R2 null.** habit_only (the depth-2 rule) and planned_only (full horizon) separated by only 0.035. Matching the scored depth to fidelity does not by itself make selection outcome-informative here. The E2-noise invariance (+0.154 for both) points the same way.
4. **Measurement design validated.** The P5 gate turned a would-be "no benefit -> weakens" into a correctly vacated criterion.
5. The familiarity half stays open behind GFLAG-0454.

Node class: `complicated (buildable)` for the prerequisite, which is the GFLAG-0485 repairs R2 + COV already named by Worker D. SD-081 itself is `complex (probe-gated) / puzzle (known rules)` for the benefit leg, and it waits on that build.

**Routing: implement-substrate.** Create `e3-outcome-informative-planned-pathway` (priority 1, severity degrading).
- Leg (i) is an ACTION-CONDITIONAL E2 world prediction, with a ree_core-owned waking objective and action-diverse training data.
- Leg (ii) is NOT 'match E3's scored horizon to fidelity' on its own. This run's habit_only arm IS that R2 depth-2 selection rule (`e3_selector.py:1928-1931`), and it separated from full-horizon selection by only 0.035. So depth-matching alone is measured inert on this row's validation statistic.
- Any depth change must keep the planned depth above the habit depth, or add a separate planned-depth knob. Otherwise SD-081's non-degeneracy precondition fails by construction.
- Dedupe: if governance registers a row from GFLAG-0485 first, treat this as an amend of that row. `e2-world-forward-sleep-trainer` and `SD-PP-B5` are adjacent rows, and neither covers this consumer.
- Validation statistic: P5 >= 0.2 in at least one cell. This bar is about the largest return shift any manipulation produced here, so it doubles as a competence probe.

- **Re-queue guidance.** Do not re-queue the same question until the planned pathway is outcome-informative. Any benefit-leg re-queue must first pass a cheap P5 pilot: planned_only vs habit_only only, 2-3 seeds.
- **Re-derive brake:** 0 prior hits for SD-081, so this autopsy is the first counting hit. The brake does not fire.
- **Granularity-debt recurrence trigger:** does NOT fire. `granularity_debt_cluster.py SD-081` finds 0 tagging targets and no `weakened` reading.
- **Not chipped here.** A /failure-autopsy session does not chip follow-on that depends on its own not-yet-governance-reviewed finding. /governance ratifies and chips.

## 8. Recommended writes (for /governance)

- SD-081: direction non_contributory; epistemic_category **standard** (the claim carries none today); `pending_retest_after_substrate: true`; status unchanged (candidate).
- Draft evidence_quality_note: see `recommended_evidence_quality_note` in the JSON. It is verbatim text covering: reach confirmed (C1 0.131, C2 0.139, 7/8 seeds), benefit untestable (P5 0.035 vs 0.2), the competence floor, GFLAG-0485, the untested "no benefit" arm, the familiarity half behind GFLAG-0454, and the P5-pilot requirement for any re-test.
- `narrow_supports` check: SD-081 has `evidence: []`, so there is no illusory-conflict risk.

## 9. Non-outcome observations (not adjudicated)

- In every arm, the E2-perturbed cell **lengthened** survival in 5 of 8 seeds (seed 6: +90 to +104 steps) and shortened it in 2-3. The effect is shared across arms within a seed, because the arms share weights and RNG. It is a seed x cell effect, not an allocation effect. It is suggestive of GFLAG-0485 (noise in E2 costs a policy nothing, or even helps, when that policy already chooses on uninformative rollout content), but it is not robust.
- E3 ticks are about 28% of env steps (seed 0 adaptive: 499 of ~1774), and the arbitration acts only on those ticks.

## 10. Hypothesis-space ledger (Step 9b)

No fan-out. No registered question names SD-081, MECH-477 or V3-EXQ-1083 (71 questions scanned). A vacated criterion discriminates no leg. The registry was not written (`hypothesis_space_ledger_pending.entries: []`).

## 11. Step 7b / 7c

- 7b `autopsy_pre_routing_checks.py`: 0 fires, both before and after the .md existed. C7 was inapplicable because of the arm-array shape.
- 7c red-team: run on **fable** (cross-model; this session drafted on Opus 5.5). Verdict **CONTESTED (narrow)**.
  - Every load-bearing number recomputed from the per-seed cells: P5 0.0347/0.0349; C1 0.177 with lower bound 0.131, 7/8; C2 0.198 with lower bound 0.139, 7/8; P4 6/8.
  - Status, direction, category, routing, severity and brake were graded as standing.
  - **Defect:** leg (ii) of the substrate row (R2 via `_score_depth_limit`) is already measured inert by this run's habit_only arm, and as a shared knob it would collapse SD-081's planned/habit contrast. The dedupe list also omitted `e2-world-forward-sleep-trainer` and `SD-PP-B5`.
  - Cheap confirmer: `sed -n 1926,1932p ree-v3/ree_core/predictors/e3_selector.py`.
  - **Accepted in full.** The row text, dedupe list and learning were rewritten, and hygiene items 1-7 were applied: GFLAG-0485 premise restated as conditional; extrapolated-vs-measured marking; P5 competence caveat; MECH-477 as beneficiary; warmup_train note; seed-2 outlier (u_planned 13-15, reach 0.606). Findings: `.scratch/orch-20260924-1707/autopsy/redteam_1083.md`.

## 12. Coordination note

The autopsy-pause claim was refused by arbitration (exit 3): four orchestrate-20260924-1707 science workers own `experiment_queue.json`, `substrate_queue.json` and `experiment_proposals.v1.json`. This autopsy writes none of them. The metaworker was therefore not paused for this diagnosis.
