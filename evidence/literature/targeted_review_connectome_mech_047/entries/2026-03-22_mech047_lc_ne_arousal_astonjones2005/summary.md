# Literature Summary: 2026-03-22_mech047_lc_ne_arousal_astonjones2005

## Claims Tested

- `MECH-047`

## Source

- Aston-Jones G, Cohen JD (2005). *An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance*. Annual Review of Neuroscience.
- DOI: `10.1146/annurev.neuro.28.061604.135709`
- URL: `https://www.annualreviews.org/doi/10.1146/annurev.neuro.28.061604.135709`

## Source Wording

The locus coeruleus (LC) operates in two electrophysiologically distinct modes. In phasic mode, brief high-amplitude bursts of norepinephrine (NE) release are time-locked to task-relevant stimuli; this transiently boosts the gain (signal-to-noise ratio) of cortical responses, facilitating rapid exploitation of the currently committed task set. In tonic mode, elevated baseline NE is decoupled from specific stimulus events; this produces broadened response tuning across cortical targets, which promotes disengagement from the current task set and exploration of alternative behavioural options. The authors propose that shifts between phasic and tonic LC modes are driven by accumulated utility signals: as performance in the current task set decays, the utility of switching increases, eventually triggering a transition to tonic mode and subsequent task-set disengagement. Salient unexpected events can also directly trigger phasic LC bursts, producing brief windows of heightened responsiveness that can either reinforce the current mode or initiate a transition.

## REE Translation

MECH-047 (LC-NE as the arousal transition gate for mode-commitment hysteresis): The phasic/tonic LC distinction provides the direct biological substrate for the mode-transition gate in MECH-047. A phasic LC burst is the neural event that lowers the energy barrier between cognitive modes, permitting a transition that the hysteresis mechanism would otherwise resist. This maps onto high-salience events in REE (e.g., unexpected harm onset, task completion signal) that trigger the LC-phasic equivalent and allow the control plane to shift modes. Tonic LC tone sets the background switching probability -- high tonic NE is the neural correlate of a low hysteresis threshold, making the system easier to dislodge from the current mode. The exploit/explore distinction maps approximately to doing-mode (exploit: committed, focused) vs. ready-vigilance (explore: disengaged, sampling alternatives). The Usher-Cohen computational model in the paper is particularly relevant: it shows that phasic LC events can shift decision boundaries transiently, which is formally analogous to the threshold-crossing event in MECH-047's transition gate.

## Caveat

Aston-Jones and Cohen's framework is explicitly two-mode (exploit/explore). The three-mode REE taxonomy adds a default-mode (DMN simulation/planning) that is not addressed in this 2005 review, predating systematic integration of DMN into arousal-modulation accounts. The mapping from LC-NE to the doing <-> ready-vigilance transition is tightly supported; the claim that LC-NE gates entry into REE's default-mode is inferential and requires additional support (e.g., from studies of LC-NE suppression during wakeful rest or daydreaming). The adaptive gain model was developed primarily from prefrontal cortex recordings and frontal task paradigms; generalization to limbic and hippocampal circuits that underpin REE's E3 and default-mode is reasonable but not directly demonstrated in this paper.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.83`
