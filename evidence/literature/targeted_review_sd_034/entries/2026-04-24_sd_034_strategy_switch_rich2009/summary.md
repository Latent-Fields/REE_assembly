# Rich & Shapiro 2009 -- mPFC strategy-switch selective coding

## Source
Rich EL, Shapiro M. Rat prefrontal cortical neurons selectively code strategy switches. J Neurosci 29(22):7208-7219. DOI: 10.1523/JNEUROSCI.6068-08.2009

## Finding
Medial prefrontal neurons (prelimbic PL and infralimbic IL) selectively fire during strategy switches in a plus-maze task. The switch signal is decoupled from motor behaviour: rats executing identical actions but switching from hippocampus-dependent to caudate-dependent strategy show distinct neural activity, whereas rats learning new contingencies within the same strategy do not. PL dynamics anticipate learning performance; IL dynamics lag -- consistent with PL initiating and IL establishing new strategies.

## Why it maps to SD-034
SD-034 posits a closure operator that detects satisfaction of a committed rule_state, releases the commitment latch (MECH-090), and imposes a temporary No-Go on re-entering the just-completed rule. Any such operator needs a circuit that explicitly signals rule / cognitive-mode transitions independently of the motor plan. The Rich & Shapiro PL / IL switch-coding population is the closest biological analog: a dedicated neural signal that fires specifically at mode transitions and is silent during within-mode learning.

The PL-then-IL temporal profile is also suggestive: a two-stage closure (first release, then install the No-Go) would predict a similar initiator-then-establisher signal in the substrate.

## Confidence: 0.70 (supports)
- source_quality 0.80 (J Neurosci, clean paradigm, lab-replicated phenomenon)
- mapping_fidelity 0.65 (substrate for mode-transition signals exists; specific endogenous-completion readout not directly demonstrated)
- transfer_risk 0.40 (rodent medial PFC maps onto a slice of the SD-033a PFC analog; SD-034 is region-agnostic)

## Key limitations
- Strategy switches in the paradigm are driven by external contingency changes. SD-034 requires endogenous rule-satisfaction detection; no direct evidence that the switch-coding cells fire on internal completion.
- Correlational single-unit recording, no lesion or causal manipulation demonstrating PL/IL cells are required for the switch.
- Two-region temporal split (PL leads, IL lags) may or may not map to SD-034's single-step closure token.

## Failure signatures
- If PL/IL switch-signalling is downstream of an upstream closure-generator, SD-034 is looking at the wrong circuit level.
- If closure in REE needs a fast single-shot signal rather than a PL-then-IL sequence, this substrate is the wrong temporal profile.
- Strategy-switch paradigm is externally cued; endogenously generated rule completion may recruit a different subpopulation.
