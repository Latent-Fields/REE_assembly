# Menon & Uddin 2010 — Salience Network Switching Model (SD-032c)

**Source:** Menon V, Uddin LQ. "Saliency, switching, attention and control: a network model of insula function." *Brain Structure and Function* 214(5-6):655–667. DOI: 10.1007/s00429-010-0262-0

## What the paper did

Menon and Uddin synthesise resting-state functional connectivity, task-based fMRI, and lesion data to propose a network-level model of anterior insula function centred on four mechanisms: (1) bottom-up detection of salient events; (2) switching between large-scale networks (task-positive central executive network vs default mode network) when a salient event is detected; (3) autonomic modulation of salience reactivity via anterior-posterior insula coordination; and (4) strong functional coupling with the anterior cingulate cortex for rapid motor-system access. The anterior insula and ACC together form a "salience network" whose core function is to segregate the most relevant among internal and extrapersonal stimuli and initiate appropriate control signals.

## Key findings relevant to SD-032c

The paper's four mechanisms map almost directly onto SD-032c's specification. Mechanism 1 (bottom-up salience detection) maps to SD-032c's input computation: AICAnalog detects when z_harm_a + drive_level crosses the switch threshold. Mechanism 2 (network switching) maps to SD-032c's output: fire a switch trigger to SalienceCoordinator (SD-032a), which arbitrates transition between operating modes. Mechanism 3 (autonomic modulation of salience reactivity via anterior-posterior insula) provides biological grounding for the drive_level dependence: the posterior insula (homeostatic/visceral processing) modulates the gain of AIC salience responses — exactly the structural drive-level → aic_salience gain that SD-032c implements. Mechanism 4 (AIC-ACC coupling for motor access) maps to SD-032c → SD-032a → action interruption pathway.

The network model also offers an important constraint: the salience network operates as a *binary switch* (network A or B), not a continuous gradient, which is consistent with SD-032c's threshold-gated architecture. Menon & Uddin cite evidence that insula activation predicts subsequent network state shifts, which is precisely the interrupt-trigger role SD-032c assigns to AICAnalog.

## Translation to SD-032c

SD-032c proposes that AICAnalog performs exactly the Menon & Uddin hub role: detect salience, fire interrupt trigger. The key addition in SD-032c relative to the Menon & Uddin model is the *drive-level dependence* — the same z_harm_a triggers different salience output depending on homeostatic state. Menon & Uddin's Mechanism 3 (posterior insula modulating AIC reactivity) provides anatomical precedent for this dependence, though it is not the paper's primary focus.

## Limitations and caveats

The Menon & Uddin model is built on resting-state connectivity and blocked-design fMRI; it describes time-averaged network states rather than moment-by-moment interrupt dynamics. The threshold character of the switch (yes/no mode change) is inferred from network state correlations, not from direct measurement of threshold-crossing events. The drive_level dependence in SD-032c (the primary testable specification) is supported by the anatomical framework but not directly measured in this paper. Transfer from large-scale resting-state network to single-module scalar computation is the key architectural gap.

## Confidence

0.74. Foundational network model that directly articulates the switch-trigger role SD-032c assigns to AICAnalog. Mapping fidelity high for the mode-switch mechanism; moderate for the drive-level gating. The resting-state-to-module transfer is the primary uncertainty.
