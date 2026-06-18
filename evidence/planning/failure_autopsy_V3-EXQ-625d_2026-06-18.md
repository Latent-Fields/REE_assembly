# Failure Autopsy — V3-EXQ-625d (sd_037 axis-b P1b joint-composite)

- **Generated:** 2026-06-18T05:52:50Z
- **Scope:** single
- **Status:** confirmed
- **Run:** `v3_exq_625d_sd037_axis_b_phase1b_joint_composite_20260617T160019Z_v3` (ree-cloud-3)
- **Queue id:** V3-EXQ-625d (supersedes V3-EXQ-625c)
- **Claim ids:** `[]` (substrate-readiness diagnostic; weights NO claim)
- **Owner node:** `sd_037_axis_b:P1b` (`evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md`)
- **Pipeline flag adjudicated:** `precondition_unmet` (self-route `substrate_not_ready_requeue`, `non_contributory`)

---

## 1. What was being tested

JOINT-COMPOSITE Phase-1b: a policy trained THROUGH the full `scaffolded_sd054_onboarding`
curriculum (603n config) + the **569i-validated TOP-K shortlist conversion config**
(`use_modulatory_shortlist_then_modulate` mode=top_k k=3 + `use_modulatory_selection_authority`
gain=2.0 std-basis + `use_modulatory_channel_routing` source=cand_world_summary +
`candidate_summary_source=e2_world_forward`) + MECH-341 + SD-056 online, measured for **z_harm_a
dynamic crossings** (sharpened C3a≥1 above→below AND C3b≥1 below→above per seed, ≥2/3 seeds) under
the **SD-029 axis-(b) sustained-threat overlay** (`scheduled_external_hazard` interval=20 prob=0.7
adjacent_only + hazard_harm=0.2 + proximity_harm_scale=0.2) on a dim-matched scaffold p2 env
(reef-bipartite + SD-049 + limb_damage).

Pre-registered: PASS = C3 (≥2/3) AND all four non-vacuity preconditions (R1 curriculum fired 3/3;
R2 z_harm_a nonzero; R3 in-arm route_range AND cand_world_pairwise_dist above floors; R4
committed-action entropy above floor). A precondition miss self-routes
`substrate_not_ready_requeue` — NEVER a weakens. Preconditions met + sub-2/3 C3 → genuine residual
verdict → /failure-autopsy.

---

## 2. Facts — reconstruction (no interpretation)

| Readiness gate | Threshold | seed 42 | seed 43 | seed 44 | frac | Met |
|---|---|---|---|---|---|---|
| R1 curriculum fired (external_hazard_event_count) | >0, 3/3 | 9 | 27 | 28 | 3/3 | **MET** |
| R2 z_harm_a nonzero fraction | ≥0.01, ≥2/3 | 1.0 | 1.0 | 1.0 | 3/3 | **MET** |
| R3 route_range_mean | >0.01 | 0.0845 | **0.0** | **0.0** | — | — |
| R3 cand_world_pairwise_dist_mean | >0.03 | **0.0245** | 0.0511 | **0.0118** | — | — |
| **R3 conversion operative** (both above) | ≥2/3 | F | F | F | **0/3** | **UNMET** |
| R4 selected_action_class_entropy | >0.3, ≥2/3 | **0.0** | **0.0** | **0.0** | **0/3** | **UNMET** |
| C3 dynamic crossings (above↔below 0.4) | ≥2/3 | 0/0 | 0/0 | 0/0 | 0/3 | FAIL |

Supporting per-seed facts:

