# Rolls (2021) — Attractor cortical neurodynamics, schizophrenia, and depression

*According to PubMed.* Rolls ET, *Translational Psychiatry* 11(1):215, 2021. [DOI](https://doi.org/10.1038/s41398-021-01333-7)

## What the paper did

Rolls reviews how the local recurrent-collateral connections between cortical neurons form attractor networks, and how the *stability parameters* of those networks — set by recurrent excitation (largely NMDA-mediated) and feedback inhibition (GABA) — map onto the symptom clusters of schizophrenia and depression. It is a conceptual/computational synthesis from one of the founders of the attractor-network approach to cortical computation.

## Key findings relevant to MECH-450

The value of this paper for MECH-450 is not in the selection mechanism (Wang 2002 and Morita 2016 cover that) but in the **failure modes** — and MECH-450's `psychiatric_failure_mode` field reads almost like a restatement of Rolls's stability analysis. Three poles are laid out:

1. **Reduced recurrent excitation / reduced firing** (e.g. NMDA receptor hypofunction, reduced spines) destabilizes the *high-firing attractor states* that normally implement short-term memory, attention and a held selection. The network cannot maintain a winner. Rolls links this to the negative and cognitive symptoms of schizophrenia. → This is MECH-450's **too-weak-settling pole**: too few or too weak inhibition rounds → failure to converge to a single winner = the indecision / blend-output / avolition analog.

2. **Reduced inhibition** lets the network make a *noise-induced jump into a high-firing attractor state even in the absence of adequate external input*. Rolls links this to the positive symptoms (hallucinations, delusions) of schizophrenia. → In REE terms this is a committed selection that the evidence does not warrant — a spurious winner — a third failure mode worth watching for in the settling step.

3. **An over-connected, over-stable attractor** — specifically the lateral-orbitofrontal-cortex *non-reward* system, which Rolls argues is over-connected and hypersensitive in depression — produces a state that *cannot be flipped by new input*. → This is MECH-450's **runaway-recurrent-gain pole**: a locked attractor that new evidence cannot dislodge = the perseveration / catatonic-fixity / obsessional-loop analog.

## How it maps to REE

MECH-450's whole rationale for replacing the one-shot argmin is that the argmin "has no settling dynamics to derange, so it cannot model either pole — it can only ever return the static F-winner." Rolls is the substantive backing for that sentence. A recurrent settling competition is a richer object precisely because it has stability parameters that can be set too low (indecision), too high (perseveration), or with too little inhibition (spurious commitment). That a single mechanism's *breakage* spans recognizable psychiatric syndromes is exactly the kind of brain-grounded, failure-mode-bearing property ARC-106 asks REE mechanisms to have, and it is the strongest reason to prefer the settling step over the argmin on more-than-engineering grounds.

## Limitations and caveats

The mapping is by *shared dynamical class*, not shared anatomy. Rolls's attractor networks are cortical — PFC short-term memory and OFC reward/non-reward valuation — whereas MECH-450 models the basal-ganglia committed-action *selection* step. The claim that the same stability poles appear in a discrete eligible-set competition with a fixed inhibition kernel is a reasonable extrapolation from the dynamics, but it is an extrapolation: only a direct REE ablation (sweep inhibition rounds / gain, look for non-convergence at one end and un-flippable lock-in at the other) can confirm that the V3 settling step actually exhibits these poles rather than degenerating gracefully. And the human-disorder mapping is itself a model, not a measurement.

## Confidence reasoning

Source quality good (authoritative review by a foundational theorist). Mapping fidelity high for the failure-mode dimension specifically — this is the closest literature anchor for the claim's psychiatric predictions. Net **0.71, supports**: it grounds MECH-450's two (really three) predicted failure poles in an established attractor-instability framework, held below 0.8 because it is conceptual and cortical rather than a measurement of the BG selection step.
