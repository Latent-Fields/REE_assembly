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
