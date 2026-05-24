# Failure Autopsy: V3-EXQ-483c (SD-037 / MECH-280 / MECH-281)

**Generated**: 2026-05-24T09:48:46Z
**Scope**: single experiment
**Status**: confirmed (user sign-off 2026-05-24)
**Autopsy session**: failure-autopsy-483c-20260523T221919Z

---

## 1. Target

| Field | Value |
|---|---|
| run_id | v3_exq_483c_sd037_broadcast_gap4_tier1_20260521T064444Z_v3 |
| queue_id | V3-EXQ-483c |
| claim_ids | SD-037, MECH-280, MECH-281 |
| outcome | FAIL |
| experiment_purpose | evidence |
| evidence_direction (manifest) | mixed -- SD-037: weakens, MECH-280: unknown, MECH-281: unknown |

---

## 2. Facts Reconstruction

### Pass/fail criteria

| Criterion | Result | Value |
|---|---|---|
| C1_cue_fires | PASS | bridge_cue_fires > 0 in all runs |
| C2_dacc_bias | **FAIL** | dacc_bias_nonzero_steps = 0 in ALL 12 runs (3 seeds x 4 arms) |
| C3_approach_commit | PASS | approach_commit_rate = 1.0 in all runs |
| C3_lift_vs_baseline | **FAIL** | approach_commit_rate = 1.0 in OFF_OFF baseline (no headroom) |
| C4_goal_active | PASS | goal_active_fraction = 1.0 in all runs |

### Per-arm summary (seeds 42, 7, 19)

| Arm | Seeds | Total steps | dacc_bias_nonzero_steps | approach_commit_rate |
|---|---|---|---|---|
| OFF_OFF | 42, 7, 19 | 1714, 59, 793 | 0, 0, 0 | 1.0, 1.0, 1.0 |
| ON_OFF | 42, 7, 19 | 1849, 59, 1154 | 0, 0, 0 | 1.0, 1.0, 1.0 |
| OFF_ON | 42, 7, 19 | 1714, 59, 793 | 0, 0, 0 | 1.0, 1.0, 1.0 |
| ON_ON | 42, 7, 19 | 1849, 59, 1154 | 0, 0, 0 | 1.0, 1.0, 1.0 |

The uniform zero across ALL arms -- including the OFF_OFF baseline where SD-037 is also
inactive -- is the canonical substrate-floor / measurement-gap fingerprint. A genuine
behavioral weakening would suppress ON arms relative to OFF baseline, not produce
identically zero values everywhere.

### Script design

4-arm factorial: GABA suppress (ON/OFF) x broadcast override (ON/OFF). None of the 4
ArmSpec definitions include `use_dacc=True`. The experiment uses
`evaluate_tier1_cohort(rows, gap4_arm_id="ON_ON", baseline_arm_id="OFF_OFF")` from
`_lib/goal_pipeline_tier1.py`.

---

## 3. Root Cause: C2 Criterion

`_dacc_bias_norm(agent)` in `goal_pipeline_tier1.py` lines 204-218:

```python
def _dacc_bias_norm(agent: REEAgent) -> float:
    if agent.dacc is None:
        return 0.0
    ...
```

`agent.dacc is None` whenever `REEAgent` is constructed without `use_dacc=True`.
None of the 4 arms pass this flag. Result: `dacc_bias_nonzero_steps` is permanently 0
in every run step of every arm. The C2 counter cannot fire regardless of what SD-037 does.

The "weakens" tag on SD-037 is auto-generated in the experiment script from binary PASS/FAIL.
It carries no scientific signal: the FAIL is a configuration omission, not a behavioral
response to the broadcast override being on vs. off.

### C2 note: is dACC bias the right criterion for SD-037?

SD-037's primary pathway is PAG freeze-gate suppression + goal seeding + salience
coordination (orexin-analog). The dACC (SD-032b) is a downstream regulatory module.
Literature (targeted_review_orexin_kinetics + targeted_review_homeostatic_override,
13 papers combined) establishes a strong orexin -> PAG arousal override pathway; the
orexin -> dACC coupling is a secondary circuit. C2_dacc_bias was inherited from the
tier-1 template without customization for SD-037's actual primary pathway.

User judgment (confirmed 2026-05-24): Replace C2 criterion in 483d with PAG/override
metric (override_signal_nonzero_steps or PAG freeze-gate suppression rate) rather than
dACC bias.

---

## 4. Root Cause: C3_lift_vs_baseline

`approach_commit_rate = 1.0` in the OFF_OFF arm (seeds 42 and 19; seed 7 trivially short
at 59 steps). The baseline already achieves 100% approach commitment. No headroom remains
for SD-037 to register lift vs. baseline.

