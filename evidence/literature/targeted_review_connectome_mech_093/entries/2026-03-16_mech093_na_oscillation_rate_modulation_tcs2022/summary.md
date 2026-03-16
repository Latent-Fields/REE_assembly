# Literature Summary: 2026-03-16_mech093_na_oscillation_rate_modulation_tcs2022

## Claims Tested

- `MECH-093`

## Source

- Dahl MJ, Mather M, Werkle-Bergner M (2022). *Noradrenergic modulation of rhythmic neural activity shapes selective attention*. Trends in Cognitive Sciences.
- DOI: `10.1016/j.tics.2021.10.009`
- URL: `https://www.sciencedirect.com/science/article/abs/pii/S1364661321002643`

## Source Wording

Locus coeruleus norepinephrine (LC-NE) activity modulates the frequency and synchrony of thalamocortical oscillations. Elevated NE shifts thalamic neurons from slow burst-firing mode (low arousal → slower, less informative oscillation) to tonic single-spike mode (high arousal → faster, information-transmitting oscillation). This upregulates the dominant cortical oscillation frequency and increases the rate of reliable information transmission. NE-mediated oscillation frequency modulation is distinct from, but interacts with, gain-control effects on signal amplitude.

## REE Translation

MECH-093 (z_beta modulates E3 heartbeat frequency): z_beta (REE affective latent, mapping primarily to the LC-NE arousal axis) modulates E3 heartbeat *rate*, not only E3 prediction error *precision-weighting* (MECH-059). High z_beta → NE-equivalent arousal signal → MD thalamic pacemaker shifts toward faster update rate → finer temporal resolution of harm attribution. Low z_beta → slower, energy-efficient E3 update regime → more stable policy behaviour. This establishes z_beta as a *rate-control* signal (MECH-093) distinct from its *gain-control* role (MECH-059): two separable contributions to E3 dynamics from the same affective latent.

## Caveat

NE modulation operates across multiple oscillatory bands and brain systems simultaneously (alpha, theta, gamma); the specific effect on a deliberative E3-rate heartbeat is one subset of a broader arousal effect. The rate-control vs gain-control distinction (MECH-093 vs MECH-059) is a REE architectural framing not directly tested in this literature — the literature supports both effects of NE but does not separate them in a heartbeat-gated planning loop. V3 experimental design (MECH-093 test) will need to explicitly dissociate rate changes from precision changes.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.72`
