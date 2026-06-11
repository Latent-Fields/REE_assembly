# Failure Autopsy — V3-EXQ-667 (Q-043 exploration-magnitude sweep)

- generated_utc: 2026-06-11T22:55:42Z
- scope: single
- status: confirmed
- run_id: v3_exq_667_q043_exploration_magnitude_sweep_20260611T182534Z_v3
- queue_id: V3-EXQ-667
- machine: ree-cloud-2
- claim_ids: [Q-043]
- experiment_purpose: diagnostic
- manifest outcome: FAIL / evidence_direction non_contributory
- manifest self-route: interpretation.label = `substrate_not_ready_requeue`
- adjudication flag: `precondition_unmet` (preconditions[0].met = false)

## 1. Scope

V3-EXQ-667 is the PRIMARY routing output of `failure_autopsy_V3-EXQ-591c_2026-06-11`.
591c FAILed because arming the ARC-065 exploration-diversity stack (MECH-313 noise
floor `noise_floor_alpha=0.1` + MECH-314 structured curiosity `curiosity_weight=0.05`)
at its **landed-default** magnitudes did not rescue the worst-case Phase-0 collapse
seed (seed 46, `h_pos_mean=0.0375`, identical to 591b with the stack OFF). 667 runs
the focused 1-D form of the Q-043 weight sweep: scale **both** knobs jointly to
1x/2x/4x/8x and ask the autopsy's fork —

- (a) collapse seed escapes Phase 0 at some magnitude above default → config-only fix
  (raise the ARC-065 default magnitudes);
- (b) collapse persists at every magnitude including 8x → passive noise+curiosity is an
  insufficient translation; an **active** Phase-0 exploration-shaping substrate is required.

The script also carries a same-statistic **non-vacuity gate** (the V3-EXQ-643 lesson):
the swept knobs must actually move exploration on the healthy-seed positive control before
the rescue fork is adjudicable.

This is a flagged diagnostic that **ran to completion** — the correct skill (`/failure-autopsy`),
not `/diagnose-errors`.

## 2. Reconstruction — facts only

5 seeds {42,43,44,45,46} × 4 magnitude scales {1,2,4,8}; per cell `alpha = 0.1*scale`,
`cw = 0.05*scale`; 160 ep × 200 steps; InfantCurriculumScheduler Phase 0→1 gate UNCHANGED
(`H_POS_FRAC_OF_MAX=0.20`, threshold ≈ 0.994).

Self-route inputs:
- healthy_seeds (genuine at 1x default) = [42, 43, 44]
- collapse_seeds_default (NOT genuine at 1x) = [45, 46]
- rescue_scale_by_seed = {45: null, 46: null} → all_collapse_rescued = **false**
- readiness_range (range across magnitude arms of the healthy-seed-averaged h_pos_mean) =
  **0.0172**, threshold 0.05 → readiness_ok = **false**
- per_arm_healthy_mean: 1x 0.5757, 2x 0.5795, 4x 0.5795, 8x 0.5929
- criteria_non_degenerate.C_collapse_seed_rescued = **false**

Routing logic: `not readiness_ok` → FAIL / `substrate_not_ready_requeue` / non_contributory.

### The load-bearing diagnostic signal (the smoking gun)

Per-seed `h_pos_mean` across the four magnitude arms (1x / 2x / 4x / 8x):

| seed | 1x | 2x | 4x | 8x | reached_phase1 | genuine | phase_0to1 ep |
|---|---|---|---|---|---|---|---|
| 42 | 0.5621 | 0.5735 | 0.5735 | 0.6136 | yes | yes | 104/113/113/111 |
| 43 | 0.3226 | 0.3226 | 0.3226 | 0.3226 | yes | yes | 114 (all) |
| 44 | 0.8424 | 0.8424 | 0.8424 | 0.8424 | yes | yes | 100 (all) |
| 45 | 0.1404 | 0.1404 | 0.1404 | 0.1404 | yes | no | 142 (all) |
| 46 | 0.0375 | 0.0375 | 0.0375 | 0.0375 | no | no | null (all) |

For **4 of 5 seeds (43, 44, 45, 46)** every per-cell statistic — `h_pos_mean`, `h_pos_min`,
`h_pos_max`, `h_pos_std`, `n_eligible_ge_threshold`, and the phase-advance episode — is
**byte-identical across an 8× joint scaling of both knobs**. Only seed 42 moves, and only
marginally (range 0.0515 over its four arms; +9% at 8x). The 0.0172 healthy-seed readiness
range is therefore driven **entirely by seed 42's wobble**; seeds 43 and 44 contribute
exactly zero variance.

Which criterion failed: the **non-vacuity precondition** (a readiness gate), not the
discrimination criterion. The rescue criterion never got to adjudicate.

