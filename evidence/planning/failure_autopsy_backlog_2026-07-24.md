# Failure Autopsy -- 2026-07-24 pending backlog (batch)

Generated: `2026-07-24T18:59:26Z` | scope: cluster/batch | status: confirmed (all Step-8 judgments user-confirmed)

Adjudicates the 24 pending FAIL / flagged-diagnostic runs that accumulated on `origin/master` since the
2026-07-24 08:05Z governance walk (V3-EXQ-811 was autopsied separately). The prior `/governance` cycle
(`honest-galois-7d2e9c`) aborted at Step 1.5 having surfaced this backlog; this artifact clears the analysis
so `/governance` can apply it. Machine-readable per-target routing is in the sibling `.json`.

**Default stance:** brains are an existence proof for the mechanism *class*; a FAIL is a
translation/dependency/measurement/environment gap until the biology says the mechanism itself is wrong.
Demotion is the highest bar. All manifests ran to completion and carry `substrate_hash` (no unfalsifiable-ceiling
recording gap).

---

## C1 -- `substrate_not_ready_requeue` family (6): one self-route, three realities

The convergent self-route is **not one bug**. Adjudicated each against the V3-EXQ-642 test (was the branch's
premise genuinely unmet, or is the precondition test itself wrong?):

| Run | Claim | Unmet gate | Reality | ev_dir / category | Route |
|---|---|---|---|---|---|
| `801` | ARC-018 | `e2_world_r2_adequate` FALSE (all arms) | **Genuine** -- forward model too weak to roll out | non_contributory / substrate_conditional | implement-substrate; `pending_retest` |
| `800` | ARC-007 | `executed_action_diversity` FALSE | **Genuine** -- agent didn't act diversely enough to read dissociation | non_contributory / substrate_conditional | implement-substrate; `pending_retest` |
| `629c` | MECH-342 | contact_rate 0; 3 gates false | **Test-bed** -- ecological scenario never materialised | non_contributory / **measurement_test_design_defect** | queue-experiment |
| `805` | ARC-016 | `precision_manipulation_took` FALSE | **Measurement** -- lever never moved rv (EXQ-396 void mode) | non_contributory / measurement_test_design_defect | queue-experiment + governance re-score flag |
| `699b` | MECH-448/449 | `gapa_consumed_summary_divergence` FALSE | **Instrument-repair** -- WITHDRAWS 699 `levers_compound` | non_contributory / measurement_test_design_defect | queue-experiment + governance withdraw |
| `813` | (fan-out) | `consumption_share_dominates` FALSE | **FALSE self-route** -- criteria discriminate cleanly | **weakens** / standard | governance (see C3) |

- **629c categorised `measurement_test_design_defect`, NOT `substrate_ceiling`**, deliberately: it would
  otherwise be MECH-342's 2nd re-derive-brake ceiling hit, but "the foraging scenario never set up" is a
  test-bed defect, not a ceiling.
- **805** additionally surfaces a governance-only item the manifest raises: ARC-016 `exp_conf 0.53` is an
  aggregation artefact of ~15 non_contributory/stale FAILs; re-scoring needs a governance eye (stripping the
  non-contributory FAILs may expose thinner remaining supports). ARC-016's core circuit is already validated
  (018b 5/5, 060 4/5); this run promotes/refutes nothing.
- **699b** is an instrument repair: it WITHDRAWS 699's `levers_compound` finding (699's DV was
  hold-duration-weighted occupancy entropy, biased toward the hypothesis) -> `levers_neutral`. 699's C1
  readiness battery STANDS.

## C2 -- `harm_advantage_not_reproduced` cluster (3): the load-bearing finding

`120a` (ARC-018, -18.1%), `114a` (ARC-007, 11.4%), `266b` (Q-020, 6.5%) share an identical decisive shape:
once selection is E3-routed, the DV is harm/episode at a **matched budget**, and a **static no-op control** is
present, the harm-reduction advantage collapses below the 15% bar. All P1-green (genuine E3 choice) =>
**measurement, not instrument** failures; all criteria non-degenerate; **decision-flipping negatives, not nulls**.

**Structural property (not 3 independent bugs):** the *sole behavioural* supports for these three claims were
**denominator artefacts of a constant-action stream** (114a's own note: EXQ-114's 99.2% was such an artefact).
None survives the matched-budget / E3-routed / static-control redesign. **USER-CONFIRMED `weakens` for all three.**
The mechanism-class existence-proof stays intact; the *translation* to a harm-navigation advantage is what fails
uniformly.

## C3 -- `conversion_ceiling_root` fan-out (734, 808, 813) -- live GOV-FANOUT-1 discrimination

State of the root-cause discrimination for the conversion/competence ceiling (MECH-457/ARC-065):

- **734** (20260722 re-run, z_world guard **GREEN**, unlike the earlier invalidated run): REE all-ON recovers at
  **no** difficulty rung; vanilla PPO recovers at D2. Valid corroboration of `H-substrate-ceiling`.
  `non_contributory` / `competence_implementation_gap`; extends the confirmed 734/737b/742a cluster.
