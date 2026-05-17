# Sustained drive and anticipatory wanting: SD-012 amendment scoping

**Created:** 2026-05-08
**Trigger:** EXQ-536a (`H_b_threshold_never_crossed: true`, `mean drive on contact:
0.005`, `n_contact_events: 2 across 4000 steps`).
**Status:** Option 1 IMPLEMENTED 2026-05-17 (goal_pipeline:GAP-3 Phase 3).
Options 2-3 gated on the Option 1 discriminative sweep outcome. Lit-pull
companion landed (`evidence/literature/wanting_liking_sleep_consolidation_synthesis.md`).

> **Knob name reconciliation (2026-05-17):** the canonical config knob is
> **`drive_ema_alpha`** (the operative `goal_pipeline_plan.md` / Q2 term),
> default **1.0 = OFF / bit-identical**. The `alpha_drive_trace` name used in
> the Option 1 sketch below is superseded -- identical semantics. The Q2
> decision set the first-PASS arm to **0.02** (~35-step half-life,
> lit-anchored) with discriminative sweep {0.01, 0.02, 0.2, 1.0}; the trace
> is **zero-initialised** (accepted ~1/alpha-step cold-start confound, not
> the first-obs init the sketch mentions). See SD-012 doc "Sustained-drive
> amendment" section and `goal_pipeline_plan.md` GAP-3.

## Problem (the finding to solve)

EXQ-536a documented a **structural anti-correlation between drive and benefit at
contact time**, not a tuning issue:

```python
# SD-012 current form (goal.py update(), line ~144):
effective_benefit = benefit_exposure * z_goal_seeding_gain * (1.0 + drive_weight * drive_level)
# where drive_level = 1.0 - agent_energy
```

Energy resets toward 1.0 the moment a resource is consumed, so `drive_level` collapses
to ~0.005 at the exact step the agent is on a resource cell. The multiplier
`(1 + 2 * 0.005) = 1.01` cancels almost all the benefit amplification SD-012 was
intended to provide. Combined with sparse contact (2 contacts in 4000 steps in 536a),
`max_effective_benefit = 0.036 < benefit_threshold = 0.1`. The persistent attractor
never seeds; the entire MECH-295 weak liking-bridge is consequently silent (per the
companion `mech188_vs_mech295_dual_path.md` note).

This is not specific to 536a. It is a general property of **instantaneous drive
× instantaneous benefit** as the multiplicative gating signal: they are forced to
anti-correlate around contact events, which is exactly when seeding needs to fire.

## What the biology says (lit-pull in Task 4 will anchor citations)

The Berridge / Robinson "wanting / liking" dissociation (incentive salience theory,
1990s onward) names this: anticipatory dopaminergic wanting persists past
satiation. Wanting is a *sustained motivational state*, not extinguished by the
consummatory pulse. Three architectural ingredients show up across the literature:

1. **Sustained / anticipatory wanting**: dopaminergic (especially mesolimbic VTA →
   NAc) tone integrates over a window much longer than the consummatory event.
2. **Schema-driven anticipatory cue activation**: cues predictive of reward
   activate wanting *before* contact (Pavlovian-instrumental transfer, sign
   tracking).
3. **Insatiability floors**: chronic homeostatic deficits (food restriction,
   sleep deprivation) maintain a baseline wanting tone independent of recent
   consumption.

