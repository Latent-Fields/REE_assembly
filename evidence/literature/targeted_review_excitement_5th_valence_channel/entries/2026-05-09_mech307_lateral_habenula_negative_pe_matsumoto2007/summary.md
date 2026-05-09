# Matsumoto and Hikosaka 2007 — Lateral habenula as the source of negative reward signals in dopamine neurons

**Source:** Matsumoto M, Hikosaka O. *Nature* 447(7148):1111-5 (2007). [DOI: 10.1038/nature05860](https://doi.org/10.1038/nature05860). PMID: 17522629.

## What the paper did

By 2007, the dopamine reward-prediction-error account (Schultz, Dayan, Montague) had been the dominant computational reading of midbrain DA activity for a decade. The core puzzle it left unresolved: where does the *negative* PE signal come from? DA neurons clearly encode negative PE — they pause on omitted-reward trials — but the source of the inhibition was not known. Several candidate inputs had been proposed but none anatomically clean.

Matsumoto and Hikosaka recorded single units from the lateral habenula (LHb) and from midbrain DA neurons in two rhesus monkeys performing a memory-guided saccade task with positionally biased rewards. The task gave them three things: cue-evoked responses (predict reward vs predict no reward), outcome-evoked responses (got reward vs got no reward), and a reversal manipulation (reward position swapped across blocks) that tested whether the responses tracked the actual reward contingency or just the cue identity.

The result was unambiguous. LHb neurons were *excited* by no-reward-predicting cues and *inhibited* by reward-predicting cues — the exact mirror of DA neurons, which were excited by reward cues and inhibited by no-reward cues. On reversal, both populations flipped their preferences in lockstep, ruling out a sensory explanation. The crucial timing finding: in unrewarded trials, the LHb excitation began *before* the DA inhibition. And weak electrical stimulation of LHb directly inhibited DA neurons. Anatomically, the LHb projects via the rostromedial tegmental nucleus (RMTg), a small GABAergic structure, to the midbrain DA neurons.

The conclusion: LHb is the upstream source of the negative-PE signal in the DA system. The brain implements signed reward-prediction-error not as a single bipolar channel but as two anatomically distinct populations with mirror-image response profiles, mutually inhibitory at the second stage.

## Key findings relevant to MECH-307 Gap 1

This is the single strongest piece of biological evidence for MECH-307 Gap 1. Currently the REE substrate writes VALENCE_SURPRISE as `max(0.0, pe_mag - pe_ema)` at agent.py:3075-3077 — the sign is discarded at the write site. Positive PE (a good thing happened unexpectedly, the dopamine RPE that underlies excitement) and negative PE (a bad thing happened unexpectedly, the LHb signature that underlies dread) get collapsed to a single non-negative magnitude.

Matsumoto and Hikosaka's evidence is that biology does not do this collapse. The brain has *two* physical populations of neurons, with response profiles that are literal mirror images of each other, deliberately separated so that downstream consumers can read signed surprise without ambiguity. The architectural commitment in MECH-307 — store signed PE, or split into VALENCE_POSITIVE_SURPRISE and VALENCE_NEGATIVE_SURPRISE — is the biologically faithful reading. The current REE implementation is the bug.

The asymmetry matters. LHb does not symmetrically respond to positive PE; it is mostly silent on positive trials (the inhibition is GABAergic and one-way). This favours the split-into-two-channels variant of Gap 1 over the single-signed-scalar variant: two non-negative channels naturally preserve the asymmetric response geometry. V3-EXQ-540's ARM_1_signed_pe currently tests the single-scalar variant; if Gap 1 needs to be promoted past the proof-of-concept stage, the split-channel variant should be wired in as the alternative arm.

## How the findings translate to REE

The translation is mechanistically direct. REE's E1 prediction error is the analog of the cue-evoked response in Matsumoto and Hikosaka's task; the residue field VALENCE_SURPRISE write is the analog of the LHb/DA population activity that downstream consumers read. The fix is small and bounded: instead of `max(0.0, pe - ema)`, write `pe - ema` and let consumers read sign or magnitude as needed; or split the residue field's surprise channel into two non-negative slots and write to whichever side the signed PE falls on.

The architectural cost is trivial (~5 lines of code). The architectural payoff is large: every downstream consumer of VALENCE_SURPRISE (MECH-205 sleep-replay-priority, MECH-292 ghost-priority, MECH-279 PAG freeze gate, the new MECH-307 conjunction-aware bridge) suddenly has access to information it currently cannot read. Excitement (positive surprise + wanting + liking + arousal) and dread (negative surprise + harm + arousal) become symmetrically detectable at predicted-imminent locations. The Adcock 2006 prediction (anticipation-marked locations get >=1.5x replay priority) can be tested with the right sign, not just the right magnitude.

## Limitations and caveats

The work is in macaques, on a saccade task, with juice reward. Both findings have been replicated in rodents and across paradigms (Hong and Hikosaka 2008 ventral pallidum; Bromberg-Martin et al. 2010 in the existing review) so the species-transfer is well-established at this point. The conceptual transfer to REE is direct because signed PE is a domain-general computation; what biology demonstrates is that the *architectural* solution (two anatomical channels) is preferred over the *engineering* solution (one signed scalar).

A subtle caveat: Matsumoto and Hikosaka work shows the LHb-DA architecture for *outcome-time* reward signals (got-reward vs not-got-reward). Cue-time predictive responses are also bipolar in their data, but the strongest single-trial dissociation is at outcome time. MECH-307's anticipatory signed-PE write happens at cue/prediction time, so the strongest evidence is for the principle (signed PE is anatomically separated) rather than for the specific timing locus (cue-time vs outcome-time) that REE's residue write needs.

## Confidence reasoning

I assign confidence 0.88 — among the highest confidence ratings I can justify for an architectural claim of this kind. Source quality is at the ceiling (Nature, foundational, definitive). Mapping fidelity to MECH-307 Gap 1 is direct: the biological architecture (two channels, mirror responses, asymmetric inhibition) maps onto the proposed REE architecture (signed PE or split surprise channels) without significant translation loss. Transfer risk is low because the signed-PE principle is general across vertebrate reward systems and the species-transfer is established.

This is the load-bearing entry for Gap 1. Without it, the case for the architectural commitment (signed VALENCE_SURPRISE) rests on engineering arguments alone; with it, the case rests on biological precedent. The architectural choice between single-signed-scalar (V3-EXQ-540 ARM_1) and split-channels remains open and should be resolved by behavioural performance after the first implementation lands.