- **808** (reward axis): the return is **survival-dominated** (consumption share 0.28 < 0.5), so the objective IS
  misspecified as hypothesised (**confirmed**); but **reweighting does NOT move competence** (C2 0.33, non-degenerate).
  Reading: misspecification is real but **not the removable lever** -- `H-objective-misspecification` is displaced as
  the actionable root, not eliminated. Live discrimination passes to policy/representation.
- **813** (policy axis, the false self-route): PPO on **raw obs clears the floor (9.03)**; PPO on the **REE latent
  does not (0.5)** under the identical survival-zeroed objective. **USER-CONFIRMED override:** ELIMINATE
  `H-policy-learning` (a competent external actor learns the policy fine) and ELEVATE a
  **representation / observation-interface** hypothesis (the REE latent does not expose foraging-adequate structure
  to a downstream reader). Registered in the frozen ledger (Step 9b).

## C4 / C5

- **689j** (MECH-448): 3 non-vacuity gates pass; `C_NOISE_LIFTS_REPOWERED` fails -- matched-noise control can't be
  verified to lift. MECH-448's primary is already SUPPORTED by 689i (PASS on C_PRIMARY); 689j is the narrow
  non-gating follow-up, so MECH-448 is unaffected. Lineage 689a->d->i->j is long -> recommend **closing** the
  noise-control axis rather than another lettered repower.
- **786b** (MECH-163): repaired retest of 786a (DV degeneracy confirmed 2026-07-24). `no_differential_recruitment`
  (C1 non-degenerate) -- first genuine V3 exp evidence on the dual-system recruitment leg. **USER-CONFIRMED `weakens`
  (leg 1).** Pairs with 811's MECH-477 supports: the arbitration fires but the novelty-graded differential-recruitment
  signature does not reproduce.

## Singletons (11)

| Run | Claim | Verdict | ev_dir / category | Route |
|---|---|---|---|---|
| `802` | ARC-005 | dissociation+reproducibility hold, **monotonicity fails** | mixed / standard | governance (partial; ARC-005 stays active) |
| `669c` | MECH-329/189 | wanting seeds more anchors, **ordering not shown** | mixed / standard | governance (supersedes 669b) |
| `804` | ARC-003 | score gradient present, no selection authority; KL 0.0507 vs 0.0588 (narrow), **leg A only** | weakens (narrow) / standard | governance (marginal weight) |
| `799` | MECH-048 | mechanism fires (mu->entropy), **no behavioural consumer** | non_contributory / competence_implementation_gap | **implement-substrate** (write_gate breadth) |
| `708b` | MECH-440 | precommit-shape headroom unexplained; levers didn't move DV | non_contributory / measurement_test_design_defect | queue-experiment |
| `810` | ARC-071/323/324 | chunk accumulator **silent** (never crystallises) | non_contributory / competence_implementation_gap | **implement-substrate** |
| `794a` | MECH-204/SD-076 | DV **still tautological** + drift source insufficient | inconclusive / measurement_test_design_defect | queue-experiment (DV redesign) |
| `812` | MECH-295 | `INVALID_HARNESS` (cue fires, DiD ~1e-9) | non_contributory / measurement_test_design_defect | queue-experiment (harness) |
| `798` | (none) | producer graded but **not learnable** | non_contributory / measurement_test_design_defect | queue-experiment (test-bed) |
| `792a` | MECH-457 | flagged vacuous_pass but **genuine PASS** (dose-response demoted, measured-drift-suppression criterion passed) | **supports** / standard | governance (first retention-consolidation support) |
| `797` | MECH-266/SD-032a | `commitment_layer_starved`; H1/H2 pre-falsified -> localises to BG commitment | non_contributory / substrate_conditional | **implement-substrate** (BG commitment layer) |

---

## Routing summary

- **governance-demotion (weakens):** 120a, 114a, 266b (C2 cluster), 786b, 804.
- **governance (mixed / supports / partial):** 802, 669c, 808, 792a (supports), 813 (fan-out).
- **implement-substrate:** 801, 800, 799, 810, 797 (+ 813 elevates the representation leg).
- **queue-experiment (redesign / test-bed):** 629c, 805, 699b, 689j, 708b, 794a, 812, 798.
- **governance-only items surfaced (not this skill's to apply):** ARC-016 exp_conf re-score (805);
  withdraw 699 `levers_compound` (699b).

## Hypothesis-space ledger (Step 9b)

`conversion_ceiling_root` updated: `H-policy-learning` -> eliminated (813 raw-obs-clears discrimination);
`H-objective-misspecification` -> resolving run 808 recorded, stays alive (misspecification confirmed but not the
lever); new leg `H-observation-interface` (representation axis) pre-registered + elevated via 813 as labelled
fan-out growth; `H-substrate-ceiling` corroborated by the valid 734 re-run. See registry + integrity report.
