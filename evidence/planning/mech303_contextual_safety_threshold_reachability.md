# MECH-303 `contextual_safety_harm_threshold` default reachability

**Status:** documented finding, `complex (probe-gated)` on the recalibration question. No
substrate change made. Chip spawned for the discriminating probe (see bottom).
**Date:** 2026-08-11
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
