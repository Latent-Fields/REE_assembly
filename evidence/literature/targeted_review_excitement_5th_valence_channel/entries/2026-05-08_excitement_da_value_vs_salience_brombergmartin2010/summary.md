# Dopamine in motivational control: rewarding, aversive, and alerting (Bromberg-Martin et al. 2010)

## What the paper did

Bromberg-Martin, Matsumoto and Hikosaka (Neuron 2010) reviewed primate and rodent electrophysiology of midbrain dopamine neurons and proposed a typology: DA neurons are not homogeneous reward-prediction-error encoders; they split into at least two populations with distinct response profiles, distinct projection targets, and distinct functional roles. A third "alerting" signal augments both populations in response to salient sensory cues.

## Key findings relevant to the SD-014 question

The architectural distinction the paper introduces is critical for thinking about excitement: motivational VALUE vs motivational SALIENCE. Value-coding DA neurons respond preferentially to reward over punishment, encode expected value, and project to circuits supporting reward-seeking and value learning. Salience-coding DA neurons respond to both rewarding AND aversive salient cues, encode "something important is happening," and project to circuits supporting orienting, general motivation, and cognition.

This poses a real architectural alternative to the VALENCE_EXCITEMENT proposal. There are two readings of "excitement":

- **Value-coded reading**: excitement is a positive-valence-selective anticipatory signal. This is what Knutson 2001a's NAcc-anticipation looks like — it does NOT respond to punishment anticipation (medial caudate does instead). Under this reading, excitement is its own value channel and warrants VALENCE_EXCITEMENT.
- **Salience-coded reading**: excitement is the alerting/orienting signal that says "imminent significant event," with valence determined separately. Under this reading, REE's z_beta arousal modulator could in principle carry the excitement function, paired with VALENCE_WANTING for the directional sign.

The paper itself doesn't arbitrate. It supports the principle that anticipatory affect is heterogeneous (not a single signal) — which favours adding new channels — but it also gives the architectural alternative that REE might not need a new channel if z_beta is broad enough.

## How this maps to REE

The honest reading is that this paper *constrains* the SD-014 amendment proposal but doesn't refute it. The Knutson MID literature is more decisive than this review: NAcc-anticipation is positive-valence-selective, not pure salience. So the *human fMRI* excitement signature is value-coded, and a value-coded 5th channel in SD-014 is the more faithful architectural choice. But the value-vs-salience taxonomy here is a useful caution: REE should be careful about whether VALENCE_EXCITEMENT writes for *all* salient cues (salience) or only for *positive* ones (value). The lit favours the latter.

## Limitations and caveats

This is a review of primate / rodent single-unit data; the spatial resolution and the construct alignment to human-MID fMRI BOLD signals is imperfect. NAcc BOLD likely integrates both DA populations spatially, so the value-vs-salience cleanness at the single-unit level may not translate to fMRI. The taxonomy is theoretically influential but has been refined in subsequent work (e.g. Schultz 2016, Bromberg-Martin 2024).

## Confidence reasoning

0.74. High source quality (canonical review in Neuron) but mixed direction for our question — supports the heterogeneity-of-anticipatory-affect principle, partially weakens the strong-form proposal that excitement needs its own channel rather than being subsumed by salience-modulators. The mapping to REE is more architectural than empirical.

Source: PubMed via PMID 21144997. [DOI](https://doi.org/10.1016/j.neuron.2010.11.022).