- **z_harm_a is pinned high, never relieves:** z_harm_a_mean **5.88 / 6.74 / 6.27**; z_harm_a_max
  **6.06 / 6.95 / 6.37**; nonzero-frac 1.0. Crossings of the 0.4 threshold: **0 above→below AND 0
  below→above** on every seed (the "continuously-frozen-above" state the script's C3 doc names).
- **Committed policy monostrategy-locked:** `selected_class_counts` = `{"0":472}` / `{"0":1061}` /
  `{"0":1061}` — every measure tick selected action-class 0; entropy 0.0 on all three seeds.
- **Harm landscape seed-fragile:** harm_eval_range **0.283 / 0.0 / 0.0**; harm_pathway_n_train_steps
  4030 / 5262 / 3745. The harm pathway trained but the E3 harm_eval head is discriminative on only
  1/3 seeds (flat on 43/44) — the 603p seed-fragility signature.
- Scaffold legs all reached P1 (reached_p1 True 3/3; p1_survival_pass T/T/F; hazard_stage_survival
  pass 3/3). The base policy is survival-competent; the failure is NOT a curriculum collapse.

---

## 3. The decisive comparison — 569i (converted) vs 625d (collapsed)

The conversion config is **byte-identical** between V3-EXQ-569i (PASS/supports, ARC-065) and
V3-EXQ-625d. What differs is the **measurement environment**, and that difference is the whole story.

| | V3-EXQ-569i (conversion CONVERTED) | V3-EXQ-625d (conversion DID NOT) |
|---|---|---|
| Env | scaffold p2, **reef-bipartite** layout, **hazard_harm 0.05** (low), no sustained-threat overlay | scaffold p2 + **axis-b sustained-threat overlay** (hazard_harm 0.2, proximity_harm_scale 0.2, scheduled hazard interval 20 prob 0.7) |
| Harm pathway | trained, low-harm env → z_harm_a small | trained → z_harm_a **mean ~6** (≈14× the 625b-era p70≈0.43 on the *untrained* base) |
| cand_world_pairwise_dist | **0.073 / 0.089 / 0.084** (3/3 > floor) | **0.024 / 0.051 / 0.012** (1/3 > floor) |
| route_range | 0.247 / 0.313 / 0.241 (3/3 operative) | 0.085 / 0.0 / 0.0 |
| committed entropy | 1.23 / 0.0 / 0.90 → strict-above both controls 2/3 → **PASS** | 0.0 / 0.0 / 0.0 → **monostrategy lock** |

**569i's reef-bipartite env STRUCTURALLY forces categorically-opposite first-action argmaxes** (the
SD-054 bipartite extension), which is what holds cand_world_pairwise_dist above floor and gives the
top-k conversion a divergent candidate pool to arbitrate over. **The axis-b env provides no such
structural guarantee, and the sustained-threat overlay collapses the candidate pool.** The 569i
conversion PASS is therefore **env-conditional**: it was demonstrated on a substrate that structurally
guarantees the candidate-divergence precondition; it does not propagate to the saturated-threat regime
that removes it.

(Note: even 569i had seed 43 collapse to entropy 0.0 with cand_world_pairwise_dist 0.089 above floor —
so candidate-pool spread above the floor is necessary but not sufficient; the bipartite *structure*
matters, not just the scalar.)

---

## 4. Why committed-action entropy collapses to 0 on axis-b — three coupled mechanisms

All three co-occur across seeds, all downstream of the axis-b **saturated-threat regime** over a
**trained-but-seed-fragile** harm pathway:

1. **z_harm_a saturation (the C3a "frozen-above" cause, independent of committed diversity).**
   z_harm_a is pinned at mean ~5.9–6.7, never near 0.4 from below → 0 downward crossings *regardless
   of action diversity*. The env overlay (hazard_harm 0.2, proximity_harm_scale 0.2) was sensitivity-
   tuned in §1.2/§2.1 of the plan against an **untrained** harm pathway (625b saw z_harm_a p70≈0.43);
   with the trained pathway (`scaffold_train_harm_pathway=True`, the post-625b/c amend) the same
   overlay over-drives z_harm_a ~14× into saturation. The C3 dynamic-crossing criterion presupposes a
   *risk-assessment-oscillation* regime (sub-saturating, time-varying threat); the env delivers a
   *tonic-immobility* regime.

