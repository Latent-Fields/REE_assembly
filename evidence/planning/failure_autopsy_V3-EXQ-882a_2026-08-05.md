# Failure Autopsy: V3-EXQ-882a (MECH-472 held-out-context vs task-memorisation, EXP-0400)

**Generated:** 2026-08-05T16:34:31Z | **Status:** confirmed | **Scope:** single (cross-referenced with the already-open `mech471_competence_acquisition_reliability` hypothesis-space question -- see Section 5)

## 1. Facts reconstruction

- **Run:** `v3_exq_882a_mech472_context_memorization_generalization_20260805T110228Z_v3`, queue_id `V3-EXQ-882a`, `supersedes=v3_exq_882_mech472_context_memorization_generalization`, `experiment_purpose=evidence`, `outcome=FAIL`, `evidence_direction=unknown` (self-routed), `dry_run=false`.
- **Dry-run check:** `check_dry_run_citations.py` -> 0 dry, 1 clean. Not a smoke.
- **Recording:** `validate_recording.py` -> OK, 1 complete, 0 always-core gaps. `substrate_stable_across_run=true`, `machine=ree-worker-1`, `elapsed_seconds=103155` (~28.6h).
- **What 882a corrects (per its own docstring, both confirmed defects from `failure_autopsy_V3-EXQ-882_2026-08-03` Sections 7/9/10):**
  1. DEFECT 1 (the load-bearing fix, Section 9/10 of the prior autopsy): `zworld_p0_episodes` was never passed to the acquisition call in V3-EXQ-882, so the SD-070 z_world P0a warmup never ran and `z_world` stayed a frozen random projection all run -- confirmed. 882a wires `zworld_p0_episodes=60` (the V3-EXQ-728/875a validated operating point) on a dedicated warmup env. **Confirmed applied**: `config.zworld_p0_episodes=60` in the manifest.
  2. DEFECT 2 (Section 5/7): 882's readiness precondition was a worst-of-3-seed veto. 882a raises seed count 3 -> 8 and adjudicates the acquisition floor on a **fraction basis** (majority must clear; non-clearing seeds recorded informationally, excluded from the load-bearing gap cohort). **Confirmed applied**: `readiness.acquisition_basis="seed_fraction_majority"`, `acquisition_seed_fraction_floor=0.5`, `n_seeds=8`.
  3. DEFECT 3 (recording gap): 882a emits an explicit `per_seed_acquisition_difficulty` block instead of forcing the reader to reconstruct the split from `arm_results`. **Confirmed present.**
