# Dragoi & Tonegawa (2011) — "Preplay of future place cell sequences by hippocampal cellular assemblies"

**Nature** 469:397–401. [DOI](https://doi.org/10.1038/nature09633). PMID 21179088.

*(According to PubMed.)*

## What the paper does

Dragoi and Tonegawa ask whether the hippocampus can generate sequence events that correspond not to past experience but to *future* experience — that is, whether place cells can fire in a temporally-ordered pattern matching a novel environment *before* the animal has entered that environment.

They recorded mouse CA1 ensembles during rest and sleep preceding a novel linear-track experience, and applied Bayesian decoding to the sequence events observed. They found that temporal sequences matching the upcoming novel track occurred at significantly above-chance rates during that pre-exposure period. These preplay events were distinguishable from and co-occurred with replay of familiar experiences. The interpretation: the hippocampus holds a repertoire of preconfigured temporal sequences, and a subset of that repertoire is recruited to represent novel experiences as they happen.

This is a substantial claim about how the hippocampus organises its expressive capacity. Replay (rehearsing the past) and preplay (expressing pre-configured sequences that will match future experience) are two modes of sequence generation, both active, and not equivalent.

## Findings relevant to MECH-269

MECH-269 predicts two channels of hippocampal rollout generation: an anchored channel that seeds from currently-aligned high-V_s states (Pfeiffer-Foster evidence), and a probe channel that inverts the gate and seeds from non-aligned states for curiosity-driven exploration. The probe channel is the harder half to defend empirically — if hippocampal sequence events were exclusively reactivations of past experience, MECH-269's probe prediction would have no biological anchor.

Dragoi and Tonegawa provide that anchor. Preplay is structurally what the probe channel needs to be: sequence events that do not correspond to past experience, but that exist in repertoire and get recruited to represent novel content. The two-channel decomposition MECH-269 proposes — anchored (current-V_s-gated) and probe (inverted gate, curiosity-driven) — maps onto the replay / preplay distinction Dragoi and Tonegawa operationalise, though not identically.

The architectural point that matters: the hippocampus can generate candidate trajectories that are not grounded in recent experience. MECH-269 needs this capacity for the probe channel to exist at all. Preplay is its biological footing.

## How it translates to REE

For V3, this means the hippocampal proposer's probe channel should be implementable as a separate sampling mode that draws from a preconfigured trajectory repertoire rather than from the anchored-to-current state. The Dragoi-Tonegawa picture — a repertoire of sequences exists, and gets selectively recruited — is the substrate-level pattern the probe channel should mimic.

MECH-094's hypothesis tag is relevant here too. If the hypothesis tag strengthens during probe-channel recruitment (so downstream consumers know this is not grounded content), then probe rollouts can be generated freely without corrupting the anchored writes. The Dragoi-Tonegawa result is consistent with this: preplay sequences do not appear to contaminate the animal's subsequent behaviour in the way a writebackable anchored trajectory would.

## Limitations and caveats

The preplay phenomenon as reported is narrower than MECH-269's probe channel. Dragoi and Tonegawa demonstrate that preconfigured sequences exist and get recruited when the animal encounters novel experience. MECH-269 requires that the hippocampus can generate probe-tagged rollouts in the *absence* of a novel stimulus, as a curiosity-driven counterfactual. The closer mapping of preplay to MECH-269's probe channel requires extrapolation: the mechanism that recruits preconfigured sequences on exposure to novelty is the same mechanism (under MECH-269) that can recruit them for offline curiosity-driven exploration. That identification is plausible but not established.

Methodological: the preplay phenomenon has been debated in the literature. Subsequent work has both replicated and criticised it, with the strongest criticisms concerning statistical thresholds and the reliability of the "future-matching" decoding. The core claim that preconfigured sequences exist in the resting hippocampus is robust; the claim that they match specific future environments with high fidelity is more contested. For MECH-269's probe channel, the weaker claim is sufficient — a repertoire of non-anchored sequences is all the probe channel needs.

Rodent spatial-only paradigm. Per-stream generalisation is not tested.

## Confidence reasoning

Source quality is high — Nature paper, Tonegawa lab, Bayesian sequence decoding with appropriate shuffling controls. Mapping fidelity is moderate: preplay is structurally the probe-channel phenomenon MECH-269 requires, but MECH-269's specific functional role for preplay-like activity (curiosity-driven probe, non-anchored seeding for exploratory value) is an extrapolation from Dragoi-Tonegawa's "available for recruitment on novel exposure" framing. Transfer risk moderate — rodent spatial preplay does not directly test the per-stream architecture. Net confidence 0.72.
