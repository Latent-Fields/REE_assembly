# Failure Autopsy (closure pass): MECH-302 / Q-045-MECH-313-MECH-260 / MECH-171 (14 runs, already covered)

**Generated:** 2026-08-08T17:10:36Z
**Scope:** cluster (14 runs across 3 independent sub-groups, 2026-05-04 to 2026-06-12)
**Status:** confirmed (Step 8 interactive gate: user confirmed closure + flag MECH-171 note correction)

## Headline finding

None of these 14 runs are un-autopsied. Every one is already covered by an existing `status: confirmed` failure-autopsy artifact, and every one of the 6 claims already carries an applied disposition in `claims.yaml`. This is a confirm-and-cite pass, not a fresh diagnosis, for all three sub-groups.

## Dry-run gate

`check_dry_run_citations.py` on all 14: 0 dry, 14 clean (top-level check). **Manual follow-up caught a gap the automated checker missed**: `v3_exq_517_..._20260504T132505Z_v3` and `..._20260504T132543Z_v3` (sub-group 1) both carry `config.dry_run: true` -- a **nested** dry-run flag the top-level-only checker doesn't catch. Both already correctly reclassified `non_contributory` with note "Dry-run artifact... reclassified 2026-05-04 governance session." No live risk, but flagged as a real automated-tool gap (see Learning Extracted #2).

## Sub-group 1 -- MECH-302 (relief/completion), 4 runs (2 real after dry-run exclusion)

**Same-day cluster verdict: not 4 independent replicates.** 2 excluded as dry-run smokes (above). Remaining 2 are a same-day recalibration pair: `150341Z` (original comparator, 5-step/5% threshold, `a_pass_rate=0/3`) and `517a` (recalibrated 30-step/0.5% threshold, still `a_pass_rate=0/3`, though `mean_arm_a_p1_events` moved 0.0->0.333).

**Already covered**: `failure_autopsy_V3-EXQ-517b_2026-05-30` (scope: "517/517a/517b -- three attempts of the same discriminative pair"). Reads the identical facts and concludes: dominant failure layer = environment adequacy. A trained avoidance policy learns to avoid hazard contact during warmup, so `z_harm_a` never accumulates enough to arm the comparator -- longer episodes give the policy *more* time to avoid, which is why events fell to zero despite doubling episode length in 517b. Rules out further parameter-tuning letters.

Biological triage (from 517b autopsy): phasic dopaminergic relief signal (Tanimoto & Heisenberg 2004; Roesch/Calu/Schoenbaum 2007) -- `SufferingDerivativeComparator` judged a faithful functional translation (lit_conf 0.897; `targeted_review_relief_completion_mechanism/`, `targeted_review_affect_stream_relief_safety_soothing/`). The critical observation: in the literature the experimenter constructs the suffering trajectory; REE inserts a trained avoidance policy between env and comparator that the biological references don't have -- a missing env prerequisite, not a mistranslation.

**claims.yaml MECH-302**: `status: provisional`, `live_status.evidence.from: failure_autopsy_V3-EXQ-517b_2026-05-30`, `non_contributory/substrate_ceiling`. Matches exactly; no drift found.

**Recommended disposition**: `132505Z`/`132543Z` -- dry-run smokes, already correctly excluded, no action. `150341Z` + `517a` -- fold into the existing confirmed 517b reading: `non_contributory`/`substrate_ceiling`, cite `failure_autopsy_V3-EXQ-517b_2026-05-30`. `routing: governance-note-only`.

**Re-derive brake**: 1 confirmed `substrate_ceiling` hit (517b). Below threshold(2) -- brake does not fire. Consistent with claims.yaml showing no GOV-CEIL-1 demotion (still `provisional`).

## Sub-group 2 -- Q-045/MECH-313/MECH-260 four-arm ablation lineage, 4 runs + Q-043 companion

**Same-day cluster**: 2026-05-21 has three V3-EXQ-603 attempts sharing one instrumentation defect (`act_with_split_obs()` bypasses `select_action()`, so `dacc.record_action()` never fires -- FIFO permanently empty, `ARM_2==ARM_0`/`ARM_3==ARM_1` to 6 decimal places). Already governance-overridden `non_contributory`/`measurement_gap` for all three. `603a` (05-24): call-path fixed, but 2/3 seeds died before the 75-step FIFO warmup -> `measurement_gap`. `603b` (our `20260526T071458Z`): hazard-tuning fix insufficient -- only seed 43 survives (effective N=1) -> folded into cluster as `substrate_ceiling`.

**Duplicate-manifest wrinkle noted (housekeeping only)**: two distinct manifests exist under the "603b" letter at different timestamps -- `20260525T065407Z` (own dedicated autopsy, `measurement_gap`) and our `20260526T071458Z` (folded into the 2026-05-29 cluster, `substrate_ceiling`). Not a contradiction (the second reclassifies once folded into the larger structural finding) but worth a disambiguating note.

**Already covered**: `failure_autopsy_V3-EXQ-603a-b-c-604-605_2026-05-29` -- Cluster A (603a/603b/603c): "convergent four-run chain demonstrating a structural seed-fragility (only seed 43 survives across all four runs) that all four measurement-layer fixes cannot resolve" -- one structural property, missing goal-pipeline/training-regime substrate enrichment, routed `scaffolded_sd054_onboarding`. Cluster B (604 + our 605/Q-043): a second, stacked substrate gap -- per-candidate z_world-variance doesn't propagate from E2 forward-model output, fixed proximally by SD-056 (05-29).

**claims.yaml state (all consistent)**: MECH-313 `epistemic_category: standard`, GOV-CEIL-1 demoted 2026-07-09 (7+ cited hits). MECH-260 `epistemic_category: standard`, GOV-CEIL-1 demoted 2026-07-09 (8+ cited hits). Q-045 `open/substrate_ceiling` -- untestable to date. Q-043 `open/substrate_conditional`.

