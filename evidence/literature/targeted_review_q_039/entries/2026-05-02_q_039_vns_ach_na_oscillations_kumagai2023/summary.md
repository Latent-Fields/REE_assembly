# Kumagai et al. 2023 -- VNS dissociates ACh and NA effects on cortical oscillations

## What the paper did

Kumagai and colleagues (Jichi Medical University and University of Tokyo) used vagus nerve stimulation (VNS) as a tool to interrogate the cholinergic and noradrenergic systems' separate contributions to cortical oscillatory activity. They recorded electrocorticography from auditory cortex of 34 anaesthetised Wistar rats while presenting click stimuli, with and without VNS. The critical experimental manipulation was local administration of cholinergic versus noradrenergic antagonists into auditory cortex, which let them ask which neuromodulatory system was responsible for which frequency-band effects. This is a textbook double-dissociation design.

## Key findings

VNS increased auditory-evoked cortical potentials. In the time-frequency analyses, VNS produced three distinct effects: it **increased** evoked gamma power, it **increased** evoked beta power, and it **decreased** theta power. The pharmacological dissociation was the cleanest part: cholinergic antagonists in cortex selectively blocked the VNS-induced gamma and beta increase, leaving the theta decrease intact. Noradrenergic antagonists did the opposite -- they selectively blocked the VNS-induced theta decrease, leaving the gamma/beta increase intact. ACh and NA each modulate different frequency bands of cortical oscillation, and in the same preparation under the same stimulation protocol.

The authors' architectural reading: VNS strengthens the feedforward (FF) pathway through the cholinergic system (which manifests in gamma and beta) and attenuates the feedback (FB) pathway through the noradrenergic system (which manifests in theta). Frequency-band-specific cortical gain modulation through distinct neuromodulatory systems.

## How this maps to REE

Q-039 asks which neuromodulators implement the control-plane parameters of REE's temporal coupling layer (TCL), and specifically whether acetylcholine and noradrenaline play distinct roles in regulating the temporal integration window vs phase alignment sensitivity. Kumagai et al. provide the cleanest pharmacological dissociation on the table: ACh and NA each act on different frequency bands in the same preparation under the same experimental protocol.

For REE, this maps onto the architectural prediction that TCL has *separate* parameters that *separate* neuromodulators control. Specifically: tau_E2-like integration-window parameters are ACh-modulated (working through gamma and beta, the bands typically associated with feedforward cortical timing and integration); phase-alignment / reset parameters are NA-modulated (working through theta, the band typically associated with longer-timescale phase organisation). This pairs naturally with the Fan et al. 2020 result on cholinergic L1 gating of temporal filtering and the Xiang et al. 2023 result on LC noradrenergic phase-locking to infra-slow rhythms. Together the three papers sketch a division of labour: ACh sets the temporal-filter window in the local circuit; NA sets the slower phase-alignment / reset signal that determines when filtering should re-zero.

This is the kind of evidence that would let Q-039 close in favour of ACh and NA acting as distinct control-plane regulators in TCL (rather than jointly controlling a single window parameter or one being a slave to the other). It does not yet address dopamine's role (the third part of Q-039 about beta_j / D_V control), but it cleanly resolves the ACh-vs-NA part.

## Limitations and caveats

The mapping from frequency-band-specific neuromodulation to REE's TCL parameter assignment depends on a hypothesis that TCL parameters correspond to specific frequency bands. That hypothesis is implicit in much of the predictive-processing literature but has not been empirically pinned down for REE specifically. If TCL's parameters do not cleanly correspond to gamma/beta vs theta, the dissociation supports the general 'ACh and NA do different things' claim without supporting the specific REE parameter assignment.

The experimental setting also matters. Anaesthetised rat auditory cortex is two qualifiers away from awake human associative cortex / REE's E3. Anaesthesia dramatically alters baseline cortical state and modulator response; sensory cortex has its own dynamics that may not generalise to associative areas. The double-dissociation logic is robust to these qualifiers (the dissociation itself is replicable in cleaner preparations) but the specific frequency-band mapping is more fragile.

## Confidence reasoning

I am holding this at 0.80 -- the highest of the Q-039 anchor papers because of the experimental design quality. Double-dissociation through frequency-specific antagonist effects in the same animals is exactly the kind of evidence Q-039 needs. Source quality is good (rigorous design, n=34, established peer-reviewed journal). Mapping fidelity is strong because the paper directly addresses Q-039's central question. Transfer risk is moderate due to the anaesthesia and sensory-cortex qualifiers, plus the dependence on a frequency-band hypothesis for TCL that is not yet pinned down.

Source: According to PubMed, [DOI: 10.1016/j.brs.2023.09.019](https://doi.org/10.1016/j.brs.2023.09.019).
