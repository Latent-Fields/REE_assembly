# Failure autopsy: V3-EXQ-1089 (MECH-268 closure-cadence dose, mode-register DV, reset ON/OFF bracket)

- Run: `v3_exq_1089_mech268_closure_cadence_mode_register_20260924T180356Z_v3` (ree-worker-3, 5 seeds, 5.5 h)
- Claim: MECH-268 (mechanism_hypothesis, provisional, epistemic_category standard). Purpose: evidence.
- Generated: 2026-09-25T01:54:53Z by orchc0925-autopsyA-1089 (orchestrate-20260924-1707 autopsy subagent A)
- Status: **confirmed**. Confirmed under the user's standing delegation via orchestrate-20260924-1707. The self-route is the driver's pre-registered branch and its cause re-derives from the manifest. Routing is a same-question test-design re-queue, and no claim status or scope moves. The sequencing question against the pending user decision dec-20260923T185804-MECH-268 is a recommendation, flagged in QUESTIONS.md.
- Chip: chip-autopsy-v3-exq-1089. Context flags: GFLAG-0466 (SD-032a exit deadlock) and GFLAG-0467 (stale GAP-4 plan rows).

## 1. Dry-run gate and recording

- `check_dry_run_citations.py`: 0 dry, clean. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- `validate_recording.py`: OK, with the always-core complete (substrate_hash `da77a773...`, which is authoritative). The stamped commit `5bf2f0c7c4` is the disk state at manifest-write time (`commit_describes_recorded_hash` false, lag 18655 s), not the commit the process ran; that commit is unresolved. Per-cell hashes agree; on-disk drift during the run does not affect the process.
- Every quantity this autopsy needed was recorded per (seed, arm): fresh and latched ticks, fires, reset flags, pe percentiles and release fractions. There is **no recording gap**.

## 2. Facts

Nine eval-only arms share one P0 training per seed: SATOFF, then s in {0.5, 0.3} x K in {6, 24} x closure reset of the outcome FIFO ON/OFF. The DV is argmax internal_planning occupancy of the soft mode vector. The discrete register is recorded but not scored, because it is structurally pinned (GFLAG-0466).

**Readiness (run-level): 2/5 seeds ready, 4 required. So the route is `substrate_not_ready_requeue` and the direction is non_contributory.**

| Seed | Ready | Fresh / 1200 steps | Latched | Closure fires (S050 K6 / K24) | pe_unsat p50 | S050_KS_OFF release | C1 delta (ON-OFF) |
|---|---|---|---|---|---|---|---|
| 42 | yes | 1160 | 3% | 113 / 28 | 4.18 | 0.239 | **0.176** |
| 43 | no | 138 | 88.5% | 0 / 0 | 2.12 | 0.790 | (0.000) |
| 44 | yes | 1184 | 1% | 117 / 29 | 5.61 | **0.000** | 0.000 |
| 45 | no | 281 | 77% | 5 / 1 | 3.21 | 0.861 | (0.085) |
| 46 | no | 301 | 75% | 9 / 2 | 3.27 | 0.867 | (0.176) |

(Parenthesised deltas are on not-ready seeds and are not scored.)

- **C1** (load-bearing), scored on the ready seeds: mean 0.088. The margin is max(2 x pstdev 0.088, 0.10) = 0.176, so C1 is not met. C2 (manipulation consistency) and C3 (floor boundary) are also not met on the ready seeds; neither gates the verdict.
- **Why seeds 43/45/46 are not ready.** E3 re-selected (a fresh dACC forward) on only 11-27% of env steps; the rest were held-action ticks. The lateral-PFC rule_state and the closure detector are both denominated on fresh ticks. rule_delta follows the same decay curve on every seed (red-team recompute) and becomes stable after about 77-100 fresh ticks.
  - Seed 43 has exactly 23 fresh ticks in every 200-step life, so it is truncated before stabilising: all 132 closure evaluations read `not_stable_yet(0/6)`. The fixed periodicity suggests a fixed-length commitment hold (MECH-090 stepping).
  - Seeds 45/46 fired only in the one or two lives that exceeded about 80-100 fresh ticks.
  - Closures therefore fired 0-2 times in the K24 arms, below the floor of 5. Seed 43's reset-flag checks read false only because it had zero fires (a vacuous result, not a flag defect).
- **Why ready seed 44 carries no signal.** pe_unsat p50 is 5.61, so the s=0.5 floor (0.25) leaves pe at 1.40, above the critical value of about 1.0. Nothing can release in any arm. The driver's own "WHY C1 CAN FAIL" note predicts this case.
- **The headroom gate read green (4/5), but it counts every seed that ran.** Three of its four passes are not-ready seeds. Among ready seeds, headroom is 1/2.
- **The pilot seed overlaps the evaluation seeds.** Thresholds and design were set from a 1-seed pilot on seed 42, which is also an evaluation seed. It is the only seed that turned out to be both ready and to have headroom, and it reproduces the pilot's effect (0.176 against the pilot's 0.229 at K=6).
- The discrete register is pinned at internal_planning in every arm on every seed (`occ_ip_current` 1.000), which corroborates GFLAG-0466 on 5 seeds.

