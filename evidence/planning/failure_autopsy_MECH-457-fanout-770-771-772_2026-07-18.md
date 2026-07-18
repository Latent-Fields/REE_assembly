# Failure Autopsy — MECH-457 GOV-FANOUT-1 discrimination portfolio (V3-EXQ-770 / 771 / 772)

- **Generated:** 2026-07-18T04:34:55Z
- **Scope:** cluster (3 legs of one fan-out)
- **Status:** confirmed (user-adjudicated at the Step 8 gate)
- **Claim under test:** MECH-457 (dedicated RPE-driven actor-critic action-learning substrate)
- **Routed by:** [failure_autopsy_V3-EXQ-769_2026-07-17](failure_autopsy_V3-EXQ-769_2026-07-17.json) (which pre-registered exactly these three legs + their nulls)
- **Analysis + handoff only** — no claims.yaml / manifest / review_tracker / substrate_queue edits. Governance applies the recommended writes.

---

## 1. Facts — the three legs

All three ran to completion, all **FAIL**, all `non_degenerate=True`, all share `substrate_hash f56e1a7e` (the **non-regressed reference build**: 128-wide actor / 3× budget / z_world detached — the 765 config, NOT the 769-falsified 256/5×). Seeds `[42,43,44]`, cloud class `linux-x86_64-py3.10`. Recording complete (`validate_recording` OK on all three; always-core + substrate_hash present).

| Leg | EXQ | Axis manipulated | Self-route label | Load-bearing criterion | Passed? |
|---|---|---|---|---|---|
| H1 | 770 | intrinsic-drive anneal **schedule** (sustained coef 1.0 vs annealed 1.0→0.05) | `drive_schedule_not_the_axis` | `C_sustained_drive_clears_lift_competent_either_rep` | **false** |
| H2 | 771 | env **reward-coupling** (metabolic forage-to-survive; contamination off + energy→health starvation) | `reward_coupling_not_the_axis` | `C_metabolic_coupling_clears_lift_competent` + aliasing guard | **false** |
| H3 | 772 | training **credit-horizon** (dense potential-based forage shaping, Ng 1999; unshaped eval) | `credit_horizon_not_the_axis` | `C_dense_credit_clears_lift_competent_either_rep` | **false** |

### Per-arm foraging_competence (the load-bearing DV)

Reference bands (shared): floor **1.0**, RND novelty plateau **5.22**, BC expert **32.72**, local-view ceiling **48.05**, greedy-oracle **57.2**; lift-competence target **13.05** (5.22 plateau + 7.83 margin).

| Arm | 770 (z_world / raw) | 771 (z_world / raw) | 772 (z_world / raw) |
|---|---|---|---|
| ctrl | 0.65 / 7.22 | 0.30 / 2.98 | 0.65 / 7.22 |
| treat | 0.88 / 0.90 | 0.42 / 0.62 | 0.33 / 0.58 |
| decouple (771 only) | — | 3.05 / 0.55 | — |
| **local_view_greedy** | **48.05** | **55.53** | **48.05** |
| **greedy_oracle** | **57.20** | **60.77** | **57.20** |
| random_walk | 0.93 | 1.47 | 0.93 |

**Every treatment arm forages at the floor (~0–1), statistically indistinguishable from `random_walk`, on both representations, under every manipulation.** Meanwhile a hand-coded greedy policy reading the learner's **own 5×5 `resource_field_view`** forages 48–55. The observation is provably sufficient; the learned converter extracts nothing.

**One live covariate:** on the **raw** 5×5 view a single seed occasionally partial-climbs (`*_ctrl_raw` per-seed `[0.9, 19.3, 1.45]` in 770/772; the 765 clearing seed 15.9). On **z_world** (the SD-056 prediction latent) it *never* does. → high-variance cold-start collapse into the passive-survival basin; the prediction-trained encoder is actively worse for the actor than the raw view.

## 2. Convergent shape — one structural property, not three bugs

These are **not** three independent bugs. Each leg's declared null (pre-registered in the 769 autopsy) hit exactly:

