# Failure Autopsy -- V3-EXQ-744 (INV-088 world/goal-evaluator DV-coupling)

- **Generated (UTC):** 2026-07-12T13:24:27Z
- **Run:** `v3_exq_744_inv088_world_goal_evaluator_dv_coupling_20260712T125137Z_v3` (ree-cloud-1)
- **Claim:** INV-088 (`world_goal_evaluator_bounded_by_z_world_differentiation`, emergent invariant, candidate / pending_substrate_reconfirmation; child (i) of INV-064, registered 2026-07-12)
- **Manifest outcome / self-route:** FAIL / `evidence_direction: weakens` / `non_degenerate: true`
- **Scope:** single
- **Status:** confirmed (interactive gate answered 2026-07-12)
- **Verdict:** **UNDER-POWERED NEAR-MISS that directionally SUPPORTS INV-088 -- NOT a refutation. Reclassify `weakens` -> `inconclusive` (non-counting). Route higher-seed V3-EXQ-744a (8 seeds).**

---

## 1. Facts (no interpretation)

The run is a **valid, non-degenerate test**. All three validity preconditions passed, so a FAIL here is a real verdict, not a vacuous contrast:

| Precondition | Value | Floor | Met |
|---|---|---|---|
| `PC_iv_moved` (z_world differentiation gradient moved) | mean IV delta 0.173 | >= 0.03 & > 0 | YES |
| `PC_dv_decodable` (mature-anchor primary DV target decodable) | 0.283 | >= 0.05 | YES |
| `PC_target_var` (primary DV target not degenerate) | min std 0.218 | >= 0.02 | YES |

PASS = C1 AND C2 AND C3. Result:

| Criterion | Definition | Observed | Verdict |
|---|---|---|---|
| **C3 noise-fit floor** (load-bearing, non-tautological) | mean immature-anchor R2_test <= 0.05 | **-0.029** (per-seed [-0.022, +0.005, -0.071]) | **PASS** |
| C1 floor | mean_seed(delta R2) >= 0.15 | 0.232 | PASS |
| **C1 effect-size gate** | mean delta >= 2.0 * SD_seed(delta) | 0.232 < **0.336** (SD 0.168) | **FAIL** |
| **C2 monotone** | mean_seed Spearman(onset, R2_test) >= 0.80 | **0.70** | **FAIL** |

**Mean by-onset harm_eval R2_test trajectory {0,1,4,12,30}:** `-0.029, -0.029, -0.041, +0.037, +0.203` -- textbook monotone: the z_world-reading evaluator is noise-fitted below chance while z_world is undifferentiated, then climbs to +0.203 at maturity. Train-test gap collapses (+0.039 -> -0.017). IV (world-feature decodability) rises 0.048 -> 0.221.

**Single-seed driver.** Per-seed values expose that one seed carries the entire FAIL:

| Seed | delta R2 | Spearman rho | Read |
|---|---|---|---|
| 42 | 0.177 | 0.90 | clean, monotone |
| **7** | **0.421** | **0.20** | **outlier: largest endpoint jump, non-monotone middle (dips onset 4/12, jumps onset 30)** |
| 19 | 0.099 | 1.00 | clean, monotone |

Seed 7 simultaneously (a) inflates SD_seed(delta) to 0.168, pushing 2*SD (0.336) above the mean (0.232) -> breaks C1's effect-size gate; and (b) drags mean rho from ~0.95 (seeds 42/19) down to 0.70 -> breaks C2. **Both failing gates are cross-seed variance gates, and both are broken by the same one seed at n=3.**

(Secondary/advisory benefit_eval leg: seed 19 is negative throughout -> `benefit_corroborates=false`. Advisory only; does not gate validity or the primary verdict.)

---

## 2. Claim-layer map

INV-088 asserts the z_world-reading evaluators (harm_eval SD-003 head, benefit_eval, goal scoring) are **strictly bounded by z_world differentiation** -- a poorly-differentiated z_world yields a **noise-fitted** evaluator, so productive evaluator training cannot precede E1 schema differentiation. The `claim_ids` tag is accurate (fresh claim, tagged at authoring, not inherited).

Did the experiment let the claim express itself? **Yes.** The IV moved validly, the primary DV target is decodable-in-principle, and the load-bearing C3 criterion -- "the immature evaluator is USELESS (noise-fitted below chance), not merely worse" -- is exactly INV-088's mechanistic claim, and it PASSED on all three seeds. The mean trajectory realises the predicted monotone coupling. The FAIL falls entirely on cross-seed robustness, which is orthogonal to whether the claim's mechanism is present.

---

## 3. Biological-reference triage

