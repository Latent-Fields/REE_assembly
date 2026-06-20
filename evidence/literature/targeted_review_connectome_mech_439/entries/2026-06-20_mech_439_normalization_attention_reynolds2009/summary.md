# Reynolds & Heeger (2009) — The normalization model of attention

**Source:** Reynolds, J. H., Heeger, D. J. (2009). *Neuron* 61(2):168-185. [DOI 10.1016/j.neuron.2009.01.002](https://doi.org/10.1016/j.neuron.2009.01.002) · PMID 19186161. (According to PubMed.)

**Claim under test:** MECH-439 — and specifically *where* a modulatory channel has to act to gain leverage over a normalized competition; supporting grounding for **MECH-448**.

## What the paper does

Reynolds & Heeger show that a single divisive-normalization circuit reproduces the *whole* zoo of attentional modulation — response-gain changes, contrast-gain changes, and the intermediate forms — that had previously looked like evidence for competing theories. The trick is the architecture: attention enters as an **attention field** that scales the **stimulus drive** (the numerator) point-by-point, and that scaled drive is then divisively normalized by a pooled **suppressive drive** (the denominator). Which empirical signature you get — response-gain vs contrast-gain — falls out of the *size of the attention field relative to the stimulus* and the spread of the normalization pool. One mechanism, regime-dependent outputs. The model is fit to the macaque and human attention literature.

The two structural facts that matter for REE: attention gains its leverage **by entering the normalization** (scaling the drive *before* the pooled divisive step), and the modulation works by changing **gain**, leaving the computation **order-preserving**.

## Why it belongs in this pull

The Carandini & Heeger anchor and the Louie value entry establish *that* F should be renormalized against the field. Reynolds & Heeger answers the next question the autopsy raises: **where does a modulatory channel have to act to convert?** MECH-439's diagnosis is that REE's modulatory / within-class / rule-bias channels have authority at the E3 accumulator but stay floor-locked — they cannot move the committed action while F dominates (the 445h / 485h / 654g signature: the bias reaches the accumulator, committed entropy does not budge). This paper gives that floor-lock a mechanistic name. In the brain, a control signal does **not** gain leverage by being *added on top of* the winning channel's raw response; it gains leverage by *modulating the normalization itself* — scaling the drive at the numerator, or reweighting the suppressive pool. REE's additive modulatory channels, sitting on top of an un-normalized, F-dominated score, are wired in the architecturally wrong place. For them to convert, the modulation has to act *on the normalization of F* — numerator gain or normalization-pool weighting — which is the mechanistic content of Reading-2 *beyond* the bare "renormalize F" statement.

## The load-bearing divergences

**Order-preservation, again.** The model reweights the competition by gain; it does not strip the dominant channel from the output. So, consistent with the other two entries, Reynolds & Heeger grounds the *rank-preserving, gain-on-the-normalization* lever and does **not** license REE's stronger asymmetric "F removed from the argmin." This is now the third independent normalization result pointing the same way: the canonical computation is rank-preserving everywhere, and the argmin-removing version of REE's lever is a different, non-canonical build.

**The single-mechanism reconciliation is double-edged.** The elegance of the model — one normalization yielding response-gain *or* contrast-gain depending on attention-field-vs-stimulus size — is also a warning. Transferred to REE, it says the *same* modulatory channel can have large or near-zero leverage on the committed action depending on the score-distribution regime: how concentrated F is, how many near-ties exist, how the pool is scoped. Modulatory leverage is **regime-contingent, not a fixed property**. MECH-448's build cannot assume a modulatory channel that gains leverage in one regime keeps it in another; the gain/leverage relationship is a surface to map, not a constant to set once.

**Domain.** This is a sensory-attention model. Its application to a value/action selector rests on the canonical-computation generality claim (Carandini & Heeger), not on direct value-domain data — that same-domain weight is carried by the Louie entry. This entry's contribution is the *structural* argument about **where** modulation must enter, and it should not be over-read as direct evidence about value-based commitment.

## How this should read against the 689a fork

689a tests whether a near-ties shortlist converts. If it does not, the autopsy routes to renormalization — and the open design question becomes not just "renormalize F" but "how do the modulatory channels actually get leverage once F is renormalized?" Reynolds & Heeger pre-answers the shape of that: the modulatory signal must enter at the normalization (numerator gain / pool weighting), and its effect will be regime-dependent. That is a concrete constraint on the rung-2 build — the modulatory channels should be re-plumbed to modulate F's normalization, not to add onto F's raw score, and the build must characterise leverage across regimes rather than tune it at one operating point.

## Confidence

**Mixed, confidence 0.56.** Source quality high — the canonical normalization model of attention, widely validated. Mapping fidelity moderate (0.55): it gives the strongest mechanistic statement of *where* a modulatory signal must enter to gain leverage, directly explaining the MECH-439 floor-lock of additive modulatory channels, but it does so for sensory attention rather than value commitment. Transfer risk moderate-high (0.45): the value/action transfer is canonical-computation-mediated, and the response-gain-vs-contrast-gain regime-contingency means leverage is not guaranteed. It stays *mixed* — supporting the where-to-modulate and rank-preserving framing while warning that modulatory leverage is regime-dependent and that the order-preserving model does not license the asymmetric argmin-removal lever.
