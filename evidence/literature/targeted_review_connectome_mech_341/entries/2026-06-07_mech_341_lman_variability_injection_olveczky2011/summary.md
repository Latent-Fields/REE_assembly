# LMAN injects controllable variability into a developing motor program (Ölveczky et al. 2011)

According to PubMed. Source: Ölveczky, Otchy, Goldberg, Aronov & Fee, *Journal of Neurophysiology* (2011), [DOI 10.1152/jn.00018.2011](https://doi.org/10.1152/jn.00018.2011) (PMC3129720).

## What the paper did

This study asks how the motor program underlying a complex learned behaviour evolves, and — crucially for MECH-341 — how a developing motor output is shaped by two distinct inputs: one carrying variability and one carrying precision. The authors recorded chronically from single neurons in RA (the robust nucleus of the arcopallium, a motor-cortex analog) in zebra finches across song learning, and then reversibly inactivated each of RA's two main inputs during singing: LMAN, the output of the basal-ganglia–forebrain loop, and HVC, the premotor nucleus.

## Key findings relevant to the claim

In young birds, RA neurons fired in highly variable patterns that became progressively more precise, sparse and bursty as the song matured. Pharmacological inactivation of LMAN during singing rendered the song-aligned RA firing *adultlike in its stereotypy* without dramatically changing the overall firing statistics — i.e. switching off the basal-ganglia input removed the exploratory variability and left a deterministic motor program. Inactivating HVC instead produced a *complete loss of stereotypy* of both song and the underlying program. So the two inputs are dissociable: LMAN supplies controllable variability, HVC supplies structure/precision, and the output's variability is set by their relative weight. As learning proceeded and the circuit matured, LMAN's relative contribution declined, letting HVC drive an increasingly stereotyped song.

## How this maps to REE (MECH-341)

MECH-341 posits that the scoring step must preserve trajectory-class diversity from the proposal layer, with a *diversity-circuit signal weight* that can be amplified to competitive parity with the dominant deterministic pathway. Ölveczky et al. provide a near-literal biological template: a diversity input and a precision input converging on a shared output stage, where (a) the diversity contribution is a tunable weight, (b) zeroing it collapses the output to a single deterministic pattern, and (c) the two functions are carried by structurally separate pathways rather than emerging from one combined ranking. This is the architectural shape MECH-341 wants the E3/CEM machinery to have. The developmental decline of LMAN's weight also bridges to MECH-333 (the plasticity-window claim) — early in learning the diversity channel dominates, and it is progressively suppressed as the precision channel crystallizes.

## Limitations and confidence

The same locus caveat applies as for Kojima et al.: the variability is injected at the motor-output convergence (RA), not at an explicit value-scoring step, and MECH-341 names the scoring stage specifically. The developmental-decline result is genuinely about a plasticity window and is used here only as corroboration of the tunable-weight point, not as primary MECH-341 evidence. Transfer from songbird single-unit electrophysiology to REE's CEM/E3 candidate scoring is substantial. Still, the dissociable two-input architecture — diversity vs precision, with a controllable balance — is exactly the feature MECH-341 cares about, and it is established here with reversible causal manipulations. I score this **supports at 0.68**: high source quality (0.82, chronic recording + reversible inactivation), moderate mapping fidelity (0.58, proposal-vs-scoring locus), moderate transfer risk (0.4).