- **Self-route label:** `substrate_not_ready_requeue`. `non_degenerate: false`. `degeneracy_reason`: "acquisition-floor clear fraction 0.250 did not exceed floor 0.500 at lowest exposure (cleared 2/8 seeds)".
- **Design.** Identical to 882: paired in-context vs held-out-context evaluation of ONE trained survival/avoidance competence under the "corner" reef geometry (`hazard_food_attraction=0.0`, decoupled from foraging), SD-056 e2 warmup then P1 REINFORCE (e2 frozen, A0 recipe -- "exactly the V3-EXQ-875a / x724 `_train_all_on_agent` recipe" per the driver's own docstring) for `exposure` in {50, 100, 250, 500} episodes, now across 8 seeds (42, 43, 45, 46, 47, 48, 49, 50; seed 44 skipped per repo convention -- recurring early-death instability). Evaluated in-context (fresh env, same seed) vs held-out (fresh env, `seed + 10007`, identical kwargs). Primary DV unchanged: `gap = in_context.survival_horizon - held_out.survival_horizon`, computed over the CLEARED cohort only, swept across exposure.
- **Readiness gate (fraction basis, 8 seeds, lowest exposure=50):** `survival_floor_ticks=90.0` (60% of 150-step episode), `random_margin_ticks=22.5` (15% margin over random-walk anchor). **2/8 seeds clear (25%)** -- seeds 43 and 50. **6/8 never clear, at any exposure tested, up to 500 episodes (10x budget):**

  | Seed | @50 | @100 | @250 | @500 | Ever clears 90-tick floor? |
  |---|---|---|---|---|---|
  | 42 | 17.50 | 20.00 | 12.50 | 23.25 | No |
  | 43 | 90.83 | 91.67 | 91.83 | 128.92 | Yes, at every exposure |
  | 45 | 22.58 | 59.00 | 27.33 | 29.25 | No |
  | 46 | 28.08 | 30.42 | 23.17 | 17.83 | No |
  | 47 | 16.58 | 29.25 | 32.58 | 37.08 | No |
  | 48 | 13.00 | 18.58 | 11.75 | 27.25 | No |
  | 49 | 21.75 | 27.33 | 21.08 | 20.83 | No |
  | 50 | 115.00 | 108.25 | 93.25 | 60.00 | Yes, at every exposure (note: *declines* with more training -- 115 -> 60 from 50 to 500 episodes) |

  The 6 non-clearing seeds show flat, noisy trajectories in the 12-37 tick range with **no improving trend** across a 10x exposure sweep -- none approaches the 90-tick floor even once. This is a stronger, better-powered version of the identical shape 882 showed at n=3 (1/3 clears immediately and stays solved; 2/3 never approach the floor across the same 10x range).
- **Expected vs observed:** expected -- both confirmed 882 confounds were fixed, and the driver's own docstring pre-registered the outcome as informative either way ("either it clears the per-seed split ... or it does not, which STRENGTHENS the genuine-difficulty reading by ruling this confound out"). Observed -- the split did NOT clear; the fraction stayed essentially unchanged (25% at n=8 vs ~33% at n=3), and the flat-across-exposure shape persisted with the z_world confound eliminated. **The failed criterion is again the readiness precondition** (now the fraction-based acquisition floor), not the discrimination criterion -- the decisive MECH-472 question remains unreached, for the second generation running.
- **Non-degeneracy check on the excluded question itself:** with only 2/8 seeds clearing, the cleared-cohort dose-response (`per_exposure_mean_gap_survival`: 9.58/12.38/2.37/10.63 ticks at 50/100/250/500) shows no clean monotonic widening and is statistically underpowered (n=2) -- correctly excluded from any decisive read by the non-degeneracy flag; not over-interpreted here.

## 2. Claim-layer mapping (MECH-472)

- **Text:** "HELD-OUT CONTEXT distinguishes skill acquisition from task memorisation..." `claim_type: mechanism_hypothesis`, `epistemic_category: standard`, `status: candidate`, `depends_on: [MECH-471, ARC-092]`.
- **Prior evidence:** V3-EXQ-882 (first-ever test, `precondition_unmet`, same acquisition-floor failure at n=3, confound-laden). This is the SECOND test, with both identified confounds from the first now fixed.
- **Did the experiment test the claim under conditions where it could express itself?** No, again, and again correctly so per the claim's own pre-registered non-degeneracy guard -- the decisive in-context/held-out comparison presupposes acquisition happened on a majority of seeds; it did not (25% vs the 50% floor required). `claim_ids` accuracy: correct, single-claim.
- **The dependency chain is now the load-bearing fact.** MECH-472 formally `depends_on: [MECH-471, ARC-092]`. Both 882 and 882a's acquisition-floor failures are occurring in the exact machinery (`_train_all_on_agent`, e2-frozen REINFORCE, all-ON REE stack, "corner" reef geometry) that MECH-471's own autopsy trail (V3-EXQ-728, 875, 875a -- see Section 5) has been independently diagnosing as unreliable across seeds for the same reasons, on overlapping seeds, with the same qualitative split. This is not a coincidence of shared library code; it is the SAME underlying open question surfacing through two different downstream claims' experiments.

## 3. Biological / formal-reference triage

Unchanged from V3-EXQ-882's own triage (Section 3 of `failure_autopsy_V3-EXQ-882_2026-08-03.md`): MECH-472 is an ML-methodology import (generalization-gap-as-promotion-gate), not a biological-mechanism translation; no biology citation is needed or claimed. Nothing in this run's evidence changes that character -- the failure occurs one level below where MECH-472's own question begins (at acquisition, not at the held-out-context comparison), so the biological-reference triage for MECH-472 itself is orthogonal to this run's finding.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | Decisive comparison still unreached; the claim's own guard correctly withheld a verdict for the second generation running. |
| Biological reference | **absent / not applicable** | ML-methodology import; unchanged from 882's triage. |
| Developmental / dependency prerequisites | **missing, and now the central finding** | MECH-472 `depends_on MECH-471`; MECH-471's own acquisition-reliability question is open and unresolved (see Section 5). This run's failure is best read as a symptom of that unresolved dependency, not an independent MECH-472-specific gap. |
| Implementation completeness | **complete and exercised** | Both confirmed 882 defects fixed and verified present in the manifest (`zworld_p0_episodes=60`, fraction-basis gate). No new implementation gap found. |
| Environment adequacy | **stable, reproduced split** | Same "corner" geometry as 882 and as V3-EXQ-875/875a's variant A. The per-seed difficulty split (seeds 43, 50 solve; 42/45/46/47/48/49 do not) reproduces the qualitative shape seen at n=3, now with n=8 and the confound eliminated. |
| Measurement adequacy | **adequate -- guard worked as designed, twice now** | The fraction-basis non-degeneracy guard correctly withheld a decisive read a second time rather than let a floor-artefact gap masquerade as a memorisation signal. |
| Integration adequacy | **coupled and stable** | No cross-module instability; z_goal_stream writer confirmed non-defective (`writer_defect=false`), substrate hash stable across run. |
| Scale / capacity | **the decisive open question, now better-evidenced** | 500 REINFORCE episodes (10x the lowest exposure) produced no improving trend for any of the 6 failing seeds. Combined with the z_world confound now ruled out, this argues more strongly than 882 alone could that more training on the SAME recipe will not close the gap -- but whether this reflects a genuine environment-difficulty split (some seed draws are harder) or a genuine acquisition-recipe capacity ceiling (some hazard/resource layouts are unlearnable by this specific recipe regardless of difficulty framing) remains open, and is squarely the open question under Section 5. |

## 5. Cross-reference: `mech471_competence_acquisition_reliability` (hypothesis-space ledger)

This is the load-bearing section of this autopsy. On 2026-08-05T06:20:43Z, a prior `/failure-autopsy` session (this morning's batch, targets V3-EXQ-875/875a) registered the question `mech471_competence_acquisition_reliability` in the hypothesis-space registry:

> "Why does survival-competence acquisition on the all-ON REE stack succeed reliably for some seeds and fail near-baseline for others, even after the SD-070 z_world fix and an aligned training budget?"

with three live hypotheses (H-exploration-init-variance, H-hazard-layout-difficulty-variance, H-bias-head-ofc-interaction) and a recommended "cheap, many-seed diagnostic probe (competence-A acquisition only, 10-20 seeds, modest budget)" -- **not yet queued** as of this autopsy.

**V3-EXQ-875a's own evidence** (MECH-471, seeds 42/43/45, budget aligned to V3-EXQ-728's validated recipe): seed 43 clears the floor strongly (172/181 ticks near a ~200-tick episode ceiling); seeds 42 and 45 stay near the random-walk baseline (~15-24 ticks) regardless of budget.

**V3-EXQ-882a independently reproduces the identical qualitative split** on overlapping seeds, using the same underlying acquisition recipe (`_train_all_on_agent`, e2-frozen REINFORCE, z_world warmed, all-ON REE stack) applied toward a *different* downstream claim (MECH-472's held-out-context comparison, rather than MECH-471's targeted-update/provenance gap):

- Seed 43: clears strongly in BOTH runs (875a and 882a).
- Seed 42: fails to clear in BOTH runs.
- Seed 45: fails to clear in BOTH runs.
- 882a additionally samples 5 new seeds (46-50) at n=8 total: only seed 50 joins seed 43 in clearing; the other 4 new seeds (46, 47, 48, 49) fail identically to 42/45's pattern.
- 882a's fuller dose-response (50/100/250/500 vs 875a's more limited sweep) shows **no improving trend for any of the 6 failing seeds** across a 10x exposure range.