Biological triage: MECH-313 = LC-NE tonic noise floor (Aston-Jones & Cohen 2005; Haarnoja 2018); MECH-260 = dACC-analog anti-recency bias. Both lit-pulled (`targeted_review_arc_065_behavioral_diversity_generation/`, `targeted_review_rl_diversity_monostrategy_curriculum/`). Faithful biological translations; ceiling is training-regime, not mistranslation.

**Recommended disposition**: all 4 (603 pair, 603a, 603b) + Q-043 companion -> cite the existing 2026-05-29 cluster autopsy, `non_contributory`/`substrate_ceiling` (or `measurement_gap` for the pre-fix same-day pair specifically, per the chain's staged history). `routing: governance-note-only`.

**Re-derive brake**: MECH-313 10 confirmed hits, MECH-260 10 confirmed hits, Q-045 6 confirmed hits -- all far past threshold=2, already fired, already routed (`implement-substrate` on `scaffolded_sd054_onboarding`).

## Sub-group 3 -- MECH-171 vicious-cycle sleep disruption, 5 runs

**Same-day cluster**: all 5 are duplicate/rerun copies of one forbidden same-EXQ silent-rerun batch (V3-EXQ-673 ran repeatedly under one queue entry; 7 total known copies exist). 2 of our 5 covered directly by `failure_autopsy_batch9_2026-06-12`; the other 3 recovered 2026-07-20 from untracked working trees during a git-wedge repair, carrying a PROPAGATED disposition from batch9.

**All 5+ are degenerate**: `ARM_A==ARM_B==ARM_C` on every metric, `late_pred_loss==0.0` throughout -- content-identical arms, zero discriminative signal. Same bug/config produced the same degenerate output every time, not independent replicates.

**Already covered**: `failure_autopsy_batch9_2026-06-12` (original) + `failure_autopsy_batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30` (confirms the pattern end-to-end via a later-recovered 7th copy). Both read `epistemic_category: out_of_domain`, `non_contributory`.

**claims.yaml MECH-171**: `status: candidate`, `claim_type: derived_prediction` (reclassified from `mechanism_hypothesis` 2026-06-14), `epistemic_category: out_of_domain`. User-adjudicated 2026-06-12/13: a multi-year clinical Alzheimer's staged-progression prediction is not faithfully instantiable in a 300-episode grid-world -- the V3 FAILs are non-discriminative by domain, not counter-evidence.

**Concrete staleness finding, flagged for correction (scoring-neutral, confirmed at Step 8 gate).** claims.yaml's `governance_2026_07_20` note for MECH-171 currently asserts the three recovered runs "are NOT arm-degenerate -- their arms genuinely differ -- so degeneracy_reason/non_degenerate are correctly left unset." **This is now factually wrong.** The manifests themselves carry a `2026-07-30` correction: "this note previously asserted [not arm-degenerate]... That assertion was an ERROR... corrected 2026-07-30... scoring-neutral: 'degenerate' and 'non_contributory' are both scoring_excluded buckets... so MECH-171 confidence does not move either way." The manifests were fixed; **claims.yaml's prose was never updated to match** and still states the withdrawn, incorrect claim as current. Net effect on claim confidence is nil, but the note is stale. **Recommend governance correct the claims.yaml note**, citing `failure_autopsy_batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30` as the source of the correction.

**Biological triage**: no dedicated targeted-review exists for "vicious-cycle sleep disruption / Alzheimer's" specifically; claim's own `notes` field cites Lucey et al. 2017 directly. Since the claim is decisively out_of_domain by design, a `/lit-pull` commission is not the live recommendation -- routing is governance-confirm the out_of_domain status (already done twice), not experiment or lit-pull.

**Recommended disposition**: all 5 -> `non_contributory`/`out_of_domain`, propagating the existing batch9 disposition exactly. `routing: governance-note-only` plus the claims.yaml staleness correction above.

**Re-derive brake**: 0 confirmed `substrate_ceiling` hits (correctly -- both confirmed autopsies read `out_of_domain`, a different category; the brake doesn't apply here).

## Cross-sub-group structural read

Explicitly not forced together -- the three sub-groups do NOT share one structural cause in the R1-R3/GOV-CEIL-1 sense (different substrate entries, different remediation paths, different epistemic_category values). A genuine family resemblance worth naming between sub-groups 1 and 2 (not 3): both are instances of "the trained policy's own behavior forecloses the very test conditions the experiment needs to measure" -- sub-group 1's own autopsy cites it as "the same shape as SD-029 monomodal-collapse." Candidate for a named cross-claim pattern, not a merged cluster; remediation substrates differ (env-injection curriculum for MECH-302 vs. goal-pipeline/training-regime enrichment for the 603 lineage). Sub-group 3 (MECH-171) is structurally unrelated to both.

## Learning extracted

1. Recording/consistency debt, not new science -- the substantive diagnostic work for this whole batch is already done and applied; the gap is bookkeeping.
2. Dry-run gate gap: `check_dry_run_citations.py` checks top-level `dry_run` only; `config.dry_run` (nested) slipped past it on 2 sub-group-1 manifests. Caught by manual governance review at the time; the tool itself has a blind spot worth a follow-up (not fixed here, read-only research).
3. Duplicate-manifest-under-one-letter (603b, two timestamps, two autopsy files) is a minor provenance wrinkle worth a disambiguating footnote.
4. Cross-claim pattern candidate: "trained policy forecloses its own test conditions" (MECH-302 env-adequacy + the 603-lineage goal-pipeline seed-fragility) -- naming candidate for governance, not a forced merge.
