---
nav_exclude: true
---

# SD-012: Homeostatic Drive Modulation

**Claim ID:** SD-012
**Subject:** `environment.homeostatic_drive`
**Status:** IMPLEMENTED (verified 2026-04-13 — see Implementation Note below)
**Registered:** 2026-03-25
**Depends on:** MECH-071, MECH-112, SD-005

---

## Problem

`GoalState.update()` does not use `drive_level`. As a result, `benefit_exposure` (EMA alpha=0.1
of raw benefit signals) never reliably crosses `benefit_threshold=0.05` during random-walk
warmup — a single resource contact produces `benefit_exposure ≈ 0.03`, which decays before the
next contact. This makes z_goal seeding fail under normal training conditions.

**Experimental evidence:** EXQ-085 through EXQ-085d (2026-03-23/24) all failed at the
goal-seeding bottleneck — z_goal_norm < 0.1 in every iteration across all runs. These
experiments were tagged MECH-071/INV-034 but produced no valid evidence for or against their
core claims because the mechanism under test (goal-state latent seeded by benefit exposure) was
never instantiated.

**Root cause:** Random-walk warmup without homeostatic drive cannot generate goal representations.
The agent is not motivated to approach resources during warmup, so resource contacts are rare and
benefit_exposure never accumulates to threshold.

**Biological grounding:** In biological systems, drive state (hunger, thirst) multiplicatively
scales reward salience — a depleted agent finds food more salient, generating stronger approach
motivation and more frequent resource contact. This is the functional role of interoceptive signals
routing through the hypothalamus into limbic/striatal circuits.

---

## Solution

Drive-scaled benefit signals: `drive_level = 1.0 - agent_energy` is already computable from
`obs_body[3]` (CausalGridWorldV2 already tracks `agent_energy` decaying at `energy_decay=0.01/step`,
restored by resource contact). The gap is wiring this into z_goal seeding.

**Required implementation changes:**

**(a) `GoalState.update()` — drive-scaled benefit amplitude:**
```python
def update(self, benefit_signal: float, drive_level: float) -> None:
    scaled_benefit = benefit_signal * (1.0 + drive_scale_factor * drive_level)
    self.benefit_exposure = alpha * self.benefit_exposure + (1 - alpha) * scaled_benefit
    if self.benefit_exposure > self.benefit_threshold:
        self._seed_goal_latent()   # z_goal seeded from benefit context
```

Where `drive_scale_factor` is a config parameter (default 2.0–4.0 based on calibration).

**(b) `LatentStack.encode()` — pass drive_level to GoalState:**
```python
drive_level = obs_body[3]   # already available from CausalGridWorldV2 body_state channel
self.goal_state.update(benefit_signal, drive_level)
```

**(c) `LatentStackConfig` — add drive_scale_factor:**
```python
drive_scale_factor: float = 3.0   # multiplier on benefit signal when depleted
```

---

## Architecture Context

### Relationship to z_harm_a (SD-011)

SD-012 and SD-011 are co-designed:
- z_harm_a (affective-motivational harm) represents the avoidance drive — accumulated homeostatic
  deviation from the harm axis
- z_goal/drive_level represents the approach drive — motivated by energy depletion and benefit
  salience
- Together they form the D1/D2 balance (ARC-030): D1 drive (wanting) + D2 avoidance (z_harm_a)
  sets the commit threshold

Without SD-012, the D1 side of the balance is permanently near-zero. The commit threshold then
reduces to harm-avoidance alone, producing the quiescence failure mode (INV-032/INV-034):
an agent that does nothing because any action might incur harm, and there's no approach drive
sufficient to commit.

### Relationship to z_beta (Affective Latent)

After SD-010 resolved the z_world contamination, a design question remains open in `l_space.md`:
should z_beta be driven from `drive_level` / `harm_history` rather than the current
interoceptive prediction error proxy? SD-012 positions `drive_level` as the appropriate
input for the homeostatic component of z_beta — though the precise wiring is not yet decided
(see `l_space.md` option C / post-SD-010 note in claims.yaml MECH-102 evidence notes).

### What SD-012 Is NOT

SD-012 is a specific, targeted fix for the goal-seeding bottleneck in CausalGridWorldV2.
It is not:
- A full redesign of the motivational architecture
- ARC-031 (z_self hippocampal navigation) — that is V4-scoped
- MECH-113 (allostatic anticipatory setpoint) — that is a Level 2 mechanism gated on EXQ-075/076

---

## What SD-012 Enables

- **Goal-directed behavior in V3 experiments:** EXQ-085 and its successors will be re-runnable
  once z_goal seeding is reliable
- **MECH-112 (wanting/liking dissociation) validation:** EXQ-074b tests whether wanting
  (z_goal_latent distance) and liking (benefit_eval_head spike) dissociate under resource
  relocation; this requires a functioning z_goal latent
- **MECH-116 (frontal working memory / E1 goal conditioning) validation:** EXQ-076b tests
  whether E1 LSTM hidden state maintains z_goal context across the theta buffer; requires
  reliable z_goal seeding
- **INV-034 (goal maintenance as necessary co-condition for ethical agency):** Claims about
  genuine agency require a functioning approach drive; SD-012 provides the minimal substrate

---

## Implementation Note (2026-04-13)

The substrate described in the Solution section is **IMPLEMENTED** in ree-v3. Verified by
source inspection on 2026-04-13:

- `GoalConfig.drive_weight` (float, default 2.0) is present in `ree_core/utils/config.py`.
- `GoalState.update()` applies `effective_benefit = benefit_exposure * z_goal_seeding_gain * (1.0 + drive_weight * drive_level)` — exactly the drive-scaled seeding specified in Solution (a).
- `REEConfig.from_dims()` wires `drive_weight` from kwargs into `GoalConfig`.

**Why experiments still failed despite correct implementation:**
All experiments from EXQ-085a through EXQ-328 used `obs_body[11]` (pre-step benefit_exposure EMA)
for seeding rather than the post-step `harm_signal` from `env.step()`. The env updates its EMA
*after* `env.step()`, so at resource contact, `obs_body[11] ≈ 0` and effective_benefit never
crosses threshold. This is a measurement/instrumentation bug in the experiment scripts, not
a substrate gap.

**EXQ-328a** (2026-04-12) fixes both the seeding signal and benefit_threshold calibration.
**EXQ-328b** (2026-04-13) is the first full real run of the correctly-instrumented script.

The "Problem" section above describes the pre-implementation state; the substrate gap it
describes no longer exists.

---

## Sustained-drive amendment (goal_pipeline:GAP-3, Option 1) — IMPLEMENTED 2026-05-17

EXQ-536a exposed a second, structural failure mode distinct from the 2026-04-13
instrumentation bug: even with the seeding signal read correctly, the multiplier
`(1 + drive_weight * drive_level)` collapses to ~1.0 the step a resource is consumed,
because `drive_level = 1 - energy` and energy resets toward 1.0 on consumption. Drive and
benefit are forced to anti-correlate around contact events — exactly when seeding must
fire (EXQ-536a: `H_b_threshold_never_crossed`, mean drive on contact 0.005, multiplier
~1.01). This is a general property of instantaneous-drive x instantaneous-benefit gating,
not a tuning issue. See `sustained_drive_anticipatory_wanting.md` for the full scoping
(three options) and `goal_pipeline_plan.md` GAP-3 / Phase 3.

**Option 1 (sustained-drive EMA) is implemented.** `GoalConfig.drive_ema_alpha`
(float, default **1.0**; in `ree_core/goal.py`). `GoalState.update()` now smooths
`drive_level` into a persistent trace before the multiplier:

```
_drive_trace = (1 - drive_ema_alpha) * _drive_trace + drive_ema_alpha * drive_level
effective_benefit = benefit_exposure * z_goal_seeding_gain
                    * (1 + drive_weight * _drive_trace)
```

- `drive_ema_alpha = 1.0` (default) -> `_drive_trace == drive_level` every step
  regardless of init -> **bit-identical** to the instantaneous form documented above.
  Backward-compatible; every existing experiment is unaffected (full contract +
  preflight suite 426/426 green; contract `test_sustained_drive_ema_gap3.py` C1/C2).
- Lit-anchored operating value **0.02** (~35-step half-life), inside the 30-60 step
  post-consummatory wanting-persistence window established in
  `evidence/literature/wanting_liking_sleep_consolidation_synthesis.md` (Berridge /
  Robinson sustained anticipatory wanting; Aponte / Livneh slow-decay hunger drive).
- `_drive_trace` is **zero-initialised** (goal_pipeline Q2 decision): for
  `alpha < 1.0` this carries a deliberate ~1/alpha-step cold-start transient that
  underestimates drive early in an episode — an accepted, documented confound the
  discriminative sweep accounts for.
- Surfaced through `REEConfig.from_dims()` mirroring the `drive_weight` plumbing.

**Naming reconciliation:** the canonical knob is `drive_ema_alpha` (the operative
`goal_pipeline_plan.md` / Q2 term). An earlier draft of
`sustained_drive_anticipatory_wanting.md` used `alpha_drive_trace`; that name is
superseded — same semantics, default 1.0 = OFF.

**Option 2 (insatiability floor) IMPLEMENTED 2026-05-17.** `GoalConfig.drive_floor`
(default 0.0 = OFF). `GoalState.update()` applies `drive_level_floored =
max(drive_level, drive_floor)` before the EMA/multiplier. Validated by V3-EXQ-582a PASS
(2026-05-19, floor=0.9 arm). Contract `test_drive_floor_gap3_opt2.py` 7/7.

**Validation outcome (goal_pipeline:GAP-3 closed 2026-05-20):** V3-EXQ-582 Option-1 EMA
sweep FAIL; V3-EXQ-582a Option-2 floor sweep PASS. **MECH-306 sustained_drive_trace**
registered in claims.yaml. Operating recommendation for downstream cascade retests:
`drive_floor=0.9`, `drive_ema_alpha=1.0` unless a combined arm is pre-registered. See
`goal_pipeline_plan.md` GAP-3 decision log 2026-05-20.

---

## Related Claims

- **SD-012** — this design decision
- **MECH-112** — wanting/liking dissociation (requires z_goal seeding)
- **MECH-113** — allostatic anticipatory setpoint (Level 2; gated on EXQ-075/076 — do not implement until gated)
- **INV-032** — moral agency requires both approach and avoidance drives
- **INV-034** — goal maintenance necessary for ethical agency
- **ARC-030** — D1/D2 approach-avoidance balance
- **Q-021** — quiescence failure mode (harm-avoidance-only architecture)
- **SD-011** — affective z_harm_a (avoidance counterpart to homeostatic drive)
- **SD-005** — z_self domain (obs_body[3] / agent_energy lives here)
