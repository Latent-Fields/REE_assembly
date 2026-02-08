# Implementation Hooks

This document provides practical guidance for future code integration of the astrocyte-aware regulatory stack **without requiring immediate code changes**. It specifies where a `RegulatoryField` module would sit in the architecture, what interfaces it should expose, and how it relates to existing REE components.

## Design philosophy

**Documentation-first:** This module does **not** mandate immediate code changes. It establishes:

- Where future regulatory field implementations should be placed.
- What interfaces they should expose.
- How they interact with existing E1/E2/E3/L-space components.

Implementers may choose to:

1. **Ignore the regulatory field initially** (treat \(\alpha_k\) as direct parameters; this is a valid v0 simplification).
2. **Add a minimal placeholder** (constant or simple decay dynamics for \(R(x,t)\)).
3. **Implement full regulatory field dynamics** (with spatial coupling, metabolic sensing, and monoaminergic integration).

## Where `RegulatoryField` sits in the architecture

### Architectural position

```
┌──────────────────────────────────────────────────┐
│  E3 (Trajectory Selector)                        │
│  ─────────────────────────────────────────────   │
│  Evaluates J(zeta) and selects action            │
└────────────┬─────────────────────────────────────┘
             │
             ↓
┌──────────────────────────────────────────────────┐
│  E2 (Fast Predictor) + E1 (Deep Predictor)       │
│  ─────────────────────────────────────────────   │
│  Fast neuronal prediction dynamics               │
│  Uses alpha_k(x,t) from RegulatoryField          │
└────────────┬─────────────────────────────────────┘
             │
             ↓
┌──────────────────────────────────────────────────┐
│  L-space (Latent State)                          │
│  ─────────────────────────────────────────────   │
│  Stores z_k(t) AND R(x,t)                        │
│  (neuro-glial state)                             │
└────────────┬─────────────────────────────────────┘
             │
             ↓
┌──────────────────────────────────────────────────┐
│  RegulatoryField (NEW MODULE)                    │
│  ─────────────────────────────────────────────   │
│  Maintains slow field state R(x,t)               │
│  Outputs gain/precision/plasticity multipliers   │
└──────────────────────────────────────────────────┘
```

**Key relationships:**

- **E2/E1** query `RegulatoryField` to get \(\alpha_k(x,t)\), \(\eta(x,t)\), and \(g(x,t)\).
- **L-space** stores both fast neuronal state \(z_k(t)\) and slow regulatory state \(R(x,t)\).
- **RegulatoryField** updates \(R(x,t)\) based on:
  - Monoaminergic signals (broadcast inputs).
  - Local activity (from E2/E1 prediction errors).
  - Metabolic constraints (from environment or homeostatic sensors).
- **E3** may query `RegulatoryField` to evaluate regulatory feasibility of candidate trajectories.

### Time-scale separation

| Component          | Timescale               | Update frequency       |
|--------------------|-------------------------|------------------------|
| E2 (Fast Pred.)    | Milliseconds            | Every time step        |
| E1 (Deep Pred.)    | 10s–100s of ms          | Every time step        |
| RegulatoryField    | Seconds to minutes      | Every N time steps (N ≫ 1) |
| Sleep (offline)    | Hours (minutes offline) | Between episodes       |

**Implication:**

> Do **not** update \(R(x,t)\) every time step. Update it every \(N\) steps (e.g., \(N=100\) if time step is 10 ms, giving updates every ~1 second).

This preserves the slow dynamics characteristic of astrocytic signaling.

## Suggested interfaces (language-agnostic)

### RegulatoryField module

