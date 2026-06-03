# Failure Autopsy — V3-EXQ-514l (SD-049 Phase-3 MECH-229 wanting/liking identity)

- **generated_utc:** 2026-06-03T06:59:06Z
- **scope:** single (convergent with the 2026-06-03 V3-EXQ-603e/626a/622 cluster)
- **status:** confirmed (user-approved 2026-06-03 via AskUserQuestion)
- **run_id:** v3_exq_514l_sd049_phase3_mech229_wanting_liking_identity_20260602T170106Z_v3
- **queue_id:** V3-EXQ-514l
- **claim_ids:** SD-049, SD-015, MECH-229, MECH-230
- **experiment_purpose:** evidence
- **supersedes:** V3-EXQ-514k (which FAILed the same branch 2026-06-01; V3-EXQ-514j FAILed it 2026-05-20)
- **machine:** ree-cloud-1

This autopsy was the diagnosis the 2026-06-03 /governance walk (GROUP B) deferred:
"514l author-stamped weakens NOT trusted (C2c insufficient identity samples +
C5/C6 dissoc-fail = foraging-competence/substrate-ceiling shape, same prerequisite
as 603e cluster); 514l STAYS pending; its interim (untrusted) weakens still weights
until autopsy lands."

---

## 1. Facts — reconstruction (no interpretation)

4-arm design (ARM_0 OFF / ARM_1 2-type / ARM_2 3-type / ARM_3 5-type), 3 seeds
(42/43/44). Phase 3 substrate: `use_sd049_per_axis_consumer_cascade=True`,
`use_mech307_conjunction=True`, `drive_floor=0.9`, SP-CEM main path, reef enabled,
`hazard_food_attraction=0.7`. P0=30 / P1=10 / EVAL=15 episodes, 300 steps/ep.

**Outcome: FAIL.** `interpretation_branch = row1b_joint_identity_probe_weak`
(C2b FAIL AND C2c FAIL).

Author-stamped per-claim directions in the manifest:
- SD-049: weakens
- SD-015: weakens
- MECH-229: non_contributory
- MECH-230: non_contributory

### Acceptance criteria (ARM_2 = primary measurement arm)

| Criterion | Type | Threshold | Observed | Result |
|---|---|---|---|---|
| C0 ARM_0 runs clean | negative-control | — | clean | PASS |
| C1a/C1b ARM_1 obs_dim + classifier converges | wiring | dim 350 / loss-drop | 3.58 -> 2.22 | PASS |
| C2a ARM_2 obs_dim | wiring | 350 | 350 | PASS |
| C2b ARM_2 probe_acc_neighborhood | **discrimination** | >= 0.6 | **0.447** | **FAIL** |
| C2c ARM_2 n_identity_samples_consumption | **discrimination** | >= 30 | **23** | **FAIL** |
| C2d ARM_2 per-axis drive evolves | wiring | > 0.02 | evolves | PASS |
| C3a/C3b ARM_3 obs_dim + classifier fired | wiring | 400 / fired | yes | PASS |
| C4 ARM_2 goal_resource_r | absolute | >= 0.5 | 0.996 | PASS |
| C5 ARM_2 - ARM_0 goal_resource_r lift | **discrimination** | >= 0.4 | **-0.004** | **FAIL** |
| C6 ARM_2 wanting!=liking dissoc fraction | **discrimination** | >= 0.6 | **0.0** | **FAIL** |

**Every absolute / negative-control / wiring criterion passes; every discrimination
criterion fails. This is the substrate-ceiling fingerprint.**

### Two load-bearing facts

1. **C6 = 0.0 on every arm and every seed.** The `|wanting - liking| > 0.1`
   condition (read from ResidueField VALENCE_WANTING vs VALENCE_LIKING at each
   valence step) fired **zero times** across the entire run. The wanting and liking
   valence streams never differentiate.

2. **Consumption starvation.** ARM_2 logged only **23** consumption-identity samples
   across 3 seeds (6 / 10 / 7) versus **818** neighborhood samples. The agent spends
   time *near* resources (818) but consumes only ~23 across ~4500 eval steps/seed
   (~0.2% consumption rate). ARM_3 seed-44 classifier collapsed to loss 0.010 on
   7+131 starved samples (overfit on tiny data, not genuine convergence).

The identity classifier *head* trains (C1b/C3b PASS) but the linear identity-recovery
*probe on z_resource* stays near chance (neighborhood 0.45-0.53; consumption 0.0-0.21),
and the consumption axis is too starved (23 < 30) to evaluate at all.

---

## 2. Claim-layer map

