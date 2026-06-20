# Failure Autopsy -- V3-EXQ-625e (sd_037 axis-b P1b joint-composite RECALIBRATED)

- **Generated (UTC):** 2026-06-20T08:31:19Z
- **Scope:** single
- **Status:** confirmed (interactive, user-ratified 2026-06-20)
- **Run:** `v3_exq_625e_sd037_axis_b_phase1b_joint_composite_recalibrated_20260619T233440Z_v3` (ree-cloud-2)
- **Queue id:** V3-EXQ-625e (supersedes V3-EXQ-625d)
- **Claim ids:** `[]` (substrate-readiness diagnostic; weights NO claim)
- **Owner node:** `sd_037_axis_b:P1b` (`evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md`)
- **Pipeline flag adjudicated:** `precondition_unmet` (self-route `substrate_not_ready_requeue`, `non_contributory`)
- **Routed by:** the 2026-06-20T06:18Z `/governance` cycle (diagnostic-adjudication gate: the indexer-flagged `precondition_unmet` self-route must NOT drive a governance action until adjudicated).

---

## 1. What was being tested

The 625d-prescribed RECALIBRATION of the JOINT-COMPOSITE Phase-1b gate. Same composite as 625d
(policy trained THROUGH the full `scaffolded_sd054_onboarding` curriculum + the 569i-validated
TOP-K shortlist conversion config + MECH-341 + SD-056 online), measured for **z_harm_a dynamic
crossings** (sharpened C3a >= 1 above->below AND C3b >= 1 below->above per seed, >= 2/3 seeds)
under the SD-029 axis-(b) overlay -- but with the two 625d-autopsy fixes applied:

1. **Recalibrated axis-(b) threat:** magnitude lowered ~10x (`hazard_harm` / `proximity_harm_scale`
   0.2 -> 0.02) **AND** time-varying / **pulsed** (`scheduled_external_hazard` duty-cycle ON 40 /
   OFF 40 ticks) -- the explicit design goal being to bring the TRAINED z_harm_a into a
   sub-saturating, oscillation-capable band so it can cross 0.4 BOTH ways.
2. **603q-stabilized harm pathway:** `scaffold_harm_pathway_encoder_lr=3e-4` + warmup 250 +
   Stage-H `num_hazards=6` so the base harm landscape forms on >= 2/3 seeds (625d hit the 603p
   1/3 seed-fragility).

Pre-registered: PASS = C3 (>= 2/3) AND all four R1-R4 non-vacuity preconditions. A precondition
miss self-routes `substrate_not_ready_requeue` -- NEVER a weakens. Preconditions met + sub-2/3 C3
-> genuine `residual_no_oscillation` verdict -> /failure-autopsy.

---

## 2. Facts -- reconstruction (no interpretation)

| Readiness gate | Threshold | seed 42 | seed 43 | seed 44 | frac | Met |
|---|---|---|---|---|---|---|
| R1 curriculum fired (external_hazard_event_count) | >0, 3/3 | 54 | 73 | 70 | 3/3 | **MET** |
| R2 z_harm_a nonzero fraction | >=0.01, >=2/3 | 1.0 | 1.0 | 1.0 | 3/3 | **MET** |
| R3 route_range_mean | >0.01 | 0.1977 | 0.0815 | **0.0048** | -- | -- |
| R3 cand_world_pairwise_dist_mean | >0.03 | 0.0586 | **0.0230** | **0.0012** | -- | -- |
| **R3 conversion operative** (BOTH above, per seed) | >=2/3 | T | F | F | **1/3** | **UNMET** |
| R4 selected_action_class_entropy | >0.3, >=2/3 | **0.0** | **0.0** | **0.0** | **0/3** | **UNMET** |
| C3 dynamic crossings (above<->below 0.4) | >=2/3 | 0/0 | 0/0 | 0/0 | 0/3 | FAIL |

Self-route resolves `substrate_not_ready_requeue` (preconditions unmet) before the C3 residual
verdict is reached. Load-bearing criterion `C3_dynamic_crossings_2of3` failed; `criteria_non_degenerate`
all true.

Supporting per-seed facts:

