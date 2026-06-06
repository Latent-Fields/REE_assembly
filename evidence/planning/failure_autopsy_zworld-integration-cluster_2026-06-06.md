# Failure Autopsy -- z_world integration / robustness cluster

- **Generated (UTC):** 2026-06-06T13:02:33Z
- **Scope:** cluster (4 targets)
- **Status:** confirmed (interactive gate cleared 2026-06-06)
- **Targets:** V3-EXQ-177, V3-EXQ-145, V3-EXQ-170, V3-EXQ-215
- **Trigger:** recurring "z_world collapse / robustness" theme; parked >2 months with "separate workstream" notes, never given a structured cross-claim diagnosis.

---

## 1. Facts reconstruction (no interpretation)

| Exp | run_id | Claim tag | Outcome / dir | World-model criterion (PASS) | Discriminative criteria (FAIL) |
|---|---|---|---|---|---|
| V3-EXQ-177 | `v3_exq_177_sd008_integration_test_20260329T215657Z_v3` | SD-008 *(mistag)* | FAIL / weakens | C2 world_forward_r2 = **0.941** (>0.30) | C1 event_selectivity_margin = **0.00034** (>0.05); C3 attribution_gap = **0.00034** (>0.005) |
| V3-EXQ-145 | `v3_exq_145_sd008_sd007_sd003_integration_20260329T215806Z_v3` | SD-008, SD-007, SD-003 | (null) / mixed | -- | reafference Phase-1 gate r2=0.076 (<0.08) **blocked the run before selectivity was measured** |
| V3-EXQ-170 | `v3_exq_170_q002_r_field_resolution_pair_20260330T070234Z_v3` | Q-002 | FAIL / mixed | C3 coarse sufficient harm events (PASS) | C1 fine-not-worse FAIL (fine harm 0.028 vs coarse 0.0003); C2 fine_residue_accuracy = **0.016** (vs coarse 0.034) |
| V3-EXQ-215 | `v3_exq_215_q002_residue_resolution_pair_20260403T202434Z_v3` | Q-002 | FAIL / weakens | C2 mean_harm_delta PASS; C4 data-quality PASS; C5 e2_world_r2 = 0.724 PASS | C1 harm-direction per-seed FAIL; C3 acc-direction per-seed FAIL (high_res_acc = **-0.0097**, negative) |

**Failed-criterion classification:** in every contributory target the **absolute / world-model / negative-control criterion PASSES** and the **discrimination criterion FAILS** -- the substrate-ceiling fingerprint.

Supporting detail (V3-EXQ-177, seed 42): n_hazard_steps=830 vs n_open_steps=126 (**6.6:1 event imbalance**), warmup_steps=5809, world_dim=32, alpha_world=0.9, SD-007/SD-008/SD-003 all enabled.

---

## 2. Claim-layer mapping

- **SD-008** (alpha_world >= 0.9): `status: stable` (2026-03-30, conflict_ratio=0). Isolated supports EXQ-023, EXQ-040 are definitive and uncontested. **V3-EXQ-177 is mistagged against it**: 177 *ran at* alpha=0.9, i.e. it presupposes SD-008 and tests downstream stack selectivity -- it neither supports nor weakens the alpha claim. Its `weakens` weight is spurious.
- **SD-007 / SD-003** (reafference correction / counterfactual attribution): exercised in 177/145 but the attribution path depends on **SD-031 (`self_attribution.comparator_z_world`), which is status `None` / not implemented** in the substrate_queue. 177's C3 attribution collapse is partly an unbuilt-comparator artifact.
- **Q-002** (spatial resolution of R(x,t) over z_world): the existing `evidence_quality_note` already honestly states "V3-scale finding: coarse adequate, fine counterproductive; does not rule out fine resolution at higher-dim z_world." 170/215 tested **only at world_dim=32**.

---

## 3. Biological-reference triage

