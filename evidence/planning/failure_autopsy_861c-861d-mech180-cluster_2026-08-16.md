# Failure autopsy -- V3-EXQ-861c + V3-EXQ-861d (MECH-180 / MECH-122 / INV-050 cluster)

Generated: `2026-08-16T17:10:38Z`
Scope: **cluster** (2 targets)
Status: **confirmed** (interactive gate, 2026-08-16)
Session: `cranky-driscoll-126a36`

---

## 0. Dry-run gate (Step 2a)

`scripts/check_dry_run_citations.py` over every run_id cited here: **0 dry cited, 0 dry in named
families, 0 ambiguous, 4 clean, 0 unknown.** Runs checked: 861c, 861d, 861b, 861 (plus queue ids
861a / 845 / 798a). `dry_run_unreachable_criterion` lint: 11 warnings corpus-wide, **all in the
`v3_exq_543` lineage, none on any 861-family driver**.

Recording provenance (`ree-v3/validate_recording.py`): **2 complete, 0 always-core gaps.** No
recording-debt route applies. (861d carries `enabled_default_off_flags: null` where 861c carries a
populated map; this is not an always-core field and the MECH-122 flags are present in `config`, so
it is noted, not a finding.)

---

## 1. Facts

Both runs are `experiment_purpose: "evidence"`, `outcome: FAIL`, ran to completion on cloud workers,
`substrate_stable_across_run: true`, and both passed **both** readiness gates (R1 world-forward
convergence, R2 ecological MEL gradient) at `1.0`.

| | **861c** | **861d** |
|---|---|---|
| run_id | `v3_exq_861c_inv050_mech180_calibration_fixed_replication_20260814T231404Z_v3` | `v3_exq_861d_mech180_mech122_spindle_content_selection_dv3_revalidation_20260815T005853Z_v3` |
| claims | INV-050, MECH-180 | MECH-180, MECH-122 |
| supersedes | V3-EXQ-861b | V3-EXQ-861a |
| seeds | 7, 271, 883 | 42, 123, 456 |
| machine | ree-cloud-4 | ree-cloud-2 |
| MECH-122 selection | `use_mech122_spindle_content_selection: **false**` | `**true**`, `mech122_novelty_reference_mode: "mel_pe"` |
| substrate_commit | `f810969` (contains the fix) | `8a68845` (contains the fix) |
| self-route label | `mel_coupling_below_calibration_noise_floor` | `mel_control_degenerate` |
| DV1 sws_power | PASS 3/3 | PASS (per-seed 2/3) |
| DV2 replay_rate | PASS 3/3 | PASS 3/3 |
| DV3 spindle_density | **scoring_excluded** (flag off) | **load-bearing, 0/3** |
| **failed criterion** | **C2** `on_factor_clears_calibration_noise_floor` (1/3 seeds) | **C1b** `spindle_density_decoupled_monotone_in_measured_mel` (0/3) |
| manifest direction | non_contributory / non_contributory | MECH-180 non_contributory; **MECH-122 `weakens`** |

### 1a. The two runs are not redundant -- they are differently configured on purpose

861c ran the MECH-122 mechanism **OFF** and correctly scoring-excluded DV3. Its exclusion text quotes
the substrate status as `implemented_validation_failed_needs_followup_fix`; that string was accurate
when the driver was written and **changed to `implemented_pending_validation` at 2026-08-14 20:31**
(`REE_assembly` `3b1c8b4593`), i.e. between the two runs. The exclusion is therefore correct for
861c's own config and is *not* an error.

861d is the **sanctioned revalidation** of the follow-up fix that landed the same day
(`ree-v3` `6aa97ca`, 2026-08-14 20:28, `chip-20260813-mech122-consolidation-ref-resource`). That
substrate note explicitly ordered: "re-run the 861-family driver (new letter) with
`use_mech122_spindle_content_selection=True` and DV3 re-enabled". 861d did exactly that. Scoring DV3
load-bearing was correct, not a mis-scoping.

### 1b. Lineage-wide z_goal writer defect -- a constant, not the discriminator

