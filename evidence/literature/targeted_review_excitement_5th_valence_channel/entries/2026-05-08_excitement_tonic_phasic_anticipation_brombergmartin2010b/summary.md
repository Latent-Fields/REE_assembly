# Distinct tonic and phasic anticipatory activity in lateral habenula and dopamine neurons (Bromberg-Martin et al. 2010b)

## What the paper did

Bromberg-Martin, Matsumoto and Hikosaka (Neuron 2010, separate paper from the same year as the review above) recorded single-unit activity in macaque lateral habenula (LHb) and midbrain DA neurons while monkeys anticipated upcoming behavioural tasks of varying valence (rewarding vs punishing). The same neurons were tracked across both tonic (slow, building) and phasic (fast, event-locked) anticipatory components.

## Key findings relevant to the SD-014 question

Two anticipatory signals coexist within the same neurons. The tonic signal builds over the anticipation period, encodes the timing distribution of the upcoming task, and is reward-preferring — it discriminates rewarding from punishing tasks and correlates with classic phasic value coding. The phasic signal fires at task onset, responds similarly to rewarding and punishing tasks, and resembles motivational salience. The two signals are dissociable within a single neuron.

For the SD-014 question, this is direct neurophysiological evidence that anticipatory affect is at least two-channel. The tonic reward-preferring signal is the closest animal-physiology correlate of what humans report as excitement: a sustained, building, valence-positive anticipatory state at the cue. The phasic salience signal is a different construct — it is an alerting/orienting response, not a positive-affect representation.

## How this maps to REE

REE's current VALENCE_WANTING is a persistent directional attractor (z_goal in z_world space) — it encodes *where to go*, not *something positive is imminent*. The tonic anticipatory signal in Bromberg-Martin's macaque data is closer to the latter than the former. The build-up over the anticipation period before task onset is exactly what excitement-as-construct names phenomenologically: arousal-positive intensification as a cue approaches reward delivery.

This supports adding VALENCE_EXCITEMENT as a 5th channel that has temporal dynamics distinct from VALENCE_WANTING. Where VALENCE_WANTING is updated on contact with benefit (the persistent attractor's update rule), VALENCE_EXCITEMENT would be written during the anticipation phase — proportional to predicted-imminent-reward × cue-availability — with its own decay dynamics.

The phasic salience signal is more naturally captured by z_beta arousal (MECH-093 already modulates heartbeat rate on salient events) and by MECH-205's surprise-gated replay write. It does not need its own valence channel.

## Limitations and caveats

Macaque single-unit data; the translation to REE residue field is interpretive. The tonic firing pattern in a single neuron does not map 1:1 to a discrete write to a valence channel — that translation requires architectural choice. The paper does not include a behavioural / phenomenological readout (no "self-reported happiness" analog), so the construct anchor is purely neurophysiological.

## Confidence reasoning

0.80. Strong neurophysiology, direct support for multi-channel anticipatory affect, mapping moderate-high. Combined with Knutson 2001a/b (human fMRI, behavioural anchor for happiness) and Bromberg-Martin 2010a (review framing), the joint reading strongly supports the 5th-channel proposal.

Source: PubMed via PMID 20624598. [DOI](https://doi.org/10.1016/j.neuron.2010.06.016).
