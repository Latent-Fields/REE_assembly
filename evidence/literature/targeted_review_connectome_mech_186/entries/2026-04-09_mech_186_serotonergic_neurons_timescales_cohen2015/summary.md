# Summary: Cohen, Amoroso & Uchida (2015) — Serotonergic neurons signal reward and punishment on multiple timescales

**Claim tested:** MECH-186 (valence_wanting_floor — tonic serotonergic floor on VALENCE_WANTING)  
**Evidence direction:** supports | **Confidence:** 0.68

## What the paper did

Cohen, Amoroso, and Uchida used channelrhodopsin-2 to optogenetically photoidentify dorsal raphe nucleus (DRN) serotonergic neurons in behaving mice during a Pavlovian reward/punishment task structured in alternating blocks. This photoidentification method is important: prior DRN recording studies relied on waveform characteristics to identify serotonergic neurons, a notoriously unreliable heuristic. Here, neurons were confirmed serotonergic by their response to brief optical stimulation. The task allowed the authors to ask whether identified 5-HT neurons carry phasic signals (locked to individual trial events), tonic signals (tracking block-level context over minutes), or both.

## Key findings relevant to MECH-186

The central result is a clean dissociation: a large fraction of DRN serotonergic neurons showed sustained, block-level modulation of their tonic firing rates — elevated in reward-dominant blocks, depressed in punishment-dominant blocks — over the course of tens of seconds to minutes. Critically, dopaminergic (DA) neurons recorded in the same paradigm did not show this block-level tonic modulation; DA responses were phasic and trial-locked. This double dissociation — 5-HT carries the slow environmental context signal, DA does not — is the empirical substrate MECH-186 requires.

## Translation to REE

MECH-186 posits a tonic serotonergic floor on VALENCE_WANTING in the residue field: when chronic harm exposure depletes motivational salience, tonic 5-HT maintains a non-zero baseline that prevents complete goal latent collapse. The Cohen et al. finding directly instantiates this signal: the sustained DRN firing rate shift across environmental context is precisely the kind of slowly integrating, environment-sensitive signal that could maintain terrain legibility when phasic incentive salience events are sparse. The DA/5-HT dissociation provides additional mechanistic support — the VALENCE_WANTING floor is a distinct channel from phasic dopaminergic incentive salience (MECH-187), not merely a scaled version of the same signal.

## Limitations and caveats

The experiment uses discrete alternating reward/punishment blocks, not continuous chronic harm-dominant environments. Mapping from block-level context to MECH-186's sustained terrain suppression requires extrapolation — the REE-specific scenario involves accumulated harm over many episodes, not a within-session block flip. The study is also in mice; human DRN serotonergic recording at the photoidentified neuron level is not currently feasible. A minority subset of 5-HT neurons showed phasic excitation to reward-predicting cues, which complicates the clean tonic/phasic separation. None of this is a refutation, but the mapping carries a meaningful inferential step.

## Confidence reasoning

Source quality is high (0.88): eLife, optogenetic photoidentification, clear behavioural design, strong negative control (DA comparison). Mapping fidelity moderate (0.70): block context is not identical to chronic harm terrain, and the REE translation requires two inferential steps. Transfer risk moderate (0.42): rodent DRN to MECH-186's computational floor is a plausible but not demonstrated bridge. Aggregate confidence: 0.68.
