# Failure autopsy -- V3-EXQ-642b (MECH-353 calibrated blocked-agency floor validation)

- **Generated (UTC):** 2026-09-01T06:44:22Z
- **Scope:** single
- **Status:** confirmed (Step 8 gate held 2026-09-01, user present)
- **Run:** `v3_exq_642b_blocked_agency_calibrated_floor_validation_20260831T131011Z_v3`
- **Outcome:** FAIL -- `experiment_purpose: diagnostic`, `claim_ids: []`
- **Self-route label:** `z_block_integrator_no_rise` -- **INCORRECT** (see below)
- **Supersedes run:** V3-EXQ-642a; **supersedes autopsy:** none (this EXTENDS `failure_autopsy_V3-EXQ-642a_2026-08-30`, it does not overturn it)
- **Dry-run gate:** checked, `dry_run: false`; 0 dry runs cited or excluded.

## 1. Facts

The run validates the baseline-relative blocked-agency `outcome_mismatch_floor` built in
ree-v3 `d49db86f3e64670`. Protocol, env, seeds, arms, budgets and the pre-registered C0-C3
thresholds are reused verbatim from V3-EXQ-642a; the sole causal change is `CALIBRATION_CONFIG`.

Criteria: **C0 PASS, C1 FAIL, C2 FAIL, C3 PASS** (C1 and C2 both load-bearing).

| seed | BLK peak | CTL peak | **peak sep** | BLK mean | CTL mean | **mean sep** | z_harm_a sep |
|---|---|---|---|---|---|---|---|
| 42 | 1.500 | 1.500 | **0.000** | 0.812 | 0.131 | **0.681** | 0.000 |
| 43 | 1.500 | 1.500 | **0.000** | 0.767 | 0.177 | **0.590** | 0.000 |
| 44 | 1.500 | 1.500 | **0.000** | 0.835 | 0.064 | **0.771** | 0.000 |

Pre-registered thresholds: `C1_MARGIN = 0.20`, `Z_BLOCK_MIN = 0.20`, `C2_MARGIN = 0.20`.
Integrator clamp: `z_block_cap = 1.5` (`ree_core/affect/blocked_agency.py:153`).

Recording provenance: always-core complete -- `recording_schema: rec/v1`, `substrate_hash`
`1dd6181a...`, `machine_class linux-x86_64-py3.10-torch2.12.0+cpu`, `seeds [42,43,44]`,
`elapsed_seconds 1465.1`, full `config`. **No recording gap.** The decisive alternative
statistic (`z_block_mean`) is already in the manifest for both arms on all three seeds.

## 2. The criterion is unsatisfiable by construction

Both C1 and C2 read **only** `z_block_peak`
(`experiments/v3_exq_642a_blocked_agency_zblock_discriminative.py:459-464`):

```
c1 = (block["z_block_peak"] - control["z_block_peak"]) >= C1_MARGIN
     and block["z_block_peak"] >= Z_BLOCK_MIN
z_block_sep  = block["z_block_peak"] - control["z_block_peak"]
z_harm_a_sep = block["z_harm_a_mean"] - control["z_harm_a_mean"]
c2 = (z_block_sep - z_harm_a_sep) >= C2_MARGIN
```

`z_block_peak` is a **max over the run against a hard clamp**. Once *either* arm touches the
cap even once, `z_block_sep` is exactly 0.0 and both criteria are false whatever the policy
did. Both arms reach exactly 1.500 on all three seeds, so C1 and C2 returned false by
arithmetic, not by measurement. C2 additionally subtracts a `z_harm_a` separation that is a
structural 0.0 (harm held at zero by design), so it inherits C1's zero with nothing to offset it.

**Counterfactual on the same recorded data**, same pre-registered margins, statistic swapped
to `z_block_mean`: C1 and C2 pass on **3/3 seeds** (separations 0.681 / 0.590 / 0.771 against
a 0.20 margin; BLOCK means 0.767-0.835 against a 0.20 floor).

## 3. The substrate build under validation WORKED

Measured against the target the 642a autopsy's own `failure_record` entry set --
*"a working calibration must leave CONTROL-arm z_block well below cap"*:

| statistic | V3-EXQ-642a (legacy absolute floor) | V3-EXQ-642b (baseline-relative floor) |
|---|---|---|
| CONTROL `z_block_mean` | 1.26 - 1.35 (of a 1.5 cap) | **0.064 - 0.177** |
| BLOCK-CONTROL mean separation | +0.165 / +0.121 / +0.083 | **+0.681 / +0.590 / +0.771** |

Separation improved **4.1x-9.3x** (seed 42 4.13x, seed 43 4.88x, seed 44 9.29x) and the control arm is no longer parked near the cap. The
`sd_blocked_agency_mismatch_floor_calibration` entry's stated success condition is met on the
mean. What remains is that the control arm still **transiently** touches the cap (peak 1.500
with a mean of 0.064-0.177), which is what keeps a peak-difference criterion at zero.

## 4. This defect was diagnosed BEFORE the run

`failure_autopsy_V3-EXQ-642a_2026-08-30.json` (confirmed, generated 2026-08-30T06:34:18Z --
one day before 642b executed at 2026-08-31T13:10Z) named both root causes. Its
`learning_extracted[1]` reads verbatim:

> "A criterion built on a PEAK of a hard-clamped integrator is degenerate whenever the
> integrator can reach its clamp. z_block_cap=1.5 is reached in both arms; the
> difference-of-peaks is then 0.0 regardless of behaviour. Prefer a DV with headroom (mean,
> time-to-threshold, area under the accumulation curve) or record the saturation fraction
> alongside the peak."

