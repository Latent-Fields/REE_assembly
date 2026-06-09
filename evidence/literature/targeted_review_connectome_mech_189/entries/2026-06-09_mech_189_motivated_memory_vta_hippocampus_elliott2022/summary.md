# Elliott et al. 2022 — Midbrain-hippocampus connectivity predicts motivated memory encoding

According to PubMed. Source: Elliott BL, D'Ardenne K, Murty VP, Brewer GA, McClure SM. *Journal of Neuroscience* 42(50):9426-9434, 2022. [DOI](https://doi.org/10.1523/JNEUROSCI.0945-22.2022)

## What the paper did

Participants encoded words randomly assigned to reward (+$1), control ($0), or punishment (-$1) conditions, then were tested on item and source memory. Source memory was *better for both reward and punishment* words than for controls — value, not valence. The novel contribution is anatomical: using diffusion-weighted MRI and probabilistic tractography, the authors quantified individual differences in SN/VTA-hippocampus and SN/VTA-striatum white-matter pathways. Tract density of the SN/VTA-*hippocampus* pathway was positively correlated with reward- and punishment-modulated memory performance; the SN/VTA-*striatum* pathway showed no such association. They explicitly frame the field's open question as a competition between "SN/VTA-NAc reward prediction errors" and "SN/VTA-hippocampus signals" as the driver of motivated memory encoding.

## Why it matters for MECH-189

Of the five entries, this is the one whose *target* lines up best with MECH-189. The claim is not about writing a neutral episodic trace; it is about writing a *value/goal anchor*. So the relevant biology is the *motivated-memory* / value-modulated encoding pathway, and this study localises it to a dopaminergic SN/VTA-hippocampus circuit and ties its strength to value-modulated memory at the individual-difference level.

Two findings bear directly on the DEV-NEED-024 verdict. First, encoding was enhanced symmetrically by reward and punishment — *absolute* salience, not signed valence. That supports MECH-189's salience gate (a) being a magnitude gate over benefit (and, by parity, harm) rather than a signed-valence gate. Second, and more pointedly, the authors name the exact fork that DEV-NEED-024 has to settle: is the write driven by a *reward-prediction-error* signal or by a *hippocampal-novelty* signal? They show value matters and the value pathway is dopaminergic, which argues for an *external, value/PE-linked* complexity signal rather than a stimulus-novelty term computed in isolation from value. It also undercuts REE's clean factorisation of gate (a) salience and gate (b) complexity: in this circuit, motivational value itself modulates the hippocampal encoding signal, so the two gates share a dopaminergic substrate.

## Limitations and caveats

Structural connectivity is a *between-subject* correlate — it tells us that people with denser SN/VTA-hippocampus pathways show more value-modulated memory, not that a within-trial PE signal causally gates a given write. The task is source memory for incentivised words, not a cross-episode super-ordinal goal store. And the paper presents the reward-PE-vs-hippocampal-novelty competition as *unresolved*: it licenses "value/PE matters for the write" more than it adjudicates PE cleanly over novelty. So I read it as supporting the *external value-PE* direction without closing the question by itself.

## Confidence reasoning

Confidence 0.74, direction `supports`. Strong human data with an unusually good target match (value/goal memory), modest transfer risk. Mapping fidelity is capped because structural correlates are indirect for a within-trial write signal. Lit confidence only; not blended into experimental confidence.