This is a behavioral property of the fishtank environment with drive_floor=0.9 + goal_stream:
the agent always commits to approach in this task. Not a SD-037 weakening signal.

---

## 5. Claim-Layer Mapping

### SD-037 (broadcast override regulator)

- claim_type: design_decision, status: candidate, v3_pending: true
- depends_on: SD-036, SD-012, SD-032a, MECH-279 (SD-032b NOT listed -- gap)
- Implementation: CONFIRMED (2026-04-25); PAG wiring confirmed by EXQ-483b (1.875x
  release ratio)
- EXQ-483c tested SD-037 under conditions where C2 COULD NOT fire regardless of SD-037
  state. "weakens" tag is not a scientific signal. Claim alignment: unclear / not tested.

### MECH-280 (LH-PAG override projection)

- status: candidate, v3_pending: true
- PAG wiring path confirmed by EXQ-483b; C2/C3 failures here say nothing about MECH-280.
- Evidence direction "unknown" is appropriate. Claim not under test by this experiment.

### MECH-281 (orexin-analog gain modulation)

- status: candidate, v3_pending: true, partially implemented
- GoalState seeding + SalienceCoordinator wired; dACC integration not tested.
- Evidence direction "unknown" is appropriate. Claim not meaningfully tested.

**Note on SD-037 depends_on gap**: SD-032b (DACCAdaptiveControl) is not in SD-037's
depends_on list in claims.yaml. If SD-037's proposed behavioral signature includes
dACC-coupled behavior, SD-032b should be added. Governance to evaluate.

---

## 6. Biological Reference Triage

SD-037 is an orexin-analog. Biological reference: **strong**.

Two lit-pulls confirmed:
- evidence/literature/targeted_review_sd_037_orexin_kinetics/synthesis.md
- evidence/literature/targeted_review_homeostatic_override (13 papers)

Primary pathway: orexin -> PAG arousal override (LC, dorsal raphe, PAG). Well-supported.
Secondary pathway: orexin -> dACC conflict monitoring modulation. Present in literature but
weaker mechanistic connection.

The FAIL does NOT challenge the orexin-analog existence proof. It is a measurement/
configuration gap in the experiment, not a failure of the biological translation.

No dACC-specific lit-pull exists for the SD-032b substrate itself -- this is a separate
gap flagged for follow-on work if dACC-coupled SD-037 behavior becomes the target.

---

## 7. Four-Layer Diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | C2 requires disabled substrate; SD-037 primary pathway not captured by any criterion |
| Biological reference | partial | Orexin -> PAG pathway strong; orexin -> dACC coupling weaker; C2 not testing primary pathway |
| Prerequisites | missing | SD-032b not in SD-037 depends_on; not enabled in any arm; identified as dependency gap |
| Implementation | complete | SD-037 implemented 2026-04-25; PAG wiring confirmed EXQ-483b (1.875x) |
| Environment | adequate | drive_floor=0.9 + goal_stream; C3_lift issue is policy ceiling, not environment |
| Measurement | misleading | C2 measures disabled substrate; C3_lift measures ceiling behavior; neither captures SD-037 |
| Integration | partial | SD-037 wired to PAG/SalienceCoordinator/GoalState; dACC integration not wired or tested |
| Scale | adequate | Seeds 42/19 run 793-1849 steps; adequate if metrics measured the right thing |

**Dominant diagnosis**: measurement_gap (both failed criteria are configuration/metric omissions,
not behavioral responses)

---

## 8. Cluster Pattern

All 5 GAP-4 tier-1 experiments share the same structural gap:

| Experiment | Claim(s) | use_dacc in arms? | C2 result |
|---|---|---|---|
| V3-EXQ-471a | catatonic lock | No | 0 in all runs |
| V3-EXQ-475a | SD-036 decay | No | 0 in all runs |
| V3-EXQ-483c | SD-037 broadcast | No | 0 in all runs |
| V3-EXQ-490g | MECH-295 cascade | No | 0 in all runs |
| V3-EXQ-524a | REEF showcase | No | 0 in all runs |

**Reading**: One structural property, not 5 independent bugs. The `evaluate_tier1_cohort`
function in `_lib/goal_pipeline_tier1.py` includes C2_dacc_bias as a mandatory criterion,
but the GAP-4 arm spec template (ENV_FISHTANK_KWARGS + ArmSpec) does not include
`use_dacc=True`. Every GAP-4 tier-1 experiment that does not explicitly add `use_dacc=True`
to its arm configs will produce C2=false unconditionally.