All five 861-family runs report `z_goal_stream.writer_defect: true` with `writer_calls: 0`:

| run | ticks | writer_calls |
|---|---|---|
| 861 | 38959 | 0 |
| 861a | 38959 | 0 |
| 861b | 43583 | 0 |
| 861c | 57863 | 0 |
| 861d | 38346 | 0 |

MEL is fed from `e3.post_action_update(actual_z_world=...)` -> `prediction_error`
(`ree_core/agent.py:9753-9761`), which does not read z_goal; z_goal enters action selection
(`e3_selector.py`) and sleep telemetry only. The defect is therefore **common-mode across every arm
and every run in the lineage, including the runs whose DVs passed**, so it cannot explain why
spindle_density fails while sws_power and replay_rate succeed. It is recorded as a real driver
defect (the lineage ran without goal-directed action selection while `goal.z_goal_enabled: true` was
declared), not as the cause of either failure.

---

## 2. The load-bearing finding: one defect, two consumption points

`on_factor` is **exactly** `mean_mel(HIGH) / mel_reference` -- verified to 4 decimal places on all
three 861c seeds (0.8366, 1.2146/1.2134, 1.8846). 861d's novelty gate is
`relative_novelty = clamp(mel/ref - 1, 0, 1)` (`ree_core/sleep/mel_consumer.py:123`). **Both runs'
load-bearing criteria are functions of the same `mel/mel_reference` ratio**, and both inherit the
same instability in where that reference lands.

### 2a. 861d -- the gate's operating point was usable on only 1 of 3 seeds

| seed | mel_reference | mel/ref - 1 across the 4 ON arms | gate range | state |
|---|---|---|---|---|
| 42 | 3.0e-5 | -0.135, -0.401, -0.036, -0.085 | **[0.000, 0.000]** | **DEAD** -- all clamp to 0 |
| 123 | 1.4e-5 | +0.623, +1.103, +1.162, +1.412 | [0.623, 1.000] | **SATURATED** -- 3/4 arms clamp to 1 |
| 456 | 3.0e-5 | +0.027, +0.183, +0.240, +0.867 | [0.027, 0.867] | **GRADED** |

On seed 42 every ON arm's MEL sits *below* the calibrated stable base, so the `mel_pe` lift
contributes **nothing** and the run silently degrades to the legacy `recency` path that 861a had
already shown to be flat. On seed 123 the gate saturates and cannot separate LOW from MED from HIGH;
that seed additionally shows 4-6 cycles of `n_cycles_insufficient_touched_slots`, diversity variance
~0 (0.0, 1.2e-5, 0.0, 6.1e-8) and one arm at exactly `0`, i.e. the DV is degenerate there
independently.

**C1b required 2/3 seeds while the mechanism under test was structurally unable to vary on 2/3.**
The 0/3 is a vacuous criterion, not a negative result -- the same class as the skill's
"structurally unsettable criterion" warning, arriving via calibration rather than dry-run truncation.

### 2b. The fix itself is validated at its own layer -- a positive result the `weakens` obscures

861a's defect was a uniformly flat `selection_weight` (~0.004-0.01). After `6aa97ca`:

| seed | ON-arm `mean_spindle_selection_weight` | OFF arm |
|---|---|---|
| 42 | 0.126, 0.009, 0.151, 0.108 | 0.008 |
| 123 | 0.561, 0.864, 0.799, **0.956** | 0.004 |
| 456 | 0.123, 0.232, 0.255, **0.761** | 0.004 |

The weight now spans ~100x, tracks measured MEL, and correctly collapses to ~0.004 on the MEL-OFF
control. **The 861a failure mode is resolved.** The blend is also not sign-inverted: in
`agent.py`, `z_world_selected = w*z_world + (1-w)*consolidation_ref`, so a higher weight *retains*
original content -- the intended direction.

### 2c. 861c -- one seed of genuine producer failure, one seed of pure calibration under-power

`mel_reference` is estimated from `CALIB_DRAWS = 5` draws at `rel_sd` 0.15-0.28, so its own sampling
scatter is the same size as the ecological effect being detected. With `K_CALIB_MARGIN = 2.0` the
required margin is `1 + 2*rel_sd/sqrt(n)`:

