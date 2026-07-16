# Failure Autopsy — V3-EXQ-765 (MECH-457 competence bootstrap-explorer, post-build retest)

- **Generated (UTC):** 2026-07-16T15:57:45Z
- **Scope:** single
- **Status:** confirmed (interactive gate cleared)
- **Run:** `v3_exq_765_mech457_bootstrap_explorer_competence_20260716T122726Z_v3`
- **Queue:** V3-EXQ-765 (diagnostic; experiment_purpose=diagnostic; PROMOTES/DEMOTES NOTHING)
- **Claim:** MECH-457 (`action_learning_as_first_class_actor_critic_substrate`; candidate / v3_pending)
- **Outcome:** FAIL — `discrimination_verdict: bootstrap_explorer_plateaus_capacity_gap_remains`
- **Ran to completion:** yes. Recording core validated OK (`validate_recording.py` — `substrate_hash` + `config` + `seeds` all present, 0 always-core gaps). Not a crash; autopsy applies.

## 1. Facts (no interpretation)

Substrate `mech457_competence_bootstrap_explorer` was BUILT 2026-07-16 (ree-v3 main 022a284) to close the MECH-457 competence-floor gap: it composes the landed RND success-independent drive + prioritized credit-replay converter + a NEW developmental intrinsic-coef/entropy anneal + 3x budget on the first-class actor-critic, on BOTH z_world (cotrain) and raw 5x5. V3-EXQ-765 is its Step-8 validation.

| Arm | Rep | forage mean (per-seed) | vs floor 1.0 | vs lift-target 13.05 |
|---|---|---|---|---|
| local_view_greedy (readiness) | env | **48.05** (45.75/49.7/48.7) | PASS | achievable ceiling |
| greedy_oracle (readiness) | env | **57.2** (57.0/57.3/57.3) | PASS | privileged anchor |
| random_walk | env | 0.93 | ~floor | — |
| boot_OFF | z_world | 5.22 (4.7/4.75/6.2) | PASS | reproduces RND plateau (drift-guard OK) |
| **boot_ON** | z_world | **0.35** (0.25/0.3/0.5) | FAIL | **ON HURTS: on_minus_off = -4.87** |
| boot_OFF | raw 5x5 | 0.62 (0.5/0.15/1.2) | sub-floor | — |
| **boot_ON** | raw 5x5 | **6.48** (0.5/3.05/15.9) | mixed | **ON helps +5.87, plateaus; 1/3 seeds supra-target** |

Reference band: floor 1.0 · RND plateau (751) 5.22 · BC expert (748) 32.72 · local-view ceiling (738) 48.05 · oracle (742) 57.2 · lift-competence target 13.05 (= 5.22 plateau + 7.83 margin).

- **Readiness / negative control PASSED:** the env is solvable from the identical 5x5 local view (48.05) and with global info (57.2), both >> the 1.0 floor. `readiness_met: true`.
- **Load-bearing discrimination criterion FAILED:** `C_bootstrap_ON_clears_lift_competent_either_rep = false`. ON clears the 13.05 lift-competence target on NEITHER representation, on a strict majority of seeds.
- **Converter demonstrably ran:** `n_credit_replay_passes` 4500-8259 on the ON arms; the drive/converter machinery fired, this is not a no-op.
- **Expected vs observed:** expected ON to lift foraging >= 7.83 above the 5.22 plateau toward BC 32.72 on at least one representation. Observed: raw ON lifts +5.87 but caps at ~6.5 (barely above the RND plateau, ~13% of the 48.05 achievable ceiling); z_world ON collapses BELOW its own OFF plateau.

This is the substrate-ceiling fingerprint: env-solvable control passes, the discrimination criterion fails.

## 2. Claim-layer map

MECH-457 = a dedicated RPE-driven actor-critic policy-learning substrate (dorsal-striatal actor + value-baseline critic), architecturally distinct from the thin bias_head REINFORCE readout. Status candidate / v3_pending / pending_retest_after_substrate. Deps SD-056 (built) + MECH-229 (built).

**Did the test let the claim express itself?** Partially. The actor-critic + composed drive ran to full budget with readiness satisfied, so the mechanism had its chance. It did NOT reach competence — but the *drive half* of the composed mechanism is now weakly supported (raw ON +5.87 over OFF is a real, converter-driven lift), while the *capacity half* (convert coverage -> competent foraging) is what plateaus. The FAIL therefore weighs against the *current build's sufficiency at this capacity/budget*, NOT against the MECH-457 claim itself. `claim_ids=[MECH-457]` is correct (not an inherited-tag error).

