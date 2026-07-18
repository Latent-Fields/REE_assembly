# Failure autopsy -- V3-EXQ-783 (z_world granularity x training crossing)

- **Generated:** 2026-07-18T18:06:59Z
- **Session:** mech-063-experiment-2ffd19 (`autopsy 783 + 778g diagnostic adjudication`)
- **Target:** `v3_exq_783_zworld_granularity_training_crossing_20260718T112340Z_v3`
- **Queue id:** V3-EXQ-783 | **Outcome:** PASS | **Purpose:** DIAGNOSTIC
- **Claims tagged:** Q-002, SD-031
- **Self-route (hypothesis):** `mixed_partial_separation`
- **Indexer adjudication:** `vacuous_pass` (BLOCKING)
- **Status:** confirmed (user-adjudicated at the Step 8 gate, 2026-07-18)

## 0. Why this run was adjudicated

A diagnostic PASS carrying a BLOCKING `vacuous_pass` flag. Per the diagnostic adjudication
gate, the label must not clear a v3_pending gate, mint or amend a substrate_queue entry, or
route a thought-intake until adjudicated. Two questions were owed: WHICH criterion is
degenerate, and whether the `mixed_partial_separation` reading survives.

Both are answered below. The short form: **the flag is a false positive produced by an
indexer asymmetry, and the label is a bright-line threshold artifact that does not survive
a noise-aware read of its own per-seed data.**

## 1. Facts reconstruction

Recording provenance is COMPLETE -- `validate_recording.py` reports OK with no always-core
gaps (`recording_schema` rec/v1, `substrate_hash`
7f856703fd038d9ea20b8435b1433f566c8afc0d9135515cc40a064d75abea9d, `machine` ree-worker-1,
`machine_class` linux-x86_64-py3.10, `elapsed_seconds` 194.9, full `config`, `seeds`
[42..49]). No recording gap; nothing here is blocked on an unrecorded readout.

Substrate provenance checks out: SD-070 landed `ree-v3` main f418400 at 2026-07-18T10:46:06Z
and the run executed at 2026-07-18T11:23:40Z, so the TRAINED arms did run the SD-070
anti-collapse recipe as designed.

### 1a. All four preconditions MET

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `raw_channel_contrast_ratio_non_degenerate` | 0.8138 | >= 0.2 | yes |
| `trained_arm_encoder_weights_actually_moved` | 7 | >= 1 | yes |
| `p1_encoder_frozen` | 0 | <= 0 (upper) | yes |
| `trained_arm_representation_not_collapsed` | 0.5768 | >= 0.5 | yes |

The second is the exact check that produced "world-path CHANGED: NONE" (0/61) on the earlier
x734 configuration. It now reads 7. The fourth is the anti-collapse guard: D32_TRAINED
retains PR 4.474 against its dim-matched untrained 6.803 (fraction 0.658), well clear of both
the 0.5 relative floor and the 2.0 absolute floor. The prescribed pre-SD-070 P0 collapsed
z_world to PR ~1.06. **The SD-070 recipe demonstrably works** -- that is the first
load-bearing finding of this run, and it is what licenses any (a1)/(a2) conclusion at all.

### 1b. Criteria

```
criteria_non_degenerate: C1 true | C2 FALSE | C3 true | C4 true
criteria:  C1_cr_crossing            load_bearing TRUE   passed TRUE
           C2_event_selectivity      load_bearing FALSE  passed TRUE
           C3_residue_fine_coarse    load_bearing FALSE  passed TRUE
           C4_attribution_dim128_only load_bearing FALSE passed TRUE
```