## 3. Claim layer

MECH-268 is provisional. Its WWA says the mechanism level (463/468, synthetic) and the live-wiring level (729 x2, narrowed 2026-09-14) are established. The ecological purpose (saturation lets a stuck register relax) and graded behaviour are **not** established. 1089 was the multi-seed test of that purpose, with a closure-cadence dose and a reset bracket for attribution.

**Did the test let the claim express itself?** Only on one seed. On seeds 43/45/46 the manipulation (closure-driven FIFO resets) was almost never delivered. On seed 44 the DV could not move at all, because of the pe scale. Seed 42 moved in the predicted direction by 0.176. This is a readiness non-result. It is not evidence against MECH-268, and one seed is not evidence for it.

## 4. Biological reference

dACC outcome, error and conflict signals adapt under repeated identical outcomes, and the outcome signal fades during exploitation (Quilodran, Rothe & Procyk 2008; Behrens 2007; Shenhav 2013/2016; Holroyd 2012). All are on file in `targeted_review_connectome_mech_268`, 6 entries. lit_status: present.

Biologically, adaptation needs a stream of outcome evaluations to act on. In latch-dominated agents, E3 rarely re-evaluates, so there is little for saturation to adapt and little for closure to reset. The failure is the trained agent's operating regime, not a translation mismatch.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Not fairly tested; 1 informative seed out of 5 |
| Biological reference | clear | Not implicated |
| Developmental / dependency prerequisites | partial | The closure-coupled FIFO needs fresh E3 ticks, and latch-dominated seeds starve it. The dacc_pe scale is uncalibrated to the critical value (open decision dec-20260923T185804-MECH-268) |
| Implementation completeness | complete | FIFO live, n_rec matches the closed form (1.0), reset flags correct where fires occur. Caveat: on seed 44 fire timing ON/OFF agrees only 0.877, so the bracket is not a pure FIFO contrast there; this is harmless because C1 is 0 by no-headroom |
| Environment adequacy | adequate | 729-lineage bed with a constant harm outcome class (scope note F6: silent on the class-transition half) |
| Measurement adequacy | partial | (a) Eval length is denominated in env steps, not fresh ticks. (b) The headroom gate is counted over all seeds, not ready seeds. (c) The single-seed pilot used an evaluation seed |
| Integration adequacy | coupled but inert (STARVED UPSTREAM) on 43/45/46 | The coupling is wired but not exercised |
| Scale / capacity | likely insufficient | 5 seeds with a ~40% ready rate |

**Failure location (GOV-FAILLOC-1): MEASURES (test design / calibration). It is not chargeable to REE or to MECH-268.**

## 6. Cluster, brake, granularity

- **Re-derive brake:** MECH-268 has **5 prior counting hits**, all from the SD-034 468 decommit-hold behavioural lineage (468b/c/d/e/f), co-tagged SD-034/MECH-090, on the closure's de-commitment-authority face. **This reading does not count.** Under R3 clause 2 it is a test-design category that owes no substrate build, so the brake does not fire. The artifact stamps an explicit producer release (`fired: false`, `literal_count_meets_threshold: true`). 1089 is a different design (mode-register DV with a reset bracket), and its repair is readiness scheduling, not another letter against the 468 ceiling. The /queue-experiment consumer gate makes its own call on a 1089a.
- **Granularity-debt trigger:** does NOT fire. `granularity_debt_cluster.py MECH-268` finds 7 tagging targets, and none reads `weakened`. The 3 `other`/`unstamped` alignment strings say "not fairly tested", "exercised+passed" or are unstamped at cluster level. This is measurement and implementation debt, not granularity debt.

## 7. Learning and routing

Learning extracted:
1. **Test-design gap.** An eval denominated in env steps cannot guarantee that a closure-coupled manipulation fires when E3 latches. Denominate on fresh ticks.
2. **Measurement gap.** A headroom gate counted over every seed certified headroom where C1 is not scored, and missed its absence on a ready seed.
3. **An unrepresentative pilot.** The single-seed pilot on an evaluation seed matched only 1 of the 5 seeds' regime. Pilot on 3 or more disjoint seeds.
4. **Two regimes after one training.** The same P0 training splits the seed population into free-selecting and held-action regimes (seed 43: exactly 23 fresh ticks per 200-step life). Every fresh-tick-denominated detector is starved in the held regime. This bears on any closure- or dACC-cadence experiment on the 729 lineage.
5. There is no recording gap.

Node class: `complex (probe-gated) / puzzle (known rules)`. The frame is well posed; the missing fact is the bracket effect on a ready, headroomed seed population.