| seed | on_factor | rel_sd | n=5 margin | n=10 margin | n=20 margin |
|---|---|---|---|---|---|
| 7 | 0.8366 | 0.283 | 1.2530 fail | 1.1789 fail | 1.1265 fail |
| 271 | **1.2146** | 0.246 | 1.2202 **fail by 0.5%** | 1.1557 **PASS** | 1.1101 **PASS** |
| 883 | 1.8846 | 0.152 | 1.1360 PASS | 1.0962 PASS | 1.0680 PASS |
| | | | **1/3 -> FAIL** | **2/3 -> PASS** | **2/3 -> PASS** |

Seed 271 misses by **0.5%** purely on calibration sample size. Seed 7 fails for a real reason -- its
HIGH arm MEL (3.04e-5) sits *below* the no-shift base (3.64e-5), the link-(i) producer failure
already documented for 677/718/718a. So C2's failure is **mixed**: one seed cheaply fixable, one
seed a genuine producer gap. (Projection assumes `rel_sd` is a property of the underlying
distribution and SEM scales as 1/sqrt(n); the reported `calib_rel_sd_of_mean` values -- 0.1265,
0.1101, 0.0680 -- match `rel_sd/sqrt(5)` to within rounding, which is the check that the model holds.)

### 2d. Structural property (cluster read)

The lineage's measurement chain is

    novelty (producer) -> MEL -> [mel/mel_reference] -> consumer -> content selection -> write path -> DV

Stages 2-4 are **proven in both runs** (duration factor monotone in measured MEL; selection weight
monotone in MEL). The two failures sit at opposite ends and are **not** independent bugs: both are
the single shared normalisation `mel/mel_reference`, whose reference is estimated too coarsely and
is not reliably positioned below the ecological MEL distribution. Whichever consumer reads it --
861c's duration factor, 861d's novelty gate -- inherits a dead, saturated, or graded operating point
as a function of seed.

**These two runs are complementary, not a redundant re-derive.** One isolates the producer/consumer
normalisation, the other the selection/write path.

### 2e. Residual anomaly (flagged, not concluded)

On seed 456 -- the only seed with a usable gate range -- the DV moves *inversely* to selection
weight (weight 0.123 -> 0.761, DV 0.0195 -> 0.0120), opposite to the criterion's predicted sign.
n=1 clean seed, small absolute effects; recorded as an anomaly to test, not a result. The known,
distinct, **still-open** V3-EXQ-436c `ContextMemory.write_gate` bias-over-content defect sits between
the selection weight and this DV and is the leading candidate explanation.

---

## 3. Claim-layer mapping

- **MECH-180** (`candidate`, `v3_pending: true`, category `standard`): not fairly tested. DV1/DV2
  track measured MEL in both runs; the conjunctive gate was vetoed by a criterion that could not
  vary. `non_contributory`, status and `v3_pending` unchanged.
- **INV-050** (`candidate`, emergent from SD-017, category `standard`): same finding via 861c's C2.
  `non_contributory`, unchanged.
- **MECH-122** (`provisional`, category `standard`): the manifest's `weakens` is **overridden**. The
  claim bundles two mechanisms; the sensory-gating half has **zero V3 code**
  (`MECH122-SENSORY-GATING-OFFLINE-PROTECTION`, status `proposed`), and the content-packaging half
  was tested through an operating point that was dead or saturated on 2/3 seeds with a distinct
  known write-path defect still open downstream. An implementation/measurement gap must not demote
  the claim. `non_contributory`, status unchanged at `provisional`.

This reading is consistent with the lineage's own prior adjudications: 701c recorded
`measurement_calibration_not_substrate_ceiling`, and 718a recorded "NOT substrate_ceiling at the
consumer ... environment / test-bed producer gap; NOT falsification".

---

## 4. Four-layer diagnosis