2. **Candidate-pool collapse (R3 / hypothesis a — confirms 614e's z_world-collapse locus).**
   cand_world_pairwise_dist 0.024/0.051/0.012 collapses below floor on 2/3 (the SD-056
   e2.world_forward per-candidate spread — the representation the top-k conversion re-sources). With a
   near-identical candidate pool the routed world-summary channel carries ~0 range (route_range 0.0 on
   seeds 43/44), so the top-k shortlist + selection authority have no per-candidate structure to convert
   → within-set argmin constant.

3. **F-dominance + harm-pathway seed-fragility (hypothesis c — seed 42 the clean case).**
   On seed 42 the route_range **was** operative (0.085 > floor) and the top-k shortlist fired (size 3)
   — yet committed entropy was still 0.0. The saturated z_harm_a (~5.88) with a discriminative harm_eval
   (range 0.283) makes the primary F-score so peaked that the same action wins within the top-3 F-best
   every tick; the modulatory range (0.085) is negligible against the F-driven spread (cf. V3-EXQ-571's
   88–89% F-dominance). On seeds 43/44 the harm_eval landscape is **flat (range 0.0)** — the 603p
   harm-pathway seed-fragility (landscape forms on ~1/3 seeds); the 603q-stabilized config (decoupled
   encoder LR + warmup) was not used in this run.

The three couple into a vicious cycle: a monostrategy-locked policy that always takes one action under
sustained threat never escapes/relieves → z_harm_a stays saturated → huge harm cost F-dominates E3
scoring → collapses behavioural diversity → … .

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | Tags no claim; SD-037/MECH-280/MECH-281 stay substrate_ceiling/pending_retest. |
| Biological reference | partial | Saturated z_harm_a~6 → single defensive action is the *tonic-immobility/learned-helplessness* regime — biologically faithful, but the wrong regime for the *risk-assessment-oscillation* the C3 dynamic-crossing criterion presupposes. |
| Prerequisites | **missing** | The 569i conversion requires a **divergent candidate pool** (cand_world_pairwise_dist > floor); the axis-b saturated-threat regime destroys it. Also the trained harm pathway needs the 603q stabilization to form a landscape on ≥2/3 seeds (here 1/3). |
| Implementation | complete | Conversion config wired identically to 569i; the four readiness gates fired correctly and refused a verdict. |
| Environment | **wrong pressures** | The axis-b overlay over-drives z_harm_a into saturation (tonic, not time-varying) AND collapses the candidate pool. Overlay calibrated against an *untrained* harm pathway. |
| Measurement | adequate | C3 dynamic-crossings + the four non-vacuity gates are well-designed; the self-route is correct. |
| Integration | isolated→unstable | Conversion works in isolation (569i) but the interaction with the saturated-threat regime collapses it. |
| Scale | n/a | — |

**Recommended `epistemic_category`:** `substrate_ceiling` (advisory; tags no claim — this is a
plan-node disposition, not a claim re-score).

---

## 6. Learning extracted

- The **569i conversion PASS is env-conditional**, not unconditional. It rests on the reef-bipartite
  env's structural guarantee of categorically-opposite first-action argmaxes. The conversion-
  propagation claim must be demonstrated on a **threat-engaged, non-bipartite, harm-elevated** regime
  before P1b can treat the conversion as available on axis-b.
- The **trained harm pathway changes z_harm_a magnitude ~14×** vs the untrained base the axis-b env
  overlay was calibrated against (625b p70≈0.43 → 625d mean≈6). The plan's §1.2/§2.1/§5 target ranges
  and overlay knobs need re-derivation for the trained-pathway regime; and the threat must be made
  **time-varying/pulsed** so z_harm_a can relieve and cross 0.4 downward (the C3a fix), not just
  magnitude-tuned.
- The **603p harm-pathway seed-fragility** (flat harm_eval on 2/3 seeds) is implicated; a 625d
  successor should adopt the **603q-stabilized** harm config (decoupled encoder LR + warmup).
- This is the **Nth autopsy circling the committed-action-diversity / F-dominance locus** (569g/569h/
  614e + the long modulatory-bias-selection-authority GAP-A amend chain) — granularity-debt signal
  (see §8).

---

## 7. Routing (user-confirmed 2026-06-18)

**Primary: `queue-experiment` (a V3-EXQ-625e successor), with a coupled substrate POINTER.**

- **625e successor (immediate next step):** recalibrate the axis-b env for the trained-harm-pathway
  z_harm_a magnitude — bring z_harm_a into a sub-saturating, oscillation-capable band (lower
  hazard_harm / proximity_harm_scale ~10× from 0.2) **and** make the threat **time-varying/pulsed**
  (on/off windows) so z_harm_a relieves and can cross 0.4 downward; **and** adopt the 603q-stabilized
  harm-pathway config so the landscape forms on ≥2/3 seeds. Carry the GAP-A conversion-propagation as a
  **hard upstream gate** (R3/R4 self-route stays — a recalibrated threat alone will not clear the
  candidate-pool collapse). Addresses causes (1) and (3).
- **Coupled substrate amend (the recommended_substrate_queue_entry below):** record the env-conditional-
  conversion finding on the `sd_037_axis_b` owner and **point at the shared
  `behavioral_diversity_isolation:GAP-A` / `modulatory-bias-selection-authority` conversion-propagation
  ceiling** — the conversion must be shown to survive a threat-engaged candidate pool before P1b
  re-gates. Addresses cause (2). This is a POINTER to existing substrate work, not a new build.

**No claims.yaml change** (tags no claim). SD-037/MECH-280/MECH-281 stay `substrate_ceiling` /
`pending_retest_after_substrate`. `sd_037_axis_b:P1b` stays non-terminal (owner_exq advances
625d → 625e on governance application; status stays upstream-blocked on the GAP-A demonstration under
threat).

Draft `evidence_quality_note` text — governance need NOT write one (no claim); recorded here for the
plan-node `governance_*` line governance will append:

> "V3-EXQ-625d self-routed `substrate_not_ready_requeue` (R3 0/3, R4 0/3) — internally consistent,
> weakens nothing. Autopsy 2026-06-18: committed-action monostrategy-lock (entropy 0.0 3/3) is
> over-determined by the axis-b saturated-threat regime — z_harm_a pinned ~6 (trained harm pathway
> over-drives the 625b-era overlay ~14×; 0 crossings), candidate-pool collapse (cand_world_pairwise_dist
> < floor 2/3), and F-dominance over the modulatory range (seed 42 route_range operative yet entropy 0).
> The 569i conversion PASS is env-conditional (reef-bipartite structural divergence guarantee, absent on
> axis-b). Route: 625e successor (sub-saturating + pulsed threat + 603q harm config + GAP-A
> conversion-propagation as hard upstream gate); conversion-propagation-under-threat amend pointer on
> the shared GAP-A / modulatory-bias-selection-authority ceiling. SD-037/MECH-280/MECH-281 unchanged."

---

## 8. Granularity-debt recurrence (/claim-synthesis flag — user-confirmed)

This is the Nth autopsy circling the **committed-action-diversity / F-dominance / committed-argmax-
collapse** locus, each with a different failure signature: 569g (entropy-only artefact), 569h
(conversion-ceiling persists), 614e (z_world candidate-pool collapse), 460e (beta-engagement), plus the
long modulatory-bias-selection-authority amend chain (gap-relative → float32 → route-range → gain/
contrast → top-k). The recurrence is the signal: the broad ARC-065 / `behavioral_diversity_isolation`
GAP-A claim is probably several finer testable claims (candidate-pool-divergence vs route-range-reach vs
F-dominance-budget vs env-structural-precondition), not one. **Recommendation: surface ARC-065 / GAP-A
to `/claim-synthesis`** for proposal-first, lit-grounded decomposition into testable children — even
though 625d's own routing is substrate/experiment. 625d adds the **env-conditional-conversion** edge:
the conversion's success is contingent on an upstream env-structural candidate-divergence guarantee.