Closest reference: cortical sensory manifolds (V1/V2/parietal) where a population code is simultaneously a good *bulk dynamical predictor* and a *discriminative, spatially-organized* substrate -- but that dual property emerges with sufficient representational dimensionality and with *behaviorally-balanced experience* (the animal must visit the discriminanda). The REE constructs here (event-selectivity, counterfactual attribution, RBF residue field) are **faithful translations, not formal-definition imports** -- so the FAIL default is a translation/dependency/scale gap, not falsification. The failure resembles exactly what a cortical area would show if (i) starved of dimensionality (dim=32) and (ii) given a monostrategy-locked behavioral diet (6.6:1 event imbalance) -- both are known missing dependencies, not evidence the mechanism class is wrong.

---

## 4. Four-layer diagnosis (cluster-dominant)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (177/145) / weakened-at-scale (170/215) | 177 mistagged; Q-002 honestly weakened only at dim=32 |
| Biological reference | clear | population code; dual predictive/discriminative property is dimensionality- and experience-dependent |
| Prerequisites | missing | SD-031 (z_world attribution comparator) = None; ARC-065 behavioral-diversity = phase_1 only |
| Implementation completeness | partial | world-forward complete (r2 0.72-0.94); discriminative/attribution heads partial/absent |
| Environment adequacy | adequate | CausalGridWorldV2 produces the events; problem is exposure balance, not env |
| Measurement adequacy | under-instrumented | event_selectivity over 126 open steps is noisy; per-seed direction unstable |
| Integration adequacy | coupled but unstable -> reframed | NOT stack-interference (see cluster read) |
| Scale / capacity | likely insufficient | world_dim=32; higher-dim SD-005 presets (128/256) exist but were never used here |

**Recommended `epistemic_category`: `substrate_ceiling`** (z_world discriminative/spatial granularity at world_dim=32), paired with `pending_retest_after_substrate`.

---

## 5. Cluster pattern

| Experiment | Claim | Absolute / world-model criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-177 | SD-008 (mistag) | world_forward_r2 0.94 PASS | event_selectivity ~0; attribution ~0 FAIL | full-stack selectivity collapse |
| V3-EXQ-145 | SD-008/007/003 | -- (blocked at reafference gate) | not reached | engineering bottleneck, non-contributory |
| V3-EXQ-170 | Q-002 | coarse events sufficient PASS | fine residue_acc 0.016 FAIL | bare-RBF fine-granularity collapse |
| V3-EXQ-215 | Q-002 | e2_world_r2 0.72 PASS | high_res_acc -0.0097 FAIL | bare-RBF fine-granularity collapse |

**Independent bugs or one structural property?** -> **One structural property.**

> z_world at world_dim=32 is a competent *bulk dynamical predictor* (world_forward_r2 0.72-0.94) but lacks *event-selective / spatially-organized discriminative structure* at the granularity downstream claims require (selectivity, counterfactual attribution, fine RBF residue all -> ~0 or negative).

**Load-bearing move:** 170/215 use a **bare RBF read of z_world spatial structure with no counterfactual stack**, yet show the *same* fine-granularity failure as 177's full-stack selectivity collapse. This convergence across structurally-different read paths **rules out the "destructive stack-composition interference" reading** (which would predict the collapse only in the combined SD-007+SD-008+SD-003 stack). The property is intrinsic to z_world at this scale.

**Three readings, adjudicated:**
- **(a) substrate granularity ceiling at world_dim=32 -- SUPPORTED.** Convergence across read paths; claims' own hedge; higher-dim presets exist but unused.
- **(b) destructive stack interference (177 only) -- RULED OUT** by 170/215 convergence.
- **(c) V_s monostrategy / behavioral-measurement confound -- REAL but PARTIAL.** 177's 6.6:1 event imbalance makes selectivity near-unmeasurable; V_s monostrategy lock is a documented confound (claims.yaml:1374). Does not explain 170/215 navigation-residue failures. Addressed by ARC-065 (phase_1_implemented) + MECH-313/314 (landed).

---

## 6. Learning extracted

