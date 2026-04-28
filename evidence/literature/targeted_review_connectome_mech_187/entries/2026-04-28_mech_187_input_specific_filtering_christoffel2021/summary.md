# Christoffel, Walsh, Hoerbelt, Heifets, Llorach, Lopez, Ramakrishnan, Deisseroth & Malenka (2021) — Selective filtering of excitatory inputs to nucleus accumbens by dopamine and serotonin

According to PubMed ([DOI](https://doi.org/10.1073/pnas.2106648118); PMID 34103400; PMC8214692).

## What the paper did

In mouse brain slices, the authors examined how dopamine and serotonin modulate excitatory postsynaptic currents (EPSCs) in NAc medium spiny neurons, separately characterising the modulation per input stream — paraventricular thalamus (PVT), ventral hippocampus (vHip), basolateral amygdala (BLA), and medial prefrontal cortex (mPFC). They then used pharmacological release of endogenous DA (methamphetamine) and 5-HT (MDMA) to verify that the slice-level effects translate to endogenous neuromodulator release. Finally, optogenetic input-specific inhibition was used to verify that the input-stream filtering causally produces the behavioural effects of the corresponding drugs.

## Key findings

DA reduced EPSCs only from PVT inputs, leaving vHip, BLA, and mPFC alone. 5-HT reduced EPSCs from PVT, vHip, and BLA inputs (sparing mPFC). Methamphetamine recapitulated the DA pattern; MDMA recapitulated the 5-HT pattern. Optogenetic inhibition of PVT inputs enhanced cocaine-conditioned place preference, while inhibition of mPFC inputs reduced MDMA-induced sociability. The clean read is: DA and 5-HT each filter excitatory drive to NAc MSNs in input-specific ways, with overlapping but distinct sets of streams, and the joint pattern sets the effective excitatory drive that produces motivated behaviour.

## Mapping to MECH-187

MECH-187 asserts that serotonin modulates the gain on dopaminergic incentive salience at the NAc transduction point. Christoffel supplies the synapse-level mechanism for that claim. DA on its own filters only PVT; 5-HT filters PVT plus vHip and BLA. So 5-HT contributes a separable gain dimension — when 5-HT tone is high, additional input streams are suppressed, changing the effective excitatory drive in a way that DA alone cannot. That separability is what makes "5-HT modulates the gain on DA-mediated incentive salience" a non-trivial mechanism rather than redundant double-counting.

The translation to MECH-187 needs a careful reading of the action. Christoffel frames the mechanism as suppression (reducing EPSCs), not gain in the multiplicative sense MECH-187 sometimes implies. The bidirectional gain reading requires that the suppression be tunable rather than gated — i.e., that endogenous 5-HT tone scales the magnitude of suppression. The dose-dependent effects of MDMA in this paper are consistent with that, but the bidirectional gain claim is not directly tested. EXQ-252's bidirectional z_goal seeding gain finding (REE PASS, 2026-04-07) is the strongest direct test we have, and Christoffel provides the substrate-level account compatible with what EXQ-252 demonstrated functionally.

The other useful constraint is the input-specificity of mPFC sparing. mPFC inputs to NAc are spared by both DA and 5-HT — meaning the cortical-PFC drive to NAc is *not* gated by either neuromodulator, only the limbic/thalamic drives are. For REE this is a useful localisation: the gain modulation MECH-187 claims operates on the limbic input set specifically.

## Caveats

The framing is suppression, not multiplicative gain. Mouse slice + behaviour with pharmacological neurotransmitter release; the endogenous-tone dynamics during ongoing motivated behaviour are not directly measured. The behavioural assays are cocaine CPP and MDMA sociability, both drug-administered rather than naturalistic motivation tasks. SD-012's threshold-vs-graded distinction is not directly tested in this paper.

## Confidence reasoning

I land at 0.84. Source quality is very high (PNAS, Malenka + Deisseroth collaboration, multi-method). Mapping fidelity is good (the locus is exactly NAc as MECH-187 specifies; the input-specificity provides useful constraints). The reduction is the suppression-vs-gain framing question and the indirect coverage of bidirectional modulation. Transfer risk is the standard rodent-to-human caveat.