INV-088 inherits its existence proof from INV-064: PFC-last-myelination developmental sequencing and the dual-systems result that cognitive-control and affective systems mature on different timetables (Casey 2011; Strang 2013). The maturation-order coupling under test is a faithful developmental translation, **not** a formal-definition import. The biology is not the locus of failure and no `/lit-pull` is owed. The failure is statistical.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not weakened; directionally strengthened** | valid non-degenerate test; C3 passed; mean monotone -> supports INV-088 |
| Biological reference | clear | PFC-last-myelination / dual-systems (inherited INV-064); not the failure locus |
| Prerequisites | present | IV moved validly + monotonically; depends_on satisfied |
| Implementation | complete | real SD-003 harm_eval_head + benefit_eval_head; frozen-rep bit-identical |
| Environment | adequate | scheduled_external_hazard OFF (537b regime) |
| **Measurement** | **UNDER-POWERED (dominant)** | n=3 vs 2*SD robustness gate + rho>=0.80; one outlier seed breaks both |
| Integration | coupled | frozen encoder + re-init heads couple as designed |
| Scale / capacity | substrate-adequate; **seed-count insufficient** | mature-anchor R2 0.20; shortfall is statistical, not substrate |

**Dominant diagnosis: measurement / statistical power.** Recommended `epistemic_category` stays **`standard`** (this is a normal testable mechanism that is underpowered, not a category shift; NOT `substrate_ceiling`).

Why more seeds is the right discriminator (not just "more power"): the 2*SD gate tests cross-seed *robustness* (`mean >= 2*SD` <=> `CV <= 0.5`), a population property that does not shrink with n. Eight seeds gives a real estimate of the true across-seed delta SD and separates two live readings: (a) seed 7 is an unlucky tail -> most seeds cluster clean, SD falls, gates pass; (b) the coupling is genuinely seed-fragile -> SD stays high, which is itself a real (weaker) finding. n=3 with one outlier cannot distinguish these.

---

## 5. Recording-provenance note (secondary)

`validate_recording.py` flags the manifest missing top-level `recording_schema`, `substrate_hash`, `machine_class`, `elapsed_seconds`, `config`. **This did NOT block adjudication:** `substrate_hash` (`b0421b44...`) and `machine_class` (`linux-x86_64-py3.10`) are present in every per-arm `arm_fingerprint`, so the substrate identity is confirmable and all seed-level data needed for the verdict is present. Fold `experiments/_lib/manifest_core.stamp_recording_core(...)` into the 744a re-run per `experimental_recording_standard_2026-07-12.md` sec 3b -- opportunistic, not the routing driver.

---

## 6. Learning extracted

1. INV-088's DV half shows a clean directional signal on V3: the z_world-reading harm evaluator is noise-fitted below chance at immaturity and climbs to held-out R2 0.20 at maturity, tracking the rising differentiation gradient -- complements 740a's validated IV half.
2. A 2*SD effect-size gate + rho>=0.80 monotone gate is stringent at n=3: one outlier seed can break both while the mean trajectory is clearly monotone. Power/robustness limitation, not a ceiling or falsification.
3. The correct adjudication of a valid-but-underpowered near-miss is `inconclusive` (non-counting) + higher-seed retest -- NOT `weakens`. Recording it as `weakens` lets one noisy seed manufacture spurious counter-evidence against a directionally-supported claim.

---

## 7. Routing (user-confirmed at the interactive gate)

- **Reclassify** `evidence_direction: weakens -> inconclusive` (non-counting). `epistemic_category` stays `standard`. Draft `evidence_quality_note` in the companion JSON, verbatim, for `/governance` to write. **Do not record INV-088 as weakened on this run.** No illusory conflict resolution: this is INV-088's only DV evidence (IV half = the supported 740a leg), so nothing negative is being hidden; `narrow_supports_flag = false`.
- **Route `/queue-experiment`** for successor **V3-EXQ-744a** (alphabetic suffix -- same scientific question, power fix): **8 seeds**, same frozen-representation design, same pre-registered C1/C2/C3 criteria, primary DV = SD-003 `harm_eval_head` on next-step hazard-proximity world feature from `harm_obs[t+1]`; add `stamp_recording_core(...)` to close the recording-core gap.
- **Re-derive brake: does NOT fire.** INV-088 fresh (0 prior autopsies); this reads the world-feature target 740a proved decodable, the `/claim-synthesis`-sanctioned world-feature leg -- not the refused realized-scalar-harm re-decode (INV-089/z_harm). The re-derive brake in this doc is inapplicable and a same-question 744a re-queue is explicitly ALLOWED (it is not circling a substrate ceiling; it is resolving cross-seed variance on a directionally-supported valid test).
- **Companion build chip:** "Fix maturation-curriculum arm reuse" -- the 744 `arm_fingerprint`s mark the frozen (seed, onset) cells `reuse_eligible: false` via the disputed `frozen_representation_from_maturation_trajectory` reason; per the standing note that flag is FALSE (cells proven deterministic bit-identical) and family-reuse needs a tensor cache. Building it lets 744a skip re-training the shared cells.

**This skill does not edit claims.yaml, the manifest, `evidence_direction`, `review_tracker.json`, or `substrate_queue.json` -- `/governance` applies the reclassification interactively.**
