# Scholl, Kolling, Nelissen, Browning, Rushworth & Harmer 2017 — Beyond negative valence: 2-week SSRI enhances reward and effort learning signals

**Source:** *PLoS Biology* 15(2):e2000756, [10.1371/journal.pbio.2000756](https://doi.org/10.1371/journal.pbio.2000756). Via PubMed (PMID 28207733).

## What the paper does

Scholl and colleagues run a randomised controlled trial in which healthy volunteers receive either citalopram (SSRI) or placebo for two weeks, then perform a concurrent reward-and-effort learning task in the scanner. The task is designed so that on each trial the participant receives both a monetary outcome (appetitive) and an effort outcome (aversive), and the expectation for each needs to be updated independently. The headline finding: 2 weeks of SSRI enhances learning signals for *both* reward and effort — the fMRI signal tracking prediction errors is larger in a widespread network (vmPFC, ACC, others), and behavioural reward learning is more robust. The effect is valence-independent, which the authors argue against the traditional "SSRIs blunt negative emotion" story and in favour of a broader gain-control interpretation: serotonin modulates the sensitivity of the cost-benefit learning circuit to new information, regardless of valence.

## Key findings relevant to the claim

- **SSRI enhances learning signals, not just valence signals.** Both reward PE and effort PE are larger under citalopram in ACC and vmPFC.
- **The effect is valence-independent.** Appetitive and aversive learning signals are co-enhanced; this is inconsistent with a pure negative-valence-blunting account.
- **Two weeks needed.** Acute SSRI does not show this effect; chronic administration does. The enhancement is a plasticity-related phenomenon, not an immediate pharmacological state.
- **The enhanced network is the cost-benefit circuit.** The regions where learning signals are enhanced overlap heavily with the Rushworth-lab effort-value network (ACC, vmPFC).

## How this maps onto REE (the translation)

Relevant specifically to MECH-260 (dACC bias suppression against monostrategy). Monostrategy in ree-v3 manifests as a degeneracy: the agent stops updating cost-benefit expectancies for alternative modes because no alternative mode is ever considered seriously, so no prediction errors arise for those modes, so no learning happens. Scholl 2017 suggests the biological solution is neuromodulatory — serotonergic tone acts as a gain-control parameter on effort-learning signals, and in healthy brains this gain presumably varies with context (mood, exploration pressure, stress) to prevent learning-rate collapse.

For ree-v3, the architectural implication is: SD-032b should not have a fixed effort-learning rate. It should have one that is modulated by a system-state parameter — conceptually a "neuromodulatory" gain — and that parameter should vary in a way that promotes occasional reconsideration of alternative modes even when the current mode is being exploited. One concrete implementation: tie the gain to an analogue of SD-012 homeostatic drive — when drive is low (organism is safe, rested, satiated), exploration-like gain is high and alternative modes receive larger learning updates; when drive is high (urgency, pain), the gain drops and the agent commits to exploitation. This would be a biologically inspired antidote to monostrategy lock-in.

This ties back to SD-032b's minimum-viable implementation: the effort-learning term cannot be hard-coded. It must be parametrically exposed to a neuromodulatory gain that the rest of the substrate (SD-012, SD-032a) can modulate. Implementing this as "effort_cost = learned_cost * sd012_gain_multiplier" is a plausible minimum-viable substrate; validating it requires showing that varying the gain produces the expected dissociation between monostrategy and exploration.

## Limitations and caveats

SSRI is a coarse pharmacological manipulation — it affects many brain regions, many receptor types, and many downstream plasticity processes. The paper shows a correlation between citalopram and enhanced learning signals, not a mechanism for how serotonin does this specifically at the dACC level. The jump from "SSRI enhances dACC learning" to "ree-v3 should have a neuromodulatory gain on SD-032b" is an architectural inference that is several steps removed from the data.

The 2-week requirement is also telling: the effect is a plasticity phenomenon, not an acute pharmacological one. Whether this maps onto a runtime-tunable gain parameter in a simulation agent (which does not have the slow-timescale protein-synthesis machinery that chronic SSRI presumably engages) is an open question. A more faithful implementation might require modelling the gain as slow-varying, not as an instantaneous parameter.

The sample is healthy volunteers; whether depressed participants (for whom the learning-enhancement story would most matter therapeutically) show the same pattern is not addressed. The Harmer lab has follow-up work on this that we have not pulled.

## Confidence reasoning

0.74. Solid RCT with fMRI, published in PLoS Biology, reasonable sample size. Source quality is good but the translation from pharmacological fMRI to an architectural principle for SD-032b is inferential. Mapping fidelity is moderate because the specific ree-v3 implementation (neuromodulatory gain on effort-learning rate) is inspired by but not directly equivalent to the clinical finding. Transfer risk is elevated because neuromodulatory state in a biological brain does not map trivially onto a simulation agent's parameters. The paper is most valuable for establishing that monostrategy lock-in has a specifiable biological unwedging mechanism — it gives MECH-260 a concrete target substrate to attack.
