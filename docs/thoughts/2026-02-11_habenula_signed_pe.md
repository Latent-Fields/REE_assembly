Status: processed

Processed in:
- `docs/architecture/control_plane.md` (MECH-053, MECH-054, Q-010)
- `docs/architecture/control_plane_signal_map.md` (signal split note)

---

Thought: Habenula-Like Aversive PE and Signed Harm/Benefit Precision

Premise

REE currently has:
- valence as a vector stream (MECH-035)
- dopamine-like precision weighting for unsigned prediction errors (MECH-043)
- mu/kappa stability overlays (MECH-048)

This is not yet explicit about aversive prediction-error channels or the circuitry that gates negative motivational signals.
In brains, aversive prediction and motivational suppression are not just the inverse of reward prediction.
We need a separate aversive gate and a signed precision split.

Core additions

1. Habenula-like aversive PE gate
- A fast negative-valence / aversive prediction-error channel
- Suppresses or vetoes commitment when harm or threat predictions spike
- Does not compute trajectories; it gates which proposals are allowed to proceed

2. Signed harm/benefit prediction-error precision
- Maintain separate precision weighting for harm-related prediction errors and benefit-related prediction errors
- Treat them as distinct channels, not a single scalar valence
- This allows hedonic tone (mu/kappa) to remain a stability modulator rather than a complete valence system

Implications

- Hedonic vs anhedonic tone should be separated from harm vs benefit prediction-error precision
- Dopamine-like precision can modulate unsigned PE, while habenula-like gating handles aversive PE in a distinct channel
- Valence vectors can coexist with signed PE precision rather than being collapsed into mu/kappa

Possible affected components:
- Control plane
- Control plane signal map
- Precision control
- Sensory stream tags (valence)
- Trajectory selection and veto thresholds
