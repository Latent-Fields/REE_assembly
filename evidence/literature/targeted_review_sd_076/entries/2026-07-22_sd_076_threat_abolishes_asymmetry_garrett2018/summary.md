# Garrett et al. (2018) -- Updating Beliefs under Perceived Threat

## What the paper did

Two experiments asked whether the optimistic asymmetry in belief updating is a fixed trait of human learners or a context-sensitive policy. The first manipulated perceived threat in the laboratory while measuring belief updates, galvanic skin response and self-reported anxiety. The second took the same measures from firefighters on active duty, where perceived threat varies naturally and substantially across shifts.

## Key findings relevant to SD-076

In the low-threat baseline the familiar asymmetry appeared: good news was incorporated more than bad news. Under perceived threat it vanished. Participants became even-handed, and the size of the improvement in incorporating bad news tracked physiological arousal. The authors read this as resolving an evolutionary puzzle -- an organism that is optimistic when safe and accurate when in danger gets the well-being benefits of optimism without paying its costs when the costs are lethal.

## How this translates to REE

I have filed this as *mixed*, and the split is clean enough to state directly. The replication of the baseline asymmetry in two independent samples, one of them ecologically valid, is support for SD-076 existing at all. The disappearance under threat is evidence against SD-076 as currently implemented, because the claim specifies a fixed asymmetry with no modulating input.

For V3 as it stands this is not yet a conflict, and I do not want to overstate it. V3 has no threat signal, no arousal variable, and nothing that would modulate the E3 asymmetry even if SD-076 were written to accept a modulator. A fixed asymmetry is the correct implementation of a context-modulated policy in a substrate with no context signal to condition on. The discrepancy becomes live the moment REE acquires an arousal or threat-like variable, and it is worth recording now so that whoever builds that variable knows there is a documented coupling waiting for it.

There is a second, subtler point. SD-076's stated sign convention is that it pushes the running variance down while MECH-204's recalibration pulls it toward the cumulative zero-point reference, so on a well-calibrated agent the two approximately cancel and the experimental signal lives in the ablation arms. If the biological asymmetry is state-dependent, then the cancellation is state-dependent too, and the Phase 7 retest is measuring a quantity that biology would only exhibit in its low-threat regime. That is fine for the retest -- V3's environments are not threatening in any sense the paper would recognise -- but it does mean the retest cannot claim to have validated a universal mechanism.

## Limitations and confidence

Perceived threat has no V3 analogue, so the paper's headline finding is untestable against REE in the current substrate, and its mapping to a second-order precision estimate carries the same first-order/second-order gap that limits the Sharot 2011 entry. Confidence 0.68: strong design, genuinely converging evidence, but a modulator REE cannot yet express and a target quantity one level removed from the one SD-076 governs.

*Retrieved via PubMed. [DOI](https://doi.org/10.1523/JNEUROSCI.0716-18.2018)*