| Layer | 861c | 861d |
|---|---|---|
| Claim alignment | intact (not fairly tested) | intact (not fairly tested) |
| Biological reference | clear -- sleep-pressure homeostat scaling consolidation with waking learning load; partial translation | clear -- spindle-mediated content packaging; partial translation |
| Prerequisites | present (R1/R2 both met) | present (R1/R2 met); downstream write-path prerequisite **missing** |
| Implementation completeness | complete | **complete at the tested layer** (fix fires, weight tracks MEL); sibling write_gate defect open |
| Environment adequacy | **partial** -- producer fails to raise MEL on seed 7 | partial (same producer) |
| Measurement adequacy | **under-instrumented** -- reference estimated from 5 draws at rel_sd 0.15-0.28 | **misleading** -- gate operating point unverified; DV degenerate on seed 123 |
| Integration adequacy | coupled | partially coupled -- selection weight live, DV unresponsive |
| Scale / capacity | adequate | adequate |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Verdict |
|---|---|
| MECHANISM FAILED | **partial** -- MECH-122 fix complete and firing; distinct 436c write_gate defect open |
| MEASURES FAILED | **established** -- calibration under-power (861c); unverified/dead/saturated operating point + degenerate DV seed (861d) |
| ENVIRONMENT FAILED | **partial** -- producer did not raise MEL above base on seed 7 |
| REE FAILED | **not established** |

**Net classification: MIXED, dominantly MEASURES -- not chargeable to REE.** Implementation,
Measurement and Environment do not all read adequate, so the REE-FAILED gate is not reached.

---

## 5. Re-derive brake (MOVE-3)

**Does NOT fire.** Prior confirmed `substrate_ceiling` hits under the R1-R3 convention: MECH-180 = 2,
INV-050 = 3, MECH-122 = 0. This autopsy recommends **`standard`**, not `substrate_ceiling`, so the
counts are unchanged.

That is the substantive call, not a technicality. The dominant blocker identified here is a
**calibration-procedure defect that is `complicated (buildable)`** -- quantified in 2c, where n=10
draws flips C2 to PASS. Per R3, "a broken instrument is not evidence of a ceiling, so counting it
inverts the brake's purpose." Had this been stamped `substrate_ceiling` it would have been
MECH-180's 3rd and INV-050's 4th hit, firing the brake and **forbidding the very re-run that would
settle the question**.

**Granularity-debt recurrence trigger: does NOT fire.** `granularity_debt_cluster.py` reports
MECH-180 7 targets (unclear=4, strengthened=2, other=1), INV-050 7 targets (unclear=4, intact=3),
MECH-122 1 target (other=1). **No target reads `weakened`** in any of the three -- measurement /
implementation debt, not granularity debt, regardless of count.

**No `fanout_recommendation`**: the bottleneck routes to one unambiguous buildable fix plus a
re-run, not a discrimination among >=2 live rival hypotheses.

---

## 6. Learning extracted

1. A consumer whose input is a **ratio against an empirically calibrated reference** silently
   inherits that reference's sampling error. Here the reference's own scatter (rel_sd 0.15-0.28 over
   5 draws) was the same magnitude as the ecological effect, so the experiment could not resolve it.
2. `clamp(x, 0, 1)` gates fail **in two opposite directions**, and both look like a clean negative:
   dead (all-zero, mechanism inert) and saturated (all-one, mechanism non-discriminating). A gated
   mechanism needs a **pre-registered operating-point precondition** proving the gate spans a usable
   range on a seed *before* that seed's criterion is scored.
3. A validated fix can be masked by a downstream, independently-known defect. 861d confirmed its own
   fix (weight now tracks MEL ~100x) while its manifest self-routed `weakens` against the claim --
   the positive result was invisible in the headline direction.
4. Scoring policy drift across sibling letters (DV3 excluded in 861c, load-bearing in 861d) is
   legitimate when the substrate changed between them, but the manifest should record *which*
   substrate state justified the change; here it took a git-history walk to establish.
5. The lineage-wide z_goal writer defect shows a common-mode substrate condition can persist across
   5 runs and 2 weeks without surfacing, because it biases no arm contrast.

---

## 7. Repair pathway (confirmed at the interactive gate)

