# Ma, Wang & Zuo 2026 — Optogenetic aIC→mPFC Mode Switching (SD-032c)

**Source:** Ma S, Wang KH, Zuo Y. "Targeting insulo-frontal pathway to reduce stress-evoked cognitive rigidity." *bioRxiv* preprint. DOI: 10.64898/2026.02.12.705479

## What the paper did

Ma et al. used attentional set-shifting tasks (AST) in mice to characterise aIC neurons projecting to medial PFC (mPFC) during adaptive vs maladaptive behavioural modes. Using two-photon calcium imaging, they found that aIC→mPFC projection neurons show heightened activity specifically following *incorrect* (salient negative) trials but not correct trials. This elevated activity persists into subsequent trials and enhances mPFC outcome-dependent updating — neural activity patterns converge across trials, a proxy for successful mode revision. Optogenetic suppression of aIC→mPFC projections during the pre-decision phase disrupted mPFC updating and impaired AST performance. Critically, stress disrupted the outcome-dependence of aIC activity (activity became non-specific), which produced cognitive rigidity. Selectively reinstating aIC→mPFC activity after incorrect trials via optogenetics restored cognitive flexibility in stressed animals.

## Key findings relevant to SD-032c

This is the most direct causal evidence available for SD-032c's urgency-interrupt architecture. Three findings are particularly relevant. First, aIC fires selectively after salient negative outcomes (not all outcomes), establishing that AIC is an event-triggered salience detector rather than a continuous monitor — consistent with SD-032c's threshold-gated architecture. Second, the signal propagates to mPFC and triggers mode revision (increased updating, convergence of activity patterns) — directly analogous to SD-032c's switch trigger to SalienceCoordinator. Third, stress disrupts this gate (aIC becomes stimulus-nonspecific), producing stuck modes — a failure signature that maps onto SD-032c's hypothesis that insufficient drive_level context collapses the salience gate.

## Translation to SD-032c

SD-032c's AICAnalog computes salience = f(z_harm_a, drive_level) and fires a switch trigger when salience > threshold. Ma et al. provide optogenetic causal evidence that aIC specifically detects salient negative events (criterion 1) and fires a signal to frontal cortex that triggers behavioural mode revision (criterion 2). The stress-disruption finding is also relevant: stress in this experiment effectively decouples outcome salience from aIC signal specificity, which is the mechanistic analogue of SD-032c losing its drive_level gain (aic_drive_protect_weight = 0 condition).

## Limitations and caveats

This is a preprint (2026) and has not been peer-reviewed. The task is cognitive set-shifting, not harm-salience urgency or metabolic drive modulation — the specificity of aIC to harm-valenced events vs general task errors is not established. The drive_level dependence in SD-032c (aic_drive_protect_weight effect on harm_s_gain) is not tested in this paper. The mPFC target in Ma et al. is the rat/mouse prelimbic/infralimbic axis, which in REE maps to PFC-like planning regions rather than the SalienceCoordinator specifically.

## Confidence

0.65. Good optogenetic causal evidence for the aIC→frontal interrupt-trigger architecture. Confidence tempered by preprint status, cognitive-flexibility task (not harm urgency), and absence of drive-level modulation test.