1. The "z_world collapse" theme decomposes into a **closed** part (SD-008 alpha-EMA suppression, fixed, stable) and an **open** part (discriminative-granularity ceiling at dim=32) -- they are not the same failure and must not be conflated.
2. Cross-claim cluster is what separates them: per-experiment, 177 reads as stack-interference and 170/215 as "RBF density irrelevant"; together they are one scale-limited representational property.
3. V3-EXQ-177's SD-008 `weakens` weight is a misattribution (presupposes the claim it is tagged against). SD-031 unbuilt + monostrategy + dim=32 make it non-contributory across all its tags.
4. The substrate to retest the open question **already exists** (SD-005 higher-dim presets; ARC-065 diversity phase_1) -- so the routing is a substrate-gated *re-run*, not new substrate and not a demotion.

---

## 7. Repair pathway / routing

**Primary routing: `/queue-experiment`** -- a single substrate-gated re-run, `pending_retest_after_substrate`:

- **Retest spec (user-confirmed):** world_dim=128 **AND** a behaviorally-balanced / exploratory policy (ARC-065 diversity active), re-measuring **event_selectivity + counterfactual attribution + fine-vs-coarse residue accuracy together** in one harness.
- **blocked_by:** ARC-065 behavioral-diversity reaching validation (balanced event distribution) and SD-031 (`comparator_z_world`) implementation for the attribution arm.
- Do **not** run until both halves are in place, else the retest reproduces the dim=32 + monostrategy + unbuilt-comparator confound.

**Governance hand-offs (this skill recommends; governance applies):**

1. **V3-EXQ-177:** set evidence_direction -> `non_contributory` for the SD-008 tag (do **not** retag to SD-003/SD-007); mark `pending_retest_after_substrate`. SD-008 stays `stable` (isolated supports untouched -> no illusory-conflict risk).
2. **V3-EXQ-145:** confirm `non_contributory` (engineering gate blocked the test).
3. **V3-EXQ-170 / V3-EXQ-215:** retain `weakens` **scoped to V3 dim=32**, add `pending_retest_after_substrate` pointing at the dim=128 retest. (Q-002 notes already honest; only the retest pointer is new.)

### Draft `evidence_quality_note` text for governance

**SD-008 (append):**
> V3-EXQ-177 reclassified non_contributory (2026-06-06 cluster autopsy `failure_autopsy_zworld-integration-cluster_2026-06-06`): the run executed at alpha_world=0.9, i.e. it presupposes SD-008 and tests full-stack event-selectivity/attribution, not the alpha value. Its prior `weakens` weight was a misattribution. SD-008 isolated supports (EXQ-023, EXQ-040) remain definitive; stable status unaffected.

**Q-002 (append):**
> 2026-06-06 cluster autopsy: V3-EXQ-170/215 weaken the fine-resolution hypothesis only at world_dim=32. Convergent with V3-EXQ-177 full-stack selectivity collapse (bare-RBF read, no counterfactual stack) -> one structural property: z_world at dim=32 is a competent bulk predictor but lacks discriminative/spatial granularity. pending_retest_after_substrate: re-run fine-vs-coarse residue at world_dim=128 with ARC-065 behavioral diversity active. Not a falsification of Q-002; a scale ceiling.

---

## 8. Routing summary

| Target | Failed criterion | Dominant layer | Recommended dir | Routing |
|---|---|---|---|---|
| V3-EXQ-177 | discrimination | scale + prerequisite (SD-031) | non_contributory | queue-experiment (gated) + governance retag-correction |
| V3-EXQ-145 | (blocked pre-test) | implementation/engineering | non_contributory | folds into same retest |
| V3-EXQ-170 | discrimination | scale | weakens @ dim=32 + pending_retest | queue-experiment (gated) |
| V3-EXQ-215 | discrimination | scale | weakens @ dim=32 + pending_retest | queue-experiment (gated) |

`epistemic_category` recommended: `substrate_ceiling` (z_world discriminative granularity at world_dim=32).
