# Serotonergic Cross-State Substrate Requirements

Created: 2026-04-06
Claims: MECH-203 (replay salience tagging), MECH-204 (REM gate zero-point)
Status: design — pre-implementation

---

## Why This Blocks Hippocampal and Sleep Functioning

MECH-203 and MECH-204 are currently V4 scope. But SD-017 (minimal sleep-phase infrastructure)
is V3. This creates a dependency problem:

**Without MECH-203**, SWS replay (MECH-121) has no benefit-salience signal. Replay will be
entirely harm-salience-driven (from the residue field). Consequence:
- Hippocampal map consolidation is biased toward threat content
- Benefit-relevant experiences are under-consolidated
- z_goal representations degrade overnight even if they were seeded during waking
- This is the depressive consolidation asymmetry — but it will occur in ALL agents, not just
  those with 5-HT deficit, because the tagging mechanism is absent entirely

**Without MECH-204**, REM precision recalibration (MECH-123) has no principled zero-point.
The system recalibrates against... what? Without 5-HT withdrawal defining "neutral", the
precision system has no reference. Consequence:
- Precision recalibration is undefined or arbitrary
- The precision system cannot distinguish "benefit-gradient-active" from "no-gradient"
- INV-045 phase ordering constraint has no implementation mechanism

**The blocking dependency chain:**
```
SD-017 (V3: minimal sleep phases)
  |
  +-> MECH-121 (V4: SWS replay) needs MECH-203 for balanced replay content
  |     Without it: harm-biased consolidation in ALL agents
  |
  +-> MECH-123 (V4: REM recalibration) needs MECH-204 for calibration target
  |     Without it: undefined recalibration reference
  |
  +-> INV-045 (V4: phase ordering) needs MECH-204 for phase boundary mechanism
        Without it: no implementation of SWS-to-REM transition trigger
```

**Recommendation**: Pull at least the substrate primitives for MECH-203/204 into V3 scope,
even if the full mechanisms remain V4. The V3 sleep system needs these hooks to function
correctly, even in minimal form.

---

## Substrate Requirements

### SR-1: Tonic 5-HT State Variable

A slow-accumulating scalar `tonic_5ht` that tracks the agent's serotonergic tone.

**Waking dynamics:**
- Increases slowly when benefit_exposure > 0 (resources encountered)
- Decays slowly toward a baseline when no benefits occur
- Suppressed by chronic high z_harm_a (MECH-186 interaction)
- Range: [0.0, 1.0] where 1.0 = fully supported benefit gradient

**Sleep dynamics:**
- During SWS: held at waking level (5-HT is active during SWS)
- During REM: drops to 0.0 (dorsal raphe quiescence, MECH-204)
- On wake: restored to pre-sleep level

**Implementation sketch:**
```python
# In agent state or a new SerotoninModule
tonic_5ht: float = 0.5  # baseline
5HT_RISE_RATE = 0.01    # per benefit event
5HT_DECAY_RATE = 0.001  # per step without benefit
5HT_HARM_SUPPRESS = 0.1 # suppression rate when z_harm_a elevated
```

This is architecturally analogous to drive_level (SD-012) but for the benefit gradient
rather than the energy/need axis.

### SR-2: Experience Benefit-Salience Tagging

When experiences are stored (for potential replay), tag each with:
```python
benefit_salience = tonic_5ht * benefit_exposure_at_time
```

This creates a replay priority signal complementary to the existing harm salience from the
residue field. The hippocampal replay system (MECH-121) should then prioritize by:
```python
replay_priority = max(harm_salience, benefit_salience)
# Or: weighted combination allowing balanced consolidation
replay_priority = alpha * harm_salience + (1 - alpha) * benefit_salience
```

**Where to store the tag:**
- Option A: In the ThetaBuffer experience entries (alongside z_world, z_harm, action)
- Option B: In the ResidueField valence vector (SD-014 already has VALENCE_WANTING component)
- Option C: New field in HippocampalModule's trajectory proposals

Option B is most natural — SD-014's valence_vecs already record [wanting, liking,
harm_discriminative, surprise] per RBF center. benefit_salience could modulate the
VALENCE_WANTING component or be a 5th dimension.

### SR-3: REM Zero-Point Mechanism

During the REM phase (when `offline_mode=True` and phase=REM):
1. Set `tonic_5ht = 0.0` (withdrawal)
2. Record the current precision state as `precision_at_zero`
3. Recalibrate precision priors against this neutral reference

**Implementation requires:**
- A precision tracking mechanism (currently E3-derived but not explicitly accumulated)
- A way to compare "precision under benefit gradient" vs "precision without gradient"
- The difference defines what to recalibrate

This is more complex than SR-1/SR-2 and may genuinely be V4. But SR-1 and SR-2 can be
implemented in V3 as hooks that the sleep system uses.

### SR-4: Phase Boundary Trigger

The SWS-to-REM transition could be triggered by:
```python
if sws_consolidation_complete():  # e.g., replay_buffer exhausted or convergence metric
    tonic_5ht = 0.0  # begin withdrawal
    enter_rem_phase()
```

The serotonergic state transition IS the phase boundary. This connects the pharmacological
claims (SSRIs affect tonic_5ht -> affect tagging -> affect consolidation) to the sleep
architecture claims (phase ordering requires neuromodulatory state transitions).

---

## V3 vs V4 Scope Decision

| Substrate | Complexity | V3 Necessity | Recommendation |
|-----------|-----------|-------------|----------------|
| SR-1: tonic_5ht variable | Low | High (without it, all replay is harm-biased) | V3 |
| SR-2: benefit_salience tag | Medium | High (replay prioritization needs both signals) | V3 |
| SR-3: REM zero-point | High | Medium (REM can use simpler proxy in V3) | V4 |
| SR-4: Phase boundary trigger | Medium | Medium (V3 uses fixed alternation) | V4 |

**Minimum V3 pull**: SR-1 + SR-2. Add tonic_5ht as a state variable and tag experiences
with benefit_salience. SWS replay uses both harm and benefit salience for prioritization.
REM and phase boundary remain V4.

---

## Connection to Existing Substrate

| Existing Component | Connection Point |
|-------------------|-----------------|
| GoalConfig.valence_wanting_floor (MECH-186) | tonic_5ht modulates this floor |
| GoalConfig.z_goal_seeding_gain (MECH-187) | tonic_5ht IS the gain signal source |
| ResidueField.valence_vecs (SD-014) | benefit_salience stored in VALENCE_WANTING |
| ThetaBuffer.consolidation_summary() | benefit_salience weights replay selection |
| Agent.enter_offline_mode() | triggers tonic_5ht dynamics switch |
| E1.shy_normalise() (MECH-120) | operates during SWS (tonic_5ht active) |
| Agent.compute_drive_level() (SD-012) | drive_level and tonic_5ht are independent axes |

The key insight: `valence_wanting_floor`, `z_goal_seeding_gain`, and `z_goal_inject` are
already in the substrate as config parameters. But they are currently STATIC — set once at
experiment start. MECH-203/204 require them to be DYNAMIC, modulated by tonic_5ht which
itself evolves over time and across wake/sleep states.

**The minimum change**: make `z_goal_seeding_gain` a function of `tonic_5ht` rather than
a static config parameter. This single change connects the waking serotonergic system to
the sleep consolidation system.