The substrate already has fragments of all three (MECH-216 schema-readout,
MECH-186 valence_wanting_floor, the persistent z_goal attractor's slow decay).
What it lacks is the **drive multiplier itself** being structured to match. The
multiplier should not collapse the moment energy is restored.

## Three substrate options

Listed in increasing order of architectural change. Each is independently
defensible; a clean experiment would test in this order (cheapest first).

### Option 1: Sustained-drive EMA

Replace instantaneous `drive_level` in the multiplier with a slow EMA:

```python
# in GoalState (or a small SustainedDriveTrace helper):
self._drive_trace = (1.0 - alpha_drive_trace) * self._drive_trace \
                  + alpha_drive_trace * drive_level
# alpha_drive_trace = 0.02  ->  half-life ~35 steps
effective_benefit = benefit_exposure * z_goal_seeding_gain \
                  * (1.0 + drive_weight * self._drive_trace)
```

**Cost:** ~10 lines in `goal.py`; one new config knob `alpha_drive_trace`
(default 1.0 preserves current behavior bit-identically); contract test pinning
the trace timescale.

**Falsifiability:** clean. ARM_OFF (alpha_drive_trace=1.0, current behavior) vs
ARM_TRACE (alpha=0.02). Predicted effect: `mean drive on contact` rises
materially (the trace doesn't collapse on energy restoration); benefit threshold
becomes reachable; z_goal seeds.

**Risk:** the trace-window-length is a free parameter. Half-life 35 steps is
a guess. Lit-pull should ground it (post-consumption wanting persistence
windows in rat operant studies are typically ~10-60s = ~30-200 of our steps).

### Option 2: Insatiability floor

Add a hard floor to drive_level used in seeding:

```python
drive_level_for_seeding = max(drive_level, drive_floor)
# drive_floor = 0.2
```

**Cost:** ~3 lines in `goal.py`; one new config knob `drive_floor` (default 0.0).

**Falsifiability:** also clean. ARM_OFF (drive_floor=0.0) vs ARM_FLOOR
(drive_floor=0.2). Predicted effect: every contact event produces
`effective_benefit >= benefit * (1 + 2 * 0.2) = 1.4 * benefit`, which clears the
threshold for `benefit > 0.072`. This unblocks seeding in the EXQ-536a regime.

**Risk:** less biological than Option 1. Insatiability floors exist (chronic
hunger, addiction), but a static floor is a crude analog. Better as a
diagnostic falsifier than a permanent change.

**Use case:** runs alongside Option 1 as a force-arm: if Option 1's trace doesn't
recover seeding because the trace mean is still too low, Option 2 isolates
whether the issue is "trace window" or "multiplier ceiling."

### Option 3: Anticipatory schema-driven wanting (existing substrate)

MECH-216 already exists: E1 predictive wanting / schema readout head
(`schema_salience -> VALENCE_WANTING`). It writes wanting to the residue field
at predicted-reward locations, before contact, gated by E1's schema readout.

The under-utilization is that **MECH-216 writes to the residue field but does
not feed into `update_z_goal()`**. The persistent attractor (`self._z_goal`) is
seeded only by the SD-012 update. So MECH-216 anticipatory wanting can fire
freely and the goal still doesn't seed.

The cleanest extension: add a path from MECH-216 schema readout into
`GoalState.update()`:

```python
# In agent.sense() before update_z_goal():
schema_wanting = self.e1.predict_wanting(z_world)  # already exists
# New: pass into update_z_goal as a sufficient seed signal.
self.goal_state.update(
    z_world_current=z_world,
    benefit_exposure=max(benefit_exposure, schema_wanting * schema_seed_gain),
    drive_level=drive_level,
)
```

**Cost:** medium. Wires MECH-216 into a new consumer; needs a config knob
`schema_seed_gain` (default 0.0 = no change); careful to avoid double-counting
during contact (when both schema_wanting and benefit_exposure fire).

**Falsifiability:** ARM_OFF (gain=0) vs ARM_ON (gain=0.5 or 1.0). Predicted
effect: seeding fires before first contact, when the schema head has built up
prediction. Most lit-aligned of the three.

**Risk:** depends on E1's schema readout actually carrying useful wanting
predictions. EXQ-503 confirmed MECH-216 fires in eval; but the regime relevance
in 514f / 536a class environments is untested.

## Recommended sequencing

1. **EXQ-538 lands first** (sleep ablation; doesn't depend on this thread).
2. **EXQ-537 lands** (SD-029 single-pass; doesn't depend either).
3. **EXQ-536c/d/e from `mech188_vs_mech295_dual_path.md` land first** if
   feasible — they discriminate whether MECH-295 itself is intact, which
   affects whether fixing seeding will produce behaviour at all.
4. **Then** queue **EXQ-539** (Option 1 sustained-drive EMA, 2-arm × 3-seed):
   ARM_OFF (alpha_drive_trace=1.0) vs ARM_TRACE (alpha=0.02). Acceptance:
   mean_drive_on_contact_arm_trace > 0.10 (10x lift over 536a's 0.005);
   max_effective_benefit > benefit_threshold across at least 2/3 seeds;
   z_goal_active_fraction > 0.20. Cost-bounded (~1.5h on Mac), single
   architectural variable.
5. **EXQ-540** (Option 2 insatiability floor, 2-arm × 3-seed) as falsifier
   only if 539 fails to produce seeding.
6. **EXQ-541** (Option 3 schema-driven anticipatory wanting) as the
   biology-aligned permanent solution if 539 reveals seeding is recoverable.

## SD-012 amendment vs SD-053-new-claim

I lean **SD-012 amendment** with a new MECH for the trace mechanism:

- SD-012 keeps its name and identity (homeostatic drive modulation for z_goal
  seeding), but the implementation_note grows to cover Option 1 (sustained-drive
  trace) as a refinement. Backward-compatible defaults (alpha=1.0) mean no
  existing experiment regresses.
- New **MECH-306 sustained_drive_trace** (mechanism_hypothesis) with
  evidence_quality_note linking EXQ-536a as the empirical anchor. Lit anchors
  TBD by Task 4 lit-pull.
- If schema-driven anticipatory wanting (Option 3) is also added, it fits
  cleanly under MECH-216 (already registered) — no new claim needed.

A new SD only makes sense if Options 1+3 together turn out to be a
qualitatively different substrate (e.g., requiring its own latent stream).
The current evidence does not support that.

## Open questions (Task 4 lit-pull will anchor)

1. What is the half-life of post-consumption wanting persistence in rat operant
   studies? (Berridge anticipatory wanting timescale.) This sets the trace
   window for Option 1.
2. Is there a literature on "drive integration" vs "drive instantaneous" in
   computational reward-prediction models that already names this anti-
   correlation problem? (Suspected: Daw / Niv / Glimcher work; Sutton temporal
   difference variants.)
3. How does Lansink 2009 / Stickgold 2013 sleep replay interact with wanting
   consolidation specifically? (For pairing with EXQ-538's sleep ablation
   result.)
4. Pavlovian-instrumental transfer (PIT) literature: does anticipatory cue-
   driven wanting *replace* instantaneous-benefit-driven seeding in animal
   models, or do they sum?

## See also

- `goal.py:106-148` — `GoalState.update()` current SD-012 form
- `agent.py:628-680` — MECH-295 weak liking bridge
- `regulators/mech295_liking_bridge.py` — bridge implementation
- `mech188_vs_mech295_dual_path.md` — companion note on the read-site
  disambiguation
- EXQ-536a manifest — empirical anchor for this memo
- MECH-186 valence_wanting_floor — adjacent prior art (residue-side floor)
