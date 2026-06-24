# Wang (2002) — Probabilistic decision making by slow reverberation in cortical circuits

*According to PubMed.* Wang XJ, *Neuron* 36(5):955-968, 2002. [DOI](https://doi.org/10.1016/s0896-6273(02)01092-9)

## What the paper did

Wang built a biophysically realistic spiking cortical network — pyramidal cells with slow NMDA-mediated recurrent excitation plus a pool of feedback inhibitory interneurons — and asked whether such a circuit could reproduce the decision-correlated single-unit activity recorded in alert primates performing random-dot motion discrimination. The network has two (or few) selective excitatory populations, each favouring one choice, that compete through shared feedback inhibition. He analysed both the full spiking model and a reduced mean-field version.

## Key findings relevant to MECH-450

The central result is mechanistic and directly germane to MECH-450's bet. Slow recurrent excitation, balanced against feedback inhibition, gives the network **attractor dynamics**: when two conflicting inputs arrive, the recurrent loop *amplifies the small difference between them* over hundreds of milliseconds until one population wins and is driven to a high-firing attractor while the other is suppressed. The choice is therefore not read off in a single feedforward comparison — it *emerges from a settling competition*. This reproduces the ramping decision activity, the psychometric function, and the reaction-time distribution of the animals.

This is precisely the dynamical primitive MECH-450 proposes to import into the V3 selector: replace the one-shot argmin/softmax over the `_modulatory_accum` field with a few rounds of mutual (surround) inhibition so that the committed action settles out of a competition rather than being returned by a single global max. Wang's network is, in effect, the canonical demonstration that "a few rounds of recurrent inhibition produce a categorical winner" is a real, biophysically grounded computation and not just a convenient engineering trick.

## How it maps to REE

MECH-450 is explicitly framed as "the V3-bounded version of the BG's recurrent settling dynamics," with the full learned thalamo-cortico-basal loop deferred to V4 (the ARC-108 coupling). Wang's cortical reverberation model is the cleanest existing instance of the bounded version: fixed (unlearned) recurrent weights, a small number of competing populations, and settling-to-attractor selection. The claim's prediction that surround inhibition turns an *additive blend* into a *competitive winner-take-most* is the discrete-action analogue of Wang's "amplify the difference between conflicting inputs."

## Limitations and caveats

Two boundaries keep this from being decisive support. First, Wang's network arbitrates between sensory-evidence-driven populations; it does **not** model an F-dominated score field, and so it does not test MECH-450's distinctive prediction — that a sufficiently strong *non-dominant* modulatory channel can **flip** the selected attractor away from the feedforward maximum (the conversion-ceiling escape, assembly-map C1). That the dynamics *could* support such a flip is plausible but unproven here. Second, the amplification leans on *slow* NMDA reverberation accumulated over a long integration window; a V3 selector with a fixed inhibition kernel and only a handful of settling iterations may lack the effective gain to override a large feedforward score gap. That is itself a useful design constraint: it predicts the too-weak-settling failure mode (failure to converge to a single winner = the blend-output / indecision pole MECH-450 names).

## Confidence reasoning

Source quality is very high (foundational, repeatedly validated). Mapping fidelity is high for the settling-vs-feedforward contrast but discounted because neither the attractor-flip nor the discrete within-eligible framing is directly instantiated. Net confidence **0.82, supports** — strong endorsement of the *mechanism's existence and plausibility*, with the claim's specific flip prediction still owed to a direct REE experiment.