**Planning decision this forces**: The tier-1 library fix and all 5 affected experiments'
evidence_direction need to be reviewed as a unit, not independently. The cluster-fix
decision (whether to patch the library default or require explicit per-experiment opt-in)
should be made once and applied to all 5 before any retest.

---

## 9. Learning Extracted

1. GAP-4 tier-1 template missing use_dacc=True -> C2_dacc_bias permanently 0 across 5
   experiments (cluster, single structural property)
2. SD-037's depends_on in claims.yaml omits SD-032b -- should be audited if dACC-coupled
   behavior is a claimed signature
3. "weakens" tag is auto-generated from binary FAIL; does not carry scientific signal when
   the failure mode is a configuration omission
4. C3_lift_vs_baseline requires a non-trivial baseline; drive_floor=0.9 + fishtank produces
   ceiling commitment in the baseline arm -- inappropriate for measuring lift
5. SD-037's primary PAG pathway is well-confirmed (EXQ-483b 1.875x); the dACC is a
   secondary pathway and C2_dacc_bias may not be the right discriminator for SD-037
   experiments at all
6. No lit-pull exists for the dACC substrate (SD-032b) specifically -- if dACC-coupled
   SD-037 behavior is later targeted, commission targeted_review_dacc_conflict_monitor

---

## 10. Repair Pathway

### Recommended routing: /queue-experiment -> V3-EXQ-483d

**Redesign spec for 483d**:

Primary change: Replace C2_dacc_bias with a PAG/override criterion that directly measures
SD-037's primary pathway:
- `override_signal_nonzero_steps`: count of steps where broadcast_override.override_signal > 1e-3
  in the ON arms (ON_OFF and ON_ON), compared to OFF arms where broadcast_override is disabled
- OR: PAG freeze-gate suppression rate delta (ON vs OFF) when drive_level > threshold AND
  z_harm sustained over the override window

Secondary change (cluster fix): Add `use_dacc=True` to all arm configs AND update the
tier-1 library (`ENV_FISHTANK_KWARGS` or a shared arm-spec factory) to include `use_dacc=True`
as a default for GAP-4 experiments. This repairs the C2_dacc_bias measurement for the 4
other affected experiments.

C3_lift issue: Consider switching from approach_commit_rate lift to a metric that has
headroom in the fishtank with drive_floor=0.9 -- e.g., override_signal magnitude at first
threat encounter, or goal_norm_peak delta vs baseline.

**Note**: The other 4 cluster experiments (471a, 475a, 490g, 524a) need their own retest
decisions via /governance -- the cluster fix in the library enables correct measurement for
all of them, but the scientific questions they ask are different.

---

## 11. Draft evidence_quality_note (governance to apply)

For SD-037:

"V3-EXQ-483c: C2_dacc_bias=0 across all 12 runs (3 seeds x 4 arms) because use_dacc=True
was omitted from all arm configs -- agent.dacc is None in every run, _dacc_bias_norm()
returns 0.0 immediately regardless of SD-037 state. C3_lift_vs_baseline=false because
approach_commit_rate=1.0 in the OFF_OFF baseline arm (policy ceiling, not SD-037
suppression). Both failures are configuration/measurement gaps; 'weakens' tag is
algorithm-generated from binary FAIL and carries no scientific signal here. SD-037
implementation confirmed functional (EXQ-483b: PAG release ratio 1.875x). Cluster: 5
GAP-4 tier-1 experiments share this gap -- single structural property of tier-1 library.
evidence_direction revised to non_contributory. Pending retest: V3-EXQ-483d with
PAG/override_signal as primary C2 criterion + use_dacc=True cluster fix. SD-032b
dependency gap flagged for depends_on audit."

For MECH-280 and MECH-281:

"V3-EXQ-483c: evidence_direction=unknown retained. PAG wiring confirmed by EXQ-483b
(1.875x release ratio). C2/C3 failures in 483c were configuration/measurement gaps not
diagnostic of MECH-280/MECH-281 behavior. Pending purposeful retest via 483d."

---

## 12. Routing Decision (confirmed by user 2026-05-24)

- evidence_direction for SD-037: non_contributory (pending 483d)
- evidence_direction for MECH-280, MECH-281: unknown (retained)
- recommended_epistemic_category: measurement_gap
- routing: /queue-experiment -> V3-EXQ-483d
- cluster fix: include use_dacc=True in tier-1 library AND 483d arm configs
- C2 criterion for 483d: PAG/override_signal metric (not dACC bias)
- SD-032b depends_on gap: flag for governance depends_on audit of SD-037
