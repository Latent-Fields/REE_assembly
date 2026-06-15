# Failure Autopsy -- V3-EXQ-514p (MECH-229 object-bound wanting != liking)

- **Generated (UTC):** 2026-06-15T16:07:08Z
- **Scope:** single target (MECH-229); third autopsy on the 514 lineage (514l, 514m, 514p)
- **Status:** confirmed (user-adjudicated Step-8, 2026-06-15)
- **Run:** `v3_exq_514p_sd049_phase2_mech229_object_bound_wanting_liking_20260615T085728Z_v3`
- **Queue id:** V3-EXQ-514p; predecessor V3-EXQ-514o (confirmatory replication, NOT supersede); machine ree-cloud-4
- **Claims tagged:** MECH-229 ONLY

## Headline

**V3-EXQ-514p is NOT a genuine MECH-229 weakening; it is a non-isolating-criterion
measurement-test-design defect.** The load-bearing criterion `C_WL` (fraction of
consumption steps where the SD-057 most-wanted z_goal pointer != last-consumed type,
threshold 0.6) does not isolate the *drive-coupled incentive-salience* content MECH-229
asserts. The manifest's own within-eval drive-dependence control
(`wl_drive_minus_nodrive`) is near-zero in BOTH the 514o PASS (0.083) and the 514p FAIL
(0.074), and in 514p it is *exactly zero on 2 of 3 seeds*. Decisively, 514o's drive-uniform
negative control (`mean_wl_nodrive = 0.717`) itself clears the 0.6 pass bar -- a criterion
whose negative control passes cannot discriminate the mechanism. The MECH-229 per-claim
`weakens` is reclassified **non_contributory** (`measurement_test_design_defect`); the
pre-registered substrate_conditional off-ramp is NOT fired (its precondition "(c) is a
genuine weakens" is unmet). `pending_retest_after_substrate=[MECH-229]` retained;
`narrow_supports_flag=true` restored.

This run is, however, the FIRST of the three 514 autopsies to clear all readiness gates
(514l = foraging-competence ceiling, non_contributory; 514m = vacuous silent valence
channels, non_contributory). 514p achieves contact (3/3 guard), a populated bank, and a
positive-control instrument separation -- so it is the first run that *could* express
MECH-229, and what it exposes is that the criterion does not isolate the claim's content.

## Facts (manifest + script + 514o predecessor)

| | 514o (PASS, seeds 42/43/44) | 514p (FAIL, seeds 45/46/47) |
|---|---|---|
| `per_seed_guard_pass` | 2/3 (seed44 fails G3) | **3/3** |
| `mean_object_bound_wl_dissoc_fraction` (drive) | 0.80 | **0.5648** (< 0.6) |
| `mean_wl_nodrive_dissoc_fraction` (drive-uniform control) | **0.7167** | 0.4907 |
| `wl_drive_minus_nodrive` | 0.083 | **0.0741** |
| `n_scored_wl_steps_total` | 11 | **27** |
| `pc_separation_frac` / `run_bank_populated_frac` | 1.0 / 1.0 | 1.0 / 1.0 |
| outcome / direction / non_degenerate | PASS / supports / true | FAIL / weakens / true |
| `route_reason` | `c_wl_met_l9_closed` | `c_wl_unmet_genuine_weakens_run_offarm_overshoot` |

514p per-seed (`object_bound_wl_dissoc_fraction` vs `wl_nodrive_dissoc_fraction`):
- seed45: 0.75 vs **0.75** (drive contributes 0)
- seed46: 0.444 vs 0.222 (the only seed with a delta; 4 vs 2 of 9 scored steps)
- seed47: 0.50 vs **0.50** (drive contributes 0)

The entire drive-dependence signal comes from one seed, ~2 scored steps. `n_scored` rose
to 27 (vs 514o's 11), so 514p is the better-powered estimate and it regresses below bar --
but the load-bearing point is criterion isolation, not power.

The 514n -> 514o -> 514p chain confirms the instrumentation chain is sound: 514n FAILed
n_scored=0 (the post-consumption-cleared obs cell read None); the 681-C4 fix sourced the
liking/L2-bind type from `info['sd049_consumed_type_tag_this_tick']`, which 514o/514p both
use (positive-control separation = 1.0, bank populated). The defect is in what `C_WL`
*scores*, not in whether the instrument fires.

## The decisive code/measurement trace

Script `_run_behavioural_eval` (lines 458-470) scores a step when `most_wanted` is defined
and the bank holds >= 2 distinct tokens; it increments `wl_dissoc_steps` when
`most_wanted != consumed_tag` (drive-favored most-wanted) and `wl_nodrive_dissoc_steps`
when `most_wanted(per_axis_drive=None) != consumed_tag`. Scoring (lines 655-677) sets
`c_wl = mean_wl >= 0.6` and `evidence_direction = "supports" if c_wl else "weakens"`,
with `wl_drive_minus_nodrive` reported but NOT a load-bearing gate.

With `n_resource_types = 3`, two categorical labels (most-wanted vs last-consumed) differ
~2/3 of the time by baseline mismatch alone, drive or no drive. The drive-uniform
most-wanted is the within-eval control precisely to subtract this baseline. The manifest's
`drive_dependence_control` block states the intended semantics verbatim: *"a genuine
MECH-229 drive-coupled dissociation has WL_drive >> WL_nodrive."* It does not: the delta is
~0.07-0.08 in both directions, and 514o's no-drive control (0.717) clears the 0.6 bar on
its own. The raw-fraction `C_WL` therefore conflates drive-coupled incentive salience (the
MECH-229 content) with drive-free categorical mismatch.

## The self-route is a hypothesis, not a verdict

`route_reason = c_wl_unmet_genuine_weakens_run_offarm_overshoot` would fire the
pre-registered Woo/Spelke off-ramp (substrate_queue SD-049-PHASE-2 row-6: queue an OFF /
bank-disabled control arm + an n=5 overshoot arm; joint failure routes MECH-229 to
`substrate_conditional` with a V4-1 multi-agent-ecology dependency). That off-ramp's
precondition is "(a)+(b) met but (c) is a *genuine* weakens." (c) is NOT genuine: the
criterion does not isolate the mechanism, and the same criterion's PASS (514o) is equally
uninterpretable. So the off-ramp is NOT fired (canonical incident parallel: V3-EXQ-642,
where a self-routed `substrate_ceiling` rested on an unmet precondition and the correct
route was re-queue, not enrichment).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | the as-scored criterion does not let MECH-229's incentive-salience content express |
| Biological reference | clear | Berridge & Robinson 2003 wanting != liking; incentive salience is drive-state-modulated (specific-PIT). The drive-dependence delta is the biologically load-bearing discriminator -- and it is ~0 |
| Prerequisites / dependency | present | scaffolded_sd054_onboarding (603n) built; contact 3/3; bank populated; channels written (681-C4) |
| Implementation | complete | the instrument fires (PC-sep 1.0); the L2-bind/L4-seed path runs at each consumption event |
| **Measurement** | **misleading (load-bearing)** | raw-fraction `C_WL`; pass bar (0.6) sits below where the drive-uniform negative control lands (514o 0.717); drive-dependence delta ~0 in PASS and FAIL |
| Environment | adequate | SD-049 Phase-2 multi-resource env; per-axis drive present |
| Scale | adequate | n_scored 27 > 514o's 11 |

**Recommended `epistemic_category`:** `measurement_test_design_defect` (same class as
514m -- there the valence channels were never written; here the criterion does not isolate
the mechanism it scores).

## Cluster / granularity-debt recurrence note

This is the third `failure_autopsy_V3-EXQ-514*` doc on MECH-229 (514l 2026-06-03, 514m
2026-06-11, 514p 2026-06-15). The granularity-debt recurrence trigger fired. Reviewed and
NOT routed to `/claim-synthesis`: 514l and 514m were both reclassified **non_contributory**
(substrate ceiling / vacuous channels) -- the claim could not express in either. 514p is
the first run that could express, and it surfaces a criterion-isolation defect, not a third
structurally-distinct refutation. **MECH-229 has never had a mechanism-isolating fair
test.** This is measurement-maturity debt, not claim-granularity debt; the right next step
is one corrected retest (514q), not decomposition. Re-evaluate the /claim-synthesis trigger
if 514q (drive-dependence load-bearing) also fails to discriminate on a fair test.

## Learning extracted

1. **Criterion-isolation rule:** for a categorical dissociation over N labels, a raw
   "labels differ" fraction is confounded by the (N-1)/N baseline mismatch. The PASS bar
   must sit ABOVE where the matched negative control lands, or the within-eval
   control-difference must itself be the load-bearing statistic. 514o passed a bar (0.6)
   its own no-drive control (0.717) cleared.
2. **The within-eval drive-dependence control must be load-bearing for MECH-229**, not
   merely reported. `WL_drive - WL_nodrive` is the statistic that maps to the claim's
   incentive-salience (drive-state-modulated wanting) content.
3. **A PASS on a non-isolating criterion is as untrustworthy as the FAIL.** The 514o
   "supports" entry and the 2026-06-15 promotion reclassification built on it must be
   re-examined, not just the 514p FAIL.

## Routing (user-confirmed 2026-06-15)

- **MECH-229 514p = non_contributory** (`measurement_test_design_defect`), scoring-excluded.
  Retain `pending_retest_after_substrate=[MECH-229]`; restore `narrow_supports_flag=true`.
  Do NOT fire the substrate_conditional off-ramp.
- **Re-examine the 514o-based promotion path (governance).** The 2026-06-15
  evidence_quality_note set `epistemic_category standard` (ceiling lifted),
  `pending_retest_after_substrate=false`, `narrow_supports_flag=false`, and made MECH-229 a
  provisional->stable promote candidate -- all on the 514o PASS, which cleared a criterion
  its own no-drive control (0.717) also clears at n=11/2 seeds. Recommend governance PAUSE
  the promotion, reconsider the ceiling-lifted reclassification, and treat 514o's
  `supports` as resting on a non-isolating criterion (candidate for `evidence_direction:
  superseded`/`non_contributory` pending the corrected retest). This skill does not edit
  claims.yaml; governance applies.
- **Route: `/queue-experiment`** -- a **V3-EXQ-514q** successor (alphabetic; same scientific
  question, corrected criterion) that:
  1. makes `wl_drive_minus_nodrive` (or an equivalent drive-coupled-dissociation statistic)
     the **load-bearing** criterion with an effect-size gate
     `max(k * pstdev(delta), FLOOR)` -- SD-of-delta + an absolute floor, NEVER
     `pstdev(baseline)` (see `feedback_effect_size_pass_gate_margin`); raw `C_WL` becomes a
     non-vacuity check only;
  2. increases seeds/scored-steps for a stable per-seed delta estimate;
  3. retains the 603n contact guard + the same-statistic WL readiness gate.
- **substrate_queue:** `action=none`. This is a test-design defect routed to
  `/queue-experiment`, not a substrate ceiling; the SD-057 object-bound substrate is built
  (2026-06-04) and contact/bank are achieved.
- **No demotion.** MECH-229 stays `provisional` (the mechanism is not refuted; it was not
  tested under a criterion that isolates its content).

## Draft `evidence_quality_note` for governance to write (verbatim)

> 2026-06-15 (failure_autopsy_V3-EXQ-514p): the MECH-229 per-claim `weakens` from V3-EXQ-514p
> is reclassified **non_contributory** (`measurement_test_design_defect`) and scoring-excluded.
> 514p cleared all readiness gates (contact guard 3/3, bank populated, positive-control
> separation 1.0) but the load-bearing criterion `C_WL` (raw fraction most-wanted != last-consumed,
> bar 0.6) does NOT isolate the drive-coupled incentive-salience content MECH-229 asserts: the
> within-eval drive-dependence control `wl_drive_minus_nodrive` is ~0 in BOTH the 514o PASS (0.083)
> and the 514p FAIL (0.074) -- exactly zero on 2 of 3 514p seeds -- and 514o's drive-uniform negative
> control (mean_wl_nodrive 0.717) itself clears the 0.6 bar. With n_resource_types=3 the raw fraction
> is dominated by ~(N-1)/N baseline categorical mismatch, drive or no drive. The self-routed genuine-
> weakens off-ramp (substrate_conditional, V4-1) is therefore NOT fired (unmet precondition;
> cf. V3-EXQ-642). RE-EXAMINE the 2026-06-15 promotion path: the substrate-ceiling-lifted /
> epistemic_category=standard / pending_retest_after_substrate=false / narrow_supports_flag=false
> reclassification all rest on the 514o PASS, which cleared the same non-isolating criterion at
> n=11/2 seeds; pause the provisional->stable promotion and treat 514o's `supports` as resting on a
> non-isolating criterion pending the corrected retest. MECH-229 stays `provisional`,
> `pending_retest_after_substrate=[MECH-229]`, `narrow_supports_flag=true`. Retest = V3-EXQ-514q:
> make the drive-dependence delta the load-bearing criterion with an effect-size gate
> max(k*pstdev(delta), FLOOR), raw C_WL a non-vacuity check only. No demotion; no substrate_queue
> create/amend (test-design defect, SD-057 substrate built 2026-06-04, contact/bank achieved).