```pseudo
class RegulatoryField:

    # ───────────────────────────────────────────────────────────────
    # State
    # ───────────────────────────────────────────────────────────────
    
    R: Array[float]  # Regulatory field state, shape (n_positions,)
                     # or (n_depths, n_positions) if depth-stratified
    
    tau_R: float     # Regulatory timescale (seconds)
    
    # ───────────────────────────────────────────────────────────────
    # Initialization
    # ───────────────────────────────────────────────────────────────
    
    def __init__(n_positions, tau_R, R_init=None):
        """
        n_positions: int, spatial dimension of regulatory field
        tau_R: float, regulatory timescale in seconds
        R_init: optional initial state (default: neutral baseline)
        """
        ...
    
    # ───────────────────────────────────────────────────────────────
    # Core update
    # ───────────────────────────────────────────────────────────────
    
    def update(dt, monoamine_signals, activity, metabolic_state):
        """
        Update R(x,t) → R(x, t+dt)
        
        Inputs:
          dt: float, elapsed time since last update (seconds)
          monoamine_signals: dict of {signal_name: level}
              e.g., {"dopamine": 0.8, "serotonin": 0.3, "noradrenaline": 0.5}
          activity: Array[float], local activity level at each position
              (e.g., magnitude of prediction error, firing rate)
          metabolic_state: Array[float], local metabolic availability
              (e.g., glucose level, lactate availability)
        
        Outputs:
          None (updates self.R in place)
        """
        ...
    
    # ───────────────────────────────────────────────────────────────
    # Query interface (used by E2/E1)
    # ───────────────────────────────────────────────────────────────
    
    def get_precision_multipliers(depth_k):
        """
        Get precision multipliers alpha_k(x,t) for depth k
        
        Inputs:
          depth_k: str or int, depth index (e.g., "gamma", "beta", "theta", "delta")
        
        Outputs:
          alpha_multipliers: Array[float], shape (n_positions,)
              Multiplicative factors for baseline precision alpha_k,0
              Example: alpha_k(x,t) = alpha_k,0 * alpha_multipliers[x]
        """
        ...
    
    def get_plasticity_multipliers():
        """
        Get plasticity rate multipliers eta(x,t)
        
        Outputs:
          eta_multipliers: Array[float], shape (n_positions,)
              Multiplicative factors for baseline learning rate eta_0
        """
        ...
    
    def get_gain_multipliers():
        """
        Get synaptic gain multipliers g(x,t)
        
        Outputs:
          gain_multipliers: Array[float], shape (n_positions,)
              Multiplicative factors for baseline gain g_0
        """
        ...
    
    # ───────────────────────────────────────────────────────────────
    # Sleep / offline integration
    # ───────────────────────────────────────────────────────────────
    
    def anneal(duration):
        """
        Run offline annealing dynamics (sleep-like recalibration)
        
        Inputs:
          duration: float, simulated offline time (seconds)
        
        Outputs:
          None (updates self.R toward baseline / smoothed state)
        """
        ...
    
    # ───────────────────────────────────────────────────────────────
    # Trajectory feasibility (optional, for E3)
    # ───────────────────────────────────────────────────────────────
    
    def evaluate_regulatory_cost(R_required, duration):
        """
        Compute cost of shifting from current R(x,t) to R_required
        
        Inputs:
          R_required: Array[float], desired regulatory state
          duration: float, time available for shift (seconds)
        
        Outputs:
          cost: float, regulatory mismatch cost
              High if R_required is far from current R and duration is short
        """
        ...
```

### Example integration into E2/E1

```pseudo
class E2_FastPredictor:
    
    regulatory_field: RegulatoryField
    alpha_baseline: dict  # {depth_k: baseline_value}
    
    def compute_prediction_error_loss(z_current, z_predicted):
        """
        Compute prediction error weighted by precision
        """
        
        # Get current precision multipliers from regulatory field
        alpha_multipliers = regulatory_field.get_precision_multipliers(depth_k)
        
        # Compute effective precision
        alpha_effective = alpha_baseline[depth_k] * alpha_multipliers
        
        # Weight prediction error by precision
        loss = alpha_effective * ||z_current - z_predicted||^2
        
        return loss
```

### Example monoaminergic signal generation

```pseudo
def generate_monoamine_signals(context):
    """
    Generate broadcast monoaminergic signals based on context
    
    This is a placeholder. In a full implementation, monoaminergic
    signals would be driven by:
      - Reward prediction errors (dopamine-like)
      - Uncertainty / surprise (noradrenaline-like)
      - Serotonin-like signals from E3 (option holding)
      - Task-dependent sensory demands (acetylcholine-like)
    
    Inputs:
      context: dict containing relevant state (reward, surprise, etc.)
    
    Outputs:
      signals: dict of {signal_name: level}
    """
    
    signals = {
        "dopamine": compute_dopamine_like(context),
        "serotonin": compute_serotonin_like(context),
        "noradrenaline": compute_noradrenaline_like(context),
        "acetylcholine": compute_acetylcholine_like(context),
    }
    
    return signals
```

## Minimal placeholder implementation

For REE-v0, a minimal placeholder that captures the key abstraction:

```pseudo
class RegulatoryField_Minimal:
    
    R: float  # Single global regulatory state (no spatial variation)
    tau_R: float = 10.0  # 10 seconds
    
    def update(dt, monoamine_signals, activity, metabolic_state):
        # Simple exponential decay toward monoamine-driven target
        R_target = weighted_sum(monoamine_signals)
        self.R += (dt / tau_R) * (R_target - self.R)
    
    def get_precision_multipliers(depth_k):
        # Uniform multiplier (no spatial variation)
        return [self.R] * n_positions
```