The successor implemented the **substrate** half of that diagnosis and, by design
("intentionally reuses 642a's ... pre-registered C0-C3 thresholds"), inherited the
**measurement** half unrepaired. The reuse was a deliberate anti-fabrication choice -- not
moving a pre-registered threshold to fit a result -- and that instinct is correct. The gap is
that a criterion already shown to be arithmetically dead is not a threshold worth preserving.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free diagnostic; `bears_on` 10 claims, none tagged |
| Biological reference | partial | frustrative-non-reward / RAGE-analog integrator; MECH-353 lit anchor present. The failure is not a biology mismatch |
| Prerequisites | present | SD-070 warmup + SD-056 world-forward ran; C0 passed 3/3 (margins 0.62/0.53/0.51 vs 0.10) |
| Implementation | **complete** | the baseline-relative floor is built, landed, and demonstrably effective on the mean |
| Environment | adequate | static landmark env, harm pinned at zero, goal pinned; all controls behaved as designed |
| Measurement | **misleading** | the load-bearing statistic is a max against a hard clamp; 0.0 by construction in both arms, 3/3 seeds |
| Integration | coupled but unstable | comparator and integrator wired and now correctly scaled; the readout is not |
| Scale | adequate | 2400 policy steps/arm/seed, 3 seeds, ~1179 blocked steps per BLOCK arm |

**Failure-location (GOV-FAILLOC-1): MEASURES FAILED, solo.** Implementation reads complete
and Environment reads adequate, so neither MECHANISM nor ENVIRONMENT is established; REE
FAILED is not reachable. Net classification: **MEASURES**, not chargeable to REE or to the
regulator.

## 6. Residual finding worth recording

The control arm reaches `z_block_peak = 1.500` while sitting at a mean of 0.064-0.177. The
integrator therefore still saturates on transients in a **free** arm. The floor calibration
fixed sustained accumulation; it did not give the integrator headroom against brief excursions.
Any successor should record a saturation fraction (`frac of steps at cap`) alongside whatever
DV it routes on, exactly as the 642a autopsy suggested.

Secondary, and **corrected by the cross-model red-team pass**: the manifest reports
`z_goal_stream.writer_defect: true` (`writer_calls = 0` over 14400 ticks). This is **not a
defect in this run** -- it is a deliberate experimental control. The driver pins the goal at a
fixed magnitude (`GOAL_PIN = 0.5`, `_pin_goal()` called at
`v3_exq_642a_blocked_agency_zblock_discriminative.py:224` and invoked at :268, :304, :333, :354
and :373), which sets z_goal directly and bypasses the counted writer. That is exactly why
`ticks_active` reads 14400/14400 and `active_frac` 1.0 alongside zero writer calls -- a
combination an omitted `update_z_goal` could not produce. Neither C0 nor C3 reads a
goal-dependent statistic, so nothing here touches the adjudication.

This is a live instance of 642a's `learning_extracted[3]`: the writer-defect detector cannot
separate an omitted `update_z_goal` from a deliberately pinned constant goal, and here it
mislabels a correct control as a defect. The detector should be taught about the pinning path,
or drivers that pin should stamp the reason -- otherwise the flag will keep surfacing this
family in `pending_review.md` as a data-quality concern it is not.

## 7. Learning extracted

1. Repairing one of two co-diagnosed defects and re-running inherits the other at full cost. The
   642a autopsy named the peak degeneracy and the floor miscalibration together; fixing only the
   floor spent a 24-minute 6-run validation on a criterion already known to be arithmetically dead.
2. "Reuse the pre-registered threshold verbatim" is the right default and the wrong move when the
   prior autopsy has already shown the statistic cannot vary. The anti-fabrication rule protects a
   *threshold*; it does not oblige reuse of a *statistic* demonstrated to be degenerate. A successor
   should re-derive the criterion's reachability in the fixed regime -- the same lesson 936a's
   `learning_extracted[1]` records for a different family.
3. A validation run's success condition should be stated on the statistic its criterion consumes.
   642a's `failure_record.target` was worded on the peak ("so a peak difference >= C1_MARGIN is
   expressible"), which is unachievable while any transient touches the cap, even though the
   calibration it was testing succeeded.

## 8. Routing (confirmed at the Step 8 gate)

**`/queue-experiment` -- V3-EXQ-642c, same-question successor under a new letter.** Reuse the
642a/642b protocol, env, seeds, arms and budgets unchanged. The sole change is the readout:

- Move C1/C2 onto a **headroom DV** -- `z_block_mean`, area under the accumulation curve, or
  time-to-threshold -- and **re-derive the margins for that statistic** rather than transplanting
  the peak-calibrated 0.20. This is the point the user ratified at the gate: 642b's recorded mean
  is a strong prior (3/3 seeds, separations 0.590-0.771) but adjudicating on it directly would
  transplant a threshold calibrated for a different statistic, which is the fabrication hazard.
- Record a **saturation fraction** per arm alongside the routed DV.
- Keep C0 and C3 as they stand; both passed and neither is degenerate.

**Explicitly NOT routed to `/implement-substrate`.** The substrate is built and works. The
re-derive brake does not fire (claim-free target, no ceiling hit against any claim), and this
reading is **not** `substrate_ceiling`.

`sd_blocked_agency_mismatch_floor_calibration` keeps `severity: corrupting` -- the residual
trap is live for any peak-shaped readout, which is what consumed this run. It is recommended to move from
`implemented_pending_validation` toward validated on the mean evidence, with 642a's
`failure_record` item marked **resolved** and a new item opened for the transient-saturation
residual. Governance applies this; this autopsy only recommends it.