| Claim | type | status | flags | What 514l tested for it |
|---|---|---|---|---|
| SD-049 | design_decision | candidate | v3_pending, implementation_phase v3 | Multi-resource substrate readiness (env + per-axis drive). Wired and firing (C0/C1/C2a/C2d/C3 PASS). |
| SD-015 | design_decision | candidate | implementation_phase v3 | z_resource identity recovery (C2b). FAILed at 0.447. |
| MECH-229 | mechanism_hypothesis | **provisional** | pending_retest_after_substrate=True | Identity-distinct wanting on multi-resource substrate (C6). Demoted active->provisional 2026-06-01 *because prior PASSes EXQ-074f/234/354 were single-resource (degenerate)*. |
| MECH-230 | mechanism_hypothesis | provisional | — | z_goal latent multi-modal structure. |

**Did the test let the claims express?** No. The discrimination criteria all depend
on the agent generating reward-contact behaviour (consuming across resource identities,
building wanting/liking traces). With a ~0.2% consumption rate the behavioural substrate
for every discrimination criterion is absent. The encoder/substrate wiring is correct;
the policy upstream of it does not forage competently.

---

## 3. Biological-reference triage

MECH-229 (identity-distinct wanting) and MECH-230 (z_goal structure) are **faithful
biological translations, not formal-definition imports**: Berridge mesolimbic-DA
incentive-salience (wanting) and opioid hedonic-hotspot (liking). The biology
*requires* learned cue-reward association and consummatory contact for (a) wanting to
become identity-distinct and (b) wanting != liking to dissociate.

A near-zero consumption rate is **exactly the signature of a missing reward-contact
dependency**. The FAIL resembles what would happen biologically if the animal never
foraged — wanting/liking cannot dissociate with no consummatory history. This is a
**discovered prerequisite, not a falsification** (the canonical correct response,
parallel to SD-010/SD-011, not the SD-003 "treat divergence as a caveat" failure mode).

Lit status: SD-049 lit_conf=0.898 (5 PubMed; Berridge 2018, Smith & Berridge 2007).
The biology is clear and supports the mechanism class; **no lit-pull is warranted** —
the gap is behavioural-substrate, not biological-translation.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | Test could not let MECH-229/230 express; no reward-contact history. MECH-229 already provisional/pending_retest with only degenerate single-resource supports. |
| Biological reference | **clear, faithful** | Berridge wanting/liking; FAIL = missing reward-contact dependency. |
| Prerequisites | **missing** | Foraging-competence (reaches resources, 818 neighborhood; consumes ~23) + benefit/consumption-contact history. Same two coupled prerequisites as the 603e/626a/622 cluster. |
| Implementation | **complete** | SD-049 Phase 1+2 + SD-015 encoder wired: obs dims grow, per-axis drive evolves, identity classifier trains and fires. Functional role present; behavioural data absent. |
| Environment | **wrong pressure for the policy** | hazard_food_attraction=0.7 (hard) + no foraging-competence scaffold (P0/P1 = 30/10) -> near-zero consumption. |
| Measurement | **under-instrumented + one defect** | C2c starved (23<30); C6 needs consumption data; **C5 lift is a test-design defect** — ARM_0 control saturates goal_resource_r ~1.0 (z_goal seeded from z_world -> cosine ~1.0), so a +0.4 lift is structurally impossible. C4/C5 are non-discriminating because goal_resource_r is near-saturated everywhere. |
| Integration | **partially coupled** | encoder + goal pipeline + valence streams wired, but the foraging policy upstream does not feed them. |
| Scale / capacity | **likely insufficient budget** | P0=30/P1=10; seed-44 classifier overfit (loss 0.010) on 7+131 samples. |

**Dominant diagnosis: substrate_ceiling** (claims are V3-tractable in principle;
the policy/substrate is too coarse to deliver the behavioural distinctions). Same
`epistemic_category` as the 603e cluster.

**failed_criterion: discrimination.**

---

## 5. Convergent-pattern note (single scope, cross-cluster convergence)