This sits inside the GOV-GRAN-1 **coherent-campaign** disposition (session gifted-kilby-8e2491, landed 50452771aa): the 750-756 recurrence is progressive localization of ONE competence-bootstrap gap (success-independent drive + actor-critic capacity), not a too-coarse claim. `/claim-synthesis` is CONTRAINDICATED — every candidate sub-claim already has an owner (ARC-065/MECH-314 curiosity, MECH-455 competence-drive, INV-088 diversity). 765 is a new hit *within* the campaign, not a new granularity signal.

## 3. Biological-reference triage

- **Closest mechanism:** dorsal-striatal actor taught by a dopaminergic RPE signal (O'Doherty 2004; Schultz 1997), here scaffolded by a novelty/curiosity drive (RND) + consolidation replay + a developmental explore->exploit anneal (a maturational curriculum analog).
- **Formal-import status:** grounded in biology (5 canonical lit entries in `targeted_review_actor_critic_action_learning/`), NOT a bare formal import. No new lit-pull owed.
- **Missing-dependency signature?** Yes. Biologically, a curiosity drive + replay are necessary but not sufficient for skilled foraging — the motor/policy apparatus must have the representational capacity and training horizon to convert exploration into competent control. The plateau (drive present, competence not reached) matches an **under-capacitated actor / immature policy horizon**, i.e. a discovered prerequisite, not a falsification of the actor-critic mechanism class.
- **Subordinate finding — z_world cotrain is destructive** (ON 0.35 < OFF 5.22): co-shaping the prediction-trained encoder with the explorer drive corrupts z_world. Biologically consistent with the decoupled-representation caution (Stooke 2021): train the policy on top of the frozen self-supervised encoder, do not let the RL drive rewrite it. The build should default the z_world path to **detached**.
- **Subordinate finding — high seed variance on raw** (seed 44 = 15.9 supra-target; 42/43 = 0.5/3.05): the mechanism *can* convert but unreliably — pointing the residual partly at credit-reliability / exploration-depth, not purely network size. The capacity build should include reliability / warm-start, not just a bigger hidden dim.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (drive-axis weakly strengthened) | test let the claim express itself; drive half supported on raw, capacity half untested-to-competence. No demotion. |
| Biological reference | clear | dorsal-striatal actor + developmental exploration scaffold; plateau matches under-capacitated actor (missing-dependency signature). |
| Developmental / dependency prerequisites | present (drive) / immature (capacity) | RND + credit-replay + anneal all built and fired (n_credit_replay_passes 4500-8259). Remaining prerequisite = adequate policy capacity / training horizon. |
| Implementation completeness | partial | composed explorer complete and runs, but at a capacity/budget insufficient to reach competence; z_world cotrain path destructive. |
| Environment adequacy | adequate | readiness proves env solvable from the local view (48.05 achievable). |
| Measurement adequacy | adequate | foraging_competence + grounded denominators + well-formed lift target. Recording complete (substrate_hash present) -> ceiling reading is falsifiable, no recording gap. |
| Integration adequacy | partially coupled but unstable | z_world encoder-cotrain coupling DEGRADES competence (ON < OFF); raw (no encoder coupling) helps. |
| Scale / capacity | **likely insufficient (dominant)** | actor_critic_hidden=128, on_budget=3000 ep; raw plateaus 6.48 vs 48.05 achievable. Verdict = "capacity_gap_remains". |

**Recommended epistemic_category:** `competence_implementation_gap` (consistent with the 752-756 campaign; NOT `substrate_ceiling` — the gap is a named buildable capacity increase = `complicated (buildable)`, and preserving 0 substrate_ceiling verdicts keeps GOV-CEIL-1 unaffected).

## 5. Learning extracted

1. The composed bootstrap explorer's **drive half works** on raw (RND + credit-replay + developmental anneal lifts raw foraging 0.62 -> 6.48, a real converter-driven +5.87); the **capacity-to-convert half remains the wall** (plateau at ~13% of the 48.05 achievable ceiling). The two-joined-halves campaign read is confirmed at the post-build layer.
2. **z_world cotrain is destructive** (ON below OFF plateau) — the explorer drive corrupts the prediction-trained encoder. Future builds must detach the z_world path (train policy on frozen encoder), per Stooke 2021.
3. **Seed variance on raw is large** (one seed clears target, two stall) — the residual is partly credit-reliability / exploration-depth, not pure network capacity. The capacity build should raise reliability (warm-start / variance reduction), not only hidden-dim.
4. MECH-457 the CLAIM is neither confirmed nor falsified: the biology supports the mechanism class; the build simply has not reached competent capacity. Demotion threshold (tested fairly + biology supports + still fails at adequate capacity) is NOT met, because capacity was NOT adequate.

## 6. Repair pathway & routing

- **Node classification:** `complicated (buildable)` — the fix is a named build (raise actor-critic capacity/budget + reliability + detach z_world cotrain), no open discrimination. NOT a `complex (probe-gated)` node → do NOT queue another spike.
- **Routing:** `implement-substrate`. **Amend** the existing `mech457_competence_bootstrap_explorer` substrate_queue entry (status flips off "implemented"): record the 765 failure and the capacity-side next build.
- **Re-derive brake: FIRED.** This is the 5th non_contributory MECH-457 autopsy (751-750, 752-753-754, 755, 746c-756 → 765). The prior brake routed to build `mech457_competence_bootstrap_explorer`, now built and retest-failed. The brake **explicitly REFUSES** any fresh same-question explorer-mechanism re-queue — no new H-* leg, no mode-gate retune, no combination cell. The only sanctioned next step is the capacity-side substrate build named here, followed by its own post-build retest. Upstream substrate to build first: `mech457_competence_bootstrap_explorer` (capacity amend).
- **No fanout.** The bottleneck routes to one unambiguous build (capacity + reliability + z_world detach are three knobs on the SAME build, not competing hypotheses needing a discrimination portfolio). GOV-FANOUT-1 does not apply.
- **MECH-457 stays candidate / v3_pending / pending_retest_after_substrate.** No claim confidence write (diagnostic, excluded from scoring). INV-088 stays candidate / pending_substrate_reconfirmation.

### Draft `evidence_quality_note` for /governance to append to MECH-457

> 2026-07-16 (V3-EXQ-765, diagnostic, claim_ids=[MECH-457]; failure_autopsy_V3-EXQ-765_2026-07-16): post-build retest of the composed `mech457_competence_bootstrap_explorer` substrate RAN and FAILED (`bootstrap_explorer_plateaus_capacity_gap_remains`). Readiness PASSED (local_view_greedy 48.05, oracle 57.2 vs 1.0 floor -- env solvable from the 5x5 view). The composed DRIVE half works on raw (ON 6.48 vs OFF 0.62, +5.87 converter-driven lift; n_credit_replay_passes 4500-8259) but the CAPACITY-to-convert half persists: raw ON plateaus at ~13% of the 48.05 achievable ceiling and clears NEITHER representation's 13.05 lift-competence target. Two subordinate findings: (1) z_world cotrain is DESTRUCTIVE (ON 0.35 < OFF 5.22 -- explorer drive corrupts the prediction-trained encoder; detach the z_world path per Stooke 2021); (2) high seed variance on raw (15.9 / 3.05 / 0.5 -- convert-ability is unreliable, residual partly credit-reliability, not pure capacity). epistemic_category competence_implementation_gap (0 substrate_ceiling verdicts preserved; GOV-CEIL-1 unaffected); evidence_direction non_contributory (diagnostic, PROMOTES/DEMOTES NOTHING). Re-derive brake FIRED (5th non_contributory MECH-457 autopsy): REFUSE any fresh same-question explorer-mechanism re-queue; route = implement-substrate capacity-side amend of mech457_competence_bootstrap_explorer (raise policy capacity/budget + reliability/warm-start + z_world cotrain detach). MECH-457 stays candidate/v3_pending. This is a NEW hit within the GOV-GRAN-1 coherent-campaign disposition, not a granularity signal.

### Recommended substrate_queue amend (for /governance to apply)

Amend `mech457_competence_bootstrap_explorer` (unblocks MECH-457, INV-088): add the 765 failure record; set the capacity-side build as the next work — (a) raise actor-critic policy capacity + training budget; (b) improve credit reliability / warm-start to cut the seed variance; (c) default the z_world path to detached (train policy on frozen encoder). Priority 1 (fresh failure record + blocks MECH-457 promotion).