## 3. Claim-layer mapping

Q-043 is an `open_question` (epistemic_category `answer_state`), claim_level mechanistic,
`implementation_phase: v3`, `depends_on: [ARC-065, MECH-313, MECH-314]`. It asks how to
**calibrate the relative weights** of MECH-313 and MECH-314 — a parametric-sweep question,
not a falsifiable mechanism claim.

Q-043 **already carries** `pending_retest_after_substrate: true` and an evidence_quality_note
recording the identical condition from the V3-EXQ-605 cluster autopsy (2026-05-29):
"calibration grid untestable on V3 default substrate — curiosity dimension fully degenerate
(curiosity_scale {1x,5x,10x} produces identical per-cell entropy + reef_fraction); noise
dimension delivers sub-threshold signal." V3-EXQ-667 reproduces that exact finding on the
591c-lineage probe. Did the experiment let the claim express itself? **No** — the question
cannot be asked while the swept knobs are inert on the positive control.

`claim_ids` accuracy: correct. The run is single-tagged `[Q-043]`, the calibration question
it actually probes; it does not over-tag MECH-313/MECH-314/ARC-065 (which would corrupt
those records with a non-contributory entry).

## 4. Biological-reference triage

Closest reference mechanisms: LC-NE **tonic** adaptive gain (Aston-Jones & Cohen 2005) for
MECH-313, and frontopolar/striatal **curiosity / novelty** drive (Wittmann 2008; Daw 2006;
Schmidhuber 1991) for MECH-314. The biological existence proof — exploration shaping works
in brains — is solid; this is a translation question, not a falsification.

These are **not** formal-definition imports in the SD-003 sense; they are biologically
grounded regulators with passing substrate contracts. The FAIL signature — an 8× knob
scaling producing exactly zero behavioural change for 4/5 seeds — matches "a known
**dependency** of the reference mechanism is absent." In brains, tonic-NE / curiosity
signals reach action selection through a **gain pathway that can actually re-weight competing
options**. In REE-v3 that pathway is currently **inert**: MECH-313 lifts the E3 softmax
temperature and MECH-314 adds a small score-bias, but both are composed at a layer where a
collapsed candidate pool + a primary-score gap that dwarfs the bias means the argmin/committed
trajectory does not move. This is exactly the **modulatory-bias-selection-authority** gap,
already diagnosed and substrate-queued.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (not testable) | Q-043 is an open calibration question; the run could not let it express itself. Not weakened. |
| Biological reference | clear | LC-NE tonic + curiosity/novelty; the inertness matches a missing dependency (the selection-authority gain pathway), not a wrong mechanism. |
| Prerequisites | **missing / immature** | The swept knobs reach E3 only through the modulatory-bias channel, which has zero authority over the committed argmin (`modulatory-bias-selection-authority`, in validation V3-EXQ-663/643a) and reads a collapsed candidate pool (ARC-065 GAP-A, V3-EXQ-649; SD-056). |
| Implementation | partial | MECH-313 NoiseFloor (temperature) + MECH-314 StructuredCuriosity (score-bias) are wired and pass contracts, but composed at the drowned/inert seam. |
| Environment | adequate | InfantCurriculumScheduler Phase-0 probe is the right bed; 591c reproduced as the 1x anchor. |
| Measurement | adequate (working as designed) | The same-statistic readiness gate correctly caught the vacuity (`readiness_range 0.0172 < 0.05`) and self-routed `substrate_not_ready_requeue` rather than emitting a false substrate verdict. |
| Integration | **isolated** | The substrate is the failure site: knobs work in isolation (unit contracts) but do not reach behaviour in the full E3 selection loop. The 4/5-byte-identical-across-8x pattern is the direct readout. |
| Scale / capacity | n/a | Magnitude is not the limiting axis — the knobs are disconnected from behaviour, not too weak. |

**Recommended epistemic_category:** `substrate_conditional` (the question depends on
upstream substrate that is planned and in validation but not yet landed). The manifest's
`non_contributory` evidence_direction is correct and should stand.

## 6. Self-route adjudication

Per the "self-route is a hypothesis, not a verdict" rule: the manifest claims
`substrate_not_ready_requeue` because the healthy-seed h_pos range fell below the floor.

- Was the branch's assumption (knobs inert on the positive control) actually met? **Yes —
  confirmed.** 4/5 seeds are byte-identical across an 8× scaling; the only movement is seed
  42's +9%. The knobs demonstrably do not modulate exploration on the positive control.
- Is the precondition test itself wrong? **No.** It measures the same per-episode `pos_entropy`
  range the rescue criterion routes on (same-statistic discipline), not a norm/mean-abs proxy.
  This is the gate working as designed.

