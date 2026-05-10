# Beierholm, Guitart-Masip, Economides, Chowdhury, Duzel, Dolan & Dayan 2013 -- L-DOPA strengthens average-reward-vigor coupling

**Citation:** Beierholm U, Guitart-Masip M, Economides M, Chowdhury R, Duzel E, Dolan R, Dayan P. Dopamine modulates reward-related vigor. *Neuropsychopharmacology*. 2013;38(8):1495-1503. PMID: 23419875. DOI: 10.1038/npp.2013.48.

## What the paper does

This is the strongest available human pharmacological test of Niv 2007's tonic-DA-vigor theoretical account. Ninety healthy subjects participated in a double-blind three-arm design: placebo, L-DOPA (raises DA availability), and citalopram (selective serotonin manipulation, control for non-specific effects). All subjects performed multiple trials of an odd-ball discrimination task with experimentally varied reward across blocks. The empirical question: does the predicted relationship between average reward rate and response vigor (faster RT at higher cumulative reward history) become stronger under L-DOPA than under placebo, and is the effect specific to DA rather than serotonin?

The reported result: yes. The beta coefficient for average-reward-rate predicting RT was significantly larger under L-DOPA than under placebo, while citalopram did not produce the same enhancement. The authors interpret this as causal evidence that DA modulates the avg-reward-rate-vigor coupling Niv 2007 derived theoretically.

## Why this matters for ARC-066

The R1 verdict (substrate attribution) needs human empirical evidence to firm up the DA-vigor substrate attribution. Salamone & Correa 2012 give the rodent / primate substrate identity; Niv 2007 gives the formalism. Beierholm 2013 provides the human pharmacological causal test. Together they form the load-bearing R1 cluster for the synthesis verdict that ARC-066's substrate is mesolimbic DA-vigor (with Aston-Jones / Kane data on the LC-NE side already showing LC-NE tonic mode is noise-mediated, not direction-mediated, and therefore covered by MECH-313 not ARC-066).

For R3 implementation shape, Beierholm 2013 provides indirect evidence for the additive-bias formalism: the empirical effect manifests as a scaling of the avg-reward-rate-RT relationship under L-DOPA, which is consistent with the avg-reward-rate scalar entering additively on the decision-dynamics side. It does not rule out a multiplicative gain alternative (which would also produce a stronger correlation), so the additive-vs-multiplicative R3 sub-question remains open empirically. The synthesis recommends additive as primary, multiplicative as falsifiable secondary.

For R4 capacity scalar composition, Beierholm 2013 gives clear evidence that the empirically tested scalar is the across-trial REWARD HISTORY (an environmental signal), not internal physiological capacity. This corroborates the R4 verdict that ARC-066's primary scalar should be a slow EWMA over realised E3-score-receipt rather than a composite of internal-capacity proxies. The user-registered slot text says "high energy AND low recent prediction error AND low drive" -- the literature attribution is to "long-run avg reward rate". The two are correlated in normal conditions but mathematically distinct.

## Caveats

The biggest caveat is the tonic-vs-phasic DA dissociation Niv 2007 specifically claims. L-DOPA elevates both tonic and phasic DA simultaneously; the Beierholm result is consistent with Niv's account but does not selectively support it. A pharmacologically selective tonic-DA tool (e.g. low-dose D2 antagonism / autoreceptor manipulation) would be needed to cleanly isolate tonic from phasic. Future work is unlikely to ever produce a clean dissociation in humans with current tools.

A second caveat: the behavioural readout is RT-on-discrimination, which sits on the vigor-of-execution axis (how fast to respond given a response is happening) rather than the act-vs-not-act selection axis ARC-066 primarily names. As with Niv 2007, the mathematical transfer is clean -- the same scalar that biases RT also biases the score gap between action and no-op trajectories -- but the empirical evidence in Beierholm 2013 directly tests the timing readout, not the selection readout. The synthesis treats this as a recurring scope mismatch across the DA-vigor literature: vigor-of-execution is what is measured; act-vs-not-act selection is what ARC-066 commits to. The slot's functional_restatement explicitly excludes vigor-of-execution from the current scope, so the entries are evidence for the substrate and form, not for the specific behavioural readout REE will use.

## Confidence reasoning

Source quality is high (double-blind RCT, N=90, top author group, top venue). Mapping fidelity is moderate-high -- direct test of the avg-reward-rate-vigor coupling but limited isolation of tonic vs phasic DA. Transfer risk is moderate -- human empirical anchor reduces species-transfer concerns, but the readout-scope concern persists. Aggregate 0.79.

According to PubMed, this paper appears under PMID 23419875.