- **z_harm_a still pinned high, never relieves.** z_harm_a_mean **4.910 / 4.712 / 4.802**;
  z_harm_a_max **4.935 / 4.743 / 4.827**; nonzero-frac 1.0. The 10x-lower + pulsed threat moved
  z_harm_a only from 625d's ~6.3 to ~4.8 -- still ~12x above the 0.4 crossing threshold, with a
  per-seed range of ~0.025. Crossings of 0.4: **0 above->below AND 0 below->above** on every seed
  (also 0 at the agent-PAG diagnostic threshold 0.2). The recalibration's PRIMARY design goal
  (sub-saturating oscillation band) was NOT achieved.
- **Committed policy monostrategy-locked.** `selected_class_counts` = `{"0":4000}` on all three
  seeds; selected-action entropy 0.0 across the board. The 569i TOP-K shortlist fired
  (`modulatory_shortlist_size_mean` 3.0 all seeds) and the authority was active
  (`modulatory_authority_active_ticks` 4000 all seeds), yet committed action never diversified.
- **Candidate-pool divergence collapses on 2/3 seeds.** cand_world_pairwise_dist 0.0586 / 0.0230 /
  0.0012 -- only seed 42 clears the 0.03 floor (the GAP-A candidate-pool statistic; the 569i
  conversion re-sources e2.world_forward per-candidate spread). route_range collapses with it
  (0.198 / 0.082 / 0.005).