**Node classification: `complicated (buildable)`** -- a named build with no open question.

**Primary -- `/queue-experiment` V3-EXQ-861e** (same-question re-run, new letter):
1. Raise `CALIB_DRAWS` from 5 to **>= 10** (2c shows this alone flips C2 to 2/3 PASS), and/or raise
   `CALIB_EPISODES_PER_DRAW` from 6.
2. Add a **pre-registered precondition** that the `mel/mel_reference` operating point spans a usable
   band on a seed before that seed's gate-dependent criterion is scored -- explicitly excluding both
   the dead (all-clamped-0) and saturated (all-clamped-1) regimes. Report the per-seed gate range in
   the manifest.
3. Score DV3 only on seeds passing that precondition; record `n_cycles_insufficient_touched_slots`
   as a DV-validity gate (seed 123 was degenerate independently).
4. Fix the z_goal writer defect in the driver's hand-rolled inner loop, or state explicitly that the
   lineage runs goal-free.

**Secondary -- substrate `amend`** on `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`: record the
vacuous revalidation, mark the 861a flat-weight failure_record item **resolved**, and keep the
distinct V3-EXQ-436c `write_gate` bias-over-content defect open as the leading candidate for 2e.

**Not routed to `/implement-substrate`**: the calibration procedure is driver-side
(`CALIB_DRAWS` is in the driver's own `thresholds`). The substrate-side hardening of
`MELConsumer.relative_novelty` (guarding its own operating point) is recorded on the substrate entry
but is not the blocking path for 861e.

### Draft `evidence_quality_note` for governance (do not apply from this skill)

> **MECH-180 / INV-050** -- V3-EXQ-861c (confirmed `failure_autopsy_861c-861d-mech180-cluster_2026-08-16`)
> -> `non_contributory`, status and `v3_pending` UNCHANGED. Both readiness gates met and DV1
> (sws_power) / DV2 (replay_rate) track measured MEL 3/3 seeds -- the consumer is functional again.
> The load-bearing C2 failure is `mel_reference` calibration under-power, not a substrate ceiling:
> `on_factor == mel_HIGH/mel_reference` exactly, the reference is estimated from 5 draws at rel_sd
> 0.15-0.28, and at n=10 draws C2 flips to 2/3 PASS (seed 271 misses by 0.5% at n=5). Seed 7 is a
> genuine link-(i) producer failure (HIGH-arm MEL below the no-shift base). Route: /queue-experiment
> V3-EXQ-861e (raise calibration draws + pre-registered operating-point precondition). Brake does NOT
> fire; category stays `standard`.
>
> **MECH-122** -- V3-EXQ-861d (same autopsy) -> `non_contributory`, status UNCHANGED at `provisional`.
> **The manifest's self-routed `weakens` is overridden.** The landed fix (ree-v3 `6aa97ca`) is
> confirmed working at its own layer -- `mean_spindle_selection_weight` now spans ~100x and tracks
> measured MEL, resolving the 861a flat-weight defect -- but the `clamp(mel/ref-1,0,1)` gate was DEAD
> on seed 42 (every ON arm below reference) and SATURATED on seed 123 (3/4 arms at 1.0, plus a
> degenerate DV with insufficient touched slots). The criterion required 2/3 seeds while the
> mechanism could not vary on 2/3, so C1b's 0/3 is vacuous, not evidence. The distinct V3-EXQ-436c
> `ContextMemory.write_gate` bias-over-content defect remains open downstream and is untested.

---

## 8. Hypothesis-space ledger (Step 9b)

**Skipped cleanly, confirmed at the gate.** No `fanout_recommendation` is emitted (single buildable
bottleneck, not a >=2-hypothesis discrimination), and no pre-registered leg in
`hypothesis_space_registry.v1.json` covers MECH-180 / MECH-122 / INV-050 -- the nearest question,
`sd017_arc045_mech166_slot_differentiation_sleep`, tags a different claim set and carries no
`growth_restriction`. Neither Step 9b trigger holds, so nothing is registered or resolved and the
registry, its two derive-only siblings and the integrity report are untouched by this autopsy.
