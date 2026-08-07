# Adolphs, Denburg & Tranel (2001) — amygdala, gist vs detail

**Claim tested:** MECH-074b (BLA analogue applies a *content-selective per-trace* retrieval weight vector — explicitly not a scalar retrieval gain).
**Direction:** supports · **Confidence:** 0.75

## What the paper did

Twenty patients with unilateral amygdala damage, one rare patient with bilateral amygdala damage, and two control groups (15 brain-damaged, 47 healthy) were tested on long-term declarative memory for the *gist* versus the *visual detail* of aversive and neutral scenes. The design lets the effect of emotional content be read off separately for the two grain sizes of memory.

## Key finding relevant to the claim

Bilateral — but not unilateral — amygdala damage produced **poorer memory for gist but *superior* memory for visual detail**. The two directions move oppositely. The authors read this as the amygdala "filtering the encoding of relevant information from stimuli that signal threat or danger." This is exactly the behavioural signature MECH-074b's mechanism is designed to reproduce and, importantly, the one a *scalar* retrieval gain cannot. A single multiplicative gain applied to every trace raises central and peripheral recall together; it can never make peripheral/detail memory go *up* when the modulator is removed. Only a per-item weighting (high weight to central/threat-associated traces, relatively suppressed weight to peripheral ones) yields an opposite-signed change in detail memory. So the paper is direct human evidence for the *content-selective, vector-not-scalar* form of the BLA→hippocampus modulation over the named scalar-gain failure signature.

## Mapping to REE and its limits

The clean part of the mapping is the falsification of scalar gain: MECH-074b insists w_i = 1 + α·arousal_tag_i be *per-trace*, and this dissociation is the canonical reason. The unclean part is *locus*. Adolphs et al. explicitly describe an **encoding-time filter**, whereas MECH-074b places the weight at **retrieval** and further asserts it is non-transient — growing with trace age from 20 minutes to a week. This study cannot separate an encoding-selection account from a retrieval-weighting account; it constrains *that* the modulation is content-selective, not *where* in the encode/retrieve cycle the selection happens. That is why `mapping_fidelity` is 0.7 rather than higher.

## Caveats and disconfirming texture

The bilateral dissociation — the only condition that showed the effect — rests on a single rare patient, and unilateral damage showed nothing. So the human evidence for the *strength* of the effect is anchored by n=1, and the direction, though canonical and widely replicated conceptually, should not be over-weighted quantitatively. Combined with the locus ambiguity above, this is strong but not decisive support: it validates the design constraint (selective, not scalar) while leaving MECH-074b's specific retrieval-time, age-growing prediction untested by this source.

According to PubMed. Source: Adolphs R, Denburg NL, Tranel D (2001), *Behavioral Neuroscience* 115(5):983-92. [DOI](https://doi.org/10.1037//0735-7044.115.5.983)
