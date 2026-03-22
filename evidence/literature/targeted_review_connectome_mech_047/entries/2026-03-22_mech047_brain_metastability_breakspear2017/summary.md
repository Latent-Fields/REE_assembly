# Literature Summary: 2026-03-22_mech047_brain_metastability_breakspear2017

## Claims Tested

- `MECH-047`

## Source

- Breakspear M (2017). *Dynamic models of large-scale brain activity*. Nature Neuroscience.
- DOI: `10.1038/nn.4497`
- URL: `https://www.nature.com/articles/nn.4497`

## Source Wording

Large-scale brain activity is characterised by metastability: the system does not converge to a single fixed attractor but instead transiently visits a sequence of quasi-stable states, dwelling within each for characteristic durations before spontaneously transitioning. Biophysical network models constrained by structural connectome data reproduce these dwell-time distributions and show that transitions are probabilistic rather than instantaneous. The system is poised near a bifurcation point where multiple attractors coexist; perturbations (arousal shifts, sensory events) tilt the energy landscape and alter transition rates. This history-dependence -- the fact that the probability of leaving a state depends on how long the system has already dwelled there -- is the hallmark of hysteretic attractor dynamics.

## REE Translation

MECH-047 (control plane mode-commitment hysteresis): The neural metastability documented in Breakspear (2017) provides the biological substrate for the claim that REE cognitive modes are not freely switchable. Once the control plane enters a mode (doing, ready-vigilance, or default-mode DMN), it dwells in that basin according to an energy-landscape logic: switching requires sufficient activation energy, modelled in REE as LC-NE arousal crossing a threshold. The dwell-time statistics directly motivate the hysteresis parameter in the mode-transition gate -- longer dwell times imply higher switching cost, which is the computational signature MECH-047 formalises. The energy-barrier metaphor also explains why abrupt interruptions (high-salience LC burst) can force premature transitions: the perturbation temporarily flattens the barrier.

## Caveat

Breakspear's review characterises metastability as an emergent property of whole-brain network dynamics, primarily in resting-state and lightly task-engaged contexts. The three REE modes (doing, ready-vigilance, default-mode) are coarser-grained than the empirically observed attractor repertoire and do not correspond to specific attractor configurations identified in the review. MECH-047 implements hysteresis as an explicit discrete gate, which is a stronger and more modular claim than the continuous energy-landscape account in the review supports. The biological evidence is therefore analogical support rather than direct mechanistic confirmation.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
