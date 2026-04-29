# Suh et al. 2019 -- Short NREM/REM cycle architecture predicts cognitive decline (KLOSCAD)

[DOI: 10.3233/JAD-190399](https://doi.org/10.3233/JAD-190399)

## What they did

A subset of 235 cognitively normal community-dwelling Korean elderly (mean age 68, 60% female) from the Korean Longitudinal Study on Cognitive Aging and Dementia (KLOSCAD) underwent baseline overnight polysomnography. After 4 years of follow-up, 14 (5.9%) had converted to MCI or dementia. The novel methodological contribution is the cycle-level decomposition: rather than treating sleep architecture as stage-percentages of the night, the authors defined an NREM/REM cycle as a sequence of NREM and REM uninterrupted by waking longer than 2 minutes, and measured architecture metrics within each cycle (cycle duration, REM duration per cycle, NREM duration per cycle, etc.). Logistic regression then asked which of these cycle-level metrics predicted incident MCI/dementia.

## Key findings relevant to Q-032

Two cycle-level metrics emerged as predictive: short average cycle length (OR 0.97 per minute, 95% CI 0.94-0.99, p=0.02) and short average REM duration per cycle (OR 0.87 per minute, 95% CI 0.76-0.98, p=0.03). Both effects survived joint modelling, meaning the REM-per-cycle signal added information beyond cycle length itself. The authors are upfront that this is exploratory and call out the small case count.

## How this maps to REE

Q-032 asks whether PSG architecture metrics can serve as pharmacodynamic biomarkers. The interesting feature of Suh 2019 is that it dissociates total REM% (a stage-percentage) from REM-per-cycle (a coordination metric). The REE pipeline-phase architecture (MECH-120 through MECH-123) treats the alternation between NREM phases (1, 2, 3) and REM phase (4) as functionally constitutive of the model-update pipeline -- it is the cyclic coordination, not the aggregate time spent in each phase, that the framework predicts as load-bearing. A drug that preserves total REM% while degrading the cycle-level alternation should look healthy on a stage-percentage report and unhealthy on a cycle-level report. Suh provides the first-pass evidence that the cycle-level read carries independent predictive signal -- which means a Q-032 PD biomarker designed at the architecture level rather than the stage-percentage level is empirically defensible.

## Limitations and caveats

n=14 incident cases is small. The OR confidence intervals at the per-minute scale are wide and a chance finding from exploratory multi-metric screening cannot be ruled out. The authors did not apply Bonferroni correction across the architecture metrics tested. Single-night baseline PSG cannot distinguish someone whose cycle architecture has always been compressed from someone whose cycles compressed recently. Replication in larger cohorts -- Sleep Heart Health Study, MrOS, Framingham, ARIC, NHANES -- is not yet available, and any Q-032 PD-biomarker proposal would need replication before regulatory acceptance. Generalisability from Korean elderly to broader populations is also a transfer step, though there is no obvious reason cycle architecture should be culturally specific.

## Confidence reasoning

I rate this 0.62. Source quality is moderate -- J Alzheimers Dis is reputable but the exploratory framing and small n=14 cases are real precision constraints. Mapping fidelity is good because cycle-level architecture maps cleanly onto the REE pipeline-coordination framing, and the dissociation from stage-percentage metrics is exactly the kind of nuance Q-032 needs. Transfer risk is moderate-to-high because (i) replication is not yet available and (ii) the Korean cohort may differ in cycle architecture norms from Western cohorts. The right reading is "Suh provides preliminary evidence that cycle-level architecture is the right level of description for a Q-032 biomarker, but replication is needed before this can stand alone."