The self-route is **correct**. This run is genuinely `non_contributory`: it cannot adjudicate
the 591c fork (a) vs (b). In particular it is **NOT** evidence for option (b)
("magnitude insufficient → active Phase-0 shaping required") — that reading is unavailable
because the knobs never moved the positive control.

## 7. Learning extracted

1. **One more confirmation of a known structural property**, not a new bug: the swept
   ARC-065 modulatory knobs (MECH-313 temperature + MECH-314 score-bias) have **zero
   authority over the committed E3 argmin** on the InfantCurriculumScheduler Phase-0 probe.
   Convergent with the documented cluster: 604a (MECH-314 `curiosity_bias_abs_mean=0.0`),
   624a (MECH-320), 614d/660b (MECH-341), 569f/661/654a, and the V3-EXQ-605 Q-043 cluster
   note already in claims.yaml.
2. The **4/5-seed byte-identical-across-8x** result is the cleanest single readout of the
   bottleneck to date: not measurement noise, but complete behavioural invariance to an 8×
   joint scaling — the knobs are disconnected at the selection layer.
3. The same-statistic readiness gate **did its job**: it converted what could have been a
   false option-(b) substrate verdict into a correctly-routed `substrate_not_ready_requeue`.
4. **Not granularity debt → NO `/claim-synthesis`.** Q-043 is a clean calibration question
   with a single, well-understood blocker, not a coarse claim fracturing into finer ones.
   The lineage (591/591b/591c → 667) is convergent iterative substrate engineering on one
   known selection-authority bottleneck, exactly as the sibling 666a autopsy concluded for
   ARC-063 CRF readiness. The recurrence belongs to the substrate stream, not to Q-043.

## 8. Routing

| Aspect | Recommendation |
|---|---|
| Manifest reclassify | None — `non_contributory` / `substrate_not_ready_requeue` stands; the run is correctly self-routed. |
| Q-043 claim | Leave `pending_retest_after_substrate: true` (already set). Append a one-line evidence_quality_note: 667 reproduces the V3-EXQ-605 inert-knobs finding on the 591c lineage; blocked on `modulatory-bias-selection-authority`. NO demotion, NO confidence change (open_question / answer_state — exempt). |
| Substrate | `implement-substrate` action = **amend**: append V3-EXQ-667 as a blocked-retest failure record to the EXISTING `modulatory-bias-selection-authority` substrate_queue entry (alongside 604a/624a/614d/569f/661/654a). Do NOT create a new entry. `ready` stays false. |
| Re-queue | `/queue-experiment` re-issue **V3-EXQ-667a** (new letter), GATED on `modulatory-bias-selection-authority` validation (V3-EXQ-663 route-range / 643a) AND ARC-065 GAP-A (V3-EXQ-649) clearing — i.e. only after the swept knobs are shown to move exploration on the healthy-seed positive control (`readiness_range >= 0.05`). Keep the 591c-faithful design + the same-statistic non-vacuity gate. Do NOT re-run under the same ID. |
| `/claim-synthesis` | **No** (see §7.4). |
| `/diagnose-errors` | No (ran to completion). |

### Draft evidence_quality_note for governance to write on Q-043

> [2026-06-11 autopsy V3-EXQ-667] Magnitude-scale sweep (MECH-313 noise_floor_alpha +
> MECH-314 curiosity_weight jointly 1x/2x/4x/8x) on the 591c InfantCurriculumScheduler
> Phase-0 probe self-routed substrate_not_ready_requeue: healthy-seed h_pos range across
> arms 0.0172 < 0.05 floor; 4/5 seeds (43/44/45/46) byte-identical across the full 8x
> scaling — the swept knobs have zero authority over E3 selection. Reproduces the
> V3-EXQ-605 inert-knobs finding on the 591c lineage. NOT evidence for "magnitude
> insufficient → active Phase-0 shaping required" (the rescue fork was unadjudicable).
> Blocked on modulatory-bias-selection-authority (V3-EXQ-663/643a) + ARC-065 GAP-A
> (V3-EXQ-649). Retest V3-EXQ-667a after those clear. pending_retest_after_substrate stays.

## 9. Cross-references

591/591b/591c lineage; modulatory-bias-selection-authority (substrate_queue, in validation
V3-EXQ-663/643a); ARC-065 GAP-A (V3-EXQ-649); SD-056 (e2 action-conditional divergence);
MECH-313 / MECH-314 / ARC-065; Q-044 (sibling sub-flavour-independence question, same
two-substrate-prereq stack); V3-EXQ-605 cluster autopsy (the prior Q-043 inert-knobs
finding); 604a/624a/614d/660b/569f/661/654a (the convergent selection-authority cluster);
failure_autopsy_V3-EXQ-591c_2026-06-11 (the routing parent).