This is **vastly simpler** than the full model but preserves:

- Slow dynamics (\(\tau_R = 10\) s).
- Monoaminergic input as a bias (not direct control).
- Interface compatibility with future extensions.

## Integration checklist (for future implementers)

When adding a full `RegulatoryField` module, ensure:

- [ ] \(R(x,t)\) is stored as part of L-space state.
- [ ] \(R(x,t)\) is updated at a slower cadence than \(z_k(t)\) (time-scale separation).
- [ ] E2/E1 query `RegulatoryField` for \(\alpha_k(x,t)\), \(\eta(x,t)\), \(g(x,t)\).
- [ ] Monoaminergic signals are generated from appropriate context (reward, surprise, etc.).
- [ ] Metabolic constraints are included (optional for v0, required for full model).
- [ ] Sleep recalibration includes `RegulatoryField.anneal()`.
- [ ] (Optional) E3 evaluates regulatory feasibility of trajectories via `evaluate_regulatory_cost()`.

## Example pseudocode: Full update loop

```pseudo
# ─────────────────────────────────────────────────────────────────
# Initialization
# ─────────────────────────────────────────────────────────────────

regulatory_field = RegulatoryField(n_positions=1024, tau_R=10.0)
E2 = E2_FastPredictor(regulatory_field)
E1 = E1_DeepPredictor(regulatory_field)

step_count = 0
regulatory_update_interval = 100  # Update R every 100 steps (~1 sec if dt=10ms)

# ─────────────────────────────────────────────────────────────────
# Main loop
# ─────────────────────────────────────────────────────────────────

for t in range(num_steps):
    
    # ───────────────────────────────────────────────────────────
    # Fast neuronal dynamics (every step)
    # ───────────────────────────────────────────────────────────
    
    o_t = observe_environment()
    z_t = E2.predict(o_t)
    z_context = E1.predict(z_t)
    action = E3.select_trajectory(z_t, z_context)
    execute_action(action)
    
    # ───────────────────────────────────────────────────────────
    # Slow regulatory dynamics (every N steps)
    # ───────────────────────────────────────────────────────────
    
    step_count += 1
    if step_count % regulatory_update_interval == 0:
        
        # Generate monoaminergic signals
        monoamine_signals = generate_monoamine_signals(context)
        
        # Compute local activity (e.g., prediction error magnitude)
        activity = compute_activity(E2, E1)
        
        # Query metabolic state (from homeostatic sensors)
        metabolic_state = get_metabolic_state()
        
        # Update regulatory field
        dt_regulatory = regulatory_update_interval * dt_step
        regulatory_field.update(dt_regulatory, monoamine_signals, activity, metabolic_state)

# ─────────────────────────────────────────────────────────────────
# Offline integration (sleep)
# ─────────────────────────────────────────────────────────────────

def sleep_recalibration():
    
    # Standard synaptic recalibration (as per existing REE spec)
    recalibrate_synaptic_weights(E2, E1)
    
    # NEW: Regulatory field annealing
    sleep_duration = 3600  # 1 hour simulated offline time
    regulatory_field.anneal(sleep_duration)
```

## Open design questions

1. **Spatial resolution:** Should \(R(x,t)\) be:
   - A single global scalar (simplest)?
   - Per-depth (one \(R_k(t)\) for each \(k \in \{\gamma, \beta, \theta, \delta\}\))?
   - Fully spatial (one \(R(x,t)\) for each position in L-space)?

2. **Monoamine signal generation:** Should monoaminergic signals be:
   - Manually specified (designer knobs)?
   - Derived from reward prediction errors / surprise (as in RL)?
   - Emergent from E3 trajectory evaluation (e.g., serotonin-like signal when multiple trajectories have similar cost)?

3. **Metabolic sensing:** Should metabolic state be:
   - A separate sensor input (requires environment to expose energy availability)?
   - Implicitly derived from activity (high activity → high energy drain)?
   - Ignored in v0 (constant metabolic state)?

These questions are **not answered here**. They are left for future design iterations.

## Summary

This document provides:

- **Architectural position** of `RegulatoryField` in REE.
- **Interface specifications** (language-agnostic pseudocode).
- **Time-scale separation** guidance (slow updates for \(R(x,t)\)).
- **Minimal placeholder** for v0 implementations.
- **Integration checklist** for full implementations.

No immediate code changes are required. This is a **forward-looking specification** to guide future development.