**Routing: queue-experiment, a same-question re-run V3-EXQ-1089a.** Spec:
- Denominate each arm's eval on **fresh E3 ticks**: at least ~100 per life. Size the env-step cap for held-action seeds; a seed-43-like agent needs about 870 env steps per life, about 4x today. Name the hold mechanism.
- Keep fire-timing agreement ON vs OFF (>= 0.9) as a **per-seed** readiness check.
- Make **per-seed headroom** a readiness condition, counted among ready seeds.
- Use **8 or more seeds**, and pilot on **3 or more seeds disjoint** from the evaluation seeds. Pre-register the expected ready fraction.
- Pre-register the floor-arm boundary contrast (release at S050_KS_OFF minus S030_KS_OFF) on every seed where SATOFF occupancy is at least 0.5, since it does not need closure fires.
- **Sequencing recommendation:** take dec-20260923T185804-MECH-268 first. If it picks the dacc_pe-normalising route (option B), run 1089a on that substrate. A fixed floor against a pe scale of 2.1-5.6 will lose seeds to no-headroom again.

`recommended_substrate_queue_entry: none`. If the decision picks option B, that decision owns its own entry.

Not chipped here: governance ratifies and chips.

## 8. Recommended writes (for /governance)

- MECH-268: direction non_contributory. The category stays standard and the status stays provisional. Append the evidence_quality_note (verbatim in the JSON `recommended_evidence_quality_note`). `change` ends "-> stamp this artifact".

## 9. Bears-on (not adjudicated here)

- **dec-20260923T185804-MECH-268** (proposed; it waits on a multi-seed replication at s=0.5). The pre-registered C3 is non_contributory, so **the replication the decision waits on did not land**. Two post-hoc observations are evidence about the calibration choice, not a verdict:
  - The pre-registered C3 was scored on the 2 ready seeds only; 1 of the 2 shows the boundary.
  - The same contrast run post-hoc on all 5 seeds (the reset-OFF floor arms need no closure fire): **3/5 replicate** (42 0.239 vs 0.000; 45 0.861 vs 0.139; 46 0.867 vs 0.040), **1/5 both-release** (43 0.790 vs 0.732, pe_unsat 2.12), **1/5 neither-release** (44, pe_unsat 5.61). Both exceptions come from pe-scale dependence.
  - pe_unsat p50 spans 2.1-5.6 across trained seeds.
  - Together these favour a scale-normalising route over a fixed-floor default.
- **GFLAG-0466:** corroborated on 5 seeds.
- **GFLAG-0467:** the commitment_closure GAP-4 rows should record 1089 as non_contributory (readiness), not as a pending or delivered replication.
- **commitment-closure-control-plane** (the 7b C2 pointer): the not-ready seeds are a regime where closure cannot fire under a held action. However, rule_state is truncated there, not broken, so a fresh-tick-denominated eval should make those seeds ready without that build. No amend is recommended.

## 10. Non-outcome observations

- Latch-dominated seeds respawned far less (6-21 respawns vs 51-75 in 1200 steps).
- Saturation ON vs SATOFF releases the soft register on 4/5 seeds at s=0.5. Where the stream is shared, this is arithmetic (dacc_weight 0 and pe_unsat x 0.25 < 1).
  - The stream is shared across all 9 arms only on seeds 42/43/44. On seed 45, SATOFF differs from the sat arms (322 vs 281 fresh ticks), and on seed 46, K24 differs from K6. This is plausibly the driver's F4 path (soft mode -> sd_033a -> lateral PFC).
  - Within every ON/OFF bracket the stream is identical, so C1's attribution is intact.
- P0 nav_competence was 0.0 at every probe on every seed, while rv converged to about 1e-6.

## 11. Hypothesis-space ledger (Step 9b)

No fan-out. No registered question names MECH-268 or V3-EXQ-1089; the nearest, `mech266_mode_arbitration_saturation`, carries MECH-266/SD-032a. A readiness-vacated run discriminates no leg. The registry was not written.

## 12. Step 7b / 7c and coordination

- **7b** (run with an explicit `--as-of`, 3 fires):
  - C1 (driver v3_exq_463 exists): **dismissed**. It is the synthetic mechanism-level falsifier (PASS 2026-04-21), a different question.
  - C2 (commitment-closure-control-plane): **acted on** as a bears-on note, with no amend, per the red-team recompute.
  - C6 (minority-seed arm divergence on 45/46): **acted on**. The shared-stream absolute is now qualified to within-bracket.
- **7c** red-team on **fable** (cross-model; drafted on Opus 5.5): **CONFIRMED**.
  - Every number recomputed from the 45 cells: C1 0.17586/0.0 with margin 0.17586; readiness; fresh/latched counts; headroom 4/5 over all seeds (driver l.697-699); seed-44 arithmetic 1.403.
  - Framing correction F-A (the 3/5 + 1/5 + 1/5 wording) was applied.
  - Hygiene H1-H6 were applied: timestamp; commit attribution; within-bracket stream; requeue cost; seed-44 timing caveat; the hold mechanism named.
  - It also corrected this draft's claim that seed-43 agents would be lost "whatever the eval length".
  - Findings: `.scratch/orch-20260924-1707/autopsy/redteam_1089.md`.
- **Coordination-plane pause:** not opened. The pause resources return NOT the owner (exit 3), because orchestrate-20260924-1707 science workers hold the queue files. This autopsy writes none of them.
