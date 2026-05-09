# Sundell et al. 2004 — Field test of the risk allocation hypothesis in voles

According to PubMed: Sundell, Dudek, Klemme, Koivisto, Pusenius & Ylonen 2004, *Oecologia* 139(1):157–62. [DOI 10.1007/s00442-004-1490-x](https://doi.org/10.1007/s00442-004-1490-x) (PMID 14730443).

## What the paper does

A field test of the canonical predation-risk-allocation hypothesis (Lima & Bednekoff 1999 — sibling entry in this pull) using bank voles (*Clethrionomys glareolus*) as prey and least weasels (*Mustela nivalis nivalis*) as predator. Temporal pattern and intensity of predation risk were manipulated in large outdoor enclosures; foraging effort and patch use were measured by giving-up densities (the canonical Brown-style metric for animal patch valuation under risk).

## What the data show

Most predictions of the canonical theory did *not* replicate. Voles showed no significant variation in feeding effort due to changes in the level of risk, nor due to changes in the proportion of time spent under high risk. The only significant effect was on attack ratio — foraging effort was higher under low-attack-ratio than under high-attack-ratio treatments. Four out of five canonical predictions failed to replicate; one out of five succeeded.

The authors attribute the partial null result partly to *voles' inability to accurately assess risk-level changes* under the outdoor manipulations, plus the inherent difficulty of testing flexible-behaviour mammals under field conditions. Whether the failure is at the architecture level (voles lack rule-apprehension capacity adequate to the task) or at the perception level (voles have the architecture but cannot extract the risk-pattern variable from outdoor sensory input) is not arbitrated by the paper.

## Why this matters for R4 (Phase 2 acceptance threshold tolerance window)

This is the load-bearing entry in the pull for *tolerance-window calibration*. Three architectural implications for the Phase 2 falsifier:

1. **The acceptance threshold should be a tolerance window, not a sharp predicted ratio.** Real animals tested against a 5-prediction theoretical battery delivered only 1/5 replications — not because the theory is wrong but because empirical biology is noisy. The appropriate analog for ARC-062's Phase 2 falsifier is "reproduces *some* risk-pattern dependence with at least one significant effect", not "reproduces all five Lima-Bednekoff predictions". A narrow acceptance criterion would falsely reject biologically plausible behaviour.

2. **The single replicating prediction was attack-ratio dependence** (foraging higher when attacks are rare per encounter). The Phase 2 falsifier should include an attack-ratio variation as one of its primary metrics, not just hazard-density. SD-054's `hazard_food_attraction` parameter is the closest analog of attack ratio (probability of attack per food-area visit); varying this across arms gives the cleanest single-prediction test.

3. **The perception-failure reading is a cautionary note for SD-054's hazard signal magnitude.** If real voles cannot represent the risk-pattern variable accurately under outdoor conditions, ARC-062 weak reading on SD-054 may produce noisy / partial allocation responses if the substrate's risk signal is below the agent's representational threshold. The architecture-vs-perception ambiguity in Sundell's data maps directly to a similar ambiguity for ARC-062: the discriminator may have the architecture but lack adequate input signal.

## Why the mixed-direction tagging matters

This is a `mixed` entry, not `weakens`. The single replicating prediction supports the *spirit* of the risk-allocation theory; the four non-replicating predictions weaken the *strict* form. The cluster's MECH-309 and ARC-062 commitments are to the *spirit* (animals can do this kind of allocation when the architecture and perception both work), not to the strict five-prediction empirical signature. Sundell's data is therefore consistent with MECH-309's logical-necessity claim while warning against over-interpreting partial empirical replications as cluster-falsifying.

If ARC-062's Phase 2 falsifier produces invariant allocation across *all* manipulations (no signal at all), Sundell's evidence does not provide cover — even partial replication is a more biologically plausible signature than total non-response. A complete null is the clean falsifier signal; a partial replication is the biologically expected signal.

## Mapping caveat

Bank voles in outdoor enclosures with weasel predator is one specific system; assessment failure may be species-specific. The paper does not arbitrate whether the partial null is at the architecture level (voles lack rule-apprehension layer adequate to the task) or at the perception level (voles have the architecture but cannot extract the risk-pattern variable from outdoor sensory input). For ARC-062 design implications, both readings are useful — the perception-failure reading informs SD-054's hazard signal magnitude tuning, the architecture-failure reading is consistent with MECH-309 in another taxon. Vole-to-fish transfer should be done carefully; cognitive capacity for risk assessment differs substantially across taxa.

## Confidence reasoning

Source quality 0.78 — solid *Oecologia* field-test paper with quantitative giving-up density measurements. Source quality reduced from highest tier because outdoor field conditions add measurement noise (the paper itself acknowledges this). Mapping fidelity 0.72 — direct test of the canonical theory but in voles rather than fish. Transfer risk 0.30 — vole-to-fish transfer requires care; species differ substantially in cognitive capacity for risk assessment. Confidence 0.71 reflects: solid empirical entry with mixed-direction signal, load-bearing for tolerance-window calibration but specific-system-bound for numerical transfer.

## Failure signatures for the cluster

1. **Narrow-window false-negative**: Sundell warns that 1/5 replication is realistic. If the Phase 2 falsifier acceptance criterion is "all five Lima-Bednekoff predictions reproduce", ARM_1 ARC-062 may FAIL despite implementing the architecture correctly. The acceptance threshold should specify "at least N significant effects of expected sign" rather than "all expected effects".

2. **Total null is the clean signal**: if ARC-062 produces invariant allocation across hazard density AND attack ratio AND chronic-vs-pulsed manipulations, that is the unambiguous monomodal-collapse signature MECH-309 predicts for an architecture without a rule-apprehension layer. Sundell's evidence does not provide cover for total invariance — even partial replication is the biologically expected baseline.