- **603q stabilization WORKED.** harm_eval_range now **0.194 / 0.151 / 0.390** -- nonzero and
  discriminative on **all 3 seeds** (vs 625d's 0.283 / 0.0 / 0.0). The 603p seed-fragility the
  625d autopsy flagged is fixed; the decoupled-encoder-LR + warmup did what it was designed to do.
- Scaffold legs all reached P1 (`reached_p1` True 3/3; `p1_survival_pass` True 3/3;
  `harm_pathway_n_train_steps` 2341 / 2494 / 1305). The base policy is survival-competent; this is
  NOT a curriculum collapse.

**Which criterion failed:** the readiness preconditions r3 (conversion operative, 1/3) and r4
(committed-action diversity, 0/3). r1/r2 (the env-engagement axis) PASSED. This is the
"discrimination-criterion fails while the absolute/engagement controls pass" substrate-ceiling
fingerprint, with the discrimination locus being committed-action diversity / candidate-pool
divergence, NOT env capability.

---

## 3. The r3 / r4 gate-direction audit (the user's explicit question)

The `interpretation.preconditions[r3].measured = 0.197728 / threshold = 0.01 / met = false` looks
contradictory (0.197 >> 0.01 yet not met). It is **not a gate-direction bug.** Confirmed against the
script (`v3_exq_625e_..._recalibrated.py:864-868`):

```
r3 = bool(route_range_mean > ROUTE_RANGE_FLOOR(0.01)
          AND cand_world_pairwise_dist_mean > C1_PAIRWISE_DIST_FLOOR(0.03))   # per seed, COMPOUND
r3_frac = fraction of seeds with r3 True ;  r3_pass = r3_frac >= 0.667
```

- The displayed `measured: 0.197728` is `route_range_max_over_seeds` (seed 42's value) -- a single
  representative scalar, NOT the gate verdict.
- The gate verdict is `readiness_gate.r3_conversion_operative_frac = 0.333` (1/3 seeds clear the
  COMPOUND criterion: seed 42 clears both sub-floors; seed 43 fails the cand_world_pairwise_dist
  sub-floor 0.023 < 0.03; seed 44 fails both). 1/3 < 2/3 -> met=False, **correctly**.
- Direction is correct throughout: higher route_range and higher cand_world_pairwise_dist are
  better; the floors are minimums. r3 fails because the candidate-pool divergence sub-floor (the
  GAP-A statistic) collapses on 2/3 seeds, not because the gate is inverted.

r4 is straightforward: `selected_action_class_entropy(0.0) > 0.3` is False on all 3 seeds (every
tick picks action class 0). Direction correct (higher entropy = more diversity = better; floor 0.3
is a minimum). **r4=0.0 is the MECH-439 F-dominance conversion-ceiling signature.**

(Transparency caveat for the readiness harness: the `interpretation.preconditions[]` block surfaces
only one of r3's two sub-metrics and the max-over-seeds rather than the fractional verdict; the
authoritative numbers are in `readiness_gate`. Not a defect -- the self-route logic is correct --
but worth tightening the displayed `measured` to the fractional verdict in a future harness pass.)

---

## 4. Adjudication -- is the self-route trustworthy?

**Yes in the narrow sense, with a hard caveat: trustworthy as a refusal-to-weaken, NOT as a
prescription-to-requeue.**

- **Trustworthy:** the self-route correctly refuses to let a monostrategy re-derivation masquerade
  as an axis-(b) verdict. claim_ids=[], evidence_direction=non_contributory -- it weakens nothing.
  This is the internally-consistent, designed behaviour of the R1-R4 guards.
- **The caveat (why a blind requeue is wrong):** r4=0.0 and the r3 cand-pool collapse are NOT an
  "env not ready / overlay mis-applied" condition. They are the **MECH-439 F-dominance conversion
  ceiling expressing itself again** -- the LIVE ROOT per `conversion_ceiling_phase0_synthesis_2026-06-18`
  (root B: F monopolises ~88-89% of E3 committed-selection variance, unmoved by the full diversity
  stack). 625e is, in effect, a data point on that synthesis's **open-question #1**: *"does the thin
  569i top-k margin survive the full 625d composite under the foraging substrate's natural
  monostrategy?"* The answer is **NO** -- committed entropy collapsed to 0.0. The 569i
  committed-action-diversity demonstration that unblocked 625d -> 625e was **env-conditional** (it
  rested on the reef-bipartite env's structural guarantee of categorically-opposite first-action
  argmaxes; 625d autopsy section 3) and does **not** propagate to the axis-(b) foraging substrate.
- **A second, independent blocker the r-gates do not see:** even if r3/r4 cleared, C3 would still
  fail. z_harm_a is pinned at ~4.8 (12x above the 0.4 crossing threshold) **despite** the
  recalibration's explicit 10x magnitude reduction + pulsing. The trained harm pathway maps even a
  10x-reduced, duty-cycled harm stream into a saturated affective latent. The R1-R4 readiness set
  has **no gate on "z_harm_a in an oscillation-capable band"** -- so the C3 dynamic-crossing
  criterion is unreachable by env-magnitude recalibration alone, and a future run with r3/r4 met
  would still FAIL C3 for the saturation reason. This is a **missing readiness precondition** + a
  z_harm_a-operating-range substrate question, distinct from the F-dominance ceiling.

So: the self-route's `substrate_not_ready_requeue` is correct as a non-weakening verdict, but
"requeue" must be read as **"hold and re-gate behind the upstream substrate work,"** NOT "re-tune the
axis-(b) threat and re-run." A 625f recalibration would reproduce r4=0.0 (F-dominance is unmoved by
threat tuning) and would still hit z_harm_a saturation.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | Tags no claim; SD-037/MECH-280/MECH-281 stay substrate_ceiling / pending_retest_after_substrate. |
| Biological reference | partial | Saturated z_harm_a ~4.8 -> a single defensive action is the tonic-immobility / learned-helplessness regime -- biologically faithful, but the wrong regime for the risk-assessment-oscillation the C3 criterion presupposes. The recalibration aimed for a phasic risk-assessment regime and did not reach it. |
| Prerequisites | **missing (two)** | (1) The 569i conversion requires a divergent candidate pool (cand_world_pairwise_dist > floor); the axis-(b) foraging regime destroys it on 2/3 seeds. (2) z_harm_a must sit in a sub-saturating oscillation band for C3 -- the trained harm pathway saturates it regardless of 10x-lower pulsed input. The 603q harm-landscape-formation prerequisite is now MET (harm_eval_range 3/3). |
| Implementation | complete | Conversion config wired (shortlist size 3.0, authority active 4000 ticks); the four readiness gates fired correctly and refused a verdict; 603q stabilization landed. |
| Environment | **wrong pressures (persists)** | The 10x magnitude reduction + pulsing did NOT desaturate z_harm_a (~6.3 -> ~4.8, 0 crossings) and did not restore candidate-pool divergence. The axis-(b) overlay still delivers a tonic, candidate-pool-collapsing regime. |
| Measurement | adequate, with a gate gap | C3 dynamic-crossings + the four non-vacuity gates are well-designed and the self-route is correct; BUT the readiness set lacks a "z_harm_a oscillation-capable band" precondition, so the saturation blocker is masked behind the r3/r4 fail. |
| Integration | isolated->unstable | The 569i conversion works in isolation (reef-bipartite, 569i PASS) but the interaction with the axis-(b) saturated-threat + candidate-pool-collapse regime collapses it -- F-dominance reasserts. |
| Scale | n/a | -- |

**Recommended `epistemic_category`:** `substrate_ceiling` (advisory; tags no claim -- a plan-node
disposition, not a claim re-score). The right response is upstream substrate enrichment
(MECH-439 F-rebalance), NOT more axis-(b) experiments on the existing substrate.

---

## 6. Learning extracted

1. **The 569i conversion PASS is env-conditional, re-confirmed under recalibration.** 625d
   established this; 625e proves it survives the 625d-prescribed fixes -- the thin top-k margin does
   NOT survive the full axis-(b) composite (committed entropy 0.0; r4 0/3). 625e is the empirical
   answer to `conversion_ceiling_phase0_synthesis` open-Q#1: F-dominance reasserts under the
   foraging substrate's natural monostrategy. This **strengthens the MECH-439 hard-ceiling framing**
   (open-Q#2) and the priority of attacking root B directly.
2. **z_harm_a saturation is NOT controllable by env-overlay magnitude scaling under the trained
   harm pathway.** A 10x input reduction (0.2 -> 0.02) + duty-cycled pulsing moved z_harm_a only
   ~6.3 -> ~4.8, nowhere near the 0.4 oscillation band; 0 crossings. C3 dynamic-crossing is
   therefore unreachable by axis-(b) threat recalibration alone. This is a NEW finding beyond 625d
   (which hypothesized recalibration would desaturate). It implies either a z_harm_a
   operating-range / normalization substrate question, or a crossing-threshold that is mis-specified
   relative to the trained-pathway z_harm_a band -- to be resolved upstream, not by another axis-(b)
   re-tune.
3. **The R1-R4 readiness set has a gap: no "z_harm_a oscillation-capable band" precondition.** It
   gates engagement (r1), nonzero affect (r2), conversion (r3), and committed diversity (r4) -- but
   not whether z_harm_a can physically cross 0.4. Add one so a future run cannot reach a vacuous C3
   verdict on a saturated channel.
4. **603q harm-pathway stabilization is validated as a side-effect.** harm_eval_range nonzero on
   3/3 seeds (vs 625d 1/3). The decoupled-encoder-LR + warmup fix worked; the seed-fragility branch
   of the 625d learning is closed.
5. **Recurrence note (granularity-debt):** this is the Nth autopsy circling the
   committed-action-diversity / F-dominance locus on `sd_037_axis_b:P1b` (625b -> 625d -> 625e). The
   `/claim-synthesis` flag was already raised by the 625d autopsy (ARC-065 / GAP-A), and the
   `conversion_ceiling_phase0_synthesis_2026-06-18` has ALREADY decomposed the locus into four
   mechanistically-distinct roots and registered MECH-439 as the F-dominance root. So the
   granularity debt is substantially DISCHARGED; 625e CONFIRMS the synthesis empirically rather than
   demanding a fresh decomposition. The correct routing is to **sequence P1b behind the
   MECH-439/689a F-rebalance chain**, not to re-flag /claim-synthesis.

---

## 7. Routing (user-confirmed 2026-06-20)

**Primary: governance-disposition (non_contributory; HOLD `sd_037_axis_b:P1b`), with a coupled
substrate POINTER. NOT a re-queue.**

- **Disposition:** `evidence_direction: non_contributory` (unchanged from the manifest). SD-037 /
  MECH-280 / MECH-281 stay `substrate_ceiling` / `pending_retest_after_substrate`. `sd_037_axis_b:P1b`
  stays `in_progress` / upstream-blocked; the hard upstream gate is now the **MECH-439 / 689a
  F-rebalance chain** (689 first falsifier FAILed 2026-06-19 -> redesigned to V3-EXQ-689a with
  gap-blind control arms; until MECH-439 demonstrably lifts the F-dominance ceiling, a P1b successor
  reproduces 625e's r4=0.0). **Do NOT blindly requeue a 625f axis-(b) recalibration** -- F-dominance
  is unmoved by threat tuning, and z_harm_a saturation persists under magnitude scaling.
- **Coupled substrate amend (Section 9, action=amend):** record both findings on the SD-037
  substrate_queue owner (which already carries `axis_b_625d_autopsy_pointer_2026_06_19`) and point
  P1b's upstream gate at the shared MECH-439 / `behavioral_diversity_isolation:GAP-A` F-rebalance
  ceiling. POINTER to existing substrate work, not a new build.
- **No claims.yaml change** (tags no claim). **625d supersession:** 625e supersedes 625d (declared
  in the manifest). Both tag claim_ids=[] / non_contributory, so neither weights a claim and the
  supersession is queue-lineage bookkeeping (scoring-neutral). Governance MAY set
  `evidence_direction: superseded` on the 625d manifest for tidiness, but it changes no
  confidence/conflict score.

Draft `evidence_quality_note` text -- governance need NOT write a claim note (no claim); recorded
here for the plan-node `governance_*` line governance will append:

> "V3-EXQ-625e (supersedes 625d) self-routed `substrate_not_ready_requeue` (R3 1/3, R4 0/3) --
> internally consistent, weakens nothing. Autopsy 2026-06-20: the 625d-prescribed recalibration
> (axis-(b) threat 10x-lower + pulsed ON40/OFF40; 603q-stabilized harm pathway) did NOT clear the
> two blockers. (1) Committed-action monostrategy persists (entropy 0.0 3/3; cand_world_pairwise_dist
> < floor 2/3) -- the MECH-439 F-dominance conversion ceiling reasserting under the axis-(b) foraging
> composite; 625e empirically answers conversion_ceiling_phase0_synthesis open-Q#1 (the thin 569i
> top-k margin does NOT survive the full composite; 569i's committed-diversity demo was env-conditional
> on the reef-bipartite structural guarantee, absent on axis-(b)). (2) z_harm_a stayed saturated
> (~4.8 mean, 0 crossings of 0.4) despite the 10x magnitude reduction + pulsing -- the trained harm
> pathway maps even a 10x-reduced pulsed harm stream to a saturated affective latent, so C3 dynamic
> crossings are unreachable by env-recalibration alone (a missing readiness precondition: no
> z_harm_a-oscillation-band gate). 603q stabilization DID fix the harm-landscape seed-fragility
> (harm_eval_range nonzero 3/3 vs 625d 1/3). Route: HOLD P1b, sequenced behind the MECH-439/689a
> F-rebalance chain; do NOT blindly requeue an axis-(b) recalibration. SD-037/MECH-280/MECH-281
> unchanged."

---

## 8. Granularity-debt recurrence (/claim-synthesis) -- ALREADY DISCHARGED

This is the second-or-later autopsy circling `sd_037_axis_b:P1b` (625b 2026-06-02; 625d 2026-06-18;
625e 2026-06-20), which normally triggers a proactive `/claim-synthesis` hook. It does NOT here,
because the decomposition has already happened:

- The 625d autopsy already surfaced the `/claim-synthesis` flag on ARC-065 / GAP-A.
- `conversion_ceiling_phase0_synthesis_2026-06-18.md` (7-agent workflow `wf_c03ff4f4-d45`) already
  decomposed the committed-action-diversity / F-dominance locus into FOUR mechanistically-distinct
  roots (A z_world collapse mitigated / **B F-dominance LIVE ROOT** / C de-commit orthogonal-open /
  D CRF-lockout closed / E within-class = symptom-of-B) and registered MECH-439 as the F-dominance
  root with its own first falsifier (689 -> 689a).

So 625e adds a confirming data point (B reasserts under the axis-(b) composite; answers open-Q#1),
not a new finer claim. The granularity debt the recurrence would flag is discharged; the
load-bearing next step is the MECH-439 / 689a F-rebalance chain, which P1b is now sequenced behind.