- H1 null: *"sustained/approach-first drive still leaves ON at passive-survival collapse (forage ~0) → ordering is not the operative axis."* ✔
- H2 null: *"even when survival requires foraging, ON does not reach competent foraging → reward-decoupling is not the wall."* ✔ (metabolic treat forages ~0.4 → the actor *dies/collapses* rather than learning to forage even when survival demands it.)
- H3 null: *"even with dense/oracle-shaped forage credit, ON does not reach competent foraging → the wall is deeper than credit horizon (representation ceiling or a different mechanism class)."* ✔

**Structural property:** the learned actor-critic converter cannot extract a competent foraging policy from a *sufficient* observation, and this is **invariant to drive-schedule, reward-coupling, and credit-horizon**. Combined with V3-EXQ-769 (capacity axis: raw ON 6.48→0.12 **regressed**), the campaign has now eliminated **four axes: capacity, drive-schedule, reward-coupling, credit-horizon.**

## 3. Claim-layer mapping

MECH-457 asserts a *dedicated* RPE-driven actor-critic is **required** for competent action learning. The substrate was built (`ree_core/action_learning/actor_critic.py`, 2026-07-12) and composed into `mech457_competence_bootstrap_explorer`. The fanout does **not** falsify the claim — it shows the actor-critic is **necessary-but-not-sufficient**: it exists, fires (credit machinery logs 9k–18k replay passes), but has **nothing competence-directed to bootstrap from**. The test let the claim express itself (readiness met, env solvable from the local view), and the substrate still cannot convert — but that localizes a *missing dependency*, not a false claim.

## 4. Biological-reference triage