**Reading, per the user's confirmed disposition at this autopsy's Step 8 gate:** this is treated as **informative corroborating context, not a formal resolution of H1/H2/H3.** 882a was not designed as a discriminator among the three hypotheses (it does not, for instance, isolate whether bias_head/OFC-devaluation drives were active during its acquisition phase the way H-bias-head-ofc-interaction would need to test). What it does add: the flat, non-improving trajectory across a 10x exposure sweep on 6 of 8 seeds weighs against H-exploration-init-variance's framing that failing seeds are stuck in an *early* local optimum that more training could plausibly escape -- none show a late-training rescue. It does not by itself distinguish H-hazard-layout-difficulty-variance from H-bias-head-ofc-interaction. The dedicated cheap many-seed probe recommended this morning remains the correct instrument to formally discriminate the three hypotheses, and per this autopsy's Step 8 gate is now **prioritised higher** given this independent n=8 replication (chipped below, Section 7).

The hypothesis-space registry's `mech471_competence_acquisition_reliability.decision.distance_phrase` is updated (Step 9b, this autopsy) to record this cross-reference. No hypothesis is moved out of `alive`; `initial_frozen_count` is untouched; no growth event is recorded because nothing was added to or removed from the frozen set.

## 6. Learning extracted

- Both prescribed fixes from the prior autopsy (z_world warmup, fraction-basis gate) were correctly and verifiably applied, and the driver's own docstring correctly pre-registered the informativeness of either outcome -- this is a second instance of a non-degeneracy guard, together with a well-designed corrective re-run, working exactly as intended even though the run itself did not reach its decisive comparison.
- The acquisition-reliability split first identified under MECH-471 is not confined to MECH-471's own experiments -- it recurs, on overlapping seeds, in an independently-authored MECH-472 experiment sharing the same underlying training machinery. This is the kind of convergent, cross-claim signal the granularity-debt/cluster machinery exists to surface, even though it crosses claim boundaries in a way the standard single-claim recurrence trigger does not check for.
- With the z_world confound now ruled out and the seed count raised from 3 to 8, the flat, non-improving 10x-exposure trend on the failing seeds is markedly stronger evidence than 882 alone could offer that "more of the same training" will not resolve this -- reinforcing 882's own prior recommendation not to try that lever again.

