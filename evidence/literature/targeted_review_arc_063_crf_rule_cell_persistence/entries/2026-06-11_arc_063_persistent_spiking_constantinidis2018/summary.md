# Persistent Spiking Activity Underlies Working Memory (Constantinidis et al., 2018)

**Claim:** ARC-063 (CandidateRuleField rule-cell maintenance) — pole (a) of the persistence fork
**Direction:** mixed · **Confidence:** 0.62
**DOI:** [10.1523/JNEUROSCI.2486-17.2018](https://doi.org/10.1523/JNEUROSCI.2486-17.2018)
*According to PubMed.*

## What the paper argues

This is the pro-persistent half of the 2018 *Journal of Neuroscience* point–counterpoint on the neural basis of working memory, authored by the lineage that built the canonical account — Constantinidis, Funahashi, Lee, Murray, Qi, Min Wang, and Arnsten (the Goldman-Rakic/Arnsten prefrontal tradition). Their position is direct: persistent spiking generated in prefrontal cortex during the delay period of a working-memory task *is* the carrier of the remembered content, it covaries with behavioural performance, and accounts that lean exclusively on rhythmic (bursty) discharge or exclusively on short-term synaptic plasticity are, in their reading, inconsistent with the primate neurophysiology. For the REE fork, this is the strongest available defence of option (a): a selected representation is held by sustained, above-threshold firing across the gap, not by a silent synaptic trace.

## Why it matters to ARC-063 and the CRF fix

The V3-EXQ-666 autopsy decomposed the CandidateRuleField failure into a tension: the `e2_world_forward` context delivers genuine rule differentiation (10–16 distinct rules, max pairwise distance 1.71) but per-rule `crf_frac_active` collapses to 0.016, because a narrowly-tuned rule matches sparsely and its availability never re-accumulates above theta between matches. The fork the autopsy posed: is rule maintenance (a) persistent firing — in which case the CRF needs a *sustained-availability term* that holds availability high across context-absent ticks — or (b) activity-silent — in which case `crf_frac_active` is itself the wrong primitive. This paper is the evidence base for (a). It says: do not throw away the sustained component; brains really do hold a maintained, readable representation of the task-relevant item across the delay.

## The honest caveat — and why this is "mixed", not "supports"

The reason I score this *mixed* rather than a clean *supports* is that the regime this camp defends is not the regime where the CRF fails. Their evidence comes from densely-cued spatial and feature working memory, where the single remembered item is continuously task-relevant. The CRF's problem child is the opposite case — a highly selective rule that is relevant only on a small slice of contexts. Even Constantinidis and colleagues do not claim a single cell fires continuously; their robust signal is the *trial- and time-averaged* elevation of rate. Once you average, sparse bursts and sustained firing become hard to distinguish — which is exactly the methodological wedge the counterpoint paper (Lundqvist, Herman & Miller, [10.1523/JNEUROSCI.2485-17.2018](https://doi.org/10.1523/JNEUROSCI.2485-17.2018)) drives in. So the paper licenses a *maintenance term* that prevents availability from collapsing between matches; it does **not** license keeping `crf_frac_active` (an instantaneous, per-tick above-theta fraction) as the readiness readout for a sparsely-matched rule. The truthful synthesis is that this camp establishes the sustained component is real, while the activity-silent camp establishes that the instantaneous readout is misleading for selective, rarely-matched cells. The CRF fix must honour both: hold availability across gaps (their point) but score readiness on maintained-and-reactivatable availability rather than continuous activation (the other camp's point).

## Confidence reasoning

Source quality is very high (definitive authors, primate single-unit data). Mapping fidelity is moderate (0.55): the translation from delay-period spike rate to an availability EMA in an abstract rule field is loose, and the transfer from a densely-cued WM item to a sparsely-matched differentiated rule — animal→REE and dense→sparse — is the precise risk the autopsy flagged. Net 0.62: a credible, well-sourced anchor for the persistent pole that nonetheless does not, on its own, settle the fork in favour of keeping the existing readout.