| Field | Reading |
|---|---|
| Closest mechanism | dorsal-striatal actor-critic action learning (O'Doherty 2004 actor; Schultz 1997 dopaminergic RPE teacher) |
| Dependencies in real brains | pre-instrumental **approach primitives** (PAG / hypothalamic appetitive drives, collicular orienting); **imitation / observational learning**; species-typical behavioral priors; scaffolded developmental progression |
| Is formal import? | partial — RPE actor-critic is biologically grounded, but the REE composition asks it to **cold-start** a forager from RPE-on-a-prediction-encoder, which no mammal does |
| Divergence (load-bearing) | mammals never learn foraging from scratch via intrinsic RPE; they inherit approach primitives and/or imitate conspecifics. The **one arm that ever cleared REE's floor was BC (imitation, 32.72)**; every self-supervised/intrinsic route (RND 5.22, SD-025, and now all four axes) fails. The 4-fold elimination is exactly the missing-dependency signature. |
| lit status | present for the actor-critic substrate; the **behavioral-prior / imitation-bootstrap dependency** is the load-bearing gap the elimination isolates |

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | MECH-457 necessary-but-not-sufficient; test let it express itself; not falsified |
| Biological reference | clear | dorsal-striatal actor-critic; failure matches "actor with no competence-directed bootstrap" |
| Developmental / dependency prerequisites | **missing** | the pre-instrumental approach primitive / imitation seed (the BC-clears-floor dependency) is absent |
| Implementation completeness | complete (for the tested axes) | drive/reward/credit/capacity all built + exercised; none is the wall |
| Environment adequacy | adequate | env solvable from the 5×5 local view (local_view_greedy 48–55, oracle 57–61) — provably sufficient |
| Measurement adequacy | adequate | `non_degenerate=True`; controls clear floor; margin/foraging DV non-vacuous |
| Integration adequacy | coupled but unstable | actor rides z_world worse than raw; high-variance cold-start collapse into passive-survival basin |
| Scale / capacity | adequate → **falsified as the axis** | 769 showed scaling capacity *regresses*; not the wall |

**Dominant diagnosis:** missing developmental dependency (competence-directed bootstrap). `epistemic_category: competence_implementation_gap` (NOT `substrate_ceiling` — 0 ceiling verdicts preserved, GOV-CEIL-1 unaffected). `evidence_direction: non_contributory` (diagnostic, promotes/demotes nothing).

## 6. Cluster pattern table

| Experiment | Claim | Negative-control / absolute (readiness) | Discrimination criterion | Read |
|---|---|---|---|---|
| 770 H1 | MECH-457 | local_view 48.05 ✔ / oracle 57.2 ✔ (floor 1.0) | sustained drive clears 13.05 lift, both reps — **false** | drive-schedule not the axis |
| 771 H2 | MECH-457 | local_view 55.5 ✔ / oracle 60.8 ✔ | metabolic coupling clears 13.05 + beats decouple by 7.83 — **false** | reward-coupling not the axis |
| 772 H3 | MECH-457 | local_view 48.05 ✔ / oracle 57.2 ✔ | dense credit clears 13.05 lift, both reps — **false** | credit-horizon not the axis |

**Reading:** one structural property (converter cannot extract a competent policy from a sufficient observation, invariant to all tested axes), **not** N independent bugs. The two live readings from H3's null — *representation ceiling* vs *a different mechanism class (missing competence-directed dependency)* — are now discriminated toward the latter by the BC existence proof and the passive-survival-basin signature (an actor that could ride the representation would not collapse to do-nothing when a greedy policy on the same view forages 48).

## 7. Learning extracted + repair pathway

**Learning:**
1. The MECH-457 competence floor is **invariant to capacity, drive-schedule, reward-coupling, and credit-horizon** (four-fold elimination across 765/769/770/771/772).
2. The missing piece is a **competence-directed bootstrap** — the actor needs something that *directs* it toward earning competence, which no intrinsic/self-supervised route (RND, SD-025, novelty, dense credit, metabolic pressure) supplies. BC (imitation, 32.72) is the only floor-clearing existence proof.
3. The passive-survival basin is the attractor: absent a competence-directed seed, more optimization drives the policy into avoidance-without-approach (confirmed 769 behavioral signature; reproduced here — treat arms collapse to random-walk-level foraging even under metabolic starvation pressure).
4. z_world (SD-056 prediction latent) is actively worse for the actor than the raw 5×5 view — a recurring, now-triply-confirmed finding.

**Node classification:** `complex (probe-gated) / puzzle (known rules)` — the frame is well-posed (the actor needs a competence-directed bootstrap) but **which dependency** (a learned behavioral prior vs an innate non-extinguishing approach primitive) is an open fact with ≥2 live, buildable-but-distinct hypotheses. → **spike = a fan-out `/queue-experiment` portfolio**, not a single blind build (user-chosen at the Step 8 gate).

**Routing: `queue-experiment` — GOV-FANOUT-1 discrimination portfolio.** The re-derive brake FIRES (7th non_contributory MECH-457 autopsy) and **refuses any further config/env/credit/capacity re-pose**. It **permits** this fan-out: NEW EXQ numbers on DIFFERENT mechanism classes (the same sanction under which 769→770/771/772 was permitted), not another letter circling the tested axes.

### Recommended fan-out (2 legs, each with a declared null, different axes, aliasing-audited)

- **H-bc-prior** (axis: learning-signal / supervised) — seed the actor with a competence-directed **behavioral prior**: BC-of-policy warm-start / imitation auxiliary loss distilled from the floor-clearing demonstrator (local_view_greedy or greedy_oracle). Existence proof: the BC arm clears the floor (32.72).
  - **Null:** even seeded by imitation of a floor-clearing demonstrator, the composed actor collapses back to passive-survival at unshaped eval → the deficit is not a missing behavioral prior but something that *erases* the seeded policy (points to a stability / representation-riding failure).
- **H-approach-primitive** (axis: intrinsic architecture / drive) — an innate, **non-extinguishing, competence-directed approach drive** (a subcortical appetitive-approach analog toward resources), architecturally distinct from novelty-class drives (RND / SD-025) that self-attenuate via familiarity. Must be **demonstrator-free** (a resource-gradient intrinsic approach, not distilled from expert demos) to avoid verdict-aliasing with H-bc-prior.
  - **Null:** a sustained competence-directed approach drive still leaves the actor in passive-survival → the missing piece is not an approach drive but the learned imitation/behavioral-prior dependency.

**Aliasing audit:** the two legs sit on different axes (supervised learning-signal vs intrinsic architecture). To keep them non-aliasing, H-approach-primitive must NOT derive its signal from a demonstrator. Both legs should record the raw-vs-z_world covariate (does the seed survive on raw but not z_world?) so a representation-riding failure is separable from a bootstrap-content failure.

### Recommended substrate hand-off (for the eventual build)

`recommended_substrate_queue_entry.action = amend`, `target_sd_id = mech457_competence_bootstrap_explorer`: record that the 770/771/772 portfolio RAN and eliminated drive/reward/credit; the next build is decided by the H-bc-prior vs H-approach-primitive discrimination (do NOT build a config/env/credit amend). Priority 1 (blocks MECH-457 + INV-088).

## 8. Governance hand-off (recommended writes — do NOT apply here)

- **MECH-457:** append the `evidence_quality_note` below; stays candidate/v3_pending; PROMOTES/DEMOTES NOTHING; 0 substrate_ceiling verdicts preserved (GOV-CEIL-1 unaffected).
- **INV-088:** stays candidate/pending_substrate_reconfirmation — the 770/771/772 portfolio was its re-routed reconfirmation path; reconfirmation did not occur; unblock re-routed onto the new H-bc-prior / H-approach-primitive portfolio.
- **Manifests:** mark 770/771/772 reviewed (governance Step 5). Diagnostic, `claim_ids=[MECH-457]`, `evidence_direction non_contributory`.

### Draft `evidence_quality_note` (exact text governance should append to MECH-457)

> 2026-07-18 (V3-EXQ-770/771/772, diagnostic cluster, claim_ids=[MECH-457]; failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18): the GOV-FANOUT-1 discrimination portfolio routed by the 769 autopsy RAN and all three FAILED, each hitting its pre-registered null. Readiness PASSED on every leg (local_view_greedy 48.05–55.53, oracle 57.2–60.77 vs the 1.0 floor — env solvable from the 5×5 local view). Every treatment arm foraged at the floor (~0–1, indistinguishable from random_walk) on BOTH z_world and raw, under drive-schedule (770), metabolic reward-coupling (771), and dense credit-horizon (772) manipulations. Verdicts drive_schedule_not_the_axis / reward_coupling_not_the_axis / credit_horizon_not_the_axis; all non_degenerate. Combined with 769 (capacity FALSIFIED), FOUR axes are now eliminated — capacity, drive-schedule, reward-coupling, credit-horizon. The wall is the learned actor-critic converter itself: it cannot extract a competent policy from a sufficient observation, invariant to all tested levers. Biological triage: mammals never cold-start a forager from RPE-on-a-prediction-encoder; the one arm that ever cleared REE's floor is BC (imitation, 32.72). Missing-dependency reframe (user-confirmed): the actor needs a competence-directed BOOTSTRAP (behavioral-prior / approach-primitive seed), not any config/env/credit lever. epistemic_category competence_implementation_gap (NOT substrate_ceiling; 0 ceiling verdicts preserved, GOV-CEIL-1 unaffected); evidence_direction non_contributory (PROMOTES/DEMOTES NOTHING). Re-derive brake FIRED (7th non_contributory MECH-457 autopsy): REFUSE any further config/env/credit/capacity explorer re-queue. Routing = GOV-FANOUT-1 discrimination portfolio, NEW EXQ numbers on different mechanism classes: H-bc-prior (competence-directed behavioral-prior / imitation warm-start of the actor policy) vs H-approach-primitive (innate non-extinguishing competence-directed approach drive, demonstrator-free), each with a declared null; substrate build (amend mech457_competence_bootstrap_explorer) deferred until the discrimination names which dependency. MECH-457 stays candidate/v3_pending; a NEW hit within the GOV-GRAN-1 coherent-campaign disposition, not a granularity signal.

---

## Confirmed routing (Step 8 gate)

- **Diagnosis:** accepted — missing-dependency reframe (converter needs a competence-directed bootstrap; MECH-457 intact/necessary-not-sufficient).
- **Routing:** **new GOV-FANOUT-1 portfolio first** — pre-register H-bc-prior vs H-approach-primitive (each with a declared null) into the frozen ledger; queue via `/queue-experiment`; defer the substrate build until the discrimination resolves.