## 7. Repair pathway

**Diagnosis category (work-graph debt vocabulary):** `complex (probe-gated) / puzzle (known rules)` -- unchanged in kind from 882, but the open question is now explicitly MECH-471's (`mech471_competence_acquisition_reliability`), not a fresh MECH-472-specific puzzle. The frame is well-posed (three named hypotheses); the missing fact is which explains the bimodal split, resolvable by the already-recommended cheap probe rather than by more MECH-472-side re-runs.

**Routing for MECH-472 (V3-EXQ-882a itself):** `governance-hold` -- no successor (V3-EXQ-882b or otherwise) should queue on the same recipe. Per the user's confirmed disposition at Step 8: explicitly hold, pending resolution of `mech471_competence_acquisition_reliability`. This is an informal application of the re-derive brake's spirit -- the formal counter does not fire (0 `substrate_ceiling`-category autopsies on MECH-472; see below) because the correct category here is `precondition_unmet`, not `substrate_ceiling`, and the gating fact belongs to MECH-471's dependency, not to a MECH-472-specific substrate gap. Re-queuing MECH-472 again on the same acquisition recipe before MECH-471's question resolves would very likely just reproduce the identical ~25% clear rate.

**Routing follow-on (chipped, not this autopsy's own recommendation -- see below):** `/queue-experiment` the MECH-471 cheap many-seed diagnostic probe recommended this morning, now at higher priority per the user's explicit confirmation at this autopsy's Step 8 gate.

**Re-derive brake:** does not formally fire. Verified via the R1-R3 counting recipe: MECH-472 has 0 prior `substrate_ceiling`-category autopsies (V3-EXQ-882 itself is `precondition_unmet`, which per R3 does not count). MECH-471 is also at 0 (875 is `precondition_unmet`, 875a is `competence_implementation_gap`). Neither claim's formal brake threshold is met. The hold recommended above is a **user-confirmed informal hold**, not a formal brake firing, and should not be conflated with one in any future recurrence count.

**Draft `evidence_quality_note` (for governance to apply, not written here; appends to the existing MECH-472 note rather than overwriting it):**

> [2026-08-05 failure autopsy, V3-EXQ-882a, confirmed failure_autopsy_V3-EXQ-882a_2026-08-05]: SECOND experimental test of MECH-472, both confirmed defects from the first test (frozen z_world, worst-of-3-seed veto) fixed and verified applied. `non_degenerate=false` again, correctly, per the claim's own guard: acquisition-floor clear fraction 0.25 (2/8 seeds) did not exceed the 0.5 majority floor at the lowest exposure, and none of the 6 non-clearing seeds approach the floor even at 10x exposure budget. The decisive in-context/held-out comparison remains unreached. With the z_world confound now ruled out, this result is best read as a symptom of MECH-472's own registered dependency on MECH-471 -- the same acquisition-reliability split (seed 43 solves, most others do not) independently reproduces on overlapping seeds in V3-EXQ-875a (MECH-471), and is now tracked as the open hypothesis-space question `mech471_competence_acquisition_reliability`. No claim-status change; v3_pending stays as registered. **HOLD on any V3-EXQ-882b or other same-recipe MECH-472 successor** until `mech471_competence_acquisition_reliability` resolves (via its recommended cheap many-seed diagnostic probe, now prioritised) -- re-queuing on the same acquisition recipe before then would very likely reproduce the identical ~25% clear rate.

## 8. Interactive gate (user-confirmed 2026-08-05T16:34Z)

Three questions posed and confirmed:

1. **Cross-claim merge into `mech471_competence_acquisition_reliability`:** user selected "record as informative context only" -- not a formal resolution of any of the three hypotheses. Applied in Section 5 and Step 9b (registry `decision.distance_phrase` updated; no hypothesis resolved, no growth event).
2. **Routing for a future V3-EXQ-882b:** user selected "hold explicitly pending MECH-471's diagnostic probe" -- applied in Section 7 and the draft `evidence_quality_note`.
3. **Priority on the MECH-471 diagnostic probe:** user selected "chip it now at higher priority" -- chipped as `/queue-experiment` follow-on (Session Land Protocol Phase 3; this is `/queue-experiment` work, not this autopsy's own routing recommendation, so the 2026-07-30 self-chip restriction does not apply -- the recommendation was independently confirmed at V3-EXQ-875a's own Step 8 gate this morning, and re-confirmed live by the user in this session).