**The degenerate criterion is C2_event_selectivity, and it is the ONLY one.** It is degenerate
for exactly one reason: `sd009_ce_label_balance_train.saturated == True` (class-0 = 95.19%,
class-1 = 4.61%, class-2 = 0.198%). It is NOT degenerate for want of data (`len(sel_vals) >= 2`
holds, which is why C2's own `passed` is True) nor for a flat spread.

## 2. The `vacuous_pass` flag is a FALSE POSITIVE -- indexer asymmetry

The flag did not fire on the modern check. In
`evidence/experiments/scripts/build_experiment_indexes.py`:

- **(3b), line ~300** -- the aggregation-vacuity check -- looks for a criterion tagged
  `load_bearing: true` with `passed: false`. 783 has no such criterion. It did NOT fire.
- **legacy fallback, line ~329** -- fires on ANY `False` value in `criteria_non_degenerate`,
  excluding only keys whose name ends in `_branch`. **It is `load_bearing`-blind.** C2 is a
  non-load-bearing criterion, so this path fired on a caveat the author deliberately recorded.

A manifest that supplies BOTH blocks -- as 783 correctly does -- is therefore adjudicated by
the blind legacy path even though the load_bearing-aware path passed it. This is the same
class of directionality/attribution false-flag as V3-EXQ-648a/649 (branch-selector `False`
misread as degeneracy), one level up: there the fix was a name-suffix exclusion, here the
needed exclusion is the explicit `load_bearing: false` tag.

The script author anticipated this exact case verbatim
(`v3_exq_783_zworld_granularity_training_crossing.py:1177-1180`):

> "C2 is degenerate when the SD-009 CE label is saturated: with class-0 dominating, the
> event-contrastive head has almost no signal to shape z_world with, so a near-zero
> selectivity margin says 'the label was starved', NOT 'selectivity is absent'. C2 is
> NOT load-bearing, so this is a recorded caveat rather than a blocker on the run."

Moreover the degeneracy is **designed-in and out of scope**. C2's saturation IS the SD-009
`transition_type` channel-mismatch fault that this experiment explicitly ROUTES AROUND via
SD-070 and explicitly does not adjudicate (the script tags neither SD-009 nor MECH-100, and
records the open question at
`evidence/planning/sd009_event_contrastive_channel_mismatch_2026-07-18.md`). The load-bearing
DV is the contrast ratio, not event selectivity.

**Adjudication: the gate is NOT cleared on a degenerate criterion. The PASS rests on
C1_cr_crossing, which is load-bearing, non-degenerate, and passed, under four met
preconditions. The `vacuous_pass` flag should be cleared for this run.**

## 3. The `mixed_partial_separation` label does NOT survive

The label is assigned by a bright-line comparison of axis-delta point estimates against
`CR_MINOR_AXIS_CEILING = 0.02` and `cr_lift_floor = 0.05`. Recomputing the paired per-seed
deltas the manifest already records (n = 8, paired by seed, t_crit(7) = 2.365):

| Axis | mean delta | sd | sem | t | CI95 | `clears` | zero in CI |
|---|---|---|---|---|---|---|---|
| training @ dim32 | +0.0814 | 0.0317 | 0.0112 | **+7.26** | [+0.0549, +0.1079] | true | no |
| training @ dim128 | +0.1074 | 0.0232 | 0.0082 | **+13.11** | [+0.0880, +0.1268] | true | no |
| dim @ untrained | -0.0032 | 0.0124 | 0.0044 | -0.73 | [-0.0135, +0.0071] | false | **yes** |
| dim @ trained | +0.0228 | 0.0404 | 0.0143 | +1.60 | [-0.0110, +0.0566] | false | **yes** |
| conjunctive D128T vs D32U | +0.1042 | 0.0319 | 0.0113 | +9.23 | [+0.0775, +0.1309] | true | no |

Tracing the label logic (`:1147-1158`): `training_lifts_both` is True; `dim_lifts_both` is
False; `dim_minor` requires `abs(mean) < 0.02` at BOTH dim contrasts -- it holds at untrained
(0.0032) and **fails at trained by 0.0028** (0.0228 vs 0.02). That single 0.0028 margin is
the entire reason the run did not route `a1_untrained_encoder_dominates`; with `dim_minor`
False, every named branch falls through to the `else`.

That margin is not a signal. `dim_at_trained`'s own SEM is 0.0143 -- **five times the margin
by which it missed** -- its CI95 straddles zero, and its per-seed deltas include -0.0376 and
-0.0105. It is statistically indistinguishable from the dim@untrained contrast, which the
same logic scored as minor.

The label logic also carries a structural gap worth naming: `clears` requires
`mean >= 0.05`, `minor` requires `abs(mean) < 0.02`, so **0.02-0.05 is a dead-band in which an
axis is neither "lifting" nor "minor"** -- with no noise allowance anywhere. `dim_at_trained`
landed in that dead-band. A noise-aware form of the same test (is the delta distinguishable
from zero?) puts it unambiguously on the "minor" side.

**Adjudicated reading (user-confirmed at the Step 8 gate): `a1_untrained_encoder_dominates`.**
Training lifts the z_world contrast ratio strongly and reproducibly at BOTH dimensionalities
(t = +7.3 and +13.1). Dimensionality lifts nothing at EITHER training state (both CI95 straddle
zero). The apparent conjunctive lift (+0.1042) is the training effect carried through, not a
dim contribution -- it is within noise of the training-at-dim128 effect alone (+0.1074).

## 4. What this discharges -- the (a2) ceiling is REFUTED

`failure_autopsy_zworld-integration-cluster_2026-06-06` adjudicated the (a2) world_dim=32
discriminative-granularity ceiling as `substrate_ceiling` / `pending_retest_after_substrate`,
and 783 IS that autopsy's user-confirmed retest spec (its section 7), run for the first time
with the encoder actually trained. Every cell measured on 2026-07-18 prior to this run was
dim=32 AND untrained, perfectly confounding (a1) with (a2).

Crossed, they separate cleanly, and **the ceiling is refuted**: raising world_dim from 32 to
128 does not improve z_world contrast at either training state. The cause of z_world
under-differentiation was (a1) -- the encoder never received gradient -- and SD-070 fixes it.

This bears directly on **Q-002's HARD PRECONDITION**, which currently reads:

> "z_world must carry enough spatial structure for fine-grained RBF accumulation; at V3 scale
> it does not, so a fine-resolution FAIL reflects the substrate ceiling (resolve via SD-005 /
> higher-dim z_world), not a settled answer."

The prescribed remedy **"higher-dim z_world" is now refuted as a route** -- dim 128 buys
nothing. The correct route is a TRAINED encoder (SD-070). Q-002's precondition text should be
updated accordingly by governance; the precondition itself is not lifted (no run has yet swept
RBF resolution on an SD-070-trained encoder), but the way to lift it has changed.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (Q-002 route corrected; SD-031 untouched) | Diagnostic; separates causes, falsifies neither claim. Q-002's remedy clause is corrected, not its question. |
| Biological reference | clear | An untrained sensory encoder carries no differentiated manifold regardless of its unit count; cortical representational differentiation is experience-driven, not dimension-driven. The 2026-06-06 dim-ceiling reading was the formal-capacity intuition (more units = more discriminability) rather than the biological one (differentiation is trained). The result matches the biology. |
| Developmental / dependency prerequisites | present | SD-070 landed and demonstrably trains the world path (weight-delta 7, PR retention 0.658). |
| Implementation completeness | complete for the tested path | P0/P1 phase separation held exactly (`p1_encoder_frozen` = 0). |
| Environment adequacy | adequate | Raw world_state contrast 0.8138 vs a 0.2 floor -- ample upstream variation to encode. |
| Measurement adequacy | adequate on the load-bearing DV; degraded on C2 | CR is offset-invariant and non-degenerate. C2 is starved by the SD-009 label saturation -- a known, out-of-scope, non-load-bearing caveat. |
| Integration adequacy | coupled and stable | Env exposure held identical across arms; arms differ in weight updates only. |
| Scale / capacity | **adequate -- and this is the finding** | dim 32 is NOT the binding constraint. 4x-ing it changes nothing. |

**Recommended `epistemic_category`: `instrument_validated_cause_discriminated`** -- the run
did what a diagnostic should: it separated two confounded causes, confirmed one, and refuted
the other, on a substrate whose readiness it independently established. It is emphatically
NOT `substrate_ceiling` (it refutes one), which is why the re-derive brake does not fire.

## 6. Re-derive brake and recurrence checks

- **Re-derive brake: does NOT fire.** Q-002 carries exactly one prior
  `substrate_ceiling`/`non_contributory` autopsy (`failure_autopsy_zworld-integration-cluster_2026-06-06`).
  This autopsy would have been N=2 had it concluded `substrate_ceiling` -- it concludes the
  opposite and DISCHARGES the prior verdict. SD-031 has no prior autopsy. No re-queue is refused.
- **Granularity-debt recurrence trigger: checked, does NOT fire.** Q-002 has a prior autopsy,
  so the count condition is met, but the substance is not: this autopsy RESOLVES the prior
  one's open (a1)/(a2) confound rather than circling the claim with a new failure signature.
  That is convergence, not granularity debt. No `/claim-synthesis` handoff.

## 7. Learning extracted

1. **z_world under-differentiation is a TRAINING fault, not a DIMENSIONALITY fault.** Crossed
   2x2, training lifts CR at both dims (t = +7.3, +13.1); dim lifts nothing at either training
   state (both CI95 straddle zero). The 2026-06-06 (a2) dim32 `substrate_ceiling` verdict is
   refuted by its own prescribed retest.
2. **SD-070 works.** It moves the world path (7 tensors vs the x734 configuration's 0/61) and
   avoids the collapse the prescribed SD-009+SD-018 P0 produced (PR retained 0.658 vs the
   pre-SD-070 collapse to PR ~1.06), while preserving P0/P1 phase separation exactly.
3. **Q-002's prescribed remedy is wrong and should be corrected.** "Resolve via SD-005 /
   higher-dim z_world" is refuted as a route; the route is a trained encoder.
4. **The indexer's legacy vacuity check is `load_bearing`-blind, while its modern (3b) check
   is not.** Any manifest supplying both `criteria[]` (with `load_bearing` tags) and
   `criteria_non_degenerate{}` can be BLOCKING-flagged on a criterion its own author correctly
   tagged non-load-bearing. This is a governance-tooling defect with corpus-wide reach, not a
   property of this run.
5. **Bright-line label thresholds with no noise allowance manufacture spurious labels.** A
   0.0028 excursion past a 0.02 ceiling, against a 0.0143 SEM, changed the routed label. The
   0.02-0.05 dead-band between `minor` and `clears` has no noise-aware form at all. Future
   crossing designs should route on a distinguishable-from-zero test, not a point estimate.

## 8. Routing (user-confirmed)

**Primary: governance adjudication (no demotion, no substrate entry).** Diagnostic evidence
does not weight governance confidence; nothing here changes a status or confidence.

1. **Clear the `vacuous_pass` flag on this run** as a false positive, per section 2.
2. **Record the adjudicated self-route as `a1_untrained_encoder_dominates`** (superseding the
   emitted `mixed_partial_separation`), per section 3.
3. **Correct Q-002's `what_would_answer` HARD PRECONDITION** to route the remedy to a trained
   encoder (SD-070) rather than higher-dim z_world, per section 4. The precondition is NOT
   lifted -- no RBF-resolution sweep has yet run on an SD-070-trained encoder.
4. **Record on the 2026-06-06 cluster autopsy's (a2) leg that its `substrate_ceiling` /
   `pending_retest_after_substrate` verdict is DISCHARGED and REFUTED** by its own retest spec.

**Secondary: governance-tooling fix (routed, not performed here).** Amend the legacy
`criteria_non_degenerate` vacuity check in `build_experiment_indexes.py` to skip any key whose
matching entry in `criteria[]` is tagged `load_bearing: false`, mirroring the `_branch`
exclusion already present and the `load_bearing` gating the (3b) path already applies. This is
REE_assembly governance tooling, not a ree-v3 substrate gap, so it takes NO
`substrate_queue.json` entry (`action: none`); it is spawned as a follow-on chip.

**No `/queue-experiment` is recommended.** The (a1)/(a2) discrimination is settled; a further
letter would circle a resolved question. A future RBF-resolution sweep on an SD-070-trained
encoder is Q-002's own `what_would_answer` and is a NEW question, not a re-test of this one.

### Draft `evidence_quality_note` for governance (Q-002)

```
[ADJUDICATED 2026-07-18 -- V3-EXQ-783 z_world granularity x training crossing, PASS,
DIAGNOSTIC so no status or confidence change. Autopsy:
evidence/planning/failure_autopsy_V3-EXQ-783_2026-07-18.]
The indexer flagged this run vacuous_pass. ADJUDICATED A FALSE POSITIVE: the sole
degenerate criterion is C2_event_selectivity, which the manifest explicitly tags
load_bearing:false and which is degenerate only because the SD-009 CE label is saturated
(class-0 95.19%) -- the very channel mismatch this experiment routes around via SD-070 and
does not adjudicate. The load-bearing C1_cr_crossing is non-degenerate and passed under four
MET preconditions (raw channel CR 0.8138 vs 0.2 floor; trained-arm world-path tensors moved
7 vs the x734 configuration's 0/61; P1 encoder frozen at 0; trained-arm PR retention 0.658
vs a 0.5 floor). The flag fired through the indexer's LEGACY criteria_non_degenerate check,
which -- unlike its modern (3b) aggregation-vacuity check -- is load_bearing-blind; a
tooling fix is routed separately.
SELF-ROUTE RE-READ. The emitted label mixed_partial_separation does NOT survive and is
superseded by a1_untrained_encoder_dominates. The emitted label turned on dim_at_trained's
point estimate (+0.0228) exceeding the CR_MINOR_AXIS_CEILING of 0.02 by 0.0028, against its
own SEM of 0.0143, with a CI95 of [-0.0110, +0.0566] straddling zero and per-seed deltas as
low as -0.0376. Paired per-seed, n=8: training lifts CR at BOTH dims (dim32 +0.0814,
t=+7.26; dim128 +0.1074, t=+13.11) while dim lifts nothing at EITHER training state
(untrained -0.0032, t=-0.73; trained +0.0228, t=+1.60 -- both CI95 straddle zero).
CONSEQUENCE FOR THIS QUESTION. The (a2) world_dim=32 discriminative-granularity ceiling --
adjudicated substrate_ceiling / pending_retest_after_substrate by
failure_autopsy_zworld-integration-cluster_2026-06-06 -- is REFUTED by that autopsy's own
user-confirmed retest spec: 4x-ing world_dim buys no contrast at either training state. The
cause was (a1), an encoder that never received gradient, and SD-070 (ree-v3 main f418400)
fixes it -- weight-delta 7, PR retention 0.658 against the pre-SD-070 P0's collapse to
PR ~1.06.
The HARD PRECONDITION in what_would_answer is CORRECTED, not lifted. Its remedy clause
"resolve via SD-005 / higher-dim z_world" is refuted as a route; the route is a TRAINED
encoder (SD-070). The precondition still stands: no run has yet swept RBF resolution on an
SD-070-trained encoder, so no fine-vs-coarse resolution answer is settled.
```

### Draft `evidence_quality_note` for governance (SD-031)

```
[NOTED 2026-07-18 -- V3-EXQ-783, PASS, DIAGNOSTIC, no status or confidence change and the
v3_pending gate is NOT cleared (a flagged-then-cleared diagnostic may not clear a
v3_pending gate).] The run exercised SD-031's phased P0/P1 protocol and confirms the phase
separation holds exactly: P1 trains E2WorldForward on stop-gradient z_world targets with
p1_encoder_frozen measured at 0 world-path tensors moved. This is plumbing-fidelity
evidence for the design's phasing only; the comparator residual itself is untested here.
The attribution leg is dim-gated by MIN_DISCRIMINATIVE_WORLD_DIM and yields a contrast at
dim=128 only, recorded as None (never 0.0) at dim=32.
```
