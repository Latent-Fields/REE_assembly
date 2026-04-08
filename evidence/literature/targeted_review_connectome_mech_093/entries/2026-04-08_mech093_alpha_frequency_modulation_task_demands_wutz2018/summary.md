# Wutz, Melcher & Samaha (2018) -- Frequency modulation of neural oscillations according to visual task demands

## What the paper did

Wutz et al. used magnetoencephalography (MEG) in human participants to test whether the peak frequency of alpha-band (8--12 Hz) oscillations shifts with task demands while stimuli remain identical. Participants alternated between two tasks on the same visual displays: a missing-element task requiring temporal integration across frames, and an odd-element task requiring temporal segregation. Task difficulty was equated via individually calibrated interstimulus intervals. The critical question was whether the brain adjusts the *frequency* of alpha oscillations -- not merely their power -- to control the temporal resolution of perception.

## Key findings

Alpha peak frequency decreased during the integration task (where longer temporal windows are needed) and increased during the segregation task (where finer temporal resolution is beneficial). The effect was statistically robust (p < 0.03) and emerged 360 ms before stimulus onset, confirming it as an anticipatory, top-down modulation rather than a stimulus-driven response. Crucially, alpha *power* was not reliably modulated by task after correction for multiple comparisons, establishing a clean dissociation: the brain controlled frequency and power independently. The frequency modulation was specific to the alpha band -- delta, theta, beta, and gamma showed no task-dependent frequency shifts. Source localization placed the effect in bilateral early visual cortex and right inferior temporal gyrus. Correct trials showed earlier onset of frequency modulation than incorrect trials, linking the mechanism to behavioral success.

## Mapping to REE MECH-093

MECH-093 claims that z_beta (affective latent) modulates E3 heartbeat frequency -- how often the deliberative cycle updates -- as a mechanism distinct from precision-weighting (MECH-059), which modulates how much each update matters. The Wutz et al. finding provides direct biological proof-of-concept for this exact architectural distinction. Their data show that a neural oscillatory system can have its frequency and its amplitude/power controlled by separate mechanisms: frequency sets the temporal grain of processing, while power/gain reflects something else entirely (likely cortical excitability or signal strength). If E3's deliberative rhythm is paced by an oscillator analogous to occipital alpha, then it is biologically feasible for one control input (z_beta/arousal) to modulate E3's update rate while a separate input (precision signal) modulates E3's gain per update.

## Limitations and caveats

The mapping requires several inferential steps. First, the frequency modulation in this paper is driven by cognitive task instructions, not by arousal or affective state -- the z_beta pathway posited in MECH-093 is subcortical and arousal-driven, not a deliberate top-down instruction. Second, the brain region involved is occipital cortex, not the prefrontal executive circuits where E3 would plausibly operate. Third, the effect size at scalp level was modest (approximately 0.04 Hz), though source-level estimates were an order of magnitude larger. The paper establishes that frequency modulation is a biologically available mechanism and that it is dissociable from gain -- but it does not demonstrate that arousal specifically drives this mechanism in executive/deliberative circuits.

## Confidence reasoning

Source quality is high (PNAS, rigorous MEG design, clean dissociation). Mapping fidelity is moderate: the principle transfers (frequency != gain), but the specific claim (arousal drives frequency in executive circuits) is not directly tested. This paper supports the *feasibility* of MECH-093's architectural distinction more than it supports the specific arousal-to-frequency pathway. Confidence: 0.62 -- the dissociation is real and important, but the domain gap (visual perception vs affective deliberation rate) limits directness.
