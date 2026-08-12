# MECH-303 `contextual_safety_harm_threshold` default reachability

**Status:** documented finding, `complex (probe-gated)` on the recalibration question. No
substrate change made. Discriminating probe (V3-EXQ-917) completed 2026-08-11 -- see the
2026-08-12 addendum at the bottom, which reconciles its sourcing-mode-dependent result
against V3-EXQ-760's MECH-303 promotion evidence. Governance review of the addendum's draft
`evidence_quality_note` is still open.
**Date:** 2026-08-11 (addendum 2026-08-12)
**Trigger:** V3-EXQ-916 (Fishtank relief/safety showcase, first driver to enable
`use_contextual_safety_terrain=True`) found `agent.residue_field.total_safety == 0` and
`num_safety_steps == 0` for an entire 4000-step diagnostic run (1 seed, 15 warmup + 5 eval
episodes x 200 steps, reef env: 12x12 grid, 4 hazards, `hazard_harm=0.05`, continuous
multi-hazard exposure).

## Finding

`REEConfig.contextual_safety_harm_threshold` defaults to `0.05`
(`ree-v3/ree_core/utils/config.py`). MECH-303's live wiring in `agent.py` `sense()`
(~line 5128-5145) gates `ResidueField.accumulate_safety()` on
`z_harm_a.norm() < contextual_safety_harm_threshold`. That gate never held true in the
V3-EXQ-916 run -- confirmed as a genuine reachability finding, not a wiring bug: the flag
correctly sets `residue_field.safety_terrain_enabled = True`, and the accumulate/evaluate
code paths execute without error.

**This is not specific to continuously-hazardous environments.** Convergent evidence from
every prior experiment that has exercised this live-path gate shows the default is
unreachable even in fully quiescent (`num_hazards=0`) contexts, because it is miscalibrated
against the affective-harm encoder's actual output scale, not against environment hazard
density:

- **V3-EXQ-520** (SD-052 substrate-readiness diagnostic; `NUM_HAZARDS=3`, 8x8 grid, 300
  ticks/arm) could not exercise the live accumulation path at the default threshold either.
  Its `ARM_1`/`ARM_2` integration arms set `harm_threshold=999` specifically "(forces
  accumulation)" -- an intentional positive-control override, not a calibrated value, used
  to isolate "does the wiring work" from "is 0.05 the right number."
- **V3-EXQ-764** (MECH-303 behavioural falsifier) measured the real z_harm_a norm baseline
  directly: **~0.547 in a SAFE context (`num_hazards=0`) and ~0.542 in an UNSAFE context
  (`num_hazards=8`)** -- both roughly **11x above** the 0.05 default, and nearly identical
  to each other. Comment at `v3_exq_764_..._falsifier.py:146-148`: "The affective-harm
  encoder z_harm_a does NOT distinguish hazard density (SD-011: ~0.547 safe vs ~0.542
  unsafe, both below the 0.55 accumulate gate)." 764 had to calibrate its own threshold to
  `0.55` (`CONTEXTUAL_HARM_THRESHOLD`, chosen "above the per-seed z_harm_a safe baseline")
  just to get accumulation to fire at all, and even then had to **freeze** live accumulation
  during its actual test window (`TEST_FREEZE_HARM_THRESHOLD = -1.0`) because 0.55 does not
  reliably discriminate safe from unsafe -- live accumulation during the test would have
  "polluted the unsafe read."