514l is on a **different substrate** (reef + SD-049 multi-resource + phased
P0/P1/P2, NOT the scaffolded_sd054_onboarding scheduler) testing **different claims**
(MECH-229/230 wanting-liking vs the 603e cluster's Q-045/MECH-313/MECH-260 diversity),
yet fails on the **same structural property**: the goal/wanting pipeline has no
behavioural substrate to express in because the agent does not forage competently.

| Run | Claim family | Negative-control / absolute | Discrimination | Read |
|---|---|---|---|---|
| 603e/626a/622 | Q-045/MECH-313/MECH-260 diversity (z_goal=0) | positive controls pass | z_goal_norm_peak=0 on all cells | foraging-competence + benefit-starvation |
| **514l** | MECH-229/230 wanting-liking | C0/C1/C2a/C2d/C3/C4 pass | C2b/C2c/C5/C6 fail; consumption ~0.2%; C6=0.0 | **same** foraging-competence + benefit-contact starvation |

**Reading:** ONE structural property (foraging-competence is a cross-cutting V3
ceiling), not N independent bugs. This convergence across structurally-different
claim families is the load-bearing signal.

---

## 6. Learning extracted

1. The SD-049 multi-resource wanting/liking test (514j/k/l — **three FAILs, same
   `row1b` branch**) is blocked by the same foraging-competence + benefit-contact
   prerequisite as the 603e scaffolded-onboarding cluster. Foraging-competence is a
   cross-cutting V3 substrate ceiling, not a per-test tuning issue.
2. **Illusory-conflict guard (load-bearing):** MECH-229's only genuine multi-resource
   test has now FAILed 3x. Its remaining "supports" (EXQ-074f/234/354) are *all
   degenerate single-resource*. Reclassifying 514l non_contributory must NOT read as
   MECH-229-resolved — it stays provisional / pending_retest with **zero genuine
   multi-resource support** (`narrow_supports_flag=true`).
3. **C5 lift is a test-design defect independent of the ceiling**: the ARM_0 control
   saturates goal_resource_r ~1.0 (z_goal seeded from z_world), so the +0.4 lift can
   never be met. The 514m redesign needs a non-saturating control / metric. (User
   decision 2026-06-03: defer the redesign until the foraging-competence substrate
   lands — no point fixing the metric while the policy still cannot forage.)

---

## 7. Repair pathway / routing (user-confirmed 2026-06-03)

**Routing: implement-substrate** (foraging-competence + benefit-contact scaffold).

- **Disposition (user-confirmed):** override the author-stamped directions. Re-tag
  ALL FOUR claims `non_contributory` + `epistemic_category: substrate_ceiling` +
  `pending_retest_after_substrate: true`. The SD-049/SD-015 "weakens" is
  substrate-ceiling-confounded (the test could not let the claims express); MECH-229/230
  were already self-stamped non_contributory (confirm). Pair with an explicit note that
  MECH-229's remaining supports are degenerate single-resource (no false "resolved").

- **Substrate routing (autopsy call, user deferred):** `action: amend` on
  **SD-049-PHASE-2**. That entry's stated deliverable is exactly "V3-EXQ-514
  behavioural validation / wanting != liking trajectory dissociation," yet it sits at
  `phase_2_implemented` with 0 failure_records — which 514l (3 FAILs) shows is
  premature. The amend adds the 514l failure_record and names the required substrate
  work (a foraging-competence + consumption-contact scaffold on the SD-049/reef
  harness), cross-referencing `scaffolded_sd054_onboarding` as the prior-art pattern
  to port from — rather than spawning a third overlapping scaffold entry.

- **C5 measurement defect:** deferred to a 514m /queue-experiment redesign AFTER the
  foraging-competence substrate lands (non-saturating control + drop/replace C5).

### Draft `evidence_quality_note` for governance to write (do NOT write here)

> 2026-06-03 (failure_autopsy_V3-EXQ-514l): V3-EXQ-514l FAIL re-tagged non_contributory
> / epistemic_category substrate_ceiling / pending_retest_after_substrate. The author-stamped
> per-claim "weakens" (SD-049, SD-015) is NOT trusted: every absolute/wiring criterion
> passed (C0/C1/C2a/C2d/C3/C4) but every discrimination criterion failed (C2b probe 0.447,
> C2c n_consumption_samples 23<30, C5 lift -0.004, C6 wanting!=liking dissoc 0.0 on all
> seeds). Root cause is a foraging-competence + benefit-contact substrate ceiling: ~0.2%
> consumption rate (23 consumption vs 818 neighborhood samples), so the Berridge
> wanting/liking dissociation has no reward-contact history to express in. Same structural
> property as the 603e/626a/622 cluster (different substrate, different claims, same
> foraging-competence ceiling). Third FAIL on the same row1b branch (514j/514k/514l).
> NOT a falsification (biology clear; discovered prerequisite). C5 is additionally a
> test-design defect (ARM_0 control saturates goal_resource_r ~1.0). For MECH-229
> specifically: this was the only genuine multi-resource test; its remaining supports
> (EXQ-074f/234/354) are degenerate single-resource, so this non_contributory does NOT
> resolve MECH-229 — it stays provisional with no genuine multi-resource support.
> Routing: implement-substrate (foraging-competence scaffold on the SD-049/reef harness;
> SD-049-PHASE-2 substrate_queue amend). 514m redesign (non-saturating C5 control)
> deferred until the substrate lands.