- **V3-EXQ-760** (MECH-303's own representation-level validation, PASS, `auc_gated=0.884`)
  does **not** exercise this gate at all. It calls `ResidueField.accumulate_safety()`
  directly with its own `QUIESCENT_THRESHOLD = 0.5` gated on **ground-truth** environment
  `hazard_field_view` proximity (exactly 0 in its `num_hazards=0` SAFE contexts, ~10-21 in
  its `num_hazards=8` UNSAFE contexts) -- explicitly to "isolate the ResidueField mechanism
  from harm-encoder fidelity (a separate claim, SD-011)." So 760's PASS validates that the
  RBF terrain mechanism CAN discriminate context given a working gate signal; it says
  nothing about whether the live agent-path gate (real z_harm_a norm vs.
  `contextual_safety_harm_threshold`) is ever satisfied in practice.

## Why this is `complex (probe-gated)`, not `complicated (buildable)`

A naive fix -- just raise the default threshold to something reachable, e.g. ~0.55 -- is
not obviously correct, because 764 already found that range does not discriminate safe from
unsafe (0.547 vs 0.542, a gap the same experiment treated as too small to trust; SD-011:
the affective-harm encoder's z_harm_a norm barely varies with hazard density at all in the
range near its own baseline). So the two things a default value needs to do here --
**reachable** and **discriminating** -- are currently in tension, and it's not established
whether any single fixed threshold satisfies both across the environments this substrate
gets used in, or whether that tension is fundamentally an SD-011 encoder limitation
(z_harm_a not being separable enough at this operating point) that a threshold value cannot
fix. Per `docs/architecture/work_graph_debt_vocabulary.md`, that unknown makes this a
`complex (probe-gated)` question -- it needs a discriminating experiment (measure the
z_harm_a norm distribution and safe/unsafe separability across a battery of environments,
not just the two already measured) before a new default can be proposed with confidence.

## What was and was not done here

- **Documented** (buildable, done in this session): `ree_core/utils/config.py` comment on
  `contextual_safety_harm_threshold` now warns explicitly that the 0.05 default is
  unreachable and cites this doc; V3-EXQ-916's docstring now carries a KNOWN LIMITATION
  block explaining the `total_safety==0` / flat `safety_terrain_read` result is expected,
  not a driver bug.
- **Not done**: no change to the default value itself, no change to MECH-303 substrate code,
  no change to `claims.yaml` (MECH-303's claim and its V3-EXQ-760 evidence are unaffected --
  this is a downstream default-config usability issue for OTHER drivers, not a defect in the
  validated mechanism).
- **Routed**: a `/queue-experiment` chip for the discriminating probe described above
  (z_harm_a norm / separability battery across environments, to determine whether a better
  fixed default exists or whether this is gated on the SD-011 encoder itself).

## Precedent this establishes

Any FUTURE driver enabling `use_contextual_safety_terrain=True` should treat the default
threshold as **not usable as-is** and must explicitly calibrate/override
`contextual_safety_harm_threshold` against that driver's own observed z_harm_a distribution
(per the config.py comment), rather than relying on the default reaching -- mirroring the
existing precedent set by V3-EXQ-520 (positive-control override) and V3-EXQ-764 (per-seed
calibration + test-time freeze).

## 2026-08-12 addendum: V3-EXQ-917 sourcing-mode battery, and its bearing on V3-EXQ-760

**Trigger.** V3-EXQ-917 (the discriminating probe this doc routed to `/queue-experiment`,
PASS/supports, `evidence/experiments/v3_exq_917_mech303_harm_threshold_calibration_battery_
20260811T205119Z_v3.json`) is the first experiment to exercise MECH-303's live gate
end-to-end through the REAL agent pipeline (real `z_harm_a`, not the ground-truth proxy
V3-EXQ-760 used). It crossed 18 candidate thresholds x 5 hazard-density levels x 2
**sourcing modes** of `harm_obs_a` (SD-022's `limb_damage_enabled` flag):

| mode | `limb_damage_enabled` | density_condition_means (h0/h1/h2/h4/h8) | best threshold found |
|---|---|---|---|
| `damage_sourced` | `True` | 0.442 / 0.442 / 0.442 / 0.442 / 0.442 (flat to the 3rd decimal) | **none** -- AUC pinned at 0.500 (chance) at every one of 18 thresholds from 0.02 to 0.80 |
| `proximity_ema_sourced` | `False` (framework default) | 0.464 / 0.522 / 0.627 / 0.765 / 0.778 (monotonic) | tau=0.6: reach=0.848, AUC=0.969 |

**Finding 1 -- confirmed, not a wiring bug: `damage_sourced` is CONSTRUCT-INAPPROPRIATE for
context safety, and that is SD-022's own stated design intent.** SD-022's own
`claims.yaml` `functional_restatement` (id `SD-022`, registered 2026-04-09) states the goal
directly: "An agent in a safe location with accumulated limb damage should have high
`z_harm_a` and near-zero `z_harm_s` -- a dissociation CausalGridWorldV2 cannot currently
produce [pre-SD-022]." SD-022 succeeded at exactly this: `limb_damage` is a slow-healing
(`heal_rate=0.002/step` default), path-dependent integral of PAST collisions that is, BY
DESIGN, decoupled from the agent's PRESENT location. That is correct and validated
behaviour for SD-011's own A-delta/C-fiber dissociation research (SD-022's own
`live_status.evidence`: `v3_exq_323a_sd019_harm_nonredundancy`, supports/PASS). It is the
*wrong* signal for a mechanism -- MECH-303 -- whose entire claim is about **current spatial
context**. Both mechanisms are doing what they were built to do; the defect is at the seam
where MECH-303 reads `z_harm_a` without accounting for what SD-022 changed it to mean.
This is a "two-defect-can-coexist" case in the sense CLAUDE.md's remedy (a2) describes for
coupled code, generalised from a code/contract pair to a shared-signal/two-consumers pair:
SD-022 (producer) and MECH-303 (consumer) each pass their own validation individually while
being mutually incompatible at the interface between them.

**Finding 2 -- V3-EXQ-917's own "production default" premise does not hold across the
actual driver population, which changes how urgent this is.** V3-EXQ-917's docstring
asserts `damage_sourced` "is what every production driver that has exercised this gate --
764, 520, 916 -- sets." Checked directly against `ree-v3/experiments/`: of the **20** driver
scripts that set `use_contextual_safety_terrain=True` (a broader set than the 3 named),
`limb_damage_enabled=True` is set explicitly by only **V3-EXQ-520** and **V3-EXQ-764**. The
other 18 (`228b/c/d`, `603j/l/o/p/q/r/s/t`, `687/687a`, `866a/b/c`, `899`, and -- contrary to
the docstring's own citation -- **916 and 916a**) do not set it at all, so they run under the
`REEConfig.from_dims`/`CausalGridWorldV2` constructor default of `False`, i.e.
`proximity_ema_sourced` -- the mode V3-EXQ-917 itself found DOES discriminate well
(AUC up to 0.969). Of the two `damage_sourced` outliers: V3-EXQ-520 is a positive-control
readiness diagnostic that force-overrides the threshold to 999 (not a calibrated production
run), and V3-EXQ-764 was never queued/run as a scored experiment (ad-hoc inline probe only,
per this doc's own earlier finding above) -- so **no reviewed, scored experiment has actually
exercised MECH-303's live gate under `damage_sourced` and reported it working**. The
practical exposure today is narrower than V3-EXQ-917's headline C1 result implies. The
residual risk is prospective, not retrospective: V3-EXQ-917's manifest is itself now a
citable "damage_sourced = production default" claim, and a future driver copying that
framing (rather than the 18-driver majority pattern) would inherit the chance-level failure.

**Finding 3 -- bearing on V3-EXQ-760 / MECH-303's `provisional` promotion.** V3-EXQ-760's
own scope note ("isolate the ResidueField mechanism from harm-encoder fidelity") is honest
about what it tested, and its AUC 0.884 remains valid evidence for exactly that narrow
claim: the RBF terrain mechanism CAN discriminate context given a working gate signal. What
V3-EXQ-917 adds is that the **live gate signal MECH-303 actually reads in most exercised
drivers is a different question from what 760 measured**, and that whether it "works" is
sourcing-mode-dependent -- worse than a simple recalibration question (this doc's original
framing), but not a null result either (C2 passed). `claims.yaml`'s existing
`evidence_quality_note` states "Promote-to-active remains gated on a behavioural falsifier
(context-safety lowers background vigilance/avoidance-commitment level)" -- that gate was
already correctly conservative and is unaffected by this finding. What IS newly relevant to
governance is whether the `provisional` evidence_quality_note should be amended to record
that the representation-level PASS (760) has now been shown NOT to transfer uniformly to
the live gate signal, with the transfer outcome depending on a sourcing-mode choice that
760 never varied and that most exercised drivers make implicitly (by omission) rather than
deliberately.

**Draft `evidence_quality_note` addendum, for governance to review/apply (NOT applied here --
`claims.yaml` is governance-only per CLAUDE.md High-Contention Files; a `/governance` session
held an active directory-scope claim over `evidence/` at investigation time, so this is
recorded here rather than as a live edit):**

> 2026-08-12: V3-EXQ-917 (harm-threshold calibration battery, PASS/supports,
> label=mech303_tension_sourcing_mode_dependent) found the live agent-path gate
> (z_harm_a.norm() < contextual_safety_harm_threshold) is chance-level (AUC ~0.500 at every
> threshold 0.02-0.80) under `damage_sourced` z_harm_a (SD-022's body-damage re-sourcing),
> but discriminates well (AUC up to 0.969) under the legacy `proximity_ema_sourced` mode
> (limb_damage_enabled=False, the framework default and what 18 of the 20 drivers
> exercising this gate actually run under, whether by omission or design). V3-EXQ-760's
> representation-level AUC 0.884 remains valid for the narrow ground-truth-isolated claim
> it tested (the RBF terrain mechanism itself); it does not establish that the live z_harm_a
> gate signal discriminates context under all sourcing configurations, and empirically it
> does not under one of the two configurations now measured. No claims.yaml status change
> recommended by this note alone -- see
> evidence/planning/mech303_contextual_safety_threshold_reachability.md 2026-08-12 addendum
> for the full reconciliation, including why "damage_sourced is the production default" (as
> V3-EXQ-917's own docstring asserted) does not hold across the actual 20-driver population.

**Recommendation, not implemented here (routed, per task scope -- no substrate/claims.yaml
change made in this session).** Two options, differentiated by evidence support:
1. **Near-term, empirically supported by V3-EXQ-917's own C2 result:** MECH-303's own
   config should not silently inherit whatever `limb_damage_enabled` the rest of a driver's
   config happens to set for SD-022's unrelated body-damage purposes. The two consumers want
   opposite things from one shared boolean (SD-022 wants body/context DECOUPLED; MECH-303
   wants body/context COUPLED), so a single flag structurally cannot serve both at once --
   this is the actual architectural gap, not merely a threshold-calibration question as
   originally framed. A driver wanting both SD-022's body-damage dissociation AND a working
   MECH-303 safety terrain currently cannot have both.
2. **Longer-term, matching the organism-review Section 5 framing (investigated, not
   validated in this session):** re-express MECH-303's gate as predicted-future-harm rather
   than current-accumulated-harm-proxy. The needed forward-prediction infrastructure
   partially exists already -- `E2_harm_a` (MECH-258/SD-032b) and `E2_harm_s` (ARC-033, with
   `counterfactual_forward`) both compute one-step-ahead predicted harm given a candidate
   action -- but neither is currently wired into trajectory-scoring or safety-terrain gating;
   both are consumed only by MECH-276's causal-attribution bookkeeping
   (`_update_scientist_attribution`). The natural home for a genuinely predictive,
   per-candidate harm signal in action selection (dACC payoff, `agent.py` ~line 6694) is an
   explicitly-acknowledged, not-yet-built TODO ("Future refinement (Croxson): harm-forward
   rollout cost"). So option 2 is buildable from existing parts but is new wiring work, not
   a config change -- option 1 is the smaller, already-evidence-backed fix; option 2 is the
   architecturally more complete one the organism review's framing points toward.

No files outside this addendum were changed by this investigation. `claims.yaml` was read
only, per the active `/governance` session's directory-scope claim over `REE_assembly/
evidence/` at the time (session `sd-016-h3-algorithm-3370cd`, `governance-pause: 2026-08-12
cycle` -- a scope-claim NOTE, not an arbitrated conflict, per CLAUDE.md Conflict resolution).
